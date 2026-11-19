---
catalog: module
lean: Cedar.Thm.verifyEvaluateOpt_eqv_verifyEvaluate_ok, Cedar.Thm.verifyEvaluatePairOpt_eqv_verifyEvaluatePair_ok, Cedar.Thm.verifyIsAuthorizedOpt_eqv_verifyIsAuthorized_ok, Cedar.Thm.verifyNeverErrorsOpt_eqv_verifyNeverErrors_ok, Cedar.Thm.verifyAlwaysMatchesOpt_eqv_verifyAlwaysMatches_ok, Cedar.Thm.verifyNeverMatchesOpt_eqv_verifyNeverMatches_ok, Cedar.Thm.verifyMatchesEquivalentOpt_eqv_verifyMatchesEquivalent_ok, Cedar.Thm.verifyMatchesImpliesOpt_eqv_verifyMatchesImplies_ok, Cedar.Thm.verifyMatchesDisjointOpt_eqv_verifyMatchesDisjoint_ok, Cedar.Thm.verifyImpliesOpt_eqv_verifyImplies_ok, Cedar.Thm.verifyAlwaysAllowsOpt_eqv_verifyAlwaysAllows_ok, Cedar.Thm.verifyAlwaysDeniesOpt_eqv_verifyAlwaysDenies_ok, Cedar.Thm.verifyEquivalentOpt_eqv_verifyEquivalent_ok, Cedar.Thm.verifyDisjointOpt_eqv_verifyDisjoint_ok
statement: formalized
proof: formalized
---

# Opt/Verifier

`Cedar.Thm.SymCC.Opt.Verifier`, in [Cedar/Thm/SymCC/Opt/Verifier.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Verifier.lean).

> Proofs that the optimized functions in SymCCOpt.Verifier are equivalent to the unoptimized
> ones in SymCC.Verifier.

