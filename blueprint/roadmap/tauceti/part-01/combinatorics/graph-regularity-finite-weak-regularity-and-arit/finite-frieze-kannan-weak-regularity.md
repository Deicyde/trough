---
declaration: theorem
origin: cited
lean: SimpleGraph.frieze_kannan
statement: formalized
proof: formalized
---

# Finite Frieze–Kannan weak regularity

For `ε > 0`, the vertices of `G` have a partition
`P` into at most `4 ^ ⌈1 / ε²⌉` parts such that, for all vertex sets `A` and `B`, the number of
edges from `A` to `B` is within `ε * (card V) ^ 2` of its stepped prediction
`G.steppedCount P A B`.

```lean
SimpleGraph.frieze_kannan.{u_1} {V : Type u_1} [Fintype V] [DecidableEq V] (G : SimpleGraph V)
  [DecidableRel G.Adj] {ε : ℝ} (hε : 0 < ε) :
  ∃ P,
    P.parts.card ≤ 4 ^ ⌈1 / ε ^ 2⌉₊ ∧
      ∀ (A B : Finset V),
        |↑(G.interedges A B).card - G.steppedCount P A B| ≤ ε * ↑(Fintype.card V) ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [SimpleGraph.cutDiscrepancy](simplegraph-cutdiscrepancy.md)

## Lean

Formalized in Tau Ceti as [`SimpleGraph.frieze_kannan`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/FriezeKannan.html#SimpleGraph.frieze_kannan).

## Sources

- [Tau Ceti documentation: `SimpleGraph.frieze_kannan`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/FriezeKannan.html#SimpleGraph.frieze_kannan)
- [Source of `SimpleGraph.frieze_kannan` in TauCeti/Combinatorics/Regularity/Graph/FriezeKannan.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Regularity/Graph/FriezeKannan.lean#L181)
- [Tau Ceti roadmap status: Graph regularity, finite weak regularity, and arity-3 hypergraph complexes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Regularity/STATUS.md)
