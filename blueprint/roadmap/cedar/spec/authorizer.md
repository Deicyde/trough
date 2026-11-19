---
catalog: module
lean: Cedar.Spec.satisfied, Cedar.Spec.satisfiedWithEffect, Cedar.Spec.satisfiedPolicies, Cedar.Spec.hasError, Cedar.Spec.errored, Cedar.Spec.errorPolicies, Cedar.Spec.isAuthorized
statement: formalized
proof: formalized
---

# Spec/Authorizer

`Cedar.Spec.Authorizer`, in [Cedar/Spec/Authorizer.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Authorizer.lean).

> This file defines the Cedar authorizer.

`Cedar.Spec.satisfied` (definition, [line 29](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Authorizer.lean#L29))

```lean
public def satisfied (policy : Policy) (req : Request) (entities : Entities) : Bool
```

`Cedar.Spec.satisfiedWithEffect` (definition, [line 32](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Authorizer.lean#L32))

```lean
public def satisfiedWithEffect (effect : Effect) (policy : Policy) (req : Request) (entities : Entities) : Option PolicyID
```

`Cedar.Spec.satisfiedPolicies` (definition, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Authorizer.lean#L37))

```lean
public def satisfiedPolicies (effect : Effect) (policies : Policies) (req : Request) (entities : Entities) : Set PolicyID
```

`Cedar.Spec.hasError` (definition, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Authorizer.lean#L40))

```lean
public def hasError (policy : Policy) (req : Request) (entities : Entities) : Bool
```

`Cedar.Spec.errored` (definition, [line 50](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Authorizer.lean#L50))

> This function is analogous to `satisfiedWithEffect` in that it returns
> `Option PolicyID`, but not analogous to `satisfiedWithEffect` in that it does
> not consider the policy's effect.

```lean
public def errored (policy : Policy) (req : Request) (entities : Entities) : Option PolicyID
```

`Cedar.Spec.errorPolicies` (definition, [line 53](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Authorizer.lean#L53))

```lean
public def errorPolicies (policies : Policies) (req : Request) (entities : Entities) : Set PolicyID
```

`Cedar.Spec.isAuthorized` (definition, [line 56](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Authorizer.lean#L56))

```lean
public def isAuthorized (req : Request) (entities : Entities) (policies : Policies) : Response
```

## Depends on

- [Spec/Evaluator](evaluator.md)
- [Response](response.md)

## Sources

- [Cedar/Spec/Authorizer.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Authorizer.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Spec.Authorizer.json)
