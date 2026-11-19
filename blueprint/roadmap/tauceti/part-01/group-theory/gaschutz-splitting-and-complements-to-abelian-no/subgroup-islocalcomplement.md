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
- [Source of `Subgroup.IsLocalComplement` in TauCeti/GroupTheory/Complement/Local.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/Complement/Local.lean#L37)
- [Tau Ceti roadmap status: Gaschütz splitting and complements to abelian normal subgroups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FiniteGroupExtensionSplitting/STATUS.md)
