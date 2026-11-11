---
declaration: section
origin: cited
lean: MetaMathlibExt.sum_signedStirlingFirst_mul_stirlingSecond, MetaMathlibExt.stirlingMatrices_mutualInverse_and_lowerTriangular, MetaMathlibExt.stirlingSecondShiftMatrix, MetaMathlibExt.stirlingSecondShiftMatrix_zero, MetaMathlibExt.stirlingSecondShiftMatrix_apply_zero_right, MetaMathlibExt.stirlingFirstMatrix, MetaMathlibExt.stirlingFirstMatrix_apply_self, MetaMathlibExt.stirlingVMatrix
statement: formalized
---

# Stirling matrices

30 results, 15 proved and 15 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html).

## Orthogonality relation for Stirling numbers

Write $c(n,k)$ for the unsigned Stirling
numbers of the first kind, $s(n,k) = (-1)^{n-k} c(n,k)$ for the signed ones, and $S(k,m)$ for the
Stirling numbers of the second kind. For all natural numbers $n$ and $m$,

$$\sum_{k=0}^{n} s(n,k)\, S(k,m) = \delta_{nm},$$

where $\delta_{nm}$ is $1$ if $n = m$ and $0$ otherwise.

Formalized by `MetaMathlibExt.sum_signedStirlingFirst_mul_stirlingSecond`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrices.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/StirlingMatrices.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#sum-signed-stirling-first-mul-stirling-s).

## Stirling matrices are mutually inverse and lower triangular

Let $N$ be a natural number,
and let $A$ and $B$ be the $N \times N$ integer matrices with rows and columns indexed by
$0, 1, \dots, N-1$ and entries $A_{ij} = (-1)^{i-j} c(i,j)$ and $B_{ij} = S(i,j)$, where $c(i,j)$
is the unsigned Stirling number of the first kind and $S(i,j)$ the Stirling number of the second
kind. Then $AB = BA = I$, and $A_{ij} = B_{ij} = 0$ whenever $i < j$.

## Sources

- Benjamin Schreyer, "Rigged Horse Numbers and their Modular Periodicity", Journal of Integer Sequences 28 (2025), Article 25.4.1, Proposition (equation stirlinginvs), lines 120–126, https://cs.uwaterloo.ca/journals/JIS/VOL28/Schreyer/schreyer7.tex (quoting L. Comtet, Advanced Combinatorics, Eqn. 6f, p. 144).

Formalized by `MetaMathlibExt.stirlingMatrices_mutualInverse_and_lowerTriangular`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrices.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/StirlingMatrices.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-matrices-mutual-inverse-and-low).

## Shifted Stirling matrix of the second kind

For natural numbers $m$ and $n$, the shifted
Stirling matrix $S^{[m]}(n)$ is the $n \times n$ matrix over $\mathbb{Q}$ whose $(i, j)$ entry is
the Stirling number of the second kind $S(i + m, j)$, for $1 \le i, j \le n$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Section 1 (definition of `S^[m](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/n)`).

Formalized by `MetaMathlibExt.stirlingSecondShiftMatrix`, a definition declared in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-second-shift-matrix).

## Shift zero gives the Stirling matrix of the second kind

For every natural number $n$, the
shifted Stirling matrix $S^{[0]}(n)$, the $n \times n$ rational matrix with entries $S(i + 0, j)$
for $1 \le i, j \le n$, equals the Stirling matrix of the second kind $S(n)$, the $n \times n$
rational matrix with entries $S(i, j)$; here $S(i, j)$ denotes the Stirling numbers of the
second kind.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Section 1 (definition of `S^[m](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/n)`).

