---
declaration: theorem
origin: cited
lean: PrimesAndPerfectSquares.infinite_prime_sq_add_one
statement: formalized
---

# Primes and perfect squares

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Landau%27s_problems#Near-square_primes)

*Quoted from [FormalConjectures/Wikipedia/PrimesAndPerfectSquares.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PrimesAndPerfectSquares.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `PrimesAndPerfectSquares.infinite_prime_sq_add_one`

Open: stated without proof.

> Are there infinitely many primes $p$ such that $p - 1$ is a perfect square? In other words: Are there infinitely many primes of the form $n^2 + 1$?

```lean
theorem infinite_prime_sq_add_one :
    {n : ℕ | Prime (n^2 + 1)}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/PrimesAndPerfectSquares.lean, line 35](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PrimesAndPerfectSquares.lean#L35).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/PrimesAndPerfectSquares.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PrimesAndPerfectSquares.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Landau%27s_problems#Near-square_primes)
