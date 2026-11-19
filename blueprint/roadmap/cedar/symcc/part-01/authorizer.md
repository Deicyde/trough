---
catalog: module
lean: Cedar.SymCC.compileWithEffect, Cedar.SymCC.satisfiedPolicies, Cedar.SymCC.isAuthorized
statement: formalized
proof: formalized
---

# Cedar/SymCC/Authorizer

`Cedar.SymCC.Authorizer`, in [Cedar/SymCC/Authorizer.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Authorizer.lean).

> This file defines the Cedar symbolic authorizer.
>
> The symbolic authorizer takes as input a set of policies and a symbolic
> environment. Given these inputs, it produces a Term encoding of the
> authorization decision for those policies. The output term is of type boolean.
> If this boolean term evaluates to true, then access is allowed. Otherwise,
> access is denied.

`Cedar.SymCC.compileWithEffect` (definition, [line 42](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Authorizer.lean#L42))

```lean
public def compileWithEffect (effect : Effect) (policy : Policy) (εnv : SymEnv) : Result (Option Term)
```

`Cedar.SymCC.satisfiedPolicies` (definition, [line 48](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Authorizer.lean#L48))

```lean
public def satisfiedPolicies (effect : Effect) (policies : Policies) (εnv : SymEnv) : Result Term
```

`Cedar.SymCC.isAuthorized` (definition, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Authorizer.lean#L52))

```lean
public def isAuthorized (policies : Policies) (εnv : SymEnv) : Result Term
```

## Depends on

- [Spec/Policy](../../spec/policy.md)
- [Cedar/SymCC/Compiler](compiler.md)

## Sources

- [Cedar/SymCC/Authorizer.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Authorizer.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.SymCC.Authorizer.json)