Formalized by `MetaMathlibExt.stirlingSecondShiftMatrix_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-second-shift-matrix-zero).

## First column of a shifted Stirling matrix

Let $m$ and $n$ be natural numbers with $n > 0$,
and let $S^{[m]}(n)$ be the $n \times n$ rational matrix with entries $S(i + m, j)$ for
$1 \le i, j \le n$, where $S(i, j)$ denotes the Stirling numbers of the second kind. Every entry
of the first column of $S^{[m]}(n)$ equals $1$: $S(i + m, 1) = 1$ for $1 \le i \le n$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Section 1, Equation (5).

Formalized by `MetaMathlibExt.stirlingSecondShiftMatrix_apply_zero_right`, a theorem declared in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-second-shift-matrix-apply-zero).

## Stirling matrix of the first kind

For a natural number $n$, the Stirling matrix of the
first kind $s(n)$ is the $n \times n$ matrix with rational entries $s(n)_{i,j} = s(i, j)$ for
$1 \le i, j \le n$, where $s(i, j)$ is the signed Stirling number of the first kind. Its
entries above the diagonal are zero, since $s(i, j) = 0$ for $j > i$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Section 1 (definition of `s(n)`).

Formalized by `MetaMathlibExt.stirlingFirstMatrix`, a definition declared in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-first-matrix).

## Diagonal of the Stirling matrix of the first kind

For every natural number $n$, every
diagonal entry of the Stirling matrix of the first kind $s(n)$ equals $1$, that is,
$s(n)_{i,i} = 1$ for $1 \le i \le n$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Section 1 (`s(n, n) = 1`).

Formalized by `MetaMathlibExt.stirlingFirstMatrix_apply_self`, a theorem declared in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-first-matrix-apply-self).

## Upper bidiagonal matrix V(n)

For a natural number $n$, $V(n)$ is the $n \times n$
matrix over $\mathbb{Q}$, with rows and columns indexed by $1, \dots, n$, whose entries are
$V_{i,i} = i$ on the diagonal, $V_{i,i+1} = 1$ just above the diagonal, and $0$ elsewhere.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Section 2 (definition of `V(n)`).

Formalized by `MetaMathlibExt.stirlingVMatrix`, a definition declared in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-vmatrix).

## Diagonal entries of the bidiagonal matrix V(n)

For every natural number $n$, let $V(n)$ be
the $n \times n$ rational upper bidiagonal matrix with $V(n)_{i,i} = i$, $V(n)_{i,i+1} = 1$ and
all other entries $0$, indices running over $1, \dots, n$. Then $V(n)_{i,i} = i$ for every
$1 \le i \le n$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Section 2 (definition of `V(n)`).

Formalized by `MetaMathlibExt.stirlingVMatrix_apply_self`, a theorem declared in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-vmatrix-apply-self).

## Upper triangular matrix Ṽ(n)

For a natural number $n$, $\tilde V(n)$ is the
$n \times n$ matrix over $\mathbb{Q}$, with rows and columns indexed by $1, \dots, n$, whose
$(i, j)$ entry is $(-1)^{j-i} (i-1)!/j!$ if $i \le j$ and $0$ if $i > j$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Section 2 (definition of `Ṽ(n)`).

Formalized by `MetaMathlibExt.stirlingVTildeMatrix`, a definition declared in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-vtilde-matrix).

## Diagonal entries of the matrix Ṽ(n)

For a natural number $n$, let $\tilde V(n)$ be the
$n \times n$ upper triangular matrix over $\mathbb{Q}$, with rows and columns indexed by
$1, \dots, n$, whose $(i, j)$ entry is $(-1)^{j-i} (i-1)!/j!$ if $i \le j$ and $0$ if $i > j$.
Then for every $i$ with $1 \le i \le n$, the $(i, i)$ entry of $\tilde V(n)$ is $1/i$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Section 2 (definition of `Ṽ(n)`).

Formalized by `MetaMathlibExt.stirlingVTildeMatrix_apply_self`, a theorem declared in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-vtilde-matrix-apply-self).

## Shifted Vandermonde matrix

For a natural number $n$, the shifted Vandermonde matrix
$E(n)$ is the $n \times n$ matrix with rational entries $E(n)_{i,j} = (j + 1)^{i-1}$ for
$1 \le i, j \le n$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Section 2 (definition of `E(n)`).

Formalized by `MetaMathlibExt.shiftedVandermondeMatrix`, a definition declared in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#shifted-vandermonde-matrix).

## First row of the shifted Vandermonde matrix

For every natural number $n \ge 1$, every
entry in the first row of the shifted Vandermonde matrix $E(n)$ equals $1$, that is,
$E(n)_{1,j} = 1$ for $1 \le j \le n$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Section 2 (definition of `E(n)`).

Formalized by `MetaMathlibExt.shiftedVandermondeMatrix_apply_zero_left`, a theorem declared in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#shifted-vandermonde-matrix-apply-zero-le).

## Strictly upper triangular matrix $Q^{(N)}(n)$

For natural numbers $N$ and $n$,
$Q^{[N]}(n)$ is the $n \times n$ matrix with rational entries

$$Q^{[N]}(n)_{i,j} = \frac{(-1)^{j-i+1}\, i^{N-1}}{(i-1)!\,(j-i-1)!} \quad (1 \le i < j \le n)$$

and $Q^{[N]}(n)_{i,j} = 0$ for $1 \le j \le i \le n$. Here $N - 1$ is truncated subtraction,
so $Q^{[0]}(n) = Q^{[1]}(n)$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Section 2, Equation (6).

Formalized by `MetaMathlibExt.stirlingQMatrix`, a definition declared in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-qmatrix).

## Vanishing of $Q^{(N)}(n)$ on and below the diagonal

For natural numbers $N$ and $n$, let
$Q^{[N]}(n)$ be the $n \times n$ rational matrix with
$Q^{[N]}(n)_{i,j} = (-1)^{j-i+1} i^{N-1} / ((i-1)!\,(j-i-1)!)$ for $1 \le i < j \le n$ and $0$
otherwise, where $N - 1$ is truncated subtraction. Then $Q^{[N]}(n)_{i,j} = 0$ for all indices
$1 \le j \le i \le n$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Section 2, Equation (6).

Formalized by `MetaMathlibExt.stirlingQMatrix_apply_of_le`, a theorem declared in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-qmatrix-apply-of-le).

## Explicit inverse of the bidiagonal matrix V(n)

For every natural number $n$, let $V(n)$ be
the $n \times n$ rational upper bidiagonal matrix with $V(n)_{i,i} = i$, $V(n)_{i,i+1} = 1$ and
all other entries $0$, and let $\tilde V(n)$ be the upper triangular matrix with
$\tilde V(n)_{i,j} = (-1)^{j-i} (i-1)!/j!$ for $j \ge i$ and $\tilde V(n)_{i,j} = 0$ for $j < i$,
all indices running over $1, \dots, n$. Then $V(n)^{-1} = \tilde V(n)$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Lemma 1.

Stated but not proved: `MetaMathlibExt.stirlingVMatrix_inv` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-vmatrix-inv).

## Recurrence for $Q^{(N)}(n)$ in $N$

For natural numbers $n$ and $N$ with $N \ge 1$, let
$V(n)$ be the $n \times n$ upper bidiagonal matrix with $V(n)_{i,i} = i$, $V(n)_{i,i+1} = 1$
and all other entries $0$, let $I_n$ be the $n \times n$ identity matrix, and for $M \ge 1$ let
$Q^{[M]}(n)$ be the $n \times n$ matrix with
$Q^{[M]}(n)_{i,j} = (-1)^{j-i+1} i^{M-1} / ((i-1)!\,(j-i-1)!)$ for $j \ge i + 1$ and $0$
otherwise. Then, as matrices over $\mathbb{Q}$,

$$Q^{[N+1]}(n) = Q^{[N]}(n)\,(V(n) - I_n).$$

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Lemma 2.

Stated but not proved: `MetaMathlibExt.stirlingQMatrix_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-qmatrix-succ).

