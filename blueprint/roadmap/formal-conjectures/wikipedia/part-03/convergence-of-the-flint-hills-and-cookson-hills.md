---
declaration: theorem
origin: cited
lean: FlintCooksonHills.flint_hills_series_converges, FlintCooksonHills.cookson_hills_series_converges
statement: formalized
---

# Convergence of the Flint Hills and Cookson Hills series

> *References:*
> - [Wikipedia: Examples of numerical series](https://en.wikipedia.org/wiki/Series_(mathematics)#Examples_of_numerical_series)
> - [MathWorld: Flint Hills Series](https://mathworld.wolfram.com/FlintHillsSeries.html)
> - [Alekseyev, On the Flint Hills series](https://doi.org/10.48550/arXiv.1104.5100)
> - [MathWorld: Cookson Hills Series](https://mathworld.wolfram.com/CooksonHillsSeries.html)

*Quoted from [FormalConjectures/Wikipedia/FlintCooksonHills.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/FlintCooksonHills.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open.

## `FlintCooksonHills.flint_hills_series_converges`

Open: stated without proof.

> The Flint Hills series summing $csc(n)^2 / n^3$ from $n=1$ to $\infty$ converges.
> (Note that we 0-index the series below.)

```lean
theorem flint_hills_series_converges :
    Summable (fun n : ℕ =>
      1 / ((((n + 1) : ℝ)^3) * (Real.sin (n + 1)^2)))
```

Category `research open`; AMS [40 Sequences, series, summability](../../by-subject/part-02/40-sequences-series-summability/README.md). Declared in [FormalConjectures/Wikipedia/FlintCooksonHills.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/FlintCooksonHills.lean#L39).

## `FlintCooksonHills.cookson_hills_series_converges`

Open: stated without proof.

> The Cookson Hills series summing $sec(n)^2 / n^3$ from $n=1$ to $\infty$ converges.

```lean
theorem cookson_hills_series_converges :
    Summable (fun n : ℕ =>
      1 / ((((n + 1) : ℝ)^3) * (Real.cos (n + 1)^2)))
```

Category `research open`; AMS [40 Sequences, series, summability](../../by-subject/part-02/40-sequences-series-summability/README.md). Declared in [FormalConjectures/Wikipedia/FlintCooksonHills.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/FlintCooksonHills.lean#L48).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/FlintCooksonHills.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/FlintCooksonHills.lean)
- [Wikipedia: Examples of numerical series](https://en.wikipedia.org/wiki/Series_%28mathematics%29#Examples_of_numerical_series)
