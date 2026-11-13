---
declaration: section
origin: cited
lean: MetaMathlibExt.euclidPPositionAux, MetaMathlibExt.euclidPPosition, MetaMathlibExt.euclidMoves, MetaMathlibExt.euclidMoves_rank_lt, MetaMathlibExt.euclidGame, MetaMathlibExt.euclidPPositionAux_eq_true_iff, MetaMathlibExt.euclidPPosition_eq_true_iff, MetaMathlibExt.euclidPPosition_small
statement: formalized
---

# Game of Euclid

25 results, 10 proved and 15 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html).

## Fuel-bounded Euclid classifier

The fuel-bounded evaluation of the P-positions of Euclid is
the function $E(f, a, b)$ of natural numbers $f, a, b$ with Boolean values defined by recursion on
the fuel $f$. With no fuel, $E(0, a, b)$ is true. Otherwise $E(f + 1, a, b)$ is true when $a = b$,
$a = 0$ or $b = 0$; when $0 < a < b$ it is true iff $E(f, a, b - ja)$ is false for every $j \ge 1$
with $ja < b$; and when $0 < b < a$ it is true iff $E(f, a - jb, b)$ is false for every $j \ge 1$
with $jb < a$.

In Euclid a move replaces the larger entry by its difference with a positive multiple of the
smaller one, keeping both entries positive, and the player facing two equal entries (no move)
loses. With fuel at least $a + b$ the value is exact.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Section 4.

Formalized by `MetaMathlibExt.euclidPPositionAux`, a definition declared in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#euclid-pposition-aux).

## Euclid P-position test

For natural numbers $a$ and $b$, the Euclid P-position test at
$(a, b)$ is the value at $(a, b)$ of the fuel-bounded evaluation of the P-positions of Euclid with
fuel $a + b$.

It is true exactly at the P-positions of Euclid, the positions from which every move leads to a
position that is not a P-position: each move lowers $a + b$, so fuel $a + b$ suffices.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Section 4.

Formalized by `MetaMathlibExt.euclidPPosition`, a definition declared in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#euclid-pposition).

## Euclid moves

The moves of Euclid from a pair $(a, b)$ of natural numbers are as follows.
If $a = b$, $a = 0$ or $b = 0$, there are none. If $0 < a < b$, the moves are to the pairs
$(a, b - ja)$ for every integer $j \ge 1$ with $ja < b$; if $0 < b < a$, the moves are to the
pairs $(a - jb, b)$ for every integer $j \ge 1$ with $jb < a$.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Section 4.

Formalized by `MetaMathlibExt.euclidMoves`, a definition declared in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#euclid-moves).

## Euclid moves lower the sum

If $(a', b')$ is a Euclid move from $(a, b)$, then
$a' + b' < a + b$.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Section 4.

Formalized by `MetaMathlibExt.euclidMoves_rank_lt`, a theorem declared in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#euclid-moves-rank-lt).

## The game Euclid

Euclid as an impartial game: its positions are the pairs $(a, b)$ of
natural numbers, its moves from $(a, b)$ are the Euclid moves, the rank of $(a, b)$ is $a + b$,
and its starting position is $(1, 1)$.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Section 4.

Formalized by `MetaMathlibExt.euclidGame`, a definition declared in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#euclid-game).

## Correctness of the fuel-bounded Euclid classifier

For all natural numbers $f$, $a$ and $b$
with $a + b \le f$, the fuel-bounded evaluation of the P-positions of Euclid with fuel $f$ returns
true at $(a, b)$ if and only if $(a, b)$ is a normal-play P-position of the Euclid game.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Section 4.

Formalized by `MetaMathlibExt.euclidPPositionAux_eq_true_iff`, a theorem declared in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#euclid-pposition-aux-eq-true-iff).

## The Euclid P-position test is correct

For all natural numbers $a$ and $b$, the Euclid
P-position test returns true at $(a, b)$ if and only if $(a, b)$ is a normal-play P-position of
the Euclid game.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Section 4.

