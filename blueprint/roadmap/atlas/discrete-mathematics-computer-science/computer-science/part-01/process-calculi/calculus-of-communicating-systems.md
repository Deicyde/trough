---
declaration: section
origin: cited
lean: Cslib.CCS.Process, Cslib.CCS.Process.RawStep, Cslib.CCS.Process.Step, Cslib.CCS.Process.lts, Cslib.CCS.Process.ChoiceLift, Cslib.CCS.Process.prefix_congr, Cslib.CCS.Process.EquationClosure, Cslib.CCS.Label
statement: formalized
proof: formalized
---

# Calculus of communicating systems

48 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html).

## Finite CCS processes

For a type $A$ of actions, the finite CCS processes over $A$ are
built from the inactive process $\mathbf{0}$ by action prefix $a.P$ (an action $a \in A$
followed by a process $P$), nondeterministic choice $P + Q$, and parallel composition
$P \mid Q$.

Formalized by `Cslib.CCS.Process`, an inductive type declared in [CSLibExt/Languages/CCS/Choice.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Choice.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#process).

## Operational semantics of finite CCS with a synchronization function

Let $\sigma$ be a
partial function that assigns to some pairs of actions $(a, b)$ an action $\sigma(a, b)$. The
transition relation $P \xrightarrow{a} P'$ on finite CCS processes (built from prefix $a.P$,
choice $P + Q$ and parallel composition $P \mid Q$) determined by $\sigma$ is the least relation
such that $a.P \xrightarrow{a} P$; if $P \xrightarrow{a} P'$ then $P + Q \xrightarrow{a} P'$,
$Q + P \xrightarrow{a} P'$, $P \mid Q \xrightarrow{a} P' \mid Q$ and
$Q \mid P \xrightarrow{a} Q \mid P'$; and if $P \xrightarrow{a} P'$, $Q \xrightarrow{b} Q'$ and
$\sigma(a, b) = c$, then $P \mid Q \xrightarrow{c} P' \mid Q'$.

