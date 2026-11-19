---
catalog: module
lean: Cedar.Thm.verifyMatchesEquivalent_wbepq, Cedar.Thm.verifyMatchesImplies_wbepq, Cedar.Thm.verifyMatchesDisjoint_wbepq
statement: formalized
proof: formalized
---

# VerifyEvaluatePairQueries

`Cedar.Thm.SymCC.Verifier.VerifyEvaluatePairQueries`, in [Cedar/Thm/SymCC/Verifier/VerifyEvaluatePairQueries.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluatePairQueries.lean).

> This file proves that `verifyEvaluatePair` queries are well-behaved.
> -

`Cedar.Thm.verifyMatchesEquivalent_wbepq` (theorem, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluatePairQueries.lean#L46))

```lean
theorem verifyMatchesEquivalent_wbepq :
  WellBehavedEvaluatePairQuery
    (λ t₁ t₂ =>
      let t₁matches := eq t₁ (⊙true)
      let t₂matches := eq t₂ (⊙true)
      eq t₁matches t₂matches)
    (λ r₁ r₂ => (r₁ == .ok true) == (r₂ == .ok true))
```

`Cedar.Thm.verifyMatchesImplies_wbepq` (theorem, [line 149](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluatePairQueries.lean#L149))

```lean
theorem verifyMatchesImplies_wbepq :
  WellBehavedEvaluatePairQuery
    (λ t₁ t₂ =>
      let t₁matches := eq t₁ (⊙true)
      let t₂matches := eq t₂ (⊙true)
      implies t₁matches t₂matches)
    (λ r₁ r₂ => (r₁ != .ok true) || (r₂ == .ok true))
```

`Cedar.Thm.verifyMatchesDisjoint_wbepq` (theorem, [line 247](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluatePairQueries.lean#L247))

```lean
theorem verifyMatchesDisjoint_wbepq :
  WellBehavedEvaluatePairQuery
    (λ t₁ t₂ =>
      let t₁matches := eq t₁ (⊙true)
      let t₂matches := eq t₂ (⊙true)
      not (and t₁matches t₂matches))
    (λ r₁ r₂ => !((r₁ == .ok true) && (r₂ == .ok true)))
```

## Depends on

- [VerifyEvaluatePair](verifyevaluatepair.md)

## Proof depends on

- [VerifyEvaluateQueries](verifyevaluatequeries.md)

## Sources

- [Cedar/Thm/SymCC/Verifier/VerifyEvaluatePairQueries.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluatePairQueries.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Verifier.VerifyEvaluatePairQueries.json)
