---
declaration: section
origin: cited
lean: Matrix.det_add_vecMulVec, Matrix.det_add_replicateCol_mul_replicateRow_general, Matrix.isUnit_add_vecMulVec_iff, Matrix.det_add_vecMulVec_of_isUnit_det
statement: formalized
proof: formalized
---

# Matrix determinant lemma

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/matrix-determinant-lemma/index.html).

## Matrix determinant lemma without invertibility

The **matrix determinant lemma**, without any invertibility hypothesis:
the determinant of a rank-one update of `A` is `det A` plus the adjugate
pairing `v ⬝ᵥ (adjugate A *ᵥ u)`. This is the general version left as a TODO
in Mathlib's `Matrix.det_add_replicateCol_mul_replicateRow`.

Formalized by `Matrix.det_add_vecMulVec`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/DeterminantLemma.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/DeterminantLemma.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/matrix-determinant-lemma/index.html#det-add-vec-mul-vec).

## Matrix determinant lemma in column-times-row form

The matrix determinant lemma in the `replicateCol` / `replicateRow`
form stated in Mathlib's TODO for
`Matrix.det_add_replicateCol_mul_replicateRow`. The `_general` suffix
avoids clashing with Mathlib's invertible version of the same name.

Formalized by `Matrix.det_add_replicateCol_mul_replicateRow_general`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/DeterminantLemma.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/DeterminantLemma.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/matrix-determinant-lemma/index.html#det-add-replicate-col-mul-replicate-row).

## Invertibility criterion for a rank-one update

A rank-one update of `A` is a unit exactly when the adjugate correction
term is a unit; no invertibility hypothesis on `A` is needed.

Formalized by `Matrix.isUnit_add_vecMulVec_iff`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/DeterminantLemma.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/DeterminantLemma.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/matrix-determinant-lemma/index.html#is-unit-add-vec-mul-vec-iff).

## Multiplicative matrix determinant lemma for invertible matrices

The matrix determinant lemma in multiplicative form, when `A.det` is a
unit: this recovers Mathlib's
`Matrix.det_add_replicateCol_mul_replicateRow` from the general version.

Formalized by `Matrix.det_add_vecMulVec_of_isUnit_det`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/DeterminantLemma.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/DeterminantLemma.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/matrix-determinant-lemma/index.html#det-add-vec-mul-vec-of-is-unit-det).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Matrix determinant lemma](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/matrix-determinant-lemma/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/determinants-and-matrix-identities/matrix-determinant-lemma)
