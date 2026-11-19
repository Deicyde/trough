---
catalog: module
lean: Cedar.Validation.PartialSchema.validateEntities_ok_iff, Cedar.Validation.entity_reference_validation_soundness, Cedar.Validation.value_validation_soundness, Cedar.Validation.request_environment_soundness, Cedar.Validation.entity_validation_soundness, Cedar.Validation.request_validation_soundness, Cedar.Validation.entity_validation_completeness, Cedar.Validation.request_validation_completeness, Cedar.Validation.complete_request_validation_agreement, Cedar.Validation.complete_entity_validation_agreement
statement: formalized
proof: formalized
---

# PartialValidation

`Cedar.Thm.External.PartialValidation`, in [Cedar/Thm/External/PartialValidation.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialValidation.lean).

`Cedar.Validation.PartialSchema.validateEntities_ok_iff` (theorem, [line 74](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialValidation.lean#L74))

> Partial entity validation accepts a store exactly when no entity has an external
> type and every entity is valid in `wfEnv`.

```lean
theorem PartialSchema.validateEntities_ok_iff {ps : PartialSchema} {entities : Entities} :
    ps.validateEntities entities = .ok () ↔
      ∀ uid data, (uid, data) ∈ entities.toList →
        (∀ ancestors, ps.ets.find? uid.ty ≠ some (.external ancestors)) ∧
        instanceOfSchema.instanceOfSchemaEntry ps.wfEnv uid data = .ok ()
```

`Cedar.Validation.entity_reference_validation_soundness` (theorem, [line 96](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialValidation.lean#L96))

> An entity reference valid against a partial schema remains valid after linking.

```lean
theorem entity_reference_validation_soundness
    {p c t : PartialSchema}
    {uid : EntityUID}
    {ety : EntityType}
    (hlink : link p c = .ok t)
    (hvalid : instanceOfEntityType uid ety p.validationView = true) :
    instanceOfEntityType uid ety t.validationView = true
```

`Cedar.Validation.value_validation_soundness` (theorem, [line 121](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialValidation.lean#L121))

> A value valid against a partial schema remains valid after linking.

```lean
theorem value_validation_soundness
    {p c t : PartialSchema}
    {v : Value}
    {ty : CedarType}
    (hlink : link p c = .ok t)
    (hvalid : instanceOfType v ty p.validationView = true) :
    instanceOfType v ty t.validationView = true
```

`Cedar.Validation.request_environment_soundness` (theorem, [line 134](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialValidation.lean#L134))

> Linking keeps every request type of a well-formed partial schema: each request
> environment of its validation view has a counterpart in the result's.

```lean
theorem request_environment_soundness
    {p c t : PartialSchema}
    {env : TypeEnv}
    (hp : p.WellFormed)
    (hlink : link p c = .ok t)
    (henv : env ∈ p.validationView.environments) :
    { ets := t.validationView.ets, acts := t.validationView.acts, reqty := env.reqty } ∈
      t.validationView.environments
```

`Cedar.Validation.entity_validation_soundness` (theorem, [line 164](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialValidation.lean#L164))

> Entities valid against a partial schema remain valid after linking.

```lean
theorem entity_validation_soundness
    {p c t : PartialSchema}
    {entities : Entities}
    (hlink : link p c = .ok t)
    (hvalid : p.validateEntities entities = .ok ()) :
    t.validateEntities entities = .ok ()
```

`Cedar.Validation.request_validation_soundness` (theorem, [line 201](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialValidation.lean#L201))

> Requests valid against a partial schema remain valid after linking.

```lean
theorem request_validation_soundness
    {p c t : PartialSchema}
    {request : Request}
    (hp : p.WellFormed)
    (hlink : link p c = .ok t)
    (hvalid : p.validateRequest request = .ok ()) :
    t.validateRequest request = .ok ()
```

`Cedar.Validation.entity_validation_completeness` (theorem, [line 233](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialValidation.lean#L233))

> Entities valid against every complete linking extension are valid against the
> partial schema.

```lean
theorem entity_validation_completeness
    {p : PartialSchema}
    {entities : Entities}
    (hp : p.WellFormed)
    (hvalid : ∀ c t,
      c.WellFormed →
      link p c = .ok t →
      t.asSchema?.isSome = true →
      t.validateEntities entities = .ok ()) :
    p.validateEntities entities = .ok ()
```

`Cedar.Validation.request_validation_completeness` (theorem, [line 272](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialValidation.lean#L272))

> Requests valid against every complete linking extension are valid against the
> partial schema.

```lean
theorem request_validation_completeness
    {p : PartialSchema}
    {request : Request}
    (hp : p.WellFormed)
    (hvalid : ∀ c t,
      c.WellFormed →
      link p c = .ok t →
      t.asSchema?.isSome = true →
      t.validateRequest request = .ok ()) :
    p.validateRequest request = .ok ()
```

`Cedar.Validation.complete_request_validation_agreement` (theorem, [line 288](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialValidation.lean#L288))

> A complete partial schema validates requests exactly as the schema completing it.

```lean
theorem complete_request_validation_agreement
    {t : PartialSchema}
    {schema : Schema}
    {request : Request}
    (hcomplete : t.asSchema? = some schema) :
    t.validateRequest request = validateRequest schema request
```

`Cedar.Validation.complete_entity_validation_agreement` (theorem, [line 300](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialValidation.lean#L300))

> At a complete link, partial entity validation implies complete validation after
> adding the canonical entity for every action.

```lean
theorem complete_entity_validation_agreement
    {p c t : PartialSchema}
    {schema : Schema}
    {entities : Entities}
    (hp : p.WellFormed)
    (hc : c.WellFormed)
    (hlink : link p c = .ok t)
    (hcomplete : t.asSchema? = some schema)
    (hvalid : t.validateEntities entities = .ok ()) :
    validateEntities schema
      (entities ++ schema.acts.mapOnValues actionSchemaEntryToEntityData) = .ok ()
```

## Depends on

- [External/PartialSchema](partialschema.md)
- [Validation/Linker](../../validation/linker.md)

## Proof depends on

- [External/Linker](linker.md)
- [RequestEntityValidation](../validation-2/requestentityvalidation.md)

## Sources

- [Cedar/Thm/External/PartialValidation.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/External/PartialValidation.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.External.PartialValidation.json)
