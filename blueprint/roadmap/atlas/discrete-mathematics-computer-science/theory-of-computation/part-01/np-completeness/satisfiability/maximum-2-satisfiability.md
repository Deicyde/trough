---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MaxTwoSat.MaxTwoSatInstance, MetaMathlibExt.Complexity.NPComplete.MaxTwoSat.WellFormed, MetaMathlibExt.Complexity.NPComplete.MaxTwoSat.MaxTwoSatFeasible, MetaMathlibExt.Complexity.NPComplete.MaxTwoSat.maxTwoSatDec, MetaMathlibExt.Complexity.NPComplete.MaxTwoSat.maxTwoSat_npComplete
statement: formalized
---

# Maximum 2-satisfiability

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/maximum-2-satisfiability/index.html).

## MAX-2SAT instances

A MAX-2SAT instance is a triple $(n, \varphi, K)$ of a natural number
$n$ (the number of variables), a CNF formula $\varphi$ and a natural number $K$ (the bound). The
type does not restrict clause lengths; that clauses have at most two literals is part of
well-formedness.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxTwoSat.MaxTwoSatInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MaxTwoSatWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaxTwoSatWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/maximum-2-satisfiability/index.html#max-two-sat-instance).

## Well-formed MAX-2SAT instances

A MAX-2SAT instance $(n, \varphi, K)$ is well formed when
every clause of $\varphi$ has at most two literals and every literal $(x, b)$ in it has variable
index $x < n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxTwoSat.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/MaxTwoSatWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaxTwoSatWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/maximum-2-satisfiability/index.html#well-formed).

## Feasible MAX-2SAT instances

A MAX-2SAT instance $(n, \varphi, K)$ is feasible when there
are truth values $a_0, \dots, a_{n-1}$ such that at least $K$ of the clauses in the list $\varphi$,
counted with multiplicity, are satisfied by the assignment $v$ with $v(x) = a_x$ for $x < n$ and
$v(x) = \mathrm{false}$ for $x \ge n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxTwoSat.MaxTwoSatFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MaxTwoSatWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaxTwoSatWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/maximum-2-satisfiability/index.html#max-two-sat-feasible).

## MAXIMUM 2-SATISFIABILITY as a decision problem

The decision problem MAXIMUM
2-SATISFIABILITY accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring
encoding of MAX-2SAT instances, to an instance $(n, \varphi, K)$ that is well formed (every clause
of $\varphi$ has at most two literals, and every literal has variable index less than $n$) and
feasible (some assignment of truth values to the $n$ variables satisfies at least $K$ of the
clauses of $\varphi$, counted with multiplicity). Bitstrings that do not decode, and bitstrings
that decode to instances that are not well formed, are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxTwoSat.maxTwoSatDec`, a definition declared in [WantedExt/Complexity/NPComplete/MaxTwoSatWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaxTwoSatWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/maximum-2-satisfiability/index.html#max-two-sat-dec).

## MAXIMUM 2-SATISFIABILITY is NP-complete

The decision problem MAXIMUM 2-SATISFIABILITY
over bitstrings lies in NP, and every decision problem in NP has a polynomial-time many-one
reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness* (1979), MAXIMUM 2-SATISFIABILITY.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MaxTwoSat.maxTwoSat_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MaxTwoSatWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaxTwoSatWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/maximum-2-satisfiability/index.html#max-two-sat-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximum 2-satisfiability](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/maximum-2-satisfiability/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/satisfiability/maximum-2-satisfiability)
