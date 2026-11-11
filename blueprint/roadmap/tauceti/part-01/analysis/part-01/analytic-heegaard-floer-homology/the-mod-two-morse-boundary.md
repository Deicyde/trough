---
declaration: def
origin: cited
lean: TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary
statement: formalized
---

# The mod-two Morse boundary

The `ZMod 2`-linear endomorphism of the free module on the
critical points of `f` sending a critical point `p` to the sum of the critical points `q` with
`ind q = ind p - 1`, each weighted by the number of trajectories from `p` to `q` modulo two.

```lean
TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary.{u_1, u_2} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {M : Type u_2}
  [TopologicalSpace M] [ChartedSpace E M] [IsManifold (modelWithCornersSelf ℝ E) (↑⊤) M]
  [CompactSpace M] [T2Space M] {f : M → ℝ} {X : (x : M) → TangentSpace (modelWithCornersSelf ℝ E) x}
  {hX : TauCeti.IsAdaptedPseudoGradient f X} (h : hX.IsMorseSmale)
  (hf : TauCeti.IsMorse (modelWithCornersSelf ℝ E) f) :
  (↑(TauCeti.criticalPoints (modelWithCornersSelf ℝ E) f) →₀ ZMod 2) →ₗ[ZMod 2]
    ↑(TauCeti.criticalPoints (modelWithCornersSelf ℝ E) f) →₀ ZMod 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Boundary/Basic.html#TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Boundary/Basic.html#TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary)
- [Source of `TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.morseBoundary` in TauCeti/Geometry/Manifold/Morse/Boundary/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Morse/Boundary/Basic.lean#L246)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HeegaardFloer/STATUS.md)
