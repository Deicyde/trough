---
declaration: lemma
origin: cited
lean: MIPRE.LCS.MagicSquare.grid, MIPRE.LCS.MagicSquare.isObservable_grid, MIPRE.LCS.MagicSquare.grid_sameEquation_comm, MIPRE.LCS.MagicSquare.merminPeresStrategy
statement: formalized
proof: formalized
---

# The Mermin–Peres strategy is perfect

There are nine observables on $(\mathbb{C}^2)^{\otimes 2}$, one per cell of the Magic Square, such that the three in each row or column commute and multiply to $+1$ for a row and $-1$ for a column. They give a strategy for the Magic Square game of value $1$ on two EPR pairs.

## Depends on

- [The Magic Square](../part-01/def-magic-square.md)
- [Binary observables](../part-01/def-observable.md)

## Proof

The grid is the Mermin–Peres square of tensor products of Pauli matrices. That each entry is an observable, and that entries sharing an equation commute, are finite computations on $4 \times 4$ matrices.

## Lean

Formalized as [`MIPRE.LCS.MagicSquare.grid`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.MagicSquare.grid), [`MIPRE.LCS.MagicSquare.isObservable_grid`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.MagicSquare.isObservable_grid), [`MIPRE.LCS.MagicSquare.grid_sameEquation_comm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.MagicSquare.grid_sameEquation_comm), [`MIPRE.LCS.MagicSquare.merminPeresStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.MagicSquare.merminPeresStrategy).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 439](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L439)
