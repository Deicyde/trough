---
declaration: theorem
origin: cited
lean: OeisA245212.conjecture
statement: formalized
---

# Difference between $n \tau(n)$ and $\sum_{d \mid n, d < n} d \tau(d)$

> The sequence $a(n) = n \tau(n) - \sum_{d \mid n, d < n} d \tau(d)$, where $\tau(n)$ is the number
> of divisors of $n$.
>
> *References:*
> - [A245212](https://oeis.org/A245212)

*Quoted from [FormalConjectures/OEIS/245212.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/245212.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA245212.conjecture`

Open: stated without proof.

> Conjecture: $a(n) = \sigma(n)$ iff $n$ is a power of $2$ (A000079).

```lean
theorem conjecture (n : ℕ) (h : 0 < n) :
    a n = (σ 1 n : ℤ) ↔ ∃ k : ℕ, n = 2 ^ k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/245212.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/245212.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/245212.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/245212.lean)
- [A245212](https://oeis.org/A245212)
