---
declaration: section
origin: cited
lean: MetaMathlibExt.wythoffExtraMoveGrundy, MetaMathlibExt.wythoffPassGrundy, MetaMathlibExt.wythoffPlusStoneGrundy, MetaMathlibExt.wythoffPassSetA, MetaMathlibExt.wythoffPassSetB, MetaMathlibExt.wythoffPassSetC, MetaMathlibExt.wythoffExtraMoveGrundy_eq, MetaMathlibExt.wythoffPassGrundy_zero_zero
statement: formalized
---

# Wythoff's game

62 results, 35 proved and 27 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html).

## Grundy numbers of Wythoff's game with an extra move

Positions are triples $(x, y, p)$
with $x, y \in \mathbb{N}$ and $p \in \{0, 1\}$. A move from $(x, y, p)$ goes to $(u, y, p)$ with
$u < x$, to $(x, v, p)$ with $v < y$, or to $(x - t, y - t, p)$ with $1 \le t \le \min(x, y)$
(the moves of a Queen in Wythoff's game), or, when $p = 1$, it is an extra move to $(x, y, 0)$.
There are two variants. In the strict variant the extra move is the one-time pass of Wythoff's
game with a pass and is not allowed at the terminal position, that is, it requires $x + y > 0$;
in the non-strict variant it is the move in an added pile of one stone and is always allowed
when $p = 1$. In each variant, the Grundy number of $(x, y, p)$ is the mex (least natural number
not attained) of the Grundy numbers of the positions reachable in one move. With $p = 0$ both
variants are classical Wythoff's game.

## Sources

- Ryohei Miyadera, Hikaru Manabe, and Masanori Fukui, *Wythoff's Game with a Pass*, INTEGERS 25 (2025), Article G4, Section 3 (the move sets `M₁, M₂, M₃, M₄, M₄'` and the Grundy numbers `𝒢₁`, `𝒢₂`).

Formalized by `MetaMathlibExt.wythoffExtraMoveGrundy`, a definition declared in [WantedExt/Combinatorics/WythoffPassWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffPassWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-extra-move-grundy).

## Grundy numbers of Wythoff's game with a pass

Wythoff's game with a pass has positions
$(x, y, p)$ with $x, y \in \mathbb{N}$ and $p \in \{0, 1\}$, where $p = 1$ means the one-time pass
is still available. A move goes from $(x, y, p)$ to $(u, y, p)$ with $u < x$, to $(x, v, p)$
with $v < y$, or to $(x - t, y - t, p)$ with $1 \le t \le \min(x, y)$, or, when $p = 1$ and
$x + y > 0$, it is the pass to $(x, y, 0)$. $\mathcal{G}_1(x, y, p)$ is the Grundy number of
$(x, y, p)$ in this game, that is, the strict variant of the Grundy numbers of Wythoff's game
with an extra move.

## Sources

- Ryohei Miyadera, Hikaru Manabe, and Masanori Fukui, *Wythoff's Game with a Pass*, INTEGERS 25 (2025), Article G4, Section 3 (Grundy numbers `𝒢₁`).

Formalized by `MetaMathlibExt.wythoffPassGrundy`, an abbreviation declared in [WantedExt/Combinatorics/WythoffPassWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffPassWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-pass-grundy).

## Grundy numbers of Wythoff's game plus one stone

For natural numbers $x, y$ and
$p \in \{0, 1\}$, $\mathcal{G}_2(x, y, p)$ is the Grundy number of the position $(x, y, p)$ in the
sum of Wythoff's game on $(x, y)$ and a pile of $p$ stones. That is, it is the Grundy function of
Wythoff's game with the extra move from $(x, y, 1)$ to $(x, y, 0)$ always available, including at
$(0, 0, 1)$.

## Sources

- Ryohei Miyadera, Hikaru Manabe, and Masanori Fukui, *Wythoff's Game with a Pass*, INTEGERS 25 (2025), Article G4, Section 3 (Grundy numbers `𝒢₂`).

Formalized by `MetaMathlibExt.wythoffPlusStoneGrundy`, an abbreviation declared in [WantedExt/Combinatorics/WythoffPassWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffPassWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-plus-stone-grundy).

## The set $A$

$A$ is the finite set of pairs of natural numbers
$A = \{(0, 0), (1, 2), (2, 1), (3, 5), (4, 7), (5, 3), (7, 4)\}$. These are the positions
$(x, y, 0)$ of the set $A$ in the source, with the third coordinate dropped.

## Sources

- Ryohei Miyadera, Hikaru Manabe, and Masanori Fukui, *Wythoff's Game with a Pass*, INTEGERS 25 (2025), Article G4, Section 4 (the set `A`, Definition 12).

Formalized by `MetaMathlibExt.wythoffPassSetA`, a definition declared in [WantedExt/Combinatorics/WythoffPassWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffPassWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-pass-set-a).

## The set $B$

$B$ is the finite set of pairs of natural numbers
$B = \{(0, 0), (1, 3), (3, 1), (2, 5), (5, 2), (4, 8), (8, 4), (6, 7), (7, 6)\}$. These are the
positions $(x, y, 1)$ of the set $B$ in the source, with the third coordinate dropped.

## Sources

- Ryohei Miyadera, Hikaru Manabe, and Masanori Fukui, *Wythoff's Game with a Pass*, INTEGERS 25 (2025), Article G4, Section 4 (the set `B`).

Formalized by `MetaMathlibExt.wythoffPassSetB`, a definition declared in [WantedExt/Combinatorics/WythoffPassWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffPassWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-pass-set-b).

## The set $C$

$C$ is the finite set of pairs of natural numbers
$C = \{(0, 1), (1, 0), (2, 2), (3, 6), (6, 3), (4, 8), (8, 4), (5, 7), (7, 5)\}$. These are the
positions $(x, y, 1)$ of the set $C$ in the source, with the third coordinate dropped.

## Sources

- Ryohei Miyadera, Hikaru Manabe, and Masanori Fukui, *Wythoff's Game with a Pass*, INTEGERS 25 (2025), Article G4, Section 4 (the set `C`).

Formalized by `MetaMathlibExt.wythoffPassSetC`, a definition declared in [WantedExt/Combinatorics/WythoffPassWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffPassWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-pass-set-c).

## Mex recursion for the Grundy numbers of Wythoff's game with an extra move

In both
variants (strict: the pass of Wythoff's game with a pass; non-strict: a pile of one stone), the
Grundy number of a position $(x, y, p)$ with $x, y \in \mathbb{N}$ and $p \in \{0, 1\}$ is the
least natural number $m$ that differs from the Grundy number of $(u, y, p)$ for every $u < x$,
from that of $(x, v, p)$ for every $v < y$, and from that of $(x - t, y - t, p)$ for every $t$
with $1 \le t \le x$ and $t \le y$, and that, when $p = 1$ and either the variant is non-strict
or $x + y > 0$, also differs from the Grundy number of $(x, y, 0)$.

## Sources

- Ryohei Miyadera, Hikaru Manabe, and Masanori Fukui, *Wythoff's Game with a Pass*, INTEGERS 25 (2025), Article G4, Section 1 (Grundy numbers as mex over moves).

Formalized by `MetaMathlibExt.wythoffExtraMoveGrundy_eq`, a theorem declared in [WantedExt/Combinatorics/WythoffPassWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffPassWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-extra-move-grundy-eq).

## The terminal position of Wythoff's game with a pass

Let $\mathcal{G}_1(x, y, p)$ be the
Grundy numbers of Wythoff's game with a pass, where $p = 1$ means the pass is still available.
Then $\mathcal{G}_1(0, 0, p) = 0$ for both $p = 0$ and $p = 1$: the terminal position $(0, 0)$
has Grundy number $0$ with or without the pass available, since the pass is not allowed from a
terminal position.

## Sources

- Ryohei Miyadera, Hikaru Manabe, and Masanori Fukui, *Wythoff's Game with a Pass*, INTEGERS 25 (2025), Article G4, Section 3 (`M₄(x, y, p) = ∅` if `x + y = 0`).

Formalized by `MetaMathlibExt.wythoffPassGrundy_zero_zero`, a theorem declared in [WantedExt/Combinatorics/WythoffPassWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffPassWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-pass-grundy-zero-zero).

## Wythoff's game plus one stone at $(0, 0, 1)$

In the sum of Wythoff's game and a pile of
one stone, the position $(0, 0, 1)$ (no Wythoff moves left, the stone present) has Grundy number
$\mathcal{G}_2(0, 0, 1) = 1$: its only move is to the terminal position $(0, 0, 0)$.

## Sources

- Ryohei Miyadera, Hikaru Manabe, and Masanori Fukui, *Wythoff's Game with a Pass*, INTEGERS 25 (2025), Article G4, Section 3 (`M₄'(x, y, 1) = {(x, y, 0)}`).

Formalized by `MetaMathlibExt.wythoffPlusStoneGrundy_zero_zero_true`, a theorem declared in [WantedExt/Combinatorics/WythoffPassWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffPassWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-plus-stone-grundy-zero-zero-true).

## The sets $B$ and $C$ have nine elements each

The sets
$B = \{(0, 0), (1, 3), (3, 1), (2, 5), (5, 2), (4, 8), (8, 4), (6, 7), (7, 6)\}$ and
$C = \{(0, 1), (1, 0), (2, 2), (3, 6), (6, 3), (4, 8), (8, 4), (5, 7), (7, 5)\}$ of pairs of
natural numbers each have exactly $9$ elements.

## Sources

- Ryohei Miyadera, Hikaru Manabe, and Masanori Fukui, *Wythoff's Game with a Pass*, INTEGERS 25 (2025), Article G4, Section 4.

Formalized by `MetaMathlibExt.wythoffPassSetB_card_wythoffPassSetC_card`, a theorem declared in [WantedExt/Combinatorics/WythoffPassWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffPassWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-pass-set-b-card-wythoff-pass-set).

## The set $A$ has seven elements

The set
$A = \{(0, 0), (1, 2), (2, 1), (3, 5), (4, 7), (5, 3), (7, 4)\}$ of pairs of natural numbers has
exactly $7$ elements.

## Sources

- Ryohei Miyadera, Hikaru Manabe, and Masanori Fukui, *Wythoff's Game with a Pass*, INTEGERS 25 (2025), Article G4, Section 4.

Formalized by `MetaMathlibExt.wythoffPassSetA_card`, a theorem declared in [WantedExt/Combinatorics/WythoffPassWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffPassWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-pass-set-a-card).

## Wythoff's theorem

Let $\mathcal{G}_1(x, y, 0)$ be the Grundy number of the position
$(x, y, 0)$ of Wythoff's game with a pass, in which the pass has been used; this is the Grundy
number of $(x, y)$ in classical Wythoff's game. Then $\mathcal{G}_1(x, y, 0) = 0$ (that is,
$(x, y)$ is a P-position) if and only if there is $n \in \mathbb{N}$ with
$(x, y) = (\lfloor n\varphi \rfloor, \lfloor n\varphi \rfloor + n)$ or
$(x, y) = (\lfloor n\varphi \rfloor + n, \lfloor n\varphi \rfloor)$, where
$\varphi = (1 + \sqrt{5})/2$ is the golden ratio.

