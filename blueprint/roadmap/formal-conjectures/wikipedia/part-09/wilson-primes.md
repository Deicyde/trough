---
declaration: theorem
origin: cited
lean: WilsonPrime.infinitely_many_wilson_primes
statement: formalized
---

# Wilson primes

> A Wilson prime is a prime $p$ for which $p^2$ divides $(p-1)!+1$. The only known examples are
> $5$, $13$, and $563$. It is conjectured that infinitely many Wilson primes exist.
>
> *References:*
> * [Wikipedia, Wilson prime](https://en.wikipedia.org/wiki/Wilson_prime)
> * [OEIS A007540](https://oeis.org/A007540)
> * E. Costa, R. Gerbicz, and D. Harvey,
>   [A search for Wilson primes](https://arxiv.org/abs/1209.3436)

*Quoted from [FormalConjectures/Wikipedia/WilsonPrime.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WilsonPrime.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `WilsonPrime.infinitely_many_wilson_primes`

Open: stated without proof.

> There are infinitely many Wilson primes.

```lean
theorem infinitely_many_wilson_primes : Set.Infinite {p : ℕ | IsWilsonPrime p}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WilsonPrime.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WilsonPrime.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/WilsonPrime.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/WilsonPrime.lean)
- [Wikipedia, Wilson prime](https://en.wikipedia.org/wiki/Wilson_prime)
