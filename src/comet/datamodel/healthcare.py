from __future__ import annotations 
from datetime import (
    datetime,
    date,
    time
)
from decimal import Decimal 
from enum import Enum 
import re
import sys
from typing import (
    Any,
    ClassVar,
    List,
    Literal,
    Dict,
    Optional,
    Union,
    Generic,
    Iterable,
    TypeVar,
    get_args
)
if sys.version_info.minor > 8:
    from typing import Annotated 
else:
    from typing_extensions import Annotated 

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator,
    GetCoreSchemaHandler
)
from pydantic_core import (
    CoreSchema,
    core_schema
)
metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root



_T = TypeVar("_T")

_RecursiveListType = Iterable[Union[_T, Iterable["_RecursiveListType"]]]

class AnyShapeArrayType(Generic[_T]):
    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler: "GetCoreSchemaHandler") -> "CoreSchema":
        # double-nested parameterized types here
        # source_type: List[Union[T,List[...]]]
        item_type = Any if get_args(get_args(source_type)[0])[0] is _T else get_args(get_args(source_type)[0])[0]

        item_schema = handler.generate_schema(item_type)
        if item_schema.get("type", "any") != "any":
            item_schema["strict"] = True

        if item_type is Any:
            # Before python 3.11, `Any` type was a special object without a __name__
            item_name = "Any"
        else:
            item_name = item_type.__name__

        array_ref = f"any-shape-array-{item_name}"

        schema = core_schema.definitions_schema(
            core_schema.list_schema(core_schema.definition_reference_schema(array_ref)),
            [
                core_schema.union_schema(
                    [
                        core_schema.list_schema(core_schema.definition_reference_schema(array_ref)),
                        item_schema,
                    ],
                    ref=array_ref,
                )
            ],
        )

        return schema


AnyShapeArray = Annotated[_RecursiveListType, AnyShapeArrayType]
linkml_meta = LinkMLMeta({'default_prefix': 'linkml_common',
     'default_range': 'string',
     'description': 'Common Data Model Elements',
     'id': 'https://w3id.org/linkml-common/healthcare',
     'imports': ['linkml:types', 'core', 'bio'],
     'license': 'MIT',
     'name': 'linkml-common-healthcare',
     'prefixes': {'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/'},
                  'fhir': {'prefix_prefix': 'fhir',
                           'prefix_reference': 'http://hl7.org/fhir/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'linkml_common': {'prefix_prefix': 'linkml_common',
                                    'prefix_reference': 'https://w3id.org/linkml-common/'},
                  'omopschema': {'prefix_prefix': 'omopschema',
                                 'prefix_reference': 'http://example.org/omop/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://linkml.github.io/linkml-common'],
     'source_file': 'src/comet/schema//healthcare.yaml',
     'title': 'linkml-common-healthcare'} )

class RelativeTimeEnum(str, Enum):
    BEFORE = "BEFORE"
    AFTER = "AFTER"
    AT_SAME_TIME_AS = "AT_SAME_TIME_AS"


class CaseOrControlEnum(str, Enum):
    case_role_in_case_control_study = "CASE"
    control_role_in_case_control_study = "CONTROL"


class StudyDesignEnum(str):
    pass


class InvestigativeProtocolEnum(str):
    pass


class SampleProcessingEnum(str):
    pass


class PresenceEnum(str, Enum):
    # The entity is present
    PRESENT = "PRESENT"
    # The entity is absent
    ABSENT = "ABSENT"
    # The entity is below the detection limit
    BELOW_DETECTION_LIMIT = "BELOW_DETECTION_LIMIT"
    # The entity is above the detection limit
    ABOVE_DETECTION_LIMIT = "ABOVE_DETECTION_LIMIT"


class LandformEnum(str):
    pass


