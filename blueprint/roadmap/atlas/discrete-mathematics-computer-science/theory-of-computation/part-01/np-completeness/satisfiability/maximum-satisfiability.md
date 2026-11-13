---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MaxSat.MaxSatInstance, MetaMathlibExt.Complexity.NPComplete.MaxSat.WellFormed, MetaMathlibExt.Complexity.NPComplete.MaxSat.MaxSatFeasible, MetaMathlibExt.Complexity.NPComplete.MaxSat.maxSatDec, MetaMathlibExt.Complexity.NPComplete.MaxSat.maxSat_npComplete
statement: formalized
---

# Maximum satisfiability

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/maximum-satisfiability/index.html).

## MAX-SAT instances

A MAX-SAT instance is a triple $(n, \varphi, K)$ of a natural number $n$
(the number of variables), a CNF formula $\varphi$ and a natural number $K$ (the bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxSat.MaxSatInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MaxSatWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaxSatWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/maximum-satisfiability/index.html#max-sat-instance).

## Well-formed MAX-SAT instances

A MAX-SAT instance $(n, \varphi, K)$ is well formed when
every literal $(x, b)$ in every clause of $\varphi$ has variable index $x < n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxSat.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/MaxSatWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaxSatWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/maximum-satisfiability/index.html#well-formed).

## Feasible MAX-SAT instances

A MAX-SAT instance $(n, \varphi, K)$ is feasible when there
are truth values $a_0, \dots, a_{n-1}$ such that at least $K$ of the clauses in the list $\varphi$,
counted with multiplicity, are satisfied by the assignment $v$ with $v(x) = a_x$ for $x < n$ and
$v(x) = \mathrm{false}$ for $x \ge n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxSat.MaxSatFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MaxSatWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaxSatWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/maximum-satisfiability/index.html#max-sat-feasible).

## MAXIMUM SATISFIABILITY as a decision problem

The decision problem MAXIMUM SATISFIABILITY
accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding of
MAX-SAT instances, to an instance $(n, \varphi, K)$ that is well formed (every literal of
$\varphi$ has variable index less than $n$) and feasible (some assignment of truth values to the
$n$ variables satisfies at least $K$ of the clauses of $\varphi$, counted with multiplicity).
Bitstrings that do not decode, and bitstrings that decode to instances that are not well formed,
are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxSat.maxSatDec`, a definition declared in [WantedExt/Complexity/NPComplete/MaxSatWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaxSatWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/maximum-satisfiability/index.html#max-sat-dec).

## MAXIMUM SATISFIABILITY is NP-complete

The decision problem MAXIMUM SATISFIABILITY over
bitstrings lies in NP, and every decision problem in NP has a polynomial-time many-one
reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness* (1979), MAXIMUM SATISFIABILITY.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MaxSat.maxSat_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MaxSatWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaxSatWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/maximum-satisfiability/index.html#max-sat-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximum satisfiability](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/maximum-satisfiability/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/satisfiability/maximum-satisfiability)
