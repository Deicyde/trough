---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.GeneralizedAssignment.GeneralizedAssignmentInstance, MetaMathlibExt.Complexity.NPComplete.GeneralizedAssignment.WellFormed, MetaMathlibExt.Complexity.NPComplete.GeneralizedAssignment.GeneralizedAssignmentFeasible, MetaMathlibExt.Complexity.NPComplete.GeneralizedAssignment.generalizedAssignmentDec, MetaMathlibExt.Complexity.NPComplete.GeneralizedAssignment.generalizedAssignment_npComplete
statement: formalized
---

# Generalized assignment problem

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/generalized-assignment-problem/index.html).

## Generalized-assignment instances

A generalized-assignment instance is a tuple
$(R, C, c, K)$ where $R$ and $C$ are finite lists of finite lists of natural numbers, read as
matrices indexed by job and machine ($R_{j,i}$ is the resource job $j$ consumes on machine $i$
and $C_{j,i}$ is the cost of assigning job $j$ to machine $i$), $c$ is a finite list of natural
numbers (the machine capacities $c_i$), and $K$ is a natural number (the cost bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.GeneralizedAssignment.GeneralizedAssignmentInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/GeneralizedAssignmentWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/GeneralizedAssignmentWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/generalized-assignment-problem/index.html#generalized-assignment-instance).

## Well-formed generalized-assignment instances

A generalized-assignment instance
$(R, C, c, K)$ is well formed when $R$ and $C$ have the same number of rows and every row of $R$
and every row of $C$ has as many entries as $c$ (one per machine).

Formalized by `MetaMathlibExt.Complexity.NPComplete.GeneralizedAssignment.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/GeneralizedAssignmentWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/GeneralizedAssignmentWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/generalized-assignment-problem/index.html#well-formed).

## Feasible generalized assignments

Let $(R, C, c, K)$ be a generalized-assignment instance,
let $n$ be the number of rows of $R$ (the jobs) and $m$ the length of $c$ (the machines), and
read entries missing from $R$ or $C$ as $0$. The instance is feasible when there are machines
$a_1, \dots, a_n \in \{1, \dots, m\}$ such that for every machine $i$ the sum of $R_{j,i}$
over the jobs $j$ with $a_j = i$ is at most $c_i$, and $\sum_{j=1}^{n} C_{j,a_j} \le K$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.GeneralizedAssignment.GeneralizedAssignmentFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/GeneralizedAssignmentWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/GeneralizedAssignmentWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/generalized-assignment-problem/index.html#generalized-assignment-feasible).

## The generalized assignment decision problem

The decision problem GENERALIZED
ASSIGNMENT accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring
encoding of generalized-assignment instances, to an instance that is well formed and feasible.
Bitstrings that do not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.GeneralizedAssignment.generalizedAssignmentDec`, a definition declared in [WantedExt/Complexity/NPComplete/GeneralizedAssignmentWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/GeneralizedAssignmentWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/generalized-assignment-problem/index.html#generalized-assignment-dec).

## GENERALIZED ASSIGNMENT is NP-complete

The generalized assignment decision problem
belongs to NP, and every decision problem in NP reduces to it by a polynomial-time many-one
reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), GENERALIZED ASSIGNMENT PROBLEM.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.GeneralizedAssignment.generalizedAssignment_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/GeneralizedAssignmentWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/GeneralizedAssignmentWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/generalized-assignment-problem/index.html#generalized-assignment-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized assignment problem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/generalized-assignment-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/generalized-assignment-problem)
