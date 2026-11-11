---
declaration: section
origin: cited
lean: MetaMathlibExt.TruncatedSucc, MetaMathlibExt.IsKCyclicPartition, MetaMathlibExt.LinearPartition
statement: formalized
proof: formalized
---

# Graphical Stirling and Lah numbers

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/graphical-stirling-and-lah-numbers/index.html).

## Truncated-cycle successor

Let $\sigma$ be a permutation of a finite linearly ordered
set $V$ and let $i, j \in V$. Then $j$ is the truncated-cycle successor $\sigma^{(i)}(i)$ of $i$
when $j$ is the first of the iterates $\sigma(i), \sigma^2(i), \dots$ that is at most $i$: there
is an $m > 0$ with $\sigma^m(i) = j$ and $j \le i$, and $\sigma^{m'}(i) > i$ for every $m'$ with
$0 < m' < m$.

Formalized by `MetaMathlibExt.TruncatedSucc`, a definition declared in [MathlibExt/Combinatorics/KCyclicPartition.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/KCyclicPartition.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/graphical-stirling-and-lah-numbers/index.html#truncated-succ).

## $k$-cyclic partition

Let $V$ be a finite linearly ordered set, $\sigma$ a
permutation of $V$, $E$ a relation on $V$ (the directed edges of a labeled graph) and $k$ a
natural number. Then $\sigma$ is a $k$-cyclic partition for $E$ when $\sigma$ has exactly $k$
cycles, fixed points counted as cycles of length one, and for all $i, j \in V$, if $j$ is the
truncated-cycle successor of $i$ under $\sigma$ (the first of $\sigma(i), \sigma^2(i), \dots$
that is at most $i$), then $E(i, j)$ does not hold.

## Sources

- Gonzales, <https://cs.uwaterloo.ca/journals/JIS/VOL25/Gonzales/gonzales2.tex>, lines 345–346.

Formalized by `MetaMathlibExt.IsKCyclicPartition`, a definition declared in [MathlibExt/Combinatorics/KCyclicPartition.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/KCyclicPartition.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/graphical-stirling-and-lah-numbers/index.html#is-kcyclic-partition).

## Linear partition of a graph

Let $G$ be a simple graph on a vertex type $V$ and let $k$
be a natural number. A $k$-linear partition of $G$ is a set of exactly $k$ blocks, each block a
nonempty finite sequence of pairwise distinct vertices, such that every vertex of $G$ lies in
exactly one block and any two consecutive vertices of a block are nonadjacent in $G$. The
blocks themselves are unordered; only the vertices within a block are ordered.

## Sources

- Gonzales, JIS VOL25, <https://cs.uwaterloo.ca/journals/JIS/VOL25/Gonzales/gonzales2.tex>.

Formalized by `MetaMathlibExt.LinearPartition`, a structure declared in [MathlibExt/Combinatorics/LinearPartition.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/LinearPartition.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/graphical-stirling-and-lah-numbers/index.html#linear-partition).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Graphical Stirling and Lah numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/graphical-stirling-and-lah-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/graphical-stirling-and-lah-numbers)
