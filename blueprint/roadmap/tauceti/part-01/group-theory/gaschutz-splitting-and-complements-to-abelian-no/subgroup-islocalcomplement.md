---
declaration: structure
origin: cited
lean: Subgroup.IsLocalComplement
statement: formalized
---

# Subgroup.IsLocalComplement

`K` is a local complement of `N` in `H` if their intersection is trivial and their join is
`H`. Normality is not part of this lattice-theoretic definition.

```lean
Subgroup.IsLocalComplement.{u_1} {G : Type u_1} [Group G] (N K H : Subgroup G) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Subgroup.IsLocalComplement`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Complement/Local.html#Subgroup.IsLocalComplement).

## Sources

- [Tau Ceti documentation: `Subgroup.IsLocalComplement`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Complement/Local.html#Subgroup.IsLocalComplement)
- [Source of `Subgroup.IsLocalComplement` in TauCeti/GroupTheory/Complement/Local.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Complement/Local.lean#L30)
- [Tau Ceti roadmap status: Gaschütz splitting and complements to abelian normal subgroups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FiniteGroupExtensionSplitting/STATUS.md)
