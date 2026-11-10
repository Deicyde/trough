---
declaration: def
origin: cited
lean: TauCeti.homotopyOperator
statement: formalized
---

# TauCeti.homotopyOperator

The **homotopy operator** on forms on the cylinder `M × [0, 1]`: the `k`-form
`x ↦ ∫₀¹ φ(x, t)(∂ₜ, (·, 0)) dt` on `M` built from a `(k + 1)`-form `φ` on `M × [0, 1]`, where
`∂ₜ = (0, 1)` is the unit time vector and tangent vectors of `M` enter through
`ContinuousLinearMap.inl`. Equivalently `h φ = ∫₀¹ ιₜ^*(∂ₜ ⌟ φ) dt` for the slices
`ιₜ x = (x, t)`. For a `C¹` form with values in a Banach space on a `C²` manifold,
`d (h φ) + h (d φ) = ι₁^* φ - ι₀^* φ`
(`TauCeti.mextDeriv_homotopyOperator_add_homotopyOperator_mextDeriv`).

```lean
TauCeti.homotopyOperator.{u_1, u_2, u_3, u_4} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  {F : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [NormedAddCommGroup F]
  [NormedSpace ℝ F] {k : ℕ}
  (φ :
    TauCeti.RoughForm (I.prod (modelWithCornersEuclideanHalfSpace 1)) (M × ↑(Set.Icc 0 1)) F
      (k + 1)) :
  TauCeti.RoughForm I M F k
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.homotopyOperator`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/HomotopyOperator.html#TauCeti.homotopyOperator).

## Sources

- [Tau Ceti documentation: `TauCeti.homotopyOperator`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/HomotopyOperator.html#TauCeti.homotopyOperator)
- [Source of `TauCeti.homotopyOperator` in TauCeti/Geometry/Manifold/DifferentialForm/HomotopyOperator.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DifferentialForm/HomotopyOperator.lean#L93)
- [Tau Ceti roadmap status: Differential geometry — forms, de Rham cohomology, flows, and degree](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