class CodeSystemEnum(str, Enum):
    """
    Used to specify why the normally expected content of the data element is missing.
    """
    # The value is expected to exist but is not known.
    Unknown = "unknown"
    # The source was asked but does not know the value.
    Asked_But_Unknown = "asked-unknown"
    # There is reason to expect (from the workflow) that the value may become known.
    Temporarily_Unknown = "temp-unknown"
    # The workflow didn't lead to this value being known.
    Not_Asked = "not-asked"
    # The source was asked but declined to answer.
    Asked_But_Declined = "asked-declined"
    # The information is not available due to security, privacy or related reasons.
    Masked = "masked"
    # There is no proper value for this element (e.g. last menstrual period for a male).
    Not_Applicable = "not-applicable"
    # The source system wasn't capable of supporting this element.
    Unsupported = "unsupported"
    # The content of the data is represented in the resource narrative.
    As_Text = "as-text"
    # Some system or workflow process error means that the information is not available.
    Error = "error"
    # The numeric value is undefined or unrepresentable due to a floating point processing error.
    Not_a_Number_LEFT_PARENTHESISNaNRIGHT_PARENTHESIS = "not-a-number"
    # The numeric value is excessively low and unrepresentable due to a floating point processing        error.
    Negative_Infinity_LEFT_PARENTHESISNINFRIGHT_PARENTHESIS = "negative-infinity"
    # The numeric value is excessively high and unrepresentable due to a floating point processing        error.
    Positive_Infinity_LEFT_PARENTHESISPINFRIGHT_PARENTHESIS = "positive-infinity"
    # The value is not available because the observation procedure (test, etc.) was not performed.
    Not_Performed = "not-performed"
    # The value is not permitted in this context (e.g. due to profiles, or the base data types).
    Not_Permitted = "not-permitted"


class HealthcareEncounterClassification(str, Enum):
    # Person visiting hospital, at a Care Site, in bed, for duration of more than one day, with physicians and other Providers permanently available to deliver service around the clock
    Inpatient_Visit = "Inpatient Visit"
    # Person visiting dedicated healthcare institution for treating emergencies, at a Care Site, within one day, with physicians and Providers permanently available to deliver service around the clock
    Emergency_Room_Visit = "Emergency Room Visit"
    # Person visiting ER followed by a subsequent Inpatient Visit, where Emergency department is part of hospital, and transition from the ER to other hospital departments is undefined
    Emergency_Room_and_Inpatient_Visit = "Emergency Room and Inpatient Visit"
    # Person visiting dedicated institution for reasons of poor health, at a Care Site, long-term or permanently, with no physician but possibly other Providers permanently available to deliver service around the clock
    Non_hospital_institution_Visit = "Non-hospital institution Visit"
    # Person visiting dedicated ambulatory healthcare institution, at a Care Site, within one day, without bed, with physicians or medical Providers delivering service during Visit
    Outpatient_Visit = "Outpatient Visit"
    # Provider visiting Person, without a Care Site, within one day, delivering service
    Home_Visit = "Home Visit"
    # Patient engages with Provider through communication media
    Telehealth_Visit = "Telehealth Visit"
    # Person visiting pharmacy for dispensing of Drug, at a Care Site, within one day
    Pharmacy_Visit = "Pharmacy Visit"
    # Patient visiting dedicated institution, at a Care Site, within one day, for the purpose of a Measurement.
    Laboratory_Visit = "Laboratory Visit"
    # Person using transportation service for the purpose of initiating one of the other Visits, without a Care Site, within one day, potentially with Providers accompanying the Visit and delivering service
    Ambulance_Visit = "Ambulance Visit"
    # Person interacting with healthcare system, without a Care Site, within a day, with no Providers involved, for administrative purposes
    Case_Management_Visit = "Case Management Visit"



