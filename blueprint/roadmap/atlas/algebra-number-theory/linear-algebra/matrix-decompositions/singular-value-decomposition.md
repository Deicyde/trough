---
declaration: section
origin: cited
lean: Matrix.exists_unitaryGroup_mul_eq_rectangularDiagonal, Matrix.exists_unitaryGroup_rectangularDiagonal_antitone, Matrix.sum_sq_singularValues_eq_sum_sq_norm_of_svd, MathlibExt.LinearAlgebra.Matrix.ComplexSVDWanted.complex_singular_value_decomposition, Matrix.exists_unitaryGroup_diagonal_nonneg, Matrix.exists_orthogonalGroup_mul_eq_rectangularDiagonal, Matrix.exists_orthogonalGroup_rectangularDiagonal_antitone, MathlibExt.LinearAlgebra.Matrix.RealSVDWanted.real_singular_value_decomposition
statement: formalized
proof: formalized
---

# Singular value decomposition

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/singular-value-decomposition/index.html).

## Unitary reduction of a complex matrix to rectangular diagonal form

Every rectangular complex matrix becomes rectangular diagonal after a unitary
change of basis on the right, with a further unitary change of basis on the
codomain (S. Axler, Linear Algebra Done Right, 4th ed., Section 7E).

Formalized by `Matrix.exists_unitaryGroup_mul_eq_rectangularDiagonal`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/ComplexSVD.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ComplexSVD.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/singular-value-decomposition/index.html#exists-unitary-group-mul-eq-rectangular).

## Complex SVD with nonincreasing singular values

This is the rectangular complex SVD with singular values in nonincreasing order.

Proof: Multiply the rectangular-diagonal factorization on the right by `Vᴴ`.

Formalized by `Matrix.exists_unitaryGroup_rectangularDiagonal_antitone`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/ComplexSVD.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ComplexSVD.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/singular-value-decomposition/index.html#exists-unitary-group-rectangular-diagona).

## Squared Frobenius norm as the sum of squared singular values

Frobenius-norm identity for an SVD: the sum of the squared singular values is
the sum of the squared norms of the entries.

Formalized by `Matrix.sum_sq_singularValues_eq_sum_sq_norm_of_svd`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/ComplexSVD.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ComplexSVD.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/singular-value-decomposition/index.html#sum-sq-singular-values-eq-sum-sq-norm-of).

## Singular value decomposition of a complex matrix

Rectangular complex singular value decomposition: every complex `m × n` matrix
factors as `U * Σ * Vᴴ` with `U` and `V` unitary and `Σ` rectangular diagonal
with nonnegative entries; the singular values beyond the first `min m n`
(indices `j` with `m ≤ j.val`) are zero.

Proof: Apply the spectral theorem to `AᴴA`, normalize the images of the
eigenvectors with positive eigenvalues, and extend them to an orthonormal basis
of the codomain, as in the proof of S. Axler, Linear Algebra Done Right,
4th ed., 7.70, and the matrix form that follows it (Section 7E).

## Sources

- S. Axler, Linear Algebra Done Right, 4th ed., Section 7E; G. H. Golub and C. F. Van Loan, Matrix Computations, 4th ed., Johns Hopkins University Press (2013), Theorem 2.4.1.

Formalized by `MathlibExt.LinearAlgebra.Matrix.ComplexSVDWanted.complex_singular_value_decomposition`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/ComplexSVD.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/ComplexSVD.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/singular-value-decomposition/index.html#complex-singular-value-decomposition).

## Singular value decomposition of a complex square matrix

Let $A$ be a square complex matrix
whose rows and columns are indexed by a finite type $n$. Then there are unitary matrices $U$ and $V$
and nonnegative real numbers $\sigma_i$ for $i \in n$ such that, writing $D$ for the diagonal
matrix with diagonal entries $\sigma_i$ and $V^*$ for the conjugate transpose of $V$, we have
$A = U D V^*$.

## Sources

- R. A. Horn and C. R. Johnson, Matrix Analysis, 2nd ed., Cambridge University Press (2013).

Formalized by `Matrix.exists_unitaryGroup_diagonal_nonneg`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/Factorizations/SVD.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/Factorizations/SVD.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/singular-value-decomposition/index.html#exists-unitary-group-diagonal-nonneg).

## Orthogonal reduction of a real matrix to rectangular diagonal form

Let $A$ be a real
$m \times n$ matrix. Then there are orthogonal matrices $U$ of size $m \times m$ and $V$ of size
$n \times n$ and real numbers $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_n \ge 0$ with
$\sigma_j = 0$ for every $j > m$, such that $AV = U\Sigma$, where $\Sigma$ is the $m \times n$
matrix with $\Sigma_{jj} = \sigma_j$ for $j \le \min(m, n)$ and all other entries zero.

## Sources

- S. Axler, Linear Algebra Done Right, 4th ed., Section 7E.

Formalized by `Matrix.exists_orthogonalGroup_mul_eq_rectangularDiagonal`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/RealSVD.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/RealSVD.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/singular-value-decomposition/index.html#exists-orthogonal-group-mul-eq-rectangul).

## Real singular value decomposition with nonincreasing singular values

Let $A$ be a real
$m \times n$ matrix. Then there are orthogonal matrices $U$ of size $m \times m$ and $V$ of size
$n \times n$ and real numbers $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_n \ge 0$ with
$\sigma_j = 0$ for every $j > m$, such that $A = U \Sigma V^{\mathsf{T}}$, where $\Sigma$ is the
$m \times n$ matrix with $\Sigma_{jj} = \sigma_j$ for $j \le \min(m, n)$ and all other entries
zero.

Proof: multiply the factorization $AV = U\Sigma$ on the right by $V^{\mathsf{T}}$.

Formalized by `Matrix.exists_orthogonalGroup_rectangularDiagonal_antitone`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/RealSVD.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/RealSVD.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/singular-value-decomposition/index.html#exists-orthogonal-group-rectangular-diag).

## Real singular value decomposition

Let $A$ be a real $m \times n$ matrix. Then there are
orthogonal matrices $U$ of size $m \times m$ and $V$ of size $n \times n$ and real numbers
$\sigma_1, \dots, \sigma_n \ge 0$ with $\sigma_j = 0$ for every $j > m$, such that
$A = U \Sigma V^{\mathsf{T}}$, where $\Sigma$ is the $m \times n$ matrix with
$\Sigma_{jj} = \sigma_j$ for $j \le \min(m, n)$ and all other entries zero.

Proof: apply the spectral theorem to $A^{\mathsf{T}} A$, normalize the images under $A$ of the
eigenvectors with positive eigenvalues, and extend them to an orthonormal basis of
$\mathbb{R}^m$, as in the proof of S. Axler, Linear Algebra Done Right, 4th ed., 7.70, and the
matrix form that follows it (Section 7E).

## Sources

- G. H. Golub and C. F. Van Loan, Matrix Computations, 4th ed., Johns Hopkins University Press (2013), Theorem 2.4.1.

Formalized by `MathlibExt.LinearAlgebra.Matrix.RealSVDWanted.real_singular_value_decomposition`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/RealSVD.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/RealSVD.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/singular-value-decomposition/index.html#real-singular-value-decomposition).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Singular value decomposition](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/singular-value-decomposition/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/matrix-decompositions/singular-value-decomposition)
