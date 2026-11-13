---
declaration: theorem
origin: cited
lean: Erdos968.erdos_968, Erdos968.erdos_968.variants.sum_abs_diff_isTheta_log_sq, Erdos968.erdos_968.variants.decreasing_steps_pos_lower_density, Erdos968.erdos_968.variants.infinite_increasingTriples, Erdos968.erdos_968.variants.infinite_decreasingTriples
statement: formalized
---

# Erdős Problem 968

> Let `uₙ = pₙ / n`, where `pₙ` is the `n`th prime. Does the set of `n` such that `uₙ < uₙ₊₁`
> have positive lower density?
>
> Erdős and Prachar also proved that `∑_{pₙ < x} |uₙ₊₁ - uₙ| ≍ (log x)^2`, and that the set of `n`
> such that `uₙ > uₙ₊₁` has positive lower density. Erdős also asked whether there are infinitely many
> increasing triples `uₙ < uₙ₊₁ < uₙ₊₂` or decreasing triples `uₙ > uₙ₊₁ > uₙ₊₂`.
>
> *Reference:* [erdosproblems.com/968](https://www.erdosproblems.com/968)
>
> [ErPr61] Erdős, P. and Prachar, K., _Sätze und Probleme über pₖ/k_. Abh. Math. Sem. Univ. Hamburg
> (1961/62), 251–256.
>
> [FMT18] Ford, K. and Maynard, J. and Tao, T., _Chains of large gaps between primes_. Irregularities
> in the distribution of prime numbers, Springer (2018), 1–21.
>
> [Ma15] Maynard, J., _Small gaps between primes_. Ann. of Math. (2015), 383–413.
>
> [OAI26a] OpenAI, _Positive lower density of large prime gaps_. OpenAI Math Release preprint (2026).
> https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/main.pdf

*Quoted from [FormalConjectures/ErdosProblems/968.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/968.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/968](https://www.erdosproblems.com/968).

The file states 5 research or textbook statements: 5 solved.

## `Erdos968.erdos_968`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/PrimeGaps/RatioCorollary.lean#L30](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/PrimeGaps/RatioCorollary.lean#L30).

> Does the set `{n | u n < u (n+1)}` have positive lower density?
>
> Yes. This was proved by an internal OpenAI model in September 2026 [OAI26a]; see the linked
> Lean proof.

```lean
theorem erdos_968 : 0 < {n : ℕ | u n < u (n + 1)}.lowerDensity
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/968.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/968.lean#L70).

## `Erdos968.erdos_968.variants.sum_abs_diff_isTheta_log_sq`

Solved: stated here without proof.

> Erdős and Prachar proved `∑_{pₙ < x} |u (n+1) - u n| ≍ (log x)^2` (see [ErPr61]).
>
> We encode `∑_{pₙ < x}` as a sum over `n < Nat.primeCounting' x` (the number of primes `< x`).

```lean
theorem erdos_968.variants.sum_abs_diff_isTheta_log_sq :
    (fun x : ℕ =>
        ∑ n < Nat.primeCounting' x, |u (n + 1) - u n|) =Θ[atTop]
      fun x : ℕ => log x ^ 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/968.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/968.lean#L79).

## `Erdos968.erdos_968.variants.decreasing_steps_pos_lower_density`

Solved: stated here without proof.

> Erdős and Prachar proved that the set `{n | u n > u (n+1)}` has positive lower density
> (see [ErPr61]).

```lean
theorem erdos_968.variants.decreasing_steps_pos_lower_density :
    0 < {n : ℕ | u n > u (n + 1)}.lowerDensity
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/968.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/968.lean#L90).

## `Erdos968.erdos_968.variants.infinite_increasingTriples`

Solved: stated here without proof.

> Erdős asked whether there are infinitely many solutions to `uₙ < uₙ₊₁ < uₙ₊₂`.
>
> The answer is yes. Since `uₙ < uₙ₊₁` is equivalent to `pₙ₊₁ - pₙ > pₙ / n`, it suffices to have
> infinitely many `n` with two consecutive prime gaps larger than `pₙ / n ∼ log n`. Ford, Maynard,
> and Tao [FMT18] proved that for every fixed `k` there are infinitely many `n` with `k` consecutive
> prime gaps all of size `≫ log pₙ · log log pₙ · log log log log pₙ / log log log pₙ`.

```lean
theorem erdos_968.variants.infinite_increasingTriples :
    {n : ℕ | u n < u (n + 1) ∧ u (n + 1) < u (n + 2)}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/968.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/968.lean#L103).

## `Erdos968.erdos_968.variants.infinite_decreasingTriples`

Solved: stated here without proof.

> Erdős asked whether there are infinitely many solutions to `uₙ > uₙ₊₁ > uₙ₊₂`.
>
> The answer is yes. Since `uₙ > uₙ₊₁` is equivalent to `pₙ₊₁ - pₙ < pₙ / n`, it suffices to have
> infinitely many `n` with `pₙ₊₂ - pₙ` bounded, because `pₙ / n → ∞`. Maynard [Ma15] proved that
> `liminf (pₙ₊₂ - pₙ) < ∞`.

```lean
theorem erdos_968.variants.infinite_decreasingTriples :
    {n : ℕ | u n > u (n + 1) ∧ u (n + 1) > u (n + 2)}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/968.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/968.lean#L115).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/968.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/968.lean)
- [erdosproblems.com/968](https://www.erdosproblems.com/968)
