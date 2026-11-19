---
catalog: module
lean: Cedar.SymCC.Opt.compileWithEffect, Cedar.SymCC.Opt.satisfiedPolicies, Cedar.SymCC.Opt.isAuthorized
statement: formalized
proof: formalized
---

# SymCCOpt/Authorizer

`Cedar.SymCCOpt.Authorizer`, in [Cedar/SymCCOpt/Authorizer.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Authorizer.lean).

`Cedar.SymCC.Opt.compileWithEffect` (definition, [line 25](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Authorizer.lean#L25))

```lean
public def compileWithEffect (effect : Effect) (policy : Policy) (εnv : SymEnv) : Result (Option CompileResult)
```

`Cedar.SymCC.Opt.satisfiedPolicies` (definition, [line 30](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Authorizer.lean#L30))

```lean
public def satisfiedPolicies (effect : Effect) (policies : Policies) (εnv : SymEnv) : Result CompileResult
```

`Cedar.SymCC.Opt.isAuthorized` (definition, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Authorizer.lean#L37))

```lean
public def isAuthorized (policies : Policies) (εnv : SymEnv) : Result CompileResult
```

## Depends on

- [Spec/Policy](../spec/policy.md)
- [SymCCOpt/Compiler](compiler.md)

## Sources

- [Cedar/SymCCOpt/Authorizer.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Authorizer.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.SymCCOpt.Authorizer.json)