class Thing(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Thing', 'from_schema': 'https://w3id.org/comet/core'})

    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["Thing"] = Field("Thing", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class Intangible(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['schema:Intangible'],
         'from_schema': 'https://w3id.org/comet/core'})

    pass


class DomainEntity(Thing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/comet/core'})

    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["DomainEntity"] = Field("DomainEntity", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class InvestigativeEntity(Thing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/comet/core'})

    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["InvestigativeEntity"] = Field("InvestigativeEntity", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class Observable(DomainEntity):
    """
    A concrete or abstract entity that has been observed or measured. Examples include a person, a region of the earth, a cell type, a tree, a mountain.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['oboe-core:Entity'],
         'from_schema': 'https://w3id.org/comet/core'})

    properties: Optional[List[AttributeValue]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'properties', 'domain_of': ['Observable', 'Event']} })
    case_or_control: Optional[CaseOrControlEnum] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'case_or_control', 'domain_of': ['Observable']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["Observable"] = Field("Observable", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class Observation(InvestigativeEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['schema:PropertyValue', 'oboe-core:Measurement'],
         'from_schema': 'https://w3id.org/comet/core'})

    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    is_about: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'is_about',
         'domain_of': ['Observation'],
         'exact_mappings': ['oboe-core:ofEntity']} })
    result: Optional[AttributeValue] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'result',
         'domain_of': ['Observation'],
         'exact_mappings': ['om:result']} })
    part_of: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'part_of', 'domain_of': ['Observation']} })
    performer: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'performer',
         'domain_of': ['Observation'],
         'exact_mappings': ['prov:wasAssociatedWith', 'fhir:performer']} })
    method: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'method', 'domain_of': ['Observation']} })
    device_used: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'device_used', 'domain_of': ['Observation']} })
    procedure_used: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'procedure_used', 'domain_of': ['Observation']} })
    procedure_configuration: Optional[ProcedureConfiguration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'procedure_configuration', 'domain_of': ['Observation']} })
    sample_used: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'sample_used', 'domain_of': ['Observation']} })
    data_used: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'data_used', 'domain_of': ['Observation']} })
    derived_from: Optional[List[str]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'derived_from', 'domain_of': ['Observation']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["Observation"] = Field("Observation", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class StructuredValueComponent(Intangible):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/comet/core'})

    pass


class AttributeValue(StructuredValueComponent):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['schema:PropertyValue', 'schema:Quantity', 'fhir:Quantity'],
         'exact_mappings': ['schema:Quantity'],
         'from_schema': 'https://w3id.org/comet/core'})

    attribute: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'attribute',
         'domain_of': ['AttributeValue'],
         'exact_mappings': ['oboe-core:ofCharacteristic', 'om:observedProperty']} })
    target: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'target', 'domain_of': ['AttributeValue']} })
    numeric_value: Optional[float] = Field(None, description="""The numeric value of the observation""", json_schema_extra = { "linkml_meta": {'alias': 'numeric_value', 'domain_of': ['AttributeValue']} })
    presence_value: Optional[PresenceEnum] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'presence_value', 'domain_of': ['AttributeValue']} })
    value_range: Optional[ValueRange] = Field(None, description="""The range of the value""", json_schema_extra = { "linkml_meta": {'alias': 'value_range', 'domain_of': ['AttributeValue']} })
    value_series: Optional[ValueSeries] = Field(None, description="""A series of values""", json_schema_extra = { "linkml_meta": {'alias': 'value_series', 'domain_of': ['AttributeValue']} })
    ratio: Optional[Ratio] = Field(None, description="""The ratio of the value""", json_schema_extra = { "linkml_meta": {'alias': 'ratio', 'domain_of': ['AttributeValue']} })
    qualitative_value: Optional[str] = Field(None, description="""A qualitative value""", json_schema_extra = { "linkml_meta": {'alias': 'qualitative_value', 'domain_of': ['AttributeValue']} })
    unit: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'unit',
         'domain_of': ['AttributeValue'],
         'exact_mappings': ['schema:unitCode', 'qudt:unit']} })
    relative_values: Optional[List[RelativeValue]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'relative_values', 'domain_of': ['AttributeValue']} })
    value_absence_reason: Optional[str] = Field(None, description="""The reason for the absence of a value""", json_schema_extra = { "linkml_meta": {'alias': 'value_absence_reason',
         'domain_of': ['AttributeValue'],
         'exact_mappings': ['fhir:dataAbsentReason']} })


class Ratio(StructuredValueComponent):
    """
    A tuple of two quantities
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fhir:Ratio', 'from_schema': 'https://w3id.org/comet/core'})

    numerator: Optional[AttributeValue] = Field(None, description="""The numerator of the ratio""", json_schema_extra = { "linkml_meta": {'alias': 'numerator', 'domain_of': ['Ratio']} })
    denominator: Optional[AttributeValue] = Field(None, description="""The denominator of the ratio""", json_schema_extra = { "linkml_meta": {'alias': 'denominator', 'domain_of': ['Ratio']} })


class ValueRange(StructuredValueComponent):
    """
    A quantity range is a property that can be measured or counted
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fhir:Range', 'from_schema': 'https://w3id.org/comet/core'})

    lower_bound: Optional[float] = Field(None, description="""The lower bound of the range""", json_schema_extra = { "linkml_meta": {'alias': 'lower_bound', 'domain_of': ['ValueRange']} })
    upper_bound: Optional[float] = Field(None, description="""The upper bound of the range""", json_schema_extra = { "linkml_meta": {'alias': 'upper_bound', 'domain_of': ['ValueRange']} })


class ValueSeries(StructuredValueComponent):
    """
    A series of values
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    values: Optional[List[float]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'values',
         'array': {'exact_number_dimensions': 1},
         'domain_of': ['ValueSeries', 'ResultMatrix']} })


class RelativeValue(StructuredValueComponent):
    """
    A value that is relative to another value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    interpretation: str = Field(..., description="""The type of relationship, e.g. high""", json_schema_extra = { "linkml_meta": {'alias': 'interpretation', 'domain_of': ['RelativeValue']} })
    reference: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'reference', 'domain_of': ['RelativeValue']} })
    target_value: Optional[AttributeValue] = Field(None, description="""The target value""", json_schema_extra = { "linkml_meta": {'alias': 'target_value', 'domain_of': ['RelativeValue']} })


class Event(DomainEntity):
    """
    A thing that happens to and potentially causally influences one of more participants.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['this class should be used for events that affect observables '
                      'under study, processes such as investigations and assays should '
                      'not use this',
                      'events can also be treated as observations where this suits the '
                      'analysis, but in general events are not considered to be '
                      'variables and instead represent some non-varying feature of the '
                      'effected observables'],
         'from_schema': 'https://w3id.org/comet/core'})

    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    has_participants: Optional[List[ParticipantInRole]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_participants', 'domain_of': ['Event']} })
    properties: Optional[List[AttributeValue]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'properties', 'domain_of': ['Observable', 'Event']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["Event"] = Field("Event", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class LocationComponent(Intangible):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/comet/core'})

    pass


class Location(LocationComponent):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    geo_location: Optional[GeoLocation] = Field(None, description="""A string representation of a geolocation""", json_schema_extra = { "linkml_meta": {'alias': 'geo_location', 'domain_of': ['Location']} })
    geo_box_location: Optional[GeoBoxLocation] = Field(None, description="""A string representation of a geobox location""", json_schema_extra = { "linkml_meta": {'alias': 'geo_box_location', 'domain_of': ['Location']} })
    named_location: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'named_location', 'domain_of': ['Location']} })
    relative_location: Optional[RelativeLocation] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'relative_location', 'domain_of': ['Location']} })
    postal_address: Optional[PostalAddress] = Field(None, description="""A postal address""", json_schema_extra = { "linkml_meta": {'alias': 'postal_address', 'domain_of': ['Location']} })


