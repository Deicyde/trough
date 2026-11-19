---
catalog: module
lean: Cedar.Validation.linker_preserves_definitions, Cedar.Validation.linker_preserves_entity_declarations, Cedar.Validation.linker_preserves_action_declarations, Cedar.Validation.linker_preserves_action_ancestors, Cedar.Validation.linker_preserves_standard_entities, Cedar.Validation.linker_action_types_not_entity_types, Cedar.Validation.linker_definitions_come_from_inputs, Cedar.Validation.linker_actions_come_from_inputs, Cedar.Validation.linker_entity_ancestors, Cedar.Validation.linker_keeps_declarations, Cedar.Validation.linker_result_kept, Cedar.Validation.linker_definitions_disjoint, Cedar.Validation.linker_completion, Cedar.Validation.linker_completion_validationView, Cedar.Validation.linker_commutativity, Cedar.Validation.linker_commutativity_error, Cedar.Validation.linker_preserves_well_formedness, Cedar.Validation.linker_completed_schema_well_formed, Cedar.Validation.linker_associativity, Cedar.Validation.linker_associativity_error, Cedar.Validation.linker_completion_exists, Cedar.Validation.stable_entity_ancestor
statement: formalized
proof: formalized
---

# External/Linker

`Cedar.Thm.External.Linker`, in [Cedar/Thm/External/Linker.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean).

`Cedar.Validation.linker_preserves_definitions` (theorem, [line 1300](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1300))

> Every entity or action definition from either input appears unchanged in the
> result.

```lean
theorem linker_preserves_definitions
    {p c t : PartialSchema}
    (hlink : link p c = .ok t) :
    (∀ ety entry, p.ets.find? ety = some (.defined entry) →
      t.ets.find? ety = some (.defined entry)) ∧
    (∀ ety entry, c.ets.find? ety = some (.defined entry) →
      t.ets.find? ety = some (.defined entry)) ∧
    (∀ uid entry, p.acts.find? uid = some (.defined entry) →
      t.acts.find? uid = some (.defined entry)) ∧
    (∀ uid entry, c.acts.find? uid = some (.defined entry) →
      t.acts.find? uid = some (.defined entry))
```

`Cedar.Validation.linker_preserves_entity_declarations` (theorem, [line 1333](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1333))

> The result declares exactly the entity types declared by either input.

```lean
theorem linker_preserves_entity_declarations
    {p c t : PartialSchema}
    (hlink : link p c = .ok t)
    (ety : EntityType) :
    t.ets.contains ety ↔ p.ets.contains ety ∨ c.ets.contains ety
```

`Cedar.Validation.linker_preserves_action_declarations` (theorem, [line 1345](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1345))

> The result declares exactly the action UIDs declared by either input.

```lean
theorem linker_preserves_action_declarations
    {p c t : PartialSchema}
    (hlink : link p c = .ok t)
    (uid : EntityUID) :
    t.acts.contains uid ↔ p.acts.contains uid ∨ c.acts.contains uid
```

`Cedar.Validation.linker_preserves_action_ancestors` (theorem, [line 1356](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1356))

> Every action from either input keeps its ancestors in the result.

```lean
theorem linker_preserves_action_ancestors
    {p c t : PartialSchema}
    (hlink : link p c = .ok t) :
    (∀ uid entry, p.acts.find? uid = some entry →
      ∃ entry', t.acts.find? uid = some entry' ∧ entry'.ancestors = entry.ancestors) ∧
    (∀ uid entry, c.acts.find? uid = some entry →
      ∃ entry', t.acts.find? uid = some entry' ∧ entry'.ancestors = entry.ancestors)
```

`Cedar.Validation.linker_preserves_standard_entities` (theorem, [line 1373](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1373))

> Every standard or external entity type from either input is standard or
> external in the result. In particular, an external entity type never links to
> an enumerated entity type.

```lean
theorem linker_preserves_standard_entities
    {p c t : PartialSchema}
    (hlink : link p c = .ok t) :
    (∀ ety entry, p.ets.find? ety = some entry → entry.isStandard = true →
      ∃ entry', t.ets.find? ety = some entry' ∧ entry'.isStandard = true) ∧
    (∀ ety entry, c.ets.find? ety = some entry → entry.isStandard = true →
      ∃ entry', t.ets.find? ety = some entry' ∧ entry'.isStandard = true)
```

