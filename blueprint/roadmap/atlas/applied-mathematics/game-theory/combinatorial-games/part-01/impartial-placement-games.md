---
declaration: section
origin: cited
lean: MetaMathlibExt.placementTerminal, MetaMathlibExt.placementUlt, MetaMathlibExt.placementPenult, MetaMathlibExt.placementGame, MetaMathlibExt.mem_placementGame_moves, MetaMathlibExt.placementFirstPlayerWins, MetaMathlibExt.placementFirstPlayerWins_iff, MetaMathlibExt.placementTerminal_univ
statement: formalized
---

# Impartial placement games

30 results, 15 proved and 15 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html).

## Terminal positions of a placement game

Let $\alpha$ be a finite set of cells and let $E$
be a predicate on subsets of $\alpha$, the condition under which play has ended. A position
$S \subseteq \alpha$ (the set of occupied cells) is terminal when $E(S)$ holds or $S = \alpha$:
play has ended, or every cell is occupied. These are the positions with no options.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Definition 1.1 (terminal positions).

Formalized by `MetaMathlibExt.placementTerminal`, a definition declared in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#placement-terminal).

## Ults of a placement game

Let $\alpha$ be a finite set of cells and let $E$ be a predicate
on subsets of $\alpha$, the condition under which play has ended. A position $S \subseteq \alpha$
is an ult when it is not terminal but has a terminal option: $S$ is not terminal, and there is a
cell $c \notin S$ such that $S \cup \{c\}$ is terminal.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Definition 1.1 (ults).

Formalized by `MetaMathlibExt.placementUlt`, a definition declared in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#placement-ult).

## Penults of a placement game

Let $\alpha$ be a finite set of cells and let $E$ be a
predicate on subsets of $\alpha$, the condition under which play has ended. A position
$S \subseteq \alpha$ is a penult when it is not terminal and all of its options are ults: $S$ is
not terminal, and $S \cup \{c\}$ is an ult for every cell $c \notin S$.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Definition 1.1 (penults).

Formalized by `MetaMathlibExt.placementPenult`, a definition declared in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#placement-penult).

## The placement game

Let $\alpha$ be a finite set of cells and let $E$ be a predicate on
subsets of $\alpha$, the condition under which play has ended. The placement game is the impartial
game whose positions are the subsets $S \subseteq \alpha$ (the occupied cells), starting from the
empty board $\emptyset$. If $E(S)$ holds there are no moves from $S$; otherwise the moves from $S$
lead to the positions $S \cup \{c\}$ with $c \notin S$. The rank of $S$ is the number
$|\alpha| - |S|$ of empty cells.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Section 1 (normal-play impartial placement games).

Formalized by `MetaMathlibExt.placementGame`, an abbreviation declared in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#placement-game).

## Moves of a placement game

Let $\alpha$ be a finite set of cells and $E$ a predicate on
subsets of $\alpha$ saying when play has ended. In the placement game on $\alpha$ with end
predicate $E$, a position $T$ is a move from a position $S$ if and only if $E(S)$ fails and
$T = S \cup \{c\}$ for some cell $c \notin S$.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Section 1 (normal-play impartial placement games).

Formalized by `MetaMathlibExt.mem_placementGame_moves`, a theorem declared in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#mem-placement-game-moves).

## First-player win in a placement game

Let $\alpha$ be a finite set of cells and $E$ a
predicate on subsets of $\alpha$ saying when play has ended. The player to move from a position
$S \subseteq \alpha$ wins the placement game on $\alpha$ with end predicate $E$ when $S$ is not a
P-position of that game under normal play, in which the player unable to move loses.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Section 1 (normal-play impartial games) and Section 4 (winning strategies).

Formalized by `MetaMathlibExt.placementFirstPlayerWins`, a definition declared in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#placement-first-player-wins).

## Normal-play recursion for placement games

