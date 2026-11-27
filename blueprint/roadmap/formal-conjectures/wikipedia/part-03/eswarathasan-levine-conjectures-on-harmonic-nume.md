---
declaration: theorem
origin: cited
lean: EswarathasanLevineConjecture.harmonicNumDivisibleSet_two_empty, EswarathasanLevineConjecture.eswarathasan_levine_three_elements_subset, EswarathasanLevineConjecture.eswarathasan_levine_harmonic_conjecture, EswarathasanLevineConjecture.eswarathasan_levine_harmonic_primes_infinite
statement: formalized
---

# Eswarathasan–Levine conjectures on harmonic numerators

> Given a prime $p$, write $J_p$ for the set of indices $n \ge 1$ where $p$ divides the reduced
> numerator of $H_n = \sum_{k=1}^n \frac{1}{k}$ (for instance $J_2 = \emptyset$ and
> $J_3 = \{2, 7, 22\}$). Arulappah Eswarathasan and Eugene Levine (1991) showed that
> $\{p - 1, p^2 - p, p^2 - 1\} \subseteq J_p$ whenever $p \ge 5$, called a prime $p \ge 5$ a
> *harmonic prime* ([OEIS A092101](https://oeis.org/A092101)) when $J_p$ consists solely of those
> three elements ($|J_p| = 3$), and conjectured both that every $J_p$ is finite and that infinitely
> many harmonic primes exist. David W. Boyd (1994) confirmed finiteness of $J_p$ for all primes
> $p \le 547$ aside from $83, 127, 397$ and proposed a $1 / e$ relative density heuristic for harmonic
> primes.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Harmonic_number#Arithmetic_properties)
> - [OEIS A092101](https://oeis.org/A092101)
> - A. Eswarathasan and E. Levine (1991), Discrete Math. **91**, no. 3, 249–257.
> - D. W. Boyd (1994), Experiment. Math. **3**, no. 4, 287–302.

*Quoted from [FormalConjectures/Wikipedia/EswarathasanLevineConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/EswarathasanLevineConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 2 open, 1 solved and 1 textbook result. It also has 2 test statements, counted here but not shown.

## `EswarathasanLevineConjecture.harmonicNumDivisibleSet_two_empty`

Textbook result, stated without proof.

> Every $H_n$ with $n \ge 1$ has odd reduced numerator, hence $J_2 = \emptyset$.

```lean
theorem harmonicNumDivisibleSet_two_empty : harmonicNumDivisibleSet 2 = ∅
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/EswarathasanLevineConjecture.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/EswarathasanLevineConjecture.lean#L77).

## `EswarathasanLevineConjecture.eswarathasan_levine_three_elements_subset`

Solved: stated here without proof.

> Eswarathasan–Levine inclusion theorem (1991): every prime $p \ge 5$ satisfies
> $\{p - 1, p^2 - p, p^2 - 1\} \subseteq J_p$ (using Wolstenholme's theorem at $p - 1$; cf.
> `WolstenholmePrime.wolstenholme_theorem` and `WolstenholmePrime.wolstenholme_harmonic`).

```lean
theorem eswarathasan_levine_three_elements_subset {p : ℕ} (hp : p.Prime) (hp5 : 5 ≤ p) :
    ({p - 1, p ^ 2 - p, p ^ 2 - 1} : Set ℕ) ⊆ harmonicNumDivisibleSet p
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/EswarathasanLevineConjecture.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/EswarathasanLevineConjecture.lean#L84).

## `EswarathasanLevineConjecture.eswarathasan_levine_harmonic_conjecture`

Open: stated without proof.

> Eswarathasan–Levine finiteness conjecture (1991): $J_p$ is finite for every prime $p$.

```lean
theorem eswarathasan_levine_harmonic_conjecture {p : ℕ} (hp : p.Prime) :
    (harmonicNumDivisibleSet p).Finite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/EswarathasanLevineConjecture.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/EswarathasanLevineConjecture.lean#L90).

## `EswarathasanLevineConjecture.eswarathasan_levine_harmonic_primes_infinite`

Open: stated without proof.

> Eswarathasan–Levine harmonic-prime conjecture (1991): infinitely many primes $p$ satisfy
> $|J_p| = 3$.

```lean
theorem eswarathasan_levine_harmonic_primes_infinite :
    {p : ℕ | IsHarmonicPrime p}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/EswarathasanLevineConjecture.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/EswarathasanLevineConjecture.lean#L97).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/EswarathasanLevineConjecture.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/EswarathasanLevineConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Harmonic_number#Arithmetic_properties)
