---
catalog: module
lean: Cedar.Thm.intoCompiledPolicySet_correctness, Cedar.Thm.cp_compile_produces_the_right_policy, Cedar.Thm.cpset_compile_produces_the_right_policies, Cedar.Thm.cp_compile_produces_the_right_env, Cedar.Thm.cpset_compile_produces_the_right_env, Cedar.Thm.cp_compile_produces_the_right_term, Cedar.Thm.cpset_compile_produces_the_right_term, Cedar.Thm.cp_compile_produces_the_right_footprint, Cedar.Thm.cpset_compile_produces_the_right_footprint, Cedar.Thm.cp_compile_produces_the_right_acyclicity, Cedar.Thm.cpset_compile_produces_the_right_acyclicity, Cedar.Thm.flatMap_allPolicies_policy, Cedar.Thm.flatMap_allPolicies_policies
statement: formalized
proof: formalized
---

# Opt/CompiledPolicies

`Cedar.Thm.SymCC.Opt.CompiledPolicies`, in [Cedar/Thm/SymCC/Opt/CompiledPolicies.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/CompiledPolicies.lean).

> Some lemmas about `CompiledPolicy`, `CompiledPolicySet`, and `CompiledPolicies`.

`Cedar.Thm.intoCompiledPolicySet_correctness` (theorem, [line 48](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/CompiledPolicies.lean#L48))

> Toplevel theorem about the correctness of `CompiledPolicy.intoCompiledPolicySet`
>
> Compiling to a `CompiledPolicy` and then using `intoCompiledPolicySet` should give
> exactly the same result as compiling with `CompiledPolicySet.compile` directly

```lean
theorem intoCompiledPolicySet_correctness {p : Policy} {s : CompiledSchema} {reqty : Validation.RequestType} :
  (do
    let cp ← CompiledPolicy.compile p s reqty
    pure cp.intoCompiledPolicySet
  ) = CompiledPolicySet.compile [p] s reqty
```

`Cedar.Thm.cp_compile_produces_the_right_policy` (theorem, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/CompiledPolicies.lean#L69))

> The `.policy` of a `CompiledPolicy` is exactly the policy produced by `wellTypedPolicy`

```lean
theorem cp_compile_produces_the_right_policy {p wp : Policy} {cp : CompiledPolicy} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicy.compile p s reqty = .ok cp →
  wellTypedPolicy p (s.typeEnv reqty) = .ok wp →
  cp.policy = wp
```

`Cedar.Thm.cpset_compile_produces_the_right_policies` (theorem, [line 81](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/CompiledPolicies.lean#L81))

> The `.policies` of a `CompiledPolicySet` is exactly the policies produced by `wellTypedPolicies`

```lean
theorem cpset_compile_produces_the_right_policies {ps wps : Policies} {cpset : CompiledPolicySet} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicySet.compile ps s reqty = .ok cpset →
  wellTypedPolicies ps (s.typeEnv reqty) = .ok wps →
  cpset.policies = wps
```

`Cedar.Thm.cp_compile_produces_the_right_env` (theorem, [line 90](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/CompiledPolicies.lean#L90))

```lean
theorem cp_compile_produces_the_right_env {p : Policy} {cp : CompiledPolicy} {s : CompiledSchema} {reqty : Validation.RequestType}  :
  CompiledPolicy.compile p s reqty = .ok cp →
  cp.εnv = s.symEnv reqty
```

`Cedar.Thm.cpset_compile_produces_the_right_env` (theorem, [line 98](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/CompiledPolicies.lean#L98))

```lean
theorem cpset_compile_produces_the_right_env {ps : Policies} {cpset : CompiledPolicySet} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicySet.compile ps s reqty = .ok cpset →
  cpset.εnv = s.symEnv reqty
```

`Cedar.Thm.cp_compile_produces_the_right_term` (theorem, [line 106](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/CompiledPolicies.lean#L106))

```lean
theorem cp_compile_produces_the_right_term {p wp : Policy} {cp : CompiledPolicy} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicy.compile p s reqty = .ok cp →
  wellTypedPolicy p (s.typeEnv reqty) = .ok wp →
  cp.term = SymCC.compile wp.toExpr (s.symEnv reqty)
```

`Cedar.Thm.cpset_compile_produces_the_right_term` (theorem, [line 120](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/CompiledPolicies.lean#L120))

```lean
theorem cpset_compile_produces_the_right_term {ps wps : Policies} {cpset : CompiledPolicySet} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicySet.compile ps s reqty = .ok cpset →
  wellTypedPolicies ps (s.typeEnv reqty) = .ok wps →
  cpset.term = SymCC.isAuthorized wps (s.symEnv reqty)
```

`Cedar.Thm.cp_compile_produces_the_right_footprint` (theorem, [line 135](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/CompiledPolicies.lean#L135))

```lean
theorem cp_compile_produces_the_right_footprint {p : Policy} {cp : CompiledPolicy} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicy.compile p s reqty = .ok cp →
  cp.footprint = footprint cp.policy.toExpr cp.εnv
```

`Cedar.Thm.cpset_compile_produces_the_right_footprint` (theorem, [line 149](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/CompiledPolicies.lean#L149))

```lean
theorem cpset_compile_produces_the_right_footprint {ps : Policies} {cpset : CompiledPolicySet} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicySet.compile ps s reqty = .ok cpset →
  cpset.footprint = footprints (cpset.policies.map Policy.toExpr) cpset.εnv
```

`Cedar.Thm.cp_compile_produces_the_right_acyclicity` (theorem, [line 163](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/CompiledPolicies.lean#L163))

```lean
theorem cp_compile_produces_the_right_acyclicity {p : Policy} {cp : CompiledPolicy} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicy.compile p s reqty = .ok cp →
  cp.acyclicity = cp.footprint.map (SymCC.acyclicity · cp.εnv.entities)
```

`Cedar.Thm.cpset_compile_produces_the_right_acyclicity` (theorem, [line 174](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/CompiledPolicies.lean#L174))

```lean
theorem cpset_compile_produces_the_right_acyclicity {ps : Policies} {cpset : CompiledPolicySet} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicySet.compile ps s reqty = .ok cpset →
  cpset.acyclicity = cpset.footprint.map (SymCC.acyclicity · cpset.εnv.entities)
```

`Cedar.Thm.flatMap_allPolicies_policy` (theorem, [line 185](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/CompiledPolicies.lean#L185))

```lean
theorem flatMap_allPolicies_policy {cps : List CompiledPolicy} :
  List.flatMap CompiledPolicies.allPolicies (cps.map CompiledPolicies.policy) = cps.map CompiledPolicy.policy
```

`Cedar.Thm.flatMap_allPolicies_policies` (theorem, [line 191](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/CompiledPolicies.lean#L191))

```lean
theorem flatMap_allPolicies_policies {cpsets : List CompiledPolicySet} :
  List.flatMap CompiledPolicies.allPolicies (cpsets.map CompiledPolicies.pset) = cpsets.flatMap CompiledPolicySet.policies
```

## Depends on

- [SymCCOpt/CompiledPolicies](../../../symccopt/compiledpolicies.md)

## Proof depends on

- [Opt/Authorizer](authorizer.md)

## Sources

- [Cedar/Thm/SymCC/Opt/CompiledPolicies.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/CompiledPolicies.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Opt.CompiledPolicies.json)
