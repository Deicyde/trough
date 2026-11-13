---
declaration: section
origin: cited
lean: MetaMathlibExt.nonattackingPlacements, MetaMathlibExt.card_nonattackingPlacements_zero, MetaMathlibExt.squareBoard, MetaMathlibExt.whiteSquares, MetaMathlibExt.blackSquares, MetaMathlibExt.bishopMoves, MetaMathlibExt.anassaMoves, MetaMathlibExt.bishopsSquare
statement: formalized
---

# Nonattacking bishops and anassas

33 results, 18 proved and 15 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html).

## Nonattacking placements

Let $B$ be a board, that is, a finite set of squares
$(i, j) \in \mathbb{Z}^2$, let $M$ be a list of basic moves $v \in \mathbb{Z}^2$, and let $k$ be a
natural number. The nonattacking placements of $k$ pieces with basic moves $M$ on $B$ are the
$k$-element subsets $S \subseteq B$ such that for all distinct squares $p, q \in S$ and every
move $v \in M$, the difference $q - p$ is not parallel to $v$, that is,
$(q_1 - p_1) v_2 \ne (q_2 - p_2) v_1$.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Section 1.

Formalized by `MetaMathlibExt.nonattackingPlacements`, a definition declared in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#nonattacking-placements).

## Exactly one nonattacking placement of no pieces

For every board $B$, a finite set of
squares of $\mathbb{Z}^2$, and every list $M$ of basic moves in $\mathbb{Z}^2$, there is
exactly one nonattacking placement of $0$ pieces with basic moves $M$ on $B$.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Section 1.

