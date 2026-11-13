---
declaration: section
origin: cited
lean: MetaMathlibExt.snortMoverWins, MetaMathlibExt.SnortFirstPlayerWins, MetaMathlibExt.SnortSecondPlayerWins, MetaMathlibExt.IsSnortResponsePair, MetaMathlibExt.IsOpposition, MetaMathlibExt.IsOpposable, MetaMathlibExt.IsAlmostOpposable, MetaMathlibExt.IsCompatiblyAlmostOpposable
statement: formalized
---

# Snort

38 results, 20 proved and 18 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html).

## Snort positions with a move bound

Let $G$ be a finite simple graph, let $k$ be a natural
number, and let $A$ and $B$ be finite sets of vertices of $G$, the vertices coloured so far by
the player to move and by the opponent. A legal move colours a vertex $v$ that lies in neither
$A$ nor $B$ and has no neighbour in $B$. With move bound $0$ the player to move loses. With move
bound $k + 1$ the player to move wins at $(A, B)$ exactly when some legal move $v$ leaves a
position $(B, A \cup \{v\})$ that the opponent, now to move with move bound $k$, does not win.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Section 1 (rules of Snort).

Formalized by `MetaMathlibExt.snortMoverWins`, a definition declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#snort-mover-wins).

## First player wins Snort

Let $G$ be a finite simple graph. In Snort on $G$ the two players
alternately colour a vertex that is not yet coloured and is not adjacent to any vertex coloured
by the opponent, and a player with no legal move loses. The first player wins Snort on $G$ when
the player who moves first has a winning strategy from the position in which no vertex is
coloured.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Section 1.

Formalized by `MetaMathlibExt.SnortFirstPlayerWins`, a definition declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#snort-first-player-wins).

## Second-player win in Snort

Let $G$ be a finite simple graph. In Snort on $G$, two
players alternately colour a vertex of $G$ that is not yet coloured, each with their own
colour, and a player may not colour a vertex adjacent to a vertex of the opponent's colour; a
player with no legal move loses. The second player wins Snort on $G$ if, starting from the
position in which no vertex is coloured, the player who moves first has no winning strategy.

Every move colours a new vertex, so the game ends after at most $|V(G)|$ moves and has no
draws; hence this says that the second player has a winning strategy.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Section 1.

Formalized by `MetaMathlibExt.SnortSecondPlayerWins`, a definition declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#snort-second-player-wins).

## Snort response pairs

In Snort on a finite graph $G$, a pair $(u, v)$ of vertices is a
response pair if $u \neq v$, $u$ and $v$ are not adjacent (so the first player colouring $u$ and
the second answering $v$ is legal), and the first player, now to move, loses from the position
in which the first player has coloured $u$ and the second player has coloured $v$.

The outcome is computed with a bound of $|V(G)| - 2$ further moves, the number of uncoloured
vertices, so the bound never cuts the game short.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Section 3 (response pair).

Formalized by `MetaMathlibExt.IsSnortResponsePair`, a definition declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#is-snort-response-pair).

## Oppositions

An opposition of a graph $G$ is an automorphism $f$ of $G$ such that for
every vertex $v$, $f(f(v)) = v$, $f(v) \neq v$, and $f(v)$ is not adjacent to $v$; that is, an
involutive automorphism moving every vertex outside its closed neighbourhood.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Section 1 (after Kakihara).

Formalized by `MetaMathlibExt.IsOpposition`, a definition declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#is-opposition).

## Opposable graphs

A graph $G$ is opposable if it has an opposition: an automorphism $f$
of $G$ such that for every vertex $v$, $f(f(v)) = v$, $f(v) \neq v$, and $f(v)$ is not adjacent
to $v$.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Section 1.

Formalized by `MetaMathlibExt.IsOpposable`, a definition declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#is-opposable).

## Almost opposable graph

A graph $G$ is almost opposable if there are a vertex $u$ and a
set $S$ of vertices with $u \in S \subseteq N[u]$, where $N[u]$ is the closed neighbourhood of $u$
($u$ together with its neighbours), such that the subgraph $G - S$ induced on the vertices
outside $S$ is opposable.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Section 4 (almost opposable graphs).

Formalized by `MetaMathlibExt.IsAlmostOpposable`, a definition declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#is-almost-opposable).

## Compatibly almost opposable graphs

