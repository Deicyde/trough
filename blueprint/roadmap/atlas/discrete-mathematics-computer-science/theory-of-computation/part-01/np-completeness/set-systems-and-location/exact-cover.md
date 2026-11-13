---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.ExactCover.ExactCoverInstance, MetaMathlibExt.Complexity.NPComplete.ExactCover.WellFormed, MetaMathlibExt.Complexity.NPComplete.ExactCover.ExactCoverFeasible, MetaMathlibExt.Complexity.NPComplete.ExactCover.exactCoverDec, MetaMathlibExt.Complexity.NPComplete.ExactCover.exactCover_npComplete
statement: formalized
---

# Exact cover

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/exact-cover/index.html).

## Instances of EXACT COVER

An instance of EXACT COVER is a pair $(n, C)$ of a natural
number $n$, the size of the universe $\{0, \dots, n - 1\}$, and a finite list $C$ of finite lists
of natural numbers, the candidate subsets. That each entry of $C$ lists distinct elements of the
universe is required by well-formedness, not by the type of instances.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ExactCover.ExactCoverInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/ExactCoverWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ExactCoverWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/exact-cover/index.html#exact-cover-instance).

## Well-formed EXACT COVER instances

An instance $(n, C)$ of EXACT COVER is well formed
when every entry of $C$ is a list of pairwise distinct natural numbers, each less than $n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ExactCover.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/ExactCoverWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ExactCoverWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/exact-cover/index.html#well-formed).

## Feasible EXACT COVER instances

An instance $(n, C)$ of EXACT COVER is feasible when $C$
has a sublist $S$, obtained by deleting some entries of $C$, such that for every natural number
$x < n$ there is exactly one list that occurs in $S$ and contains $x$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ExactCover.ExactCoverFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/ExactCoverWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ExactCoverWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/exact-cover/index.html#exact-cover-feasible).

## EXACT COVER as a decision problem

The decision problem EXACT COVER accepts a bitstring
$x$ exactly when $x$ decodes, under the canonical bitstring encoding of pairs of a natural number
and a list of lists of natural numbers, to an instance of EXACT COVER that is well formed and
feasible; bitstrings that do not decode are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ExactCover.exactCoverDec`, a definition declared in [WantedExt/Complexity/NPComplete/ExactCoverWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ExactCoverWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/exact-cover/index.html#exact-cover-dec).

## EXACT COVER is NP-complete

The decision problem EXACT COVER is in NP, and every decision
problem in NP has a polynomial-time many-one reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), EXACT COVER; R. M. Karp, "Reducibility among combinatorial problems" (1972).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.ExactCover.exactCover_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/ExactCoverWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ExactCoverWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/exact-cover/index.html#exact-cover-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exact cover](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/exact-cover/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/exact-cover)
