---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.TotalTardiness.TotalTardinessInstance, MetaMathlibExt.Complexity.NPComplete.TotalTardiness.TardinessStep, MetaMathlibExt.Complexity.NPComplete.TotalTardiness.TotalTardinessValue, MetaMathlibExt.Complexity.NPComplete.TotalTardiness.TotalTardinessFeasible, MetaMathlibExt.Complexity.NPComplete.TotalTardiness.totalTardinessDec, MetaMathlibExt.Complexity.NPComplete.TotalTardiness.totalTardiness_npComplete
statement: formalized
---

# Total tardiness scheduling

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/total-tardiness-scheduling/index.html).

## Instances of TOTAL TARDINESS

An instance of TOTAL TARDINESS is a pair $(J, K)$ consisting
of a finite list $J = ((p_0, d_0), \dots, (p_{n-1}, d_{n-1}))$ of jobs, where job $j$ has
processing time $p_j \in \mathbb{N}$ and due date $d_j \in \mathbb{N}$, and a bound
$K \in \mathbb{N}$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.TotalTardiness.TotalTardinessInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/TotalTardinessWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/TotalTardinessWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/total-tardiness-scheduling/index.html#total-tardiness-instance).

## One step of the tardiness computation

Let $J = ((p_0, d_0), \dots, (p_{n-1}, d_{n-1}))$
be a list of jobs with processing times $p_i \in \mathbb{N}$ and due dates $d_i \in \mathbb{N}$,
let $j \in \mathbb{N}$, and let $(p, d) = (p_j, d_j)$ if $j < n$ and $(p, d) = (0, 0)$ otherwise.
Running job $j$ from the state $(t, s) \in \mathbb{N} \times \mathbb{N}$, where $t$ is the elapsed
time and $s$ the accumulated tardiness, gives the state $(t + p, \, s + \max(t + p - d, 0))$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.TotalTardiness.TardinessStep`, a definition declared in [WantedExt/Complexity/NPComplete/TotalTardinessWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/TotalTardinessWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/total-tardiness-scheduling/index.html#tardiness-step).

## Total tardiness of a job order

Let $J = ((p_0, d_0), \dots, (p_{n-1}, d_{n-1}))$ be a
list of jobs with processing times $p_i \in \mathbb{N}$ and due dates $d_i \in \mathbb{N}$, and
set $(p_i, d_i) = (0, 0)$ for $i \ge n$. For a list $(j_1, \dots, j_m)$ of natural numbers (job
indices), let $C_k = p_{j_1} + \dots + p_{j_k}$ be the completion time of the $k$-th job when the
jobs are run in this order. The total tardiness of the order is
$\sum_{k=1}^{m} \max(C_k - d_{j_k}, 0)$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.TotalTardiness.TotalTardinessValue`, a definition declared in [WantedExt/Complexity/NPComplete/TotalTardinessWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/TotalTardinessWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/total-tardiness-scheduling/index.html#total-tardiness-value).

## Feasible TOTAL TARDINESS instances

An instance $(J, K)$ of TOTAL TARDINESS with $n$ jobs
is feasible when some ordering of its jobs, that is, some permutation $(j_1, \dots, j_n)$ of
$(0, 1, \dots, n - 1)$, has total tardiness at most $K$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.TotalTardiness.TotalTardinessFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/TotalTardinessWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/TotalTardinessWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/total-tardiness-scheduling/index.html#total-tardiness-feasible).

## The TOTAL TARDINESS decision problem

The decision problem TOTAL TARDINESS accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding (natural numbers in
binary), to an instance of TOTAL TARDINESS that is feasible, that is, whose jobs admit an ordering
of total tardiness at most its bound. It rejects every bitstring that does not decode to an
instance.

Formalized by `MetaMathlibExt.Complexity.NPComplete.TotalTardiness.totalTardinessDec`, a definition declared in [WantedExt/Complexity/NPComplete/TotalTardinessWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/TotalTardinessWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/total-tardiness-scheduling/index.html#total-tardiness-dec).

## TOTAL TARDINESS is NP-complete

The TOTAL TARDINESS decision problem belongs to NP, and
every decision problem in NP reduces to it by a polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), TOTAL TARDINESS (1||sum T_j); J. Du and J. Y.-T. Leung, "Minimizing total tardiness on one machine is NP-hard" (1990).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.TotalTardiness.totalTardiness_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/TotalTardinessWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/TotalTardinessWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/total-tardiness-scheduling/index.html#total-tardiness-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Total tardiness scheduling](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/total-tardiness-scheduling/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/scheduling/total-tardiness-scheduling)
