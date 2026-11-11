---
declaration: section
origin: cited
lean: MetaMathlibExt.impartialGame_equiv_iff_isP_gameSum, MetaMathlibExt.isP_start_iff_of_equiv_nimHeap, MetaMathlibExt.spragueGrundyValue_eq_mex_options, MetaMathlibExt.princessRoses, MetaMathlibExt.mem_slowANimMoves_one_two, MetaMathlibExt.zero_zero_mem_princessRoses_moves_one_one, MetaMathlibExt.princessRoses_five_piles_isP_iff, MetaMathlibExt.princessRoses_two_piles_equiv_nimHeap
statement: formalized
---

# Princess and the Roses game

34 results, 15 proved and 19 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html).

## Equivalence of impartial games via their sum

Two finite impartial games $G$ and $H$ are
equivalent if and only if their sum $G + H$ is a P-position, that is, the position of $G + H$ in
which both $G$ and $H$ are at their starting positions is a P-position.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Lemma 5.

Stated but not proved: `MetaMathlibExt.impartialGame_equiv_iff_isP_gameSum` is written with `theorem_wanted` in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#impartial-game-equiv-iff-is-p-game-sum).

## P-positions are the games of Sprague–Grundy value zero

Let $G$ be a finite impartial game
and $n$ a natural number such that $G$ is equivalent to the Nim heap $*n$, that is, $G$ has
Sprague–Grundy value $n$. Then the starting position of $G$ is a P-position if and only if
$n = 0$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Theorem 6.

Stated but not proved: `MetaMathlibExt.isP_start_iff_of_equiv_nimHeap` is written with `theorem_wanted` in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#is-p-start-iff-of-equiv-nim-heap).

## Mex rule for Sprague–Grundy values

Let $G$ be a finite impartial game and $n$ a natural
number such that $G$ is equivalent to the Nim heap $*n$, that is, $G$ has Sprague–Grundy value
$n$. For a move from the start position of $G$ to a position $q$, write $G_q$ for the game $G$
started at $q$. Then no $G_q$ is equivalent to $*n$, and for every natural number $m < n$ some
$G_q$ is equivalent to $*m$. That is, the Sprague–Grundy value of $G$ is the mex of the
Sprague–Grundy values of the games $G_q$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Corollary 4.

Stated but not proved: `MetaMathlibExt.spragueGrundyValue_eq_mex_options` is written with `theorem_wanted` in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#sprague-grundy-value-eq-mex-options).

## The Princess and the Roses game

For $k \in \mathbb{N}$ and $p \in \mathbb{N}^k$, the
Princess and the Roses game (P&R) with $k$ labelled piles started at $p$ is the impartial game
whose positions are the $q \in \mathbb{N}^k$, with $q_i$ objects on pile $i$, and whose moves
remove one object from one nonempty pile, or one object from each of two distinct nonempty
piles. It is Slow$A$-Nim $\mathrm{SN}(k, \{1, 2\})$ started at $p$, and its rank is the total
number of objects $\sum_i q_i$.

Pile order is not normalized; the paper's convention of listing piles in non-increasing order
does not change the game.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Section 2.1.

Formalized by `MetaMathlibExt.princessRoses`, a definition declared in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses).

## Options in Princess and the Roses

Let $p$ and $q$ be positions of Slow$A$-Nim on $k$
stacks with $A = \{1, 2\}$, which is the Princess and the Roses game. Then $q$ is an option of
$p$ if and only if there are stacks $i \le j$ with $p_i \ge 1$ and $p_j \ge 1$ such that
$q_l = p_l - 1$ for $l \in \{i, j\}$ and $q_l = p_l$ for every other stack $l$; that is, $q$
removes one token from stack $i$ when $i = j$, and one token from each of stacks $i$ and $j$
otherwise.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Section 2.1.

Formalized by `MetaMathlibExt.mem_slowANimMoves_one_two`, a theorem declared in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#mem-slow-anim-moves-one-two).

## In two-pile Princess and the Roses, $(1, 1)$ moves to $(0, 0)$

In the Princess and the
Roses game on two piles, $(0, 0)$ is an option of the position $(1, 1)$: one may take one object
from each pile.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Section 2.1.

