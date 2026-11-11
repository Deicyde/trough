---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Parallel.Brent.Dag, Cslib.Algorithms.Lean.Parallel.Brent.depth, Cslib.Algorithms.Lean.Parallel.Brent.span, Cslib.Algorithms.Lean.Parallel.Brent.depth_lt_of_mem, Cslib.Algorithms.Lean.Parallel.Brent.depthsUpTo, Cslib.Algorithms.Lean.Parallel.Brent.depthTable, Cslib.Algorithms.Lean.Parallel.Brent.getD_depthTable, Cslib.Algorithms.Lean.Parallel.Brent.Schedule
statement: formalized
proof: formalized
---

# Work–span model and Brent's theorem

36 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html).

## Computation DAG

A computation DAG on $n$ unit-time tasks, numbered $0, \dots, n - 1$,
assigns to each task $v$ a list of predecessors (the tasks $v$ waits for), each numbered below
$v$; so the numbering is a topological order.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.Dag`, a structure declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#dag).

## Depth of a task in a computation DAG

The depth of a task $v$ is the number of tasks on a
longest path ending at $v$: it is $1$ plus the largest depth of a predecessor of $v$, or $1$ if
$v$ has no predecessors.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.depth`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#depth).

## Span of a computation DAG

The span of a computation DAG is the number of tasks on a
longest path, that is, the largest depth of a task, and $0$ when there are no tasks.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.span`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#span).

## Predecessors have smaller depth

In a computation DAG, if $u$ is a predecessor of $v$,
then the depth of $u$ is strictly less than the depth of $v$.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.depth_lt_of_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#depth-lt-of-mem).

## Depths of an initial segment of tasks

For $k \le n$, the list of the depths of tasks
$0, \dots, k - 1$ of a computation DAG on $n$ tasks, computed in topological order: the empty
list for $k = 0$, and for $k + 1$ the list for $k$ followed by $1$ plus the largest entry of that
list at a predecessor of task $k$ (or $1$ if task $k$ has no predecessors).

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.depthsUpTo`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#depths-up-to).

## Table of depths

The list of the depths of tasks $0, \dots, n - 1$ of a computation DAG on
$n$ tasks, computed once each in topological order: the entry for task $k$ is $1$ plus the largest
entry at a predecessor of $k$, or $1$ if $k$ has no predecessors.

With lists (appending and indexed reads take linear time) this costs $O(n^2 + n|E|)$, where $|E|$
is the total number of predecessor entries; evaluating the depth directly from its recursive
definition instead recomputes shared subpaths exponentially often.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.depthTable`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#depth-table).

## The table of depths is correct

For every task $v$ of a computation DAG, the entry of the
table of depths at position $v$ equals the depth of $v$.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.getD_depthTable`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#get-d-depth-table).

## Schedule of a computation DAG

A schedule of a computation DAG on $n$ tasks on $p$
processors assigns to each task $v$ a step $t(v) \in \mathbb{N}$ in which it runs, such that
$t(u) < t(v)$ whenever $u$ is a predecessor of $v$, and for every step $s$ at most $p$ tasks $v$
have $t(v) = s$.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.Schedule`, a structure declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#schedule).

## Length of a schedule

The length of a schedule is the number of steps it takes: one more
than the latest step in which a task runs (steps are numbered from $0$), or $0$ if there are no
tasks.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.Schedule.length`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#length).

## The work law

For a computation DAG on $n$ tasks, every schedule of it on $p$ processors
that takes $T$ steps satisfies $n \le p T$. In particular, for $p > 0$ the schedule takes at
least $n / p$ steps.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.Schedule.work_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#work-le).

## Depth bounds the step of a task

For every schedule of a computation DAG on $p$
processors, with steps numbered from $0$, every task $v$ runs in a step $t$ with
$\operatorname{depth}(v) \le t + 1$.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.Schedule.depth_le_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#depth-le-time).

## The span law

No schedule is shorter than the span.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.Schedule.span_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#span-le).

## Level size

For a computation DAG and a natural number $d$, the size of level $d$ is the
number of tasks of depth $d$.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.levelCard`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#level-card).

## Steps of a level

For a computation DAG and natural numbers $p$ and $d$, let $L_d$ be the
number of tasks of depth $d$. The number of steps of level $d$ on $p$ processors is
$\lceil L_d / p \rceil$ if $p \ge 1$, and $0$ if $p = 0$.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.levelSteps`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#level-steps).

