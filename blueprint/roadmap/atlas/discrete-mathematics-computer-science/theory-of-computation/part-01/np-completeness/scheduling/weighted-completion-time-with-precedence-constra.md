---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.PrecedenceWeightedCompletion.PrecedenceWeightedCompletionInstance, MetaMathlibExt.Complexity.NPComplete.PrecedenceWeightedCompletion.WeightedCompletionStep, MetaMathlibExt.Complexity.NPComplete.PrecedenceWeightedCompletion.WeightedCompletion, MetaMathlibExt.Complexity.NPComplete.PrecedenceWeightedCompletion.WellFormed, MetaMathlibExt.Complexity.NPComplete.PrecedenceWeightedCompletion.PrecedenceWeightedCompletionFeasible, MetaMathlibExt.Complexity.NPComplete.PrecedenceWeightedCompletion.precedenceWeightedCompletionDec, MetaMathlibExt.Complexity.NPComplete.PrecedenceWeightedCompletion.precedenceWeightedCompletion_npComplete
statement: formalized
---

# Weighted completion time with precedence constraints

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/weighted-completion-time-with-precedence-constra/index.html).

## Instances of single-machine weighted completion with precedence

An instance of the
scheduling problem $1 \mid \mathrm{prec} \mid \sum w_j C_j$ (one machine, precedence constraints,
objective the sum over jobs $j$ of the weight $w_j$ times the completion time $C_j$) is a triple
$(J, P, K)$: a list $J$ of jobs, each a pair $(p, w)$ of natural numbers giving its processing
time and weight; a list $P$ of pairs of natural numbers, read as precedence constraints between
job indices; and a natural number bound $K$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PrecedenceWeightedCompletion.PrecedenceWeightedCompletionInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/PrecedenceWeightedCompletionWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/PrecedenceWeightedCompletionWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/weighted-completion-time-with-precedence-constra/index.html#precedence-weighted-completion-instance).

## One step of the weighted completion time computation

Let $J$ be a list of jobs, each a
pair (processing time, weight), let $(t, s)$ be a state consisting of the elapsed time $t$ and the
accumulated weighted completion time $s$, and let $j$ be a job index. With $(p, w)$ the job at
position $j$ of $J$ counting from $0$, or $(0, 0)$ if $J$ has no such position, the step sends
$(t, s)$ to $(t + p, s + w (t + p))$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PrecedenceWeightedCompletion.WeightedCompletionStep`, a definition declared in [WantedExt/Complexity/NPComplete/PrecedenceWeightedCompletionWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/PrecedenceWeightedCompletionWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/weighted-completion-time-with-precedence-constra/index.html#weighted-completion-step).

## Total weighted completion time of a job order

Let $J$ be a list of jobs, each a pair
$(p_i, w_i)$ of processing time and weight indexed from $0$, with $(p_i, w_i) = (0, 0)$ for $i$
outside the list. For a list $j_1, \dots, j_m$ of job indices, the total weighted completion time
is $\sum_{k=1}^{m} w_{j_k} C_k$, where $C_k = p_{j_1} + \dots + p_{j_k}$ is the completion time of
the $k$-th job in the order.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PrecedenceWeightedCompletion.WeightedCompletion`, a definition declared in [WantedExt/Complexity/NPComplete/PrecedenceWeightedCompletionWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/PrecedenceWeightedCompletionWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/weighted-completion-time-with-precedence-constra/index.html#weighted-completion).

## Well-formed weighted completion instances

An instance $(J, P, K)$ whose job list $J$ has
$n$ jobs is well formed when every precedence pair $(a, b)$ in $P$ satisfies $a < n$, $b < n$ and
$a \ne b$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PrecedenceWeightedCompletion.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/PrecedenceWeightedCompletionWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/PrecedenceWeightedCompletionWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/weighted-completion-time-with-precedence-constra/index.html#well-formed).

## Feasible weighted completion instances

Let $(J, P, K)$ be an instance whose job list $J$
consists of $n$ jobs $(p_0, w_0), \dots, (p_{n-1}, w_{n-1})$ (processing time, weight). It is
feasible when there is an ordering $j_1, \dots, j_n$ of the indices $0, \dots, n-1$, each listed
exactly once, such that for every pair $(a, b)$ in $P$ the position of $a$ in the ordering is
smaller than the position of $b$, where an index that does not occur gets position $n + 1$, and
$\sum_{k=1}^{n} w_{j_k} (p_{j_1} + \dots + p_{j_k}) \le K$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PrecedenceWeightedCompletion.PrecedenceWeightedCompletionFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/PrecedenceWeightedCompletionWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/PrecedenceWeightedCompletionWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/weighted-completion-time-with-precedence-constra/index.html#precedence-weighted-completion-feasible).

## SINGLE-MACHINE WEIGHTED COMPLETION WITH PRECEDENCE as a decision problem

The decision
problem accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding,
to an instance $(J, P, K)$ that is well formed and feasible: every precedence pair in $P$ consists
of two distinct job indices of $J$, and some ordering of all the jobs that puts the first job of
every precedence pair before the second has total weighted completion time at most $K$.
Bitstrings that do not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.PrecedenceWeightedCompletion.precedenceWeightedCompletionDec`, a definition declared in [WantedExt/Complexity/NPComplete/PrecedenceWeightedCompletionWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/PrecedenceWeightedCompletionWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/weighted-completion-time-with-precedence-constra/index.html#precedence-weighted-completion-dec).

## SINGLE-MACHINE WEIGHTED COMPLETION WITH PRECEDENCE is NP-complete

The decision problem
SINGLE-MACHINE WEIGHTED COMPLETION WITH PRECEDENCE on bitstrings belongs to NP, and every
decision problem in NP reduces to it by a polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), 1|prec|sum w_j C_j; E. L. Lawler, "Sequencing jobs to minimize total weighted completion time subject to precedence constraints", Annals of Discrete Mathematics 2 (1978), 75-90; J. K. Lenstra and A. H. G. Rinnooy Kan, "Complexity of scheduling under precedence constraints", Operations Research 26 (1978), 22-35.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.PrecedenceWeightedCompletion.precedenceWeightedCompletion_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/PrecedenceWeightedCompletionWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/PrecedenceWeightedCompletionWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/weighted-completion-time-with-precedence-constra/index.html#precedence-weighted-completion-np-comple).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weighted completion time with precedence constraints](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/scheduling/weighted-completion-time-with-precedence-constra/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/scheduling/weighted-completion-time-with-precedence-constra)