Formalized by `MetaMathlibExt.zero_zero_mem_princessRoses_moves_one_one`, a theorem declared in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#zero-zero-mem-princess-roses-moves-one-o).

## Lim's theorem on five-pile P&R

Let $a \ge b \ge c \ge d \ge e$ be natural numbers. The
Princess and the Roses position $(a, b, c, d, e)$ is a P-position if and only if the parities of
$a, b, c, d, e$ are, in this order, (even, even, even, even, even), (odd, odd, odd, even, even),
(even, odd, odd, odd, odd) or (odd, even, even, odd, odd).

Positions with fewer piles are the cases with trailing zero piles.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Theorem 7.

Stated but not proved: `MetaMathlibExt.princessRoses_five_piles_isP_iff` is written with `theorem_wanted` in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-five-piles-is-p-iff).

## Sprague–Grundy values of two-pile Princess and the Roses

For natural numbers $a \ge b$,
the Princess and the Roses position $(a, b)$ is equivalent to the Nim heap $*n$, that is, it has
Sprague–Grundy value $n$, where $n = 0$ if $a$ and $b$ are both even, $n = 1$ if $a$ is odd and
$b$ is even, $n = 2$ if $a$ and $b$ are both odd, and $n = 3$ if $a$ is even and $b$ is odd.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Theorem 8.

Stated but not proved: `MetaMathlibExt.princessRoses_two_piles_equiv_nimHeap` is written with `theorem_wanted` in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-two-piles-equiv-nim-heap).

## Sprague–Grundy values of three-pile Princess and the Roses

For natural numbers
$a \ge b \ge c$, the Princess and the Roses position $(a, b, c)$ is equivalent to the Nim heap
$*n$, that is, it has Sprague–Grundy value $n$, where $n = 0$ if $a$ and $b$ both have the parity
of $c$, $n = 1$ if $a$ differs from $c$ in parity and $b$ does not, $n = 2$ if $a$ and $b$ both
differ from $c$ in parity, and $n = 3$ if $b$ differs from $c$ in parity and $a$ does not.

Writing $E$ for even and $O$ for odd, the value is $0$ on $(E, E, E)$ and $(O, O, O)$, $1$ on
$(O, E, E)$ and $(E, O, O)$, $2$ on $(O, O, E)$ and $(E, E, O)$, and $3$ on $(E, O, E)$ and
$(O, E, O)$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Corollary 10.

Stated but not proved: `MetaMathlibExt.princessRoses_three_piles_equiv_nimHeap` is written with `theorem_wanted` in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-three-piles-equiv-nim-hea).

## Adding to the three largest piles of four-pile P&R

For natural numbers
$a \ge b \ge c \ge d$ and every natural number $n$, the Princess and the Roses positions
$(a, b, c, d)$ and $(a + n, b + n, c + n, d)$ are equivalent; that is, they have the same
Sprague–Grundy value.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Lemma 9.

Stated but not proved: `MetaMathlibExt.princessRoses_four_piles_equiv_add_three_largest` is written with `theorem_wanted` in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-four-piles-equiv-add-thre).

## Moves of simplified P&R

The simplified Princess and the Roses game on four sorted piles
$(a, b, c, d)$ has seven moves, given as the amounts removed from $(a, b, c, d)$: $(1, 0, 0, 0)$,
$(0, 1, 0, 0)$, $(0, 0, 0, 1)$, $(1, 1, 0, 0)$, $(1, 0, 0, 1)$, $(0, 1, 0, 1)$ and $(0, 0, 1, 1)$.

These are the moves of four-pile Princess and the Roses except taking one object from the third
pile alone or together with the first or second pile, so the third pile may be taken from only
together with the fourth.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Section 3.1.

Formalized by `MetaMathlibExt.simplifiedPrincessRosesMoveList`, a definition declared in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#simplified-princess-roses-move-list).

## Options in simplified Princess and the Roses

