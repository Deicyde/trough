---
declaration: structure
origin: cited
lean: Equidecomp.Equipartition
statement: formalized
---

# Equidecomp.Equipartition

An *equipartition* of `X` for an action of `G`: a finite set of pairs `(Aᵢ, gᵢ)` of a nonempty
source piece `Aᵢ : Set X` and a group element `gᵢ : G`, such that the source pieces `Aᵢ` are
pairwise disjoint and the target pieces `gᵢ • Aᵢ` are pairwise disjoint. When `G` is a group
acting on `X`, moving each `Aᵢ` by `gᵢ` is then an equidecomposition of the union of the `Aᵢ` with
the union of the `gᵢ • Aᵢ` (see `Equidecomp.Equipartition.toEquidecomp`).

```lean
Equidecomp.Equipartition.{u_1, u_2} (X : Type u_1) (G : Type u_2) [SMul G X] : Type (max u_1 u_2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Equidecomp.Equipartition`](https://taucetiproject.org/docs/TauCeti/Algebra/Group/Action/Equipartition.html#Equidecomp.Equipartition).

## Sources

- [Tau Ceti documentation: `Equidecomp.Equipartition`](https://taucetiproject.org/docs/TauCeti/Algebra/Group/Action/Equipartition.html#Equidecomp.Equipartition)
- [Source of `Equidecomp.Equipartition` in TauCeti/Algebra/Group/Action/Equipartition.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Group/Action/Equipartition.lean#L82)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AmenableGroups/STATUS.md)
