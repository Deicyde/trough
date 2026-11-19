---
catalog: module
lean: Cedar.Thm.ofEnv_completeness
statement: formalized
proof: formalized
---

# Completeness

`Cedar.Thm.SymCC.Env.Completeness`, in [Cedar/Thm/SymCC/Env/Completeness.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Completeness.lean).

> This file contains the completeness theorems of `Sym.ofEnv`

`Cedar.Thm.ofEnv_completeness` (theorem, [line 1245](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Completeness.lean#L1245))

```lean
theorem ofEnv_completeness
  {Γ : TypeEnv} {env : Env}
  (hwf_Γ : Γ.WellFormed)
  (hwf_env : env.StronglyWellFormed)
  (henum_comp : Env.EnumCompleteFor env (SymEnv.ofEnv Γ))
  (hinst : env ∈ᵢ SymEnv.ofEnv Γ) :
  InstanceOfWellFormedEnvironment env.request env.entities Γ
```

## Depends on

- [Strongly well-formed ancestor relations](../data/hierarchy.md)
- [Typechecker/Types](../../validation-2/typechecker-2/types.md)

## Proof depends on

- [Properties of interpretations on symbolic environments](interpret.md)
- [ofEnv](ofenv.md)
- [ofType](../term/oftype.md)

## Sources

- [Cedar/Thm/SymCC/Env/Completeness.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Completeness.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Env.Completeness.json)
