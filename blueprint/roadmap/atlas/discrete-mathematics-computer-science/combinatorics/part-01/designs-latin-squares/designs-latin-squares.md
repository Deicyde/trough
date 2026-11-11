---
declaration: section
origin: cited
lean: MetaMathlibExt.binaryMatrixRotationOrbitCount, MetaMathlibExt.mann_product_criterion_for_orthogonal_latin_squares
statement: formalized
proof: formalized
---

# Designs, Latin squares and combinatorial matrices: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/index.html).

Block designs, Steiner systems, pairwise balanced designs and linear spaces, Latin squares and transversals, Hadamard and partial Hadamard matrices, magic squares, 0-1 matrices with prescribed margins (Gale–Ryser), binary matrices up to rotation, and sign tables from determinant-moment expansions; cyclic difference sets go to Sidon sets and difference sets.

## Counting binary matrices up to cyclic rotations

Let $m, n \ge 1$. For an $m \times n$
matrix $x$ with entries $x_{r,s} \in \{0, 1\}$, rows indexed by $0 \le r < m$ and columns by
$0 \le s < n$, put $N(x) = \sum_{r=0}^{m-1} \sum_{s=0}^{n-1} x_{r,s} \, 2^{rn+s}$, and for
$0 \le i < m$, $0 \le j < n$ let $x^{(i,j)}$ be the rotated matrix with entries
$x^{(i,j)}_{r,s} = x_{(r+i) \bmod m, \, (s+j) \bmod n}$. The number of such matrices $x$ with
$N(x) \le N(x^{(i,j)})$ for all $i$ and $j$ equals

$$\left\lfloor \frac{1}{mn} \sum_{c \mid m} \sum_{d \mid n} \varphi(c) \, \varphi(d) \,
2^{mn / \operatorname{lcm}(c,d)} \right\rfloor,$$

where $\varphi$ is Euler's totient function.

Since $N$ is injective, each orbit under the cyclic row and column rotations contains exactly one
such matrix, so this is the number of binary $m \times n$ matrices up to rotation; by Burnside's
lemma the division is exact (the Pólya enumeration formula).

## Sources

- S. N. Ethier, "Counting Toroidal Binary Arrays," Journal of Integer Sequences 16 (2013), Article 13.4.7, Theorem, lines 172–176, <https://cs.uwaterloo.ca/journals/JIS/VOL16/Ethier/ethier2.tex>.

Formalized by `MetaMathlibExt.binaryMatrixRotationOrbitCount`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BinaryMatrixRotationOrbitCount.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/BinaryMatrixRotationOrbitCount.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/index.html#binary-matrix-rotation-orbit-count).

## Mann's product criterion for orthogonal Latin squares

Let $n$ be a natural number,
write $[n] = \{0, \dots, n-1\}$, and let $A$ and $B$ be Latin squares of order $n$ with rows,
columns and entries indexed by $[n]$: every row and every column of each square is a bijection
of $[n]$. For a row index $i$ write $A_i$ and $B_i$ for the permutations $j \mapsto A_{ij}$ and
$j \mapsto B_{ij}$ of $[n]$. Then the map $(i, j) \mapsto (A_{ij}, B_{ij})$ is a bijection of
$[n] \times [n]$ (that is, $A$ and $B$ are orthogonal) if and only if the square $C$ with
entries $C_{ij} = A_i(B_i^{-1}(j))$ is a Latin square, meaning that every row $j \mapsto C_{ij}$
and every column $i \mapsto C_{ij}$ of $C$ is a bijection of $[n]$.

The equivalence uses only the row conditions on $A$ and $B$; the column conditions are kept so
that both inputs are Latin squares. The row condition on $C$ follows from the row conditions on
$A$ and $B$, and is included so that the right side is the full Latin-square condition.

Formalized by `MetaMathlibExt.mann_product_criterion_for_orthogonal_latin_squares`, a theorem declared in [MathlibExt/Combinatorics/LatinSquare/Mann.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/LatinSquare/Mann.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/index.html#mann-product-criterion-for-orthogonal-la).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Designs, Latin squares and combinatorial matrices](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/designs-latin-squares)
