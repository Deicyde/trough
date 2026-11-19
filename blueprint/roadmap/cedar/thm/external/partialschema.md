---
catalog: module
lean: Cedar.Validation.PartialEntitySchema.AncestorsClosed, Cedar.Validation.PartialEntitySchema.ExternalParentsStandard, Cedar.Validation.PartialSchema.WellFormed, Cedar.Validation.PartialSchema.wfEnv, Cedar.Validation.DeclarationsKept, Cedar.Validation.EntryKept, Cedar.Validation.PartialEntitySchemaEntry.completeWith, Cedar.Validation.PartialSchema.completeWith, Cedar.Validation.toPartialSchema_asSchema?, Cedar.Validation.toPartialSchema_validationView, Cedar.Validation.toPartialSchema_ets_find?, Cedar.Validation.toPartialSchema_acts_find?, Cedar.Validation.toPartialSchema_wfEnv, Cedar.Validation.asSchema?_isSome_iff_isComplete, Cedar.Validation.validationView_find?_ets, Cedar.Validation.validationView_find?_acts, Cedar.Validation.validationView_eq_of_asSchema?, Cedar.Validation.PartialActionSchemaEntry.validationView_ancestors, Cedar.Validation.PartialEntitySchemaEntry.validationView_isStandard, Cedar.Validation.PartialEntitySchemaEntry.validationView_isValidEntityEID, Cedar.Validation.PartialEntitySchemaEntry.withAncestors_isStandard, Cedar.Validation.PartialSchema.WellFormed.etsMap, Cedar.Validation.PartialSchema.WellFormed.actsMap, Cedar.Validation.PartialSchema.wellFormed_iff, Cedar.Validation.PartialSchema.wfEnv_ets_find?, Cedar.Validation.PartialSchema.wfEnv_acts_find?, Cedar.Validation.PartialSchema.wfEnv_ets_contains, Cedar.Validation.PartialSchema.wfEnv_acts_contains, Cedar.Validation.PartialSchema.WellFormed.entry, Cedar.Validation.PartialSchema.WellFormed.action, Cedar.Validation.PartialSchema.WellFormed.external_parent_isStandard, Cedar.Validation.PartialSchema.WellFormed.ancestor_declared, Cedar.Validation.PartialSchema.WellFormed.action_ancestor, Cedar.Validation.PartialSchema.WellFormed.acyclic, Cedar.Validation.PartialSchema.WellFormed.transitive, Cedar.Validation.PartialSchema.WellFormed.disjoint, Cedar.Validation.PartialSchema.WellFormed.ancestors_wf, Cedar.Validation.PartialEntitySchema.AncestorsClosed.reach, Cedar.Validation.PartialActionSchemaEntry.external_validationView_wf, Cedar.Validation.DeclarationsKept.acts_contains, Cedar.Validation.DeclarationsKept.entityType_wf, Cedar.Validation.DeclarationsKept.cedarType_wf, Cedar.Validation.DeclarationsKept.ancestor_declared, Cedar.Validation.DeclarationsKept.definition_wf, Cedar.Validation.DeclarationsKept.action_wf, Cedar.Validation.DeclarationsKept.transitive, Cedar.Validation.DeclarationsKept.trans, Cedar.Validation.DeclarationsKept.entry, Cedar.Validation.DeclarationsKept.antisymm, Cedar.Validation.DeclarationsKept.eq_toPartialSchema, Cedar.Validation.completeWith_ets_find?, Cedar.Validation.completeWith_empty, Cedar.Validation.PartialEntitySchemaEntry.completeWith_ancestors, Cedar.Validation.PartialEntitySchemaEntry.completeWith_isStandard, Cedar.Validation.toPartialSchema_completeWith_ets_find?, Cedar.Validation.toPartialSchema_completeWith_acts_find?, Cedar.Validation.DeclarationsKept.completeWith, Cedar.Validation.PartialSchema.WellFormed.completeWith
statement: formalized
proof: formalized
---

# External/PartialSchema

`Cedar.Thm.External.PartialSchema`, in [Cedar/Thm/External/PartialSchema.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean).

`Cedar.Validation.PartialEntitySchema.AncestorsClosed` (definition, [line 31](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L31))

> Every ancestor set is transitively closed.
> …

```lean
def PartialEntitySchema.AncestorsClosed (schema : PartialEntitySchema) : Prop
```

