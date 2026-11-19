---
declaration: theorem
origin: cited
lean: Distribution.apply_eq_integral_polarDensity
statement: formalized
proof: formalized
---

# The polar decomposition `T = τ ‖T‖`

A functional `T` on test functions with locally
finite mass is integration of `τ(x) (φ x)` against its mass measure, where `τ` is its polar
density.

```lean
Distribution.apply_eq_integral_polarDensity.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F]
  {Ω : TopologicalSpace.Opens E} {T : TestFunction Ω F ⊤ →L[ℝ] ℝ}
  (hT : Distribution.HasLocallyFiniteMass ⇑T) (φ : TestFunction Ω F ⊤) :
  T φ = ∫ (x : ↥Ω), (Distribution.polarDensity T x) (φ ↑x) ∂Distribution.massMeasure T
```

## Depends on

- [Distribution.massMeasure](distribution-massmeasure.md)

## Lean

Formalized in Tau Ceti as [`Distribution.apply_eq_integral_polarDensity`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Mass/PolarDensity.html#Distribution.apply_eq_integral_polarDensity).

## Sources

- [Tau Ceti documentation: `Distribution.apply_eq_integral_polarDensity`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Mass/PolarDensity.html#Distribution.apply_eq_integral_polarDensity)
- [Source of `Distribution.apply_eq_integral_polarDensity` in TauCeti/Analysis/Distribution/Mass/PolarDensity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Distribution/Mass/PolarDensity.lean#L245)
- [Tau Ceti roadmap status: Integral currents, geometric homology and minimizing hypersurfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricCurrents/STATUS.md)
