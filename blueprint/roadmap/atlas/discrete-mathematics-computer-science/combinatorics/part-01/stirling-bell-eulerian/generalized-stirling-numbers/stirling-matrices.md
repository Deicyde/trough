---
declaration: section
origin: cited
lean: MetaMathlibExt.alphaStirlingEntry, MetaMathlibExt.shiftedAlphaStirlingEntry, MetaMathlibExt.alphaUpperEntry, MetaMathlibExt.alphaStirlingEntry_succ_succ, MetaMathlibExt.alphaStirlingEntry_zero_right, MetaMathlibExt.shiftedAlphaStirlingEntry_succ_succ, MetaMathlibExt.shiftedAlphaStirlingEntry_zero_left, MetaMathlibExt.alphaUpperEntry_succ_succ
statement: formalized
---

# α-Stirling matrices

50 results, 43 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html).

## Entries of the α-Stirling matrix

Let $R$ be a commutative ring and let
$\alpha_0, \alpha_1, \alpha_2, \dots$ be a sequence in $R$ ($\alpha_0$ is never used). The
α-Stirling entries $s_{i,j} \in R$, for $i, j \ge 0$, are defined recursively by
$s_{i,0} = \alpha_1$ for all $i$, $s_{0,j} = 0$ for $j \ge 1$, and
$s_{i+1,j+1} = s_{i,j} + \alpha_{j+2} s_{i,j+1}$ for all $i, j \ge 0$.

These are the entries of the paper's matrix $S_\alpha(n)$ with indices shifted to start at $0$.
Writing $\hat S_{i,j}$ for the entries of $S_\alpha(n)$ in the paper's $1$-based indexing, the
first column is $\alpha_1$, the rest of the first row is $0$, and
$\hat S_{i,j} = \hat S_{i-1,j-1} + \alpha_j \hat S_{i-1,j}$ for $i, j \ge 2$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Section 1.4, equation (a-1).

Formalized by `MetaMathlibExt.alphaStirlingEntry`, a definition declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#alpha-stirling-entry).

## Entries of the shifted α-Stirling matrix

Let $R$ be a commutative ring and let
$\alpha = (\alpha_j)_{j \ge 1}$ be a sequence in $R$. The entries $\mathsf{S}_{i,j} \in R$ of the
shifted $\alpha$-Stirling matrix of $\alpha$, for natural numbers $i$ and $j$ counted from $0$, are
defined by $\mathsf{S}_{i,0} = \alpha_1$ for all $i$, $\mathsf{S}_{0,j} = \alpha_1$ for all $j$,
and

$$\mathsf{S}_{i+1,j+1} = \mathsf{S}_{i+1,j} + \alpha_{j+2} \mathsf{S}_{i,j+1}.$$

The paper indexes from $1$: its entry $(i, j)$ is $P_{i,j} = \mathsf{S}_{i-1,j-1}$ for
$i, j \ge 1$. In this indexing the first row and the first column equal $\alpha_1$, and
$P_{i,j} = P_{i,j-1} + \alpha_j P_{i-1,j}$ for $i, j \ge 2$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Section 1.4.

Formalized by `MetaMathlibExt.shiftedAlphaStirlingEntry`, a definition declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#shifted-alpha-stirling-entry).

## Entries of the α-upper matrix

Let $R$ be a commutative ring and let
$\alpha_0, \alpha_1, \alpha_2, \dots$ be a sequence in $R$ ($\alpha_0$ is never used). The
α-upper entries $u_{i,j} \in R$, for $i, j \ge 0$, are defined recursively by $u_{0,j} = 1$ for
all $j$, $u_{i,0} = 0$ for $i \ge 1$, and
$u_{i+1,j+1} = u_{i+1,j} + \alpha_{i+1} u_{i,j} + (\alpha_{j+2} - \alpha_{i+1}) u_{i,j+1}$ for
all $i, j \ge 0$.

These are the entries of the paper's matrix $\mathsf{U}_\alpha(n)$ with indices shifted to start
at $0$; in the paper's $1$-based indexing the first row is $1$, the rest of the first column is
$0$, and $\mathsf{U}_{i,j} = \mathsf{U}_{i,j-1} + \alpha_{i-1} \mathsf{U}_{i-1,j-1} +
(\alpha_j - \alpha_{i-1}) \mathsf{U}_{i-1,j}$ for $i, j \ge 2$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Section 2, equation (u-1-2).

Formalized by `MetaMathlibExt.alphaUpperEntry`, a definition declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#alpha-upper-entry).

## Recurrence for the α-Stirling entries

Let $R$ be a commutative ring, let $\alpha$ be a
sequence in $R$, and let $s_{i,j}$ ($i, j \ge 0$) be the α-Stirling entries of $\alpha$. Then for
all $i, j \ge 0$, $s_{i+1,j+1} = s_{i,j} + \alpha_{j+2} s_{i,j+1}$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, equation (a-1).

Formalized by `MetaMathlibExt.alphaStirlingEntry_succ_succ`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#alpha-stirling-entry-succ-succ).

## First column of the α-Stirling entries

Let $R$ be a commutative ring, let $\alpha$ be a
sequence in $R$, and let $s_{i,j}$ ($i, j \ge 0$) be the α-Stirling entries of $\alpha$. Then
$s_{i,0} = \alpha_1$ for every $i \ge 0$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, equation (a-1).

