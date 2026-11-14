---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.BinaryQuotient.composedSumBitsProg, MIPRE.LowDegree.BinaryQuotient.composedSumBits_correct
statement: formalized
proof: formalized
---

# Effective combination of coprime degrees

A fixed polynomial-time program combines monic irreducible binary polynomials $f,g$ of coprime degrees $a,b$ into a monic irreducible binary polynomial of degree $ab$. Its inputs are the lower coefficient bits of $f$ and the full coefficient bits of $g$.

## Depends on

- [Canonical coordinates in monic binary quotients](lem-binary-monic-quotient.md)
- [Effective closed Frobenius orbit polynomials](lem-binary-orbit-polynomial.md)

## Proof depends on

- [The low-degree code](../../structure-of-the-proof/part-07/def-ld-encoding.md)

## Proof

In the supplied quotient for $f$, form $H(X)=\prod_{i=0}^{a-1}g(X+\alpha^{2^i})$, where $\alpha$ is its specified root. Frobenius permutes the factors, so the coefficients descend to binary bits. This polynomial is monic of degree $ab$ and vanishes at $\alpha+\beta$ for a root $\beta$ of $g$ in a common algebraic closure. Coprimality of the two Frobenius periods forces the degree of $\alpha+\beta$ to be $ab$; comparison with its minimal polynomial proves irreducibility. Polynomial translation, multiplication, and the length-$a$ product use bounded coefficient arrays.

## Lean

Formalized as [`MIPRE.LowDegree.BinaryQuotient.composedSumBitsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.composedSumBitsProg), [`MIPRE.LowDegree.BinaryQuotient.composedSumBits_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.composedSumBits_correct).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6806](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6806)