## Sources

- Ryohei Miyadera, Hikaru Manabe, and Masanori Fukui, *Wythoff's Game with a Pass*, INTEGERS 25 (2025), Article G4, Theorem 2, quoting Wythoff.

Stated but not proved: `MetaMathlibExt.wythoffGrundy_eq_zero_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffPassWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffPassWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-grundy-eq-zero-iff).

## Grundy-one positions of Wythoff's game lie near P-positions

Let
$\mathcal{G}_1(x, y, 0)$ be the Grundy number of the position $(x, y, 0)$ of Wythoff's game with
a pass, in which the pass has been used; this is the Grundy number of $(x, y)$ in classical
Wythoff's game. If $\mathcal{G}_1(x, y, 0) = 1$, then there are $v, w \in \mathbb{N}$ with
$\mathcal{G}_1(v, w, 0) = 0$ and $(x - v)^2 + (y - w)^2 \le 20$: every position with Grundy
number $1$ lies within Euclidean distance $\sqrt{20}$ of a P-position.

## Sources

- Ryohei Miyadera, Hikaru Manabe, and Masanori Fukui, *Wythoff's Game with a Pass*, INTEGERS 25 (2025), Article G4, Corollary 1.

Stated but not proved: `MetaMathlibExt.wythoffGrundy_one_near_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffPassWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffPassWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-grundy-one-near-zero).

## P-positions of Wythoff's game with a pass for $x, y \le 8$

Let $\mathcal{G}_1(x, y, p)$ be
the Grundy number of Wythoff's game with a one-time pass ($p = 1$: the pass is still available;
$p = 0$: classical Wythoff's game), and $\mathcal{G}_2(x, y, p)$ the Grundy number of the sum of
Wythoff's game and a pile of $p$ stones. Let
$A = \{(0, 0), (1, 2), (2, 1), (3, 5), (5, 3), (4, 7), (7, 4)\}$,
$B = \{(0, 0), (1, 3), (3, 1), (2, 5), (5, 2), (4, 8), (8, 4), (6, 7), (7, 6)\}$ and
$C = \{(0, 1), (1, 0), (2, 2), (3, 6), (6, 3), (4, 8), (8, 4), (5, 7), (7, 5)\}$. Then for all
natural numbers $x \le 8$ and $y \le 8$: $\mathcal{G}_1(x, y, 0) = 0$ if and only if
$(x, y) \in A$; $\mathcal{G}_1(x, y, 1) = 0$ if and only if $(x, y) \in B$; and
$\mathcal{G}_2(x, y, 1) = 0$ if and only if $(x, y) \in C$.

## Sources

- Ryohei Miyadera, Hikaru Manabe, and Masanori Fukui, *Wythoff's Game with a Pass*, INTEGERS 25 (2025), Article G4, Lemma 1.

Stated but not proved: `MetaMathlibExt.wythoffPass_pPositions_le_eight` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffPassWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffPassWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-pass-p-positions-le-eight).

## Moves into the sets $B$ and $C$ away from the corner

