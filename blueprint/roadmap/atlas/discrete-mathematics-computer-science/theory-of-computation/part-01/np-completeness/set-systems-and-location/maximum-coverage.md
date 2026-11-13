---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MaximumCoverage.MaximumCoverageInstance, MetaMathlibExt.Complexity.NPComplete.MaximumCoverage.WellFormed, MetaMathlibExt.Complexity.NPComplete.MaximumCoverage.MaximumCoverageFeasible, MetaMathlibExt.Complexity.NPComplete.MaximumCoverage.maximumCoverageDec, MetaMathlibExt.Complexity.NPComplete.MaximumCoverage.maximumCoverage_npComplete
statement: formalized
---

# Maximum coverage

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/maximum-coverage/index.html).

## Maximum-coverage instances

A maximum-coverage instance is a tuple $(n, S, K, M)$ of a
natural number $n$ (the universe size), a list $S$ of lists of natural numbers (the subsets), a
natural number $K$ (the set budget) and a natural number $M$ (the coverage target).

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaximumCoverage.MaximumCoverageInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MaximumCoverageWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaximumCoverageWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/maximum-coverage/index.html#maximum-coverage-instance).

## Well-formed maximum-coverage instances

A maximum-coverage instance $(n, S, K, M)$ is
well formed when every subset in the list $S$ has no repeated elements and all of its elements
are less than $n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaximumCoverage.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/MaximumCoverageWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaximumCoverageWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/maximum-coverage/index.html#well-formed).

## Feasible maximum-coverage instances

A maximum-coverage instance $(n, S, K, M)$, with
universe size $n$, list of subsets $S$, set budget $K$ and coverage target $M$, is feasible when
there are a sublist $T$ of $S$ with at most $K$ entries and a list of at least $M$ pairwise
distinct natural numbers, each less than $n$ and each belonging to some subset in $T$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaximumCoverage.MaximumCoverageFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MaximumCoverageWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaximumCoverageWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/maximum-coverage/index.html#maximum-coverage-feasible).

## The MAXIMUM COVERAGE decision problem

MAXIMUM COVERAGE is the decision problem that
accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a
maximum-coverage instance $(n, S, K, M)$ that is well formed and feasible: every subset in the
list $S$ has no repeated elements and only elements less than $n$, and some sublist of $S$ with
at most $K$ entries covers at least $M$ distinct elements less than $n$. Bitstrings that do not
decode are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaximumCoverage.maximumCoverageDec`, a definition declared in [WantedExt/Complexity/NPComplete/MaximumCoverageWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaximumCoverageWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/maximum-coverage/index.html#maximum-coverage-dec).

## MAXIMUM COVERAGE is NP-complete

The MAXIMUM COVERAGE decision problem belongs to NP,
and every decision problem in NP reduces to it by a polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), SET COVER: maximum coverage with target `M = n` is exactly set cover (at most `K` sets covering all `n` elements).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MaximumCoverage.maximumCoverage_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MaximumCoverageWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaximumCoverageWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/maximum-coverage/index.html#maximum-coverage-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximum coverage](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/maximum-coverage/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/maximum-coverage)
