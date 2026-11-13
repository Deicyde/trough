---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.BipartiteMatching.IsMatching, Cslib.Algorithms.Lean.BipartiteMatching.pairs, Cslib.Algorithms.Lean.BipartiteMatching.Valid, Cslib.Algorithms.Lean.BipartiteMatching.Free, Cslib.Algorithms.Lean.BipartiteMatching.layers, Cslib.Algorithms.Lean.BipartiteMatching.exists_mate_of_mem_layers, Cslib.Algorithms.Lean.BipartiteMatching.layers_fst_eq_of_eq, Cslib.Algorithms.Lean.BipartiteMatching.layers_fst_stable
statement: formalized
proof: formalized
---

# Maximum bipartite matching

91 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html).

## Matching in a bipartite graph

Let a bipartite graph have left vertices $0, \dots, a-1$,
right vertices $0, \dots, b-1$ and an adjacency list for each left vertex. A finite set $M$ of
pairs $(i, j)$ of a left vertex $i$ and a right vertex $j$ is a matching when every pair in $M$ is
an edge ($j$ is in the adjacency list of $i$), no two distinct pairs of $M$ have the same left
vertex, and no two distinct pairs of $M$ have the same right vertex.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.IsMatching`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#is-matching).

## Matched pairs of a partner assignment

Given a partner assignment $\mathrm{mate}$ that
sends each right vertex $j < b$ to a left vertex $i < a$ or to nothing, the matched pairs of
$\mathrm{mate}$ form the set of all pairs $(i, j)$ of a left vertex $i < a$ and a right vertex
$j < b$ with $\mathrm{mate}(j) = i$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.pairs`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#pairs).

## Partner arrays that describe a matching

Consider a bipartite graph with left vertices
$\{0, \dots, a-1\}$, right vertices $\{0, \dots, b-1\}$ and, for each left vertex $i$, a list of
its neighbours. A partner array assigns to each right vertex $j$ either no partner or a left
vertex as its partner. It is valid when every partner is a neighbour (if $i$ is the partner of
$j$, then $j$ is in the list of neighbours of $i$) and no left vertex is the partner of two
different right vertices (if $i$ is the partner of both $j$ and $j'$, then $j = j'$).

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.Valid`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#valid).

## Unmatched left vertex

Given a partner array $\mu$, which assigns to each right vertex $j$
either a left vertex $\mu(j)$ as partner or no partner, a left vertex $i$ is unmatched (free) when
no right vertex $j$ has $\mu(j) = i$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.Free`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#free).

## Alternating breadth-first layers

Let $\mu$ give each right vertex $j$ of a bipartite
graph at most one partner $\mu(j)$ among the left vertices. The layers are pairs $(Z_k, R_k)$ of a
set $Z_k$ of left vertices and a set $R_k$ of right vertices, defined by recursion on $k$: $Z_0$ is
the set of unmatched left vertices (those that are the partner of no right vertex) and
$R_0 = \emptyset$; $R_{k+1}$ is the set of right vertices $j$ adjacent to some $i \in Z_k$ with
$\mu(j) \ne i$, and $Z_{k+1}$ is $Z_k$ together with the left vertices $\mu(j)$ for $j \in R_{k+1}$.

The layers are cumulative on both sides: $Z_k$ holds the left vertices reached within $k$ rounds
and $R_k$ the right vertices reached within $k$ rounds. The round where a vertex is first reached
is its breadth-first level.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.layers`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#layers).

## Matched reached left vertices are reached through a partner

Let $\mu$ be a partner array
and $k$ a natural number. If a left vertex $i$ is reached within $k$ rounds of the layered search
and is matched (some right vertex has partner $i$), then some right vertex $j$ reached within $k$
rounds has partner $i$, that is, $\mu(j) = i$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.exists_mate_of_mem_layers`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#exists-mate-of-mem-layers).

## The left layers stop growing once two consecutive ones agree

For any partner array, if
the layered search reaches the same left vertices within $k$ rounds as within $k + 1$ rounds,
then for every $m \ge k$ it reaches exactly those left vertices within $m$ rounds.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.layers_fst_eq_of_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#layers-fst-eq-of-eq).

## Rounds $a$ and $a + 1$ reach the same left vertices

In a bipartite graph with $a$ left
vertices, for every partner array $\mu$, the alternating layered search for $\mu$ reaches the same
left vertices within $a + 1$ rounds as within $a$ rounds.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.layers_fst_stable`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#layers-fst-stable).

## Walking the layers back

Given the adjacency lists $\mathrm{adj}$ of a bipartite graph, a
partner assignment $\mathrm{mate}$, a level $k$ and a right vertex $j$, the walk back from $j$ at
level $k$ is a list of pairs defined by recursion on $k$. At level $0$ it is $[(i, j)]$ for the
least unmatched left vertex $i$ with $j \in \mathrm{adj}(i)$ and $\mathrm{mate}(j) \ne i$, and
empty if there is none. At level $k + 1$, if $j$ is reached within $k + 1$ rounds of the
alternating layered search, it is the walk back from $j$ at level $k$. Otherwise take the least
left vertex $i$ reached within $k + 1$ rounds with $j \in \mathrm{adj}(i)$ and
$\mathrm{mate}(j) \ne i$ (the walk is empty if there is none): if no right vertex has partner $i$
the walk is $[(i, j)]$, and otherwise it is $(i, j)$ followed by the walk back at level $k$ from
the least right vertex $j'$ with $\mathrm{mate}(j') = i$.

When $j$ is reached within $k + 1$ rounds, the walk descends to the round where $j$ is first
reached and lists the pairs to match, $j$ first.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.pathTo`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#path-to).

## Flipping a list of pairs

Let $\mu$ be a partner array, assigning to each right vertex
either a left partner or none, and let $P$ be a list of pairs $(i, j)$ of a left vertex $i$ and a
right vertex $j$. The flip of $\mu$ along $P$ sends each right vertex $j$ to the left vertex of
the first pair in $P$ whose right vertex is $j$, and to $\mu(j)$ (a partner or none) when no pair
of $P$ has right vertex $j$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.flip`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#flip).

## Alternating path

Let $\mu$ be a partner array, giving each right vertex at most one left
vertex as its partner, let $k$ be a natural number and $j$ a right vertex. A list $P$ of pairs
$(i, j')$ of a left vertex $i$ and a right vertex $j'$ is an alternating path from $j$ within
round $k$ when all of the following hold: $P$ is nonempty and its first pair has right vertex
$j$; for every pair $(i, j')$ of $P$, $j'$ is a neighbour of $i$ but $i$ is not the partner of
$j'$; for every pair $(i, j')$ of $P$, the alternating search from the unmatched left vertices
reaches $i$ within $k$ rounds and $j'$ within $k + 1$ rounds; no left vertex and no right vertex
occurs twice in $P$; for any two consecutive pairs $(i, j')$ and $(i', j'')$ of $P$, $i$ is the
partner of $j''$; and the left vertex of the last pair of $P$ is the partner of no right vertex.

When $j$ is unmatched as well, $P$ is an augmenting path.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.AltPath`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#alt-path).

