---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.ParallelMachinesDeadlines.ParallelMachinesDeadlinesInstance, MetaMathlibExt.Complexity.NPComplete.ParallelMachinesDeadlines.ParallelMachinesDeadlinesFeasible, MetaMathlibExt.Complexity.NPComplete.ParallelMachinesDeadlines.parallelMachinesDeadlinesDec, MetaMathlibExt.Complexity.NPComplete.ParallelMachinesDeadlines.parallelMachinesDeadlines_npComplete
statement: formalized
---

# Parallel machine scheduling with deadlines

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/parallel-machine-scheduling-with-deadlines/index.html).

## Parallel machine scheduling instances

An instance of parallel machine scheduling with
deadlines is a pair consisting of a finite list of jobs, each a pair $(p, d)$ of natural numbers
giving its processing time $p$ and deadline $d$, and a natural number $m$, the number of
machines.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ParallelMachinesDeadlines.ParallelMachinesDeadlinesInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/ParallelMachinesDeadlinesWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ParallelMachinesDeadlinesWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/parallel-machine-scheduling-with-deadlines/index.html#parallel-machines-deadlines-instance).

## Feasible schedules on parallel machines with deadlines

An instance consisting of jobs
$(p_1, d_1), \dots, (p_k, d_k)$, where job $j$ has processing time $p_j$ and deadline $d_j$, and
a number $m$ of machines is feasible when there are start times $s_1, \dots, s_k \in \mathbb{N}$
and machines $\mu_1, \dots, \mu_k \in \{0, \dots, m - 1\}$ such that $s_j + p_j \le d_j$ for
every $j$, and for all $a \ne b$ with $\mu_a = \mu_b$, either $s_a + p_a \le s_b$ or
$s_b + p_b \le s_a$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ParallelMachinesDeadlines.ParallelMachinesDeadlinesFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/ParallelMachinesDeadlinesWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ParallelMachinesDeadlinesWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/parallel-machine-scheduling-with-deadlines/index.html#parallel-machines-deadlines-feasible).

## The PARALLEL MACHINES WITH DEADLINES decision problem

This decision problem accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to jobs
$(p_1, d_1), \dots, (p_k, d_k)$ of natural numbers (processing times and deadlines) and a number
$m$ of machines for which there are start times $s_1, \dots, s_k \in \mathbb{N}$ and machines
$\mu_1, \dots, \mu_k \in \{0, \dots, m - 1\}$ such that $s_j + p_j \le d_j$ for every $j$, and
for all $a \ne b$ with $\mu_a = \mu_b$, either $s_a + p_a \le s_b$ or $s_b + p_b \le s_a$. It
rejects every bitstring that does not decode.

Formalized by `MetaMathlibExt.Complexity.NPComplete.ParallelMachinesDeadlines.parallelMachinesDeadlinesDec`, a definition declared in [WantedExt/Complexity/NPComplete/ParallelMachinesDeadlinesWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ParallelMachinesDeadlinesWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/parallel-machine-scheduling-with-deadlines/index.html#parallel-machines-deadlines-dec).

## PARALLEL MACHINES WITH DEADLINES is NP-complete

The PARALLEL MACHINES WITH DEADLINES
decision problem belongs to NP, and every decision problem in NP reduces to it by a
polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), PARALLEL MACHINE SCHEDULING WITH DEADLINES.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.ParallelMachinesDeadlines.parallelMachinesDeadlines_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/ParallelMachinesDeadlinesWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/ParallelMachinesDeadlinesWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/parallel-machine-scheduling-with-deadlines/index.html#parallel-machines-deadlines-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Parallel machine scheduling with deadlines](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/parallel-machine-scheduling-with-deadlines/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/scheduling/parallel-machine-scheduling-with-deadlines)
