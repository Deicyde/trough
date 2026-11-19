---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.TailoredGame.repeat_accepts_iff, MIPRE.Tailored.TailoredGame.satisfies_padCons_iff
statement: formalized
proof: formalized
---

# The canonical decider of the product

The canonical decider of the product accepts a pair of answers at $(\bar{x}, \bar{y})$ exactly when they have the right lengths and the canonical decider of $\mathfrak{G}$ accepts, at every coordinate $i$, the coordinate's answers read off them.

## Depends on

- [The $k$-fold tailored product; II:11377, direct form](def-tailored-product.md)

## Proof

A coordinate's answer is two blocks of the tuple's answer, its readable bits after the readable bits of the coordinates before it and its linear bits likewise. Cut the tuple's answers into the thirteen blocks the padding is made of: a constraint of the right length pairs with the whole answers block by block, the zero blocks contributing nothing and the others pairing as the constraint does with the coordinate's answers; one of the wrong length pads to a vector of the wrong length, and both sides reject. The readable answers of a coordinate are its block of the readable answers of the tuple, so the constraints of the coordinate are evaluated at the right readable answers.

## Lean

Formalized as [`MIPRE.Tailored.TailoredGame.repeat_accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.repeat_accepts_iff), [`MIPRE.Tailored.TailoredGame.satisfies_padCons_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.satisfies_padCons_iff).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1139](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1139)