## Augmenting path

Let $\mu$ be a partner array, $k$ a natural number and $j$ a right
vertex. A list $P$ of pairs of a left vertex and a right vertex is an augmenting path from $j$
within round $k$ when $P$ is an alternating path from $j$ within round $k$ and $j$ is unmatched:
$\mu$ gives $j$ no partner.

Since the last left vertex of an alternating path is unmatched, both endpoints of an augmenting
path are unmatched.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.IsAugmentingPath`, a structure declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#is-augmenting-path).

## The walk back is an alternating path

Let $\mathrm{mate}$ be a valid partner assignment.
For every level $k$ and every right vertex $j$ reached within $k + 1$ rounds of the alternating
layered search, the walk back from $j$ at level $k$ is an alternating path from $j$ at level $k$:
it starts at $j$, its pairs are non-matching edges, its left vertices are reached within $k$
rounds and its right vertices within $k + 1$ rounds, no vertex occurs twice, each right vertex
after the first is the partner of the previous left vertex, and the last left vertex is
unmatched.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.pathTo_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#path-to-spec).

## Flipping an alternating path keeps a matching

Let $\mu$ be a valid partner array (partners
are neighbours and no left vertex is the partner of two right vertices), and let $P$ be an
alternating path for $\mu$ from a right vertex $j$ with round bound $k$. Then the partner array
obtained from $\mu$ by matching each pair of $P$ and keeping the other partners is valid.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.valid_flip`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#valid-flip).

## Matched right vertices

Let $\mu$ give each right vertex $j$ of a bipartite graph at
most one partner $\mu(j)$ among the left vertices. The matched right vertices of $\mu$ are the
right vertices $j$ that have a partner $\mu(j)$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.matched`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 450](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L450). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#matched).

## Flipping an alternating path matches its first vertex

Let $\mu$ give each right
vertex of a bipartite graph at most one partner among the left vertices, and let $P$ be an
alternating path for $\mu$ starting at the right vertex $j$. Then the right vertices matched after
flipping $P$ are exactly $j$ and the right vertices matched under $\mu$.

The other right vertices of $P$ change partners but stay matched.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.matched_flip`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#matched-flip).

## The walk back from an unmatched reached vertex is an augmenting path

Let $\mu$ be a valid
partner array, $k$ a natural number and $j$ a right vertex that is unmatched and is reached within
$k + 1$ rounds of the alternating layered search for $\mu$. Then the walk back from $j$ at level
$k$ is an augmenting path from $j$ within round $k$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.pathTo_isAugmentingPath`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 482](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L482). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#path-to-is-augmenting-path).

## Flipping an augmenting path adds one matched vertex

If $P$ is an augmenting path for a
partner array $\mu$, then flipping $P$ in $\mu$ gives a partner array with exactly one more
matched right vertex than $\mu$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.card_matched_flip`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 488](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L488). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#card-matched-flip).

## One augmentation step

Let $\mu$ be a partner array on a bipartite graph with $a$ left
vertices and $b$ right vertices. Run the alternating search from the unmatched left vertices for
$a + 1$ rounds and take the first right vertex $j$, in the order $0, \dots, b - 1$, that is
unmatched and reached. If there is none, the step fails. Otherwise it returns the partner array
obtained from $\mu$ by flipping the path found by walking back from $j$ through the search
layers: every right vertex $j'$ on the path gets as partner the left vertex paired with it on the
path, and every other right vertex keeps its partner.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.augment`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 500](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L500). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#augment).

## Augmentation loop

Given a fuel $f \in \mathbb{N}$ and a partner array $\mu$ (assigning to
each right vertex at most one left partner), the loop returns $\mu$ when $f = 0$. When $f \ge 1$ it
performs one augmentation step on $\mu$: if the layered search reaches no unmatched right vertex,
the loop returns $\mu$; otherwise it runs with fuel $f - 1$ on the array that this step returns,
obtained by flipping the pairs walked back through the layers from the least-indexed unmatched
right vertex that the search reaches. Thus it augments while possible, at most $f$ times.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.maxMatchingAux`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 507](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L507). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#max-matching-aux).

## The augmenting-path maximum matching

In a bipartite graph with right vertices
$0, \dots, b-1$, the partner array obtained by running the augmentation loop with fuel $b + 1$ from
the empty matching, in which no right vertex has a partner.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.maxMatching`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 515](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L515). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#max-matching).

## Matched pairs and matched right vertices are equinumerous

For every partner array
$\mu$, the number of matched pairs $(i, j)$ of $\mu$, those with $\mu(j) = i$, equals the number
of matched right vertices of $\mu$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.card_pairs`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#card-pairs).

## A valid partner array gives a matching

Let each right vertex $j$ of a bipartite graph
have at most one partner, a left vertex. If the partners are valid for the graph (each partner of
$j$ is adjacent to $j$, and no left vertex is the partner of two right vertices), then the set of
pairs $(i, j)$ with $i$ the partner of $j$ is a matching of the graph.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.isMatching_pairs`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 535](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L535). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#is-matching-pairs).

## A successful augmentation grows the matching by one edge

Let $\mu$ be a partner array
that describes a matching. If the augmentation step on $\mu$ returns a partner array $\mu'$, then
$\mu'$ also describes a matching, and $\mu'$ has exactly one more matched right vertex than
$\mu$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.augment_some`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 547](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L547). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#augment-some).

## A failed augmentation reaches no unmatched right vertex