`Cedar.Validation.PartialEntitySchema.ExternalParentsStandard` (definition, [line 43](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L43))

> No external entity type declaration lists an enum entity type as a parent: a
> definition of the external must list the parent, so only a declaration of the
> parent, which an enum definition cannot be, can supply it.

```lean
def PartialEntitySchema.ExternalParentsStandard (schema : PartialEntitySchema) : Prop
```

`Cedar.Validation.PartialSchema.WellFormed` (definition, [line 54](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L54))

> A partial schema is well-formed when its definitions satisfy the existing
> schema conditions, its externals satisfy those conditions using only their
> known ancestors, and no external lists an enum entity type as a parent.

```lean
def PartialSchema.WellFormed (schema : PartialSchema) : Prop
```

`Cedar.Validation.PartialSchema.wfEnv` (definition, [line 70](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L70))

> The environment in which `PartialSchema.WellFormed` checks a partial schema and
> `PartialSchema.validateEntities` validates entities: the validation view with the
> default request type.

```lean
def PartialSchema.wfEnv (schema : PartialSchema) : TypeEnv
```

`Cedar.Validation.DeclarationsKept` (structure, [line 78](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L78))

> `t` keeps every declaration of `s`: its entity types with their definitions,
> standard entity types, and listed ancestors, and its actions with their
> ancestors and definitions.

```lean
structure DeclarationsKept (s t : PartialSchema) : Prop where
  entities : ∀ ety, s.ets.contains ety → t.ets.contains ety
  definitions : ∀ ety entry, s.ets.find? ety = some (.defined entry) →
    t.ets.find? ety = some (.defined entry)
  standard : ∀ ety entry, s.ets.find? ety = some entry → entry.isStandard = true →
    ∃ entry', t.ets.find? ety = some entry' ∧ entry'.isStandard = true
  ancestors : ∀ ety entry ancestor, s.ets.find? ety = some entry → ancestor ∈ entry.ancestors →
    ∃ entry', t.ets.find? ety = some entry' ∧ ancestor ∈ entry'.ancestors
  actions : ∀ uid entry, s.acts.find? uid = some entry →
    ∃ entry', t.acts.find? uid = some entry' ∧ entry'.ancestors = entry.ancestors
  actionDefinitions : ∀ uid entry, s.acts.find? uid = some (.defined entry) →
    t.acts.find? uid = some (.defined entry)
```

`Cedar.Validation.EntryKept` (structure, [line 92](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L92))

> `z` keeps the definition, the standard kind, and the ancestors of the entity entry `x`.

```lean
structure EntryKept (x z : PartialEntitySchemaEntry) : Prop where
  definition : ∀ entry, x = .defined entry → z = .defined entry
  standard : x.isStandard = true → z.isStandard = true
  ancestors : x.ancestors ⊆ z.ancestors
```

`Cedar.Validation.PartialEntitySchemaEntry.completeWith` (definition, [line 101](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L101))

> The definition that completes an entity entry: its definition, or a standard
> entity type with its ancestors, the attributes `attrs`, and no tags.

```lean
def PartialEntitySchemaEntry.completeWith (attrs : RecordType) :
    PartialEntitySchemaEntry → EntitySchemaEntry
```

`Cedar.Validation.PartialSchema.completeWith` (definition, [line 110](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L110))

> The schema that completes `p`: it defines each external entity type of `p` with
> the attributes `attrs`, and each external action by its validation view.

```lean
def PartialSchema.completeWith (p : PartialSchema) (attrs : RecordType) : Schema
```

`Cedar.Validation.toPartialSchema_asSchema?` (theorem, [line 117](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L117))

> Coercing a schema to a partial schema and back preserves it.

```lean
theorem toPartialSchema_asSchema? (schema : Schema) :
    (Schema.toPartialSchema schema).asSchema? = some schema
```

`Cedar.Validation.toPartialSchema_validationView` (theorem, [line 129](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L129))

> Coercing a schema to a partial schema preserves its validation view.

```lean
theorem toPartialSchema_validationView (schema : Schema) :
    (Schema.toPartialSchema schema).validationView = schema
```

`Cedar.Validation.toPartialSchema_ets_find?` (theorem, [line 140](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L140))

> Coercing a schema to a partial schema defines each of its entity types.

