---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.ZeroOneILP.ZeroOneILPInstance, MetaMathlibExt.Complexity.NPComplete.ZeroOneILP.WellFormed, MetaMathlibExt.Complexity.NPComplete.ZeroOneILP.ZeroOneILPFeasible, MetaMathlibExt.Complexity.NPComplete.ZeroOneILP.zeroOneILPDec, MetaMathlibExt.Complexity.NPComplete.ZeroOneILP.zeroOneILP_npComplete
statement: formalized
---

# 0-1 integer programming

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/0-1-integer-programming/index.html).

## 0-1 integer programming instances

A 0-1 integer programming instance is a triple
$(n, A, b)$ consisting of a natural number $n$ (the number of variables), a coefficient matrix
$A$ given as a list of rows, each row a list of pairs of natural numbers, and a right-hand side
$b$ given as a list of pairs of natural numbers. A pair $(p, q)$ is read as the integer $p - q$,
so coefficients and right-hand side entries are stored by positive and negative parts.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ZeroOneILP.ZeroOneILPInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/ZeroOneILPWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ZeroOneILPWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/0-1-integer-programming/index.html#zero-one-ilpinstance).

## Well-formed 0-1 integer programming instances

A 0-1 integer programming instance
$(n, A, b)$ is well formed when the right-hand side list $b$ has as many entries as there are
rows of the coefficient matrix $A$, and every row of $A$ has exactly $n$ entries.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ZeroOneILP.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/ZeroOneILPWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ZeroOneILPWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/0-1-integer-programming/index.html#well-formed).

## Feasible 0-1 integer programs

Let $(n, A, b)$ be a 0-1 integer programming instance whose
coefficient matrix has the rows $A_0, \dots, A_{m-1}$, with list entries indexed from $0$. For
$r < m$ and $j < n$, let $a_{rj}$ be the integer $p - q$ if row $A_r$ has a $j$-th entry
$(p, q)$, and $a_{rj} = 0$ otherwise; let $b_r$ be the integer $p' - q'$ if $b$ has an $r$-th
entry $(p', q')$, and $b_r = 0$ otherwise. The instance is feasible when there is
$x \in \{0, 1\}^n$ such that $\sum_{j < n} a_{rj} x_j \le b_r$ in $\mathbb{Z}$ for every $r < m$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ZeroOneILP.ZeroOneILPFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/ZeroOneILPWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ZeroOneILPWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/0-1-integer-programming/index.html#zero-one-ilpfeasible).

## 0-1 integer programming feasibility as a decision problem

The decision problem 0-1
INTEGER PROGRAMMING FEASIBILITY accepts a bitstring $x$ exactly when $x$ decodes, under the
canonical bitstring encoding, to a 0-1 integer programming instance that is well formed and
feasible; it rejects every bitstring that does not decode to such an instance.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ZeroOneILP.zeroOneILPDec`, a definition declared in [WantedExt/Complexity/NPComplete/ZeroOneILPWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ZeroOneILPWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/0-1-integer-programming/index.html#zero-one-ilpdec).

## 0-1 INTEGER PROGRAMMING FEASIBILITY is NP-complete

The decision problem 0-1 INTEGER
PROGRAMMING FEASIBILITY belongs to NP, and every decision problem in NP has a polynomial-time
many-one reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), 0-1 INTEGER PROGRAMMING; R. M. Karp, "Reducibility among combinatorial problems" (1972).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.ZeroOneILP.zeroOneILP_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/ZeroOneILPWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ZeroOneILPWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/0-1-integer-programming/index.html#zero-one-ilp-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: 0-1 integer programming](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/0-1-integer-programming/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/number-and-packing-problems/0-1-integer-programming)
