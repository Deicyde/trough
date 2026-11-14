---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.BinaryPolynomial.normalize_monic, MIPRE.LowDegree.BinaryPolynomial.evalBits_xor, MIPRE.LowDegree.BinaryPolynomial.evalBits_mulReduce, MIPRE.LowDegree.BinaryPolynomial.xorBitsProg, MIPRE.LowDegree.BinaryPolynomial.mulReduceProg, MIPRE.LowDegree.BinaryPolynomial.shoupLowerCoeffs_length, MIPRE.LowDegree.BinaryPolynomial.shoupLowerCoeffs_poly, MIPRE.SAT.quotientBinField, MIPRE.SAT.quotientBinField_toBits_ofBits, MIPRE.SAT.quotientBinField_ofBits, MIPRE.SAT.quotientBinField_add, MIPRE.SAT.quotientBinField_mul, MIPRE.SAT.shoupBinField, MIPRE.SAT.shoupAdmissibleField, MIPRE.SAT.shoupMulProg_time_le, MIPRE.SAT.shoupMulProg_correct
statement: formalized
proof: formalized
---

# Effective polynomial-basis field arithmetic

For a monic irreducible binary polynomial $f$ of degree $k$, its quotient field has a canonical $k$-bit power-basis representation. Uniform ambient programs on coefficient lists implement addition and multiplication in that field. Using the proved Shoup construction, one uniform multiplication program also constructs the modulus from unary $k$, and runs in time polynomial in $k$ on $k$-bit operands. This supplies a field family for every admissible odd $k$.

## Depends on

- [The low-degree code](../../structure-of-the-proof/part-07/def-ld-encoding.md)

## Proof

XOR implements addition. Shift a coefficient vector and, when its highest bit is one, XOR the lower coefficients of the monic modulus. Horner multiplication uses this reduction after each shift. The accumulator length never increases, so the ambient fold has a polynomial size and time bound. Horner evaluation at a root of $f$ proves correctness, and the quotient's power basis proves that correctly sized bit vectors are canonical. Normalize Shoup's output by taking its first $k$ coefficients and treating the leading monic coefficient implicitly. Compose the programs; the encoded input has size at most $10k+5$.

## Lean

Formalized as [`MIPRE.LowDegree.BinaryPolynomial.normalize_monic`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.normalize_monic), [`MIPRE.LowDegree.BinaryPolynomial.evalBits_xor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.evalBits_xor), [`MIPRE.LowDegree.BinaryPolynomial.evalBits_mulReduce`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.evalBits_mulReduce), [`MIPRE.LowDegree.BinaryPolynomial.xorBitsProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.xorBitsProg), [`MIPRE.LowDegree.BinaryPolynomial.mulReduceProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.mulReduceProg), [`MIPRE.LowDegree.BinaryPolynomial.shoupLowerCoeffs_length`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.shoupLowerCoeffs_length), [`MIPRE.LowDegree.BinaryPolynomial.shoupLowerCoeffs_poly`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryPolynomial.shoupLowerCoeffs_poly), [`MIPRE.SAT.quotientBinField`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.quotientBinField), [`MIPRE.SAT.quotientBinField_toBits_ofBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.quotientBinField_toBits_ofBits), [`MIPRE.SAT.quotientBinField_ofBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.quotientBinField_ofBits), [`MIPRE.SAT.quotientBinField_add`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.quotientBinField_add), [`MIPRE.SAT.quotientBinField_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.quotientBinField_mul), [`MIPRE.SAT.shoupBinField`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupBinField), [`MIPRE.SAT.shoupAdmissibleField`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupAdmissibleField), [`MIPRE.SAT.shoupMulProg_time_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupMulProg_time_le), [`MIPRE.SAT.shoupMulProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupMulProg_correct).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6909](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6909)
