---
declaration: section
origin: cited
lean: MetaMathlibExt.det_maxMatrix_sub_X_smul_minMatrix, MetaMathlibExt.generalizedEigenvalue_interlacing
statement: formalized
---

# Generalized eigenvalues of max and min matrices

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/generalized-eigenvalues-of-max-and-min-matrices/index.html).

## Generalized eigenvalues of a MAX matrix to a MIN matrix

Let $n > 2$ and let
$0 < s_1 < s_2 < \dots < s_n$ be real numbers. Let $M$ be the $n \times n$ matrix with entries
$M_{ij} = \max(s_i, s_j)$, let $N$ be the $n \times n$ matrix with entries
$N_{ij} = \min(s_i, s_j)$, and put $\rho = \sqrt{s_n / s_1}$. Then, as polynomials in $X$ with
real coefficients,

$$\det(M - XN) = (-1)^n \det(N) \, (X - \rho)(X + 1)^{n-2}(X + \rho).$$

The roots of $\det(M - XN)$ are the generalized eigenvalues of $M$ to $N$.

## Sources

- Jorma K. Merikoski, Pentti Haukkanen, Antonio Sasaki, and Timo Tossavainen, *On Generalized Eigenvalues of MAX Matrices to MIN Matrices and LCM Matrices to GCD Matrices*, Journal of Integer Sequences 28 (2025), Article 25.7.1, Theorem 1 (`jis-2025-25.7.1-thm-1`).

Stated but not proved: `MetaMathlibExt.det_maxMatrix_sub_X_smul_minMatrix` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/MaxMinGeneralizedEigenvalueWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/LinearAlgebra/MaxMinGeneralizedEigenvalueWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/generalized-eigenvalues-of-max-and-min-matrices/index.html#det-max-matrix-sub-x-smul-min-matrix).

## Cauchy interlacing for generalized eigenvalues

Let $n \ge 1$, let $A$ be a Hermitian
and $B$ a positive definite complex $(n+1) \times (n+1)$ matrix, and let $A'$ and $B'$ be their
leading principal $n \times n$ submatrices (rows and columns $1, \dots, n$). Let
$\lambda_1 \ge \dots \ge \lambda_{n+1}$ be real numbers such that the roots of the polynomial
$\det(A - XB)$, counted with multiplicity, are exactly $\lambda_1, \dots, \lambda_{n+1}$, and
let $\lambda'_1 \ge \dots \ge \lambda'_n$ be real numbers such that the roots of
$\det(A' - XB')$, counted with multiplicity, are exactly $\lambda'_1, \dots, \lambda'_n$. Then
$\lambda_{k+1} \le \lambda'_k \le \lambda_k$ for every $k = 1, \dots, n$.

## Sources

- Jorma K. Merikoski, Pentti Haukkanen, Antonio Sasaki, and Timo Tossavainen, *On Generalized Eigenvalues of MAX Matrices to MIN Matrices and LCM Matrices to GCD Matrices*, Journal of Integer Sequences 28 (2025), Article 25.7.1, Theorem 6 (`jis-2025-25.7.1-thm-6`).

Stated but not proved: `MetaMathlibExt.generalizedEigenvalue_interlacing` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/MaxMinGeneralizedEigenvalueWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/LinearAlgebra/MaxMinGeneralizedEigenvalueWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/generalized-eigenvalues-of-max-and-min-matrices/index.html#generalized-eigenvalue-interlacing).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized eigenvalues of max and min matrices](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/generalized-eigenvalues-of-max-and-min-matrices/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/generalized-eigenvalues-of-max-and-min-matrices)