Formalized by `MetaMathlibExt.alphaStirlingEntry_zero_right`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#alpha-stirling-entry-zero-right).

## Recurrence for the shifted α-Stirling entries

Let $R$ be a commutative ring, let
$\alpha = (\alpha_j)_{j \ge 1}$ be a sequence in $R$, and write $\mathsf{S}_{i,j}$ for the entries
of the shifted $\alpha$-Stirling matrix of $\alpha$, indexed from $0$. For all natural numbers $i$
and $j$,

$$\mathsf{S}_{i+1,j+1} = \mathsf{S}_{i+1,j} + \alpha_{j+2} \mathsf{S}_{i,j+1}.$$

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Section 1.4.

Formalized by `MetaMathlibExt.shiftedAlphaStirlingEntry_succ_succ`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#shifted-alpha-stirling-entry-succ-succ).

## First row of the shifted α-Stirling matrix

Let $R$ be a commutative ring, let
$\alpha = (\alpha_j)_{j \ge 1}$ be a sequence in $R$, and write $\mathsf{S}_{i,j}$ for the entries
of the shifted $\alpha$-Stirling matrix of $\alpha$, indexed from $0$. For every natural number
$j$, $\mathsf{S}_{0,j} = \alpha_1$; that is, the first row is constant, equal to $\alpha_1$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Section 1.4.

Formalized by `MetaMathlibExt.shiftedAlphaStirlingEntry_zero_left`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#shifted-alpha-stirling-entry-zero-left).

## Recurrence for the α-upper entries

Let $R$ be a commutative ring, let $\alpha$ be a
sequence in $R$, and let $u_{i,j}$ ($i, j \ge 0$) be the α-upper entries of $\alpha$. Then for all
$i, j \ge 0$,
$u_{i+1,j+1} = u_{i+1,j} + \alpha_{i+1} u_{i,j} + (\alpha_{j+2} - \alpha_{i+1}) u_{i,j+1}$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, equation (u-1-2).

Formalized by `MetaMathlibExt.alphaUpperEntry_succ_succ`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#alpha-upper-entry-succ-succ).

## Small α-upper entries

Let $R$ be a commutative ring, let $\alpha$ be a sequence in $R$,
and let $u_{i,j}$ ($i, j \ge 0$) be the α-upper entries of $\alpha$. Then $u_{1,1} = \alpha_2$ and
$u_{1,2} = \alpha_2 + \alpha_3$.

Writing $\mathsf{U}_{i,j}$ for the entries of the paper's matrix $\mathsf{U}_\alpha(n)$ in its
$1$-based indexing, these are $\mathsf{U}_{2,2} = \alpha_2$ and
$\mathsf{U}_{2,3} = \alpha_2 + \alpha_3$, as in the paper's display of $\mathsf{U}_\alpha(4)$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Section 2.

Formalized by `MetaMathlibExt.alphaUpperEntry_one_one_one_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#alpha-upper-entry-one-one-one-two).

## The α-Stirling matrix

Let $R$ be a commutative ring, let $\alpha$ be a sequence in $R$,
and let $s_{i,j}$ ($i, j \ge 0$) be the α-Stirling entries of $\alpha$. For $n \ge 0$, the matrix
$S_\alpha(n)$ is the $n \times n$ matrix over $R$, with rows and columns indexed by
$0, 1, \dots, n - 1$, whose $(i, j)$ entry is $s_{i,j}$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Section 1.4.

Formalized by `MetaMathlibExt.alphaStirlingMatrix`, a definition declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#alpha-stirling-matrix).

## Shifted α-Stirling matrix

Let $R$ be a commutative ring, let
$\alpha = (\alpha_j)_{j \ge 1}$ be a sequence in $R$, and let $n$ be a natural number. The shifted
$\alpha$-Stirling matrix $\mathsf{S}_\alpha(n)$ is the $n \times n$ matrix over $R$ whose entry in
row $i$ and column $j$ (counted from $0$) is the shifted $\alpha$-Stirling entry
$\mathsf{S}_{i,j}$, given by $\mathsf{S}_{i,0} = \mathsf{S}_{0,j} = \alpha_1$ and
$\mathsf{S}_{i+1,j+1} = \mathsf{S}_{i+1,j} + \alpha_{j+2} \mathsf{S}_{i,j+1}$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Section 1.4.

Formalized by `MetaMathlibExt.shiftedAlphaStirlingMatrix`, a definition declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#shifted-alpha-stirling-matrix).

## The α-upper matrix

Let $R$ be a commutative ring, let $\alpha$ be a sequence in $R$, and
let $u_{i,j}$ ($i, j \ge 0$) be the α-upper entries of $\alpha$. For $n \ge 0$, the matrix
$\mathsf{U}_\alpha(n)$ is the $n \times n$ matrix over $R$, with rows and columns indexed by
$0, 1, \dots, n - 1$, whose $(i, j)$ entry is $u_{i,j}$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Section 2.

Formalized by `MetaMathlibExt.alphaUpperMatrix`, a definition declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#alpha-upper-matrix).

## α-upper entries are complete homogeneous symmetric polynomials

Let $R$ be a commutative
ring, let $\alpha$ be a sequence in $R$, and let $u_{i,j}$ ($i, j \ge 0$) be the α-upper entries
of $\alpha$. For all $i \le j$, $u_{i,j} = h_i(\alpha_{i+1}, \alpha_{i+2}, \dots, \alpha_{j+1})$,
where $h_i$ is the complete homogeneous symmetric polynomial of degree $i$ in $j - i + 1$
variables.

Writing $\mathsf{U}_{i,j}$ for the entries of the paper's matrix $\mathsf{U}_\alpha(n)$ in its
$1$-based indexing, this reads $\mathsf{U}_{i,j} = h_{i-1}(\alpha_i, \dots, \alpha_j)$ for
$j \ge i \ge 1$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Lemma 1 (`jis-2026-26.5.4-lem-1`).

Stated but not proved: `MetaMathlibExt.alphaUpperEntry_eq_hsymm` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#alpha-upper-entry-eq-hsymm).

## Determinant of the α-upper matrix

Let $R$ be a commutative ring and let $\alpha$ be a
sequence in $R$. For every $n \ge 0$, the determinant of the $n \times n$ α-upper matrix
$\mathsf{U}_\alpha(n)$ is $\det \mathsf{U}_\alpha(n) = \prod_{i=1}^{n} \alpha_i^{i-1}$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Lemma 1 (`jis-2026-26.5.4-lem-1`).

Stated but not proved: `MetaMathlibExt.det_alphaUpperMatrix` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#det-alpha-upper-matrix).

## LU decomposition of the shifted α-Stirling matrix

Let $R$ be a commutative ring, let
$\alpha = (\alpha_j)_{j \ge 1}$ be a sequence in $R$, and let $n$ be a natural number. Then

$$\mathsf{S}_\alpha(n) = S_\alpha(n) \mathsf{U}_\alpha(n),$$

where $\mathsf{S}_\alpha(n)$ is the $n \times n$ shifted $\alpha$-Stirling matrix, $S_\alpha(n)$
is the $n \times n$ $\alpha$-Stirling matrix and $\mathsf{U}_\alpha(n)$ is the $n \times n$ upper
matrix of $\alpha$.

The paper assumes $\alpha_1 = 1$. The identity holds for every sequence $\alpha$ because both
sides scale by $\alpha_1$ and $\mathsf{U}_\alpha(n)$ does not depend on $\alpha_1$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Theorem 2 (`jis-2026-26.5.4-thm-2`).

Stated but not proved: `MetaMathlibExt.shiftedAlphaStirlingMatrix_eq_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#shifted-alpha-stirling-matrix-eq-mul).

