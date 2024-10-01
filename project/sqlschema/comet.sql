-- # Class: "Thing" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "Intangible" Description: ""
--     * Slot: id Description: 
-- # Class: "DomainEntity" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "InvestigativeEntity" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "Observable" Description: "A concrete or abstract entity that has been observed or measured. Examples include a person, a region of the earth, a cell type, a tree, a mountain."
--     * Slot: case_or_control Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "Observation" Description: ""
--     * Slot: is_about Description: 
--     * Slot: part_of Description: 
--     * Slot: performer Description: 
--     * Slot: method Description: 
--     * Slot: device_used Description: 
--     * Slot: procedure_used Description: 
--     * Slot: sample_used Description: 
--     * Slot: data_used Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: has_time_id Description: 
--     * Slot: result_id Description: 
--     * Slot: procedure_configuration_id Description: 
--     * Slot: has_location_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "StructuredValueComponent" Description: ""
--     * Slot: id Description: 
-- # Class: "AttributeValue" Description: ""
--     * Slot: id Description: 
--     * Slot: attribute Description: 
--     * Slot: target Description: 
--     * Slot: numeric_value Description: The numeric value of the observation
--     * Slot: presence_value Description: 
--     * Slot: qualitative_value Description: A qualitative value
--     * Slot: unit Description: 
--     * Slot: value_absence_reason Description: The reason for the absence of a value
--     * Slot: Observable_id Description: Autocreated FK slot
--     * Slot: Event_id Description: Autocreated FK slot
--     * Slot: Sample_id Description: Autocreated FK slot
--     * Slot: State_id Description: Autocreated FK slot
--     * Slot: ProcedureConfiguration_id Description: Autocreated FK slot
--     * Slot: EnvironmentalMaterial_id Description: Autocreated FK slot
--     * Slot: Organism_id Description: Autocreated FK slot
--     * Slot: OrganismPart_id Description: Autocreated FK slot
--     * Slot: OrganismPopulation_id Description: Autocreated FK slot
--     * Slot: Microbiome_id Description: Autocreated FK slot
--     * Slot: Patient_id Description: Autocreated FK slot
--     * Slot: Cohort_id Description: Autocreated FK slot
--     * Slot: HealthcareEncounter_id Description: Autocreated FK slot
--     * Slot: value_range_id Description: The range of the value
--     * Slot: value_series_id Description: A series of values
--     * Slot: ratio_id Description: The ratio of the value
-- # Class: "Ratio" Description: "A tuple of two quantities"
--     * Slot: id Description: 
--     * Slot: numerator_id Description: The numerator of the ratio
--     * Slot: denominator_id Description: The denominator of the ratio
-- # Class: "ValueRange" Description: "A quantity range is a property that can be measured or counted"
--     * Slot: id Description: 
--     * Slot: lower_bound Description: The lower bound of the range
--     * Slot: upper_bound Description: The upper bound of the range
-- # Class: "ValueSeries" Description: "A series of values"
--     * Slot: id Description: 
--     * Slot: values Description: 
-- # Class: "RelativeValue" Description: "A value that is relative to another value"
--     * Slot: id Description: 
--     * Slot: interpretation Description: The type of relationship, e.g. high
--     * Slot: reference Description: 
--     * Slot: AttributeValue_id Description: Autocreated FK slot
--     * Slot: target_value_id Description: The target value
-- # Class: "Event" Description: "A thing that happens to and potentially causally influences one of more participants."
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: has_time_id Description: 
--     * Slot: has_location_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "LocationComponent" Description: ""
--     * Slot: id Description: 
-- # Class: "Location" Description: ""
--     * Slot: id Description: 
--     * Slot: named_location Description: 
--     * Slot: geo_location_id Description: A string representation of a geolocation
--     * Slot: geo_box_location_id Description: A string representation of a geobox location
--     * Slot: relative_location_id Description: 
--     * Slot: postal_address_id Description: A postal address
-- # Class: "GeoLocation" Description: ""
--     * Slot: id Description: 
--     * Slot: latitude Description: 
--     * Slot: longitude Description: 
-- # Class: "GeoBoxLocation" Description: ""
--     * Slot: id Description: 
--     * Slot: west_bounding_coordinate Description: The westernmost coordinate of the location
--     * Slot: east_bounding_coordinate Description: The easternmost coordinate of the location
--     * Slot: north_bounding_coordinate Description: The northernmost coordinate of the location
--     * Slot: south_bounding_coordinate Description: The southernmost coordinate of the location
-- # Class: "RelativeLocation" Description: ""
--     * Slot: id Description: 
--     * Slot: relationship_type Description: 
--     * Slot: target_location_id Description: 
-- # Class: "PostalAddress" Description: "Represents an Address"
--     * Slot: id Description: 
--     * Slot: street_address Description: The street address
--     * Slot: street_address_additional Description: 
--     * Slot: city Description: The city
--     * Slot: state Description: The state
--     * Slot: postal_code Description: The postal code or zip code
--     * Slot: country Description: The country
-- # Class: "Sample" Description: ""
--     * Slot: case_or_control Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "Investigation" Description: ""
--     * Slot: objectives Description: 
--     * Slot: hypothesis Description: 
--     * Slot: design Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: has_time_id Description: 
--     * Slot: has_location_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "InformationEntity" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "InvestigativeProtocol" Description: ""
--     * Slot: protocols_io_url Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "StudyDesign" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "StudyResult" Description: ""
--     * Slot: hypothesis Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "StudyHypothesis" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "Agent" Description: "Represents an Agent"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "Organization" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "Relationship" Description: ""
--     * Slot: id Description: 
--     * Slot: subject Description: 
--     * Slot: predicate Description: 
--     * Slot: object Description: 
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: has_time_id Description: 
-- # Class: "Temporal" Description: ""
--     * Slot: id Description: 
-- # Class: "Duration" Description: ""
--     * Slot: id Description: 
--     * Slot: start_time_id Description: 
--     * Slot: end_time_id Description: 
--     * Slot: happens_at_id Description: 
--     * Slot: is_ongoing_as_of_id Description: 
--     * Slot: recurring_id Description: 
-- # Class: "RecurringTemporalWindow" Description: ""
--     * Slot: id Description: 
--     * Slot: count Description: 
--     * Slot: period_unit Description: 
--     * Slot: enumerated_times_id Description: 
--     * Slot: period_id Description: 
-- # Class: "TimePoint" Description: "A point in time. Can be fully specified, or specified in relative terms."
--     * Slot: id Description: 
--     * Slot: year_value Description: 
--     * Slot: date_value Description: 
--     * Slot: time_value Description: 
--     * Slot: datetime_value Description: 
--     * Slot: marker_event Description: 
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "ProvenanceComponent" Description: ""
--     * Slot: id Description: 
-- # Class: "CreationHistory" Description: ""
--     * Slot: id Description: 
-- # Class: "CreationHistoryAction" Description: ""
--     * Slot: id Description: 
--     * Slot: description Description: 
--     * Slot: CreationHistory_id Description: Autocreated FK slot
-- # Class: "AgentRole" Description: ""
--     * Slot: id Description: 
--     * Slot: agent Description: 
--     * Slot: role Description: 
-- # Class: "CreationMetadata" Description: ""
--     * Slot: id Description: 
--     * Slot: title Description: The title of the item
--     * Slot: abstract Description: A summary of the item
--     * Slot: rights Description: Information about rights held in and over the item
-- # Class: "Concept" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "UnitConcept" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "QuantityKind" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "AttributeConcept" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "Variable" Description: ""
--     * Slot: fixed_unit Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "ParticipantInRole" Description: ""
--     * Slot: id Description: 
--     * Slot: participant Description: 
--     * Slot: role Description: 
-- # Class: "Device" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "DataObject" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "InvestigationSite" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "Procedure" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "State" Description: ""
--     * Slot: id Description: 
-- # Class: "ProcedureConfiguration" Description: ""
--     * Slot: id Description: 
-- # Class: "ResultMatrix" Description: ""
--     * Slot: id Description: 
--     * Slot: values Description: 
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: "Dataset" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "EnvironmentalMaterial" Description: ""
--     * Slot: case_or_control Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "Organism" Description: ""
--     * Slot: case_or_control Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "OrganismPart" Description: ""
--     * Slot: case_or_control Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "OrganismPopulation" Description: ""
--     * Slot: case_or_control Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "Microbiome" Description: ""
--     * Slot: case_or_control Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "Patient" Description: ""
--     * Slot: case_or_control Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "Cohort" Description: "A group of patients with a common characteristic"
--     * Slot: case_or_control Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "HealthcareSite" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "HealthcareEncounter" Description: "An interaction between a patient and one or more healthcare providers"
--     * Slot: patient Description: 
--     * Slot: provider Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_time_id Description: 
--     * Slot: has_location_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "HealthcareOrganization" Description: "An organization that provides healthcare services"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: has_location_id Description: 
--     * Slot: has_time_id Description: 
--     * Slot: metadata_id Description: 
-- # Class: "Thing_ontology_types" Description: ""
--     * Slot: Thing_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "DomainEntity_ontology_types" Description: ""
--     * Slot: DomainEntity_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "InvestigativeEntity_ontology_types" Description: ""
--     * Slot: InvestigativeEntity_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Observable_ontology_types" Description: ""
--     * Slot: Observable_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Observation_derived_from" Description: ""
--     * Slot: Observation_id Description: Autocreated FK slot
--     * Slot: derived_from_id Description: 
-- # Class: "Observation_ontology_types" Description: ""
--     * Slot: Observation_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Event_has_participants" Description: ""
--     * Slot: Event_id Description: Autocreated FK slot
--     * Slot: has_participants_id Description: 
-- # Class: "Event_ontology_types" Description: ""
--     * Slot: Event_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Sample_ontology_types" Description: ""
--     * Slot: Sample_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Investigation_variables" Description: ""
--     * Slot: Investigation_id Description: Autocreated FK slot
--     * Slot: variables_id Description: 
-- # Class: "Investigation_results" Description: ""
--     * Slot: Investigation_id Description: Autocreated FK slot
--     * Slot: results_id Description: 
-- # Class: "Investigation_ontology_types" Description: ""
--     * Slot: Investigation_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "InformationEntity_ontology_types" Description: ""
--     * Slot: InformationEntity_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "InvestigativeProtocol_ontology_types" Description: ""
--     * Slot: InvestigativeProtocol_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "StudyDesign_ontology_types" Description: ""
--     * Slot: StudyDesign_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "StudyResult_results" Description: ""
--     * Slot: StudyResult_id Description: Autocreated FK slot
--     * Slot: results_id Description: 
-- # Class: "StudyResult_ontology_types" Description: ""
--     * Slot: StudyResult_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "StudyHypothesis_ontology_types" Description: ""
--     * Slot: StudyHypothesis_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Agent_ontology_types" Description: ""
--     * Slot: Agent_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Organization_ontology_types" Description: ""
--     * Slot: Organization_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "CreationHistoryAction_roles" Description: ""
--     * Slot: CreationHistoryAction_id Description: Autocreated FK slot
--     * Slot: roles_id Description: 
-- # Class: "CreationMetadata_creators" Description: ""
--     * Slot: CreationMetadata_id Description: Autocreated FK slot
--     * Slot: creators_id Description: The person or organization who created the work
-- # Class: "CreationMetadata_contributors" Description: ""
--     * Slot: CreationMetadata_id Description: Autocreated FK slot
--     * Slot: contributors_id Description: A person or organization that contributed to the creation of the work
-- # Class: "CreationMetadata_contacts" Description: ""
--     * Slot: CreationMetadata_id Description: Autocreated FK slot
--     * Slot: contacts_id Description: A contact point for a person or organization
-- # Class: "CreationMetadata_keywords" Description: ""
--     * Slot: CreationMetadata_id Description: Autocreated FK slot
--     * Slot: keywords Description: Keywords or tags used to describe this item
-- # Class: "Concept_ontology_types" Description: ""
--     * Slot: Concept_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "UnitConcept_ontology_types" Description: ""
--     * Slot: UnitConcept_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "QuantityKind_ontology_types" Description: ""
--     * Slot: QuantityKind_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "AttributeConcept_ontology_types" Description: ""
--     * Slot: AttributeConcept_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Variable_ontology_types" Description: ""
--     * Slot: Variable_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Device_ontology_types" Description: ""
--     * Slot: Device_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "DataObject_ontology_types" Description: ""
--     * Slot: DataObject_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "InvestigationSite_ontology_types" Description: ""
--     * Slot: InvestigationSite_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Procedure_ontology_types" Description: ""
--     * Slot: Procedure_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Dataset_ontology_types" Description: ""
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "EnvironmentalMaterial_ontology_types" Description: ""
--     * Slot: EnvironmentalMaterial_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Organism_ontology_types" Description: ""
--     * Slot: Organism_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "OrganismPart_ontology_types" Description: ""
--     * Slot: OrganismPart_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "OrganismPopulation_ontology_types" Description: ""
--     * Slot: OrganismPopulation_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Microbiome_ontology_types" Description: ""
--     * Slot: Microbiome_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Patient_ontology_types" Description: ""
--     * Slot: Patient_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Cohort_ontology_types" Description: ""
--     * Slot: Cohort_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "HealthcareSite_ontology_types" Description: ""
--     * Slot: HealthcareSite_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "HealthcareEncounter_has_participants" Description: ""
--     * Slot: HealthcareEncounter_id Description: Autocreated FK slot
--     * Slot: has_participants_id Description: 
-- # Class: "HealthcareEncounter_ontology_types" Description: ""
--     * Slot: HealthcareEncounter_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "HealthcareOrganization_ontology_types" Description: ""
--     * Slot: HealthcareOrganization_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.

