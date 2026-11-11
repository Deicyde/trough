---
declaration: section
origin: cited
lean: MetaMathlibExt.pebblingStep, MetaMathlibExt.sum_pebblingStep_add_one, MetaMathlibExt.pebblingMoves, MetaMathlibExt.mem_pebblingMoves, MetaMathlibExt.pebblingGame, MetaMathlibExt.pebblingGame_isP_of_forall_le, MetaMathlibExt.pebblingAllNTotals, MetaMathlibExt.zero_not_mem_pebblingAllNTotals
statement: formalized
---

# Impartial pebbling games

42 results, 19 proved and 23 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html).

## A $(k+1:k)$-pebbling move

Let $a = (a_0, \dots, a_{n-1})$ be a distribution of pebbles on
the vertices $0, \dots, n-1$, let $k$ be a natural number and let $i$ and $j$ be vertices. The
position after the $(k+1:k)$-pebbling move from $i$ to $j$ is the distribution $b$ with
$b_j = a_j + k$, $b_i = a_i - (k + 1)$ if $i \ne j$, and $b_x = a_x$ for every other vertex $x$.
When $i \ne j$ and $a_i \ge k + 1$, this removes $k + 1$ pebbles from $i$ and adds $k$ pebbles
to $j$.

Subtraction is truncated at $0$, so $b_i = 0$ when $i \ne j$ and $a_i < k + 1$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Section 1 (definition of a `(k+1:k)`-pebbling move).

Formalized by `MetaMathlibExt.pebblingStep`, a definition declared in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-step).

## A pebbling move removes exactly one pebble

Let $n, k \in \mathbb{N}$, let $a$ assign
$a(x) \in \mathbb{N}$ pebbles to each vertex $x \in \{0, \dots, n-1\}$, and let $i \ne j$ be
vertices with $a(i) \ge k + 1$. Then the pebbling step from $i$ to $j$, which removes $k + 1$
pebbles from $i$ and adds $k$ pebbles to $j$, gives a position $b$ with
$\sum_x b(x) + 1 = \sum_x a(x)$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Section 1 (definition of a `(k+1:k)`-pebbling move).

Formalized by `MetaMathlibExt.sum_pebblingStep_add_one`, a theorem declared in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#sum-pebbling-step-add-one).

## Moves of the $(k+1:k)$-pebbling game

Let $G$ be a simple graph on the vertices
$0, \dots, n-1$, let $k$ be a natural number and let $a = (a_0, \dots, a_{n-1})$ be a distribution
of pebbles on the vertices. This is the finite set of distributions reachable from $a$ by one
$(k+1:k)$-pebbling move on $G$: for adjacent vertices $i$ and $j$ with $a_i \ge k + 1$, remove
$k + 1$ pebbles from $i$ and add $k$ pebbles to $j$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Section 1 (successors of a game).

Formalized by `MetaMathlibExt.pebblingMoves`, a definition declared in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-moves).

## Successors of a pebbling position

Let $G$ be a simple graph on the vertices
$0, \dots, n-1$, let $k$ be a natural number, and let $a$ and $b$ be distributions of pebbles on
the vertices of $G$. Then $b$ is reachable from $a$ by one $(k+1:k)$-pebbling move on $G$ if and
only if there are adjacent vertices $i$ and $j$ of $G$ such that $i$ holds at least $k + 1$
pebbles in $a$ and $b$ is obtained from $a$ by removing $k + 1$ pebbles from $i$ and adding $k$
pebbles to $j$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Section 1 (successors of a game).

Formalized by `MetaMathlibExt.mem_pebblingMoves`, a theorem declared in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#mem-pebbling-moves).

## The $(k+1:k)$-pebbling game

Let $G$ be a simple graph on the vertices $0, \dots, n-1$ and
let $k$ be a natural number. The impartial two-player $(k+1:k)$-pebbling game
$\Gamma^{(k+1:k)}_G$ has as positions all distributions $a = (a_0, \dots, a_{n-1})$ of pebbles on
the vertices, with $a_i \in \mathbb{N}$. A move from $a$ chooses adjacent vertices $i$ and $j$
with $a_i \ge k + 1$, removes $k + 1$ pebbles from $i$ and adds $k$ pebbles to $j$. The game is
ranked by the total number of pebbles $a_0 + \dots + a_{n-1}$, which every move decreases.