```lean
theorem toPartialSchema_ets_find? (schema : Schema) (ety : EntityType) :
    (Schema.toPartialSchema schema).ets.find? ety = (schema.ets.find? ety).map .defined
```

`Cedar.Validation.toPartialSchema_acts_find?` (theorem, [line 145](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L145))

> Coercing a schema to a partial schema defines each of its actions.

```lean
theorem toPartialSchema_acts_find? (schema : Schema) (uid : EntityUID) :
    (Schema.toPartialSchema schema).acts.find? uid = (schema.acts.find? uid).map .defined
```

`Cedar.Validation.toPartialSchema_wfEnv` (theorem, [line 150](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L150))

> A coerced schema is checked in the environment with its own maps.

```lean
theorem toPartialSchema_wfEnv (schema : Schema) :
    (Schema.toPartialSchema schema).wfEnv =
      { ets := schema.ets, acts := schema.acts, reqty := default }
```

`Cedar.Validation.asSchema?_isSome_iff_isComplete` (theorem, [line 156](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L156))

> A partial schema converts to a schema exactly when it is complete.

```lean
theorem asSchema?_isSome_iff_isComplete (schema : PartialSchema) :
    schema.asSchema?.isSome ↔ schema.isComplete
```

`Cedar.Validation.validationView_find?_ets` (theorem, [line 188](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L188))

> The entity validation view maps the entry found in the partial schema.

```lean
theorem validationView_find?_ets (schema : PartialSchema) (ety : EntityType) :
    schema.validationView.ets.find? ety =
      (schema.ets.find? ety).map PartialEntitySchemaEntry.validationView
```

`Cedar.Validation.validationView_find?_acts` (theorem, [line 194](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L194))

> The action validation view maps the entry found in the partial schema.

```lean
theorem validationView_find?_acts (schema : PartialSchema) (uid : EntityUID) :
    schema.validationView.acts.find? uid =
      (schema.acts.find? uid).map PartialActionSchemaEntry.validationView
```

`Cedar.Validation.validationView_eq_of_asSchema?` (theorem, [line 200](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L200))

> A completed partial schema agrees with its validation view.

```lean
theorem validationView_eq_of_asSchema?
    {ps : PartialSchema} {schema : Schema}
    (h : ps.asSchema? = some schema) :
    ps.validationView = schema
```

`Cedar.Validation.PartialActionSchemaEntry.validationView_ancestors` (theorem, [line 245](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L245))

> The validation view keeps an action's ancestors.

```lean
theorem PartialActionSchemaEntry.validationView_ancestors
    (entry : PartialActionSchemaEntry) :
    entry.validationView.ancestors = entry.ancestors
```

`Cedar.Validation.PartialEntitySchemaEntry.validationView_isStandard` (theorem, [line 251](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L251))

> The validation view keeps whether an entity type is standard or external.

```lean
theorem PartialEntitySchemaEntry.validationView_isStandard
    (entry : PartialEntitySchemaEntry) :
    entry.validationView.isStandard = entry.isStandard
```

`Cedar.Validation.PartialEntitySchemaEntry.validationView_isValidEntityEID` (theorem, [line 257](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L257))

> A standard or external entity type accepts every entity id in the validation view.

```lean
theorem PartialEntitySchemaEntry.validationView_isValidEntityEID
    {entry : PartialEntitySchemaEntry}
    (h : entry.isStandard = true)
    (eid : String) :
    entry.validationView.isValidEntityEID eid = true
```

`Cedar.Validation.PartialEntitySchemaEntry.withAncestors_isStandard` (theorem, [line 270](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L270))

> Replacing ancestors keeps an entry standard or external.

```lean
theorem PartialEntitySchemaEntry.withAncestors_isStandard
    (entry : PartialEntitySchemaEntry) (ancestors : Set EntityType) :
    (entry.withAncestors ancestors).isStandard = entry.isStandard
```

`Cedar.Validation.PartialSchema.WellFormed.etsMap` (theorem, [line 280](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L280))

> A well-formed partial schema has a well-formed entity map.

```lean
theorem PartialSchema.WellFormed.etsMap
    {schema : PartialSchema} (h : schema.WellFormed) :
    schema.ets.WellFormed
```

`Cedar.Validation.PartialSchema.WellFormed.actsMap` (theorem, [line 287](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L287))

> A well-formed partial schema has a well-formed action map.

