---
declaration: section
origin: cited
lean: Cslib.Decidability.charFun, Cslib.Decidability.computablePred_iff_partrec_charFun, Cslib.Decidability.ComputablePred.of_turingReducible, Cslib.Decidability.haltingSet, Cslib.Decidability.not_turingReducible_halting, Cslib.Decidability.turingReducible_of_manyOneReducible, Cslib.Decidability.turingEquivalent_charFun_not, Cslib.Decidability.not_manyOneReducible_not_halting
statement: formalized
proof: formalized
---

# Turing reducibility

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-reducibility/index.html).

## Characteristic function of a set of naturals

The characteristic function of a set $p$ of
natural numbers is the partial function $\mathbb{N} \rightharpoonup \mathbb{N}$ that is defined at
every $n$, with value $1$ if $n \in p$ and value $0$ otherwise.

Formalized by `Cslib.Decidability.charFun`, a definition declared in [CSLibExt/Computability/Decidability/TuringReducible.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/TuringReducible.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-reducibility/index.html#char-fun).

## A set is decidable iff its characteristic function is partial recursive

A set $p$ of
natural numbers is decidable (computable as a predicate) if and only if its characteristic function
is partial recursive.

Formalized by `Cslib.Decidability.computablePred_iff_partrec_charFun`, a theorem declared in [CSLibExt/Computability/Decidability/TuringReducible.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/TuringReducible.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-reducibility/index.html#computable-pred-iff-partrec-char-fun).

## Decidability transfers down Turing reducibility

Let $p$ and $q$ be sets of natural numbers
such that the characteristic function of $p$ is Turing reducible to the characteristic function of
$q$. If $q$ is decidable, then $p$ is decidable.

Formalized by `Cslib.Decidability.ComputablePred.of_turingReducible`, a theorem declared in [CSLibExt/Computability/Decidability/TuringReducible.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/TuringReducible.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-reducibility/index.html#of-turing-reducible).

## Halting set

Fix the standard bijective numbering $n \mapsto c_n$ of the codes of partial
recursive functions $\mathbb{N} \rightharpoonup \mathbb{N}$. The halting set is the set of natural
numbers $n$ such that the partial recursive function with code $c_n$ is defined at $0$.

Formalized by `Cslib.Decidability.haltingSet`, a definition declared in [CSLibExt/Computability/Decidability/TuringReducible.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/TuringReducible.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-reducibility/index.html#halting-set).

## The halting set is not Turing reducible to a decidable set

For every decidable set $q$ of
natural numbers, the characteristic function of the halting set is not Turing reducible to the
characteristic function of $q$.

Formalized by `Cslib.Decidability.not_turingReducible_halting`, a theorem declared in [CSLibExt/Computability/Decidability/TuringReducible.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/TuringReducible.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-reducibility/index.html#not-turing-reducible-halting).

## Many-one reducibility implies Turing reducibility

If $p$ and $q$ are sets of natural
numbers and $p$ is many-one reducible to $q$, that is, there is a computable
$f : \mathbb{N} \to \mathbb{N}$ with $n \in p \iff f(n) \in q$ for all $n$, then the characteristic
function of $p$ is Turing reducible to the characteristic function of $q$.

Formalized by `Cslib.Decidability.turingReducible_of_manyOneReducible`, a theorem declared in [CSLibExt/Computability/Decidability/TuringReducible.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/TuringReducible.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-reducibility/index.html#turing-reducible-of-many-one-reducible).

## Every set is Turing equivalent to its complement

For every set $p$ of natural numbers,
the characteristic function of the complement $\mathbb{N} \setminus p$ and the characteristic
function of $p$ are Turing equivalent: each is Turing reducible to the other.

Formalized by `Cslib.Decidability.turingEquivalent_charFun_not`, a theorem declared in [CSLibExt/Computability/Decidability/TuringReducible.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/TuringReducible.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-reducibility/index.html#turing-equivalent-char-fun-not).

## The complement of the halting set is not many-one reducible to it

There is no computable
function $f : \mathbb{N} \to \mathbb{N}$ such that, for every $n$, $n$ is outside the halting set
if and only if $f(n)$ is in the halting set.

The halting set is recognizable and its complement is not. Since every set is Turing equivalent to
its complement, Turing reducibility is strictly coarser than many-one reducibility.

Formalized by `Cslib.Decidability.not_manyOneReducible_not_halting`, a theorem declared in [CSLibExt/Computability/Decidability/TuringReducible.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/TuringReducible.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-reducibility/index.html#not-many-one-reducible-not-halting).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Turing reducibility](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-reducibility/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/degrees-and-hierarchies/turing-reducibility)
