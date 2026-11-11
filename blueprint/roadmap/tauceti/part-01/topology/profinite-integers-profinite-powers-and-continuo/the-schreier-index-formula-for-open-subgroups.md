---
declaration: theorem
origin: cited
lean: TauCeti.freeProP.topologicalGeneratorRankNat_openSubgroup, TauCeti.freeProP.topologicalGeneratorRankNat_add_index
statement: formalized
proof: formalized
---

# The Schreier index formula for open subgroups

For an open subgroup `U` of index
`m` in the free pro-`p` group on a nonempty finite type `X` of cardinality `n`,
`d(U) = 1 + m * (n - 1)`.

```lean
TauCeti.freeProP.topologicalGeneratorRankNat_openSubgroup.{u} {p : ℕ} {X : Type u}
  [hp : Fact (Nat.Prime p)] [Finite X] [Nonempty X] (U : OpenSubgroup (TauCeti.freeProP p X)) :
  TauCeti.topologicalGeneratorRankNat ↥↑U ⋯ = 1 + (↑U).index * (Nat.card X - 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Burnside's basis theorem, cardinal form](../algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [The two-term Euler formula](../algebra/part-02/the-two-term-euler-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProP.topologicalGeneratorRankNat_openSubgroup`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/OpenSubgroup.html#TauCeti.freeProP.topologicalGeneratorRankNat_openSubgroup).

## Other forms

**The Schreier index formula for open subgroups, additive form.** Formalized in Tau Ceti as [`TauCeti.freeProP.topologicalGeneratorRankNat_add_index`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/OpenSubgroup.html#TauCeti.freeProP.topologicalGeneratorRankNat_add_index).

```lean
TauCeti.freeProP.topologicalGeneratorRankNat_add_index.{u} {p : ℕ} {X : Type u}
  [hp : Fact (Nat.Prime p)] [Finite X] (U : OpenSubgroup (TauCeti.freeProP p X)) :
  TauCeti.topologicalGeneratorRankNat ↥↑U ⋯ + (↑U).index = 1 + (↑U).index * Nat.card X
```

## Sources

- [Tau Ceti documentation: `TauCeti.freeProP.topologicalGeneratorRankNat_openSubgroup`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/OpenSubgroup.html#TauCeti.freeProP.topologicalGeneratorRankNat_openSubgroup)
- [Source of `TauCeti.freeProP.topologicalGeneratorRankNat_openSubgroup` in TauCeti/Topology/Algebra/Group/Profinite/Free/OpenSubgroup.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Free/OpenSubgroup.lean#L81)
