---
declaration: section
origin: cited
lean: Matrix.exists_unitaryGroup_posSemidef, Matrix.exists_unique_unitaryGroup_posDef_of_isUnit_det, MathlibExt.LinearAlgebra.Matrix.PolarDecompositionGLWanted.polar_decomposition_gl_real, MathlibExt.LinearAlgebra.Matrix.PolarDecompositionGLWanted.polar_decomposition_gl_complex
statement: formalized
proof: formalized
---

# Polar decomposition

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/polar-decomposition/index.html).

## Polar decomposition of a complex square matrix

Let $A$ be a square complex matrix indexed by
a finite type, and let $A^*$ be its conjugate transpose. Then there are a unitary matrix $U$ and a
positive semidefinite matrix $P$ such that $P^2 = A^* A$ and $A = UP$.

## Sources

- R. A. Horn and C. R. Johnson, Matrix Analysis, 2nd ed., Cambridge University Press (2013).

Formalized by `Matrix.exists_unitaryGroup_posSemidef`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/Factorizations/Polar.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/Factorizations/Polar.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/polar-decomposition/index.html#exists-unitary-group-pos-semidef).

## Uniqueness of the polar decomposition of an invertible matrix

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, and let $A$ be a square matrix over $\mathbb{K}$, indexed by a finite
type, with $\det A \neq 0$. Then there are a unitary matrix $U$ and a positive-definite matrix $P$
with $A = UP$, and they are unique: if $U'$ is unitary, $P'$ is positive definite and
$A = U'P'$, then $U' = U$ and $P' = P$.

Formalized by `Matrix.exists_unique_unitaryGroup_posDef_of_isUnit_det`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/Factorizations/Polar.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/Factorizations/Polar.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/polar-decomposition/index.html#exists-unique-unitary-group-pos-def-of-i).

## Polar decomposition of invertible real matrices

Let $A$ be a real square matrix with rows
and columns indexed by a finite set, and suppose $\det A \ne 0$. Then there are an orthogonal
matrix $O$ and a positive-definite symmetric matrix $S$ with $A = OS$, and they are unique: if
$O'$ is orthogonal, $S'$ is positive-definite symmetric and $A = O'S'$, then $O' = O$ and
$S' = S$.

Proof: take $S$ to be the positive-definite square root of $A^{\mathsf{T}} A$ and $O = AS^{-1}$,
the construction in Wikipedia, "Polar decomposition".

## Sources

- R. A. Horn and C. R. Johnson, Matrix Analysis, 2nd ed., Cambridge University Press (2013), Theorem 7.3.1.

Formalized by `MathlibExt.LinearAlgebra.Matrix.PolarDecompositionGLWanted.polar_decomposition_gl_real`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PolarDecompositionGL.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/PolarDecompositionGL.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/polar-decomposition/index.html#polar-decomposition-gl-real).

## Polar decomposition of invertible complex matrices

Let $A$ be a complex square matrix with
rows and columns indexed by a finite set, and suppose $\det A \ne 0$. Then there are a unitary
matrix $U$ and a positive-definite Hermitian matrix $P$ with $A = UP$, and they are unique: if
$U'$ is unitary, $P'$ is positive-definite Hermitian and $A = U'P'$, then $U' = U$ and $P' = P$.

Proof: take $P$ to be the positive-definite square root of $A^* A$ and $U = AP^{-1}$, the
construction in Wikipedia, "Polar decomposition".

## Sources

- R. A. Horn and C. R. Johnson, Matrix Analysis, 2nd ed., Cambridge University Press (2013), Theorem 7.3.1.

Formalized by `MathlibExt.LinearAlgebra.Matrix.PolarDecompositionGLWanted.polar_decomposition_gl_complex`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PolarDecompositionGL.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/PolarDecompositionGL.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/polar-decomposition/index.html#polar-decomposition-gl-complex).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polar decomposition](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/polar-decomposition/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/matrix-decompositions/polar-decomposition)
