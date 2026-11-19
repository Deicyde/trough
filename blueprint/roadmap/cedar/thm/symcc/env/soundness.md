---
catalog: module
lean: Cedar.Thm.env_symbolize?_wf, Cedar.Thm.env_symbolize?_same, Cedar.Thm.ofEnv_soundness
statement: formalized
proof: formalized
---

# Env/Soundness

`Cedar.Thm.SymCC.Env.Soundness`, in [Cedar/Thm/SymCC/Env/Soundness.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Soundness.lean).

> This file contains the soundness theorems of `Sym.ofEnv`

`Cedar.Thm.env_symbolize?_wf` (theorem, [line 1585](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Soundness.lean#L1585))

```lean
theorem env_symbolize?_wf
  {Γ : TypeEnv} {env : Env}
  (hwf_env : env.StronglyWellFormed)
  (hinst : InstanceOfWellFormedEnvironment env.request env.entities Γ) :
  (env.symbolize? Γ).WellFormed (SymEnv.ofEnv Γ).entities
```

`Cedar.Thm.env_symbolize?_same` (theorem, [line 1605](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Soundness.lean#L1605))

```lean
theorem env_symbolize?_same
  {Γ : TypeEnv} {env : Env}
  (hwf_env : env.StronglyWellFormed)
  (hinst : InstanceOfWellFormedEnvironment env.request env.entities Γ) :
  env ∼ (SymEnv.ofEnv Γ).interpret (env.symbolize? Γ)
```

`Cedar.Thm.ofEnv_soundness` (theorem, [line 1615](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Soundness.lean#L1615))

```lean
theorem ofEnv_soundness
  {Γ : TypeEnv} {env : Env}
  (hwf_env : env.StronglyWellFormed)
  (hinst : InstanceOfWellFormedEnvironment env.request env.entities Γ) :
  env ∈ᵢ SymEnv.ofEnv Γ
```

## Depends on

- [Cedar/SymCC/Symbolizer](../../../symcc/part-01/symbolizer.md)
- [Strongly well-formed ancestor relations](../data/hierarchy.md)
- [Typechecker/Types](../../validation-2/typechecker-2/types.md)

## Proof depends on

- [UUF](../data/uuf.md)
- [Thm/SymCC/Decoder](../decoder.md)
- [Thm/SymCC/Symbolizer](../symbolizer.md)
- [Properties of the `Same` predicate on Terms](../term/same.md)

## Sources

- [Cedar/Thm/SymCC/Env/Soundness.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/Soundness.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Env.Soundness.json)
