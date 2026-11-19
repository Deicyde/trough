---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.isClosed_range_of_compact_estimate
statement: formalized
proof: formalized
---

# Peetre's lemma

a compact-error estimate gives closed range. Together with
`finiteDimensional_ker_of_compact_estimate`, this proves the upper semi-Fredholm property. No
completeness of the codomain or of the scalar field is required.

```lean
ContinuousLinearMap.isClosed_range_of_compact_estimate.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} {G : Type u_4} [NontriviallyNormedField 𝕜] [NormedAddCommGroup E]
  [NormedSpace 𝕜 E] [SeminormedAddCommGroup G] [NormedSpace 𝕜 G] {C : ℝ} [CompleteSpace E]
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] (T : E →L[𝕜] F) {K : E →L[𝕜] G}
  (hK : IsCompactOperator ⇑K) (hbound : ∀ (x : E), ‖x‖ ≤ C * ‖T x‖ + ‖K x‖) : IsClosed ↑(↑T).range
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Riesz's lemma, translated form](rieszs-lemma-translated-form.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.isClosed_range_of_compact_estimate`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Compact/Estimate.html#ContinuousLinearMap.isClosed_range_of_compact_estimate).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.isClosed_range_of_compact_estimate`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Compact/Estimate.html#ContinuousLinearMap.isClosed_range_of_compact_estimate)
- [Source of `ContinuousLinearMap.isClosed_range_of_compact_estimate` in TauCeti/Analysis/Normed/Operator/Compact/Estimate.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Operator/Compact/Estimate.lean#L143)
