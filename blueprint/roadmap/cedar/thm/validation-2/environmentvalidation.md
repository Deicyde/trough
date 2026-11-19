---
catalog: module
lean: Cedar.Thm.entity_type_validate_well_formed_is_sound, Cedar.Thm.validate_attrs_well_formed_is_sound, Cedar.Thm.type_validate_well_formed_is_sound, Cedar.Thm.type_validate_lifted_is_sound, Cedar.Thm.standard_schema_entry_validate_well_formed_is_sound, Cedar.Thm.entity_schema_entry_validate_well_formed_is_sound, Cedar.Thm.entity_schema_validate_well_formed_is_sound, Cedar.Thm.action_schema_entry_validate_well_formed_is_sound, Cedar.Thm.action_schema_validate_acyclic_action_hierarchy_is_sound, Cedar.Thm.action_schema_validate_transitive_action_hierarchy_is_sound, Cedar.Thm.action_schema_validate_well_formed_is_sound, Cedar.Thm.request_type_validate_well_formed_is_sound, Cedar.Thm.env_validate_well_formed_is_sound, Cedar.Thm.environment_some_mem_environments, Cedar.Thm.entity_type_validate_well_formed_is_complete, Cedar.Thm.validate_attrs_well_formed_is_complete, Cedar.Thm.type_validate_well_formed_is_complete, Cedar.Thm.type_validate_lifted_is_complete, Cedar.Thm.standard_schema_entry_validate_well_formed_is_complete, Cedar.Thm.entity_schema_entry_validate_well_formed_is_complete, Cedar.Thm.entity_schema_validate_well_formed_is_complete, Cedar.Thm.action_schema_entry_validate_well_formed_is_complete, Cedar.Thm.action_schema_validate_acyclic_action_hierarchy_is_complete, Cedar.Thm.action_schema_validate_transitive_action_hierarchy_is_complete, Cedar.Thm.action_schema_validate_well_formed_is_complete, Cedar.Thm.request_type_validate_well_formed_is_complete, Cedar.Thm.env_validate_well_formed_is_complete, Cedar.Thm.mem_environments, Cedar.Thm.schema_validate_well_formed_is_complete
statement: formalized
proof: formalized
---

# EnvironmentValidation

`Cedar.Thm.Validation.EnvironmentValidation`, in [Cedar/Thm/Validation/EnvironmentValidation.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean).

> This file proves that various `*.validateWellFormed` functions
> correctly implement their spec versions.

`Cedar.Thm.entity_type_validate_well_formed_is_sound` (theorem, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L39))

```lean
theorem entity_type_validate_well_formed_is_sound
  {env : TypeEnv} {ety : EntityType}
  (hok : EntityType.validateWellFormed env ety = .ok ()) :
  EntityType.WellFormed env ety
```

`Cedar.Thm.validate_attrs_well_formed_is_sound` (theorem, [line 70](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L70))

```lean
theorem validate_attrs_well_formed_is_sound
  {env : TypeEnv} {rty} {attr : Attr} {qty : QualifiedType}
  (hwf : (Map.mk rty).WellFormed)
  (hok : validateAttrsWellFormed env rty = .ok ())
  (hfind : (Map.mk rty).find? attr = some qty) :
  QualifiedType.WellFormed env qty
```

`Cedar.Thm.type_validate_well_formed_is_sound` (theorem, [line 133](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L133))

```lean
theorem type_validate_well_formed_is_sound
  {env : TypeEnv} {ty : CedarType}
  (hok : ty.validateWellFormed env = .ok ()) :
  CedarType.WellFormed env ty
```

`Cedar.Thm.type_validate_lifted_is_sound` (theorem, [line 179](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L179))

```lean
theorem type_validate_lifted_is_sound
  {ty : CedarType}
  (hok : ty.validateLifted = .ok ()) :
  CedarType.IsLifted ty
```

`Cedar.Thm.standard_schema_entry_validate_well_formed_is_sound` (theorem, [line 225](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L225))

```lean
theorem standard_schema_entry_validate_well_formed_is_sound
  {env : TypeEnv} {entry : StandardSchemaEntry}
  (hok : entry.validateWellFormed env = .ok ()) :
  StandardSchemaEntry.WellFormed env entry
```

`Cedar.Thm.entity_schema_entry_validate_well_formed_is_sound` (theorem, [line 272](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L272))

```lean
theorem entity_schema_entry_validate_well_formed_is_sound
  {env : TypeEnv} {entry : EntitySchemaEntry}
  (hok : entry.validateWellFormed env = .ok ()) :
  EntitySchemaEntry.WellFormed env entry
```