## Determinant of the shifted $\alpha$-Stirling matrix

Let $R$ be a commutative ring and
let $(\alpha_j)_{j \ge 1}$ be a sequence in $R$ with $\alpha_1 = 1$. For $n \ge 0$ let
$\mathsf{S}_\alpha(n)$ be the $n \times n$ matrix whose $(i, j)$ entry $\mathsf{S}_{i,j}$, with
rows and columns indexed from $1$, is $\alpha_1$ when $i = 1$ or $j = 1$, and satisfies
$\mathsf{S}_{i,j} = \mathsf{S}_{i,j-1} + \alpha_j \mathsf{S}_{i-1,j}$ for $i, j \ge 2$. Then
$\det \mathsf{S}_\alpha(n) = \prod_{j=1}^{n} \alpha_j^{\,j-1}$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Theorem 2 (`jis-2026-26.5.4-thm-2`).

Stated but not proved: `MetaMathlibExt.det_shiftedAlphaStirlingMatrix` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#det-shifted-alpha-stirling-matrix).

## Pascal diagonal matrices

For $m, n \ge 0$, $\mathsf{L}_{d^{(m)}}(n)$ is the $n \times n$
real matrix that carries the $m$-th diagonal $d^{(m)}_b = \binom{m+b}{b}$ ($b \ge 0$) of Pascal's
triangle on its $m$-th subdiagonal: with rows and columns indexed from $0$, its $(b + m, b)$ entry
is $\binom{m+b}{b}$ for every $b$ with $b + m < n$, and all its other entries are $0$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Section 3.

Formalized by `MetaMathlibExt.pascalDiagonalMatrix`, a definition declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#pascal-diagonal-matrix).

## The zeroth Pascal diagonal matrix is the identity

For $m, n \ge 0$ let
$\mathsf{L}_{d^{(m)}}(n)$ be the $n \times n$ real matrix whose $(b + m, b)$ entry is
$\binom{m+b}{b}$ for each $b$ with $b + m < n$ and whose other entries are $0$, with rows and
columns indexed from $0$. Then $\mathsf{L}_{d^{(0)}}(n) = I_n$, the $n \times n$ identity matrix,
for every $n \ge 0$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Section 3.

Formalized by `MetaMathlibExt.pascalDiagonalMatrix_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#pascal-diagonal-matrix-zero).

## First-column sequence for exponentials of Pascal diagonal matrices

For $k \ge 0$, the
sequence of natural numbers $\alpha^{(k)} = (\alpha^{(k)}_i)_{i \ge 0}$ is defined by
$\alpha^{(k)}_0 = 0$, $\alpha^{(k)}_1 = 1$ and, for $i \ge 2$,
$\alpha^{(k)}_i = \binom{i-2}{k-1} \alpha^{(k)}_{i-k}$ if $1 \le k < i$ and $\alpha^{(k)}_i = 0$
otherwise. Thus $\alpha^{(k)}_i = 0$ for $2 \le i \le k$, and $\alpha^{(0)}_i = 0$ for all
$i \ne 1$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Theorem 3.

Formalized by `MetaMathlibExt.pascalExpFirstColumn`, a definition declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#pascal-exp-first-column).

## First term of the Pascal first-column sequence

For every $k \ge 0$, the first-column
sequence $\alpha^{(k)}$ satisfies $\alpha^{(k)}_1 = 1$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Theorem 3.

Formalized by `MetaMathlibExt.pascalExpFirstColumn_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#pascal-exp-first-column-one).

