---
declaration: section
origin: cited
lean: Cslib.Computability.Turing.SingleTape.SingleTapeNTM.accepts_iff_exists_labels, Cslib.Computability.Turing.SingleTape.SingleTapeNTM.accepts_append, Cslib.Computability.Turing.SingleTape.SingleTapeNTM.accepts_of_accepts_nil, Cslib.Computability.Turing.SingleTape.SingleTapeNTM.not_forall_accepts_encodeNat_iff_eq_zero, Cslib.Computability.Turing.SingleTape.SingleTapeNTM.rePred_accepts, Cslib.Decidability.singleTapeRecognizable_accepts, Cslib.Decidability.singleTapeRecognizable_accepts_comp, Cslib.Decidability.SingleTapeNTMRecognizable
statement: formalized
proof: formalized
---

# Nondeterministic Turing machines

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/nondeterministic-turing-machines/index.html).

## Single Tape NTM

## Acceptance as a label list

A single-tape nondeterministic Turing machine $m$ accepts a
word $x$ if and only if there is a list $\mu$ of transition labels (read a symbol, write a symbol,
move, skip) such that applying the labels of $\mu$ in order to the input tape of $x$ (the tape
holding $x$ from the head cell rightward, every other cell blank) never fails, that is, every read
label finds its symbol in the cell under the head, and $\mu$ leads the automaton of $m$ from some
start state to some accepting state.

Formalized by `Cslib.Computability.Turing.SingleTape.SingleTapeNTM.accepts_iff_exists_labels`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/nondeterministic-turing-machines/index.html#accepts-iff-exists-labels).

## Acceptance is closed under extension on the right

If a single-tape nondeterministic
Turing machine $m$ accepts a word $x$ over its tape alphabet, then $m$ accepts $xy$ for every word
$y$ over that alphabet.

This is a defect of CSLib's definition of these machines: a transition can only test the cell
under the head for a symbol, never for a blank, so every cell that an accepting run on $x$ reads
holds a letter of $x$ or one the run wrote, and the same run accepts $xy$.

## Sources

- defect of the pinned CSLib definition, fixed upstream by leanprover/cslib#1039.

Formalized by `Cslib.Computability.Turing.SingleTape.SingleTapeNTM.accepts_append`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/nondeterministic-turing-machines/index.html#accepts-append).

## An NTM that accepts the empty word accepts every word

If a single-tape nondeterministic
Turing machine $m$ accepts the empty word, then $m$ accepts every word over its tape alphabet.

This is a special case of acceptance being closed under extension on the right, a defect of
CSLib's definition of these machines.

Formalized by `Cslib.Computability.Turing.SingleTape.SingleTapeNTM.accepts_of_accepts_nil`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/nondeterministic-turing-machines/index.html#accepts-of-accepts-nil).

## No NTM accepts exactly the binary code of $0$

Let $m$ be a single-tape nondeterministic
Turing machine with tape alphabet $\Sigma$, and let $\iota$ be any map from the bits to $\Sigma$.
For a natural number $n$, write $w_n$ for the word over $\Sigma$ obtained by applying $\iota$
letter by letter to the little-endian binary code of $n$, in which $0$ is coded by the empty word.
Then it is not the case that, for every natural number $n$, $m$ accepts $w_n$ if and only if
$n = 0$.

The word $w_0$ is empty, and a machine that accepts the empty word accepts every word, in
particular $w_1$.

Formalized by `Cslib.Computability.Turing.SingleTape.SingleTapeNTM.not_forall_accepts_encodeNat_iff_eq_zero`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/nondeterministic-turing-machines/index.html#not-forall-accepts-encode-nat-iff-eq-zer).

## Acceptance by an NTM with finite state and tape alphabets is r.e

**Acceptance by an NTM with finite state and tape alphabets is r.e.** in the input word
(Sipser, Theorem 3.16, through recursion theory): search for a label list that applies to the
input tape, checked on coded tapes, and along which the image of the start states, a finite set,
meets the accepting states.

Formalized by `Cslib.Computability.Turing.SingleTape.SingleTapeNTM.rePred_accepts`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/nondeterministic-turing-machines/index.html#re-pred-accepts).

## Deterministic machines recognize NTM acceptance

Let $m$ be a single-tape nondeterministic
Turing machine with a finite set of states and a finite tape alphabet $\Sigma$ that has decidable
equality and a primitive recursive encoding. Then the predicate on words over $\Sigma$ that holds
at a word exactly when $m$ accepts it is recognizable by a single-tape deterministic Turing
machine.

