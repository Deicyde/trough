---
declaration: section
origin: cited
lean: Cslib.Turing.SingleTapeTM.consComputer, Cslib.Turing.SingleTapeTM.write_moveLeft_mk₁, Cslib.Turing.SingleTapeTM.consComputer_outputsWithinTime, Cslib.Turing.SingleTapeTM.consComputer_outputs, Cslib.Turing.SingleTapeTM.OfTM2.inputCode, Cslib.Turing.SingleTapeTM.OfTM2.reverse_tail_encodeNat_inputCode, Cslib.Turing.SingleTapeTM.OfTM2.inputDecode, Cslib.Turing.SingleTapeTM.OfTM2.inCell
statement: formalized
proof: formalized
---

# Single-tape machines decide the recursive predicates

55 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html).

## The machine that prepends a symbol

For a symbol $c$, this is the single-tape machine
with two states that, from its start state, writes back the symbol under the head, moves left and
enters its second state, and from its second state writes $c$ and halts without moving.

On an input word $l$ it outputs $c$ followed by $l$.

Formalized by `Cslib.Turing.SingleTapeTM.consComputer`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#cons-computer).

## Prepending a symbol by stepping left

Let $c$ be a symbol and $l$ a list of symbols, and
consider the tape holding $l$ from the head rightwards, all other cells blank. Writing back the
symbol under the head, moving the head one cell left, and then writing $c$ gives the tape holding
the list $c$ followed by $l$ from the head rightwards, all other cells blank.

Formalized by `Cslib.Turing.SingleTapeTM.write_moveLeft_mk₁`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#write-move-left-mk).

## Prepending a symbol takes at most two steps

For every symbol $c$ and every word $l$, the
machine that prepends $c$, started on $l$, halts with output the word $c$ followed by $l$ within
at most two steps.

Formalized by `Cslib.Turing.SingleTapeTM.consComputer_outputsWithinTime`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#cons-computer-outputs-within-time).

## Correctness of the prepending machine

For every symbol $c$ and every word $l$, the
machine that prepends $c$, started on $l$, halts with output the word $c$ followed by $l$.

Formalized by `Cslib.Turing.SingleTapeTM.consComputer_outputs`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#cons-computer-outputs).

## Input code of a bit word

For a list of bits $w$, let $b_0, \dots, b_n$ be the reversal of
$w$ followed by $\mathsf{true}$, reading $\mathsf{true}$ as $1$ and $\mathsf{false}$ as $0$. The
input code of $w$ is the natural number $\sum_{i=0}^{n} b_i 2^i$. Its binary expansion, least
significant bit first, is $b_0, \dots, b_n$: the input stack on which the single-tape emulation
starts for the input word $w$.

Formalized by `Cslib.Turing.SingleTapeTM.OfTM2.inputCode`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#input-code).

## Recovering a word from its input code

For every list of bits $w$, reversing the binary
encoding (least significant bit first) of the input code of $w$ and then dropping the first bit of
the result gives back $w$.

Formalized by `Cslib.Turing.SingleTapeTM.OfTM2.reverse_tail_encodeNat_inputCode`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#reverse-tail-encode-nat-input-code).

## Input decoding

For a natural number $m > 0$, let $b_0, \dots, b_n$ be its binary
expansion, least significant bit first, without trailing zeros. The input decoding of $m$ is
$\sum_{i=0}^{n-1} b_{n-1-i} 2^i$, the value, least significant bit first, of the reversed
expansion with its first bit dropped. The input decoding of $0$, whose expansion is empty, is $0$.

It undoes the encoding of input words: for every natural number $k$ with binary expansion $w$,
least significant bit first, the input decoding of the number whose binary expansion, least
significant bit first, is the reversal of $w$ followed by $1$ is $k$.

Formalized by `Cslib.Turing.SingleTapeTM.OfTM2.inputDecode`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#input-decode).

## Input cell of a bit