## Vanishing terms of the Pascal first-column sequence

For all natural numbers $k$ and $i$
with $2 \le i \le k$, the first-column sequence $\alpha^{(k)}$ satisfies $\alpha^{(k)}_i = 0$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Theorem 3.

Formalized by `MetaMathlibExt.pascalExpFirstColumn_of_le`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#pascal-exp-first-column-of-le).

## Recurrence for the Pascal first-column sequence

For all natural numbers $k$ and $i$ with
$1 \le k < i$, the first-column sequence $\alpha^{(k)}$ satisfies
$\alpha^{(k)}_i = \binom{i-2}{k-1} \alpha^{(k)}_{i-k}$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Theorem 3.

Formalized by `MetaMathlibExt.pascalExpFirstColumn_of_lt`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#pascal-exp-first-column-of-lt).

## Exponential of a Pascal diagonal matrix

Let $k \ge 1$ and $n \ge 0$. For $m \ge 0$ let
$\mathsf{L}_{d^{(m)}}(n)$ be the $n \times n$ real matrix whose $(b + m, b)$ entry is
$\binom{m+b}{b}$ for each $b$ with $b + m < n$ and whose other entries are $0$ (indices from
$0$). Let $\alpha^{(k)} = (\alpha^{(k)}_i)_{i \ge 1}$ be given by $\alpha^{(k)}_1 = 1$,
$\alpha^{(k)}_i = 0$ for $2 \le i \le k$ and
$\alpha^{(k)}_i = \binom{i-2}{k-1} \alpha^{(k)}_{i-k}$ for $i > k$, and let
$T_{\alpha^{(k)}, \beta}(n)$ be the $n \times n$ lower triangular Toeplitz matrix with first
column $\alpha^{(k)}$ and first row $\beta = (1, 0, 0, \ldots)$, that is, with $(a, b)$ entry
$\alpha^{(k)}_{a-b+1}$ for $b \le a$ and $0$ for $b > a$. Then $\exp(\mathsf{L}_{d^{(k)}}(n))$
equals the Hadamard (entrywise) product
$T_{\alpha^{(k)}, \beta}(n) \odot \sum_{i=0}^{n-1} \mathsf{L}_{d^{(ki)}}(n)$.

The paper sums over all $i \ge 0$; the terms with $i \ge n$ are zero matrices, since then
$ki \ge n$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Theorem 3 (`jis-2026-26.5.4-thm-3`).

Stated but not proved: `MetaMathlibExt.exp_pascalDiagonalMatrix` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#exp-pascal-diagonal-matrix).

## Factorial matrix of a power series

Let $K$ be a field, let $f$ be a formal power series
over $K$ in the variable $t$, and let $n$ be a natural number. The factorial matrix $M_n(f)$ is
the $n \times n$ matrix over $K$ whose entry in row $a$ and column $b$ (counted from $0$) is
$(a! \cdot 1_K) / (b! \cdot 1_K)$ times the coefficient of $t^{a-b}$ in $f$ when $b \le a$, and
$0$ when $b > a$. Here the quotient is taken in $K$ and is read as $0$ when $b! \cdot 1_K = 0$,
which can happen only in positive characteristic. When $K$ has characteristic zero, the factor is
the integer $a!/b!$ and $M_n(f)$ is the leading $n \times n$ section of the infinite lower
triangular matrix $M(f)$ of Moghaddamfar, Salehy and Salehy.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Section 3.

Formalized by `MetaMathlibExt.powerSeriesFactorialMatrix`, a definition declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#power-series-factorial-matrix).

## Diagonal of the factorial matrix of a power series

Let $K$ be a field of characteristic
zero, let $f$ be a formal power series over $K$ and let $n \ge 0$. Every diagonal entry of the
leading $n \times n$ section of $M(f)$, the lower triangular matrix whose $(a, b)$ entry, with rows
and columns indexed from $0$, is $\frac{a!}{b!} [t^{a-b}] f$ for $b \le a$ and $0$ for $b > a$,
equals the constant coefficient $[t^0] f$ of $f$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Section 3.

Formalized by `MetaMathlibExt.powerSeriesFactorialMatrix_apply_self`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#power-series-factorial-matrix-apply-self).

## Multiplicativity of the factorial matrix of a power series

Let $K$ be a field of
characteristic zero, let $f$ and $g$ be formal power series over $K$ in the variable $t$, and let
$n$ be a natural number. For a power series $h$ over $K$, write $M_n(h)$ for the $n \times n$
factorial matrix of $h$, whose entry in row $a$ and column $b$ (counted from $0$) is
$\frac{a!}{b!}$ times the coefficient of $t^{a-b}$ in $h$ when $b \le a$, and $0$ otherwise. Then
$M_n(f) M_n(g) = M_n(fg)$.

