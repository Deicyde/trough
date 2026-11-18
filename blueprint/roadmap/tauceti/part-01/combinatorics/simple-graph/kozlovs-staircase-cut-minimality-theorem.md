---
declaration: theorem
origin: cited
lean: SimpleGraph.isCutMinimal_staircase
statement: formalized
proof: formalized
---

# Kozlov's staircase cut-minimality theorem

for all `c t : ℕ`, `staircase c t` is
cut-minimal (Kozlov, arXiv:1610.07136v2, Lemma 3.8 and Corollary 3.13).

```lean
SimpleGraph.isCutMinimal_staircase (c t : ℕ) : (SimpleGraph.staircase c t).IsCutMinimal
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SimpleGraph.isCutMinimal_staircase`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Staircase.html#SimpleGraph.isCutMinimal_staircase).

## Sources

- [Tau Ceti documentation: `SimpleGraph.isCutMinimal_staircase`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Staircase.html#SimpleGraph.isCutMinimal_staircase)
- [Source of `SimpleGraph.isCutMinimal_staircase` in TauCeti/Combinatorics/SimpleGraph/Staircase.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/SimpleGraph/Staircase.lean#L581)
