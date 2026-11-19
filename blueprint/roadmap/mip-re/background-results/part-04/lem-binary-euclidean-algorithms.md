---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.BinaryPolynomial.normalizeBits_eq_nil_iff, MIPRE.LowDegree.BinaryPolynomial.length_normalizeBits, MIPRE.LowDegree.BinaryPolynomial.divModBits_eq_div_modByMonic, MIPRE.LowDegree.BinaryPolynomial.gcdBitsProg, MIPRE.LowDegree.BinaryPolynomial.polyOfBits_gcdBits, MIPRE.LowDegree.BinaryPolynomial.gcdBits_width, MIPRE.LowDegree.BinaryPolynomial.quotientBitsProg, MIPRE.LowDegree.BinaryPolynomial.polyOfBits_quotientBits, MIPRE.LowDegree.BinaryPolynomial.polyOfBits_quotientBits_mul, MIPRE.LowDegree.BinaryPolynomial.quotientBits_width
statement: formalized
proof: formalized
---

# Canonical binary Euclidean algorithms

Normalization of a binary coefficient list is empty exactly when its polynomial is zero; otherwise its length is the degree plus one. List-based monic division agrees with polynomial division. Uniform deterministic polynomial-time programs compute the normalized polynomial gcd and polynomial quotient on all binary coefficient lists. The quotient by zero is zero. For a nonzero divisor which divides the dividend, the quotient reconstructs the dividend by multiplication. The gcd width is at most the larger input width, and quotient width is at most the dividend width.

## Depends on

- [Effective monic binary division](lem-binary-monic-division.md)

## Proof

A nonempty normalized list ends in one, determining the degree and monicity. The reconstruction identity and strict remainder-degree bound uniquely identify monic quotient and remainder. Euclidean steps preserve the gcd and strictly decrease the normalized remainder length until it is zero, so the original divisor width bounds the iteration count. Intermediate widths never exceed the initial maximum, including malformed states of the ambient loop. Quotient computation normalizes the divisor and invokes monic division, with an explicit zero branch.

## Lean

Formalized as [`MIPRE.LowDegree.BinaryPolynomial.normalizeBits_eq_nil_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.normalizeBits_eq_nil_iff), [`MIPRE.LowDegree.BinaryPolynomial.length_normalizeBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.length_normalizeBits), [`MIPRE.LowDegree.BinaryPolynomial.divModBits_eq_div_modByMonic`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.divModBits_eq_div_modByMonic), [`MIPRE.LowDegree.BinaryPolynomial.gcdBitsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.gcdBitsProg), [`MIPRE.LowDegree.BinaryPolynomial.polyOfBits_gcdBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.polyOfBits_gcdBits), [`MIPRE.LowDegree.BinaryPolynomial.gcdBits_width`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.gcdBits_width), [`MIPRE.LowDegree.BinaryPolynomial.quotientBitsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.quotientBitsProg), [`MIPRE.LowDegree.BinaryPolynomial.polyOfBits_quotientBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.polyOfBits_quotientBits), [`MIPRE.LowDegree.BinaryPolynomial.polyOfBits_quotientBits_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.polyOfBits_quotientBits_mul), [`MIPRE.LowDegree.BinaryPolynomial.quotientBits_width`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.quotientBits_width).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6600](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6600)
