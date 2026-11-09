---
declaration: theorem
origin: cited
lean: Equidecomp.exists_iff_exists_finpartition
statement: formalized
proof: formalized
---

# Equidecompositions as partitions

Two sets `A` and `B` are related by an
equidecomposition exactly when there are a finite partition of `A` and a group element `γ s` for
each part `s`, such that the translates `γ s • s` are pairwise disjoint with union `B`.

```lean
Equidecomp.exists_iff_exists_finpartition.{u_1, u_2} {X : Type u_1} {G : Type u_2} [Group G]
  [MulAction G X] {A B : Set X} :
  (∃ f, f.source = A ∧ f.target = B) ↔
    ∃ P γ, ((↑P.parts).PairwiseDisjoint fun s => γ s • s) ∧ ⋃ s ∈ P.parts, γ s • s = B
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Equidecomp.Equipartition](equidecomp-equipartition.md)

## Lean

Formalized in Tau Ceti as [`Equidecomp.exists_iff_exists_finpartition`](https://taucetiproject.org/docs/TauCeti/Algebra/Group/Action/Equipartition.html#Equidecomp.exists_iff_exists_finpartition).

## Sources

- [Tau Ceti documentation: `Equidecomp.exists_iff_exists_finpartition`](https://taucetiproject.org/docs/TauCeti/Algebra/Group/Action/Equipartition.html#Equidecomp.exists_iff_exists_finpartition)
- [Source of `Equidecomp.exists_iff_exists_finpartition` in TauCeti/Algebra/Group/Action/Equipartition.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Group/Action/Equipartition.lean#L422)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AmenableGroups/STATUS.md)
