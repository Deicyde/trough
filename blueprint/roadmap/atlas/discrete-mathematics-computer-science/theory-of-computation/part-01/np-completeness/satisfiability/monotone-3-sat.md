---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MonotoneThreeSat.MonotoneThreeSatInstance, MetaMathlibExt.Complexity.NPComplete.MonotoneThreeSat.WellFormed, MetaMathlibExt.Complexity.NPComplete.MonotoneThreeSat.MonotoneThreeSatFeasible, MetaMathlibExt.Complexity.NPComplete.MonotoneThreeSat.monotoneThreeSatDec, MetaMathlibExt.Complexity.NPComplete.MonotoneThreeSat.monotoneThreeSat_npComplete
statement: formalized
---

# Monotone 3-SAT

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/monotone-3-sat/index.html).

## Monotone 3-SAT instances

A monotone 3-SAT instance is a pair $(n, \varphi)$ of a
natural number $n$, the number of variables, and a CNF formula $\varphi$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MonotoneThreeSat.MonotoneThreeSatInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MonotoneThreeSatWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MonotoneThreeSatWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/monotone-3-sat/index.html#monotone-three-sat-instance).

## Well-formed monotone 3-SAT instances

A monotone 3-SAT instance $(n, \varphi)$ is well
formed when every clause of the CNF formula $\varphi$ is a list of exactly three literals
(repetitions allowed), each with a variable below $n$, and the literals of each clause are all
positive or all negative.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MonotoneThreeSat.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/MonotoneThreeSatWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MonotoneThreeSatWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/monotone-3-sat/index.html#well-formed).

## Satisfiable monotone 3-SAT instances

A monotone 3-SAT instance $(n, \varphi)$ is
feasible when there is a list of $n$ truth values $a_0, \dots, a_{n-1}$ such that the assignment
sending each variable $x < n$ to $a_x$ and every variable $x \ge n$ to false satisfies the CNF
formula $\varphi$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MonotoneThreeSat.MonotoneThreeSatFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MonotoneThreeSatWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MonotoneThreeSatWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/monotone-3-sat/index.html#monotone-three-sat-feasible).

## MONOTONE 3-SAT as a decision problem

The decision problem MONOTONE 3-SAT accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a pair
$(n, \varphi)$ of a natural number $n$ and a CNF formula $\varphi$ such that every clause of
$\varphi$ is a list of exactly three literals (repetitions allowed), every literal of $\varphi$
has a variable below $n$, the literals of each clause are all positive or all negative, and
some assignment of truth values to the variables $0, \dots, n-1$, with every other variable
false, satisfies $\varphi$. Bitstrings that do not decode are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MonotoneThreeSat.monotoneThreeSatDec`, a definition declared in [WantedExt/Complexity/NPComplete/MonotoneThreeSatWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MonotoneThreeSatWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/monotone-3-sat/index.html#monotone-three-sat-dec).

## MONOTONE 3-SAT is NP-complete

The decision problem MONOTONE 3-SAT belongs to NP, and
every decision problem in NP has a polynomial-time many-one reduction to MONOTONE 3-SAT.

## Sources

- T. J. Schaefer, "The complexity of satisfiability problems", Proceedings of the Tenth Annual ACM Symposium on Theory of Computing (STOC 1978), ACM, 1978, 216-226 (dichotomy theorem).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MonotoneThreeSat.monotoneThreeSat_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MonotoneThreeSatWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MonotoneThreeSatWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/monotone-3-sat/index.html#monotone-three-sat-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monotone 3-SAT](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/monotone-3-sat/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/satisfiability/monotone-3-sat)
