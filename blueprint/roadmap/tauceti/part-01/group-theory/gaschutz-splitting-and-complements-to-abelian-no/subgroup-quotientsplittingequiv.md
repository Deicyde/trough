---
declaration: def
origin: cited
lean: Subgroup.quotientSplittingEquiv
statement: formalized
---

# Subgroup.quotientSplittingEquiv

Splittings of the quotient extension correspond bijectively to subgroup complements.

```lean
Subgroup.quotientSplittingEquiv.{u_1} {G : Type u_1} [Group G] (N : Subgroup G) [N.Normal] :
  N.quotientExtension.Splitting ≃ { D // N.IsComplement' D }
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Subgroup.quotientSplittingEquiv`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupExtension/Quotient/Basic.html#Subgroup.quotientSplittingEquiv).

## Sources

- [Tau Ceti documentation: `Subgroup.quotientSplittingEquiv`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupExtension/Quotient/Basic.html#Subgroup.quotientSplittingEquiv)
- [Source of `Subgroup.quotientSplittingEquiv` in TauCeti/GroupTheory/GroupExtension/Quotient/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/GroupExtension/Quotient/Basic.lean#L99)
- [Tau Ceti roadmap status: Gaschütz splitting and complements to abelian normal subgroups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FiniteGroupExtensionSplitting/STATUS.md)