```lean
theorem PartialSchema.WellFormed.actsMap
    {schema : PartialSchema} (h : schema.WellFormed) :
    schema.acts.WellFormed
```

`Cedar.Validation.PartialSchema.wellFormed_iff` (theorem, [line 294](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L294))

> `PartialSchema.WellFormed` checks the maps in `wfEnv`.

```lean
theorem PartialSchema.wellFormed_iff {schema : PartialSchema} :
    schema.WellFormed ↔ schema.ets.AncestorsClosed ∧
      schema.ets.ExternalParentsStandard ∧
      schema.wfEnv.ets.WellFormed schema.wfEnv ∧ schema.wfEnv.acts.WellFormed schema.wfEnv
```

`Cedar.Validation.PartialSchema.wfEnv_ets_find?` (theorem, [line 301](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L301))

> Each entity entry of `wfEnv` is the view of an entry of the partial schema.

```lean
theorem PartialSchema.wfEnv_ets_find? {schema : PartialSchema} {ety : EntityType}
    {entry : EntitySchemaEntry} (h : schema.wfEnv.ets.find? ety = some entry) :
    ∃ entry', schema.ets.find? ety = some entry' ∧ entry'.validationView = entry
```

`Cedar.Validation.PartialSchema.wfEnv_acts_find?` (theorem, [line 307](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L307))

> Each action entry of `wfEnv` is the view of an entry of the partial schema.

```lean
theorem PartialSchema.wfEnv_acts_find? {schema : PartialSchema} {uid : EntityUID}
    {entry : ActionSchemaEntry} (h : schema.wfEnv.acts.find? uid = some entry) :
    ∃ entry', schema.acts.find? uid = some entry' ∧ entry'.validationView = entry
```

`Cedar.Validation.PartialSchema.wfEnv_ets_contains` (theorem, [line 313](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L313))

> `wfEnv` declares the entity types of the partial schema.

```lean
theorem PartialSchema.wfEnv_ets_contains (schema : PartialSchema) (ety : EntityType) :
    schema.wfEnv.ets.contains ety = schema.ets.contains ety
```

`Cedar.Validation.PartialSchema.wfEnv_acts_contains` (theorem, [line 318](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L318))

> `wfEnv` declares the actions of the partial schema.

```lean
theorem PartialSchema.wfEnv_acts_contains (schema : PartialSchema) (uid : EntityUID) :
    schema.wfEnv.acts.contains uid = schema.acts.contains uid
```

`Cedar.Validation.PartialSchema.WellFormed.entry` (theorem, [line 323](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L323))

> In a well-formed partial schema, the view of each entity entry is well-formed.

```lean
theorem PartialSchema.WellFormed.entry {schema : PartialSchema} {ety : EntityType}
    {entry : PartialEntitySchemaEntry} (h : schema.WellFormed)
    (hfind : schema.ets.find? ety = some entry) :
    entry.validationView.WellFormed schema.wfEnv
```

`Cedar.Validation.PartialSchema.WellFormed.action` (theorem, [line 330](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L330))

> In a well-formed partial schema, the view of each action is well-formed.

```lean
theorem PartialSchema.WellFormed.action {schema : PartialSchema} {uid : EntityUID}
    {entry : PartialActionSchemaEntry} (h : schema.WellFormed)
    (hfind : schema.acts.find? uid = some entry) :
    entry.validationView.WellFormed schema.wfEnv
```

`Cedar.Validation.PartialSchema.WellFormed.external_parent_isStandard` (theorem, [line 337](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L337))

> In a well-formed partial schema, no parent of an external entity type is an enum.

```lean
theorem PartialSchema.WellFormed.external_parent_isStandard {schema : PartialSchema}
    {ety parent : EntityType} {parents : Set EntityType} (h : schema.WellFormed)
    (hfind : schema.ets.find? ety = some (.external parents)) (hmem : parent ∈ parents) :
    ∃ entry, schema.ets.find? parent = some entry ∧ entry.isStandard
```

`Cedar.Validation.PartialSchema.WellFormed.ancestor_declared` (theorem, [line 344](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L344))

> In a well-formed partial schema, every ancestor of an entity type is declared.

