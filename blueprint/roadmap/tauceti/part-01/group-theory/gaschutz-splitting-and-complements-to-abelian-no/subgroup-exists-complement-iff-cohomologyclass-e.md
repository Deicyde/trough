---
declaration: theorem
origin: cited
lean: Subgroup.exists_complement_iff_cohomologyClass_eq_zero
statement: formalized
proof: formalized
---

# Subgroup.exists_complement_iff_cohomologyClass_eq_zero

An abelian normal subgroup has a complement if and only if the class of its quotient
extension vanishes, for the quotient conjugation action and any normalized section.

```lean
Subgroup.exists_complement_iff_cohomologyClass_eq_zero {G : Type} [Group G] (N : Subgroup G)
  [N.Normal] [IsMulCommutative ↥N] (σ : N.quotientExtension.Section) (hσ : σ 1 = 1) :
  (∃ D, N.IsComplement' D) ↔ (TauCeti.GroupExtension.factorSet σ hσ ⋯).cohomologyClass = 0
```

## Depends on

- [Subgroup.quotientConjugationAction](subgroup-quotientconjugationaction.md)

## Proof depends on

- [Subgroup.quotientSplittingEquiv](subgroup-quotientsplittingequiv.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.exists_complement_iff_cohomologyClass_eq_zero`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupExtension/Quotient/Cohomology.html#Subgroup.exists_complement_iff_cohomologyClass_eq_zero).

## Sources

- [Tau Ceti documentation: `Subgroup.exists_complement_iff_cohomologyClass_eq_zero`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupExtension/Quotient/Cohomology.html#Subgroup.exists_complement_iff_cohomologyClass_eq_zero)
- [Source of `Subgroup.exists_complement_iff_cohomologyClass_eq_zero` in TauCeti/GroupTheory/GroupExtension/Quotient/Cohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/GroupExtension/Quotient/Cohomology.lean#L37)
- [Tau Ceti roadmap status: Gaschütz splitting and complements to abelian normal subgroups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FiniteGroupExtensionSplitting/STATUS.md)
