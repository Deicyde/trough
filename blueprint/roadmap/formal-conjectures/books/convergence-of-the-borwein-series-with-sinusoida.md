---
declaration: theorem
origin: cited
lean: BorweinSineSeries.borwein_sine_series
statement: formalized
---

# Convergence of the Borwein Series with Sinusoidal Coefficient

> *References:*
> - [MathWorld, Harmonic Series](https://mathworld.wolfram.com/HarmonicSeries.html)
> - Borwein, J.; Bailey, D.; Girgensohn, R. *Experimentation in Mathematics: Computational Paths
>   to Discovery*, A K Peters, 2004, p. 56.

*Quoted from [FormalConjectures/Books/BorweinSineSeries.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Books/BorweinSineSeries.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `BorweinSineSeries.borwein_sine_series`

Solved: stated here; a Lean proof is at [https://github.com/AxiomMath/gdm-formal-conjectures/blob/main/BorweinSineSeries/solution.lean](https://github.com/AxiomMath/gdm-formal-conjectures/blob/main/BorweinSineSeries/solution.lean).

> Does the series
>
> $$
>   \sum_{n=1}^{\infty} \frac{\left(\frac{2}{3} + \frac{1}{3}\sin n\right)^n}{n}
> $$
>
> converge?
>
> After computing approximately $10^7$ terms, the partial sums approximate $2.163$.
>
> See https://arxiv.org/abs/2007.11017 for a proof of the convergence,
> relying on an irrationality measure for pi.
>
> Also see
> https://github.com/AxiomMath/gdm-formal-conjectures/blob/main/docs/BorweinSineSeries.md
> for a partial formalization of the conjecture,
> conditional on such an irrationality measure of pi (cf https://arxiv.org/abs/1912.06345).

```lean
theorem borwein_sine_series :
    Summable fun n : ℕ+ ↦ ((2 / 3 + 1 / 3 * Real.sin (n : ℝ)) ^ (n : ℕ)) / (n : ℝ)
```

Category `research solved`; AMS [26 Real functions](../by-subject/part-01/26-real-functions/README.md), [40 Sequences, series, summability](../by-subject/part-02/40-sequences-series-summability/README.md). Declared in [FormalConjectures/Books/BorweinSineSeries.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Books/BorweinSineSeries.lean#L52).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Books/BorweinSineSeries.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Books/BorweinSineSeries.lean)
- [MathWorld, Harmonic Series](https://mathworld.wolfram.com/HarmonicSeries.html)