Formalized by `MetaMathlibExt.card_nonattackingPlacements_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#card-nonattacking-placements-zero).

## The square board

For a natural number $m$, the square board $S_m$ is the set of squares
$(i, j) \in \mathbb{Z}^2$ with $1 \le i \le m$ and $1 \le j \le m$.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Section 2.

Formalized by `MetaMathlibExt.squareBoard`, a definition declared in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#square-board).

## White squares of the square board

For a natural number $m$, the white squares of the
square board $S_m = [1, m]^2$ are the integer squares $(i, j) \in S_m$ for which $i + j$ is
even.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Section 2, Table 1.

Formalized by `MetaMathlibExt.whiteSquares`, a definition declared in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#white-squares).

## Black squares of the square board

For a natural number $m$, the black squares of the
$m \times m$ board $S_m = [1, m]^2$ are the squares $(i, j) \in S_m$ with $i + j$ odd.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Section 2, Table 1.

Formalized by `MetaMathlibExt.blackSquares`, a definition declared in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#black-squares).

## Basic moves of the bishop

The basic moves of the bishop are the two vectors $(1, 1)$
and $(-1, 1)$ in $\mathbb{Z}^2$.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Section 2.

Formalized by `MetaMathlibExt.bishopMoves`, a definition declared in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#bishop-moves).

## Basic moves of the anassa

The basic moves of the anassa are the two vectors $(0, 1)$
and $(1, 1)$ in $\mathbb{Z}^2$.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Section 3.

Formalized by `MetaMathlibExt.anassaMoves`, a definition declared in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#anassa-moves).

## Nonattacking bishops on a square board

For natural numbers $m$ and $k$, $B_S(m, k)$ is the
number of ways to place $k$ nonattacking bishops on the $m \times m$ board $S_m = [1, m]^2$, that
is, the number of $k$-element subsets of $S_m$ no two of whose squares lie on a common line of
slope $1$ or $-1$.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Theorem 2.1.

Formalized by `MetaMathlibExt.bishopsSquare`, a definition declared in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#bishops-square).

## Nonattacking bishops on the white squares

For natural numbers $m$ and $k$, $R_W(m, k)$ is
the number of $k$-element sets of white squares of the $m \times m$ board $S_m = [1, m]^2$ (the
squares $(i, j)$ with $i + j$ even) no two of which lie on a common line of slope $1$ or $-1$, that
is, the number of ways to place $k$ nonattacking bishops on the white squares of $S_m$.

In the source, $R_W(m, k)$ counts placements of $k$ nonattacking rooks on the white board $W_m$,
whose rows and columns are the diagonals of the white squares of $S_m$.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Theorem 2.2.

Formalized by `MetaMathlibExt.bishopsWhite`, a definition declared in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#bishops-white).

## Nonattacking bishops on the black squares

For natural numbers $m$ and $k$, $R_K(m, k)$ is
the number of $k$-element sets of black squares of the $m \times m$ board $S_m = [1, m]^2$ (the
squares $(i, j)$ with $i + j$ odd) no two of which lie on a common line of slope $1$ or $-1$, that
is, the number of ways to place $k$ nonattacking bishops on the black squares of $S_m$.

In the source, $R_K(m, k)$ counts placements of $k$ nonattacking rooks on the black board $K_m$,
whose rows and columns are the diagonals of the black squares of $S_m$.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Theorem 2.2.

Formalized by `MetaMathlibExt.bishopsBlack`, a definition declared in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#bishops-black).

## Nonattacking anassas by number below the diagonal

For natural numbers $m$, $k$ and
$p$, $A_S(m, k, p)$ is the number of nonattacking placements of $k$ anassas on the square board
$S_m = \{1, \dots, m\}^2$ (that is, of $k$-element sets of squares of $S_m$ no two of which lie
on a common line in the direction $(0, 1)$ or $(1, 1)$) in which exactly $p$ of the squares
$(i, j)$ satisfy $j < i$, that is, lie strictly below the main diagonal.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Theorem 3.1.

Formalized by `MetaMathlibExt.anassasBelow`, a definition declared in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#anassas-below).

## Extended Stirling numbers of the second kind

Knuth's extended Stirling number of the
second kind at integers $n$ and $k$ is the natural number equal to the Stirling number of the
second kind $S(n, k)$ if $n \ge 0$ and $k \ge 0$, equal to the unsigned Stirling number of the
first kind $c(-k, -n)$ if $n < 0$ and $k < 0$, and equal to $0$ otherwise. Here $c(j, i)$ is the
number of permutations of $j$ elements with exactly $i$ cycles.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Section 1 (extended Stirling numbers, with the identity `{-j, -k} = [k, j]`).

Formalized by `MetaMathlibExt.extStirlingSecond`, a definition declared in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#ext-stirling-second).

## Extended Stirling numbers at natural arguments

For all natural numbers $n$ and $k$, the
extended Stirling number of the second kind at $(n, k)$ equals the Stirling number of the second
kind $S(n, k)$.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Section 1.

Formalized by `MetaMathlibExt.extStirlingSecond_natCast`, a theorem declared in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#ext-stirling-second-nat-cast).

## Extended Stirling numbers at negative arguments

For all positive integers $a$ and $b$,
the extended Stirling number of the second kind at $(-a, -b)$ equals the unsigned Stirling number
of the first kind $c(b, a)$, the number of permutations of $b$ elements with exactly $a$ cycles.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, proof of Theorem 2.2.

Formalized by `MetaMathlibExt.extStirlingSecond_neg_neg`, a theorem declared in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#ext-stirling-second-neg-neg).

## Santos's coefficients

For natural numbers $i$, $p$, $q$ and a complex number $z$,
Santos's coefficient $\beta_i(p, q, z)$ is the complex number

$$
\beta_i(p, q, z) = 2^{-2q} \sum_{b=\max(0, i-p)}^{q} 2^b \binom{2q-b}{q}
\sum_{a=0}^{b} \binom{p+b-q-z}{a} \binom{q+z}{b-a} \binom{a-q}{p+b-i},
$$

where $\binom{w}{n} = w(w-1)\cdots(w-n+1)/n!$ for complex $w$ and natural $n$.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Lemma 2.7, equation (9).

Formalized by `MetaMathlibExt.santosBeta`, a definition declared in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#santos-beta).

## Santos's coefficient with all indices zero

For every complex number $z$, Santos's
coefficient satisfies $\beta_0(0, 0, z) = 1$.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Lemma 2.7.

Formalized by `MetaMathlibExt.santosBeta_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#santos-beta-zero).

## Constituent coefficients for bishops on one color

For natural numbers $k$, $d$ and a
complex number $z$, the constituent coefficient $c_{k,d}(z)$ is

