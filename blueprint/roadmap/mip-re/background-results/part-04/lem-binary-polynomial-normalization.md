---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.BinaryPolynomial.normalizeBitsProg, MIPRE.LowDegree.BinaryPolynomial.normalizeBitsProg_apply, MIPRE.LowDegree.BinaryPolynomial.length_normalizeBits_le, MIPRE.LowDegree.BinaryPolynomial.evalBits_normalizeBits, MIPRE.LowDegree.BinaryPolynomial.polyOfBits_normalizeBits, MIPRE.LowDegree.BinaryPolynomial.normalizeBits_getLast
statement: formalized
proof: formalized
---

# Effective normalization of binary polynomials

One fixed deterministic ambient program removes the trailing zero coefficients from any little-endian binary coefficient list in polynomial time. Its output is no longer than the input, is empty or ends in one, and represents the same polynomial over $\mathbb{F}_2$. More generally it preserves Horner evaluation at any element of any commutative ring. This program requires no irreducible-polynomial construction.

## Depends on

- [The low-degree code](../../structure-of-the-proof/part-07/def-ld-encoding.md)

## Proof

Fold the coefficient list from its highest coefficient downwards. Ignore a zero while the accumulator is empty; otherwise prepend the current coefficient. Induction proves preservation of Horner evaluation and the leading-coefficient property. Each step adds at most one coefficient, so every intermediate encoded accumulator has size bounded by the input and the generic bounded-fold program gives the polynomial runtime bound.

## Lean

Formalized as [`MIPRE.LowDegree.BinaryPolynomial.normalizeBitsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.normalizeBitsProg), [`MIPRE.LowDegree.BinaryPolynomial.normalizeBitsProg_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.normalizeBitsProg_apply), [`MIPRE.LowDegree.BinaryPolynomial.length_normalizeBits_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.length_normalizeBits_le), [`MIPRE.LowDegree.BinaryPolynomial.evalBits_normalizeBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.evalBits_normalizeBits), [`MIPRE.LowDegree.BinaryPolynomial.polyOfBits_normalizeBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.polyOfBits_normalizeBits), [`MIPRE.LowDegree.BinaryPolynomial.normalizeBits_getLast`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.normalizeBits_getLast).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6515](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6515)