The seven simplified Princess and the Roses
moves are the removal vectors $(1, 0, 0, 0)$, $(0, 1, 0, 0)$, $(0, 0, 0, 1)$, $(1, 1, 0, 0)$,
$(1, 0, 0, 1)$, $(0, 1, 0, 1)$ and $(0, 0, 1, 1)$. For a quadruple $(a, b, c, d)$ of natural
numbers, its options are the quadruples $(a - r_1, b - r_2, c - r_3, d - r_4)$ for those moves
$(r_1, r_2, r_3, r_4)$ with $r_1 \le a$, $r_2 \le b$, $r_3 \le c$ and $r_4 \le d$ whose result is
in non-increasing order: $a - r_1 \ge b - r_2 \ge c - r_3 \ge d - r_4$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Sections 2.2 and 3.1.

Formalized by `MetaMathlibExt.simplifiedPrincessRosesMoves`, a definition declared in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#simplified-princess-roses-moves).

## Characterization of simplified P&R options

For natural numbers $a, b, c, d$ and
$a', b', c', d'$, the position $[a', b', c', d']$ is an option of the simplified P&R position
$[a, b, c, d]$ if and only if $a' \le a$, $b' \le b$, $c' \le c$, $d' \le d$,
$a' \ge b' \ge c' \ge d'$, and the amounts removed $(a - a', b - b', c - c', d - d')$ form one of
the seven simplified P&R moves $(1, 0, 0, 0)$, $(0, 1, 0, 0)$, $(0, 0, 0, 1)$, $(1, 1, 0, 0)$,
$(1, 0, 0, 1)$, $(0, 1, 0, 1)$ and $(0, 0, 1, 1)$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Sections 2.2 and 3.1.

Formalized by `MetaMathlibExt.mem_simplifiedPrincessRosesMoves`, a theorem declared in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#mem-simplified-princess-roses-moves).

## Simplified P&R moves decrease the number of objects

For all quadruples $(a, b, c, d)$
and $(a', b', c', d')$ of natural numbers, if $(a', b', c', d')$ is an option of $(a, b, c, d)$
in simplified Princess and the Roses, then $a' + b' + c' + d' < a + b + c + d$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Section 3.1.

Formalized by `MetaMathlibExt.simplifiedPrincessRosesMoves_rank_lt`, a theorem declared in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#simplified-princess-roses-moves-rank-lt).

## A terminal position of simplified P&R

In simplified Princess and the Roses, the
position $(3, 3, 3, 0)$ has no options.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Section 3.1.

Formalized by `MetaMathlibExt.simplifiedPrincessRosesMoves_three_three_three_zero`, a theorem declared in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#simplified-princess-roses-moves-three-th).

## Simplified Princess and the Roses

For a quadruple $p$ of natural numbers, simplified
Princess and the Roses started at $p$ is the impartial game whose positions are all quadruples
$(a, b, c, d)$ of natural numbers, whose options from a position are its simplified Princess and
the Roses options (the results of the seven simplified moves that take no pile below zero and
leave the piles in non-increasing order), whose rank is the total number of objects
$a + b + c + d$, and whose start position is $p$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Section 3.1.

Formalized by `MetaMathlibExt.simplifiedPrincessRoses`, a definition declared in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#simplified-princess-roses).

## Four-pile P&R is equivalent to simplified P&R

For natural numbers $a \ge b \ge c \ge d$
and every natural number $n$, the Princess and the Roses position $(a, b, c, d)$ is equivalent to
the simplified P&R position $[a + n, b + n, c + n, d]$; that is, the two have the same
Sprague–Grundy value.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Lemma 11.

Stated but not proved: `MetaMathlibExt.princessRoses_equiv_simplifiedPrincessRoses` is written with `theorem_wanted` in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-equiv-simplified-princess).

## Moves of P&R Helper

The list of the seven moves of P&R Helper on a position $[x, y, z]$,
each given as the triple of amounts removed from $(x, y, z)$: in order, $(1, 1, 1)$, $(1, 0, 0)$,
$(1, 2, 1)$, $(1, 1, 2)$, $(0, 1, 0)$, $(0, 1, 1)$ and $(0, 0, 1)$. As changes to the position
these are $(-1, -1, -1)$, $(-1, 0, 0)$, $(-1, -2, -1)$, $(-1, -1, -2)$, $(0, -1, 0)$,
$(0, -1, -1)$ and $(0, 0, -1)$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Section 3.1.

Formalized by `MetaMathlibExt.princessRosesHelperMoveList`, a definition declared in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-helper-move-list).