Formalized by `MetaMathlibExt.euclidPPosition_eq_true_iff`, a theorem declared in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#euclid-pposition-eq-true-iff).

## Small P-positions of Euclid

The Euclid P-position test returns true at the pairs $(1, 1)$
and $(3, 2)$ and false at the pairs $(2, 1)$ and $(1, 2)$.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Section 4.

Formalized by `MetaMathlibExt.euclidPPosition_small`, a theorem declared in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#euclid-pposition-small).

## Rows of the Calkin–Wilf tree

Row $k$ of the Calkin–Wilf tree is a list of
numerator–denominator pairs, the pair $(a, b)$ standing for $a/b$. Row $0$ is the single pair
$(1, 1)$, and row $k + 1$ is obtained from row $k$ by replacing each pair $(a, b)$, in order, by
its two children $(a, a + b)$ and $(a + b, b)$.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Section 2.

Formalized by `MetaMathlibExt.calkinWilfRow`, a definition declared in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#calkin-wilf-row).

## The first rows of the Calkin–Wilf tree

As lists of numerator–denominator pairs, row $1$
of the Calkin–Wilf tree is $(1, 2), (2, 1)$ and row $2$ is $(1, 3), (3, 2), (2, 3), (3, 1)$, in
this order.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Section 2.

Formalized by `MetaMathlibExt.calkinWilfRow_one_two`, a theorem declared in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#calkin-wilf-row-one-two).

## Number of P-positions of Euclid in a row of the Calkin–Wilf tree

Let $L_k$ be the
number of P-positions of Euclid in row $k$ of the Calkin–Wilf tree. Then $L_0 = 1$, $L_1 = 0$,
$L_{k+2} = L_{k+1} + 2L_k$ for every $k$, and $3L_k = 2^k + 2(-1)^k$ for every $k$, that is,
$L_k = 2^k/3 + 2(-1)^k/3$.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Corollary 4.6.

Stated but not proved: `MetaMathlibExt.count_euclidPPosition_calkinWilfRow` is written with `theorem_wanted` in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#count-euclid-pposition-calkin-wilf-row).

## Distinguishing the tops of arches

Call a pair $(a, b)$ of natural numbers a P-position
when the Euclid P-position test returns true at $(a, b)$, and read it as the vertex $a/b$ of the
Calkin–Wilf tree, with son $a/(a+b)$ and daughter $(a+b)/b$. Let $m, n$ be positive integers. If
$m/n$ is a P-position, then so are its son's daughter $(2m+n)/(m+n)$ and its daughter's son
$(m+n)/(m+2n)$.

The statement covers all positive pairs; the tree vertices are the coprime ones.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Proposition 4.1.

Stated but not proved: `MetaMathlibExt.euclidPPosition_tops_of_arch` is written with `theorem_wanted` in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#euclid-pposition-tops-of-arch).

## Establishing branches: nieces and nephews of P-positions

Call a pair $(a, b)$ of natural
numbers a P-position when the Euclid P-position test returns true at $(a, b)$, and read it as the
vertex $a/b$ of the Calkin–Wilf tree, with son $a/(a+b)$ and daughter $(a+b)/b$. Let $x, y$ be
positive integers. If the daughter $(x+y)/y$ of $x/y$ is a P-position, then so is its niece
$(2x+y)/(x+y)$, the daughter of its sibling $x/(x+y)$. If the son $x/(x+y)$ of $x/y$ is a
P-position, then so is its nephew $(x+y)/(x+2y)$, the son of its sibling $(x+y)/y$.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Proposition 4.2.

Stated but not proved: `MetaMathlibExt.euclidPPosition_branch_step` is written with `theorem_wanted` in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#euclid-pposition-branch-step).

## Aunt or cousin of a P-position

