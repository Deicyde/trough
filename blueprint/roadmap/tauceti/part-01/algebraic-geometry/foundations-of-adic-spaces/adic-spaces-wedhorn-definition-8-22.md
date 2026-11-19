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

## Lean

Formalized in Tau Ceti as [`TauCeti.PreAdicSpace.isAdic`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Adic.html#TauCeti.PreAdicSpace.isAdic).

## Sources

- [Tau Ceti documentation: `TauCeti.PreAdicSpace.isAdic`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Adic.html#TauCeti.PreAdicSpace.isAdic)
- [Source of `TauCeti.PreAdicSpace.isAdic` in TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Adic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/Adic.lean#L212)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/AdicSpaces/STATUS.md)