```lean
theorem PartialSchema.WellFormed.ancestor_declared {schema : PartialSchema}
    {ety ancestor : EntityType} {entry : PartialEntitySchemaEntry} (h : schema.WellFormed)
    (hfind : schema.ets.find? ety = some entry) (hmem : ancestor ∈ entry.ancestors) :
    ∃ entry', schema.ets.find? ancestor = some entry'
```

`Cedar.Validation.PartialSchema.WellFormed.action_ancestor` (theorem, [line 361](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L361))

> In a well-formed partial schema, every ancestor of an action is an action.

```lean
theorem PartialSchema.WellFormed.action_ancestor {schema : PartialSchema}
    {uid ancestor : EntityUID} {entry : PartialActionSchemaEntry} (h : schema.WellFormed)
    (hfind : schema.acts.find? uid = some entry) (hmem : ancestor ∈ entry.ancestors) :
    schema.acts.contains ancestor
```

`Cedar.Validation.PartialSchema.WellFormed.acyclic` (theorem, [line 370](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L370))

> A well-formed partial schema has no action among its own ancestors.

```lean
theorem PartialSchema.WellFormed.acyclic {schema : PartialSchema} {uid : EntityUID}
    {entry : PartialActionSchemaEntry} (h : schema.WellFormed)
    (hfind : schema.acts.find? uid = some entry) :
    uid ∉ entry.ancestors
```

`Cedar.Validation.PartialSchema.WellFormed.transitive` (theorem, [line 378](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L378))

> A well-formed partial schema has transitively closed action ancestors.

```lean
theorem PartialSchema.WellFormed.transitive {schema : PartialSchema}
    {uid₁ uid₂ : EntityUID} {entry₁ entry₂ : PartialActionSchemaEntry}
    (h : schema.WellFormed)
    (hfind₁ : schema.acts.find? uid₁ = some entry₁)
    (hfind₂ : schema.acts.find? uid₂ = some entry₂)
    (hmem : uid₂ ∈ entry₁.ancestors) :
    entry₂.ancestors ⊆ entry₁.ancestors
```

`Cedar.Validation.PartialSchema.WellFormed.disjoint` (theorem, [line 393](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L393))

> A well-formed partial schema declares no action type as an entity type.

```lean
theorem PartialSchema.WellFormed.disjoint {schema : PartialSchema} {uid : EntityUID}
    (h : schema.WellFormed) (haction : schema.acts.contains uid) :
    ¬schema.ets.contains uid.ty
```

`Cedar.Validation.PartialSchema.WellFormed.ancestors_wf` (theorem, [line 401](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L401))

> In a well-formed partial schema, every entity entry has well-formed ancestors.

```lean
theorem PartialSchema.WellFormed.ancestors_wf {schema : PartialSchema}
    {ety : EntityType} {entry : PartialEntitySchemaEntry} (h : schema.WellFormed)
    (hfind : schema.ets.find? ety = some entry) :
    entry.ancestors.WellFormed
```

`Cedar.Validation.PartialEntitySchema.AncestorsClosed.reach` (theorem, [line 414](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L414))

> With closed ancestors, every entity type reachable through listed ancestors is listed.

```lean
theorem PartialEntitySchema.AncestorsClosed.reach {ets : PartialEntitySchema}
    (h : ets.AncestorsClosed) {ety ancestor : EntityType} {entry : PartialEntitySchemaEntry}
    (hfind : ets.find? ety = some entry)
    (hreach : Relation.TransGen (fun x y => ∃ e, ets.find? x = some e ∧ y ∈ e.ancestors)
      ety ancestor) :
    ancestor ∈ entry.ancestors
```

`Cedar.Validation.PartialActionSchemaEntry.external_validationView_wf` (theorem, [line 430](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L430))

> An external action's view is well-formed when its ancestors are a well-formed set of actions.

```lean
theorem PartialActionSchemaEntry.external_validationView_wf {env : TypeEnv}
    {ancestors : Set EntityUID} (hwf : ancestors.WellFormed)
    (hactions : ∀ a ∈ ancestors, env.acts.contains a) :
    (PartialActionSchemaEntry.external ancestors).validationView.WellFormed env
```

`Cedar.Validation.DeclarationsKept.acts_contains` (theorem, [line 442](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L442))

> `t` declares every action of `s`.

```lean
theorem DeclarationsKept.acts_contains {s t : PartialSchema} (h : DeclarationsKept s t)
    {uid : EntityUID} (hs : s.acts.contains uid) :
    t.acts.contains uid
```