Let $\mu$ be a partner array on a
bipartite graph with $a$ left vertices. If the augmentation step on $\mu$ fails, then no unmatched
right vertex is reached within $a + 1$ rounds of the alternating search from the unmatched left
vertices.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.augment_none`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 563](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L563). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#augment-none).

## Kőnig's certificate

Let $\mu$ be a partner array on a bipartite graph with $a$ left
vertices that describes a matching. If no unmatched right vertex is reached within $a + 1$ rounds
of the alternating search from the unmatched left vertices, then no matching has more edges than
the matching of $\mu$: the unreached left vertices and the reached right vertices cover every
edge, and each of them is matched, to distinct matching edges.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.card_le_of_no_free`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 576](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L576). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#card-le-of-no-free).

## Enough augmentations reach a maximum matching

In a bipartite graph with right vertices
$0, \dots, b-1$, let $\mu$ be a valid partner array (it assigns to each right vertex at most one
left partner, partners are neighbours, and no left vertex is the partner of two right vertices).
Let $f \in \mathbb{N}$ satisfy $b < |\mathrm{matched}(\mu)| + f$, where $\mathrm{matched}(\mu)$ is
the set of right vertices with a partner, and let $\mu'$ be the result of the augmentation loop
from $\mu$ with fuel $f$. Then $\mu'$ is valid, and every matching $M$ of the graph satisfies
$|M| \le |\mathrm{pairs}(\mu')|$, where $\mathrm{pairs}(\mu')$ is the set of pairs $(i, j)$ with
$\mu'(j) = i$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.maxMatchingAux_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 627](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L627). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#max-matching-aux-spec).

## The augmenting-path algorithm returns a matching

For every bipartite graph with left
vertices $0, \dots, a-1$, right vertices $0, \dots, b-1$ and an adjacency list for each left
vertex, the pairs $(i, j)$ such that the augmenting-path maximum matching algorithm (from the
empty matching, repeatedly flip an augmenting path found by the layered search) makes $i$ the
partner of $j$ form a matching of the graph: each pair is an edge, and no two distinct pairs
share a left or a right vertex.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.isMatching_maxMatching`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 644](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L644). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#is-matching-max-matching).

## Optimality of the augmenting-path matching algorithm

In a bipartite graph with $b$ right
vertices, start from the empty matching and repeat the augmentation step until it fails, at most
$b + 1$ times. No matching of the graph has more edges than the resulting matching.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.card_le_maxMatching`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 648](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L648). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#card-le-max-matching).

## Partner of a left vertex

Given a partner assignment $\mathrm{mate}$ that sends each right
vertex $j < b$ to a left vertex $i < a$ or to nothing, the partner of a left vertex $i$ is the
least right vertex $j$ with $\mathrm{mate}(j) = i$; it is undefined when there is no such $j$,
that is, when $i$ is unmatched.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.partnerOf`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 657](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L657). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#partner-of).

## Marking a right vertex dead

Given a set $D$ of right vertices, represented by its
indicator function, and a right vertex $j$, the result is the indicator function of
$D \cup \{j\}$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.markDead`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 661](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L661). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#mark-dead).

## Trying the candidate predecessors of a right vertex

Let $j$ be a right vertex,
$\mathrm{ok}$ a test on left vertices, $\pi$ a map giving each left vertex an optional right vertex
(its partner, if any), and $s$ a search taking a right vertex and a dead set (a set of right
vertices) to an optional path, a list of pairs of a left and a right vertex, and a new dead set.
Given a list of left vertices and a dead set $D$, the procedure goes through the list in order,
skipping the vertices that fail $\mathrm{ok}$. At the first remaining vertex $i$: if $\pi(i)$ is
undefined, it returns the path $[(i, j)]$ and $D$; if $\pi(i) = j'$ and $s(j', D)$ finds a path
$P$, it returns the path $(i, j)$ followed by $P$, with the dead set returned by $s$; if
$s(j', D)$ finds no path, it continues with the rest of the list from the dead set returned by
$s$. When the list is exhausted, it fails and returns the current dead set with $j$ added.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.tryPreds`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 668](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L668). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#try-preds).

## Depth-first search of a Hopcroft–Karp phase

Fix a partner array $\mu$ assigning each right
vertex at most one left partner, and a set $U$ of used left vertices. Write $L_n$ and $R_n$ for
the left and right vertices reached within $n$ rounds of the alternating breadth-first layers of
$\mu$ (so $R_0 = \emptyset$). A left vertex $i$ is unmatched if no right vertex has partner $i$;
otherwise its partner is the least right vertex $j'$ with $\mu(j') = i$. The search from a right
vertex $j$ with bound $n$ and a set $D$ of dead right vertices returns an optional path (a list of
pairs of a left and a right vertex) together with a new dead set:

* if $j \in D$, it fails and returns $D$ unchanged;
* otherwise, if $j \in R_n$, it is the search from $j$ with bound $n - 1$ and dead set $D$;
* otherwise it goes through the candidates, the left vertices $i \in L_n$ in increasing order with
  $j$ adjacent to $i$, $\mu(j) \ne i$ and $i \notin U$. For an unmatched candidate $i$ it returns
  the path $[(i, j)]$ and the current dead set. For a matched candidate $i$ it searches from the
  partner of $i$ with bound $n - 1$ and the current dead set (when $n = 0$ this search fails and
  returns the dead set unchanged); if that search finds a path $P$, it returns $(i, j)$ followed
  by $P$, with the dead set that search returned, and otherwise it moves on to the next candidate
  with the dead set that search returned. If every candidate fails, it fails and returns the
  current dead set with $j$ added.

This is the pruning of Hopcroft and Karp: a right vertex from which the search fails is marked
dead and not searched again.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.searchPath`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 688](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L688). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#search-path).

## Trying candidates keeps dead vertices dead

