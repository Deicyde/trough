---
declaration: section
origin: cited
lean: Matrix.lowerToeplitz, Matrix.lowerToeplitz_apply_of_le, Matrix.lowerToeplitz_apply_of_gt, Matrix.lowerToeplitz_apply_diag, MetaMathlibExt.IsToeplitzMatrix, MetaMathlibExt.IsSymmetricToeplitzMatrix, MetaMathlibExt.isToeplitzMatrix_of_witness, MetaMathlibExt.isSymmetricToeplitzMatrix_of_witness
statement: formalized
proof: formalized
---

# Toeplitz matrices

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-matrices/index.html).

## Lower-triangular Toeplitz matrix

Let $R$ be a set with a zero element $0$ and let
$a = (a_0, a_1, a_2, \dots)$ be a sequence in $R$. The lower-triangular Toeplitz matrix of $a$
is the matrix with rows and columns indexed by $\mathbb{N}$ whose $(i, j)$ entry is $a_{i-j}$
when $j \le i$ and $0$ when $j > i$. In particular it is constant along each diagonal and
vanishes strictly above the main diagonal.

## Sources

- Ming-Jian Ding and Jiang Zeng, "Some New Results on the Minuscule Polynomials of Type A," Journal of Integer Sequences 28 (2025), lines 640-653. URL: <https://cs.uwaterloo.ca/journals/JIS/VOL28/Zeng/zeng26.tex>.

Formalized by `Matrix.lowerToeplitz`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/LowerToeplitz.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/LowerToeplitz.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-matrices/index.html#lower-toeplitz).

## Entries on and below the diagonal of a lower-triangular Toeplitz matrix

Let $R$ be a
set with a zero element and $a = (a_0, a_1, \dots)$ a sequence in $R$. For natural numbers
$j \le i$, the $(i, j)$ entry of the lower-triangular Toeplitz matrix of $a$ is $a_{i-j}$.

Formalized by `Matrix.lowerToeplitz_apply_of_le`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/LowerToeplitz.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/LowerToeplitz.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-matrices/index.html#lower-toeplitz-apply-of-le).

## Entries above the diagonal of a lower-triangular Toeplitz matrix

Let $R$ be a set with
a zero element and $a = (a_0, a_1, \dots)$ a sequence in $R$. For natural numbers $i < j$, the
$(i, j)$ entry of the lower-triangular Toeplitz matrix of $a$ is $0$.

Formalized by `Matrix.lowerToeplitz_apply_of_gt`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/LowerToeplitz.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/LowerToeplitz.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-matrices/index.html#lower-toeplitz-apply-of-gt).

## Diagonal entries of a lower-triangular Toeplitz matrix

Let $R$ be a set with a zero
element and $a = (a_0, a_1, \dots)$ a sequence in $R$. For every natural number $i$, the
$(i, i)$ entry of the lower-triangular Toeplitz matrix of $a$ is $a_0$.

Formalized by `Matrix.lowerToeplitz_apply_diag`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/LowerToeplitz.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/LowerToeplitz.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-matrices/index.html#lower-toeplitz-apply-diag).

## Toeplitz matrix

A real $(n+1) \times (n+1)$ matrix $A = (a_{ij})$, with rows and columns
indexed by $\{0, \dots, n\}$, is Toeplitz if there is a function $c : \mathbb{Z} \to \mathbb{R}$
such that $a_{ij} = c(i - j)$ for all $i, j$. Equivalently, $A$ is constant along each of its
diagonals.

Only the values $c(k)$ with $-n \le k \le n$ enter the condition, so this is the same as asking
for real coefficients $c_{-n}, \dots, c_n$.

## Sources

- https://cs.uwaterloo.ca/journals/JIS/VOL18/Felsner/felsner2.tex

Formalized by `MetaMathlibExt.IsToeplitzMatrix`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/Toeplitz.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/Toeplitz.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-matrices/index.html#is-toeplitz-matrix).

## Symmetric Toeplitz matrix

A real $(n+1) \times (n+1)$ matrix $A = (a_{ij})$, with rows
and columns indexed by $\{0, \dots, n\}$, is symmetric Toeplitz if there is a function
$c : \mathbb{Z} \to \mathbb{R}$ such that $c(-k) = c(k)$ for every integer $k$ and
$a_{ij} = c(i - j)$ for all $i, j$.

## Sources

- https://cs.uwaterloo.ca/journals/JIS/VOL18/Felsner/felsner2.tex

Formalized by `MetaMathlibExt.IsSymmetricToeplitzMatrix`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/Toeplitz.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/Toeplitz.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-matrices/index.html#is-symmetric-toeplitz-matrix).

## Toeplitz matrices from coefficients

Let $A = (a_{ij})$ be a real $(n+1) \times (n+1)$
matrix with rows and columns indexed by $\{0, \dots, n\}$. If $c : \mathbb{Z} \to \mathbb{R}$
satisfies $a_{ij} = c(i - j)$ for all $i, j$, then $A$ is a Toeplitz matrix.

Formalized by `MetaMathlibExt.isToeplitzMatrix_of_witness`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/Toeplitz.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/Toeplitz.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-matrices/index.html#is-toeplitz-matrix-of-witness).

## Symmetric Toeplitz matrices from even coefficients

Let $A = (a_{ij})$ be a real
$(n+1) \times (n+1)$ matrix with rows and columns indexed by $\{0, \dots, n\}$. If
$c : \mathbb{Z} \to \mathbb{R}$ satisfies $c(-k) = c(k)$ for every integer $k$ and
$a_{ij} = c(i - j)$ for all $i, j$, then $A$ is a symmetric Toeplitz matrix.

Formalized by `MetaMathlibExt.isSymmetricToeplitzMatrix_of_witness`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/Toeplitz.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/Toeplitz.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-matrices/index.html#is-symmetric-toeplitz-matrix-of-witness).

## Symmetric Toeplitz matrices are Toeplitz

Every real $(n+1) \times (n+1)$ symmetric
Toeplitz matrix is a Toeplitz matrix.

Formalized by `MetaMathlibExt.IsSymmetricToeplitzMatrix.isToeplitz`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/Toeplitz.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/Toeplitz.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-matrices/index.html#is-toeplitz).

## Symmetric Toeplitz matrices are symmetric

If $A = (a_{ij})$ is a real
$(n+1) \times (n+1)$ symmetric Toeplitz matrix, with rows and columns indexed by
$\{0, \dots, n\}$, then $a_{ij} = a_{ji}$ for all $i, j$.

Formalized by `MetaMathlibExt.IsSymmetricToeplitzMatrix.entry_comm`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/Toeplitz.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/Toeplitz.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-matrices/index.html#entry-comm).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Toeplitz matrices](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/toeplitz-matrices/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/special-matrices/toeplitz-matrices)
