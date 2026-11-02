---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: SimpleGraph.triangle_removal
mathlib_file: Mathlib/Combinatorics/SimpleGraph/Triangle/Removal.lean
---

# Triangle removal lemma

**Triangle Removal Lemma**. If there are not too many triangles (on the order of `(card α)^3`)
then they can all be removed by removing a few edges (on the order of `(card α)^2`).

```lean
SimpleGraph.triangle_removal.{u_1} {α : Type u_1} [DecidableEq α] [Fintype α] {G : SimpleGraph α}
  [DecidableRel G.Adj] {ε : ℝ}
  (hG : ↑(G.cliqueFinset 3).card < SimpleGraph.triangleRemovalBound ε * ↑(Fintype.card α) ^ 3) :
  ∃ G' ≤ G,
    ∃ x, ↑G.edgeFinset.card - ↑G'.edgeFinset.card < ε * ↑(Fintype.card α ^ 2) ∧ G'.CliqueFree 3
```

## Depends on

- [Logarithm](../../analysis/special-functions/logarithm.md)
- [Simple graph](simple-graph.md)

## Proof depends on

- [Regularity lemma](regularity-lemma.md)
- [Triangle counting lemma](triangle-counting-lemma.md)

## Sources

- [Mathlib documentation: `SimpleGraph.triangle_removal`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SimpleGraph/Triangle/Removal.html#SimpleGraph.triangle_removal)
- [Source of `SimpleGraph.triangle_removal` in Mathlib/Combinatorics/SimpleGraph/Triangle/Removal.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/SimpleGraph/Triangle/Removal.lean#L160)
- [Mathlib overview: Combinatorics › Graph theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L532)
