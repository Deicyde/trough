---
declaration: theorem
origin: cited
lean: OeisA7468.conjecture
statement: formalized
---

# Sum of next $n$ primes

> The sum of the primes in the $n$-th row of the prime number triangle:
>
> $$a(n) = \sum_{i = 1 + n(n-1)/2}^{n + n(n-1)/2} p_i$$
>
> with $a(0) = 0$.
>
> *References:*
> - [A007468](https://oeis.org/A007468)

*Quoted from [FormalConjectures/OEIS/7468.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/7468.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `OeisA7468.conjecture`

Open: stated without proof.

> The only positive integer $n$ such that $a(n)$ is a perfect square is $n=38$.
> - Carlos Eduardo Olivieri, Mar 09 2015

```lean
theorem conjecture (n : ℕ) (hn : 0 < n) : IsSquare (a n) ↔ n = 38
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/7468.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/7468.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/7468.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/7468.lean)
- [A007468](https://oeis.org/A007468)
