---
declaration: section
origin: cited
lean: MathlibExt.LinearAlgebra.Matrix.HadamardDeterminant.hadamard_determinant_inequality, Matrix.PosSemidef.det_re_le_prod_diag_re, Matrix.PosSemidef.geomMean_det_le_trace_div, Matrix.PosSemidef.det_re_le_pow_trace_div, Matrix.PosSemidef.amgm_eq_iff, Matrix.PosSemidef.trace_mul_nonneg_re
statement: formalized
proof: formalized
---

# Hadamard's inequality and determinant bounds for positive semidefinite matrices

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/hadamard-s-inequality-and-determinant-bounds-for/index.html).

## Hadamard's determinant inequality

For every natural number $n$ and every $n \times n$
complex matrix $A = (a_{ij})$,

$$|\det A| \le \prod_{i=1}^{n} \Big( \sum_{j=1}^{n} |a_{ij}|^2 \Big)^{1/2},$$

that is, the absolute value of the determinant of $A$ is at most the product of the Euclidean
lengths of its rows.

## Sources

- J. Hadamard, Résolution d'une question relative aux déterminants, Bulletin des Sciences Mathématiques 17 (1893), 240–246.

Formalized by `MathlibExt.LinearAlgebra.Matrix.HadamardDeterminant.hadamard_determinant_inequality`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/HadamardDeterminant.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/HadamardDeterminant.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/hadamard-s-inequality-and-determinant-bounds-for/index.html#hadamard-determinant-inequality).

## Hadamard's inequality for positive semidefinite matrices

Let $A$ be a positive
semidefinite complex $n \times n$ matrix. Then the real part of the determinant of $A$ is at most
the product of the real parts of its diagonal entries:
$\operatorname{Re} \det A \le \prod_{i=1}^{n} \operatorname{Re} A_{ii}$.

Formalized by `Matrix.PosSemidef.det_re_le_prod_diag_re`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PosSemidefDeterminant.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/PosSemidefDeterminant.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/hadamard-s-inequality-and-determinant-bounds-for/index.html#det-re-le-prod-diag-re).

## AM–GM inequality for the determinant of a positive semidefinite matrix

Let $n \ge 1$
and let $A$ be a positive semidefinite complex $n \times n$ matrix. Then
$(\operatorname{Re} \det A)^{1/n} \le \operatorname{Re}(\operatorname{tr} A)/n$.

This is the arithmetic–geometric mean inequality for the eigenvalues of $A$.

Formalized by `Matrix.PosSemidef.geomMean_det_le_trace_div`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PosSemidefDeterminant.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/PosSemidefDeterminant.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/hadamard-s-inequality-and-determinant-bounds-for/index.html#geom-mean-det-le-trace-div).

## AM–GM inequality for the determinant of a positive semidefinite matrix, power form

Let $n \ge 1$ and let $A$ be a positive semidefinite complex $n \times n$ matrix. Then
$\operatorname{Re} \det A \le (\operatorname{Re}(\operatorname{tr} A)/n)^n$.

Formalized by `Matrix.PosSemidef.det_re_le_pow_trace_div`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PosSemidefDeterminant.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/PosSemidefDeterminant.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/hadamard-s-inequality-and-determinant-bounds-for/index.html#det-re-le-pow-trace-div).

## Equality in the AM–GM bound for the determinant

Let $n \ge 1$ and let $A$ be a positive
semidefinite complex $n \times n$ matrix. Then $(\operatorname{Re} \det A)^{1/n} =
\operatorname{Re}(\operatorname{tr} A)/n$ if and only if $A = cI$ for some real number $c \ge 0$,
where $I$ is the $n \times n$ identity matrix.

Formalized by `Matrix.PosSemidef.amgm_eq_iff`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PosSemidefDeterminant.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/PosSemidefDeterminant.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/hadamard-s-inequality-and-determinant-bounds-for/index.html#amgm-eq-iff).

## The trace of a product of positive semidefinite matrices has nonnegative real part

Let
$A$ and $B$ be positive semidefinite complex $n \times n$ matrices. Then the real part of the
trace of $AB$ is nonnegative: $\operatorname{Re} \operatorname{tr}(AB) \ge 0$.

Formalized by `Matrix.PosSemidef.trace_mul_nonneg_re`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PosSemidefDeterminant.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/PosSemidefDeterminant.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/hadamard-s-inequality-and-determinant-bounds-for/index.html#trace-mul-nonneg-re).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hadamard's inequality and determinant bounds for positive semidefinite matrices](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/hadamard-s-inequality-and-determinant-bounds-for/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/positive-definite-matrices/hadamard-s-inequality-and-determinant-bounds-for)
