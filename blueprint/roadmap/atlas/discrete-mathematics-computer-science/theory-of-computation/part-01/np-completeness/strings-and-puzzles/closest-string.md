---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.ClosestString.ClosestStringInstance, MetaMathlibExt.Complexity.NPComplete.ClosestString.WellFormed, MetaMathlibExt.Complexity.NPComplete.ClosestString.ClosestStringFeasible, MetaMathlibExt.Complexity.NPComplete.ClosestString.closestStringDec, MetaMathlibExt.Complexity.NPComplete.ClosestString.closestString_npComplete
statement: formalized
---

# Closest string

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/closest-string/index.html).

## Closest-string instances

A closest-string instance is a pair $(S, d)$ of a finite list
$S$ of bitstrings (finite lists of booleans) and a natural number $d$, the distance bound.

The bitstrings are not required to have equal length; that is the well-formedness condition.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ClosestString.ClosestStringInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/ClosestStringWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ClosestStringWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/closest-string/index.html#closest-string-instance).

## Well-formed closest-string instances

A closest-string instance $(S, d)$ is well formed
when all bitstrings in the list $S$ have the same length.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ClosestString.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/ClosestStringWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ClosestStringWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/closest-string/index.html#well-formed).

## Feasible closest-string instances

Write $\ell(x)$ for the length of a bitstring $x$.
A closest-string instance $(S, d)$ is feasible when there is a bitstring $c$ with
$\ell(c) = \ell(s_1)$, where $s_1$ is the first bitstring of $S$ (and $\ell(c) = 0$ if $S$ is
empty), such that for every $s$ in $S$ the number of positions $j < \min(\ell(c), \ell(s))$ at
which $c$ and $s$ differ is at most $d$.

If all bitstrings of $S$ have length $\ell(c)$, this number is the Hamming distance between $c$
and $s$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ClosestString.ClosestStringFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/ClosestStringWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ClosestStringWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/closest-string/index.html#closest-string-feasible).

## The CLOSEST STRING decision problem

The decision problem CLOSEST STRING accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding of
closest-string instances, to an instance that is well formed and feasible. Bitstrings that do
not decode to a closest-string instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ClosestString.closestStringDec`, a definition declared in [WantedExt/Complexity/NPComplete/ClosestStringWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ClosestStringWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/closest-string/index.html#closest-string-dec).

## CLOSEST STRING is NP-complete

The CLOSEST STRING decision problem belongs to NP, and
every decision problem in NP has a polynomial-time many-one reduction to it.

## Sources

- J. K. Lanctot et al., "Distinguishing string selection problems" (2003); M. Frances and A. Litman, "On covering problems of codes" (1997).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.ClosestString.closestString_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/ClosestStringWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ClosestStringWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/closest-string/index.html#closest-string-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Closest string](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/closest-string/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/closest-string)
