---
catalog: module
lean: Cedar.Thm.instance_of_bool_type_refl, Cedar.Thm.instance_of_entity_type_refl, Cedar.Thm.instance_of_ext_type_refl, Cedar.Thm.instance_of_type_refl, Cedar.Thm.instance_of_request_type_refl, Cedar.Thm.instance_of_schema_refl, Cedar.Thm.instance_of_well_formed_env, Cedar.Thm.request_and_entities_validate_implies_instance_of_wf_schema, Cedar.Thm.instanceOfType_mono, Cedar.Thm.instanceOfType_record_contains, Cedar.Thm.instanceOfType_record_required, Cedar.Thm.instanceOfEntitySchemaEntry_mono, Cedar.Thm.instanceOfActionSchemaEntry_mono, Cedar.Thm.instanceOfActionSchemaEntry_find?, Cedar.Thm.instanceOfSchemaEntry_eq, Cedar.Thm.instanceOfSchemaEntry_attrs, Cedar.Thm.instanceOfSchemaEntry_actionEntity
statement: formalized
proof: formalized
---

# RequestEntityValidation

`Cedar.Thm.Validation.RequestEntityValidation`, in [Cedar/Thm/Validation/RequestEntityValidation.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/RequestEntityValidation.lean).

`Cedar.Thm.instance_of_bool_type_refl` (theorem, [line 20](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/RequestEntityValidation.lean#L20))

```lean
theorem instance_of_bool_type_refl {b : Bool} {bty : BoolType} :
  instanceOfBoolType b bty = true → InstanceOfBoolType b bty
```

`Cedar.Thm.instance_of_entity_type_refl` (theorem, [line 27](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/RequestEntityValidation.lean#L27))

```lean
theorem instance_of_entity_type_refl {e : EntityUID} {ety : EntityType} {env : TypeEnv} :
  instanceOfEntityType e ety env.schema = true → InstanceOfEntityType e ety env
```

`Cedar.Thm.instance_of_ext_type_refl` (theorem, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/RequestEntityValidation.lean#L36))

```lean
theorem instance_of_ext_type_refl {ext : Ext} {extty : ExtType} :
  instanceOfExtType ext extty = true → InstanceOfExtType ext extty
```

`Cedar.Thm.instance_of_type_refl` (theorem, [line 43](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/RequestEntityValidation.lean#L43))

```lean
theorem instance_of_type_refl {v : Value} {ty : CedarType} {env : TypeEnv} :
  instanceOfType v ty env.schema = true → InstanceOfType env v ty
```

`Cedar.Thm.instance_of_request_type_refl` (theorem, [line 156](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/RequestEntityValidation.lean#L156))

```lean
theorem instance_of_request_type_refl {request : Request} {env : TypeEnv}:
  instanceOfRequestType request env = true → InstanceOfRequestType request env
```

`Cedar.Thm.instance_of_schema_refl` (theorem, [line 171](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/RequestEntityValidation.lean#L171))

```lean
theorem instance_of_schema_refl {entities : Entities} {env : TypeEnv} :
  instanceOfSchema entities env = .ok () → InstanceOfSchema entities env
```

`Cedar.Thm.instance_of_well_formed_env` (theorem, [line 255](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/RequestEntityValidation.lean#L255))

```lean
theorem instance_of_well_formed_env {env : TypeEnv} {request : Request} {entities : Entities} :
  env.validateWellFormed = .ok () →
  requestMatchesEnvironment env request →
  entitiesMatchEnvironment env entities = .ok () →
  InstanceOfWellFormedEnvironment request entities env
```

`Cedar.Thm.request_and_entities_validate_implies_instance_of_wf_schema` (theorem, [line 272](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/RequestEntityValidation.lean#L272))

```lean
theorem request_and_entities_validate_implies_instance_of_wf_schema (schema : Schema) (request : Request) (entities : Entities) :
  schema.validateWellFormed = .ok () →
  validateRequest schema request = .ok () →
  validateEntities schema entities = .ok () →
  InstanceOfWellFormedSchema schema request entities
```

`Cedar.Thm.instanceOfType_mono` (theorem, [line 296](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/RequestEntityValidation.lean#L296))

> `instanceOfType` depends on its schema only through `instanceOfEntityType`.

```lean
theorem instanceOfType_mono {s₁ s₂ : Schema}
  (hmono : ∀ e ety, instanceOfEntityType e ety s₁ = true →
    instanceOfEntityType e ety s₂ = true)
  (v : Value) (ty : CedarType) (h : instanceOfType v ty s₁ = true) :
  instanceOfType v ty s₂ = true
```

`Cedar.Thm.instanceOfType_record_contains` (theorem, [line 359](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/RequestEntityValidation.lean#L359))

> A record valid against a record type has only attributes of that type.

```lean
theorem instanceOfType_record_contains {r : Map Attr Value} {rty : RecordType} {schema : Schema}
  {a : Attr}
  (h : instanceOfType (.record r) (.record rty) schema = true)
  (ha : r.contains a = true) :
  rty.contains a = true
```

`Cedar.Thm.instanceOfType_record_required` (theorem, [line 371](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/RequestEntityValidation.lean#L371))

> A record valid against a record type has each required attribute of that type.

```lean
theorem instanceOfType_record_required {r : Map Attr Value} {rty : RecordType} {schema : Schema}
  {a : Attr} {ty : CedarType}
  (h : instanceOfType (.record r) (.record rty) schema = true)
  (hrequired : rty.find? a = some (.required ty)) :
  r.contains a = true
```

`Cedar.Thm.instanceOfEntitySchemaEntry_mono` (theorem, [line 385](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/RequestEntityValidation.lean#L385))

> Entity-entry validation depends on its schema only through `instanceOfEntityType`.

```lean
theorem instanceOfEntitySchemaEntry_mono {env₁ env₂ : TypeEnv}
  {uid : EntityUID} {data : EntityData} {entry : EntitySchemaEntry}
  (h : instanceOfSchema.instanceOfEntitySchemaEntry env₁ uid data entry = .ok ())
  (hmono : ∀ e ety, instanceOfEntityType e ety env₁.schema = true →
    instanceOfEntityType e ety env₂.schema = true) :
  instanceOfSchema.instanceOfEntitySchemaEntry env₂ uid data entry = .ok ()
```

`Cedar.Thm.instanceOfActionSchemaEntry_mono` (theorem, [line 420](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/RequestEntityValidation.lean#L420))

> Action-entry validation depends on its schema only through the action's ancestors.

```lean
theorem instanceOfActionSchemaEntry_mono {env₁ env₂ : TypeEnv}
  {uid : EntityUID} {data : EntityData}
  (h : instanceOfSchema.instanceOfActionSchemaEntry env₁ uid data = .ok ())
  (hacts : ∀ entry, env₁.acts.find? uid = some entry →
    ∃ entry', env₂.acts.find? uid = some entry' ∧ entry'.ancestors = entry.ancestors) :
  instanceOfSchema.instanceOfActionSchemaEntry env₂ uid data = .ok ()
```

`Cedar.Thm.instanceOfActionSchemaEntry_find?` (theorem, [line 442](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/RequestEntityValidation.lean#L442))

> A valid action entity is an action of the schema.

```lean
theorem instanceOfActionSchemaEntry_find? {env : TypeEnv}
  {uid : EntityUID} {data : EntityData}
  (h : instanceOfSchema.instanceOfActionSchemaEntry env uid data = .ok ()) :
  ∃ entry, env.acts.find? uid = some entry
```

`Cedar.Thm.instanceOfSchemaEntry_eq` (theorem, [line 456](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/RequestEntityValidation.lean#L456))

> Validating an entity depends on the environment only through its entity and action schemas.

```lean
theorem instanceOfSchemaEntry_eq {env₁ env₂ : TypeEnv}
  (hets : env₁.ets = env₂.ets) (hacts : env₁.acts = env₂.acts) :
  instanceOfSchema.instanceOfSchemaEntry env₁ =
    instanceOfSchema.instanceOfSchemaEntry env₂
```

`Cedar.Thm.instanceOfSchemaEntry_attrs` (theorem, [line 468](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/RequestEntityValidation.lean#L468))

> A valid entity of a type the schema declares has attributes of that type.

```lean
theorem instanceOfSchemaEntry_attrs {env : TypeEnv} {uid : EntityUID}
  {data : EntityData} {entry : EntitySchemaEntry}
  (h : instanceOfSchema.instanceOfSchemaEntry env uid data = .ok ())
  (hfind : env.ets.find? uid.ty = some entry) :
  instanceOfType data.attrs (.record entry.attrs) env.schema = true
```

`Cedar.Thm.instanceOfSchemaEntry_actionEntity` (theorem, [line 481](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/RequestEntityValidation.lean#L481))

> In a well-formed environment, the entity of each action is valid.

```lean
theorem instanceOfSchemaEntry_actionEntity {env : TypeEnv} {uid : EntityUID}
  {entry : ActionSchemaEntry} (hwf : env.WellFormed) (hmem : (uid, entry) ∈ env.acts.toList) :
  instanceOfSchema.instanceOfSchemaEntry env uid (actionSchemaEntryToEntityData entry) =
    .ok ()
```

## Depends on

- [Thm/Validation/Validator](validator.md)
- [EnvironmentValidator](../../validation/environmentvalidator.md)
- [RequestEntityValidator](../../validation/requestentityvalidator.md)

## Proof depends on

- [EnvironmentValidation](environmentvalidation.md)

## Sources

- [Cedar/Thm/Validation/RequestEntityValidation.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/RequestEntityValidation.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Validation.RequestEntityValidation.json)
