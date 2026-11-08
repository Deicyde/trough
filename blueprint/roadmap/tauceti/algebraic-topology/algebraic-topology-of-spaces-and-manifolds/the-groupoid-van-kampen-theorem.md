---
declaration: def
origin: cited
lean: TauCeti.FundamentalGroupoid.isColimitCechCocone
statement: formalized
---

# The groupoid van Kampen theorem

For an open cover of `X`, the fundamental groupoid of
`X` is the colimit of the fundamental groupoids of the nonempty finite intersections of members
of the cover.

```lean
TauCeti.FundamentalGroupoid.isColimitCechCocone.{u, v} {X : TopCat} {ι : Type u}
  {U : ι → TopologicalSpace.Opens ↑X} (hU : TopologicalSpace.IsOpenCover U) :
  CategoryTheory.Limits.IsColimit (TauCeti.FundamentalGroupoid.cechCocone U)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FundamentalGroupoid.isColimitCechCocone`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroupoid/Cech/Colimit.html#TauCeti.FundamentalGroupoid.isColimitCechCocone).

## Sources

- [Tau Ceti documentation: `TauCeti.FundamentalGroupoid.isColimitCechCocone`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroupoid/Cech/Colimit.html#TauCeti.FundamentalGroupoid.isColimitCechCocone)
- [Source of `TauCeti.FundamentalGroupoid.isColimitCechCocone` in TauCeti/AlgebraicTopology/FundamentalGroupoid/Cech/Colimit.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/FundamentalGroupoid/Cech/Colimit.lean#L138)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicTopology/STATUS.md)
