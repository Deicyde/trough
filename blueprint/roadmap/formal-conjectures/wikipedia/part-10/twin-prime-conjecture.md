---
declaration: theorem
origin: cited
lean: TwinPrimes.twin_primes
statement: formalized
---

# Twin prime conjecture

> *References:*
> - [Landau Problems Wikipedia Page](https://en.wikipedia.org/wiki/Landau%27s_problems#Twin_prime_conjecture)
> - [Twin Primes Conjecture Wikipedia Page](https://en.wikipedia.org/wiki/Twin_prime#Twin_prime_conjecture)

*Quoted from [FormalConjectures/Wikipedia/TwinPrimes.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/TwinPrimes.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `TwinPrimes.twin_primes`

Open: stated without proof.

> Are there infinitely many primes p such that p + 2 is prime?

```lean
theorem twin_primes :
    {p : ℕ | Prime p ∧ Prime (p + 2)}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/TwinPrimes.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/TwinPrimes.lean#L37).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/TwinPrimes.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/TwinPrimes.lean)
- [Landau Problems Wikipedia Page](https://en.wikipedia.org/wiki/Landau%27s_problems#Twin_prime_conjecture)
