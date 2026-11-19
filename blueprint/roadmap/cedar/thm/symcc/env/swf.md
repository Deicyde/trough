---
catalog: module
lean: Cedar.Thm.swf_εnv_implies_wf, Cedar.Thm.swf_εnv_all_implies_swf_all, Cedar.Thm.swf_εnv_all_implies_wf_all, Cedar.Thm.swf_εnv_for_implies_wf_for, Cedar.Thm.swf_env_implies_wf, Cedar.Thm.swf_env_all_implies_swf_all, Cedar.Thm.swf_env_all_implies_wf_all, Cedar.Thm.swf_env_for_implies_wf_for, Cedar.Thm.swf_εnv_for_policy_iff_swf_for_polices, Cedar.Thm.swf_env_for_policy_iff_swf_for_polices, Cedar.Thm.swf_εnv_for_policies_iff_swf_for_append, Cedar.Thm.swf_env_for_policies_iff_swf_for_append, Cedar.Thm.swf_εnv_for_policies_implies_wf_for_policies, Cedar.Thm.swf_env_for_policies_implies_wf_for_policies
statement: formalized
proof: formalized
---

# Basic properties of strongly well-formed symbolic environments

`Cedar.Thm.SymCC.Env.SWF`, in [Cedar/Thm/SymCC/Env/SWF.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/SWF.lean).

> This file proves basic lemmas about the strong well-formedness predicate on environments.
> -

`Cedar.Thm.swf_εnv_implies_wf` (theorem, [line 30](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/SWF.lean#L30))

```lean
theorem swf_εnv_implies_wf {εnv : SymEnv} :
   εnv.StronglyWellFormed → εnv.WellFormed
```

`Cedar.Thm.swf_εnv_all_implies_swf_all` (theorem, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/SWF.lean#L36))

```lean
theorem swf_εnv_all_implies_swf_all {εnv : SymEnv} {xs : List Expr} :
  εnv.StronglyWellFormedForAll xs →
  ∀ x ∈ xs, εnv.StronglyWellFormedFor x
```

`Cedar.Thm.swf_εnv_all_implies_wf_all` (theorem, [line 43](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/SWF.lean#L43))

```lean
theorem swf_εnv_all_implies_wf_all {εnv : SymEnv} {xs : List Expr} :
  εnv.StronglyWellFormedForAll xs →
  ∀ x ∈ xs, εnv.WellFormedFor x
```

`Cedar.Thm.swf_εnv_for_implies_wf_for` (theorem, [line 50](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/SWF.lean#L50))

```lean
theorem swf_εnv_for_implies_wf_for {εnv : SymEnv} {x : Expr} :
  εnv.StronglyWellFormedFor x →
  εnv.WellFormedFor x
```

`Cedar.Thm.swf_env_implies_wf` (theorem, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/SWF.lean#L57))

```lean
theorem swf_env_implies_wf {env : Env} :
   env.StronglyWellFormed → env.WellFormed
```

`Cedar.Thm.swf_env_all_implies_swf_all` (theorem, [line 63](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/SWF.lean#L63))

```lean
theorem swf_env_all_implies_swf_all {env : Env} {xs : List Expr} :
  env.StronglyWellFormedForAll xs →
  ∀ x ∈ xs, env.StronglyWellFormedFor x
```

`Cedar.Thm.swf_env_all_implies_wf_all` (theorem, [line 70](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/SWF.lean#L70))

```lean
theorem swf_env_all_implies_wf_all {env : Env} {xs : List Expr} :
  env.StronglyWellFormedForAll xs →
  ∀ x ∈ xs, env.WellFormedFor x
```

`Cedar.Thm.swf_env_for_implies_wf_for` (theorem, [line 77](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/SWF.lean#L77))

```lean
theorem swf_env_for_implies_wf_for {env : Env} {x : Expr} :
  env.StronglyWellFormedFor x →
  env.WellFormedFor x
```

`Cedar.Thm.swf_εnv_for_policy_iff_swf_for_polices` (theorem, [line 84](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/SWF.lean#L84))

```lean
theorem swf_εnv_for_policy_iff_swf_for_polices {εnv : SymEnv} {p : Policy} :
  εnv.StronglyWellFormedForPolicy p ↔
  εnv.StronglyWellFormedForPolicies [p]
```

`Cedar.Thm.swf_env_for_policy_iff_swf_for_polices` (theorem, [line 97](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/SWF.lean#L97))

```lean
theorem swf_env_for_policy_iff_swf_for_polices {env : Env} {p : Policy} :
  env.StronglyWellFormedForPolicy p ↔
  env.StronglyWellFormedForPolicies [p]
```

`Cedar.Thm.swf_εnv_for_policies_iff_swf_for_append` (theorem, [line 110](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/SWF.lean#L110))

```lean
theorem swf_εnv_for_policies_iff_swf_for_append {εnv : SymEnv} {ps₁ ps₂ : Policies} :
  εnv.StronglyWellFormedForPolicies ps₁ ∧ εnv.StronglyWellFormedForPolicies ps₂ ↔
  εnv.StronglyWellFormedForPolicies (ps₁ ++ ps₂)
```

`Cedar.Thm.swf_env_for_policies_iff_swf_for_append` (theorem, [line 131](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/SWF.lean#L131))

```lean
theorem swf_env_for_policies_iff_swf_for_append {env : Env} {ps₁ ps₂ : Policies} :
  env.StronglyWellFormedForPolicies ps₁ ∧ env.StronglyWellFormedForPolicies ps₂ ↔
  env.StronglyWellFormedForPolicies (ps₁ ++ ps₂)
```

`Cedar.Thm.swf_εnv_for_policies_implies_wf_for_policies` (theorem, [line 152](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/SWF.lean#L152))

```lean
theorem swf_εnv_for_policies_implies_wf_for_policies {εnv : SymEnv} {ps : Policies} :
  εnv.StronglyWellFormedForPolicies ps →
  εnv.WellFormedForPolicies ps
```

`Cedar.Thm.swf_env_for_policies_implies_wf_for_policies` (theorem, [line 163](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/SWF.lean#L163))

```lean
theorem swf_env_for_policies_implies_wf_for_policies {env : Env} {ps : Policies} :
  env.StronglyWellFormedForPolicies ps →
  env.WellFormedForPolicies ps
```

## Depends on

- [Strongly well-formed ancestor relations](../data/hierarchy.md)

## Sources

- [Cedar/Thm/SymCC/Env/SWF.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Env/SWF.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Env.SWF.json)
