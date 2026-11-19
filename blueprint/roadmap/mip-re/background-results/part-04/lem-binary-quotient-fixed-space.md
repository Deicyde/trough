---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.BinaryQuotient.frobeniusMatrixProg, MIPRE.LowDegree.BinaryQuotient.frobeniusMatrixProg_correct, MIPRE.LowDegree.BinaryQuotient.fixedGeneratorsProg, MIPRE.LowDegree.BinaryQuotient.fixedGeneratorsProg_correct, MIPRE.LowDegree.BinaryQuotient.fixedGenerator_idempotent, MIPRE.LowDegree.BinaryQuotient.fixedGenerator_spans, MIPRE.LowDegree.BinaryQuotient.square_bijective
statement: formalized
proof: formalized
---

# Effective Frobenius fixed spaces in binary quotients

For a monic binary modulus of degree $d$, uniform deterministic polynomial-time programs compute the matrix of squaring and a family of $d$ vectors spanning its fixed space. Every decoded generator is idempotent, and every idempotent lies in their binary span. If the modulus is squarefree, squaring on the quotient is bijective.

## Depends on

- [Canonical coordinates in monic binary quotients](lem-binary-monic-quotient.md)
- [Effective indexing and padding arithmetic](../../structure-of-the-proof/part-07/lem-pcp-padding-programs.md)

## Proof

Square each power-basis vector using the supplied modulus and transpose the resulting columns. The fixed-space matrix is this matrix plus the identity; the verified binary kernel program prints a spanning family. The power-basis coordinate equivalence transports the kernel and its span back to quotient elements. For a squarefree modulus, equality of squares makes the square of the difference zero. A polynomial lift of that difference has its square divisible by the modulus; squarefreeness implies divisibility of the lift itself. Squaring is therefore injective, hence bijective on the finite quotient.

## Lean

Formalized as [`MIPRE.LowDegree.BinaryQuotient.frobeniusMatrixProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.frobeniusMatrixProg), [`MIPRE.LowDegree.BinaryQuotient.frobeniusMatrixProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.frobeniusMatrixProg_correct), [`MIPRE.LowDegree.BinaryQuotient.fixedGeneratorsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.fixedGeneratorsProg), [`MIPRE.LowDegree.BinaryQuotient.fixedGeneratorsProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.fixedGeneratorsProg_correct), [`MIPRE.LowDegree.BinaryQuotient.fixedGenerator_idempotent`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.fixedGenerator_idempotent), [`MIPRE.LowDegree.BinaryQuotient.fixedGenerator_spans`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.fixedGenerator_spans), [`MIPRE.LowDegree.BinaryQuotient.square_bijective`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryQuotient.square_bijective).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6635](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6635)