## Factorization of $Q^{(N)}(n)$ through $Q^{(1)}(n)$

For natural numbers $n$ and $N$ with
$N \ge 1$, let $V(n)$ be the $n \times n$ upper bidiagonal matrix with $V(n)_{i,i} = i$,
$V(n)_{i,i+1} = 1$ and all other entries $0$, let $I_n$ be the $n \times n$ identity matrix,
and for $M \ge 1$ let $Q^{[M]}(n)$ be the $n \times n$ matrix with
$Q^{[M]}(n)_{i,j} = (-1)^{j-i+1} i^{M-1} / ((i-1)!\,(j-i-1)!)$ for $j \ge i + 1$ and $0$
otherwise. Then, as matrices over $\mathbb{Q}$,

$$Q^{[N]}(n) = Q^{[1]}(n)\,(V(n) - I_n)^{N-1}.$$

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Corollary 1.

Stated but not proved: `MetaMathlibExt.stirlingQMatrix_eq_one_mul_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-qmatrix-eq-one-mul-pow).

## Stirling matrix of the second kind times $V(n) - I_n$

Let $n$ be a natural number. Let
$S(n)$ be the $n \times n$ Stirling matrix of the second kind, with entries the Stirling numbers
of the second kind $S(i, j)$ for $1 \le i, j \le n$; let $V(n)$ be the $n \times n$ upper
bidiagonal matrix with $V(n)_{i,i} = i$, $V(n)_{i,i+1} = 1$ and all other entries $0$; let
$I_n$ be the identity matrix, $E(n)$ the shifted Vandermonde matrix with
$E(n)_{i,j} = (j + 1)^{i-1}$, and $Q^{[1]}(n)$ the matrix with
$Q^{[1]}(n)_{i,j} = (-1)^{j-i+1} / ((i-1)!\,(j-i-1)!)$ for $j \ge i + 1$ and $0$ otherwise.
Then, as matrices over $\mathbb{Q}$,

$$S(n)\,(V(n) - I_n) = E(n)\,Q^{[1]}(n).$$

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Lemma 3, Equation (7).

Stated but not proved: `MetaMathlibExt.stirlingMatrix2_mul_sub_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-matrix2-mul-sub-one).

