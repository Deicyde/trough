---
declaration: theorem
origin: cited
lean: OeisA243512.conjecture
statement: formalized
---

# Least index $i$ for which $\text{num}(\sigma_1(i)/i) - \text{den}(\sigma_1(i)/i) = n$

> Let $A243473(i)$ be the difference between the numerator $p$ and the denominator $q$
> when the abundancy index $\sigma_1(i) / i$ is written in lowest terms $p / q$.
> The sequence $a(n)$ is the least positive integer $i$ such that $A243473(i) = n$,
> or $0$ if no such index exists.
>
> *References:*
> - [A243512](https://oeis.org/A243512)

*Quoted from [FormalConjectures/OEIS/243512.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/243512.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA243512.conjecture`

Open: stated without proof.

> Motivated by the observation that some small numbers $(2, 12, 14, 18, \dots)$ occur only very late in
> the recently added sequence A243473, but all numbers seem to appear sooner or later. (The definition
> is completed by "$0$ if no such index exists" to guarantee well-definedness in absence of a proof,
> but I conjecture that no such $0$ will ever occur.)

```lean
theorem conjecture (n : ℕ) : a n ≠ 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/243512.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/243512.lean#L76).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/243512.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/243512.lean)
- [A243512](https://oeis.org/A243512)
