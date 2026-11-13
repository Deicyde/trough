---
declaration: section
origin: cited
lean: MetaMathlibExt.AccelZeckMove, MetaMathlibExt.accelZeckMove_single_one_two, MetaMathlibExt.not_accelZeckMove_zero, MetaMathlibExt.IsAccelZeckGame, MetaMathlibExt.isAccelZeckGame_zero, MetaMathlibExt.AccelZeckLosing, MetaMathlibExt.AccelZeckWinning, MetaMathlibExt.accelZeckWinning_iff
statement: formalized
---

# Accelerated Zeckendorf game

22 results, 13 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html).

## Moves of the Accelerated Zeckendorf Game

Index the Fibonacci numbers as $F_1 = 1$,
$F_2 = 2$ and $F_{i+1} = F_i + F_{i-1}$, and call a finitely supported function
$s : \mathbb{N} \to \mathbb{N}$ a state, $s(i)$ being the number of copies of $F_i$. A move
takes a state $s$ to a state $t$ if for some multiplicity $m > 0$ one of the following holds:
the move $m \cdot C_i$ with $i \ge 2$, where $s(i-1) \ge m$, $s(i) \ge m$ and $t$ is
obtained from $s$ by removing $m$ copies each of $F_{i-1}$ and $F_i$ and adding $m$ copies
of $F_{i+1}$; the move $m \cdot C_1$, where $s(1) \ge 2m$ and $t$ is obtained by replacing
$2m$ copies of $F_1$ by $m$ copies of $F_2$; the move $m \cdot S_2$, where $s(2) \ge 2m$ and
$t$ is obtained by replacing $2m$ copies of $F_2$ by $m$ copies each of $F_1$ and $F_3$; or
the move $m \cdot S_i$ with $i \ge 3$, where $s(i) \ge 2m$ and $t$ is obtained by replacing
$2m$ copies of $F_i$ by $m$ copies each of $F_{i-2}$ and $F_{i+1}$.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Definition 1.2.

Formalized by `MetaMathlibExt.AccelZeckMove`, a definition declared in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#accel-zeck-move).

## Two ones combine into a two in the Accelerated Zeckendorf Game

Index the Fibonacci
numbers as $F_1 = 1$, $F_2 = 2$, $F_{i+1} = F_i + F_{i-1}$. Passing from the state consisting of
two copies of $F_1$ to the state consisting of one copy of $F_2$ is a move of the Accelerated
Zeckendorf Game.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Definition 1.2.

Formalized by `MetaMathlibExt.accelZeckMove_single_one_two`, a theorem declared in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#accel-zeck-move-single-one-two).

## No move from the empty state

No move takes the empty state (no copies of any $F_i$) to
any state.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Definition 1.2.

Formalized by `MetaMathlibExt.not_accelZeckMove_zero`, a theorem declared in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#not-accel-zeck-move-zero).

## Complete Accelerated Zeckendorf Games

A sequence of states $g_0, g_1, \dots$ is a
complete Accelerated Zeckendorf Game on $n$ with $L$ moves if $g_0$ consists of $n$ copies of
$F_1$, for every $j < L$ some move takes $g_j$ to $g_{j+1}$, and no move is possible from
$g_L$. The states after $g_L$ play no role.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Definition 1.2.

Formalized by `MetaMathlibExt.IsAccelZeckGame`, a definition declared in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#is-accel-zeck-game).

## The complete game on $0$

The sequence whose states are all the empty state is a
complete Accelerated Zeckendorf Game on $0$ with $0$ moves.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Definition 1.2.

Formalized by `MetaMathlibExt.isAccelZeckGame_zero`, a theorem declared in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#is-accel-zeck-game-zero).

## Losing states of the Accelerated Zeckendorf Game

The losing and the winning states of
the Accelerated Zeckendorf Game are defined by simultaneous induction: a state is losing when
every move from it leads to a winning state, and a state is winning when some move from it leads
to a losing state. In particular every state from which no move is possible is losing.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Section 2.2 (rules (1)-(4) for winning and losing states).

Formalized by `MetaMathlibExt.AccelZeckLosing`, an inductive type declared in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#accel-zeck-losing).

## Winning states of the Accelerated Zeckendorf Game

A state $s$ is winning (the player
to move has a winning strategy) if some move takes $s$ to a losing state. Winning and losing
states are defined by simultaneous induction: a state is losing if every move from it reaches
a winning state.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Section 2.2 (rules (1)-(4) for winning and losing states).

Formalized by `MetaMathlibExt.AccelZeckWinning`, an inductive type declared in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#accel-zeck-winning).

## Characterization of winning states

A state $s$ is winning if and only if some move
takes $s$ to a losing state.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Section 2.2, rules (3)-(4).

Formalized by `MetaMathlibExt.accelZeckWinning_iff`, a theorem declared in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#accel-zeck-winning-iff).

## Terminal states are losing in the Accelerated Zeckendorf Game

Every state of the
Accelerated Zeckendorf Game from which no move is possible is a losing state.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Section 2.2, rule (1).