For a right vertex $j$, a test $\mathrm{ok}$ on left vertices, a map $\pi$ giving each left vertex
an optional right vertex, and a search $s$ taking a right vertex and a dead set (a set of right
vertices) to an optional path and a new dead set, write $T(l, D)$ for the optional path and the
dead set returned by trying the left vertices of the list $l$ as predecessors of $j$, starting from
the dead set $D$.
Suppose $s$ never shrinks the dead set: for every right vertex $j'$ and every dead set $d$, the
dead set returned by $s(j', d)$ contains $d$.
Then for every list $l$ of left vertices and every dead set $D$, the dead set of $T(l, D)$
contains $D$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.tryPreds_mono`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 721](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L721). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#try-preds-mono).

## A path found by trying candidates comes from one candidate

For a right vertex $j$, a test $\mathrm{ok}$ on left vertices, a map $\pi$ giving each left vertex
an optional right vertex, and a search $s$ taking a right vertex and a dead set (a set of right
vertices) to an optional path and a new dead set, write $T(l, D)$ for the optional path and the
dead set returned by trying the left vertices of the list $l$ as predecessors of $j$, starting from
the dead set $D$.
Suppose $s$ never shrinks the dead set: for every right vertex $j'$ and every dead set $d$, the
dead set returned by $s(j', d)$ contains $d$.
If $T(l, D)$ returns a path $P$, then there are a vertex $i$ of $l$ with $\mathrm{ok}(i)$ and a
dead set $D_0$ containing $D$ such that either $\pi(i)$ is undefined and $P = [(i, j)]$, or
$\pi(i) = j'$ for a right vertex $j'$ and $s(j', D_0)$ returns a path $P'$ with $P$ equal to
$(i, j)$ followed by $P'$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.tryPreds_some`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 745](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L745). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#try-preds-some).

## When trying candidates finds a path

For a right vertex $j$, a test $\mathrm{ok}$ on left vertices, a map $\pi$ giving each left vertex
an optional right vertex, and a search $s$ taking a right vertex and a dead set (a set of right
vertices) to an optional path and a new dead set, write $T(l, D)$ for the optional path and the
dead set returned by trying the left vertices of the list $l$ as predecessors of $j$, starting from
the dead set $D$.
Suppose some vertex of $l$ passes $\mathrm{ok}$, and for every vertex $i$ of $l$ passing
$\mathrm{ok}$ and every right vertex $j'$ with $\pi(i) = j'$, the search $s(j', D)$ finds a path.
Then $T(l, D)$ finds a path.

Only the initial dead set matters: it does not change before the first vertex passing
$\mathrm{ok}$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.tryPreds_isSome`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 778](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L778). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#try-preds-is-some).

## The dead set of a search only grows

For every set of used left vertices, every level
$k$, every right vertex $j$ and every set of dead right vertices, each right vertex that is dead
before the search at level $k$ from $j$ is still dead after it.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.searchPath_mono`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 808](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L808). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#search-path-mono).

## Search paths are alternating paths through unused vertices

Suppose the partner array
describes a matching, $k$ is a level and $j$ is a right vertex reached within $k + 1$ rounds of the
alternating breadth-first search. For every set of used left vertices and every set of dead right
vertices, if the search at level $k$ from $j$ finds a path $P$, then $P$ is an alternating path at
level $k$ from $j$, no left vertex of $P$ is used, and no right vertex of $P$ was dead before the
search.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.searchPath_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 824](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L824). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#search-path-spec).

## Searches from reached vertices succeed when nothing is used or dead

If the partner array
describes a matching, then for every $k$ and every right vertex $j$ reached within $k + 1$ rounds
of the alternating breadth-first search, the search at level $k$ from $j$, with no left vertex
used and no right vertex dead, finds a path.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.searchPath_isSome`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 908](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L908). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#search-path-is-some).

## Marking the left vertices of a path used

Given a set $U$ of left vertices, represented
by its indicator function, and a list $P$ of pairs $(i, j)$ of a left vertex $i$ and a right
vertex $j$, the result is the indicator function of $U$ together with the left vertices of the
pairs of $P$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.markL`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 936](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L936). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#mark-l).

## Marking the right vertices of a path used

Given a set $U$ of right vertices,
represented by its indicator function, and a list $P$ of pairs $(i, j)$ of a left vertex $i$ and
a right vertex $j$, the result is the indicator function of $U$ together with the right vertices
of the pairs of $P$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.markR`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 940](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L940). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#mark-r).

## Phase search over candidates

Given a partner assignment $\mathrm{mate}$, a level $k$, a
list of candidate right vertices, a set $U$ of used left vertices and a set $D$ of used or dead
right vertices, the phase search tries the candidates in order. For a candidate $j$ it runs the
layered depth-first search from $j$ at level $k$ with used left vertices $U$ and dead set $D$,
which returns an optional path and an enlarged dead set $D'$. If it finds no path, the phase
search continues with the remaining candidates, $U$ and $D'$; if it finds a path $P$, it records
$P$ and continues with the remaining candidates, $U$ together with the left vertices of $P$, and
$D'$ together with the right vertices of $P$. The result is the list of the recorded paths.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.phaseAux`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 946](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L946). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#phase-aux).

## First free round

For a partner array $\mu$ of a bipartite graph with $a$ left vertices,
the first free round of $\mu$ is the least $d \le a$ such that some unmatched right vertex is
reached within $d + 1$ rounds of the layered search; it is undefined if there is no such $d$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.firstFreeRound`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 956](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L956). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#first-free-round).

## Hopcroft–Karp phase

If no round of the alternating breadth-first search reaches an
unmatched right vertex, the phase finds no path. Otherwise let $d$ be the earliest round such that
round $d + 1$ reaches one. The phase runs the search at level $d$ from each unmatched right vertex
reached within $d + 1$ rounds, in increasing order, starting with no left vertex used and no right
vertex dead, and lists the paths found. After each search, the left vertices of the path found
become used and its right vertices become dead, and right vertices that the search marked dead
stay dead for the later searches.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.phase`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 962](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L962). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#phase).

## Hopcroft–Karp step

Given a partner array $\mu$, consider the phase of $\mu$, a list of
paths, each a list of pairs. If the phase is empty, the step returns nothing; otherwise it returns
the flip of $\mu$ along the concatenation of all the paths of the phase.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.hkStep`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 971](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L971). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#hk-step).

## Hopcroft–Karp phase loop

Given a fuel $n \in \mathbb{N}$ and a partner array $\mu$, the
loop returns $\mu$ when $n = 0$ or when the Hopcroft–Karp step on $\mu$ returns nothing; when
$n \ge 1$ and the step returns a partner array $\mu'$, it returns the loop with fuel $n - 1$ run
from $\mu'$. So it runs Hopcroft–Karp steps while they find paths, at most $n$ times.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.hopcroftKarpAux`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 976](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L976). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#hopcroft-karp-aux).

## Hopcroft–Karp

Let a bipartite graph have left vertices $0, \dots, a-1$, right
vertices $0, \dots, b-1$ and an adjacency list for each left vertex. Starting from the empty
matching, the Hopcroft–Karp algorithm runs phases, at most $b + 1$ of them, and stops early at
the first phase that finds no path: each phase computes the layered search once, collects
vertex-disjoint augmenting paths from the unmatched right vertices reached in the earliest round
that reaches any, and flips all of them at once. The result is the final matching, given as the
partner (or the absence of one) of each right vertex.

