---
declaration: theorem
origin: cited
lean: DescartesNumber.descartes_cubeFree_not_dvd_three_primeFactors_gt_million, DescartesNumber.descartes_non_example_factor_gt_ten_pow_twelve, DescartesNumber.descartes_cubeFree_lt_seven_primeFactors_unique, DescartesNumber.descartes_number_unique
statement: formalized
---

# Descartes Numbers

> A *Descartes number* (or spoof odd perfect integer) is an odd integer $n = m \cdot w$ where $w$ is
> composite (`Nat.Composite`), $\gcd(m, w) = 1$, and $\sigma_1(m)(w + 1) = 2 m w$, so treating $w$ as
> a prime factor would yield $\sigma_1(n) = 2n$. René Descartes (1638) found
>
> $$D = 3^2 \cdot 7^2 \cdot 11^2 \cdot 13^2 \cdot 22021 = 198{,}585{,}576{,}189,$$
>
> with composite spoof factor $22021 = 19^2 \cdot 61$; no further example is known [KW91]. Banks,
> Güloğlu, Nevans, and Saidak [BGNS08] proved that $D$ is the unique cube-free Descartes integer with
> fewer than seven distinct prime divisors and that every cube-free Descartes integer coprime to $3$
> has over $10^6$ distinct prime divisors; Tóth [To21] showed that any other Descartes factorization
> $n = m \cdot w \ne D$ satisfies $m > 10^{12}$.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Descartes_number)
> - [KW91] V. Klee and S. Wagon (1991), Dolciani Math. Expositions **11**, Math. Assoc. America.
> - [BGNS08] W. D. Banks, A. M. Güloğlu, C. W. Nevans, and F. Saidak (2008), CRM Proc. Lecture Notes
>   **46**, Amer. Math. Soc., 167–173.
> - [To21] L. Tóth (2021), Comput. Methods Sci. Technol. **27**, no. 1, 25–31.

*Quoted from [FormalConjectures/Wikipedia/DescartesNumber.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/DescartesNumber.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 1 open and 3 solved. It also has 2 test statements and 2 API statements, counted here but not shown.

## `DescartesNumber.descartes_cubeFree_not_dvd_three_primeFactors_gt_million`

Solved: stated here without proof.

> **Banks–Güloğlu–Nevans–Saidak Theorem** [BGNS08]: every cube-free Descartes integer not
> divisible by $3$ has strictly more than $10^6$ distinct prime factors.

```lean
theorem descartes_cubeFree_not_dvd_three_primeFactors_gt_million (n : ℕ)
    (hd : IsDescartesNumber n) (hcf : Powerfree 3 n) (h3 : ¬ 3 ∣ n) :
    10 ^ 6 < n.primeFactors.card
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/DescartesNumber.lean, line 144](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/DescartesNumber.lean#L144).

## `DescartesNumber.descartes_non_example_factor_gt_ten_pow_twelve`

Solved: stated here without proof.

> **Tóth's Lower Bound on Spoof Factorizations** [To21]: every Descartes factorization
> $m \cdot w \ne 198{,}585{,}576{,}189$ satisfies $m > 10^{12}$.

```lean
theorem descartes_non_example_factor_gt_ten_pow_twelve (m w : ℕ)
    (hf : IsDescartesFactorization m w) (hne : m * w ≠ descartesExample) :
    10 ^ 12 < m
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/DescartesNumber.lean, line 152](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/DescartesNumber.lean#L152).

## `DescartesNumber.descartes_cubeFree_lt_seven_primeFactors_unique`

Solved: stated here without proof.

> **Banks–Güloğlu–Nevans–Saidak Uniqueness Theorem** [BGNS08] (see also [To21, §1]):
> $198{,}585{,}576{,}189$ is the unique cube-free Descartes integer with fewer than seven distinct
> prime divisors.

```lean
theorem descartes_cubeFree_lt_seven_primeFactors_unique (n : ℕ)
    (hd : IsDescartesNumber n) (hcf : Powerfree 3 n) (hcard : n.primeFactors.card < 7) :
    n = descartesExample
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/DescartesNumber.lean, line 161](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/DescartesNumber.lean#L161).

## `DescartesNumber.descartes_number_unique`

Open: stated without proof.

> Is $198{,}585{,}576{,}189$ the only Descartes number?

```lean
theorem descartes_number_unique :
    ∀ n : ℕ, IsDescartesNumber n → n = descartesExample
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/DescartesNumber.lean, line 168](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/DescartesNumber.lean#L168).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/DescartesNumber.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/DescartesNumber.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Descartes_number)
