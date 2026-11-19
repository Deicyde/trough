---
declaration: def
origin: cited
lean: TauCeti.FourTensor.ricci
statement: formalized
---

# TauCeti.FourTensor.ricci

The Ricci contraction `Ric(u, v) = tr (x, y ↦ r(x, u, y, v))` of a four-tensor, the metric
trace over its first and third arguments. In an orthonormal basis it is
`∑ᵢ r(eᵢ, u, eᵢ, v)`, see `TauCeti.FourTensor.ricci_apply_orthonormalBasis`.

```lean
TauCeti.FourTensor.ricci.{u_1} {V : Type u_1} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
  [FiniteDimensional ℝ V] : TauCeti.FourTensor V →ₗ[ℝ] LinearMap.BilinForm ℝ V
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FourTensor.ricci`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/AlgebraicCurvature/Basic.html#TauCeti.FourTensor.ricci).

## Sources

- [Tau Ceti documentation: `TauCeti.FourTensor.ricci`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/AlgebraicCurvature/Basic.html#TauCeti.FourTensor.ricci)
- [Source of `TauCeti.FourTensor.ricci` in TauCeti/Analysis/InnerProductSpace/AlgebraicCurvature/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/AlgebraicCurvature/Basic.lean#L354)
- [Tau Ceti roadmap status: Ricci flow, preserved curvature cones, and sphere theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RicciFlow/STATUS.md)