The result is a maximum matching.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.hopcroftKarp`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 984](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L984). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#hopcroft-karp).

## Characterization of the first free round

For a partner array $\mu$ of a bipartite graph
with $a$ left vertices and a natural number $d$, the first free round of $\mu$ equals $d$ if and
only if $d \le a$, some unmatched right vertex is reached within $d + 1$ rounds of the layered
search, and for every $k < d$ no unmatched right vertex is reached within $k + 1$ rounds.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.firstFreeRound_eq_some`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1000](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1000). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#first-free-round-eq-some).

## When there is no first free round

For a partner array $\mu$ of a bipartite graph with
$a$ left vertices, the first free round of $\mu$ is undefined if and only if no unmatched right
vertex is reached within $a + 1$ rounds of the layered search.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.firstFreeRound_eq_none`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1010](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1010). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#first-free-round-eq-none).

## Phase paths are disjoint augmenting paths

Let $\mathrm{mate}$ be a valid partner
assignment, $k$ a level, $J$ a list of right vertices each unmatched and reached within $k + 1$
rounds of the alternating layered search, and $U_L$, $U_R$ sets of left and right vertices. Then
every path that the phase search at level $k$ collects from $J$ with used left vertices $U_L$ and
used right vertices $U_R$ is an augmenting path from some right vertex, with left vertices reached
within $k$ rounds and right vertices within $k + 1$ rounds; no left vertex and no right vertex
occurs twice among all pairs of all these paths; and every pair $(i, j)$ of these paths has
$i \notin U_L$ and $j \notin U_R$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.phaseAux_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1020](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1020). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#phase-aux-spec).

## Flipping disjoint alternating paths at once keeps a matching

Let $\mu$ be a valid partner
array (partners are neighbours and no left vertex is the partner of two right vertices), $k$ a
natural number, and $P_1, \dots, P_r$ paths each of which is an alternating path for $\mu$, with
round bound $k$, from some right vertex. Suppose no left vertex and no right vertex occurs twice in
the concatenation $P_1 \cdots P_r$. Then the partner array obtained from $\mu$ by matching each
pair of the concatenation and keeping the other partners is valid.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.valid_flip_flatten`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1077](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1077). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#valid-flip-flatten).

## Flipping disjoint augmenting paths matches at least one more vertex

Let $\mu$ be a
partner array and let $P_1, \dots, P_n$, with $n \ge 1$, be augmenting paths for $\mu$, all for
the same number $k$ of search rounds, such that no right vertex occurs twice in the concatenation
$P_1 P_2 \cdots P_n$. Then flipping this concatenation in $\mu$ gives a partner array with at
least one more matched right vertex than $\mu$: the right vertices matched before stay matched,
and so does the start of the first path.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.card_matched_flip_flatten`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#card-matched-flip-flatten).

## A phase finds a path when an unmatched right vertex is reached

If the partner array
describes a matching and some unmatched right vertex is reached within $a + 1$ rounds of the
alternating breadth-first search, where $a$ is the number of left vertices, then the phase finds
at least one path.

The search from the first candidate always yields a path.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.phase_ne_nil`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#phase-ne-nil).

## A successful Hopcroft–Karp step grows the matching

Let $\mu$ be a valid partner array (a
matching of the graph). If the Hopcroft–Karp step on $\mu$ returns a partner array $\mu'$, then
$\mu'$ is valid and $|\mathrm{matched}(\mu)| + 1 \le |\mathrm{matched}(\mu')|$, where
$\mathrm{matched}(\nu)$ is the set of right vertices that have a partner in $\nu$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.hkStep_some`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#hk-step-some).

## A Hopcroft–Karp step that finds nothing

Let $\mu$ be a valid partner array (a matching of
the graph, whose left vertices number $a$). If the Hopcroft–Karp step on $\mu$ returns nothing,
then no right vertex without a partner in $\mu$ is reached within $a + 1$ rounds of the
alternating breadth-first layers of $\mu$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.hkStep_none`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#hk-step-none).

## Correctness of the phase loop

Let $\mu$ be a valid partner array (a matching of the
graph) on $b$ right vertices, and let $n \in \mathbb{N}$ be a fuel with
$b < |\mathrm{matched}(\mu)| + n$, where $\mathrm{matched}(\mu)$ is the set of right vertices with
a partner in $\mu$; so $n$ exceeds the number of unmatched right vertices. Let $\mu'$ be the
result of the Hopcroft–Karp phase loop with fuel $n$ from $\mu$. Then $\mu'$ is valid, and every
matching $M$ of the graph satisfies $|M| \le |\mathrm{pairs}(\mu')|$, where $\mathrm{pairs}(\mu')$
is the set of pairs $(i, j)$ with $\mu'(j) = i$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.hopcroftKarpAux_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#hopcroft-karp-aux-spec).

## Hopcroft–Karp returns a matching

For every bipartite graph with left vertices
$0, \dots, a-1$, right vertices $0, \dots, b-1$ and an adjacency list for each left vertex, the
pairs $(i, j)$ such that the Hopcroft–Karp algorithm makes $i$ the partner of $j$ form a matching
of the graph: each pair is an edge, and no two distinct pairs share a left or a right vertex.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.isMatching_hopcroftKarp`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#is-matching-hopcroft-karp).

## Correctness of Hopcroft–Karp

No matching is larger than the result.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.card_le_hopcroftKarp`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#card-le-hopcroft-karp).

## The start of an alternating chain of $L$ pairs is reached within $L$ rounds

Let $\mu$ be
a partner array, let $L \ge 1$, and let $(i_1, j_1), \dots, (i_L, j_L)$ be pairs of a left and a
right vertex such that each $j_t$ is adjacent to $i_t$ with $\mu(j_t) \ne i_t$, each $j_{t+1}$ has
partner $\mu(j_{t+1}) = i_t$ for $t < L$, and $i_L$ is unmatched. Then $j_1$ is among the right
vertices reached within $L$ rounds of the alternating layered search for $\mu$.

From the unmatched end, each pair advances one round.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.mem_layers_length`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#mem-layers-length).

## No augmenting path is shorter than a phase's

Let $\mu$ give each right vertex of a
bipartite graph at most one partner among the left vertices. If the first free round of $\mu$ is
$d$, then every augmenting path for $\mu$ has at least $d + 1$ pairs.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.le_length_of_isAugmentingPath`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#le-length-of-is-augmenting-path).

