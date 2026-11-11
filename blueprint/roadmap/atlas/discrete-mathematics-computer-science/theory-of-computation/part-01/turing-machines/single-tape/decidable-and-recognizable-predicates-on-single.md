---
declaration: section
origin: cited
lean: Cslib.Turing.SingleTapeTM.HaltsOn, Cslib.Turing.SingleTapeTM.HaltsFrom, Cslib.Turing.SingleTapeTM.haltsOn_iff_haltsFrom, Cslib.Turing.SingleTapeTM.step_some, Cslib.Turing.SingleTapeTM.Outputs.haltsOn, Cslib.Turing.SingleTapeTM.rightUnique_transitionRelation, Cslib.Turing.SingleTapeTM.step_eq_none_iff, Cslib.Turing.SingleTapeTM.haltsFrom_iff_normalizable
statement: formalized
proof: formalized
---

# Decidable and recognizable predicates on single-tape Turing machines

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/decidable-and-recognizable-predicates-on-single/index.html).

## Single Tape TM

## Halting on an input

A single-tape Turing machine $M$ halts on an input word $w$ when its
run from the initial configuration on $w$ (the start state, with $w$ written from the head
position rightwards on an otherwise blank tape) reaches, in finitely many steps (possibly none), a
configuration in the halting state.

Formalized by `Cslib.Turing.SingleTapeTM.HaltsOn`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/decidable-and-recognizable-predicates-on-single/index.html#halts-on).

## Halting from a configuration

A single-tape Turing machine $M$ halts from a configuration
$c$ when its run from $c$ reaches, in finitely many steps (possibly none), a configuration in the
halting state.

Equivalently, $c$ is normalizable for the transition relation of $M$, since the configurations in
the halting state are exactly those without a successor; the same holds for CSLib's register
machines.

Formalized by `Cslib.Turing.SingleTapeTM.HaltsFrom`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/decidable-and-recognizable-predicates-on-single/index.html#halts-from).

## Halting on an input is halting from the initial configuration

A single-tape Turing machine
$M$ halts on an input word $w$ if and only if $M$ halts from the initial configuration on $w$.

Formalized by `Cslib.Turing.SingleTapeTM.haltsOn_iff_haltsFrom`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/decidable-and-recognizable-predicates-on-single/index.html#halts-on-iff-halts-from).

## One step of a single-tape Turing machine

Let $M$ be a single-tape Turing machine, $q$ a
state of $M$ other than the halting state and $t$ a tape, and let the transition function of $M$
at $q$ and the symbol under the head of $t$ (possibly blank) give the symbol $s$ to write
(possibly blank), the head movement $d$ (left, right or none) and the next state $q'$ (possibly
the halting state). Then the configuration in state $q$ with tape $t$ has a successor, namely the
configuration in state $q'$ whose tape is obtained from $t$ by writing $s$ under the head and
then moving the head by $d$.

Formalized by `Cslib.Turing.SingleTapeTM.step_some`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/decidable-and-recognizable-predicates-on-single/index.html#step-some).

## A machine that produces an output halts

If a single-tape Turing machine $M$ outputs a word
$w'$ on an input word $w$, then $M$ halts on $w$.

Formalized by `Cslib.Turing.SingleTapeTM.Outputs.haltsOn`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/decidable-and-recognizable-predicates-on-single/index.html#halts-on-2).

## Single-tape Turing machines are deterministic

For a single-tape Turing machine $M$, every
configuration of $M$ has at most one successor under the transition relation of $M$.

Formalized by `Cslib.Turing.SingleTapeTM.rightUnique_transitionRelation`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/decidable-and-recognizable-predicates-on-single/index.html#right-unique-transition-relation).

## Halting configurations are exactly those without a successor

For a single-tape Turing
machine $M$ and a configuration $c$ of $M$, one step of $M$ from $c$ gives no configuration if
and only if $c$ is in the halting state.

Formalized by `Cslib.Turing.SingleTapeTM.step_eq_none_iff`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/decidable-and-recognizable-predicates-on-single/index.html#step-eq-none-iff).

## Halting from a configuration is normalizability

Let $M$ be a single-tape Turing machine
and $c$ a configuration of $M$. Then $M$ halts from $c$ if and only if $c$ is normalizable for
the transition relation of $M$, that is, the run of $M$ from $c$ reaches, in finitely many steps
(possibly none), a configuration that has no successor.

The configurations without a successor are exactly those in the halting state.

Formalized by `Cslib.Turing.SingleTapeTM.haltsFrom_iff_normalizable`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/decidable-and-recognizable-predicates-on-single/index.html#halts-from-iff-normalizable).

