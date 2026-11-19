---
declaration: theorem
origin: cited
lean: SimpleGraph.card_oddTriangleFinset_staircase
statement: formalized
proof: formalized
---

# Kozlov's staircase odd-triangle formula

in `staircase c t` on `n = c * (2 * t + 1)`
vertices, the number of `3`-vertex subsets spanning an odd number of edges is
`(n / 3) * #(staircase c t).edgeFinset` over `ℝ`
(Kozlov, arXiv:1610.07136v2, equation (2.5) and Lemma 3.10).

```lean
SimpleGraph.card_oddTriangleFinset_staircase (c t : ℕ) :
  ↑(SimpleGraph.staircase c t).oddTriangleFinset.card =
    ↑c * (2 * ↑t + 1) / 3 * ↑(SimpleGraph.staircase c t).edgeFinset.card
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Kozlov's odd-triangle identity](kozlovs-odd-triangle-identity.md)

## Lean

Formalized in Tau Ceti as [`SimpleGraph.card_oddTriangleFinset_staircase`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Staircase.html#SimpleGraph.card_oddTriangleFinset_staircase).

## Sources

- [Tau Ceti documentation: `SimpleGraph.card_oddTriangleFinset_staircase`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Staircase.html#SimpleGraph.card_oddTriangleFinset_staircase)
- [Source of `SimpleGraph.card_oddTriangleFinset_staircase` in TauCeti/Combinatorics/SimpleGraph/Staircase.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/SimpleGraph/Staircase.lean#L689)