Its designated start position, which is not used, is the empty distribution.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Section 1.

Formalized by `MetaMathlibExt.pebblingGame`, a definition declared in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-game).

## Positions with at most $k$ pebbles on every vertex are P-positions

Let $G$ be a simple
graph on the vertices $0, \dots, n-1$ and let $k$ be a natural number. In the
$(k+1:k)$-pebbling game on $G$, every position with at most $k$ pebbles on each vertex is a
P-position.

Such a position is terminating: no move is possible from it.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Section 1 (terminating games are P-games).

Formalized by `MetaMathlibExt.pebblingGame_isP_of_forall_le`, a theorem declared in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-game-is-p-of-forall-le).

## Totals at which every pebbling game is an N-game

Let $G$ be a simple graph on the
vertices $0, \dots, n-1$ and let $k$ be a natural number. In the $(k+1:k)$-pebbling game on $G$,
a move removes $k+1$ pebbles from a vertex and adds $k$ pebbles to an adjacent vertex. This is
the set of natural numbers $m$ such that every position with $m$ pebbles in total (a number of
pebbles on each vertex, summing to $m$) is an N-position, that is, not a P-position.

The paper's $m^{(k+1:k)}(G)$ is the least element of this set when the set is nonempty, and
"$m^{(k+1:k)}(G)$ does not exist" means the set is empty. The paper takes $m$ positive; $0$ never
lies in the set, because the empty position is a P-position.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Section 1 (definition of `m^{(k+1:k)}(G)`).

Formalized by `MetaMathlibExt.pebblingAllNTotals`, a definition declared in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-all-ntotals).

## The total zero is never an all-N total

For every simple graph $G$ on the vertex set
$\{0, \dots, n-1\}$ and every $k \in \mathbb{N}$, the number $0$ does not belong to the set of
totals $m$ such that every $(k+1:k)$-pebbling game on $G$ with $m$ pebbles is an N-game. Indeed,
the empty position admits no move, so it is a P-game.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Section 1 (definition of `m^{(k+1:k)}(G)`).

Formalized by `MetaMathlibExt.zero_not_mem_pebblingAllNTotals`, a theorem declared in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#zero-not-mem-pebbling-all-ntotals).

## Winning positions of $(2:1)$-pebbling on $K_2$

Let $a = (a_0, a_1)$ be a position of the
$(2:1)$-pebbling game on the complete graph $K_2$, with $a_0$ and $a_1$ pebbles on its two
vertices. If $a_0 + a_1$ is even, then $a$ is an N-position (that is, not a P-position) if and
only if $a_0 \not\equiv a_1 \pmod 3$. If $a_0 + a_1$ is odd, then $a$ is an N-position if and
only if $a_0 \equiv a_1 \pmod 3$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Theorem 1(a), quoting E. Fiorini, M. Lind, A. Woldar, and T. W. H. Wong, J. Integer Sequences 24 (2021), Article 21.6.4.

Stated but not proved: `MetaMathlibExt.pebbling_completeTwo_isN_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-complete-two-is-n-iff).

## No all-N threshold for $(2:1)$-pebbling on $K_2$

For every natural number $m$, some
$(2:1)$-pebbling game on the complete graph $K_2$ with $m$ pebbles in total is a P-game; that is,
$m^{(2:1)}(K_2)$, the least total at which every game is an N-game, does not exist.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Theorem 1(a), quoting Fiorini, Lind, Woldar, and Wong (2021).

Stated but not proved: `MetaMathlibExt.pebblingAllNTotals_completeTwo_eq_empty` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-all-ntotals-complete-two-eq-emp).

## All-N threshold of $(2:1)$-pebbling on $K_3$

The least number $m$ such that every
$(2:1)$-pebbling game on the complete graph $K_3$ with $m$ pebbles in total is an N-game, written
$m^{(2:1)}(K_3)$, exists and equals $7$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Theorem 1(b), quoting Fiorini, Lind, Woldar, and Wong (2021).

Stated but not proved: `MetaMathlibExt.isLeast_pebblingAllNTotals_completeThree_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#is-least-pebbling-all-ntotals-complete-t).

