---
declaration: theorem
origin: cited
lean: TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary_comp_morseBoundary_eq_zero_iff
statement: formalized
proof: formalized
---

# `∂² = 0` reduces to counting broken trajectories

The mod-two Morse boundary squares to
zero exactly when, between any two critical points, the number of broken index-two trajectories
is even.

```lean
TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary_comp_morseBoundary_eq_zero_iff.{u_1, u_2}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {M : Type u_2}
  [TopologicalSpace M] [ChartedSpace E M] [IsManifold (modelWithCornersSelf ℝ E) (↑⊤) M]
  [CompactSpace M] [T2Space M] {f : M → ℝ} {X : (x : M) → TangentSpace (modelWithCornersSelf ℝ E) x}
  {hX : TauCeti.IsAdaptedPseudoGradient f X} (h : hX.IsMorseSmale)
  (hf : TauCeti.IsMorse (modelWithCornersSelf ℝ E) f) :
  h.morseBoundary hf ∘ₗ h.morseBoundary hf = 0 ↔
    ∀ (p r : ↑(TauCeti.criticalPoints (modelWithCornersSelf ℝ E) f)),
      Even (hX.morseBrokenTrajectorySet ↑p ↑r).ncard
```

## Depends on

- [The mod-two Morse boundary](the-mod-two-morse-boundary.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary_comp_morseBoundary_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Boundary/Square.html#TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary_comp_morseBoundary_eq_zero_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary_comp_morseBoundary_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Boundary/Square.html#TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary_comp_morseBoundary_eq_zero_iff)
- [Source of `TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary_comp_morseBoundary_eq_zero_iff` in TauCeti/Geometry/Manifold/Morse/Boundary/Square.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Morse/Boundary/Square.lean#L130)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HeegaardFloer/STATUS.md)
