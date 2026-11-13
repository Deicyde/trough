---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.AdjacencyMatrix, Cslib.Algorithms.Lean.AdjacencyMatrix.empty, Cslib.Algorithms.Lean.AdjacencyMatrix.hasEdge, Cslib.Algorithms.Lean.AdjacencyMatrix.hasEdge_empty, Cslib.Algorithms.Lean.AdjacencyMatrix.addEdge, Cslib.Algorithms.Lean.AdjacencyMatrix.hasEdge_addEdge, Cslib.Algorithms.Lean.AdjacencyMatrix.hasEdge_addEdge_of_ne, Cslib.Algorithms.Lean.AdjacencyMatrix.hasEdge_addEdge_iff
statement: formalized
proof: formalized
---

# Adjacency matrix

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html).

## Adjacency Matrix

## Adjacency matrix

For a natural number $n$, an adjacency matrix on $n$ vertices is a
directed graph on the vertex set $\{0, \dots, n-1\}$ given by a Boolean-valued function
$\mathrm{adj}$ on ordered pairs of vertices: $\mathrm{adj}(i, j)$ is true exactly when there is a
directed edge from $i$ to $j$.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#adjacency-matrix).

## Empty adjacency matrix

For every natural number $n$, the empty adjacency matrix on $n$
vertices is the directed graph on $\{0, \dots, n-1\}$ with no edges: its adjacency function is
false on every ordered pair of vertices.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#empty).

## Edge query of an adjacency matrix

For an adjacency matrix $m$ on the vertex set
$\{0, \dots, n-1\}$ and vertices $i, j$, the edge query of $m$ at $(i, j)$ is the Boolean value
that is true exactly when $m$ has a directed edge from $i$ to $j$.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.hasEdge`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#has-edge).

## The empty adjacency matrix has no edges

For every natural number $n$ and all vertices $i$
and $j$ among the $n$ vertices, the empty adjacency matrix on $n$ vertices has no edge from $i$ to
$j$.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.hasEdge_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#has-edge-empty).

## Edge insertion in an adjacency matrix

For an adjacency matrix $m$ on the vertex set
$\{0, \dots, n-1\}$ and vertices $i$ and $j$, adding the edge from $i$ to $j$ gives the adjacency
matrix that has an edge from $i$ to $j$ and agrees with $m$ on every other ordered pair of
vertices.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.addEdge`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#add-edge).

## An inserted edge is present

For an adjacency matrix $m$ on $n$ vertices and vertices $i$
and $j$, the matrix obtained from $m$ by adding the edge from $i$ to $j$ has an edge from $i$ to
$j$.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.hasEdge_addEdge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#has-edge-add-edge).

## Inserting an edge leaves other pairs unchanged

For an adjacency matrix $m$ on $n$
vertices and vertices $i$, $j$, $a$, $b$ with $a \ne i$ or $b \ne j$, the matrix obtained from $m$
by adding the edge from $i$ to $j$ has an edge from $a$ to $b$ if and only if $m$ does.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.hasEdge_addEdge_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#has-edge-add-edge-of-ne).

## Edges after inserting an edge

For an adjacency matrix $m$ on $n$ vertices and vertices
$i$, $j$, $a$, $b$, the matrix obtained from $m$ by adding the edge from $i$ to $j$ has an edge
from $a$ to $b$ if and only if $a = i$ and $b = j$, or $m$ has an edge from $a$ to $b$.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.hasEdge_addEdge_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#has-edge-add-edge-iff).

## Edge deletion in an adjacency matrix

