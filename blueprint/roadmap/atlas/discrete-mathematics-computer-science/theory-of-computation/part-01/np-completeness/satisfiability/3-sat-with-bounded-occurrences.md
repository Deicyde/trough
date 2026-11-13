---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.BoundedOccurrenceThreeSat.BoundedOccurrenceThreeSatInstance, MetaMathlibExt.Complexity.NPComplete.BoundedOccurrenceThreeSat.WellFormed, MetaMathlibExt.Complexity.NPComplete.BoundedOccurrenceThreeSat.BoundedOccurrenceThreeSatFeasible, MetaMathlibExt.Complexity.NPComplete.BoundedOccurrenceThreeSat.boundedOccurrenceThreeSatDec, MetaMathlibExt.Complexity.NPComplete.BoundedOccurrenceThreeSat.boundedOccurrenceThreeSat_npComplete
statement: formalized
---

# 3-SAT with bounded occurrences

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-sat-with-bounded-occurrences/index.html).

## Bounded-occurrence 3-SAT instances

A bounded-occurrence 3-SAT instance is a pair
$(n, \varphi)$ of a natural number $n$, the number of variables, and a CNF formula $\varphi$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.BoundedOccurrenceThreeSat.BoundedOccurrenceThreeSatInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/BoundedOccurrenceThreeSatWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/BoundedOccurrenceThreeSatWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-sat-with-bounded-occurrences/index.html#bounded-occurrence-three-sat-instance).

## Well-formed bounded-occurrence 3-SAT instances

A bounded-occurrence 3-SAT instance
$(n, \varphi)$ is well formed when every clause of $\varphi$ is a list of exactly three literals,
not necessarily distinct, every literal of $\varphi$ has a variable less than $n$, and for every
variable $v < n$ at most four of the literals in the clauses of $\varphi$, counted with
multiplicity and with either polarity, have variable $v$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.BoundedOccurrenceThreeSat.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/BoundedOccurrenceThreeSatWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/BoundedOccurrenceThreeSatWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-sat-with-bounded-occurrences/index.html#well-formed).

## Satisfiable bounded-occurrence 3-SAT instances

A bounded-occurrence 3-SAT instance
$(n, \varphi)$ is satisfiable when there is a list $(a_0, \dots, a_{n-1})$ of booleans such that
$\varphi$ is satisfied by the assignment sending each variable $x < n$ to $a_x$ and every
variable $x \ge n$ to false.

Formalized by `MetaMathlibExt.Complexity.NPComplete.BoundedOccurrenceThreeSat.BoundedOccurrenceThreeSatFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/BoundedOccurrenceThreeSatWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/BoundedOccurrenceThreeSatWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-sat-with-bounded-occurrences/index.html#bounded-occurrence-three-sat-feasible).

## 3-SAT with bounded occurrences as a decision problem

The decision problem 3-SAT WITH
BOUNDED OCCURRENCES accepts a bitstring $x$ exactly when $x$ decodes, under the canonical
bitstring encoding of bounded-occurrence 3-SAT instances, to an instance that is well formed and
satisfiable; it rejects every other bitstring, including every bitstring that does not decode.

Formalized by `MetaMathlibExt.Complexity.NPComplete.BoundedOccurrenceThreeSat.boundedOccurrenceThreeSatDec`, a definition declared in [WantedExt/Complexity/NPComplete/BoundedOccurrenceThreeSatWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/BoundedOccurrenceThreeSatWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-sat-with-bounded-occurrences/index.html#bounded-occurrence-three-sat-dec).

## 3-SAT WITH BOUNDED OCCURRENCES is NP-complete

The decision problem 3-SAT WITH BOUNDED
OCCURRENCES over bitstrings belongs to NP, and every decision problem in NP has a polynomial-time
many-one reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness* (1979), 3-SAT with bounded occurrences; C. A. Tovey, "A simplified NP-complete satisfiability problem" (1984).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.BoundedOccurrenceThreeSat.boundedOccurrenceThreeSat_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/BoundedOccurrenceThreeSatWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/BoundedOccurrenceThreeSatWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-sat-with-bounded-occurrences/index.html#bounded-occurrence-three-sat-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: 3-SAT with bounded occurrences](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-sat-with-bounded-occurrences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/satisfiability/3-sat-with-bounded-occurrences)
