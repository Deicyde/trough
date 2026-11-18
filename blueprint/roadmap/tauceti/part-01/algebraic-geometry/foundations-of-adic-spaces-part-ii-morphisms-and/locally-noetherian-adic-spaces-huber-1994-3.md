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

## Lean

Formalized in Tau Ceti as [`TauCeti.AdicSpace.IsLocallyNoetherian`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/LocallyNoetherian.html#TauCeti.AdicSpace.IsLocallyNoetherian).

## Sources

- [Tau Ceti documentation: `TauCeti.AdicSpace.IsLocallyNoetherian`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/LocallyNoetherian.html#TauCeti.AdicSpace.IsLocallyNoetherian)
- [Source of `TauCeti.AdicSpace.IsLocallyNoetherian` in TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/LocallyNoetherian.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/LocallyNoetherian.lean#L227)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
