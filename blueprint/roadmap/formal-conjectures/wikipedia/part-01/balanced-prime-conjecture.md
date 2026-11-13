---
declaration: theorem
origin: cited
lean: BalancedPrimes.balanced_primes, BalancedPrimes.balanced_primes_order
statement: formalized
---

# Balanced prime conjecture

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Balanced_prime)
> - [OEIS A6562](https://oeis.org/A6562)

*Quoted from [FormalConjectures/Wikipedia/BalancedPrimes.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BalancedPrimes.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open.

## `BalancedPrimes.balanced_primes`

Open: stated without proof.

> Let $p_k$ be the $k$-th prime number.
> Are there infinitely many $n$ such that $(p_n + p_{n+2}) / 2$ is prime?

```lean
theorem balanced_primes :
    {n : ℕ | Prime ((Nat.nth Prime n + Nat.nth Prime (n + 2)) / 2)}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/BalancedPrimes.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BalancedPrimes.lean#L37).

## `BalancedPrimes.balanced_primes_order`

Open: stated without proof.

> Let $p_k$ be the $k$-th prime number.
> Are there infinitely many $n$ such that
> $p_n = \dfrac{\sum_{i = 1} ^ k p_{n - i} + p_{n + i}}{2*k}$?

```lean
theorem balanced_primes_order :
    ∀ k > 0, {n : ℕ | k ≤ n ∧ 2 * k * Nat.nth Prime n = ∑ i ∈ .Ioc 0 k,
      ((n - i).nth Prime + (n + i).nth Prime)}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/BalancedPrimes.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BalancedPrimes.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/BalancedPrimes.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BalancedPrimes.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Balanced_prime)