$$c_{k,d}(z) = \sum_{i=d}^{2k} \frac{(-1)^{i-d}}{i!} {i \brack d}
\sum_{p=\max(0, i-k)}^{k} \sum_{j=p}^{k} S_2(p+j, p) \, \beta_i(p+j, k-j, z),$$

where ${i \brack d}$ is the unsigned Stirling number of the first kind, $S_2(n, r)$ is the
2-associated Stirling number of the second kind, and $\beta_i(p, q, z)$ is the coefficient
$\beta$ of Santos's Lemma 2.7.

Taking $z = -\pi(m)$ and $z = \pi(m)$, where $\pi(m) \in \{0, 1\}$ is the parity of $m$, gives
the coefficients of $m^d$ in the quasi-polynomials (13) and (14) for $k$ bishops on the white
and black squares.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Theorem 2.8.

Formalized by `MetaMathlibExt.bishopColorQuasiCoeff`, a definition declared in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#bishop-color-quasi-coeff).

## Constituent coefficient for no bishops

For every complex number $z$, the constituent
coefficient $c_{0,0}(z)$ of the bishop quasi-polynomials (the case $k = d = 0$) equals $1$.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Theorem 2.8.

Formalized by `MetaMathlibExt.bishopColorQuasiCoeff_zero_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#bishop-color-quasi-coeff-zero-zero).

## Arshon's formula for nonattacking bishops (Kotěšovec's form)

For all natural numbers $m$
and $k$, the number $B_S(m, k)$ of placements of $k$ nonattacking bishops on the $m \times m$
board satisfies

$$
B_S(m, k) = \sum_{j=0}^{m} \sum_{i=0}^{\lfloor (m+1)/2 \rfloor}
\binom{\lfloor (m+1)/2 \rfloor}{i} S\bigl(i + \lfloor m/2 \rfloor, m - j\bigr)
\sum_{l=0}^{\lfloor m/2 \rfloor} \binom{\lfloor m/2 \rfloor}{l}
S\bigl(l + \lfloor (m+1)/2 \rfloor, m - k + j\bigr),
$$

where, for integers $a \ge 0$ and $b$, $S(a, b)$ is the Stirling number of the second kind when
$b \ge 0$ and $0$ when $b < 0$ (Knuth's extended Stirling numbers of the second kind).

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Theorem 3 (Arshon, Kotěšovec) (`jis-2025-25.8.6-thm-3`).

Stated but not proved: `MetaMathlibExt.bishopsSquare_eq_arshon` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#bishops-square-eq-arshon).

## Recurrence for bishops on white squares

Write $R_W(m, k)$ for the number of placements of
$k$ nonattacking bishops on the white squares (those $(i, j)$ with $i + j$ even) of the
$m \times m$ board $[1, m]^2$, and $\pi(n) \in \lbrace 0, 1 \rbrace$ for the remainder of $n$
modulo $2$. For all natural numbers $m$ and $k$,

$$
R_W(m + 1, k + 1) = R_W(m, k + 1) + \bigl(m - k + \pi(m + 1)\bigr) R_W(m, k),
$$

$R_W(m, 0) = 1$ and $R_W(0, k + 1) = 0$.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Theorem 4 (`jis-2025-25.8.6-thm-4`).

Stated but not proved: `MetaMathlibExt.bishopsWhite_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#bishops-white-recurrence).

## Recurrence for bishops on the black squares

Let $R_K(m, k)$ be the number of
nonattacking placements of $k$ bishops on the black squares $(i, j)$, with $i + j$ odd, of the
board $\{1, \dots, m\}^2$, and let $\pi(m) \in \{0, 1\}$ be the remainder of $m$ modulo $2$.
For $m, k \ge 1$,

$$R_K(m, k) = R_K(m-1, k) + (m - k + 1 - \pi(m)) \, R_K(m-1, k-1)$$

in the integers, and for every natural number $m$, $R_K(m, 0) = 1$ and $R_K(0, k) = 0$ for
$k \ge 1$.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Theorem 4 (`jis-2025-25.8.6-thm-4`).

