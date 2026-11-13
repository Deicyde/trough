---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Graph.hamiltonianCycleToTsp, Cslib.Algorithms.Lean.Graph.hamiltonianCycleToTsp_size, Cslib.Algorithms.Lean.Graph.hamiltonianCycleToTsp_getElem?, Cslib.Algorithms.Lean.Graph.hamiltonianCycleToTsp_time, Cslib.Algorithms.Lean.Graph.hamiltonianCycleToTsp_costs, Cslib.Algorithms.Lean.Graph.hamiltonianCycleToTsp_forward, Cslib.Algorithms.Lean.Graph.hamiltonianCycleToTsp_reverse, Cslib.Algorithms.Lean.Graph.hamiltonianCycleToTsp_iff
statement: formalized
---

# Traveling salesperson problem

14 results, 13 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/traveling-salesperson-problem/index.html).

## Hamiltonian-cycle to TSP converter

The Hamiltonian-cycle to TSP converter takes a Boolean
array $x$ and, starting from the empty array, scans $x$ from left to right and appends the
negation of each cell, charging one time unit before and one time unit after each append (one
read and one write per cell). It returns the resulting array of negated cells together with the
total time charged.

Formalized by `Cslib.Algorithms.Lean.Graph.hamiltonianCycleToTsp`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/HamiltonianCycleToTsp.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HamiltonianCycleToTsp.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/traveling-salesperson-problem/index.html#hamiltonian-cycle-to-tsp).

## The Hamiltonian-cycle to TSP converter preserves length

For every Boolean array $x$, the
array output by the Hamiltonian-cycle to TSP converter on $x$ has the same length as $x$.

No assumption that $x$ encodes a graph is needed.

Formalized by `Cslib.Algorithms.Lean.Graph.hamiltonianCycleToTsp_size`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HamiltonianCycleToTsp.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HamiltonianCycleToTsp.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/traveling-salesperson-problem/index.html#hamiltonian-cycle-to-tsp-size).

## The Hamiltonian-cycle to TSP converter negates every cell

For every Boolean array $x$ and
every index $k$, the array output by the Hamiltonian-cycle to TSP converter on $x$ has a cell at
index $k$ exactly when $x$ does, and that cell is the negation of the cell of $x$ at index $k$.

Formalized by `Cslib.Algorithms.Lean.Graph.hamiltonianCycleToTsp_getElem?`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HamiltonianCycleToTsp.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HamiltonianCycleToTsp.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/traveling-salesperson-problem/index.html#hamiltonian-cycle-to-tsp-get-elem).

## Running time of the Hamiltonian-cycle to TSP converter

For every Boolean array $x$, the
time charged by the Hamiltonian-cycle to TSP converter on $x$ is $2m$, where $m$ is the length of
$x$: one unit for reading and one unit for writing each cell.

Formalized by `Cslib.Algorithms.Lean.Graph.hamiltonianCycleToTsp_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HamiltonianCycleToTsp.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HamiltonianCycleToTsp.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/traveling-salesperson-problem/index.html#hamiltonian-cycle-to-tsp-time).

## Costs produced by the Hamiltonian-cycle to TSP converter

Let $G$ be a simple graph on the
vertex set $\{0, \dots, n-1\}$, let $x$ be a Boolean array of length $n^2$ such that for all
$i, j < n$ the cell of $x$ at index $in + j$ exists and is true exactly when $i$ and $j$ are
adjacent in $G$, and let $y$ be the array output by the Hamiltonian-cycle to TSP converter on $x$,
with a Boolean cell read as $1$ if true and $0$ if false. Then for all $i, j < n$ the cell of $y$
at index $in + j$ exists and equals $0$ if $i$ and $j$ are adjacent in $G$ and $1$ otherwise; for
every $i < n$ the cell of $y$ at index $in + i$ exists and equals $1$; and for all $i, j < n$ the
cells of $y$ at indices $in + j$ and $jn + i$ are equal.

Formalized by `Cslib.Algorithms.Lean.Graph.hamiltonianCycleToTsp_costs`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HamiltonianCycleToTsp.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HamiltonianCycleToTsp.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/traveling-salesperson-problem/index.html#hamiltonian-cycle-to-tsp-costs).

## Hamiltonian cycles of the source graph give zero-cost tours

Let $G$ be a simple graph on
the vertex set $\{0, \dots, n-1\}$, let $x$ be a Boolean array of length $n^2$ such that for all
$i, j < n$ the cell of $x$ at index $in + j$ exists and is true exactly when $i$ and $j$ are
adjacent in $G$, and let $y$ be the array output by the Hamiltonian-cycle to TSP converter on $x$,
with a Boolean cell read as $1$ if true and $0$ if false. Let $p$ be a Hamiltonian cycle in $G$
based at a vertex $a$, and let $p'$ be $p$ regarded as a closed walk in the complete graph on
$\{0, \dots, n-1\}$. Then $p'$ is a Hamiltonian cycle, $p'$ visits the same sequence of vertices
as $p$, and for every directed edge $(u, v)$ traversed by $p'$ the cell of $y$ at index $un + v$
exists, and the sum of these cells over the directed edges of $p'$ is $0$.

Formalized by `Cslib.Algorithms.Lean.Graph.hamiltonianCycleToTsp_forward`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HamiltonianCycleToTsp.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HamiltonianCycleToTsp.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/traveling-salesperson-problem/index.html#hamiltonian-cycle-to-tsp-forward).

## Tours of cost zero give Hamiltonian cycles of the source graph

Let $G$ be a simple graph
on the vertex set $\{0, \dots, n-1\}$, let $x$ be a Boolean array of length $n^2$ such that for
all $i, j < n$ the cell of $x$ at index $in + j$ exists and is true exactly when $i$ and $j$ are
adjacent in $G$, and let $y$ be the array output by the Hamiltonian-cycle to TSP converter on $x$,
with a Boolean cell read as $1$ if true and $0$ if false. Let $p$ be a Hamiltonian cycle based at
a vertex $a$ in the complete graph on $\{0, \dots, n-1\}$ such that for every directed edge
$(u, v)$ traversed by $p$ the cell of $y$ at index $un + v$ exists and the sum of these cells over
the directed edges of $p$ is at most $0$. Then there is a Hamiltonian cycle $q$ in $G$ based at
$a$ that visits the same sequence of vertices as $p$.

Formalized by `Cslib.Algorithms.Lean.Graph.hamiltonianCycleToTsp_reverse`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HamiltonianCycleToTsp.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HamiltonianCycleToTsp.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/traveling-salesperson-problem/index.html#hamiltonian-cycle-to-tsp-reverse).

## Correctness of the Hamiltonian-cycle to TSP reduction

Let $G$ be a simple graph on the
vertex set $V = \{0, \dots, n-1\}$, let $x$ be a Boolean array of length $n^2$ such that for all
$i, j < n$ the cell of $x$ at index $in + j$ exists and is true exactly when $i$ and $j$ are
adjacent in $G$, and let $y$ be the array output by the Hamiltonian-cycle to TSP converter on $x$,
with a Boolean cell read as $1$ if true and $0$ if false. Then $G$ has a Hamiltonian cycle if and
only if the complete graph on $V$ has a Hamiltonian cycle $p$ such that for every directed edge
$(u, v)$ traversed by $p$ the cell of $y$ at index $un + v$ exists and the sum of these cells over
the directed edges of $p$ is at most $0$.

Formalized by `Cslib.Algorithms.Lean.Graph.hamiltonianCycleToTsp_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HamiltonianCycleToTsp.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Graph/HamiltonianCycleToTsp.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/traveling-salesperson-problem/index.html#hamiltonian-cycle-to-tsp-iff).