## Options in P&R Helper

The P&R Helper game is played on triples of natural numbers with
the seven moves that subtract $(1, 1, 1)$, $(1, 0, 0)$, $(1, 2, 1)$, $(1, 1, 2)$, $(0, 1, 0)$,
$(0, 1, 1)$ or $(0, 0, 1)$. The options of a position $(x, y, z)$ are the triples
$(x - u, y - v, z - w)$ for those moves $(u, v, w)$ with $u \le x$, $v \le y$, $w \le z$ and
$x - u \le y - v \le z - w$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Section 3.1.

Formalized by `MetaMathlibExt.princessRosesHelperMoves`, a definition declared in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-helper-moves).

## Characterization of P&R Helper options

For natural numbers $x, y, z, x', y', z'$, the
position $[x', y', z']$ is an option of the P&R Helper position $[x, y, z]$ if and only if
$x' \le x$, $y' \le y$, $z' \le z$, $x' \le y' \le z'$, and the amounts removed
$(x - x', y - y', z - z')$ form one of the seven P&R Helper moves $(1, 1, 1)$, $(1, 0, 0)$,
$(1, 2, 1)$, $(1, 1, 2)$, $(0, 1, 0)$, $(0, 1, 1)$ and $(0, 0, 1)$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Section 3.1.

Formalized by `MetaMathlibExt.mem_princessRosesHelperMoves`, a theorem declared in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#mem-princess-roses-helper-moves).

## P&R Helper moves decrease the coordinate sum

For all triples $(x, y, z)$ and
$(x', y', z')$ of natural numbers, if $(x', y', z')$ is an option of $(x, y, z)$ in the P&R Helper
game, then $x' + y' + z' < x + y + z$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Section 3.1.

Formalized by `MetaMathlibExt.princessRosesHelperMoves_rank_lt`, a theorem declared in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-helper-moves-rank-lt).

## Small P&R Helper positions

In the P&R Helper game, the position $(0, 0, 0)$ has no
options, and the options of $(1, 1, 1)$ are exactly $(0, 0, 0)$ and $(0, 1, 1)$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Section 3.1.

Formalized by `MetaMathlibExt.princessRosesHelperMoves_small`, a theorem declared in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-helper-moves-small).

## The P&R Helper game

For a triple $p$ of natural numbers, P&R Helper started at $p$ is
the impartial game whose positions are the triples $(x, y, z)$ of natural numbers, whose options
from $(x, y, z)$ are the triples $(x - u, y - v, z - w)$ for $(u, v, w)$ among $(1, 1, 1)$,
$(1, 0, 0)$, $(1, 2, 1)$, $(1, 1, 2)$, $(0, 1, 0)$, $(0, 1, 1)$ and $(0, 0, 1)$ with $u \le x$,
$v \le y$, $w \le z$ and $x - u \le y - v \le z - w$, whose rank is $x + y + z$, and which
starts at $p$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Section 3.1.

Formalized by `MetaMathlibExt.princessRosesHelper`, a definition declared in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-helper).

## Four-pile P&R reduces to P&R Helper

For natural numbers $a \ge b \ge c \ge d$, the
Princess and the Roses position $(a, b, c, d)$ is equivalent to the P&R Helper position
$[d, b - c + d, a - c + d]$; that is, the two have the same Sprague–Grundy value.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Theorem 12.

Stated but not proved: `MetaMathlibExt.princessRoses_equiv_princessRosesHelper` is written with `theorem_wanted` in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-equiv-princess-roses-help).

## P&R Helper positions of Sprague–Grundy value 0

For natural numbers $x \le y \le z$,
the P&R Helper game started at $[x, y, z]$ is equivalent to the Nim heap of size $0$ (that is,
has Sprague–Grundy value $0$) if and only if $x$, $y$ and $z$ are all even.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Theorem 13, first bullet.

Stated but not proved: `MetaMathlibExt.princessRosesHelper_equiv_nimHeap_zero_iff` is written with `theorem_wanted` in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-helper-equiv-nim-heap-zer).

## P&R Helper positions of Sprague–Grundy value 1 on regions U and R

