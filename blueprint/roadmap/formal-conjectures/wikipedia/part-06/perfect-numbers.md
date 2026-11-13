---
declaration: theorem
origin: cited
lean: PerfectNumbers.infinitely_many_perfect, PerfectNumbers.infinitely_many_even_perfect, PerfectNumbers.odd_perfect_number_conjecture, PerfectNumbers.odd_perfect_number.lower_bound, PerfectNumbers.odd_perfect_number.euler_form
statement: formalized
---

# Perfect numbers

> A perfect number is a positive integer that equals the sum of its proper divisors
> (i.e., all its positive divisors excluding the number itself).
>
> For example, 6 is perfect because its proper divisors are 1, 2, and 3, and 1 + 2 + 3 = 6.
> Similarly, 28 is perfect because 1 + 2 + 4 + 7 + 14 = 28.
>
> All known perfect numbers are even. Several open problems about perfect numbers are
> formalised here:
>
> * Are there infinitely many perfect numbers?
> * Are there infinitely many even perfect numbers?
> * Do odd perfect numbers exist?
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Perfect_number)
> - [Wikipedia, Odd perfect numbers](https://en.wikipedia.org/wiki/Perfect_number#Odd_perfect_numbers)

*Quoted from [FormalConjectures/Wikipedia/PerfectNumbers.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/PerfectNumbers.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 3 open and 2 solved.

## `PerfectNumbers.infinitely_many_perfect`

Open: stated without proof.

> **Infinitely many perfect numbers conjecture.**
> Are there infinitely many perfect numbers?
>
> *Reference:*
> [Wikipedia](https://en.wikipedia.org/wiki/Perfect_number)

```lean
theorem infinitely_many_perfect :
    {n : ℕ | Perfect n}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/PerfectNumbers.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/PerfectNumbers.lean#L55).

## `PerfectNumbers.infinitely_many_even_perfect`

Open: stated without proof.

> **Infinitely many even perfect numbers conjecture.**
> Are there infinitely many even perfect numbers?
>
> This is equivalent to asking whether there are infinitely many Mersenne primes,
> since by the Euclid–Euler theorem an even number is perfect if and only if it
> has the form $2^{p-1}(2^p - 1)$ where $2^p - 1$ is a Mersenne prime.
>
> *Reference:*
> [Wikipedia](https://en.wikipedia.org/wiki/Perfect_number)

```lean
theorem infinitely_many_even_perfect :
    {n : ℕ | Perfect n ∧ Even n}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/PerfectNumbers.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/PerfectNumbers.lean#L71).

## `PerfectNumbers.odd_perfect_number_conjecture`

Open: stated without proof.

> **Odd Perfect Number Conjecture.**
> The Odd Perfect Number Conjecture states that all perfect numbers are even.
>
> *Reference:*
> [Wikipedia](https://en.wikipedia.org/wiki/Perfect_number#Odd_perfect_numbers)

```lean
theorem odd_perfect_number_conjecture (n : ℕ) (hn : Perfect n) : Even n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/PerfectNumbers.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/PerfectNumbers.lean#L83).

## `PerfectNumbers.odd_perfect_number.lower_bound`

Solved: stated here without proof.

> A known result: If an odd perfect number exists, it must be greater than $10^{1500}$
> and must have at least 101 prime factors (including multiplicities).
>
> *Reference:* Pascal Ochem, Michaël Rao (2012).
> "Odd perfect numbers are greater than 10^1500"

```lean
theorem odd_perfect_number.lower_bound (n : ℕ) (hn : Odd n) (hp : Perfect n) :
    n > 10^1500 ∧ (n.primeFactorsList).length ≥ 101
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/PerfectNumbers.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/PerfectNumbers.lean#L94).

## `PerfectNumbers.odd_perfect_number.euler_form`

Solved: stated here; a Lean proof is at [https://github.com/mzhorvath1/formal-conjectures/blob/7deed78f7babe2ae9ea13969a8dfa26854982407/FormalConjectures/Wikipedia/PerfectNumbers.lean#L110](https://github.com/mzhorvath1/formal-conjectures/blob/7deed78f7babe2ae9ea13969a8dfa26854982407/FormalConjectures/Wikipedia/PerfectNumbers.lean#L110).

> A known result: If an odd perfect number exists, it must be of the form
> $p^α * m^2$ where $p$ is prime, $p \equiv 1 \pmod{4}$, $\alpha \equiv 1 \pmod{4}$,
> and $p \nmid m$.
>
> *Reference:* Euler's theorem on odd perfect numbers.
>
> Formal proof linked here provided by AlphaProof.

```lean
theorem odd_perfect_number.euler_form (n : ℕ) (hn : Odd n) (hp : Perfect n) :
    ∃ (p m α : ℕ),
      p.Prime ∧
      p ≡ 1 [ZMOD 4] ∧
      α ≡ 1 [ZMOD 4] ∧
      ¬ p ∣ m ∧
      n = p^α * m^2
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/PerfectNumbers.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/PerfectNumbers.lean#L109).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/PerfectNumbers.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/PerfectNumbers.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Perfect_number)