`Cedar.Validation.linker_action_types_not_entity_types` (theorem, [line 1399](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1399))

> The result never declares the entity type of an action as an entity type.

```lean
theorem linker_action_types_not_entity_types
    {p c t : PartialSchema}
    {uid : EntityUID}
    (hlink : link p c = .ok t)
    (haction : t.acts.contains uid) :
    ¬t.ets.contains uid.ty
```

`Cedar.Validation.linker_definitions_come_from_inputs` (theorem, [line 1412](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1412))

> Every entity definition of the result is a definition from either input.

```lean
theorem linker_definitions_come_from_inputs
    {p c t : PartialSchema}
    {ety : EntityType}
    {entry : EntitySchemaEntry}
    (hlink : link p c = .ok t)
    (hfind : t.ets.find? ety = some (.defined entry)) :
    p.ets.find? ety = some (.defined entry) ∨ c.ets.find? ety = some (.defined entry)
```

`Cedar.Validation.linker_actions_come_from_inputs` (theorem, [line 1434](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1434))

> Every action entry of the result is that action's entry in either input.

```lean
theorem linker_actions_come_from_inputs
    {p c t : PartialSchema}
    {uid : EntityUID}
    {entry : PartialActionSchemaEntry}
    (hlink : link p c = .ok t)
    (hfind : t.acts.find? uid = some entry) :
    p.acts.find? uid = some entry ∨ c.acts.find? uid = some entry
```

`Cedar.Validation.linker_entity_ancestors` (theorem, [line 1454](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1454))

> An entity type's ancestors in the result are exactly the entity types reachable
> from it through the ancestors listed by either input.

```lean
theorem linker_entity_ancestors
    {p c t : PartialSchema}
    {ety ancestor : EntityType}
    {entry : PartialEntitySchemaEntry}
    (hlink : link p c = .ok t)
    (hfind : t.ets.find? ety = some entry) :
    ancestor ∈ entry.ancestors ↔
      Relation.TransGen (fun x y =>
        (∃ e, p.ets.find? x = some e ∧ y ∈ e.ancestors) ∨
        (∃ e, c.ets.find? x = some e ∧ y ∈ e.ancestors)) ety ancestor
```

`Cedar.Validation.linker_keeps_declarations` (theorem, [line 1484](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1484))

> The result keeps every declaration of either input.

```lean
theorem linker_keeps_declarations
    {p c t : PartialSchema}
    (hlink : link p c = .ok t) :
    DeclarationsKept p t ∧ DeclarationsKept c t
```

`Cedar.Validation.linker_result_kept` (theorem, [line 1521](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1521))

> A partial schema with closed ancestors that keeps the declarations of both
> inputs keeps the declarations of the result.

```lean
theorem linker_result_kept
    {p c t u : PartialSchema}
    (hlink : link p c = .ok t)
    (hclosed : u.ets.AncestorsClosed)
    (hpu : DeclarationsKept p u)
    (hcu : DeclarationsKept c u) :
    DeclarationsKept t u
```

`Cedar.Validation.linker_definitions_disjoint` (theorem, [line 1572](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1572))

> No entity type or action is defined by both inputs.

```lean
theorem linker_definitions_disjoint
    {p c t : PartialSchema}
    (hlink : link p c = .ok t) :
    (∀ ety e₁ e₂, p.ets.find? ety = some (.defined e₁) →
      c.ets.find? ety ≠ some (.defined e₂)) ∧
    (∀ uid e₁ e₂, p.acts.find? uid = some (.defined e₁) →
      c.acts.find? uid ≠ some (.defined e₂))
```

`Cedar.Validation.linker_completion` (theorem, [line 1592](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1592))

> A well-formed partial schema links into the schema that completes it with
> attributes `attrs`, when these are well-formed and lifted.

```lean
theorem linker_completion
    {p : PartialSchema}
    {attrs : RecordType}
    (hp : p.WellFormed)
    (hwf : ∀ env, (CedarType.record attrs).WellFormed env)
    (hlifted : (CedarType.record attrs).IsLifted) :
    ∃ c, c.WellFormed ∧ link p c = .ok (p.completeWith attrs)
```

`Cedar.Validation.linker_completion_validationView` (theorem, [line 1639](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1639))

