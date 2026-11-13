---
declaration: theorem
origin: cited
lean: RegularPrimes.not_isRegularPrime_37, RegularPrimes.small_regular_primes, RegularPrimes.isRegularPrime_iff_Bernoulli, RegularPrimes.infinitude_of_irregularprimes, RegularPrimes.regularprime_conjecture
statement: formalized
---

# Infinite Regular Primes

> We define the notion of regular primes, which are prime numbers that are coprime with the
> cardinality of the class group of the `p`-th cyclotomic field. We also state that there are
> infinitely many regular primes.
>
> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Regular_prime)

*Quoted from [FormalConjectures/Wikipedia/RegularPrimes.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/RegularPrimes.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 1 open, 1 solved and 3 textbook results.

## `RegularPrimes.not_isRegularPrime_37`

Textbook result, stated without proof.

> The prime 37 is not a regular prime.

```lean
theorem not_isRegularPrime_37 : ¬ @IsRegularPrime 37 (by decide)
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/RegularPrimes.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/RegularPrimes.lean#L45).

## `RegularPrimes.small_regular_primes`

Textbook result, stated without proof.

> The primes 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, and 31 are regular.

```lean
lemma small_regular_primes :
    { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31 } ⊆ regularPrimes
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/RegularPrimes.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/RegularPrimes.lean#L56).

## `RegularPrimes.isRegularPrime_iff_Bernoulli`

Textbook result, stated without proof.

> **Kummer's criterion.** An equivalent definition of a regular prime `p` is that it does not
> divide the numerator of any of the Bernoulli numbers $B_k$ for $k = 2, 4, 6, \dots, p - 3$.
> Not in Mathlib.

```lean
theorem isRegularPrime_iff_Bernoulli (p : ℕ) [Fact p.Prime] :
    IsRegularPrime p ↔ ∀ k ∈ Finset.Icc 2 (p - 3), Even k → ¬ (p : ℤ) ∣ (bernoulli' k).num
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/RegularPrimes.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/RegularPrimes.lean#L64).

## `RegularPrimes.infinitude_of_irregularprimes`

Solved: stated here without proof.

> The set of irregular primes is infinite.

```lean
theorem infinitude_of_irregularprimes : irregularPrimes.Infinite
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/RegularPrimes.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/RegularPrimes.lean#L70).

## `RegularPrimes.regularprime_conjecture`

Open: stated without proof.

> Conjecture: The set of regular primes is infinite.

```lean
theorem regularprime_conjecture : RegularPrimeConjecture
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/RegularPrimes.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/RegularPrimes.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/RegularPrimes.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/RegularPrimes.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Regular_prime)
