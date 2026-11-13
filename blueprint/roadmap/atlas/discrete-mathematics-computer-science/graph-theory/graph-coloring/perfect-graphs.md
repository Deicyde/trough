---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SimpleGraph.PerfectGraphWanted.IsPerfect, MathlibExt.Combinatorics.SimpleGraph.PerfectGraphWanted.PerfIneq, MathlibExt.Combinatorics.SimpleGraph.PerfectGraphWanted.perfect_implies_ineq, MathlibExt.Combinatorics.SimpleGraph.PerfectGraphWanted.lovasz_weak_perfect_graph_general, MathlibExt.Combinatorics.SimpleGraph.PerfectGraphWanted.lovasz_weak_perfect_graph, MathlibExt.Combinatorics.PerfectGraphNPWanted.PerfectGraphInstance, MathlibExt.Combinatorics.PerfectGraphNPWanted.PerfectGraphInstance.Valid, MathlibExt.Combinatorics.PerfectGraphNPWanted.PerfectGraphInstance.toSimpleGraph
statement: formalized
---

# Perfect graphs

11 results, 10 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/perfect-graphs/index.html).

## Perfect graph

A finite simple graph $G$ is perfect if, for every set $S$ of its
vertices, the induced subgraph $G[S]$ has chromatic number equal to its clique number, the
largest size of a clique in $G[S]$.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.PerfectGraphWanted.IsPerfect`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/PerfectGraph.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/PerfectGraph.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/perfect-graphs/index.html#is-perfect).

## Gasparian's condition (P)

A finite simple graph $G$ satisfies condition (P) if, for
every set $S$ of its vertices, the induced subgraph $G[S]$, with independence number
$\alpha(G[S])$ and clique number $\omega(G[S])$, satisfies
$|S| \le \alpha(G[S]) \cdot \omega(G[S])$.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.PerfectGraphWanted.PerfIneq`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/PerfectGraph.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/PerfectGraph.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/perfect-graphs/index.html#perf-ineq).

## Perfect graphs satisfy condition (P)

Every finite perfect graph $G$ satisfies
Gasparian's condition (P): for every set $S$ of its vertices, the induced subgraph $G[S]$,
with independence number $\alpha(G[S])$ and clique number $\omega(G[S])$, satisfies
$|S| \le \alpha(G[S]) \cdot \omega(G[S])$.