> A well-formed partial schema links into its validation view.

```lean
theorem linker_completion_validationView
    {p : PartialSchema}
    (hp : p.WellFormed) :
    ∃ c, c.WellFormed ∧ link p c = .ok p.validationView
```

`Cedar.Validation.linker_commutativity` (theorem, [line 1649](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1649))

> Changing the input order does not change a successful link.

```lean
theorem linker_commutativity
    {p c t : PartialSchema}
    (hc : c.WellFormed)
    (hlink : link p c = .ok t) :
    link c p = .ok t
```

`Cedar.Validation.linker_commutativity_error` (theorem, [line 1662](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1662))

> Changing the input order does not change whether linking fails.

```lean
theorem linker_commutativity_error
    {p c : PartialSchema}
    (hp : p.WellFormed)
    (hc : c.WellFormed) :
    (∃ err, link p c = .error err) ↔
    (∃ err, link c p = .error err)
```

`Cedar.Validation.linker_preserves_well_formedness` (theorem, [line 1677](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1677))

> Linking well-formed partial schemas produces a well-formed partial schema.

```lean
theorem linker_preserves_well_formedness
    {p c t : PartialSchema}
    (hp : p.WellFormed)
    (hc : c.WellFormed)
    (hlink : link p c = .ok t) :
    t.WellFormed
```

`Cedar.Validation.linker_completed_schema_well_formed` (theorem, [line 1757](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1757))

> A complete link passes the existing schema well-formedness check.

```lean
theorem linker_completed_schema_well_formed
    {p c t : PartialSchema}
    {schema : Schema}
    (hp : p.WellFormed)
    (hc : c.WellFormed)
    (hlink : link p c = .ok t)
    (hcomplete : t.asSchema? = some schema) :
    schema.validateWellFormed = .ok ()
```

`Cedar.Validation.linker_associativity` (theorem, [line 1822](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1822))

> Changing the grouping does not change a successful link.

```lean
theorem linker_associativity
    {p c d t₁ t : PartialSchema}
    (hp : p.WellFormed)
    (hc : c.WellFormed)
    (hd : d.WellFormed)
    (hpc : link p c = .ok t₁)
    (hpcd : link t₁ d = .ok t) :
    ∃ t₂, link c d = .ok t₂ ∧ link p t₂ = .ok t
```

`Cedar.Validation.linker_associativity_error` (theorem, [line 1884](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1884))

> Changing the grouping does not change whether linking fails.

```lean
theorem linker_associativity_error
    {p c d : PartialSchema}
    (hp : p.WellFormed)
    (hc : c.WellFormed)
    (hd : d.WellFormed) :
    (∃ err, (do
      let t₁ ← link p c
      link t₁ d) = .error err) ↔
    (∃ err, (do
      let t₂ ← link c d
      link p t₂) = .error err)
```

`Cedar.Validation.linker_completion_exists` (theorem, [line 1921](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1921))

> Every well-formed partial schema has a complete linking extension.

```lean
theorem linker_completion_exists
    {p : PartialSchema}
    (hp : p.WellFormed) :
    ∃ c t schema,
      c.WellFormed ∧
      link p c = .ok t ∧
      t.asSchema? = some schema
```

`Cedar.Validation.stable_entity_ancestor` (theorem, [line 1932](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean#L1932))

> A defined entity keeps its closed ancestor set after linking.

```lean
theorem stable_entity_ancestor
    {p c t : PartialSchema}
    {ety : EntityType}
    {entry : EntitySchemaEntry}
    (hlink : link p c = .ok t)
    (hentry : p.ets.find? ety = some (.defined entry)) :
    ∃ linkedEntry,
      t.ets.find? ety = some (.defined linkedEntry) ∧
      linkedEntry.ancestors = entry.ancestors
```

## Depends on

- [External/PartialSchema](partialschema.md)
- [EnvironmentValidator](../../validation/environmentvalidator.md)
- [Validation/Linker](../../validation/linker.md)

## Proof depends on

- [Lemmas about List.mapUnion operator](../data/mapunion.md)
- [Paths along a relation](../data/relation.md)
- [EnvironmentValidation](../validation-2/environmentvalidation.md)

## Sources

- [Cedar/Thm/External/Linker.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/Linker.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.External.Linker.json)
