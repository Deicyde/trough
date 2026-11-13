---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.HoffmanWielandtWanted.hoffman_wielandt_hermitian, Matrix.PosDef.log_det_mul_le_trace
statement: formalized
proof: formalized
---

# Positive definite matrices and matrix inequalities: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/index.html).

Positive definite and semidefinite matrices, criteria for definiteness, and inequalities for their determinants, traces and eigenvalues.

## Hoffman–Wielandt inequality for Hermitian matrices

Let $A$ and $B$ be Hermitian
$n \times n$ complex matrices with eigenvalues $\lambda_1 \ge \dots \ge \lambda_n$ and
$\mu_1 \ge \dots \ge \mu_n$ respectively, counted with multiplicity. Then
$\sum_{i=1}^n (\lambda_i - \mu_i)^2 \le \sum_{i=1}^n \sum_{j=1}^n |A_{ij} - B_{ij}|^2$, that is,
the left side is at most the squared Frobenius norm of $A - B$.

## Sources

- A. J. Hoffman and H. W. Wielandt, Duke Math. J. 20 (1953), DOI 10.1215/S0012-7094-53-02004-3.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HoffmanWielandtWanted.hoffman_wielandt_hermitian`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HoffmanWielandt.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/HoffmanWielandt.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/index.html#hoffman-wielandt-hermitian).

## Log-determinant trace inequality

Let $A$ and $B$ be positive definite real square
matrices indexed by a finite set with $n$ elements. Then
$\log(\det A \cdot \det B) \le \operatorname{tr}(AB) - n$.

The eigenvalues $\lambda$ of the positive definite matrix $B^{1/2} A B^{1/2}$, where $B^{1/2}$ is
the positive semidefinite square root of $B$, satisfy $\log \lambda \le \lambda - 1$; this
matrix has determinant $\det A \det B$ and trace $\operatorname{tr}(AB)$.

Formalized by `Matrix.PosDef.log_det_mul_le_trace`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/LogDetTrace.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/LogDetTrace.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/index.html#log-det-mul-le-trace).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Positive definite matrices and matrix inequalities](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/positive-definite-matrices)