Since these matrices are lower triangular and $M_n(h)$ is the leading $n \times n$ section of the
infinite matrix $M(h)$, this is equivalent to $M(f) M(g) = M(fg)$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Lemma 5 (`jis-2026-26.5.4-lem-5`).

Stated but not proved: `MetaMathlibExt.powerSeriesFactorialMatrix_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#power-series-factorial-matrix-mul).

## Banded Hessenberg–Toeplitz determinants and linear recurrences

Let $R$ be a commutative
ring, let $k \ge 1$, and let $(c_j)_{j \ge 1}$ and $(\beta_m)_{m \ge 1}$ be sequences in $R$ such
that $\beta_1 = \cdots = \beta_{k-1} = 0$, $\beta_k = 1$ and
$\beta_m = \sum_{j=1}^{k} c_j \beta_{m-j}$ for every $m > k$. For $n \ge 0$ let $H_n$ be the
$n \times n$ upper Hessenberg Toeplitz matrix whose $(i, j)$ entry is $c_{j-i+1}$ if
$0 \le j - i \le k - 1$, is $-1$ if $i = j + 1$, and is $0$ otherwise. Then
$\det H_n = \beta_{n+k}$.

Unlike the paper, this is stated over any commutative ring, without the assumption $c_k \ne 0$,
and also for $n = 0$.

## Sources

- A. R. Moghaddamfar, Navid Salehy and Nima Salehy, *A Generalization of the Pascal and Stirling Matrices*, Journal of Integer Sequences 29 (2026), Article 26.5.4, Theorem 7 (`jis-2026-26.5.4-thm-7`).

Stated but not proved: `MetaMathlibExt.det_hessenbergToeplitz_eq_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PascalStirlingGeneralizationWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#det-hessenberg-toeplitz-eq-recurrence).

## Entries of the Stirling-like matrix $S_\alpha$

For a sequence
$\alpha = (\alpha_0, \alpha_1, \dots)$ of rationals, the numbers $S_{i,j}$ for natural numbers
$i, j$ are defined recursively by $S_{1,j} = \alpha_{j-1}$ for $j \ge 1$, $S_{i,1} = \alpha_0$ for
$i \ge 2$, $S_{i,j} = S_{i-1,j-1} + j \, S_{i-1,j}$ for $i, j \ge 2$, and $S_{i,j} = 0$ when
$i = 0$ or $j = 0$.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.stirlingLikeEntry`, a definition declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#stirling-like-entry).

## Entries of the matrix $U_\alpha$

For a sequence $\alpha = (\alpha_0, \alpha_1, \dots)$
of rational numbers, the entries $U_{i,j}$ ($i, j \ge 1$) of the matrix $U_\alpha$ are defined by
recursion on the row index $i$. The first row is $U_{1,j} = \alpha_{j-1}$. For $i \ge 2$ the
first column is $U_{i,1} = 0$, and for $j \ge 2$

$$U_{i,j} = U_{i-1,j-1} + (j - i + 1)\, U_{i-1,j}.$$

Entries with $i = 0$ or $j = 0$ are set to $0$.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.uEntry`, a definition declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#u-entry).

## The sum $\Psi_\alpha(k)$

For a sequence $\alpha = (\alpha_0, \alpha_1, \dots)$ of
rationals and a natural number $k$, $\Psi_\alpha(k) = \sum_{l=0}^{k-1} \frac{\alpha_l}{(k-1-l)!}$;
in particular $\Psi_\alpha(0) = 0$.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.psi`, a definition declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#psi).

## The sum $\Omega(\alpha, j)$

For a sequence $\alpha = (\alpha_0, \alpha_1, \dots)$ of
rationals and a natural number $j$,
$\Omega(\alpha, j) = \sum_{l=0}^{j-1} (j-1)^{\underline{l}} \, \alpha_l$, where
$m^{\underline{l}} = m(m-1)\cdots(m-l+1)$ is the falling factorial; in particular
$\Omega(\alpha, 0) = 0$.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.omega`, a definition declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#omega).

## The sum $\Lambda(\alpha, k_1, k_2)$

For a sequence $\alpha = (\alpha_0, \alpha_1, \dots)$
of rationals and natural numbers $k_1, k_2$,

$$
\Lambda(\alpha, k_1, k_2) = \sum_{l=0}^{k_1-1} \binom{k_1-1}{l}
\frac{(l+k_2-k_1)!}{(k_2-k_1)!} \, \alpha_{l+k_2-k_1},
$$

where differences of natural numbers are truncated at $0$ (this matters only when $k_2 < k_1$).

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.lambda`, a definition declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#lambda).

## Entries of the matrix $R_\alpha$

For a sequence $\alpha = (\alpha_0, \alpha_1, \dots)$ of
rationals and natural numbers $i, j$, the entry $R_{i,j}$ is
$\frac{(-1)^{j-i}}{(j-i)!} \Psi_\alpha(i)$ if $i \le j$ and $0$ if $i > j$, where
$\Psi_\alpha(k) = \sum_{l=0}^{k-1} \frac{\alpha_l}{(k-1-l)!}$. The matrix $R_\alpha$ uses the
indices $i, j \ge 1$.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.rEntry`, a definition declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#r-entry).

## Entries of the matrix $\tilde R_\alpha$