A graph $G$ is compatibly almost opposable if there
are a vertex $u$, a set $S$ of vertices with $u \in S \subseteq N[u]$ (the closed neighbourhood
of $u$), an automorphism $\alpha$ of $G$ with $\alpha(\alpha(v)) = v$ for every vertex $v$, and
an opposition $f$ of the subgraph $G - S$ induced on the vertices outside $S$, such that
$\alpha(x) = f(x)$ for every vertex $x \notin S$.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Section 4 (compatibly almost opposable graphs).

Formalized by `MetaMathlibExt.IsCompatiblyAlmostOpposable`, a definition declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#is-compatibly-almost-opposable).

## Opposition matchings

Let $K$ be a graph. A subgraph $M$ of $K$ is an opposition matching
of $K$ if it is a perfect matching of $K$ and for any two distinct edges $ab$ and $cd$ of $M$,
$ac \in E(K) \iff bd \in E(K)$ and $ad \in E(K) \iff bc \in E(K)$.

Since both matching edges are present, this says that $K$ induces on $\{a, b, c, d\}$ either
$K_4$, a $4$-cycle, or just the two matching edges.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Section 2 (opposition matchings).

Formalized by `MetaMathlibExt.IsOppositionMatching`, a definition declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#is-opposition-matching).

## Graph product given by a Boolean formula

Let $G$ and $H$ be graphs with vertex sets $V$
and $W$, and let $\varphi$ be a Boolean function of four Boolean arguments. The product
$G \varphi H$ is the graph on $V \times W$ in which two distinct vertices $(g_1, h_1)$ and
$(g_2, h_2)$ are adjacent exactly when
$\varphi(g_1 g_2 \in E(G), h_1 h_2 \in E(H), g_1 = g_2, h_1 = h_2)$ is true.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Section 2 (graph products `GφH`).

Formalized by `MetaMathlibExt.formulaProduct`, a definition declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#formula-product).

## Strong product of graphs

For simple graphs $G$ on $V$ and $H$ on $W$, the strong
product $G \boxtimes H$ is the simple graph on $V \times W$ in which $(g_1, h_1)$ and
$(g_2, h_2)$ are adjacent if and only if $g_1 = g_2$ and $h_1 h_2$ is an edge of $H$, or
$g_1 g_2$ is an edge of $G$ and $h_1 = h_2$, or $g_1 g_2$ is an edge of $G$ and $h_1 h_2$ is
an edge of $H$.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Section 2 (table of products).

Formalized by `MetaMathlibExt.strongProd`, an abbreviation declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#strong-prod).

## Firework of a graph

For a graph $G$, vertices $u$ and $v$ of $G$ and a natural number $n$,
the $n$-firework of $G$ at $(u, v)$ is the graph obtained from $G$ by adding $2n$ new vertices,
$n$ of which are adjacent only to $u$ and the other $n$ adjacent only to $v$.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Section 3 (the `n`-firework).

Formalized by `MetaMathlibExt.firework`, a definition declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#firework).

## Strong grid

For $k \in \mathbb{N}$ and natural numbers $n_0, \dots, n_{k-1}$, the
$k$-dimensional strong grid $P_{n_0} \boxtimes \cdots \boxtimes P_{n_{k-1}}$ is the simple
graph whose vertices are the tuples $(x_0, \dots, x_{k-1})$ of integers with $0 \le x_i < n_i$
for each $i$, in which two vertices $x$ and $y$ are adjacent if and only if $x \ne y$ and
$|x_i - y_i| \le 1$ for every $i$.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Corollary 3 (strong grids).

Formalized by `MetaMathlibExt.strongGrid`, a definition declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#strong-grid).

## Cartesian grid

For $k \in \mathbb{N}$ and side lengths $n_1, \dots, n_k \in \mathbb{N}$,
the $k$-dimensional Cartesian grid has as vertices the tuples $(x_1, \dots, x_k)$ of integers
with $0 \le x_i < n_i$ for each $i$, and two tuples are adjacent when they differ in exactly one
coordinate, and there by exactly one. It is the Cartesian product
$P_{n_1} \square \cdots \square P_{n_k}$ of the paths $P_{n_i}$ on $n_i$ vertices.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Corollary 4 (Cartesian grids).

Formalized by `MetaMathlibExt.cartesianGrid`, a definition declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#cartesian-grid).

## King's graph