## All-N threshold of $(2:1)$-pebbling on $K_4$

The least number $m$ such that every
$(2:1)$-pebbling game on the complete graph $K_4$ with $m$ pebbles in total is an N-game, written
$m^{(2:1)}(K_4)$, exists and equals $23$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Theorem 1(c), quoting Fiorini, Lind, Woldar, and Wong (2021).

Stated but not proved: `MetaMathlibExt.isLeast_pebblingAllNTotals_completeFour_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#is-least-pebbling-all-ntotals-complete-f).

## All-N threshold of $(2:1)$-pebbling on $K_n$ for odd $n$

For every odd $n \ge 5$, the
least number $m$ such that every $(2:1)$-pebbling game on the complete graph $K_n$ with $m$
pebbles in total is an N-game, written $m^{(2:1)}(K_n)$, exists and equals $n + 2$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Theorem 1(d), quoting Fiorini, Lind, Woldar, and Wong (2021).

Stated but not proved: `MetaMathlibExt.isLeast_pebblingAllNTotals_complete_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#is-least-pebbling-all-ntotals-complete-o).

## All-N threshold of $(2:1)$-pebbling on $K_n$ for even $n$

For every even $n \ge 6$, the
least number $m$ such that every $(2:1)$-pebbling game on the complete graph $K_n$ with $m$
pebbles in total is an N-game, written $m^{(2:1)}(K_n)$, exists and equals $n + 7$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Theorem 1(e), quoting Fiorini, Lind, Woldar, and Wong (2021).

Stated but not proved: `MetaMathlibExt.isLeast_pebblingAllNTotals_complete_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#is-least-pebbling-all-ntotals-complete-e).

## All-N threshold of $(k+1:k)$-pebbling on $K_3$

For every positive integer $k$, the least
number $m$ such that every $(k+1:k)$-pebbling game on the complete graph $K_3$ with $m$ pebbles in
total is an N-game, written $m^{(k+1:k)}(K_3)$, exists and equals $6k + 1$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Theorem 2.

Stated but not proved: `MetaMathlibExt.isLeast_pebblingAllNTotals_completeThree` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#is-least-pebbling-all-ntotals-complete-t-2).

## Pebbling on the triangle: a single pile of 2k+3 pebbles is a P-position

Let $k$ be a
positive integer and consider the $(k+1:k)$-pebbling game on the complete graph $K_3$, where a
move removes $k+1$ pebbles from one vertex and adds $k$ pebbles to another. Every position with
$2k + 3$ pebbles on one vertex and none on the other two is a P-position.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Lemma 4.

Stated but not proved: `MetaMathlibExt.pebbling_completeThree_isP_twoKAddThree` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-complete-three-is-p-two-kadd-th).

## Pebbling on the triangle: a two-parameter family of P-positions

Let $k$ be a positive
integer and consider the $(k+1:k)$-pebbling game on the complete graph $K_3$, where a move removes
$k+1$ pebbles from one vertex and adds $k$ pebbles to another. Let $\ell_1 \le \ell_2$ be
natural numbers with $\ell_1 + \ell_2 \le k - 1$. Every position whose three piles are
$2k - 1 - \ell_1 - \ell_2$, $k - \ell_1$ and $k - \ell_2$ in some order is a P-position.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Lemma 5.

Stated but not proved: `MetaMathlibExt.pebbling_completeThree_isP_twoKSubOne` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-complete-three-is-p-two-ksub-on).

## Pebbling on the triangle: piles 4k+1, k-1, k-1 form a P-position

Let $k$ be a positive
integer and consider the $(k+1:k)$-pebbling game on the complete graph $K_3$, where a move removes
$k+1$ pebbles from one vertex and adds $k$ pebbles to another. Every position whose three piles
are $4k + 1$, $k - 1$ and $k - 1$ in some order is a P-position.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Lemma 6.

Stated but not proved: `MetaMathlibExt.pebbling_completeThree_isP_fourKAddOne` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-complete-three-is-p-four-kadd-o).

## Pebbling on the triangle: a reply that brings every pile below the bound

Let $k$ be a
positive integer and consider the $(k+1:k)$-pebbling game on the complete graph $K_3$, where a
move removes $k+1$ pebbles from one vertex and adds $k$ pebbles to another. Let $\ell$ be a
natural number with $\ell \le 2k - 1$, and let $a$ be a position with $6k - 2\ell$ pebbles in
total in which some pile has at least $k + 1$ pebbles and every pile has at most $3k - \ell$
pebbles. Then for every position $b$ reachable from $a$ by one move there is a position $c$
reachable from $b$ by one move in which every pile has at most $3k - \ell - 1$ pebbles.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Lemma 7.

Stated but not proved: `MetaMathlibExt.pebbling_completeThree_response_lowersMax` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-complete-three-response-lowers).

## Pebbling on the triangle: total 6k-2ℓ with no pile above half is a P-position

Let $k$ be
a positive integer and consider the $(k+1:k)$-pebbling game on the complete graph $K_3$, where a
move removes $k+1$ pebbles from one vertex and adds $k$ pebbles to another. Let $\ell$ be a
natural number with $\ell \le 2k - 1$. Every position with $6k - 2\ell$ pebbles in total in which
every pile is at most $3k - \ell$ is a P-position.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Lemma 8.

Stated but not proved: `MetaMathlibExt.pebbling_completeThree_isP_of_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-complete-three-is-p-of-le).