## First step of a level

For a computation DAG and natural numbers $p$ and $d$, let $s_e$
be the number of steps of level $e$ on $p$ processors: $\lceil L_e / p \rceil$ if $p \ge 1$ and
$0$ if $p = 0$, where $L_e$ is the number of tasks of depth $e$. The first step of level $d$ is
$\sum_{e < d} s_e$.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.offset`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#offset).

## Rank within a level

In a computation DAG, the rank of a task $v$ is the number of tasks
of the same depth as $v$ with a smaller number than $v$. Taken in numbering order, the tasks of a
level have ranks $0, 1, 2, \dots$

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.rank`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#rank).

## Step of a task in Brent's schedule

Let $G$ be a computation DAG and $p$ a natural number.
If $p \ge 1$, for each $d$ let $L_d$ be the number of tasks of depth $d$ and
$o_d = \sum_{e < d} \lceil L_e / p \rceil$, and for each task $v$ let $r(v)$ be the number of tasks
of the same depth as $v$ with a smaller number; the step of a task $v$ is
$o_{\operatorname{depth}(v)} + \lfloor r(v) / p \rfloor$. If $p = 0$, the step of every task is $0$.

For $p \ge 1$ this runs the tasks level by level, each level of $L_d$ tasks in
$\lceil L_d / p \rceil$ steps of at most $p$ tasks.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.levelTime`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#level-time).

## No step of Brent's level schedule mixes levels

Let $G$ be a computation DAG and
$p \ge 1$. If two tasks $u$ and $v$ run in the same step of Brent's level-by-level schedule on
$p$ processors, then $u$ and $v$ have the same depth.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.depth_eq_of_levelTime_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#depth-eq-of-level-time-eq).

## Ranks increase within a level

In a computation DAG, if tasks $u$ and $v$ have the same
depth and $u$ has a smaller number than $v$, then the rank of $u$ is smaller than the rank of
$v$, where the rank of a task is the number of tasks of the same depth with a smaller number.
In particular, ranks are distinct within a level.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.rank_lt_rank`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#rank-lt-rank).

## Brent's level schedule

Let $G$ be a computation DAG and $p \ge 1$. For each $d$ let
$L_d$ be the number of tasks of depth $d$ and $o_d = \sum_{e < d} \lceil L_e / p \rceil$, and for
each task $v$ let $r(v)$ be the number of tasks of the same depth as $v$ with a smaller number.
Brent's level schedule is the schedule of $G$ on $p$ processors that runs each task $v$ at step
$o_{\operatorname{depth}(v)} + \lfloor r(v) / p \rfloor$.

It runs the tasks level by level, in order of depth, each level of $L_d$ tasks in
$\lceil L_d / p \rceil$ steps of at most $p$ tasks.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.levelSchedule`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#level-schedule).

## Level $0$ is empty

In every computation DAG no task has depth $0$, so the number of
tasks of depth $0$ is $0$.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.levelCard_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#level-card-zero).

## Brent's theorem

Let $G$ be a computation DAG with $n$ tasks and span $D$, and let
$p \ge 1$. If Brent's level schedule of $G$ on $p$ processors takes $T$ steps, then
$pT \le n + (p - 1) D$, that is, $T \le (n - D)/p + D$.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.levelSchedule_length`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#level-schedule-length).

## Brent's theorem with the work and span laws

Let $G$ be a computation DAG on $n$
unit-time tasks with span $D$, and let $p \ge 1$. Then some schedule of $G$ on $p$ processors
has length $T$ with $pT \le n + (p - 1)D$, and every schedule of $G$ on $p$ processors has a
length $T'$ with $n \le pT'$ (the work law) and $D \le T'$ (the span law).

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.brent`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/Brent.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/Brent.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#brent).

## Load of a step

The load of step $t$ in a schedule $S$ of a computation DAG is the number
of tasks that $S$ runs in step $t$.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.Schedule.load`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#load).

## Ready task