Stated but not proved: `MetaMathlibExt.bishopsBlack_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#bishops-black-recurrence).

## Extended Stirling formula for bishops on white squares

For all natural numbers $m$ and
$k$, the number $R_W(m, k)$ of placements of $k$ nonattacking bishops on the white squares (those
$(i, j)$ with $i + j$ even) of the $m \times m$ board $[1, m]^2$ satisfies

$$
R_W(m, k) = \sum_{j=0}^{k} \binom{\lceil m/2 \rceil}{j} S(m - j, m - k),
$$

where $S(a, b)$ is Knuth's extended Stirling number of the second kind for integers $a, b$: the
Stirling number of the second kind when $a, b \ge 0$, the unsigned Stirling number of the first
kind with arguments $-b, -a$ when $a, b < 0$, and $0$ otherwise.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Theorem 4 (`jis-2025-25.8.6-thm-4`).

Stated but not proved: `MetaMathlibExt.bishopsWhite_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#bishops-white-eq-sum).

## Sum formula for bishops on the black squares

Let $R_K(m, k)$ be the number of
nonattacking placements of $k$ bishops on the black squares $(i, j)$, with $i + j$ odd, of the
board $\{1, \dots, m\}^2$, and let ${n \brace j}$ be Knuth's extended Stirling numbers of the
second kind. For all natural numbers $m$ and $k$,

$$R_K(m, k) = \sum_{j=0}^{k} \binom{\lfloor m/2 \rfloor}{j} {m-j \brace m-k}.$$

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Theorem 4 (`jis-2025-25.8.6-thm-4`).

Stated but not proved: `MetaMathlibExt.bishopsBlack_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#bishops-black-eq-sum).

## Extended Stirling formula for bishops on a square board

For all natural numbers $m$ and
$k$, the number $B_S(m, k)$ of placements of $k$ nonattacking bishops on the $m \times m$ board
satisfies

$$
B_S(m, k) = \sum_{j=0}^{k} \sum_{i=0}^{j} \binom{\lfloor m/2 \rfloor}{i} S(m - i, m - j)
\sum_{l=0}^{k-j} \binom{\lceil m/2 \rceil}{l} S(m - l, m - k + j),
$$

where $S(a, b)$ is Knuth's extended Stirling number of the second kind for integers $a, b$: the
Stirling number of the second kind when $a, b \ge 0$, the unsigned Stirling number of the first
kind with arguments $-b, -a$ when $a, b < 0$, and $0$ otherwise.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Theorem 6 (`jis-2025-25.8.6-thm-6`).

Stated but not proved: `MetaMathlibExt.bishopsSquare_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#bishops-square-eq-sum).

## Ward's identity for Stirling numbers of the second kind

For natural numbers $k \le m$,

$$S(m, m - k) = \sum_{p=0}^{k} S_2(k + p, p) \binom{m}{k + p},$$

where $S$ denotes the Stirling numbers of the second kind and $S_2$ the 2-associated Stirling
numbers of the second kind.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Lemma 8 (`jis-2025-25.8.6-lem-8`).

Stated but not proved: `MetaMathlibExt.stirlingSecond_sub_eq_sum_associated` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#stirling-second-sub-eq-sum-associated).

## Santos's expansion of a product of binomial coefficients

For natural numbers $p$, $q$
and complex numbers $x$, $z$,

$$\binom{2x + z - q}{p} \binom{x}{q} = \sum_{i=0}^{p+q} \beta_i(p, q, z) \binom{2x + z}{i},$$

where $\beta_i(p, q, z)$ are Santos's coefficients and, for complex $w$ and natural $n$,
$\binom{w}{n} = w(w-1)\cdots(w-n+1)/n!$.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Lemma 9 (`jis-2025-25.8.6-lem-9`).

Stated but not proved: `MetaMathlibExt.choose_mul_choose_eq_sum_santosBeta` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#choose-mul-choose-eq-sum-santos-beta).

## Quasi-polynomial formula for bishops on white squares

Write $R_W(m, k)$ for the number of
placements of $k$ nonattacking bishops on the white squares (those $(i, j)$ with $i + j$ even) of
the $m \times m$ board $[1, m]^2$, $\pi(m) \in \lbrace 0, 1 \rbrace$ for the remainder of $m$
modulo $2$, and $c_{k,d}(z) \in \mathbb{C}$ for the constituent coefficient of the bishop colour
quasi-polynomials (defined for natural $k, d$ and complex $z$). For all natural numbers $m$ and
$k$, as complex numbers,