For natural numbers
$x \le y \le z$ with $z < x + y$ (the union of the regions $U$ and $R$), the P&R Helper game
started at $[x, y, z]$ is equivalent to the Nim heap of size $1$ (that is, has Sprague–Grundy
value $1$) if and only if one of the following holds: $(x, y, z) = (1, 1, 1)$; or $y = x$,
$z = x$ and $x \equiv 3 \pmod 4$; or $y = x$, $z = x + 1$, $x \equiv 1 \pmod 4$ and $x \ne 1$;
or $y = x + 1$, $z = x + 1$, $x \equiv 0 \pmod 4$ and $x \ne 0$; or $y + z - x \equiv 1 \pmod 4$
and $z > x + 1$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Theorem 13, value `1` on `U ∪ R`.

Stated but not proved: `MetaMathlibExt.princessRosesHelper_equiv_nimHeap_one_iff_of_lt_add` is written with `theorem_wanted` in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-helper-equiv-nim-heap-one).

## P&R Helper positions of Sprague–Grundy value 2 on region U

For natural numbers
$x \le y \le z$ with $z < x + y$ and $y \le 2x + 1$ (the region $U$), write $s = y + z - x$. The
P&R Helper game started at $[x, y, z]$ is equivalent to the Nim heap of size $2$ (that is, has
Sprague–Grundy value $2$) if and only if one of the following holds:
(a) $y = x$, $z = x$, $x \equiv 1 \pmod 4$ and $x \ne 1$;
(b) $y = x$, $z = x + 1$ and $x \equiv 3 \pmod 4$;
(c) $y = x + 1$, $z = x + 1$, $x \equiv 2 \pmod 4$ and $x \ne 2$;
(d) $y = x$, $z = x + 2$, $x \equiv 1 \pmod 4$ and $x \ne 1$;
(e) $y = x + 1$, $z = x + 2$, $x \equiv 0 \pmod 4$ and $x \ne 0$;
(f) $y = x + 2$, $z = x + 2$ and $x \equiv 3 \pmod 4$;
(g) $s \equiv 7 \pmod 8$, and either $z > x + 4$ and $y = x$, or $z > x + 5$ and $y = x + 1$,
or $z > x + 2$ and $z = x + y - 1$;
(h) $s \equiv 4 \pmod 8$, $y = x$, $x$ is odd and $z > x + 4$;
(i) $s \equiv 2 \pmod 4$, $x$, $y$, $z$ are not all even, $z > x + 2$, it is not the case that
$s \equiv 6 \pmod 8$, $z > x + 4$ and $y \le x + 1$, and it is not the case that
$s \equiv 6 \pmod 8$ and $z = x + y - 2$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Theorem 13, value `2` on `U`.

Stated but not proved: `MetaMathlibExt.princessRosesHelper_equiv_nimHeap_two_iff_of_mem_U` is written with `theorem_wanted` in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-helper-equiv-nim-heap-two).

## P&R Helper positions of Sprague–Grundy value 3 on region U

For natural numbers
$x \le y \le z$ with $z < x + y$ and $y \le 2x + 1$ (the region $U$), write $s = y + z - x$. The
P&R Helper game started at $[x, y, z]$ is equivalent to the Nim heap of size $3$ (that is, has
Sprague–Grundy value $3$) if and only if one of the following holds:
(a) $(x, y, z)$ is one of $(1, 2, 2)$, $(2, 2, 3)$, $(5, 6, 6)$, $(6, 6, 7)$, $(3, 4, 5)$,
$(5, 5, 8)$;
(b) $y = x$, $z = x + 1$, $x \equiv 0 \pmod 4$ and $x \notin \{0, 4\}$;
(c) $y = x + 1$, $z = x + 1$, $x \equiv 3 \pmod 4$ and $x \notin \{3, 7\}$;
(d) $y = x + 1$, $z = x + 2$, $x \equiv 1 \pmod 4$ and $x \notin \{1, 5\}$;
(e) $s \equiv 0 \pmod 8$, $y = x$, $x$ is odd and $z > x + 5$;
(f) $s \equiv 6 \pmod 8$, $x$, $y$, $z$ are not all even, and either $z > x + 4$ and
$y \le x + 1$, or $z > x + 2$ and $z = x + y - 2$;
(g) $s \equiv 3 \pmod 4$, $z > x + 2$, it is not the case that $s \equiv 7 \pmod 8$,
$z > x + 4$ and $y \le x + 2$, and it is not the case that $s \equiv 7 \pmod 8$, $y \le 2x$
and $x + y - z \le 3$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Theorem 13, value `3` on `U`.

