---
declaration: section
origin: cited
lean: MathlibExt.LinearAlgebra.Matrix.LUDecompositionWanted.exists_lu_decomposition_of_minors_ne_zero, MathlibExt.LinearAlgebra.Matrix.LUDecompositionWanted.lu_decomposition_unique
statement: formalized
proof: formalized
---

# LU decomposition

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/lu-decomposition/index.html).

## LU decomposition without pivoting

Let $K$ be a field and $A$ an $n \times n$ matrix over
$K$ whose leading principal minors are all nonzero: for every $k \le n$, the determinant of the
upper-left $k \times k$ block of $A$ is nonzero. Then $A = LU$ for some $n \times n$ matrices
$L$ and $U$ over $K$ such that $L$ is lower triangular with every diagonal entry equal to $1$ and
$U$ is upper triangular.

Proof: Induct on the dimension and extend the factorization of the leading principal block by a
bordered (Schur-complement) step. The statement is the existence half of Wikipedia, "LU
decomposition", section "Existence and uniqueness".

## Sources

- L. N. Trefethen and D. Bau, Numerical Linear Algebra, SIAM (1997), Lecture 20.

Formalized by `MathlibExt.LinearAlgebra.Matrix.LUDecompositionWanted.exists_lu_decomposition_of_minors_ne_zero`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/LUDecomposition.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/LUDecomposition.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/lu-decomposition/index.html#exists-lu-decomposition-of-minors-ne-zer).

## Uniqueness of the LU decomposition

Let $K$ be a field and $A$ an invertible $n \times n$
matrix over $K$. Suppose $A = L_1 U_1 = L_2 U_2$, where $L_1$ and $L_2$ are lower triangular
$n \times n$ matrices over $K$ with every diagonal entry equal to $1$, and $U_1$ and $U_2$ are
upper triangular $n \times n$ matrices over $K$. Then $L_1 = L_2$ and $U_1 = U_2$.

Proof: Move the invertible triangular factors across the equality, then use the triangular inverse
and diagonal formulas to show the resulting matrix is the identity. The statement is the
uniqueness half of Wikipedia, "LU decomposition", section "Existence and uniqueness".

## Sources

- L. N. Trefethen and D. Bau, Numerical Linear Algebra, SIAM (1997), Lecture 20.

Formalized by `MathlibExt.LinearAlgebra.Matrix.LUDecompositionWanted.lu_decomposition_unique`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/LUDecomposition.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/LUDecomposition.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/lu-decomposition/index.html#lu-decomposition-unique).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: LU decomposition](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/lu-decomposition/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/matrix-decompositions/lu-decomposition)