Let
$B = \{(0, 0), (1, 3), (3, 1), (2, 5), (5, 2), (4, 8), (8, 4), (6, 7), (7, 6)\}$ and
$C = \{(0, 1), (1, 0), (2, 2), (3, 6), (6, 3), (4, 8), (8, 4), (5, 7), (7, 5)\}$. For natural
numbers $x, y$, call the pairs $(u, y)$ with $u < x$ the horizontal moves from $(x, y)$, the
pairs $(x, v)$ with $v < y$ its vertical moves, and the pairs $(x - t, y - t)$ with
$1 \le t \le \min(x, y)$ its diagonal moves. Suppose that $x \ge 9$ or $y \ge 9$. Then (i) if
$y \le 8$, some horizontal move lies in $B$ and some horizontal move lies in $C$, while no
vertical move lies in $B$ or in $C$; (ii) if $x \le 8$, some vertical move lies in $B$ and some
vertical move lies in $C$, while no horizontal move lies in $B$ or in $C$; (iii) if
$x \le y + 4$ and $y \le x + 4$, some diagonal move lies in $B$ and some diagonal move lies in
$C$; (iv) if $x \ge y + 5$ or $y \ge x + 5$, no diagonal move lies in $B$ or in $C$.

In the source these are the moves from the position $(x, y, 1)$ of Wythoff's game with a pass,
with the third coordinate dropped.

## Sources

- Ryohei Miyadera, Hikaru Manabe, and Masanori Fukui, *Wythoff's Game with a Pass*, INTEGERS 25 (2025), Article G4, Lemma 2.

Stated but not proved: `MetaMathlibExt.wythoffPass_moves_meet_setB_setC` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffPassWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffPassWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-pass-moves-meet-set-b-set-c).

## Moves from a large position meet $B$ exactly when they meet $C$

Let
$B = \{(0, 0), (1, 3), (3, 1), (2, 5), (5, 2), (4, 8), (8, 4), (6, 7), (7, 6)\}$ and
$C = \{(0, 1), (1, 0), (2, 2), (3, 6), (6, 3), (4, 8), (8, 4), (5, 7), (7, 5)\}$. Let $x, y$ be
natural numbers with $x \ge 9$ or $y \ge 9$. Then some pair $(u, y)$ with $u < x$ lies in $B$ if
and only if some such pair lies in $C$; some pair $(x, v)$ with $v < y$ lies in $B$ if and only
if some such pair lies in $C$; and some pair $(x - t, y - t)$ with $1 \le t \le \min(x, y)$ lies
in $B$ if and only if some such pair lies in $C$.

In the source these pairs are the horizontal, vertical and diagonal moves from the position
$(x, y, 1)$ of Wythoff's game with a pass, with the third coordinate dropped.

## Sources

- Ryohei Miyadera, Hikaru Manabe, and Masanori Fukui, *Wythoff's Game with a Pass*, INTEGERS 25 (2025), Article G4, Lemma 3.

Stated but not proved: `MetaMathlibExt.wythoffPass_moves_meet_setB_iff_setC` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffPassWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffPassWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-pass-moves-meet-set-b-iff-set-c).

## Pass versus a pile of one stone in Wythoff's game

Let $\mathcal{G}_1(x, y, p)$ be the
Grundy numbers of Wythoff's game with a pass, where $p = 1$ means the pass is still available,
and let $\mathcal{G}_2(x, y, p)$ be the Grundy numbers of the sum of Wythoff's game and a pile of
$p \in \{0, 1\}$ stones. If $x \ge 9$ or $y \ge 9$, then $\mathcal{G}_1(x, y, 1) = 0$ if and only
if $\mathcal{G}_2(x, y, 1) = 0$: away from the $9 \times 9$ corner, Wythoff's game with an
available pass has the same P-positions as Wythoff's game plus a pile of one stone.

## Sources

- Ryohei Miyadera, Hikaru Manabe, and Masanori Fukui, *Wythoff's Game with a Pass*, INTEGERS 25 (2025), Article G4, Theorem 4.

Stated but not proved: `MetaMathlibExt.wythoffPassGrundy_eq_zero_iff_plusStone` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffPassWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffPassWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-pass-grundy-eq-zero-iff-plus-sto).

## Away from the corner, P-positions with a pass are Wythoff's Grundy-one positions

Let
$\mathcal{G}_1(x, y, p)$ be the Grundy numbers of Wythoff's game with a pass, where $p = 1$ means
the pass is still available and $p = 0$ means it has been used, so that $\mathcal{G}_1(x, y, 0)$
is the Grundy number of $(x, y)$ in classical Wythoff's game. If $x \ge 9$ or $y \ge 9$, then
$\mathcal{G}_1(x, y, 1) = 0$ if and only if $\mathcal{G}_1(x, y, 0) = 1$.

## Sources

- Ryohei Miyadera, Hikaru Manabe, and Masanori Fukui, *Wythoff's Game with a Pass*, INTEGERS 25 (2025), Article G4, Corollary 2.