## Stirling matrix of the second kind times powers of $V(n) - I_n$

Let $n$ and $N$ be
natural numbers with $N \ge 1$. Let $S(n)$ be the $n \times n$ Stirling matrix of the second
kind, with entries the Stirling numbers of the second kind $S(i, j)$ for $1 \le i, j \le n$; let
$V(n)$ be the $n \times n$ upper bidiagonal matrix with $V(n)_{i,i} = i$, $V(n)_{i,i+1} = 1$
and all other entries $0$; let $I_n$ be the identity matrix, $E(n)$ the shifted Vandermonde
matrix with $E(n)_{i,j} = (j + 1)^{i-1}$, and $Q^{[N]}(n)$ the matrix with
$Q^{[N]}(n)_{i,j} = (-1)^{j-i+1} i^{N-1} / ((i-1)!\,(j-i-1)!)$ for $j \ge i + 1$ and $0$
otherwise. Then, as matrices over $\mathbb{Q}$,

$$S(n)\,(V(n) - I_n)^N = E(n)\,Q^{[N]}(n).$$

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Theorem 1.

Stated but not proved: `MetaMathlibExt.stirlingMatrix2_mul_sub_one_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-matrix2-mul-sub-one-pow).

## Factorization and determinant of shifted Stirling matrices

For natural numbers $m$ and
$n$, let $S(n)$ and $S^{[m]}(n)$ be the $n \times n$ rational matrices with entries $S(i, j)$ and
$S(i + m, j)$, where $S(i, j)$ denotes the Stirling numbers of the second kind, and let $V(n)$ be
the upper bidiagonal matrix with $V(n)_{i,i} = i$, $V(n)_{i,i+1} = 1$ and all other entries $0$,
all indices running over $1, \dots, n$. Then $S^{[m]}(n) = S(n)\, V(n)^m$ and
$\det S^{[m]}(n) = (n!)^m$.

The paper assumes $m, n \ge 1$; the cases $m = 0$ and $n = 0$ hold as well.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Theorem 2, Equation (18).

Stated but not proved: `MetaMathlibExt.stirlingSecondShiftMatrix_eq_mul_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-second-shift-matrix-eq-mul-pow).

