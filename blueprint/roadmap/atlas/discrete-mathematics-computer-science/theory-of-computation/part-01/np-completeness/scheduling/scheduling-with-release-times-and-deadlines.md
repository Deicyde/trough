---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.ReleaseDeadlinesScheduling.ReleaseDeadlinesSchedulingInstance, MetaMathlibExt.Complexity.NPComplete.ReleaseDeadlinesScheduling.ReleaseDeadlinesSchedulingFeasible, MetaMathlibExt.Complexity.NPComplete.ReleaseDeadlinesScheduling.releaseDeadlinesSchedulingDec, MetaMathlibExt.Complexity.NPComplete.ReleaseDeadlinesScheduling.releaseDeadlinesScheduling_npComplete
statement: formalized
---

# Scheduling with release times and deadlines

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/scheduling-with-release-times-and-deadlines/index.html).

## Instances of single-machine scheduling with release times and deadlines

A
release-deadlines instance is a list of jobs $(p_0, r_0, d_0), \dots, (p_{n-1}, r_{n-1}, d_{n-1})$
of triples of natural numbers, where $p_j$ is the processing time, $r_j$ the release time and
$d_j$ the deadline of job $j$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ReleaseDeadlinesScheduling.ReleaseDeadlinesSchedulingInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/ReleaseDeadlinesSchedulingWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ReleaseDeadlinesSchedulingWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/scheduling-with-release-times-and-deadlines/index.html#release-deadlines-scheduling-instance).

## Feasible single-machine schedules with release times and deadlines

A release-deadlines
instance with jobs $(p_j, r_j, d_j)$ for $j < n$ is feasible when there are start times
$s_0, \dots, s_{n-1} \in \mathbb{N}$ such that $r_j \le s_j$ and $s_j + p_j \le d_j$ for every
$j < n$, and for all $a < b < n$ either $s_a + p_a \le s_b$ or $s_b + p_b \le s_a$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ReleaseDeadlinesScheduling.ReleaseDeadlinesSchedulingFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/ReleaseDeadlinesSchedulingWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ReleaseDeadlinesSchedulingWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/scheduling-with-release-times-and-deadlines/index.html#release-deadlines-scheduling-feasible).

## Single-machine scheduling with release times and deadlines as a decision problem

SINGLE-MACHINE SCHEDULING WITH RELEASE TIMES AND DEADLINES is the decision problem that accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding of
release-deadlines instances, to a feasible instance. Bitstrings that do not decode to an instance
are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ReleaseDeadlinesScheduling.releaseDeadlinesSchedulingDec`, a definition declared in [WantedExt/Complexity/NPComplete/ReleaseDeadlinesSchedulingWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ReleaseDeadlinesSchedulingWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/scheduling-with-release-times-and-deadlines/index.html#release-deadlines-scheduling-dec).

## SINGLE-MACHINE SCHEDULING WITH RELEASE TIMES AND DEADLINES is NP-complete

The
decision problem SINGLE-MACHINE SCHEDULING WITH RELEASE TIMES AND DEADLINES belongs to NP, and
every decision problem in NP has a polynomial-time many-one reduction to it.

## Sources

- J. K. Lenstra, A. H. G. Rinnooy Kan, and P. Brucker, "Complexity of machine scheduling problems", Annals of Discrete Mathematics 1 (1977), 343-362 (strong NP-hardness of nonpreemptive 1|r_j|L_max; feasibility is L_max <= 0).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.ReleaseDeadlinesScheduling.releaseDeadlinesScheduling_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/ReleaseDeadlinesSchedulingWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/ReleaseDeadlinesSchedulingWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/scheduling-with-release-times-and-deadlines/index.html#release-deadlines-scheduling-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Scheduling with release times and deadlines](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/scheduling-with-release-times-and-deadlines/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/scheduling/scheduling-with-release-times-and-deadlines)
