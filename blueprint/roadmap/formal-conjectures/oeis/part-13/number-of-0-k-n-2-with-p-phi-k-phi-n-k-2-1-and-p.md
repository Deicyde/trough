---
declaration: theorem
origin: cited
lean: OeisA236097.conjecture
statement: formalized
---

# Number of $0 < k < n-2$ with $p = \phi(k) + \phi(n-k)/2 + 1$ and $p_p - p \pm 1$ prime

> Let $\phi$ denote Euler's totient function and $p_m$ denote the $m$-th prime number.
> The sequence $a(n)$ counts the number of integers $0 < k < n - 2$ such that
> $p = \phi(k) + \phi(n-k)/2 + 1$, $p_p - p - 1$, and $p_p - p + 1$ are all prime.
>
> *References:*
> - [A236097](https://oeis.org/A236097)

*Quoted from [FormalConjectures/OEIS/236097.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/236097.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 6 test statements, counted here but not shown.

## `OeisA236097.conjecture`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 31$.

```lean
theorem conjecture (n : ℕ) (hn : 31 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/236097.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/236097.lean#L93).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/236097.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/236097.lean)
- [A236097](https://oeis.org/A236097)
