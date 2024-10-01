-- # Class: "Container" Description: ""
--     * Slot: id Description: 
-- # Class: "Thing" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
-- # Class: "Intangible" Description: ""
--     * Slot: id Description: 
-- # Class: "Observable" Description: "A concrete or abstract entity that has been observed or measured. Examples include a person, a region of the earth, a cell type, a tree, a mountain."
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: Container_id Description: Autocreated FK slot
-- # Class: "Observation" Description: ""
--     * Slot: has_duration Description: 
--     * Slot: is_about Description: 
--     * Slot: part_of Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: Container_id Description: Autocreated FK slot
--     * Slot: result_id Description: 
-- # Class: "AttributeValue" Description: ""
--     * Slot: id Description: 
--     * Slot: attribute Description: 
--     * Slot: target Description: 
--     * Slot: numeric_value Description: The numeric value of the observation
--     * Slot: unit Description: 
--     * Slot: Observable_id Description: Autocreated FK slot
--     * Slot: value_range_id Description: The range of the value
--     * Slot: ratio_id Description: The ratio of the value
-- # Class: "Event" Description: "A thing that happens to and potentially causally influences one of more participants."
--     * Slot: has_duration Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: Container_id Description: Autocreated FK slot
-- # Class: "Location" Description: ""
--     * Slot: id Description: 
-- # Class: "Investigation" Description: ""
--     * Slot: has_duration Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: Container_id Description: Autocreated FK slot
-- # Class: "Agent" Description: "Represents an Agent"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
-- # Class: "Relationship" Description: ""
--     * Slot: id Description: 
--     * Slot: has_duration Description: 
--     * Slot: subject Description: 
--     * Slot: predicate Description: 
--     * Slot: object Description: 
--     * Slot: Container_id Description: Autocreated FK slot
-- # Class: "Duration" Description: ""
--     * Slot: has_duration Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: starts_at_id Description: 
--     * Slot: ends_at_id Description: 
--     * Slot: happens_at_id Description: 
--     * Slot: is_ongoing_as_of_id Description: 
-- # Class: "TimePoint" Description: "A point in time. Can be fully specified, or specified in relative terms."
--     * Slot: id Description: 
--     * Slot: year_value Description: 
--     * Slot: date_value Description: 
--     * Slot: time_value Description: 
--     * Slot: datetime_value Description: 
--     * Slot: marker_event Description: 
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "Ratio" Description: "A tuple of two quantities"
--     * Slot: id Description: 
--     * Slot: numerator_id Description: The numerator of the ratio
--     * Slot: denominator_id Description: The denominator of the ratio
-- # Class: "ValueRange" Description: "A quantity range is a property that can be measured or counted"
--     * Slot: id Description: 
--     * Slot: lower_bound Description: The lower bound of the range
--     * Slot: upper_bound Description: The upper bound of the range
-- # Class: "Concept" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
--     * Slot: Container_id Description: Autocreated FK slot
-- # Class: "UnitConcept" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
-- # Class: "QuantityKind" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
-- # Class: "AttributeConcept" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
-- # Class: "ParticipantInRole" Description: ""
--     * Slot: id Description: 
--     * Slot: participant Description: 
--     * Slot: role Description: 
-- # Class: "DataObject" Description: ""
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: type Description: A type for a thing. The range of this should be a class within the schema. It is intended for schema-based classification. Anything beneath the shoreline of the schema should use `classification`.
--     * Slot: classification Description: A precise classification of the thing, using a concept from an ontology, controlled vocabulary, thesaurus, or taxonomy. Some schema classes may choose to restrict the range of values which this slot can take, using `values_from`, or bindings.
-- # Class: "Thing_ontology_types" Description: ""
--     * Slot: Thing_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Observable_ontology_types" Description: ""
--     * Slot: Observable_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Observation_ontology_types" Description: ""
--     * Slot: Observation_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Event_has_participants" Description: ""
--     * Slot: Event_id Description: Autocreated FK slot
--     * Slot: has_participants_id Description: 
-- # Class: "Event_ontology_types" Description: ""
--     * Slot: Event_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Investigation_ontology_types" Description: ""
--     * Slot: Investigation_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Agent_ontology_types" Description: ""
--     * Slot: Agent_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
-- # Class: "Duration_ontology_types" Description: ""
--     * Slot: Duration_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.
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
-- # Class: "DataObject_ontology_types" Description: ""
--     * Slot: DataObject_id Description: Autocreated FK slot
--     * Slot: ontology_types_id Description: A collection of concepts that help to classify the thing, using concepts from an ontolology,  thesaurus, or taxonomy.