class GeoLocation(LocationComponent):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    latitude: Optional[Decimal] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'latitude', 'domain_of': ['GeoLocation'], 'slot_uri': 'wgs84:lat'} })
    longitude: Optional[Decimal] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'longitude', 'domain_of': ['GeoLocation'], 'slot_uri': 'wgs84:long'} })


class GeoBoxLocation(LocationComponent):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    west_bounding_coordinate: Optional[Decimal] = Field(None, description="""The westernmost coordinate of the location""", json_schema_extra = { "linkml_meta": {'alias': 'west_bounding_coordinate', 'domain_of': ['GeoBoxLocation']} })
    east_bounding_coordinate: Optional[Decimal] = Field(None, description="""The easternmost coordinate of the location""", json_schema_extra = { "linkml_meta": {'alias': 'east_bounding_coordinate', 'domain_of': ['GeoBoxLocation']} })
    north_bounding_coordinate: Optional[Decimal] = Field(None, description="""The northernmost coordinate of the location""", json_schema_extra = { "linkml_meta": {'alias': 'north_bounding_coordinate', 'domain_of': ['GeoBoxLocation']} })
    south_bounding_coordinate: Optional[Decimal] = Field(None, description="""The southernmost coordinate of the location""", json_schema_extra = { "linkml_meta": {'alias': 'south_bounding_coordinate', 'domain_of': ['GeoBoxLocation']} })


class RelativeLocation(LocationComponent):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    relationship_type: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'relationship_type', 'domain_of': ['RelativeLocation']} })
    target_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'target_location', 'domain_of': ['RelativeLocation']} })