## Length bound for search paths

For every set of used left vertices, every level $k$,
every right vertex $j$ and every set of dead right vertices, a path found by the search at level
$k$ from $j$ has at most $k + 1$ pairs.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.searchPath_length_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#search-path-length-le).

## Length bound for phase paths

For every partner assignment $\mathrm{mate}$, level $k$,
list of candidate right vertices and sets of used left and right vertices, every path that the
phase search at level $k$ collects from these candidates has at most $k + 1$ pairs.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.phaseAux_length_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#phase-aux-length-le).

## Phases use shortest augmenting paths

Let $\mu$ be a valid partner assignment of a
bipartite graph (a matching) whose first free round is $d$. Then every path of the phase of $\mu$
has exactly $d + 1$ pairs.

Every augmenting path for $\mu$ has at least $d + 1$ pairs, so these paths are shortest
augmenting paths.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.length_of_mem_phase`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1314](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#length-of-mem-phase).

## Exact level of a right vertex

For a partner array $\mu$, a natural number $m$ and a
right vertex $z$, $z$ has exact level $m$ when $z$ is first reached in round $m + 1$ of the
layered search for $\mu$: it is reached within $m + 1$ rounds but not within $m$ rounds.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.ExactLevel`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1327](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#exact-level).

## Alternating chain to an unmatched left vertex

In a bipartite graph, let each right vertex
have at most one partner, a left vertex (the partners need not form a matching), and let $z$ be a
right vertex. A list $Q$ of pairs (left vertex, right vertex) is an alternating chain from $z$
when its first pair has right vertex $z$, each of its pairs $(i, j)$ is an edge with $i$ not the
partner of $j$, each right vertex after the first is the partner of the preceding left vertex,
and its last left vertex is the partner of no right vertex.

Unlike an augmenting path, $z$ may be matched, the vertices need not lie in the layers of the
search, and a vertex may occur more than once.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.IsChainFrom`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#is-chain-from).

## No shortest escape

Let $\mu$ be a partner array, $U$ a set of left vertices, $D$ a set of
right vertices and $z$ a right vertex. Then $z$ has no escape avoiding $U$ and $D$ when there are
no $m \in \mathbb{N}$ and no list of pairs $(i_1, j_1), \dots, (i_{m+1}, j_{m+1})$ such that $z$ is
first reached in round $m + 1$ of the alternating layered search for $\mu$, the list is an
alternating chain from $z$, no $i_t$ lies in $U$, and no $j_t$ with $t \ge 2$ lies in $D$. Here
the list is an alternating chain from $z$ when $j_1 = z$, each $j_t$ is adjacent to $i_t$ with
$\mu(j_t) \ne i_t$, $\mu(j_{t+1}) = i_t$ for $t \le m$, and $i_{m+1}$ is unmatched.

A phase gives this property to every right vertex it marks dead after a failed search.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.NoEscape`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1340](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#no-escape).

## The second pair of a shortest alternating chain

Let $\mu$ be a partner array and $z$ a
right vertex first reached in round $m + 1$ of the alternating breadth-first layers of $\mu$, and
let $Q$ be an alternating chain for $\mu$ from $z$ ending at an unmatched left vertex, with exactly
$m + 1$ pairs, at least two of them. Let $(i', j')$ be the second pair of $Q$. Then $m \ge 1$, the
right vertex $j'$ is first reached in round $m$, and $Q$ without its first pair is an alternating
chain for $\mu$ from $j'$ ending at an unmatched left vertex.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.ExactLevel.tail`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1373](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#tail).

## Partners of predecessors lie one level earlier

Let $\mathrm{mate}$ be a valid partner
assignment for the bipartite graph with adjacency lists $\mathrm{adj}$. Let $z$ be a right
vertex first reached in round $k + 2$ of the alternating layered search, let $i$ be a left vertex
reached within $k + 1$ rounds with $z \in \mathrm{adj}(i)$ and $\mathrm{mate}(z) \ne i$, and let
$j'$ be a right vertex with $\mathrm{mate}(j') = i$. Then $j'$ is first reached in round
$k + 1$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.ExactLevel.partner`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#partner).

## Where newly dead vertices come from

For a right vertex $j$, a test $\mathrm{ok}$ on left vertices, a map $\pi$ giving each left vertex
an optional right vertex, and a search $s$ taking a right vertex and a dead set (a set of right
vertices) to an optional path and a new dead set, write $T(l, D)$ for the optional path and the
dead set returned by trying the left vertices of the list $l$ as predecessors of $j$, starting from
the dead set $D$.
Suppose $s$ never shrinks the dead set: for every right vertex $j'$ and every dead set $d$, the
dead set returned by $s(j', d)$ contains $d$.
Let $E$ be the dead set of $T(l, D)$ and let $y$ be a right vertex in $E$ but not in $D$. Then
either $T(l, D)$ finds no path and $y = j$, or there are a vertex $i$ of $l$ passing
$\mathrm{ok}$, a right vertex $j'$ and a dead set $d$ containing $D$ such that $\pi(i) = j'$,
$y \notin d$, $y$ is in the dead set returned by $s(j', d)$, and that dead set is contained in
$E$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.tryPreds_dead`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1414](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1414). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#try-preds-dead).

## When trying candidates fails

For a right vertex $j$, a test $\mathrm{ok}$ on left vertices, a map $\pi$ giving each left vertex
an optional right vertex, and a search $s$ taking a right vertex and a dead set (a set of right
vertices) to an optional path and a new dead set, write $T(l, D)$ for the optional path and the
dead set returned by trying the left vertices of the list $l$ as predecessors of $j$, starting from
the dead set $D$.
Suppose $s$ never shrinks the dead set: for every right vertex $j'$ and every dead set $d$, the
dead set returned by $s(j', d)$ contains $d$.
If $T(l, D)$ finds no path, then $j$ is in the dead set $E$ of $T(l, D)$, and for every vertex $i$
of $l$ passing $\mathrm{ok}$ there are a right vertex $j'$ and a dead set $d$ such that
$\pi(i) = j'$, $s(j', d)$ finds no path, and the dead set returned by $s(j', d)$ is contained in
$E$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.tryPreds_none`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1470](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1470). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#try-preds-none).

## A failed search marks its start dead

For every set of used left vertices, every level
$k$, every right vertex $z$ and every set of dead right vertices, if the search at level $k$ from
$z$ finds no path, then $z$ is dead after it.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.searchPath_none_marks`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1504](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1504). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#search-path-none-marks).

