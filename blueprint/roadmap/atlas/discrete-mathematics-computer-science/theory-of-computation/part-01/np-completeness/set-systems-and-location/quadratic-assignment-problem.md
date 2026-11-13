---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.QuadraticAssignment.QuadraticAssignmentInstance, MetaMathlibExt.Complexity.NPComplete.QuadraticAssignment.WellFormed, MetaMathlibExt.Complexity.NPComplete.QuadraticAssignment.QuadraticAssignmentFeasible, MetaMathlibExt.Complexity.NPComplete.QuadraticAssignment.quadraticAssignmentDec, MetaMathlibExt.Complexity.NPComplete.QuadraticAssignment.quadraticAssignment_npComplete
statement: formalized
---

# Quadratic assignment problem

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/quadratic-assignment-problem/index.html).

## Instances of QUADRATIC ASSIGNMENT

An instance of quadratic assignment is a tuple
$(n, F, D, K)$ consisting of a natural number $n$ (the size), a flow matrix $F$ and a distance
matrix $D$, each given as a list of rows that are lists of natural numbers, and a natural
number $K$ (the cost bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.QuadraticAssignment.QuadraticAssignmentInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/QuadraticAssignmentWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/QuadraticAssignmentWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/quadratic-assignment-problem/index.html#quadratic-assignment-instance).

## Well-formed quadratic assignment instances

An instance $(n, F, D, K)$ of quadratic
assignment is well formed when the flow matrix $F$ and the distance matrix $D$ each have
exactly $n$ rows and every row of each has length $n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.QuadraticAssignment.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/QuadraticAssignmentWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/QuadraticAssignmentWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/quadratic-assignment-problem/index.html#well-formed).

## Feasible quadratic assignment instances

An instance $(n, F, D, K)$ of quadratic
assignment is feasible when there is a permutation $\pi$ of the numbers $0, \dots, n - 1$ such
that

$$
\sum_{a < n} \sum_{b < n} F_{a b} \, D_{\pi(a) \pi(b)} \le K.
$$

Here $F_{a b}$ is entry $b$ of row $a$ of $F$, and likewise for $D$; an entry that is missing,
because the matrix has too few rows or the row is too short, is read as $0$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.QuadraticAssignment.QuadraticAssignmentFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/QuadraticAssignmentWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/QuadraticAssignmentWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/quadratic-assignment-problem/index.html#quadratic-assignment-feasible).

## QUADRATIC ASSIGNMENT as a decision problem

The decision problem QUADRATIC ASSIGNMENT
accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a
quadratic assignment instance that is well formed and feasible; bitstrings that do not decode
are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.QuadraticAssignment.quadraticAssignmentDec`, a definition declared in [WantedExt/Complexity/NPComplete/QuadraticAssignmentWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/QuadraticAssignmentWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/quadratic-assignment-problem/index.html#quadratic-assignment-dec).

## QUADRATIC ASSIGNMENT is NP-complete

The decision problem QUADRATIC ASSIGNMENT lies in NP,
and every decision problem in NP reduces to it by a polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), QUADRATIC ASSIGNMENT PROBLEM; S. Sahni and T. Gonzalez, "P-complete approximation problems" (1976).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.QuadraticAssignment.quadraticAssignment_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/QuadraticAssignmentWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/QuadraticAssignmentWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/quadratic-assignment-problem/index.html#quadratic-assignment-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Quadratic assignment problem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/quadratic-assignment-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/quadratic-assignment-problem)