Call a pair $(a, b)$ of natural numbers a P-position when
the Euclid P-position test returns true at $(a, b)$, and let its son be $s(a, b) = (a, a + b)$ and
its daughter $d(a, b) = (a + b, b)$, as in the Calkin–Wilf tree. Let $x, y$ be positive integers,
let $r = (x, y)$, let $q$ be one of the two children $s(r)$ and $d(r)$ of $r$, and let $q'$ be the
other one. If the daughter $d(q)$ is a P-position, then exactly one of its aunt $q'$ and its male
cousin $s(q')$ is a P-position. If the son $s(q)$ is a P-position, then exactly one of its uncle
$q'$ and its female cousin $d(q')$ is a P-position.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Proposition 4.3.

Stated but not proved: `MetaMathlibExt.euclidPPosition_aunt_xor_cousin` is written with `theorem_wanted` in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#euclid-pposition-aunt-xor-cousin).

## Self-similarity of the P-positions of Euclid

Call a pair $(a, b)$ of natural numbers a
P-position when the Euclid P-position test returns true at $(a, b)$, and read it as the vertex
$a/b$ of the Calkin–Wilf tree, with son $a/(a+b)$ and daughter $(a+b)/b$. Let $V$ be a vertex in
some row of the Calkin–Wilf tree that is a P-position. Then for every finite sequence $w$ of steps,
each step going to the son or to the daughter, the vertex reached from $V$ by following $w$ is a
P-position if and only if the vertex reached from the root $1/1$ by following $w$ is one.

In other words, below every P-position the P-positions sit exactly where they sit below the root.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Theorem 4.5.

Stated but not proved: `MetaMathlibExt.euclidPPosition_self_similar` is written with `theorem_wanted` in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#euclid-pposition-self-similar).

## Number of arch tops in a row of the Calkin–Wilf tree

For $k \ge 2$ let $T_k$ be the
number of vertices of row $k$ of the Calkin–Wilf tree of the form $(2m+n)/(m+n)$ with $m/n$ a
P-position of Euclid in row $k - 2$. Then $3T_k = 2^{k-2} + 2(-1)^k$, that is,
$T_k = 2^{k-2}/3 + 2(-1)^k/3$.

The vertex $(2m+n)/(m+n)$ is the son's daughter of $m/n$, the left top of the arch below $m/n$;
the daughter's son $(m+n)/(m+2n)$ is the right top, so $T_k$ counts the arches whose tops lie in
row $k$.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Corollary 4.7.

Stated but not proved: `MetaMathlibExt.count_arch_tops_calkinWilfRow` is written with `theorem_wanted` in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#count-arch-tops-calkin-wilf-row).

## Levels of the branches of an arch

On numerator–denominator pairs write
$s(x, y) = (x, x + y)$ for the son and $t(x, y) = (x + y, y)$ for the daughter of a vertex of the
Calkin–Wilf tree. Let $a, b, c, d, k$ be natural numbers with $0 < b < a$ and $0 < c < d$. Then
$t(s^k(a - b, b))$, the daughter of the $k$-fold son of $(a - b, b)$, has first entry
$(k+1)a - kb$ and second entry $ka - (k-1)b$, and $s(t^k(c, d - c))$, the son of the $k$-fold
daughter of $(c, d - c)$, has first entry $kd - (k-1)c$ and second entry $(k+1)d - kc$, the
right-hand sides computed in the integers.

When $a/b$ and $c/d$ are the left and right tops of an arch, these pairs are level $k$ (level $0$
the top) of its left branch, which descends by nieces, and of its right branch, which descends by
nephews; the formulas hold without the arch-top hypothesis.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Lemma 5.1.

Stated but not proved: `MetaMathlibExt.arch_branch_levels` is written with `theorem_wanted` in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#arch-branch-levels).

## The Fibonacci arches

