---
declaration: section
origin: cited
lean: MetaMathlibExt.robbins_theorem_connected, MetaMathlibExt.robbins_theorem
statement: formalized
proof: formalized
---

# Robbins' theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/robbins-theorem/index.html).

## Robbins' theorem

Let $G$ be a simple graph on a finite nonempty vertex set $V$. Then $G$
is connected and, after deleting any single edge of $G$, every vertex is still reachable from
every vertex (that is, $G$ is 2-edge-connected) if and only if $G$ has a strongly connected
orientation: a relation $D$ on $V$ such that $D(u, v)$ holds only when $u$ and $v$ are
adjacent, for every edge $uv$ exactly one of $D(u, v)$ and $D(v, u)$ holds, and every vertex
$v$ can be reached from every vertex $u$ by a finite, possibly empty, sequence of $D$-steps.

## Sources

- H. E. Robbins, "A Theorem on Graphs, with an Application to a Problem of Traffic Control," American Mathematical Monthly 46 (1939), 281–283; https://en.wikipedia.org/wiki/Robbins%27_theorem

Formalized by `MetaMathlibExt.robbins_theorem_connected`, a theorem declared in [MathlibExt/Combinatorics/Graph/RobbinsTheorem.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Graph/RobbinsTheorem.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/robbins-theorem/index.html#robbins-theorem-connected).

## Robbins' theorem, allowing the empty graph

Let $G$ be a simple graph on a finite,
possibly empty, vertex set $V$. Then every vertex of $G$ is reachable from every vertex and,
after deleting any single edge of $G$, every vertex is still reachable from every vertex, if
and only if $G$ has a strongly connected orientation: a relation $D$ on $V$ such that $D(u, v)$
holds only when $u$ and $v$ are adjacent, for every edge $uv$ exactly one of $D(u, v)$ and
$D(v, u)$ holds, and every vertex $v$ can be reached from every vertex $u$ by a finite,
possibly empty, sequence of $D$-steps.

For nonempty $V$ the left-hand condition says that $G$ is 2-edge-connected; for empty $V$ both
sides hold.

## Sources

- https://en.wikipedia.org/wiki/Robbins%27_theorem

Formalized by `MetaMathlibExt.robbins_theorem`, a theorem declared in [MathlibExt/Combinatorics/Graph/RobbinsTheorem.lean, line 529](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Graph/RobbinsTheorem.lean#L529). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/robbins-theorem/index.html#robbins-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Robbins' theorem](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/robbins-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/directed-graphs/robbins-theorem)
