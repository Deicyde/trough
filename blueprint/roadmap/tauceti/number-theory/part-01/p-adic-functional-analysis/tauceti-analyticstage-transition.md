---
declaration: def
origin: cited
lean: TauCeti.AnalyticStage.transition
statement: formalized
---

# TauCeti.AnalyticStage.transition

The transition `LA_h(E) → LA_{h+1}(E)`. The disc of `a ∈ ZMod (pʰ)` is the union of the discs
of the classes `a' = a + pʰ b`, `0 ≤ b < p`, in `ZMod (p ^ (h + 1))`, where `b = ⌊a'.val / pʰ⌋`.
On the disc of `a'` the coordinates are related by `w = b + p v`, and the transition re-expands
`∑ₖ c(a, k) wᵏ` in powers of `v`:

`d(a', j) = ∑ₖ (k choose j) b^(k - j) pʲ • c(a, k)`.

```lean
TauCeti.AnalyticStage.transition.{u_1, u_2} {p : ℕ} [hp : Fact (Nat.Prime p)] {h : ℕ} {E : Type u_1}
  [NormedAddCommGroup E] [_root_.Module ℤ_[p] E] [IsBoundedSMul ℤ_[p] E] [IsUltrametricDist E]
  [CompleteSpace E] (S : Type u_2) [Semiring S] [_root_.Module S E] [ContinuousConstSMul S E]
  [SMulCommClass ℤ_[p] S E] : TauCeti.AnalyticStage p h E →L[S] TauCeti.AnalyticStage p (h + 1) E
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AnalyticStage.transition`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/AnalyticStage.html#TauCeti.AnalyticStage.transition).

## Sources

- [Tau Ceti documentation: `TauCeti.AnalyticStage.transition`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/AnalyticStage.html#TauCeti.AnalyticStage.transition)
- [Source of `TauCeti.AnalyticStage.transition` in TauCeti/NumberTheory/Padics/Distribution/AnalyticStage.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/Distribution/AnalyticStage.lean#L376)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
