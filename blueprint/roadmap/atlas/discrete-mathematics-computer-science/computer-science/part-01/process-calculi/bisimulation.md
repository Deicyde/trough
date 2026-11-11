---
declaration: section
origin: cited
lean: Cslib.LTS.HomBisimilarity.mtr, Cslib.LTS.HomBisimilarity.hasOutLabel_iff, Cslib.LTS.HomBisimilarity.outgoingLabels_eq, Cslib.LTS.τSTr.of_tr, Cslib.LTS.τSTr.cons, Cslib.LTS.τSTr_iff_exists_mtr, Cslib.LTS.STr.iff_exists_of_ne, Cslib.LTS.τSTr.trans_sTr
statement: formalized
proof: formalized
---

# Bisimulation

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/bisimulation/index.html).

## Bisimilarity transfers multistep transitions

Let $s$ and $t$ be bisimilar states of a
labelled transition system, and suppose $s$ reaches a state $s'$ by a multistep transition along
a finite (possibly empty) list of labels $\mu_1, \dots, \mu_n$. Then there is a state $t'$ such
that $t$ reaches $t'$ by a multistep transition along the same list of labels, and $s'$ and $t'$
are bisimilar.

Formalized by `Cslib.LTS.HomBisimilarity.mtr`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/Bisimulation.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/Bisimulation.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/bisimulation/index.html#mtr).

## Bisimilar states enable the same labels

Let $s$ and $t$ be bisimilar states of a
labelled transition system. Then for every label $\mu$, $s$ has a transition labelled $\mu$ if
and only if $t$ has a transition labelled $\mu$.

Formalized by `Cslib.LTS.HomBisimilarity.hasOutLabel_iff`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/Bisimulation.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/Bisimulation.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/bisimulation/index.html#has-out-label-iff).

## Bisimilar states have equal sets of outgoing labels

Let $s$ and $t$ be bisimilar states
of a labelled transition system. Then the set of labels $\mu$ for which $s$ has a transition
labelled $\mu$ equals the set of labels $\mu$ for which $t$ has a transition labelled $\mu$.

Formalized by `Cslib.LTS.HomBisimilarity.outgoingLabels_eq`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/Bisimulation.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/Bisimulation.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/bisimulation/index.html#outgoing-labels-eq).

## A silent step lies in the silent closure

In a labelled transition system with a silent
label $\tau$, write $\Rightarrow$ for the silent closure, the reflexive-transitive closure of
the $\tau$-transition relation. If $s \xrightarrow{\tau} t$ is a transition, then
$s \Rightarrow t$.

Formalized by `Cslib.LTS.τSTr.of_tr`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/bisimulation/index.html#of-tr).

## Prepending a silent step to the silent closure

In a labelled transition system with a
silent label $\tau$, write $\Rightarrow$ for the silent closure, the reflexive-transitive
closure of the $\tau$-transition relation. If $s \xrightarrow{\tau} m$ is a transition and
$m \Rightarrow t$, then $s \Rightarrow t$.

Formalized by `Cslib.LTS.τSTr.cons`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/bisimulation/index.html#cons).

## The silent closure is made of runs of silent steps

In a labelled transition system
with a silent label $\tau$, write $\Rightarrow$ for the silent closure, the
reflexive-transitive closure of the $\tau$-transition relation. Then $s \Rightarrow t$ if and
only if, for some $n \in \mathbb{N}$, there is a multistep transition from $s$ to $t$ whose
list of labels consists of $n$ copies of $\tau$.

Formalized by `Cslib.LTS.τSTr_iff_exists_mtr`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/bisimulation/index.html#str-iff-exists-mtr).

## Weak transitions with a visible label

In a labelled transition system with a silent
label $\tau$, write $\Rightarrow$ for the reflexive-transitive closure of the
$\tau$-transition relation. A weak transition $s \stackrel{\mu}{\Longrightarrow} t$ is either
the trivial one $s \stackrel{\tau}{\Longrightarrow} s$ or a composite
$s \Rightarrow s_1 \xrightarrow{\mu} s_2 \Rightarrow t$. For a label $\mu \ne \tau$,
$s \stackrel{\mu}{\Longrightarrow} t$ holds if and only if there are states $s_1, s_2$ with
$s \Rightarrow s_1$, $s_1 \xrightarrow{\mu} s_2$ and $s_2 \Rightarrow t$.

Formalized by `Cslib.LTS.STr.iff_exists_of_ne`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/bisimulation/index.html#iff-exists-of-ne).

## Silent steps before a weak transition

