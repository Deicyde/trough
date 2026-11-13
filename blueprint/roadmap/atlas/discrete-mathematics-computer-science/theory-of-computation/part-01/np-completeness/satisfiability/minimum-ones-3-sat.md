---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MinOnesThreeSat.MinOnesThreeSatInstance, MetaMathlibExt.Complexity.NPComplete.MinOnesThreeSat.WellFormed, MetaMathlibExt.Complexity.NPComplete.MinOnesThreeSat.MinOnesThreeSatFeasible, MetaMathlibExt.Complexity.NPComplete.MinOnesThreeSat.minOnesThreeSatDec, MetaMathlibExt.Complexity.NPComplete.MinOnesThreeSat.minOnesThreeSat_npComplete
statement: formalized
---

# Minimum-ones 3-SAT

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/minimum-ones-3-sat/index.html).

## MINIMUM ONES 3-SAT instances

An instance of MINIMUM ONES 3-SAT is a triple
$(n, \varphi, K)$ of a natural number $n$ (the number of variables), a CNF formula $\varphi$ and a
natural number $K$ (the bound). No condition is placed on $\varphi$ here; clauses of exactly three
literals are required separately, by well-formedness.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinOnesThreeSat.MinOnesThreeSatInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MinOnesThreeSatWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinOnesThreeSatWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/minimum-ones-3-sat/index.html#min-ones-three-sat-instance).

## Well-formed MINIMUM ONES 3-SAT instances

A triple $(n, \varphi, K)$ of a natural number
$n$, a CNF formula $\varphi$ and a natural number $K$ is well formed when every clause of $\varphi$
is a list of exactly three literals and every literal of every clause has variable index less
than $n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinOnesThreeSat.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/MinOnesThreeSatWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinOnesThreeSatWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/minimum-ones-3-sat/index.html#well-formed).

## Feasible MINIMUM ONES 3-SAT instances

A triple $(n, \varphi, K)$ of a natural number $n$,
a CNF formula $\varphi$ and a natural number $K$ is feasible when there is an assignment of truth
values to the variables $0, \dots, n-1$ that, with every variable $x \ge n$ set to false,
satisfies $\varphi$ and sets at most $K$ of the variables $0, \dots, n-1$ to true.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinOnesThreeSat.MinOnesThreeSatFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MinOnesThreeSatWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinOnesThreeSatWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/minimum-ones-3-sat/index.html#min-ones-three-sat-feasible).

## The MINIMUM ONES 3-SAT decision problem

MINIMUM ONES 3-SAT is the decision problem that
accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a
triple $(n, \varphi, K)$ of a natural number $n$, a CNF formula $\varphi$ and a natural number $K$
such that every clause of $\varphi$ is a list of exactly three literals whose variables are all
less than $n$, and some assignment of truth values to the variables $0, \dots, n-1$ satisfies
$\varphi$ and sets at most $K$ of them to true. Every other bitstring is rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinOnesThreeSat.minOnesThreeSatDec`, a definition declared in [WantedExt/Complexity/NPComplete/MinOnesThreeSatWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinOnesThreeSatWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/minimum-ones-3-sat/index.html#min-ones-three-sat-dec).

## MINIMUM ONES 3-SAT is NP-complete

Let MINIMUM ONES 3-SAT be the decision problem that
accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a
triple $(n, \varphi, K)$ of a natural number $n$, a CNF formula $\varphi$ and a natural number $K$
such that every clause of $\varphi$ is a list of exactly three literals whose variables are all
less than $n$, and some assignment of truth values to the variables $0, \dots, n-1$ satisfies
$\varphi$ and sets at most $K$ of them to true. Then MINIMUM ONES 3-SAT belongs to NP, and every
decision problem $L$ in NP reduces to it by a polynomial-time many-one reduction: there is a
polynomial-time computable map $f$ on bitstrings such that, for every bitstring $x$, $L$ accepts
$x$ exactly when MINIMUM ONES 3-SAT accepts $f(x)$.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness* (1979), MINIMUM ONES 3-SAT.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MinOnesThreeSat.minOnesThreeSat_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MinOnesThreeSatWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinOnesThreeSatWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/minimum-ones-3-sat/index.html#min-ones-three-sat-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Minimum-ones 3-SAT](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/minimum-ones-3-sat/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/satisfiability/minimum-ones-3-sat)
