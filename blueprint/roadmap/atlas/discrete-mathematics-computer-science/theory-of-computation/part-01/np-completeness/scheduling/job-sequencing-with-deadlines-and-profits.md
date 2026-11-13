---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.JobSequencingWithProcessingTimes.JobSequencingWithProcessingTimesInstance, MetaMathlibExt.Complexity.NPComplete.JobSequencingWithProcessingTimes.JobSequencingWithProcessingTimesFeasible, MetaMathlibExt.Complexity.NPComplete.JobSequencingWithProcessingTimes.jobSequencingWithProcessingTimesDec, MetaMathlibExt.Complexity.NPComplete.JobSequencingWithProcessingTimes.jobSequencingWithProcessingTimes_npComplete
statement: formalized
---

# Job sequencing with deadlines and profits

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/job-sequencing-with-deadlines-and-profits/index.html).

## Job-sequencing instances

An instance of job sequencing with deadlines, processing times
and profits is a pair $(J, K)$ of a finite list $J$ of jobs, each a triple $(p, d, w)$ of natural
numbers giving its processing time $p$, deadline $d$ and profit $w$, and a natural number $K$,
the profit bound.

Formalized by `MetaMathlibExt.Complexity.NPComplete.JobSequencingWithProcessingTimes.JobSequencingWithProcessingTimesInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/JobSequencingWithProcessingTimesWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/JobSequencingWithProcessingTimesWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/job-sequencing-with-deadlines-and-profits/index.html#job-sequencing-with-processing-times-ins).

## Feasible job-sequencing instances

Let $(J, K)$ be a job-sequencing instance with jobs
$J = (p_0, d_0, w_0), \dots, (p_{n-1}, d_{n-1}, w_{n-1})$. The instance is feasible when there
are distinct indices $j_1, \dots, j_m < n$, for some $m \ge 0$, such that
$w_{j_1} + \dots + w_{j_m} \ge K$ and, for every $t$ with $1 \le t \le m$,
$p_{j_1} + \dots + p_{j_t} \le d_{j_t}$: the selected jobs, run one after another in this order
from time $0$, each finish by their deadlines, and their total profit is at least $K$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.JobSequencingWithProcessingTimes.JobSequencingWithProcessingTimesFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/JobSequencingWithProcessingTimesWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/JobSequencingWithProcessingTimesWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/job-sequencing-with-deadlines-and-profits/index.html#job-sequencing-with-processing-times-fea).

## Job sequencing with deadlines, processing times and profits as a decision problem

This
decision problem accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring
encoding, to a job-sequencing instance that is feasible; bitstrings that do not decode to an
instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.JobSequencingWithProcessingTimes.jobSequencingWithProcessingTimesDec`, a definition declared in [WantedExt/Complexity/NPComplete/JobSequencingWithProcessingTimesWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/JobSequencingWithProcessingTimesWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/job-sequencing-with-deadlines-and-profits/index.html#job-sequencing-with-processing-times-dec).

## JOB SEQUENCING WITH DEADLINES, PROCESSING TIMES, AND PROFITS is NP-complete

The decision
problem of job sequencing with deadlines, processing times and profits on bitstrings is
NP-complete: it belongs to NP, and every decision problem in NP has a polynomial-time many-one
reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), SEQUENCING WITH DEADLINES AND PROFITS (arbitrary processing times); R. M. Karp, "Reducibility among combinatorial problems" (1972).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.JobSequencingWithProcessingTimes.jobSequencingWithProcessingTimes_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/JobSequencingWithProcessingTimesWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/JobSequencingWithProcessingTimesWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/job-sequencing-with-deadlines-and-profits/index.html#job-sequencing-with-processing-times-np).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Job sequencing with deadlines and profits](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/job-sequencing-with-deadlines-and-profits/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/scheduling/job-sequencing-with-deadlines-and-profits)