Let $M$ be a multi-stack machine with finitely many stacks, labels
and internal states, and let $e$ be a bijection from the alphabet of its input stack to the bits.
The input cell of a bit $b$ is the non-blank cell of the single-tape emulation of $M$ whose
bottom-of-stack flag is off, whose entry for the input stack is $e^{-1}(b)$, and whose entries for
all other stacks are empty.

Formalized by `Cslib.Turing.SingleTapeTM.OfTM2.inCell`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#in-cell).

## The bottom cell of the start tape

Let $M$ be a finite multi-stack machine whose input
stack alphabet is identified with the bits. The bottom cell of the emulation's start tape is the
cell flagged as the stack bottom that holds the symbol for $\mathrm{true}$ on the input stack and
nothing on every other stack.

Formalized by `Cslib.Turing.SingleTapeTM.OfTM2.botCell`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#bot-cell).

## States of the single-tape emulation

Let $M$ be a multi-stack machine with finitely many
stacks, labels and internal states and a finite input alphabet. Its plain single-tape emulation
is the translation of $M$ to a single-tape machine with a finite store, followed by the
translation of that machine to a plain single-tape machine, whose states are pairs of a
statement of the intermediate machine, or the halting state, and an internal state. This is the
finite set of those pairs whose first entry is the halting state or a statement occurring in the
program of one of the labels that the first translation produces from the labels of $M$.

The emulation only visits states in this set.

Formalized by `Cslib.Turing.SingleTapeTM.OfTM2.emuSupport`, an abbreviation declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#emu-support).

## Finite single-tape emulation of a multi-stack machine

Let $M$ be a multi-stack machine
with finitely many stacks, labels and internal states, and with finite stack alphabets. Its
finite single-tape emulation is the single-tape machine that runs the plain single-tape emulation
of $M$ (through a single-tape machine with a finite store) step for step: its states are those in
the finite set of states the emulation visits, and its tape alphabet is the set of non-blank cells
of the emulation, where a cell is a bottom-of-stack flag together with an optional symbol for each
stack.

Formalized by `Cslib.Turing.SingleTapeTM.OfTM2.emuTM`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#emu-tm).

## The recognizer of a multi-stack machine

Let $M$ be a finite multi-stack machine all of
whose stack alphabets are finite, and let $e$ be an identification of the alphabet of its input
stack with the booleans. The recognizer of $M$ is the single-tape machine, over the non-blank
cells of the multi-stack-to-single-tape translation of $M$, that first runs the machine
prepending the bottom cell determined by $M$ and $e$ (the bottom-flagged cell holding
$e^{-1}(\mathrm{true})$ on the input stack and nothing on the other stacks) to its input and, when
that machine halts, runs the single-tape emulation of $M$.

Formalized by `Cslib.Turing.SingleTapeTM.OfTM2.recognizerTM`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#recognizer-tm).

## The bottom cell followed by the input word is the emulation's start tape

Let $M$ be a
multi-stack machine with finitely many stacks, labels and internal states, and let $e$ be a
bijection from the alphabet of its input stack to the bits. For every list of bits $w$, the bottom
cell followed by the input cells of the bits of $w$, read as cells of the emulation, is the start
tape that the single-tape emulation assigns to the input stack obtained by applying $e^{-1}$ to
each entry of the reversal of $w$ followed by $\mathsf{true}$.

Formalized by `Cslib.Turing.SingleTapeTM.OfTM2.map_val_botCell_cons`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#map-val-bot-cell-cons).

## The recognizer halts iff the multi-stack machine does

Let $M$ be a multi-stack machine
with finitely many stacks, labels and internal states and with finite stack alphabets, and let
$e$ be a bijection from the alphabet of its input stack to the bits. For every list of bits $w$,
the recognizer built from $M$ and $e$ halts on the word of input cells of the bits of $w$ if and
only if $M$ halts when started on the input stack obtained by applying $e^{-1}$ to each entry of
the reversal of $w$ followed by $\mathsf{true}$.

Formalized by `Cslib.Turing.SingleTapeTM.OfTM2.haltsOn_recognizerTM_iff`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#halts-on-recognizer-tm-iff).