`Cedar.Thm.entity_schema_validate_well_formed_is_sound` (theorem, [line 296](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L296))

```lean
theorem entity_schema_validate_well_formed_is_sound
  {env : TypeEnv} {ets : EntitySchema}
  (hok : ets.validateWellFormed env = .ok ()) :
  EntitySchema.WellFormed env ets
```

`Cedar.Thm.action_schema_entry_validate_well_formed_is_sound` (theorem, [line 315](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L315))

```lean
theorem action_schema_entry_validate_well_formed_is_sound
  {env : TypeEnv} {entry : ActionSchemaEntry}
  (hok : entry.validateWellFormed env = .ok ()) :
  ActionSchemaEntry.WellFormed env entry
```

`Cedar.Thm.action_schema_validate_acyclic_action_hierarchy_is_sound` (theorem, [line 378](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L378))

```lean
theorem action_schema_validate_acyclic_action_hierarchy_is_sound
  {acts : ActionSchema}
  (hok : acts.validateAcyclicActionHierarchy = .ok ()) :
  ActionSchema.AcyclicActionHierarchy acts
```

`Cedar.Thm.action_schema_validate_transitive_action_hierarchy_is_sound` (theorem, [line 395](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L395))

```lean
theorem action_schema_validate_transitive_action_hierarchy_is_sound
  {acts : ActionSchema}
  (hok : acts.validateTransitiveActionHierarchy = .ok ()) :
  ActionSchema.TransitiveActionHierarchy acts
```

`Cedar.Thm.action_schema_validate_well_formed_is_sound` (theorem, [line 416](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L416))

```lean
theorem action_schema_validate_well_formed_is_sound
  {env : TypeEnv} {acts : ActionSchema}
  (hok : acts.validateWellFormed env = .ok ()) :
  ActionSchema.WellFormed env acts
```

`Cedar.Thm.request_type_validate_well_formed_is_sound` (theorem, [line 466](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L466))

```lean
theorem request_type_validate_well_formed_is_sound
  {env : TypeEnv} {reqty : RequestType}
  (hok : reqty.validateWellFormed env = .ok ()) :
  RequestType.WellFormed env reqty
```

`Cedar.Thm.env_validate_well_formed_is_sound` (theorem, [line 498](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L498))

```lean
theorem env_validate_well_formed_is_sound
  {env : TypeEnv}
  (hok : env.validateWellFormed = .ok ()) :
  TypeEnv.WellFormed env
```

`Cedar.Thm.environment_some_mem_environments` (theorem, [line 527](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L527))

```lean
theorem environment_some_mem_environments {schema : Schema}
  {principal resource : EntityType} {action : EntityUID} {env : TypeEnv}
  (h : schema.environment? principal resource action = .some env) :
  env ∈ schema.environments
```

> ### Completeness: well-formed environments pass the executable checks

`Cedar.Thm.entity_type_validate_well_formed_is_complete` (theorem, [line 552](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L552))

```lean
theorem entity_type_validate_well_formed_is_complete
  {env : TypeEnv} {ety : EntityType}
  (hwf : EntityType.WellFormed env ety) :
  EntityType.validateWellFormed env ety = .ok ()
```

`Cedar.Thm.validate_attrs_well_formed_is_complete` (theorem, [line 568](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L568))

```lean
theorem validate_attrs_well_formed_is_complete
  {env : TypeEnv} {rty : List (Attr × QualifiedType)}
  (hwf : ∀ attr qty, (attr, qty) ∈ rty → QualifiedType.WellFormed env qty) :
  validateAttrsWellFormed env rty = .ok ()
```

`Cedar.Thm.type_validate_well_formed_is_complete` (theorem, [line 600](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L600))

```lean
theorem type_validate_well_formed_is_complete
  {env : TypeEnv} {ty : CedarType}
  (hwf : CedarType.WellFormed env ty) :
  ty.validateWellFormed env = .ok ()
```

`Cedar.Thm.type_validate_lifted_is_complete` (theorem, [line 627](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L627))

```lean
theorem type_validate_lifted_is_complete
  {ty : CedarType}
  (hlifted : CedarType.IsLifted ty) :
  ty.validateLifted = .ok ()
```

`Cedar.Thm.standard_schema_entry_validate_well_formed_is_complete` (theorem, [line 659](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L659))

