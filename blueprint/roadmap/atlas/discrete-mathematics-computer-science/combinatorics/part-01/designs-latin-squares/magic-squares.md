---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.Ramanujan.Part1Ch1.Entry1Magicsquare3.ramanujan_part1_ch1_entry1_magicsquare3, MetaMathlibExt.IsMagicSquare, MetaMathlibExt.IsReducedMagicSquare, MetaMathlibExt.isReducedMagicSquare_loShu, MetaMathlibExt.not_isReducedMagicSquare_zero_one_two_three, MetaMathlibExt.isReducedMagicSquare_extendedStrachey, MetaMathlibExt.isReducedMagicSquare_refSymmetric_strachey
statement: formalized
---

# Magic squares

7 results, 5 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/magic-squares/index.html).

## Equal line sums from two orthogonal diagonal Latin squares

Let $n \ge 1$, let
$a, b : \{0, \dots, n-1\} \to \mathbb{N}$, and let $L$ and $R$ be $n \times n$ arrays with entries
$L_{ij}, R_{ij} \in \{0, \dots, n-1\}$ (rows $i$ and columns $j$ indexed by $\{0, \dots, n-1\}$)
such that, in each of $L$ and $R$, every row, every column, the main diagonal (entries $(i, i)$)
and the antidiagonal (entries $(i, n-1-i)$) contains each value exactly once. Suppose also that
$(i, j) \mapsto (L_{ij}, R_{ij})$ is a bijection of $\{0, \dots, n-1\}^2$ onto itself. Then there
is a natural number $S$ such that, in the $n \times n$ array with entries $a(L_{ij}) + b(R_{ij})$,
every row sum, every column sum, the main diagonal sum and the antidiagonal sum equal $S$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 1, Entry 1.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch1.Entry1Magicsquare3.ramanujan_part1_ch1_entry1_magicsquare3`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch1Entry1.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch1Entry1.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/magic-squares/index.html#ramanujan-part1-ch1-entry1-magicsquare3).

## Magic squares

An $n \times n$ array $M$ of natural numbers, with rows and columns
indexed by $0, 1, \dots, n - 1$, is a *magic square* when there is a natural number $s$ such
that every row of $M$ and every column of $M$ sums to $s$, and also $\sum_i M_{i,i} = s$ (the
main diagonal) and $\sum_i M_{i,n-1-i} = s$ (the anti-diagonal).

No condition is imposed on the entries themselves.

## Sources

- Gek L. Chia and Wai Keong Kok, *Self-Complementary Magic Squares of Singly Even Orders*, Journal of Integer Sequences 27 (2024), Article 24.1.4, Section 1.

Formalized by `MetaMathlibExt.IsMagicSquare`, a definition declared in [WantedExt/Combinatorics/SinglyEvenMagicSquaresWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SinglyEvenMagicSquaresWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/magic-squares/index.html#is-magic-square).

## Reduced magic squares

An $n \times n$ array $M$ of natural numbers is a *reduced magic
square of order $n$* when it is a magic square and its entries are $0, 1, \dots, n^2 - 1$, each
exactly once; equivalently, every entry of $M$ is less than $n^2$ and distinct cells of $M$
hold distinct entries.

These are the magic squares of order $n$ with entries $1, 2, \dots, n^2$, each exactly once,
with every entry reduced by $1$.

## Sources

- Gek L. Chia and Wai Keong Kok, *Self-Complementary Magic Squares of Singly Even Orders*, Journal of Integer Sequences 27 (2024), Article 24.1.4, Section 3.

Formalized by `MetaMathlibExt.IsReducedMagicSquare`, a definition declared in [WantedExt/Combinatorics/SinglyEvenMagicSquaresWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SinglyEvenMagicSquaresWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/magic-squares/index.html#is-reduced-magic-square).

## The reduced Lo Shu square

The $3 \times 3$ square with rows $(7, 0, 5)$, $(2, 4, 6)$ and
$(3, 8, 1)$, a form of the Lo Shu square with every entry reduced by $1$, is a reduced magic
square of order $3$; its magic sum is $12$.

## Sources

- Gek L. Chia and Wai Keong Kok, *Self-Complementary Magic Squares of Singly Even Orders*, Journal of Integer Sequences 27 (2024), Article 24.1.4, Section 3 (reduced magic squares).

Formalized by `MetaMathlibExt.isReducedMagicSquare_loShu`, a theorem declared in [WantedExt/Combinatorics/SinglyEvenMagicSquaresWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SinglyEvenMagicSquaresWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/magic-squares/index.html#is-reduced-magic-square-lo-shu).

## A 2×2 square that is not a reduced magic square

The $2 \times 2$ square with rows
$(0, 1)$ and $(2, 3)$ is not a reduced magic square.

Its entries are $0, 1, 2, 3$, each once, but its row sums are $1$ and $5$, so it is not magic.

## Sources

- Gek L. Chia and Wai Keong Kok, *Self-Complementary Magic Squares of Singly Even Orders*, Journal of Integer Sequences 27 (2024), Article 24.1.4, Section 3 (reduced magic squares).

Formalized by `MetaMathlibExt.not_isReducedMagicSquare_zero_one_two_three`, a theorem declared in [WantedExt/Combinatorics/SinglyEvenMagicSquaresWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SinglyEvenMagicSquaresWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/magic-squares/index.html#not-is-reduced-magic-square-zero-one-two).

## Extended Strachey construction

Let $m$ be a natural number, let $q = (2m+1)^2$, and let
$A_0$, $A_1$, $B_1$, $B_2$ be $(2m+1) \times (2m+1)$ arrays of natural numbers. Suppose that every
entry of $A_0$ is $0$ or $3$, every row of $A_0$ has exactly $m+1$ zeros, and the main diagonal
and the anti-diagonal of $A_0$ each have exactly $m+1$ threes; that every entry of $A_1$ is $1$
or $2$, every row of $A_1$ has exactly $m+2$ ones, and the main diagonal and the anti-diagonal
of $A_1$ each have exactly $m+2$ ones; and that $B_1$ and $B_2$ are reduced magic squares. Then
the square of order $2(2m+1)$ made of four $(2m+1) \times (2m+1)$ blocks, whose $(i, j)$ entries
are $q A_0(i,j) + B_1(i,j)$ in the top left block, $q (3 - A_1(i,j)) + B_2(i,j)$ in the top
right block, $q (3 - A_0(i,j)) + B_1(i,j)$ in the bottom left block and
$q A_1(i,j) + B_2(i,j)$ in the bottom right block, is a reduced magic square.

At $m = 0$ no array $A_1$ satisfies the row condition (a row of length $1$ cannot hold two
ones), so the statement is vacuous there.

## Sources

- Gek L. Chia and Wai Keong Kok, *Self-Complementary Magic Squares of Singly Even Orders*, Journal of Integer Sequences 27 (2024), Article 24.1.4, Theorem 1, with Definitions 1-3 (`jis-2024-24.1.4-thm-1`).

Stated but not proved: `MetaMathlibExt.isReducedMagicSquare_extendedStrachey` is written with `theorem_wanted` in [WantedExt/Combinatorics/SinglyEvenMagicSquaresWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SinglyEvenMagicSquaresWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/magic-squares/index.html#is-reduced-magic-square-extended-strache).

## Ref-symmetric squares from the Strachey construction

Let $m$ be a natural number, let
$q = (2m+1)^2$, and let $A_0$, $A_1$ and $M$ be $(2m+1) \times (2m+1)$ arrays of natural
numbers, with rows and columns indexed by $0, 1, \dots, 2m$; write $\bar\imath = 2m - i$ and
$\bar\jmath = 2m - j$. Suppose that every entry of $A_0$ is $0$ or $3$, every row of $A_0$ has
exactly $m+1$ zeros, and the main diagonal and the anti-diagonal of $A_0$ each have exactly
$m+1$ threes; that every entry of $A_1$ is $1$ or $2$, every row of $A_1$ has exactly $m+2$
ones, and the main diagonal and the anti-diagonal of $A_1$ each have exactly $m+2$ ones; that
$A_k(\bar\imath, j) = A_k(i, j)$ and $A_k(m, \bar\jmath) = A_k(m, j)$ for $k = 0, 1$ and all
$i$, $j$; that $M$ is a reduced magic square; and that
$M(i, j) + M(\bar\imath, \bar\jmath) = q - 1$ for all $i$, $j$. Let $B_1(i, j) = M(i, \bar\jmath)$
if $i > m$ and $B_1(i, j) = M(i, j)$ otherwise, and let $B_1^*(i, j) = M(i, \bar\jmath)$ if
$i \ge m$ and $B_1^*(i, j) = M(i, j)$ otherwise. Let $n = 2(2m+1)$ and let $S$ be the square of
order $n$, with rows and columns indexed by $0, 1, \dots, n-1$, made of four
$(2m+1) \times (2m+1)$ blocks whose $(i, j)$ entries are $q A_0(i, j) + B_1(i, j)$ in the top
left block, $q (3 - A_1(i, j)) + B_1(i, \bar\jmath)$ in the top right block,
$q (3 - A_0(i, j)) + B_1^*(i, j)$ in the bottom left block and
$q A_1(i, j) + B_1^*(i, \bar\jmath)$ in the bottom right block. Then $S$ is a reduced magic
square, and $S(i, j) + S(n - 1 - i, j) = n^2 - 1$ for all $i$, $j$.

The last identity is the reduced form of the paper's condition $a_{i,j} + a_{n+1-i,j} = n^2 + 1$.
As in the extended Strachey construction, the statement is vacuous at $m = 0$, where no array
$A_1$ satisfies the row condition.

## Sources

- Gek L. Chia and Wai Keong Kok, *Self-Complementary Magic Squares of Singly Even Orders*, Journal of Integer Sequences 27 (2024), Article 24.1.4, Theorem 2, with Definitions 4-6 (`jis-2024-24.1.4-thm-2`).

Stated but not proved: `MetaMathlibExt.isReducedMagicSquare_refSymmetric_strachey` is written with `theorem_wanted` in [WantedExt/Combinatorics/SinglyEvenMagicSquaresWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SinglyEvenMagicSquaresWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/magic-squares/index.html#is-reduced-magic-square-ref-symmetric-st).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Magic squares](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/magic-squares/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/designs-latin-squares/magic-squares)