In a schedule $S$ of a task graph, a task $v$ is ready at step $t$ if $v$
runs in a step later than $t$ and every predecessor of $v$ runs in a step earlier than $t$.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.Schedule.Ready`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#ready).

## Greedy schedule

A schedule $S$ of a computation DAG on $p$ processors is greedy if, for
every step $t$ and every task that is ready at step $t$, exactly $p$ tasks run in step $t$: a step
leaves a ready task waiting only when all $p$ processors are busy.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.Schedule.Greedy`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#greedy).

## Greediness need only be checked at the steps of the schedule

Let $S$ be a schedule of a
computation DAG on $p$ processors taking $T$ steps. Then $S$ is greedy if and only if, for every
step $t < T$ and every task $v$ that is ready at step $t$, exactly $p$ tasks run in step $t$.

This holds because a task is never ready at or after the last step.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.Schedule.greedy_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#greedy-iff).

## Number of incomplete steps

For a schedule $S$ of a computation DAG on $p$ processors and
a natural number $t$, the number of incomplete steps before step $t$ is the number of steps
$s < t$ in which $S$ runs fewer than $p$ tasks.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.Schedule.incomplete`, a definition declared in [CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#incomplete).

## Each incomplete step advances the critical path

In a greedy schedule, fewer than
`depth v` incomplete steps precede the step of task `v`.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.Schedule.incomplete_lt_depth`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#incomplete-lt-depth).

## The step loads add up to the number of tasks

For a schedule $S$ of a task graph with $n$
tasks that takes $T$ steps, the numbers of tasks run in the steps $0, 1, \dots, T - 1$ add up
to $n$.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.Schedule.sum_load`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#sum-load).

## Complete steps are bounded by the work

Let $G$ be a computation DAG with $n$ tasks, and
let $S$ be a schedule of $G$ on $p$ processors taking $T$ steps. If $C$ is the number of steps
$t < T$ in which $S$ runs at least $p$ tasks (the complete steps, where all $p$ processors are
busy), then $pC \le n$.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.Schedule.mul_complete_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#mul-complete-le).

## A greedy schedule has at most $D$ incomplete steps

Let $G$ be a computation DAG with span
$D$, and let $S$ be a greedy schedule of $G$ on $p$ processors taking $T$ steps. Then at most $D$
of the steps $t < T$ are incomplete, that is, run fewer than $p$ tasks.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.Schedule.incomplete_length_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#incomplete-length-le).

## Every step of a schedule has a task running at or after it

Let $S$ be a schedule of a
computation DAG on $p$ processors taking $T$ steps, numbered from $0$. For every step $t < T$
there is a task that $S$ runs at step $t$ or later.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.Schedule.exists_le_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#exists-le-time).

## A greedy schedule never idles

Let $S$ be a greedy schedule of a task graph on $p$
processors that takes $T$ steps, numbered $0, \dots, T - 1$. Then every step $t < T$ of $S$
runs at least one task.

The task that runs earliest among those not run before step $t$ has all its predecessors done
before step $t$. If step $t$ ran no task, this task would be ready at step $t$, while a greedy
step with a ready task keeps all $p$ processors busy.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.Schedule.one_le_load`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#one-le-load).

## The greedy scheduling bound

Let $G$ be a computation DAG with $n$ tasks and span $D$, and
let $S$ be a greedy schedule of $G$ on $p$ processors taking $T$ steps. Then
$pT \le n + (p - 1)D$.

Each complete step runs $p$ tasks, and each of the at most $D$ incomplete steps runs at least one.

## Sources

- the unit-task case of Graham's list-scheduling argument, Graham, *Bounds for certain multiprocessing anomalies*, Bell System Tech. J. 45, 1966.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.Schedule.greedy_length_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#greedy-length-le).

## The work-span bound for greedy schedules

Let $G$ be a computation DAG with $n$ tasks and
span $D$, and let $S$ be a greedy schedule of $G$ on $p$ processors taking $T$ steps. Then
$pT \le n + pD$, that is, $T \le n/p + D$ when $p \ge 1$.

This is a weakening of the greedy scheduling bound $pT \le n + (p - 1)D$.

## Sources

- CLRS, third edition, Theorem 27.1.

Formalized by `Cslib.Algorithms.Lean.Parallel.Brent.Schedule.greedy_length`, a theorem declared in [CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Parallel/GreedyScheduler.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html#greedy-length).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Work–span model and Brent's theorem](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/parallel-algorithms/work-span-model-and-brent-s-theorem)
