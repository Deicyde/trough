---
declaration: theorem
origin: cited
lean: OeisA230241.conjecture
statement: formalized
---

# Partitions $n = p + q$ with $p$, $3p - 10$, and $(p - 1)q - 1$ prime

> Number of ways to write $n = p + q$ with $p$, $3p - 10$ and $(p-1)q - 1$ all prime, where $q$ is a
> positive integer.
>
> *References:*
> - [A230241](https://oeis.org/A230241)

*Quoted from [FormalConjectures/OEIS/230241.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/230241.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 7 test statements, counted here but not shown.

## `OeisA230241.conjecture`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 5$.

```lean
theorem conjecture (n : ℕ) (hn : n > 5) : a n > 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/230241.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/230241.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/230241.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/230241.lean)
- [A230241](https://oeis.org/A230241)
