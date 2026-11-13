---
declaration: theorem
origin: cited
lean: FactorialPrime.infinitely_many_factorial_primes
statement: formalized
---

# Factorial primes

> A factorial prime is a prime that is one more or one less than a factorial. It
> is conjectured that there are infinitely many factorial primes.
>
> *References:*
> - [Wikipedia, Factorial prime](https://en.wikipedia.org/wiki/Factorial_prime)
> - [OEIS A088054](https://oeis.org/A088054)

*Quoted from [FormalConjectures/Wikipedia/FactorialPrime.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/FactorialPrime.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 2 test statements, counted here but not shown.

## `FactorialPrime.infinitely_many_factorial_primes`

Open: stated without proof.

> There are infinitely many factorial primes.

```lean
theorem infinitely_many_factorial_primes :
    Set.Infinite {p : ℕ | IsFactorialPrime p}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/FactorialPrime.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/FactorialPrime.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/FactorialPrime.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/FactorialPrime.lean)
- [Wikipedia, Factorial prime](https://en.wikipedia.org/wiki/Factorial_prime)