Let $L$ be a labelled transition system with a
silent label $\tau$. A weak $\tau$-transition is a sequence of zero or more $\tau$-steps, and for
$\mu \ne \tau$ a weak $\mu$-transition is zero or more $\tau$-steps, one $\mu$-step and zero or
more $\tau$-steps. If a state $s$ reaches a state $m$ by zero or more $\tau$-steps and there is a
weak $\mu$-transition from $m$ to $t$, then there is a weak $\mu$-transition from $s$ to $t$.

Formalized by `Cslib.LTS.τSTr.trans_sTr`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/bisimulation/index.html#trans-s-tr).

## Silent steps after a weak transition

Let $L$ be a labelled transition system with a
silent label $\tau$. A weak $\tau$-transition is a sequence of zero or more $\tau$-steps, and for
$\mu \ne \tau$ a weak $\mu$-transition is zero or more $\tau$-steps, one $\mu$-step and zero or
more $\tau$-steps. If there is a weak $\mu$-transition from a state $s$ to a state $m$ and $m$
reaches a state $t$ by zero or more $\tau$-steps, then there is a weak $\mu$-transition from $s$
to $t$.

Formalized by `Cslib.LTS.STr.trans_τSTr`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/bisimulation/index.html#trans-str).

## Strong traces are weak traces

Let $L$ be a labelled transition system with a silent
label $\tau$. A weak $\tau$-transition is a sequence of zero or more $\tau$-steps, and for
$\mu \ne \tau$ a weak $\mu$-transition is zero or more $\tau$-steps, one $\mu$-step and zero or
more $\tau$-steps; the saturation of $L$ is the system on the same states whose
$\mu$-transitions are the weak $\mu$-transitions of $L$. If $L$ moves from a state $s$ to a
state $t$ by a sequence of transitions labelled $\mu_1, \dots, \mu_n$, then the saturation of
$L$ moves from $s$ to $t$ by a sequence of transitions with the same labels
$\mu_1, \dots, \mu_n$.

Formalized by `Cslib.LTS.MTr.to_saturate`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/bisimulation/index.html#to-saturate).

## Weak bisimilarity is bisimilarity of the saturated system

In a labelled transition
system with a silent label $\tau$, write $\Rightarrow$ for the reflexive-transitive
closure of the $\tau$-transition relation. The weak transitions
$s \stackrel{\mu}{\Longrightarrow} t$ are the trivial ones $s \stackrel{\tau}{\Longrightarrow} s$
and the composites $s \Rightarrow s_1 \xrightarrow{\mu} s_2 \Rightarrow t$; the saturated
system has the same states and has the weak transitions as its transitions. Two states are
weakly bisimilar if some bisimulation of the saturated system relates them.
Thus two states are weakly bisimilar if and only if they are bisimilar in the saturated
system; this holds by definition.

Formalized by `Cslib.LTS.HomWeakBisimilarity.iff_homBisimilarity_saturate`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/bisimulation/index.html#iff-hom-bisimilarity-saturate).

## Weak bisimilarity answers a strong step with a weak step

Let $L$ be a labelled
transition system with a silent label $\tau$. A weak $\tau$-transition is a sequence of zero or
more $\tau$-steps, and for $\mu \ne \tau$ a weak $\mu$-transition is zero or more $\tau$-steps,
one $\mu$-step and zero or more $\tau$-steps. Two states are weakly bisimilar when some
bisimulation of the system whose $\mu$-transitions are the weak $\mu$-transitions of $L$ relates
them. If $p$ and $q$ are weakly bisimilar and $L$ has a transition from $p$ to $p'$ labelled
$\mu$, then there is a state $q'$ with a weak $\mu$-transition from $q$ to $q'$ such that $p'$
and $q'$ are weakly bisimilar.

Formalized by `Cslib.LTS.HomWeakBisimilarity.tr`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/bisimulation/index.html#tr).

## Weak bisimilarity transfers weak transitions

In a labelled transition system with a
silent label $\tau$, write $\Rightarrow$ for the reflexive-transitive
closure of the $\tau$-transition relation. The weak transitions
$s \stackrel{\mu}{\Longrightarrow} t$ are the trivial ones $s \stackrel{\tau}{\Longrightarrow} s$
and the composites $s \Rightarrow s_1 \xrightarrow{\mu} s_2 \Rightarrow t$; the saturated
system has the same states and has the weak transitions as its transitions. Two states are
weakly bisimilar if some bisimulation of the saturated system relates them.
If $s$ and $t$ are weakly bisimilar and $s \stackrel{\mu}{\Longrightarrow} s'$, then there is a
state $t'$ with $t \stackrel{\mu}{\Longrightarrow} t'$ such that $s'$ and $t'$ are weakly
bisimilar.