For natural numbers $n$ and $m$, the king's graph of the $n \times m$
board is the simple graph whose vertices are the pairs $(i, j)$ with $0 \le i < n$ and
$0 \le j < m$, in which two distinct pairs $(i, j)$ and $(i', j')$ are adjacent when
$|i - i'| \le 1$ and $|j - j'| \le 1$.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Section 5.

Formalized by `MetaMathlibExt.kingGraph`, a definition declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#king-graph).

## Knight's graph

For natural numbers $n$ and $m$, the knight's graph of the $n \times m$
board is the simple graph whose vertices are the pairs $(i, j)$ with $0 \le i < n$ and
$0 \le j < m$, in which two pairs $(i, j)$ and $(i', j')$ are adjacent when either
$|i - i'| = 1$ and $|j - j'| = 2$, or $|i - i'| = 2$ and $|j - j'| = 1$.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Section 5 (proof of Theorem 9).

Formalized by `MetaMathlibExt.knightGraph`, a definition declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#knight-graph).

## Bishop's graph

For natural numbers $n$ and $m$, the bishop's graph on the $n \times m$
board has as vertices the cells $(i, j)$ with $0 \le i < n$ and $0 \le j < m$, and two distinct
cells $(i, j)$ and $(i', j')$ are adjacent when they lie on a common diagonal, that is, when
$|i - i'| = |j - j'|$.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Section 5 (proof of Theorem 10).

Formalized by `MetaMathlibExt.bishopGraph`, a definition declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#bishop-graph).

## Queen's graph

For natural numbers $n$ and $m$, the queen's graph of the $n \times m$
board is the simple graph whose vertices are the pairs $(i, j)$ with $0 \le i < n$ and
$0 \le j < m$, in which two distinct pairs $(i, j)$ and $(i', j')$ are adjacent when $i = i'$,
or $j = j'$, or $|i - i'| = |j - j'|$; that is, when they share a row, a column or a diagonal.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Section 5.

Formalized by `MetaMathlibExt.queenGraph`, a definition declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#queen-graph).

## Snort on two vertices

The first player wins Snort on the complete graph $K_2$, and
the second player wins Snort on the graph with two vertices and no edges.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Section 1; characteristic check of `snortMoverWins`.

Formalized by `MetaMathlibExt.snort_two_vertices`, a theorem declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#snort-two-vertices).

## Snort on the $2 \times 2$ queen's and rook's graphs

The first player wins Snort on
the queen's graph of the $2 \times 2$ board (the Peaceable Queens game), and the second
player wins Snort on the rook's graph of the $2 \times 2$ board (the Peaceable Rooks game).

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Section 5; characteristic check of `queenGraph` and `SimpleGraph.rookGraph`.

Formalized by `MetaMathlibExt.snort_two_by_two`, a theorem declared in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#snort-two-by-two).

## The second player wins Snort on opposable graphs

If a finite simple graph $G$ is
opposable, then the second player wins Snort on $G$.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Lemma 1 (Kakihara, Proposition 3.6).

Stated but not proved: `MetaMathlibExt.snortSecondPlayerWins_of_isOpposable` is written with `theorem_wanted` in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#snort-second-player-wins-of-is-opposable).

## Oppositions and opposition matchings

A graph $G$ is opposable if and only if its
complement $\overline{G}$ has an opposition matching.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Theorem 1.

Stated but not proved: `MetaMathlibExt.isOpposable_iff_exists_oppositionMatching` is written with `theorem_wanted` in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#is-opposable-iff-exists-opposition-match).

## Gluing oppositions of blocks

Let $G$ be a graph, let $p$ be a map from its vertices to
an index set, with blocks $B_i = \{v : p(v) = i\}$, and let $f$ be a map from the vertices of $G$
to themselves. Suppose that for every index $i$ there is an opposition of the subgraph of $G$
induced on $B_i$ that agrees with $f$ on $B_i$, and that for all vertices $u, w$ with
$p(u) \neq p(w)$ we have $uw \in E(G) \iff f(u)f(w) \in E(G)$ and
$uf(w) \in E(G) \iff f(u)w \in E(G)$. Then $G$ is opposable.

Since $uf(u)$ and $wf(w)$ are non-edges, the second condition says that the four vertices
$u, f(u), w, f(w)$ induce $C_4$, $2K_2$ or $4K_1$.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Theorem 2.

Stated but not proved: `MetaMathlibExt.isOpposable_of_blocks` is written with `theorem_wanted` in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#is-opposable-of-blocks).