## Recurrence for shifted Stirling matrices

For natural numbers $m$ and $n$, let $S^{[m]}(n)$
be the $n \times n$ rational matrix with entries $S(i + m, j)$, where $S(i, j)$ denotes the
Stirling numbers of the second kind, and let $V(n)$ be the upper bidiagonal matrix with
$V(n)_{i,i} = i$, $V(n)_{i,i+1} = 1$ and all other entries $0$, all indices running over
$1, \dots, n$. Then $S^{[m+1]}(n) = S^{[m]}(n)\, V(n)$ and
$\det S^{[m+1]}(n) = n! \cdot \det S^{[m]}(n)$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Corollary 2.

Stated but not proved: `MetaMathlibExt.stirlingSecondShiftMatrix_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-second-shift-matrix-succ).

## Composition of shifted Stirling matrices

For natural numbers $m$ and $n$, let $S^{[m]}(n)$
be the $n \times n$ rational matrix with entries $S(i + m, j)$ for $1 \le i, j \le n$, where
$S(i, j)$ denotes the Stirling numbers of the second kind, and let $s(n)$ be the $n \times n$
rational matrix with entries the signed Stirling numbers of the first kind $s(i, j)$ for
$1 \le i, j \le n$. Then for all natural numbers $m_1$, $m_2$ and $n$,
$S^{[m_1 + m_2]}(n) = S^{[m_1]}(n)\, s(n)\, S^{[m_2]}(n)$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Corollary 3.

Stated but not proved: `MetaMathlibExt.stirlingSecondShiftMatrix_add` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-second-shift-matrix-add).

## Inverse of a shifted Stirling matrix

For natural numbers $m$ and $n$, let $S^{[m]}(n)$ be
the $n \times n$ rational matrix with entries $S(i + m, j)$, where $S(i, j)$ denotes the Stirling
numbers of the second kind; let $s(n)$ be the matrix with entries the signed Stirling numbers of
the first kind $s(i, j)$; and let $\tilde V(n)$ be the upper triangular matrix with
$\tilde V(n)_{i,j} = (-1)^{j-i} (i-1)!/j!$ for $j \ge i$ and $\tilde V(n)_{i,j} = 0$ for $j < i$,
all indices running over $1, \dots, n$. Then $S^{[m]}(n)^{-1} = \tilde V(n)^m\, s(n)$.

The paper assumes $m \ge 1$; the case $m = 0$, which reads $S^{[0]}(n)^{-1} = s(n)$, holds as well.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Theorem 3.

Stated but not proved: `MetaMathlibExt.stirlingSecondShiftMatrix_inv` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-second-shift-matrix-inv).

## Shifted orthogonality of Stirling numbers

Write $s(n, k)$ for the signed Stirling
numbers of the first kind and $S(n, k)$ for the Stirling numbers of the second kind. For all
natural numbers $i$, $j$, $m$ with $1 \le j \le i$, the integer
$\sum_{l=1}^{i} s(i, l)\, S(l + m, j)$ equals $i^m$ if $i = j$ and $0$ if $i > j$.

The case $m = 0$ is included, although the source assumes $m \ge 1$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Theorem 4.

Stated but not proved: `MetaMathlibExt.sum_signedStirlingFirst_mul_stirlingSecond_add` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#sum-signed-stirling-first-mul-stirling-s-2).

## Alternating binomial sums of shifted Stirling numbers of the second kind

Write
$S(n, k)$ for the Stirling numbers of the second kind. For all natural numbers $i, j, N \ge 1$,
the following identity holds in the rational numbers:

$$\sum_{l=0}^{N} (-1)^{N-l} \binom{N}{l} S(i+l, j) =
\sum_{k=1}^{j-1} \frac{(-1)^{j-k+1} k^{N-1} (k+1)^{i-1}}{(k-1)!\,(j-k-1)!}.$$

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Theorem 5.

Stated but not proved: `MetaMathlibExt.sum_choose_stirlingSecond_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#sum-choose-stirling-second-eq).

