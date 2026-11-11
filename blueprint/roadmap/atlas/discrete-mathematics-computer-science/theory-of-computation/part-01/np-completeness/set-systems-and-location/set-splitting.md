---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.SetSplitting.SetSplittingInstance, MetaMathlibExt.Complexity.NPComplete.SetSplitting.WellFormed, MetaMathlibExt.Complexity.NPComplete.SetSplitting.SetSplittingFeasible, MetaMathlibExt.Complexity.NPComplete.SetSplitting.setSplittingDec, MetaMathlibExt.Complexity.NPComplete.SetSplitting.setSplitting_npComplete
statement: formalized
---

# Set splitting

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-splitting/index.html).

## Set-splitting instances

A set-splitting instance is a pair $(n, C)$ of a natural number
$n$, the size of the universe, and a list $C$ of lists of natural numbers, the subsets to be
split.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SetSplitting.SetSplittingInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/SetSplittingWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/SetSplittingWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-splitting/index.html#set-splitting-instance).

## Well-formed set-splitting instances

A set-splitting instance $(n, C)$, a natural number
$n$ together with a list $C$ of lists of natural numbers, is well formed when every list in $C$
has no repeated entries and all its entries are less than $n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SetSplitting.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/SetSplittingWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/SetSplittingWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-splitting/index.html#well-formed).

## Feasible set-splitting instances

A set-splitting instance $(n, C)$, a natural number $n$
together with a list $C$ of lists of natural numbers, is feasible when there is a finite set $S$
of natural numbers, all less than $n$, such that every list in $C$ has an entry in $S$ and an
entry not in $S$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SetSplitting.SetSplittingFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/SetSplittingWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/SetSplittingWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-splitting/index.html#set-splitting-feasible).

## The SET SPLITTING decision problem

SET SPLITTING is the decision problem that accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a pair
$(n, C)$ of a natural number $n$ and a list $C$ of lists of natural numbers such that every list
in $C$ has no repeated entries and only entries less than $n$, and some finite set $S$ of natural
numbers less than $n$ contains an entry of every list in $C$ and misses an entry of every list in
$C$. Bitstrings that do not decode to such a pair are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SetSplitting.setSplittingDec`, a definition declared in [WantedExt/Complexity/NPComplete/SetSplittingWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/SetSplittingWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-splitting/index.html#set-splitting-dec).

## SET SPLITTING is NP-complete

The SET SPLITTING decision problem belongs to NP, and every
decision problem in NP reduces to it by a polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), SET SPLITTING (hypergraph 2-coloring); S. Lovasz, "Coverings and colorings of hypergraphs" (1973).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.SetSplitting.setSplitting_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/SetSplittingWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/SetSplittingWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-splitting/index.html#set-splitting-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Set splitting](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-splitting/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-splitting)
