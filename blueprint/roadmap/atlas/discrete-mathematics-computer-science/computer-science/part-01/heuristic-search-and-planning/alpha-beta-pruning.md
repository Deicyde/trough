---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.AlphaBeta.GameTree, Cslib.Algorithms.Lean.AlphaBeta.leaves, Cslib.Algorithms.Lean.AlphaBeta.leavesList, Cslib.Algorithms.Lean.AlphaBeta.alphaBeta, Cslib.Algorithms.Lean.AlphaBeta.alphaBetaList, Cslib.Algorithms.Lean.AlphaBeta.le_alphaBetaList_true, Cslib.Algorithms.Lean.AlphaBeta.alphaBetaList_false_le, Cslib.Algorithms.Lean.AlphaBeta.alphaBeta_time_le
statement: formalized
proof: formalized
---

# Alpha–beta pruning

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning/index.html).

## Game tree

A game tree with values in a type $\alpha$ is either a leaf, which carries a
value in $\alpha$ (the value of a terminal position), or an inner node, which carries a finite
list of game trees (the positions reachable in one move; the list may be empty). Game trees are
built inductively, so every game tree is finite.

Formalized by `Cslib.Algorithms.Lean.AlphaBeta.GameTree`, an inductive type declared in [CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning/index.html#game-tree).

## Number of leaves

The number of leaves of a game tree is defined recursively: a leaf counts
$1$, and an inner node counts the total number of leaves of its children (so an inner node without
children counts $0$).

Formalized by `Cslib.Algorithms.Lean.AlphaBeta.leaves`, a definition declared in [CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning/index.html#leaves).

## Number of leaves of a list of game trees

The number of leaves of a finite list of game
trees is the sum of the numbers of leaves of its members ($0$ for the empty list).

Formalized by `Cslib.Algorithms.Lean.AlphaBeta.leavesList`, a definition declared in [CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning/index.html#leaves-list).

## Alpha-beta pruning

For a player $p$ to move and values $a$ and $b$ in a linear order,
alpha-beta pruning with window $[a, b]$ returns the value of a leaf at a cost of one unit (one
leaf evaluation), and on an inner node runs the alpha-beta scan of its children for $p$ with
window $[a, b]$.

Formalized by `Cslib.Algorithms.Lean.AlphaBeta.alphaBeta`, a definition declared in [CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning/index.html#alpha-beta).

## Alpha-beta scan of the children

Given the player $p$ to move, values $a$ and $b$ in a
linear order and a list of game trees (the children of a position), the scan runs alpha-beta
pruning for the other player on the children in order, each time with the current bounds $a$ and
$b$. The maximizer replaces $a$ by $\max(a, v)$, where $v$ is the child's returned value, and
stops as soon as $b \le a$, returning the new $a$; if it never stops early it returns the final
$a$ ($a$ itself for an empty list). The minimizer replaces $b$ by $\min(b, v)$ and stops as soon
as $b \le a$, returning the new $b$; if it never stops early it returns the final $b$ ($b$ itself
for an empty list). The cost of the scan is the total cost of the children it evaluates.

Formalized by `Cslib.Algorithms.Lean.AlphaBeta.alphaBetaList`, a definition declared in [CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning/index.html#alpha-beta-list).

## Lower bound for the maximizer's scan

Let values lie in a linear order. For all values $a$
and $b$ and every finite list of game trees, the value returned by the alpha-beta scan of the list
with the maximizer to move and window $[a, b]$ is at least $a$.

Formalized by `Cslib.Algorithms.Lean.AlphaBeta.le_alphaBetaList_true`, a theorem declared in [CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning/index.html#le-alpha-beta-list-true).

## The minimizer's alpha-beta scan stays at or below its upper bound

For all values $a, b$ in
a linear order and every list $ts$ of game trees, the value returned by the alpha-beta scan of
$ts$ for the minimizer with lower bound $a$ and upper bound $b$ is at most $b$.

Formalized by `Cslib.Algorithms.Lean.AlphaBeta.alphaBetaList_false_le`, a theorem declared in [CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning/index.html#alpha-beta-list-false-le).

## Alpha-beta never evaluates more leaves than the tree has

For either player $p$ to move
and all values $a, b$ in a linear order, alpha-beta pruning run on a game tree $t$ for $p$ with
window $[a, b]$ evaluates at most as many leaves as $t$ has, each leaf evaluation costing one
unit.

Formalized by `Cslib.Algorithms.Lean.AlphaBeta.alphaBeta_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning/index.html#alpha-beta-time-le).

## Cost of the alpha-beta scan

For either player $p$, all values $a, b$ in a linear order
and every list $ts$ of game trees, the alpha-beta scan of $ts$ for $p$ with lower bound $a$ and
upper bound $b$ evaluates at most as many leaves as the trees in $ts$ have in total, each leaf
evaluation costing one unit.

Formalized by `Cslib.Algorithms.Lean.AlphaBeta.alphaBetaList_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning/index.html#alpha-beta-list-time-le).

## Minimax value

Let values lie in a bounded linear order. The minimax value of a game tree
with player $p$ to move (the maximizer or the minimizer) is defined recursively: a leaf is worth
the value it carries; an inner node is worth, for the maximizer, the maximum of the minimax values
of its children with the minimizer to move, and for the minimizer, the minimum of the minimax
values of its children with the maximizer to move. An inner node without children is worth $\bot$
to the maximizer and $\top$ to the minimizer.

Formalized by `Cslib.Algorithms.Lean.AlphaBeta.minimax`, a definition declared in [CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning/index.html#minimax).

## Minimax value of a list of positions

Let values lie in a bounded linear order. For a player
$p$ and a finite list of game trees, the value for $p$ is the best of their minimax values with the
other player to move: for the maximizer, the maximum of these values, or $\bot$ if the list is
empty; for the minimizer, the minimum of these values, or $\top$ if the list is empty.

Formalized by `Cslib.Algorithms.Lean.AlphaBeta.minimaxList`, a definition declared in [CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning/index.html#minimax-list).

## Alpha-beta is correct

**Alpha-beta is correct** (Knuth and Moore 1975, Theorem 1): for `a ≤ b`, the result of
alpha-beta agrees with the minimax value after clamping both to the window `[a, b]`.

Formalized by `Cslib.Algorithms.Lean.AlphaBeta.alphaBeta_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning/index.html#alpha-beta-spec).

## Correctness of the alpha-beta scan

Let $p$ be the player to move, $ts$ a list of game
trees with values in a bounded linear order, and $a \le b$. Let $r$ be the value returned by the
alpha-beta scan of $ts$ for $p$ with window $[a, b]$, and let $m$ be the best value for $p$ among
$ts$: the maximum of the minimax values of the trees in $ts$ for the minimizer ($\bot$ if $ts$ is
empty) when $p$ is the maximizer, and the minimum of their minimax values for the maximizer
($\top$ if $ts$ is empty) when $p$ is the minimizer. Then $\max(a, \min(b, r)) =
\max(a, \min(b, m))$.

Formalized by `Cslib.Algorithms.Lean.AlphaBeta.alphaBetaList_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning/index.html#alpha-beta-list-spec).

## Alpha-beta fails low when the minimax value is at most the lower bound

Let $t$ be a game
tree with values in a bounded linear order, $p$ the player to move and $a < b$ values. If the
minimax value of $t$ for $p$ is at most $a$, then alpha-beta pruning run on $t$ for $p$ with the
window $[a, b]$ returns a value at most $a$.

Formalized by `Cslib.Algorithms.Lean.AlphaBeta.alphaBeta_le_of_minimax_le`, a theorem declared in [CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning/index.html#alpha-beta-le-of-minimax-le).

## Alpha-beta is exact inside the window

Let $t$ be a game tree with values in a bounded
linear order, $p$ the player to move and $a, b$ values. If the minimax value $v$ of $t$ for $p$
satisfies $a < v < b$, then alpha-beta pruning run on $t$ for $p$ with the window $[a, b]$ returns
exactly $v$.

Formalized by `Cslib.Algorithms.Lean.AlphaBeta.alphaBeta_eq_of_mem_window`, a theorem declared in [CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning/index.html#alpha-beta-eq-of-mem-window).

## Alpha-beta at or above the top of the window

Let values lie in a bounded linear order, let
$t$ be a game tree, let $p$ be a player, and let $a < b$. If the minimax value of $t$ with $p$ to
move is at least $b$, then the value returned by alpha-beta pruning on $t$ with $p$ to move and
window $[a, b]$ is at least $b$.

Formalized by `Cslib.Algorithms.Lean.AlphaBeta.le_alphaBeta_of_le_minimax`, a theorem declared in [CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning/index.html#le-alpha-beta-of-le-minimax).

## Alpha-beta with the full window returns the minimax value

Let $t$ be a game tree whose
values lie in a bounded linear order with least element $\bot$ and greatest element $\top$. For
either player $p$ to move, alpha-beta pruning run on $t$ for $p$ with the window $[\bot, \top]$
returns exactly the minimax value of $t$ for $p$.

Formalized by `Cslib.Algorithms.Lean.AlphaBeta.alphaBeta_bot_top`, a theorem declared in [CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/GameTree/AlphaBeta.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning/index.html#alpha-beta-bot-top).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Alpha–beta pruning](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/heuristic-search-and-planning/alpha-beta-pruning)
