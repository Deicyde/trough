---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MinTwoSat.MinTwoSatInstance, MetaMathlibExt.Complexity.NPComplete.MinTwoSat.WellFormed, MetaMathlibExt.Complexity.NPComplete.MinTwoSat.MinTwoSatFeasible, MetaMathlibExt.Complexity.NPComplete.MinTwoSat.minTwoSatDec, MetaMathlibExt.Complexity.NPComplete.MinTwoSat.minTwoSat_npComplete
statement: formalized
---

# Minimum 2-satisfiability

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/minimum-2-satisfiability/index.html).

## MINIMUM 2-SATISFIABILITY instances

An instance of MINIMUM 2-SATISFIABILITY is a triple
$(n, \varphi, K)$ of a natural number $n$ (the number of variables), a CNF formula $\varphi$ and a
natural number $K$ (the bound). No condition is placed on $\varphi$ here; clauses of at most two
literals are required separately, by well-formedness.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinTwoSat.MinTwoSatInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MinTwoSatWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinTwoSatWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/minimum-2-satisfiability/index.html#min-two-sat-instance).

## Well-formed MINIMUM 2-SATISFIABILITY instances

A triple $(n, \varphi, K)$ of a natural
number $n$, a CNF formula $\varphi$ and a natural number $K$ is well formed when every clause of
$\varphi$ has at most two literals and every literal of every clause has variable index less than
$n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinTwoSat.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/MinTwoSatWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinTwoSatWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/minimum-2-satisfiability/index.html#well-formed).

## Feasible MINIMUM 2-SATISFIABILITY instances

A triple $(n, \varphi, K)$ of a natural number
$n$, a CNF formula $\varphi$ with clauses $C_0, \dots, C_{m-1}$ and a natural number $K$ is
feasible when there is an assignment of truth values to the variables $0, \dots, n-1$ that, with
every variable $x \ge n$ set to false, satisfies $C_j$ for at most $K$ indices $j < m$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinTwoSat.MinTwoSatFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MinTwoSatWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinTwoSatWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/minimum-2-satisfiability/index.html#min-two-sat-feasible).

## The MINIMUM 2-SATISFIABILITY decision problem

MINIMUM 2-SATISFIABILITY is the decision
problem that accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring
encoding, to a triple $(n, \varphi, K)$ of a natural number $n$, a CNF formula $\varphi$ with
clauses $C_0, \dots, C_{m-1}$ and a natural number $K$ such that every clause has at most two
literals, all with variables less than $n$, and some assignment of truth values to the variables
$0, \dots, n-1$ satisfies $C_j$ for at most $K$ indices $j < m$. Every other bitstring is
rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinTwoSat.minTwoSatDec`, a definition declared in [WantedExt/Complexity/NPComplete/MinTwoSatWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinTwoSatWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/minimum-2-satisfiability/index.html#min-two-sat-dec).

## MINIMUM 2-SATISFIABILITY is NP-complete

Let MINIMUM 2-SATISFIABILITY be the decision
problem that accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring
encoding, to a triple $(n, \varphi, K)$ of a natural number $n$, a CNF formula $\varphi$ with
clauses $C_0, \dots, C_{m-1}$ and a natural number $K$ such that every clause has at most two
literals, all with variables less than $n$, and some assignment of truth values to the variables
$0, \dots, n-1$ satisfies $C_j$ for at most $K$ indices $j < m$. Then MINIMUM 2-SATISFIABILITY
belongs to NP, and every decision problem $L$ in NP reduces to it by a polynomial-time many-one
reduction: there is a polynomial-time computable map $f$ on bitstrings such that, for every
bitstring $x$, $L$ accepts $x$ exactly when MINIMUM 2-SATISFIABILITY accepts $f(x)$.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness* (1979), MINIMUM 2-SATISFIABILITY; R. Kohli, R. Krishnamurti, and P. Mirchandani, "The minimum satisfiability problem" (1994).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MinTwoSat.minTwoSat_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MinTwoSatWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinTwoSatWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/minimum-2-satisfiability/index.html#min-two-sat-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Minimum 2-satisfiability](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/minimum-2-satisfiability/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/satisfiability/minimum-2-satisfiability)