## The emulation's final tape

Let $M$ be a multi-stack machine with finitely many stacks,
labels and internal states and a finite input alphabet, let $L$ be a list of symbols of its input
stack, and suppose that $M$, started with $L$ on its input stack and every other stack empty,
halts at the configuration $c$. Then its plain single-tape emulation, started on the tape that
holds the symbols of $L$ bottom first on the input stack with the first cell flagged as the
bottom, halts at a configuration $c_0$ for which there is a list $L'$ of columns, each holding an
optional symbol for every stack and padded with blank columns, such that for every stack $k$ the
entries of $L'$ for $k$ are the symbols of stack $k$ of $c$ listed bottom first, followed by
blanks, and the tape of $c_0$ is blank to the left of the head and holds $L'$ from the head
rightwards, with the bottom-of-stack flag set on its first cell and cleared on all others.

Formalized by `Cslib.Turing.SingleTapeTM.OfTM2.exists_mem_eval_tr`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#exists-mem-eval-tr).

## Stacks of height at most one give a one-cell tape

Let $M$ be a finite multi-stack
machine, and let $S$ assign to every stack $k$ of $M$ a list $S_k$ of length at most $1$. Let $L'$
be a tape of stack columns whose $k$-th track, for every $k$, is $S_k$ laid out bottom first and
followed by blanks. Then adding the bottom marker to $L'$, as in the translation of $M$ to a
single-tape machine, gives the tape whose first cell is flagged as the bottom and holds the top of
$S_k$ on every stack $k$ (nothing if $S_k$ is empty), followed by blank cells.

Formalized by `Cslib.Turing.SingleTapeTM.OfTM2.addBottom_eq_of_length_le_one`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#add-bottom-eq-of-length-le-one).

## The answer bit of a cell

Let $M$ be a finite multi-stack machine whose output stack
alphabet is identified with the bits. The answer read from a non-blank cell of the single-tape
emulation of $M$ is $\mathrm{true}$ exactly when the cell holds the symbol for $\mathrm{true}$ on
the output stack.

Formalized by `Cslib.Turing.SingleTapeTM.OfTM2.cellAnswer`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#cell-answer).

## The answer machine

Let $M$ be a finite multi-stack machine whose stack alphabets are all
finite, with its input and output stack alphabets identified with the bits. The answer machine of
$M$ is the single-tape machine over the non-blank cells of the single-tape emulation of $M$ with a
single state that, in one step, replaces the symbol under the head by the input-bit cell for the
answer read from that cell (the answer $\mathrm{false}$ if the cell is blank), does not move, and
halts.

Formalized by `Cslib.Turing.SingleTapeTM.OfTM2.answerTM`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#answer-tm).

## The answer machine outputs the answer of a one-cell input

Let $M$ be a finite multi-stack
machine whose stack alphabets are all finite, with its input and output stack alphabets
identified with the bits. For every non-blank cell $x$ of the single-tape emulation of $M$, the
answer machine of $M$, started on the one-cell input $x$, halts with the one-cell output holding
the input-bit cell for the answer read from $x$.

Formalized by `Cslib.Turing.SingleTapeTM.OfTM2.answerTM_outputs`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#answer-tm-outputs).

## The decider of a multi-stack machine

Let $M$ be a finite multi-stack machine whose stack
alphabets are all finite, with its input and output stack alphabets identified with the bits. The
decider of $M$ is the single-tape machine over the non-blank cells of the single-tape emulation of
$M$ that runs the recognizer of $M$ and, once the recognizer halts, runs the answer machine of $M$
on the resulting tape.

Formalized by `Cslib.Turing.SingleTapeTM.OfTM2.deciderTM`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#decider-tm).

## The decider outputs the answer bit