`Cedar.Validation.DeclarationsKept.entityType_wf` (theorem, [line 450](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L450))

> An entity type well-formed for `s` is well-formed for `t`.

```lean
theorem DeclarationsKept.entityType_wf {s t : PartialSchema} (h : DeclarationsKept s t)
    {ety : EntityType} (hwf : EntityType.WellFormed s.wfEnv ety) :
    EntityType.WellFormed t.wfEnv ety
```

`Cedar.Validation.DeclarationsKept.cedarType_wf` (theorem, [line 462](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L462))

> A type well-formed for `s` is well-formed for `t`.

```lean
theorem DeclarationsKept.cedarType_wf {s t : PartialSchema} (h : DeclarationsKept s t)
    {ty : CedarType} (hwf : CedarType.WellFormed s.wfEnv ty) :
    CedarType.WellFormed t.wfEnv ty
```

`Cedar.Validation.DeclarationsKept.ancestor_declared` (theorem, [line 468](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L468))

> An ancestor listed in a well-formed `s` is declared in `t`.

```lean
theorem DeclarationsKept.ancestor_declared {s t : PartialSchema}
    (h : DeclarationsKept s t) (hs : s.WellFormed) {ety ancestor : EntityType}
    {entry : PartialEntitySchemaEntry}
    (hfind : s.ets.find? ety = some entry) (hmem : ancestor ∈ entry.ancestors) :
    ∃ ventry, t.wfEnv.ets.find? ancestor = some ventry
```

`Cedar.Validation.DeclarationsKept.definition_wf` (theorem, [line 480](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L480))

> A definition of a well-formed `s` is well-formed in `t`.

```lean
theorem DeclarationsKept.definition_wf {s t : PartialSchema}
    (h : DeclarationsKept s t) (hs : s.WellFormed) {ety : EntityType}
    {entry : EntitySchemaEntry} (hfind : s.ets.find? ety = some (.defined entry)) :
    entry.WellFormed t.wfEnv
```

`Cedar.Validation.DeclarationsKept.action_wf` (theorem, [line 494](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L494))

> An action of a well-formed `s` is well-formed in `t`.

```lean
theorem DeclarationsKept.action_wf {s t : PartialSchema}
    (h : DeclarationsKept s t) (hs : s.WellFormed) {uid : EntityUID}
    {entry : PartialActionSchemaEntry} (hfind : s.acts.find? uid = some entry) :
    entry.validationView.WellFormed t.wfEnv
```

`Cedar.Validation.DeclarationsKept.transitive` (theorem, [line 511](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L511))

> In `t`, the ancestors of an ancestor of an action of a well-formed `s` are
> ancestors of that action.

```lean
theorem DeclarationsKept.transitive {s t : PartialSchema}
    (h : DeclarationsKept s t) (hs : s.WellFormed) {uid₁ uid₂ : EntityUID}
    {entry₁ entry₂ : PartialActionSchemaEntry}
    (hfind₁ : s.acts.find? uid₁ = some entry₁)
    (hfind₂ : t.acts.find? uid₂ = some entry₂)
    (hmem : uid₂ ∈ entry₁.ancestors) :
    entry₂.ancestors ⊆ entry₁.ancestors
```

`Cedar.Validation.DeclarationsKept.trans` (theorem, [line 526](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L526))

> Keeping declarations is transitive.

```lean
theorem DeclarationsKept.trans {s t u : PartialSchema}
    (hst : DeclarationsKept s t) (htu : DeclarationsKept t u) :
    DeclarationsKept s u
```

`Cedar.Validation.DeclarationsKept.entry` (theorem, [line 545](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L545))

> The entry of `t` for an entity type of `s` keeps the entry of `s`.

```lean
theorem DeclarationsKept.entry {s t : PartialSchema} (h : DeclarationsKept s t)
    {ety : EntityType} {x z : PartialEntitySchemaEntry}
    (hx : s.ets.find? ety = some x) (hz : t.ets.find? ety = some z) :
    EntryKept x z
```

`Cedar.Validation.DeclarationsKept.antisymm` (theorem, [line 562](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L562))

> Well-formed partial schemas that keep each other's declarations are equal.

