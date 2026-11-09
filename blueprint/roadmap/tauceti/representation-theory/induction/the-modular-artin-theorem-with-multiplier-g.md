---
declaration: theorem
origin: cited
lean: TauCeti.modularArtin_natCard_nsmul_mem_indCyclicCoprimeK0
statement: formalized
proof: formalized
---

# The modular Artin theorem with multiplier `|G|`

In characteristic `p`, the group-order
multiple of every class in `G₀(k[G])` lies in `TauCeti.indCyclicCoprimeK0`, the subgroup generated
by the classes induced from cyclic subgroups of order prime to `p`; for the prime `p`, order prime
to `p` is non-divisibility of the order by `p` (`Nat.Prime.coprime_iff_not_dvd`).

```lean
TauCeti.modularArtin_natCard_nsmul_mem_indCyclicCoprimeK0.{u} {k G : Type u} [Field k] [Group G]
  [Finite G] (p : ℕ) [Fact (Nat.Prime p)] [CharP k p]
  (x : TauCeti.ExactK0 (TauCeti.finiteModulesExactStructure (MonoidAlgebra k G))) :
  Nat.card G • x ∈ TauCeti.indCyclicCoprimeK0 k G p
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Artin's induction identity for every virtual class over every field](../grothendieck-group/artins-induction-identity-for-every-virtual-clas.md)
- [The dual Noether isomorphism](../../category-theory/exact/the-dual-noether-isomorphism.md)
- [Kolchin's common fixed vector theorem](../../linear-algebra/other-results/kolchins-common-fixed-vector-theorem.md)
- [The Noether isomorphism for exact categories](../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.modularArtin_natCard_nsmul_mem_indCyclicCoprimeK0`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Artin/Spanning.html#TauCeti.modularArtin_natCard_nsmul_mem_indCyclicCoprimeK0).

## Sources

- [Tau Ceti documentation: `TauCeti.modularArtin_natCard_nsmul_mem_indCyclicCoprimeK0`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Artin/Spanning.html#TauCeti.modularArtin_natCard_nsmul_mem_indCyclicCoprimeK0)
- [Source of `TauCeti.modularArtin_natCard_nsmul_mem_indCyclicCoprimeK0` in TauCeti/RepresentationTheory/Induction/Artin/Spanning.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Induction/Artin/Spanning.lean#L72)
