---
declaration: theorem
origin: cited
lean: Erdos375.erdos_375, Erdos375.erdos_375.variants.bounded_gap, Erdos375.erdos_375.variants.legendre, Erdos375.erdos_375.variants.le_two, Erdos375.erdos_375.variants.log
statement: formalized
---

# Erdős Problem 375

> *References:*
>  - [erdosproblems.com/375](https://www.erdosproblems.com/375)
>  - [ErGr80] Erdős, P. and Graham, R., Old and new problems and results in combinatorial number
>     theory. Monographies de L'Enseignement Mathematique (1980).
>  - [RST75] Ramachandra, K. and Shorey, T. N. and Tijdeman, R., On Grimm's problem relating to
>     factorisation of a block of consecutive integers. J. Reine Angew. Math. (1975), 109-124.
>  -

*Quoted from [FormalConjectures/ErdosProblems/375.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/375.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/375](https://www.erdosproblems.com/375).

The file states 5 research or textbook statements: 1 open and 4 solved.

## `Erdos375.erdos_375`

Open: stated without proof.

> Is `Erdos375Prop` true?

```lean
theorem erdos_375 : Erdos375Prop
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/375.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/375.lean#L47).

## `Erdos375.erdos_375.variants.bounded_gap`

Solved: stated here without proof.

> If `Erdos375Prop` is true, then `(n + 1).nth Prime - n.nth Prime < (n.nth Prime) ^ (1 / 2 - c)`
> for some `c > 0`.

```lean
theorem erdos_375.variants.bounded_gap : Erdos375Prop →
    ∃ c > 0, ∀ᶠ n in atTop, (n + 1).nth Nat.Prime - n.nth Nat.Prime
    < (n.nth Nat.Prime : ℝ) ^ (1 / (2 : ℝ) - c)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/375.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/375.lean#L53).

## `Erdos375.erdos_375.variants.legendre`

Proved here.

> In particular, if `Erdos375Prop` is true, then Legendre's conjecture is asymptotically true.

```lean
theorem erdos_375.variants.legendre : Erdos375Prop →
    (∀ᶠ n in atTop, ∃ p ∈ Set.Ioo (n ^ 2) ((n + 1) ^ 2), Nat.Prime p)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/375.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/375.lean#L60).

## `Erdos375.erdos_375.variants.le_two`

Proved here.

> It is easy to see that for any `n ≥ 1` and `k ≤ 2`, if `n + 1, ..., n + k` are all composite,
> then there are distinct primes `p₁, ... pₖ` such that `pᵢ ∣ n + i` for all `1 ≤ i ≤ k`.

```lean
theorem erdos_375.variants.le_two : ∀ n ≥ 1, ∀ k ≤ 2, (∀ i < k, ¬ (n + i + 1).Prime) →
    ∃ p : Fin k → ℕ, p.Injective ∧ ∀ i, (p i).Prime ∧ p i ∣ n + i + 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/375.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/375.lean#L67).

## `Erdos375.erdos_375.variants.log`

Solved: stated here without proof.

> There exists a constant `c > 0` such that for all `n`, if
> `k < c * (log n / (log (log n))) ^ 3 → (∀ i < k, ¬ (n + i + 1).Prime)`, then
> there are distinct primes `p₁, ... pₖ` such that `pᵢ ∣ n + i` for all `1 ≤ i ≤ k`. This is proved
> in [RST75]. There is no need to only consider sufficiently large `n` because one can always take
> `c` small enough so that `k < c * (log n / (log (log n))) ^ 3` implies that `k = 0` until `n` is
> large.

```lean
theorem erdos_375.variants.log : ∃ c > 0, ∀ n k : ℕ,
    k < c * (Real.log n / (Real.log (Real.log n))) ^ 3 → (∀ i < k, ¬ (n + i + 1).Prime) →
    ∃ p : Fin k → ℕ, p.Injective ∧ ∀ i, (p i).Prime ∧ p i ∣ n + i + 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/375.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/375.lean#L91).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/375.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/375.lean)
- [erdosproblems.com/375](https://www.erdosproblems.com/375)