Stated but not proved: `MetaMathlibExt.wythoffPassGrundy_true_eq_zero_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffPassWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffPassWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-pass-grundy-true-eq-zero-iff).

## P-positions with the pass available lie near Wythoff P-positions

Let
$\mathcal{G}_1(x, y, p)$ be the Grundy number of Wythoff's game with a one-time pass, where $p = 1$
means the pass is still available and $p = 0$ gives classical Wythoff's game. For all natural
numbers $x, y$ with $\mathcal{G}_1(x, y, 1) = 0$ there exist natural numbers $v, w$ with
$\mathcal{G}_1(v, w, 0) = 0$ and $(x - v)^2 + (y - w)^2 \le 20$, that is, $(v, w)$ lies within
Euclidean distance $\sqrt{20}$ of $(x, y)$.

## Sources

- Ryohei Miyadera, Hikaru Manabe, and Masanori Fukui, *Wythoff's Game with a Pass*, INTEGERS 25 (2025), Article G4, Theorem 5.

Stated but not proved: `MetaMathlibExt.wythoffPass_pPosition_near_wythoff_pPosition` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffPassWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffPassWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-pass-p-position-near-wythoff-p-p).

## Moves of Wythoff's game with terminal positions

Let $\ell$ be a natural number. In the
game $K^\ell$, whose positions are pairs $(x, y)$ of natural numbers (the sizes of two piles of
tokens), there is a move from $(x, y)$ to $(x', y')$ when $x + y > \ell$ and either $y' = y$ and
$x' < x$, or $x' = x$ and $y' < y$, or $x = x' + k$ and $y = y' + k$ for some $k > 0$. Thus the
positions with $x + y \le \ell$ are terminal, and from any other position a move removes a
positive number of tokens from one pile, or the same positive number from both piles.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, the game `K^ℓ` of Theorem 17 (`jis-2026-26.1.6-thm-17`): Wythoff's moves with terminal positions `{(x, y) | x + y ≤ ℓ}`.

Formalized by `MetaMathlibExt.wythoffTerminalMove`, a definition declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-terminal-move).

## No moves from terminal positions

Let $\ell$ be a natural number. In the game $K^\ell$
(Wythoff's game in which the positions $(x, y)$ with $x + y \le \ell$ are terminal), there is no
move from a position $(x, y)$ with $x + y \le \ell$ to any position.

## Sources

- Antoine Renard and Michel Rigo, Journal of Integer Sequences 29 (2026), Article 26.1.6, terminal positions of `K^ℓ` (Theorem 17).

Formalized by `MetaMathlibExt.not_wythoffTerminalMove_of_terminal`, a theorem declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#not-wythoff-terminal-move-of-terminal).

## A move to the origin in $K^0$

In the game $K^0$ (Wythoff's game in which only $(0, 0)$ is
terminal), there is a move from the position $(1, 0)$ to the position $(0, 0)$.

## Sources

- Antoine Renard and Michel Rigo, Journal of Integer Sequences 29 (2026), Article 26.1.6, Wythoff's moves (Theorem 17).

Formalized by `MetaMathlibExt.wythoffTerminalMove_zero_one_zero`, a theorem declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-terminal-move-zero-one-zero).

## The mex sequence of Wythoff's game with terminal positions

Fix a natural number $\ell$.
The sequence $(a_n)_{n \ge 0}$ is defined recursively: $a_n$ is the least natural number greater
than $\ell$ that differs from $a_i$ and from $a_i + i + \ell + 1$ for every $i < n$. Writing
$b_i = a_i + i + \ell + 1$, this says that $a_n$ is the least natural number outside
$\{0, 1, \dots, \ell\} \cup \{a_i, b_i : i < n\}$; in particular $a_0 = \ell + 1$ and
$b_0 = 2\ell + 2$.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 17, equation (mexdef) (`jis-2026-26.1.6-thm-17`).

Formalized by `MetaMathlibExt.wythoffMexA`, a definition declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-mex-a).

## The companion of the mex sequence

Fix a natural number $\ell$ and let $(a_n)$ be the mex
sequence of $K^\ell$ (Wythoff's game in which the positions $(x, y)$ with $x + y \le \ell$ are
terminal). Its companion sequence is $b_n = a_n + n + \ell + 1$ for every natural number $n$.

## Sources

- Antoine Renard and Michel Rigo, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 17, equation (mexdef).

Formalized by `MetaMathlibExt.wythoffMexB`, a definition declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-mex-b).

## The term $a_0$ of the mex sequence

For every natural number $\ell$, the mex sequence
$(a_n)$ of $K^\ell$ (Wythoff's game in which the positions $(x, y)$ with $x + y \le \ell$ are
terminal) satisfies $a_0 = \ell + 1$.

## Sources

- Antoine Renard and Michel Rigo, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 17 (`(a₀, b₀) = (ℓ + 1, 2ℓ + 2)`).

Formalized by `MetaMathlibExt.wythoffMexA_zero`, a theorem declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-mex-a-zero).

## The term $a_1$ of the mex sequence

Let $\ell \ge 1$, let $K^\ell$ be Wythoff's game in
which the positions $(x, y)$ with $x + y \le \ell$ are terminal, and let $(a_n)$ be the mex
sequence of $K^\ell$. Then $a_1 = \ell + 2$.

This is the least integer greater than $\ell$ other than $a_0 = \ell + 1$ and
$a_0 + \ell + 1 = 2\ell + 2$.

## Sources

- Antoine Renard and Michel Rigo, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 17, equation (mexdef).

Formalized by `MetaMathlibExt.wythoffMexA_one`, a theorem declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-mex-a-one).

## The term $b_0$ of the companion sequence

For every natural number $\ell$, the companion
sequence $(b_n)$ of the mex sequence of $K^\ell$ (Wythoff's game in which the positions $(x, y)$
with $x + y \le \ell$ are terminal) satisfies $b_0 = 2\ell + 2$.

## Sources

- Antoine Renard and Michel Rigo, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 17 (`(a₀, b₀) = (ℓ + 1, 2ℓ + 2)`).

Formalized by `MetaMathlibExt.wythoffMexB_zero`, a theorem declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-mex-b-zero).

## Predicted P-positions of $K^\ell$

Let $\ell$ be a natural number, let $a_n$ be the least
natural number $m > \ell$ with $m \ne a_i$ and $m \ne b_i$ for all $i < n$, where
$b_i = a_i + i + \ell + 1$ (the mex sequences of $K^\ell$). This is the set of positions
$(x, y)$ of natural numbers with $x + y \le \ell$ (the terminal positions of $K^\ell$),
together with the pairs $(a_n, b_n)$ and $(b_n, a_n)$ for $n \ge 0$.

## Sources

- Antoine Renard and Michel Rigo, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 17.

Formalized by `MetaMathlibExt.wythoffTerminalPSet`, a definition declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-terminal-pset).

## Terminal positions lie in the predicted P-position set

Let $\ell$ be a natural number.
Every position $(x, y) \in \mathbb{N} \times \mathbb{N}$ with $x + y \le \ell$ belongs to the
predicted P-position set of the game $K^\ell$ (Wythoff's game in which the positions with
$x + y \le \ell$ are terminal).

## Sources

- Antoine Renard and Michel Rigo, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 17.

Formalized by `MetaMathlibExt.mem_wythoffTerminalPSet_of_terminal`, a theorem declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#mem-wythoff-terminal-pset-of-terminal).

## The Komak sequence $g$

Let $\varphi$ be the golden ratio. The sequence
$g : \mathbb{N} \to \mathbb{N}$ of Komak et al. is defined by recursion on $n$: if some
$m < n$ satisfies $\lfloor n\varphi \rfloor = \lfloor m\varphi^2 \rfloor + 1$, then
$g(n) = 1 - g(m)$ for the least such $m$; otherwise $g(n) = 1$.

Such an $m$ is unique when it exists, and every $m$ with
$\lfloor n\varphi \rfloor = \lfloor m\varphi^2 \rfloor + 1$ satisfies $m < n$, so this agrees
with the source's definition, which does not restrict $m$ (there $\varphi^2$ is written
$\varphi + 1$). In particular $g(0) = 1$ and $g(1) = 0$.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Definition `def:fg` (arXiv:2512.11601v1).

Formalized by `MetaMathlibExt.komakG`, a definition declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#komak-g).

## Value of the Komak sequence at 0

The sequence $g$ of Komak et al. satisfies
$g(0) = 1$.

## Sources

- Antoine Renard and Michel Rigo, Journal of Integer Sequences 29 (2026), Article 26.1.6, Definition `def:fg`.

Formalized by `MetaMathlibExt.komakG_zero`, a theorem declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#komak-g-zero).

## Value of the Komak sequence at 1

The sequence $g$ of Komak et al. satisfies
$g(1) = 0$: with $\varphi$ the golden ratio, $\lfloor \varphi \rfloor = 1 =
\lfloor 0 \cdot \varphi^2 \rfloor + 1$, so $g(1) = 1 - g(0) = 0$.

## Sources

- Antoine Renard and Michel Rigo, Journal of Integer Sequences 29 (2026), Article 26.1.6, Definition `def:fg` and Table `tab:gh`.

Formalized by `MetaMathlibExt.komakG_one`, a theorem declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#komak-g-one).

## Greedy Fibonacci digits

Let $F_0 = 1$, $F_1 = 2$ and $F_{i+2} = F_{i+1} + F_i$. For
$k, n \in \mathbb{N}$, the greedy digits of $n$ at positions $k - 1, \dots, 0$ are the list of
$k$ digits, most significant first, computed with a remainder $r$ that starts at $n$: for
$j = k - 1, \dots, 0$ in turn, the digit at position $j$ is $1$ if $F_j \le r$, in which case
$F_j$ is subtracted from $r$, and $0$ otherwise. The digits $1$ and $0$ are encoded as the
booleans true and false.

## Sources

- Antoine Renard and Michel Rigo, Journal of Integer Sequences 29 (2026), Article 26.1.6, Definition `def:fib_rep` (greedy representation).

Formalized by `MetaMathlibExt.fibGreedyDigits`, a definition declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#fib-greedy-digits).

## Fibonacci digit count

Let $F_0 = 1$, $F_1 = 2$ and $F_{i+2} = F_{i+1} + F_i$. For
$n, s, k_0 \in \mathbb{N}$, the digit count of $n$ searched from $k_0$ in at most $s$ steps is
the least $k$ with $k_0 \le k < k_0 + s$ and $n < F_k$ if there is one, and $k_0 + s$
otherwise.

With $k_0 = 0$ and $s = n + 1$ it is the number of digits of the greedy Fibonacci
representation of $n$, the least $k$ with $n < F_k$, which exists since $n < F_n$.

## Sources

- Antoine Renard and Michel Rigo, Journal of Integer Sequences 29 (2026), Article 26.1.6, Definition `def:fib_rep` (greedy representation).

Formalized by `MetaMathlibExt.fibDigitCount`, a definition declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#fib-digit-count).

## Greedy Fibonacci representation

Let $F_0 = 1$, $F_1 = 2$ and $F_{i+2} = F_{i+1} + F_i$.
The greedy Fibonacci representation $\mathrm{rep}_F(n)$ of $n \in \mathbb{N}$ is the word of
digits $d_{k-1} \cdots d_0$, most significant first, where $k$ is the least integer with
$n < F_k$ and the digits are chosen greedily: starting from the remainder $n$, for
$j = k - 1, \dots, 0$ in turn, $d_j = 1$ and $F_j$ is subtracted from the remainder if $F_j$ is
at most the remainder, and $d_j = 0$ otherwise. It has no leading zero, and
$\mathrm{rep}_F(0)$ is the empty word. The digits $1$ and $0$ are encoded as the booleans true
and false.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Definition `def:fib_rep`.

Formalized by `MetaMathlibExt.fibRep`, a definition declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#fib-rep).

## Greedy Fibonacci representations of 0, 2, 4, 7 and 12

With $F_0 = 1$, $F_1 = 2$ and
$F_{i+2} = F_{i+1} + F_i$, the greedy Fibonacci representations are
$\mathrm{rep}_F(0) = \varepsilon$ (the empty word), $\mathrm{rep}_F(2) = 10$,
$\mathrm{rep}_F(4) = 101$, $\mathrm{rep}_F(7) = 1010$ and $\mathrm{rep}_F(12) = 10101$.

## Sources

- Antoine Renard and Michel Rigo, Journal of Integer Sequences 29 (2026), Article 26.1.6, Definition `def:fib_rep` and Table `tab:K1`.

Formalized by `MetaMathlibExt.fibRep_examples`, a theorem declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#fib-rep-examples).

## Fibonacci-automatic sequences

A sequence $u : \mathbb{N} \to \mathbb{N}$ is
Fibonacci-automatic if there are a finite set $Q$ of states, a transition function
$\delta : Q \times \{0, 1\} \to Q$, an initial state $q_0 \in Q$ and an output map
$\tau : Q \to \mathbb{N}$ such that for every $n$, $u(n) = \tau(q)$, where $q$ is the state
reached from $q_0$ by reading the digits of the greedy Fibonacci representation
$\mathrm{rep}_F(n)$ with $\delta$, most significant digit first.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Section 2 (Fibonacci-automatic sequences, DFAO fed with `rep_F(n)`).

Formalized by `MetaMathlibExt.IsFibonacciAutomatic`, a definition declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#is-fibonacci-automatic).

## Constant sequences are Fibonacci-automatic

For every $c \in \mathbb{N}$, the constant
sequence $n \mapsto c$ is Fibonacci-automatic.

## Sources

- Antoine Renard and Michel Rigo, Journal of Integer Sequences 29 (2026), Article 26.1.6, Section 2 (Fibonacci-automatic sequences).

Formalized by `MetaMathlibExt.isFibonacciAutomatic_const`, a theorem declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#is-fibonacci-automatic-const).

## A prefix of the fourth iterate of $f_1$

Let $f_1$ be the map on the alphabet
$\{0, 1, 2, 3, 4\}$ given by $0 \mapsto 01$, $1 \mapsto 2$, $2 \mapsto 34$, $3 \mapsto 31$ and
$4 \mapsto 2$, extended to finite words by concatenation. The first six letters of the word
$f_1^4(0)$ are $0, 1, 2, 3, 4, 3$.

## Sources

- Antoine Renard and Michel Rigo, Journal of Integer Sequences 29 (2026), Article 26.1.6, table after Proposition 22.

Formalized by `MetaMathlibExt.morphIterate_wythoffTerminal_one_example`, a theorem declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#morph-iterate-wythoff-terminal-one-examp).

## Larsson's set $R_2$

Let $\varphi = (1 + \sqrt{5})/2$ be the golden ratio. The set
$R_2 \subseteq \mathbb{N} \times \mathbb{N}$ consists of $(0, 0)$ together with, for every natural
number $n$, the pairs $(n, 2n + 1)$ and $(2n + 1, n)$ and the pairs
$(2\lfloor n\varphi \rfloor + 2, 2\lfloor n\varphi^2 \rfloor + 2)$ and
$(2\lfloor n\varphi^2 \rfloor + 2, 2\lfloor n\varphi \rfloor + 2)$.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 26.

Formalized by `MetaMathlibExt.larssonSetTwo`, a definition declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#larsson-set-two).

## Sample positions in Larsson's set $R_2$

The positions $(0, 0)$, $(0, 1)$ and
$(2, 2)$ belong to Larsson's set $R_2$.

## Sources

- Antoine Renard and Michel Rigo, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 26.

Formalized by `MetaMathlibExt.larssonSetTwo_examples`, a theorem declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#larsson-set-two-examples).

## Larsson's set $R_3$

Larsson's set $R_3 \subseteq \mathbb{N} \times \mathbb{N}$
consists of $(0, 0)$ together with the pairs $(n, 2n + 1)$, $(2n + 1, n)$, $(n, 2n + 2)$ and
$(2n + 2, n)$ for all $n \ge 0$.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 28.

Formalized by `MetaMathlibExt.larssonSetThree`, a definition declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#larsson-set-three).

## Sample positions in Larsson's set $R_3$

The positions $(0, 0)$, $(0, 2)$ and
$(3, 1)$ belong to Larsson's set $R_3$.

## Sources

- Antoine Renard and Michel Rigo, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 28.

Formalized by `MetaMathlibExt.larssonSetThree_examples`, a theorem declared in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#larsson-set-three-examples).

## P-positions of Wythoff's game with terminal positions

Let $\ell \ge 1$. Let $a_n$ be the
least natural number $m > \ell$ with $m \ne a_i$ and $m \ne b_i$ for all $i < n$, where
$b_i = a_i + i + \ell + 1$. Let $P$ be the set of positions $(x, y)$ with $x + y \le \ell$,
together with the pairs $(a_n, b_n)$ and $(b_n, a_n)$ for $n \ge 0$. Then $P$ is stable, meaning
no move of $K^\ell$ leads from a position of $P$ to a position of $P$, and absorbing, meaning
from every position outside $P$ some move of $K^\ell$ leads into $P$.

Since the move relation is well founded, a stable and absorbing set is the set of P-positions,
so the non-terminal P-positions of $K^\ell$ are exactly the pairs $(a_n, b_n)$ and $(b_n, a_n)$.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 17 (`jis-2026-26.1.6-thm-17`).

Stated but not proved: `MetaMathlibExt.wythoffTerminal_pPositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-terminal-p-positions).

