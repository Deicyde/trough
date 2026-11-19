---
declaration: definition
origin: cited
lean: MIPRE.Tailored.TailoredGame.repeat, MIPRE.Tailored.TailoredGame.varEquiv, MIPRE.Tailored.TailoredGame.coord, MIPRE.Tailored.TailoredGame.coordR, MIPRE.Tailored.TailoredGame.padCons
statement: formalized
---

# The $k$-fold tailored product; II:11377, direct form

The $k$-fold product of a tailored game $\mathfrak{G}$ asks $k$-tuples of questions with the product distribution $\prod_i \mu(x_i, y_i)$. The variables at $\bar{x}$ are those of its coordinates, the readable ones first, as a tailored answer must have them: the readable variables of $x_1, \ldots, x_k$ in this order, then their linear variables, so that $\ell^R(\bar{x}) = \sum_i \ell^R(x_i)$ and $\ell^L(\bar{x}) = \sum_i \ell^L(x_i)$. The constraints at $(\bar{x}, \bar{y})$ are those of every coordinate, each written over all the variables with zero coefficients outside its coordinate. A constraint is cut into its five blocks of coefficients — readable and linear at $x_i$, readable and linear at $y_i$, affine — by prefixes and suffixes, each put at its coordinate's place among the variables of its kind; the blocks partition the constraint whatever its length, so a constraint of the wrong length pads to a vector of the wrong length, which the canonical decider rejects, as it rejects the constraint in its coordinate. No length is tested, so a program computes the padding as defined.

## Depends on

- [Tailored game; II:1243](../part-01/def-tailored-game.md)

## Lean

Formalized as [`MIPRE.Tailored.TailoredGame.repeat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.repeat), [`MIPRE.Tailored.TailoredGame.varEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.varEquiv), [`MIPRE.Tailored.TailoredGame.coord`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.coord), [`MIPRE.Tailored.TailoredGame.coordR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.coordR), [`MIPRE.Tailored.TailoredGame.padCons`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.padCons).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1118](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1118)
