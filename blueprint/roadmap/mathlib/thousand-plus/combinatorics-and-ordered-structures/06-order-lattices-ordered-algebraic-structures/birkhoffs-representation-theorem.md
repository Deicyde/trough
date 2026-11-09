# Birkhoff's representation theorem

**Birkhoff's Representation Theorem**. Any finite distributive lattice can be embedded in a
powerset lattice.

```lean
LatticeHom.birkhoffSet.{u_1} {α : Type u_1} [DistribLattice α] [Fintype α]
  [DecidablePred SupIrred] : LatticeHom α (Set { a // SupIrred a })
```

## Depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Set](../../../overview/data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `LatticeHom.birkhoffSet`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/Birkhoff.html#LatticeHom.birkhoffSet)
- [Source of `LatticeHom.birkhoffSet` in Mathlib/Order/Birkhoff.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Order/Birkhoff.lean#L218)
- [1000+ theorems list: Q17005116](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L4106)
- [1000+ theorems project: Q17005116](https://1000-plus.github.io/all.html?length=-1#Q17005116)
- [Wikipedia: Birkhoff's representation theorem](https://en.wikipedia.org/wiki/Birkhoff's_representation_theorem)
- [Wikidata: Q17005116](https://www.wikidata.org/wiki/Q17005116)
