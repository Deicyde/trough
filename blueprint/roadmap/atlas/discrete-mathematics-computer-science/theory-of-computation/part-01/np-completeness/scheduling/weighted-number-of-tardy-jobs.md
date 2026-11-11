---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.WeightedTardyJobs.WeightedTardyJobsInstance, MetaMathlibExt.Complexity.NPComplete.WeightedTardyJobs.WeightedTardyStep, MetaMathlibExt.Complexity.NPComplete.WeightedTardyJobs.WeightedTardy, MetaMathlibExt.Complexity.NPComplete.WeightedTardyJobs.WeightedTardyJobsFeasible, MetaMathlibExt.Complexity.NPComplete.WeightedTardyJobs.weightedTardyJobsDec, MetaMathlibExt.Complexity.NPComplete.WeightedTardyJobs.weightedTardyJobs_npComplete
statement: formalized
---

# Weighted number of tardy jobs

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/weighted-number-of-tardy-jobs/index.html).

## Weighted tardy jobs instances

An instance of WEIGHTED NUMBER OF TARDY JOBS is a pair
consisting of a finite list of jobs, each a triple $(p, d, w)$ of natural numbers giving its
processing time $p$, due date $d$ and weight $w$, and a natural number $K$, the bound.

Formalized by `MetaMathlibExt.Complexity.NPComplete.WeightedTardyJobs.WeightedTardyJobsInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/WeightedTardyJobsWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/WeightedTardyJobsWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/weighted-number-of-tardy-jobs/index.html#weighted-tardy-jobs-instance).

## One step of the weighted tardy jobs computation

Let $J$ be a list of jobs, each a triple
$(p, d, w)$ of natural numbers (processing time, due date, weight). Given a state $(t, s)$ and a
natural number $j$, let $(p, d, w)$ be the job at position $j$ of $J$, counting from $0$, or
$(0, 0, 0)$ if $J$ has no position $j$, and let $t' = t + p$. The step returns $(t', s + w)$ if
$d < t'$, and $(t', s)$ otherwise.

Formalized by `MetaMathlibExt.Complexity.NPComplete.WeightedTardyJobs.WeightedTardyStep`, a definition declared in [WantedExt/Complexity/NPComplete/WeightedTardyJobsWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/WeightedTardyJobsWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/weighted-number-of-tardy-jobs/index.html#weighted-tardy-step).

## Weighted number of tardy jobs of an ordering

Let $J$ be a list of jobs, each a triple of
natural numbers (processing time, due date, weight), and write $(p_i, d_i, w_i)$ for the job at
position $i$ of $J$, counting from $0$, with $(p_i, d_i, w_i) = (0, 0, 0)$ when $J$ has no
position $i$. For a list $(j_1, \dots, j_m)$ of natural numbers, the weighted number of tardy
jobs of this order is the sum of $w_{j_k}$ over all $k$ with $d_{j_k} < C_k$, where
$C_k = p_{j_1} + \dots + p_{j_k}$ is the completion time of the $k$-th job.

Formalized by `MetaMathlibExt.Complexity.NPComplete.WeightedTardyJobs.WeightedTardy`, a definition declared in [WantedExt/Complexity/NPComplete/WeightedTardyJobsWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/WeightedTardyJobsWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/weighted-number-of-tardy-jobs/index.html#weighted-tardy).

## Feasible weighted tardy jobs instances

A weighted tardy jobs instance, consisting of a
list of $n$ jobs and a bound $K$, is feasible when there is an ordering of its jobs, that is, a
list of the job indices $0, 1, \dots, n - 1$ in which each index occurs exactly once, whose
weighted number of tardy jobs is at most $K$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.WeightedTardyJobs.WeightedTardyJobsFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/WeightedTardyJobsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/WeightedTardyJobsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/weighted-number-of-tardy-jobs/index.html#weighted-tardy-jobs-feasible).

## The weighted number of tardy jobs decision problem

WEIGHTED NUMBER OF TARDY JOBS is the
decision problem that accepts a bitstring $x$ exactly when $x$ decodes, under the canonical
bitstring encoding of weighted tardy jobs instances, to a feasible instance, that is, an instance
having an ordering of its jobs whose weighted number of tardy jobs is at most its bound. A
bitstring that decodes to no instance is rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.WeightedTardyJobs.weightedTardyJobsDec`, a definition declared in [WantedExt/Complexity/NPComplete/WeightedTardyJobsWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/WeightedTardyJobsWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/weighted-number-of-tardy-jobs/index.html#weighted-tardy-jobs-dec).

## WEIGHTED NUMBER OF TARDY JOBS is NP-complete

The weighted number of tardy jobs decision
problem lies in NP, and every decision problem in NP has a polynomial-time many-one reduction to
it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), WEIGHTED NUMBER OF TARDY JOBS (1||sum w_j U_j).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.WeightedTardyJobs.weightedTardyJobs_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/WeightedTardyJobsWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/WeightedTardyJobsWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/weighted-number-of-tardy-jobs/index.html#weighted-tardy-jobs-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weighted number of tardy jobs](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/weighted-number-of-tardy-jobs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/scheduling/weighted-number-of-tardy-jobs)
