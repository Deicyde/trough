---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Graph.verifyHamiltonianCycle, Cslib.Algorithms.Lean.Graph.verifyHamiltonianCycle_iff, Cslib.Algorithms.Lean.Graph.verifyHamiltonianCycle_sound, Cslib.Algorithms.Lean.Graph.verifyHamiltonianCycle_complete, Cslib.Algorithms.Lean.Graph.verifyHamiltonianCycle_language_iff, Cslib.Algorithms.Lean.Graph.verifyHamiltonianCycle_certificate_size, Cslib.Algorithms.Lean.Graph.verifyHamiltonianCycle_time_le, Cslib.Algorithms.Lean.Graph.verifyHamiltonianCycle_time_le_of_accept
statement: formalized
---

# Undirected Hamiltonian cycle

14 results, 13 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-cycle/index.html).

## Hamiltonian-cycle verifier

Given bit strings $x$ and $y$, let
$m = \lfloor \sqrt{|x|} \rfloor$ and let $w$ be the least natural number with $m \le 2^w$. The
verifier reads $x$ as the adjacency matrix of a graph on the vertices $0, \dots, m - 1$, stored
row by row, and $y$ as $m$ words of $w$ bits, the $i$-th word giving a number $v_i$ in binary,
least significant bit first. It accepts exactly when $|x| = m^2$, every diagonal entry of the
matrix is false, the matrix is symmetric, $m \ge 3$, $|y| = mw$, the numbers
$v_0, \dots, v_{m-1}$ are distinct and less than $m$, and $v_i$ is adjacent to
$v_{(i+1) \bmod m}$ for every $i < m$. Along with the answer it returns a step count of the
operations it performs: bit reads from $x$ and $y$, checks and updates.