Let $M$ be a finite multi-stack machine whose stack
alphabets are all finite, with its input and output stack alphabets identified with the bits, and
let $w$ be a word of bits. Suppose that $M$, started with the input stack holding the reverse of
$w$ followed by $\mathrm{true}$, halts with the output stack holding a list $u$ of length at most
$1$, every other stack empty and its variable back at its initial value. Then there is a bit $b$
such that the decider of $M$, started on the input-bit cells of $w$, halts with the one-cell
output holding the input-bit cell for $b$, and $b = \mathrm{true}$ exactly when $u$ is nonempty
and its first symbol is the symbol for $\mathrm{true}$.

Formalized by `Cslib.Turing.SingleTapeTM.OfTM2.deciderTM_outputs`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#decider-tm-outputs).

## R.e. predicates are recognizable by single-tape machines

**R.e. predicates are recognizable by single-tape machines.**

Formalized by `Cslib.Decidability.SingleTapeRecognizable.of_rePred`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#of-re-pred).

## Computable predicates are decidable by single-tape machines

Let $\alpha$ be a type with a
primitive recursive encoding into $\mathbb{N}$, and let $p$ be a computable predicate on $\alpha$,
that is, one whose indicator function $\alpha \to \{0, 1\}$ is computable. Then $p$ is decidable
by a single-tape Turing machine.

Formalized by `Cslib.Decidability.SingleTapeDecidable.of_computablePred`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/OfRecursive.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#of-computable-pred).

## Pushing a cell onto a coded tape

For any type $\Sigma$, an element $x$ of
$\Sigma \cup \{\bot\}$ (with $\bot$ the blank) and a finite list $l$ over $\Sigma \cup \{\bot\}$,
the push of $x$ onto $l$ is the empty list when $x = \bot$ and $l$ is empty, and otherwise the list
obtained by prepending $x$ to $l$.

Formalized by `Cslib.Turing.SingleTapeTM.codedCons`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#coded-cons).

## The head of a stack tape is the first entry of its list

For every one-sided tape $s$ over
an alphabet $\Sigma$, stored as a finite list of cells in $\Sigma \cup \{\bot\}$ (with $\bot$ the
blank) that does not end in $\bot$, the symbol at the head of $s$ is the first entry of that list,
and the blank $\bot$ when the list is empty.

Formalized by `Cslib.Turing.StackTape.head_eq_headI`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#head-eq-head-i).

## Tail of a stack tape, on cell lists

Let $s$ be a stack tape, a one-sided tape stored as
its list of cells without trailing blanks. Then the cell list of the tail of $s$ is the tail of
the cell list of $s$, the tail of the empty list being empty.

Formalized by `Cslib.Turing.StackTape.toList_tail`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#to-list-tail).

## Pushing onto a stack tape, on cell lists

Let $s$ be a stack tape, a one-sided tape stored
as its list of cells without trailing blanks, and $x$ a cell content, either a symbol or blank.
Then the cell list of the tape obtained by pushing $x$ onto $s$ is the coded push of $x$ applied to
the cell list of $s$: $x$ prepended to it, except that pushing a blank onto the empty tape gives
the empty list.

Formalized by `Cslib.Turing.StackTape.toList_cons`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#to-list-cons).

## Pushing a cell onto a coded tape is primitive recursive

Let $\Sigma$ be a type with a
primitive recursive coding, and let $x$ be a cell content, either a symbol of $\Sigma$ or blank.
Then the coded push of $x$, the map on lists of cell contents that prepends $x$ to a list, except
that it sends the empty list to the empty list when $x$ is blank, is primitive recursive.

Formalized by `Cslib.Turing.SingleTapeTM.primrec_codedCons`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#primrec-coded-cons).

## Binary codes of natural numbers in a tape alphabet are primitive recursive

Let $\Sigma$ be
a type with a primitive recursive coding and $\iota$ any map from the Booleans to $\Sigma$. Then
the map sending $n \in \mathbb{N}$ to the word over $\Sigma$ obtained by applying $\iota$ letterwise
to the binary code of $n$ (least significant bit first, the empty word for $0$) is primitive
recursive.

Formalized by `Cslib.Turing.SingleTapeTM.primrec_map_encodeNat`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#primrec-map-encode-nat).

## Halting is termination of the run

