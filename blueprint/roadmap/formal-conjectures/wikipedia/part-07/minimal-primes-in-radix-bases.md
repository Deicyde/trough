---
declaration: theorem
origin: cited
lean: MinimalPrime.minimal_primes_finite_in_every_base, MinimalPrime.base_ten_minimal_primes_card, MinimalPrime.base_ten_minimal_primes_eq, MinimalPrime.base_seventeen_f19_family_minimal_prime_question
statement: formalized
---

# Minimal primes in radix bases

> Fix an integer base $b \ge 2$. A prime $p$ is *minimal in base $b$* if no proper subsequence (not
> necessarily contiguous) of its canonical base-$b$ expansion represents a prime—equivalently, no
> prime $q \neq p$ has its canonical base-$b$ digit list as a sublist of `Nat.digits b p`. By
> Higman's lemma, the set of minimal primes in base $b$ is finite for every $b \ge 2$. Jeffrey
> Shallit (2000) classified all $26$ base-$10$ minimal primes (`OEIS A071062`, up to $66600049$).
> Curtis Bright, Raymond Devillers, and Shallit (2016) extended minimal-prime classifications to
> larger bases; in base $17$, they already reduced the classification to $1279$ minimal probable
> primes (not all certified prime) together with the single unresolved candidate family
> $\mathrm{F}1\{9\}$ (base-$17$ digits $15, 1, 9, \dots, 9$).
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Minimal_prime_(recreational_mathematics))
> - [OEIS A071062](https://oeis.org/A071062)
> - J. Shallit, *Minimal primes*, J. Recreational Math. **30** (1999–2000), 113–117.
> - C. Bright, R. Devillers, and J. Shallit, *Minimal elements for the prime numbers*, Exp. Math.
>   **25** (2016), 321–331.

*Quoted from [FormalConjectures/Wikipedia/MinimalPrime.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MinimalPrime.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 1 open, 2 solved and 1 textbook result. It also has 3 test statements, counted here but not shown.

## `MinimalPrime.minimal_primes_finite_in_every_base`

Textbook result, stated without proof.

> Finiteness of minimal primes (empty for $b < 2$, and finite by Higman's lemma for $b \ge 2$):
> for every $b \in \mathbb{N}$, the set of primes satisfying `IsMinimalPrimeInBase b p` is finite.

```lean
theorem minimal_primes_finite_in_every_base (b : ℕ) :
    {p : ℕ | IsMinimalPrimeInBase b p}.Finite
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Wikipedia/MinimalPrime.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MinimalPrime.lean#L120).

## `MinimalPrime.base_ten_minimal_primes_card`

Solved: stated here without proof.

> Base-$10$ classification (Shallit 2000): exactly $26$ primes satisfy
> `IsMinimalPrimeInBase 10 p`.

```lean
theorem base_ten_minimal_primes_card :
    {p : ℕ | IsMinimalPrimeInBase 10 p}.ncard = 26
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Wikipedia/MinimalPrime.lean, line 127](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MinimalPrime.lean#L127).

## `MinimalPrime.base_ten_minimal_primes_eq`

Solved: stated here without proof.

> Explicit base-$10$ minimal prime set (Shallit 2000, `OEIS A071062`): the primes satisfying
> `IsMinimalPrimeInBase 10 p` are precisely the $26$ integers listed below.

```lean
theorem base_ten_minimal_primes_eq :
    {p : ℕ | IsMinimalPrimeInBase 10 p} =
      {2, 3, 5, 7, 11, 19, 41, 61, 89, 409, 449, 499, 881, 991, 6469, 6949, 9001, 9049, 9649,
        9949, 60649, 666649, 946669, 60000049, 66000049, 66600049}
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Wikipedia/MinimalPrime.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MinimalPrime.lean#L134).

## `MinimalPrime.base_seventeen_f19_family_minimal_prime_question`

Open: stated without proof.

> Unresolved base-$17$ candidate family $\mathrm{F}1\{9\}$: does there exist $k \in \mathbb{N}$
> such that the integer with base-$17$ digits $15, 1, \underbrace{9, \dots, 9}_{k}$ (namely
> $15 \cdot 17^{k + 1} + 17^k + \sum_{i < k} 9 \cdot 17^i$) satisfies
> `IsMinimalPrimeInBase 17`?

```lean
theorem base_seventeen_f19_family_minimal_prime_question :
    ∃ k : ℕ, IsMinimalPrimeInBase 17
      (15 * 17 ^ (k + 1) + 17 ^ k + ∑ i ∈ Finset.range k, 9 * 17 ^ i)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Wikipedia/MinimalPrime.lean, line 145](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MinimalPrime.lean#L145).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/MinimalPrime.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MinimalPrime.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Minimal_prime_%28recreational_mathematics%29)
