---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.PrecedenceMultiprocessorScheduling.PrecedenceMultiprocessorSchedulingInstance, MetaMathlibExt.Complexity.NPComplete.PrecedenceMultiprocessorScheduling.WellFormed, MetaMathlibExt.Complexity.NPComplete.PrecedenceMultiprocessorScheduling.PrecedenceMultiprocessorSchedulingFeasible, MetaMathlibExt.Complexity.NPComplete.PrecedenceMultiprocessorScheduling.precedenceMultiprocessorSchedulingDec, MetaMathlibExt.Complexity.NPComplete.PrecedenceMultiprocessorScheduling.precedenceMultiprocessorScheduling_npComplete
statement: formalized
---

# Precedence-constrained multiprocessor scheduling

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/precedence-constrained-multiprocessor-scheduling/index.html).

## Instances of precedence-constrained multiprocessor scheduling

An instance is a tuple
$(d, P, m, D)$ in which $d = (d_0, \dots, d_{n-1})$ is a list of natural numbers, $d_j$ being the
duration of job $j$; $P$ is a list of pairs $(a, b)$ of natural numbers, each read as the
precedence constraint that job $a$ precedes job $b$; $m$ is a natural number, the number of
machines; and $D$ is a natural number, the deadline.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PrecedenceMultiprocessorScheduling.PrecedenceMultiprocessorSchedulingInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/PrecedenceMultiprocessorSchedulingWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PrecedenceMultiprocessorSchedulingWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/precedence-constrained-multiprocessor-scheduling/index.html#precedence-multiprocessor-scheduling-ins).

## Well-formed precedence-multiprocessor scheduling instances

An instance $(d, P, m, D)$
whose list of job durations $d$ has length $n$ is well formed when every precedence pair
$(a, b) \in P$ satisfies $a < n$, $b < n$ and $a \ne b$, and there is an ordering of the jobs
$0, \dots, n-1$ (a permutation of this list) in which $a$ comes before $b$ for every
$(a, b) \in P$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PrecedenceMultiprocessorScheduling.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/PrecedenceMultiprocessorSchedulingWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PrecedenceMultiprocessorSchedulingWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/precedence-constrained-multiprocessor-scheduling/index.html#well-formed).

## Feasible precedence-multiprocessor scheduling instances

An instance $(d, P, m, D)$ with
job durations $d = (d_0, \dots, d_{n-1})$ is feasible when there are start times
$s_0, \dots, s_{n-1} \in \mathbb{N}$ and machines $\mu_0, \dots, \mu_{n-1} \in \mathbb{N}$ such
that $\mu_j < m$ and $s_j + d_j \le D$ for every $j < n$, $s_a + d_a \le s_b$ for every
precedence pair $(a, b) \in P$, and for all jobs $a < b < n$ with $\mu_a = \mu_b$, either
$s_a + d_a \le s_b$ or $s_b + d_b \le s_a$. Here $s_j$ and $d_j$ are read as $0$ when
$j \ge n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PrecedenceMultiprocessorScheduling.PrecedenceMultiprocessorSchedulingFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/PrecedenceMultiprocessorSchedulingWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PrecedenceMultiprocessorSchedulingWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/precedence-constrained-multiprocessor-scheduling/index.html#precedence-multiprocessor-scheduling-fea).

## The precedence-constrained multiprocessor scheduling decision problem

The decision
problem that accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring
encoding, to a precedence-multiprocessor scheduling instance that is well formed and feasible.
Bitstrings that do not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PrecedenceMultiprocessorScheduling.precedenceMultiprocessorSchedulingDec`, a definition declared in [WantedExt/Complexity/NPComplete/PrecedenceMultiprocessorSchedulingWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PrecedenceMultiprocessorSchedulingWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/precedence-constrained-multiprocessor-scheduling/index.html#precedence-multiprocessor-scheduling-dec).

## PRECEDENCE-CONSTRAINED MULTIPROCESSOR SCHEDULING is NP-complete

The
precedence-constrained multiprocessor scheduling decision problem is in NP, and every decision
problem in NP has a polynomial-time many-one reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), PRECEDENCE-CONSTRAINED MULTIPROCESSOR SCHEDULING; J. D. Ullman, "NP-complete scheduling problems" (1975).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.PrecedenceMultiprocessorScheduling.precedenceMultiprocessorScheduling_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/PrecedenceMultiprocessorSchedulingWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/PrecedenceMultiprocessorSchedulingWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/precedence-constrained-multiprocessor-scheduling/index.html#precedence-multiprocessor-scheduling-np).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Precedence-constrained multiprocessor scheduling](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/precedence-constrained-multiprocessor-scheduling/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/scheduling/precedence-constrained-multiprocessor-scheduling)
