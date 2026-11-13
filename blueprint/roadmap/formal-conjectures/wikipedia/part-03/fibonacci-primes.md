---
declaration: theorem
origin: cited
lean: FibonacciPrimes.fib_primes_infinite, FibonacciPrimes.fib_primes_infinite.variant
statement: formalized
---

# Fibonacci Primes

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_prime)

*Quoted from [FormalConjectures/Wikipedia/FibonacciPrimes.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/FibonacciPrimes.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 1 test statement, counted here but not shown.

## `FibonacciPrimes.fib_primes_infinite`

Open: stated without proof.

> There are infinitely many Fibonacci primes, i.e., Fibonacci numbers that are prime
> It is also a barrier to defining a benchmark from this paper:
> https://arxiv.org/html/2505.13938v1 (see Figure 8).

```lean
theorem fib_primes_infinite : {n : ℕ | (∃ m : ℕ, m.fib = n) ∧ n.Prime}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/FibonacciPrimes.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/FibonacciPrimes.lean#L37).

## `FibonacciPrimes.fib_primes_infinite.variant`

Open: stated without proof.

> There are infinitely many indices $i$, such that the $i$-th Fibonacci is prime.

```lean
theorem fib_primes_infinite.variant : {n : ℕ | n.fib.Prime}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/FibonacciPrimes.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/FibonacciPrimes.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/FibonacciPrimes.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/FibonacciPrimes.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_prime)