## Pebbling on the triangle: N-positions with total 6k-2ℓ+1 and a small pile

Let $k$ be a
positive integer and consider the $(k+1:k)$-pebbling game on the complete graph $K_3$, where a
move removes $k+1$ pebbles from one vertex and adds $k$ pebbles to another. Let $\ell$ be an
integer with $1 \le \ell \le 2k - 1$. Every position with $6k - 2\ell + 1$ pebbles in total in
which every pile is at most $4k - \ell + 1$ and some pile is at most $2k - \ell$ is an
N-position, that is, not a P-position.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Lemma 9.

Stated but not proved: `MetaMathlibExt.pebbling_completeThree_isN_of_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-complete-three-is-n-of-le).

## Pebbling on the triangle: total 6k-1 with every pile at most 4k

Let $k$ be a positive
integer and consider the $(k+1:k)$-pebbling game on the complete graph $K_3$, where a move removes
$k+1$ pebbles from one vertex and adds $k$ pebbles to another. Every position with $6k - 1$
pebbles in total in which every pile is at most $4k$ is an N-position, that is, not a P-position.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Corollary 10.

Stated but not proved: `MetaMathlibExt.pebbling_completeThree_isN_of_le_fourK` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-complete-three-is-n-of-le-four).

## Pebbling on the triangle: N-positions with an empty vertex

Let $k$ be a natural number
and consider the $(k+1:k)$-pebbling game on the complete graph $K_3$, where a move removes $k+1$
pebbles from one vertex and adds $k$ pebbles to another. Let $\ell$ be an integer with
$1 \le \ell \le k - 1$, and let $a_1, a_2$ be natural numbers with $a_1 + a_2 = 6k - 2\ell + 1$
and $a_2 \le k$. Every position whose three piles are $a_1$, $a_2$ and $0$ in some order is an
N-position, that is, not a P-position.

The paper's ordering $a_1 \ge a_2$ follows from these hypotheses.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Lemma 11.

Stated but not proved: `MetaMathlibExt.pebbling_completeThree_isN_of_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-complete-three-is-n-of-zero).

## Pebbling on the triangle: total 6k-1 with a pile of at least 4k+1

Let $k$ be a positive
integer and consider the $(k+1:k)$-pebbling game on the complete graph $K_3$, where a move removes
$k+1$ pebbles from one vertex and adds $k$ pebbles to another. Every position with $6k - 1$
pebbles in total in which some pile is at least $4k + 1$, other than the positions whose three
piles are $4k + 1$, $k - 1$ and $k - 1$ in some order, is an N-position, that is, not a
P-position.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Lemma 12.