For a sequence
$\alpha = (\alpha_0, \alpha_1, \dots)$ of rationals and natural numbers $i, j$, the entry
$\tilde R_{i,j}$ is $(j-1)^{\underline{i-1}} / \Omega(\alpha, j)$ if $i \le j$ and $0$ if
$i > j$, where $\Omega(\alpha, j) = \sum_{l=0}^{j-1} (j-1)^{\underline{l}} \, \alpha_l$,
$m^{\underline{l}} = m(m-1)\cdots(m-l+1)$ is the falling factorial, $0 - 1$ is read as $0$, and
division by $0$ gives $0$. The matrix $\tilde R_\alpha$ uses the indices $i, j \ge 1$.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.rTildeEntry`, a definition declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#r-tilde-entry).

## Stirling-like matrix

For a sequence $\alpha \colon \mathbb{N} \to \mathbb{Q}$ and
$n \in \mathbb{N}$, the Stirling-like matrix $S_\alpha(n)$ is the $n \times n$ rational matrix,
with rows and columns indexed by $1, \dots, n$, whose $(i, j)$ entry is $S_{i,j}$, where
$S_{1,j} = \alpha_{j-1}$ for $j \ge 1$, $S_{i,1} = \alpha_0$ for $i \ge 2$, and
$S_{i,j} = S_{i-1,j-1} + j \, S_{i-1,j}$ for $i, j \ge 2$.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.stirlingLikeMatrix`, a definition declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#stirling-like-matrix).

## The matrix $U_\alpha(n)$

For a sequence $\alpha = (\alpha_0, \alpha_1, \dots)$ of
rationals and a natural number $n$, $U_\alpha(n)$ is the $n \times n$ rational matrix whose
$(i, j)$ entry, for $1 \le i, j \le n$, is $U_{i,j}$, where $U_{1,j} = \alpha_{j-1}$ for
$j \ge 1$, $U_{i,1} = 0$ for $i \ge 2$, and $U_{i,j} = U_{i-1,j-1} + (j - i + 1) \, U_{i-1,j}$
for $i, j \ge 2$.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.uMatrix`, a definition declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#u-matrix).

## The matrix $R_\alpha(n)$

For a sequence $\alpha = (\alpha_0, \alpha_1, \dots)$ of
rationals and a natural number $n$, $R_\alpha(n)$ is the $n \times n$ rational matrix whose
$(i, j)$ entry, for $1 \le i, j \le n$, is $\frac{(-1)^{j-i}}{(j-i)!} \Psi_\alpha(i)$ if
$i \le j$ and $0$ if $i > j$, where
$\Psi_\alpha(k) = \sum_{l=0}^{k-1} \frac{\alpha_l}{(k-1-l)!}$.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.rMatrix`, a definition declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#r-matrix).

## The matrix $\tilde R_\alpha(n)$

For a sequence $\alpha = (\alpha_0, \alpha_1, \dots)$ of
rationals and a natural number $n$, $\tilde R_\alpha(n)$ is the $n \times n$ rational matrix
whose $(i, j)$ entry, for $1 \le i, j \le n$, is $(j-1)^{\underline{i-1}} / \Omega(\alpha, j)$
if $i \le j$ and $0$ if $i > j$, where
$\Omega(\alpha, j) = \sum_{l=0}^{j-1} (j-1)^{\underline{l}} \, \alpha_l$,
$m^{\underline{l}} = m(m-1)\cdots(m-l+1)$ is the falling factorial, and division by $0$ gives
$0$.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.rTildeMatrix`, a definition declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#r-tilde-matrix).

## Stirling matrix of the second kind

For $n \in \mathbb{N}$, the Stirling matrix of the
second kind $S(n)$ is the $n \times n$ rational matrix, with rows and columns indexed by
$1, \dots, n$, whose $(i, j)$ entry is the Stirling number of the second kind $S(i, j)$, the
number of partitions of an $i$-element set into $j$ nonempty blocks.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.stirlingMatrix2`, a definition declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#stirling-matrix2).

## The Vandermonde matrix $V(n)$

For $n \in \mathbb{N}$, $V(n)$ is the $n \times n$ rational
matrix whose entry in row $i$ and column $j$ ($1 \le i, j \le n$) is $V_{i,j} = j^{i-1}$.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.vandermondeMatrix`, a definition declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#vandermonde-matrix).

## Explicit formula for the entries of $U_\alpha$

Let
$\alpha \colon \mathbb{N} \to \mathbb{Q}$ and let $U_\alpha = (U_{i,j})_{i \ge 1, j \ge 0}$ be
given by $U_{i,0} = 0$, $U_{1,j} = \alpha_{j-1}$ for $j \ge 1$, $U_{i,1} = 0$ for $i \ge 2$, and
$U_{i,j} = U_{i-1,j-1} + (j-i+1) \, U_{i-1,j}$ for $i, j \ge 2$. For $k_1 \le k_2$ let
$\Lambda(\alpha, k_1, k_2) = \sum_{l=0}^{k_1-1} \binom{k_1-1}{l}
\frac{(l+k_2-k_1)!}{(k_2-k_1)!} \, \alpha_{l+k_2-k_1}$. Then $U_{i,j} = \Lambda(\alpha, i, j)$
for all $1 \le i \le j$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Nima Salehy, and Navid Salehy, "Some Identities Involving Stirling Numbers Arising from Matrix Decompositions", Lemma 1.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.uEntry_eq_lambda`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#u-entry-eq-lambda).

