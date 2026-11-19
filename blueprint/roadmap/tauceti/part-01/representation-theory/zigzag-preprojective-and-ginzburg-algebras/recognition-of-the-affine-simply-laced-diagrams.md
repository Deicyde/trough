---
declaration: theorem
origin: cited
lean: SimpleGraph.Connected.exists_sum_eq_two_mul_iff_existsUnique_affineDynkinType_iso
statement: formalized
proof: formalized
---

# Recognition of the affine simply-laced diagrams

A connected finite simple graph carries a
nonzero weight `a : V → ℕ` with `∑_{j ∼ i} a j = 2 * a i` at every vertex exactly when it is
isomorphic to the graph of a unique valid affine simply-laced diagram other than `Ã₁`: a cycle
`Ãₙ` with `n ≥ 2`, affine `Dₙ` with `n ≥ 4`, or affine `E₆`, `E₇` or `E₈`.

```lean
SimpleGraph.Connected.exists_sum_eq_two_mul_iff_existsUnique_affineDynkinType_iso.{u_1}
  {V : Type u_1} [Fintype V] {G : SimpleGraph V} [DecidableRel G.Adj] (hG : G.Connected) :
  (∃ a, a ≠ 0 ∧ ∀ (i : V), ∑ j ∈ G.neighborFinset i, a j = 2 * a i) ↔
    ∃! t, t.Valid ∧ t.IsGraphical ∧ Nonempty (G ≃g t.graph)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SimpleGraph.Connected.exists_sum_eq_two_mul_iff_existsUnique_affineDynkinType_iso`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/AffineDynkinType/Recognition.html#SimpleGraph.Connected.exists_sum_eq_two_mul_iff_existsUnique_affineDynkinType_iso).

## Sources

- [Tau Ceti documentation: `SimpleGraph.Connected.exists_sum_eq_two_mul_iff_existsUnique_affineDynkinType_iso`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/AffineDynkinType/Recognition.html#SimpleGraph.Connected.exists_sum_eq_two_mul_iff_existsUnique_affineDynkinType_iso)
- [Source of `SimpleGraph.Connected.exists_sum_eq_two_mul_iff_existsUnique_affineDynkinType_iso` in TauCeti/LinearAlgebra/RootSystem/AffineDynkinType/Recognition.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/RootSystem/AffineDynkinType/Recognition.lean#L52)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