For an adjacency matrix $m$ on the vertex set
$\{0, \dots, n-1\}$ and vertices $i$ and $j$, removing the edge from $i$ to $j$ gives the adjacency
matrix that has no edge from $i$ to $j$ and agrees with $m$ on every other ordered pair of
vertices.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.eraseEdge`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#erase-edge).

## Deleting an edge removes it

Let $m$ be an adjacency matrix on the vertex set
$\{0, \dots, n-1\}$ and let $i, j$ be vertices. Then the graph obtained from $m$ by deleting the
edge from $i$ to $j$ has no edge from $i$ to $j$.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.hasEdge_eraseEdge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#has-edge-erase-edge).

## Deleting an edge leaves the other entries unchanged

Let $m$ be an adjacency matrix on the
vertex set $\{0, \dots, n-1\}$ and let $i, j, a, b$ be vertices with $(a, b) \ne (i, j)$, that is,
$a \ne i$ or $b \ne j$. Then the graph obtained from $m$ by deleting the edge from $i$ to $j$ has
an edge from $a$ to $b$ if and only if $m$ has an edge from $a$ to $b$.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.hasEdge_eraseEdge_of_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#has-edge-erase-edge-of-ne).

## Edges after deleting an edge

For an adjacency matrix $m$ on $n$ vertices and vertices $i$,
$j$, $a$, $b$, the matrix obtained from $m$ by removing the edge from $i$ to $j$ has an edge from
$a$ to $b$ if and only if $(a, b) \ne (i, j)$ and $m$ has an edge from $a$ to $b$.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.hasEdge_eraseEdge_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#has-edge-erase-edge-iff).

## Extensionality of adjacency matrices

Two adjacency matrices $m$ and $m'$ on the same $n$
vertices are equal if, for all vertices $i$ and $j$, $m$ has an edge from $i$ to $j$ exactly when
$m'$ does.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.ext`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#ext).

## Out-neighbor list

For an adjacency matrix $m$ on the vertex set $\{0, \dots, n-1\}$ and a
vertex $i$, the out-neighbor list of $i$ is the list of all vertices $j$ such that $m$ has a
directed edge from $i$ to $j$, in increasing order.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.neighbors`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#neighbors).

## The out-neighbor list matches the edge query

Let $m$ be an adjacency matrix on the vertex
set $\{0, \dots, n-1\}$ and let $i, j$ be vertices. Then $j$ belongs to the out-neighbor list of
$i$ if and only if $m$ has a directed edge from $i$ to $j$.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.mem_neighbors`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#mem-neighbors).

## Out-neighbor lists have no duplicates

For an adjacency matrix $m$ on the vertex set
$\{0, \dots, n-1\}$ and a vertex $i$, no vertex occurs twice in the out-neighbor list of $i$.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.neighbors_nodup`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#neighbors-nodup).

## Out-neighbor lists are strictly increasing

For an adjacency matrix $m$ on the vertex set
$\{0, \dots, n-1\}$ and a vertex $i$, the out-neighbor list of $i$ is strictly increasing: every
vertex in it is smaller than every vertex that comes after it.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.neighbors_pairwise_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#neighbors-pairwise-lt).

## Out-neighbor lists of the empty graph

In the graph with no edges on the vertex set
$\{0, \dots, n-1\}$, the out-neighbor list of every vertex $i$ is the empty list.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.neighbors_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#neighbors-empty).

## Adding an edge makes its target an out-neighbor

Let $m$ be an adjacency matrix on the
vertex set $\{0, \dots, n-1\}$ and let $i, j$ be vertices. Then $j$ belongs to the out-neighbor
list of $i$ in the graph obtained from $m$ by adding the edge from $i$ to $j$.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.mem_neighbors_addEdge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#mem-neighbors-add-edge).

## Deleting an edge removes the out-neighbor

Let $G$ be a directed graph on the vertices
$0, \dots, n-1$, given by its adjacency matrix, and let $i$ and $j$ be vertices. After the edge
from $i$ to $j$ is deleted from $G$ (whether or not $G$ had that edge), $j$ is not an
out-neighbor of $i$.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.not_mem_neighbors_eraseEdge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#not-mem-neighbors-erase-edge).

## Out-neighbors after adding an edge

Let $m$ be an adjacency matrix on the vertex set
$\{0, \dots, n-1\}$ and let $i, j, b$ be vertices. Then $b$ belongs to the out-neighbor list of
$i$ in the graph obtained from $m$ by adding the edge from $i$ to $j$ if and only if $b = j$ or
$b$ belongs to the out-neighbor list of $i$ in $m$.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.mem_neighbors_addEdge_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#mem-neighbors-add-edge-iff).

## Out-degree

The out-degree of a vertex $i$ of a directed graph given by an adjacency
matrix is the number of its out-neighbors, that is, the number of vertices $j$ such that there is
an edge from $i$ to $j$.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.outDegree`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#out-degree).

## Vertices of the empty graph have out-degree zero

For every $n$, every vertex of the
empty directed graph on the vertices $0, \dots, n-1$ has out-degree $0$.

Formalized by `Cslib.Algorithms.Lean.AdjacencyMatrix.outDegree_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DataStructures/AdjacencyMatrix.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html#out-degree-empty).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Adjacency matrix](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/graph-algorithms/traversal-and-connectivity/adjacency-matrix)
