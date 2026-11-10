---
declaration: theorem
origin: cited
lean: LegendreConjecture.legendre_conjecture, LegendreConjecture.bounded_gap_legendre, LegendreConjecture.legendre_conjecture.ferreira_large_n
statement: formalized
---

# Legendre's conjecture

> *References:*
> - [Landau Problems Wikipedia Page](https://en.wikipedia.org/wiki/Landau%27s_problems#Twin_prime_conjecture)
> - [Legendre Conjecture Wikipedia Page](https://en.wikipedia.org/wiki/Legendre%27s_conjecture)
> - [Luan Alberto Ferreira, *Real exponential sums over primes and prime gaps*](https://arxiv.org/abs/2307.08725)

*Quoted from [FormalConjectures/Wikipedia/LegendreConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/LegendreConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved.

## `LegendreConjecture.legendre_conjecture`

Open: stated without proof.

> Does there always exist at least one prime between consecutive perfect squares?

```lean
theorem legendre_conjecture :
    ∀ n ≥ 1, ∃ p ∈ Set.Ioo (n ^ 2) ((n + 1) ^ 2), Nat.Prime p
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/LegendreConjecture.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/LegendreConjecture.lean#L38).

## `LegendreConjecture.bounded_gap_legendre`

Solved: stated here; a Lean proof is at [https://github.com/mzhorvath1/formal-conjectures/blob/a4568d467b4f42884b6a4bd09c40d65f92113ee7/FormalConjectures/Wikipedia/LegendreConjecture.lean#L48](https://github.com/mzhorvath1/formal-conjectures/blob/a4568d467b4f42884b6a4bd09c40d65f92113ee7/FormalConjectures/Wikipedia/LegendreConjecture.lean#L48).

> If there exists a constant `c > 0` such that
> `(n + 1).nth Nat.Prime - n.nth Nat.Prime < (n.nth Nat.Prime) ^ (1 / 2 - c)` for all large `n`,
> then Legendre's conjecture is asymptotically true.
>
> Formal proof linked here provided by AlphaProof.

```lean
theorem bounded_gap_legendre
    (H : ∃ c > 0, ∀ᶠ n in atTop, (n + 1).nth Nat.Prime - n.nth Nat.Prime <
      (n.nth Nat.Prime : ℝ) ^ (1 / (2 : ℝ) - c)) :
    ∀ᶠ n in atTop, ∃ p ∈ Set.Ioo (n ^ 2) ((n + 1) ^ 2), Nat.Prime p
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/LegendreConjecture.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/LegendreConjecture.lean#L51).

## `LegendreConjecture.legendre_conjecture.ferreira_large_n`

Solved: stated here without proof.

> Ferreira proved that the conjecture is true for sufficiently large n.

```lean
theorem legendre_conjecture.ferreira_large_n :
    ∀ᶠ n in atTop, ∃ p ∈ Set.Ioo (n ^ 2) ((n + 1) ^ 2), Nat.Prime p
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/LegendreConjecture.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/LegendreConjecture.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/LegendreConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/LegendreConjecture.lean)
- [Landau Problems Wikipedia Page](https://en.wikipedia.org/wiki/Landau%27s_problems#Twin_prime_conjecture)