A single-tape machine $M$ halts on an input word $l$ if
and only if iterating the step function of $M$ from the initial configuration on $l$, until a
configuration with no successor is reached, terminates.

Formalized by `Cslib.Turing.SingleTapeTM.haltsOn_iff_dom_eval`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#halts-on-iff-dom-eval).

## Outputs are the ends of runs

A single-tape machine $M$ outputs the word $l'$ on the input
word $l$ if and only if iterating the step function of $M$ from the initial configuration on $l$,
until a configuration with no successor is reached, terminates at the halting configuration for
$l'$: the halting state, with $l'$ written from the head rightwards and every other cell blank.

Formalized by `Cslib.Turing.SingleTapeTM.outputs_iff_mem_eval`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#outputs-iff-mem-eval).

## Coded configurations of a single-tape machine

For a single-tape Turing machine with state
set $Q$ and tape alphabet $\Sigma$, write $\bot$ for an absent value. A coded configuration is a
quadruple $(q, h, L, R)$ where $q \in Q \cup \{\bot\}$ is the state ($\bot$ meaning halted),
$h \in \Sigma \cup \{\bot\}$ is the symbol under the head ($\bot$ being the blank), and $L$ and $R$
are finite lists over $\Sigma \cup \{\bot\}$, meant as the cells to the left and to the right of
the head.

Formalized by `Cslib.Turing.SingleTapeTM.CodedCfg`, an abbreviation declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#coded-cfg).

## Code of a single-tape configuration

The code of a configuration of a single-tape machine
is the quadruple consisting of its state (or the halting state), the symbol under the head (or
blank), and the lists of cells, without trailing blanks, of the tapes to the left and to the right
of the head.

Formalized by `Cslib.Turing.SingleTapeTM.Cfg.toCodedCfg`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#to-coded-cfg).

## One step of a single-tape machine on coded configurations

