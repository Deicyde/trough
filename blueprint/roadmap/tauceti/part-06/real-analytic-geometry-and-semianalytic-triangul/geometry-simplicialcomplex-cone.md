---
declaration: def
origin: cited
lean: Geometry.SimplicialComplex.cone
statement: formalized
---

# Geometry.SimplicialComplex.cone

The cone `pK` on a simplicial complex `K` with apex `p`. Its faces are the nonempty finite sets
whose vertices other than `p` form a face of `K` or are empty: the faces of `K`, the faces of `K`
with `p` adjoined, and the vertex `{p}`.

```lean
Geometry.SimplicialComplex.cone.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [Field 𝕜] [LinearOrder 𝕜]
  [IsStrictOrderedRing 𝕜] [AddCommGroup E] [_root_.Module 𝕜 E] [DecidableEq E]
  (K : Geometry.SimplicialComplex 𝕜 E) (p : E) (h : K.IsConeApex p) : Geometry.SimplicialComplex 𝕜 E
```

## Depends on

- [Geometry.SimplicialComplex.IsConeApex](geometry-simplicialcomplex-isconeapex.md)

## Lean

Formalized in Tau Ceti as [`Geometry.SimplicialComplex.cone`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/SimplicialComplex/Cone.html#Geometry.SimplicialComplex.cone).

## Sources

- [Tau Ceti documentation: `Geometry.SimplicialComplex.cone`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/SimplicialComplex/Cone.html#Geometry.SimplicialComplex.cone)
- [Source of `Geometry.SimplicialComplex.cone` in TauCeti/Analysis/Convex/SimplicialComplex/Cone.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Convex/SimplicialComplex/Cone.lean#L205)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
