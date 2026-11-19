---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.BinaryPolynomial.powerBitsProg, MIPRE.LowDegree.BinaryPolynomial.evalBits_powerBits, MIPRE.LowDegree.BinaryPolynomial.evalBits_inverseBits, MIPRE.SAT.shoupInvProg_correct, MIPRE.SAT.shoupInvProg_time_le, MIPRE.LowDegree.BinaryPolynomial.frobeniusTraceProg, MIPRE.LowDegree.BinaryPolynomial.evalBits_frobeniusTrace, MIPRE.LowDegree.BinaryPolynomial.evalBits_frobeniusTrace_trace, MIPRE.SAT.shoupBinField_finrank, MIPRE.SAT.shoupFrobeniusTraceProg_frobenius, MIPRE.SAT.shoupFrobeniusTraceProg_period, MIPRE.SAT.shoupTraceProg_correct, MIPRE.SAT.shoupTraceProg_time_le
statement: formalized
proof: formalized
---

# Effective inversion, Frobenius iteration and trace

Uniform ambient programs compute binary exponentiation, inversion of nonzero field elements, iterated Frobenius, and the trace in the Shoup polynomial-basis field. Inversion and trace computation, including construction of the modulus, take polynomial time in the unary extension degree $k$ on $k$-bit operands. After $k$ squarings an element returns to itself, and the sum of its first $k$ Frobenius iterates is its algebraic trace embedded in the extension field.

## Depends on

- [Effective polynomial-basis field arithmetic](lem-effective-binary-field-arithmetic.md)

## Proof

Binary exponentiation reads the exponent bit by bit, squaring the current power and multiplying the accumulator when the bit is one. For a nonzero operand use the exponent $2^k-2$, constructed directly as a $k$-bit string. Fixed-width accumulators give a polynomial bound even on malformed inputs. A second loop squares its current element and XORs it into an accumulator. Induction identifies the accumulated sum, and the finite-field trace formula identifies it with the algebraic trace. The concrete programs preserve the canonical quotient encoding.

## Lean

Formalized as [`MIPRE.LowDegree.BinaryPolynomial.powerBitsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.powerBitsProg), [`MIPRE.LowDegree.BinaryPolynomial.evalBits_powerBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.evalBits_powerBits), [`MIPRE.LowDegree.BinaryPolynomial.evalBits_inverseBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.evalBits_inverseBits), [`MIPRE.SAT.shoupInvProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupInvProg_correct), [`MIPRE.SAT.shoupInvProg_time_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupInvProg_time_le), [`MIPRE.LowDegree.BinaryPolynomial.frobeniusTraceProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.frobeniusTraceProg), [`MIPRE.LowDegree.BinaryPolynomial.evalBits_frobeniusTrace`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.evalBits_frobeniusTrace), [`MIPRE.LowDegree.BinaryPolynomial.evalBits_frobeniusTrace_trace`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.evalBits_frobeniusTrace_trace), [`MIPRE.SAT.shoupBinField_finrank`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupBinField_finrank), [`MIPRE.SAT.shoupFrobeniusTraceProg_frobenius`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupFrobeniusTraceProg_frobenius), [`MIPRE.SAT.shoupFrobeniusTraceProg_period`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupFrobeniusTraceProg_period), [`MIPRE.SAT.shoupTraceProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupTraceProg_correct), [`MIPRE.SAT.shoupTraceProg_time_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupTraceProg_time_le).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6951](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6951)
