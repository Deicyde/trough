---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.ThreeDimensionalMatching.ThreeDimensionalMatchingInstance, MetaMathlibExt.Complexity.NPComplete.ThreeDimensionalMatching.WellFormed, MetaMathlibExt.Complexity.NPComplete.ThreeDimensionalMatching.ThreeDimensionalMatchingFeasible, MetaMathlibExt.Complexity.NPComplete.ThreeDimensionalMatching.threeDimensionalMatchingDec, MetaMathlibExt.Complexity.NPComplete.ThreeDimensionalMatching.threeDimensionalMatching_npComplete
statement: formalized
---

# 3-dimensional matching

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/3-dimensional-matching/index.html).

## 3-dimensional matching instances

An instance of 3-DIMENSIONAL MATCHING is a pair $(n, T)$
of a natural number $n$, the part size, and a finite list $T$ of triples of natural numbers.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ThreeDimensionalMatching.ThreeDimensionalMatchingInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/ThreeDimensionalMatchingWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ThreeDimensionalMatchingWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/3-dimensional-matching/index.html#three-dimensional-matching-instance).

## Well-formed 3-dimensional matching instances

A 3-dimensional matching instance $(n, T)$
is well formed when each of the three coordinates of every triple in $T$ is less than $n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ThreeDimensionalMatching.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/ThreeDimensionalMatchingWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ThreeDimensionalMatchingWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/3-dimensional-matching/index.html#well-formed).

## Feasible 3-dimensional matching instances

A 3-dimensional matching instance $(n, T)$ is
feasible, or has a perfect matching, when there is a list $M$ of length $n$, obtained from the
list of triples $T$ by deleting some of its entries, such that for each of the three coordinate
positions, every natural number $a < n$ occurs in that position in exactly one triple of $M$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ThreeDimensionalMatching.ThreeDimensionalMatchingFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/ThreeDimensionalMatchingWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ThreeDimensionalMatchingWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/3-dimensional-matching/index.html#three-dimensional-matching-feasible).

## 3-DIMENSIONAL MATCHING as a decision problem

The decision problem 3-DIMENSIONAL MATCHING
accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a
3-dimensional matching instance $(n, T)$ that is well formed (every coordinate of every triple in
$T$ is less than $n$) and feasible (it has a perfect matching). Bitstrings that do not decode to
an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ThreeDimensionalMatching.threeDimensionalMatchingDec`, a definition declared in [WantedExt/Complexity/NPComplete/ThreeDimensionalMatchingWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ThreeDimensionalMatchingWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/3-dimensional-matching/index.html#three-dimensional-matching-dec).

## 3-DIMENSIONAL MATCHING is NP-complete

The decision problem 3-DIMENSIONAL MATCHING on
bitstrings is in NP, and every decision problem in NP reduces to it by a polynomial-time many-one
reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), 3-DIMENSIONAL MATCHING; R. M. Karp, "Reducibility among combinatorial problems" (1972).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.ThreeDimensionalMatching.threeDimensionalMatching_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/ThreeDimensionalMatchingWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ThreeDimensionalMatchingWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/3-dimensional-matching/index.html#three-dimensional-matching-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: 3-dimensional matching](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/3-dimensional-matching/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/3-dimensional-matching)