Formalized by `Cslib.CCS.Process.RawStep`, an inductive type declared in [CSLibExt/Languages/CCS/Choice.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Choice.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#raw-step).

## Transitions of finite CCS without communication

The transition relation
$P \xrightarrow{a} P'$ on finite CCS processes is the operational semantics of finite CCS whose
synchronization function is undefined on every pair of actions. Thus prefix and choice move as
usual, and a parallel composition $P \mid Q$ moves only by letting one of $P$ and $Q$ move;
there are no communication steps.

Formalized by `Cslib.CCS.Process.Step`, an abbreviation declared in [CSLibExt/Languages/CCS/Choice.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Choice.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#step).

## Labelled transition system of finite CCS

The labelled transition system whose states are
the finite CCS processes, whose labels are the actions, and whose transitions $P \xrightarrow{a} P'$
are those of the communication-free operational semantics of finite CCS.

Formalized by `Cslib.CCS.Process.lts`, a definition declared in [CSLibExt/Languages/CCS/Choice.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Choice.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#lts).

## Lifting relations through choice

Given relations $R$ and $S$ on finite CCS processes,
write $P_1 + P_2$ for the nondeterministic choice of $P_1$ and $P_2$. The choice lift of $R$
and $S$ relates $P$ to $Q$ exactly when $R(P, Q)$ holds, or $S(P, Q)$ holds, or $P = P_1 + P_2$
and $Q = Q_1 + Q_2$ with $R(P_1, Q_1)$ and $S(P_2, Q_2)$.

Formalized by `Cslib.CCS.Process.ChoiceLift`, an inductive type declared in [CSLibExt/Languages/CCS/Choice.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Choice.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#choice-lift).

## Prefix preserves strong bisimilarity

For every action $a$ and all finite CCS processes
$P$ and $Q$, if $P$ and $Q$ are strongly bisimilar in the labelled transition system of finite
CCS, then the prefixed processes $a.P$ and $a.Q$ are strongly bisimilar there as well.

Formalized by `Cslib.CCS.Process.prefix_congr`, a theorem declared in [CSLibExt/Languages/CCS/Choice.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Choice.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#prefix-congr).

## Reflexive closure of a relation on processes

Given a relation $E$ on finite CCS processes,
its equation closure relates $P$ to $Q$ exactly when $P = Q$ or $E(P, Q)$; that is, it is the
reflexive closure of $E$.

It is used to prove the algebraic laws of nondeterministic choice up to strong bisimilarity.

Formalized by `Cslib.CCS.Process.EquationClosure`, a definition declared in [CSLibExt/Languages/CCS/Choice.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Choice.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#equation-closure).

## CCS labels

For a set of names, a CCS label is either the silent action $\tau$, the input
on a name $a$, or the output on a name $a$.

Formalized by `Cslib.CCS.Label`, an inductive type declared in [CSLibExt/Languages/CCS/Parallel.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Parallel.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#label).

## Complementary labels

Two CCS labels are complementary when one is the input on a name $a$
and the other is the output on the same name $a$, in either order. No other pair of labels is
complementary; in particular the silent label $\tau$ has no complement.

Formalized by `Cslib.CCS.Label.Complementary`, a definition declared in [CSLibExt/Languages/CCS/Parallel.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Parallel.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#complementary).

## Synchronization of CCS labels

Let the names form a type with decidable equality. For
labels $a$ and $b$, the synchronization of $a$ with $b$ is the silent action $\tau$ when $a$ is
the input on a name $n$ and $b$ is the output on the same name $n$, or when $a$ is the output on
$n$ and $b$ is the input on $n$. For every other pair of labels, including any pair involving
$\tau$, there is no result.

This partial function supplies the communication rule of the CCS operational semantics.

Formalized by `Cslib.CCS.Label.synchronize`, a definition declared in [CSLibExt/Languages/CCS/Parallel.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Parallel.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#synchronize).

## CCS transition relation with communication

The transition relation on CCS processes with
labels over a set of names given by the raw step relation for the synchronization function under
which an input and an output on the same name, in either order, synchronize to the silent label
$\tau$, and no other pair of labels synchronizes.

Formalized by `Cslib.CCS.Process.CommunicationStep`, an abbreviation declared in [CSLibExt/Languages/CCS/Parallel.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Parallel.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#communication-step).

## Labelled transition system of CCS with communication

The labelled transition system whose
states are CCS processes with labels over a set of names, whose labels are CCS labels over those
names, and whose transition relation is the CCS transition relation with communication.

Formalized by `Cslib.CCS.Process.communicationLTS`, a definition declared in [CSLibExt/Languages/CCS/Parallel.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Parallel.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#communication-lts).

## Transitions of a parallel composition

For CCS processes $P$, $Q$, $R$ and a CCS label $a$,
the parallel composition $P \mid Q$ has a transition labelled $a$ to $R$ in the CCS transition
relation with communication if and only if one of the following holds: $P$ has a transition
labelled $a$ to some $P'$ and $R = P' \mid Q$; or $Q$ has a transition labelled $a$ to some $Q'$
and $R = P \mid Q'$; or $a = \tau$ and there are processes $P'$, $Q'$ and complementary labels
$b$, $c$ such that $P$ has a transition labelled $b$ to $P'$, $Q$ has a transition labelled $c$
to $Q'$, and $R = P' \mid Q'$.

Formalized by `Cslib.CCS.Process.communication_parallel_step_iff`, a theorem declared in [CSLibExt/Languages/CCS/Parallel.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Parallel.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#communication-parallel-step-iff).

## Parallel lift of two relations

Given two relations $R$ and $S$ on CCS processes with
labels over a set of names, their parallel lift relates a process $U$ to a process $V$ exactly
when $R$ relates $U$ to $V$, or $S$ relates $U$ to $V$, or $U = P_1 \mid Q_1$ and
$V = P_2 \mid Q_2$ where $R$ relates $P_1$ to $P_2$ and $S$ relates $Q_1$ to $Q_2$.

Formalized by `Cslib.CCS.Process.ParallelLift`, an inductive type declared in [CSLibExt/Languages/CCS/Parallel.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Parallel.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#parallel-lift).

## Parallel composition preserves strong bisimilarity

For CCS processes $P_1$, $P_2$, $Q_1$,
$Q_2$ with labels over a set of names: if $P_1$ and $P_2$ are strongly bisimilar and $Q_1$ and
$Q_2$ are strongly bisimilar in the labelled transition system of CCS with communication, then
the parallel compositions $P_1 \mid Q_1$ and $P_2 \mid Q_2$ are strongly bisimilar there.

Formalized by `Cslib.CCS.Process.parallel_congr`, a theorem declared in [CSLibExt/Languages/CCS/Parallel.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Parallel.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#parallel-congr).

## Prefix preserves strong bisimilarity in CCS with communication

For every CCS label $a$ and
all CCS processes $P$ and $Q$: if $P$ and $Q$ are strongly bisimilar in the labelled transition
system of CCS with communication, then so are the prefixed processes $a.P$ and $a.Q$.

Formalized by `Cslib.CCS.Process.communication_prefix_congr`, a theorem declared in [CSLibExt/Languages/CCS/Parallel.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Parallel.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#communication-prefix-congr).

## Choice preserves strong bisimilarity in CCS with communication

For CCS processes $P_1$,
$P_2$, $Q_1$, $Q_2$ with labels over a set of names: if $P_1$ and $P_2$ are strongly bisimilar and
$Q_1$ and $Q_2$ are strongly bisimilar in the labelled transition system of CCS with
communication, then the choices $P_1 + Q_1$ and $P_2 + Q_2$ are strongly bisimilar there.

Formalized by `Cslib.CCS.Process.communication_choice_congr`, a theorem declared in [CSLibExt/Languages/CCS/Parallel.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Parallel.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#communication-choice-congr).

## Parallel composition is commutative up to strong bisimilarity

For all CCS processes $P$
and $Q$ with labels over a set of names, $P \mid Q$ and $Q \mid P$ are strongly bisimilar in the
labelled transition system of CCS with communication.

Formalized by `Cslib.CCS.Process.parallel_comm`, a theorem declared in [CSLibExt/Languages/CCS/Parallel.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Parallel.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#parallel-comm).

## The inactive process is a left unit for parallel composition

Let the names form a type
with decidable equality. For every CCS process $P$ over input, output and silent labels on these
names, the parallel composition $0 \mid P$ of the inactive process $0$ with $P$ is strongly
bisimilar to $P$ in the communication labelled transition system.

Formalized by `Cslib.CCS.Process.parallel_nil_left`, a theorem declared in [CSLibExt/Languages/CCS/Parallel.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Parallel.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#parallel-nil-left).

## The inactive process is a right unit for parallel composition

Let the names form a type
with decidable equality. For every CCS process $P$ over input, output and silent labels on these
names, the parallel composition $P \mid 0$ of $P$ with the inactive process $0$ is strongly
bisimilar to $P$ in the communication labelled transition system.

Formalized by `Cslib.CCS.Process.parallel_nil_right`, a theorem declared in [CSLibExt/Languages/CCS/Parallel.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Parallel.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#parallel-nil-right).

## Visible CCS label

A visible CCS label, excluding the silent action.

Formalized by `Cslib.CCS.VisibleLabel`, an inductive type declared in [CSLibExt/Languages/CCS/StaticOperators.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/StaticOperators.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#visible-label).

## Complement of a visible label

The complement of the input label on a channel $a$ is the
output label on $a$, and the complement of the output label on $a$ is the input label on $a$.

Formalized by `Cslib.CCS.VisibleLabel.complement`, a definition declared in [CSLibExt/Languages/CCS/StaticOperators.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/StaticOperators.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#complement).

## Visible labels as CCS labels

The inclusion of visible labels into CCS labels sends the
input on a channel $a$ to the input on $a$, and the output on $a$ to the output on $a$.

Formalized by `Cslib.CCS.VisibleLabel.toLabel`, a definition declared in [CSLibExt/Languages/CCS/StaticOperators.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/StaticOperators.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#to-label).

## Relabelling

A finite CCS relabelling over channel names is a finite list of entries
$(a, \ell)$, each pairing a channel name $a$ with a visible label $\ell$, that is, an input or an
output on some channel. The entry $(a, \ell)$ gives $\ell$ as the image of the input on $a$; the
image of the output on $a$ is then the complement of $\ell$. The first entry with name $a$ is
used, and a name occurring in no entry is mapped to itself.

Formalized by `Cslib.CCS.Relabelling`, a structure declared in [CSLibExt/Languages/CCS/StaticOperators.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/StaticOperators.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#relabelling).

## Applying a relabelling to a channel name

Let $f$ be a finite relabelling whose table lists
the entries $(a_1, \ell_1), \dots, (a_k, \ell_k)$, where each $a_i$ is a channel name and each
$\ell_i$ a visible label. The image of a channel name $a$ under $f$ is $\ell_i$ for the first index
$i$ with $a_i = a$, and the input label on $a$ when no entry has name $a$.

Formalized by `Cslib.CCS.Relabelling.apply`, a definition declared in [CSLibExt/Languages/CCS/StaticOperators.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/StaticOperators.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#apply).

## Static CCS processes

Finite CCS processes with the static operators, over a type of
channel names, are built from the inactive process $0$ by the prefix $\alpha.P$ of a CCS action
$\alpha$ (silent, an input or an output) and a process $P$, the choice $P + Q$, the parallel
composition $P \mid Q$, the restriction $P \setminus L$ of $P$ by a finite list $L$ of names, and
the relabelling $P[f]$ of $P$ by a finite relabelling $f$.

Unlike function-valued operators, finite lists and tables preserve decidable
equality of processes and cannot express relabellings that alter the silent action $\tau$ or fail
to preserve complementary visible actions.

Formalized by `Cslib.CCS.StaticProcess`, an inductive type declared in [CSLibExt/Languages/CCS/StaticOperators.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/StaticOperators.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#static-process).

## Embedding finite CCS into CCS with static operators

Each finite CCS process over CCS
labels is sent to the process with static operators of the same shape: the inactive process goes
to the inactive process, the prefix of an action $\alpha$ to a process $P$ goes to the prefix of
$\alpha$ to the image of $P$, and a choice or a parallel composition of $P$ and $Q$ goes to the
choice or the parallel composition of the images of $P$ and $Q$.

Formalized by `Cslib.CCS.StaticProcess.ofProcess`, a definition declared in [CSLibExt/Languages/CCS/StaticOperators.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/StaticOperators.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#of-process).

## Relabelling an action

For a relabelling $f$, the silent action $\tau$ is relabelled to
$\tau$, an input on a channel $a$ is relabelled to the image of $a$ under $f$, and an output on
$a$ is relabelled to the complement of the image of $a$ under $f$, each viewed as a CCS label.

Formalized by `Cslib.CCS.StaticProcess.relabelAction`, a definition declared in [CSLibExt/Languages/CCS/StaticOperators.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/StaticOperators.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#relabel-action).

## Relabelling preserves complementary actions

For every relabelling $f$ and all CCS labels
$\alpha$ and $\beta$, if $\alpha$ and $\beta$ are complementary, then the actions obtained by
relabelling $\alpha$ and $\beta$ with $f$ are complementary.

Formalized by `Cslib.CCS.StaticProcess.relabelAction_complementary`, a theorem declared in [CSLibExt/Languages/CCS/StaticOperators.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/StaticOperators.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#relabel-action-complementary).

## Actions permitted by a restriction

Given a finite list $L$ of blocked channel names, the
silent action $\tau$ is always permitted, and an input or an output on a channel $a$ is permitted
exactly when $a \notin L$.

Formalized by `Cslib.CCS.StaticProcess.Allowed`, a definition declared in [CSLibExt/Languages/CCS/StaticOperators.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/StaticOperators.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#allowed).

## Transitions of static CCS

The labelled transition relation $P \xrightarrow{\alpha} P'$ on
static CCS processes, with actions $\alpha$ the CCS labels (silent $\tau$, inputs and outputs), is
the least relation closed under the following rules, where $\alpha.P$ is the prefix, $P + Q$ the
choice, $P \mid Q$ the parallel composition, $P \setminus L$ the restriction of $P$ by a finite
list $L$ of channel names, and $P[f]$ the relabelling of $P$ by a finite relabelling $f$. The
prefix has the transition $\alpha.P \xrightarrow{\alpha} P$. If $P \xrightarrow{\alpha} P'$, then
$P + Q \xrightarrow{\alpha} P'$, $Q + P \xrightarrow{\alpha} P'$,
$P \mid Q \xrightarrow{\alpha} P' \mid Q$ and $Q \mid P \xrightarrow{\alpha} Q \mid P'$. If
$P \xrightarrow{\alpha} P'$ and $Q \xrightarrow{\beta} Q'$ where $\alpha$ and $\beta$ are
complementary (an input and an output on the same channel), then
$P \mid Q \xrightarrow{\tau} P' \mid Q'$. If $P \xrightarrow{\alpha} P'$ and $\alpha$ is $\tau$ or
its channel is not in $L$, then $P \setminus L \xrightarrow{\alpha} P' \setminus L$. If
$P \xrightarrow{\alpha} P'$, then $P[f] \xrightarrow{f(\alpha)} P'[f]$, where $f(\tau) = \tau$, an
input on a channel $a$ is sent to the visible label $f(a)$ that $f$ assigns to $a$, and an output
on $a$ is sent to the complement of $f(a)$.

Formalized by `Cslib.CCS.StaticProcess.Step`, an inductive type declared in [CSLibExt/Languages/CCS/StaticOperators.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/StaticOperators.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#step-3).

## Transition system of CCS with restriction and relabelling

The labelled transition system
of finite CCS with static operators has the finite CCS processes with restriction and relabelling
as states and the CCS labels as labels, and its transitions are the steps of the structural
operational semantics of these processes.

Formalized by `Cslib.CCS.StaticProcess.lts`, a definition declared in [CSLibExt/Languages/CCS/StaticOperators.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/StaticOperators.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#lts-3).

## Lifting a relation through a restriction

Given a finite list $L$ of channel names and a
relation $R$ on static CCS processes, the lifted relation relates $P$ to $Q$ exactly when either
$R$ relates $P$ to $Q$, or $P = P' \setminus L$ and $Q = Q' \setminus L$ for some processes $P'$
and $Q'$ that $R$ relates.

Formalized by `Cslib.CCS.StaticProcess.RestrictionLift`, an inductive type declared in [CSLibExt/Languages/CCS/StaticOperators.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/StaticOperators.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#restriction-lift).

## Restriction preserves strong bisimilarity

For every finite list $L$ of channel names and
all static CCS processes $P$ and $Q$, if $P$ and $Q$ are strongly bisimilar in the labelled
transition system of finite CCS with static operators, then so are the restricted processes
$P \setminus L$ and $Q \setminus L$.

Formalized by `Cslib.CCS.StaticProcess.restriction_congr`, a theorem declared in [CSLibExt/Languages/CCS/StaticOperators.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/StaticOperators.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#restriction-congr).

## Closure of a relation under one relabelling

Given a relabelling $f$ and a relation $R$
on finite CCS processes with static operators, the lifted relation is the least relation that
relates $P$ to $Q$ and relates the relabelling of $P$ by $f$ to the relabelling of $Q$ by $f$
whenever $R$ relates $P$ to $Q$.

Formalized by `Cslib.CCS.StaticProcess.RelabellingLift`, an inductive type declared in [CSLibExt/Languages/CCS/StaticOperators.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/StaticOperators.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#relabelling-lift).

## Relabelling preserves strong bisimilarity

For every relabelling $f$ and all finite CCS
processes $P$ and $Q$ with static operators, if $P$ and $Q$ are strongly bisimilar in the
labelled transition system of finite CCS with static operators, then the relabellings of $P$
and of $Q$ by $f$ are strongly bisimilar there.

Formalized by `Cslib.CCS.StaticProcess.relabelling_congr`, a theorem declared in [CSLibExt/Languages/CCS/StaticOperators.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/StaticOperators.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#relabelling-congr).

## Recursive CCS processes

Given a set of names and a set of process constants, the
recursive CCS processes are generated by the following constructors: the inactive process
$\mathbf{0}$; a process constant $A$; a prefix $\alpha.P$ for a CCS label $\alpha$ and a
process $P$; a choice $P + Q$; a parallel composition $P \mid Q$; a restriction
$P \setminus L$ for a finite list $L$ of names; and a relabelling $P[f]$ for a CCS
relabelling $f$.

Formalized by `Cslib.CCS.Recursive.Process`, an inductive type declared in [CSLibExt/Languages/CCS/Recursion.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Recursion.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#process-2).

## Recursive CCS specification

Given a type of channel names and a type of process constants,
a recursive specification assigns to each process constant $A$ a defining body: a CCS process
expression over those names, which may itself mention process constants (including $A$).

Formalized by `Cslib.CCS.Recursive.Specification`, an abbreviation declared in [CSLibExt/Languages/CCS/Recursion.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Recursion.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#specification).

## Transitions of recursive CCS

Let the channel names have decidable equality and let
$\Delta$ be a recursive specification, assigning to each process constant $A$ its defining body
$\Delta(A)$. The labelled transition relation $P \xrightarrow{\alpha} P'$ relative to $\Delta$ on
recursive CCS processes, with actions $\alpha$ the CCS labels (silent $\tau$, inputs and outputs),
is the least relation closed under the following rules, where $\alpha.P$ is the prefix, $P + Q$
the choice, $P \mid Q$ the parallel composition, $P \setminus L$ the restriction of $P$ by a
finite list $L$ of channel names, and $P[f]$ the relabelling of $P$ by a finite relabelling $f$.
If $\Delta(A) \xrightarrow{\alpha} P'$, then $A \xrightarrow{\alpha} P'$. The prefix has the
transition $\alpha.P \xrightarrow{\alpha} P$. If $P \xrightarrow{\alpha} P'$, then
$P + Q \xrightarrow{\alpha} P'$, $Q + P \xrightarrow{\alpha} P'$,
$P \mid Q \xrightarrow{\alpha} P' \mid Q$ and $Q \mid P \xrightarrow{\alpha} Q \mid P'$. If
$P \xrightarrow{\alpha} P'$ and $Q \xrightarrow{\beta} Q'$ where $\alpha$ and $\beta$ are
complementary (an input and an output on the same channel), then
$P \mid Q \xrightarrow{\tau} P' \mid Q'$. If $P \xrightarrow{\alpha} P'$ and $\alpha$ is $\tau$ or
its channel is not in $L$, then $P \setminus L \xrightarrow{\alpha} P' \setminus L$. If
$P \xrightarrow{\alpha} P'$, then $P[f] \xrightarrow{f(\alpha)} P'[f]$, where $f(\tau) = \tau$, an
input on a channel $a$ is sent to the visible label $f(a)$ that $f$ assigns to $a$, and an output
on $a$ is sent to the complement of $f(a)$.

Formalized by `Cslib.CCS.Recursive.Process.Step`, an inductive type declared in [CSLibExt/Languages/CCS/Recursion.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Recursion.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#step-2).

## Labelled transition system of a recursive specification

Assuming equality of names
is decidable, for a recursive specification $\Delta$ the labelled transition system generated
by $\Delta$ has the recursive CCS processes as states and the CCS labels as labels, and its
transitions $P \xrightarrow{\alpha} P'$ are exactly the steps of the structural operational
semantics relative to $\Delta$.

Formalized by `Cslib.CCS.Recursive.Process.lts`, a definition declared in [CSLibExt/Languages/CCS/Recursion.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Recursion.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#lts-2).

## Guardedness under a prefix flag

For a Boolean flag $b$, recording whether an action
prefix has already been crossed, guardedness of a recursive CCS process under $b$ is defined
recursively: the inactive process $\mathbf{0}$ is guarded under $b$; a constant $A$ is guarded
under $b$ exactly when $b$ is true; a prefix $\alpha.Q$ is guarded under $b$ when $Q$ is guarded
under true; a choice $Q + R$ or a parallel composition $Q \mid R$ is guarded under $b$ when
both $Q$ and $R$ are; and a restriction $Q \setminus L$ or a relabelling $Q[f]$ is guarded
under $b$ when $Q$ is.

Thus under the flag false a process is guarded exactly when every constant occurrence lies
beneath an action prefix. Static operators and parallel/choice contexts do not themselves
guard recursion.

Formalized by `Cslib.CCS.Recursive.Process.GuardedUnder`, a definition declared in [CSLibExt/Languages/CCS/Recursion.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Recursion.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#guarded-under).

## Guarded process

A recursive CCS process is guarded when all of its constant
occurrences lie beneath an action prefix.

Formalized by `Cslib.CCS.Recursive.Process.Guarded`, a definition declared in [CSLibExt/Languages/CCS/Recursion.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Recursion.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#guarded).

## Every process is guarded beneath a prefix

Every recursive CCS process $P$ is guarded
under the flag $\mathrm{true}$: once an action prefix has been crossed, every constant
occurrence counts as guarded.

Formalized by `Cslib.CCS.Recursive.Process.guardedUnder_true`, a theorem declared in [CSLibExt/Languages/CCS/Recursion.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Recursion.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#guarded-under-true).

## Constant occurrences of a process

The constant occurrences of a recursive CCS
process $P$ are the list of the process constants occurring in $P$, from left to right and
with repetitions: the inactive process $\mathbf{0}$ has none; a constant $A$ has the single
occurrence $A$; a prefix $\alpha.Q$, a restriction $Q \setminus L$ and a relabelling $Q[f]$
have the occurrences of $Q$; and a choice $Q + R$ or a parallel composition $Q \mid R$ has
the occurrences of $Q$ followed by those of $R$.

Formalized by `Cslib.CCS.Recursive.Process.constantOccurrences`, a definition declared in [CSLibExt/Languages/CCS/Recursion.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Recursion.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#constant-occurrences).

## Constants of a process

Assuming equality of process constants is decidable, the
constants of a recursive CCS process $P$ are the list obtained from the constant occurrences
of $P$ by removing duplicates, so that every process constant occurring in $P$ appears in it
exactly once.

Formalized by `Cslib.CCS.Recursive.Process.constants`, a definition declared in [CSLibExt/Languages/CCS/Recursion.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Recursion.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#constants).

## Renaming process constants

Given a map $\rho$ from one set of process constants to
another, renaming the constants of a recursive CCS process $P$ by $\rho$ replaces each
occurrence of a constant $A$ by $\rho(A)$ and leaves $P$ otherwise unchanged: the inactive
process, prefixes, choices, parallel compositions, restrictions and relabellings are kept as
they are.

Formalized by `Cslib.CCS.Recursive.Process.mapConstants`, a definition declared in [CSLibExt/Languages/CCS/Recursion.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Recursion.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#map-constants).

## Renaming constants preserves guardedness

Let $P$ be a recursive CCS process, let
$\rho$ be a map from its process constants to another set of constants, and let $P\rho$ be
the process obtained from $P$ by renaming its constants by $\rho$. Then for each Boolean flag
$b$, $P\rho$ is guarded under $b$ if and only if $P$ is guarded under $b$.

Formalized by `Cslib.CCS.Recursive.Process.guardedUnder_mapConstants`, a theorem declared in [CSLibExt/Languages/CCS/Recursion.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Recursion.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#guarded-under-map-constants).

## Guarded recursive specification

A recursive specification $\Delta$, which assigns
to each process constant $A$ a body $\Delta(A)$, is guarded when for every constant $A$ the
body $\Delta(A)$ is a guarded process.

Formalized by `Cslib.CCS.Recursive.Specification.Guarded`, a definition declared in [CSLibExt/Languages/CCS/Recursion.lean, line 398](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/CCS/Recursion.lean#L398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html#guarded-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Calculus of communicating systems](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/process-calculi/calculus-of-communicating-systems)
