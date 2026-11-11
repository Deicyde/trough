---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.WeylEigenvalueSum.weyl_eigenvalue_add_le, MathlibExt.Analysis.InnerProductSpace.WeylEigenvalueSum.le_weyl_eigenvalue_add, Matrix.IsHermitian.eigenvalues₀_add_le, Matrix.IsHermitian.le_eigenvalues₀_add, Matrix.IsHermitian.eigenvalues₀_congr, Matrix.IsHermitian.eigenvalues₀_diagonal_of_antitone, MathlibExt.Analysis.InnerProductSpace.WeylPerturbationWanted.weyl_eigenvalue_perturbation_le
statement: formalized
proof: formalized
---

# Weyl's eigenvalue inequalities

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/weyl-s-eigenvalue-inequalities/index.html).

## Weyl's inequality (upper bound)

For self-adjoint operators `T, S`,
`λ_{a+b}(T + S) ≤ λ_a(T) + λ_b(S)` whenever `a + b < n`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeylEigenvalueSum.weyl_eigenvalue_add_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeylEigenvalueSum.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/WeylEigenvalueSum.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/weyl-s-eigenvalue-inequalities/index.html#weyl-eigenvalue-add-le).

## Weyl's inequality (lower bound)

For self-adjoint operators `T, S`,
`λ_a(T) + λ_b(S) ≤ λ_{a+b-(n-1)}(T + S)` whenever `n - 1 ≤ a + b`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeylEigenvalueSum.le_weyl_eigenvalue_add`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeylEigenvalueSum.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/WeylEigenvalueSum.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/weyl-s-eigenvalue-inequalities/index.html#le-weyl-eigenvalue-add).

## Weyl's inequality (upper bound), matrix form

For Hermitian matrices
`A, B`, `λ_{a+b}(A + B) ≤ λ_a(A) + λ_b(B)` whenever `a + b < n`.

Formalized by `Matrix.IsHermitian.eigenvalues₀_add_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeylEigenvalueSum.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/WeylEigenvalueSum.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/weyl-s-eigenvalue-inequalities/index.html#eigenvalues-add-le).

## Weyl's inequality (lower bound), matrix form

For Hermitian matrices
`A, B`, `λ_a(A) + λ_b(B) ≤ λ_{a+b-(n-1)}(A + B)` whenever `n - 1 ≤ a + b`.

Formalized by `Matrix.IsHermitian.le_eigenvalues₀_add`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeylEigenvalueSum.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/WeylEigenvalueSum.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/weyl-s-eigenvalue-inequalities/index.html#le-eigenvalues-add).

## Eigenvalues of equal Hermitian matrices agree

Eigenvalues are unchanged when the matrix is replaced by an equal
matrix (useful to transport eigenvalue computations along identities such
as `diagonal d₁ + diagonal d₂ = diagonal (d₁ + d₂)`).

Formalized by `Matrix.IsHermitian.eigenvalues₀_congr`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeylEigenvalueSum.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/WeylEigenvalueSum.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/weyl-s-eigenvalue-inequalities/index.html#eigenvalues-congr).

## Eigenvalues of a diagonal matrix with decreasing entries

The eigenvalues of a diagonal Hermitian matrix whose diagonal entries
are already in decreasing order are exactly those entries.

Formalized by `Matrix.IsHermitian.eigenvalues₀_diagonal_of_antitone`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeylEigenvalueSum.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/WeylEigenvalueSum.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/weyl-s-eigenvalue-inequalities/index.html#eigenvalues-diagonal-of-antitone).

## Weyl's perturbation inequality

Let $A$ and $B$ be Hermitian $n \times n$ complex matrices,
and let $\lambda_1(A) \ge \dots \ge \lambda_n(A)$ and $\lambda_1(B) \ge \dots \ge \lambda_n(B)$ be
their eigenvalues, listed with multiplicity in decreasing order. Then
$|\lambda_i(A) - \lambda_i(B)| \le \|A - B\|$ for every $i$, where $\|A - B\|$ is the operator
norm of $A - B$ acting on $\mathbb{C}^n$ with the Euclidean norm.

## Sources

- H. Weyl, Math. Ann. 71 (1912), DOI 10.1007/BF01456804.

Formalized by `MathlibExt.Analysis.InnerProductSpace.WeylPerturbationWanted.weyl_eigenvalue_perturbation_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/WeylPerturbation.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/WeylPerturbation.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/weyl-s-eigenvalue-inequalities/index.html#weyl-eigenvalue-perturbation-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weyl's eigenvalue inequalities](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/weyl-s-eigenvalue-inequalities/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/eigenvalue-inequalities/weyl-s-eigenvalue-inequalities)
