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
- [Source of `TauCeti.Manifold.scalarCurvatureOfJet` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Jet.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Jet.lean#L157)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
