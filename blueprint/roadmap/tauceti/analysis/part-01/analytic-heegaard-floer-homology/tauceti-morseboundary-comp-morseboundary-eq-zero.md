---
declaration: theorem
origin: cited
lean: TauCeti.morseBoundary_comp_morseBoundary_eq_zero_iff
statement: formalized
proof: formalized
---

# TauCeti.morseBoundary_comp_morseBoundary_eq_zero_iff

The mod-two Morse boundary squares to zero exactly when, between any two critical points,
the number of broken index-two trajectories is even.

```lean
TauCeti.morseBoundary_comp_morseBoundary_eq_zero_iff.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {f : E → ℝ} {K : NNReal} (hfs : ContDiff ℝ 2 f)
  (hf : LipschitzWith K (gradient f)) (hM : TauCeti.HasNondegenerateCriticalPointsOn f Set.univ)
  (hcompact : ∀ (c : ℝ), IsCompact {z | f z ≤ c}) (htr : TauCeti.IsMorseSmale f hf) :
  TauCeti.morseBoundary hfs hf hM hcompact htr ∘ₗ TauCeti.morseBoundary hfs hf hM hcompact htr = 0 ↔
    ∀ (p r : TauCeti.MorseCriticalPoint f), Even (TauCeti.morseBrokenTrajectorySet hf ↑p ↑r).ncard
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Morse form of the convergence theorem](../../part-02/calculus/part-01/the-morse-form-of-the-convergence-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.morseBoundary_comp_morseBoundary_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Boundary/Square.html#TauCeti.morseBoundary_comp_morseBoundary_eq_zero_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.morseBoundary_comp_morseBoundary_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Boundary/Square.html#TauCeti.morseBoundary_comp_morseBoundary_eq_zero_iff)
- [Source of `TauCeti.morseBoundary_comp_morseBoundary_eq_zero_iff` in TauCeti/Analysis/Calculus/Morse/Boundary/Square.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/Morse/Boundary/Square.lean#L200)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/HeegaardFloer/STATUS.md)