Indeed, $G[S]$ has a coloring with $\omega(G[S])$ colors, and each color class is an
independent set, so it has at most $\alpha(G[S])$ vertices.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.PerfectGraphWanted.perfect_implies_ineq`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/PerfectGraph.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/PerfectGraph.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/perfect-graphs/index.html#perfect-implies-ineq).

## Weak perfect graph theorem

A finite simple graph $G$ is perfect if and only if its
complement $\overline{G}$ is perfect.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.PerfectGraphWanted.lovasz_weak_perfect_graph_general`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/PerfectGraph.lean, line 960](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/PerfectGraph.lean#L960). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/perfect-graphs/index.html#lovasz-weak-perfect-graph-general).

## Lovász's weak perfect graph theorem

A finite simple graph $G$ is perfect if and only if
its complement $\overline{G}$ is perfect.

## Sources

- L. Lovasz, "Normal hypergraphs and the perfect graph conjecture", Discrete Math. 2 (1972), 253-267, DOI 10.1016/0012-365X(72)90006-4.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.PerfectGraphWanted.lovasz_weak_perfect_graph`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/PerfectGraph.lean, line 982](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/PerfectGraph.lean#L982). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/perfect-graphs/index.html#lovasz-weak-perfect-graph).

## Adjacency-matrix graph instance

An instance consists of a natural number $n$ and a
Boolean $n \times n$ matrix $A$ with rows and columns indexed by $\{0, \dots, n-1\}$, read as the
adjacency matrix of a graph on the vertices $0, \dots, n-1$. The matrix is arbitrary; symmetry
and the absence of loops are imposed separately by the validity condition.

## Sources

- [AIM-COMBINATORICS-0270] Source item 4, notes[269], Section A.4.

Formalized by `MathlibExt.Combinatorics.PerfectGraphNPWanted.PerfectGraphInstance`, a structure declared in [WantedExt/Combinatorics/PerfectGraphNPWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PerfectGraphNPWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/perfect-graphs/index.html#perfect-graph-instance).

## Valid adjacency-matrix instance

An instance with $n$ vertices and adjacency matrix $A$ is
valid when $A$ is symmetric, that is, $A_{yx}$ is true whenever $A_{xy}$ is true, and has no
loops, that is, $A_{xx}$ is false for every vertex $x$.

Formalized by `MathlibExt.Combinatorics.PerfectGraphNPWanted.PerfectGraphInstance.Valid`, a definition declared in [WantedExt/Combinatorics/PerfectGraphNPWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PerfectGraphNPWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/perfect-graphs/index.html#valid).

## Graph of a valid instance

A valid instance with $n$ vertices and adjacency matrix $A$
determines the simple graph on the vertex set $\{0, \dots, n-1\}$ in which vertices $x$ and $y$
are adjacent exactly when $A_{xy}$ is true.

Formalized by `MathlibExt.Combinatorics.PerfectGraphNPWanted.PerfectGraphInstance.toSimpleGraph`, a definition declared in [WantedExt/Combinatorics/PerfectGraphNPWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PerfectGraphNPWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/perfect-graphs/index.html#to-simple-graph).

## The perfect-graph decision problem

The decision problem on bitstrings that accepts a
bitstring $x$ exactly when $x$ decodes, under the bitstring encoding of adjacency-matrix
instances, to a valid instance whose graph is perfect. Bitstrings that do not decode to an
instance, or decode to an invalid one, are rejected.

## Sources

- [AIM-COMBINATORICS-0270] Source item 4, notes[269], Section A.4.

Formalized by `MathlibExt.Combinatorics.PerfectGraphNPWanted.perfectGraphProblem`, a definition declared in [WantedExt/Combinatorics/PerfectGraphNPWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PerfectGraphNPWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/perfect-graphs/index.html#perfect-graph-problem).

## Edmonds's question: an NP description of perfect graphs

The perfect-graph decision
problem, which accepts exactly the bitstrings that decode to a valid adjacency-matrix instance
whose graph is perfect, lies in the complexity class NP: there are a polynomial $p$ with
natural-number coefficients and a polynomial-time verifier $R$ on pairs of bitstrings such that a
bitstring $x$ is accepted if and only if $R$ accepts $(x, w)$ for some bitstring $w$ of length at
most $p(|x|)$.

## Sources

- [AIM-COMBINATORICS-0270] Source item 4, notes[269], Section A.4, Contributor Jack Edmonds.

Formalized by `MathlibExt.Combinatorics.PerfectGraphNPWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/PerfectGraphNPWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PerfectGraphNPWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/perfect-graphs/index.html#conjecture).

## Perfect graphs have an NP description

The perfect-graph decision problem, which accepts
exactly the bitstrings that decode to a valid adjacency-matrix instance whose graph is perfect,
lies in the complexity class NP.

Chudnovsky, Cornuéjols, Liu, Seymour and Vušković recognize Berge graphs in polynomial time,
and the Strong Perfect Graph Theorem identifies Berge graphs with perfect graphs; hence
perfect-graph recognition is in P, and so in NP.

## Sources

- Maria Chudnovsky, Gerard Cornuejols, Xinming Liu, Paul Seymour, Kristina Vuskovic, Recognizing Berge graphs, Combinatorica 25 (2005), 143-186, https://doi.org/10.1007/s00493-005-0012-8; Maria Chudnovsky, Neil Robertson, Paul Seymour, Robin Thomas, The strong perfect graph theorem, Annals of Mathematics 164 (2006), 51-229, https://doi.org/10.4007/annals.2006.164.51.

Stated but not proved: `MathlibExt.Combinatorics.PerfectGraphNPWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/PerfectGraphNPWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/PerfectGraphNPWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/perfect-graphs/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Perfect graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/perfect-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/graph-coloring/part-01/perfect-graphs)
