---
declaration: theorem
origin: cited
lean: GoldbachConjecture.goldbach, TernaryGoldbachConjecture.ternaryGoldbach
statement: formalized
---

# Goldbach's conjecture

> *References:*
> - [Landau Problems Wikipedia Page](https://en.wikipedia.org/wiki/Landau%27s_problems#Twin_prime_conjecture)
> - [Goldbach's Conjecture Wikipedia Page](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture)

*Quoted from [FormalConjectures/Wikipedia/GoldbachConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/GoldbachConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved.

## `GoldbachConjecture.goldbach`

Open: stated without proof.

> Can every even integer greater than 2 be written as the sum of two primes?

```lean
theorem goldbach :
    ∀ n : ℕ, 2 < n → Even n → ∃ p q, Prime p ∧ Prime q ∧ n = p + q
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/GoldbachConjecture.lean, line 36](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/GoldbachConjecture.lean#L36).

## `TernaryGoldbachConjecture.ternaryGoldbach`

Solved: stated here without proof.

> Can every odd integer greater than 5 be written as the sum of three primes?
> (A prime may be used more than once.)
>
> NB. While Harald Helfgott's solution is not published in a peer-reviewed journal yet,
> his results seem generally accepted.

```lean
theorem ternaryGoldbach (n : ℕ) (hn : 5 < n) (hn_odd : Odd n) :
    ∃ p q r, Nat.Prime p ∧ Nat.Prime q ∧ Nat.Prime r ∧ n = p + q + r
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/GoldbachConjecture.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/GoldbachConjecture.lean#L52).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/GoldbachConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/GoldbachConjecture.lean)
- [Landau Problems Wikipedia Page](https://en.wikipedia.org/wiki/Landau%27s_problems#Twin_prime_conjecture)