## Halting from a configuration is invariant along a run

Let $M$ be a single-tape Turing
machine and let $a$ and $b$ be configurations of $M$ such that the run of $M$ from $a$ reaches $b$
in finitely many steps (possibly none). Then $M$ halts from $a$ if and only if $M$ halts from $b$.

The backward direction holds for any relation; the forward direction uses that $M$ is
deterministic.

Formalized by `Cslib.Turing.SingleTapeTM.haltsFrom_iff_of_reflTransGen`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/decidable-and-recognizable-predicates-on-single/index.html#halts-from-iff-of-refl-trans-gen).

## Configurations with the same successor halt together

Let $M$ be a single-tape Turing
machine and let $a$ and $b$ be configurations of $M$ that have the same successor, or that both
have no successor. Then $M$ halts from $a$ if and only if $M$ halts from $b$.

Formalized by `Cslib.Turing.SingleTapeTM.haltsFrom_iff_of_step_eq`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/decidable-and-recognizable-predicates-on-single/index.html#halts-from-iff-of-step-eq).

## Distinct words give distinct tapes

The map sending a word $w$ to the tape that holds $w$
from the head position rightwards, every other cell blank, is injective.

Formalized by `Cslib.Turing.SingleTapeTM.mk₁_injective`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/decidable-and-recognizable-predicates-on-single/index.html#mk-injective).

## Outputs are unique

If a single-tape Turing machine $M$ outputs the word $l_1$ on the
input $l$ and also outputs the word $l_2$ on the input $l$, then $l_1 = l_2$. Here $M$ outputs a
word $w$ on $l$ when its run from the initial configuration on $l$ halts with exactly $w$ on the
tape, every other cell blank and the head on the first symbol of $w$ (an all-blank tape if $w$ is
empty).

The run of a machine is determined by its input, and a halting configuration has no successor.

Formalized by `Cslib.Turing.SingleTapeTM.Outputs.unique`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/decidable-and-recognizable-predicates-on-single/index.html#unique).

## Predicates decidable by a single-tape Turing machine

Let $\alpha$ be a type with a
primitive recursive encoding into $\mathbb{N}$. A predicate $p$ on $\alpha$ is decidable by a
single-tape machine when there are a finite, nonempty tape alphabet $\Sigma$, an injective map
$\iota$ from the bits $\{0, 1\}$ to $\Sigma$ and a single-tape Turing machine $M$ over $\Sigma$
such that for every $a \in \alpha$ there is a bit $b$ for which $M$ outputs the one-symbol word
$\iota(b)$ on the input word obtained by writing the binary encoding of the code of $a$ in
$\mathbb{N}$ letter by letter through $\iota$, and $b = 1$ exactly when $p(a)$ holds. Here $M$
outputs a word $w$ on an input when its run from the input halts with exactly $w$ on the tape,
every other cell blank and the head on the first symbol of $w$.

Formalized by `Cslib.Decidability.SingleTapeDecidable`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/decidable-and-recognizable-predicates-on-single/index.html#single-tape-decidable).

## Predicates recognizable by a single-tape Turing machine

Let $\alpha$ be a type with a
primitive recursive encoding into $\mathbb{N}$. A predicate $p$ on $\alpha$ is recognizable by a
single-tape machine when there are a finite, nonempty tape alphabet $\Sigma$, an injective map
$\iota$ from the bits $\{0, 1\}$ to $\Sigma$ and a single-tape Turing machine $M$ over $\Sigma$
such that for every $a \in \alpha$, the run of $M$ on the input word obtained by writing the
binary encoding of the code of $a$ in $\mathbb{N}$ letter by letter through $\iota$ reaches the
halting state if and only if $p(a)$ holds.

Formalized by `Cslib.Decidability.SingleTapeRecognizable`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/decidable-and-recognizable-predicates-on-single/index.html#single-tape-recognizable).

## Co-recognizability by single-tape machines

Let $\alpha$ be a primcodable type. A predicate
$p$ on $\alpha$ is co-recognizable by a single-tape Turing machine when its complement $\neg p$ is
recognizable by a single-tape Turing machine.

Formalized by `Cslib.Decidability.SingleTapeCoRecognizable`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Classes.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/decidable-and-recognizable-predicates-on-single/index.html#single-tape-co-recognizable).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Decidable and recognizable predicates on single-tape Turing machines](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/turing-machines/single-tape/decidable-and-recognizable-predicates-on-single/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/turing-machines/single-tape/decidable-and-recognizable-predicates-on-single)