Let $F_j$ be the Fibonacci numbers with $F_0 = F_1 = 1$ and
$F_{j+2} = F_{j+1} + F_j$. Call a pair $(a, b)$ of natural numbers a P-position when the Euclid
P-position test returns true at $(a, b)$, read it as the vertex $a/b$ of the Calkin–Wilf tree, and
let $s(a/b) = a/(a+b)$ be its son and $d(a/b) = (a+b)/b$ its daughter; write $s^k$ and $d^k$ for
the $k$-fold iterates. Let $n \ge 1$ and $k \ge 0$, and let $V = F_{2n-1}/F_{2n-2}$. Then $V$ is a
P-position, its son's daughter $d(s(V))$ is $F_{2n+1}/F_{2n}$, and its daughter's son $s(d(V))$
is $F_{2n}/(F_{2n} + F_{2n-2})$. The vertex $L = d(s^k((F_{2n+1} - F_{2n})/F_{2n}))$ is a
P-position whose numerator is $F_{2n+1} + kF_{2n-1}$ and whose denominator is
$F_{2n+1} + (k-1)F_{2n-1}$, and the vertex $R = s(d^k(F_{2n}/F_{2n-2}))$ is the P-position
$(F_{2n} + kF_{2n-2})/(F_{2n} + (k+1)F_{2n-2})$.

Here $L$ and $R$ are level $k$ (level $0$ the top) of the left and right branches of the arch
topped by $d(s(V))$ and $s(d(V))$.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Proposition 5.2.

Stated but not proved: `MetaMathlibExt.fibonacci_arch_positions` is written with `theorem_wanted` in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#fibonacci-arch-positions).

## Fibonacci arch tops

Index the Fibonacci numbers as in the source, $F_0 = F_1 = 1$ and
$F_{j+2} = F_{j+1} + F_j$. Write $a/b$ for the position $(a, b)$ of Euclid, and call $a/(a+b)$
its son and $(a+b)/b$ its daughter. Let $n \ge 1$ and $k \ge 0$ be integers, and let
$X = (F_{2n+1} + kF_{2n-1})/(F_{2n+1} + (k-1)F_{2n-1})$ and
$Y = (F_{2n} + kF_{2n-2})/(F_{2n} + (k+1)F_{2n-2})$. Then $X$ is a P-position of Euclid, and so
are its son's daughter $(3F_{2n+1} + (3k-1)F_{2n-1})/(2F_{2n+1} + (2k-1)F_{2n-1})$ and its
daughter's son $(2F_{2n+1} + (2k-1)F_{2n-1})/(3F_{2n+1} + (3k-2)F_{2n-1})$. Likewise $Y$ is a
P-position of Euclid, and so are its son's daughter
$(3F_{2n} + (3k+1)F_{2n-2})/(2F_{2n} + (2k+1)F_{2n-2})$ and its daughter's son
$(2F_{2n} + (2k+1)F_{2n-2})/(3F_{2n} + (3k+2)F_{2n-2})$.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Corollary 5.3.

Stated but not proved: `MetaMathlibExt.fibonacci_arch_tops` is written with `theorem_wanted` in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#fibonacci-arch-tops).

## Positions of a Calkin–Wilf row with maximal optimal play in Euclid

For every $k \ge 0$,
the number of positions in row $k$ of the Calkin–Wilf tree whose Smith remoteness in the Euclid
game is $k$ equals $2^{k/2}$ if $k$ is even and $2^{(k+1)/2}$ if $k$ is odd.

Smith remoteness is the length of optimal play when the winner hurries and the loser delays.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Proposition 6.1.

Stated but not proved: `MetaMathlibExt.count_max_remoteness_calkinWilfRow` is written with `theorem_wanted` in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#count-max-remoteness-calkin-wilf-row).

## Maximal-remoteness paths alternate in pairs

In the Calkin–Wilf tree the vertex $a/b$ has
son $a/(a+b)$ and daughter $(a+b)/b$. Let $w = (w_0, \dots, w_{\ell-1})$ be a sequence of steps,
each "son" or "daughter", and let $a/b$ be the vertex reached from the root $1/1$ by following
$w$. If the Smith remoteness of the position $(a, b)$ of Euclid equals $\ell$, then
$w_{2i} \ne w_{2i+1}$ for every $i$ with $2i + 1 < \ell$; that is, steps $2i+1$ and $2i+2$ are
one son step and one daughter step, in either order.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Proposition 6.2.

