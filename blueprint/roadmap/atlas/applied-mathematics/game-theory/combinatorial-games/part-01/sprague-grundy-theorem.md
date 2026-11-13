---
declaration: section
origin: cited
lean: MetaMathlibExt.pPositions_unique, MetaMathlibExt.SpragueGrundy.ImpartialGame, MetaMathlibExt.SpragueGrundy.IsP, MetaMathlibExt.SpragueGrundy.gameSum, MetaMathlibExt.SpragueGrundy.nimHeap, MetaMathlibExt.SpragueGrundy.Equiv, MetaMathlibExt.SpragueGrundy.isP_iff, MetaMathlibExt.SpragueGrundy.sprague_grundy
statement: formalized
proof: formalized
---

# Sprague–Grundy theorem

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/sprague-grundy-theorem/index.html).

## Uniqueness of the P-positions of a terminating impartial game

Write $x \to y$ when there is a
move from position $x$ to position $y$, and assume there is no infinite sequence of moves
$x_0 \to x_1 \to x_2 \to \cdots$. Call a set $P$ of positions stable if no move leads from a
position in $P$ to a position in $P$, and absorbing if from every position outside $P$ some move
leads to a position in $P$. Then any two stable and absorbing sets of positions are equal.

In particular the P-positions are determined by stability and absorption, and the N-positions
are their complement.

## Sources

- Antoine Renard and Michel Rigo, "Variants of Wythoff Game with Terminal Positions or Blocking Maneuvers," Journal of Integer Sequences 29 (2026), Article 26.1.6, Proposition (Folklore), lines 438–448, https://cs.uwaterloo.ca/journals/JIS/VOL29/Rigo/rigo5.tex; stability and absorption are defined in lines 430–436. Termination is encoded by the well-foundedness of the move relation on the acyclic game graph.

Formalized by `MetaMathlibExt.pPositions_unique`, a theorem declared in [MathlibExt/GameTheory/ImpartialAcyclicGame.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GameTheory/ImpartialAcyclicGame.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/sprague-grundy-theorem/index.html#p-positions-unique).

## Impartial game

An impartial game consists of a type of positions, a starting position,
for each position $p$ a finite set of positions reachable from $p$ in one move, and a rank
function assigning a natural number to each position such that every move strictly decreases the
rank: if $q$ is reachable from $p$ in one move, then $\mathrm{rank}(q) < \mathrm{rank}(p)$.

Because the move sets are finite and the rank strictly decreases along moves, every play
terminates and only finitely many positions are reachable from any position, even if the type of
positions is infinite or contains unreachable positions.

Formalized by `MetaMathlibExt.SpragueGrundy.ImpartialGame`, a structure declared in [MathlibExt/GameTheory/SpragueGrundy.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GameTheory/SpragueGrundy.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/sprague-grundy-theorem/index.html#impartial-game).

## P-positions

In an impartial game $G$, the P-positions are defined by well-founded
recursion along moves: a position $p$ is a P-position if and only if no position reachable from
$p$ in one move is a P-position. Positions that are not P-positions are called N-positions.

Under normal play, where the player unable to move loses, the P-positions are exactly the
positions from which the player to move loses.

Formalized by `MetaMathlibExt.SpragueGrundy.IsP`, a definition declared in [MathlibExt/GameTheory/SpragueGrundy.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GameTheory/SpragueGrundy.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/sprague-grundy-theorem/index.html#is-p).

## Sum of impartial games

The sum $G + H$ of two impartial games $G$ and $H$ is the
impartial game whose positions are the pairs $(a, b)$ of a position $a$ of $G$ and a position $b$
of $H$, and in which a move changes exactly one component: from $(a, b)$ one may move to
$(a', b)$ for any move from $a$ to $a'$ in $G$, or to $(a, b')$ for any move from $b$ to $b'$ in
$H$. Its starting position is the pair of the starting positions of $G$ and $H$, and the rank of
$(a, b)$ is the sum of the ranks of $a$ in $G$ and of $b$ in $H$.

Formalized by `MetaMathlibExt.SpragueGrundy.gameSum`, a definition declared in [MathlibExt/GameTheory/SpragueGrundy.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GameTheory/SpragueGrundy.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/sprague-grundy-theorem/index.html#game-sum).

## Nim heap

For a natural number $n$, the Nim heap of size $n$ is the impartial game whose
positions are $0, 1, \dots, n$, whose starting position is $n$, and in which a move from $k$ goes
to any $j < k$; the rank of a position is its value.

Formalized by `MetaMathlibExt.SpragueGrundy.nimHeap`, a definition declared in [MathlibExt/GameTheory/SpragueGrundy.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GameTheory/SpragueGrundy.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/sprague-grundy-theorem/index.html#nim-heap).

## Equivalence of impartial games

Two impartial games $G$ and $H$ are equivalent when no
third game tells them apart as summands: for every impartial game $K$, the starting position of
the sum $G + K$ is a P-position if and only if the starting position of the sum $H + K$ is a
P-position. The starting position of a sum is the pair of the starting positions of its summands.

Formalized by `MetaMathlibExt.SpragueGrundy.Equiv`, a definition declared in [MathlibExt/GameTheory/SpragueGrundy.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GameTheory/SpragueGrundy.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/sprague-grundy-theorem/index.html#equiv).

## Recursive characterization of P-positions

In an impartial game $G$, a position $p$ is a
P-position if and only if every position reachable from $p$ in one move is not a P-position.

Formalized by `MetaMathlibExt.SpragueGrundy.isP_iff`, a theorem declared in [MathlibExt/GameTheory/SpragueGrundy.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GameTheory/SpragueGrundy.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/sprague-grundy-theorem/index.html#is-p-iff).

## Sprague–Grundy theorem

Every impartial game $G$ is equivalent to a Nim heap: there is a
natural number $n$ such that $G$ is equivalent to the Nim heap of size $n$.

## Sources

- Tanya Khovanova and Joshua Xiong, "Nim Fractals", Journal of Integer Sequences 17 (2014), lines 101–105, https://cs.uwaterloo.ca/journals/JIS/VOL17/Khovanova/khova6.tex. Its cited original references: Grundy, Eureka 2 (1939), 6–8, reprinted 27 (1964), 9–11; Sprague, Tôhoku Math. Journal 41 (1935–1936), 438–444.

Formalized by `MetaMathlibExt.SpragueGrundy.sprague_grundy`, a theorem declared in [MathlibExt/GameTheory/SpragueGrundy.lean, line 433](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GameTheory/SpragueGrundy.lean#L433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/sprague-grundy-theorem/index.html#sprague-grundy).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sprague–Grundy theorem](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/sprague-grundy-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GameTheory/combinatorial-games/sprague-grundy-theorem)
