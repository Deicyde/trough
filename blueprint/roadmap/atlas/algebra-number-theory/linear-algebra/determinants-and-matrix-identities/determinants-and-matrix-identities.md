---
declaration: section
origin: cited
lean: MetaMathlibExt.CarrollIdentity.carroll_identity, MathlibExt.LinearAlgebra.Matrix.JacobiDetDerivativeWanted.jacobi_det_derivative, Matrix.isSymm_prod_iff, MathlibExt.LinearAlgebra.SymplecticDetWanted.LinearAlgebra.symplectic_matrix_det
statement: formalized
---

# Determinants and matrix identities: its own results

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/index.html).

Determinant expansions and identities, determinants of special products and exponentials, derivatives of determinants, and algebraic identities between matrices.

## Carroll (Desnanot–Jacobi) identity

Let $R$ be a commutative ring, let $n$ be a natural
number, and let $C$ be an $(n + 2) \times (n + 2)$ matrix over $R$. For indices $a$ and $b$,
write $C^{a}_{b}$ for the $(n + 1) \times (n + 1)$ matrix obtained from $C$ by deleting row $a$
and column $b$. Let $i \ne j$ be distinct indices and let $C^{ij}_{ij}$ be the $n \times n$
matrix obtained from $C$ by deleting rows $i$ and $j$ and columns $i$ and $j$. Then

$$\det C \cdot \det C^{ij}_{ij} = \det C^{i}_{i} \det C^{j}_{j} - \det C^{i}_{j} \det C^{j}_{i}.$$

For $n = 0$ the matrix $C^{ij}_{ij}$ is empty and its determinant is $1$.

## Sources

- Charles Delorme and Guillermo Pineda-Villavicencio, "Quadratic Form Representations via Generalized Continuants", Journal of Integer Sequences 18 (2015), Article 15.6.4, displayed lemma lines 133–142. https://cs.uwaterloo.ca/journals/JIS/VOL18/Pineda/pin2.tex. The source cites C. L. Dodgson, "Condensation of determinants, being a new and brief method for computing their arithmetical values", Proc. Roy. Soc. Lond. 15 (1866), 150–155.

Formalized by `MetaMathlibExt.CarrollIdentity.carroll_identity`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/CarrollIdentity.lean, line 996](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/CarrollIdentity.lean#L996). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/index.html#carroll-identity).

## Jacobi's formula

Let $n$ be a finite type, and let $A$ be a curve
$\mathbb{R} \to \mathbb{R}^{n \times n}$ of square real matrices with rows and columns indexed
by $n$. Suppose $A$ is differentiable at $t \in \mathbb{R}$. Then the derivative of
$s \mapsto \det A(s)$ at $t$ is $\operatorname{tr}\bigl(\operatorname{adj}(A(t))\, A'(t)\bigr)$,
where $\operatorname{adj}$ denotes the adjugate matrix and $A'(t)$ the derivative of $A$ at $t$.

## Sources

- R. A. Horn and C. R. Johnson, Matrix Analysis, 2nd ed., Cambridge Univ. Press, 2013, §0.8.10; https://en.wikipedia.org/wiki/Jacobi%27s_formula

Stated but not proved: `MathlibExt.LinearAlgebra.Matrix.JacobiDetDerivativeWanted.jacobi_det_derivative` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/Matrix/JacobiDetDerivativeWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/LinearAlgebra/Matrix/JacobiDetDerivativeWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/index.html#jacobi-det-derivative).

## Symmetry criterion for matrices indexed by a product

A matrix on a product is symmetric exactly when its restrictions to each row and column are
symmetric and both diagonals of every ordered rectangle agree in opposite directions.

Formalized by `Matrix.isSymm_prod_iff`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/ProductSymmetry.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/ProductSymmetry.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/index.html#is-symm-prod-iff).

## Symplectic matrices have determinant one

Let $R$ be a commutative ring, $l$ a finite
set, $I$ the identity matrix indexed by $l$, and
$J = \begin{pmatrix} 0 & -I \\ I & 0 \end{pmatrix}$ the matrix over $R$ indexed by the disjoint
union $l \sqcup l$. Every square matrix $A$ over $R$ indexed by $l \sqcup l$ with
$A J A^{\mathsf{T}} = J$ satisfies $\det A = 1$.

## Sources

- Folklore (Pfaffian computation). Listed as §39 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `symplectic_matrix_det` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.LinearAlgebra.SymplecticDetWanted.LinearAlgebra.symplectic_matrix_det` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/SymplecticDetWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/LinearAlgebra/SymplecticDetWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/index.html#symplectic-matrix-det).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Determinants and matrix identities](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/determinants-and-matrix-identities/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/determinants-and-matrix-identities)
