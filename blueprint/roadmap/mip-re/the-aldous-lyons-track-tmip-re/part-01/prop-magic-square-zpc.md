---
declaration: proposition
origin: cited
lean: MIPRE.Tailored.MagicSquare.game, MIPRE.Tailored.MagicSquare.obs, MIPRE.Tailored.MagicSquare.strategy, MIPRE.Tailored.MagicSquare.value_strategy, MIPRE.Tailored.MagicSquare.hasPerfectZPC, MIPRE.Tailored.MagicSquare.valStar_eq_one
statement: formalized
proof: formalized
---

# The Magic Square game; Examples II:1300–1370

Tailor the Mermin–Peres Magic Square, as a linear constraint system game, with all its variables linear: the questions are the six constraints — each row of the $3 \times 3$ grid summing to $0$, each column to $1$ — and the nine cells; an edge joins a constraint to one of its cells, with weight $\frac1{18}$, and checks that the constraint holds and that the constraint's value at the cell is the cell's. This game has a perfect ZPC strategy on the signed set of eight points $(\mathbb{F}_2^2)_\pm$: the grid

$$
\begin{array}{ccc}
X \otimes {I} & {I} \otimes X & X \otimes X \\
{I} \otimes Z & Z \otimes {I} & Z \otimes Z \\
-X \otimes Z & -Z \otimes X & -XZ \otimes XZ
\end{array}
$$

of signed permutations, $X$ flipping a bit and $Z$ flipping the sign at the bit $1$. Its quantum value is therefore $1$, while the linear system has no solution, so that no deterministic strategy, and no ZPC strategy for the tailoring with all variables readable, is perfect (Remark II:1250).

## Depends on

- [ZPC strategies are PCC strategies](lem-zpc-pcc.md)
- [Signed permutation matrices](lem-signed-perm.md)

## Proof

The observables are involutions commuting along each row and each column, the rows multiply to ${I}$ and the columns to $-{I}$; these are identities in the group of signed permutations of four points, checked by computation, and the matrix map transports them. All variables being linear, Z-alignment is vacuous; an edge joins a constraint to one of its cells, whose observable is one of the constraint's, so the strategy commutes along edges. The observable of a consistency check is the square of a cell's observable, ${I}$, and that of a row or column check is the product of its three observables, ${I}$ or $-{I}$ as the parity requires, so every sampled answer pair is accepted by Lemma [When a permutation strategy is perfect](lem-perm-strategy-perfect.md). The quantum value is $1$ by Lemma [ZPC strategies are PCC strategies](lem-zpc-pcc.md).

## Lean

Formalized as [`MIPRE.Tailored.MagicSquare.game`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.MagicSquare.game), [`MIPRE.Tailored.MagicSquare.obs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.MagicSquare.obs), [`MIPRE.Tailored.MagicSquare.strategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.MagicSquare.strategy), [`MIPRE.Tailored.MagicSquare.value_strategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.MagicSquare.value_strategy), [`MIPRE.Tailored.MagicSquare.hasPerfectZPC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.MagicSquare.hasPerfectZPC), [`MIPRE.Tailored.MagicSquare.valStar_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.MagicSquare.valStar_eq_one).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 289](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L289)