Stated but not proved: `MetaMathlibExt.pebbling_completeThree_isN_of_ge_fourKAddOne` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-complete-three-is-n-of-ge-four).

## The set $X_{aaab}$ of $C_4$ positions

A position $a = (a_0, a_1, a_2, a_3)$ of
natural-number pebble counts on the vertices $v_0, v_1, v_2, v_3$ of $C_4$, with indices read
modulo $4$, lies in $X_{aaab}$ when there is an index $i$ such that
$a_i \equiv a_{i+1} \equiv a_{i+2} \pmod 3$ and $a_{i-1} \not\equiv a_i \pmod 3$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Section 3 (definition of `X_{aaab}`).

Formalized by `MetaMathlibExt.C4PatternAAAB`, a definition declared in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#c4-pattern-aaab).

## The set $X_{abab}$ of $C_4$ positions

A position $a = (a_0, a_1, a_2, a_3)$ of
natural-number pebble counts on the vertices $v_0, v_1, v_2, v_3$ of $C_4$ lies in $X_{abab}$
when $a_0 \equiv a_2 \pmod 3$, $a_1 \equiv a_3 \pmod 3$ and $a_0 \not\equiv a_1 \pmod 3$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Section 3 (definition of `X_{abab}`).

Formalized by `MetaMathlibExt.C4PatternABAB`, a definition declared in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#c4-pattern-abab).

## The set $X_{aabc}$ of $C_4$ positions

A position $a = (a_0, a_1, a_2, a_3)$ of
natural-number pebble counts on the vertices $v_0, v_1, v_2, v_3$ of $C_4$, with indices read
modulo $4$, lies in $X_{aabc}$ when there is an index $i$ with $a_i \equiv a_{i+1} \pmod 3$ such
that $a_i$, $a_{i+2}$ and $a_{i-1}$ are pairwise incongruent modulo $3$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Section 3 (definition of `X_{aabc}`).

Formalized by `MetaMathlibExt.C4PatternAABC`, a definition declared in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#c4-pattern-aabc).

## The set $X_{abac}$ of $C_4$ positions

A position $a = (a_0, a_1, a_2, a_3)$ of
natural-number pebble counts on the vertices $v_0, v_1, v_2, v_3$ of $C_4$, with indices read
modulo $4$, lies in $X_{abac}$ when there is $i \in \{0, 1\}$ with $a_i \equiv a_{i+2} \pmod 3$
such that $a_i$, $a_{i+1}$ and $a_{i-1}$ are pairwise incongruent modulo $3$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Section 3 (definition of `X_{abac}`).

Formalized by `MetaMathlibExt.C4PatternABAC`, a definition declared in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#c4-pattern-abac).

## The set $\hat X_{aabb}$ of $C_4$ positions

A position $a = (a_0, a_1, a_2, a_3)$ of
natural-number pebble counts on the vertices $v_0, v_1, v_2, v_3$ of $C_4$, with indices read
modulo $4$, lies in $\hat X_{aabb}$ when there is $i \in \{0, 1\}$ with
$a_i \equiv a_{i+1} \pmod 3$ and $a_{i+2} \equiv a_{i-1} \pmod 3$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Section 3 (definition of `\hat X_{aabb}`).

Formalized by `MetaMathlibExt.C4PatternAABBHat`, a definition declared in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#c4-pattern-aabbhat).

## The set $Y_{aabc}$ of $C_4$ positions

A position $a = (a_0, a_1, a_2, a_3)$ of
natural-number pebble counts on the vertices $v_0, v_1, v_2, v_3$ of $C_4$, with indices read
modulo $4$, lies in $Y_{aabc}$ when there is an index $i$ with $a_{i+2} \equiv a_i + 2 \pmod 4$
and $a_{i+1} \equiv a_{i-1} + 1 \pmod 4$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Section 3 (definition of `Y_{aabc}`).

Formalized by `MetaMathlibExt.C4ModFourAABC`, a definition declared in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#c4-mod-four-aabc).

## The set $\hat Y_{abac}$ of $C_4$ positions