`Cedar.Thm.verifyEvaluateOpt_eqv_verifyEvaluate_ok` (theorem, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Verifier.lean#L37))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `verifyEvaluate` and `verifyEvaluateOpt` are
> equivalent.

```lean
theorem verifyEvaluateOpt_eqv_verifyEvaluate_ok {p wp : Policy} {cp : CompiledPolicy} {s : CompiledSchema} {reqty : Validation.RequestType} {φ : Term → Term} :
  CompiledPolicy.compile p s reqty = .ok cp →
  wellTypedPolicy p (s.typeEnv reqty) = .ok wp →
  verifyEvaluate φ wp (s.symEnv reqty) ~ .ok (verifyEvaluateOpt φ cp)
```

`Cedar.Thm.verifyEvaluatePairOpt_eqv_verifyEvaluatePair_ok` (theorem, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Verifier.lean#L61))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `verifyEvaluatePair` and `verifyEvaluatePairOpt` are
> equivalent.

```lean
theorem verifyEvaluatePairOpt_eqv_verifyEvaluatePair_ok {p₁ p₂ wp₁ wp₂ : Policy} {cp₁ cp₂ : CompiledPolicy} {s : CompiledSchema} {reqty : Validation.RequestType} {φ : Term → Term → Term} :
  CompiledPolicy.compile p₁ s reqty = .ok cp₁ →
  CompiledPolicy.compile p₂ s reqty = .ok cp₂ →
  wellTypedPolicy p₁ (s.typeEnv reqty) = .ok wp₁ →
  wellTypedPolicy p₂ (s.typeEnv reqty) = .ok wp₂ →
  verifyEvaluatePair φ wp₁ wp₂ (s.symEnv reqty) ~ .ok (verifyEvaluatePairOpt φ cp₁ cp₂)
```

`Cedar.Thm.verifyIsAuthorizedOpt_eqv_verifyIsAuthorized_ok` (theorem, [line 97](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Verifier.lean#L97))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `verifyIsAuthorized` and `verifyIsAuthorizedOpt` are
> equivalent.

```lean
theorem verifyIsAuthorizedOpt_eqv_verifyIsAuthorized_ok {ps₁ ps₂ wps₁ wps₂ : Policies} {cpset₁ cpset₂ : CompiledPolicySet} {s : CompiledSchema} {reqty : Validation.RequestType} {φ : Term → Term → Term} :
  CompiledPolicySet.compile ps₁ s reqty = .ok cpset₁ →
  CompiledPolicySet.compile ps₂ s reqty = .ok cpset₂ →
  wellTypedPolicies ps₁ (s.typeEnv reqty) = .ok wps₁ →
  wellTypedPolicies ps₂ (s.typeEnv reqty) = .ok wps₂ →
  verifyIsAuthorized φ wps₁ wps₂ (s.symEnv reqty) ~ .ok (verifyIsAuthorizedOpt φ cpset₁ cpset₂)
```

`Cedar.Thm.verifyNeverErrorsOpt_eqv_verifyNeverErrors_ok` (theorem, [line 133](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Verifier.lean#L133))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `verifyNeverErrors` and `verifyNeverErrorsOpt` are
> equivalent.

```lean
theorem verifyNeverErrorsOpt_eqv_verifyNeverErrors_ok {p wp : Policy} {cp : CompiledPolicy} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicy.compile p s reqty = .ok cp →
  wellTypedPolicy p (s.typeEnv reqty) = .ok wp →
  verifyNeverErrors wp (s.symEnv reqty) ~ .ok (verifyNeverErrorsOpt cp)
```

`Cedar.Thm.verifyAlwaysMatchesOpt_eqv_verifyAlwaysMatches_ok` (theorem, [line 146](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Verifier.lean#L146))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `verifyAlwaysMatches` and `verifyAlwaysMatchesOpt` are
> equivalent.

```lean
theorem verifyAlwaysMatchesOpt_eqv_verifyAlwaysMatches_ok {p wp : Policy} {cp : CompiledPolicy} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicy.compile p s reqty = .ok cp →
  wellTypedPolicy p (s.typeEnv reqty) = .ok wp →
  verifyAlwaysMatches wp (s.symEnv reqty) ~ .ok (verifyAlwaysMatchesOpt cp)
```

`Cedar.Thm.verifyNeverMatchesOpt_eqv_verifyNeverMatches_ok` (theorem, [line 159](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Verifier.lean#L159))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `verifyNeverMatches` and `verifyNeverMatchesOpt` are
> equivalent.

```lean
theorem verifyNeverMatchesOpt_eqv_verifyNeverMatches_ok {p wp : Policy} {cp : CompiledPolicy} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicy.compile p s reqty = .ok cp →
  wellTypedPolicy p (s.typeEnv reqty) = .ok wp →
  verifyNeverMatches wp (s.symEnv reqty) ~ .ok (verifyNeverMatchesOpt cp)
```

`Cedar.Thm.verifyMatchesEquivalentOpt_eqv_verifyMatchesEquivalent_ok` (theorem, [line 172](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Verifier.lean#L172))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `verifyMatchesEquivalent` and
> `verifyMatchesEquivalentOpt` are equivalent.

```lean
theorem verifyMatchesEquivalentOpt_eqv_verifyMatchesEquivalent_ok {p₁ p₂ wp₁ wp₂ : Policy} {cp₁ cp₂ : CompiledPolicy} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicy.compile p₁ s reqty = .ok cp₁ →
  CompiledPolicy.compile p₂ s reqty = .ok cp₂ →
  wellTypedPolicy p₁ (s.typeEnv reqty) = .ok wp₁ →
  wellTypedPolicy p₂ (s.typeEnv reqty) = .ok wp₂ →
  verifyMatchesEquivalent wp₁ wp₂ (s.symEnv reqty) ~ .ok (verifyMatchesEquivalentOpt cp₁ cp₂)
```

`Cedar.Thm.verifyMatchesImpliesOpt_eqv_verifyMatchesImplies_ok` (theorem, [line 187](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Verifier.lean#L187))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `verifyMatchesImplies` and
> `verifyMatchesImpliesOpt` are equivalent.

```lean
theorem verifyMatchesImpliesOpt_eqv_verifyMatchesImplies_ok {p₁ p₂ wp₁ wp₂ : Policy} {cp₁ cp₂ : CompiledPolicy} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicy.compile p₁ s reqty = .ok cp₁ →
  CompiledPolicy.compile p₂ s reqty = .ok cp₂ →
  wellTypedPolicy p₁ (s.typeEnv reqty) = .ok wp₁ →
  wellTypedPolicy p₂ (s.typeEnv reqty) = .ok wp₂ →
  verifyMatchesImplies wp₁ wp₂ (s.symEnv reqty) ~ .ok (verifyMatchesImpliesOpt cp₁ cp₂)
```

`Cedar.Thm.verifyMatchesDisjointOpt_eqv_verifyMatchesDisjoint_ok` (theorem, [line 202](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Verifier.lean#L202))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `verifyMatchesDisjoint` and
> `verifyMatchesDisjointOpt` are equivalent.

```lean
theorem verifyMatchesDisjointOpt_eqv_verifyMatchesDisjoint_ok {p₁ p₂ wp₁ wp₂ : Policy} {cp₁ cp₂ : CompiledPolicy} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicy.compile p₁ s reqty = .ok cp₁ →
  CompiledPolicy.compile p₂ s reqty = .ok cp₂ →
  wellTypedPolicy p₁ (s.typeEnv reqty) = .ok wp₁ →
  wellTypedPolicy p₂ (s.typeEnv reqty) = .ok wp₂ →
  verifyMatchesDisjoint wp₁ wp₂ (s.symEnv reqty) ~ .ok (verifyMatchesDisjointOpt cp₁ cp₂)
```

`Cedar.Thm.verifyImpliesOpt_eqv_verifyImplies_ok` (theorem, [line 217](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Verifier.lean#L217))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `verifyImplies` and `verifyImpliesOpt` are
> equivalent.

```lean
theorem verifyImpliesOpt_eqv_verifyImplies_ok {ps₁ ps₂ wps₁ wps₂ : Policies} {cpset₁ cpset₂ : CompiledPolicySet} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicySet.compile ps₁ s reqty = .ok cpset₁ →
  CompiledPolicySet.compile ps₂ s reqty = .ok cpset₂ →
  wellTypedPolicies ps₁ (s.typeEnv reqty) = .ok wps₁ →
  wellTypedPolicies ps₂ (s.typeEnv reqty) = .ok wps₂ →
  verifyImplies wps₁ wps₂ (s.symEnv reqty) ~ .ok (verifyImpliesOpt cpset₁ cpset₂)
```

`Cedar.Thm.verifyAlwaysAllowsOpt_eqv_verifyAlwaysAllows_ok` (theorem, [line 232](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Verifier.lean#L232))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `verifyAlwaysAllows` and `verifyAlwaysAllowsOpt` are
> equivalent.

```lean
theorem verifyAlwaysAllowsOpt_eqv_verifyAlwaysAllows_ok {ps wps : Policies} {cpset : CompiledPolicySet} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicySet.compile ps s reqty = .ok cpset →
  wellTypedPolicies ps (s.typeEnv reqty) = .ok wps →
  verifyAlwaysAllows wps (s.symEnv reqty) ~ .ok (verifyAlwaysAllowsOpt cpset)
```

`Cedar.Thm.verifyAlwaysDeniesOpt_eqv_verifyAlwaysDenies_ok` (theorem, [line 249](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Verifier.lean#L249))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `verifyAlwaysAllows` and `verifyAlwaysAllowsOpt` are
> equivalent.

```lean
theorem verifyAlwaysDeniesOpt_eqv_verifyAlwaysDenies_ok {ps wps : Policies} {cpset : CompiledPolicySet} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicySet.compile ps s reqty = .ok cpset →
  wellTypedPolicies ps (s.typeEnv reqty) = .ok wps →
  verifyAlwaysDenies wps (s.symEnv reqty) ~ .ok (verifyAlwaysDeniesOpt cpset)
```

`Cedar.Thm.verifyEquivalentOpt_eqv_verifyEquivalent_ok` (theorem, [line 268](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Verifier.lean#L268))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `verifyEquivalent` and `verifyEquivalentOpt` are
> equivalent.

```lean
theorem verifyEquivalentOpt_eqv_verifyEquivalent_ok {ps₁ ps₂ wps₁ wps₂ : Policies} {cpset₁ cpset₂ : CompiledPolicySet} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicySet.compile ps₁ s reqty = .ok cpset₁ →
  CompiledPolicySet.compile ps₂ s reqty = .ok cpset₂ →
  wellTypedPolicies ps₁ (s.typeEnv reqty) = .ok wps₁ →
  wellTypedPolicies ps₂ (s.typeEnv reqty) = .ok wps₂ →
  verifyEquivalent wps₁ wps₂ (s.symEnv reqty) ~ .ok (verifyEquivalentOpt cpset₁ cpset₂)
```

`Cedar.Thm.verifyDisjointOpt_eqv_verifyDisjoint_ok` (theorem, [line 283](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Verifier.lean#L283))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `verifyDisjoint` and `verifyDisjointOpt` are
> equivalent.

```lean
theorem verifyDisjointOpt_eqv_verifyDisjoint_ok {ps₁ ps₂ wps₁ wps₂ : Policies} {cpset₁ cpset₂ : CompiledPolicySet} {s : CompiledSchema} {reqty : Validation.RequestType} :
  CompiledPolicySet.compile ps₁ s reqty = .ok cpset₁ →
  CompiledPolicySet.compile ps₂ s reqty = .ok cpset₂ →
  wellTypedPolicies ps₁ (s.typeEnv reqty) = .ok wps₁ →
  wellTypedPolicies ps₂ (s.typeEnv reqty) = .ok wps₂ →
  verifyDisjoint wps₁ wps₂ (s.symEnv reqty) ~ .ok (verifyDisjointOpt cpset₁ cpset₂)
```

## Depends on

- [SymCCOpt/Verifier](../../../symccopt/verifier.md)
- [Opt/Asserts](asserts.md)

## Proof depends on

- [AllowDeny](allowdeny.md)
- [Opt/Enforcer](enforcer.md)

## Sources

- [Cedar/Thm/SymCC/Opt/Verifier.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Verifier.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Opt.Verifier.json)