class PostalAddress(LocationComponent):
    """
    Represents an Address
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['omopschema:CARE_SITE', 'schema:PostalAddress'],
         'from_schema': 'https://w3id.org/comet/core'})

    street_address: Optional[str] = Field(None, description="""The street address""", json_schema_extra = { "linkml_meta": {'alias': 'street_address',
         'domain_of': ['PostalAddress'],
         'exact_mappings': ['omopschema:address_1']} })
    street_address_additional: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'street_address_additional',
         'domain_of': ['PostalAddress'],
         'exact_mappings': ['omopschema:address_2']} })
    city: Optional[str] = Field(None, description="""The city""", json_schema_extra = { "linkml_meta": {'alias': 'city', 'domain_of': ['PostalAddress']} })
    state: Optional[str] = Field(None, description="""The state""", json_schema_extra = { "linkml_meta": {'alias': 'state', 'domain_of': ['PostalAddress']} })
    postal_code: Optional[str] = Field(None, description="""The postal code or zip code""", json_schema_extra = { "linkml_meta": {'alias': 'postal_code', 'domain_of': ['PostalAddress']} })
    country: Optional[str] = Field(None, description="""The country""", json_schema_extra = { "linkml_meta": {'alias': 'country', 'domain_of': ['PostalAddress']} })


class Sample(Observable):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    properties: Optional[List[AttributeValue]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'properties', 'domain_of': ['Observable', 'Event']} })
    case_or_control: Optional[CaseOrControlEnum] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'case_or_control', 'domain_of': ['Observable']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["Sample"] = Field("Sample", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class Investigation(InvestigativeEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    objectives: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'objectives', 'domain_of': ['Investigation']} })
    variables: Optional[List[str]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'variables', 'domain_of': ['Investigation']} })
    hypothesis: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'hypothesis', 'domain_of': ['Investigation', 'StudyResult']} })
    design: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'design', 'domain_of': ['Investigation']} })
    results: Optional[List[str]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'results', 'domain_of': ['Investigation', 'StudyResult']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["Investigation"] = Field("Investigation", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class InformationEntity(InvestigativeEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["InformationEntity"] = Field("InformationEntity", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class StudyResult(InformationEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    hypothesis: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'hypothesis', 'domain_of': ['Investigation', 'StudyResult']} })
    results: Optional[List[AttributeValue]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'results', 'domain_of': ['Investigation', 'StudyResult']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["StudyResult"] = Field("StudyResult", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class StudyHypothesis(InformationEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["StudyHypothesis"] = Field("StudyHypothesis", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class Agent(InvestigativeEntity):
    """
    Represents an Agent
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['prov:Agent', 'fibo.commons.PartiesAndSituations:Agent'],
         'from_schema': 'https://w3id.org/comet/core'})

    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["Agent"] = Field("Agent", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class Organization(InvestigativeEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["Organization"] = Field("Organization", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class Relationship(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'close_mappings': ['rdfs:Statement'],
         'from_schema': 'https://w3id.org/comet/core'})

    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    subject: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'subject', 'domain_of': ['Relationship']} })
    predicate: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'predicate', 'domain_of': ['Relationship']} })
    object: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'object', 'domain_of': ['Relationship']} })


class Temporal(Intangible):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/comet/core'})

    pass


class Duration(Temporal):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    start_time: Optional[TimePoint] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'start_time', 'domain_of': ['Duration']} })
    end_time: Optional[TimePoint] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'end_time', 'domain_of': ['Duration']} })
    happens_at: Optional[TimePoint] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'happens_at', 'domain_of': ['Duration']} })
    is_ongoing_as_of: Optional[TimePoint] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'is_ongoing_as_of', 'domain_of': ['Duration']} })
    recurring: Optional[RecurringTemporalWindow] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'recurring', 'domain_of': ['Duration']} })


class RecurringTemporalWindow(Temporal):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    enumerated_times: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'enumerated_times', 'domain_of': ['RecurringTemporalWindow']} })
    count: Optional[int] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'count', 'domain_of': ['RecurringTemporalWindow']} })
    period: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'period', 'domain_of': ['RecurringTemporalWindow']} })
    period_unit: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'period_unit', 'domain_of': ['RecurringTemporalWindow']} })


