---
declaration: section
origin: cited
lean: MathlibExt.LinearAlgebra.TriangularizationWanted.exists_basis_upperTriangular_toMatrix, MathlibExt.LinearAlgebra.TriangularizationWanted.exists_upperTriangular_similar_of_splits
statement: formalized
proof: formalized
---

# Triangularization

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/triangularization/index.html).

## Triangularization of an endomorphism with split characteristic polynomial

Let $V$ be a
finite-dimensional vector space over a field $K$, let $f$ be an endomorphism of $V$ whose
characteristic polynomial splits over $K$, and let $\iota$ be a finite linearly ordered set with
exactly $\dim_K V$ elements. Then there is a basis $(b_i)_{i \in \iota}$ of $V$ in which the matrix
of $f$ is upper triangular: its $(i, j)$ entry is $0$ whenever $j < i$.

Proof: induction on dimension. An eigenvector spans an invariant line, the induced map on the
quotient has split minimal polynomial (it divides that of $f$), and a triangularizing basis of the
quotient lifts, together with the eigenvector, to one of $V$. This is the eigenvector-deflation
induction of the proof of Schur's theorem in R. A. Horn and C. R. Johnson, Matrix Analysis, 2nd
ed., Cambridge University Press (2013), Theorem 2.3.1, without unitarity.

## Sources

- S. Axler, Linear Algebra Done Right, 4th ed., Springer (2024), Theorem 5.41.

Formalized by `MathlibExt.LinearAlgebra.TriangularizationWanted.exists_basis_upperTriangular_toMatrix`, a theorem declared in [MathlibExt/LinearAlgebra/Triangularization.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Triangularization.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/triangularization/index.html#exists-basis-upper-triangular-to-matrix).

## Triangularization of a matrix with split characteristic polynomial

Let $K$ be a field, let
$n$ be a finite linearly ordered index set, and let $A$ be a square matrix over $K$ with rows and
columns indexed by $n$ whose characteristic polynomial splits over $K$. Then there are an
invertible matrix $P$ and a matrix $T$, both over $K$ and indexed by $n$, such that $T$ is upper
triangular ($T_{ij} = 0$ whenever $j < i$) and $A = P T P^{-1}$.

Proof: triangularize the endomorphism of $K^n$ given by $A$ in the standard basis, and conjugate
by the change-of-basis matrix from the standard basis to the triangularizing basis.

## Sources

- R. A. Horn and C. R. Johnson, Matrix Analysis, 2nd ed., Cambridge University Press (2013), Theorem 2.3.1.

Formalized by `MathlibExt.LinearAlgebra.TriangularizationWanted.exists_upperTriangular_similar_of_splits`, a theorem declared in [MathlibExt/LinearAlgebra/Triangularization.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Triangularization.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/triangularization/index.html#exists-upper-triangular-similar-of-split).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Triangularization](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/triangularization/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/triangularization)
