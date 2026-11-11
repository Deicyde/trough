---
declaration: section
origin: cited
lean: Cslib.LTS.RootedWeakStep, Cslib.LTS.rootedWeakStep_of_tr, Cslib.LTS.RootedWeakStep.toSTr, Cslib.LTS.τSTr.rootedWeakStep_trans, Cslib.LTS.RootedWeakStep.trans_τSTr, Cslib.LTS.RootedWeakStep.trans_sTr, Cslib.LTS.RootedWeaklyBisimilar, Cslib.LTS.RootedWeaklyBisimilar.match_rootedLeft
statement: formalized
proof: formalized
---

# Observational congruence

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/observational-congruence/index.html).

## Rooted weak transition

In a labelled transition system whose labels include a silent
label $\tau$, there is a rooted weak transition from $s$ to $t$ with label $\mu$ when there are
states $s_1$ and $s_2$ such that $s$ reaches $s_1$ by zero or more $\tau$-transitions,
$s_1 \xrightarrow{\mu} s_2$ is a transition, and $s_2$ reaches $t$ by zero or more
$\tau$-transitions. In particular, a rooted weak transition with label $\tau$ contains at least
one actual $\tau$-transition.

Formalized by `Cslib.LTS.RootedWeakStep`, a definition declared in [CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/observational-congruence/index.html#rooted-weak-step).

## Transitions are rooted weak transitions

In a labelled transition system with a silent
label $\tau$, every transition $s \xrightarrow{\mu} t$ is a rooted weak transition from $s$ to $t$
with label $\mu$.

Formalized by `Cslib.LTS.rootedWeakStep_of_tr`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/observational-congruence/index.html#rooted-weak-step-of-tr).

## Rooted weak transitions are weak transitions

In a labelled transition system with a
silent label $\tau$, every rooted weak transition from $s$ to $t$ with label $\mu$ is a weak
transition from $s$ to $t$ with label $\mu$, where a weak transition with label $\mu$ is either
the trivial step from a state to itself with label $\tau$, or a transition with label $\mu$
preceded and followed by zero or more $\tau$-transitions.

Formalized by `Cslib.LTS.RootedWeakStep.toSTr`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/observational-congruence/index.html#to-str).

## Silent steps before a rooted weak transition

In a labelled transition system with a
silent label $\tau$, if $s$ reaches $m$ by zero or more $\tau$-transitions and there is a rooted
weak transition from $m$ to $t$ with label $\mu$, then there is a rooted weak transition from $s$
to $t$ with label $\mu$.

Formalized by `Cslib.LTS.τSTr.rootedWeakStep_trans`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/observational-congruence/index.html#rooted-weak-step-trans).

## Appending silent steps to a rooted weak transition

In a labelled transition system with
silent action $\tau$, if there is a rooted weak transition from $s$ to $m$ with label $a$, and $t$
is reachable from $m$ by zero or more $\tau$-transitions, then there is a rooted weak transition
from $s$ to $t$ with label $a$.

Formalized by `Cslib.LTS.RootedWeakStep.trans_τSTr`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/observational-congruence/index.html#trans-str).

## A rooted silent step followed by a weak transition is rooted

In a labelled transition
system with a silent label $\tau$, if there is a rooted weak transition from $s$ to $m$ with
label $\tau$ and a weak transition from $m$ to $t$ with label $\mu$, then there is a rooted weak
transition from $s$ to $t$ with label $\mu$. Here a weak transition with label $\mu$ is either
the trivial step from a state to itself with label $\tau$, or a transition with label $\mu$
preceded and followed by zero or more $\tau$-transitions.

The initial rooted transition supplies the required actual silent step even when the following
weak transition is reflexive.

Formalized by `Cslib.LTS.RootedWeakStep.trans_sTr`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/observational-congruence/index.html#trans-s-tr).

## Rooted observation congruence

In a labelled transition system with a silent label
$\tau$, states $p$ and $q$ are rooted weakly bisimilar (observation congruent) when every
transition $p \xrightarrow{\mu} p'$ is matched by a rooted weak transition from $q$ to some $q'$
with label $\mu$ such that $p'$ and $q'$ are weakly bisimilar, and every transition
$q \xrightarrow{\mu} q'$ is matched by a rooted weak transition from $p$ to some $p'$ with label
$\mu$ such that $p'$ and $q'$ are weakly bisimilar.

Formalized by `Cslib.LTS.RootedWeaklyBisimilar`, a definition declared in [CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/observational-congruence/index.html#rooted-weakly-bisimilar).

## Observation congruence matches rooted weak transitions

In a labelled transition system
with a silent label $\tau$, if $p$ and $q$ are rooted weakly bisimilar and there is a rooted weak
transition from $p$ to $p'$ with label $\mu$, then there is a state $q'$ with a rooted weak
transition from $q$ to $q'$ with label $\mu$ such that $p'$ and $q'$ are weakly bisimilar.

Formalized by `Cslib.LTS.RootedWeaklyBisimilar.match_rootedLeft`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/observational-congruence/index.html#match-rooted-left).

## Transitivity of rooted observational congruence

In a labelled transition system with
silent action $\tau$, if $p$ is rooted observationally congruent to $q$ and $q$ is rooted
observationally congruent to $r$, then $p$ is rooted observationally congruent to $r$.

Formalized by `Cslib.LTS.RootedWeaklyBisimilar.trans`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/observational-congruence/index.html#trans).

## Observation congruence is an equivalence relation

In every labelled transition system
with a silent label $\tau$, rooted weak bisimilarity (observation congruence) is reflexive,
symmetric and transitive.

Formalized by `Cslib.LTS.observationCongruent_equivalence`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/observational-congruence/index.html#observation-congruent-equivalence).

## Strong bisimilarity implies observation congruence

In a labelled transition system with
a silent label $\tau$, any two strongly bisimilar states are rooted weakly bisimilar.

Formalized by `Cslib.LTS.observationCongruent_of_bisimilar`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/observational-congruence/index.html#observation-congruent-of-bisimilar).

## Observation congruence implies weak bisimilarity

In a labelled transition system with
a silent label $\tau$, any two rooted weakly bisimilar states are weakly bisimilar.

Formalized by `Cslib.LTS.RootedWeaklyBisimilar.to_homWeakBisimilarity`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/ObservationCongruence.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/observational-congruence/index.html#to-hom-weak-bisimilarity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Observational congruence](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/observational-congruence/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/process-calculi/observational-congruence)
