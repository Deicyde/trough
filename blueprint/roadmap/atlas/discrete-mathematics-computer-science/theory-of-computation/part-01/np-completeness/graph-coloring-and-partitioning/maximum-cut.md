---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MaxCut.MaxCutInstance, MetaMathlibExt.Complexity.NPComplete.MaxCut.WellFormed, MetaMathlibExt.Complexity.NPComplete.MaxCut.MaxCutFeasible, MetaMathlibExt.Complexity.NPComplete.MaxCut.maxCutDec, MetaMathlibExt.Complexity.NPComplete.MaxCut.maxCut_npComplete
statement: formalized
---

# Maximum cut

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/maximum-cut/index.html).

## Instances of MAXIMUM CUT

An instance of MAXIMUM CUT is a triple $(n, E, K)$ of a natural
number $n$ (the number of vertices), a finite list $E$ of ordered pairs of natural numbers (the
edges) and a natural number $K$ (the bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxCut.MaxCutInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MaxCutWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaxCutWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/maximum-cut/index.html#max-cut-instance).

## Well-formed MAXIMUM CUT instances

An instance $(n, E, K)$ of MAXIMUM CUT is well formed
when the list $E$ has no repeated entries and every pair $(u, v)$ in $E$ satisfies $u < n$,
$v < n$ and $u \ne v$, and the reversed pair $(v, u)$ does not occur in $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxCut.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/MaxCutWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaxCutWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/maximum-cut/index.html#well-formed).

## Feasible MAXIMUM CUT instances

An instance $(n, E, K)$ of MAXIMUM CUT is feasible when
there are a finite set $S$ of natural numbers, all less than $n$, and a list $C$ of length at
least $K$ obtained from $E$ by deleting zero or more of its entries, such that every pair
$(u, v)$ in $C$ has exactly one of $u$ and $v$ in $S$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxCut.MaxCutFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MaxCutWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaxCutWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/maximum-cut/index.html#max-cut-feasible).

## MAXIMUM CUT as a decision problem

The decision problem MAXIMUM CUT accepts a bitstring
$x$ exactly when decoding $x$ with the canonical bitstring encoding of instances of MAXIMUM CUT
succeeds and yields an instance that is well formed and feasible. All other bitstrings, including
those that fail to decode, are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxCut.maxCutDec`, a definition declared in [WantedExt/Complexity/NPComplete/MaxCutWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaxCutWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/maximum-cut/index.html#max-cut-dec).

## MAXIMUM CUT is NP-complete

The decision problem MAXIMUM CUT lies in NP, and every
decision problem in NP has a polynomial-time many-one reduction to MAXIMUM CUT.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), MAXIMUM CUT.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MaxCut.maxCut_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MaxCutWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaxCutWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/maximum-cut/index.html#max-cut-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximum cut](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/maximum-cut/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/maximum-cut)