Let $M$ be a single-tape Turing
machine with transition function $\delta$, and write $\bot$ both for the halting state and for the
blank. For a finite list $l$ of cells, let $\mathrm{hd}(l)$ be the first entry of $l$, the blank
$\bot$ when $l$ is empty; let $\mathrm{tl}(l)$ be $l$ without its first entry, the empty list when
$l$ is empty; and for a cell $w$ let $w \cdot l$, the push of $w$ onto $l$, be $l$ when $w = \bot$
and $l$ is empty, and $w$ prepended to $l$ otherwise. A coded configuration $(\bot, h, L, R)$ in
the halting state has no successor. For a running state $q$, write $\delta(q, h) = ((w, d), q')$,
where $w$ is the symbol to write, $d$ is either no move or a direction, and $q'$ is the new state,
possibly the halting state $\bot$. The successor of $(q, h, L, R)$ is $(q', w, L, R)$ if $d$ is no
move, $(q', \mathrm{hd}(L), \mathrm{tl}(L), w \cdot R)$ if $d$ is left, and
$(q', \mathrm{hd}(R), w \cdot L, \mathrm{tl}(R))$ if $d$ is right.

Formalized by `Cslib.Turing.SingleTapeTM.codedStep`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#coded-step).

## The coded step commutes with coding

For every configuration $c$ of a single-tape machine
$M$, the code of $c$ has no successor under the coded step exactly when $c$ has no successor
under the step function of $M$, and otherwise the coded step sends the code of $c$ to the code
of the successor of $c$.

Formalized by `Cslib.Turing.SingleTapeTM.codedStep_toCodedCfg`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#coded-step-to-coded-cfg).

## The coded step of a single-tape machine is primitive recursive

Let $M$ be a single-tape
Turing machine over a finite alphabet $\Sigma$, and fix primitive recursive codings of $\Sigma$ and
of the states of $M$. Then the coded step of $M$, which maps a coded configuration to the coded
configuration after one step of $M$ and has no value when the state is the halting state, is
primitive recursive.

Formalized by `Cslib.Turing.SingleTapeTM.primrec_codedStep`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#primrec-coded-step).

## Running the coded step mirrors running the machine

For every configuration $c$ of a
single-tape machine $M$, iterating the coded step from the code of $c$ until a coded
configuration with no successor is reached terminates exactly when iterating the step function
of $M$ from $c$ until a configuration with no successor is reached does, and then it ends at the
code of the configuration where the run of $M$ from $c$ ends.

Formalized by `Cslib.Turing.SingleTapeTM.eval_codedStep`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#eval-coded-step).

## The code of the initial configuration is primitive recursive

Let $M$ be a single-tape
Turing machine over a finite alphabet $\Sigma$, and fix primitive recursive codings of $\Sigma$ and
of the states of $M$. Then the map sending an input word $w$ over $\Sigma$ to the code of the
initial configuration of $M$ on $w$ is primitive recursive.

Formalized by `Cslib.Turing.SingleTapeTM.primrec_toCodedCfg_initCfg`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#primrec-to-coded-cfg-init-cfg).

## The final tape of a run is partial recursive in the input word

Let $M$ be a single-tape
Turing machine whose finite alphabet $\Sigma$ carries a primitive recursive coding. The partial
function sending an input word $l$ over $\Sigma$ to the final tape of the run of $M$ on $l$ (the
symbol under the head, and the lists of cells to the left and to the right of the head), defined
exactly when $M$ halts on $l$, is partial recursive.

Formalized by `Cslib.Turing.SingleTapeTM.partrec_eval`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#partrec-eval).

## The halting set of a single-tape machine is r.e

Let $M$ be a single-tape Turing machine
over a finite alphabet $\Sigma$, and fix a primitive recursive coding of $\Sigma$. Then the set of
input words over $\Sigma$ on which $M$ halts is recursively enumerable.

Formalized by `Cslib.Turing.SingleTapeTM.rePred_haltsOn`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#re-pred-halts-on).

## The halting set of a single-tape machine on binary inputs is r.e

Let $M$ be a single-tape
Turing machine over a finite alphabet $\Sigma$ and $\iota$ any map from the Booleans to $\Sigma$.
Then the set of natural numbers $n$ such that $M$ halts on the word obtained by applying $\iota$
letterwise to the binary code of $n$ (least significant bit first, the empty word for $0$) is
recursively enumerable.

Formalized by `Cslib.Turing.SingleTapeTM.rePred_haltsOn_encodeNat`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#re-pred-halts-on-encode-nat).

## A predicate recognized by a single-tape machine is r.e

**A predicate recognized by a single-tape machine is r.e.**

Formalized by `Cslib.Decidability.SingleTapeRecognizable.rePred`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#re-pred).

## A predicate decided by a single-tape machine is computable

The decider's answer is the
symbol under the head of its final tape.

Formalized by `Cslib.Decidability.SingleTapeDecidable.computablePred`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/ToRecursive.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#computable-pred).

## Single-tape decidable predicates are exactly the computable predicates

Let $\alpha$ be a
primcodable type (it has an encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is
primitive recursive). A predicate $p$ on $\alpha$ is decidable by a single-tape machine if and only
if it is computable, that is, $p$ is decidable and its Boolean characteristic function
$\alpha \to \mathrm{Bool}$ is computable.

Formalized by `Cslib.Decidability.singleTapeDecidable_iff_computablePred`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#single-tape-decidable-iff-computable-pre).

## Single-tape recognizable predicates are exactly the r.e. predicates

Let $\alpha$ be a
primcodable type (it has an encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is
primitive recursive). A predicate $p$ on $\alpha$ is recognizable by a single-tape machine if and
only if it is recursively enumerable, that is, the partial function on $\alpha$ that is defined,
with a trivial value, exactly where $p$ holds is partial recursive.

Formalized by `Cslib.Decidability.singleTapeRecognizable_iff_rePred`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#single-tape-recognizable-iff-re-pred).

## Single-tape co-recognizable predicates are those with an r.e. complement

Let $\alpha$ be a
primcodable type (it has an encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is
primitive recursive). A predicate $p$ on $\alpha$ is co-recognizable by a single-tape machine if
and only if its complement $\neg p$ is recursively enumerable, that is, the partial function on
$\alpha$ that is defined, with a trivial value, exactly where $\neg p$ holds is partial
recursive.

Formalized by `Cslib.Decidability.singleTapeCoRecognizable_iff_rePred_not`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#single-tape-co-recognizable-iff-re-pred).

## Single-tape and multi-stack machines decide the same predicates

**Single-tape and multi-stack machines decide the same predicates.**

Formalized by `Cslib.Decidability.singleTapeDecidable_iff_tm2Decidable`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#single-tape-decidable-iff-tm2-decidable).

## Single-tape and multi-stack machines recognize the same predicates

Let $\alpha$ be a
primcodable type (it has an encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is
primitive recursive). A predicate $p$ on $\alpha$ is recognizable by a single-tape machine if and
only if it is recognizable by a multi-stack machine.

Formalized by `Cslib.Decidability.singleTapeRecognizable_iff_tm2Recognizable`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#single-tape-recognizable-iff-tm2-recogni).

## Post's theorem

**Post's theorem** for single-tape machines: a predicate is decidable iff it is recognizable
and co-recognizable.

Formalized by `Cslib.Decidability.singleTapeDecidable_iff_singleTapeRecognizable_and_singleTapeCoRecognizable`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#single-tape-decidable-iff-single-tape-re).

## Decidable predicates are recognizable by single-tape machines

Let $\alpha$ be a
primcodable type (it has an encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is
primitive recursive). If a predicate $p$ on $\alpha$ is decidable by a single-tape machine, then
$p$ is recognizable by a single-tape machine.

Formalized by `Cslib.Decidability.SingleTapeDecidable.singleTapeRecognizable`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#single-tape-recognizable).

## Single-tape decidable predicates are co-recognizable

Let $\alpha$ be a primcodable type
(it has an encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is primitive
recursive). If a predicate $p$ on $\alpha$ is decidable by a single-tape machine, then $p$ is
co-recognizable by a single-tape machine, that is, its complement $\neg p$ is recognizable by a
single-tape machine.

Formalized by `Cslib.Decidability.SingleTapeDecidable.singleTapeCoRecognizable`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#single-tape-co-recognizable).

## Single-tape decidable predicates are closed under complement

Let $\alpha$ be a
primcodable type (it has an encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is
primitive recursive). If a predicate $p$ on $\alpha$ is decidable by a single-tape machine, then so
is its complement $\neg p$.

Formalized by `Cslib.Decidability.SingleTapeDecidable.not`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#not).

## The halting problem for partial recursive codes is undecidable on single-tape machines

For every $n \in \mathbb{N}$, no single-tape machine decides whether a partial recursive code halts
on input $n$.

## Sources

- Sipser, Theorem 5.1, for codes of partial recursive functions run on $n$.

Formalized by `Cslib.Decidability.not_singleTapeDecidable_halting`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#not-single-tape-decidable-halting).

## The halting problem for partial recursive codes is recognizable on single-tape machines

For every $n \in \mathbb{N}$, the set of partial recursive codes whose program halts on input $n$
is recognizable by a single-tape machine.

Formalized by `Cslib.Decidability.singleTapeRecognizable_halting`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#single-tape-recognizable-halting).

## The halting problem for partial recursive codes is not co-recognizable on single-tape machines

**The halting problem for partial recursive codes is not co-recognizable on single-tape
machines.** For every $n \in \mathbb{N}$, the set of partial recursive codes whose program halts on
input $n$ is not co-recognizable by a single-tape machine: no single-tape machine halts on exactly
the codes whose program does not halt on input $n$.

## Sources

- Sipser, Corollary 4.23 (there for $A_{TM}$), with partial recursive codes run on $n$.

Formalized by `Cslib.Decidability.not_singleTapeCoRecognizable_halting`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/SingleTape/Bridge.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html#not-single-tape-co-recognizable-halting).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Single-tape machines decide the recursive predicates](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/equivalence-of-models/single-tape-machines-decide-the-recursive-predic)
