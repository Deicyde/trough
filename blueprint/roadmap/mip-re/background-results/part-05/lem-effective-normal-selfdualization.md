---
declaration: lemma
origin: cited
lean: MIPRE.Cost.recordIteratesProg, MIPRE.Cost.recordIteratesProg_apply, MIPRE.LowDegree.BinaryLinear.groupMatrixHom, MIPRE.LowDegree.BinaryLinear.inverseMatrix_groupMatrix, MIPRE.LowDegree.BinaryLinear.inverseRootMatrix_square, MIPRE.LowDegree.BinaryLinear.inverseRootMatrix_gram, MIPRE.LowDegree.BinaryLinear.circulantBitsProg_correct, MIPRE.LowDegree.BinaryLinear.rootBitsProg_vectorBits, MIPRE.LowDegree.BinaryLinear.inverseRootMatrixProg, MIPRE.LowDegree.BinaryLinear.inverseRootMatrixProg_correct, MIPRE.SAT.shoupTraceGram_normal_circulant, MIPRE.SAT.shoupNormalGram_selfDualize, MIPRE.SAT.shoupChangedVectors_normal, MIPRE.SAT.shoupSelfDualBasis_selfDual, MIPRE.SAT.shoupSelfDualBasis_normal, MIPRE.SAT.shoupSelfDualizeProg, MIPRE.SAT.shoupSelfDualizeProg_correct, MIPRE.SAT.shoupSelfDualizeProg_time_le
statement: formalized
proof: formalized
---

# Effective self-dualization of a supplied normal basis

Given the polynomial-basis encodings of any normal basis in the degree-$k$ Shoup field, for odd $k$, a uniform deterministic polynomial-time ambient program outputs the canonical encodings of a self-dual normal basis.

## Depends on

- [The binary square-root program](../part-04/lem-binary-square-root-program.md)
- [Self-dual and normal bases](../part-04/def-self-dual-basis.md)
- [Effective indexing and padding arithmetic](../../structure-of-the-proof/part-07/lem-pcp-padding-programs.md)

## Proof

The normal Gram matrix is the circulant determined by its first column. The regular representation embeds the binary cyclic group algebra into matrices, and the inverse of a nonsingular circulant remains circulant. Read the computed inverse's first column at doubled indices, then print its circulant matrix $H$. The coefficient square-root identity gives $H^2=G^{-1}$; symmetry and commutation give $H^{\mathsf T}GH=I$. Apply $H$ to the supplied basis columns. The identity Gram matrix proves independence, and a circulant change of coordinates preserves the Frobenius orbit. All matrix constructions and the final change of basis are implemented with polynomial runtime in $k$.

## Lean

Formalized as [`MIPRE.Cost.recordIteratesProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.recordIteratesProg), [`MIPRE.Cost.recordIteratesProg_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.recordIteratesProg_apply), [`MIPRE.LowDegree.BinaryLinear.groupMatrixHom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryLinear.groupMatrixHom), [`MIPRE.LowDegree.BinaryLinear.inverseMatrix_groupMatrix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryLinear.inverseMatrix_groupMatrix), [`MIPRE.LowDegree.BinaryLinear.inverseRootMatrix_square`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryLinear.inverseRootMatrix_square), [`MIPRE.LowDegree.BinaryLinear.inverseRootMatrix_gram`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryLinear.inverseRootMatrix_gram), [`MIPRE.LowDegree.BinaryLinear.circulantBitsProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryLinear.circulantBitsProg_correct), [`MIPRE.LowDegree.BinaryLinear.rootBitsProg_vectorBits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryLinear.rootBitsProg_vectorBits), [`MIPRE.LowDegree.BinaryLinear.inverseRootMatrixProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryLinear.inverseRootMatrixProg), [`MIPRE.LowDegree.BinaryLinear.inverseRootMatrixProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.BinaryLinear.inverseRootMatrixProg_correct), [`MIPRE.SAT.shoupTraceGram_normal_circulant`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupTraceGram_normal_circulant), [`MIPRE.SAT.shoupNormalGram_selfDualize`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupNormalGram_selfDualize), [`MIPRE.SAT.shoupChangedVectors_normal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupChangedVectors_normal), [`MIPRE.SAT.shoupSelfDualBasis_selfDual`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupSelfDualBasis_selfDual), [`MIPRE.SAT.shoupSelfDualBasis_normal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupSelfDualBasis_normal), [`MIPRE.SAT.shoupSelfDualizeProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupSelfDualizeProg), [`MIPRE.SAT.shoupSelfDualizeProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupSelfDualizeProg_correct), [`MIPRE.SAT.shoupSelfDualizeProg_time_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupSelfDualizeProg_time_le).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 7160](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L7160)
