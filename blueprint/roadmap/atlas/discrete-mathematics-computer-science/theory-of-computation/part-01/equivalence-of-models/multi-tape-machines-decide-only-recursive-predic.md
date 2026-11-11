---
declaration: section
origin: cited
lean: Cslib.Decidability.MultiTapeDecidable, Cslib.Decidability.MultiTapeRecognizable, Cslib.Decidability.MultiTapeCoRecognizable, Cslib.Decidability.MultiTapeRecognizable.rePred, Cslib.Decidability.MultiTapeDecidable.rePred, Cslib.Decidability.MultiTapeDecidable.rePred_not, Cslib.Decidability.MultiTapeDecidable.computablePred, Cslib.Decidability.multiTapeDecidable_implies_tm2Decidable
statement: formalized
proof: formalized
---

# Multi-tape machines decide only recursive predicates

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/multi-tape-machines-decide-only-recursive-predic/index.html).

## Decidability by multi-tape machines

Let $\alpha$ be a primcodable type (it has an
encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is primitive recursive). A
predicate $p$ on $\alpha$ is decidable by a multi-tape machine when there are a number $k$ and a
deterministic Turing machine $M$ with finitely many states, a read-only input tape, $k$ work tapes
and a write-only output tape, all over the Boolean alphabet, such that for every $a \in \alpha$
there is a Boolean $b$ for which $M$ computes the one-letter word $b$ on the binary word of
$\mathrm{encode}(a)$ (least significant bit first), and $b$ is true exactly when $p(a)$ holds.
Here $M$ computes a word $v$ on an input word $w$ when its run started on $w$ halts with $v$ on
its output tape.

Formalized by `Cslib.Decidability.MultiTapeDecidable`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Bridge.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/Bridge.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/multi-tape-machines-decide-only-recursive-predic/index.html#multi-tape-decidable).

## Recognizability by multi-tape machines

Let $\alpha$ be a primcodable type (it has an
encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is primitive recursive). A
predicate $p$ on $\alpha$ is recognizable by a multi-tape machine when there are a number $k$ and
a deterministic Turing machine $M$ with finitely many states, a read-only input tape, $k$ work
tapes and a write-only output tape, all over the Boolean alphabet, such that for every
$a \in \alpha$, the run of $M$ started on the binary word of $\mathrm{encode}(a)$ (least
significant bit first) halts if and only if $p(a)$ holds.

Formalized by `Cslib.Decidability.MultiTapeRecognizable`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Bridge.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/Bridge.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/multi-tape-machines-decide-only-recursive-predic/index.html#multi-tape-recognizable).

## Co-recognizability by multi-tape machines

Let $\alpha$ be a primcodable type (it has an
encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is primitive recursive). A
predicate $p$ on $\alpha$ is co-recognizable by a multi-tape machine when its complement
$\neg p$ is recognizable by a multi-tape machine.

Formalized by `Cslib.Decidability.MultiTapeCoRecognizable`, a definition declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Bridge.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/Bridge.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/multi-tape-machines-decide-only-recursive-predic/index.html#multi-tape-co-recognizable).

## A predicate recognizable by a multi-tape machine is recursively enumerable

Let $\alpha$
be a primcodable type (it has an encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding
is primitive recursive). If a predicate $p$ on $\alpha$ is recognizable by a multi-tape machine,
then $p$ is recursively enumerable, that is, the partial function on $\alpha$ that is defined,
with a trivial value, exactly where $p$ holds is partial recursive.

Formalized by `Cslib.Decidability.MultiTapeRecognizable.rePred`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Bridge.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/Bridge.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/multi-tape-machines-decide-only-recursive-predic/index.html#re-pred).

## A predicate decided by a multi-tape machine is recursively enumerable

Let $\alpha$ be a
primcodable type (it has an encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is
primitive recursive). If a predicate $p$ on $\alpha$ is decidable by a multi-tape machine, then
$p$ is recursively enumerable, that is, the partial function on $\alpha$ that is defined, with a
trivial value, exactly where $p$ holds is partial recursive.

Formalized by `Cslib.Decidability.MultiTapeDecidable.rePred`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Bridge.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/Bridge.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/multi-tape-machines-decide-only-recursive-predic/index.html#re-pred-2).

## A predicate decided by a multi-tape machine has a recursively enumerable complement

Let
$\alpha$ be a primcodable type (it has an encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose
decoding is primitive recursive). If a predicate $p$ on $\alpha$ is decidable by a multi-tape
machine, then its complement $\neg p$ is recursively enumerable, that is, the partial function on
$\alpha$ that is defined, with a trivial value, exactly where $\neg p$ holds is partial
recursive.

Formalized by `Cslib.Decidability.MultiTapeDecidable.rePred_not`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Bridge.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/Bridge.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/multi-tape-machines-decide-only-recursive-predic/index.html#re-pred-not).

## A predicate decided by a multi-tape machine is computable

Let $\alpha$ be a primcodable
type (it has an encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is primitive
recursive). If a predicate $p$ on $\alpha$ is decidable by a multi-tape machine, then $p$ is
computable, that is, $p$ is decidable and its Boolean characteristic function
$\alpha \to \mathrm{Bool}$ is computable.

This is Post's theorem applied to $p$ and its complement, both recursively enumerable.

Formalized by `Cslib.Decidability.MultiTapeDecidable.computablePred`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Bridge.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/Bridge.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/multi-tape-machines-decide-only-recursive-predic/index.html#computable-pred).

## Multi-tape machines decide no more than multi-stack machines

Let $\alpha$ be a
primcodable type (it has an encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is
primitive recursive). Every predicate on $\alpha$ that is decidable by a multi-tape machine is
decidable by a multi-stack machine.

Formalized by `Cslib.Decidability.multiTapeDecidable_implies_tm2Decidable`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Bridge.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/Bridge.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/multi-tape-machines-decide-only-recursive-predic/index.html#multi-tape-decidable-implies-tm2-decidab).

## Multi-tape machines recognize no more than multi-stack machines

Let $\alpha$ be a
primcodable type (it has an encoding $\mathrm{encode} : \alpha \to \mathbb{N}$ whose decoding is
primitive recursive). Every predicate on $\alpha$ that is recognizable by a multi-tape machine is
recognizable by a multi-stack machine.

Formalized by `Cslib.Decidability.multiTapeRecognizable_implies_tm2Recognizable`, a theorem declared in [CSLibExt/Computability/Machines/Turing/MultiTape/Bridge.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Machines/Turing/MultiTape/Bridge.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/multi-tape-machines-decide-only-recursive-predic/index.html#multi-tape-recognizable-implies-tm2-reco).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multi-tape machines decide only recursive predicates](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/multi-tape-machines-decide-only-recursive-predic/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/equivalence-of-models/multi-tape-machines-decide-only-recursive-predic)