Let $\alpha$ be a finite set of cells and $E$ a
predicate on subsets of $\alpha$ saying when play has ended. In the placement game on $\alpha$
with end predicate $E$, the player to move from a position $S \subseteq \alpha$ wins if and only
if $E(S)$ fails and there is a cell $c \notin S$ such that the player to move from $S \cup \{c\}$
does not win.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Section 1 (normal-play impartial games).

Formalized by `MetaMathlibExt.placementFirstPlayerWins_iff`, a theorem declared in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#placement-first-player-wins-iff).

## The full board is terminal

Let $\alpha$ be a finite set of cells. For every predicate $E$
on subsets of $\alpha$, the full board $\alpha$ is a terminal position of the placement game with
ending condition $E$.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Definition 1.1 (a position with no options is terminal).

Formalized by `MetaMathlibExt.placementTerminal_univ`, a theorem declared in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#placement-terminal-univ).

## End of Impartial Tic

Write the cells of the $n \times n$ board as pairs $(r, c)$ (row,
column) in $\{0, \dots, n-1\}^2$. Impartial Tic has ended at a set $S$ of occupied cells when some
row or some column is full: there is a row $r$ with $(r, c) \in S$ for every column $c$, or there
is a column $c$ with $(r, c) \in S$ for every row $r$.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Section 1 (rules of Impartial Tic).

Formalized by `MetaMathlibExt.ticEnded`, a definition declared in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#tic-ended).

## Impartial Tic has not ended on the empty board

For $n \ge 1$, play of Impartial Tic has
not ended on the empty $n \times n$ board: no row and no column is full.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Section 1 (rules of Impartial Tic).

Formalized by `MetaMathlibExt.not_ticEnded_empty`, a theorem declared in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#not-tic-ended-empty).

## Orthogonal adjacency

Two cells $p = (p_1, p_2)$ and $q = (q_1, q_2)$ of the $n \times n$
board $\{0, \dots, n-1\}^2$, written as (row, column), are orthogonally adjacent when they lie in
the same row and their columns differ by $1$ ($p_1 = q_1$ and $|p_2 - q_2| = 1$), or they lie in
the same column and their rows differ by $1$ ($p_2 = q_2$ and $|p_1 - q_1| = 1$).

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Section 1 (orthogonal paths in Impartial Tak).

Formalized by `MetaMathlibExt.takAdjacent`, a definition declared in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#tak-adjacent).

## Roads in Impartial Tak

Write the cells of the $n \times n$ board as pairs (row, column)
in $\{0, \dots, n-1\}^2$. Impartial Tak has ended at a set $S$ of occupied cells when the tokens
contain an orthogonal path from an edge of the board to the opposite edge: there are a token
$a \in S$ and a cell $b$ joined by a sequence $a = p_0, p_1, \dots, p_k = b$ with $k \ge 0$, in
which each $p_{i+1}$ is a token in $S$ orthogonally adjacent to $p_i$, such that $a$ lies in the
first column and $b$ in the last column, or $a$ lies in the first row and $b$ in the last row.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Section 1 (rules of Impartial Tak).

Formalized by `MetaMathlibExt.takHasRoad`, a definition declared in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#tak-has-road).

## The empty board has no Tak road

For every $n$, the empty $n \times n$ board contains no
road of Impartial Tak.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Section 1 (rules of Impartial Tak).

Formalized by `MetaMathlibExt.not_takHasRoad_empty`, a theorem declared in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#not-tak-has-road-empty).

## Weights of the Weighted Cross

For natural numbers $a$ and $b$, the weight $w(a, b)$ is
$0$ if $a, b \in \{0, 4\}$; otherwise it is $2$ if $a = 2$ and $1 \le b \le 3$, or $b = 2$ and
$1 \le a \le 3$; and it is $1$ in all other cases. On the $5 \times 5$ window $0 \le a, b \le 4$
this puts weight $0$ at the four corners, $2$ on the central plus (the centre $(2, 2)$ and its
four orthogonal neighbours) and $1$ elsewhere.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Figure 10 (c) (the Weighted Cross; arXiv:2408.01837v1, Figure 7 (c)).

