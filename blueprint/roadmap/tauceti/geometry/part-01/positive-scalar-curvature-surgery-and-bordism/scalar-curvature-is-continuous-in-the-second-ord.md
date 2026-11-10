---
declaration: theorem
origin: cited
lean: ContinuousAt.scalarCurvatureOfJet
statement: formalized
proof: formalized
---

# Scalar curvature is continuous in the second-order jet of the metric

The scalar curvature
of a coordinate jet depends continuously on the jet at every jet whose Gram matrix is invertible.

```lean
ContinuousAt.scalarCurvatureOfJet.{u_1, u_2} {ι : Type u_1} [Fintype ι] [DecidableEq ι]
  {X : Type u_2} [TopologicalSpace X] {g : X → Matrix ι ι ℝ} {dg : X → ι → ι → ι → ℝ}
  {ddg : X → ι → ι → ι → ι → ℝ} {x : X} (hg : ContinuousAt g x) (hdet : (g x).det ≠ 0)
  (hdg : ContinuousAt dg x) (hddg : ContinuousAt ddg x) :
  ContinuousAt (fun y => TauCeti.Manifold.scalarCurvatureOfJet (g y) (dg y) (ddg y)) x
```

## Depends on

- [TauCeti.Manifold.scalarCurvatureOfJet](tauceti-manifold-scalarcurvatureofjet.md)

## Lean

Formalized in Tau Ceti as [`ContinuousAt.scalarCurvatureOfJet`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Jet.html#ContinuousAt.scalarCurvatureOfJet).

## Sources

- [Tau Ceti documentation: `ContinuousAt.scalarCurvatureOfJet`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Jet.html#ContinuousAt.scalarCurvatureOfJet)
- [Source of `ContinuousAt.scalarCurvatureOfJet` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Jet.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Jet.lean#L216)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
