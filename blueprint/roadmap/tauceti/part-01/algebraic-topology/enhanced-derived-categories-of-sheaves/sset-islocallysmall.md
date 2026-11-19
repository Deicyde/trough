---
declaration: class
origin: cited
lean: SSet.IsLocallySmall
statement: formalized
---

# SSet.IsLocallySmall

A simplicial set `X` is *locally `u`-small* when each right mapping space `Hom^R_X(x, y)` has
the homotopy type of a Kan complex in universe `u`. Only the homotopy types of the mapping
spaces are constrained, not the sizes of their sets of simplices. The notion is intended for
quasicategories, whose right mapping spaces model their spaces of maps.

```lean
SSet.IsLocallySmall.{u, v} (X : _root_.SSet) : Prop
```

## Depends on

- [TauCeti.HasSmallSpaceModel](tauceti-hassmallspacemodel.md)

## Lean

Formalized in Tau Ceti as [`SSet.IsLocallySmall`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Quasicategory/LocallySmall.html#SSet.IsLocallySmall).

## Sources

- [Tau Ceti documentation: `SSet.IsLocallySmall`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Quasicategory/LocallySmall.html#SSet.IsLocallySmall)
- [Source of `SSet.IsLocallySmall` in TauCeti/AlgebraicTopology/Quasicategory/LocallySmall.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Quasicategory/LocallySmall.lean#L62)
- [Tau Ceti roadmap status: Enhanced derived categories of sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EnhancedDerivedSheaves/STATUS.md)
