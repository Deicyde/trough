---
declaration: def
origin: cited
lean: TauCeti.Manifold.scalarCurvatureOfJet
statement: formalized
---

# TauCeti.Manifold.scalarCurvatureOfJet

The **scalar curvature of a coordinate jet** `(g, ∂g, ∂²g)`: the contraction
`Σⱼₖ g^(jk) Σᵢ Rⁱᵢⱼₖ` of the curvature coefficients `riemannOfJet` against the inverse of the
Gram matrix `g`.

```lean
TauCeti.Manifold.scalarCurvatureOfJet.{u_1} {ι : Type u_1} [Fintype ι] [DecidableEq ι]
  (g : Matrix ι ι ℝ) (dg : ι → ι → ι → ℝ) (ddg : ι → ι → ι → ι → ℝ) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.scalarCurvatureOfJet`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Jet.html#TauCeti.Manifold.scalarCurvatureOfJet).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.scalarCurvatureOfJet`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Jet.html#TauCeti.Manifold.scalarCurvatureOfJet)
- [Source of `TauCeti.Manifold.scalarCurvatureOfJet` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Jet.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Jet.lean#L157)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
