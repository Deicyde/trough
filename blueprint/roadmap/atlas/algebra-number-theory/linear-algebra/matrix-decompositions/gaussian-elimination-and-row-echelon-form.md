---
declaration: section
origin: cited
lean: Matrix.exists_unitLowerTriangular_mul_submatrix_isRowEchelon, MathlibExt.LinearAlgebra.Matrix.GaussPivotWanted.gauss_pivot_elim_step, MathlibExt.LinearAlgebra.Matrix.GaussPivotWanted.exists_gauss_elimination_opList, Matrix.IsReducedRowEchelon.col_eq_single_of_isLeadingEntry, Matrix.IsReducedRowEchelon.submatrix_orderIso, MathlibExt.LinearAlgebra.Matrix.ReducedRowEchelonWanted.exists_isReducedRowEchelon_rowEquivalent, MathlibExt.LinearAlgebra.Matrix.ReducedRowEchelonWanted.isReducedRowEchelon_unique_of_rowEquivalent, MathlibExt.LinearAlgebra.Matrix.ReducedRowEchelonWanted.ker_mulVecLin_mul_left_isUnit
statement: formalized
proof: formalized
---

# Gaussian elimination and row echelon form

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/gaussian-elimination-and-row-echelon-form/index.html).

## Row echelon form via a row permutation and a unit lower-triangular matrix

