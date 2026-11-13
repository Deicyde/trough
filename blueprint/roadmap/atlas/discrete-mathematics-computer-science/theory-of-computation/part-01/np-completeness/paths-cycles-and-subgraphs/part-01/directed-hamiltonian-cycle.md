---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.HamiltonianCycleDirected.HamiltonianCycleDirectedInstance, MetaMathlibExt.Complexity.NPComplete.HamiltonianCycleDirected.DAdj, MetaMathlibExt.Complexity.NPComplete.HamiltonianCycleDirected.WellFormed, MetaMathlibExt.Complexity.NPComplete.HamiltonianCycleDirected.HamiltonianCycleDirectedFeasible, MetaMathlibExt.Complexity.NPComplete.HamiltonianCycleDirected.hamiltonianCycleDirectedDec, MetaMathlibExt.Complexity.NPComplete.HamiltonianCycleDirected.hamiltonianCycleDirected_npComplete
statement: formalized
---

# Directed Hamiltonian cycle

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/directed-hamiltonian-cycle/index.html).

## Instances of HAMILTONIAN CYCLE (DIRECTED)

An instance of HAMILTONIAN CYCLE (DIRECTED)
is a pair $(n, E)$ of a natural number $n$, the number of vertices, and a finite list $E$ of
ordered pairs of natural numbers, the arcs.

Formalized by `MetaMathlibExt.Complexity.NPComplete.HamiltonianCycleDirected.HamiltonianCycleDirectedInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/HamiltonianCycleDirectedWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/HamiltonianCycleDirectedWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/directed-hamiltonian-cycle/index.html#hamiltonian-cycle-directed-instance).

## Directed adjacency for HAMILTONIAN CYCLE (DIRECTED)

For a finite list $E$ of ordered
pairs of natural numbers and natural numbers $u$ and $v$, the directed adjacency of $u$ to $v$
in $E$ is the boolean value that is true exactly when the pair $(u, v)$ occurs in $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.HamiltonianCycleDirected.DAdj`, a definition declared in [WantedExt/Complexity/NPComplete/HamiltonianCycleDirectedWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/HamiltonianCycleDirectedWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/directed-hamiltonian-cycle/index.html#dadj).

## Well-formed instances of HAMILTONIAN CYCLE (DIRECTED)

An instance $(n, E)$ of
HAMILTONIAN CYCLE (DIRECTED), with $n$ a natural number and $E$ a finite list of ordered pairs
of natural numbers, is well formed when $n > 0$, the list $E$ has no repeated entries, and
every pair $(u, v)$ in $E$ satisfies $u < n$, $v < n$ and $u \ne v$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.HamiltonianCycleDirected.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/HamiltonianCycleDirectedWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/HamiltonianCycleDirectedWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/directed-hamiltonian-cycle/index.html#well-formed).

## Directed Hamiltonian cycles of an instance

An instance $(n, E)$ of HAMILTONIAN CYCLE
(DIRECTED), with $n$ a natural number and $E$ a finite list of ordered pairs of natural numbers,
has a directed Hamiltonian cycle when there is a list $(v_0, \dots, v_{n-1})$ of $n$ distinct
natural numbers containing every natural number below $n$ such that the pair
$(v_j, v_{(j+1) \bmod n})$ occurs in $E$ for every $j < n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.HamiltonianCycleDirected.HamiltonianCycleDirectedFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/HamiltonianCycleDirectedWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/HamiltonianCycleDirectedWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/directed-hamiltonian-cycle/index.html#hamiltonian-cycle-directed-feasible).

## The directed Hamiltonian cycle decision problem

The decision problem HAMILTONIAN CYCLE
(DIRECTED) accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring
encoding, to an instance $(n, E)$, consisting of a natural number $n$ and a finite list $E$ of
ordered pairs of natural numbers, such that $(n, E)$ is well formed ($n > 0$, $E$ has no
repeated entries, and every pair $(u, v)$ in $E$ satisfies $u < n$, $v < n$ and $u \ne v$) and
has a directed Hamiltonian cycle (a list $(v_0, \dots, v_{n-1})$ of $n$ distinct natural
numbers containing every natural number below $n$ such that $(v_j, v_{(j+1) \bmod n})$ occurs
in $E$ for every $j < n$). It rejects every bitstring that does not decode to an instance.

Formalized by `MetaMathlibExt.Complexity.NPComplete.HamiltonianCycleDirected.hamiltonianCycleDirectedDec`, a definition declared in [WantedExt/Complexity/NPComplete/HamiltonianCycleDirectedWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/HamiltonianCycleDirectedWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/directed-hamiltonian-cycle/index.html#hamiltonian-cycle-directed-dec).

## HAMILTONIAN CYCLE (DIRECTED) is NP-complete

The decision problem HAMILTONIAN CYCLE
(DIRECTED) belongs to NP, and every decision problem $L$ in NP has a polynomial-time many-one
reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), HAMILTONIAN CIRCUIT (directed); R. M. Karp, "Reducibility among combinatorial problems" (1972).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.HamiltonianCycleDirected.hamiltonianCycleDirected_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/HamiltonianCycleDirectedWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/HamiltonianCycleDirectedWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/directed-hamiltonian-cycle/index.html#hamiltonian-cycle-directed-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Directed Hamiltonian cycle](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/directed-hamiltonian-cycle/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/directed-hamiltonian-cycle)