CREATE TABLE "Container" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Intangible" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "AttributeValue" (
	id INTEGER NOT NULL, 
	attribute TEXT, 
	target TEXT, 
	numeric_value FLOAT, 
	unit TEXT, 
	"Observable_id" TEXT, 
	value_range_id INTEGER, 
	ratio_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(attribute) REFERENCES "AttributeConcept" (id), 
	FOREIGN KEY(target) REFERENCES "Concept" (id), 
	FOREIGN KEY(unit) REFERENCES "UnitConcept" (id), 
	FOREIGN KEY("Observable_id") REFERENCES "Observable" (id), 
	FOREIGN KEY(value_range_id) REFERENCES "ValueRange" (id), 
	FOREIGN KEY(ratio_id) REFERENCES "Ratio" (id)
);
CREATE TABLE "Event" (
	has_duration TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	"Container_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_duration) REFERENCES "Duration" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY("Container_id") REFERENCES "Container" (id)
);
CREATE TABLE "Location" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Duration" (
	has_duration TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	starts_at_id INTEGER, 
	ends_at_id INTEGER, 
	happens_at_id INTEGER, 
	is_ongoing_as_of_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_duration) REFERENCES "Duration" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY(starts_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(ends_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(happens_at_id) REFERENCES "TimePoint" (id), 
	FOREIGN KEY(is_ongoing_as_of_id) REFERENCES "TimePoint" (id)
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
CREATE TABLE "Concept" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	"Container_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY("Container_id") REFERENCES "Container" (id)
);
CREATE TABLE "Thing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "Observable" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	"Container_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY("Container_id") REFERENCES "Container" (id)
);
CREATE TABLE "Investigation" (
	has_duration TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	"Container_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_duration) REFERENCES "Duration" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY("Container_id") REFERENCES "Container" (id)
);
CREATE TABLE "Agent" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "UnitConcept" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "QuantityKind" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "AttributeConcept" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "DataObject" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id)
);
CREATE TABLE "Event_ontology_types" (
	"Event_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Event_id", ontology_types_id), 
	FOREIGN KEY("Event_id") REFERENCES "Event" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Duration_ontology_types" (
	"Duration_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Duration_id", ontology_types_id), 
	FOREIGN KEY("Duration_id") REFERENCES "Duration" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Concept_ontology_types" (
	"Concept_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Concept_id", ontology_types_id), 
	FOREIGN KEY("Concept_id") REFERENCES "Concept" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Observation" (
	has_duration TEXT, 
	is_about TEXT, 
	part_of TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type TEXT, 
	classification TEXT, 
	"Container_id" INTEGER, 
	result_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_duration) REFERENCES "Duration" (id), 
	FOREIGN KEY(is_about) REFERENCES "Observable" (id), 
	FOREIGN KEY(part_of) REFERENCES "Investigation" (id), 
	FOREIGN KEY(classification) REFERENCES "Concept" (id), 
	FOREIGN KEY("Container_id") REFERENCES "Container" (id), 
	FOREIGN KEY(result_id) REFERENCES "AttributeValue" (id)
);
CREATE TABLE "Relationship" (
	id INTEGER NOT NULL, 
	has_duration TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT, 
	"Container_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_duration) REFERENCES "Duration" (id), 
	FOREIGN KEY(subject) REFERENCES "Thing" (id), 
	FOREIGN KEY(predicate) REFERENCES "Concept" (id), 
	FOREIGN KEY(object) REFERENCES "Thing" (id), 
	FOREIGN KEY("Container_id") REFERENCES "Container" (id)
);
CREATE TABLE "ParticipantInRole" (
	id INTEGER NOT NULL, 
	participant TEXT, 
	role TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(participant) REFERENCES "Thing" (id), 
	FOREIGN KEY(role) REFERENCES "Concept" (id)
);
CREATE TABLE "Thing_ontology_types" (
	"Thing_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Thing_id", ontology_types_id), 
	FOREIGN KEY("Thing_id") REFERENCES "Thing" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Observable_ontology_types" (
	"Observable_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Observable_id", ontology_types_id), 
	FOREIGN KEY("Observable_id") REFERENCES "Observable" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Investigation_ontology_types" (
	"Investigation_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Investigation_id", ontology_types_id), 
	FOREIGN KEY("Investigation_id") REFERENCES "Investigation" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Agent_ontology_types" (
	"Agent_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Agent_id", ontology_types_id), 
	FOREIGN KEY("Agent_id") REFERENCES "Agent" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "UnitConcept_ontology_types" (
	"UnitConcept_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("UnitConcept_id", ontology_types_id), 
	FOREIGN KEY("UnitConcept_id") REFERENCES "UnitConcept" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
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
CREATE TABLE "DataObject_ontology_types" (
	"DataObject_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("DataObject_id", ontology_types_id), 
	FOREIGN KEY("DataObject_id") REFERENCES "DataObject" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Observation_ontology_types" (
	"Observation_id" TEXT, 
	ontology_types_id TEXT, 
	PRIMARY KEY ("Observation_id", ontology_types_id), 
	FOREIGN KEY("Observation_id") REFERENCES "Observation" (id), 
	FOREIGN KEY(ontology_types_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Event_has_participants" (
	"Event_id" TEXT, 
	has_participants_id INTEGER, 
	PRIMARY KEY ("Event_id", has_participants_id), 
	FOREIGN KEY("Event_id") REFERENCES "Event" (id), 
	FOREIGN KEY(has_participants_id) REFERENCES "ParticipantInRole" (id)
);