---
declaration: section
origin: cited
lean: MetaMathlibExt.IsIntegerCFiniteSequence, MetaMathlibExt.isIntegerCFiniteSequence_of_isSolution, MetaMathlibExt.isSolution_tail_of_cFiniteWitness, MetaMathlibExt.IsIntegerCFiniteSequence.exists_isSolution_tail
statement: formalized
proof: formalized
---

# C-finite sequences

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/c-finite-sequences/index.html).

## C-finite integer sequences

An integer sequence $s \colon \mathbb{N} \to \mathbb{Z}$ is
C-finite if there are $p, q \in \mathbb{N}$ and integers $c_0, \dots, c_{p-1}$ such that
$s(n + p) = \sum_{i=0}^{p-1} c_i \, s(n + i)$ for every $n \ge q$.

## Sources

- JIS VOL26/Fischer–Kotek–Makowsky, <https://cs.uwaterloo.ca/journals/JIS/VOL26/Makowsky/makowsky16.tex>, lines 249–259.

Formalized by `MetaMathlibExt.IsIntegerCFiniteSequence`, a definition declared in [MathlibExt/NumberTheory/CFiniteSequence.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CFiniteSequence.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/c-finite-sequences/index.html#is-integer-cfinite-sequence).

## Solutions of linear recurrences are C-finite

Let $p \in \mathbb{N}$ and let
$c_0, \dots, c_{p-1}$ be integers. If an integer sequence $s$ satisfies
$s(n + p) = \sum_{i=0}^{p-1} c_i \, s(n + i)$ for every $n \in \mathbb{N}$, then $s$ is C-finite.

Formalized by `MetaMathlibExt.isIntegerCFiniteSequence_of_isSolution`, a theorem declared in [MathlibExt/NumberTheory/CFiniteSequence.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CFiniteSequence.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/c-finite-sequences/index.html#is-integer-cfinite-sequence-of-is-soluti).

## Discarding the exceptional prefix of a C-finite recurrence

Let $s$ be an integer
sequence, let $p, q \in \mathbb{N}$ and let $c_0, \dots, c_{p-1}$ be integers. If
$s(n + p) = \sum_{i=0}^{p-1} c_i \, s(n + i)$ for every $n \ge q$, then the shifted sequence
$t(n) = s(n + q)$ satisfies $t(n + p) = \sum_{i=0}^{p-1} c_i \, t(n + i)$ for every
$n \in \mathbb{N}$.

Formalized by `MetaMathlibExt.isSolution_tail_of_cFiniteWitness`, a theorem declared in [MathlibExt/NumberTheory/CFiniteSequence.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CFiniteSequence.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/c-finite-sequences/index.html#is-solution-tail-of-c-finite-witness).

## A tail of a C-finite sequence satisfies a linear recurrence

If an integer sequence $s$
is C-finite, then there are a shift $q \in \mathbb{N}$, an order $p \in \mathbb{N}$ and integers
$c_0, \dots, c_{p-1}$ such that the shifted sequence $t(n) = s(n + q)$ satisfies
$t(n + p) = \sum_{i=0}^{p-1} c_i \, t(n + i)$ for every $n \in \mathbb{N}$.

Formalized by `MetaMathlibExt.IsIntegerCFiniteSequence.exists_isSolution_tail`, a theorem declared in [MathlibExt/NumberTheory/CFiniteSequence.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CFiniteSequence.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/c-finite-sequences/index.html#exists-is-solution-tail).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: C-finite sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/c-finite-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/recurrence-theory/c-finite-sequences)
