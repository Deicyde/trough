---
declaration: theorem
origin: cited
lean: OeisA233864.conjecture_1, OeisA233864.conjecture_2
statement: formalized
---

# Values $m = \sigma(k)$ ($0 < m < 2n$) with $2n - 1 - m$ and $2n - 1 + m$ prime

> Let $\sigma$ denote the sum-of-divisors function. The sequence $a(n)$ counts the integers
> $0 < m < 2n$ of the form $m = \sigma(k)$ ($k > 0$) such that $2n - 1 - m$ and $2n - 1 + m$ are
> both prime.
>
> *References:*
> - [A233864](https://oeis.org/A233864)

*Quoted from [FormalConjectures/OEIS/233864.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/233864.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 6 test statements, counted here but not shown.

## `OeisA233864.conjecture_1`

Open: stated without proof.

> Conjecture (i): $a(n) > 0$ for all $n > 3$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 3 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/233864.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/233864.lean#L78).

## `OeisA233864.conjecture_2`

Open: stated without proof.

> Conjecture (ii): For any even number $2n > 0$, $2n + \sigma(k)$ is prime for some $0 < k < 2n$.

```lean
theorem conjecture_2 (n : ℕ) (hn : 0 < n) :
    ∃ k, 0 < k ∧ k < 2 * n ∧ Nat.Prime (2 * n + σ 1 k)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/233864.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/233864.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/233864.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/233864.lean)
- [A233864](https://oeis.org/A233864)