```lean
theorem DeclarationsKept.antisymm {s t : PartialSchema}
    (hs : s.WellFormed) (ht : t.WellFormed)
    (hst : DeclarationsKept s t) (hts : DeclarationsKept t s) :
    s = t
```

`Cedar.Validation.DeclarationsKept.eq_toPartialSchema` (theorem, [line 617](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L617))

> A partial schema with well-formed maps is a schema that it keeps and that keeps it.

```lean
theorem DeclarationsKept.eq_toPartialSchema {t : PartialSchema} {schema : Schema}
    (hets : t.ets.WellFormed) (hacts : t.acts.WellFormed)
    (hschema : (Schema.toPartialSchema schema).WellFormed)
    (hts : DeclarationsKept t schema) (hst : DeclarationsKept schema t) :
    t = schema
```

`Cedar.Validation.completeWith_ets_find?` (theorem, [line 652](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L652))

> Completing a partial schema completes each of its entity entries.

```lean
theorem completeWith_ets_find? (p : PartialSchema) (attrs : RecordType) (ety : EntityType) :
    (p.completeWith attrs).ets.find? ety = (p.ets.find? ety).map (·.completeWith attrs)
```

`Cedar.Validation.completeWith_empty` (theorem, [line 657](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L657))

> Completing with no attributes gives the validation view.

```lean
theorem completeWith_empty (p : PartialSchema) : p.completeWith Map.empty = p.validationView
```

`Cedar.Validation.PartialEntitySchemaEntry.completeWith_ancestors` (theorem, [line 665](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L665))

> Completing an entry keeps its ancestors.

```lean
theorem PartialEntitySchemaEntry.completeWith_ancestors (attrs : RecordType)
    (entry : PartialEntitySchemaEntry) :
    (entry.completeWith attrs).ancestors = entry.ancestors
```

`Cedar.Validation.PartialEntitySchemaEntry.completeWith_isStandard` (theorem, [line 671](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L671))

> Completing an entry keeps whether it is standard or external.

```lean
theorem PartialEntitySchemaEntry.completeWith_isStandard (attrs : RecordType)
    (entry : PartialEntitySchemaEntry) :
    (entry.completeWith attrs).isStandard = entry.isStandard
```

`Cedar.Validation.toPartialSchema_completeWith_ets_find?` (theorem, [line 677](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L677))

> The partial schema of a completion defines each entity type of `p` by its completion.

```lean
theorem toPartialSchema_completeWith_ets_find? (p : PartialSchema) (attrs : RecordType)
    (ety : EntityType) :
    (Schema.toPartialSchema (p.completeWith attrs)).ets.find? ety =
      (p.ets.find? ety).map fun entry => .defined (entry.completeWith attrs)
```

`Cedar.Validation.toPartialSchema_completeWith_acts_find?` (theorem, [line 685](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L685))

> The partial schema of a completion defines each action of `p` by its validation view.

```lean
theorem toPartialSchema_completeWith_acts_find? (p : PartialSchema) (attrs : RecordType)
    (uid : EntityUID) :
    (Schema.toPartialSchema (p.completeWith attrs)).acts.find? uid =
      (p.acts.find? uid).map fun entry => .defined entry.validationView
```

`Cedar.Validation.DeclarationsKept.completeWith` (theorem, [line 694](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L694))

> Completing `p` keeps the declarations of `p`.

```lean
theorem DeclarationsKept.completeWith (p : PartialSchema) (attrs : RecordType) :
    DeclarationsKept p (p.completeWith attrs)
```

`Cedar.Validation.PartialSchema.WellFormed.completeWith` (theorem, [line 717](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean#L717))

> Completing a well-formed partial schema with well-formed lifted attributes is well-formed.

```lean
theorem PartialSchema.WellFormed.completeWith {p : PartialSchema} {attrs : RecordType}
    (hp : p.WellFormed) (hwf : ∀ env, (CedarType.record attrs).WellFormed env)
    (hlifted : (CedarType.record attrs).IsLifted) :
    PartialSchema.WellFormed (p.completeWith attrs)
```

## Depends on

- [Typechecker/WF](../validation-2/typechecker-2/wf.md)
- [PartialRequestEntityValidator](../../validation/partialrequestentityvalidator.md)

## Proof depends on

- [Thm/Data/LT](../data/lt.md)

## Sources

- [Cedar/Thm/External/PartialSchema.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialSchema.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.External.PartialSchema.json)
