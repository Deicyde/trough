---
declaration: section
origin: cited
lean: Cslib.Turing.RevTail.K, Cslib.Turing.RevTail.L, Cslib.Turing.RevTail.prog, Cslib.Turing.RevTail.comp, Cslib.Turing.RevTail.run, Cslib.Turing.RevTail.computable, Cslib.Turing.SingleTapeTM.OfTM2.answerTM_outputsWithinTime, Cslib.Turing.SingleTapeTM.OfTM2.deciderTM_outputsWithinTime
statement: formalized
proof: formalized
---

# Polynomial time on single-tape machines

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-on-single-tape-machines/index.html).

## Rev Tail

## Stacks of the reversal component

The two stack indices of the reversal component: the
input stack $X$ and the output stack $O$.

Formalized by `Cslib.Turing.RevTail.K`, an inductive type declared in [CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-on-single-tape-machines/index.html#k).

## Labels of the reversal component

The three labels of the reversal component: mv (move
the input onto the output), drop (drop one symbol) and done.

Formalized by `Cslib.Turing.RevTail.L`, an inductive type declared in [CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-on-single-tape-machines/index.html#l).

## Program of the reversal component

The multi-stack program over the stacks $X$ and $O$,
both with alphabet $\mathrm{Bool}$, with a Boolean internal state: at label mv it moves the bits
of $X$ one at a time onto $O$ (reversing them) and then goes to drop; at drop it pops $O$ once
and goes to done; at done it halts.

Formalized by `Cslib.Turing.RevTail.prog`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-on-single-tape-machines/index.html#prog).

## The reversal component

The component machine with two stacks, the input stack $X$ and
the output stack $O$, both over the alphabet $\mathrm{Bool}$; the three labels mv, drop and done;
the program that moves the bits of $X$ onto $O$ (reversing them), pops $O$ once and halts; and
the stack list $[X, O]$.

Formalized by `Cslib.Turing.RevTail.comp`, an abbreviation declared in [CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-on-single-tape-machines/index.html#comp).

## Running the reversal component

For every bit list $x$, the program of the reversal
component, started at label mv with internal state false, with the bits of $x$ on the input stack
$X$ and every other stack empty, reaches label done within at most $|x| + 2$ steps, with some
internal state and some stacks whose output stack $O$ holds the reversal of $x$ with its first
entry removed.

Formalized by `Cslib.Turing.RevTail.run`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-on-single-tape-machines/index.html#run).

## Reversing and dropping the first bit is polynomial-time

A finite multi-stack Turing
machine whose input and output alphabets are both identified with the bits, together with a
polynomial $p$ with natural-number coefficients, such that for every bit list $x$, given bit by
bit as its own encoding, the machine outputs the reversal of $x$ with its first entry removed
(that is, $x$ without its last bit, in reverse order) within $p(|x|)$ steps.

Formalized by `Cslib.Turing.RevTail.computable`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-on-single-tape-machines/index.html#computable).

## The answer machine runs in one step

Let $M$ be a finite multi-stack machine with finite
stack alphabets, whose input alphabet is identified with the bits by $e$ and whose output alphabet
by $e_1$. For every non-blank cell $x$ of the single-tape emulation alphabet of $M$, the answer
machine of $M$, started on the one-cell tape $x$, halts within at most one step on the one-cell
tape holding the input-bit cell of the answer of $x$ (the bit telling whether $x$ holds
$e_1^{-1}(\mathrm{true})$ on the output stack).

Formalized by `Cslib.Turing.SingleTapeTM.OfTM2.answerTM_outputsWithinTime`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-on-single-tape-machines/index.html#answer-tm-outputs-within-time).

## The decider within time

Let $M$ be a finite multi-stack machine with finite stack
alphabets, whose input alphabet is identified with the bits by $e$ and whose output alphabet by
$e_1$, and let $C$ be the emulation constant of $M$. Let $w$ be a bit list, $b$ a bit and $t$ a
natural number. Suppose $M$, started with its input stack holding the bits of $w$ in reverse order
followed by $\mathrm{true}$ (read through $e^{-1}$), is after exactly $t$ steps in the halting
configuration whose output stack holds just $e_1^{-1}(b)$, whose other stacks are empty and whose
internal state is the initial one. Then the single-tape decider of $M$, started on the tape of
input-bit cells of $w$, halts on the one-cell tape holding the input-bit cell of $b$ within
$C t (|w| + 1 + C t + 1) + 4$ steps.

Formalized by `Cslib.Turing.SingleTapeTM.OfTM2.deciderTM_outputsWithinTime`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-on-single-tape-machines/index.html#decider-tm-outputs-within-time).

## Polynomial time on single-tape machines

The class of decision problems $L$ for which
there are a finite alphabet $\Sigma$ with a designated default element, an injective map $\iota$
from the bits to $\Sigma$, a single-tape Turing machine $M$ over $\Sigma$ and a polynomial $p$
with natural-number coefficients such that, for every bit list $w$, the machine $M$ started on the
word $\iota(w)$ (the bits of $w$ mapped by $\iota$) halts on the one-cell tape $\iota(L(w))$
within $p(|w|)$ steps.

Formalized by `Cslib.Complexity.SingleTapeP`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-on-single-tape-machines/index.html#single-tape-p).

## Problems in P are decided in polynomial time by single-tape machines

Every decision
problem in the class $\mathrm{P}$ (defined with multi-stack machines) belongs to the class of
decision problems decided in polynomial time by single-tape machines.

The proof reverses the input, restricts the multi-stack machine to finite alphabets and emulates
it on a single tape within quadratic overhead.

Formalized by `Cslib.Complexity.P_subset_singleTapeP`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/PolyTime.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-on-single-tape-machines/index.html#p-subset-single-tape-p).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polynomial time on single-tape machines](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-on-single-tape-machines/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/complexity-classes/polynomial-time-on-single-tape-machines)
