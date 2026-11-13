---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.ExactCoverBy3Sets.ExactCoverBy3SetsInstance, MetaMathlibExt.Complexity.NPComplete.ExactCoverBy3Sets.WellFormed, MetaMathlibExt.Complexity.NPComplete.ExactCoverBy3Sets.ExactCoverBy3SetsFeasible, MetaMathlibExt.Complexity.NPComplete.ExactCoverBy3Sets.exactCoverBy3SetsDec, MetaMathlibExt.Complexity.NPComplete.ExactCoverBy3Sets.exactCoverBy3Sets_npComplete
statement: formalized
---

# Exact cover by 3-sets

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/exact-cover-by-3-sets/index.html).

## Instances of EXACT COVER BY 3-SETS

An instance of EXACT COVER BY 3-SETS is a pair
$(q, C)$ of a natural number $q$ and a finite list $C$ of finite lists of natural numbers. The
intended universe is $\{0, \dots, 3q - 1\}$ and the entries of $C$ are the candidate
three-element subsets; that each entry lists three distinct elements of the universe is
required by well-formedness, not by the type of instances.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ExactCoverBy3Sets.ExactCoverBy3SetsInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/ExactCoverBy3SetsWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ExactCoverBy3SetsWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/exact-cover-by-3-sets/index.html#exact-cover-by3-sets-instance).

## Well-formed EXACT COVER BY 3-SETS instances

An instance $(q, C)$ of EXACT COVER BY
3-SETS is well formed when every entry of $C$ is a list of exactly three pairwise distinct
natural numbers, each less than $3q$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ExactCoverBy3Sets.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/ExactCoverBy3SetsWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ExactCoverBy3SetsWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/exact-cover-by-3-sets/index.html#well-formed).

## Feasible EXACT COVER BY 3-SETS instances

An instance $(q, C)$ of EXACT COVER BY 3-SETS
is feasible when $C$ has a sublist $S$, obtained by deleting some entries of $C$, such that for
every natural number $x < 3q$ there is exactly one list that occurs in $S$ and contains $x$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ExactCoverBy3Sets.ExactCoverBy3SetsFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/ExactCoverBy3SetsWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ExactCoverBy3SetsWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/exact-cover-by-3-sets/index.html#exact-cover-by3-sets-feasible).

## EXACT COVER BY 3-SETS as a decision problem

The decision problem EXACT COVER BY 3-SETS
accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding of pairs
of a natural number and a list of lists of natural numbers, to an instance of EXACT COVER BY
3-SETS that is well formed and feasible; bitstrings that do not decode are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ExactCoverBy3Sets.exactCoverBy3SetsDec`, a definition declared in [WantedExt/Complexity/NPComplete/ExactCoverBy3SetsWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ExactCoverBy3SetsWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/exact-cover-by-3-sets/index.html#exact-cover-by3-sets-dec).

## EXACT COVER BY 3-SETS is NP-complete

The decision problem EXACT COVER BY 3-SETS is in
NP, and every decision problem in NP has a polynomial-time many-one reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), EXACT COVER BY 3-SETS.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.ExactCoverBy3Sets.exactCoverBy3Sets_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/ExactCoverBy3SetsWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ExactCoverBy3SetsWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/exact-cover-by-3-sets/index.html#exact-cover-by3-sets-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exact cover by 3-sets](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/exact-cover-by-3-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/exact-cover-by-3-sets)
