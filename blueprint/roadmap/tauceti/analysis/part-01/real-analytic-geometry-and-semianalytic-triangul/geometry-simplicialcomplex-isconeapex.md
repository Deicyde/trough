---
declaration: structure
origin: cited
lean: Geometry.SimplicialComplex.IsConeApex
statement: formalized
---

# Geometry.SimplicialComplex.IsConeApex

A point `p` is a *cone apex* for a geometric simplicial complex `K` if `p ∉ |K|` and every
segment from `p` to a point `y ∈ |K|` meets `|K|` only at `y`. These are the conditions under
which joining `p` to the faces of `K` gives a simplicial complex, the cone `K.cone p h`.

```lean
Geometry.SimplicialComplex.IsConeApex.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [Field 𝕜]
  [LinearOrder 𝕜] [AddCommGroup E] [_root_.Module 𝕜 E] (K : Geometry.SimplicialComplex 𝕜 E)
  (p : E) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Geometry.SimplicialComplex.IsConeApex`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/SimplicialComplex/Cone.html#Geometry.SimplicialComplex.IsConeApex).

## Sources

- [Tau Ceti documentation: `Geometry.SimplicialComplex.IsConeApex`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/SimplicialComplex/Cone.html#Geometry.SimplicialComplex.IsConeApex)
- [Source of `Geometry.SimplicialComplex.IsConeApex` in TauCeti/Analysis/Convex/SimplicialComplex/Cone.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Convex/SimplicialComplex/Cone.lean#L78)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
