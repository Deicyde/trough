---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.IntervalCompatible, Cslib.Algorithms.Lean.TimeM.IntervalCompatible.symm, Cslib.Algorithms.Lean.TimeM.intervalSchedule, Cslib.Algorithms.Lean.TimeM.intervalSchedule_correct, Cslib.Algorithms.Lean.TimeM.intervalSchedule_time
statement: formalized
proof: formalized
---

# Interval scheduling

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/interval-scheduling/index.html).

## Compatible activities

Let each activity $a$ have a start time $s(a)$ and a finish time
$f(a)$ in a linearly ordered type, thought of as the closed-open interval $[s(a), f(a))$. Two
activities $a$ and $b$ are compatible when $f(a) \le s(b)$ or $f(b) \le s(a)$; in particular,
activities whose intervals only touch at an endpoint are compatible.

Formalized by `Cslib.Algorithms.Lean.TimeM.IntervalCompatible`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/IntervalScheduling.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/IntervalScheduling.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/interval-scheduling/index.html#interval-compatible).

## Symmetry of interval compatibility

For any start and finish times and any activities $a$
and $b$, if $a$ is compatible with $b$, then $b$ is compatible with $a$.

Formalized by `Cslib.Algorithms.Lean.TimeM.IntervalCompatible.symm`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/IntervalScheduling.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/IntervalScheduling.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/interval-scheduling/index.html#symm).

## Earliest-finish greedy interval scheduling

Given start and finish times $s$ and $f$ in a
linear order and a list $L$ of activities, sort $L$ by finish time with merge sort, then scan the
sorted list: the first activity is selected, and each later activity $a$ is selected exactly when
$s(a)$ is at least the finish time of the last selected activity. The result is the list of
selected activities in sorted order, together with a cost that counts one for each finish-time
comparison made by the merge sort and one for each scanned activity after the first.

Formalized by `Cslib.Algorithms.Lean.TimeM.intervalSchedule`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/IntervalScheduling.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/IntervalScheduling.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/interval-scheduling/index.html#interval-schedule).

## Correctness and optimality of earliest-finish interval scheduling

Let $s$ and $f$ assign
start and finish times in a linear order to activities, and let $L$ be a list of activities with
$s(a) < f(a)$ for every $a$ in $L$. Let $S$ be the list returned by the earliest-finish schedule
of $L$. Then $S$ is a subpermutation of $L$ (each activity occurs in $S$ at most as often as in
$L$), any two entries of $S$ at distinct positions are compatible, and every subpermutation $M$
of $L$ whose entries at distinct positions are pairwise compatible has length at most the length
of $S$.

Formalized by `Cslib.Algorithms.Lean.TimeM.intervalSchedule_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/IntervalScheduling.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/IntervalScheduling.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/interval-scheduling/index.html#interval-schedule-correct).

## Comparison bound for earliest-finish interval scheduling

For any start and finish times
and any list of $n$ activities, the earliest-finish schedule charges at most
$n \lceil \log_2 n \rceil + (n - 1)$ comparisons when $n \ge 1$, and none when $n = 0$.

Formalized by `Cslib.Algorithms.Lean.TimeM.intervalSchedule_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/IntervalScheduling.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/IntervalScheduling.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/interval-scheduling/index.html#interval-schedule-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Interval scheduling](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/interval-scheduling/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/greedy-algorithms-and-matroids/interval-scheduling)