## Formula products with an opposable first factor

Let $G$ and $H$ be graphs, let
$\varphi$ be a Boolean function of four truth values, and let $G \varphi H$ be the formula
product, in which distinct pairs $(g_1, h_1)$ and $(g_2, h_2)$ are adjacent when $\varphi$ is
true at the atoms $g_1g_2 \in E(G)$, $h_1h_2 \in E(H)$, $g_1 = g_2$, $h_1 = h_2$. Suppose that
for all distinct non-adjacent vertices $g_1, g_2$ of $G$ and every vertex $h$ of $H$, $\varphi$
is false at the atoms $g_1g_2 \in E(G)$, $hh \in E(H)$, $g_1 = g_2$, $h = h$ (whose values are
false, false, false, true). If $G$ is opposable, then $G \varphi H$ is opposable.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Theorem 3.

Stated but not proved: `MetaMathlibExt.isOpposable_formulaProduct` is written with `theorem_wanted` in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#is-opposable-formula-product).

## Standard products with an opposable first factor

If $G$ is an opposable graph, then for
every graph $H$ the Cartesian product $G \mathbin{\square} H$, the strong product $G \boxtimes H$,
and the tensor, lexicographic, co-normal and homomorphic products of $G$ with $H$ are opposable.
Here distinct pairs $(g_1, h_1)$ and $(g_2, h_2)$ are adjacent in the tensor product when
$g_1g_2 \in E(G)$ and $h_1h_2 \in E(H)$; in the lexicographic product when $g_1g_2 \in E(G)$,
or $g_1 = g_2$ and $h_1h_2 \in E(H)$; in the co-normal product when $g_1g_2 \in E(G)$ or
$h_1h_2 \in E(H)$; and in the homomorphic product when $g_1 = g_2$, or $g_1g_2 \in E(G)$ and
$h_1h_2 \notin E(H)$.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Corollary 1.

Stated but not proved: `MetaMathlibExt.isOpposable_products` is written with `theorem_wanted` in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#is-opposable-products).

## Fireworks preserve second-player wins in Snort

Let $G$ be a finite simple graph and let
$(u, v)$ be a response pair of $G$ whose distance in $G$ is at least $3$ (infinite distance,
when $u$ and $v$ lie in different components, is allowed). If the second player wins Snort on
$G$, then for every natural number $n$ at least the number $|V(G)|$ of vertices of $G$, the
second player wins Snort on the $n$-firework of $G$ at $(u, v)$.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Theorem 4.

Stated but not proved: `MetaMathlibExt.snortSecondPlayerWins_firework` is written with `theorem_wanted` in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#snort-second-player-wins-firework).

## Arbitrarily large trees on which the second player wins Snort

For every natural number
$N$ there is a tree $T$ on $n \ge N$ vertices such that the second player wins Snort on $T$.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Corollary 2.

Stated but not proved: `MetaMathlibExt.exists_large_tree_snortSecondPlayerWins` is written with `theorem_wanted` in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#exists-large-tree-snort-second-player-wi).

## Almost opposable graphs are first-player wins in Snort

For every finite simple graph $G$
that is almost opposable, the first player wins Snort on $G$.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Lemma 3.

Stated but not proved: `MetaMathlibExt.snortFirstPlayerWins_of_isAlmostOpposable` is written with `theorem_wanted` in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#snort-first-player-wins-of-is-almost-opp).

## Strong products of compatibly almost opposable graphs

If $G$ and $H$ are compatibly
almost opposable graphs, then their strong product $G \boxtimes H$ is compatibly almost
opposable.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Theorem 5.

Stated but not proved: `MetaMathlibExt.isCompatiblyAlmostOpposable_strongProd` is written with `theorem_wanted` in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#is-compatibly-almost-opposable-strong-pr).

## Strong products with a graph that has a universal vertex

Let $G$ and $H$ be graphs. If
$G$ is almost opposable and $H$ has a universal vertex, that is, a vertex adjacent to every other
vertex of $H$, then the strong product $G \boxtimes H$ is almost opposable.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Theorem 6.

Stated but not proved: `MetaMathlibExt.isAlmostOpposable_strongProd` is written with `theorem_wanted` in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 367](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L367). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#is-almost-opposable-strong-prod).

## Cartesian products of compatibly almost opposable graphs