Let $K$ be a
field and let $A$ be a matrix over $K$ whose rows and columns are indexed by finite linearly
ordered sets. Then there are a permutation $\sigma$ of the row indices and a square matrix $L$ over
$K$ indexed by the row indices, lower triangular with every diagonal entry equal to $1$, such that
the matrix $L A_\sigma$ is in row echelon form. Here $A_\sigma$ is the matrix with entries
$(A_\sigma)_{ic} = A_{\sigma(i) c}$, and a matrix $B$ is in row echelon form when for all rows
$i_1 < i_2$ and every column $c$, if $B_{i_1 c'} = 0$ for every column $c' < c$, then
$B_{i_2 c} = 0$.

Formalized by `Matrix.exists_unitLowerTriangular_mul_submatrix_isRowEchelon`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/GaussPivot.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/GaussPivot.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/gaussian-elimination-and-row-echelon-form/index.html#exists-unit-lower-triangular-mul-submatr).

## One pivot step of Gaussian elimination

Let $K$ be a field and let $A$ be a matrix over $K$
whose rows are indexed by a finite linearly ordered set and whose columns are indexed by any
set. Let $r$ and $i_0$ be row
indices and $j$ a column index with $A_{i_0 j} \ne 0$, and let $A'$ be the matrix obtained from
$A$ by exchanging rows $r$ and $i_0$. Then there is a square matrix $P$ over $K$ indexed by the
row indices, lower triangular with every diagonal entry equal to $1$, such that
$(P A')_{i j} = 0$ for every row $i > r$.

The row $i_0$ may be any row with a nonzero entry in column $j$; this is not
magnitude-maximizing partial pivoting.

Proof: Use an entrywise unit lower-triangular matrix whose pivot column contains the elimination
coefficients, then evaluate the matrix product as a finite sum (row operations of type 3,
https://en.wikipedia.org/wiki/Gaussian_elimination).

## Sources

- L. N. Trefethen and D. Bau, Numerical Linear Algebra, SIAM (1997), Lectures 20-21.

Formalized by `MathlibExt.LinearAlgebra.Matrix.GaussPivotWanted.gauss_pivot_elim_step`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/GaussPivot.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/GaussPivot.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/gaussian-elimination-and-row-echelon-form/index.html#gauss-pivot-elim-step).

## Gaussian elimination as a product of row operations

Let $K$ be a field and let $A$ be a
matrix over $K$ whose rows and columns are indexed by finite linearly ordered sets. Then there
are a permutation $\sigma$ of the row indices and a finite, possibly empty, list
$M_1, \dots, M_\ell$ of square matrices over $K$ indexed by the row indices, each lower
triangular with every diagonal entry equal to $1$, such that the matrix
$M_1 M_2 \cdots M_\ell A_\sigma$ is in row echelon form. Here $A_\sigma$ is the matrix with
entries $(A_\sigma)_{ic} = A_{\sigma(i) c}$, the empty product is the identity matrix, and a
matrix $B$ is in row echelon form when for all rows $i_1 < i_2$ and every column $c$, if
$B_{i_1 c'} = 0$ for every column $c' < c$, then $B_{i_2 c} = 0$.

This records the factorization, not the intermediate matrices of an algorithm trace.

Proof: Induct on the columns after identifying the ordered index sets with initial segments of
the natural numbers; a nonzero first column uses a row pivot and recurses on the lower-right
block. Package the resulting single unit lower-triangular matrix as a one-element list (forward
elimination to row echelon form, https://en.wikipedia.org/wiki/Gaussian_elimination).

## Sources

- L. N. Trefethen and D. Bau, Numerical Linear Algebra, SIAM (1997), Lectures 20-21.

Formalized by `MathlibExt.LinearAlgebra.Matrix.GaussPivotWanted.exists_gauss_elimination_opList`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/GaussPivot.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/GaussPivot.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/gaussian-elimination-and-row-echelon-form/index.html#exists-gauss-elimination-op-list).

## Pivot columns of a reduced row echelon matrix

Let $R$ be a type with elements $0$ and
$1$, and let $A$ be a matrix over $R$ in reduced row echelon form whose rows are indexed by a
linearly ordered set and whose columns are indexed by a set with a relation $<$. Suppose that the
leading entry of row $i$ of $A$ is in column $c$, that is, $A_{ic} \neq 0$ and $A_{ij} = 0$ for
every column $j < c$. Then column $c$ of $A$ is the standard basis vector $e_i$: $A_{ic} = 1$ and
$A_{kc} = 0$ for every row $k \neq i$.

Formalized by `Matrix.IsReducedRowEchelon.col_eq_single_of_isLeadingEntry`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/ReducedRowEchelon.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/ReducedRowEchelon.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/gaussian-elimination-and-row-echelon-form/index.html#col-eq-single-of-is-leading-entry).

## Order-preserving reindexing of columns preserves reduced row echelon form

Let $R$ be a
type with elements $0$ and $1$, and let $A$ be a matrix over $R$ in reduced row echelon form whose
rows are indexed by a linearly ordered set and whose columns are indexed by a linearly ordered
set $N$. Let $e : O \to N$ be an order isomorphism from a linearly ordered set $O$. Then the
matrix $B$ with columns indexed by $O$ and entries $B_{ik} = A_{i\,e(k)}$ is in reduced row
echelon form.

Formalized by `Matrix.IsReducedRowEchelon.submatrix_orderIso`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/ReducedRowEchelon.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/ReducedRowEchelon.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/gaussian-elimination-and-row-echelon-form/index.html#submatrix-order-iso).

## Existence of the reduced row echelon form

Let $K$ be a field, let $m$ and $n$ be finite
linearly ordered sets, and let $A$ be an $m \times n$ matrix over $K$. Then there are an
$m \times n$ matrix $R$ over $K$ in reduced row echelon form and an invertible $m \times m$
matrix $P$ over $K$ with $R = PA$. In other words, $A$ is row-equivalent to a matrix in reduced
row echelon form.

Proof: Choose pivot columns greedily (columns outside the span of the earlier ones), extend them
to a basis of $K^m$ whose order matches the order of the rows, and take $R$ to be the coordinate
matrix of the columns of $A$ in that basis and $P$ the matrix of the coordinate map.

## Sources

- G. Strang, Introduction to Linear Algebra, 6th ed., Wellesley-Cambridge Press (2023), Section 2.2.

Formalized by `MathlibExt.LinearAlgebra.Matrix.ReducedRowEchelonWanted.exists_isReducedRowEchelon_rowEquivalent`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/ReducedRowEchelon.lean, line 571](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/ReducedRowEchelon.lean#L571). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/gaussian-elimination-and-row-echelon-form/index.html#exists-is-reduced-row-echelon-row-equiva).

## Uniqueness of the reduced row echelon form

Let $K$ be a field, let $m$ and $n$ be finite
linearly ordered sets, and let $R_1$ and $R_2$ be $m \times n$ matrices over $K$ in reduced row
echelon form. If $R_2 = P R_1$ for some invertible $m \times m$ matrix $P$ over $K$, then
$R_1 = R_2$. In other words, a row-equivalence class contains at most one matrix in reduced row
echelon form.

Proof: Reindex the columns along the order isomorphism between $\{0, \dots, |n| - 1\}$ and $n$.
For columns indexed by an initial segment of the natural numbers, induct on the number of
columns: the matrices agree on all but the last column by induction, and that forces their last
columns to agree.

## Sources

- G. Strang, Introduction to Linear Algebra, 6th ed., Wellesley-Cambridge Press (2023), Section 2.2.

Formalized by `MathlibExt.LinearAlgebra.Matrix.ReducedRowEchelonWanted.isReducedRowEchelon_unique_of_rowEquivalent`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/ReducedRowEchelon.lean, line 605](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/ReducedRowEchelon.lean#L605). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/gaussian-elimination-and-row-echelon-form/index.html#is-reduced-row-echelon-unique-of-row-equ).

## Invertible row operations preserve the null space

Let $K$ be a field, let $m$ and $n$ be
finite sets, let $A$ be an $m \times n$ matrix over $K$, and let $P$ be an
invertible $m \times m$ matrix over $K$. Then the linear maps $x \mapsto PAx$ and $x \mapsto Ax$
on $K^n$ have the same kernel; that is, the homogeneous systems $PAx = 0$ and $Ax = 0$ have the
same solutions.

Proof: For every $x \in K^n$ we have $(PA)x = P(Ax)$, and multiplication by $P$ is injective
because $P$ is invertible, so $(PA)x = 0$ if and only if $Ax = 0$.

## Sources

- G. Strang, Introduction to Linear Algebra, 6th ed., Wellesley-Cambridge Press (2023), Section 2.2.

Formalized by `MathlibExt.LinearAlgebra.Matrix.ReducedRowEchelonWanted.ker_mulVecLin_mul_left_isUnit`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/ReducedRowEchelon.lean, line 642](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/ReducedRowEchelon.lean#L642). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/gaussian-elimination-and-row-echelon-form/index.html#ker-mul-vec-lin-mul-left-is-unit).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gaussian elimination and row echelon form](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/gaussian-elimination-and-row-echelon-form/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/matrix-decompositions/gaussian-elimination-and-row-echelon-form)
