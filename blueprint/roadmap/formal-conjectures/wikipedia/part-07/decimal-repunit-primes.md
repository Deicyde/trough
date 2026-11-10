---
declaration: theorem
origin: cited
lean: RepunitPrime.infinitely_many_repunit_primes
statement: formalized
---

# Decimal Repunit Primes

> A decimal repunit is a natural number whose decimal representation consists entirely of ones.
> It is conjectured that infinitely many decimal repunits are prime.
>
> *References:*
> - [Wikipedia: Repunit](https://en.wikipedia.org/wiki/Repunit#Decimal_repunit_primes)
> - [OEIS A002275](https://oeis.org/A002275)
> - [OEIS A004022](https://oeis.org/A004022)
> - [OEIS A004023](https://oeis.org/A004023)

*Quoted from [FormalConjectures/Wikipedia/RepunitPrime.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RepunitPrime.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 7 test statements, counted here but not shown.

## `RepunitPrime.infinitely_many_repunit_primes`

Open: stated without proof.

> [Wikipedia's repunit article](https://en.wikipedia.org/wiki/Repunit#Decimal_repunit_primes)
> states: "It has been conjectured that there are infinitely many repunit primes."

```lean
theorem infinitely_many_repunit_primes :
    {n : ℕ | (repunit10 n).Prime}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/RepunitPrime.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RepunitPrime.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/RepunitPrime.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RepunitPrime.lean)
- [Wikipedia: Repunit](https://en.wikipedia.org/wiki/Repunit#Decimal_repunit_primes)