Formalized by `MetaMathlibExt.accelZeckLosing_of_terminal`, a theorem declared in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#accel-zeck-losing-of-terminal).

## The first player wins the game on $2$

The state consisting of two copies of $F_1$ is
winning.

The winning move is $1 \cdot C_1$, which reaches the terminal state with one copy of $F_2$.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Section 2.2 (Player 1 wins for `n = 2`).

Formalized by `MetaMathlibExt.accelZeckWinning_single_one_two`, a theorem declared in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#accel-zeck-winning-single-one-two).

## Zeckendorf decomposition as a game state

Index the Fibonacci numbers as $F_1 = 1$,
$F_2 = 2$ and $F_{i+1} = F_i + F_{i-1}$, and record a game state as a finitely supported
function $s : \mathbb{N} \to \mathbb{N}$, where $s(i)$ is the number of copies of $F_i$. Every
$n \in \mathbb{N}$ has a unique Zeckendorf decomposition $n = F_{i_1} + \cdots + F_{i_r}$ with
$r \ge 0$, indices $i_1, \dots, i_r \ge 1$ and $i_t \ge i_{t+1} + 2$ for $1 \le t < r$. The
Zeckendorf state of $n$ is the game state with one copy of each $F_{i_t}$: $s(i) = 1$ if
$i \in \{i_1, \dots, i_r\}$ and $s(i) = 0$ otherwise.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Section 1.1 and Theorem 1.3.

Formalized by `MetaMathlibExt.zeckendorfState`, a definition declared in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#zeckendorf-state).

## The Zeckendorf state of zero is empty

The Zeckendorf state of $0$ is the empty game
state, with no copies of any Fibonacci number.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Section 1.1.

Formalized by `MetaMathlibExt.zeckendorfState_zero`, a theorem declared in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#zeckendorf-state-zero).

## The Zeckendorf state of $4$

The Zeckendorf state of $4$ consists of one copy of $F_3$
and one copy of $F_1$, reflecting the Zeckendorf decomposition $4 = F_3 + F_1 = 3 + 1$.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Section 1.1.

Formalized by `MetaMathlibExt.zeckendorfState_four`, a theorem declared in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#zeckendorf-state-four).

## The Accelerated Zeckendorf Game terminates at the Zeckendorf decomposition

Index the
Fibonacci numbers as $F_1 = 1$, $F_2 = 2$, $F_{i+1} = F_i + F_{i-1}$. Let $n$ be a natural
number, let $Z(n)$ be the number of terms of the Zeckendorf decomposition of $n$, and let $IZ(n)$
be the sum of the indices $k$ of its terms $F_k$. Then there is no infinite sequence of moves
starting from $n$ copies of $F_1$. Moreover, every complete Accelerated Zeckendorf Game on $n$
(a sequence of moves from $n$ copies of $F_1$ to a state from which no move is possible) ends at
the state with one copy of each term of the Zeckendorf decomposition of $n$, and its number $L$
of moves satisfies

$$L \le \frac{3 + \sqrt 5}{2} n - IZ(n) - \frac{1 + \sqrt 5}{2} Z(n).$$

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Theorem 1.3.

Stated but not proved: `MetaMathlibExt.accelZeckGame_terminates_at_zeckendorf` is written with `theorem_wanted` in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#accel-zeck-game-terminates-at-zeckendorf).

## Sharp lower bound on the length of an Accelerated Zeckendorf Game

Index the Fibonacci
numbers as $F_1 = 1$, $F_2 = 2$, $F_{i+1} = F_i + F_{i-1}$. Let $n \ge 1$ and let $F_k$ be the
largest Fibonacci number with $F_k \le n$, the largest term of the Zeckendorf decomposition of
$n$. Then every complete Accelerated Zeckendorf Game on $n$ (a sequence of moves from $n$ copies
of $F_1$ to a state from which no move is possible) has at least $k - 1$ moves, and some complete
game on $n$ has exactly $k - 1$ moves.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Theorem 1.4.

Stated but not proved: `MetaMathlibExt.accelZeckGame_sharp_lower_bound` is written with `theorem_wanted` in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#accel-zeck-game-sharp-lower-bound).

## Lower bound on the length of an Accelerated Zeckendorf Game

Index the Fibonacci numbers
as $F_1 = 1$, $F_2 = 2$, $F_{i+1} = F_i + F_{i-1}$. Let $n \ge 1$ and let $F_k$ be the largest
Fibonacci number with $F_k \le n$, the largest term of the Zeckendorf decomposition of $n$. Then
every complete Accelerated Zeckendorf Game on $n$ (a sequence of moves from $n$ copies of $F_1$
to a state from which no move is possible) has at least $k - 1$ moves.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Lemma 2.1.

Stated but not proved: `MetaMathlibExt.accelZeckGame_lower_bound` is written with `theorem_wanted` in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#accel-zeck-game-lower-bound).

## Moving a Fibonacci number of pairs in the Accelerated Zeckendorf Game

