---
declaration: def
origin: cited
lean: TauCeti.smoothSingularSubcomplex
statement: formalized
---

# TauCeti.smoothSingularSubcomplex

The smooth singular simplices of `M`: those singular simplices which, read on the
full-dimensional standard simplex, are smooth in the sense of maps on arbitrary subsets. They form a
subcomplex of the singular simplicial set, since every simplicial operator is the restriction of a
smooth map of the ambient Euclidean spaces.

```lean
TauCeti.smoothSingularSubcomplex.{u, u_1, u_2} {E : Type u_1} {H : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [TopologicalSpace H] (I : ModelWithCorners ℝ E H) (M : Type u)
  [TopologicalSpace M] [ChartedSpace H M] : (TopCat.toSSet.obj ↧M).Subcomplex
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.smoothSingularSubcomplex`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/Basic.html#TauCeti.smoothSingularSubcomplex).

## Sources

- [Tau Ceti documentation: `TauCeti.smoothSingularSubcomplex`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/Basic.html#TauCeti.smoothSingularSubcomplex)
- [Source of `TauCeti.smoothSingularSubcomplex` in TauCeti/Geometry/Manifold/SmoothSingular/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/SmoothSingular/Basic.lean#L75)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
