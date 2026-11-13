---
declaration: section
origin: cited
lean: Cslib.LTS.CanReach.trans, Cslib.Semantics.shiftSeq, Cslib.LTS.FiniteRun, Cslib.LTS.OmegaRun, Cslib.LTS.forall_state_of_invariant, Cslib.LTS.omegaExecution_of_omegaRun, Cslib.LTS.omegaRun_of_omegaExecution, Cslib.LTS.shiftSeq_eq_drop
statement: formalized
proof: formalized
---

# Labelled transition systems

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/labelled-transition-systems/index.html).

## Reachability in a labelled transition system is transitive

In a labelled transition
system, say that a state $s$ can reach a state $t$ when there is a finite list of labels along
which $s$ makes a multistep transition to $t$. If $s$ can reach $m$ and $m$ can reach $t$, then
$s$ can reach $t$.

The witnessing list of labels is the concatenation of the two given lists.

Formalized by `Cslib.LTS.CanReach.trans`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/Basic.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Semantics/LTS/Basic.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/labelled-transition-systems/index.html#trans).

## Shifted sequence

For a sequence $s_0, s_1, s_2, \dots$ and a natural number $k$, the shift
of the sequence by $k$ is the sequence whose $i$-th term is $s_{i+k}$; that is, the suffix
starting at index $k$, re-indexed from $0$.

Formalized by `Cslib.Semantics.shiftSeq`, a definition declared in [CSLibExt/Foundations/Semantics/LTS/OmegaRun.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Semantics/LTS/OmegaRun.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/labelled-transition-systems/index.html#shift-seq).

## Finite run

In a labelled transition system, a sequence of states $s_0, s_1, s_2, \dots$
is a finite run of length $k$ when for every $i < k$ there is a label $a$ such that there is a
transition from $s_i$ to $s_{i+1}$ labelled $a$.

The states after index $k$ are unconstrained.

Formalized by `Cslib.LTS.FiniteRun`, a definition declared in [CSLibExt/Foundations/Semantics/LTS/OmegaRun.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Semantics/LTS/OmegaRun.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/labelled-transition-systems/index.html#finite-run).

## Infinite run

In a labelled transition system, a sequence of states $s_0, s_1, s_2, \dots$
is an infinite run when for every $i$ there is a label $a$ such that there is a transition from
$s_i$ to $s_{i+1}$ labelled $a$.

Formalized by `Cslib.LTS.OmegaRun`, a definition declared in [CSLibExt/Foundations/Semantics/LTS/OmegaRun.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Semantics/LTS/OmegaRun.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/labelled-transition-systems/index.html#omega-run).

## Invariant principle for infinite runs

Let $P$ be a predicate on the states of a labelled
transition system such that, whenever $P(s)$ holds and there is a transition from $s$ to $t$ with
some label, $P(t)$ holds. Then for every infinite run $s_0, s_1, s_2, \dots$ with $P(s_0)$, the
predicate $P(s_k)$ holds for every $k$.

Formalized by `Cslib.LTS.forall_state_of_invariant`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/OmegaRun.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Semantics/LTS/OmegaRun.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/labelled-transition-systems/index.html#forall-state-of-invariant).

## Infinite state runs lift to labeled executions

Select a witnessing label at each step of an infinite state run.

Formalized by `Cslib.LTS.omegaExecution_of_omegaRun`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/OmegaExecution.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Semantics/LTS/OmegaExecution.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/labelled-transition-systems/index.html#omega-execution-of-omega-run).

## Labeled infinite executions give state runs

Forget the labels of a canonical infinite execution.

Formalized by `Cslib.LTS.omegaRun_of_omegaExecution`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/OmegaExecution.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Semantics/LTS/OmegaExecution.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/labelled-transition-systems/index.html#omega-run-of-omega-execution).

## Shifted function sequences agree with ω-sequence drop

Function-sequence suffixes agree with canonical `ωSequence.drop`.

Formalized by `Cslib.LTS.shiftSeq_eq_drop`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/OmegaExecution.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Foundations/Semantics/LTS/OmegaExecution.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/labelled-transition-systems/index.html#shift-seq-eq-drop).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Labelled transition systems](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/labelled-transition-systems/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/process-calculi/labelled-transition-systems)