## Sources

- Sipser, Theorem 3.16.

Formalized by `Cslib.Decidability.singleTapeRecognizable_accepts`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/nondeterministic-turing-machines/index.html#single-tape-recognizable-accepts).

## Deterministic machines recognize NTM acceptance along a computable map

Let $m$ be a
single-tape nondeterministic Turing machine with a finite set of states and a finite tape alphabet
$\Sigma$ that has decidable equality and a primitive recursive encoding. Let $\alpha$ be a
primitively encodable type and $f$ a computable map from $\alpha$ to words over $\Sigma$. Then the
predicate on $\alpha$ that holds at $a$ exactly when $m$ accepts $f(a)$ is recognizable by a
single-tape deterministic Turing machine.

## Sources

- Sipser, Theorem 3.16.

Formalized by `Cslib.Decidability.singleTapeRecognizable_accepts_comp`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/nondeterministic-turing-machines/index.html#single-tape-recognizable-accepts-comp).

## Predicates recognizable by a single-tape nondeterministic machine

Let $\alpha$ be a type
with a primitive recursive encoding into $\mathbb{N}$. A predicate $p$ on $\alpha$ is recognizable
by a single-tape nondeterministic machine when there are a finite set of states, a finite tape
alphabet $\Sigma$ with decidable equality, an injective map $\iota$ from the bits $\{0, 1\}$ to
$\Sigma$ and a single-tape nondeterministic Turing machine $M$ with these states over $\Sigma$
such that for every $a \in \alpha$, $M$ accepts the input word obtained by writing the binary
encoding of the code of $a$ in $\mathbb{N}$ letter by letter through $\iota$ if and only if
$p(a)$ holds. Here $M$ accepts a word when some run of $M$ from one of its start states on the
tape holding the word, with the head on its first symbol, reaches an accepting state.

In this model a machine cannot test whether a cell is blank, so a machine that accepts a word
accepts every extension of the word on the right. Every such predicate is recognizable by a
single-tape deterministic machine, but not conversely: the predicate $n = 0$ on $\mathbb{N}$ is
decidable by a single-tape deterministic machine and is not recognizable by a single-tape
nondeterministic machine.

## Sources

- the pinned CSLib definition of nondeterministic machines; the upstream PR leanprover/cslib#1039 lets machines read and write blank cells.

Formalized by `Cslib.Decidability.SingleTapeNTMRecognizable`, a definition declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean, line 410](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean#L410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/nondeterministic-turing-machines/index.html#single-tape-ntmrecognizable).

## A predicate recognized by a single-tape NTM is recognized by a deterministic single-tape machine

**A predicate recognized by a single-tape NTM is recognized by a deterministic single-tape
machine** (Sipser, Theorem 3.16, through recursion theory).

Formalized by `Cslib.Decidability.SingleTapeNTMRecognizable.singleTapeRecognizable`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/nondeterministic-turing-machines/index.html#single-tape-recognizable).

## No single-tape NTM recognizes $n = 0$

The predicate $n = 0$ on the natural numbers is not
recognizable by any single-tape nondeterministic Turing machine.

The binary code of $0$ is the empty word, and a single-tape nondeterministic machine that accepts
the empty word accepts every word.

## Sources

- defect of the pinned CSLib definition, fixed upstream by leanprover/cslib#1039.

Formalized by `Cslib.Decidability.not_singleTapeNTMRecognizable_eq_zero`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean, line 430](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean#L430). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/nondeterministic-turing-machines/index.html#not-single-tape-ntmrecognizable-eq-zero).

## A decidable predicate that no single-tape NTM recognizes

There is a predicate $p$ on the
natural numbers that is decidable by a single-tape deterministic Turing machine but is not
recognizable by any single-tape nondeterministic Turing machine.

The predicate $n = 0$ is such a predicate.

## Sources

- Sipser, Corollary 3.18, whose half "every Turing-recognizable language is recognized by a nondeterministic machine" fails on the pinned CSLib definition; fixed upstream by leanprover/cslib#1039.

Formalized by `Cslib.Decidability.exists_singleTapeDecidable_not_singleTapeNTMRecognizable`, a theorem declared in [CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean, line 439](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Machines/Turing/SingleTape/Nondeterministic.lean#L439). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/nondeterministic-turing-machines/index.html#exists-single-tape-decidable-not-single).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Nondeterministic Turing machines](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/equivalence-of-models/nondeterministic-turing-machines/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/equivalence-of-models/nondeterministic-turing-machines)
