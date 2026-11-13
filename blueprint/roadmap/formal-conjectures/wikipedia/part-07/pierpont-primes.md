---
declaration: theorem
origin: cited
lean: PierpontPrime.infinitely_many_pierpont_primes
statement: formalized
---

# Pierpont primes

> A Pierpont prime is a prime of the form $2^a 3^b + 1$, where $a$ and $b$ are
> nonnegative integers. Marc Gleason conjectured that there are infinitely many.
>
> *References:*
> - [Wikipedia, Pierpont prime](https://en.wikipedia.org/wiki/Pierpont_prime)
> - [OEIS A005109](https://oeis.org/A005109)

*Quoted from [FormalConjectures/Wikipedia/PierpontPrime.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/PierpontPrime.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 2 test statements, counted here but not shown.

## `PierpontPrime.infinitely_many_pierpont_primes`

Open: stated without proof.

> There are infinitely many Pierpont primes.

```lean
theorem infinitely_many_pierpont_primes :
    Set.Infinite {p : ℕ | IsPierpontPrime p}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/PierpontPrime.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/PierpontPrime.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/PierpontPrime.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/PierpontPrime.lean)
- [Wikipedia, Pierpont prime](https://en.wikipedia.org/wiki/Pierpont_prime)