Formalized by `MetaMathlibExt.weightedCrossWeight`, a definition declared in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#weighted-cross-weight).

## Total weight of the Weighted Cross

The weights $w(a, b)$ of the Weighted Cross over the
$5 \times 5$ window sum to $26$: $\sum_{a=0}^{4} \sum_{b=0}^{4} w(a, b) = 26$.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Figure 10 (c) and Proposition 14 (coefficient `26`).

Formalized by `MetaMathlibExt.sum_weightedCrossWeight`, a theorem declared in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#sum-weighted-cross-weight).

## The first player wins Impartial Tic exactly on odd boards

For every natural number $n$,
under normal play the first player wins Impartial Tic on the $n \times n$ board, starting from the
empty board, if and only if $n$ is odd; for even $n$ the second player wins.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Proposition 1.

Stated but not proved: `MetaMathlibExt.impartialTic_firstPlayerWins_iff_odd` is written with `theorem_wanted` in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#impartial-tic-first-player-wins-iff-odd).

## The second player wins Impartial Tak on even boards

Impartial Tak is the impartial
placement game on the $n \times n$ board in which the players alternately place a token on an
empty cell, play ends once the tokens contain a road, and the player unable to move loses. If $n$
is even, the first player does not win from the empty $n \times n$ board, that is, the second
player wins.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Proposition 2.

Stated but not proved: `MetaMathlibExt.impartialTak_not_firstPlayerWins_of_even` is written with `theorem_wanted` in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#impartial-tak-not-first-player-wins-of-e).

## The first player wins Impartial Tak on the $5 \times 5$ board

Impartial Tak is the
impartial placement game on the $n \times n$ board in which the players alternately place a token
on an empty cell, play ends once the tokens contain a road, and the player unable to move loses.
On the $5 \times 5$ board the first player wins from the empty board.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Proposition 3.

Stated but not proved: `MetaMathlibExt.impartialTak_five_firstPlayerWins` is written with `theorem_wanted` in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#impartial-tak-five-first-player-wins).

## Token bound for dual Impartial Tic penults

Let $n \ge 5$. If $S$ is a penult of
Impartial Tic on the $n \times n$ board, then at most $4(n - 2)$ cells of the board lie outside
$S$.

In the dual of Impartial Tic, tokens are removed from a full board and play ends once some row or
column is empty; its penults are the sets of empty cells of Impartial Tic penults, so this says
that a penult of the dual game on the $n \times n$ board has at most $4(n - 2)$ tokens.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Proposition 4.

Stated but not proved: `MetaMathlibExt.impartialTic_dual_penult_card_le` is written with `theorem_wanted` in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#impartial-tic-dual-penult-card-le).

## Dual Impartial Tic penults on the 4 × 4 board have at most 9 tokens

If $S$ is a penult of
Impartial Tic on the $4 \times 4$ board, then at most $9$ cells of the board lie outside $S$.

In the dual of Impartial Tic, tokens are removed from a full board and play ends once some row or
column is empty; its penults are the sets of empty cells of Impartial Tic penults, so this says
that a penult of the dual game on the $4 \times 4$ board has at most $9$ tokens.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Proposition 4.

Stated but not proved: `MetaMathlibExt.impartialTic_dual_penult_card_le_of_four` is written with `theorem_wanted` in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#impartial-tic-dual-penult-card-le-of-fou).

## Token counts of dual Impartial Tic penults

Let $n \ge 5$ and let $x$ be a natural number
with $2n \le x \le 4(n - 2)$. Then there is a penult $S$ of Impartial Tic on the $n \times n$
board such that exactly $x$ cells of the board lie outside $S$.

