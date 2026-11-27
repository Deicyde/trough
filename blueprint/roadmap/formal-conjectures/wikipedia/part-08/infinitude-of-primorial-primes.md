---
declaration: theorem
origin: cited
lean: PrimorialPrime.infinitely_many_primorial_primes, PrimorialPrime.infinitely_many_primorial_primes.variants.kummer, PrimorialPrime.infinitely_many_primorial_primes.variants.composite, PrimorialPrime.infinitely_many_primorial_primes.variants.composite_euclid, PrimorialPrime.infinitely_many_primorial_primes.variants.composite_kummer
statement: formalized
---

# Infinitude of primorial primes

> For $n \in \mathbb{N}$, let $p_n\#$ (`Nat.kthPrimorial n`) denote the primorial multiplying the
> initial $n$ primes (with $p_0\# = 1$), so `EuclidNumbers.Euclid n` equals $p_n\# + 1$ and
> $p_n\# - 1$ is a *Kummer number* (`OEIS A057588`). Primes equal to $p_n\# + 1$ (prime Euclid
> numbers, `OEIS A018239`) or $p_n\# - 1$ (prime Kummer numbers, `OEIS A057705`) are called
> *primorial primes* (`OEIS A228486`, studied computationally by Dubner 1987). Although $p_n\# + 1$
> always has a prime factor exceeding $p_n$, the integers $p_n\# \pm 1$ are often composite
> (beginning with $p_4\# - 1 = 209 = 11 \times 19$ and $p_6\# + 1 = 30031 = 59 \times 509$). Whether
> infinitely many primorial primes exist, whether infinitely many Kummer numbers are prime, and
> whether infinitely many integers $p_n\# \pm 1$ (or of either sign individually) are composite all
> remain open.
>
> *References:*
> - [Wikipedia: Primorial prime](https://en.wikipedia.org/wiki/Primorial_prime)
> - [Wikipedia: Euclid number](https://en.wikipedia.org/wiki/Euclid_number#Unsolved_problems)
> - [OEIS A228486](https://oeis.org/A228486)
> - [OEIS A018239](https://oeis.org/A018239)
> - [OEIS A057705](https://oeis.org/A057705)
> - H. Dubner, *Factorial and primorial primes*, J. Recreational Math. **19** (1987), no. 3,
>   197–203.

*Quoted from [FormalConjectures/Wikipedia/PrimorialPrime.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/PrimorialPrime.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 5 open. It also has 3 test statements and 2 API statements, counted here but not shown.

## `PrimorialPrime.infinitely_many_primorial_primes`

Open: stated without proof.

> Do infinitely many primorial primes $p_n\# \pm 1$ exist? (The positive-sign case $p_n\# + 1$
> appears as `EuclidNumbers.infinite_prime_euclid_numbers`.)

```lean
theorem infinitely_many_primorial_primes :
    {q : ℕ | IsPrimorialPrime q}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/PrimorialPrime.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/PrimorialPrime.lean#L121).

## `PrimorialPrime.infinitely_many_primorial_primes.variants.kummer`

Open: stated without proof.

> Do infinitely many prime Kummer numbers $p_n\# - 1$ exist?

```lean
theorem infinitely_many_primorial_primes.variants.kummer :
    {q : ℕ | IsKummerPrimorialPrime q}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/PrimorialPrime.lean, line 127](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/PrimorialPrime.lean#L127).

## `PrimorialPrime.infinitely_many_primorial_primes.variants.composite`

Open: stated without proof.

> Are infinitely many integers of the form $p_n\# \pm 1$ composite? This statement takes the
> union over both signs ($m = p_n\# + 1$ or $m = p_n\# - 1$).

```lean
theorem infinitely_many_primorial_primes.variants.composite :
    {m : ℕ | m.Composite ∧
      ∃ n : ℕ, m = EuclidNumbers.Euclid n ∨ m + 1 = Nat.kthPrimorial n}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/PrimorialPrime.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/PrimorialPrime.lean#L134).

## `PrimorialPrime.infinitely_many_primorial_primes.variants.composite_euclid`

Open: stated without proof.

> Are infinitely many Euclid numbers $p_n\# + 1$ composite?

```lean
theorem infinitely_many_primorial_primes.variants.composite_euclid :
    {n : ℕ | (EuclidNumbers.Euclid n).Composite}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/PrimorialPrime.lean, line 141](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/PrimorialPrime.lean#L141).

## `PrimorialPrime.infinitely_many_primorial_primes.variants.composite_kummer`

Open: stated without proof.

> Are infinitely many Kummer numbers $p_n\# - 1$ composite?

```lean
theorem infinitely_many_primorial_primes.variants.composite_kummer :
    {m : ℕ | m.Composite ∧ ∃ n : ℕ, m + 1 = Nat.kthPrimorial n}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/PrimorialPrime.lean, line 147](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/PrimorialPrime.lean#L147).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/PrimorialPrime.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/PrimorialPrime.lean)
- [Wikipedia: Primorial prime](https://en.wikipedia.org/wiki/Primorial_prime)
