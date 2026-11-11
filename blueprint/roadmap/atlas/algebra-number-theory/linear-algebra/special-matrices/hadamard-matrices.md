---
declaration: section
origin: cited
lean: MetaMathlibExt.isHadamardMatrix, MetaMathlibExt.exists_hadamard_matrix_with_circulant_core, MetaMathlibExt.isHadamardMatrix_iff_isHadamard, MetaMathlibExt.hasCirculantCore_iff_circulant, MetaMathlibExt.exists_isHadamard_with_circulant_core
statement: formalized
proof: formalized
---

# Hadamard matrices

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/hadamard-matrices/index.html).

## Hadamard matrix

For a natural number $m$, an $m \times m$ matrix $H$ with integer
entries is a Hadamard matrix when every entry of $H$ is $1$ or $-1$ and
$H^{\mathsf T} H = m I$, where $I$ is the $m \times m$ identity matrix.

This predicate is used for Hadamard matrices of order $n + 1$ with circulant core, which exist
when $n$ is a prime congruent to $3$ mod $4$ (Paley) or $n = p(p + 2)$ with $p$ and $p + 2$
both prime (Stanton–Sprott/Whiteman).

## Sources

- Richard P. Brent and Adam B. Yedidia, "Computation of Maximal Determinants of Binary Circulant Matrices," Journal of Integer Sequences 21 (2018), Article 18.5.6, Theorem, lines 684–695, https://cs.uwaterloo.ca/journals/JIS/VOL21/Brent/brent11.tex quoting Kotsireas et al.; attributions at lines 698–704. The prime-power versions of cases (1)–(2), if the source allows them, and cases (3)–(4) of the source theorem (Singer, Hall) are not part of this statement.

Formalized by `MetaMathlibExt.isHadamardMatrix`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/HadamardCirculantCore.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/HadamardCirculantCore.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/hadamard-matrices/index.html#is-hadamard-matrix).

## Hadamard matrices with circulant core: Paley and twin-prime cases

Let $n$ be a natural
number such that either $n$ is a prime with $n \equiv 3 \pmod 4$, or $n = p(p + 2)$ for some
natural number $p$ with $p$ and $p + 2$ both prime. Then there is an $(n + 1) \times (n + 1)$
Hadamard matrix $H$ with integer entries, rows and columns indexed by $0, 1, \dots, n$ (so every
entry of $H$ is $1$ or $-1$ and $H^{\mathsf T} H = (n + 1) I$), that has a circulant core: there
is a function $v \colon \{0, \dots, n - 1\} \to \mathbb{Z}$ with $H_{i+1, j+1} = v(i - j)$ for
all $i, j \in \{0, \dots, n - 1\}$, where $i - j$ is taken modulo $n$.

Formalized by `MetaMathlibExt.exists_hadamard_matrix_with_circulant_core`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/HadamardCirculantCore.lean, line 1109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/HadamardCirculantCore.lean#L1109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/hadamard-matrices/index.html#exists-hadamard-matrix-with-circulant-co).

## One-sided orthogonality characterizes Hadamard matrices

Let $m$ be a natural number and
let $H$ be an $m \times m$ integer matrix. Then every entry of $H$ is $1$ or $-1$ and
$H^{\mathsf T} H = m I$ if and only if every entry of $H$ is a unitary element of $\mathbb{Z}$
(that is, $1$ or $-1$), $H H^{\mathsf T} = m I$ and $H^{\mathsf T} H = m I$. The right-hand side
is the general notion of a Hadamard matrix, with entries unitary and $H H^{*} = H^{*} H = m I$;
over $\mathbb{Z}$ the conjugate transpose $H^{*}$ is the transpose.

Formalized by `MetaMathlibExt.isHadamardMatrix_iff_isHadamard`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/HadamardCirculantCore.lean, line 1187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/HadamardCirculantCore.lean#L1187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/hadamard-matrices/index.html#is-hadamard-matrix-iff-is-hadamard).

## A circulant core is a circulant submatrix

Let $n$ be a natural number and let $H$ be an
$(n + 1) \times (n + 1)$ integer matrix with rows and columns indexed by $0, 1, \dots, n$. Then
$H$ has a circulant core, meaning that there is a function
$v \colon \{0, \dots, n - 1\} \to \mathbb{Z}$ with $H_{i+1, j+1} = v(i - j)$ for all
$i, j \in \{0, \dots, n - 1\}$, if and only if there is a function
$v \colon \{0, \dots, n - 1\} \to \mathbb{Z}$ such that the submatrix
$(H_{i+1, j+1})_{0 \le i, j \le n - 1}$ equals the circulant matrix of $v$, whose $(i, j)$
entry is $v(i - j)$. In both conditions $i - j$ is taken modulo $n$.

Formalized by `MetaMathlibExt.hasCirculantCore_iff_circulant`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/HadamardCirculantCore.lean, line 1222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/HadamardCirculantCore.lean#L1222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/hadamard-matrices/index.html#has-circulant-core-iff-circulant).

## Circulant-core Hadamard matrices with orthogonal rows and columns

Let $n$ be a natural
number such that either $n$ is a prime with $n \equiv 3 \pmod 4$, or $n = p(p + 2)$ for some
natural number $p$ with $p$ and $p + 2$ both prime. Then there is an $(n + 1) \times (n + 1)$
integer matrix $H$, with rows and columns indexed by $0, 1, \dots, n$, such that every entry of
$H$ is $1$ or $-1$, $H H^{\mathsf T} = (n + 1) I$ and $H^{\mathsf T} H = (n + 1) I$, and there
is a function $v \colon \{0, \dots, n - 1\} \to \mathbb{Z}$ such that the submatrix
$(H_{i+1, j+1})_{0 \le i, j \le n - 1}$ obtained by deleting row $0$ and column $0$ equals the
circulant matrix of $v$, whose $(i, j)$ entry is $v(i - j)$ with $i - j$ taken modulo $n$.

Formalized by `MetaMathlibExt.exists_isHadamard_with_circulant_core`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/HadamardCirculantCore.lean, line 1237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/HadamardCirculantCore.lean#L1237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/hadamard-matrices/index.html#exists-is-hadamard-with-circulant-core).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hadamard matrices](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/hadamard-matrices/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/special-matrices/hadamard-matrices)
