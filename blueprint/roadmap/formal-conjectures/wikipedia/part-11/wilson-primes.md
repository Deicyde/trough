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

*Quoted from [FormalConjectures/Wikipedia/WilsonPrime.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/WilsonPrime.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `WilsonPrime.infinitely_many_wilson_primes`

Open: stated without proof.

> There are infinitely many Wilson primes.

```lean
theorem infinitely_many_wilson_primes : Set.Infinite {p : ℕ | IsWilsonPrime p}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WilsonPrime.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/WilsonPrime.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/WilsonPrime.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/WilsonPrime.lean)
- [Wikipedia, Wilson prime](https://en.wikipedia.org/wiki/Wilson_prime)
