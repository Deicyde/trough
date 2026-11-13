---
declaration: section
origin: cited
lean: Cslib.Turing.SingleTapeTM.compCfgLeft, Cslib.Turing.SingleTapeTM.compCfgRight, Cslib.Turing.SingleTapeTM.transitionRelation_compCfgLeft, Cslib.Turing.SingleTapeTM.step_compCfgRight, Cslib.Turing.SingleTapeTM.transitionRelation_compCfgRight, Cslib.Turing.SingleTapeTM.exists_of_reflTransGen_compCfgRight, Cslib.Turing.SingleTapeTM.Outputs.compComputer, Cslib.Turing.SingleTapeTM.OutputsWithinTime.compComputer
statement: formalized
proof: formalized
---

# Running two single-tape machines one after the other

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/running-two-single-tape-machines-one-after-the-o/index.html).

## Embedding the first machine's configurations into a composite

Let $M_1$ and $M_2$ be
single-tape Turing machines over the same alphabet, and let $M$ be their composite, whose states
are the disjoint union of those of $M_1$ and of $M_2$: $M$ starts in the start state of $M_1$ and
runs $M_1$, where $M_1$ would halt it enters the start state of $M_2$ instead, and it then runs
$M_2$ and halts where $M_2$ halts. A configuration of $M_1$ with tape $t$ is sent to the
configuration of $M$ with the same tape $t$ whose state is the copy of $q$ if $M_1$ is in state
$q$, and the start state of $M_2$ if $M_1$ has halted.

## Sources

- public version of upstream CSLib's private `toCompCfg_left`.

Formalized by `Cslib.Turing.SingleTapeTM.compCfgLeft`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Comp.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Comp.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/running-two-single-tape-machines-one-after-the-o/index.html#comp-cfg-left).

## Embedding the second machine's configurations into a composite

Let $M_1$ and $M_2$ be
single-tape Turing machines over the same alphabet, and let $M$ be their composite, whose states
are the disjoint union of those of $M_1$ and of $M_2$: $M$ starts in the start state of $M_1$ and
runs $M_1$, where $M_1$ would halt it enters the start state of $M_2$ instead, and it then runs
$M_2$ and halts where $M_2$ halts. A configuration of $M_2$ with tape $t$ is sent to the
configuration of $M$ with the same tape $t$ whose state is the copy of $q$ if $M_2$ is in state
$q$, and which is halted if $M_2$ has halted.

## Sources

- public version of upstream CSLib's private `toCompCfg_right`.

Formalized by `Cslib.Turing.SingleTapeTM.compCfgRight`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Comp.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Comp.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/running-two-single-tape-machines-one-after-the-o/index.html#comp-cfg-right).

## The composite simulates steps of the first machine

