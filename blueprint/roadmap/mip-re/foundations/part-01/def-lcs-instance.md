---
declaration: definition
origin: cited
lean: MIPRE.LCS.Layout, MIPRE.LCS.Game
statement: formalized
---

# LCS instance

A *binary linear constraint system* consists of $r$ equations over $s$ $\mathbb{F}_2$-valued variables, specified by the set $V_i \subseteq \{1, \dots, s\}$ of variables occurring in each equation $i$ together with a right-hand side $b \in \mathbb{F}_2^r$; equation $i$ reads $\sum_{j \in V_i} x_j = b_i$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.LCS.Layout`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.Layout), [`MIPRE.LCS.Game`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.Game).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 323](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L323)
