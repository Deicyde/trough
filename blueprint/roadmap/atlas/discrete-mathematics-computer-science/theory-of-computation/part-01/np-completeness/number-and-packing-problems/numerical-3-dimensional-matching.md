---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.Numerical3DM.Numerical3DMInstance, MetaMathlibExt.Complexity.NPComplete.Numerical3DM.WellFormed, MetaMathlibExt.Complexity.NPComplete.Numerical3DM.Numerical3DMFeasible, MetaMathlibExt.Complexity.NPComplete.Numerical3DM.numerical3DMDec, MetaMathlibExt.Complexity.NPComplete.Numerical3DM.numerical3DM_npComplete
statement: formalized
---

# Numerical 3-dimensional matching

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/numerical-3-dimensional-matching/index.html).

## Numerical 3-dimensional matching instances

An instance of NUMERICAL 3-DIMENSIONAL
MATCHING is a quadruple $(A, B, C, t)$ of three finite lists $A$, $B$, $C$ of natural numbers
and a natural number $t$, the target.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Numerical3DM.Numerical3DMInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/Numerical3DMWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/Numerical3DMWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/numerical-3-dimensional-matching/index.html#numerical3-dminstance).

## Well-formed numerical 3-dimensional matching instances

An instance $(A, B, C, t)$ of
NUMERICAL 3-DIMENSIONAL MATCHING is well formed when the lists $B$ and $C$ have the same length
as the list $A$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Numerical3DM.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/Numerical3DMWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/Numerical3DMWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/numerical-3-dimensional-matching/index.html#well-formed).

## Feasible numerical 3-dimensional matching instances

Let $(A, B, C, t)$ be an instance
and let $n$ be the length of $A$, with lists indexed from $0$. The instance is feasible when
there are permutations $p$ and $q$ of the numbers $0$ through $n-1$ such that
$A_j + B_{p(j)} + C_{q(j)} = t$ for every $j < n$, where an entry of $B$ or $C$ at an index past
the end of its list counts as $0$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Numerical3DM.Numerical3DMFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/Numerical3DMWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/Numerical3DMWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/numerical-3-dimensional-matching/index.html#numerical3-dmfeasible).

## NUMERICAL 3-DIMENSIONAL MATCHING as a decision problem

The decision problem NUMERICAL
3-DIMENSIONAL MATCHING accepts a bitstring $x$ exactly when $x$ decodes, under the canonical
bitstring encoding (natural numbers in binary), to an instance $(A, B, C, t)$ that is well
formed and feasible: the lists $B$ and $C$ have the same length $n$ as the list $A$, and there
are permutations $p$ and $q$ of the numbers $0$ through $n-1$ such that
$A_j + B_{p(j)} + C_{q(j)} = t$ for every $j < n$, with lists indexed from $0$. Every other
bitstring is rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.Numerical3DM.numerical3DMDec`, a definition declared in [WantedExt/Complexity/NPComplete/Numerical3DMWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/Numerical3DMWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/numerical-3-dimensional-matching/index.html#numerical3-dmdec).

## NUMERICAL 3-DIMENSIONAL MATCHING is NP-complete

The decision problem NUMERICAL
3-DIMENSIONAL MATCHING belongs to NP, and every decision problem in NP reduces to it by a
polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), NUMERICAL 3-DIMENSIONAL MATCHING (strongly NP-complete).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.Numerical3DM.numerical3DM_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/Numerical3DMWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/Numerical3DMWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/numerical-3-dimensional-matching/index.html#numerical3-dm-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Numerical 3-dimensional matching](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/numerical-3-dimensional-matching/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/numerical-3-dimensional-matching)
