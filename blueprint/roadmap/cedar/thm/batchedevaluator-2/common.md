---
catalog: module
lean: Cedar.Thm.EntityLoader.WellBehaved, Cedar.Thm.environment?_schema, Cedar.Thm.actionEntities_refines, Cedar.Thm.as_partial_request_refines, Cedar.Thm.any_refines_empty_entities, Cedar.Thm.entities_refine_append, Cedar.Thm.direct_request_and_entities_refine
statement: formalized
proof: formalized
---

# Common

`Cedar.Thm.BatchedEvaluator.Common`, in [Cedar/Thm/BatchedEvaluator/Common.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Common.lean).

> Shared definitions and lemmas for batched evaluator theorems.

`Cedar.Thm.EntityLoader.WellBehaved` (abbreviation, [line 25](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Common.lean#L25))

> A well behaved entity loader
> 1. Loads all the requested entities, returning none for missing entities
> 2. Refines the backing entity store
>
> The first condition is required for convergence of
> batched evaluation, which has not been proven. It is unused
> in the code base at the moment.

```lean
abbrev EntityLoader.WellBehaved (store: Entities) (loader: EntityLoader) : Prop
```

`Cedar.Thm.environment?_schema` (theorem, [line 30](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Common.lean#L30))

> `Schema.environment?` carries the schema's entity and action types through unchanged.

```lean
theorem environment?_schema {schema : Schema} {pty rty : EntityType} {act : EntityUID}
  {env : TypeEnv} (h : schema.environment? pty rty act = .some env) :
  env.ets = schema.ets ∧ env.acts = schema.acts
```

`Cedar.Thm.actionEntities_refines` (theorem, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Common.lean#L41))

```lean
theorem actionEntities_refines {env : TypeEnv} {es : Entities}
  (hwf : env.WellFormed) (hinst : InstanceOfSchema es env) :
  EntitiesRefine es (actionEntities env.acts)
```

`Cedar.Thm.as_partial_request_refines` (theorem, [line 70](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Common.lean#L70))

```lean
theorem as_partial_request_refines {req : Request} :
  RequestRefines req req.asPartialRequest
```

`Cedar.Thm.any_refines_empty_entities` (theorem, [line 83](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Common.lean#L83))

```lean
theorem any_refines_empty_entities :
  EntitiesRefine es Data.Map.empty
```

`Cedar.Thm.entities_refine_append` (theorem, [line 89](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Common.lean#L89))

```lean
theorem entities_refine_append (es : Entities) (m1 m2 : PartialEntities) :
  EntitiesRefine es m1 → EntitiesRefine es m2 → EntitiesRefine es (m2 ++ m1)
```

`Cedar.Thm.direct_request_and_entities_refine` (theorem, [line 110](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Common.lean#L110))

```lean
theorem direct_request_and_entities_refine (req : Request) (es : Entities) :
  RequestAndEntitiesRefine req es req.asPartialRequest es.asPartial
```

## Depends on

- [TPE/BatchedEvaluator](../../tpe/batchedevaluator.md)
- [Thm/TPE/Input](../tpe-2/input.md)
- [Typechecker/Types](../validation-2/typechecker-2/types.md)

## Proof depends on

- [EnvironmentValidation](../validation-2/environmentvalidation.md)

## Sources

- [Cedar/Thm/BatchedEvaluator/Common.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Common.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.BatchedEvaluator.Common.json)
