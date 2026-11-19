---
declaration: theorem
origin: cited
lean: TauCeti.AnalyticStage.exists_eval_eq_addChar_iff
statement: formalized
proof: formalized
---

# The analyticity criterion for the character `χ_t`

For a multiplicative norm, the
character `x ↦ (1 + t) ^ x` is the evaluation of a coefficient vector in `LA_h(K)` exactly when
`‖t‖ < r_h = p ^ (-1 / ((p - 1) pʰ))`.

```lean
TauCeti.AnalyticStage.exists_eval_eq_addChar_iff.{u_3, u_4} {p : ℕ} [hp : Fact (Nat.Prime p)]
  {K : Type u_3} [NormedRing K] [NormMulClass K] [NormOneClass K] [Algebra ℤ_[p] K]
  [IsBoundedSMul ℤ_[p] K] [_root_.Module ℚ_[p] K] [NormSMulClass ℚ_[p] K] [IsUltrametricDist K]
  [CompleteSpace K] (S : Type u_4) [Semiring S] [_root_.Module S K] [ContinuousConstSMul S K]
  [SMulCommClass ℤ_[p] S K] {h : ℕ} {t : K}
  (hr : Filter.Tendsto (fun x => t ^ x) Filter.atTop (nhds 0)) :
  (∃ f, ⇑((TauCeti.AnalyticStage.eval S) f) = ⇑(PadicInt.addChar_of_value_at_one t hr)) ↔
    ‖t‖ < TauCeti.amiceRadius p h
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Amice's theorem](amices-theorem.md)
- [Legendre's formula for `(pᵏ)!`](../../part-03/padics/legendres-formula-for-pk.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AnalyticStage.exists_eval_eq_addChar_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Character.html#TauCeti.AnalyticStage.exists_eval_eq_addChar_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.AnalyticStage.exists_eval_eq_addChar_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Character.html#TauCeti.AnalyticStage.exists_eval_eq_addChar_iff)
- [Source of `TauCeti.AnalyticStage.exists_eval_eq_addChar_iff` in TauCeti/NumberTheory/Padics/Distribution/Amice/Character.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Padics/Distribution/Amice/Character.lean#L424)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
