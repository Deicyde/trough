---
declaration: theorem
origin: cited
lean: TauCeti.exists_regular_lineDeriv_ofFun_apply_eq
statement: formalized
proof: formalized
---

# The directional derivatives of a function of locally finite variation are signed Radon measures

If every compact `K ⊆ Ω` has an open neighbourhood `U` on which `u` has finite total
variation, then for every direction `v` there are regular measures `ν₁` and `ν₂` on `Ω` with
`∂_v u (φ) = ∫ φ dν₁ - ∫ φ dν₂` for every test function `φ`, where `∂_v u` is the derivative of
the distribution `Distribution.ofFun Ω u μ ⊤`. If `u` is locally integrable on `Ω`, this is the
distributional derivative of `u`, `∂_v u (φ) = -∫ ∂_v φ * u`; otherwise `Distribution.ofFun` is
zero by convention and the statement is trivial. The measures are finite on compact subsets of
`Ω` but need not be finite.

```lean
TauCeti.exists_regular_lineDeriv_ofFun_apply_eq.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] {μ : MeasureTheory.Measure E}
  {Ω : TopologicalSpace.Opens E} {u : E → ℝ} [BorelSpace E]
  (hu : ∀ (K : Set E), IsCompact K → K ⊆ ↑Ω → ∃ U, K ⊆ ↑U ∧ TauCeti.totalVariationOn μ U u ≠ ⊤)
  (v : E) :
  ∃ ν₁ ν₂,
    ν₁.Regular ∧
      ν₂.Regular ∧
        ∀ (φ : TestFunction Ω ℝ ⊤),
          (LineDeriv.lineDerivOp v (Distribution.ofFun Ω u μ ⊤)) φ =
            ∫ (x : ↥Ω), φ ↑x ∂ν₁ - ∫ (x : ↥Ω), φ ↑x ∂ν₂
```

## Depends on

- [TauCeti.totalVariationOn](tauceti-totalvariationon.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_regular_lineDeriv_ofFun_apply_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/DerivativeMeasure.html#TauCeti.exists_regular_lineDeriv_ofFun_apply_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_regular_lineDeriv_ofFun_apply_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/DerivativeMeasure.html#TauCeti.exists_regular_lineDeriv_ofFun_apply_eq)
- [Source of `TauCeti.exists_regular_lineDeriv_ofFun_apply_eq` in TauCeti/Analysis/BoundedVariation/DerivativeMeasure.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/BoundedVariation/DerivativeMeasure.lean#L80)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
