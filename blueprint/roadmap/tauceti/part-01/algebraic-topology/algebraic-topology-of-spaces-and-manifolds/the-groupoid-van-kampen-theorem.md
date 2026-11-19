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
- [Source of `TauCeti.FundamentalGroupoid.isColimitCechCocone` in TauCeti/AlgebraicTopology/FundamentalGroupoid/Cech/Colimit.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/FundamentalGroupoid/Cech/Colimit.lean#L122)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AlgebraicTopology/STATUS.md)
