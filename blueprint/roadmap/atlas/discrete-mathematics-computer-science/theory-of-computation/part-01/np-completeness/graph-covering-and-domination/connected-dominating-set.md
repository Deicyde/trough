---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.ConnectedDominatingSet.ConnectedDominatingSetInstance, MetaMathlibExt.Complexity.NPComplete.ConnectedDominatingSet.Graph, MetaMathlibExt.Complexity.NPComplete.ConnectedDominatingSet.WellFormed, MetaMathlibExt.Complexity.NPComplete.ConnectedDominatingSet.ConnectedDominatingSetFeasible, MetaMathlibExt.Complexity.NPComplete.ConnectedDominatingSet.connectedDominatingSetDec, MetaMathlibExt.Complexity.NPComplete.ConnectedDominatingSet.connectedDominatingSet_npComplete
statement: formalized
---

# Connected dominating set

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/connected-dominating-set/index.html).

## Instances of CONNECTED DOMINATING SET

An instance of CONNECTED DOMINATING SET is a triple
$(n, E, K)$ of a natural number $n$ (the number of vertices), a list $E$ of pairs of natural
numbers (the edges) and a natural number $K$ (the bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.ConnectedDominatingSet.ConnectedDominatingSetInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/ConnectedDominatingSetWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ConnectedDominatingSetWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/connected-dominating-set/index.html#connected-dominating-set-instance).

## Graph of a CONNECTED DOMINATING SET instance

For an instance $(n, E, K)$ of CONNECTED
DOMINATING SET, its graph is the simple graph on the vertex set $\{0, \dots, n - 1\}$ in which
distinct vertices $i$ and $j$ are adjacent when $(i, j)$ or $(j, i)$ belongs to $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ConnectedDominatingSet.Graph`, a definition declared in [WantedExt/Complexity/NPComplete/ConnectedDominatingSetWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ConnectedDominatingSetWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/connected-dominating-set/index.html#graph).

## Well-formed CONNECTED DOMINATING SET instances

An instance $(n, E, K)$ of CONNECTED
DOMINATING SET is well formed when the list $E$ has no repeated entries and every pair $(u, v)$
in $E$ has $u < n$, $v < n$ and $u \ne v$, with the reversed pair $(v, u)$ not in $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ConnectedDominatingSet.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/ConnectedDominatingSetWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ConnectedDominatingSetWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/connected-dominating-set/index.html#well-formed).

## Feasible CONNECTED DOMINATING SET instances

An instance $(n, E, K)$ of CONNECTED
DOMINATING SET is feasible when there is a set $S$ of vertices of its graph $G$ with at most $K$
elements such that every vertex of $G$ lies in $S$ or is adjacent in $G$ to a vertex of $S$, and
the subgraph of $G$ induced by $S$ is connected (in particular, $S$ is nonempty).

Formalized by `MetaMathlibExt.Complexity.NPComplete.ConnectedDominatingSet.ConnectedDominatingSetFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/ConnectedDominatingSetWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ConnectedDominatingSetWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/connected-dominating-set/index.html#connected-dominating-set-feasible).

## The decision problem CONNECTED DOMINATING SET

CONNECTED DOMINATING SET accepts a bitstring
$x$ exactly when $x$ decodes, under the canonical bitstring encoding, to an instance of CONNECTED
DOMINATING SET that is well formed and feasible. Bitstrings that do not decode to an instance are
rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ConnectedDominatingSet.connectedDominatingSetDec`, a definition declared in [WantedExt/Complexity/NPComplete/ConnectedDominatingSetWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ConnectedDominatingSetWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/connected-dominating-set/index.html#connected-dominating-set-dec).

## CONNECTED DOMINATING SET is NP-complete

The decision problem CONNECTED DOMINATING SET
belongs to NP, and every decision problem in NP reduces to it by a polynomial-time many-one
reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), CONNECTED DOMINATING SET.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.ConnectedDominatingSet.connectedDominatingSet_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/ConnectedDominatingSetWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ConnectedDominatingSetWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/connected-dominating-set/index.html#connected-dominating-set-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Connected dominating set](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/connected-dominating-set/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/connected-dominating-set)
