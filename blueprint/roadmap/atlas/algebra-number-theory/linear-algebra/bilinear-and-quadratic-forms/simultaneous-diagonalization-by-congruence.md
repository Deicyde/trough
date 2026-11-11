---
declaration: section
origin: cited
lean: Matrix.PosDef.exists_isUnit_transpose_mul_mul_eq_one, MathlibExt.LinearAlgebra.Matrix.SimultaneousDiagonalizationWanted.simultaneous_diagonalization_posDef
statement: formalized
proof: formalized
---

# Simultaneous diagonalization by congruence

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/simultaneous-diagonalization-by-congruence/index.html).

## Positive-definite matrices are congruent to the identity

Let $P$ be a real square matrix
with rows and columns indexed by a finite set, and suppose $P$ is positive definite: $P$ is
symmetric and $x^{\mathsf{T}} P x > 0$ for every nonzero real vector $x$. Then there is an
invertible real matrix $Q$ of the same size such that $Q^{\mathsf{T}} P Q = I$, where $I$ is the
identity matrix.

Formalized by `Matrix.PosDef.exists_isUnit_transpose_mul_mul_eq_one`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SimultaneousDiagonalization.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SimultaneousDiagonalization.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/simultaneous-diagonalization-by-congruence/index.html#exists-is-unit-transpose-mul-mul-eq-one).

## Simultaneous diagonalization by congruence

Let $S$ and $P$ be real square matrices with rows
and columns indexed by a finite set $n$, where $S$ is symmetric and $P$ is positive definite. Then
there is an invertible real matrix $C$, indexed by $n$, such that $C^{\mathsf T} S C$ is diagonal
and $C^{\mathsf T} P C$ is the identity matrix.

Proof: Normalize $P$ to the identity by a congruence built from its orthonormal eigenbasis, scaled
by the inverse square roots of its eigenvalues, then orthogonally diagonalize the transformed
symmetric matrix. This is the argument of Wikipedia's "Definite matrix", section "Simultaneous
diagonalization", with the eigenbasis scaling in place of a Cholesky factor.

## Sources

- R. A. Horn and C. R. Johnson, Matrix Analysis, 2nd ed., Cambridge University Press (2013), Theorem 4.5.15.

Formalized by `MathlibExt.LinearAlgebra.Matrix.SimultaneousDiagonalizationWanted.simultaneous_diagonalization_posDef`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/SimultaneousDiagonalization.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/SimultaneousDiagonalization.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/simultaneous-diagonalization-by-congruence/index.html#simultaneous-diagonalization-pos-def).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Simultaneous diagonalization by congruence](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/simultaneous-diagonalization-by-congruence/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/bilinear-and-quadratic-forms/simultaneous-diagonalization-by-congruence)