Stated but not proved: `MetaMathlibExt.max_remoteness_path_alternates` is written with `theorem_wanted` in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#max-remoteness-path-alternates).

## Golden-ratio bounds for N-positions of maximal remoteness above 1

Let $\varphi$ be the
golden ratio. If the pair $(m, n)$, read as the fraction $m/n$, lies in row $k$ of the Calkin–Wilf
tree, $n < m$, the position $(m, n)$ of Euclid is not a P-position, and its Smith remoteness in
Euclid equals $k$, then $\varphi < m/n < \varphi + 1$.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Proposition 6.3.

Stated but not proved: `MetaMathlibExt.golden_bounds_of_max_remoteness_N` is written with `theorem_wanted` in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#golden-bounds-of-max-remoteness-n).

## Golden-ratio bounds for N-positions of maximal remoteness below 1

Let $\varphi$ be the
golden ratio. If the pair $(m, n)$, read as the fraction $m/n$, lies in row $k$ of the Calkin–Wilf
tree, $m < n$, the position $(m, n)$ of Euclid is not a P-position, and its Smith remoteness in
Euclid equals $k$, then $1/(\varphi + 1) < m/n < 1/\varphi$.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Corollary 6.4.

Stated but not proved: `MetaMathlibExt.golden_bounds_of_max_remoteness_N_symm` is written with `theorem_wanted` in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#golden-bounds-of-max-remoteness-n-symm).

## Golden-ratio bounds for P-positions of maximal remoteness

Let $\varphi$ be the golden
ratio. If the pair $(m, n)$, read as the fraction $m/n$, lies in row $k$ of the Calkin–Wilf tree,
$m \ne n$, the position $(m, n)$ of Euclid is a P-position, and its Smith remoteness in Euclid
equals $k$, then $(\varphi + 2)/(\varphi + 1) < m/n < \varphi$ or
$1/\varphi < m/n < (\varphi + 1)/(\varphi + 2)$.

The hypothesis $m \ne n$ corrects the printed statement, which fails at the root $1/1$ (a
P-position with $0$ moves in row $0$, and $1$ lies in neither interval).

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Proposition 6.5.

Stated but not proved: `MetaMathlibExt.golden_bounds_of_max_remoteness_P` is written with `theorem_wanted` in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#golden-bounds-of-max-remoteness-p).

## Continued fractions with maximal optimal play in Euclid

For natural numbers
$a_0, \dots, a_r$ write $[a_0, \dots, a_r]$ for the continued fraction
$a_0 + 1/(a_1 + 1/(\cdots + 1/a_r))$, and $1^j$ for a block of $j$ ones; read a positive rational
$u/v$ in lowest terms as the position $(u, v)$ of the Euclid game. Let $n \ge 1$, $i$ and $k$ be
natural numbers. If the position of $[1^{n-1}, 2]$ lies in row $k$ of the Calkin–Wilf tree, its
Smith remoteness is $k$. If the position of $[1^{n-1}, 3]$ lies in row $k$, its Smith remoteness
is less than $k$. If $1 \le i \le n - 2$ and the position of $[1^i, 2, 1^{n-2-i}, 2]$ lies in
row $k$, its Smith remoteness is $k$ when $i \equiv n \pmod 2$ and less than $k$ when
$i \not\equiv n \pmod 2$.

Proposition 6.6 also identifies these pairs as the ones taking the most steps in the Euclidean
algorithm, a result of Hopkins and Tangboonduangjit; that half is not part of this statement.

## Sources

- Michael A. Jones and Brittany C. Ohlinger, *Self-Similar Structure of P-Positions of the Game Euclid*, The Fibonacci Quarterly 62.1 (2024), Proposition 6.6.

Stated but not proved: `MetaMathlibExt.continued_fraction_max_remoteness` is written with `theorem_wanted` in [WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GameTheory/EuclidGameCalkinWilfWanted.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html#continued-fraction-max-remoteness).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Game of Euclid](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/game-of-euclid/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GameTheory/combinatorial-games/game-of-euclid)
