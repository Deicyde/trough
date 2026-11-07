---
declaration: theorem
origin: cited
lean: Geometry.SimplicialComplex.space_cone_of_space_eq_intrinsicFrontier
statement: formalized
proof: formalized
---

# Geometry.SimplicialComplex.space\_cone\_of\_space\_eq\_intrinsicFrontier

Coning a triangulation of the intrinsic frontier of a compact convex set `C` to a point of the
intrinsic interior of `C` triangulates `C`: every point of `C` is either the apex or lies on a
segment from the apex to a point of the intrinsic frontier.

```lean
Geometry.SimplicialComplex.space_cone_of_space_eq_intrinsicFrontier.{u_1} {E : Type u_1}
  [AddCommGroup E] [_root_.Module ℝ E] [TopologicalSpace E] [IsTopologicalAddGroup E]
  [ContinuousSMul ℝ E] [T2Space E] [DecidableEq E] {K : Geometry.SimplicialComplex ℝ E} {C : Set E}
  {p : E} (hCc : IsCompact C) (hC : Convex ℝ C) (hK : K.space = intrinsicFrontier ℝ C)
  (hp : p ∈ intrinsicInterior ℝ C) : (K.cone p ⋯).space = C
```

## Depends on

- [Geometry.SimplicialComplex.cone](geometry-simplicialcomplex-cone.md)
- [Geometry.SimplicialComplex.IsConeApex](geometry-simplicialcomplex-isconeapex.md)

## Lean

Formalized in Tau Ceti as [`Geometry.SimplicialComplex.space_cone_of_space_eq_intrinsicFrontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/SimplicialComplex/Cone.html#Geometry.SimplicialComplex.space_cone_of_space_eq_intrinsicFrontier).

## Sources

- [Tau Ceti documentation: `Geometry.SimplicialComplex.space_cone_of_space_eq_intrinsicFrontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/SimplicialComplex/Cone.html#Geometry.SimplicialComplex.space_cone_of_space_eq_intrinsicFrontier)
- [Source of `Geometry.SimplicialComplex.space_cone_of_space_eq_intrinsicFrontier` in TauCeti/Analysis/Convex/SimplicialComplex/Cone.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Convex/SimplicialComplex/Cone.lean#L339)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