Stated but not proved: `MetaMathlibExt.princessRosesHelper_equiv_nimHeap_three_iff_of_mem_U` is written with `theorem_wanted` in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 410](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-helper-equiv-nim-heap-thr).

## P&R Helper positions of Sprague–Grundy value 4 on region U

For natural numbers
$x \le y \le z$ with $z < x + y$ and $y \le 2x + 1$ (the region $U$), write $s = y + z - x$. The
P&R Helper game started at $[x, y, z]$ is equivalent to the Nim heap of size $4$ (that is, has
Sprague–Grundy value $4$) if and only if one of the following holds:
(a) $(x, y, z)$ is one of $(2, 3, 3)$, $(5, 6, 7)$, $(4, 4, 5)$, $(7, 8, 8)$;
(b) $y = x$, $z = x + 1$, $x \equiv 2 \pmod 4$ and $x \notin \{2, 6\}$;
(c) $y = x + 1$, $z = x + 1$, $x \equiv 1 \pmod 4$ and $x \notin \{1, 5\}$;
(d) $y = x + 1$, $z = x + 2$, $x \equiv 3 \pmod 4$ and $x \notin \{3, 7\}$;
(e) $y = x + 1$, $z = x + 5$ and $x \equiv 1 \pmod 8$;
(f) $s \equiv 0 \pmod 4$, $x$, $y$, $z$ are not all even, $z > x + 2$, and none of the
following holds: $(x, y, z) = (5, 5, 8)$; $z > x + 4$, $s \equiv 4 \pmod 8$ and $y = x$;
$z > x + 5$, $s \equiv 0 \pmod 8$ and $y = x$; $y = x + 1$, $z = x + 3$, $x \equiv 0 \pmod 4$
and $x \notin \{0, 4, 8\}$; $y = x + 2$, $z = x + 3$, $x \equiv 3 \pmod 4$ and
$x \notin \{3, 7\}$; $y = x + 1$, $z = x + 5$ and $x \equiv 2 \pmod 8$; $y = x + 2$,
$z = x + 5$ and $x \equiv 1 \pmod 8$; $y = x + 1$, $z = x + 6$ and $x \equiv 1 \pmod 8$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Theorem 13, value `4` on `U`.

Stated but not proved: `MetaMathlibExt.princessRosesHelper_equiv_nimHeap_four_iff_of_mem_U` is written with `theorem_wanted` in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-helper-equiv-nim-heap-fou).

## Sprague–Grundy value $5$ of P&R Helper on region $U$

Let $x \le y \le z$ be natural
numbers with $z < x + y$ and $y \le 2x + 1$ (the region $U$). The P&R Helper position $[x, y, z]$
is equivalent to the Nim heap $*5$, that is, has Sprague–Grundy value $5$, if and only if one of
the following holds:
- $[x, y, z]$ is $[3, 4, 4]$ or $[7, 8, 9]$;
- $y = x + 1$, $z = x + 3$, $x \equiv 0 \pmod 4$ and $x \notin \{0, 4, 8\}$;
- $y = x + 2$, $z = x + 3$, $x \equiv 3 \pmod 4$ and $x \notin \{3, 7\}$;
- $y = x + 1$, $z = x + 5$ and $x \equiv 2 \pmod 8$;
- $y = x + 1$, $z = x + 6$ and $x \equiv 1 \pmod 8$;
- $y + z - x \equiv 7 \pmod 8$, $y = x + 2$, $z > x + 4$ and $x + y - z > 2$;
- $y + z - x \equiv 7 \pmod 8$, $z = x + y - 3$ and $x + 2 < y \le 2x$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Theorem 13, value `5` on `U`.

Stated but not proved: `MetaMathlibExt.princessRosesHelper_equiv_nimHeap_five_iff_of_mem_U` is written with `theorem_wanted` in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-helper-equiv-nim-heap-fiv).

## P&R Helper positions of Sprague–Grundy value 6 or 7 on region U