A position $a = (a_0, a_1, a_2, a_3)$ of
natural-number pebble counts on the vertices $v_0, v_1, v_2, v_3$ of $C_4$, with indices read
modulo $4$, lies in $\hat Y_{abac}$ when there is an index $i$ with $a_i \equiv a_{i+2} \pmod 4$
and $a_{i+1} \equiv a_{i-1} + 1 \pmod 4$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Section 3 (definition of `\hat Y_{abac}`).

Formalized by `MetaMathlibExt.C4ModFourABACHat`, a definition declared in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#c4-mod-four-abachat).

## The set $\hat Y_{abab}$ of $C_4$ positions

A position $a = (a_0, a_1, a_2, a_3)$ of
natural-number pebble counts on the vertices $v_0, v_1, v_2, v_3$ of $C_4$ lies in
$\hat Y_{abab}$ when $a_0 \equiv a_2 \pmod 4$ and $a_1 \equiv a_3 \pmod 4$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Section 3 (definition of `\hat Y_{abab}`).

Formalized by `MetaMathlibExt.C4ModFourABABHat`, a definition declared in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#c4-mod-four-ababhat).

## The complement set $(\hat Y_{abab})^c$ of $C_4$ positions

A position
$a = (a_0, a_1, a_2, a_3)$ of natural-number pebble counts on the vertices $v_0, v_1, v_2, v_3$
of $C_4$ lies in $(\hat Y_{abab})^c$ when its total $a_0 + a_1 + a_2 + a_3$ is even and $a$ does
not lie in $\hat Y_{abab}$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Section 3 (definition of `(\hat Y_{abab})^c`).

Formalized by `MetaMathlibExt.C4ModFourABABHatCompl`, a definition declared in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#c4-mod-four-ababhat-compl).

## Examples of the mod-$3$ pattern classes on $C_4$

Writing a distribution of pebbles on the
vertices $v_0, v_1, v_2, v_3$ of $C_4$ as $(a_0, a_1, a_2, a_3)$, we have
$(0,0,0,0) \in \hat X_{aabb}$, $(1,0,0,0) \in X_{aaab}$, $(0,1,0,1) \in X_{abab}$,
$(0,0,1,2) \in X_{aabc}$, $(0,1,0,2) \in X_{abac}$, and $(0,0,0,0) \notin X_{aaab}$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Section 3 (definitions of the sets `X`).

Formalized by `MetaMathlibExt.c4Pattern_examples`, a theorem declared in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#c4-pattern-examples).

## Examples of positions in the sets $Y$ for $C_4$

Writing $(a_0, a_1, a_2, a_3)$ for the
position with $a_j$ pebbles on vertex $v_j$ of $C_4$: the position $(2, 0, 0, 1)$ lies in
$Y_{aabc}$, the position $(0, 1, 0, 0)$ lies in $\hat Y_{abac}$, the position $(0, 0, 0, 0)$ lies
in $\hat Y_{abab}$, and the position $(1, 1, 0, 0)$ lies in $(\hat Y_{abab})^c$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Section 3 (definitions of the sets `Y`).

Formalized by `MetaMathlibExt.c4ModFour_examples`, a theorem declared in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 413](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L413). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#c4-mod-four-examples).

## Invariance of the mod-$3$ pattern classes under symmetric replies on $C_4$

Consider the
$(2:1)$-pebbling game on the cycle $C_4$ with vertices $v_0, v_1, v_2, v_3$, indices read modulo
$4$, and let $a = (a_0, a_1, a_2, a_3)$ be a position with $a_i$ pebbles on $v_i$. Let $j$ be an
index with $a_j \ge 2$, let $\varepsilon \in \{1, -1\}$, and let $b$ be the position obtained from
$a$ by the move from $v_j$ to $v_{j+\varepsilon}$, which removes two pebbles from $v_j$ and adds
one pebble to $v_{j+\varepsilon}$. Let $c$ be obtained from $b$ either by the move from $v_{j+2}$
to $v_{j-\varepsilon}$, where $b_{j+2} \ge 2$, or by the move from $v_{j-\varepsilon}$ to
$v_{j+2}$, where $b_{j-\varepsilon} \ge 2$. Then for each of the sets $X_{aaab}$, $X_{abab}$,
$X_{aabc}$, $X_{abac}$ and $\hat X_{aabb}$, if $a$ lies in the set, then so does $c$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Lemma 14.