In the dual of Impartial Tic, tokens are removed from a full board and play ends once some row or
column is empty; its penults are the sets of empty cells of Impartial Tic penults, so this gives a
penult of the dual game on the $n \times n$ board with exactly $x$ tokens.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Proposition 5.

Stated but not proved: `MetaMathlibExt.impartialTic_exists_dual_penult_card` is written with `theorem_wanted` in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#impartial-tic-exists-dual-penult-card).

## Impartial Tak penults of every size from $n^2 - 4(n - 2) - 2$ to $n^2 - 2n$

Impartial Tak
is the placement game on the $n \times n$ board whose play ends once the tokens contain a road. Let
$n \ge 4$ and let $x$ be a natural number with $n^2 - 4(n - 2) - 2 \le x \le n^2 - 2n$. Then there
is an Impartial Tak penult on the $n \times n$ board with exactly $x$ tokens.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Proposition 6.

Stated but not proved: `MetaMathlibExt.impartialTak_exists_penult_card` is written with `theorem_wanted` in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#impartial-tak-exists-penult-card).

## The largest Impartial Tak penult

Impartial Tak is the placement game on the $n \times n$
board whose play ends once the tokens contain a road. For every $n \ge 2$, the largest number of
tokens in an Impartial Tak penult on the $n \times n$ board is $U(n) = n^2 - 2n$: some penult has
exactly $n^2 - 2n$ tokens and no penult has more.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Corollary 1.

Stated but not proved: `MetaMathlibExt.impartialTak_isGreatest_penult_card` is written with `theorem_wanted` in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#impartial-tak-is-greatest-penult-card).

## Impartial Tak penults with about $n^2/3$ tokens

Impartial Tak is the placement game on
the $n \times n$ board whose play ends once the tokens contain a road. For every $n \ge 6$ there
is an Impartial Tak penult $S$ on the $n \times n$ board whose number of tokens $|S|$ satisfies
$3|S| + 8 = n^2 + 4n$ if $n \equiv 1$ or $4 \pmod 6$, $3|S| + 12 = n^2 + 4n$ if
$n \equiv 2$ or $3 \pmod 6$, $3|S| + 16 = n^2 + 6n$ if $n \equiv 5 \pmod 6$, and
$3|S| + 18 = n^2 + 6n$ if $n \equiv 0 \pmod 6$.

That is, $|S|$ is $n^2/3 + 4n/3 - 8/3$, $n^2/3 + 4n/3 - 4$, $n^2/3 + 2n - 16/3$ and
$n^2/3 + 2n - 6$ in the four cases.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Proposition 7.

Stated but not proved: `MetaMathlibExt.impartialTak_exists_snake_penult` is written with `theorem_wanted` in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#impartial-tak-exists-snake-penult).

## Every Cross meets an Impartial Tak penult

Impartial Tak is the placement game on the
$n \times n$ board whose play ends once the tokens contain a road. Let $S$ be an Impartial Tak
penult on the $n \times n$ board and let $c$ be an interior cell, that is, a cell in neither the
first nor the last row and in neither the first nor the last column. Then $S$ contains $c$ or a
cell orthogonally adjacent to $c$: every Cross (an interior cell together with its four
orthogonal neighbours) contains a token.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Proposition 8.

Stated but not proved: `MetaMathlibExt.impartialTak_penult_cross_nonempty` is written with `theorem_wanted` in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#impartial-tak-penult-cross-nonempty).

## An $n^2/5$ lower bound for Impartial Tak penults

Impartial Tak is the placement game on
the $n \times n$ board whose play ends once the tokens contain a road. There is a real constant $C$
such that for every natural number $n$, every Impartial Tak penult on the $n \times n$ board has at
least $n^2/5 - Cn$ tokens; that is, every penult has at least $n^2/5 + O(n)$ tokens.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Proposition 9.

Stated but not proved: `MetaMathlibExt.impartialTak_penult_card_ge_fifth` is written with `theorem_wanted` in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#impartial-tak-penult-card-ge-fifth).

