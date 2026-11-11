---
declaration: section
origin: cited
lean: EndpointMapMultigraph.incident, EndpointMapMultigraph.degreeWithin, EndpointMapMultigraph.support, EndpointMapMultigraph.AdjacentUsing, EndpointMapMultigraph.IsConnectedOnSupport, EndpointMapMultigraph.IsCircuit, EndpointMapMultigraph.cut, EndpointMapMultigraph.degreeWithin_eq_card_incident_of_loopless
statement: formalized
proof: formalized
---

# Finite multigraphs

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/finite-multigraphs/index.html).

## Edges incident to a vertex

Let $\mathrm{end}_1, \mathrm{end}_2 : E \to V$ be maps, viewed
as an undirected multigraph on $V$ in which each edge $e \in E$ has endpoints $\mathrm{end}_1(e)$
and $\mathrm{end}_2(e)$. For a vertex $v \in V$ and a finite set $F \subseteq E$, the edges of
$F$ incident to $v$ form the finite set of all $e \in F$ with $\mathrm{end}_1(e) = v$ or
$\mathrm{end}_2(e) = v$. An edge appears once even when it is a loop.

Formalized by `EndpointMapMultigraph.incident`, a definition declared in [MathlibExt/Combinatorics/EndpointMapMultigraph.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/EndpointMapMultigraph.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/finite-multigraphs/index.html#incident).

## Degree within an edge set

Let $\mathrm{end}_1, \mathrm{end}_2 : E \to V$ be maps, viewed
as an undirected multigraph on $V$ in which each edge $e \in E$ has endpoints $\mathrm{end}_1(e)$
and $\mathrm{end}_2(e)$. For a finite set $F \subseteq E$ and a vertex $v \in V$, the degree of
$v$ in $F$ is the number of $e \in F$ with $\mathrm{end}_1(e) = v$ plus the number of $e \in F$
with $\mathrm{end}_2(e) = v$. Each endpoint incidence counts once, so a loop at $v$ contributes
two.

Formalized by `EndpointMapMultigraph.degreeWithin`, a definition declared in [MathlibExt/Combinatorics/EndpointMapMultigraph.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/EndpointMapMultigraph.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/finite-multigraphs/index.html#degree-within).

## Support of an edge set

Let $\mathrm{end}_1, \mathrm{end}_2 : E \to V$ be maps, viewed as
an undirected multigraph on $V$ in which each edge $e \in E$ has endpoints $\mathrm{end}_1(e)$
and $\mathrm{end}_2(e)$. The support of a finite set $F \subseteq E$ is the set of vertices
$v \in V$ such that $\mathrm{end}_1(e) = v$ or $\mathrm{end}_2(e) = v$ for some $e \in F$.

Formalized by `EndpointMapMultigraph.support`, a definition declared in [MathlibExt/Combinatorics/EndpointMapMultigraph.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/EndpointMapMultigraph.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/finite-multigraphs/index.html#support).

## Adjacency through an edge set

Let $\mathrm{end}_1, \mathrm{end}_2 : E \to V$ be maps,
viewed as an undirected multigraph on $V$ in which each edge $e \in E$ has endpoints
$\mathrm{end}_1(e)$ and $\mathrm{end}_2(e)$. For a finite set $F \subseteq E$, vertices
$u, v \in V$ are adjacent using $F$ when some $e \in F$ has $\mathrm{end}_1(e) = u$ and
$\mathrm{end}_2(e) = v$, or $\mathrm{end}_1(e) = v$ and $\mathrm{end}_2(e) = u$.

Formalized by `EndpointMapMultigraph.AdjacentUsing`, a definition declared in [MathlibExt/Combinatorics/EndpointMapMultigraph.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/EndpointMapMultigraph.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/finite-multigraphs/index.html#adjacent-using).

## Edge sets connected on their support

Let $\mathrm{end}_1, \mathrm{end}_2 : E \to V$ be
maps, viewed as an undirected multigraph on $V$ in which each edge $e \in E$ has endpoints
$\mathrm{end}_1(e)$ and $\mathrm{end}_2(e)$. A finite set $F \subseteq E$ is connected on its
support when for all vertices $u$ and $v$ in the support of $F$ there are vertices
$u = w_0, w_1, \dots, w_k = v$, with $k \ge 0$, such that $w_{i-1}$ and $w_i$ are adjacent
using $F$ for each $1 \le i \le k$.

Formalized by `EndpointMapMultigraph.IsConnectedOnSupport`, a definition declared in [MathlibExt/Combinatorics/EndpointMapMultigraph.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/EndpointMapMultigraph.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/finite-multigraphs/index.html#is-connected-on-support).

## Circuits in an edge set

Let $\mathrm{end}_1, \mathrm{end}_2 : E \to V$ be maps, viewed
as an undirected multigraph on $V$ in which each edge $e \in E$ has endpoints $\mathrm{end}_1(e)$
and $\mathrm{end}_2(e)$. A finite set $F \subseteq E$ is a circuit when $F$ is nonempty, $F$ is
connected on its support, and every vertex in the support of $F$ has degree exactly $2$ in $F$,
where degree counts endpoint incidences, so that a loop contributes two.

This includes a loop as a $1$-circuit and two parallel edges between distinct vertices as a
$2$-circuit.

Formalized by `EndpointMapMultigraph.IsCircuit`, a definition declared in [MathlibExt/Combinatorics/EndpointMapMultigraph.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/EndpointMapMultigraph.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/finite-multigraphs/index.html#is-circuit).

## Cut of a vertex set

Let $E$ be a finite set and $\mathrm{end}_1, \mathrm{end}_2 : E \to V$
be maps, viewed as an undirected multigraph on $V$ in which each edge $e \in E$ has endpoints
$\mathrm{end}_1(e)$ and $\mathrm{end}_2(e)$. For a finite set $X \subseteq V$, the cut of $X$ is
the set of edges $e \in E$ such that exactly one of $\mathrm{end}_1(e)$ and $\mathrm{end}_2(e)$
lies in $X$. Loops never cross a cut.

Formalized by `EndpointMapMultigraph.cut`, a definition declared in [MathlibExt/Combinatorics/EndpointMapMultigraph.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/EndpointMapMultigraph.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/finite-multigraphs/index.html#cut).

## Degree counts incident edges in a loopless edge set

Let
$\mathrm{end}_1, \mathrm{end}_2 : E \to V$ be maps, viewed as an undirected multigraph on $V$ in
which each edge $e \in E$ has endpoints $\mathrm{end}_1(e)$ and $\mathrm{end}_2(e)$. Let
$F \subseteq E$ be a finite set of edges with no loops, that is,
$\mathrm{end}_1(e) \ne \mathrm{end}_2(e)$ for every $e \in F$. Then for every vertex $v \in V$,
the degree of $v$ in $F$ equals the number of edges of $F$ incident to $v$.

Formalized by `EndpointMapMultigraph.degreeWithin_eq_card_incident_of_loopless`, a theorem declared in [MathlibExt/Combinatorics/EndpointMapMultigraph.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/EndpointMapMultigraph.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/finite-multigraphs/index.html#degree-within-eq-card-incident-of-loople).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite multigraphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/finite-multigraphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/graph-families-and-operations/finite-multigraphs)