## The matrix $U_\alpha$ is upper triangular

Let $\alpha \colon \mathbb{N} \to \mathbb{Q}$
and let $U_\alpha = (U_{i,j})_{i \ge 1, j \ge 0}$ be given by $U_{i,0} = 0$,
$U_{1,j} = \alpha_{j-1}$ for $j \ge 1$, $U_{i,1} = 0$ for $i \ge 2$, and
$U_{i,j} = U_{i-1,j-1} + (j-i+1) \, U_{i-1,j}$ for $i, j \ge 2$. Then $U_{i,j} = 0$ for all
natural numbers $j < i$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Nima Salehy, and Navid Salehy, "Some Identities Involving Stirling Numbers Arising from Matrix Decompositions", Lemma 1.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.uEntry_eq_zero_of_lt`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#u-entry-eq-zero-of-lt).

## Column sums of the matrix $R_\alpha$

Let $\alpha \colon \mathbb{N} \to \mathbb{Q}$, let
$\Psi_\alpha(k) = \sum_{l=0}^{k-1} \alpha_l / (k-1-l)!$, and let $R_\alpha$ be the matrix with
entries $R_{i,j} = \frac{(-1)^{j-i}}{(j-i)!} \Psi_\alpha(i)$ for $1 \le i \le j$ and
$R_{i,j} = 0$ for $i > j$. Then for every $j \ge 1$, $\sum_{i=1}^{j} R_{i,j} = \alpha_{j-1}$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Nima Salehy, and Navid Salehy, "Some Identities Involving Stirling Numbers Arising from Matrix Decompositions", Lemma 2.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.sum_rEntry_col`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#sum-r-entry-col).

## Two factorizations of the Stirling-like matrix

Let
$\alpha = (\alpha_0, \alpha_1, \dots)$ be a sequence of rationals. For natural numbers
$i, j \ge 1$ define $S_{i,j}$ and $U_{i,j}$ by $S_{1,j} = U_{1,j} = \alpha_{j-1}$,
$S_{i,1} = \alpha_0$ and $U_{i,1} = 0$ for $i \ge 2$, and, for $i, j \ge 2$,
$S_{i,j} = S_{i-1,j-1} + j \, S_{i-1,j}$ and $U_{i,j} = U_{i-1,j-1} + (j-i+1) \, U_{i-1,j}$;
let $R_{i,j} = \frac{(-1)^{j-i}}{(j-i)!} \Psi_\alpha(i)$ if $i \le j$ and $R_{i,j} = 0$ if
$i > j$, where $\Psi_\alpha(k) = \sum_{l=0}^{k-1} \frac{\alpha_l}{(k-1-l)!}$. For every natural
number $n$, let $S_\alpha(n)$, $U_\alpha(n)$ and $R_\alpha(n)$ be the $n \times n$ matrices
$(S_{i,j})$, $(U_{i,j})$ and $(R_{i,j})$ with $1 \le i, j \le n$, let
$S(n) = (S(i,j))_{1 \le i, j \le n}$ be the matrix of Stirling numbers of the second kind, and
let $V(n) = (j^{i-1})_{1 \le i, j \le n}$. Then $S_\alpha(n) = S(n) \, U_\alpha(n)$ and
$S_\alpha(n) = V(n) \, R_\alpha(n)$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Nima Salehy, and Navid Salehy, "Some Identities Involving Stirling Numbers Arising from Matrix Decompositions", Theorem 3.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.stirlingLikeMatrix_decomp`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 517](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L517). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#stirling-like-matrix-decomp).

## Determinant of the Stirling-like matrix

For a sequence
$\alpha \colon \mathbb{N} \to \mathbb{Q}$ and $j \ge 1$ let
$\Omega(\alpha, j) = \sum_{l=0}^{j-1} (j-1)^{\underline{l}} \, \alpha_l$, where
$m^{\underline{l}} = m(m-1)\cdots(m-l+1)$ is the falling factorial. Then for every
$n \in \mathbb{N}$ the determinant of the $n \times n$ Stirling-like matrix $S_\alpha(n)$ is
$\det S_\alpha(n) = \prod_{j=1}^{n} \Omega(\alpha, j)$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Nima Salehy, and Navid Salehy, "Some Identities Involving Stirling Numbers Arising from Matrix Decompositions", Theorem 4.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.stirlingLikeMatrix_det`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 559](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L559). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#stirling-like-matrix-det).

## Second-kind Stirling transform of the $\Lambda$ coefficients

Let
$\alpha \colon \mathbb{N} \to \mathbb{Q}$, let $S(i, k)$ denote the Stirling numbers of the
second kind, let $\Psi_\alpha(k) = \sum_{l=0}^{k-1} \alpha_l / (k-1-l)!$, and for $k_1 \le k_2$
let $\Lambda(\alpha, k_1, k_2) = \sum_{l=0}^{k_1-1} \binom{k_1-1}{l}
\frac{(l+k_2-k_1)!}{(k_2-k_1)!} \, \alpha_{l+k_2-k_1}$. Then for all $i, j \ge 1$,

