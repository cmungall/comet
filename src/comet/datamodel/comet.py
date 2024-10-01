# Auto generated from comet.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-09-13T18:36:53
# Schema: comet
#
# id: https://w3id.org/comet
# description: Common Data Model Elements
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime, time
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Date, Datetime, Decimal, Float, Integer, String, Time, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Decimal, URI, URIorCURIE, XSDDate, XSDDateTime, XSDTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
UCUM = CurieNamespace('UCUM', 'http://unitsofmeasure.org/')
UO = CurieNamespace('UO', 'http://example.org/UNKNOWN/UO/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
COMET = CurieNamespace('comet', 'https://w3id.org/comet/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
EXAMPLE = CurieNamespace('example', 'http://example.org/')
FHIR = CurieNamespace('fhir', 'http://hl7.org/fhir/')
FIBO_DATESANDTIMES = CurieNamespace('fibo_DatesAndTimes', 'http://example.org/UNKNOWN/fibo.DatesAndTimes/')
FIBO_QUANTITIESANDUNITS = CurieNamespace('fibo_QuantitiesAndUnits', 'http://example.org/UNKNOWN/fibo.QuantitiesAndUnits/')
FIBO_COMMONS_PARTIESANDSITUATIONS = CurieNamespace('fibo_commons_PartiesAndSituations', 'http://example.org/UNKNOWN/fibo.commons.PartiesAndSituations/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LINKML_COMMON = CurieNamespace('linkml_common', 'https://w3id.org/linkml-common/')
OBOE_CORE = CurieNamespace('oboe-core', 'http://ecoinformatics.org/oboe/oboe.1.0/oboe-core.owl#')
OM = CurieNamespace('om', 'http://www.opengis.net/om/2.0')
OMOPSCHEMA = CurieNamespace('omopschema', 'http://example.org/omop/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUDT = CurieNamespace('qudt', 'http://example.org/UNKNOWN/qudt/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
WGS84 = CurieNamespace('wgs84', 'http://www.w3.org/2003/01/geo/wgs84_pos#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = COMET


# Types
class CountScalar(Integer):
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "CountScalar"
    type_model_uri = COMET.CountScalar


# Class references
class ThingId(URIorCURIE):
    pass


class DomainEntityId(ThingId):
    pass


class InvestigativeEntityId(ThingId):
    pass


class ObservableId(DomainEntityId):
    pass


class ObservationId(InvestigativeEntityId):
    pass


class EventId(DomainEntityId):
    pass


class SampleId(ObservableId):
    pass


class InvestigationId(InvestigativeEntityId):
    pass


class InformationEntityId(InvestigativeEntityId):
    pass


class StudyResultId(InformationEntityId):
    pass


class StudyHypothesisId(InformationEntityId):
    pass


class AgentId(InvestigativeEntityId):
    pass


class OrganizationId(InvestigativeEntityId):
    pass


class ConceptId(ThingId):
    pass


class UnitConceptId(ConceptId):
    pass


class QuantityKindId(ConceptId):
    pass


class AttributeConceptId(ConceptId):
    pass


class VariableId(ConceptId):
    pass


class DeviceId(InvestigativeEntityId):
    pass


class DataObjectId(InvestigativeEntityId):
    pass


class InvestigationSiteId(InvestigativeEntityId):
    pass


class ProcedureId(InvestigativeEntityId):
    pass


class InvestigativeProtocolId(ProcedureId):
    pass


class StudyDesignId(ProcedureId):
    pass


class DatasetId(InvestigativeEntityId):
    pass


class PatientId(ObservableId):
    pass


class CohortId(ObservableId):
    pass


class HealthcareSiteId(InvestigationSiteId):
    pass


class HealthcareEncounterId(EventId):
    pass


class HealthcareOrganizationId(OrganizationId):
    pass


class EnvironmentalMaterialId(ObservableId):
    pass


class OrganismId(ObservableId):
    pass


class OrganismPartId(ObservableId):
    pass


class OrganismPopulationId(ObservableId):
    pass


class MicrobiomeId(OrganismPopulationId):
    pass


@dataclass(repr=False)
class Thing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = COMET.Thing

    id: Union[str, ThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    classification: Optional[Union[str, ConceptId]] = None
    ontology_types: Optional[Union[Union[str, ConceptId], List[Union[str, ConceptId]]]] = empty_list()
    has_location: Optional[Union[dict, "Location"]] = None
    has_time: Optional[Union[dict, "Duration"]] = None
    metadata: Optional[Union[dict, "CreationHistory"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThingId):
            self.id = ThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self.type = str(self.class_name)

        if self.classification is not None and not isinstance(self.classification, ConceptId):
            self.classification = ConceptId(self.classification)

        if not isinstance(self.ontology_types, list):
            self.ontology_types = [self.ontology_types] if self.ontology_types is not None else []
        self.ontology_types = [v if isinstance(v, ConceptId) else ConceptId(v) for v in self.ontology_types]

        if self.has_location is not None and not isinstance(self.has_location, Location):
            self.has_location = Location(**as_dict(self.has_location))

        if self.has_time is not None and not isinstance(self.has_time, Duration):
            self.has_time = Duration(**as_dict(self.has_time))

        if self.metadata is not None and not isinstance(self.metadata, CreationHistory):
            self.metadata = CreationHistory(**as_dict(self.metadata))

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



class Intangible(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["Intangible"]
    class_class_curie: ClassVar[str] = "comet:Intangible"
    class_name: ClassVar[str] = "Intangible"
    class_model_uri: ClassVar[URIRef] = COMET.Intangible


@dataclass(repr=False)
class DomainEntity(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["DomainEntity"]
    class_class_curie: ClassVar[str] = "comet:DomainEntity"
    class_name: ClassVar[str] = "DomainEntity"
    class_model_uri: ClassVar[URIRef] = COMET.DomainEntity

    id: Union[str, DomainEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class InvestigativeEntity(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["InvestigativeEntity"]
    class_class_curie: ClassVar[str] = "comet:InvestigativeEntity"
    class_name: ClassVar[str] = "InvestigativeEntity"
    class_model_uri: ClassVar[URIRef] = COMET.InvestigativeEntity

    id: Union[str, InvestigativeEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class Observable(DomainEntity):
    """
    A concrete or abstract entity that has been observed or measured. Examples include a person, a region of the
    earth, a cell type, a tree, a mountain.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["Observable"]
    class_class_curie: ClassVar[str] = "comet:Observable"
    class_name: ClassVar[str] = "Observable"
    class_model_uri: ClassVar[URIRef] = COMET.Observable

    id: Union[str, ObservableId] = None
    properties: Optional[Union[Union[dict, "AttributeValue"], List[Union[dict, "AttributeValue"]]]] = empty_list()
    case_or_control: Optional[Union[str, "CaseOrControlEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObservableId):
            self.id = ObservableId(self.id)

        if not isinstance(self.properties, list):
            self.properties = [self.properties] if self.properties is not None else []
        self.properties = [v if isinstance(v, AttributeValue) else AttributeValue(**as_dict(v)) for v in self.properties]

        if self.case_or_control is not None and not isinstance(self.case_or_control, CaseOrControlEnum):
            self.case_or_control = CaseOrControlEnum(self.case_or_control)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class Observation(InvestigativeEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["Observation"]
    class_class_curie: ClassVar[str] = "comet:Observation"
    class_name: ClassVar[str] = "Observation"
    class_model_uri: ClassVar[URIRef] = COMET.Observation

    id: Union[str, ObservationId] = None
    has_time: Optional[Union[dict, "Duration"]] = None
    is_about: Optional[Union[str, ObservableId]] = None
    result: Optional[Union[dict, "AttributeValue"]] = None
    part_of: Optional[Union[str, InvestigationId]] = None
    performer: Optional[Union[str, AgentId]] = None
    method: Optional[Union[str, ConceptId]] = None
    device_used: Optional[Union[str, DeviceId]] = None
    procedure_used: Optional[Union[str, ProcedureId]] = None
    procedure_configuration: Optional[Union[dict, "ProcedureConfiguration"]] = None
    sample_used: Optional[Union[str, SampleId]] = None
    data_used: Optional[Union[str, DataObjectId]] = None
    derived_from: Optional[Union[Union[str, ObservationId], List[Union[str, ObservationId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObservationId):
            self.id = ObservationId(self.id)

        if self.has_time is not None and not isinstance(self.has_time, Duration):
            self.has_time = Duration(**as_dict(self.has_time))

        if self.is_about is not None and not isinstance(self.is_about, ObservableId):
            self.is_about = ObservableId(self.is_about)

        if self.result is not None and not isinstance(self.result, AttributeValue):
            self.result = AttributeValue(**as_dict(self.result))

        if self.part_of is not None and not isinstance(self.part_of, InvestigationId):
            self.part_of = InvestigationId(self.part_of)

        if self.performer is not None and not isinstance(self.performer, AgentId):
            self.performer = AgentId(self.performer)

        if self.method is not None and not isinstance(self.method, ConceptId):
            self.method = ConceptId(self.method)

        if self.device_used is not None and not isinstance(self.device_used, DeviceId):
            self.device_used = DeviceId(self.device_used)

        if self.procedure_used is not None and not isinstance(self.procedure_used, ProcedureId):
            self.procedure_used = ProcedureId(self.procedure_used)

        if self.procedure_configuration is not None and not isinstance(self.procedure_configuration, ProcedureConfiguration):
            self.procedure_configuration = ProcedureConfiguration(**as_dict(self.procedure_configuration))

        if self.sample_used is not None and not isinstance(self.sample_used, SampleId):
            self.sample_used = SampleId(self.sample_used)

        if self.data_used is not None and not isinstance(self.data_used, DataObjectId):
            self.data_used = DataObjectId(self.data_used)

        if not isinstance(self.derived_from, list):
            self.derived_from = [self.derived_from] if self.derived_from is not None else []
        self.derived_from = [v if isinstance(v, ObservationId) else ObservationId(v) for v in self.derived_from]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class StructuredValueComponent(Intangible):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["StructuredValueComponent"]
    class_class_curie: ClassVar[str] = "comet:StructuredValueComponent"
    class_name: ClassVar[str] = "StructuredValueComponent"
    class_model_uri: ClassVar[URIRef] = COMET.StructuredValueComponent


@dataclass(repr=False)
class AttributeValue(StructuredValueComponent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["AttributeValue"]
    class_class_curie: ClassVar[str] = "comet:AttributeValue"
    class_name: ClassVar[str] = "AttributeValue"
    class_model_uri: ClassVar[URIRef] = COMET.AttributeValue

    attribute: Optional[Union[str, AttributeConceptId]] = None
    target: Optional[Union[str, ConceptId]] = None
    numeric_value: Optional[float] = None
    presence_value: Optional[Union[str, "PresenceEnum"]] = None
    value_range: Optional[Union[dict, "ValueRange"]] = None
    value_series: Optional[Union[dict, "ValueSeries"]] = None
    ratio: Optional[Union[dict, "Ratio"]] = None
    qualitative_value: Optional[Union[str, ConceptId]] = None
    unit: Optional[Union[str, UnitConceptId]] = None
    relative_values: Optional[Union[Union[dict, "RelativeValue"], List[Union[dict, "RelativeValue"]]]] = empty_list()
    value_absence_reason: Optional[Union[str, ConceptId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.attribute is not None and not isinstance(self.attribute, AttributeConceptId):
            self.attribute = AttributeConceptId(self.attribute)

        if self.target is not None and not isinstance(self.target, ConceptId):
            self.target = ConceptId(self.target)

        if self.numeric_value is not None and not isinstance(self.numeric_value, float):
            self.numeric_value = float(self.numeric_value)

        if self.presence_value is not None and not isinstance(self.presence_value, PresenceEnum):
            self.presence_value = PresenceEnum(self.presence_value)

        if self.value_range is not None and not isinstance(self.value_range, ValueRange):
            self.value_range = ValueRange(**as_dict(self.value_range))

        if self.value_series is not None and not isinstance(self.value_series, ValueSeries):
            self.value_series = ValueSeries(**as_dict(self.value_series))

        if self.ratio is not None and not isinstance(self.ratio, Ratio):
            self.ratio = Ratio(**as_dict(self.ratio))

        if self.qualitative_value is not None and not isinstance(self.qualitative_value, ConceptId):
            self.qualitative_value = ConceptId(self.qualitative_value)

        if self.unit is not None and not isinstance(self.unit, UnitConceptId):
            self.unit = UnitConceptId(self.unit)

        if not isinstance(self.relative_values, list):
            self.relative_values = [self.relative_values] if self.relative_values is not None else []
        self.relative_values = [v if isinstance(v, RelativeValue) else RelativeValue(**as_dict(v)) for v in self.relative_values]

        if self.value_absence_reason is not None and not isinstance(self.value_absence_reason, ConceptId):
            self.value_absence_reason = ConceptId(self.value_absence_reason)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Ratio(StructuredValueComponent):
    """
    A tuple of two quantities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FHIR["Ratio"]
    class_class_curie: ClassVar[str] = "fhir:Ratio"
    class_name: ClassVar[str] = "Ratio"
    class_model_uri: ClassVar[URIRef] = COMET.Ratio

    numerator: Optional[Union[dict, AttributeValue]] = None
    denominator: Optional[Union[dict, AttributeValue]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.numerator is not None and not isinstance(self.numerator, AttributeValue):
            self.numerator = AttributeValue(**as_dict(self.numerator))

        if self.denominator is not None and not isinstance(self.denominator, AttributeValue):
            self.denominator = AttributeValue(**as_dict(self.denominator))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ValueRange(StructuredValueComponent):
    """
    A quantity range is a property that can be measured or counted
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FHIR["Range"]
    class_class_curie: ClassVar[str] = "fhir:Range"
    class_name: ClassVar[str] = "ValueRange"
    class_model_uri: ClassVar[URIRef] = COMET.ValueRange

    lower_bound: Optional[float] = None
    upper_bound: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.lower_bound is not None and not isinstance(self.lower_bound, float):
            self.lower_bound = float(self.lower_bound)

        if self.upper_bound is not None and not isinstance(self.upper_bound, float):
            self.upper_bound = float(self.upper_bound)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ValueSeries(StructuredValueComponent):
    """
    A series of values
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["ValueSeries"]
    class_class_curie: ClassVar[str] = "comet:ValueSeries"
    class_name: ClassVar[str] = "ValueSeries"
    class_model_uri: ClassVar[URIRef] = COMET.ValueSeries

    values: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.values is not None and not isinstance(self.values, float):
            self.values = float(self.values)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelativeValue(StructuredValueComponent):
    """
    A value that is relative to another value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["RelativeValue"]
    class_class_curie: ClassVar[str] = "comet:RelativeValue"
    class_name: ClassVar[str] = "RelativeValue"
    class_model_uri: ClassVar[URIRef] = COMET.RelativeValue

    interpretation: Union[str, ConceptId] = None
    reference: Optional[Union[str, ConceptId]] = None
    target_value: Optional[Union[dict, AttributeValue]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.interpretation):
            self.MissingRequiredField("interpretation")
        if not isinstance(self.interpretation, ConceptId):
            self.interpretation = ConceptId(self.interpretation)

        if self.reference is not None and not isinstance(self.reference, ConceptId):
            self.reference = ConceptId(self.reference)

        if self.target_value is not None and not isinstance(self.target_value, AttributeValue):
            self.target_value = AttributeValue(**as_dict(self.target_value))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Event(DomainEntity):
    """
    A thing that happens to and potentially causally influences one of more participants.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["Event"]
    class_class_curie: ClassVar[str] = "comet:Event"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = COMET.Event

    id: Union[str, EventId] = None
    has_time: Optional[Union[dict, "Duration"]] = None
    has_participants: Optional[Union[Union[dict, "ParticipantInRole"], List[Union[dict, "ParticipantInRole"]]]] = empty_list()
    properties: Optional[Union[Union[dict, AttributeValue], List[Union[dict, AttributeValue]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventId):
            self.id = EventId(self.id)

        if self.has_time is not None and not isinstance(self.has_time, Duration):
            self.has_time = Duration(**as_dict(self.has_time))

        if not isinstance(self.has_participants, list):
            self.has_participants = [self.has_participants] if self.has_participants is not None else []
        self.has_participants = [v if isinstance(v, ParticipantInRole) else ParticipantInRole(**as_dict(v)) for v in self.has_participants]

        if not isinstance(self.properties, list):
            self.properties = [self.properties] if self.properties is not None else []
        self.properties = [v if isinstance(v, AttributeValue) else AttributeValue(**as_dict(v)) for v in self.properties]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


class LocationComponent(Intangible):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["LocationComponent"]
    class_class_curie: ClassVar[str] = "comet:LocationComponent"
    class_name: ClassVar[str] = "LocationComponent"
    class_model_uri: ClassVar[URIRef] = COMET.LocationComponent


@dataclass(repr=False)
class Location(LocationComponent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["Location"]
    class_class_curie: ClassVar[str] = "comet:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = COMET.Location

    geo_location: Optional[Union[dict, "GeoLocation"]] = None
    geo_box_location: Optional[Union[dict, "GeoBoxLocation"]] = None
    named_location: Optional[Union[str, ConceptId]] = None
    relative_location: Optional[Union[dict, "RelativeLocation"]] = None
    postal_address: Optional[Union[dict, "PostalAddress"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.geo_location is not None and not isinstance(self.geo_location, GeoLocation):
            self.geo_location = GeoLocation(**as_dict(self.geo_location))

        if self.geo_box_location is not None and not isinstance(self.geo_box_location, GeoBoxLocation):
            self.geo_box_location = GeoBoxLocation(**as_dict(self.geo_box_location))

        if self.named_location is not None and not isinstance(self.named_location, ConceptId):
            self.named_location = ConceptId(self.named_location)

        if self.relative_location is not None and not isinstance(self.relative_location, RelativeLocation):
            self.relative_location = RelativeLocation(**as_dict(self.relative_location))

        if self.postal_address is not None and not isinstance(self.postal_address, PostalAddress):
            self.postal_address = PostalAddress(**as_dict(self.postal_address))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeoLocation(LocationComponent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["GeoLocation"]
    class_class_curie: ClassVar[str] = "comet:GeoLocation"
    class_name: ClassVar[str] = "GeoLocation"
    class_model_uri: ClassVar[URIRef] = COMET.GeoLocation

    latitude: Optional[Decimal] = None
    longitude: Optional[Decimal] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.latitude is not None and not isinstance(self.latitude, Decimal):
            self.latitude = Decimal(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, Decimal):
            self.longitude = Decimal(self.longitude)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeoBoxLocation(LocationComponent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["GeoBoxLocation"]
    class_class_curie: ClassVar[str] = "comet:GeoBoxLocation"
    class_name: ClassVar[str] = "GeoBoxLocation"
    class_model_uri: ClassVar[URIRef] = COMET.GeoBoxLocation

    west_bounding_coordinate: Optional[Decimal] = None
    east_bounding_coordinate: Optional[Decimal] = None
    north_bounding_coordinate: Optional[Decimal] = None
    south_bounding_coordinate: Optional[Decimal] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.west_bounding_coordinate is not None and not isinstance(self.west_bounding_coordinate, Decimal):
            self.west_bounding_coordinate = Decimal(self.west_bounding_coordinate)

        if self.east_bounding_coordinate is not None and not isinstance(self.east_bounding_coordinate, Decimal):
            self.east_bounding_coordinate = Decimal(self.east_bounding_coordinate)

        if self.north_bounding_coordinate is not None and not isinstance(self.north_bounding_coordinate, Decimal):
            self.north_bounding_coordinate = Decimal(self.north_bounding_coordinate)

        if self.south_bounding_coordinate is not None and not isinstance(self.south_bounding_coordinate, Decimal):
            self.south_bounding_coordinate = Decimal(self.south_bounding_coordinate)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelativeLocation(LocationComponent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["RelativeLocation"]
    class_class_curie: ClassVar[str] = "comet:RelativeLocation"
    class_name: ClassVar[str] = "RelativeLocation"
    class_model_uri: ClassVar[URIRef] = COMET.RelativeLocation

    relationship_type: Optional[Union[str, ConceptId]] = None
    target_location: Optional[Union[dict, Location]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.relationship_type is not None and not isinstance(self.relationship_type, ConceptId):
            self.relationship_type = ConceptId(self.relationship_type)

        if self.target_location is not None and not isinstance(self.target_location, Location):
            self.target_location = Location(**as_dict(self.target_location))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PostalAddress(LocationComponent):
    """
    Represents an Address
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["PostalAddress"]
    class_class_curie: ClassVar[str] = "comet:PostalAddress"
    class_name: ClassVar[str] = "PostalAddress"
    class_model_uri: ClassVar[URIRef] = COMET.PostalAddress

    street_address: Optional[str] = None
    street_address_additional: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[Union[str, ConceptId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.street_address is not None and not isinstance(self.street_address, str):
            self.street_address = str(self.street_address)

        if self.street_address_additional is not None and not isinstance(self.street_address_additional, str):
            self.street_address_additional = str(self.street_address_additional)

        if self.city is not None and not isinstance(self.city, str):
            self.city = str(self.city)

        if self.state is not None and not isinstance(self.state, str):
            self.state = str(self.state)

        if self.postal_code is not None and not isinstance(self.postal_code, str):
            self.postal_code = str(self.postal_code)

        if self.country is not None and not isinstance(self.country, ConceptId):
            self.country = ConceptId(self.country)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(Observable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["Sample"]
    class_class_curie: ClassVar[str] = "comet:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = COMET.Sample

    id: Union[str, SampleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleId):
            self.id = SampleId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class Investigation(InvestigativeEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["Investigation"]
    class_class_curie: ClassVar[str] = "comet:Investigation"
    class_name: ClassVar[str] = "Investigation"
    class_model_uri: ClassVar[URIRef] = COMET.Investigation

    id: Union[str, InvestigationId] = None
    has_time: Optional[Union[dict, "Duration"]] = None
    objectives: Optional[str] = None
    variables: Optional[Union[Union[str, ConceptId], List[Union[str, ConceptId]]]] = empty_list()
    hypothesis: Optional[Union[str, StudyHypothesisId]] = None
    design: Optional[Union[str, StudyDesignId]] = None
    results: Optional[Union[Union[str, StudyResultId], List[Union[str, StudyResultId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InvestigationId):
            self.id = InvestigationId(self.id)

        if self.has_time is not None and not isinstance(self.has_time, Duration):
            self.has_time = Duration(**as_dict(self.has_time))

        if self.objectives is not None and not isinstance(self.objectives, str):
            self.objectives = str(self.objectives)

        if not isinstance(self.variables, list):
            self.variables = [self.variables] if self.variables is not None else []
        self.variables = [v if isinstance(v, ConceptId) else ConceptId(v) for v in self.variables]

        if self.hypothesis is not None and not isinstance(self.hypothesis, StudyHypothesisId):
            self.hypothesis = StudyHypothesisId(self.hypothesis)

        if self.design is not None and not isinstance(self.design, StudyDesignId):
            self.design = StudyDesignId(self.design)

        if not isinstance(self.results, list):
            self.results = [self.results] if self.results is not None else []
        self.results = [v if isinstance(v, StudyResultId) else StudyResultId(v) for v in self.results]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class InformationEntity(InvestigativeEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["InformationEntity"]
    class_class_curie: ClassVar[str] = "comet:InformationEntity"
    class_name: ClassVar[str] = "InformationEntity"
    class_model_uri: ClassVar[URIRef] = COMET.InformationEntity

    id: Union[str, InformationEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationEntityId):
            self.id = InformationEntityId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class StudyResult(InformationEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["StudyResult"]
    class_class_curie: ClassVar[str] = "comet:StudyResult"
    class_name: ClassVar[str] = "StudyResult"
    class_model_uri: ClassVar[URIRef] = COMET.StudyResult

    id: Union[str, StudyResultId] = None
    hypothesis: Optional[Union[str, StudyHypothesisId]] = None
    results: Optional[Union[Union[dict, AttributeValue], List[Union[dict, AttributeValue]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyResultId):
            self.id = StudyResultId(self.id)

        if self.hypothesis is not None and not isinstance(self.hypothesis, StudyHypothesisId):
            self.hypothesis = StudyHypothesisId(self.hypothesis)

        if not isinstance(self.results, list):
            self.results = [self.results] if self.results is not None else []
        self.results = [v if isinstance(v, AttributeValue) else AttributeValue(**as_dict(v)) for v in self.results]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class StudyHypothesis(InformationEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["StudyHypothesis"]
    class_class_curie: ClassVar[str] = "comet:StudyHypothesis"
    class_name: ClassVar[str] = "StudyHypothesis"
    class_model_uri: ClassVar[URIRef] = COMET.StudyHypothesis

    id: Union[str, StudyHypothesisId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyHypothesisId):
            self.id = StudyHypothesisId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class Agent(InvestigativeEntity):
    """
    Represents an Agent
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["Agent"]
    class_class_curie: ClassVar[str] = "comet:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = COMET.Agent

    id: Union[str, AgentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AgentId):
            self.id = AgentId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class Organization(InvestigativeEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["Organization"]
    class_class_curie: ClassVar[str] = "comet:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = COMET.Organization

    id: Union[str, OrganizationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganizationId):
            self.id = OrganizationId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class Relationship(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["Relationship"]
    class_class_curie: ClassVar[str] = "comet:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = COMET.Relationship

    has_time: Optional[Union[dict, "Duration"]] = None
    subject: Optional[Union[str, ThingId]] = None
    predicate: Optional[Union[str, ConceptId]] = None
    object: Optional[Union[str, ThingId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_time is not None and not isinstance(self.has_time, Duration):
            self.has_time = Duration(**as_dict(self.has_time))

        if self.subject is not None and not isinstance(self.subject, ThingId):
            self.subject = ThingId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, ConceptId):
            self.predicate = ConceptId(self.predicate)

        if self.object is not None and not isinstance(self.object, ThingId):
            self.object = ThingId(self.object)

        super().__post_init__(**kwargs)


class Temporal(Intangible):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["Temporal"]
    class_class_curie: ClassVar[str] = "comet:Temporal"
    class_name: ClassVar[str] = "Temporal"
    class_model_uri: ClassVar[URIRef] = COMET.Temporal


@dataclass(repr=False)
class Duration(Temporal):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["Duration"]
    class_class_curie: ClassVar[str] = "comet:Duration"
    class_name: ClassVar[str] = "Duration"
    class_model_uri: ClassVar[URIRef] = COMET.Duration

    start_time: Optional[Union[dict, "TimePoint"]] = None
    end_time: Optional[Union[dict, "TimePoint"]] = None
    happens_at: Optional[Union[dict, "TimePoint"]] = None
    is_ongoing_as_of: Optional[Union[dict, "TimePoint"]] = None
    recurring: Optional[Union[dict, "RecurringTemporalWindow"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.start_time is not None and not isinstance(self.start_time, TimePoint):
            self.start_time = TimePoint(**as_dict(self.start_time))

        if self.end_time is not None and not isinstance(self.end_time, TimePoint):
            self.end_time = TimePoint(**as_dict(self.end_time))

        if self.happens_at is not None and not isinstance(self.happens_at, TimePoint):
            self.happens_at = TimePoint(**as_dict(self.happens_at))

        if self.is_ongoing_as_of is not None and not isinstance(self.is_ongoing_as_of, TimePoint):
            self.is_ongoing_as_of = TimePoint(**as_dict(self.is_ongoing_as_of))

        if self.recurring is not None and not isinstance(self.recurring, RecurringTemporalWindow):
            self.recurring = RecurringTemporalWindow(**as_dict(self.recurring))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecurringTemporalWindow(Temporal):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["RecurringTemporalWindow"]
    class_class_curie: ClassVar[str] = "comet:RecurringTemporalWindow"
    class_name: ClassVar[str] = "RecurringTemporalWindow"
    class_model_uri: ClassVar[URIRef] = COMET.RecurringTemporalWindow

    enumerated_times: Optional[Union[dict, Duration]] = None
    count: Optional[int] = None
    period: Optional[Union[dict, Duration]] = None
    period_unit: Optional[Union[str, UnitConceptId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.enumerated_times is not None and not isinstance(self.enumerated_times, Duration):
            self.enumerated_times = Duration(**as_dict(self.enumerated_times))

        if self.count is not None and not isinstance(self.count, int):
            self.count = int(self.count)

        if self.period is not None and not isinstance(self.period, Duration):
            self.period = Duration(**as_dict(self.period))

        if self.period_unit is not None and not isinstance(self.period_unit, UnitConceptId):
            self.period_unit = UnitConceptId(self.period_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TimePoint(Temporal):
    """
    A point in time. Can be fully specified, or specified in relative terms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["TimePoint"]
    class_class_curie: ClassVar[str] = "comet:TimePoint"
    class_name: ClassVar[str] = "TimePoint"
    class_model_uri: ClassVar[URIRef] = COMET.TimePoint

    year_value: Optional[int] = None
    date_value: Optional[Union[str, XSDDate]] = None
    time_value: Optional[Union[str, XSDTime]] = None
    datetime_value: Optional[Union[str, XSDDateTime]] = None
    marker_event: Optional[Union[str, EventId]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.year_value is not None and not isinstance(self.year_value, int):
            self.year_value = int(self.year_value)

        if self.date_value is not None and not isinstance(self.date_value, XSDDate):
            self.date_value = XSDDate(self.date_value)

        if self.time_value is not None and not isinstance(self.time_value, XSDTime):
            self.time_value = XSDTime(self.time_value)

        if self.datetime_value is not None and not isinstance(self.datetime_value, XSDDateTime):
            self.datetime_value = XSDDateTime(self.datetime_value)

        if self.marker_event is not None and not isinstance(self.marker_event, EventId):
            self.marker_event = EventId(self.marker_event)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


class ProvenanceComponent(Intangible):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["ProvenanceComponent"]
    class_class_curie: ClassVar[str] = "comet:ProvenanceComponent"
    class_name: ClassVar[str] = "ProvenanceComponent"
    class_model_uri: ClassVar[URIRef] = COMET.ProvenanceComponent


@dataclass(repr=False)
class CreationHistory(ProvenanceComponent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["CreationHistory"]
    class_class_curie: ClassVar[str] = "comet:CreationHistory"
    class_name: ClassVar[str] = "CreationHistory"
    class_model_uri: ClassVar[URIRef] = COMET.CreationHistory

    actions: Optional[Union[Union[dict, "CreationHistoryAction"], List[Union[dict, "CreationHistoryAction"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.actions, list):
            self.actions = [self.actions] if self.actions is not None else []
        self.actions = [v if isinstance(v, CreationHistoryAction) else CreationHistoryAction(**as_dict(v)) for v in self.actions]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CreationHistoryAction(ProvenanceComponent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["CreationHistoryAction"]
    class_class_curie: ClassVar[str] = "comet:CreationHistoryAction"
    class_name: ClassVar[str] = "CreationHistoryAction"
    class_model_uri: ClassVar[URIRef] = COMET.CreationHistoryAction

    description: Optional[str] = None
    roles: Optional[Union[Union[dict, "AgentRole"], List[Union[dict, "AgentRole"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.roles, list):
            self.roles = [self.roles] if self.roles is not None else []
        self.roles = [v if isinstance(v, AgentRole) else AgentRole(**as_dict(v)) for v in self.roles]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AgentRole(ProvenanceComponent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["AgentRole"]
    class_class_curie: ClassVar[str] = "comet:AgentRole"
    class_name: ClassVar[str] = "AgentRole"
    class_model_uri: ClassVar[URIRef] = COMET.AgentRole

    agent: Optional[Union[str, AgentId]] = None
    role: Optional[Union[str, ConceptId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.agent is not None and not isinstance(self.agent, AgentId):
            self.agent = AgentId(self.agent)

        if self.role is not None and not isinstance(self.role, ConceptId):
            self.role = ConceptId(self.role)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CreationMetadata(ProvenanceComponent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["CreationMetadata"]
    class_class_curie: ClassVar[str] = "comet:CreationMetadata"
    class_name: ClassVar[str] = "CreationMetadata"
    class_model_uri: ClassVar[URIRef] = COMET.CreationMetadata

    title: Optional[str] = None
    abstract: Optional[str] = None
    rights: Optional[str] = None
    creators: Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]] = empty_list()
    contributors: Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]] = empty_list()
    contacts: Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]] = empty_list()
    keywords: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.abstract is not None and not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if self.rights is not None and not isinstance(self.rights, str):
            self.rights = str(self.rights)

        if not isinstance(self.creators, list):
            self.creators = [self.creators] if self.creators is not None else []
        self.creators = [v if isinstance(v, AgentId) else AgentId(v) for v in self.creators]

        if not isinstance(self.contributors, list):
            self.contributors = [self.contributors] if self.contributors is not None else []
        self.contributors = [v if isinstance(v, AgentId) else AgentId(v) for v in self.contributors]

        if not isinstance(self.contacts, list):
            self.contacts = [self.contacts] if self.contacts is not None else []
        self.contacts = [v if isinstance(v, AgentId) else AgentId(v) for v in self.contacts]

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Concept(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["Concept"]
    class_class_curie: ClassVar[str] = "comet:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = COMET.Concept

    id: Union[str, ConceptId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConceptId):
            self.id = ConceptId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class UnitConcept(Concept):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["UnitConcept"]
    class_class_curie: ClassVar[str] = "comet:UnitConcept"
    class_name: ClassVar[str] = "UnitConcept"
    class_model_uri: ClassVar[URIRef] = COMET.UnitConcept

    id: Union[str, UnitConceptId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnitConceptId):
            self.id = UnitConceptId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class QuantityKind(Concept):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["QuantityKind"]
    class_class_curie: ClassVar[str] = "comet:QuantityKind"
    class_name: ClassVar[str] = "QuantityKind"
    class_model_uri: ClassVar[URIRef] = COMET.QuantityKind

    id: Union[str, QuantityKindId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantityKindId):
            self.id = QuantityKindId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class AttributeConcept(Concept):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["AttributeConcept"]
    class_class_curie: ClassVar[str] = "comet:AttributeConcept"
    class_name: ClassVar[str] = "AttributeConcept"
    class_model_uri: ClassVar[URIRef] = COMET.AttributeConcept

    id: Union[str, AttributeConceptId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AttributeConceptId):
            self.id = AttributeConceptId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class Variable(Concept):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["Variable"]
    class_class_curie: ClassVar[str] = "comet:Variable"
    class_name: ClassVar[str] = "Variable"
    class_model_uri: ClassVar[URIRef] = COMET.Variable

    id: Union[str, VariableId] = None
    fixed_unit: Optional[Union[str, UnitConceptId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariableId):
            self.id = VariableId(self.id)

        if self.fixed_unit is not None and not isinstance(self.fixed_unit, UnitConceptId):
            self.fixed_unit = UnitConceptId(self.fixed_unit)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class ParticipantInRole(Intangible):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["ParticipantInRole"]
    class_class_curie: ClassVar[str] = "comet:ParticipantInRole"
    class_name: ClassVar[str] = "ParticipantInRole"
    class_model_uri: ClassVar[URIRef] = COMET.ParticipantInRole

    participant: Optional[Union[str, ThingId]] = None
    role: Optional[Union[str, ConceptId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.participant is not None and not isinstance(self.participant, ThingId):
            self.participant = ThingId(self.participant)

        if self.role is not None and not isinstance(self.role, ConceptId):
            self.role = ConceptId(self.role)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Device(InvestigativeEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["Device"]
    class_class_curie: ClassVar[str] = "comet:Device"
    class_name: ClassVar[str] = "Device"
    class_model_uri: ClassVar[URIRef] = COMET.Device

    id: Union[str, DeviceId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class DataObject(InvestigativeEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["DataObject"]
    class_class_curie: ClassVar[str] = "comet:DataObject"
    class_name: ClassVar[str] = "DataObject"
    class_model_uri: ClassVar[URIRef] = COMET.DataObject

    id: Union[str, DataObjectId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataObjectId):
            self.id = DataObjectId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class InvestigationSite(InvestigativeEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["InvestigationSite"]
    class_class_curie: ClassVar[str] = "comet:InvestigationSite"
    class_name: ClassVar[str] = "InvestigationSite"
    class_model_uri: ClassVar[URIRef] = COMET.InvestigationSite

    id: Union[str, InvestigationSiteId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InvestigationSiteId):
            self.id = InvestigationSiteId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class Procedure(InvestigativeEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["Procedure"]
    class_class_curie: ClassVar[str] = "comet:Procedure"
    class_name: ClassVar[str] = "Procedure"
    class_model_uri: ClassVar[URIRef] = COMET.Procedure

    id: Union[str, ProcedureId] = None
    classification: Optional[Union[str, ConceptId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcedureId):
            self.id = ProcedureId(self.id)

        if self.classification is not None and not isinstance(self.classification, ConceptId):
            self.classification = ConceptId(self.classification)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class InvestigativeProtocol(Procedure):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["InvestigativeProtocol"]
    class_class_curie: ClassVar[str] = "comet:InvestigativeProtocol"
    class_name: ClassVar[str] = "InvestigativeProtocol"
    class_model_uri: ClassVar[URIRef] = COMET.InvestigativeProtocol

    id: Union[str, InvestigativeProtocolId] = None
    protocols_io_url: Optional[Union[str, URI]] = None
    classification: Optional[Union[str, ConceptId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InvestigativeProtocolId):
            self.id = InvestigativeProtocolId(self.id)

        if self.protocols_io_url is not None and not isinstance(self.protocols_io_url, URI):
            self.protocols_io_url = URI(self.protocols_io_url)

        if self.classification is not None and not isinstance(self.classification, ConceptId):
            self.classification = ConceptId(self.classification)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class StudyDesign(Procedure):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["StudyDesign"]
    class_class_curie: ClassVar[str] = "comet:StudyDesign"
    class_name: ClassVar[str] = "StudyDesign"
    class_model_uri: ClassVar[URIRef] = COMET.StudyDesign

    id: Union[str, StudyDesignId] = None
    classification: Optional[Union[str, ConceptId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyDesignId):
            self.id = StudyDesignId(self.id)

        if self.classification is not None and not isinstance(self.classification, ConceptId):
            self.classification = ConceptId(self.classification)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class State(Intangible):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["State"]
    class_class_curie: ClassVar[str] = "comet:State"
    class_name: ClassVar[str] = "State"
    class_model_uri: ClassVar[URIRef] = COMET.State

    parameters: Optional[Union[Union[dict, AttributeValue], List[Union[dict, AttributeValue]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.parameters, list):
            self.parameters = [self.parameters] if self.parameters is not None else []
        self.parameters = [v if isinstance(v, AttributeValue) else AttributeValue(**as_dict(v)) for v in self.parameters]

        super().__post_init__(**kwargs)


class ProcedureConfiguration(State):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["ProcedureConfiguration"]
    class_class_curie: ClassVar[str] = "comet:ProcedureConfiguration"
    class_name: ClassVar[str] = "ProcedureConfiguration"
    class_model_uri: ClassVar[URIRef] = COMET.ProcedureConfiguration


@dataclass(repr=False)
class ResultMatrix(Intangible):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["ResultMatrix"]
    class_class_curie: ClassVar[str] = "comet:ResultMatrix"
    class_name: ClassVar[str] = "ResultMatrix"
    class_model_uri: ClassVar[URIRef] = COMET.ResultMatrix

    values: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.values is not None and not isinstance(self.values, float):
            self.values = float(self.values)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(InvestigativeEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["Dataset"]
    class_class_curie: ClassVar[str] = "comet:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = COMET.Dataset

    id: Union[str, DatasetId] = None
    observables: Optional[Union[Dict[Union[str, ObservableId], Union[dict, Observable]], List[Union[dict, Observable]]]] = empty_dict()
    observations: Optional[Union[Dict[Union[str, ObservationId], Union[dict, Observation]], List[Union[dict, Observation]]]] = empty_dict()
    concepts: Optional[Union[Dict[Union[str, ConceptId], Union[dict, Concept]], List[Union[dict, Concept]]]] = empty_dict()
    events: Optional[Union[Dict[Union[str, EventId], Union[dict, Event]], List[Union[dict, Event]]]] = empty_dict()
    investigations: Optional[Union[Dict[Union[str, InvestigationId], Union[dict, Investigation]], List[Union[dict, Investigation]]]] = empty_dict()
    relationships: Optional[Union[Union[dict, Relationship], List[Union[dict, Relationship]]]] = empty_list()
    agents: Optional[Union[Dict[Union[str, AgentId], Union[dict, Agent]], List[Union[dict, Agent]]]] = empty_dict()
    devices: Optional[Union[Dict[Union[str, DeviceId], Union[dict, Device]], List[Union[dict, Device]]]] = empty_dict()
    samples: Optional[Union[Dict[Union[str, SampleId], Union[dict, Sample]], List[Union[dict, Sample]]]] = empty_dict()
    result_matrices: Optional[Union[Union[dict, ResultMatrix], List[Union[dict, ResultMatrix]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        self._normalize_inlined_as_list(slot_name="observables", slot_type=Observable, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="observations", slot_type=Observation, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="concepts", slot_type=Concept, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="events", slot_type=Event, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="investigations", slot_type=Investigation, key_name="id", keyed=True)

        if not isinstance(self.relationships, list):
            self.relationships = [self.relationships] if self.relationships is not None else []
        self.relationships = [v if isinstance(v, Relationship) else Relationship(**as_dict(v)) for v in self.relationships]

        self._normalize_inlined_as_list(slot_name="agents", slot_type=Agent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="devices", slot_type=Device, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="samples", slot_type=Sample, key_name="id", keyed=True)

        if not isinstance(self.result_matrices, list):
            self.result_matrices = [self.result_matrices] if self.result_matrices is not None else []
        self.result_matrices = [v if isinstance(v, ResultMatrix) else ResultMatrix(**as_dict(v)) for v in self.result_matrices]

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class Patient(Observable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Patient"]
    class_class_curie: ClassVar[str] = "linkml_common:Patient"
    class_name: ClassVar[str] = "Patient"
    class_model_uri: ClassVar[URIRef] = COMET.Patient

    id: Union[str, PatientId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PatientId):
            self.id = PatientId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class Cohort(Observable):
    """
    A group of patients with a common characteristic
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["Cohort"]
    class_class_curie: ClassVar[str] = "linkml_common:Cohort"
    class_name: ClassVar[str] = "Cohort"
    class_model_uri: ClassVar[URIRef] = COMET.Cohort

    id: Union[str, CohortId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CohortId):
            self.id = CohortId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class HealthcareSite(InvestigationSite):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["HealthcareSite"]
    class_class_curie: ClassVar[str] = "linkml_common:HealthcareSite"
    class_name: ClassVar[str] = "HealthcareSite"
    class_model_uri: ClassVar[URIRef] = COMET.HealthcareSite

    id: Union[str, HealthcareSiteId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HealthcareSiteId):
            self.id = HealthcareSiteId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class HealthcareEncounter(Event):
    """
    An interaction between a patient and one or more healthcare providers
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["HealthcareEncounter"]
    class_class_curie: ClassVar[str] = "linkml_common:HealthcareEncounter"
    class_name: ClassVar[str] = "HealthcareEncounter"
    class_model_uri: ClassVar[URIRef] = COMET.HealthcareEncounter

    id: Union[str, HealthcareEncounterId] = None
    patient: Optional[Union[str, PatientId]] = None
    provider: Optional[Union[str, HealthcareOrganizationId]] = None
    classification: Optional[Union[str, "HealthcareEncounterClassification"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HealthcareEncounterId):
            self.id = HealthcareEncounterId(self.id)

        if self.patient is not None and not isinstance(self.patient, PatientId):
            self.patient = PatientId(self.patient)

        if self.provider is not None and not isinstance(self.provider, HealthcareOrganizationId):
            self.provider = HealthcareOrganizationId(self.provider)

        if self.classification is not None and not isinstance(self.classification, HealthcareEncounterClassification):
            self.classification = HealthcareEncounterClassification(self.classification)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class HealthcareOrganization(Organization):
    """
    An organization that provides healthcare services
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_COMMON["HealthcareOrganization"]
    class_class_curie: ClassVar[str] = "linkml_common:HealthcareOrganization"
    class_name: ClassVar[str] = "HealthcareOrganization"
    class_model_uri: ClassVar[URIRef] = COMET.HealthcareOrganization

    id: Union[str, HealthcareOrganizationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HealthcareOrganizationId):
            self.id = HealthcareOrganizationId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class EnvironmentalMaterial(Observable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["EnvironmentalMaterial"]
    class_class_curie: ClassVar[str] = "comet:EnvironmentalMaterial"
    class_name: ClassVar[str] = "EnvironmentalMaterial"
    class_model_uri: ClassVar[URIRef] = COMET.EnvironmentalMaterial

    id: Union[str, EnvironmentalMaterialId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalMaterialId):
            self.id = EnvironmentalMaterialId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class Organism(Observable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["Organism"]
    class_class_curie: ClassVar[str] = "comet:Organism"
    class_name: ClassVar[str] = "Organism"
    class_model_uri: ClassVar[URIRef] = COMET.Organism

    id: Union[str, OrganismId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganismId):
            self.id = OrganismId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class OrganismPart(Observable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["OrganismPart"]
    class_class_curie: ClassVar[str] = "comet:OrganismPart"
    class_name: ClassVar[str] = "OrganismPart"
    class_model_uri: ClassVar[URIRef] = COMET.OrganismPart

    id: Union[str, OrganismPartId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganismPartId):
            self.id = OrganismPartId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class OrganismPopulation(Observable):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["OrganismPopulation"]
    class_class_curie: ClassVar[str] = "comet:OrganismPopulation"
    class_name: ClassVar[str] = "OrganismPopulation"
    class_model_uri: ClassVar[URIRef] = COMET.OrganismPopulation

    id: Union[str, OrganismPopulationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganismPopulationId):
            self.id = OrganismPopulationId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


@dataclass(repr=False)
class Microbiome(OrganismPopulation):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMET["Microbiome"]
    class_class_curie: ClassVar[str] = "comet:Microbiome"
    class_name: ClassVar[str] = "Microbiome"
    class_model_uri: ClassVar[URIRef] = COMET.Microbiome

    id: Union[str, MicrobiomeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MicrobiomeId):
            self.id = MicrobiomeId(self.id)

        super().__post_init__(**kwargs)
        self.type = str(self.class_name)


# Enumerations
class RelativeTimeEnum(EnumDefinitionImpl):

    BEFORE = PermissibleValue(text="BEFORE")
    AFTER = PermissibleValue(text="AFTER")
    AT_SAME_TIME_AS = PermissibleValue(text="AT_SAME_TIME_AS")

    _defn = EnumDefinition(
        name="RelativeTimeEnum",
    )

class CaseOrControlEnum(EnumDefinitionImpl):

    CASE = PermissibleValue(
        text="CASE",
        meaning=OBI["0002492"])
    CONTROL = PermissibleValue(
        text="CONTROL",
        meaning=OBI["0002493"])

    _defn = EnumDefinition(
        name="CaseOrControlEnum",
    )

class StudyDesignEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="StudyDesignEnum",
    )

class InvestigativeProtocolEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="InvestigativeProtocolEnum",
    )

class SampleProcessingEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="SampleProcessingEnum",
    )

class PresenceEnum(EnumDefinitionImpl):

    PRESENT = PermissibleValue(
        text="PRESENT",
        description="The entity is present")
    ABSENT = PermissibleValue(
        text="ABSENT",
        description="The entity is absent")
    BELOW_DETECTION_LIMIT = PermissibleValue(
        text="BELOW_DETECTION_LIMIT",
        description="The entity is below the detection limit")
    ABOVE_DETECTION_LIMIT = PermissibleValue(
        text="ABOVE_DETECTION_LIMIT",
        description="The entity is above the detection limit")

    _defn = EnumDefinition(
        name="PresenceEnum",
    )

class HealthcareEncounterClassification(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="HealthcareEncounterClassification",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Inpatient Visit",
            PermissibleValue(
                text="Inpatient Visit",
                description="""Person visiting hospital, at a Care Site, in bed, for duration of more than one day, with physicians and other Providers permanently available to deliver service around the clock"""))
        setattr(cls, "Emergency Room Visit",
            PermissibleValue(
                text="Emergency Room Visit",
                description="""Person visiting dedicated healthcare institution for treating emergencies, at a Care Site, within one day, with physicians and Providers permanently available to deliver service around the clock"""))
        setattr(cls, "Emergency Room and Inpatient Visit",
            PermissibleValue(
                text="Emergency Room and Inpatient Visit",
                description="""Person visiting ER followed by a subsequent Inpatient Visit, where Emergency department is part of hospital, and transition from the ER to other hospital departments is undefined"""))
        setattr(cls, "Non-hospital institution Visit",
            PermissibleValue(
                text="Non-hospital institution Visit",
                description="""Person visiting dedicated institution for reasons of poor health, at a Care Site, long-term or permanently, with no physician but possibly other Providers permanently available to deliver service around the clock"""))
        setattr(cls, "Outpatient Visit",
            PermissibleValue(
                text="Outpatient Visit",
                description="""Person visiting dedicated ambulatory healthcare institution, at a Care Site, within one day, without bed, with physicians or medical Providers delivering service during Visit"""))
        setattr(cls, "Home Visit",
            PermissibleValue(
                text="Home Visit",
                description="Provider visiting Person, without a Care Site, within one day, delivering service"))
        setattr(cls, "Telehealth Visit",
            PermissibleValue(
                text="Telehealth Visit",
                description="Patient engages with Provider through communication media"))
        setattr(cls, "Pharmacy Visit",
            PermissibleValue(
                text="Pharmacy Visit",
                description="Person visiting pharmacy for dispensing of Drug, at a Care Site, within one day"))
        setattr(cls, "Laboratory Visit",
            PermissibleValue(
                text="Laboratory Visit",
                description="""Patient visiting dedicated institution, at a Care Site, within one day, for the purpose of a Measurement."""))
        setattr(cls, "Ambulance Visit",
            PermissibleValue(
                text="Ambulance Visit",
                description="""Person using transportation service for the purpose of initiating one of the other Visits, without a Care Site, within one day, potentially with Providers accompanying the Visit and delivering service"""))
        setattr(cls, "Case Management Visit",
            PermissibleValue(
                text="Case Management Visit",
                description="""Person interacting with healthcare system, without a Care Site, within a day, with no Providers involved, for administrative purposes"""))

class CodeSystemEnum(EnumDefinitionImpl):
    """
    Used to specify why the normally expected content of the data element is missing.
    """
    unknown = PermissibleValue(
        text="unknown",
        description="The value is expected to exist but is not known.",
        meaning=None)
    masked = PermissibleValue(
        text="masked",
        description="The information is not available due to security, privacy or related reasons.",
        meaning=None)
    unsupported = PermissibleValue(
        text="unsupported",
        description="The source system wasn't capable of supporting this element.",
        meaning=None)
    error = PermissibleValue(
        text="error",
        description="Some system or workflow process error means that the information is not available.",
        meaning=None)

    _defn = EnumDefinition(
        name="CodeSystemEnum",
        description="Used to specify why the normally expected content of the data element is missing.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "asked-unknown",
            PermissibleValue(
                text="asked-unknown",
                description="The source was asked but does not know the value.",
                meaning=None))
        setattr(cls, "temp-unknown",
            PermissibleValue(
                text="temp-unknown",
                description="There is reason to expect (from the workflow) that the value may become known.",
                meaning=None))
        setattr(cls, "not-asked",
            PermissibleValue(
                text="not-asked",
                description="The workflow didn't lead to this value being known.",
                meaning=None))
        setattr(cls, "asked-declined",
            PermissibleValue(
                text="asked-declined",
                description="The source was asked but declined to answer.",
                meaning=None))
        setattr(cls, "not-applicable",
            PermissibleValue(
                text="not-applicable",
                description="There is no proper value for this element (e.g. last menstrual period for a male).",
                meaning=None))
        setattr(cls, "as-text",
            PermissibleValue(
                text="as-text",
                description="The content of the data is represented in the resource narrative.",
                meaning=None))
        setattr(cls, "not-a-number",
            PermissibleValue(
                text="not-a-number",
                description="""The numeric value is undefined or unrepresentable due to a floating point processing error.""",
                meaning=None))
        setattr(cls, "negative-infinity",
            PermissibleValue(
                text="negative-infinity",
                description="""The numeric value is excessively low and unrepresentable due to a floating point processing        error.""",
                meaning=None))
        setattr(cls, "positive-infinity",
            PermissibleValue(
                text="positive-infinity",
                description="""The numeric value is excessively high and unrepresentable due to a floating point processing        error.""",
                meaning=None))
        setattr(cls, "not-performed",
            PermissibleValue(
                text="not-performed",
                description="""The value is not available because the observation procedure (test, etc.) was not performed.""",
                meaning=None))
        setattr(cls, "not-permitted",
            PermissibleValue(
                text="not-permitted",
                description="""The value is not permitted in this context (e.g. due to profiles, or the base data types).""",
                meaning=None))

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=COMET.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=COMET.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=COMET.description, domain=None, range=Optional[str])

slots.type = Slot(uri=COMET.type, name="type", curie=COMET.curie('type'),
                   model_uri=COMET.type, domain=None, range=Optional[str])

slots.classification = Slot(uri=COMET.classification, name="classification", curie=COMET.curie('classification'),
                   model_uri=COMET.classification, domain=None, range=Optional[Union[str, ConceptId]])

slots.ontology_types = Slot(uri=COMET.ontology_types, name="ontology_types", curie=COMET.curie('ontology_types'),
                   model_uri=COMET.ontology_types, domain=None, range=Optional[Union[Union[str, ConceptId], List[Union[str, ConceptId]]]])

slots.describes = Slot(uri=SCHEMA.describes, name="describes", curie=SCHEMA.curie('describes'),
                   model_uri=COMET.describes, domain=None, range=Optional[Union[str, ThingId]])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=COMET.subject, domain=None, range=Optional[Union[str, ThingId]])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=COMET.object, domain=None, range=Optional[Union[str, ThingId]])

slots.has_participants = Slot(uri=COMET.has_participants, name="has_participants", curie=COMET.curie('has_participants'),
                   model_uri=COMET.has_participants, domain=None, range=Optional[Union[Union[dict, ParticipantInRole], List[Union[dict, ParticipantInRole]]]])

slots.has_location = Slot(uri=COMET.has_location, name="has_location", curie=COMET.curie('has_location'),
                   model_uri=COMET.has_location, domain=None, range=Optional[Union[dict, Location]])

slots.start_time = Slot(uri=COMET.start_time, name="start_time", curie=COMET.curie('start_time'),
                   model_uri=COMET.start_time, domain=None, range=Optional[Union[dict, TimePoint]])

slots.end_time = Slot(uri=COMET.end_time, name="end_time", curie=COMET.curie('end_time'),
                   model_uri=COMET.end_time, domain=None, range=Optional[Union[dict, TimePoint]])

slots.happens_at = Slot(uri=COMET.happens_at, name="happens_at", curie=COMET.curie('happens_at'),
                   model_uri=COMET.happens_at, domain=None, range=Optional[Union[dict, TimePoint]])

slots.year_value = Slot(uri=COMET.year_value, name="year_value", curie=COMET.curie('year_value'),
                   model_uri=COMET.year_value, domain=None, range=Optional[int])

slots.date_value = Slot(uri=COMET.date_value, name="date_value", curie=COMET.curie('date_value'),
                   model_uri=COMET.date_value, domain=None, range=Optional[Union[str, XSDDate]])

slots.time_value = Slot(uri=COMET.time_value, name="time_value", curie=COMET.curie('time_value'),
                   model_uri=COMET.time_value, domain=None, range=Optional[Union[str, XSDTime]])

slots.datetime_value = Slot(uri=COMET.datetime_value, name="datetime_value", curie=COMET.curie('datetime_value'),
                   model_uri=COMET.datetime_value, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.marker_event = Slot(uri=COMET.marker_event, name="marker_event", curie=COMET.curie('marker_event'),
                   model_uri=COMET.marker_event, domain=None, range=Optional[Union[str, EventId]])

slots.has_time = Slot(uri=COMET.has_time, name="has_time", curie=COMET.curie('has_time'),
                   model_uri=COMET.has_time, domain=None, range=Optional[Union[dict, Duration]])

slots.is_ongoing_as_of = Slot(uri=COMET.is_ongoing_as_of, name="is_ongoing_as_of", curie=COMET.curie('is_ongoing_as_of'),
                   model_uri=COMET.is_ongoing_as_of, domain=None, range=Optional[Union[dict, TimePoint]])

slots.recurring = Slot(uri=COMET.recurring, name="recurring", curie=COMET.curie('recurring'),
                   model_uri=COMET.recurring, domain=None, range=Optional[Union[dict, RecurringTemporalWindow]])

slots.metadata = Slot(uri=COMET.metadata, name="metadata", curie=COMET.curie('metadata'),
                   model_uri=COMET.metadata, domain=None, range=Optional[Union[dict, CreationHistory]])

slots.properties = Slot(uri=COMET.properties, name="properties", curie=COMET.curie('properties'),
                   model_uri=COMET.properties, domain=None, range=Optional[Union[Union[dict, AttributeValue], List[Union[dict, AttributeValue]]]])

slots.observable__properties = Slot(uri=COMET.properties, name="observable__properties", curie=COMET.curie('properties'),
                   model_uri=COMET.observable__properties, domain=None, range=Optional[Union[Union[dict, AttributeValue], List[Union[dict, AttributeValue]]]])

slots.observable__case_or_control = Slot(uri=COMET.case_or_control, name="observable__case_or_control", curie=COMET.curie('case_or_control'),
                   model_uri=COMET.observable__case_or_control, domain=None, range=Optional[Union[str, "CaseOrControlEnum"]])

slots.observation__is_about = Slot(uri=COMET.is_about, name="observation__is_about", curie=COMET.curie('is_about'),
                   model_uri=COMET.observation__is_about, domain=None, range=Optional[Union[str, ObservableId]])

slots.observation__result = Slot(uri=COMET.result, name="observation__result", curie=COMET.curie('result'),
                   model_uri=COMET.observation__result, domain=None, range=Optional[Union[dict, AttributeValue]])

slots.observation__part_of = Slot(uri=COMET.part_of, name="observation__part_of", curie=COMET.curie('part_of'),
                   model_uri=COMET.observation__part_of, domain=None, range=Optional[Union[str, InvestigationId]])

slots.observation__performer = Slot(uri=COMET.performer, name="observation__performer", curie=COMET.curie('performer'),
                   model_uri=COMET.observation__performer, domain=None, range=Optional[Union[str, AgentId]])

slots.observation__method = Slot(uri=COMET.method, name="observation__method", curie=COMET.curie('method'),
                   model_uri=COMET.observation__method, domain=None, range=Optional[Union[str, ConceptId]])

slots.observation__device_used = Slot(uri=COMET.device_used, name="observation__device_used", curie=COMET.curie('device_used'),
                   model_uri=COMET.observation__device_used, domain=None, range=Optional[Union[str, DeviceId]])

slots.observation__procedure_used = Slot(uri=COMET.procedure_used, name="observation__procedure_used", curie=COMET.curie('procedure_used'),
                   model_uri=COMET.observation__procedure_used, domain=None, range=Optional[Union[str, ProcedureId]])

slots.observation__procedure_configuration = Slot(uri=COMET.procedure_configuration, name="observation__procedure_configuration", curie=COMET.curie('procedure_configuration'),
                   model_uri=COMET.observation__procedure_configuration, domain=None, range=Optional[Union[dict, ProcedureConfiguration]])

slots.observation__sample_used = Slot(uri=COMET.sample_used, name="observation__sample_used", curie=COMET.curie('sample_used'),
                   model_uri=COMET.observation__sample_used, domain=None, range=Optional[Union[str, SampleId]])

slots.observation__data_used = Slot(uri=COMET.data_used, name="observation__data_used", curie=COMET.curie('data_used'),
                   model_uri=COMET.observation__data_used, domain=None, range=Optional[Union[str, DataObjectId]])

slots.observation__derived_from = Slot(uri=COMET.derived_from, name="observation__derived_from", curie=COMET.curie('derived_from'),
                   model_uri=COMET.observation__derived_from, domain=None, range=Optional[Union[Union[str, ObservationId], List[Union[str, ObservationId]]]])

slots.attributeValue__attribute = Slot(uri=COMET.attribute, name="attributeValue__attribute", curie=COMET.curie('attribute'),
                   model_uri=COMET.attributeValue__attribute, domain=None, range=Optional[Union[str, AttributeConceptId]])

slots.attributeValue__target = Slot(uri=COMET.target, name="attributeValue__target", curie=COMET.curie('target'),
                   model_uri=COMET.attributeValue__target, domain=None, range=Optional[Union[str, ConceptId]])

slots.attributeValue__numeric_value = Slot(uri=COMET.numeric_value, name="attributeValue__numeric_value", curie=COMET.curie('numeric_value'),
                   model_uri=COMET.attributeValue__numeric_value, domain=None, range=Optional[float])

slots.attributeValue__presence_value = Slot(uri=COMET.presence_value, name="attributeValue__presence_value", curie=COMET.curie('presence_value'),
                   model_uri=COMET.attributeValue__presence_value, domain=None, range=Optional[Union[str, "PresenceEnum"]])

slots.attributeValue__value_range = Slot(uri=COMET.value_range, name="attributeValue__value_range", curie=COMET.curie('value_range'),
                   model_uri=COMET.attributeValue__value_range, domain=None, range=Optional[Union[dict, ValueRange]])

slots.attributeValue__value_series = Slot(uri=COMET.value_series, name="attributeValue__value_series", curie=COMET.curie('value_series'),
                   model_uri=COMET.attributeValue__value_series, domain=None, range=Optional[Union[dict, ValueSeries]])

slots.attributeValue__ratio = Slot(uri=COMET.ratio, name="attributeValue__ratio", curie=COMET.curie('ratio'),
                   model_uri=COMET.attributeValue__ratio, domain=None, range=Optional[Union[dict, Ratio]])

slots.attributeValue__qualitative_value = Slot(uri=COMET.qualitative_value, name="attributeValue__qualitative_value", curie=COMET.curie('qualitative_value'),
                   model_uri=COMET.attributeValue__qualitative_value, domain=None, range=Optional[Union[str, ConceptId]])

slots.attributeValue__unit = Slot(uri=COMET.unit, name="attributeValue__unit", curie=COMET.curie('unit'),
                   model_uri=COMET.attributeValue__unit, domain=None, range=Optional[Union[str, UnitConceptId]])

slots.attributeValue__relative_values = Slot(uri=COMET.relative_values, name="attributeValue__relative_values", curie=COMET.curie('relative_values'),
                   model_uri=COMET.attributeValue__relative_values, domain=None, range=Optional[Union[Union[dict, RelativeValue], List[Union[dict, RelativeValue]]]])

slots.attributeValue__value_absence_reason = Slot(uri=COMET.value_absence_reason, name="attributeValue__value_absence_reason", curie=COMET.curie('value_absence_reason'),
                   model_uri=COMET.attributeValue__value_absence_reason, domain=None, range=Optional[Union[str, ConceptId]])

slots.ratio__numerator = Slot(uri=COMET.numerator, name="ratio__numerator", curie=COMET.curie('numerator'),
                   model_uri=COMET.ratio__numerator, domain=None, range=Optional[Union[dict, AttributeValue]])

slots.ratio__denominator = Slot(uri=COMET.denominator, name="ratio__denominator", curie=COMET.curie('denominator'),
                   model_uri=COMET.ratio__denominator, domain=None, range=Optional[Union[dict, AttributeValue]])

slots.valueRange__lower_bound = Slot(uri=COMET.lower_bound, name="valueRange__lower_bound", curie=COMET.curie('lower_bound'),
                   model_uri=COMET.valueRange__lower_bound, domain=None, range=Optional[float])

slots.valueRange__upper_bound = Slot(uri=COMET.upper_bound, name="valueRange__upper_bound", curie=COMET.curie('upper_bound'),
                   model_uri=COMET.valueRange__upper_bound, domain=None, range=Optional[float])

slots.valueSeries__values = Slot(uri=COMET.values, name="valueSeries__values", curie=COMET.curie('values'),
                   model_uri=COMET.valueSeries__values, domain=None, range=Optional[float])

slots.relativeValue__interpretation = Slot(uri=COMET.interpretation, name="relativeValue__interpretation", curie=COMET.curie('interpretation'),
                   model_uri=COMET.relativeValue__interpretation, domain=None, range=Union[str, ConceptId])

slots.relativeValue__reference = Slot(uri=COMET.reference, name="relativeValue__reference", curie=COMET.curie('reference'),
                   model_uri=COMET.relativeValue__reference, domain=None, range=Optional[Union[str, ConceptId]])

slots.relativeValue__target_value = Slot(uri=COMET.target_value, name="relativeValue__target_value", curie=COMET.curie('target_value'),
                   model_uri=COMET.relativeValue__target_value, domain=None, range=Optional[Union[dict, AttributeValue]])

slots.location__geo_location = Slot(uri=COMET.geo_location, name="location__geo_location", curie=COMET.curie('geo_location'),
                   model_uri=COMET.location__geo_location, domain=None, range=Optional[Union[dict, GeoLocation]])

slots.location__geo_box_location = Slot(uri=COMET.geo_box_location, name="location__geo_box_location", curie=COMET.curie('geo_box_location'),
                   model_uri=COMET.location__geo_box_location, domain=None, range=Optional[Union[dict, GeoBoxLocation]])

slots.location__named_location = Slot(uri=COMET.named_location, name="location__named_location", curie=COMET.curie('named_location'),
                   model_uri=COMET.location__named_location, domain=None, range=Optional[Union[str, ConceptId]])

slots.location__relative_location = Slot(uri=COMET.relative_location, name="location__relative_location", curie=COMET.curie('relative_location'),
                   model_uri=COMET.location__relative_location, domain=None, range=Optional[Union[dict, RelativeLocation]])

slots.location__postal_address = Slot(uri=COMET.postal_address, name="location__postal_address", curie=COMET.curie('postal_address'),
                   model_uri=COMET.location__postal_address, domain=None, range=Optional[Union[dict, PostalAddress]])

slots.geoLocation__latitude = Slot(uri=WGS84.lat, name="geoLocation__latitude", curie=WGS84.curie('lat'),
                   model_uri=COMET.geoLocation__latitude, domain=None, range=Optional[Decimal])

slots.geoLocation__longitude = Slot(uri=WGS84.long, name="geoLocation__longitude", curie=WGS84.curie('long'),
                   model_uri=COMET.geoLocation__longitude, domain=None, range=Optional[Decimal])

slots.geoBoxLocation__west_bounding_coordinate = Slot(uri=COMET.west_bounding_coordinate, name="geoBoxLocation__west_bounding_coordinate", curie=COMET.curie('west_bounding_coordinate'),
                   model_uri=COMET.geoBoxLocation__west_bounding_coordinate, domain=None, range=Optional[Decimal])

slots.geoBoxLocation__east_bounding_coordinate = Slot(uri=COMET.east_bounding_coordinate, name="geoBoxLocation__east_bounding_coordinate", curie=COMET.curie('east_bounding_coordinate'),
                   model_uri=COMET.geoBoxLocation__east_bounding_coordinate, domain=None, range=Optional[Decimal])

slots.geoBoxLocation__north_bounding_coordinate = Slot(uri=COMET.north_bounding_coordinate, name="geoBoxLocation__north_bounding_coordinate", curie=COMET.curie('north_bounding_coordinate'),
                   model_uri=COMET.geoBoxLocation__north_bounding_coordinate, domain=None, range=Optional[Decimal])

slots.geoBoxLocation__south_bounding_coordinate = Slot(uri=COMET.south_bounding_coordinate, name="geoBoxLocation__south_bounding_coordinate", curie=COMET.curie('south_bounding_coordinate'),
                   model_uri=COMET.geoBoxLocation__south_bounding_coordinate, domain=None, range=Optional[Decimal])

slots.relativeLocation__relationship_type = Slot(uri=COMET.relationship_type, name="relativeLocation__relationship_type", curie=COMET.curie('relationship_type'),
                   model_uri=COMET.relativeLocation__relationship_type, domain=None, range=Optional[Union[str, ConceptId]])

slots.relativeLocation__target_location = Slot(uri=COMET.target_location, name="relativeLocation__target_location", curie=COMET.curie('target_location'),
                   model_uri=COMET.relativeLocation__target_location, domain=None, range=Optional[Union[dict, Location]])

slots.postalAddress__street_address = Slot(uri=COMET.street_address, name="postalAddress__street_address", curie=COMET.curie('street_address'),
                   model_uri=COMET.postalAddress__street_address, domain=None, range=Optional[str])

slots.postalAddress__street_address_additional = Slot(uri=COMET.street_address_additional, name="postalAddress__street_address_additional", curie=COMET.curie('street_address_additional'),
                   model_uri=COMET.postalAddress__street_address_additional, domain=None, range=Optional[str])

slots.postalAddress__city = Slot(uri=COMET.city, name="postalAddress__city", curie=COMET.curie('city'),
                   model_uri=COMET.postalAddress__city, domain=None, range=Optional[str])

slots.postalAddress__state = Slot(uri=COMET.state, name="postalAddress__state", curie=COMET.curie('state'),
                   model_uri=COMET.postalAddress__state, domain=None, range=Optional[str])

slots.postalAddress__postal_code = Slot(uri=COMET.postal_code, name="postalAddress__postal_code", curie=COMET.curie('postal_code'),
                   model_uri=COMET.postalAddress__postal_code, domain=None, range=Optional[str])

slots.postalAddress__country = Slot(uri=COMET.country, name="postalAddress__country", curie=COMET.curie('country'),
                   model_uri=COMET.postalAddress__country, domain=None, range=Optional[Union[str, ConceptId]])

slots.investigation__objectives = Slot(uri=COMET.objectives, name="investigation__objectives", curie=COMET.curie('objectives'),
                   model_uri=COMET.investigation__objectives, domain=None, range=Optional[str])

slots.investigation__variables = Slot(uri=COMET.variables, name="investigation__variables", curie=COMET.curie('variables'),
                   model_uri=COMET.investigation__variables, domain=None, range=Optional[Union[Union[str, ConceptId], List[Union[str, ConceptId]]]])

slots.investigation__hypothesis = Slot(uri=COMET.hypothesis, name="investigation__hypothesis", curie=COMET.curie('hypothesis'),
                   model_uri=COMET.investigation__hypothesis, domain=None, range=Optional[Union[str, StudyHypothesisId]])

slots.investigation__design = Slot(uri=COMET.design, name="investigation__design", curie=COMET.curie('design'),
                   model_uri=COMET.investigation__design, domain=None, range=Optional[Union[str, StudyDesignId]])

slots.investigation__results = Slot(uri=COMET.results, name="investigation__results", curie=COMET.curie('results'),
                   model_uri=COMET.investigation__results, domain=None, range=Optional[Union[Union[str, StudyResultId], List[Union[str, StudyResultId]]]])

slots.investigativeProtocol__protocols_io_url = Slot(uri=COMET.protocols_io_url, name="investigativeProtocol__protocols_io_url", curie=COMET.curie('protocols_io_url'),
                   model_uri=COMET.investigativeProtocol__protocols_io_url, domain=None, range=Optional[Union[str, URI]])

slots.studyResult__hypothesis = Slot(uri=COMET.hypothesis, name="studyResult__hypothesis", curie=COMET.curie('hypothesis'),
                   model_uri=COMET.studyResult__hypothesis, domain=None, range=Optional[Union[str, StudyHypothesisId]])

slots.studyResult__results = Slot(uri=COMET.results, name="studyResult__results", curie=COMET.curie('results'),
                   model_uri=COMET.studyResult__results, domain=None, range=Optional[Union[Union[dict, AttributeValue], List[Union[dict, AttributeValue]]]])

slots.relationship__subject = Slot(uri=COMET.subject, name="relationship__subject", curie=COMET.curie('subject'),
                   model_uri=COMET.relationship__subject, domain=None, range=Optional[Union[str, ThingId]])

slots.relationship__predicate = Slot(uri=COMET.predicate, name="relationship__predicate", curie=COMET.curie('predicate'),
                   model_uri=COMET.relationship__predicate, domain=None, range=Optional[Union[str, ConceptId]])

slots.relationship__object = Slot(uri=COMET.object, name="relationship__object", curie=COMET.curie('object'),
                   model_uri=COMET.relationship__object, domain=None, range=Optional[Union[str, ThingId]])

slots.recurringTemporalWindow__enumerated_times = Slot(uri=COMET.enumerated_times, name="recurringTemporalWindow__enumerated_times", curie=COMET.curie('enumerated_times'),
                   model_uri=COMET.recurringTemporalWindow__enumerated_times, domain=None, range=Optional[Union[dict, Duration]])

slots.recurringTemporalWindow__count = Slot(uri=COMET.count, name="recurringTemporalWindow__count", curie=COMET.curie('count'),
                   model_uri=COMET.recurringTemporalWindow__count, domain=None, range=Optional[int])

slots.recurringTemporalWindow__period = Slot(uri=COMET.period, name="recurringTemporalWindow__period", curie=COMET.curie('period'),
                   model_uri=COMET.recurringTemporalWindow__period, domain=None, range=Optional[Union[dict, Duration]])

slots.recurringTemporalWindow__period_unit = Slot(uri=COMET.period_unit, name="recurringTemporalWindow__period_unit", curie=COMET.curie('period_unit'),
                   model_uri=COMET.recurringTemporalWindow__period_unit, domain=None, range=Optional[Union[str, UnitConceptId]])

slots.creationHistory__actions = Slot(uri=COMET.actions, name="creationHistory__actions", curie=COMET.curie('actions'),
                   model_uri=COMET.creationHistory__actions, domain=None, range=Optional[Union[Union[dict, CreationHistoryAction], List[Union[dict, CreationHistoryAction]]]])

slots.creationHistoryAction__description = Slot(uri=COMET.description, name="creationHistoryAction__description", curie=COMET.curie('description'),
                   model_uri=COMET.creationHistoryAction__description, domain=None, range=Optional[str])

slots.creationHistoryAction__roles = Slot(uri=COMET.roles, name="creationHistoryAction__roles", curie=COMET.curie('roles'),
                   model_uri=COMET.creationHistoryAction__roles, domain=None, range=Optional[Union[Union[dict, AgentRole], List[Union[dict, AgentRole]]]])

slots.agentRole__agent = Slot(uri=COMET.agent, name="agentRole__agent", curie=COMET.curie('agent'),
                   model_uri=COMET.agentRole__agent, domain=None, range=Optional[Union[str, AgentId]])

slots.agentRole__role = Slot(uri=COMET.role, name="agentRole__role", curie=COMET.curie('role'),
                   model_uri=COMET.agentRole__role, domain=None, range=Optional[Union[str, ConceptId]])

slots.creationMetadata__title = Slot(uri=COMET.title, name="creationMetadata__title", curie=COMET.curie('title'),
                   model_uri=COMET.creationMetadata__title, domain=None, range=Optional[str])

slots.creationMetadata__abstract = Slot(uri=COMET.abstract, name="creationMetadata__abstract", curie=COMET.curie('abstract'),
                   model_uri=COMET.creationMetadata__abstract, domain=None, range=Optional[str])

slots.creationMetadata__rights = Slot(uri=COMET.rights, name="creationMetadata__rights", curie=COMET.curie('rights'),
                   model_uri=COMET.creationMetadata__rights, domain=None, range=Optional[str])

slots.creationMetadata__creators = Slot(uri=DCTERMS.creator, name="creationMetadata__creators", curie=DCTERMS.curie('creator'),
                   model_uri=COMET.creationMetadata__creators, domain=None, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.creationMetadata__contributors = Slot(uri=DCTERMS.contributor, name="creationMetadata__contributors", curie=DCTERMS.curie('contributor'),
                   model_uri=COMET.creationMetadata__contributors, domain=None, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.creationMetadata__contacts = Slot(uri=SCHEMA.contactPoint, name="creationMetadata__contacts", curie=SCHEMA.curie('contactPoint'),
                   model_uri=COMET.creationMetadata__contacts, domain=None, range=Optional[Union[Union[str, AgentId], List[Union[str, AgentId]]]])

slots.creationMetadata__keywords = Slot(uri=SCHEMA.keywords, name="creationMetadata__keywords", curie=SCHEMA.curie('keywords'),
                   model_uri=COMET.creationMetadata__keywords, domain=None, range=Optional[Union[str, List[str]]])

slots.variable__fixed_unit = Slot(uri=COMET.fixed_unit, name="variable__fixed_unit", curie=COMET.curie('fixed_unit'),
                   model_uri=COMET.variable__fixed_unit, domain=None, range=Optional[Union[str, UnitConceptId]])

slots.participantInRole__participant = Slot(uri=COMET.participant, name="participantInRole__participant", curie=COMET.curie('participant'),
                   model_uri=COMET.participantInRole__participant, domain=None, range=Optional[Union[str, ThingId]])

slots.participantInRole__role = Slot(uri=COMET.role, name="participantInRole__role", curie=COMET.curie('role'),
                   model_uri=COMET.participantInRole__role, domain=None, range=Optional[Union[str, ConceptId]])

slots.state__parameters = Slot(uri=COMET.parameters, name="state__parameters", curie=COMET.curie('parameters'),
                   model_uri=COMET.state__parameters, domain=None, range=Optional[Union[Union[dict, AttributeValue], List[Union[dict, AttributeValue]]]])

slots.resultMatrix__values = Slot(uri=COMET.values, name="resultMatrix__values", curie=COMET.curie('values'),
                   model_uri=COMET.resultMatrix__values, domain=None, range=Optional[float])

slots.dataset__observables = Slot(uri=COMET.observables, name="dataset__observables", curie=COMET.curie('observables'),
                   model_uri=COMET.dataset__observables, domain=None, range=Optional[Union[Dict[Union[str, ObservableId], Union[dict, Observable]], List[Union[dict, Observable]]]])

slots.dataset__observations = Slot(uri=COMET.observations, name="dataset__observations", curie=COMET.curie('observations'),
                   model_uri=COMET.dataset__observations, domain=None, range=Optional[Union[Dict[Union[str, ObservationId], Union[dict, Observation]], List[Union[dict, Observation]]]])

slots.dataset__concepts = Slot(uri=COMET.concepts, name="dataset__concepts", curie=COMET.curie('concepts'),
                   model_uri=COMET.dataset__concepts, domain=None, range=Optional[Union[Dict[Union[str, ConceptId], Union[dict, Concept]], List[Union[dict, Concept]]]])

slots.dataset__events = Slot(uri=COMET.events, name="dataset__events", curie=COMET.curie('events'),
                   model_uri=COMET.dataset__events, domain=None, range=Optional[Union[Dict[Union[str, EventId], Union[dict, Event]], List[Union[dict, Event]]]])

slots.dataset__investigations = Slot(uri=COMET.investigations, name="dataset__investigations", curie=COMET.curie('investigations'),
                   model_uri=COMET.dataset__investigations, domain=None, range=Optional[Union[Dict[Union[str, InvestigationId], Union[dict, Investigation]], List[Union[dict, Investigation]]]])

slots.dataset__relationships = Slot(uri=COMET.relationships, name="dataset__relationships", curie=COMET.curie('relationships'),
                   model_uri=COMET.dataset__relationships, domain=None, range=Optional[Union[Union[dict, Relationship], List[Union[dict, Relationship]]]])

slots.dataset__agents = Slot(uri=COMET.agents, name="dataset__agents", curie=COMET.curie('agents'),
                   model_uri=COMET.dataset__agents, domain=None, range=Optional[Union[Dict[Union[str, AgentId], Union[dict, Agent]], List[Union[dict, Agent]]]])

slots.dataset__devices = Slot(uri=COMET.devices, name="dataset__devices", curie=COMET.curie('devices'),
                   model_uri=COMET.dataset__devices, domain=None, range=Optional[Union[Dict[Union[str, DeviceId], Union[dict, Device]], List[Union[dict, Device]]]])

slots.dataset__samples = Slot(uri=COMET.samples, name="dataset__samples", curie=COMET.curie('samples'),
                   model_uri=COMET.dataset__samples, domain=None, range=Optional[Union[Dict[Union[str, SampleId], Union[dict, Sample]], List[Union[dict, Sample]]]])

slots.dataset__result_matrices = Slot(uri=COMET.result_matrices, name="dataset__result_matrices", curie=COMET.curie('result_matrices'),
                   model_uri=COMET.dataset__result_matrices, domain=None, range=Optional[Union[Union[dict, ResultMatrix], List[Union[dict, ResultMatrix]]]])

slots.healthcareEncounter__patient = Slot(uri=LINKML_COMMON.patient, name="healthcareEncounter__patient", curie=LINKML_COMMON.curie('patient'),
                   model_uri=COMET.healthcareEncounter__patient, domain=None, range=Optional[Union[str, PatientId]])

slots.healthcareEncounter__provider = Slot(uri=LINKML_COMMON.provider, name="healthcareEncounter__provider", curie=LINKML_COMMON.curie('provider'),
                   model_uri=COMET.healthcareEncounter__provider, domain=None, range=Optional[Union[str, HealthcareOrganizationId]])

slots.InvestigativeProtocol_classification = Slot(uri=COMET.classification, name="InvestigativeProtocol_classification", curie=COMET.curie('classification'),
                   model_uri=COMET.InvestigativeProtocol_classification, domain=InvestigativeProtocol, range=Optional[Union[str, ConceptId]])

slots.StudyDesign_classification = Slot(uri=COMET.classification, name="StudyDesign_classification", curie=COMET.curie('classification'),
                   model_uri=COMET.StudyDesign_classification, domain=StudyDesign, range=Optional[Union[str, ConceptId]])

slots.Procedure_classification = Slot(uri=COMET.classification, name="Procedure_classification", curie=COMET.curie('classification'),
                   model_uri=COMET.Procedure_classification, domain=Procedure, range=Optional[Union[str, ConceptId]])

slots.HealthcareEncounter_classification = Slot(uri=COMET.classification, name="HealthcareEncounter_classification", curie=COMET.curie('classification'),
                   model_uri=COMET.HealthcareEncounter_classification, domain=HealthcareEncounter, range=Optional[Union[str, "HealthcareEncounterClassification"]])