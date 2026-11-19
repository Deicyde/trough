---
catalog: module
lean: Cedar.TPE.EntityLoader, Cedar.TPE.batchedEvaluateLoop, Cedar.TPE.actionEntities, Cedar.TPE.batchedEvaluate, Cedar.TPE.batchedAuthorizeLoop, Cedar.TPE.batchedAuthorize, Cedar.TPE.entityLoaderFor
statement: formalized
proof: formalized
---

# TPE/BatchedEvaluator

`Cedar.TPE.BatchedEvaluator`, in [Cedar/TPE/BatchedEvaluator.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/BatchedEvaluator.lean).

`Cedar.TPE.EntityLoader` (abbreviation, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/BatchedEvaluator.lean#L38))

> Loads everything requested by the set of entity ids,
>   returning `Option.none` for missing entities.
> Loading more entities than requested is okay.
> See `EntityLoader.WellBehaved` for a formal definition.

```lean
abbrev EntityLoader
```

`Cedar.TPE.batchedEvaluateLoop` (definition, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/BatchedEvaluator.lean#L46))

> The batched evaluation loop for a single residual expression.
>   1. Asks for any new entities referenced by the residual
>   2. Partially evaluates now that new entities are loaded
>   3. Exits if a value has been found or it hits the maximum iteration limit

```lean
def batchedEvaluateLoop
  (env : TypeEnv)
  (residual : Residual)
  (req : Request)
  (loader : EntityLoader)
  (store : PartialEntities)
  : Nat → Residual
```

`Cedar.TPE.actionEntities` (definition, [line 63](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/BatchedEvaluator.lean#L63))

```lean
def actionEntities (acts : ActionSchema) : PartialEntities
```

`Cedar.TPE.batchedEvaluate` (definition, [line 73](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/BatchedEvaluator.lean#L73))

> Evaluate a single cedar expression using an EntityLoader
> instead of a full Entities store.
> Performs a maximum of `iter` number of calls to `loader`,
> but may perform fewer when a value is found.

```lean
def batchedEvaluate
  (env : TypeEnv)
  (x : TypedExpr)
  (req : Request)
  (loader : EntityLoader)
  (iters : Nat)
  : Residual
```

`Cedar.TPE.batchedAuthorizeLoop` (definition, [line 87](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/BatchedEvaluator.lean#L87))

> The batched authorization loop for authorization over a list of policies.

```lean
def batchedAuthorizeLoop
  (env : TypeEnv)
  (residuals : List ResidualPolicy) (req : Request) (loader : EntityLoader)
  (store : PartialEntities) (n : Nat)
  : Response
```

`Cedar.TPE.batchedAuthorize` (definition, [line 112](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/BatchedEvaluator.lean#L112))

> Evaluate an authorization request using an EntityLoader instead of a full Entities store.
>
> Performs a maximum of `iter` number of calls to `loader`, but may perform fewer when an authorization decision is reached early.

```lean
def batchedAuthorize
  (schema : Schema)
  (policies : List Policy)
  (req : Request)
  (loader : EntityLoader)
  (iters : Nat)
  : Except Error Response
```

`Cedar.TPE.entityLoaderFor` (definition, [line 131](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/BatchedEvaluator.lean#L131))

> Create an entity loader for a given entity store.
> This is used for testing.

```lean
def entityLoaderFor (es: Entities) (uids : Set EntityUID)
```

## Depends on

- [Cedar/TPE/Authorizer](authorizer.md)

## Sources

- [Cedar/TPE/BatchedEvaluator.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/BatchedEvaluator.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.TPE.BatchedEvaluator.json)