## P-positions of $K^1$

Let $a_n$ be the least natural number $m > 1$ with $m \ne a_i$ and
$m \ne b_i$ for all $i < n$, where $b_i = a_i + i + 2$; so $(a_0, b_0) = (2, 4)$. Let $P$ be the
set of positions $(x, y)$ with $x + y \le 1$, together with the pairs $(a_n, b_n)$ and
$(b_n, a_n)$ for $n \ge 0$. Then $P$ is stable, meaning no move of $K^1$ leads from a position
of $P$ to a position of $P$, and absorbing, meaning from every position outside $P$ some move
of $K^1$ leads into $P$.

This is the case $\ell = 1$ of Theorem 17. Since the move relation is well founded, a stable
and absorbing set is the set of P-positions, so $P$ is the set of P-positions of $K^1$.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Proposition 15 (`jis-2026-26.1.6-prop-15`).

Stated but not proved: `MetaMathlibExt.wythoffTerminal_one_pPositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-terminal-one-p-positions).

## P-positions of Wythoff's game when positions of total at most 2 are terminal

In the game
$K^2$ on two piles, a move from a position $(x, y)$ with $x + y > 2$ removes a positive number
of tokens from one pile or the same positive number from both piles, and no move is allowed
from a position with $x + y \le 2$. Let $a_n$ be the least integer $m > 2$ that differs from
$a_i$ and $b_i$ for every $i < n$, and let $b_n = a_n + n + 3$, so that $(a_0, b_0) = (3, 6)$.
Let $P$ consist of the positions $(x, y)$ with $x + y \le 2$ together with the pairs
$(a_n, b_n)$ and $(b_n, a_n)$ for $n \ge 0$. Then no move of $K^2$ leads from a position in $P$
to a position in $P$, and from every position not in $P$ some move of $K^2$ leads into $P$.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Proposition 16 (`jis-2026-26.1.6-prop-16`).

Stated but not proved: `MetaMathlibExt.wythoffTerminal_two_pPositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-terminal-two-p-positions).