## Dead vertices have no escape

Suppose the partner array describes a matching. Run the
search at level $k$ from a right vertex $z$ first reached in round $k + 1$, with a set $U$ of used
left vertices and an initial set $D$ of dead right vertices, and let $D'$ be the dead set after
it. Then every right vertex $y$ in $D'$ but not in $D$ has no escape avoiding $U$ and $D'$: if $y$
is first reached in round $m + 1$, no alternating chain from $y$ to an unmatched left vertex with
$m + 1$ pairs has all its left vertices outside $U$ and all its right vertices after $y$ outside
$D'$.

So Hopcroft and Karp's pruning loses no path.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.searchPath_dead`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1521](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1521). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#search-path-dead).

## Shortest chains avoiding earlier paths contain no dead vertex

Let $\mu$ be a partner
array, $U$ a set of left vertices and $D$ a set of right vertices, and let $L$ be a set of left
vertices and $R$ a set of right vertices such that every vertex of $U$ lies in $L$ and every
vertex of $D$ lies in $R$ or has no escape avoiding $U$ and $D$. Let $m \in \mathbb{N}$, let $z$ be
a right vertex first reached in round $m + 1$ of the alternating layered search for $\mu$, and let
$S$ be an alternating chain from $z$ with $m + 1$ pairs such that no left vertex of $S$ lies in $L$
and no right vertex of $S$ lies in $R$. Then no right vertex of $S$ lies in $D$.

In a phase, $L$ and $R$ are the left and right vertices of the paths found so far.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.not_dead_of_chain`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1594](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1594). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#not-dead-of-chain).

## Invariant of a phase

Let $\mathrm{mate}$ be a valid partner assignment, let $j$ be a
right vertex first reached in round $d + 1$ of the alternating layered search, and let $Q$ be an
alternating chain from $j$ with $d + 1$ pairs. Let $J$ be a list of right vertices each first
reached in round $d + 1$, $U$ a set of left vertices, $D$ a set of right vertices and $F$ a list of
paths, such that every vertex in $U$ is a left vertex of a path in $F$, and every vertex in $D$
either has no escape avoiding $U$ and $D$ or is a right vertex of a path in $F$. If $j$ is in $J$
or in $D$, then some path in $F$, or among the paths that the phase search at level $d$ collects
from $J$ with used left vertices $U$ and used right vertices $D$, shares a left vertex or a right
vertex with $Q$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.phaseAux_maximal`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1629](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1629). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#phase-aux-maximal).

## Phases are maximal

Suppose the partner array describes a matching and $d$ is the earliest
round such that round $d + 1$ of the alternating breadth-first search reaches an unmatched right
vertex. Then for every $k$, every augmenting path $Q$ at level $k$ with exactly $d + 1$ pairs
shares a vertex with some path $P$ of the phase: some pair of $Q$ has its left vertex among the
left vertices of $P$ or its right vertex among the right vertices of $P$.

Every augmenting path has at least $d + 1$ pairs, so these are the shortest augmenting paths, and
the phase's vertex-disjoint shortest augmenting paths form a maximal set, as Hopcroft and Karp
require.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.phase_maximal`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1726](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1726). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#phase-maximal).

## A matched right vertex is reached no later than its partner

Let $\mu$ be a valid partner
array (partners are neighbours, and no left vertex is the partner of two right vertices), let $j$
be a right vertex with partner $\mu(j) = i$, and let $k \in \mathbb{N}$. If $i$ is among the left
vertices reached within $k$ rounds of the alternating layered search for $\mu$, then $j$ is among
the right vertices reached within $k$ rounds.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.mem_layers_snd_of_mate`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1763](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1763). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#mem-layers-snd-of-mate).

## Levels along a shortest alternating chain

Let $\mu$ be a partner array, let
$m \in \mathbb{N}$, let $z$ be a right vertex first reached in round $m + 1$ of the alternating
layered search for $\mu$, and let $S$ be an alternating chain from $z$ with $m + 1$ pairs. Then
for every pair $(i, j)$ of $S$ there is $m' \in \mathbb{N}$ such that $j$ is first reached in round
$m' + 1$ and $i$ is reached within $m'$ rounds.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.pair_levels_of_chain`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1770](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1770). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#pair-levels-of-chain).

## Levels of the pairs of a phase

In a bipartite graph with left vertices $0, \dots, a-1$, let
$\mu$ be a valid partner array (partners are neighbours, and no left vertex is the partner of two
right vertices), and let $d \le a$ be such that round $d + 1$ of the alternating layered search for
$\mu$ reaches an unmatched right vertex and no earlier round does. Then for every pair $(i, j)$ on
a path of the Hopcroft–Karp phase for $\mu$ there is $m \in \mathbb{N}$ such that $j$ is first
reached in round $m + 1$ and $i$ is among the left vertices reached within $m$ rounds.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.pair_levels_of_mem_phase`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1796](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1796). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#pair-levels-of-mem-phase).

## A phase leaves no new unmatched left vertex

Let $\mu$ be a valid partner array (a
matching of the graph) whose first free round is defined, equal to some $d$. If a left vertex $i$
is unmatched in the flip of $\mu$ along the concatenation of all the paths of the phase of $\mu$,
then $i$ is unmatched in $\mu$.

The first pair of each path starts at an unmatched right vertex, and every other right vertex of a
path had the previous left vertex as partner, which the phase rematches.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.free_of_free_flip`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1824](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1824). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#free-of-free-flip).

## Distances do not decrease across a phase

Let the partner array of a bipartite graph with
$a$ left vertices be valid, and suppose that some round $r \le a + 1$ of the layered search
reaches an unmatched right vertex, so that a phase runs from the earliest such round. After
flipping all the paths that phase finds, for every $k \in \mathbb{N}$ the left vertices and the
right vertices reached within $k$ rounds of the layered search were already reached within $k$
rounds before the flip.

This is a step of Hopcroft and Karp's analysis.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.layers_flip_phase_subset`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1855](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1855). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#layers-flip-phase-subset).

## The first free round does not decrease across a phase

