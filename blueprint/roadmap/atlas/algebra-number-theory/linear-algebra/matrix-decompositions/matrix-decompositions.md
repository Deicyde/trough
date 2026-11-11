---
declaration: section
origin: cited
lean: MathlibExt.LinearAlgebra.Matrix.JacobiIterationWanted.jacobi_iteration_converges, MetaMathlibExt.rouche_capelli, Matrix.exists_unitaryGroup_isUpperTriangular
statement: formalized
---

# Matrix decompositions and linear systems: its own results

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/index.html).

Factorizations of matrices (singular value, polar, Schur and LU decompositions), Gaussian elimination and the solvability of linear systems, iterative methods and condition numbers.

## Convergence of the Jacobi method for strictly diagonally dominant matrices

Let $A$ be a
real square matrix with rows and columns indexed by a finite type, and let $b$ be a real vector.
Suppose $A$ is strictly diagonally dominant: $\sum_{j \ne i} |A_{ij}| < |A_{ii}|$ for every $i$.
Define the Jacobi sweep $J$ by $J(x)_i = \bigl(b_i - \sum_{j \ne i} A_{ij} x_j\bigr) / A_{ii}$.
Then there is a vector $x^*$ with $A x^* = b$ such that, for every starting vector $x_0$, the
iterates $J^k(x_0)$ converge to $x^*$ as $k \to \infty$.

## Sources

- G. H. Golub and C. F. Van Loan, Matrix Computations, 4th ed., Johns Hopkins Univ. Press, 2013, §11.2; https://en.wikipedia.org/wiki/Jacobi_method

Stated but not proved: `MathlibExt.LinearAlgebra.Matrix.JacobiIterationWanted.jacobi_iteration_converges` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/Matrix/JacobiIterationWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/LinearAlgebra/Matrix/JacobiIterationWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/index.html#jacobi-iteration-converges).

## Rouché–Capelli theorem

Let $K$ be a field, let $m$ be a set and $n$ a finite set, let $A$
be an $m \times n$ matrix over $K$, and let $b \in K^m$. Then the linear system $Ax = b$ has a
solution $x \in K^n$ if and only if the rank of $A$ equals the rank of the augmented matrix
$(A \mid b)$, whose columns are the columns of $A$ followed by the single column $b$.

Proof: Following the column-space argument in [Wikipedia, *Rouché–Capelli theorem*,
"Proof"](https://en.wikipedia.org/wiki/Rouch%C3%A9%E2%80%93Capelli_theorem#Proof), solvability is
membership of $b$ in the column span, which we compare before and after adjoining $b$.

## Sources

- https://en.wikipedia.org/wiki/Rouch%C3%A9%E2%80%93Capelli_theorem.

Formalized by `MetaMathlibExt.rouche_capelli`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/RoucheCapelli.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/RoucheCapelli.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/index.html#rouche-capelli).

## Schur decomposition of a complex square matrix

Let $A$ be a square complex matrix whose rows
and columns are indexed by a finite linearly ordered type $n$. Then there are a unitary matrix $U$,
with conjugate transpose $U^*$, and a matrix $T$ that is upper triangular with respect to the order
on $n$ (that is, $T_{ij} = 0$ whenever $j < i$) such that $A = U T U^*$.

## Sources

- I. Schur, Uber charakteristische Wurzeln, Math. Ann. 66 (1909), 488-510, DOI 10.1007/BF01450045.

Formalized by `Matrix.exists_unitaryGroup_isUpperTriangular`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/Factorizations/Schur.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/Factorizations/Schur.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/index.html#exists-unitary-group-is-upper-triangular).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Matrix decompositions and linear systems](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/matrix-decompositions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/matrix-decompositions)