## Structure of the mex sequences of $K^\ell$

Let $\ell \ge 1$. Let $a_n$ be the least
natural number $m > \ell$ with $m \ne a_i$ and $m \ne b_i$ for all $i < n$, where
$b_i = a_i + i + \ell + 1$ (the mex sequences of the game $K^\ell$). Then $(a_n)$ and $(b_n)$
are strictly increasing; a natural number $j$ satisfies $j > \ell$ if and only if $j = a_n$ or
$j = b_n$ for some $n$; $a_n \ne b_m$ for all $n$ and $m$; every $j > \ell$ equals $b_n - a_n$
for exactly one $n$; and for every $n$, $a_{n+1} - a_n \in \{1, 2\}$,
$b_{n+1} - b_n \in \{2, 3\}$ and $b_{n+1} - b_n = (a_{n+1} - a_n) + 1$.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Lemma 18 (`jis-2026-26.1.6-lem-18`).

Stated but not proved: `MetaMathlibExt.wythoffMex_properties` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-mex-properties).

## Golden-ratio formula for the mex sequences

Let $\ell \ge 1$, let $\varphi$ be the golden
ratio, let $K^\ell$ be Wythoff's game in which the positions $(x, y)$ with $x + y \le \ell$ are
terminal, and let $(a_n)$ be the mex sequence of $K^\ell$ and $(b_n)$ its companion sequence.
Then there are integers $\lambda_n$ for $n \ge 0$ and an integer $C$ with $|\lambda_n| \le C$
for all $n$ such that, for every natural number $n$,
$a_n = \lfloor (n + \ell)\varphi \rfloor + \lambda_n$ and
$b_n = \lfloor (n + \ell)\varphi^2 \rfloor + \lambda_n + 1$.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Corollary 19 (`jis-2026-26.1.6-cor-19`).

Stated but not proved: `MetaMathlibExt.wythoffMex_floor_goldenRatio` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-mex-floor-golden-ratio).

## Growth of the mex sequences of $K^\ell$

Let $\ell \ge 1$. Let $a_n$ be the least natural
number $m > \ell$ with $m \ne a_i$ and $m \ne b_i$ for all $i < n$, where
$b_i = a_i + i + \ell + 1$ (the mex sequences of the game $K^\ell$), and let
$\varphi = (1 + \sqrt{5})/2$ be the golden ratio. Then $a_n / n \to \varphi$ and
$b_n / n \to \varphi^2$ as $n \to \infty$.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Corollary 20 (`jis-2026-26.1.6-cor-20`).

Stated but not proved: `MetaMathlibExt.wythoffMex_tendsto_goldenRatio` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-mex-tendsto-golden-ratio).

## Komak's description of the P-positions of $K^2$

Let $\varphi$ be the golden ratio
and $g$ the sequence of Komak et al. Let $S$ be the set of pairs $(x, y)$ of natural numbers
with $x + y \le 2$, together with the pairs
$(\lfloor n\varphi \rfloor + g(n) - 1, \lfloor n\varphi^2 \rfloor + g(n))$ and
$(\lfloor n\varphi^2 \rfloor + g(n), \lfloor n\varphi \rfloor + g(n) - 1)$ for all $n \ge 0$.
In the game $K^2$ (Wythoff's game in which the positions with $x + y \le 2$ are terminal),
no move leads from a position in $S$ to a position in $S$, and from every position outside
$S$ some move leads to a position in $S$.

These two properties determine the set of P-positions, so the P-positions of $K^2$ are
exactly the positions in $S$. The source omits the terminal positions $(0, 0)$ and $(1, 1)$,
which are P-positions since no move leaves them; they are included here.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 2 (`jis-2026-26.1.6-thm-2`).

Stated but not proved: `MetaMathlibExt.komak_pPositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#komak-p-positions).

## Hofstadter recursion for the Komak sequence

Let $h$ be Hofstadter's $G$-sequence
(OEIS A005206), given by $h(0) = 0$ and $h(n) = n - h(h(n - 1))$ for $n \ge 1$. The sequence
$g$ of Komak et al. satisfies $g(0) = 1$, $g(1) = 0$, and for every $n \ge 2$,
$g(n) = 1 - g(h(n - 1))$ if $h(n - 2) < h(n - 1)$, and $g(n) = 1$ otherwise.

The source prints $g(1) = 1$. With $\varphi$ the golden ratio, $\lfloor \varphi \rfloor = 1 =
\lfloor 0 \cdot \varphi^2 \rfloor + 1$, so the definition of $g$ gives $g(1) = 1 - g(0) = 0$,
as in the source's table of values; the value is corrected to $g(1) = 0$.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Proposition 4 (`jis-2026-26.1.6-prop-4`).

Stated but not proved: `MetaMathlibExt.komakG_hofstadter` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#komak-g-hofstadter).

## The Komak sequence $g$ is Fibonacci-automatic

The sequence $g$ of Komak et al. is
Fibonacci-automatic.

Only the existence of an automaton is asserted; the explicit automaton that the source draws
for $g$ is not part of the statement.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Proposition 6 (`jis-2026-26.1.6-prop-6`).

Stated but not proved: `MetaMathlibExt.isFibonacciAutomatic_komakG` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 397](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L397). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#is-fibonacci-automatic-komak-g).

## Fibonacci characterization of the P-positions of $K^1$

For a natural number $n$, let
$\operatorname{rep}_F(n)$ be its greedy Fibonacci representation for $F_0 = 1$, $F_1 = 2$,
$F_{i+2} = F_{i+1} + F_i$: a word over $\{0, 1\}$, most significant digit first, without leading
zeros, empty for $n = 0$. Let $S$ be the set of positions $(x, y)$ with $x + y \le 1$, together
with the pairs $(a, b)$ and $(b, a)$ for natural numbers $a \le b$ such that
$\operatorname{rep}_F(a)$ is nonempty and ends in $0$ and
$\operatorname{rep}_F(b) = \operatorname{rep}_F(a)\,1$. Then $S$ is stable, meaning no move of
$K^1$ leads from a position of $S$ to a position of $S$, and absorbing, meaning from every
position outside $S$ some move of $K^1$ leads into $S$.

Since the move relation is well founded, $S$ is therefore the set of P-positions of $K^1$. As
printed, the theorem imposes the condition on all pairs $a \le b$, which fails at the terminal
P-positions $(0, 0)$ and $(0, 1)$ because $\operatorname{rep}_F(0)$ is empty; the terminal
positions are therefore listed separately.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 12 (`jis-2026-26.1.6-thm-12`).

Stated but not proved: `MetaMathlibExt.wythoffTerminal_one_fibRep` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-terminal-one-fib-rep).

## Golden-ratio formula for Wythoff's game with terminal positions up to total 3

Let
$\varphi$ be the golden ratio. Let $a_n$ be the least integer greater than $3$ that differs from
$a_i$ and $b_i$ for all $i < n$, and let $b_n = a_n + n + 4$. Then there is a Fibonacci-automatic
sequence $g_3 : \mathbb{N} \to \mathbb{N}$ with $g_3(n) \le 2$ for all $n$ such that, for every
$n \ge 0$, $a_n = \lfloor (n + 2)\varphi \rfloor + g_3(n + 1) - 1$ and
$b_n = \lfloor (n + 2)\varphi^2 \rfloor + g_3(n + 1) + 1$.

Here $(a_n, b_n)$ are the mex pairs of $K^3$, Wythoff's game in which every position $(x, y)$
with $x + y \le 3$ is terminal; by Theorem 17 of the source they are its non-terminal
P-positions with $a_n < b_n$.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 13 (`jis-2026-26.1.6-thm-13`).

Stated but not proved: `MetaMathlibExt.exists_fibonacciAutomatic_wythoffTerminal_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 424](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L424). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#exists-fibonacci-automatic-wythoff-termi).