Stated but not proved: `MetaMathlibExt.c4Pattern_invariant_rotationalSymmetric_reflectional` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 427](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#c4-pattern-invariant-rotational-symmetri).

## Closure of the mod-$3$ pattern classes under moves on $C_4$

Let $a$ and $b$ be
distributions of pebbles on the vertices of the $4$-cycle $C_4$ such that $b$ is obtained from $a$
by one $(2:1)$-pebbling move, that is, by removing two pebbles from a vertex holding at least two
pebbles and adding one pebble to an adjacent vertex. If $a \in \hat X_{aabb} \cup X_{abac}$, then
$b \in \hat X_{aabb} \cup X_{abac}$; and if $a \in X_{aaab} \cup X_{abab} \cup X_{aabc}$, then
$b \in X_{aaab} \cup X_{abab} \cup X_{aabc}$.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Lemma 15.

Stated but not proved: `MetaMathlibExt.c4Pattern_closed_under_moves` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#c4-pattern-closed-under-moves).

## Parity decides $(2:1)$-pebbling on $C_4$ in $\hat X_{aabb} \cup X_{abac}$

Consider the
$(2:1)$-pebbling game on the cycle $C_4$ with vertices $v_0, v_1, v_2, v_3$, where $v_i$ is
adjacent to $v_{i \pm 1}$ (indices mod $4$), and let $a = (a_0, a_1, a_2, a_3)$ be a position
with $a_i$ pebbles on $v_i$. Suppose that $a$ lies in $\hat X_{aabb} \cup X_{abac}$, where
$\hat X_{aabb}$ means that for some $i \in \{0, 1\}$, $a_i \equiv a_{i+1}$ and
$a_{i+2} \equiv a_{i-1} \pmod 3$, and $X_{abac}$ means that for some $i \in \{0, 1\}$,
$a_i \equiv a_{i+2} \pmod 3$ and $a_i$, $a_{i+1}$, $a_{i-1}$ are pairwise incongruent mod $3$.
Then $a$ is a P-position if and only if $a_0 + a_1 + a_2 + a_3$ is even.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Theorem 16.

Stated but not proved: `MetaMathlibExt.pebbling_cycleFour_isP_iff_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-cycle-four-is-p-iff-even).

## Positions in $\hat Y_{abab}$ are P-positions of $(2:1)$-pebbling on $C_4$

Consider the
$(2:1)$-pebbling game on the cycle $C_4$ with vertices $v_0, v_1, v_2, v_3$, where $v_i$ is
adjacent to $v_{i \pm 1}$ (indices mod $4$). Every position $a = (a_0, a_1, a_2, a_3)$, with
$a_i$ pebbles on $v_i$, that lies in $\hat Y_{abab}$, that is, with $a_0 \equiv a_2$ and
$a_1 \equiv a_3 \pmod 4$, is a P-position.

The paper's sets range over positive totals; this statement also covers the empty position,
which lies in $\hat Y_{abab}$ and is a P-position because no move is possible from it.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Theorem 17.

Stated but not proved: `MetaMathlibExt.pebbling_cycleFour_isP_of_modFourABABHat` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 466](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-cycle-four-is-p-of-mod-four-aba).

## Positions in $(X_{abab} \cup X_{aabc} \cup X_{aaab}) \cap \hat Y_{abac}$ are P-positions of $(2:1)$-pebbling on $C_4$

**Positions in $(X_{abab} \cup X_{aabc} \cup X_{aaab}) \cap \hat Y_{abac}$ are P-positions
of $(2:1)$-pebbling on $C_4$.** Consider the
$(2:1)$-pebbling game on the cycle $C_4$ with vertices $v_0, v_1, v_2, v_3$, where $v_i$ is
adjacent to $v_{i \pm 1}$ (indices mod $4$), and let $a = (a_0, a_1, a_2, a_3)$ be a position
with $a_i$ pebbles on $v_i$. Suppose that $a$ lies in $X_{abab} \cup X_{aabc} \cup X_{aaab}$,
where $X_{abab}$ means $a_0 \equiv a_2$, $a_1 \equiv a_3$ and $a_0 \not\equiv a_1 \pmod 3$;
$X_{aabc}$ means that for some $i$, $a_i \equiv a_{i+1} \pmod 3$ and $a_i$, $a_{i+2}$, $a_{i-1}$
are pairwise incongruent mod $3$; and $X_{aaab}$ means that for some $i$,
$a_i \equiv a_{i+1} \equiv a_{i+2} \not\equiv a_{i-1} \pmod 3$. Suppose also that $a$ lies in
$\hat Y_{abac}$: for some $i$, $a_i \equiv a_{i+2}$ and $a_{i+1} \equiv a_{i-1} + 1 \pmod 4$.
Then $a$ is a P-position.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Theorem 18.

Stated but not proved: `MetaMathlibExt.pebbling_cycleFour_isP_of_modFourABACHat` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 475](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L475). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-cycle-four-is-p-of-mod-four-aba-2).

## Positions in $Y_{aabc}$ are N-positions of $(2:1)$-pebbling on $C_4$

Consider the
$(2:1)$-pebbling game on the cycle $C_4$ with vertices $v_0, v_1, v_2, v_3$, where $v_i$ is
adjacent to $v_{i \pm 1}$ (indices mod $4$). Let $a = (a_0, a_1, a_2, a_3)$ be a position, with
$a_i$ pebbles on $v_i$, that lies in $Y_{aabc}$: for some $i$, $a_{i+2} \equiv a_i + 2$ and
$a_{i+1} \equiv a_{i-1} + 1 \pmod 4$. Then $a$ is an N-position, that is, not a P-position.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Theorem 19.

Stated but not proved: `MetaMathlibExt.pebbling_cycleFour_isN_of_modFourAABC` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 484](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L484). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-cycle-four-is-n-of-mod-four-aab).

## Positions in $(X_{abab} \cup X_{aabc} \cup X_{aaab}) \cap (\hat Y_{abab})^c$ are N-positions of $(2:1)$-pebbling on $C_4$

**Positions in $(X_{abab} \cup X_{aabc} \cup X_{aaab}) \cap (\hat Y_{abab})^c$ are
N-positions of $(2:1)$-pebbling on $C_4$.** Consider the
$(2:1)$-pebbling game on the cycle $C_4$ with vertices $v_0, v_1, v_2, v_3$, where $v_i$ is
adjacent to $v_{i \pm 1}$ (indices mod $4$), and let $a = (a_0, a_1, a_2, a_3)$ be a position
with $a_i$ pebbles on $v_i$. Suppose that $a$ lies in $X_{abab} \cup X_{aabc} \cup X_{aaab}$,
where $X_{abab}$ means $a_0 \equiv a_2$, $a_1 \equiv a_3$ and $a_0 \not\equiv a_1 \pmod 3$;
$X_{aabc}$ means that for some $i$, $a_i \equiv a_{i+1} \pmod 3$ and $a_i$, $a_{i+2}$, $a_{i-1}$
are pairwise incongruent mod $3$; and $X_{aaab}$ means that for some $i$,
$a_i \equiv a_{i+1} \equiv a_{i+2} \not\equiv a_{i-1} \pmod 3$. Suppose also that $a$ lies in
$(\hat Y_{abab})^c$: the total $a_0 + a_1 + a_2 + a_3$ is even, and it is not the case that both
$a_0 \equiv a_2$ and $a_1 \equiv a_3 \pmod 4$. Then $a$ is an N-position, that is, not a
P-position.

## Sources

- Barker, DeStefano, Fiorini, Gohn, Miller, Roeder, and Wong, *Generalized Impartial Two-player Pebbling Games on `K_3` and `C_4`*, Journal of Integer Sequences 27 (2024), Article 24.5.8, Theorem 20.

Stated but not proved: `MetaMathlibExt.pebbling_cycleFour_isN_of_modFourABABHatCompl` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean, line 493](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImpartialPebblingGameWanted.lean#L493). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html#pebbling-cycle-four-is-n-of-mod-four-aba).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Impartial pebbling games](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GameTheory/combinatorial-games/impartial-pebbling-games)
