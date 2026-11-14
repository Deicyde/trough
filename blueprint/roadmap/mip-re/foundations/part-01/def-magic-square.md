---
declaration: definition
origin: cited
lean: MIPRE.LCS.MagicSquare.layout, MIPRE.LCS.MagicSquare.game, MIPRE.LCS.MagicSquare.solutionGroup
statement: formalized
---

# The Magic Square

The Magic Square is the LCS instance over $\mathbb{F}_2$ with nine variables in a $3 \times 3$ grid and six equations, one per row and column, the rows summing to $0$ and the columns to $1$. It has no classical solution, since the six equations sum to $0 = 1$.

## Depends on

- [LCS instance](def-lcs-instance.md)
- [Solution group](def-solution-group.md)

## Lean

Formalized as [`MIPRE.LCS.MagicSquare.layout`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.MagicSquare.layout), [`MIPRE.LCS.MagicSquare.game`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.MagicSquare.game), [`MIPRE.LCS.MagicSquare.solutionGroup`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.MagicSquare.solutionGroup).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 428](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L428)
