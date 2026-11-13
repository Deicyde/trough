---
declaration: section
origin: cited
lean: Matrix.IsHurwitz, Matrix.IsZMatrix, Matrix.IsNonsingularMMatrix, Matrix.isUnit_one_sub_of_spectralRadius_lt_one, Matrix.inv_one_sub_nonneg, Matrix.le_spectralRadius_of_smul_le_mulVec, Matrix.IsNonsingularMMatrix.isUnit, Matrix.IsNonsingularMMatrix.inv_nonneg
statement: formalized
proof: formalized
---

# M-matrices and Hurwitz stability

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/m-matrices-and-hurwitz-stability/index.html).

## Hurwitz matrix

A real square matrix is **Hurwitz** if every complex eigenvalue has negative real part.

Formalized by `Matrix.IsHurwitz`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/MMatrix.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/MMatrix.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/m-matrices-and-hurwitz-stability/index.html#is-hurwitz).

## Z-matrix

A **Z-matrix** has nonpositive off-diagonal entries.

Formalized by `Matrix.IsZMatrix`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/MMatrix.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/MMatrix.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/m-matrices-and-hurwitz-stability/index.html#is-zmatrix).

## Nonsingular M-matrix

A **nonsingular M-matrix** is a Z-matrix all of whose complex eigenvalues have positive
real part (Berman–Plemmons, Ch. 6, Theorem 2.3, condition (G20)).

Formalized by `Matrix.IsNonsingularMMatrix`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/MMatrix.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/MMatrix.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/m-matrices-and-hurwitz-stability/index.html#is-nonsingular-mmatrix).

## Invertibility of 1 − K when the spectral radius is below one

If the spectral radius of `K` is `< 1`, then `1` is not an eigenvalue of `K`, so `1 - K`
is invertible.

Formalized by `Matrix.isUnit_one_sub_of_spectralRadius_lt_one`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/MMatrix.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/MMatrix.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/m-matrices-and-hurwitz-stability/index.html#is-unit-one-sub-of-spectral-radius-lt-on).

## Neumann series

If `K` is entrywise nonnegative with spectral radius `< 1`, then
`(1 - K)⁻¹` is entrywise nonnegative (the proof identifies it with the limit of the partial
sums `∑_{n<N} Kⁿ`).

Formalized by `Matrix.inv_one_sub_nonneg`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/MMatrix.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/MMatrix.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/m-matrices-and-hurwitz-stability/index.html#inv-one-sub-nonneg).

## Collatz–Wielandt lower bound

If `K ≥ 0` entrywise, `z ≥ 0`, `z ≠ 0` and
`r • z ≤ K *ᵥ z` with `r ≥ 0`, then `r` is at most the spectral radius of `K`.

Formalized by `Matrix.le_spectralRadius_of_smul_le_mulVec`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/MMatrix.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/MMatrix.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/m-matrices-and-hurwitz-stability/index.html#le-spectral-radius-of-smul-le-mul-vec).

## Nonsingular M-matrices are invertible

A nonsingular M-matrix is invertible.

Formalized by `Matrix.IsNonsingularMMatrix.isUnit`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/MMatrix.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/MMatrix.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/m-matrices-and-hurwitz-stability/index.html#is-unit).

## Inverse positivity of M-matrices

The inverse of a nonsingular M-matrix is entrywise
nonnegative (Berman–Plemmons, Ch. 6, Theorem 2.3, (G20) ⇒ (N38)).

Formalized by `Matrix.IsNonsingularMMatrix.inv_nonneg`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/MMatrix.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/MMatrix.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/m-matrices-and-hurwitz-stability/index.html#inv-nonneg).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: M-matrices and Hurwitz stability](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/m-matrices-and-hurwitz-stability/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/special-matrices/m-matrices-and-hurwitz-stability)
