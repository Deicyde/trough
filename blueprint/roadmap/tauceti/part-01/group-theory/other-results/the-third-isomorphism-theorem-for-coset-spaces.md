---
declaration: def
origin: cited
lean: QuotientGroup.quotientQuotientEquivQuotientSup, QuotientAddGroup.quotientQuotientEquivQuotientSup
statement: formalized
---

# The third isomorphism theorem for coset spaces

For a normal `N` and an *arbitrary*
subgroup `H`, the cosets of the image of `H` in `G ⧸ N` are the cosets of `H ⊔ N` in `G`, both
directions sending the class of `g` to the class of `g`.

Mathlib's `QuotientGroup.quotientQuotientEquivQuotient` is the group isomorphism this
generalises: it asks for `N ≤ M` with `M` normal, so that both sides are groups and the map is a
homomorphism. Here neither side need be a group — `H` is unconstrained — and what survives is the
bijection of coset spaces, which is what a coset-indexed sum or family needs.

```lean
QuotientGroup.quotientQuotientEquivQuotientSup.{u_1} {G : Type u_1} [Group G] (H N : Subgroup G)
  [N.Normal] : (G ⧸ N) ⧸ Subgroup.map (QuotientGroup.mk' N) H ≃ G ⧸ H ⊔ N
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`QuotientGroup.quotientQuotientEquivQuotientSup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/QuotientGroup/ThirdIso.html#QuotientGroup.quotientQuotientEquivQuotientSup).

## Other forms

**The third isomorphism theorem for coset spaces, additive version.** Formalized in Tau Ceti as [`QuotientAddGroup.quotientQuotientEquivQuotientSup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/QuotientGroup/ThirdIso.html#QuotientAddGroup.quotientQuotientEquivQuotientSup).

```lean
QuotientAddGroup.quotientQuotientEquivQuotientSup.{u_1} {G : Type u_1} [AddGroup G]
  (H N : AddSubgroup G) [N.Normal] :
  (G ⧸ N) ⧸ AddSubgroup.map (QuotientAddGroup.mk' N) H ≃ G ⧸ H ⊔ N
```

## Sources

- [Tau Ceti documentation: `QuotientGroup.quotientQuotientEquivQuotientSup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/QuotientGroup/ThirdIso.html#QuotientGroup.quotientQuotientEquivQuotientSup)
- [Source of `QuotientGroup.quotientQuotientEquivQuotientSup` in TauCeti/GroupTheory/QuotientGroup/ThirdIso.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/QuotientGroup/ThirdIso.lean#L51)
