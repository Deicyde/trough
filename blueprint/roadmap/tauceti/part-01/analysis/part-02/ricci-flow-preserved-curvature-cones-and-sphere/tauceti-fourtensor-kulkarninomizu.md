---
declaration: def
origin: cited
lean: TauCeti.FourTensor.kulkarniNomizu
statement: formalized
---

# TauCeti.FourTensor.kulkarniNomizu

The Kulkarni–Nomizu product of two bilinear forms as a four-tensor, in the curvature
convention `r(u, v, z, w) = g(R(u, v)w, z)`:
`(h ⊙ k)(u, v, z, w) = h(u, z) k(v, w) + h(v, w) k(u, z) - h(u, w) k(v, z) - h(v, z) k(u, w)`.
It is `LinearMap.BilinForm.kulkarniNomizu` with its last two arguments interchanged.

```lean
TauCeti.FourTensor.kulkarniNomizu.{u_1} {V : Type u_1} [NormedAddCommGroup V] [NormedSpace ℝ V]
  [FiniteDimensional ℝ V] :
  LinearMap.BilinForm ℝ V →ₗ[ℝ] LinearMap.BilinForm ℝ V →ₗ[ℝ] TauCeti.FourTensor V
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FourTensor.kulkarniNomizu`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/AlgebraicCurvature/Basic.html#TauCeti.FourTensor.kulkarniNomizu).

## Sources

- [Tau Ceti documentation: `TauCeti.FourTensor.kulkarniNomizu`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/AlgebraicCurvature/Basic.html#TauCeti.FourTensor.kulkarniNomizu)
- [Source of `TauCeti.FourTensor.kulkarniNomizu` in TauCeti/Analysis/InnerProductSpace/AlgebraicCurvature/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/AlgebraicCurvature/Basic.lean#L309)
- [Tau Ceti roadmap status: Ricci flow, preserved curvature cones, and sphere theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RicciFlow/STATUS.md)
