---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ErdosProblem358IntervalSumsWanted.RepCount, MathlibExt.NumberTheory.ErdosProblem358IntervalSumsWanted.conjecture, MathlibExt.NumberTheory.ErdosProblem358IntervalSumsWanted.conjecture_holds
statement: formalized
---

# Sums of consecutive terms of a sequence

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-consecutive-terms-of-a-sequence/index.html).

## Interval-sum representation count

For a sequence $a_0, a_1, a_2, \ldots$ of natural
numbers and a natural number $n$, $f_a(n)$ is the number of pairs $(u, v)$ of natural numbers
with $u \le v$ and $a_u + a_{u+1} + \cdots + a_v = n$, and $f_a(n) = 0$ if there are infinitely
many such pairs.

The sequence is indexed from $0$ rather than from $1$ as in the source; this does not change the
count. When the sequence is strictly increasing with positive terms there are only finitely many
such pairs, so $f_a(n)$ is then the true number of representations.

Formalized by `MathlibExt.NumberTheory.ErdosProblem358IntervalSumsWanted.RepCount`, a definition declared in [WantedExt/NumberTheory/ErdosProblem358IntervalSumsWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem358IntervalSumsWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-consecutive-terms-of-a-sequence/index.html#rep-count).

## The interval-sum conjecture of Erdős Problem 358

This is the proposition that there is a
strictly increasing sequence $a_0 < a_1 < a_2 < \cdots$ of positive integers whose interval-sum
representation count $f(n)$, the number of pairs $(u, v)$ of natural numbers with $u \le v$ and
$a_u + a_{u+1} + \cdots + a_v = n$, tends to infinity as $n \to \infty$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem358IntervalSumsWanted.conjecture`, a definition declared in [WantedExt/NumberTheory/ErdosProblem358IntervalSumsWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem358IntervalSumsWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-consecutive-terms-of-a-sequence/index.html#conjecture).

## Interval sums with unbounded representation counts (Erdős Problem 358)

There is a
strictly increasing sequence $a_0 < a_1 < a_2 < \cdots$ of positive integers such that the
number $f(n)$ of pairs $(u, v)$ of natural numbers with $u \le v$ and
$a_u + a_{u+1} + \cdots + a_v = n$ tends to infinity as $n \to \infty$.

Resolved true: Resolved by Tao's February 2026 construction of a set A of positive integers with
f(n) >> log n for all large n, hence f(n) -> infinity (Erdos Problems record 358, [Ta26]).

## Sources

- Terence Tao, construction of a set A of positive integers with f(n) >> log n for Erdos Problem 358, February 2026, https://terrytao.wordpress.com/wp-content/uploads/2026/02/erdos-358-2.pdf.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem358IntervalSumsWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem358IntervalSumsWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem358IntervalSumsWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-consecutive-terms-of-a-sequence/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sums of consecutive terms of a sequence](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-consecutive-terms-of-a-sequence/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/additive-number-theory/sums-of-consecutive-terms-of-a-sequence)
