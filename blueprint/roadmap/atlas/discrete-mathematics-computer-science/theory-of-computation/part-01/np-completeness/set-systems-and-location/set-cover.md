---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.SetCover.SetCoverInstance, MetaMathlibExt.Complexity.NPComplete.SetCover.WellFormed, MetaMathlibExt.Complexity.NPComplete.SetCover.SetCoverFeasible, MetaMathlibExt.Complexity.NPComplete.SetCover.setCoverDec, MetaMathlibExt.Complexity.NPComplete.SetCover.setCover_npComplete
statement: formalized
---

# Set cover

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-cover/index.html).

## Set-cover instances

A set-cover instance is a triple $(n, C, K)$ consisting of a natural
number $n$, the size of the universe, a finite list $C$ of finite lists of natural numbers, the
subsets, and a natural number $K$, the bound.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SetCover.SetCoverInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/SetCoverWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/SetCoverWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-cover/index.html#set-cover-instance).

## Well-formed set-cover instances

A set-cover instance $(n, C, K)$ is well formed when every
list $s$ in $C$ has no repeated entries and every entry of $s$ is less than $n$, that is, each
member of $C$ lists the elements of a subset of $\{0, \dots, n - 1\}$ without repetition.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SetCover.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/SetCoverWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/SetCoverWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-cover/index.html#well-formed).

## Feasible set-cover instances

A set-cover instance $(n, C, K)$ is feasible when there is a
sublist $D$ of $C$ (a list obtained from $C$ by deleting entries while keeping their order) with
at most $K$ entries such that every natural number $x < n$ belongs to some list in $D$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SetCover.SetCoverFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/SetCoverWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/SetCoverWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-cover/index.html#set-cover-feasible).

## The SET COVER decision problem

SET COVER is the decision problem that accepts a bitstring
$x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a set-cover instance
$(n, C, K)$ that is both well formed and feasible: every list in $C$ has no repeated entries and
only entries less than $n$, and some sublist of $C$ with at most $K$ entries contains every natural
number $y < n$ in one of its lists. Bitstrings that do not decode to a set-cover instance are
rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SetCover.setCoverDec`, a definition declared in [WantedExt/Complexity/NPComplete/SetCoverWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/SetCoverWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-cover/index.html#set-cover-dec).

## SET COVER is NP-complete

The SET COVER decision problem lies in NP, and every decision
problem $L$ in NP has a polynomial-time many-one reduction to SET COVER.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), SET COVER; R. M. Karp, "Reducibility among combinatorial problems" (1972).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.SetCover.setCover_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/SetCoverWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/SetCoverWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-cover/index.html#set-cover-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Set cover](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-cover/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/set-cover)
