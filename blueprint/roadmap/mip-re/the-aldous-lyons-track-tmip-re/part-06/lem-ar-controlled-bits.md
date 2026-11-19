---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.isSignedPerm_controlledSum, MIPRE.Tailored.isXBit_controlledBy, MIPRE.Tailored.isZBit_comp_of_isDiag, MIPRE.Tailored.isDiag_coarse_of_isZBit, MIPRE.Tailored.IsAffine2.eq_sum, MIPRE.Tailored.isXBit_affine, MIPRE.Tailored.isXBit_of_controlledAffine, MIPRE.Tailored.isZBit_of_readable, MIPRE.Tailored.PermStrategy.toSync_len, MIPRE.Tailored.PermStrategy.toSync_bit
statement: formalized
proof: formalized
---

# Bits controlled by readable data

Let $P$ be a projective measurement on $\mathbb{C}^m$. A bit of its outcome that is a function of some Z-bits of $P$ (bits whose observables are diagonal signed permutations) is a Z-bit. A bit that is, for each value of those Z-bits, an $\mathbb{F}_2$-affine function of some X-bits of $P$ (bits whose observables are signed permutations) is an X-bit. The answer bits of the synchronous strategy of a permutation strategy are X-bits, and Z-bits below the readable length.

## Depends on

- [The input strategy's answer bits](../part-03/lem-input-answer-bits.md)
- [ZPC strategies are PCC strategies](../part-01/lem-zpc-pcc.md)
- [The low-degree code](../../structure-of-the-proof/part-07/def-ld-encoding.md)

## Proof

The coarse-graining of $P$ along Z-bits is diagonal, and a sum $\sum_k \Pi_k W_k$ over a diagonal projective measurement $\Pi$ of signed permutations $W_k$ commuting with it is a signed permutation: on the basis vectors of outcome $k$ it acts as $W_k$, which keeps them there. An affine function of X-bits is a constant exclusive or of some of them, whose observable is a product of signed permutations.

## Lean

Formalized as [`MIPRE.Tailored.isSignedPerm_controlledSum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isSignedPerm_controlledSum), [`MIPRE.Tailored.isXBit_controlledBy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isXBit_controlledBy), [`MIPRE.Tailored.isZBit_comp_of_isDiag`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isZBit_comp_of_isDiag), [`MIPRE.Tailored.isDiag_coarse_of_isZBit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isDiag_coarse_of_isZBit), [`MIPRE.Tailored.IsAffine2.eq_sum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.IsAffine2.eq_sum), [`MIPRE.Tailored.isXBit_affine`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isXBit_affine), [`MIPRE.Tailored.isXBit_of_controlledAffine`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isXBit_of_controlledAffine), [`MIPRE.Tailored.isZBit_of_readable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isZBit_of_readable), [`MIPRE.Tailored.PermStrategy.toSync_len`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.toSync_len), [`MIPRE.Tailored.PermStrategy.toSync_bit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.toSync_bit).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3018](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3018)
