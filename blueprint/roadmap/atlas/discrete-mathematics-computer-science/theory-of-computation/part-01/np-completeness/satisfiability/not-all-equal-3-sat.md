---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.NaeThreeSat.NaeThreeSatInstance, MetaMathlibExt.Complexity.NPComplete.NaeThreeSat.WellFormed, MetaMathlibExt.Complexity.NPComplete.NaeThreeSat.NaeThreeSatFeasible, MetaMathlibExt.Complexity.NPComplete.NaeThreeSat.naeThreeSatDec, MetaMathlibExt.Complexity.NPComplete.NaeThreeSat.naeThreeSat_npComplete
statement: formalized
---

# Not-all-equal 3-SAT

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/not-all-equal-3-sat/index.html).

## NOT-ALL-EQUAL 3-SAT instances

A NOT-ALL-EQUAL 3-SAT instance is a pair $(n, \varphi)$ of
a natural number $n$, the number of variables, and a CNF formula $\varphi$. The formula is not
required to have three literals per clause; that is part of well-formedness.

Formalized by `MetaMathlibExt.Complexity.NPComplete.NaeThreeSat.NaeThreeSatInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/NaeThreeSatWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/NaeThreeSatWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/not-all-equal-3-sat/index.html#nae-three-sat-instance).

## Well-formed NOT-ALL-EQUAL 3-SAT instances

A NOT-ALL-EQUAL 3-SAT instance $(n, \varphi)$
is well-formed when every clause of $\varphi$ is a list of exactly three literals, repetitions
allowed, and every literal $(x, b)$ in it has variable index $x < n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.NaeThreeSat.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/NaeThreeSatWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/NaeThreeSatWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/not-all-equal-3-sat/index.html#well-formed).

## Not-all-equal satisfiability of an instance

A NOT-ALL-EQUAL 3-SAT instance
$(n, \varphi)$, with $n \in \mathbb{N}$ and $\varphi$ a CNF formula, is not-all-equal satisfiable
when there are truth values $a_0, \dots, a_{n-1}$ such that, for the assignment $v$ with
$v(x) = a_x$ for $x < n$ and $v(x) = \mathrm{false}$ for $x \ge n$, every clause of $\varphi$
contains a literal satisfied by $v$ and a literal not satisfied by $v$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.NaeThreeSat.NaeThreeSatFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/NaeThreeSatWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/NaeThreeSatWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/not-all-equal-3-sat/index.html#nae-three-sat-feasible).

## NOT-ALL-EQUAL 3-SAT as a decision problem

The decision problem NOT-ALL-EQUAL 3-SAT
accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a
NOT-ALL-EQUAL 3-SAT instance $(n, \varphi)$ that is well-formed and not-all-equal satisfiable.
Every bitstring that decodes to no instance is rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.NaeThreeSat.naeThreeSatDec`, a definition declared in [WantedExt/Complexity/NPComplete/NaeThreeSatWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/NaeThreeSatWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/not-all-equal-3-sat/index.html#nae-three-sat-dec).

## NOT-ALL-EQUAL 3-SAT is NP-complete

The decision problem NOT-ALL-EQUAL 3-SAT over
bitstrings belongs to NP, and every decision problem in NP has a polynomial-time many-one
reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness* (1979), NOT-ALL-EQUAL 3-SAT; T. J. Schaefer, "The complexity of satisfiability problems" (1978).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.NaeThreeSat.naeThreeSat_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/NaeThreeSatWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/NaeThreeSatWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/not-all-equal-3-sat/index.html#nae-three-sat-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Not-all-equal 3-SAT](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/not-all-equal-3-sat/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/satisfiability/not-all-equal-3-sat)
