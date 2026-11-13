---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.Scheduling.IsScheduleOf, Cslib.Algorithms.Lean.Scheduling.makespan, Cslib.Algorithms.Lean.Scheduling.leastLoaded, Cslib.Algorithms.Lean.Scheduling.listScheduleScan, Cslib.Algorithms.Lean.Scheduling.listSchedule, Cslib.Algorithms.Lean.Scheduling.lpt, Cslib.Algorithms.Lean.Scheduling.isScheduleOf_nil, Cslib.Algorithms.Lean.Scheduling.IsScheduleOf.le_makespan
statement: formalized
proof: formalized
---

# List scheduling on identical machines

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html).

## Schedule of a list of jobs

Let $m$ be a natural number. An assignment $\sigma$ of a list
$\sigma(i)$ of natural numbers (processing times) to each machine $i \in \{0, \dots, m - 1\}$ is a
schedule of a list $J$ of natural numbers when the sum over all machines $i$ of the multisets of
entries of $\sigma(i)$ equals the multiset of entries of $J$, that is, every number occurs in
the lists $\sigma(i)$ together exactly as often as it occurs in $J$.

Formalized by `Cslib.Algorithms.Lean.Scheduling.IsScheduleOf`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#is-schedule-of).

## Makespan

For a schedule $\sigma$ that gives each of $m$ machines a list of processing
times, the load of a machine is the sum of its list, and the makespan of $\sigma$ is the largest
machine load ($0$ when $m = 0$).

Formalized by `Cslib.Algorithms.Lean.Scheduling.makespan`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#makespan).

## Least-loaded machine

Let $m \ge 1$ and let $L$ assign a load $L(i) \in \mathbb{N}$ to
each machine $i \in \{0, \dots, m - 1\}$. The least-loaded machine for $L$ is the smallest index
$i$ at which $L(i)$ is minimal.

Formalized by `Cslib.Algorithms.Lean.Scheduling.leastLoaded`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#least-loaded).

## List scheduling from an intermediate state

Let $m \ge 1$. Given loads $L(i)$ and job
lists $\sigma(i)$ for the machines $i \in \{0, \dots, m - 1\}$ and a list of remaining jobs, list
scheduling returns $\sigma$ at cost $0$ when no jobs remain. Otherwise it charges cost $m$, takes
the first remaining job $p$, appends $p$ to $\sigma(k)$ and adds $p$ to $L(k)$ for the
least-loaded machine $k$ for $L$, and continues in the same way with the other remaining jobs.
The loads $L$ are not required to be the sums of the lists $\sigma(i)$.

Formalized by `Cslib.Algorithms.Lean.Scheduling.listScheduleScan`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#list-schedule-scan).

## Graham's list scheduling

Given $m \ge 1$ identical machines and a list of job
processing times (natural numbers), start with every machine empty and take the jobs in the
given order, appending each job to the list of a currently least-loaded machine (the first one in
index order), where the load of a machine is the sum of its jobs. The result assigns to each
machine its list of jobs. The cost counted is $m$ per job, one unit for each machine load
inspected.

Formalized by `Cslib.Algorithms.Lean.Scheduling.listSchedule`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#list-schedule).

## Longest processing time first (LPT)

Given $m \ge 1$ identical machines and a list of job
processing times (natural numbers), LPT sorts the jobs into nonincreasing order by merge sort and
then applies Graham's list scheduling on $m$ machines to the sorted list. The cost counted is the
number of comparisons made by merge sort plus the cost of list scheduling, $m$ per job.

Formalized by `Cslib.Algorithms.Lean.Scheduling.lpt`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#lpt).

## The empty schedule

For every number $m$ of machines, the assignment of the empty list
to each of the $m$ machines is a schedule of the empty list of jobs.

Formalized by `Cslib.Algorithms.Lean.Scheduling.isScheduleOf_nil`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#is-schedule-of-nil).

## Every job is at most the makespan

Let $\sigma$ be a schedule on $m$ machines of a list
$J$ of processing times. Then every entry $x$ of $J$ is at most the makespan of $\sigma$.

Formalized by `Cslib.Algorithms.Lean.Scheduling.IsScheduleOf.le_makespan`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#le-makespan).

## Total work is at most $m$ times the makespan

If $\sigma$ is a schedule of a list $P$ of
jobs on $m$ machines, then the total processing time of $P$ is at most $m$ times the makespan of
$\sigma$.

