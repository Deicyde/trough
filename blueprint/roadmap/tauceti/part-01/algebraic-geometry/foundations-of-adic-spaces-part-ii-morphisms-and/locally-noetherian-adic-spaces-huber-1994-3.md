---
declaration: def
origin: cited
lean: TauCeti.AdicSpace.IsLocallyNoetherian
statement: formalized
---

# Locally noetherian adic spaces (Huber 1994, §3)

an adic space `X` is *locally noetherian*
when every point has an open affinoid neighbourhood of noetherian type, that is, an open `U` with
`X|_U ≅ Spa(A, A⁺)` for a complete Hausdorff Huber pair with `A` of noetherian type. By
`TauCeti.AdicSpace.IsLocallyNoetherian.spa` this covers sheafy `Spa(A, A⁺)` with `A` discrete or a
strongly noetherian Tate ring; a discrete `A` need not be noetherian.

```lean
TauCeti.AdicSpace.IsLocallyNoetherian.{u} (X : TauCeti.AdicSpace) : Prop
```

## Depends on

- [Adic spaces (Wedhorn, Definition 8.22)](../foundations-of-adic-spaces/adic-spaces-wedhorn-definition-8-22.md)

## Proof depends on

- [Ideals contained in supports](../foundations-of-adic-spaces/ideals-contained-in-supports.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AdicSpace.IsLocallyNoetherian`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/LocallyNoetherian.html#TauCeti.AdicSpace.IsLocallyNoetherian).

## Sources

- [Tau Ceti documentation: `TauCeti.AdicSpace.IsLocallyNoetherian`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/LocallyNoetherian.html#TauCeti.AdicSpace.IsLocallyNoetherian)
- [Source of `TauCeti.AdicSpace.IsLocallyNoetherian` in TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/LocallyNoetherian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/LocallyNoetherian.lean#L227)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
