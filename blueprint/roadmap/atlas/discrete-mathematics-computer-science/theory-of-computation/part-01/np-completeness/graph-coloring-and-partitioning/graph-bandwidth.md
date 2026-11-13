---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.Bandwidth.BandwidthInstance, MetaMathlibExt.Complexity.NPComplete.Bandwidth.WellFormed, MetaMathlibExt.Complexity.NPComplete.Bandwidth.BandwidthFeasible, MetaMathlibExt.Complexity.NPComplete.Bandwidth.bandwidthDec, MetaMathlibExt.Complexity.NPComplete.Bandwidth.bandwidth_npComplete
statement: formalized
---

# Graph bandwidth

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-bandwidth/index.html).

## BANDWIDTH instances

An instance of BANDWIDTH is a triple $(n, E, K)$ of a natural number
$n$ (the number of vertices), a list $E$ of ordered pairs of natural numbers (the edges) and a
natural number $K$ (the bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.Bandwidth.BandwidthInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/BandwidthWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/BandwidthWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-bandwidth/index.html#bandwidth-instance).

## Well-formed BANDWIDTH instances

A BANDWIDTH instance $(n, E, K)$ is well formed when the
list $E$ has no repeated entries and every pair $(u, v)$ in $E$ satisfies $u < n$, $v < n$ and
$u \ne v$, and its reverse $(v, u)$ does not occur in $E$. Thus $E$ lists the edges of a loopless
undirected graph on the vertices $0, \dots, n-1$, each edge exactly once.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Bandwidth.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/BandwidthWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/BandwidthWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-bandwidth/index.html#well-formed).

## BANDWIDTH feasibility

A BANDWIDTH instance $(n, E, K)$ is feasible when there is an
ordering of the numbers $0, \dots, n-1$ such that $|p(u) - p(v)| \le K$ for every pair $(u, v)$
in $E$, where $p(m)$ is the position of $m$ in the ordering, counting from $0$, and $p(m) = n$
when $m$ is not among $0, \dots, n-1$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Bandwidth.BandwidthFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/BandwidthWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/BandwidthWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-bandwidth/index.html#bandwidth-feasible).

## The BANDWIDTH decision problem

BANDWIDTH accepts a bitstring $x$ exactly when $x$
decodes, under the canonical bitstring encoding of triples $(n, E, K)$ of a natural number, a
list of pairs of natural numbers and a natural number, to a BANDWIDTH instance that is both well
formed and feasible. Bitstrings that do not decode to such a triple are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Bandwidth.bandwidthDec`, a definition declared in [WantedExt/Complexity/NPComplete/BandwidthWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/BandwidthWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-bandwidth/index.html#bandwidth-dec).

## BANDWIDTH is NP-complete

The BANDWIDTH decision problem belongs to NP, and every decision
problem in NP has a polynomial-time many-one reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), BANDWIDTH; C. H. Papadimitriou, "The NP-completeness of the bandwidth minimization problem" (1976).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.Bandwidth.bandwidth_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/BandwidthWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/BandwidthWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-bandwidth/index.html#bandwidth-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Graph bandwidth](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-bandwidth/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-bandwidth)
