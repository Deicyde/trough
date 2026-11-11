---
declaration: section
origin: cited
lean: Matrix.leadingPrincipalSubmatrix, Matrix.leadingPrincipalSubmatrix_self, Matrix.PosDef.fromBlocks, Matrix.posDef_iff_leadingPrincipalMinors_pos
statement: formalized
proof: formalized
---

# Sylvester's criterion

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/sylvester-s-criterion/index.html).

## Leading principal submatrix

The leading `k × k` principal submatrix of `A`: the submatrix on the
first `k` rows and columns.

Formalized by `Matrix.leadingPrincipalSubmatrix`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/SylvesterCriterion.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SylvesterCriterion.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/sylvester-s-criterion/index.html#leading-principal-submatrix).

## Full leading principal submatrix is the matrix itself

The full leading principal submatrix is the matrix itself.

Formalized by `Matrix.leadingPrincipalSubmatrix_self`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SylvesterCriterion.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SylvesterCriterion.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/sylvester-s-criterion/index.html#leading-principal-submatrix-self).

## Positive definiteness of a block matrix via the Schur complement

A block matrix with a positive definite top-left block and a positive
definite Schur complement is positive definite. This is the one-step
induction step of Sylvester's criterion, stated for a `1 × 1`
bottom-right block.

Formalized by `Matrix.PosDef.fromBlocks`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SylvesterCriterion.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SylvesterCriterion.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/sylvester-s-criterion/index.html#from-blocks).

## Sylvester's criterion

A Hermitian real matrix is positive
definite if and only if all of its leading principal minors are
positive. The Hermitian hypothesis is essential: `!![1, 2; 0, 1]` has
leading minors `1` and `1` but is not Hermitian, hence not positive
definite.

Formalized by `Matrix.posDef_iff_leadingPrincipalMinors_pos`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SylvesterCriterion.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SylvesterCriterion.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/sylvester-s-criterion/index.html#pos-def-iff-leading-principal-minors-pos).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sylvester's criterion](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/sylvester-s-criterion/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/positive-definite-matrices/sylvester-s-criterion)