$$
R_W(m, k) = \sum_{d=0}^{2k} c_{k,d}\bigl(-\pi(m)\bigr)\, m^d.
$$

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Theorem 10 (`jis-2025-25.8.6-thm-10`).

Stated but not proved: `MetaMathlibExt.bishopsWhite_eq_quasi` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#bishops-white-eq-quasi).

## Quasi-polynomial formula for bishops on the black squares

Let $R_K(m, k)$ be the
number of nonattacking placements of $k$ bishops on the black squares $(i, j)$, with $i + j$
odd, of the board $\{1, \dots, m\}^2$, and let $c_{k,d}(z)$ be the constituent coefficients of
the bishop quasi-polynomials. For all natural numbers $m$ and $k$,

$$R_K(m, k) = \sum_{d=0}^{2k} c_{k,d}(\pi(m)) \, m^d$$

in $\mathbb{C}$, where $\pi(m) \in \{0, 1\}$ is the remainder of $m$ modulo $2$.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Theorem 10 (`jis-2025-25.8.6-thm-10`).

Stated but not proved: `MetaMathlibExt.bishopsBlack_eq_quasi` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#bishops-black-eq-quasi).

## Quasi-polynomial formula for bishops on a square board

Write $B_S(m, k)$ for the number of
placements of $k$ nonattacking bishops on the $m \times m$ board $[1, m]^2$,
$\pi(m) \in \lbrace 0, 1 \rbrace$ for the remainder of $m$ modulo $2$, and
$c_{k,d}(z) \in \mathbb{C}$ for the constituent coefficient of the bishop colour quasi-polynomials
(defined for natural $k, d$ and complex $z$). For all natural numbers $m$ and $k$, as complex
numbers,

$$
B_S(m, k) = \sum_{d=0}^{2k} \Biggl( \sum_{j=0}^{k} \sum_{i=0}^{d}
c_{j,i}\bigl(-\pi(m)\bigr)\, c_{k-j,\,d-i}\bigl(\pi(m)\bigr) \Biggr) m^d.
$$

The factors $c_{j,i}(-\pi(m))$ and $c_{k-j,d-i}(\pi(m))$ are the coefficients of the corresponding
quasi-polynomial formulas for bishops on the white and on the black squares.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Theorem 10 (`jis-2025-25.8.6-thm-10`).

Stated but not proved: `MetaMathlibExt.bishopsSquare_eq_quasi` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#bishops-square-eq-quasi).

## Recurrence for anassas below the diagonal

Let $A(m, k, p)$ be the number of
nonattacking placements of $k$ anassas on the square board $\{1, \dots, m\}^2$ with exactly $p$
of them strictly below the main diagonal, let ${n \brace j}$ be Knuth's extended Stirling
numbers of the second kind, and let $\delta$ be the Kronecker delta. For $m \ge 1$, $k \ge 2$
and $p \ge 1$,

$$A(m, k, p) = A(m-1, k, p) + (m-k+1) A(m-1, k-1, p) + (m-p) A(m-1, k-1, p-1) +
(m-p)(m-k+1) A(m-1, k-2, p-1)$$

in the integers. Moreover, for all natural numbers $m$, $k$ and $p$,
$A(0, k, p) = \delta_{k0} \delta_{p0}$, $A(m, 0, p) = \delta_{p0}$,
$A(m, 1, p) = {m+1 \brace m} \delta_{p0} + {m \brace m-1} \delta_{p1}$ and
$A(m, k, 0) = {m+1 \brace m-k+1}$.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Theorem 11 (`jis-2025-25.8.6-thm-11`).