Formalized by `Cslib.Algorithms.Lean.Graph.verifyHamiltonianCycle`, a definition declared in [CSLibExt/Algorithms/Lean/Graph/HamiltonianCycle/Basic.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/HamiltonianCycle/Basic.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-cycle/index.html#verify-hamiltonian-cycle).

## Acceptance condition of the Hamiltonian-cycle verifier

Let $x$ and $y$ be bit strings,
$m = \lfloor \sqrt{|x|} \rfloor$, and $w$ the least natural number with $m \le 2^w$. For each $i$
let $d_i$ be the number whose binary digits, least significant first, are the bits of $y$ at
positions $iw, \dots, iw + w - 1$ (counting from $0$; positions past the end of $y$ are
omitted). The Hamiltonian-cycle verifier accepts $x$ and $y$ if and only if $|x| = m^2$,
$m \ge 3$, $|y| = mw$, and for all $i, j < m$: entry $im + i$ of $x$ is false, entries $im + j$
and $jm + i$ of $x$ are equal, $d_i < m$, $d_i = d_j$ implies $i = j$, and entry
$d_i m + d_{(i+1) \bmod m}$ of $x$ exists and is true.

Formalized by `Cslib.Algorithms.Lean.Graph.verifyHamiltonianCycle_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HamiltonianCycle/Correctness.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/HamiltonianCycle/Correctness.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-cycle/index.html#verify-hamiltonian-cycle-iff).

## Soundness of the Hamiltonian-cycle verifier

If the Hamiltonian-cycle verifier accepts
the bit strings $x$ and $y$, then, with $m = \lfloor \sqrt{|x|} \rfloor$, we have $|x| = m^2$ and
$m \ge 3$, and there is a simple graph $G$ on the vertices $0, \dots, m - 1$ in which $i$ and $j$
are adjacent exactly when entry $im + j$ of $x$ (counting from $0$) is true, and $G$ has a
Hamiltonian cycle.

Formalized by `Cslib.Algorithms.Lean.Graph.verifyHamiltonianCycle_sound`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HamiltonianCycle/Correctness.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/HamiltonianCycle/Correctness.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-cycle/index.html#verify-hamiltonian-cycle-sound).

## Completeness of the Hamiltonian-cycle verifier

Let $x$ be a bit string and
$m = \lfloor \sqrt{|x|} \rfloor$, suppose $|x| = m^2$, and let $G$ be a simple graph on the
vertices $0, \dots, m - 1$ in which $i$ and $j$ are adjacent exactly when entry $im + j$ of $x$
(counting from $0$) is true. If $G$ has a Hamiltonian cycle, then there is a bit string $y$ of
length $mw$, where $w$ is the least natural number with $m \le 2^w$, such that the
Hamiltonian-cycle verifier accepts $x$ and $y$.

Formalized by `Cslib.Algorithms.Lean.Graph.verifyHamiltonianCycle_complete`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HamiltonianCycle/Correctness.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/HamiltonianCycle/Correctness.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-cycle/index.html#verify-hamiltonian-cycle-complete).

## Certificates exist exactly for Hamiltonian graphs

For every bit string $x$, with
$m = \lfloor \sqrt{|x|} \rfloor$, some bit string $y$ makes the Hamiltonian-cycle verifier accept
$x$ and $y$ if and only if $|x| = m^2$, $m \ge 3$, and there is a simple graph $G$ on the vertices
$0, \dots, m - 1$ in which $i$ and $j$ are adjacent exactly when entry $im + j$ of $x$ (counting
from $0$) is true, and $G$ has a Hamiltonian cycle.

Formalized by `Cslib.Algorithms.Lean.Graph.verifyHamiltonianCycle_language_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HamiltonianCycle/Correctness.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/HamiltonianCycle/Correctness.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-cycle/index.html#verify-hamiltonian-cycle-language-iff).

## Size of an accepted Hamiltonian-cycle certificate

If the Hamiltonian-cycle verifier
accepts the bit strings $x$ and $y$, then $|y| = mw$, where $m = \lfloor \sqrt{|x|} \rfloor$ and
$w$ is the least natural number with $m \le 2^w$, and moreover $|y| \le |x|$.

Formalized by `Cslib.Algorithms.Lean.Graph.verifyHamiltonianCycle_certificate_size`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HamiltonianCycle/Bounds.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/HamiltonianCycle/Bounds.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-cycle/index.html#verify-hamiltonian-cycle-certificate-siz).

## Quadratic step bound for the Hamiltonian-cycle verifier

There is a constant $c > 0$ such
that for all bit strings $x$ and $y$, the step count of the Hamiltonian-cycle verifier on $x$ and
$y$ is at most $c\,(|x| + |y| + 1)^2$.

Formalized by `Cslib.Algorithms.Lean.Graph.verifyHamiltonianCycle_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HamiltonianCycle/Bounds.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/HamiltonianCycle/Bounds.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-cycle/index.html#verify-hamiltonian-cycle-time-le).

## Step bound for accepted Hamiltonian-cycle certificates

There is a constant $c > 0$ such
that for all bit strings $x$ and $y$ that the Hamiltonian-cycle verifier accepts, its step count
on $x$ and $y$ is at most $c\,(|x| + 1)^2$.

Formalized by `Cslib.Algorithms.Lean.Graph.verifyHamiltonianCycle_time_le_of_accept`, a theorem declared in [CSLibExt/Algorithms/Lean/Graph/HamiltonianCycle/Bounds.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Graph/HamiltonianCycle/Bounds.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-cycle/index.html#verify-hamiltonian-cycle-time-le-of-acce).

## Instances of HAMILTONIAN CYCLE (UNDIRECTED)

An instance of HAMILTONIAN CYCLE
(UNDIRECTED) is a pair $(n, E)$ of a natural number $n$, the number of vertices, and a finite
list $E$ of pairs of natural numbers, the edges.

Formalized by `MetaMathlibExt.Complexity.NPComplete.HamiltonianCycleUndirected.HamiltonianCycleUndirectedInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/HamiltonianCycleUndirectedWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/HamiltonianCycleUndirectedWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-cycle/index.html#hamiltonian-cycle-undirected-instance).

## Graph of a HAMILTONIAN CYCLE (UNDIRECTED) instance

For an instance $(n, E)$, its graph
is the simple graph on the vertices $\{0, \dots, n-1\}$ in which distinct vertices $i$ and $j$
are adjacent when $(i, j)$ or $(j, i)$ belongs to $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.HamiltonianCycleUndirected.Graph`, a definition declared in [WantedExt/Complexity/NPComplete/HamiltonianCycleUndirectedWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/HamiltonianCycleUndirectedWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-cycle/index.html#graph).

## Well-formed HAMILTONIAN CYCLE (UNDIRECTED) instances

An instance $(n, E)$ is well formed
when $0 < n$, the list $E$ has no repeated entries, and every pair $(u, v)$ in $E$ satisfies
$u < n$, $v < n$ and $u \ne v$, and its reversal $(v, u)$ does not belong to $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.HamiltonianCycleUndirected.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/HamiltonianCycleUndirectedWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/HamiltonianCycleUndirectedWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-cycle/index.html#well-formed).

## Feasible HAMILTONIAN CYCLE (UNDIRECTED) instances

An instance $(n, E)$ is feasible when
$n \ge 3$ and its graph has a Hamiltonian cycle, that is, a cycle that visits every vertex exactly
once.

Formalized by `MetaMathlibExt.Complexity.NPComplete.HamiltonianCycleUndirected.HamiltonianCycleUndirectedFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/HamiltonianCycleUndirectedWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/HamiltonianCycleUndirectedWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-cycle/index.html#hamiltonian-cycle-undirected-feasible).

## HAMILTONIAN CYCLE (UNDIRECTED) as a decision problem

The decision problem HAMILTONIAN
CYCLE (UNDIRECTED) accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring
encoding, to a well-formed instance $(n, E)$ with $n \ge 3$ whose graph has a Hamiltonian cycle.
It rejects every bitstring that does not decode to an instance.

Formalized by `MetaMathlibExt.Complexity.NPComplete.HamiltonianCycleUndirected.hamiltonianCycleUndirectedDec`, a definition declared in [WantedExt/Complexity/NPComplete/HamiltonianCycleUndirectedWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/HamiltonianCycleUndirectedWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-cycle/index.html#hamiltonian-cycle-undirected-dec).

## HAMILTONIAN CYCLE (UNDIRECTED) is NP-complete

The decision problem HAMILTONIAN CYCLE
(UNDIRECTED) belongs to NP, and every decision problem in NP has a polynomial-time many-one
reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), HAMILTONIAN CIRCUIT; R. M. Karp, "Reducibility among combinatorial problems" (1972).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.HamiltonianCycleUndirected.hamiltonianCycleUndirected_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/HamiltonianCycleUndirectedWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/HamiltonianCycleUndirectedWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-cycle/index.html#hamiltonian-cycle-undirected-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Undirected Hamiltonian cycle](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-cycle/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/undirected-hamiltonian-cycle)
