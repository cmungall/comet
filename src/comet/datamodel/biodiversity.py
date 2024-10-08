from __future__ import annotations 
from datetime import (
    datetime,
    date
)
from decimal import Decimal 
from enum import Enum 
import re
import sys
from typing import (
    Any,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic.version import VERSION  as PYDANTIC_VERSION 
if int(PYDANTIC_VERSION[0])>=2:
    from pydantic import (
        BaseModel,
        ConfigDict,
        Field,
        field_validator
    )
else:
    from pydantic import (
        BaseModel,
        Field,
        validator
    )

metamodel_version = "None"
version = "None"


class WeakRefShimBaseModel(BaseModel):
    __slots__ = '__weakref__'

class ConfiguredBaseModel(WeakRefShimBaseModel,
                validate_assignment = True,
                validate_all = True,
                underscore_attrs_are_private = True,
                extra = "forbid",
                arbitrary_types_allowed = True,
                use_enum_values = True):
    pass


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


class Identified(ConfiguredBaseModel):
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")


class Typed(ConfiguredBaseModel):
    type: Literal["Typed"] = Field("Typed", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Entity(Typed):
    """
    A physical, digital, conceptual, or other kind of thing with some common characteristics
    """
    type: Literal["Entity"] = Field("Entity", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Event(Entity, Identified):
    """
    A thing that happens
    """
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Event"] = Field("Event", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Observation(Event):
    """
    A statement about the state of something
    """
    observation_subject: Optional[Union[Entity,Event,SubjectHistory,Intangible,PhysicalEntity,PhysicalDevice,SampleMaterial,SetOfObservations,Variable,TimePointOrTemporalInterval,Quantity,QuantityRange,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,PlannedProcessConfiguration,TemporalRelationship,Location,PointLocation,Specification,StudyHypothesis,StudyResult,Procedure,InvestigativeProtocol,StudyDesign,QuantityKind,UnitConcept,Duration,SimpleQuantity,Ratio,TemporalInterval,TimePoint,SubjectObservationHistory,Observation,ExecutionOfProcedure,Investigation,PlannedProcess,ComputationalPlannedProcess,MaterialCollection,MaterialProcessing,InvestigativeProcess,SampleCollectionProcess,DataGenerationFromSample,SampleProcessing,Measurement,QualitativeObservation,OrganismObservation]] = Field(None)
    variable_measured: Optional[Variable] = Field(None, description="""The variable being measured""")
    measured_using: Optional[str] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Observation"] = Field("Observation", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Measurement(Observation):
    quantity_measured: Optional[Union[Quantity,Duration,SimpleQuantity,Ratio]] = Field(None, description="""The quantity being measured""")
    observation_subject: Optional[Union[Entity,Event,SubjectHistory,Intangible,PhysicalEntity,PhysicalDevice,SampleMaterial,SetOfObservations,Variable,TimePointOrTemporalInterval,Quantity,QuantityRange,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,PlannedProcessConfiguration,TemporalRelationship,Location,PointLocation,Specification,StudyHypothesis,StudyResult,Procedure,InvestigativeProtocol,StudyDesign,QuantityKind,UnitConcept,Duration,SimpleQuantity,Ratio,TemporalInterval,TimePoint,SubjectObservationHistory,Observation,ExecutionOfProcedure,Investigation,PlannedProcess,ComputationalPlannedProcess,MaterialCollection,MaterialProcessing,InvestigativeProcess,SampleCollectionProcess,DataGenerationFromSample,SampleProcessing,Measurement,QualitativeObservation,OrganismObservation]] = Field(None)
    variable_measured: Optional[Variable] = Field(None, description="""The variable being measured""")
    measured_using: Optional[str] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Measurement"] = Field("Measurement", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class QualitativeObservation(Observation):
    observation_subject: Optional[Union[Entity,Event,SubjectHistory,Intangible,PhysicalEntity,PhysicalDevice,SampleMaterial,SetOfObservations,Variable,TimePointOrTemporalInterval,Quantity,QuantityRange,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,PlannedProcessConfiguration,TemporalRelationship,Location,PointLocation,Specification,StudyHypothesis,StudyResult,Procedure,InvestigativeProtocol,StudyDesign,QuantityKind,UnitConcept,Duration,SimpleQuantity,Ratio,TemporalInterval,TimePoint,SubjectObservationHistory,Observation,ExecutionOfProcedure,Investigation,PlannedProcess,ComputationalPlannedProcess,MaterialCollection,MaterialProcessing,InvestigativeProcess,SampleCollectionProcess,DataGenerationFromSample,SampleProcessing,Measurement,QualitativeObservation,OrganismObservation]] = Field(None)
    variable_measured: Optional[Variable] = Field(None, description="""The variable being measured""")
    measured_using: Optional[str] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["QualitativeObservation"] = Field("QualitativeObservation", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class SubjectHistory(Entity):
    subject: str = Field(...)
    events: Optional[List[str]] = Field(default_factory=list)
    over_interval: Optional[TemporalInterval] = Field(None)
    type: Literal["SubjectHistory"] = Field("SubjectHistory", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class SubjectObservationHistory(SubjectHistory):
    observations: Optional[List[Union[Observation,Measurement,QualitativeObservation,OrganismObservation]]] = Field(default_factory=list)
    measurements: Optional[List[Measurement]] = Field(default_factory=list)
    interpretations: Optional[List[Union[Observation,Measurement,QualitativeObservation,OrganismObservation]]] = Field(default_factory=list)
    subject: str = Field(...)
    events: Optional[List[str]] = Field(default_factory=list)
    over_interval: Optional[TemporalInterval] = Field(None)
    type: Literal["SubjectObservationHistory"] = Field("SubjectObservationHistory", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Intangible(Entity):
    """
    An entity that is not a physical object, process, or information
    """
    type: Literal["Intangible"] = Field("Intangible", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class SetOfObservations(Intangible):
    observation_subject: Optional[Union[Entity,Event,SubjectHistory,Intangible,PhysicalEntity,PhysicalDevice,SampleMaterial,SetOfObservations,Variable,TimePointOrTemporalInterval,Quantity,QuantityRange,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,PlannedProcessConfiguration,TemporalRelationship,Location,PointLocation,Specification,StudyHypothesis,StudyResult,Procedure,InvestigativeProtocol,StudyDesign,QuantityKind,UnitConcept,Duration,SimpleQuantity,Ratio,TemporalInterval,TimePoint,SubjectObservationHistory,Observation,ExecutionOfProcedure,Investigation,PlannedProcess,ComputationalPlannedProcess,MaterialCollection,MaterialProcessing,InvestigativeProcess,SampleCollectionProcess,DataGenerationFromSample,SampleProcessing,Measurement,QualitativeObservation,OrganismObservation]] = Field(None)
    observations: Optional[Union[Observation,Measurement,QualitativeObservation,OrganismObservation]] = Field(None)
    type: Literal["SetOfObservations"] = Field("SetOfObservations", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Variable(Intangible):
    allowed_units: Optional[List[str]] = Field(default_factory=list, description="""The units that are allowed for this variable""")
    type: Literal["Variable"] = Field("Variable", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class TimePointOrTemporalInterval(Intangible):
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    type: Literal["TimePointOrTemporalInterval"] = Field("TimePointOrTemporalInterval", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class TemporalInterval(TimePointOrTemporalInterval):
    """
    A period of time
    """
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    type: Literal["TemporalInterval"] = Field("TemporalInterval", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class TimePoint(TimePointOrTemporalInterval):
    """
    A point in time. Can be fully specified, or specified in relative terms.
    """
    year_value: Optional[int] = Field(None)
    date_value: Optional[date] = Field(None)
    time_value: Optional[str] = Field(None)
    datetime_value: Optional[datetime ] = Field(None)
    marker_event: Optional[str] = Field(None)
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    type: Literal["TimePoint"] = Field("TimePoint", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Quantity(Intangible):
    has_quantity_kind: Optional[str] = Field(None, description="""The kind of quantity""")
    type: Literal["Quantity"] = Field("Quantity", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Duration(Quantity):
    """
    A length of time
    """
    has_quantity_kind: Optional[str] = Field(None, description="""The kind of quantity""")
    type: Literal["Duration"] = Field("Duration", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class SimpleQuantity(Quantity):
    """
    A quantity is a property that can be measured or counted
    """
    value: Optional[float] = Field(None, description="""The value of the quantity""")
    unit: Optional[str] = Field(None)
    has_quantity_kind: Optional[str] = Field(None, description="""The kind of quantity""")
    type: Literal["SimpleQuantity"] = Field("SimpleQuantity", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Ratio(Quantity):
    """
    A tuple of two quantities
    """
    numerator: Optional[Union[Quantity,Duration,SimpleQuantity,Ratio]] = Field(None, description="""The numerator of the ratio""")
    denominator: Optional[Union[Quantity,Duration,SimpleQuantity,Ratio]] = Field(None, description="""The denominator of the ratio""")
    has_quantity_kind: Optional[str] = Field(None, description="""The kind of quantity""")
    type: Literal["Ratio"] = Field("Ratio", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class QuantityRange(Intangible):
    """
    A quantity range is a property that can be measured or counted
    """
    lower_bound: Optional[Union[Quantity,Duration,SimpleQuantity,Ratio]] = Field(None, description="""The lower bound of the range""")
    upper_bound: Optional[Union[Quantity,Duration,SimpleQuantity,Ratio]] = Field(None, description="""The upper bound of the range""")
    type: Literal["QuantityRange"] = Field("QuantityRange", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class PhysicalEntity(Entity, Identified):
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["PhysicalEntity"] = Field("PhysicalEntity", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Concept(Intangible, Identified):
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Concept"] = Field("Concept", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class QuantityKind(Concept):
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["QuantityKind"] = Field("QuantityKind", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class UnitConcept(Concept):
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["UnitConcept"] = Field("UnitConcept", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class InformationEntity(Intangible, Identified):
    """
    An entity that describes some information
    """
    describes: Optional[Any] = Field(None, description="""The thing that is being described""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["InformationEntity"] = Field("InformationEntity", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class PhysicalDevice(PhysicalEntity):
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["PhysicalDevice"] = Field("PhysicalDevice", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class StructuredValue(Intangible):
    """
    A value that is a structured collection of other values
    """
    type: Literal["StructuredValue"] = Field("StructuredValue", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Role(Intangible):
    type: Literal["Role"] = Field("Role", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Relationship(Intangible):
    subject: Optional[Union[Entity,Event,SubjectHistory,Intangible,PhysicalEntity,PhysicalDevice,SampleMaterial,SetOfObservations,Variable,TimePointOrTemporalInterval,Quantity,QuantityRange,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,PlannedProcessConfiguration,TemporalRelationship,Location,PointLocation,Specification,StudyHypothesis,StudyResult,Procedure,InvestigativeProtocol,StudyDesign,QuantityKind,UnitConcept,Duration,SimpleQuantity,Ratio,TemporalInterval,TimePoint,SubjectObservationHistory,Observation,ExecutionOfProcedure,Investigation,PlannedProcess,ComputationalPlannedProcess,MaterialCollection,MaterialProcessing,InvestigativeProcess,SampleCollectionProcess,DataGenerationFromSample,SampleProcessing,Measurement,QualitativeObservation,OrganismObservation]] = Field(None)
    predicate: Optional[str] = Field(None)
    object: Optional[Union[Entity,Event,SubjectHistory,Intangible,PhysicalEntity,PhysicalDevice,SampleMaterial,SetOfObservations,Variable,TimePointOrTemporalInterval,Quantity,QuantityRange,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,PlannedProcessConfiguration,TemporalRelationship,Location,PointLocation,Specification,StudyHypothesis,StudyResult,Procedure,InvestigativeProtocol,StudyDesign,QuantityKind,UnitConcept,Duration,SimpleQuantity,Ratio,TemporalInterval,TimePoint,SubjectObservationHistory,Observation,ExecutionOfProcedure,Investigation,PlannedProcess,ComputationalPlannedProcess,MaterialCollection,MaterialProcessing,InvestigativeProcess,SampleCollectionProcess,DataGenerationFromSample,SampleProcessing,Measurement,QualitativeObservation,OrganismObservation]] = Field(None)
    type: Literal["Relationship"] = Field("Relationship", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class TemporalRelationship(Relationship):
    """
    A relationship to another time point
    """
    predicate: Optional[RelativeTimeEnum] = Field(None, description="""The relationship between the two time points""")
    relative_to: Optional[Union[TemporalInterval, TimePoint, str]] = Field(None)
    subject: Optional[Union[Entity,Event,SubjectHistory,Intangible,PhysicalEntity,PhysicalDevice,SampleMaterial,SetOfObservations,Variable,TimePointOrTemporalInterval,Quantity,QuantityRange,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,PlannedProcessConfiguration,TemporalRelationship,Location,PointLocation,Specification,StudyHypothesis,StudyResult,Procedure,InvestigativeProtocol,StudyDesign,QuantityKind,UnitConcept,Duration,SimpleQuantity,Ratio,TemporalInterval,TimePoint,SubjectObservationHistory,Observation,ExecutionOfProcedure,Investigation,PlannedProcess,ComputationalPlannedProcess,MaterialCollection,MaterialProcessing,InvestigativeProcess,SampleCollectionProcess,DataGenerationFromSample,SampleProcessing,Measurement,QualitativeObservation,OrganismObservation]] = Field(None)
    object: Optional[Union[Entity,Event,SubjectHistory,Intangible,PhysicalEntity,PhysicalDevice,SampleMaterial,SetOfObservations,Variable,TimePointOrTemporalInterval,Quantity,QuantityRange,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,PlannedProcessConfiguration,TemporalRelationship,Location,PointLocation,Specification,StudyHypothesis,StudyResult,Procedure,InvestigativeProtocol,StudyDesign,QuantityKind,UnitConcept,Duration,SimpleQuantity,Ratio,TemporalInterval,TimePoint,SubjectObservationHistory,Observation,ExecutionOfProcedure,Investigation,PlannedProcess,ComputationalPlannedProcess,MaterialCollection,MaterialProcessing,InvestigativeProcess,SampleCollectionProcess,DataGenerationFromSample,SampleProcessing,Measurement,QualitativeObservation,OrganismObservation]] = Field(None)
    type: Literal["TemporalRelationship"] = Field("TemporalRelationship", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Location(StructuredValue):
    type: Literal["Location"] = Field("Location", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class PointLocation(Location):
    type: Literal["PointLocation"] = Field("PointLocation", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Specification(InformationEntity):
    """
    A specification of a thing
    """
    describes: Optional[Any] = Field(None, description="""The thing that is being described""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Specification"] = Field("Specification", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Procedure(Specification):
    """
    A canonical series of actions conducted in a certain order or manner
    """
    describes: Optional[Any] = Field(None, description="""The thing that is being described""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Procedure"] = Field("Procedure", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class EntitySet(Intangible):
    """
    A group of things. The collection may be heterogeneous or homogeneous.
    """
    members: Optional[List[Union[Entity,Event,SubjectHistory,Intangible,PhysicalEntity,PhysicalDevice,SampleMaterial,SetOfObservations,Variable,TimePointOrTemporalInterval,Quantity,QuantityRange,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,PlannedProcessConfiguration,TemporalRelationship,Location,PointLocation,Specification,StudyHypothesis,StudyResult,Procedure,InvestigativeProtocol,StudyDesign,QuantityKind,UnitConcept,Duration,SimpleQuantity,Ratio,TemporalInterval,TimePoint,SubjectObservationHistory,Observation,ExecutionOfProcedure,Investigation,PlannedProcess,ComputationalPlannedProcess,MaterialCollection,MaterialProcessing,InvestigativeProcess,SampleCollectionProcess,DataGenerationFromSample,SampleProcessing,Measurement,QualitativeObservation,OrganismObservation]]] = Field(default_factory=list, description="""The members of the collection""")
    type: Literal["EntitySet"] = Field("EntitySet", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class ExecutionOfProcedure(Event):
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["ExecutionOfProcedure"] = Field("ExecutionOfProcedure", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class PlannedProcessConfiguration(Intangible):
    type: Literal["PlannedProcessConfiguration"] = Field("PlannedProcessConfiguration", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class PlannedProcess(ExecutionOfProcedure):
    """
    A process that follows a defined procedure or plan
    """
    follows_procedure: Optional[str] = Field(None)
    uses_physical_device: Optional[str] = Field(None)
    uses_configuration: Optional[PlannedProcessConfiguration] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["PlannedProcess"] = Field("PlannedProcess", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class ComputationalPlannedProcess(PlannedProcess):
    """
    Application of a mathematical operation to one or more inputs to produce one or more outputs
    """
    inputs: Optional[List[Any]] = Field(default_factory=list, description="""The inputs to the operation""")
    outputs: Optional[List[Any]] = Field(default_factory=list, description="""The outputs of the operation""")
    parts: Optional[List[str]] = Field(default_factory=list, description="""The parts of the process""")
    immediate_preceding_steps: Optional[List[str]] = Field(default_factory=list, description="""The steps that immediately precede this step""")
    follows_procedure: Optional[str] = Field(None)
    uses_physical_device: Optional[str] = Field(None)
    uses_configuration: Optional[PlannedProcessConfiguration] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["ComputationalPlannedProcess"] = Field("ComputationalPlannedProcess", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class MaterialCollection(PlannedProcess):
    follows_procedure: Optional[str] = Field(None)
    uses_physical_device: Optional[str] = Field(None)
    uses_configuration: Optional[PlannedProcessConfiguration] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["MaterialCollection"] = Field("MaterialCollection", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class MaterialProcessing(PlannedProcess):
    follows_procedure: Optional[str] = Field(None)
    uses_physical_device: Optional[str] = Field(None)
    uses_configuration: Optional[PlannedProcessConfiguration] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["MaterialProcessing"] = Field("MaterialProcessing", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class Investigation(Event):
    objectives: Optional[str] = Field(None)
    variables: Optional[List[Variable]] = Field(default_factory=list)
    hypothesis: Optional[str] = Field(None)
    design: Optional[str] = Field(None)
    results: Optional[List[str]] = Field(default_factory=list)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["Investigation"] = Field("Investigation", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class InvestigativeProtocol(Procedure):
    protocols_io_url: Optional[str] = Field(None)
    describes: Optional[Any] = Field(None, description="""The thing that is being described""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["InvestigativeProtocol"] = Field("InvestigativeProtocol", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class StudyHypothesis(InformationEntity):
    describes: Optional[Any] = Field(None, description="""The thing that is being described""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["StudyHypothesis"] = Field("StudyHypothesis", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class StudyDesign(Procedure):
    describes: Optional[Any] = Field(None, description="""The thing that is being described""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["StudyDesign"] = Field("StudyDesign", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class StudyResult(InformationEntity):
    hypothesis: Optional[str] = Field(None)
    result: Optional[str] = Field(None)
    describes: Optional[Any] = Field(None, description="""The thing that is being described""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["StudyResult"] = Field("StudyResult", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class SampleMaterial(PhysicalEntity):
    classification: Optional[str] = Field(None, description="""A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.""")
    ontology_types: Optional[List[str]] = Field(default_factory=list, description="""A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.""")
    description: Optional[str] = Field(None, description="""A human-readable description for a thing""")
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["SampleMaterial"] = Field("SampleMaterial", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class InvestigativeProcess(PlannedProcess):
    follows_procedure: Optional[str] = Field(None)
    part_of: Optional[str] = Field(None)
    uses_physical_device: Optional[str] = Field(None)
    uses_configuration: Optional[PlannedProcessConfiguration] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["InvestigativeProcess"] = Field("InvestigativeProcess", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class SampleCollectionProcess(InvestigativeProcess):
    material_collected: Optional[str] = Field(None)
    collected_from: Optional[str] = Field(None)
    follows_procedure: Optional[str] = Field(None)
    part_of: Optional[str] = Field(None)
    uses_physical_device: Optional[str] = Field(None)
    uses_configuration: Optional[PlannedProcessConfiguration] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["SampleCollectionProcess"] = Field("SampleCollectionProcess", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class SampleProcessing(MaterialProcessing):
    follows_procedure: Optional[str] = Field(None)
    uses_physical_device: Optional[str] = Field(None)
    uses_configuration: Optional[PlannedProcessConfiguration] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["SampleProcessing"] = Field("SampleProcessing", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class DataGenerationFromSample(InvestigativeProcess):
    follows_procedure: Optional[str] = Field(None)
    part_of: Optional[str] = Field(None)
    uses_physical_device: Optional[str] = Field(None)
    uses_configuration: Optional[PlannedProcessConfiguration] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["DataGenerationFromSample"] = Field("DataGenerationFromSample", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


class OrganismObservation(Observation):
    observation_subject: Optional[Union[Entity,Event,SubjectHistory,Intangible,PhysicalEntity,PhysicalDevice,SampleMaterial,SetOfObservations,Variable,TimePointOrTemporalInterval,Quantity,QuantityRange,Concept,InformationEntity,StructuredValue,Role,Relationship,EntitySet,PlannedProcessConfiguration,TemporalRelationship,Location,PointLocation,Specification,StudyHypothesis,StudyResult,Procedure,InvestigativeProtocol,StudyDesign,QuantityKind,UnitConcept,Duration,SimpleQuantity,Ratio,TemporalInterval,TimePoint,SubjectObservationHistory,Observation,ExecutionOfProcedure,Investigation,PlannedProcess,ComputationalPlannedProcess,MaterialCollection,MaterialProcessing,InvestigativeProcess,SampleCollectionProcess,DataGenerationFromSample,SampleProcessing,Measurement,QualitativeObservation,OrganismObservation]] = Field(None)
    variable_measured: Optional[Variable] = Field(None, description="""The variable being measured""")
    measured_using: Optional[str] = Field(None)
    starts_at: Optional[TimePoint] = Field(None)
    ends_at: Optional[TimePoint] = Field(None)
    happens_at: Optional[TimePoint] = Field(None)
    has_interval: Optional[TemporalInterval] = Field(None)
    has_duration: Optional[Duration] = Field(None)
    is_ongoing_as_of: Optional[TimePoint] = Field(None)
    id: str = Field(..., description="""A unique identifier for a thing""")
    name: Optional[str] = Field(None, description="""A human-readable name for a thing""")
    type: Literal["OrganismObservation"] = Field("OrganismObservation", description="""A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.""")


# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
Identified.update_forward_refs()
Typed.update_forward_refs()
Entity.update_forward_refs()
Event.update_forward_refs()
Observation.update_forward_refs()
Measurement.update_forward_refs()
QualitativeObservation.update_forward_refs()
SubjectHistory.update_forward_refs()
SubjectObservationHistory.update_forward_refs()
Intangible.update_forward_refs()
SetOfObservations.update_forward_refs()
Variable.update_forward_refs()
TimePointOrTemporalInterval.update_forward_refs()
TemporalInterval.update_forward_refs()
TimePoint.update_forward_refs()
Quantity.update_forward_refs()
Duration.update_forward_refs()
SimpleQuantity.update_forward_refs()
Ratio.update_forward_refs()
QuantityRange.update_forward_refs()
PhysicalEntity.update_forward_refs()
Concept.update_forward_refs()
QuantityKind.update_forward_refs()
UnitConcept.update_forward_refs()
InformationEntity.update_forward_refs()
PhysicalDevice.update_forward_refs()
StructuredValue.update_forward_refs()
Role.update_forward_refs()
Relationship.update_forward_refs()
TemporalRelationship.update_forward_refs()
Location.update_forward_refs()
PointLocation.update_forward_refs()
Specification.update_forward_refs()
Procedure.update_forward_refs()
EntitySet.update_forward_refs()
ExecutionOfProcedure.update_forward_refs()
PlannedProcessConfiguration.update_forward_refs()
PlannedProcess.update_forward_refs()
ComputationalPlannedProcess.update_forward_refs()
MaterialCollection.update_forward_refs()
MaterialProcessing.update_forward_refs()
Investigation.update_forward_refs()
InvestigativeProtocol.update_forward_refs()
StudyHypothesis.update_forward_refs()
StudyDesign.update_forward_refs()
StudyResult.update_forward_refs()
SampleMaterial.update_forward_refs()
InvestigativeProcess.update_forward_refs()
SampleCollectionProcess.update_forward_refs()
SampleProcessing.update_forward_refs()
DataGenerationFromSample.update_forward_refs()
OrganismObservation.update_forward_refs()