Stated but not proved: `MetaMathlibExt.anassasBelow_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#anassas-below-recurrence).

## Sum formula for anassas below the diagonal

Let $A(m, k, p)$ be the number of
nonattacking placements of $k$ anassas on the square board $\{1, \dots, m\}^2$ with exactly $p$
of them strictly below the main diagonal, and let ${n \brace j}$ be Knuth's extended Stirling
numbers of the second kind. For natural numbers $m$, $k$, $p$ with $p \le k$,

$$A(m, k, p) = \sum_{j=0}^{p} (m-k+j)_j \binom{k-p-1}{j} \binom{k-j}{k-p}
{m+1 \brace m-k+j+1}$$

in the integers, where $(x)_j = x(x-1)\cdots(x-j+1)$ is the falling factorial and
$\binom{k-p-1}{j}$ is the generalized binomial coefficient, so that $\binom{-1}{j} = (-1)^j$.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Theorem 11 (`jis-2025-25.8.6-thm-11`).

Stated but not proved: `MetaMathlibExt.anassasBelow_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#anassas-below-eq-sum).

## Total number of nonattacking anassas on the square board

For natural numbers $m$ and
$k$ and each $p$, let $A_S(m, k, p)$ be the number of nonattacking placements of $k$ anassas on
the square board $[1, m]^2$ with exactly $p$ of them strictly below the main diagonal, that is,
the number of $k$-element sets of squares $(i, j) \in [1, m]^2$ in which no two squares have
the same $i$ or the same $i - j$ and exactly $p$ squares satisfy $j < i$. Then, in $\mathbb{Q}$,

$$
\sum_{p=0}^{k} A_S(m, k, p) = \sum_{j=0}^{\lceil k/2 \rceil} (m-k+j)_j
\left\{ {m \atop m-k+j} \right\} 2^{k-2j} \left( \binom{k-j}{j-1} + \binom{k-j+1}{j} \right),
$$

where $(x)_j = x(x-1) \cdots (x-j+1)$ is the falling factorial, $\binom{k-j}{-1} = 0$, the power
$2^{k-2j}$ has an integer exponent, and $\left\{ {n \atop i} \right\}$ is Knuth's extension of
the Stirling numbers of the second kind to integer arguments; since $m \ge 0$, here it is the
ordinary Stirling number when $m - k + j \ge 0$ and $0$ otherwise.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Theorem 13 (`jis-2025-25.8.6-thm-13`).

Stated but not proved: `MetaMathlibExt.sum_anassasBelow_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 354](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L354). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#sum-anassas-below-eq).

## Polynomial formula for the number of nonattacking anassas

For natural numbers $m$ and
$k$, let $A_S(m, k, p)$ be the number of nonattacking placements of $k$ anassas on the square
board $[1, m]^2$ with exactly $p$ of them strictly below the main diagonal, that is, the number
of $k$-element sets of squares $(i, j) \in [1, m]^2$ in which no two squares have the same $i$
or the same $i - j$ and exactly $p$ squares satisfy $j < i$. Then, in $\mathbb{Q}$,
$\sum_{p=0}^{k} A_S(m, k, p) = \sum_{d=0}^{2k} c_d m^d$ with

$$
c_d = \sum_{i=d}^{2k} \frac{(-1)^{i-d}}{i!} \left[ {i \atop d} \right]
\sum_{j=0}^{U(i,k)} \alpha(k, j) \sum_{p=L(i,k)}^{k-j} S_2(p+k-j, p)
\sum_{b=0}^{j} \binom{p}{b} \binom{k}{j-b} \binom{b}{k+p-i},
$$

where $\left[ {i \atop d} \right]$ is the unsigned Stirling number of the first kind, $S_2$ is
the 2-associated Stirling number of the second kind,
$\alpha(k, j) = 2^{k-2j} \left( \binom{k-j}{j-1} + \binom{k-j+1}{j} \right) j!$ with
$\binom{k-j}{-1} = 0$ and an integer exponent in $2^{k-2j}$,
$U(i, k) = \min(\lceil k/2 \rceil, 2k - i)$ and $L(i, k) = \max(0, i - k)$.

## Sources

- Eder G. Santos, *Counting Nonattacking Chess Piece Placements: Bishops and Anassas*, Journal of Integer Sequences 28 (2025), Article 25.8.6, Theorem 16 (`jis-2025-25.8.6-thm-16`).

Stated but not proved: `MetaMathlibExt.sum_anassasBelow_eq_poly` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NonattackingBishopsAnassasWanted.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html#sum-anassas-below-eq-poly).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Nonattacking bishops and anassas](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/tilings-board-placements/nonattacking-bishops-and-anassas)