CREATE TABLE "Intangible" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "StructuredValueComponent" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "AttributeValue" (
	id INTEGER NOT NULL, 
	attribute TEXT, 
	target TEXT, 
	numeric_value FLOAT, 
	presence_value VARCHAR(21), 
	qualitative_value TEXT, 
	unit TEXT, 
	value_absence_reason TEXT, 
	"Observable_id" TEXT, 
	"Event_id" TEXT, 
	"Sample_id" TEXT, 
	"State_id" INTEGER, 
	"ProcedureConfiguration_id" INTEGER, 
	"EnvironmentalMaterial_id" TEXT, 
	"Organism_id" TEXT, 
	"OrganismPart_id" TEXT, 
	"OrganismPopulation_id" TEXT, 
	"Microbiome_id" TEXT, 
	"Patient_id" TEXT, 
	"Cohort_id" TEXT, 
	"HealthcareEncounter_id" TEXT, 
	value_range_id INTEGER, 
	value_series_id INTEGER, 
	ratio_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(attribute) REFERENCES "AttributeConcept" (id), 
	FOREIGN KEY(target) REFERENCES "Concept" (id), 
	FOREIGN KEY(qualitative_value) REFERENCES "Concept" (id), 
	FOREIGN KEY(unit) REFERENCES "UnitConcept" (id), 
	FOREIGN KEY(value_absence_reason) REFERENCES "Concept" (id), 
	FOREIGN KEY("Observable_id") REFERENCES "Observable" (id), 
	FOREIGN KEY("Event_id") REFERENCES "Event" (id), 
	FOREIGN KEY("Sample_id") REFERENCES "Sample" (id), 
	FOREIGN KEY("State_id") REFERENCES "State" (id), 
	FOREIGN KEY("ProcedureConfiguration_id") REFERENCES "ProcedureConfiguration" (id), 
	FOREIGN KEY("EnvironmentalMaterial_id") REFERENCES "EnvironmentalMaterial" (id), 
	FOREIGN KEY("Organism_id") REFERENCES "Organism" (id), 
	FOREIGN KEY("OrganismPart_id") REFERENCES "OrganismPart" (id), 
	FOREIGN KEY("OrganismPopulation_id") REFERENCES "OrganismPopulation" (id), 
	FOREIGN KEY("Microbiome_id") REFERENCES "Microbiome" (id), 
	FOREIGN KEY("Patient_id") REFERENCES "Patient" (id), 
	FOREIGN KEY("Cohort_id") REFERENCES "Cohort" (id), 
	FOREIGN KEY("HealthcareEncounter_id") REFERENCES "HealthcareEncounter" (id), 
	FOREIGN KEY(value_range_id) REFERENCES "ValueRange" (id), 
	FOREIGN KEY(value_series_id) REFERENCES "ValueSeries" (id), 
	FOREIGN KEY(ratio_id) REFERENCES "Ratio" (id)
);
CREATE TABLE "Ratio" (
	id INTEGER NOT NULL, 
	numerator_id INTEGER, 
	denominator_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(numerator_id) REFERENCES "AttributeValue" (id), 
	FOREIGN KEY(denominator_id) REFERENCES "AttributeValue" (id)
);
CREATE TABLE "ValueRange" (
	id INTEGER NOT NULL, 
	lower_bound FLOAT, 
	upper_bound FLOAT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ValueSeries" (
	id INTEGER NOT NULL, 
	"values" FLOAT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Event" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	"Dataset_id" TEXT, 
	has_time_id INTEGER, 
	has_location_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "LocationComponent" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Location" (
	id INTEGER NOT NULL, 
	named_location TEXT, 
	geo_location_id INTEGER, 
	geo_box_location_id INTEGER, 
	relative_location_id INTEGER, 
	postal_address_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(named_location) REFERENCES "Concept" (id), 
	FOREIGN KEY(geo_location_id) REFERENCES "GeoLocation" (id), 
	FOREIGN KEY(geo_box_location_id) REFERENCES "GeoBoxLocation" (id), 
	FOREIGN KEY(relative_location_id) REFERENCES "RelativeLocation" (id), 
	FOREIGN KEY(postal_address_id) REFERENCES "PostalAddress" (id)
);
CREATE TABLE "GeoLocation" (
	id INTEGER NOT NULL, 
	latitude INTEGER, 
	longitude INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "GeoBoxLocation" (
	id INTEGER NOT NULL, 
	west_bounding_coordinate INTEGER, 
	east_bounding_coordinate INTEGER, 
	north_bounding_coordinate INTEGER, 
	south_bounding_coordinate INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "RelativeLocation" (
	id INTEGER NOT NULL, 
	relationship_type TEXT, 
	target_location_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(relationship_type) REFERENCES "Concept" (id), 
	FOREIGN KEY(target_location_id) REFERENCES "Location" (id)
);
CREATE TABLE "PostalAddress" (
	id INTEGER NOT NULL, 
	street_address TEXT, 
	street_address_additional TEXT, 
	city TEXT, 
	state TEXT, 
	postal_code TEXT, 
	country TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(country) REFERENCES "Concept" (id)
);
CREATE TABLE "Temporal" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Duration" (
	id INTEGER NOT NULL, 
	start_time_id INTEGER, 
	end_time_id INTEGER, 
	happens_at_id INTEGER, 
	is_ongoing_as_of_id INTEGER, 
	recurring_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(start_time_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(end_time_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(happens_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(is_ongoing_as_of_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(recurring_id) REFERENCES "RecurringTemporalWindow" (id)
);
CREATE TABLE "RecurringTemporalWindow" (
	id INTEGER NOT NULL, 
	count INTEGER, 
	period_unit TEXT, 
	enumerated_times_id INTEGER, 
	period_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(period_unit) REFERENCES "UnitConcept" (id), 
	FOREIGN KEY(enumerated_times_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(period_id) REFERENCES "Duration" (id)
);
CREATE TABLE "TimePoint" (
	id INTEGER NOT NULL, 
	year_value INTEGER, 
	date_value DATE, 
	time_value TIME, 
	datetime_value DATETIME, 
	marker_event TEXT, 
	description TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(marker_event) REFERENCES "Event" (id)
);
CREATE TABLE "ProvenanceComponent" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "CreationHistory" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "CreationMetadata" (
	id INTEGER NOT NULL, 
	title TEXT, 
	abstract TEXT, 
	rights TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Concept" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	"Dataset_id" TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "UnitConcept" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "State" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ProcedureConfiguration" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Dataset" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "Thing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "DomainEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "InvestigativeEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "Observable" (
	case_or_control VARCHAR(7), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	"Dataset_id" TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "RelativeValue" (
	id INTEGER NOT NULL, 
	interpretation TEXT NOT NULL, 
	reference TEXT, 
	"AttributeValue_id" INTEGER, 
	target_value_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(interpretation) REFERENCES "Concept" (id), 
	FOREIGN KEY(reference) REFERENCES "Concept" (id), 
	FOREIGN KEY("AttributeValue_id") REFERENCES "AttributeValue" (id), 
	FOREIGN KEY(target_value_id) REFERENCES "AttributeValue" (id)
);
CREATE TABLE "Sample" (
	case_or_control VARCHAR(7), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	"Dataset_id" TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "InformationEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "InvestigativeProtocol" (
	protocols_io_url TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "StudyDesign" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "StudyHypothesis" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "Agent" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	"Dataset_id" TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "Organization" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "CreationHistoryAction" (
	id INTEGER NOT NULL, 
	description TEXT, 
	"CreationHistory_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("CreationHistory_id") REFERENCES "CreationHistory" (id)
);
CREATE TABLE "QuantityKind" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "AttributeConcept" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "Variable" (
	fixed_unit TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(fixed_unit) REFERENCES "UnitConcept" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "Device" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	"Dataset_id" TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "DataObject" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "InvestigationSite" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "Procedure" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "ResultMatrix" (
	id INTEGER NOT NULL, 
	"values" FLOAT, 
	"Dataset_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE TABLE "EnvironmentalMaterial" (
	case_or_control VARCHAR(7), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "Organism" (
	case_or_control VARCHAR(7), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "OrganismPart" (
	case_or_control VARCHAR(7), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "OrganismPopulation" (
	case_or_control VARCHAR(7), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "Microbiome" (
	case_or_control VARCHAR(7), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "Patient" (
	case_or_control VARCHAR(7), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "Cohort" (
	case_or_control VARCHAR(7), 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "HealthcareSite" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "HealthcareOrganization" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "Event_ontology_types" (
	"Event_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Event_id", ontology_types_id), 
	FOREIGN KEY("Event_id") REFERENCES "Event" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "CreationMetadata_keywords" (
	"CreationMetadata_id" INTEGER, 
	keywords TEXT, 
	PRIMARY KEY ("CreationMetadata_id", keywords), 
	FOREIGN KEY("CreationMetadata_id") REFERENCES "CreationMetadata" (id)
);
CREATE TABLE "Concept_ontology_types" (
	"Concept_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Concept_id", ontology_types_id), 
	FOREIGN KEY("Concept_id") REFERENCES "Concept" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "UnitConcept_ontology_types" (
	"UnitConcept_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("UnitConcept_id", ontology_types_id), 
	FOREIGN KEY("UnitConcept_id") REFERENCES "UnitConcept" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Dataset_ontology_types" (
	"Dataset_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Dataset_id", ontology_types_id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Investigation" (
	objectives TEXT, 
	hypothesis TEXT, 
	design TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	"Dataset_id" TEXT, 
	has_time_id INTEGER, 
	has_location_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(hypothesis) REFERENCES "StudyHypothesis" (id), 
	FOREIGN KEY(design) REFERENCES "StudyDesign" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "StudyResult" (
	hypothesis TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	has_location_id INTEGER, 
	has_time_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(hypothesis) REFERENCES "StudyHypothesis" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "Relationship" (
	id INTEGER NOT NULL, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT, 
	"Dataset_id" TEXT, 
	has_time_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES "Thing" (id), 
	FOREIGN KEY(predicate) REFERENCES "Concept" (id), 
	FOREIGN KEY(object) REFERENCES "Thing" (id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id)
);
CREATE TABLE "AgentRole" (
	id INTEGER NOT NULL, 
	agent TEXT, 
	role TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(agent) REFERENCES "Agent" (id), 
	FOREIGN KEY(role) REFERENCES "Concept" (id)
);
CREATE TABLE "ParticipantInRole" (
	id INTEGER NOT NULL, 
	participant TEXT, 
	role TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(participant) REFERENCES "Thing" (id), 
	FOREIGN KEY(role) REFERENCES "Concept" (id)
);
CREATE TABLE "HealthcareEncounter" (
	patient TEXT, 
	provider TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification VARCHAR(34), 
	has_time_id INTEGER, 
	has_location_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(patient) REFERENCES "Patient" (id), 
	FOREIGN KEY(provider) REFERENCES "HealthcareOrganization" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "Thing_ontology_types" (
	"Thing_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Thing_id", ontology_types_id), 
	FOREIGN KEY("Thing_id") REFERENCES "Thing" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "DomainEntity_ontology_types" (
	"DomainEntity_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("DomainEntity_id", ontology_types_id), 
	FOREIGN KEY("DomainEntity_id") REFERENCES "DomainEntity" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "InvestigativeEntity_ontology_types" (
	"InvestigativeEntity_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("InvestigativeEntity_id", ontology_types_id), 
	FOREIGN KEY("InvestigativeEntity_id") REFERENCES "InvestigativeEntity" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Observable_ontology_types" (
	"Observable_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Observable_id", ontology_types_id), 
	FOREIGN KEY("Observable_id") REFERENCES "Observable" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Sample_ontology_types" (
	"Sample_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Sample_id", ontology_types_id), 
	FOREIGN KEY("Sample_id") REFERENCES "Sample" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "InformationEntity_ontology_types" (
	"InformationEntity_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("InformationEntity_id", ontology_types_id), 
	FOREIGN KEY("InformationEntity_id") REFERENCES "InformationEntity" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "InvestigativeProtocol_ontology_types" (
	"InvestigativeProtocol_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("InvestigativeProtocol_id", ontology_types_id), 
	FOREIGN KEY("InvestigativeProtocol_id") REFERENCES "InvestigativeProtocol" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "StudyDesign_ontology_types" (
	"StudyDesign_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("StudyDesign_id", ontology_types_id), 
	FOREIGN KEY("StudyDesign_id") REFERENCES "StudyDesign" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "StudyHypothesis_ontology_types" (
	"StudyHypothesis_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("StudyHypothesis_id", ontology_types_id), 
	FOREIGN KEY("StudyHypothesis_id") REFERENCES "StudyHypothesis" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Agent_ontology_types" (
	"Agent_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Agent_id", ontology_types_id), 
	FOREIGN KEY("Agent_id") REFERENCES "Agent" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Organization_ontology_types" (
	"Organization_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Organization_id", ontology_types_id), 
	FOREIGN KEY("Organization_id") REFERENCES "Organization" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "CreationMetadata_creators" (
	"CreationMetadata_id" INTEGER, 
	creators_id TEXT, 
	PRIMARY KEY ("CreationMetadata_id", creators_id), 
	FOREIGN KEY("CreationMetadata_id") REFERENCES "CreationMetadata" (id), 
	FOREIGN KEY(creators_id) REFERENCES "Agent" (id)
);
CREATE TABLE "CreationMetadata_contributors" (
	"CreationMetadata_id" INTEGER, 
	contributors_id TEXT, 
	PRIMARY KEY ("CreationMetadata_id", contributors_id), 
	FOREIGN KEY("CreationMetadata_id") REFERENCES "CreationMetadata" (id), 
	FOREIGN KEY(contributors_id) REFERENCES "Agent" (id)
);
CREATE TABLE "CreationMetadata_contacts" (
	"CreationMetadata_id" INTEGER, 
	contacts_id TEXT, 
	PRIMARY KEY ("CreationMetadata_id", contacts_id), 
	FOREIGN KEY("CreationMetadata_id") REFERENCES "CreationMetadata" (id), 
	FOREIGN KEY(contacts_id) REFERENCES "Agent" (id)
);
CREATE TABLE "QuantityKind_ontology_types" (
	"QuantityKind_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("QuantityKind_id", ontology_types_id), 
	FOREIGN KEY("QuantityKind_id") REFERENCES "QuantityKind" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "AttributeConcept_ontology_types" (
	"AttributeConcept_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("AttributeConcept_id", ontology_types_id), 
	FOREIGN KEY("AttributeConcept_id") REFERENCES "AttributeConcept" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Variable_ontology_types" (
	"Variable_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Variable_id", ontology_types_id), 
	FOREIGN KEY("Variable_id") REFERENCES "Variable" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Device_ontology_types" (
	"Device_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Device_id", ontology_types_id), 
	FOREIGN KEY("Device_id") REFERENCES "Device" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "DataObject_ontology_types" (
	"DataObject_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("DataObject_id", ontology_types_id), 
	FOREIGN KEY("DataObject_id") REFERENCES "DataObject" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "InvestigationSite_ontology_types" (
	"InvestigationSite_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("InvestigationSite_id", ontology_types_id), 
	FOREIGN KEY("InvestigationSite_id") REFERENCES "InvestigationSite" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Procedure_ontology_types" (
	"Procedure_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Procedure_id", ontology_types_id), 
	FOREIGN KEY("Procedure_id") REFERENCES "Procedure" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "EnvironmentalMaterial_ontology_types" (
	"EnvironmentalMaterial_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("EnvironmentalMaterial_id", ontology_types_id), 
	FOREIGN KEY("EnvironmentalMaterial_id") REFERENCES "EnvironmentalMaterial" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Organism_ontology_types" (
	"Organism_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Organism_id", ontology_types_id), 
	FOREIGN KEY("Organism_id") REFERENCES "Organism" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "OrganismPart_ontology_types" (
	"OrganismPart_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("OrganismPart_id", ontology_types_id), 
	FOREIGN KEY("OrganismPart_id") REFERENCES "OrganismPart" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "OrganismPopulation_ontology_types" (
	"OrganismPopulation_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("OrganismPopulation_id", ontology_types_id), 
	FOREIGN KEY("OrganismPopulation_id") REFERENCES "OrganismPopulation" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Microbiome_ontology_types" (
	"Microbiome_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Microbiome_id", ontology_types_id), 
	FOREIGN KEY("Microbiome_id") REFERENCES "Microbiome" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Patient_ontology_types" (
	"Patient_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Patient_id", ontology_types_id), 
	FOREIGN KEY("Patient_id") REFERENCES "Patient" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Cohort_ontology_types" (
	"Cohort_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Cohort_id", ontology_types_id), 
	FOREIGN KEY("Cohort_id") REFERENCES "Cohort" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "HealthcareSite_ontology_types" (
	"HealthcareSite_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("HealthcareSite_id", ontology_types_id), 
	FOREIGN KEY("HealthcareSite_id") REFERENCES "HealthcareSite" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "HealthcareOrganization_ontology_types" (
	"HealthcareOrganization_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("HealthcareOrganization_id", ontology_types_id), 
	FOREIGN KEY("HealthcareOrganization_id") REFERENCES "HealthcareOrganization" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Observation" (
	is_about TEXT, 
	part_of TEXT, 
	performer TEXT, 
	method TEXT, 
	device_used TEXT, 
	procedure_used TEXT, 
	sample_used TEXT, 
	data_used TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	"Dataset_id" TEXT, 
	has_time_id INTEGER, 
	result_id INTEGER, 
	procedure_configuration_id INTEGER, 
	has_location_id INTEGER, 
	metadata_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(is_about) REFERENCES "Observable" (id), 
	FOREIGN KEY(part_of) REFERENCES "Investigation" (id), 
	FOREIGN KEY(performer) REFERENCES "Agent" (id), 
	FOREIGN KEY(method) REFERENCES "Concept" (id), 
	FOREIGN KEY(device_used) REFERENCES "Device" (id), 
	FOREIGN KEY(procedure_used) REFERENCES "Procedure" (id), 
	FOREIGN KEY(sample_used) REFERENCES "Sample" (id), 
	FOREIGN KEY(data_used) REFERENCES "DataObject" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id), 
	FOREIGN KEY(has_time_id) REFERENCES "Duration" (id), 
	FOREIGN KEY(result_id) REFERENCES "AttributeValue" (id), 
	FOREIGN KEY(procedure_configuration_id) REFERENCES "ProcedureConfiguration" (id), 
	FOREIGN KEY(has_location_id) REFERENCES "Location" (id), 
	FOREIGN KEY(metadata_id) REFERENCES "CreationHistory" (id)
);
CREATE TABLE "Event_has_participants" (
	"Event_id" TEXT, 
	has_participants_id INTEGER, 
	PRIMARY KEY ("Event_id", has_participants_id), 
	FOREIGN KEY("Event_id") REFERENCES "Event" (id), 
	FOREIGN KEY(has_participants_id) REFERENCES "ParticipantInRole" (id)
);
CREATE TABLE "Investigation_variables" (
	"Investigation_id" TEXT, 
	variables_id TEXT, 
	PRIMARY KEY ("Investigation_id", variables_id), 
	FOREIGN KEY("Investigation_id") REFERENCES "Investigation" (id), 
	FOREIGN KEY(variables_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Investigation_results" (
	"Investigation_id" TEXT, 
	results_id TEXT, 
	PRIMARY KEY ("Investigation_id", results_id), 
	FOREIGN KEY("Investigation_id") REFERENCES "Investigation" (id), 
	FOREIGN KEY(results_id) REFERENCES "StudyResult" (id)
);
CREATE TABLE "Investigation_ontology_types" (
	"Investigation_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Investigation_id", ontology_types_id), 
	FOREIGN KEY("Investigation_id") REFERENCES "Investigation" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "StudyResult_results" (
	"StudyResult_id" TEXT, 
	results_id INTEGER, 
	PRIMARY KEY ("StudyResult_id", results_id), 
	FOREIGN KEY("StudyResult_id") REFERENCES "StudyResult" (id), 
	FOREIGN KEY(results_id) REFERENCES "AttributeValue" (id)
);
CREATE TABLE "StudyResult_ontology_types" (
	"StudyResult_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("StudyResult_id", ontology_types_id), 
	FOREIGN KEY("StudyResult_id") REFERENCES "StudyResult" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "CreationHistoryAction_roles" (
	"CreationHistoryAction_id" INTEGER, 
	roles_id INTEGER, 
	PRIMARY KEY ("CreationHistoryAction_id", roles_id), 
	FOREIGN KEY("CreationHistoryAction_id") REFERENCES "CreationHistoryAction" (id), 
	FOREIGN KEY(roles_id) REFERENCES "AgentRole" (id)
);
CREATE TABLE "HealthcareEncounter_has_participants" (
	"HealthcareEncounter_id" TEXT, 
	has_participants_id INTEGER, 
	PRIMARY KEY ("HealthcareEncounter_id", has_participants_id), 
	FOREIGN KEY("HealthcareEncounter_id") REFERENCES "HealthcareEncounter" (id), 
	FOREIGN KEY(has_participants_id) REFERENCES "ParticipantInRole" (id)
);
CREATE TABLE "HealthcareEncounter_ontology_types" (
	"HealthcareEncounter_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("HealthcareEncounter_id", ontology_types_id), 
	FOREIGN KEY("HealthcareEncounter_id") REFERENCES "HealthcareEncounter" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Observation_derived_from" (
	"Observation_id" TEXT, 
	derived_from_id TEXT, 
	PRIMARY KEY ("Observation_id", derived_from_id), 
	FOREIGN KEY("Observation_id") REFERENCES "Observation" (id), 
	FOREIGN KEY(derived_from_id) REFERENCES "Observation" (id)
);
CREATE TABLE "Observation_ontology_types" (
	"Observation_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Observation_id", ontology_types_id), 
	FOREIGN KEY("Observation_id") REFERENCES "Observation" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);