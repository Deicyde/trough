---
declaration: theorem
origin: cited
lean: OeisA234809.conjecture
statement: formalized
---

# Number of integers $0 < k < n$ such that $p = k + \phi(n - k)$ and $2(n - p) + 1$ are both prime

> Let $\phi$ denote Euler's totient function. The sequence $a(n)$ counts the integers $0 < k < n$
> such that $p = k + \phi(n - k)$ and $2(n - p) + 1$ are both prime.
>
> *References:*
> - [A234809](https://oeis.org/A234809)

*Quoted from [FormalConjectures/OEIS/234809.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/234809.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA234809.conjecture`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 2$.

```lean
theorem conjecture (n : ℕ) (hn : 2 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/234809.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/234809.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/234809.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/234809.lean)
- [A234809](https://oeis.org/A234809)
