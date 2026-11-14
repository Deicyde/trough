---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.BinaryPolynomial.divModBitsProg, MIPRE.LowDegree.BinaryPolynomial.divModBitsProg_apply, MIPRE.LowDegree.BinaryPolynomial.divModBits_width, MIPRE.LowDegree.BinaryPolynomial.polyOfBits_divModBits, MIPRE.LowDegree.BinaryPolynomial.degree_divModBits_remainder_lt
statement: formalized
proof: formalized
---

# Effective monic binary division

Given a binary coefficient list $a$ and the $d$ lower coefficients $p$ of a monic polynomial $f$, one deterministic ambient polynomial-time program returns coefficient lists $q,r$ satisfying $fq+r=a$ and $\deg r\lt d$. Their lengths are at most the length of $a$ and $d$, respectively. The case $d=0$ divides by one and returns zero remainder.

## Depends on

- [Effective normalization of binary polynomials](lem-binary-polynomial-normalization.md)

## Proof

Process the dividend by Horner's rule, keeping a remainder of width $d$ and recording its discarded high bit as the next quotient coefficient. Each shift subtracts the indicated multiple of the monic divisor; induction gives the reconstruction identity. The remainder width bounds its degree. Normalize both outputs. The quotient grows by one bit per iteration and the remainder cannot grow, even from malformed initial states, so the ambient bounded-fold theorem gives the global polynomial bound.

## Lean

Formalized as [`MIPRE.LowDegree.BinaryPolynomial.divModBitsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.divModBitsProg), [`MIPRE.LowDegree.BinaryPolynomial.divModBitsProg_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.divModBitsProg_apply), [`MIPRE.LowDegree.BinaryPolynomial.divModBits_width`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.divModBits_width), [`MIPRE.LowDegree.BinaryPolynomial.polyOfBits_divModBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.polyOfBits_divModBits), [`MIPRE.LowDegree.BinaryPolynomial.degree_divModBits_remainder_lt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.degree_divModBits_remainder_lt).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6544](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6544)