## Symmetric TSP instances

An instance of the symmetric traveling salesperson problem is a
triple $(n, w, B)$ of a natural number $n$, the number of cities, a weight matrix $w$ given as a
finite list of rows, each a finite list of natural numbers, and a natural number $B$, the bound.

The type itself does not require $w$ to be an $n \times n$ symmetric matrix with zero diagonal.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Tsp.TspInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/TspWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/TspWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/traveling-salesperson-problem/index.html#tsp-instance).

## Length of a tour in the symmetric TSP

Let $w$ be a matrix of natural numbers given as a
list of rows, where an entry $w_{a,b}$ outside the list (no row $a$, or row $a$ too short) is
read as $0$, and rows and columns are numbered from $0$. The length of a list
$(t_0, \dots, t_{k-1})$ of natural numbers with respect to $w$ is
$\sum_{j\lt k} w_{t_j, t_{(j+1) \bmod k}}$, the total weight of the edges along the cycle
$t_0, t_1, \dots, t_{k-1}, t_0$, including the return edge; the empty list has length $0$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Tsp.TourLength`, a definition declared in [WantedExt/Complexity/NPComplete/TspWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/TspWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/traveling-salesperson-problem/index.html#tour-length).

## Well-formed symmetric TSP instances

A symmetric TSP instance $(n, w, B)$ is well formed
when $n > 0$, the weight matrix $w$ has exactly $n$ rows and each row has exactly $n$ entries, $w$
is symmetric, that is $w_{a,b} = w_{b,a}$ for all $a, b < n$, and $w$ has zero diagonal, that is
$w_{a,a} = 0$ for all $a < n$. Rows and columns are numbered from $0$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Tsp.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/TspWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/TspWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/traveling-salesperson-problem/index.html#well-formed).

## Feasible symmetric TSP instances

A symmetric TSP instance $(n, w, B)$ is feasible when
there is a list of $n$ pairwise distinct natural numbers containing every $v < n$, that is, an
ordering of the cities $0, 1, \dots, n-1$ visiting each exactly once, whose tour length with
respect to $w$ (the sum of the weights of consecutive edges, including the return edge) is at
most $B$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Tsp.TspFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/TspWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/TspWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/traveling-salesperson-problem/index.html#tsp-feasible).

## Symmetric TSP as a decision problem

The symmetric traveling salesperson problem is the
decision problem that accepts a bitstring $x$ exactly when $x$ decodes, under the canonical
bitstring encoding of symmetric TSP instances, to an instance $(n, w, B)$ that is well formed and
feasible. Bitstrings that fail to decode, and bitstrings that decode to instances that are not
well formed, are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Tsp.tspDec`, a definition declared in [WantedExt/Complexity/NPComplete/TspWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/TspWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/traveling-salesperson-problem/index.html#tsp-dec).

## TRAVELING SALESPERSON (SYMMETRIC) is NP-complete

The symmetric traveling salesperson
decision problem belongs to NP, and every decision problem in NP reduces to it by a
polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), TRAVELING SALESPERSON PROBLEM.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.Tsp.tsp_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/TspWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/TspWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/traveling-salesperson-problem/index.html#tsp-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Traveling salesperson problem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/traveling-salesperson-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/traveling-salesperson-problem)
