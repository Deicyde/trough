---
declaration: def
origin: cited
lean: TauCeti.PreAdicSpace.isAdic
statement: formalized
---

# TauCeti.PreAdicSpace.isAdic

**Adic spaces** (Wedhorn, Definition 8.22): the objects of `𝒱`, the sheafy objects of
`𝒱^pre`, that admit an open cover by affinoid adic spaces. Since the restriction of a sheafy object
to an open is sheafy (`isSheafy_restrict`), an open cover by affinoid adic spaces is the same as an
open cover by open affinoid subspaces: an adic space is a sheafy locally affinoid object of
`𝒱^pre`. Their full subcategory of `𝒱^pre` is Wedhorn's category `(Adic)`, `TauCeti.AdicSpace`.

```lean
TauCeti.PreAdicSpace.isAdic.{u} : CategoryTheory.ObjectProperty TauCeti.PreAdicSpace
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PreAdicSpace.isAdic`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Adic.html#TauCeti.PreAdicSpace.isAdic).

## Sources

- [Tau Ceti documentation: `TauCeti.PreAdicSpace.isAdic`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Adic.html#TauCeti.PreAdicSpace.isAdic)
- [Source of `TauCeti.PreAdicSpace.isAdic` in TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Adic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Adic.lean#L210)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/AdicSpaces/STATUS.md)
