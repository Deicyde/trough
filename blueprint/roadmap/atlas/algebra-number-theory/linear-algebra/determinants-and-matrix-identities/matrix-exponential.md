---
declaration: section
origin: cited
lean: Matrix.exp_mul_eq_mul_exp_of_mul_eq, MathlibExt.LinearAlgebra.Matrix.MatrixExpDetTraceWanted.matrix_det_exp_eq_exp_trace, MathlibExt.LinearAlgebra.Matrix.MatrixExpDetTraceWanted.matrix_exp_eq_sum_of_isNilpotent
statement: formalized
proof: formalized
---

# Matrix exponential

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/matrix-exponential/index.html).

## Intertwining passes to the exponential

If `A * X = X * B` for a rectangular matrix
`X`, then `exp A * X = X * exp B`.

Formalized by `Matrix.exp_mul_eq_mul_exp_of_mul_eq`, a theorem declared in [MathlibExt/Analysis/Normed/Algebra/MatrixExponentialIntertwining.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Algebra/MatrixExponentialIntertwining.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/matrix-exponential/index.html#exp-mul-eq-mul-exp-of-mul-eq).

## Determinant of the matrix exponential

For every complex square matrix $A$ indexed by a
finite set, $\det(e^A) = e^{\operatorname{tr} A}$, where $e^A$ is the matrix exponential. This
identity is sometimes called Jacobi's formula.

Proof: the three cases of B. C. Hall, An Elementary Introduction to Groups and Representations,
https://arxiv.org/abs/math-ph/0005032, Theorem 3.10. The Jordan-Chevalley decomposition writes
$A = N + S$ with $N$ nilpotent, $S$ semisimple and $NS = SN$, so $e^A = e^N e^S$. Diagonalizing
$S$ gives $\det(e^S) = e^{\operatorname{tr} S}$. For the nilpotent part, where Hall uses a
strictly upper-triangular form, $e^N - I$ is nilpotent, so $\det(e^N) = 1$, while
$\operatorname{tr} N = 0$.

## Sources

- B. C. Hall, Lie Groups, Lie Algebras, and Representations, 2nd ed., Springer (2015), Proposition 2.23.

Formalized by `MathlibExt.LinearAlgebra.Matrix.MatrixExpDetTraceWanted.matrix_det_exp_eq_exp_trace`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/MatrixExpDetTrace.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/MatrixExpDetTrace.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/matrix-exponential/index.html#matrix-det-exp-eq-exp-trace).

## Exponential of a nilpotent matrix

If $A$ is a nilpotent complex square matrix indexed by a
finite set, then there is a natural number $m$ such that
$e^A = \sum_{k=0}^{m-1} \frac{1}{k!} A^k$, where $e^A$ is the matrix exponential.

Proof: if $A^m = 0$, every term of the exponential series from index $m$ on vanishes.

## Sources

- R. A. Horn and C. R. Johnson, Matrix Analysis, 2nd ed., Cambridge University Press (2013), Section 3.2.

Formalized by `MathlibExt.LinearAlgebra.Matrix.MatrixExpDetTraceWanted.matrix_exp_eq_sum_of_isNilpotent`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/MatrixExpDetTrace.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/MatrixExpDetTrace.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/matrix-exponential/index.html#matrix-exp-eq-sum-of-is-nilpotent).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Matrix exponential](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/matrix-exponential/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/determinants-and-matrix-identities/matrix-exponential)