```lean
theorem standard_schema_entry_validate_well_formed_is_complete
  {env : TypeEnv} {entry : StandardSchemaEntry}
  (hwf : StandardSchemaEntry.WellFormed env entry) :
  entry.validateWellFormed env = .ok ()
```

`Cedar.Thm.entity_schema_entry_validate_well_formed_is_complete` (theorem, [line 680](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L680))

```lean
theorem entity_schema_entry_validate_well_formed_is_complete
  {env : TypeEnv} {entry : EntitySchemaEntry}
  (hwf : EntitySchemaEntry.WellFormed env entry) :
  entry.validateWellFormed env = .ok ()
```

`Cedar.Thm.entity_schema_validate_well_formed_is_complete` (theorem, [line 691](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L691))

```lean
theorem entity_schema_validate_well_formed_is_complete
  {env : TypeEnv} {ets : EntitySchema}
  (hwf : EntitySchema.WellFormed env ets) :
  ets.validateWellFormed env = .ok ()
```

`Cedar.Thm.action_schema_entry_validate_well_formed_is_complete` (theorem, [line 704](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L704))

```lean
theorem action_schema_entry_validate_well_formed_is_complete
  {env : TypeEnv} {entry : ActionSchemaEntry}
  (hwf : ActionSchemaEntry.WellFormed env entry) :
  entry.validateWellFormed env = .ok ()
```

`Cedar.Thm.action_schema_validate_acyclic_action_hierarchy_is_complete` (theorem, [line 730](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L730))

```lean
theorem action_schema_validate_acyclic_action_hierarchy_is_complete
  {acts : ActionSchema}
  (hmap : Map.WellFormed acts)
  (hacyclic : ActionSchema.AcyclicActionHierarchy acts) :
  acts.validateAcyclicActionHierarchy = .ok ()
```

`Cedar.Thm.action_schema_validate_transitive_action_hierarchy_is_complete` (theorem, [line 742](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L742))

```lean
theorem action_schema_validate_transitive_action_hierarchy_is_complete
  {acts : ActionSchema}
  (hmap : Map.WellFormed acts)
  (htransitive : ActionSchema.TransitiveActionHierarchy acts) :
  acts.validateTransitiveActionHierarchy = .ok ()
```

`Cedar.Thm.action_schema_validate_well_formed_is_complete` (theorem, [line 760](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L760))

```lean
theorem action_schema_validate_well_formed_is_complete
  {env : TypeEnv} {acts : ActionSchema}
  (hwf : ActionSchema.WellFormed env acts) :
  acts.validateWellFormed env = .ok ()
```

`Cedar.Thm.request_type_validate_well_formed_is_complete` (theorem, [line 778](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L778))

```lean
theorem request_type_validate_well_formed_is_complete
  {env : TypeEnv} {reqty : RequestType}
  (hwf : RequestType.WellFormed env reqty) :
  reqty.validateWellFormed env = .ok ()
```

`Cedar.Thm.env_validate_well_formed_is_complete` (theorem, [line 787](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L787))

```lean
theorem env_validate_well_formed_is_complete
  {env : TypeEnv}
  (hwf : TypeEnv.WellFormed env) :
  env.validateWellFormed = .ok ()
```

`Cedar.Thm.mem_environments` (theorem, [line 801](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L801))

> Every environment of a schema has the schema's maps and the request type of
> one of its actions.

```lean
theorem mem_environments {schema : Schema} {env : TypeEnv}
  (h : env ∈ schema.environments) :
  env.ets = schema.ets ∧ env.acts = schema.acts ∧
  ∃ entry, (env.reqty.action, entry) ∈ schema.acts.toList ∧
    env.reqty.principal ∈ entry.appliesToPrincipal ∧
    env.reqty.resource ∈ entry.appliesToResource ∧
    env.reqty.context = entry.context
```

`Cedar.Thm.schema_validate_well_formed_is_complete` (theorem, [line 825](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean#L825))

> A schema passes the well-formedness check when its maps are well-formed in each
> of its environments.

```lean
theorem schema_validate_well_formed_is_complete
  {schema : Schema}
  (hwf : ∀ env ∈ schema.environments, env.ets.WellFormed env ∧ env.acts.WellFormed env) :
  schema.validateWellFormed = .ok ()
```

## Depends on

- [Typechecker/WF](typechecker-2/wf.md)
- [EnvironmentValidator](../../validation/environmentvalidator.md)

## Proof depends on

- [Thm/Data/LT](../data/lt.md)

## Sources

- [Cedar/Thm/Validation/EnvironmentValidation.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/EnvironmentValidation.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Validation.EnvironmentValidation.json)