## Golden-ratio formula for Wythoff's game with terminal positions up to total 4

Let
$\varphi$ be the golden ratio. Let $a_n$ be the least natural number greater than $4$ that
differs from $a_i$ and $b_i$ for all $i < n$, and let $b_n = a_n + n + 5$. Then there is a
Fibonacci-automatic sequence $g_4 : \mathbb{N} \to \mathbb{N}$ with $g_4(n) \le 2$ for all $n$
such that, for every $n \ge 0$, $a_n = \lfloor (n + 2)\varphi \rfloor + g_4(n + 1)$ and
$b_n = \lfloor (n + 2)\varphi^2 \rfloor + g_4(n + 1) + 3$.

Here $(a_n, b_n)$ are the mex pairs of $K^4$, Wythoff's game in which every position $(x, y)$
with $x + y \le 4$ is terminal; by Theorem 17 of the source they are its non-terminal
P-positions with $a_n < b_n$. The source defines $g_4$ through an infinite word generated by a
morphism $\mu_4$ from the letter $1$, which is not well defined as printed ($\mu_4(1) = 2$ does
not start with $1$); $g_4$ is therefore existentially quantified.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 14 (`jis-2026-26.1.6-thm-14`).

Stated but not proved: `MetaMathlibExt.exists_fibonacciAutomatic_wythoffTerminal_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#exists-fibonacci-automatic-wythoff-termi-2).

## Morphic coding of the Wythoff mex pairs at level one

Let $a_n$ be the least natural
number $m > 1$ that differs from $a_i$ and $b_i$ for every $i < n$, and let $b_n = a_n + n + 2$,
so that $(a_0, b_0) = (2, 4)$. Let $f_1$ be the morphism on the alphabet $\{0, 1, 2, 3, 4\}$
given by $0 \mapsto 0\,1$, $1 \mapsto 2$, $2 \mapsto 3\,4$, $3 \mapsto 3\,1$, $4 \mapsto 2$ and
extended to finite words by concatenation, and let $g_1$ send the letters $0, 1, 3$ to $a$ and
the letters $2, 4$ to $b$. Then there is an infinite word $w = w(0)\,w(1)\,w(2) \cdots$ over this
alphabet that is the limit of the iterates $f_1^k(0)$ (each $f_1^k(0)$ is a prefix of $w$, and
their lengths are unbounded), and for every such $w$ and every $n \ge 0$, $g_1(w(a_n - 2)) = a$
and $g_1(w(b_n - 2)) = b$.

By Theorem 17 of the source, the pairs $(a_n, b_n)$ and $(b_n, a_n)$ are the non-terminal
P-positions of $K^1$, Wythoff's game in which no move is allowed from a position $(x, y)$ with
$x + y \le 1$; indexing the letters of $w$ from $2$, the letter at $a_n$ is coded $a$ and the
letter at $b_n$ is coded $b$.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Proposition 22 (`jis-2026-26.1.6-prop-22`).

Stated but not proved: `MetaMathlibExt.wythoffTerminal_one_morphic` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 453](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L453). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-terminal-one-morphic).

## Morphic coding of the Wythoff mex pairs at level two

Let $a_n$ be the least integer
$m > 2$ that differs from $a_i$ and $b_i$ for every $i < n$, and let $b_n = a_n + n + 3$, so that
$(a_0, b_0) = (3, 6)$. Let $f_2$ be the morphism on the alphabet $\{0, 1, \dots, 15\}$ given by
$0 \mapsto 0\,1$, $1 \mapsto 2$, $2 \mapsto 3\,4$, $3 \mapsto 5\,6$, $4 \mapsto 7$,
$5 \mapsto 8\,9$, $6 \mapsto 10$, $7 \mapsto 11\,12$, $8 \mapsto 10\,13$, $9 \mapsto 14$,
$10 \mapsto 10\,13$, $11 \mapsto 5\,6$, $12 \mapsto 15$, $13 \mapsto 5$, $14 \mapsto 8\,9$,
$15 \mapsto 11\,12$ and extended to finite words by concatenation, and let $g_2$ send the
letters $3, 5, 7, 10$ to $b$ and every other letter to $a$. Then there is an infinite word
$w = w(0)\,w(1)\,w(2) \cdots$ over this alphabet that is the limit of the iterates $f_2^k(0)$
(each $f_2^k(0)$ is a prefix of $w$, and their lengths are unbounded), and for every such $w$
and every $n \ge 0$, $g_2(w(a_n - 3)) = a$ and $g_2(w(b_n - 3)) = b$.

By Theorem 17 of the source, the pairs $(a_n, b_n)$ and $(b_n, a_n)$ are the non-terminal
P-positions of $K^2$, Wythoff's game in which no move is allowed from a position $(x, y)$ with
$x + y \le 2$; indexing the letters of $w$ from $3$, the letter at $a_n$ is coded $a$ and the
letter at $b_n$ is coded $b$.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Proposition 23 (`jis-2026-26.1.6-prop-23`).

Stated but not proved: `MetaMathlibExt.wythoffTerminal_two_morphic` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 469](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-terminal-two-morphic).

## Morphic coding of the Wythoff mex pairs at level three

Let $a_n$ be the least integer
$m > 3$ that differs from $a_i$ and $b_i$ for every $i < n$, and let $b_n = a_n + n + 4$, so that
$(a_0, b_0) = (4, 8)$. Let $f_3$ be the morphism on the alphabet $\{0, 1, \dots, 21\}$ given by
$0 \mapsto 0\,1$, $1 \mapsto 2$, $2 \mapsto 3\,4$, $3 \mapsto 5\,6$, $4 \mapsto 7$,
$5 \mapsto 8\,9$, $6 \mapsto 10$, $7 \mapsto 11\,12$, $8 \mapsto 13\,12$, $9 \mapsto 14$,
$10 \mapsto 15\,16$, $11 \mapsto 14\,17$, $12 \mapsto 18$, $13 \mapsto 14\,17$,
$14 \mapsto 19\,12$, $15 \mapsto 18\,20$, $16 \mapsto 21$, $17 \mapsto 18$, $18 \mapsto 13\,12$,
$19 \mapsto 19\,12$, $20 \mapsto 14$, $21 \mapsto 15\,16$ and extended to finite words by
concatenation, and let $g_3$ send the letters $4, 6, 8, 10, 13, 15, 17, 19, 20$ to $b$ and every
other letter to $a$. Then there is an infinite word $w = w(0)\,w(1)\,w(2) \cdots$ over this
alphabet that is the limit of the iterates $f_3^k(0)$ (each $f_3^k(0)$ is a prefix of $w$, and
their lengths are unbounded), and for every such $w$ and every $n \ge 0$,
$g_3(w(a_n - 4)) = a$ and $g_3(w(b_n - 4)) = b$.

By Theorem 17 of the source, the pairs $(a_n, b_n)$ and $(b_n, a_n)$ are the non-terminal
P-positions of $K^3$, Wythoff's game in which no move is allowed from a position $(x, y)$ with
$x + y \le 3$; indexing the letters of $w$ from $4$, the letter at $a_n$ is coded $a$ and the
letter at $b_n$ is coded $b$.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Proposition 24 (`jis-2026-26.1.6-prop-24`).

Stated but not proved: `MetaMathlibExt.wythoffTerminal_three_morphic` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 486](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L486). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-terminal-three-morphic).

## Larsson's P-positions of Blocking Wythoff Nim with one blocked option

Let $\varphi$ be
the golden ratio, and let $R_2$ consist of $(0, 0)$ and, for every $n \ge 0$, the positions
$(n, 2n + 1)$, $(2n + 1, n)$, $(2\lfloor n\varphi \rfloor + 2, 2\lfloor n\varphi^2 \rfloor + 2)$
and $(2\lfloor n\varphi^2 \rfloor + 2, 2\lfloor n\varphi \rfloor + 2)$. A Wythoff move from a
position of two piles removes a positive number of tokens from one pile, or the same positive
number from both. Then every position in $R_2$ has at most one Wythoff move to a position in
$R_2$, and every position outside $R_2$ has at least two Wythoff moves to positions in $R_2$.

Hence $R_2$ is the set of P-positions of $W^2$, Wythoff's game in which the previous player may
forbid one option.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 26 (`jis-2026-26.1.6-thm-26`).

Stated but not proved: `MetaMathlibExt.blockingWythoff_two_pPositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 503](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L503). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#blocking-wythoff-two-p-positions).