For natural numbers
$x \le y \le z$ with $z < x + y$ and $y \le 2x + 1$ (the region $U$), the P&R Helper game started
at $[x, y, z]$ is equivalent to the Nim heap of size $6$ (that is, has Sprague–Grundy value $6$)
if and only if $y = x + 2$, $z = x + 5$ and $x \equiv 1 \pmod 8$; and it is never equivalent to
the Nim heap of size $7$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Theorem 13, values `6` and `7` on `U`.

Stated but not proved: `MetaMathlibExt.princessRosesHelper_equiv_nimHeap_six_iff_of_mem_U` is written with `theorem_wanted` in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 469](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-helper-equiv-nim-heap-six).

## Sprague–Grundy values of P&R Helper on region R

Let $x \le y \le z$ be natural numbers
with $z < x + y$ and $y > 2x + 1$ (the region $R$), and write $s = y + z - x$. For every natural
number $n$, the P&R Helper game started at $[x, y, z]$ is equivalent to the Nim heap of size $n$
(that is, has Sprague–Grundy value $n$) if and only if one of the following holds: $n = 0$ and
$x$, $y$, $z$ are all even; $n = 1$ and $s \equiv 1 \pmod 4$; $n = 2$, $x$ is even and $y$, $z$
are odd; $n = 3$ and $s \equiv 3 \pmod 4$; $n = 4$, $x$ is odd and $s \equiv 0 \pmod 4$;
$n = 5$, $x$ is odd and $s \equiv 2 \pmod 4$.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Theorem 13, region `R`.

Stated but not proved: `MetaMathlibExt.princessRosesHelper_equiv_nimHeap_iff_of_mem_R` is written with `theorem_wanted` in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 482](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L482). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-helper-equiv-nim-heap-iff).

## Sprague–Grundy values of P&R Helper on region L

Let $x \le y \le z$ be natural numbers
with $z \ge x + y$ and $y \le 2x$ (the region $L$). For every natural number $n$, the P&R Helper
game started at $[x, y, z]$ is equivalent to the Nim heap of size $n$ (that is, has
Sprague–Grundy value $n$) if and only if one of the following holds: $n = 0$ and $x$, $y$, $z$
are all even; $n = 1$, $x$ and $y$ are even and $z$ is odd; $n = 2$ and
$y + 2z - 2x \equiv 3 \pmod 4$; $n = 3$ and $y + 2z - 2x \equiv 1 \pmod 4$; $n = 4$, $x$ and $z$
are odd and $y$ is even; $n = 5$, $x$ is odd and $y$ and $z$ are even.

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Theorem 13, region `L`.

Stated but not proved: `MetaMathlibExt.princessRosesHelper_equiv_nimHeap_iff_of_mem_L` is written with `theorem_wanted` in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 498](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L498). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-helper-equiv-nim-heap-iff-2).

## Sprague–Grundy values of P&R Helper on region D

Let $x \le y \le z$ be natural numbers
with $z \ge x + y$ and $y > 2x$ (the region $D$). For every natural number $n$, the P&R Helper
game started at $[x, y, z]$ is equivalent to the Nim heap of size $n$ (that is, has
Sprague–Grundy value $n$) if and only if $n$ is the number assigned to the parities of
$(x, y, z)$ as follows: $0$ to (even, even, even), $1$ to (even, even, odd), $2$ to
(even, odd, odd), $3$ to (even, odd, even), $4$ to (odd, even, odd), $5$ to (odd, even, even),
$6$ to (odd, odd, even) and $7$ to (odd, odd, odd).

## Sources

- Zev Friedman, *Sprague-Grundy Values for 4-Pile Princess and the Roses*, INTEGERS 26 (2026), Article G4, Theorem 13, region `D`.

Stated but not proved: `MetaMathlibExt.princessRosesHelper_equiv_nimHeap_iff_of_mem_D` is written with `theorem_wanted` in [WantedExt/GameTheory/PrincessAndRosesWanted.lean, line 514](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PrincessAndRosesWanted.lean#L514). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html#princess-roses-helper-equiv-nim-heap-iff-3).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Princess and the Roses game](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GameTheory/combinatorial-games/princess-and-the-roses-game)
