---
catalog: module
lean: Cedar.Thm.enforce_eq_map_union, Cedar.Thm.enforceCompiledPolicy_eqv_enforce_ok, Cedar.Thm.enforcePairCompiledPolicy_eqv_enforce_ok, Cedar.Thm.enforcePairCompiledPolicySet_eqv_enforce_ok
statement: formalized
proof: formalized
---

# Opt/Enforcer

`Cedar.Thm.SymCC.Opt.Enforcer`, in [Cedar/Thm/SymCC/Opt/Enforcer.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Enforcer.lean).

> Proofs that the optimized functions in SymCCOpt.Enforcer are equivalent to the unoptimized
> ones in SymCC.Enforcer.

`Cedar.Thm.enforce_eq_map_union` (theorem, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Enforcer.lean#L34))

> Rephrases the unoptimized `enforce` as the union of the acyclicity and transitivity constraints
> using the `Set.map`/`Set.product`/`∪` operations that the optimized `enforce*CompiledPolicy*`
> functions are defined with.

```lean
theorem enforce_eq_map_union {xs : List Expr} {εnv : SymEnv} :
  enforce xs εnv =
    (footprints xs εnv).map (acyclicity · εnv.entities) ∪
    ((footprints xs εnv).product (footprints xs εnv)).map (fun (t₁, t₂) => transitivity t₁ t₂ εnv.entities)
```

`Cedar.Thm.enforceCompiledPolicy_eqv_enforce_ok` (theorem, [line 56](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Enforcer.lean#L56))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `enforce` and `enforceCompiledPolicy` are equivalent.

```lean
theorem enforceCompiledPolicy_eqv_enforce_ok {p wp : Policy} {cp : CompiledPolicy} {s : CompiledSchema} {reqty : Validation.RequestType}  :
  CompiledPolicy.compile p s reqty = .ok cp →
  wellTypedPolicy p (s.typeEnv reqty) = .ok wp →
  enforce [wp.toExpr] (s.symEnv reqty) = enforceCompiledPolicy cp
```

`Cedar.Thm.enforcePairCompiledPolicy_eqv_enforce_ok` (theorem, [line 77](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Enforcer.lean#L77))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `enforce` and `enforcePairCompiledPolicy` are
> equivalent.

```lean
theorem enforcePairCompiledPolicy_eqv_enforce_ok {p₁ p₂ wp₁ wp₂ : Policy} {cp₁ cp₂ : CompiledPolicy} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicy.compile p₁ s reqty = .ok cp₁ →
  CompiledPolicy.compile p₂ s reqty = .ok cp₂ →
  wellTypedPolicy p₁ (s.typeEnv reqty) = .ok wp₁ →
  wellTypedPolicy p₂ (s.typeEnv reqty) = .ok wp₂ →
  enforce [wp₁.toExpr, wp₂.toExpr] (s.symEnv reqty) = enforcePairCompiledPolicy cp₁ cp₂
```

`Cedar.Thm.enforcePairCompiledPolicySet_eqv_enforce_ok` (theorem, [line 110](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Enforcer.lean#L110))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `enforce` and `enforcePairCompiledPolicySet` are
> equivalent.

```lean
theorem enforcePairCompiledPolicySet_eqv_enforce_ok {ps₁ ps₂ wps₁ wps₂ : Policies} {cpset₁ cpset₂ : CompiledPolicySet} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicySet.compile ps₁ s reqty = .ok cpset₁ →
  CompiledPolicySet.compile ps₂ s reqty = .ok cpset₂ →
  wellTypedPolicies ps₁ (s.typeEnv reqty) = .ok wps₁ →
  wellTypedPolicies ps₂ (s.typeEnv reqty) = .ok wps₂ →
  enforce (wps₁.map Policy.toExpr ++ wps₂.map Policy.toExpr) (s.symEnv reqty) = enforcePairCompiledPolicySet cpset₁ cpset₂
```

## Depends on

- [SymCCOpt/Enforcer](../../../symccopt/enforcer.md)

## Proof depends on

- [Opt/CompiledPolicies](compiledpolicies.md)

## Sources

- [Cedar/Thm/SymCC/Opt/Enforcer.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Enforcer.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Opt.Enforcer.json)
