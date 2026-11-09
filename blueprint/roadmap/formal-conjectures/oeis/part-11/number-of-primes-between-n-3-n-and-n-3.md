---
declaration: theorem
origin: cited
lean: OeisA216265.conjecture
statement: formalized
---

# Number of primes between $n^3 - n$ and $n^3$

> For $n \ge 1$, $a(n)$ is the number of primes $p$ satisfying $n^3 - n < p \le n^3$,
> given by $\pi(n^3) - \pi(n^3 - n)$.
>
> *References:*
> - [A216265](https://oeis.org/A216265)

*Quoted from [FormalConjectures/OEIS/216265.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/216265.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 6 test statements, counted here but not shown.

## `OeisA216265.conjecture`

Open: stated without proof.

> Conjecture: For every $n > 13$, $a(n) > 0$.

```lean
theorem conjecture (n : ℕ) (hn : 13 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/216265.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/216265.lean#L105).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/216265.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/216265.lean)
- [A216265](https://oeis.org/A216265)