Let $\mu$ be a valid partner
assignment of a bipartite graph (a matching), and let $\mu'$ be obtained from $\mu$ by flipping
all the paths of the phase of $\mu$ at once. If the first free round of $\mu$ is $d$ and the first
free round of $\mu'$ is $d'$, then $d \le d'$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.le_firstFreeRound_flip_phase`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1890](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1890). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#le-first-free-round-flip-phase).

## The paths of a phase are vertex-disjoint augmenting paths

Suppose the partner array
describes a matching and $d$ is the earliest round such that round $d + 1$ of the alternating
breadth-first search reaches an unmatched right vertex. Then every path of the phase is an
augmenting path at level $d$ from some right vertex, and no left vertex and no right vertex occurs
twice among the pairs of all the paths of the phase.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.phase_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1908](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1908). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#phase-spec).

## Shortest chains from a vertex whose level a phase keeps were chains before it

Let $\mu$
be a valid partner array whose first free round is defined, and let $\mu'$ be obtained from $\mu$
by flipping all the paths of the phase of $\mu$. Let $z$ be a right vertex and $m$ a natural
number such that $z$ is first reached in round $m + 1$ of the layered search both for $\mu$ and
for $\mu'$, and let $S$ be an alternating chain for $\mu'$ from $z$ to an unmatched left vertex
with exactly $m + 1$ pairs. Then $S$ is also an alternating chain for $\mu$ from $z$ to an
unmatched left vertex, and for every pair of $S$ after the first, its right vertex is not the
right vertex of any pair on the paths of the phase.

A flipped edge would step back a round, which a chain of this length cannot afford.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.chain_of_chain_flip_phase`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1920](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1920). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#chain-of-chain-flip-phase).

## The next phase's paths are strictly longer

**The next phase's paths are strictly longer** (Hopcroft and Karp). Let $\mu$ be a valid
partner assignment of a bipartite graph (a matching), and let $\mu'$ be obtained from $\mu$ by
flipping all the paths of the phase of $\mu$ at once. If the first free round of $\mu$ is $d$ and
the first free round of $\mu'$ is $d'$, then $d < d'$.

A shortest augmenting path for $\mu'$ of the same length would be a shortest augmenting chain for
$\mu$ that is disjoint from the paths of the phase, contradicting the maximality of the phase.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.lt_firstFreeRound_flip_phase`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 1991](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L1991). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#lt-first-free-round-flip-phase).

## One round of the layered search bounds the deficit

If no unmatched right vertex is reached
by round `k + 1`, every matching has at most as many edges as the current one plus the right
vertices first reached in round `k + 1`: the unreached left vertices and the right vertices reached
by round `k + 1` cover every edge.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.card_le_card_pairs_add`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 2093](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L2093). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#card-le-card-pairs-add).

## The deficit is at most $b / d$

In a bipartite graph with right vertices $0, \dots, b-1$,
let $\mu$ be a valid partner array (partners are neighbours, and no left vertex is the partner of
two right vertices), let $M$ be any matching of the graph, and let $d \in \mathbb{N}$. Suppose that
for every $k < d$, no unmatched right vertex is among the right vertices reached within $k + 1$
rounds of the alternating layered search for $\mu$. Then $d \cdot \max(|M| - |P_\mu|, 0) \le |R_d|$,
where $P_\mu$ is the set of pairs $(i, j)$ with $\mu(j) = i$ and $R_d$ is the set of right vertices
reached within $d$ rounds.

This is the counting step of Hopcroft and Karp's bound: since $R_d$ has at most $b$ elements, the
deficit of the current matching against any matching is at most $b / d$ when $d \ge 1$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.mul_card_sub_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 2147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L2147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#mul-card-sub-le).

## The phase loop stops when a step finds nothing

If the Hopcroft–Karp step on a partner
array $\mu$ returns nothing, then for every fuel $f \in \mathbb{N}$ the Hopcroft–Karp phase loop
with fuel $f$ from $\mu$ returns $\mu$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.hopcroftKarpAux_of_hkStep_none`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 2162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L2162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#hopcroft-karp-aux-of-hk-step-none).

## Fuel adds up in the phase loop

For all $f, g \in \mathbb{N}$ and every partner array
$\mu$, the Hopcroft–Karp phase loop with fuel $f + g$ from $\mu$ returns the same partner array as
the loop with fuel $g$ run from the result of the loop with fuel $f$ from $\mu$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.hopcroftKarpAux_add`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 2168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L2168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#hopcroft-karp-aux-add).

## Each phase lengthens the shortest augmenting paths

Let $\mu$ be a valid partner array
and $c$ a natural number such that the first free round of $\mu$, if defined, is at least $c$.
For every natural number $f$, running at most $f$ Hopcroft–Karp phases from $\mu$, stopping
early when a phase finds no path, gives a valid partner array whose first free round, if
defined, is at least $c + f$.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.firstFreeRound_hopcroftKarpAux`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 2183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L2183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#first-free-round-hopcroft-karp-aux).

## Closing a deficit of $f$ in $f$ Hopcroft–Karp phases

Let $\mu$ be a valid partner array,
$M$ a matching of the bipartite graph and $f \in \mathbb{N}$. If $M$ has at most $f$ more pairs
than the matched pairs of $\mu$, then $M$ has at most as many pairs as the matched pairs of the
partner array returned by the Hopcroft–Karp phase loop with fuel $f$ from $\mu$.

Each phase that finds a path adds at least one edge, and a phase that finds none leaves a maximum
matching.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.card_le_hopcroftKarpAux_of_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 2218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L2218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#card-le-hopcroft-karp-aux-of-le).

## Hopcroft and Karp's bound on the number of phases

In a bipartite graph with $b$ right
vertices, run at most $2 \lfloor \sqrt{b} \rfloor + 2$ Hopcroft–Karp phases from the empty
matching, stopping early when a phase finds no augmenting path. Then no matching of the graph has
more edges than the resulting one.

After the first $\lfloor \sqrt{b} \rfloor + 1$ phases every augmenting path has more than
$\lfloor \sqrt{b} \rfloor$ pairs, so the deficit against any matching is at most
$\lfloor \sqrt{b} \rfloor$, and each further phase adds an edge.

Formalized by `Cslib.Algorithms.Lean.BipartiteMatching.card_le_hopcroftKarpAux_sqrt`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean, line 2238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/BipartiteMatching.lean#L2238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html#card-le-hopcroft-karp-aux-sqrt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximum bipartite matching](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/graph-algorithms/spanning-trees-flows-matchings/maximum-bipartite-matching)