Index the
Fibonacci numbers as $F_1 = 1$, $F_2 = 2$, $F_{j+1} = F_j + F_{j-1}$, extended by $F_0 = 1$ and
$F_{-1} = 0$. Let $p \ge 2$ and $i \ge 1$, and let $s$ be a state with $F_{i-1}$ copies of
$F_{p-1}$, $F_i$ copies of $F_p$ and no copy of $F_{p+1}$. Let $t$ be the state obtained from $s$
by replacing $F_{i-1}$ copies of each of $F_{p-1}$ and $F_p$ by $F_{i-1}$ copies of $F_{p+1}$.
Then passing from $s$ to $t$ is a move, and $t$ has no copy of $F_{p-1}$, $F_{i-2}$ copies of
$F_p$ and $F_{i-1}$ copies of $F_{p+1}$.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Lemma 2.2.

Stated but not proved: `MetaMathlibExt.accelZeckMove_fib_combine` is written with `theorem_wanted` in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#accel-zeck-move-fib-combine).

## Sharp lower bound for the Accelerated Zeckendorf Game on a Fibonacci number

Index the
Fibonacci numbers as $F_1 = 1$, $F_2 = 2$, $F_{i+1} = F_i + F_{i-1}$, and let $k \ge 1$. Every
complete Accelerated Zeckendorf Game on $F_k$ (a sequence of moves from $F_k$ copies of $F_1$ to
a state from which no move is possible) has at least $k - 1$ moves, and some complete game on
$F_k$ has exactly $k - 1$ moves.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Lemma 2.3.

Stated but not proved: `MetaMathlibExt.accelZeckGame_sharp_lower_bound_fib` is written with `theorem_wanted` in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#accel-zeck-game-sharp-lower-bound-fib).

## Unique winning first move

For every $n$, if the state consisting of $n$ copies of $F_1$
is winning, then exactly one state reachable from it in one move is losing: when the first
player has a winning strategy in the game on $n$, exactly one first move preserves it.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Proposition 1.5.

Stated but not proved: `MetaMathlibExt.accelZeck_unique_winning_first_move` is written with `theorem_wanted` in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#accel-zeck-unique-winning-first-move).

## Accelerated Zeckendorf Game: Conjecture 1.7 implies Conjecture 1.6

Index the Fibonacci
numbers as $F_1 = 1$, $F_2 = 2$, $F_{i+1} = F_i + F_{i-1}$. Suppose that for every $n$ such that
the state consisting of $n$ copies of $F_1$ is losing, and every $k$ with $3k \le n$, the state
consisting of $k$ copies of $F_3$ and $n - 3k$ copies of $F_1$ is losing. Then for every $n > 9$
the state consisting of $n$ copies of $F_1$ (the starting position of the Accelerated Zeckendorf
Game on $n$) is winning.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Theorem 1.8 (with Conjectures 1.6 and 1.7).

Stated but not proved: `MetaMathlibExt.accelZeck_conjecture17_implies_conjecture16` is written with `theorem_wanted` in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#accel-zeck-conjecture17-implies-conjectu).

## Accelerated Zeckendorf Game: Conjecture 1.7 in its first five cases

Index the Fibonacci
numbers as $F_1 = 1$, $F_2 = 2$, $F_{i+1} = F_i + F_{i-1}$. Let $n$ be such that the state
consisting of $n$ copies of $F_1$ (the starting position of the Accelerated Zeckendorf Game on
$n$) is losing. Then for every $k$ with $1 \le k \le 5$ and $3k \le n$, the state consisting of
$k$ copies of $F_3$ and $n - 3k$ copies of $F_1$ is losing.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Lemma 1.9.

Stated but not proved: `MetaMathlibExt.accelZeck_conjecture17_le_five` is written with `theorem_wanted` in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#accel-zeck-conjecture17-le-five).

## Unique losing move from $k$ copies of $F_2$ for odd $k$

Let $k$ be odd and $n \ge 2k$,
and suppose that for every $i < k$ with $3i \le n$ the state with $i$ copies of $F_3$,
$n - 3i$ copies of $F_1$ and nothing else is losing. Then $n \ge 3k$; the state $T$ with $k$
copies of $F_3$, $n - 3k$ copies of $F_1$ and nothing else is losing and is reached in one
move from the state $S$ with $k$ copies of $F_2$, $n - 2k$ copies of $F_1$ and nothing else;
and every losing state reached in one move from $S$ equals $T$.

## Sources

- Diego Garcia-Fernandezsesma, Steven J. Miller, Thomas Rascon, Risa Vandegrift, and Ajmain Yamin, *The Accelerated Zeckendorf Game*, The Fibonacci Quarterly 62 (2024), no. 1, Article milleretal04072023, Lemma 2.4.

Stated but not proved: `MetaMathlibExt.accelZeck_odd_unique_losing_move` is written with `theorem_wanted` in [WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AcceleratedZeckendorfGameWanted.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html#accel-zeck-odd-unique-losing-move).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Accelerated Zeckendorf game](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GameTheory/combinatorial-games/accelerated-zeckendorf-game)