Let $M_1$ and $M_2$ be single-tape
Turing machines over the same alphabet, and let $M$ be their composite, whose states are the
disjoint union of those of $M_1$ and of $M_2$: $M$ starts in the start state of $M_1$ and runs
$M_1$, where $M_1$ would halt it enters the start state of $M_2$ instead, and it then runs $M_2$
and halts where $M_2$ halts. Let $\iota_1$ send a configuration of $M_1$ to the configuration of
$M$ with the same tape whose state is the copy of the state of $M_1$, or the start state of $M_2$
if $M_1$ has halted. If $M_1$ moves from a configuration $c$ to a configuration $c'$ in one step,
then $M$ moves from $\iota_1(c)$ to $\iota_1(c')$ in one step.

## Sources

- upstream CSLib's private `map_toCompCfg_left_step`, stated as a relation.

Formalized by `Cslib.Turing.SingleTapeTM.transitionRelation_compCfgLeft`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Comp.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Comp.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/running-two-single-tape-machines-one-after-the-o/index.html#transition-relation-comp-cfg-left).

## Step function of a composite on configurations of the second machine

Let $M_1$ and $M_2$
be single-tape Turing machines over the same alphabet, and let $M$ be their composite, whose
states are the disjoint union of those of $M_1$ and of $M_2$: $M$ starts in the start state of
$M_1$ and runs $M_1$, where $M_1$ would halt it enters the start state of $M_2$ instead, and it
then runs $M_2$ and halts where $M_2$ halts. Let $\iota_2$ send a configuration of $M_2$ to the
configuration of $M$ with the same tape whose state is the copy of the state of $M_2$, halted if
$M_2$ has halted. For every configuration $c$ of $M_2$: if $M_2$ moves from $c$ to $c'$ in one
step, then $M$ moves from $\iota_2(c)$ to $\iota_2(c')$ in one step, and if $c$ has no successor
in $M_2$, then $\iota_2(c)$ has no successor in $M$.

## Sources

- upstream CSLib's private `map_toCompCfg_right_step`.

Formalized by `Cslib.Turing.SingleTapeTM.step_compCfgRight`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Comp.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Comp.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/running-two-single-tape-machines-one-after-the-o/index.html#step-comp-cfg-right).

## The composite simulates steps of the second machine

Let $M_1$ and $M_2$ be single-tape
Turing machines over the same alphabet, and let $M$ be their composite, whose states are the
disjoint union of those of $M_1$ and of $M_2$: $M$ starts in the start state of $M_1$ and runs
$M_1$, where $M_1$ would halt it enters the start state of $M_2$ instead, and it then runs $M_2$
and halts where $M_2$ halts. Let $\iota_2$ send a configuration of $M_2$ to the configuration of
$M$ with the same tape whose state is the copy of the state of $M_2$, halted if $M_2$ has halted.
If $M_2$ moves from a configuration $c$ to a configuration $c'$ in one step, then $M$ moves from
$\iota_2(c)$ to $\iota_2(c')$ in one step.

Formalized by `Cslib.Turing.SingleTapeTM.transitionRelation_compCfgRight`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Comp.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Comp.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/running-two-single-tape-machines-one-after-the-o/index.html#transition-relation-comp-cfg-right).

## Runs of a composite from configurations of the second machine

Let $M_1$ and $M_2$ be
single-tape Turing machines over the same alphabet, and let $M$ be their composite, whose states
are the disjoint union of those of $M_1$ and of $M_2$: $M$ starts in the start state of $M_1$ and
runs $M_1$, where $M_1$ would halt it enters the start state of $M_2$ instead, and it then runs
$M_2$ and halts where $M_2$ halts. Let $\iota_2$ send a configuration of $M_2$ to the
configuration of $M$ with the same tape whose state is the copy of the state of $M_2$, halted if
$M_2$ has halted. If $c$ is a configuration of $M_2$ and $M$ moves from $\iota_2(c)$ to a
configuration $d$ in finitely many (possibly zero) steps, then there is a configuration $c'$ of
$M_2$ such that $M_2$ moves from $c$ to $c'$ in finitely many (possibly zero) steps and
$d = \iota_2(c')$.

Formalized by `Cslib.Turing.SingleTapeTM.exists_of_reflTransGen_compCfgRight`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Comp.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Comp.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/running-two-single-tape-machines-one-after-the-o/index.html#exists-of-refl-trans-gen-comp-cfg-right).

## Outputs compose

Let $M_1$ and $M_2$ be single-tape Turing machines over the same
alphabet, and let $M$ be their composite, whose states are the disjoint union of those of $M_1$
and of $M_2$: $M$ starts in the start state of $M_1$ and runs $M_1$, where $M_1$ would halt it
enters the start state of $M_2$ instead, and it then runs $M_2$ and halts where $M_2$ halts. Say
that a machine outputs a word $w$ on a word $v$ when, started in its start state on a tape
holding $v$, it reaches the halted configuration whose tape holds exactly $w$, with the head at
the start of $w$. For all words $a$, $b$, $c$: if $M_1$ outputs $b$ on $a$ and $M_2$ outputs $c$
on $b$, then $M$ outputs $c$ on $a$.

Formalized by `Cslib.Turing.SingleTapeTM.Outputs.compComputer`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Comp.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Comp.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/running-two-single-tape-machines-one-after-the-o/index.html#comp-computer).

## Timed outputs compose

Let $M_1$ and $M_2$ be single-tape Turing machines over the same
alphabet, and let $M$ be their composite, whose states are the disjoint union of those of $M_1$
and of $M_2$: $M$ starts in the start state of $M_1$ and runs $M_1$, where $M_1$ would halt it
enters the start state of $M_2$ instead, and it then runs $M_2$ and halts where $M_2$ halts. Say
that a machine outputs a word $w$ on a word $v$ within $t$ steps when, started in its start state
on a tape holding $v$, it reaches in at most $t$ steps the halted configuration whose tape holds
exactly $w$, with the head at the start of $w$. For all words $a$, $b$, $c$ and all natural
numbers $t_1$, $t_2$: if $M_1$ outputs $b$ on $a$ within $t_1$ steps and $M_2$ outputs $c$ on $b$
within $t_2$ steps, then $M$ outputs $c$ on $a$ within $t_1 + t_2$ steps.

Formalized by `Cslib.Turing.SingleTapeTM.OutputsWithinTime.compComputer`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Comp.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Comp.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/running-two-single-tape-machines-one-after-the-o/index.html#comp-computer-2).

## Halting of a composite

Let $M_1$ and $M_2$ be single-tape Turing machines over the same
alphabet, and let $M$ be their composite, whose states are the disjoint union of those of $M_1$
and of $M_2$: $M$ starts in the start state of $M_1$ and runs $M_1$, where $M_1$ would halt it
enters the start state of $M_2$ instead, and it then runs $M_2$ and halts where $M_2$ halts. Say
that a machine outputs a word $w$ on a word $v$ when, started in its start state on a tape
holding $v$, it reaches the halted configuration whose tape holds exactly $w$, with the head at
the start of $w$. For all words $a$ and $b$ such that $M_1$ outputs $b$ on $a$: $M$, started in
its start state on a tape holding $a$, halts if and only if $M_2$, started in its start state on
a tape holding $b$, halts.

Formalized by `Cslib.Turing.SingleTapeTM.haltsOn_compComputer_iff`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Comp.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Comp.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/running-two-single-tape-machines-one-after-the-o/index.html#halts-on-comp-computer-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Running two single-tape machines one after the other](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/running-two-single-tape-machines-one-after-the-o/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/turing-machines/single-tape/running-two-single-tape-machines-one-after-the-o)
