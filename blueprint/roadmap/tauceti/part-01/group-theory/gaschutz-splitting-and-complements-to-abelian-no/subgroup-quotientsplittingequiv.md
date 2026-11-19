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
- [Source of `Subgroup.quotientSplittingEquiv` in TauCeti/GroupTheory/GroupExtension/Quotient/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/GroupExtension/Quotient/Basic.lean#L99)
- [Tau Ceti roadmap status: Gaschütz splitting and complements to abelian normal subgroups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FiniteGroupExtensionSplitting/STATUS.md)
