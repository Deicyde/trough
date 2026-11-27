---
declaration: theorem
origin: cited
lean: WoodallPrimes.infinitely_many_woodall_primes
statement: formalized
---

# Woodall Primes

> References:
> * [Wikipedia/Woodall Number](https://en.wikipedia.org/wiki/Woodall_number#Woodall_primes)
> * [A2234](https://oeis.org/A2234)

*Quoted from [FormalConjectures/Wikipedia/WoodalPrimes.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/WoodalPrimes.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `WoodallPrimes.infinitely_many_woodall_primes`

Open: stated without proof.

> There are infinitely many prime numbers of the form `k * 2 ^ k - 1` for `k > 1`.

```lean
theorem infinitely_many_woodall_primes : {k : ℕ | 1 < k ∧ (k * 2 ^ k - 1).Prime}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/WoodalPrimes.lean, line 34](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/WoodalPrimes.lean#L34).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/WoodalPrimes.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/WoodalPrimes.lean)
- [Wikipedia/Woodall Number](https://en.wikipedia.org/wiki/Woodall_number#Woodall_primes)