Formalized by `Cslib.LTS.HomWeakBisimilarity.sTr`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/bisimulation/index.html#s-tr).

## Weak bisimilarity transfers weak traces

In a labelled transition system with a
silent label $\tau$, write $\Rightarrow$ for the reflexive-transitive
closure of the $\tau$-transition relation. The weak transitions
$s \stackrel{\mu}{\Longrightarrow} t$ are the trivial ones $s \stackrel{\tau}{\Longrightarrow} s$
and the composites $s \Rightarrow s_1 \xrightarrow{\mu} s_2 \Rightarrow t$; the saturated
system has the same states and has the weak transitions as its transitions. Two states are
weakly bisimilar if some bisimulation of the saturated system relates them.
Suppose $s$ and $t$ are weakly bisimilar and $s$ reaches $s'$ by a multistep transition of
the saturated system with label list $\mu_1, \dots, \mu_n$, that is, by weak transitions
$s \stackrel{\mu_1}{\Longrightarrow} \cdots \stackrel{\mu_n}{\Longrightarrow} s'$. Then $t$
reaches some $t'$ by a multistep transition of the saturated system with the same label list,
and $s'$ and $t'$ are weakly bisimilar.

Formalized by `Cslib.LTS.HomWeakBisimilarity.saturate_mtr`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/bisimulation/index.html#saturate-mtr).

## Strong bisimilarity implies weak bisimilarity

In a labelled transition system with a
silent label $\tau$, write $\Rightarrow$ for the reflexive-transitive
closure of the $\tau$-transition relation. The weak transitions
$s \stackrel{\mu}{\Longrightarrow} t$ are the trivial ones $s \stackrel{\tau}{\Longrightarrow} s$
and the composites $s \Rightarrow s_1 \xrightarrow{\mu} s_2 \Rightarrow t$; the saturated
system has the same states and has the weak transitions as its transitions. Two states are
weakly bisimilar if some bisimulation of the saturated system relates them.
If two states are bisimilar in the original system, then they are weakly bisimilar.

Formalized by `Cslib.LTS.HomBisimilarity.to_homWeakBisimilarity`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/bisimulation/index.html#to-hom-weak-bisimilarity).

## Weakly bisimilar states enable the same weak labels

In a labelled transition system
with a silent label $\tau$, write $\Rightarrow$ for the reflexive-transitive
closure of the $\tau$-transition relation. The weak transitions
$s \stackrel{\mu}{\Longrightarrow} t$ are the trivial ones $s \stackrel{\tau}{\Longrightarrow} s$
and the composites $s \Rightarrow s_1 \xrightarrow{\mu} s_2 \Rightarrow t$; the saturated
system has the same states and has the weak transitions as its transitions. Two states are
weakly bisimilar if some bisimulation of the saturated system relates them.
If $s$ and $t$ are weakly bisimilar, then for every label $\mu$, there is a weak transition
$s \stackrel{\mu}{\Longrightarrow} s'$ for some $s'$ if and only if there is a weak transition
$t \stackrel{\mu}{\Longrightarrow} t'$ for some $t'$.

Formalized by `Cslib.LTS.HomWeakBisimilarity.hasOutLabel_saturate_iff`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/bisimulation/index.html#has-out-label-saturate-iff).

## Weakly bisimilar states have the same set of weak labels

In a labelled transition
system with a silent label $\tau$, write $\Rightarrow$ for the reflexive-transitive
closure of the $\tau$-transition relation. The weak transitions
$s \stackrel{\mu}{\Longrightarrow} t$ are the trivial ones $s \stackrel{\tau}{\Longrightarrow} s$
and the composites $s \Rightarrow s_1 \xrightarrow{\mu} s_2 \Rightarrow t$; the saturated
system has the same states and has the weak transitions as its transitions. Two states are
weakly bisimilar if some bisimulation of the saturated system relates them.
If $s$ and $t$ are weakly bisimilar, then the set of labels $\mu$ with
$s \stackrel{\mu}{\Longrightarrow} s'$ for some $s'$ equals the set of labels $\mu$ with
$t \stackrel{\mu}{\Longrightarrow} t'$ for some $t'$.

Formalized by `Cslib.LTS.HomWeakBisimilarity.outgoingLabels_saturate_eq`, a theorem declared in [CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Semantics/LTS/WeakBisimulation.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/bisimulation/index.html#outgoing-labels-saturate-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bisimulation](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/bisimulation/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/process-calculi/bisimulation)