class TimePoint(Temporal):
    """
    A point in time. Can be fully specified, or specified in relative terms.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['fibo.DatesAndTimes:TimeInstant'],
         'from_schema': 'https://w3id.org/comet/core'})

    year_value: Optional[int] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'year_value',
         'domain_of': ['TimePoint'],
         'unit': {'symbol': 'year', 'ucum_code': 'a'}} })
    date_value: Optional[date] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'date_value', 'domain_of': ['TimePoint']} })
    time_value: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'time_value', 'domain_of': ['TimePoint']} })
    datetime_value: Optional[datetime ] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'datetime_value', 'domain_of': ['TimePoint']} })
    marker_event: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'marker_event', 'domain_of': ['TimePoint']} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })


class ProvenanceComponent(Intangible):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/comet/core'})

    pass


class CreationHistory(ProvenanceComponent):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    actions: Optional[List[CreationHistoryAction]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'actions', 'domain_of': ['CreationHistory']} })


class CreationHistoryAction(ProvenanceComponent):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    description: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction']} })
    roles: Optional[List[AgentRole]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'roles', 'domain_of': ['CreationHistoryAction']} })


class AgentRole(ProvenanceComponent):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    agent: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'agent', 'domain_of': ['AgentRole']} })
    role: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'role', 'domain_of': ['AgentRole', 'ParticipantInRole']} })


class CreationMetadata(ProvenanceComponent):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    title: Optional[str] = Field(None, description="""The title of the item""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['CreationMetadata'],
         'exact_mappings': ['dcterms:title']} })
    abstract: Optional[str] = Field(None, description="""A summary of the item""", json_schema_extra = { "linkml_meta": {'alias': 'abstract', 'domain_of': ['CreationMetadata']} })
    rights: Optional[str] = Field(None, description="""Information about rights held in and over the item""", json_schema_extra = { "linkml_meta": {'alias': 'rights', 'domain_of': ['CreationMetadata']} })
    creators: Optional[List[str]] = Field(None, description="""The person or organization who created the work""", json_schema_extra = { "linkml_meta": {'alias': 'creators',
         'domain_of': ['CreationMetadata'],
         'slot_uri': 'dcterms:creator'} })
    contributors: Optional[List[str]] = Field(None, description="""A person or organization that contributed to the creation of the work""", json_schema_extra = { "linkml_meta": {'alias': 'contributors',
         'domain_of': ['CreationMetadata'],
         'slot_uri': 'dcterms:contributor'} })
    contacts: Optional[List[str]] = Field(None, description="""A contact point for a person or organization""", json_schema_extra = { "linkml_meta": {'alias': 'contacts',
         'domain_of': ['CreationMetadata'],
         'slot_uri': 'schema:contactPoint'} })
    keywords: Optional[List[str]] = Field(None, description="""Keywords or tags used to describe this item""", json_schema_extra = { "linkml_meta": {'alias': 'keywords',
         'domain_of': ['CreationMetadata'],
         'slot_uri': 'schema:keywords'} })


class Concept(Thing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["Concept"] = Field("Concept", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class UnitConcept(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['qudt:Unit', 'oboe-core:Unit'],
         'from_schema': 'https://w3id.org/comet/core',
         'id_prefixes': ['UO', 'UCUM', 'qudt']})

    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["UnitConcept"] = Field("UnitConcept", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class QuantityKind(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['qudt:QuantityKind',
                            'fibo.QuantitiesAndUnits:ScalarQuantity'],
         'from_schema': 'https://w3id.org/comet/core'})

    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["QuantityKind"] = Field("QuantityKind", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class AttributeConcept(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['oboe-core:Characteristic'],
         'from_schema': 'https://w3id.org/comet/core',
         'id_prefixes': ['PATO']})

    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["AttributeConcept"] = Field("AttributeConcept", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class Variable(Concept):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    fixed_unit: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'fixed_unit', 'domain_of': ['Variable']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["Variable"] = Field("Variable", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class ParticipantInRole(Intangible):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    participant: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'participant', 'domain_of': ['ParticipantInRole']} })
    role: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'role', 'domain_of': ['AgentRole', 'ParticipantInRole']} })


class Device(InvestigativeEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["Device"] = Field("Device", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class DataObject(InvestigativeEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["DataObject"] = Field("DataObject", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class InvestigationSite(InvestigativeEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["InvestigationSite"] = Field("InvestigationSite", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class Procedure(InvestigativeEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['OBI:0000260', 'OBI:0000272', 'OBI:0000070'],
         'from_schema': 'https://w3id.org/comet/core',
         'slot_usage': {'classification': {'bindings': [{'binds_value_of': 'id',
                                                         'obligation_level': 'RECOMMENDED',
                                                         'range': 'InvestigativeProtocolEnum'}],
                                           'name': 'classification'}}})

    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["Procedure"] = Field("Procedure", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'RECOMMENDED',
                       'range': 'InvestigativeProtocolEnum'}],
         'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class InvestigativeProtocol(Procedure):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core',
         'slot_usage': {'classification': {'bindings': [{'binds_value_of': 'id',
                                                         'obligation_level': 'RECOMMENDED',
                                                         'range': 'InvestigativeProtocolEnum'}],
                                           'name': 'classification'}}})

    protocols_io_url: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'protocols_io_url', 'domain_of': ['InvestigativeProtocol']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["InvestigativeProtocol"] = Field("InvestigativeProtocol", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'RECOMMENDED',
                       'range': 'InvestigativeProtocolEnum'}],
         'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class StudyDesign(Procedure):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core',
         'slot_usage': {'classification': {'bindings': [{'binds_value_of': 'id',
                                                         'obligation_level': 'RECOMMENDED',
                                                         'range': 'StudyDesignEnum'}],
                                           'name': 'classification'}}})

    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["StudyDesign"] = Field("StudyDesign", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification',
         'bindings': [{'binds_value_of': 'id',
                       'obligation_level': 'RECOMMENDED',
                       'range': 'StudyDesignEnum'}],
         'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class State(Intangible):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    parameters: Optional[List[AttributeValue]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'parameters', 'domain_of': ['State']} })


class ProcedureConfiguration(State):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    parameters: Optional[List[AttributeValue]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'parameters', 'domain_of': ['State']} })