## Larsson's P-positions of Blocking Wythoff Nim with two blocked options

Let $R_3$
consist of $(0, 0)$ and, for every $n \ge 0$, the positions $(n, 2n + 1)$, $(2n + 1, n)$,
$(n, 2n + 2)$ and $(2n + 2, n)$. A Wythoff move from a position of two piles removes a positive
number of tokens from one pile, or the same positive number from both. Then every position in
$R_3$ has at most two Wythoff moves to positions in $R_3$, and every position outside $R_3$ has
at least three Wythoff moves to positions in $R_3$.

Hence $R_3$ is the set of P-positions of $W^3$, Wythoff's game in which the previous player may
forbid two options.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 28 (`jis-2026-26.1.6-thm-28`).

Stated but not proved: `MetaMathlibExt.blockingWythoff_three_pPositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 514](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L514). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#blocking-wythoff-three-p-positions).

## No redundant move in $K^\ell$ for $1 \le \ell \le 4$

Let $1 \le \ell \le 4$. Let $a_n$ be
the least natural number $m > \ell$ with $m \ne a_i$ and $m \ne b_i$ for all $i < n$, where
$b_i = a_i + i + \ell + 1$, and let $P$ be the set of positions $(x, y)$ with $x + y \le \ell$
together with the pairs $(a_n, b_n)$ and $(b_n, a_n)$ for $n \ge 0$. Let $v$ be one of the move
vectors $(i, 0)$, $(0, i)$ or $(i, i)$ with $i > 0$. Then there is a position $p \notin P$ such
that every move of $K^\ell$ from $p$ to a position $q \in P$ satisfies $p = q + v$.

In other words, once the moves by $v$ are removed from $K^\ell$, the set $P$ is no longer
absorbing. Since $P$ is the set of P-positions of $K^\ell$ (Theorem 17) and stays stable when
moves are removed, removing the moves by $v$ changes the set of P-positions.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 30 (`jis-2026-26.1.6-thm-30`).

Stated but not proved: `MetaMathlibExt.wythoffTerminal_no_redundant_move` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 527](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L527). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#wythoff-terminal-no-redundant-move).

## Blocking Wythoff Nim with one or two blocked options has no redundant move

Let
$\varphi$ be the golden ratio. Let $R_2$ consist of $(0, 0)$ and, for every $n \ge 0$, the
positions $(n, 2n + 1)$, $(2n + 1, n)$,
$(2\lfloor n\varphi \rfloor + 2, 2\lfloor n\varphi^2 \rfloor + 2)$ and
$(2\lfloor n\varphi^2 \rfloor + 2, 2\lfloor n\varphi \rfloor + 2)$, and let $R_3$ consist of
$(0, 0)$ and, for every $n \ge 0$, the positions $(n, 2n + 1)$, $(2n + 1, n)$, $(n, 2n + 2)$ and
$(2n + 2, n)$. A Wythoff move from a position $x$ of two piles to a position $y$ removes a
positive number of tokens from one pile, or the same positive number from both. Let $v$ be
$(i, 0)$, $(0, i)$ or $(i, i)$ for an integer $i > 0$. Then some position $x \notin R_2$ has
fewer than two Wythoff moves to positions $y \in R_2$ with $y + v \ne x$, and some position
$x \notin R_3$ has fewer than three Wythoff moves to positions $y \in R_3$ with $y + v \ne x$.

So once the moves by $v$ are removed, $R_2$ and $R_3$ are no longer the sets of P-positions of
$W^2$ and $W^3$, Wythoff's game in which the previous player may forbid one, respectively two,
options.

## Sources

- Antoine Renard and Michel Rigo, *Variants of Wythoff Game With Terminal Positions or Blocking Maneuvers*, Journal of Integer Sequences 29 (2026), Article 26.1.6, Theorem 31 (`jis-2026-26.1.6-thm-31`).

Stated but not proved: `MetaMathlibExt.blockingWythoff_no_redundant_move` is written with `theorem_wanted` in [WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean, line 539](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/WythoffTerminalPositionsWanted.lean#L539). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html#blocking-wythoff-no-redundant-move).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Wythoff's game](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/wythoff-s-game/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GameTheory/combinatorial-games/wythoff-s-game)