## Difference of consecutive Stirling numbers of the second kind

For natural numbers
$i \ge 1$ and $j \ge 1$, the Stirling numbers of the second kind $S(i, j)$ satisfy, in $\mathbb{Q}$,

$$
S(i + 1, j) - S(i, j) = \sum_{k=1}^{j-1} \frac{(-1)^{j-k+1} (k + 1)^{i-1}}{(k - 1)!\,(j - k - 1)!}.
$$

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Corollary 4.

Stated but not proved: `MetaMathlibExt.stirlingSecond_succ_sub_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#stirling-second-succ-sub-eq-sum).

## Double-sum Kronecker delta identity for Stirling numbers

Write $S(n, k)$ for the Stirling
numbers of the second kind and $s(n, k)$ for the signed Stirling numbers of the first kind. For
all natural numbers $i, j, n$ with $i \ge 1$, $n \ge i$ and $n \ge j$, in the rational numbers,

$$\sum_{k_1=1}^{n} \sum_{k_2=k_1}^{n} (-1)^{k_2-k_1} \frac{(k_1-1)!}{k_2!}\,
S(i+1, k_1)\, s(k_2, j) = \delta_{i,j},$$

where $\delta_{i,j}$ is $1$ if $i = j$ and $0$ otherwise.

The hypothesis $i \ge 1$ cannot be dropped: for $i = j = 0$ the left side is $0$. The source's
hypothesis $j \ge 1$ is not needed.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Theorem 6.

Stated but not proved: `MetaMathlibExt.sum_sum_stirlingSecond_signedStirlingFirst_eq_ite` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#sum-sum-stirling-second-signed-stirling).

## Stirling numbers of the second kind from the next row

Write $S(n, k)$ for the Stirling
numbers of the second kind. For all natural numbers $i \ge 1$ and $j$, the rational number

$$\sum_{k=1}^{\min(i+1, j)} (-1)^{j-k} \frac{(k-1)!}{j!} S(i+1, k)$$

equals $S(i, j)$ if $j \le i$ and $0$ if $j > i$.

The case $j = 0$, where both sides vanish, is included although the source assumes $j \ge 1$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Theorem 7.

Stated but not proved: `MetaMathlibExt.sum_stirlingSecond_succ_eq_ite` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#sum-stirling-second-succ-eq-ite).

## Double-sum shift identity for Stirling numbers

Write $S(n, k)$ for the Stirling numbers
of the second kind and $s(n, k)$ for the signed Stirling numbers of the first kind. For all
natural numbers $i, j, n, m_1, m_2$ with $i \ge 1$, $n \ge i$ and $n \ge j$,

$$\sum_{k_1=1}^{n} \sum_{k_2=1}^{k_1} S(i+m_1, k_1)\, s(k_1, k_2)\, S(k_2+m_2, j) =
S(i+m_1+m_2, j).$$

The source leaves the shifts $m_1, m_2$ unquantified; here they are arbitrary natural numbers,
as in Corollary 3 of the source, and the source's hypothesis $j \ge 1$ is not needed.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *On Matrices Whose Entries Are Stirling Numbers of the Second Kind (I)*, INTEGERS 25 (2025), Article A27, Theorem 8.

Stated but not proved: `MetaMathlibExt.sum_sum_stirlingSecond_signedStirlingFirst_stirlingSecond` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/StirlingSecondKindMatricesWanted.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html#sum-sum-stirling-second-signed-stirling-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stirling matrices](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/stirling-matrices)
