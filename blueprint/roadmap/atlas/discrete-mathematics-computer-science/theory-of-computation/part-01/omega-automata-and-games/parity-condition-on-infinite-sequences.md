---
declaration: section
origin: cited
lean: Cslib.ωSequence.IsMaxInfOcc, Cslib.ωSequence.ParityEven, Cslib.ωSequence.ParityOdd, Cslib.ωSequence.exists_isMaxInfOcc, Cslib.ωSequence.IsMaxInfOcc.eventually_le, Cslib.ωSequence.parityOdd_iff_not_parityEven, Cslib.ωSequence.parityEven_iff_frequently_two, Cslib.ωSequence.isMaxInfOcc_drop_iff
statement: formalized
proof: formalized
---

# Parity condition on infinite sequences

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-condition-on-infinite-sequences/index.html).

## Largest infinitely occurring value

Let $(p_k)_{k \in \mathbb{N}}$ be a sequence of natural
numbers and $n \in \mathbb{N}$. Then $n$ is the largest value occurring infinitely often in
$(p_k)$ if $p_k = n$ for infinitely many $k$, and every $m \in \mathbb{N}$ with $p_k = m$ for
infinitely many $k$ satisfies $m \le n$.

Larger values may still occur, each only finitely often; for bounded sequences they eventually
stop occurring.

Formalized by `Cslib.ωSequence.IsMaxInfOcc`, a definition declared in [CSLibExt/Foundations/Data/OmegaSequence/Parity.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Data/OmegaSequence/Parity.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-condition-on-infinite-sequences/index.html#is-max-inf-occ).

## Even max-parity condition

A sequence $(p_k)_{k \in \mathbb{N}}$ of natural numbers
(priorities) satisfies the even max-parity condition if there is an even $n$ that is the largest
value occurring infinitely often in $(p_k)$.

This is the winning condition of the even player under the max-parity convention.

Formalized by `Cslib.ωSequence.ParityEven`, a definition declared in [CSLibExt/Foundations/Data/OmegaSequence/Parity.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Data/OmegaSequence/Parity.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-condition-on-infinite-sequences/index.html#parity-even).

## Odd max-parity condition

A sequence $(p_k)_{k \in \mathbb{N}}$ of natural numbers
(priorities) satisfies the odd max-parity condition if there is an odd $n$ that is the largest
value occurring infinitely often in $(p_k)$.

This is the winning condition of the odd player under the max-parity convention.

Formalized by `Cslib.ωSequence.ParityOdd`, a definition declared in [CSLibExt/Foundations/Data/OmegaSequence/Parity.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Data/OmegaSequence/Parity.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-condition-on-infinite-sequences/index.html#parity-odd).

## Bounded sequences have a largest infinitely occurring value

Let $d \in \mathbb{N}$. If a
sequence $(p_k)_{k \in \mathbb{N}}$ of natural numbers satisfies $p_k \le d$ for all $k$, then some
natural number $n \le d$ is the largest value occurring infinitely often in $(p_k)$.

Formalized by `Cslib.ωSequence.exists_isMaxInfOcc`, a theorem declared in [CSLibExt/Foundations/Data/OmegaSequence/Parity.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Data/OmegaSequence/Parity.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-condition-on-infinite-sequences/index.html#exists-is-max-inf-occ).

## The tail of a bounded sequence is bounded by its largest infinitely occurring value

Let
$d \in \mathbb{N}$, let $(p_k)_{k \in \mathbb{N}}$ be a sequence of natural numbers with $p_k \le d$
for all $k$, and let $n$ be the largest value occurring infinitely often in $(p_k)$. Then
$p_k \le n$ for all sufficiently large $k$.

Formalized by `Cslib.ωSequence.IsMaxInfOcc.eventually_le`, a theorem declared in [CSLibExt/Foundations/Data/OmegaSequence/Parity.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Data/OmegaSequence/Parity.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-condition-on-infinite-sequences/index.html#eventually-le).

## For bounded sequences the odd parity condition is the negation of the even one

Let
$d \in \mathbb{N}$. If a sequence $(p_k)_{k \in \mathbb{N}}$ of natural numbers satisfies
$p_k \le d$ for all $k$, then it satisfies the odd max-parity condition if and only if it does not
satisfy the even max-parity condition.

Formalized by `Cslib.ωSequence.parityOdd_iff_not_parityEven`, a theorem declared in [CSLibExt/Foundations/Data/OmegaSequence/Parity.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Data/OmegaSequence/Parity.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-condition-on-infinite-sequences/index.html#parity-odd-iff-not-parity-even).

## Max-parity with priorities 1 and 2 is the Büchi condition

Let $(p_k)_{k \in \mathbb{N}}$ be
a sequence of natural numbers with $p_k \in \{1, 2\}$ for every $k$. Then $(p_k)$ satisfies the even
max-parity condition if and only if $p_k = 2$ for infinitely many $k$.

Formalized by `Cslib.ωSequence.parityEven_iff_frequently_two`, a theorem declared in [CSLibExt/Foundations/Data/OmegaSequence/Parity.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Data/OmegaSequence/Parity.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-condition-on-infinite-sequences/index.html#parity-even-iff-frequently-two).

## Prefix independence of the largest infinitely occurring value

Let
$(p_k)_{k \in \mathbb{N}}$ be a sequence of natural numbers and let $j, n \in \mathbb{N}$. Then
$n$ is the largest value occurring infinitely often in the shifted sequence
$(p_{j+k})_{k \in \mathbb{N}}$ if and only if $n$ is the largest value occurring infinitely often
in $(p_k)$.

Formalized by `Cslib.ωSequence.isMaxInfOcc_drop_iff`, a theorem declared in [CSLibExt/Foundations/Data/OmegaSequence/Parity.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Foundations/Data/OmegaSequence/Parity.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-condition-on-infinite-sequences/index.html#is-max-inf-occ-drop-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Parity condition on infinite sequences](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/omega-automata-and-games/parity-condition-on-infinite-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/omega-automata-and-games/parity-condition-on-infinite-sequences)
