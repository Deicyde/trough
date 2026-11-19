---
declaration: def
origin: cited
lean: Distribution.massMeasure
statement: formalized
---

# Distribution.massMeasure

The **mass measure** `‖T‖` of a real-valued linear map `T` on test functions with locally
finite mass: the regular Borel measure on `Ω` whose value on `Ω ∩ U`, for `U` open, is the local
mass of `T` on `U` (`Distribution.massMeasure_preimage_coe`). It dominates evaluation,
`|T φ| ≤ ∫ ‖φ‖ d‖T‖` (`Distribution.enorm_apply_le_lintegral_massMeasure`), and is the least
outer regular measure doing so (`Distribution.massMeasure_le_of_enorm_apply_le`). If `T` does not
have locally finite mass, it is the zero measure by convention.

```lean
Distribution.massMeasure.{u_1, u_2, u_3} {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  {Ω : TopologicalSpace.Opens E} {n : ℕ∞} {𝓕 : Type u_3} [FunLike 𝓕 (TestFunction Ω F n) ℝ]
  [LinearMapClass 𝓕 ℝ (TestFunction Ω F n) ℝ] [MeasurableSpace E] [BorelSpace E] (T : 𝓕) :
  MeasureTheory.Measure ↥Ω
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Distribution.massMeasure`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Mass/Measure.html#Distribution.massMeasure).

## Sources

- [Tau Ceti documentation: `Distribution.massMeasure`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Mass/Measure.html#Distribution.massMeasure)
- [Source of `Distribution.massMeasure` in TauCeti/Analysis/Distribution/Mass/Measure.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Distribution/Mass/Measure.lean#L212)
- [Tau Ceti roadmap status: Integral currents, geometric homology and minimizing hypersurfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricCurrents/STATUS.md)
