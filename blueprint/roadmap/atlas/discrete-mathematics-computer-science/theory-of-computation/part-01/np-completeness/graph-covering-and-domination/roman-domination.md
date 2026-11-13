---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.RomanDomination.RomanDominationInstance, MetaMathlibExt.Complexity.NPComplete.RomanDomination.Graph, MetaMathlibExt.Complexity.NPComplete.RomanDomination.WellFormed, MetaMathlibExt.Complexity.NPComplete.RomanDomination.RomanDominationFeasible, MetaMathlibExt.Complexity.NPComplete.RomanDomination.romanDominationDec, MetaMathlibExt.Complexity.NPComplete.RomanDomination.romanDomination_npComplete
statement: formalized
---

# Roman domination

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/roman-domination/index.html).

## Roman domination instances

An instance of ROMAN DOMINATION is a triple $(n, E, K)$ of a
natural number $n$, the number of vertices, a list $E$ of pairs of natural numbers, the edges,
and a natural number $K$, the weight bound.

Formalized by `MetaMathlibExt.Complexity.NPComplete.RomanDomination.RomanDominationInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/RomanDominationWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/RomanDominationWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/roman-domination/index.html#roman-domination-instance).

## Graph of a Roman domination instance

For an instance $(n, E, K)$ of ROMAN DOMINATION,
its graph is the graph of the edge list $E$ on $n$ vertices: the simple graph on
$\{0, \dots, n - 1\}$ in which distinct vertices $i$ and $j$ are adjacent when $(i, j)$ or
$(j, i)$ belongs to $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.RomanDomination.Graph`, a definition declared in [WantedExt/Complexity/NPComplete/RomanDominationWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/RomanDominationWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/roman-domination/index.html#graph).

## Well-formed Roman domination instances

An instance $(n, E, K)$ of ROMAN DOMINATION is
well formed when the list $E$ has no repeated entries and every pair $(u, v)$ in $E$ has
$u < n$, $v < n$, $u \ne v$ and $(v, u) \notin E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.RomanDomination.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/RomanDominationWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/RomanDominationWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/roman-domination/index.html#well-formed).

## Feasible Roman domination instances

An instance $(n, E, K)$ of ROMAN DOMINATION is
feasible when there is a function $f$ from the vertices $\{0, \dots, n - 1\}$ of its graph to
$\{0, 1, 2\}$ such that every vertex $v$ with $f(v) = 0$ is adjacent to some vertex $u$ with
$f(u) = 2$, and the total weight $\sum_v f(v)$ is at most $K$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.RomanDomination.RomanDominationFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/RomanDominationWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/RomanDominationWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/roman-domination/index.html#roman-domination-feasible).

## ROMAN DOMINATION as a decision problem

The decision problem ROMAN DOMINATION accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to an instance
$(n, E, K)$ of ROMAN DOMINATION that is well formed and feasible; it rejects every other
bitstring.

Formalized by `MetaMathlibExt.Complexity.NPComplete.RomanDomination.romanDominationDec`, a definition declared in [WantedExt/Complexity/NPComplete/RomanDominationWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/RomanDominationWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/roman-domination/index.html#roman-domination-dec).

## ROMAN DOMINATION is NP-complete

The decision problem ROMAN DOMINATION belongs to NP, and
every decision problem in NP reduces to it by a polynomial-time many-one reduction.

## Sources

- E. J. Cockayne, P. A. Dreyer Jr., S. M. Hedetniemi, and S. T. Hedetniemi, "Roman domination in graphs", Discrete Mathematics 278 (2004), 11-22.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.RomanDomination.romanDomination_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/RomanDominationWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/RomanDominationWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/roman-domination/index.html#roman-domination-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Roman domination](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/roman-domination/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/roman-domination)
