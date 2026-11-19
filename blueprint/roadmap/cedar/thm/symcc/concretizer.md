---
catalog: module
lean: Cedar.Thm.exists_wf_env, Cedar.Thm.exists_wf_env_for_policies
statement: formalized
proof: formalized
---

# Concretizer

`Cedar.Thm.SymCC.Concretizer`, in [Cedar/Thm/SymCC/Concretizer.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer.lean).

> This file proves a key auxiliary lemma used to show the completeness of Cedar's
> symbolic compiler: for every symbolic environment `εnv` that is well-formed for
> an expression `x`, and for interpretation `I` that is well-formed for εnv, there
> is concrete environment `env` that is well-formed with respect to `x` and that
> corresponds to the interpretation of `εnv` under `I`. The concrete environment
> `env` is obtained by concretizing `εnv.interpret I` with respect to `x`.
> -

`Cedar.Thm.exists_wf_env` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer.lean#L35))

```lean
theorem exists_wf_env {x : Expr} {εnv : SymEnv} {I : Interpretation} :
  εnv.WellFormedFor x →
  I.WellFormed εnv.entities →
  ∃ (env : Env),
    env ∼ εnv.interpret I ∧
    env.WellFormedFor x
```

`Cedar.Thm.exists_wf_env_for_policies` (theorem, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer.lean#L52))

```lean
theorem exists_wf_env_for_policies {ps : Policies} {εnv : SymEnv} {I : Interpretation} :
  εnv.WellFormedForPolicies ps →
  I.WellFormed εnv.entities →
  ∃ (env : Env),
    env ∼ εnv.interpret I ∧
    env.WellFormedForPolicies ps
```

## Depends on

- [Well-formedness and interpretations](data/basic.md)

## Proof depends on

- [Lit](concretizer-2/lit.md)
- [Concretizer/WF](concretizer-2/wf.md)
- [Properties of interpretations on symbolic environments](env/interpret.md)

## Sources

- [Cedar/Thm/SymCC/Concretizer.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Concretizer.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.SymCC.Concretizer.json)
