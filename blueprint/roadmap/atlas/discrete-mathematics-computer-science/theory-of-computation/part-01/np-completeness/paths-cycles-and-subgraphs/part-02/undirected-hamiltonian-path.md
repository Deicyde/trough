---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.HamiltonianPathUndirected.HamiltonianPathUndirectedInstance, MetaMathlibExt.Complexity.NPComplete.HamiltonianPathUndirected.Graph, MetaMathlibExt.Complexity.NPComplete.HamiltonianPathUndirected.WellFormed, MetaMathlibExt.Complexity.NPComplete.HamiltonianPathUndirected.HamiltonianPathUndirectedFeasible, MetaMathlibExt.Complexity.NPComplete.HamiltonianPathUndirected.hamiltonianPathUndirectedDec, MetaMathlibExt.Complexity.NPComplete.HamiltonianPathUndirected.hamiltonianPathUndirected_npComplete
statement: formalized
---

# Undirected Hamiltonian path

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-path/index.html).

## Instances of undirected Hamiltonian path

An instance of undirected Hamiltonian path is a
pair $(n, E)$ of a natural number $n$, the number of vertices, and a finite list $E$ of pairs of
natural numbers, the edge list.

Formalized by `MetaMathlibExt.Complexity.NPComplete.HamiltonianPathUndirected.HamiltonianPathUndirectedInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/HamiltonianPathUndirectedWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/HamiltonianPathUndirectedWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-path/index.html#hamiltonian-path-undirected-instance).

## Graph of an undirected Hamiltonian path instance

For an instance $(n, E)$ of undirected
Hamiltonian path, its graph is the simple graph on the vertex set $\{0, \dots, n-1\}$ in which
distinct vertices $i$ and $j$ are adjacent when $(i, j)$ or $(j, i)$ belongs to $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.HamiltonianPathUndirected.Graph`, a definition declared in [WantedExt/Complexity/NPComplete/HamiltonianPathUndirectedWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/HamiltonianPathUndirectedWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-path/index.html#graph).

## Well-formed undirected Hamiltonian path instances

An instance $(n, E)$ of undirected
Hamiltonian path is well formed when $n > 0$, the list $E$ has no repeated entries, and every pair
$(u, v)$ in $E$ satisfies $u < n$, $v < n$ and $u \ne v$, and the reversed pair $(v, u)$ does not
belong to $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.HamiltonianPathUndirected.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/HamiltonianPathUndirectedWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/HamiltonianPathUndirectedWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-path/index.html#well-formed).

## Feasible undirected Hamiltonian path instances

An instance $(n, E)$ of undirected
Hamiltonian path is feasible when its graph has a Hamiltonian path: a list of length $n$ of
vertices of the graph, with no repeated entries and containing every vertex, in which any two
consecutive entries are adjacent.

Formalized by `MetaMathlibExt.Complexity.NPComplete.HamiltonianPathUndirected.HamiltonianPathUndirectedFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/HamiltonianPathUndirectedWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/HamiltonianPathUndirectedWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-path/index.html#hamiltonian-path-undirected-feasible).

## HAMILTONIAN PATH (UNDIRECTED) as a decision problem

The decision problem HAMILTONIAN PATH
(UNDIRECTED) accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring
encoding, to an instance $(n, E)$ of undirected Hamiltonian path that is well formed and feasible;
bitstrings that do not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.HamiltonianPathUndirected.hamiltonianPathUndirectedDec`, a definition declared in [WantedExt/Complexity/NPComplete/HamiltonianPathUndirectedWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/HamiltonianPathUndirectedWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-path/index.html#hamiltonian-path-undirected-dec).

## HAMILTONIAN PATH (UNDIRECTED) is NP-complete

The decision problem HAMILTONIAN PATH
(UNDIRECTED) belongs to NP, and every decision problem in NP reduces to it by a polynomial-time
many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), HAMILTONIAN PATH.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.HamiltonianPathUndirected.hamiltonianPathUndirected_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/HamiltonianPathUndirectedWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/HamiltonianPathUndirectedWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-path/index.html#hamiltonian-path-undirected-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Undirected Hamiltonian path](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-path/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-path)
