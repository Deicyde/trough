---
declaration: section
origin: cited
lean: Matrix.det_add_smul_vecMulVec, Matrix.detLinear, Matrix.coeff_one_det_add_X_smul, Matrix.detLinear_add, Matrix.detLinear_smul
statement: formalized
proof: formalized
---

# First-order expansion of the determinant

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/first-order-expansion-of-the-determinant/index.html).

## The determinant is affine along a rank-one direction

Let $K$ be a field, let $B$ be a
square matrix over $K$ indexed by a finite type $n$, and let $u, v \in K^n$. Then for every
$t \in K$, $\det(B + t\,uv^{\mathsf T}) = \det B + t\,(\det(B + uv^{\mathsf T}) - \det B)$.

Formalized by `Matrix.det_add_smul_vecMulVec`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/MvPolynomial.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/MvPolynomial.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/first-order-expansion-of-the-determinant/index.html#det-add-smul-vec-mul-vec).

## First-order term of the determinant

Let $R$ be a commutative ring and let $A$ and $B$ be
square matrices over $R$ indexed by a finite type $n$. The first-order term of the determinant
of $B$ in the direction $A$ is $L_B(A) = \sum_{i \in n} \det B^{(i)}$, where $B^{(i)}$ is the
matrix $B$ with its $i$-th row replaced by the $i$-th row of $A$.

It is the coefficient of $X$ in the polynomial $\det(B + XA)$.

Formalized by `Matrix.detLinear`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/MvPolynomial.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/MvPolynomial.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/first-order-expansion-of-the-determinant/index.html#det-linear).

## The coefficient of $X$ in $\det(B + XA)$

Let $R$ be a commutative ring and let $A$ and
$B$ be square matrices over $R$ indexed by a finite type $n$. Regard $B + XA$ as a matrix over
the polynomial ring $R[X]$. Then the coefficient of $X$ in the polynomial $\det(B + XA)$ equals
the first-order term of the determinant $L_B(A) = \sum_{i \in n} \det B^{(i)}$, where $B^{(i)}$
is the matrix $B$ with its $i$-th row replaced by the $i$-th row of $A$.

Formalized by `Matrix.coeff_one_det_add_X_smul`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/MvPolynomial.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/MvPolynomial.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/first-order-expansion-of-the-determinant/index.html#coeff-one-det-add-x-smul).

## Additivity of the first-order term of the determinant

Let $R$ be a commutative ring
and let $A$, $B$, $C$ be square matrices over $R$ indexed by a finite type $n$. Write
$L_B(A) = \sum_{i \in n} \det B^{(i)}_A$, where $B^{(i)}_A$ is the matrix $B$ with its $i$-th
row replaced by the $i$-th row of $A$. Then $L_B(A + C) = L_B(A) + L_B(C)$.

Formalized by `Matrix.detLinear_add`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/MvPolynomial.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/MvPolynomial.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/first-order-expansion-of-the-determinant/index.html#det-linear-add).

## Homogeneity of the first-order term of the determinant

Let $R$ be a commutative ring,
let $a \in R$, and let $A$ and $B$ be square matrices over $R$ indexed by a finite type $n$.
Write $L_B(A) = \sum_{i \in n} \det B^{(i)}_A$, where $B^{(i)}_A$ is the matrix $B$ with its
$i$-th row replaced by the $i$-th row of $A$. Then $L_B(aA) = a \, L_B(A)$.

Formalized by `Matrix.detLinear_smul`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/MvPolynomial.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/MvPolynomial.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/first-order-expansion-of-the-determinant/index.html#det-linear-smul).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: First-order expansion of the determinant](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/first-order-expansion-of-the-determinant/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/determinants-and-matrix-identities/first-order-expansion-of-the-determinant)