## Every Thick Cross holds three tokens of an Impartial Tak penult

Impartial Tak is the
placement game on the $n \times n$ board whose play ends once the tokens contain a road. Index the
rows and columns by $0, \dots, n - 1$, let $S$ be an Impartial Tak penult on the $n \times n$
board, and let $r, c$ be natural numbers with $r + 4 \le n$ and $c + 4 \le n$. The Thick Cross at
$(r, c)$ is the $4 \times 4$ window of cells in rows $r, \dots, r + 3$ and columns
$c, \dots, c + 3$ with its four corners $(r, c)$, $(r, c + 3)$, $(r + 3, c)$ and
$(r + 3, c + 3)$ removed. Then at least $3$ cells of the Thick Cross belong to $S$.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Proposition 11.

Stated but not proved: `MetaMathlibExt.impartialTak_penult_thickCross` is written with `theorem_wanted` in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#impartial-tak-penult-thick-cross).

## An $n^2/4$ lower bound for Impartial Tak penults

Impartial Tak is the placement game on
the $n \times n$ board whose play ends once the tokens contain a road. There is a real constant $C$
such that for every natural number $n$, every Impartial Tak penult on the $n \times n$ board has at
least $n^2/4 - Cn$ tokens; that is, every penult has at least $n^2/4 + O(n)$ tokens.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Proposition 12.

Stated but not proved: `MetaMathlibExt.impartialTak_penult_card_ge_quarter` is written with `theorem_wanted` in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#impartial-tak-penult-card-ge-quarter).

## Weighted Cross bound for Impartial Tak penults

Let $S$ be a penult of Impartial Tak on
the $n \times n$ board, with rows and columns numbered from $0$. For all natural numbers $r, c$
with $r + 5 \le n$ and $c + 5 \le n$, consider the $5 \times 5$ window of rows $r, \dots, r + 4$
and columns $c, \dots, c + 4$, and give each token of $S$ in the window, lying in row $i$ and
column $j$ of the board, the Weighted Cross weight of position $(i - r, j - c)$. Then the tokens
of $S$ in the window have total weight at least $7$.

## Sources

- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Proposition 13.

Stated but not proved: `MetaMathlibExt.impartialTak_penult_weightedCross` is written with `theorem_wanted` in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#impartial-tak-penult-weighted-cross).

## A $\frac{7}{26}(n - 4)^2$ lower bound for Impartial Tak penults

Impartial Tak is the
placement game on the $n \times n$ board whose play ends once the tokens contain a road. For every
$n \ge 5$, every Impartial Tak penult $S$ on the $n \times n$ board satisfies
$7(n - 4)^2 \le 26|S|$, that is, it has at least $\frac{7}{26}(n - 4)^2$ tokens.

## Sources

- the journal text layer prints the bound as `26 (n - 4)2` with the numerator lost; the numerator `7` is the one in arXiv:2408.01837v1, whose statement prints `(7/26)(n - 8)²` but whose proof (summing the Weighted Cross bound of Proposition 13 over the `(n - 4)²` windows, each cell carrying total weight at most `26`) concludes `(7/26)(n - 4)²`, matching the journal's `(n - 4)²`.
- Boris Alexeev, Paul Ellis, Michael Richter, and Thotsaporn Aek Thanatipanonda, *The Penults of Tak: Adventures in Impartial, Normal-Play, Positional Games*, INTEGERS 25 (2025), Article G1, Proposition 14.

Stated but not proved: `MetaMathlibExt.impartialTak_penult_card_ge_weightedCross` is written with `theorem_wanted` in [WantedExt/GameTheory/PenultsOfTakWanted.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/PenultsOfTakWanted.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html#impartial-tak-penult-card-ge-weighted-cr).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Impartial placement games](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/impartial-placement-games/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GameTheory/combinatorial-games/impartial-placement-games)
