---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.SteinerTree.SteinerTreeInstance, MetaMathlibExt.Complexity.NPComplete.SteinerTree.Graph, MetaMathlibExt.Complexity.NPComplete.SteinerTree.WellFormed, MetaMathlibExt.Complexity.NPComplete.SteinerTree.SteinerTreeFeasible, MetaMathlibExt.Complexity.NPComplete.SteinerTree.steinerTreeDec, MetaMathlibExt.Complexity.NPComplete.SteinerTree.steinerTree_npComplete
statement: formalized
---

# Steiner tree

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/steiner-tree/index.html).

## Steiner tree instances

A Steiner tree instance is a quadruple $(n, E, R, K)$ of a
natural number $n$ (the number of vertices), a list $E$ of triples $(u, v, w)$ of natural numbers
(an edge between $u$ and $v$ of weight $w$), a list $R$ of natural numbers (the terminals) and a
natural number $K$ (the budget).

Formalized by `MetaMathlibExt.Complexity.NPComplete.SteinerTree.SteinerTreeInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/SteinerTreeWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SteinerTreeWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/steiner-tree/index.html#steiner-tree-instance).

## Graph of a candidate edge set

Given a Steiner tree instance with vertex count $n$ and a
list $T$ of triples $(u, v, w)$ of natural numbers, the graph of $T$ is the simple graph on
$\{0, \dots, n - 1\}$ in which distinct vertices $i$ and $j$ are adjacent when $(i, j, w)$ or
$(j, i, w)$ belongs to $T$ for some natural number $w$. Weights are ignored, and triples with an
endpoint at least $n$ contribute no edge.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SteinerTree.Graph`, a definition declared in [WantedExt/Complexity/NPComplete/SteinerTreeWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SteinerTreeWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/steiner-tree/index.html#graph).

## Well-formed Steiner tree instances

A Steiner tree instance with vertex count $n$, edge
list $E$ of triples $(u, v, w)$ and terminal list $R$ is well formed when $E$ has no repeated
entries; every $(u, v, w)$ in $E$ has $u < n$, $v < n$, $u \ne v$ and $w > 0$; any two entries
of $E$ with the same endpoints, in the same or the reverse order, are equal; $R$ has no repeated
entries; and every terminal in $R$ is less than $n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SteinerTree.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/SteinerTreeWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SteinerTreeWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/steiner-tree/index.html#well-formed).

## Feasible Steiner tree instances

A Steiner tree instance with vertex count $n$, edge list
$E$ of triples $(u, v, w)$, terminal list $R$ and budget $K$ is feasible when every terminal in
$R$ is less than $n$ and there is a sublist $T$ of $E$ (a not necessarily contiguous
subsequence) whose weights $w$ sum to at most $K$ such that any two terminals in $R$ are joined
by a path in the graph of $T$, the simple graph on $\{0, \dots, n - 1\}$ in which distinct
vertices are adjacent when they are the endpoints $u, v$ of some triple in $T$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SteinerTree.SteinerTreeFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/SteinerTreeWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SteinerTreeWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/steiner-tree/index.html#steiner-tree-feasible).

## The STEINER TREE decision problem

The decision problem STEINER TREE accepts a bitstring
$x$ exactly when $x$ decodes, under the canonical bitstring encoding of Steiner tree instances,
to a Steiner tree instance that is both well formed and feasible. Bitstrings that do not decode
are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SteinerTree.steinerTreeDec`, a definition declared in [WantedExt/Complexity/NPComplete/SteinerTreeWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SteinerTreeWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/steiner-tree/index.html#steiner-tree-dec).

## STEINER TREE is NP-complete

The decision problem STEINER TREE belongs to NP, and every
decision problem in NP reduces to STEINER TREE by a polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), STEINER TREE IN GRAPHS; R. M. Karp, "Reducibility among combinatorial problems" (1972).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.SteinerTree.steinerTree_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/SteinerTreeWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/SteinerTreeWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/steiner-tree/index.html#steiner-tree-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Steiner tree](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/steiner-tree/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/steiner-tree)
