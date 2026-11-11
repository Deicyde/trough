---
declaration: section
origin: cited
lean: MetaMathlibExt.inverse_eigenvalues, Matrix.exists_unitary_diagonal_of_isStarNormal
statement: formalized
---

# Eigenvalues and canonical forms: its own results

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/index.html).

Eigenvalues, eigenspaces and characteristic polynomials of matrices and endomorphisms, and the normal forms they lead to: diagonalization, triangularization, Jordan and Smith normal forms.

## Eigenvalues of the inverse matrix

Let $M$ be a square matrix over a field $K$, with rows
and columns indexed by a finite type, whose determinant is a unit of $K$ (so $M$ is invertible),
and let $\mu \in K$ be nonzero. Then a vector $x$ is an eigenvector of $M$ with eigenvalue $\mu$
(that is, $x \ne 0$ and $Mx = \mu x$) if and only if $x$ is an eigenvector of $M^{-1}$ with
eigenvalue $\mu^{-1}$.

## Sources

- https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix.

Stated but not proved: `MetaMathlibExt.inverse_eigenvalues` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/Matrix/InverseEigenvaluesWanted.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/LinearAlgebra/Matrix/InverseEigenvaluesWanted.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/index.html#inverse-eigenvalues).

## Spectral theorem for normal matrices

Let $M$ be a complex square matrix whose rows and
columns are indexed by a finite set $n$, and write $M^*$ for its conjugate transpose. If $M$ is
normal, that is, $M^* M = M M^*$, then there exist a unitary matrix $P$ indexed by $n$ (so
$P^* P = P P^* = I$) and a family of complex numbers $(d_i)_{i \in n}$ such that $P^* M P$ is
the diagonal matrix with diagonal entries $d_i$.

## Sources

- AlgebraNotes, Section: The Spectral Theorem, Subsection: The Spectral Theorem, Theorem (Spectral Theorem) (normal-matrix case; the Hermitian cases are Mathlib's `Matrix.IsHermitian.spectral_theorem`).

Formalized by `Matrix.exists_unitary_diagonal_of_isStarNormal`, a theorem declared in [MathlibExt/Analysis/Matrix/NormalSpectralTheorem.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Matrix/NormalSpectralTheorem.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/index.html#exists-unitary-diagonal-of-is-star-norma).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Eigenvalues and canonical forms](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms)
