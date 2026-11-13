---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MaxKCut.MaxKCutInstance, MetaMathlibExt.Complexity.NPComplete.MaxKCut.WellFormed, MetaMathlibExt.Complexity.NPComplete.MaxKCut.MaxKCutFeasible, MetaMathlibExt.Complexity.NPComplete.MaxKCut.maxKCutDec, MetaMathlibExt.Complexity.NPComplete.MaxKCut.maxKCut_npComplete
statement: formalized
---

# Maximum k-cut

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/maximum-k-cut/index.html).

## Instances of MAXIMUM k-CUT

An instance of MAXIMUM k-CUT is a quadruple $(n, E, k, K)$ of
a natural number $n$ (the number of vertices), a finite list $E$ of ordered pairs of natural
numbers (the edges), a natural number $k$ (the number of parts) and a natural number $K$ (the
bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxKCut.MaxKCutInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MaxKCutWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaxKCutWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/maximum-k-cut/index.html#max-kcut-instance).

## Well-formed MAXIMUM k-CUT instances

An instance $(n, E, k, K)$ of MAXIMUM k-CUT is well
formed when the list $E$ has no repeated entries and every pair $(u, v)$ in $E$ satisfies
$u < n$, $v < n$ and $u \ne v$, and the reversed pair $(v, u)$ does not occur in $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxKCut.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/MaxKCutWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaxKCutWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/maximum-k-cut/index.html#well-formed).

## Feasible MAXIMUM k-CUT instances

An instance $(n, E, k, K)$ of MAXIMUM k-CUT is feasible
when there are a list $(a_0, \dots, a_{n-1})$ of $n$ natural numbers, each less than $k$, and a
list $C$ of length at least $K$ obtained from $E$ by deleting zero or more of its entries, such
that $a_u \ne a_v$ for every pair $(u, v)$ in $C$, where $a_w$ is read as $0$ when $w \ge n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxKCut.MaxKCutFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MaxKCutWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaxKCutWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/maximum-k-cut/index.html#max-kcut-feasible).

## MAXIMUM k-CUT as a decision problem

The decision problem MAXIMUM k-CUT accepts a
bitstring $x$ exactly when decoding $x$ with the canonical bitstring encoding of instances of
MAXIMUM k-CUT succeeds and yields an instance that is well formed and feasible. All other
bitstrings, including those that fail to decode, are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxKCut.maxKCutDec`, a definition declared in [WantedExt/Complexity/NPComplete/MaxKCutWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaxKCutWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/maximum-k-cut/index.html#max-kcut-dec).

## MAXIMUM k-CUT is NP-complete

The decision problem MAXIMUM k-CUT lies in NP, and every
decision problem in NP has a polynomial-time many-one reduction to MAXIMUM k-CUT.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), MAXIMUM k-CUT (the `k = 2` slice is MAX CUT).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MaxKCut.maxKCut_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MaxKCutWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaxKCutWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/maximum-k-cut/index.html#max-kcut-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximum k-cut](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/maximum-k-cut/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/maximum-k-cut)
