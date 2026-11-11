---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ErdosProblem851Wanted.HasAtMostRPrimeFactors, MathlibExt.NumberTheory.ErdosProblem851Wanted.Representable, MathlibExt.NumberTheory.ErdosProblem851Wanted.PrimeRepresentable, MathlibExt.NumberTheory.ErdosProblem851Wanted.Statement, MathlibExt.NumberTheory.ErdosProblem851Wanted.Statement_holds
statement: formalized
---

# Romanoff's theorem

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/romanoff-s-theorem/index.html).

## Natural numbers with at most $r$ distinct prime factors

For natural numbers $n$ and $r$,
$n$ has at most $r$ distinct prime factors when $n = 0$ or at most $r$ distinct primes divide $n$;
the number $0$ is counted as having no prime factors.

## Sources

- EP-851 [Erdős Problems].

Formalized by `MathlibExt.NumberTheory.ErdosProblem851Wanted.HasAtMostRPrimeFactors`, a definition declared in [WantedExt/NumberTheory/ErdosProblem851Wanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem851Wanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/romanoff-s-theorem/index.html#has-at-most-rprime-factors).

## Sums of a power of two and a number with few prime factors

For a natural number $r$, a
natural number $m$ is of this form when $m = 2^k + n$ for some natural numbers $k$ and $n$ such
that $n = 0$ or at most $r$ distinct primes divide $n$.

## Sources

- EP-851 [Erdős Problems].

Formalized by `MathlibExt.NumberTheory.ErdosProblem851Wanted.Representable`, a definition declared in [WantedExt/NumberTheory/ErdosProblem851Wanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem851Wanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/romanoff-s-theorem/index.html#representable).

## Sums of a power of two and a prime

A natural number $m$ is of this form when
$m = 2^k + p$ for some natural number $k$ and some prime $p$.

## Sources

- Romanoff's theorem in EP-851 [Erdős Problems].

Formalized by `MathlibExt.NumberTheory.ErdosProblem851Wanted.PrimeRepresentable`, a definition declared in [WantedExt/NumberTheory/ErdosProblem851Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem851Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/romanoff-s-theorem/index.html#prime-representable).

## Erdős Problem 851

The proposition asserts two things. First, the set of natural numbers
of the form $2^k + p$, with $k$ a natural number and $p$ prime, has positive lower density
(Romanoff's theorem). Second, for every real number $\varepsilon > 0$ there is a natural number
$r$ such that the set of natural numbers of the form $2^k + n$, with $k$ and $n$ natural numbers
and with $n = 0$ or at most $r$ distinct primes dividing $n$, has lower density at least
$1 - \varepsilon$.

## Sources

- EP-851 [Erdős Problems].

Formalized by `MathlibExt.NumberTheory.ErdosProblem851Wanted.Statement`, a definition declared in [WantedExt/NumberTheory/ErdosProblem851Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem851Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/romanoff-s-theorem/index.html#statement).

## Erdős Problem 851 is true

The set of natural numbers of the form $2^k + p$, with $k$ a natural
number and $p$ prime, has positive lower density. Moreover, for every real number
$\varepsilon > 0$ there is a natural number $r$ such that the set of natural numbers of the form
$2^k + n$, with $k$ and $n$ natural numbers and with $n = 0$ or at most $r$ distinct primes dividing
$n$, has lower density at least $1 - \varepsilon$.

Romanoff proved the positive-density clause in 1934; Price and GPT-5.2 Pro proved the near-one
density statement affirmatively in 2026.

## Sources

- Lean proof of Erdős Problem 851, https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos851.lean#L37; Yuchen Ding and Wenguang Zhai, A generalization of the Romanoff theorem, arXiv:2401.15892v3 (2024), https://arxiv.org/abs/2401.15892v3.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem851Wanted.Statement_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem851Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem851Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/romanoff-s-theorem/index.html#statement-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Romanoff's theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/romanoff-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/additive-number-theory/romanoff-s-theorem)
