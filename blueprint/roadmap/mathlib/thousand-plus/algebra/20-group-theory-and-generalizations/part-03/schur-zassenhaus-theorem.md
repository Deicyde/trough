---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Subgroup.exists_left_complement'_of_coprime
mathlib_file: Mathlib/GroupTheory/SchurZassenhaus.lean
---

# Schur–Zassenhaus theorem

**Schur-Zassenhaus** for normal subgroups:
If `H : Subgroup G` is normal, and has order coprime to its index, then there exists a
subgroup `K` which is a (left) complement of `H`.

```lean
Subgroup.exists_left_complement'_of_coprime.{u} {G : Type u} [Group G] {N : Subgroup G} [N.Normal]
  (hN : (Nat.card ↥N).Coprime N.index) : ∃ H, H.IsComplement' N
```

## Depends on

- [Cardinal](../../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Index of a subgroup](../../../../overview/general-algebra/group-theory/part-01/index-of-a-subgroup.md)
- [Integer](../../../../overview/general-algebra/numbers/integer.md)
- [Normal subgroup](../../../../overview/general-algebra/group-theory/part-01/normal-subgroup.md)
- [Ring morphism](../../../../overview/general-algebra/rings/ring-morphism.md)

## Proof depends on

- [Euclid's' algorithm](../../../../overview/general-algebra/divisibility-in-integral-domains/euclids-algorithm.md)
- [Third Sylow theorem](../../../../overview/general-algebra/group-theory/part-02/third-sylow-theorem.md)

## Sources

- [Mathlib documentation: `Subgroup.exists_left_complement'_of_coprime`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SchurZassenhaus.html#Subgroup.exists_left_complement'_of_coprime)
- [Source of `Subgroup.exists_left_complement'_of_coprime` in Mathlib/GroupTheory/SchurZassenhaus.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/SchurZassenhaus.lean#L294)
- [1000+ theorems list: Q2226800](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2100)
- [1000+ theorems project: Q2226800](https://1000-plus.github.io/all.html?length=-1#Q2226800)
- [Wikipedia: Schur–Zassenhaus theorem](https://en.wikipedia.org/wiki/Schur%E2%80%93Zassenhaus_theorem)
- [Wikidata: Q2226800](https://www.wikidata.org/wiki/Q2226800)