Let $G$ and $H$ be compatibly
almost opposable graphs. Suppose that for some vertex $u$ of $G$ there are an involutive
automorphism $\alpha$ of $G$ and an opposition $f$ of the induced subgraph $G - u$ on the vertices
other than $u$ such that $\alpha(x) = f(x)$ for every vertex $x \neq u$. Then the Cartesian product
$G \square H$ is compatibly almost opposable.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Theorem 7.

Stated but not proved: `MetaMathlibExt.isCompatiblyAlmostOpposable_boxProd` is written with `theorem_wanted` in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#is-compatibly-almost-opposable-box-prod).

## Almost opposability of strong grids

Let $k \ge 1$ and $n_1, \dots, n_k \ge 1$. Then the
$k$-dimensional strong grid $P_{n_1} \boxtimes \cdots \boxtimes P_{n_k}$, the strong product of the
paths $P_{n_i}$ on $n_i$ vertices, is almost opposable.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Corollary 3.

Stated but not proved: `MetaMathlibExt.isAlmostOpposable_strongGrid` is written with `theorem_wanted` in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#is-almost-opposable-strong-grid).

## Opposability of Cartesian grids

Let $k \ge 1$ and $n_1, \dots, n_k \ge 1$, and let
$G = P_{n_1} \square \cdots \square P_{n_k}$ be the $k$-dimensional Cartesian grid, the Cartesian
product of the paths $P_{n_i}$ on $n_i$ vertices. Then $G$ is almost opposable if and only if at
most one of $n_1, \dots, n_k$ is even, and $G$ is opposable if more than one of them is even.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Corollary 4.

Stated but not proved: `MetaMathlibExt.cartesianGrid_opposability` is written with `theorem_wanted` in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 398](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#cartesian-grid-opposability).

## First player wins Peaceable Kings

For all natural numbers $n \ge 1$ and $m \ge 1$, the
first player wins Snort on the king's graph of the $n \times m$ board (the Peaceable Kings game).

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Theorem 8.

Stated but not proved: `MetaMathlibExt.snortFirstPlayerWins_kingGraph` is written with `theorem_wanted` in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 407](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L407). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#snort-first-player-wins-king-graph).

## Snort on the knight's graph

For natural numbers $n \ge 1$ and $m \ge 1$, the
second player wins Snort on the knight's graph of the $n \times m$ board (the Peaceable
Knights game) if and only if $n$ is even or $m$ is even.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Theorem 9.

Stated but not proved: `MetaMathlibExt.snortSecondPlayerWins_knightGraph_iff` is written with `theorem_wanted` in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#snort-second-player-wins-knight-graph-if).

## Second player wins Peaceable Bishops exactly when a side is even

For all natural numbers
$n \ge 1$ and $m \ge 1$, the second player wins Snort on the bishop's graph of the $n \times m$
board (the Peaceable Bishops game) if and only if $n$ or $m$ is even.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Theorem 10.

Stated but not proved: `MetaMathlibExt.snortSecondPlayerWins_bishopGraph_iff` is written with `theorem_wanted` in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#snort-second-player-wins-bishop-graph-if).

## Snort on the rook's graph

For natural numbers $n \ge 1$ and $m \ge 1$, the
second player wins Snort on the rook's graph of the $n \times m$ board (the Peaceable
Rooks game) if and only if $n$ and $m$ are both even.

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Theorem 11.

Stated but not proved: `MetaMathlibExt.snortSecondPlayerWins_rookGraph_iff` is written with `theorem_wanted` in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 431](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L431). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#snort-second-player-wins-rook-graph-iff).

## First player wins Peaceable Queens on boards with an odd side

Let $n \ge 1$ and
$m \ge 1$ be natural numbers such that $n$ or $m$ is odd. Then the first player wins Snort on the
queen's graph of the $n \times m$ board (the Peaceable Queens game).

## Sources

- Ashmore, Austin, Davies, Dyer, Kellough, *On Graph Automorphisms Related to SNORT*, INTEGERS 26 (2026), Article G2, Theorem 12.

Stated but not proved: `MetaMathlibExt.snortFirstPlayerWins_queenGraph` is written with `theorem_wanted` in [WantedExt/GraphTheory/SnortOppositionsWanted.lean, line 439](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/SnortOppositionsWanted.lean#L439). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html#snort-first-player-wins-queen-graph).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Snort](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/snort/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GameTheory/combinatorial-games/snort)
