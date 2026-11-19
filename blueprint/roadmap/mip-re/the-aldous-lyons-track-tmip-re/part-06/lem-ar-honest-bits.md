---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.getD_honestBits_readable, MIPRE.Tailored.AnsRed.Typed.ofBool_getD_pairPcp_affine, MIPRE.Tailored.AnsRed.Typed.isXBit_diag, MIPRE.Tailored.AnsRed.Typed.isZBit_diag, MIPRE.Tailored.AnsRed.Typed.isXBit_pair, MIPRE.Tailored.AnsRed.Typed.isZBit_pair
statement: formalized
proof: formalized
---

# The answer bits of the honest answers

The answer bits of an isolated player's honest answer are X-bits of the input strategy's measurement at its question, and its readable answer bits are Z-bits; the same holds of the oracle's honest answer and the input strategy's measurements at both questions of its seed, jointly.

## Depends on

- [Bits controlled by readable data](lem-ar-controlled-bits.md)
- [The honest PCP of an answer pair](lem-ar-pair-pcp.md)
- [The honest answers](def-ar-honest-answers.md)

## Proof depends on

- [Presenting a game as a tailored game](../part-03/lem-presentation-transport.md)
- [Slot values and block-local polynomials](lem-ar-slots.md)

## Proof

A readable bit lies in a readable codeword, a function of the readable input bits, which are Z-bits. Every bit is, the readable input bits fixed, affine in the linear input bits, which are X-bits: the codewords are affine in them, and values, restrictions to lines and canonical bits of field elements are additive. Lemma [Bits controlled by readable data](lem-ar-controlled-bits.md) concludes.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.getD_honestBits_readable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.getD_honestBits_readable), [`MIPRE.Tailored.AnsRed.Typed.ofBool_getD_pairPcp_affine`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ofBool_getD_pairPcp_affine), [`MIPRE.Tailored.AnsRed.Typed.isXBit_diag`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.isXBit_diag), [`MIPRE.Tailored.AnsRed.Typed.isZBit_diag`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.isZBit_diag), [`MIPRE.Tailored.AnsRed.Typed.isXBit_pair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.isXBit_pair), [`MIPRE.Tailored.AnsRed.Typed.isZBit_pair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.isZBit_pair).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3043](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3043)
