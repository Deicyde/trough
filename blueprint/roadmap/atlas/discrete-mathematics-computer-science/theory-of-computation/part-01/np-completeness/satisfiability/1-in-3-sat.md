---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.OneInThreeSat.OneInThreeSatInstance, MetaMathlibExt.Complexity.NPComplete.OneInThreeSat.WellFormed, MetaMathlibExt.Complexity.NPComplete.OneInThreeSat.OneInThreeSatFeasible, MetaMathlibExt.Complexity.NPComplete.OneInThreeSat.oneInThreeSatDec, MetaMathlibExt.Complexity.NPComplete.OneInThreeSat.oneInThreeSat_npComplete
statement: formalized
---

# 1-in-3 SAT

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/1-in-3-sat/index.html).

## 1-in-3-SAT instances

A 1-in-3-SAT instance is a pair $(n, \varphi)$ of a natural number
$n$, the number of variables, and a CNF formula $\varphi$.

Any CNF formula is allowed here; that $\varphi$ has three literals per clause, all over the
variables below $n$, is required separately by well-formedness.

Formalized by `MetaMathlibExt.Complexity.NPComplete.OneInThreeSat.OneInThreeSatInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/OneInThreeSatWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/OneInThreeSatWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/1-in-3-sat/index.html#one-in-three-sat-instance).

## Well-formed 1-in-3-SAT instances

A 1-in-3-SAT instance $(n, \varphi)$ is well formed
when every clause of $\varphi$ has exactly three literals and every literal $(x, b)$ in it has
variable index $x < n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.OneInThreeSat.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/OneInThreeSatWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/OneInThreeSatWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/1-in-3-sat/index.html#well-formed).

## Feasible 1-in-3-SAT instances

A 1-in-3-SAT instance $(n, \varphi)$ is feasible when
there is an assignment $v$ of truth values to the variables $0, \dots, n - 1$, with variables
$y \ge n$ read as false, such that every clause of $\varphi$ has exactly one position holding a
literal $(y, b)$ with $v(y) = b$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.OneInThreeSat.OneInThreeSatFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/OneInThreeSatWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/OneInThreeSatWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/1-in-3-sat/index.html#one-in-three-sat-feasible).

## The 1-in-3-SAT decision problem

The 1-in-3-SAT decision problem accepts a bitstring $x$
exactly when $x$ decodes, under the canonical bitstring encoding, to a pair $(n, \varphi)$ of a
natural number $n$ and a CNF formula $\varphi$ such that every clause of $\varphi$ has exactly
three literals, every literal $(y, b)$ of $\varphi$ has variable index $y < n$, and some
assignment $v$ of truth values to the variables $0, \dots, n - 1$ makes exactly one position
of every clause hold a literal $(y, b)$ with $v(y) = b$. It rejects every bitstring that does
not decode.

Formalized by `MetaMathlibExt.Complexity.NPComplete.OneInThreeSat.oneInThreeSatDec`, a definition declared in [WantedExt/Complexity/NPComplete/OneInThreeSatWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/OneInThreeSatWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/1-in-3-sat/index.html#one-in-three-sat-dec).

## 1-IN-3-SAT is NP-complete

The 1-in-3-SAT decision problem belongs to NP, and every
decision problem in NP reduces to it by a polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness* (1979), ONE-IN-THREE 3-SAT; T. J. Schaefer, "The complexity of satisfiability problems" (1978).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.OneInThreeSat.oneInThreeSat_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/OneInThreeSatWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/OneInThreeSatWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/1-in-3-sat/index.html#one-in-three-sat-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: 1-in-3 SAT](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/1-in-3-sat/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/satisfiability/1-in-3-sat)
