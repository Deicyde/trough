---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.ListColoring.ListColoringInstance, MetaMathlibExt.Complexity.NPComplete.ListColoring.WellFormed, MetaMathlibExt.Complexity.NPComplete.ListColoring.ListColoringFeasible, MetaMathlibExt.Complexity.NPComplete.ListColoring.listColoringDec, MetaMathlibExt.Complexity.NPComplete.ListColoring.listColoring_npComplete
statement: formalized
---

# List coloring

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/list-coloring/index.html).

## List-coloring instances

A list-coloring instance is a triple $(n, E, L)$ of a natural
number $n$ (the number of vertices), a list $E$ of pairs of natural numbers (the edges), and a
list $L$ of lists of natural numbers (the allowed colors of each vertex).

Formalized by `MetaMathlibExt.Complexity.NPComplete.ListColoring.ListColoringInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/ListColoringWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ListColoringWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/list-coloring/index.html#list-coloring-instance).

## Well-formed list-coloring instances

A list-coloring instance $(n, E, L)$ is well formed
when the edge list $E$ has no repeated entries, every edge $(u, v)$ in $E$ satisfies $u < n$,
$v < n$ and $u \ne v$ and its reversal $(v, u)$ does not occur in $E$, and the list $L$ of
color lists has length $n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ListColoring.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/ListColoringWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ListColoringWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/list-coloring/index.html#well-formed).

## Feasible list-coloring instances

A list-coloring instance $(n, E, L)$ is feasible when
there is a list $c = (c_0, \dots, c_{n-1})$ of $n$ natural numbers such that for every $v < n$
the number $c_v$ belongs to the $v$-th entry $L_v$ of $L$ (taken to be the empty list when $L$
has at most $v$ entries), and $c_u \ne c_v$ for every edge $(u, v)$ in $E$, where $c_w$ is read
as $0$ when $w \ge n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ListColoring.ListColoringFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/ListColoringWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ListColoringWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/list-coloring/index.html#list-coloring-feasible).

## The LIST COLORING decision problem

LIST COLORING is the decision problem that
accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a
list-coloring instance that is well formed and feasible. Bitstrings that do not decode are
rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ListColoring.listColoringDec`, a definition declared in [WantedExt/Complexity/NPComplete/ListColoringWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ListColoringWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/list-coloring/index.html#list-coloring-dec).

## LIST COLORING is NP-complete

The LIST COLORING decision problem belongs to NP, and every
decision problem in NP reduces to it by a polynomial-time many-one reduction.

## Sources

- J. Kratochvíl and Z. Tuza, "Algorithmic complexity of list colorings", Discrete Applied Mathematics, 1994.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.ListColoring.listColoring_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/ListColoringWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ListColoringWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/list-coloring/index.html#list-coloring-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: List coloring](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/list-coloring/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/list-coloring)
