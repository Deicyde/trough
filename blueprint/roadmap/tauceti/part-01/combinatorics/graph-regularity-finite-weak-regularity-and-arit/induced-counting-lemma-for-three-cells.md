---
declaration: theorem
origin: cited
lean: SimpleGraph.abs_card_induced_fin_three_sub_le
statement: formalized
proof: formalized
---

# Induced counting lemma for three cells

Let `A 0`, `A 1`, `A 2` be pairwise `ε`-uniform
cells of `G`, and `J` a graph on `Fin 3`. Then the number of maps `g` with `g i ∈ A i` such that
`g i` and `g j` are adjacent in `G` exactly when `i` and `j` are adjacent in `J` differs from
`|A 0| |A 1| |A 2|` times the product, over the pairs `i < j`, of the edge density of
`(A i, A j)` (if `i` and `j` are adjacent in `J`) or of its nonedge density `1 - d(A i, A j)`
(otherwise), that is `SimpleGraph.patternDensity`, by at most `3 ε |A 0| |A 1| |A 2|`.

```lean
SimpleGraph.abs_card_induced_fin_three_sub_le.{u_1, u_2} {α : Type u_1} {𝕜 : Type u_2} [Field 𝕜]
  [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] {G : SimpleGraph α} [DecidableRel G.Adj] {ε : 𝕜}
  (J : SimpleGraph (Fin 3)) [DecidableRel J.Adj] {A : Fin 3 → Finset α}
  (hA : ∀ (i j : Fin 3), i < j → G.IsUniform ε (A i) (A j)) :
  |↑{g ∈ Fintype.piFinset A | ∀ (i j : Fin 3), J.Adj i j ↔ G.Adj (g i) (g j)}.card -
        (∏ i, ↑(A i).card) * ∏ p, G.patternDensity (J.Adj (↑p).1 (↑p).2) (A (↑p).1) (A (↑p).2)| ≤
    3 * ε * ∏ i, ↑(A i).card
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SimpleGraph.abs_card_induced_fin_three_sub_le`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/Counting.html#SimpleGraph.abs_card_induced_fin_three_sub_le).

## Sources

- [Tau Ceti documentation: `SimpleGraph.abs_card_induced_fin_three_sub_le`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/Counting.html#SimpleGraph.abs_card_induced_fin_three_sub_le)
- [Source of `SimpleGraph.abs_card_induced_fin_three_sub_le` in TauCeti/Combinatorics/Regularity/Graph/Counting.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Regularity/Graph/Counting.lean#L153)
- [Tau Ceti roadmap status: Graph regularity, finite weak regularity, and arity-3 hypergraph complexes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Regularity/STATUS.md)
