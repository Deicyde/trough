---
declaration: theorem
origin: cited
lean: MIPRE.LCS.exists_tensorStrategy_value_eq_one_of_localLoss_annihilates_epr
statement: formalized
proof: formalized
---

# Perfect strategies from operator solutions

If a bipartite observable strategy for an LCS instance is perfect — its local loss operators annihilate the EPR vector — then the associated LCS game has a tensor-product strategy of value $1$.

## Depends on

- [LCS game](../part-01/def-lcs-game.md)
- [Tensor-product strategy](../part-01/def-tensor-strategy.md)
- [Quantum value](../part-01/def-q-value.md)
- [From an observable strategy to a projective strategy](../part-01/lem-observable-strategy.md)

## Proof

Take both players' spaces to be $\mathbb{C}^n$ with the normalized EPR state. The game is symmetric, so each player needs measurements at both kinds of question, and both use the same ones: at an equation, the joint projective measurement of its observables, answered as an assignment extended by zero; at a variable, the binary measurement of its observable. At an equation–variable incidence the accepted Born-rule weight is the EPR expectation of the local winning operator, which is $1$ because the local loss operator annihilates the EPR vector. The other orientation has the same weight, since $\langle \Omega, (A \otimes B) \Omega\rangle = \sum_{a,k} A_{ak} B_{ak}$ is symmetric in $A$ and $B$ and the decider is symmetric in the players. No transposes are needed.

## Lean

Formalized as [`MIPRE.LCS.exists_tensorStrategy_value_eq_one_of_localLoss_annihilates_epr`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.exists_tensorStrategy_value_eq_one_of_localLoss_annihilates_epr).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 457](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L457)
