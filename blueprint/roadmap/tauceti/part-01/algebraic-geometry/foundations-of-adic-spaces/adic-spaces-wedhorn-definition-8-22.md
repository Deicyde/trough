---
declaration: def
origin: cited
lean: TauCeti.PreAdicSpace.isAdic
statement: formalized
---

# Adic spaces (Wedhorn, Definition 8.22)

the objects of `𝒱`, the sheafy objects of
`𝒱^pre`, that admit an open cover by affinoid adic spaces. Since the restriction of a sheafy object
to an open is sheafy (`isSheafy_restrict`), an open cover by affinoid adic spaces is the same as an
open cover by open affinoid subspaces: an adic space is a sheafy locally affinoid object of
`𝒱^pre`. Their full subcategory of `𝒱^pre` is Wedhorn's category `(Adic)`, `TauCeti.AdicSpace`.

```lean
TauCeti.PreAdicSpace.isAdic.{u} : CategoryTheory.ObjectProperty TauCeti.PreAdicSpace
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Ideals contained in supports](ideals-contained-in-supports.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PreAdicSpace.isAdic`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Adic.html#TauCeti.PreAdicSpace.isAdic).

## Sources

- [Tau Ceti documentation: `TauCeti.PreAdicSpace.isAdic`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Adic.html#TauCeti.PreAdicSpace.isAdic)
- [Source of `TauCeti.PreAdicSpace.isAdic` in TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Adic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Adic.lean#L212)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AdicSpaces/STATUS.md)