$$\sum_{k=1}^{\min(i,j)} S(i,k) \, \Lambda(\alpha, k, j) =
\sum_{k=1}^{j} k^{i-1} \, \frac{(-1)^{j-k}}{(j-k)!} \, \Psi_\alpha(k).$$

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Nima Salehy, and Navid Salehy, "Some Identities Involving Stirling Numbers Arising from Matrix Decompositions", Proposition 5.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.sum_stirlingSecond_lambda`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 585](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L585). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#sum-stirling-second-lambda).

## The inverse of the matrix $R_\alpha(n)$

For a sequence
$\alpha = (\alpha_0, \alpha_1, \dots)$ of rationals, let
$\Psi_\alpha(k) = \sum_{l=0}^{k-1} \frac{\alpha_l}{(k-1-l)!}$ and
$\Omega(\alpha, j) = \sum_{l=0}^{j-1} (j-1)^{\underline{l}} \, \alpha_l$, where
$m^{\underline{l}} = m(m-1)\cdots(m-l+1)$ is the falling factorial. For a natural number $n$,
let $R_\alpha(n)$ and $\tilde R_\alpha(n)$ be the upper triangular $n \times n$ rational
matrices whose $(i, j)$ entries for $1 \le i \le j \le n$ are
$\frac{(-1)^{j-i}}{(j-i)!} \Psi_\alpha(i)$ and $(j-1)^{\underline{i-1}} / \Omega(\alpha, j)$
respectively. If $\prod_{j=1}^{n} \Omega(\alpha, j) \ne 0$, then
$\tilde R_\alpha(n) = R_\alpha(n)^{-1}$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Nima Salehy, and Navid Salehy, "Some Identities Involving Stirling Numbers Arising from Matrix Decompositions", Lemma 7.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.rTildeMatrix_eq_inv`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 661](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L661). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#r-tilde-matrix-eq-inv).

## Stirling and falling-factorial sum of the $\Lambda$ coefficients

Let
$\alpha \colon \mathbb{N} \to \mathbb{Q}$, let $S(i, k)$ denote the Stirling numbers of the
second kind, let $m^{\underline{l}} = m(m-1)\cdots(m-l+1)$ be the falling factorial, let
$\Omega(\alpha, j) = \sum_{l=0}^{j-1} (j-1)^{\underline{l}} \, \alpha_l$, and for $k_1 \le k_2$
let $\Lambda(\alpha, k_1, k_2) = \sum_{l=0}^{k_1-1} \binom{k_1-1}{l}
\frac{(l+k_2-k_1)!}{(k_2-k_1)!} \, \alpha_{l+k_2-k_1}$. If $i, j \ge 1$ and
$\prod_{k=1}^{\max(i,j)} \Omega(\alpha, k) \ne 0$, then

$$\sum_{k_1=1}^{i} \sum_{k_2=k_1}^{j} S(i,k_1) \, (j-1)^{\underline{k_2-1}} \,
\Lambda(\alpha, k_1, k_2) = j^{i-1} \, \Omega(\alpha, j).$$

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Nima Salehy, and Navid Salehy, "Some Identities Involving Stirling Numbers Arising from Matrix Decompositions", Proposition 8.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.sum_stirlingSecond_descFactorial_lambda`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 700](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L700). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#sum-stirling-second-desc-factorial-lambd).

## First-kind Stirling formula for $\Lambda(\alpha, i, j)$

Let
$\alpha \colon \mathbb{N} \to \mathbb{Q}$, let $s(i, k)$ denote the signed Stirling numbers of
the first kind, let $\Psi_\alpha(k) = \sum_{l=0}^{k-1} \alpha_l / (k-1-l)!$, and for
$k_1 \le k_2$ let $\Lambda(\alpha, k_1, k_2) = \sum_{l=0}^{k_1-1} \binom{k_1-1}{l}
\frac{(l+k_2-k_1)!}{(k_2-k_1)!} \, \alpha_{l+k_2-k_1}$. Then for all $i, j \ge 1$ the sum

$$\sum_{k_1=1}^{i} \sum_{k_2=1}^{j} s(i,k_1) \, k_2^{k_1-1} \, \frac{(-1)^{j-k_2}}{(j-k_2)!} \,
\Psi_\alpha(k_2)$$

equals $\Lambda(\alpha, i, j)$ if $i \le j$ and $0$ if $i > j$.

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Nima Salehy, and Navid Salehy, "Some Identities Involving Stirling Numbers Arising from Matrix Decompositions", Proposition 9.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.sum_signed_psi_eq`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 769](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L769). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#sum-signed-psi-eq).

## Kronecker-delta identity for signed Stirling numbers of the first kind

Let $s(i, k)$
denote the signed Stirling numbers of the first kind and $\delta_{i,j}$ the Kronecker delta
($1$ if $i = j$ and $0$ otherwise). Then for all integers $i, j \ge 1$, in $\mathbb{Q}$,

$$\sum_{k_1=1}^{i} \sum_{k_2=1}^{j}
\frac{(-1)^{j-k_2} \, s(i,k_1) \, k_2^{k_1-1}}{(j-k_2)! \, (k_2-1)!} = \delta_{i,j}.$$

## Sources

- M. Bahrami-Taghanaki, A. R. Moghaddamfar, Nima Salehy, and Navid Salehy, "Some Identities Involving Stirling Numbers Arising from Matrix Decompositions", Corollary 10.

Formalized by `MathlibExt.Combinatorics.Enumerative.StirlingMatrixWanted.sum_signed_eq_delta`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean, line 828](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/StirlingMatrix.lean#L828). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html#sum-signed-eq-delta).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: α-Stirling matrices](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/stirling-matrices)