class ResultMatrix(Intangible):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core'})

    values: Optional[List[List[Union[AnyShapeArray[float], float]]]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'values',
         'array': {'dimensions': [{'alias': 'observables'}],
                   'maximum_number_dimensions': False,
                   'minimum_number_dimensions': 2},
         'domain_of': ['ValueSeries', 'ResultMatrix']} })


class Dataset(InvestigativeEntity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/core', 'tree_root': True})

    observables: Optional[List[Union[Observable,Sample,EnvironmentalMaterial,Organism,OrganismPart,OrganismPopulation,Patient,Cohort,Microbiome]]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'observables', 'domain_of': ['Dataset']} })
    observations: Optional[List[Observation]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'observations', 'domain_of': ['Dataset']} })
    concepts: Optional[List[Union[Concept,UnitConcept,QuantityKind,AttributeConcept,Variable]]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'concepts', 'domain_of': ['Dataset']} })
    events: Optional[List[Union[Event,HealthcareEncounter]]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'events', 'domain_of': ['Dataset']} })
    investigations: Optional[List[Investigation]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'investigations', 'domain_of': ['Dataset']} })
    relationships: Optional[List[Relationship]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'relationships', 'domain_of': ['Dataset']} })
    agents: Optional[List[Agent]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'agents', 'domain_of': ['Dataset']} })
    devices: Optional[List[Device]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'devices', 'domain_of': ['Dataset']} })
    samples: Optional[List[Sample]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'samples', 'domain_of': ['Dataset']} })
    result_matrices: Optional[List[ResultMatrix]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'result_matrices', 'domain_of': ['Dataset']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["Dataset"] = Field("Dataset", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class EnvironmentalMaterial(Observable):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/bio'})

    properties: Optional[List[AttributeValue]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'properties', 'domain_of': ['Observable', 'Event']} })
    case_or_control: Optional[CaseOrControlEnum] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'case_or_control', 'domain_of': ['Observable']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["EnvironmentalMaterial"] = Field("EnvironmentalMaterial", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class Organism(Observable):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/bio'})

    properties: Optional[List[AttributeValue]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'properties', 'domain_of': ['Observable', 'Event']} })
    case_or_control: Optional[CaseOrControlEnum] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'case_or_control', 'domain_of': ['Observable']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["Organism"] = Field("Organism", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class OrganismPart(Observable):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/bio'})

    properties: Optional[List[AttributeValue]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'properties', 'domain_of': ['Observable', 'Event']} })
    case_or_control: Optional[CaseOrControlEnum] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'case_or_control', 'domain_of': ['Observable']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["OrganismPart"] = Field("OrganismPart", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class OrganismPopulation(Observable):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/bio'})

    properties: Optional[List[AttributeValue]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'properties', 'domain_of': ['Observable', 'Event']} })
    case_or_control: Optional[CaseOrControlEnum] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'case_or_control', 'domain_of': ['Observable']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["OrganismPopulation"] = Field("OrganismPopulation", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class Microbiome(OrganismPopulation):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/comet/bio'})

    properties: Optional[List[AttributeValue]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'properties', 'domain_of': ['Observable', 'Event']} })
    case_or_control: Optional[CaseOrControlEnum] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'case_or_control', 'domain_of': ['Observable']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["Microbiome"] = Field("Microbiome", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class Patient(Observable):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['fhir:Patient'],
         'from_schema': 'https://w3id.org/linkml-common/healthcare'})

    properties: Optional[List[AttributeValue]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'properties', 'domain_of': ['Observable', 'Event']} })
    case_or_control: Optional[CaseOrControlEnum] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'case_or_control', 'domain_of': ['Observable']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["Patient"] = Field("Patient", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class Cohort(Observable):
    """
    A group of patients with a common characteristic
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['omopschema:COHORT'],
         'from_schema': 'https://w3id.org/linkml-common/healthcare'})

    properties: Optional[List[AttributeValue]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'properties', 'domain_of': ['Observable', 'Event']} })
    case_or_control: Optional[CaseOrControlEnum] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'case_or_control', 'domain_of': ['Observable']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["Cohort"] = Field("Cohort", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class HealthcareSite(InvestigationSite):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['omopschema:CARE_SITE'],
         'from_schema': 'https://w3id.org/linkml-common/healthcare'})

    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["HealthcareSite"] = Field("HealthcareSite", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class HealthcareEncounter(Event):
    """
    An interaction between a patient and one or more healthcare providers
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['omopschema:VISIT_OCCURRENCE'],
         'from_schema': 'https://w3id.org/linkml-common/healthcare',
         'slot_usage': {'classification': {'name': 'classification',
                                           'range': 'HealthcareEncounterClassification'}}})

    patient: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'patient', 'domain_of': ['HealthcareEncounter']} })
    provider: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'provider', 'domain_of': ['HealthcareEncounter']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    has_participants: Optional[List[ParticipantInRole]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_participants', 'domain_of': ['Event']} })
    properties: Optional[List[AttributeValue]] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'properties', 'domain_of': ['Observable', 'Event']} })
    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["HealthcareEncounter"] = Field("HealthcareEncounter", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[HealthcareEncounterClassification] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


class HealthcareOrganization(Organization):
    """
    An organization that provides healthcare services
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml-common/healthcare'})

    id: str = Field(..., description="""A unique identifier for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Thing'],
         'exact_mappings': ['rdfs:label'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Thing', 'TimePoint', 'CreationHistoryAction'],
         'slot_uri': 'schema:description'} })
    type: Literal["HealthcareOrganization"] = Field("HealthcareOrganization", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""", json_schema_extra = { "linkml_meta": {'alias': 'type', 'designates_type': True, 'domain_of': ['Thing']} })
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""", json_schema_extra = { "linkml_meta": {'alias': 'classification', 'domain_of': ['Thing']} })
    ontology_types: Optional[List[str]] = Field(None, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""", json_schema_extra = { "linkml_meta": {'alias': 'ontology_types', 'domain_of': ['Thing']} })
    has_location: Optional[Location] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_location', 'domain_of': ['Thing']} })
    has_time: Optional[Duration] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_time',
         'domain_of': ['Thing',
                       'Observation',
                       'Event',
                       'Investigation',
                       'Relationship']} })
    metadata: Optional[CreationHistory] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'metadata', 'domain_of': ['Thing']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Thing.model_rebuild()
Intangible.model_rebuild()
DomainEntity.model_rebuild()
InvestigativeEntity.model_rebuild()
Observable.model_rebuild()
Observation.model_rebuild()
StructuredValueComponent.model_rebuild()
AttributeValue.model_rebuild()
Ratio.model_rebuild()
ValueRange.model_rebuild()
ValueSeries.model_rebuild()
RelativeValue.model_rebuild()
Event.model_rebuild()
LocationComponent.model_rebuild()
Location.model_rebuild()
GeoLocation.model_rebuild()
GeoBoxLocation.model_rebuild()
RelativeLocation.model_rebuild()
PostalAddress.model_rebuild()
Sample.model_rebuild()
Investigation.model_rebuild()
InformationEntity.model_rebuild()
StudyResult.model_rebuild()
StudyHypothesis.model_rebuild()
Agent.model_rebuild()
Organization.model_rebuild()
Relationship.model_rebuild()
Temporal.model_rebuild()
Duration.model_rebuild()
RecurringTemporalWindow.model_rebuild()
TimePoint.model_rebuild()
ProvenanceComponent.model_rebuild()
CreationHistory.model_rebuild()
CreationHistoryAction.model_rebuild()
AgentRole.model_rebuild()
CreationMetadata.model_rebuild()
Concept.model_rebuild()
UnitConcept.model_rebuild()
QuantityKind.model_rebuild()
AttributeConcept.model_rebuild()
Variable.model_rebuild()
ParticipantInRole.model_rebuild()
Device.model_rebuild()
DataObject.model_rebuild()
InvestigationSite.model_rebuild()
Procedure.model_rebuild()
InvestigativeProtocol.model_rebuild()
StudyDesign.model_rebuild()
State.model_rebuild()
ProcedureConfiguration.model_rebuild()
ResultMatrix.model_rebuild()
Dataset.model_rebuild()
EnvironmentalMaterial.model_rebuild()
Organism.model_rebuild()
OrganismPart.model_rebuild()
OrganismPopulation.model_rebuild()
Microbiome.model_rebuild()
Patient.model_rebuild()
Cohort.model_rebuild()
HealthcareSite.model_rebuild()
HealthcareEncounter.model_rebuild()
HealthcareOrganization.model_rebuild()