Formalized by `Cslib.Algorithms.Lean.Scheduling.IsScheduleOf.sum_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#sum-le).

## List-scheduling state invariant

A list $P$ of jobs, machine loads $\ell_i \in \mathbb{N}$
for $i < m$, and a schedule $\sigma$ on $m$ machines satisfy the invariant when $\sigma$ is a
schedule of $P$ and, for every machine $i$, $\ell_i$ is the load of machine $i$ in $\sigma$, the
sum of the processing times assigned to it.

Formalized by `Cslib.Algorithms.Lean.Scheduling.ScanInv`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#scan-inv).

## Invariant bound for list scheduling

Let $m \ge 1$ and $a, b, M \in \mathbb{N}$. Let
$\sigma$ assign job lists to the $m$ machines so that $\sigma$ is a schedule of a list $P$ of
jobs already placed, let $L(i)$ be the sum of $\sigma(i)$ for each machine $i$, and let $R$ be a
list of remaining jobs. Assume that $a$ times the makespan of $\sigma$ is at most $bM$. Assume
also that whenever $P$ followed by $R$ equals $P'$ followed by a job $p$ followed by a list
$R'$, and $\sigma'$ is any schedule of $P'$ with loads $L'(i)$ equal to the sum of
$\sigma'(i)$, we have $a(L'(k) + p) \le bM$, where $k$ is the least-loaded machine for $L'$.
Then list scheduling of $R$ started from the loads $L$ and machine lists $\sigma$ produces a
schedule whose makespan $C$ satisfies $aC \le bM$.

Formalized by `Cslib.Algorithms.Lean.Scheduling.listScheduleScan_bound`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#list-schedule-scan-bound).

## A least-loaded machine carries at most the average load

Let $\sigma$ be a schedule of a
list $P$ of jobs on $m \ge 1$ machines, with load $\ell_i$ on machine $i$. Then $m$ times the load
of a least-loaded machine is at most the total processing time $T$ of the jobs in $P$, counted
with multiplicity: $m \min_i \ell_i \le T$.

Formalized by `Cslib.Algorithms.Lean.Scheduling.mul_leastLoaded_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#mul-least-loaded-le).

## Graham's bound for list scheduling

Let $m \ge 1$ and let $J$ be a list of processing
times. Let $C$ be the makespan of the schedule that list scheduling on $m$ machines produces
from $J$, taking the jobs in the order of $J$, and let $M$ be the makespan of any schedule of $J$
on $m$ machines. Then $mC \le (2m - 1)M$, that is, $C \le (2 - 1/m)M$.

## Sources

- Graham, "Bounds for certain multiprocessing anomalies", Bell System Technical Journal 45 (1966).

Formalized by `Cslib.Algorithms.Lean.Scheduling.listSchedule_approx`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#list-schedule-approx).

## Counting jobs when every machine is heavily loaded

Let $\sigma$ be a schedule of a list
$P$ of jobs on $m$ machines, let $p$ and $M$ be natural numbers, and let $d = \max(M - p, 0)$. If
every job in $P$ is at least $p$ and every machine has load (the sum of its jobs) greater than
$d$, then $2m \le n + k$, where $n$ is the number of jobs in $P$ and $k$ is the number of jobs
$x$ in $P$ with $p \le x$ and $x > d$, both counted with multiplicity.

The reason is that each machine then holds two jobs or one job longer than $d$.

Formalized by `Cslib.Algorithms.Lean.Scheduling.two_mul_le_of_loads_gt`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#two-mul-le-of-loads-gt).

## At most two long jobs per machine

Let $p$ and $M$ be natural numbers with $M < 3p$,
and let $\ell$ be a list of natural numbers (the jobs of one machine) whose sum is at most $M$.
Then the number of entries of $\ell$ that are at least $p$, plus the number of entries that are
at least $p$ and greater than $M - p$, is at most $2$. Here $M - p$ is truncated subtraction,
equal to $0$ when $M < p$. So $\ell$ has at most two entries that are at least $p$, and at most
one if one of them is greater than $M - p$.

Formalized by `Cslib.Algorithms.Lean.Scheduling.countP_add_countP_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#count-p-add-count-p-le).

## The LPT placement step

Let $m \ge 1$ and let a list of job processing times, in
nonincreasing order, be the concatenation of a list $P$, a job $p$ and a list $R$. Let $\sigma$
be a schedule of the jobs $P$ on $m$ machines, with load $\ell_i$ on machine $i$, and let
$L = \min_i \ell_i$ be the load of a least-loaded machine. Then for every schedule $\tau$ of all
the jobs on the $m$ machines, with makespan $M$, we have $3m(L + p) \le (4m - 1)M$.

Formalized by `Cslib.Algorithms.Lean.Scheduling.lpt_step_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#lpt-step-le).

## Graham's bound for LPT scheduling

Let $m \ge 1$ and let $J$ be a list of natural numbers
(job processing times). Let $C$ be the makespan of the schedule of $J$ on $m$ machines produced
by the LPT algorithm, and let $M$ be the makespan of any schedule $\tau$ of $J$ on $m$ machines.
Then $3mC \le (4m - 1)M$, that is, $C \le (4/3 - 1/(3m))M$.

## Sources

- Graham, "Bounds on multiprocessing timing anomalies", SIAM J. Appl. Math. 17 (1969).

Formalized by `Cslib.Algorithms.Lean.Scheduling.lpt_approx`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#lpt-approx).

## List scheduling schedules every job

For $m \ge 1$ and every list $J$ of processing
times, the assignment that list scheduling on $m$ machines produces from $J$ is a schedule of
$J$.

Formalized by `Cslib.Algorithms.Lean.Scheduling.listSchedule_isScheduleOf`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 418](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L418). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#list-schedule-is-schedule-of).

## Running time of list scheduling

For $m \ge 1$ and every list of $n$ jobs, list
scheduling on $m$ machines has cost exactly $nm$, in the cost model that charges $m$ for each job
placed (one unit per machine load inspected).

Formalized by `Cslib.Algorithms.Lean.Scheduling.listSchedule_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#list-schedule-time).

## Running time of LPT

On $m \ge 1$ machines and a list of $n$ jobs, LPT costs at most
$n \lceil \log_2 n \rceil + nm$, counting merge-sort comparisons and machine load inspections.

Formalized by `Cslib.Algorithms.Lean.Scheduling.lpt_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/ListScheduling.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html#lpt-time-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: List scheduling on identical machines](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/approximation-algorithms/list-scheduling-on-identical-machines)
