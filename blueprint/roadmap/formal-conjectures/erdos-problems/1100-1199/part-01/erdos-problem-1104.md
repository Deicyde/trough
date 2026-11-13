---
declaration: theorem
origin: cited
lean: Erdos1104.erdos_1104.variants.lower, Erdos1104.erdos_1104.variants.upper
statement: formalized
---

# Erdős Problem 1104

> *Reference:* https://www.erdosproblems.com/1104

*Quoted from [FormalConjectures/ErdosProblems/1104.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1104.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1104](https://www.erdosproblems.com/1104).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1104.erdos_1104.variants.lower`

Solved: stated here without proof.

> Lower bound (Hefty–Horn–King–Pfender 2025).
>
> $$
> (1 - o(1)) \sqrt{\frac{n}{\log n}} \le f(n),
> $$
>
> where $f(n)$ denotes the maximum chromatic number of a triangle-free graph on
> $n$ vertices, formalized as `triangleFreeMaxChromatic n`.

```lean
theorem erdos_1104.variants.lower :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      (1 - ε) * Real.sqrt (n : ℝ) / Real.sqrt (Real.log (n : ℝ))
        ≤ (triangleFreeMaxChromatic n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1104.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1104.lean#L48).

## `Erdos1104.erdos_1104.variants.upper`

Solved: stated here without proof.

> Upper bound (Davies–Illingworth 2022).
>
> $$
> f(n) \le (2 + o(1)) \sqrt{\frac{n}{\log n}},
> $$
>
> where $f(n)$ denotes the maximum chromatic number of a triangle-free graph on
> $n$ vertices, formalized as `triangleFreeMaxChromatic n`.

```lean
theorem erdos_1104.variants.upper :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      (triangleFreeMaxChromatic n : ℝ)
        ≤ (2 + ε) * Real.sqrt (n : ℝ) / Real.sqrt (Real.log (n : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1104.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1104.lean#L63).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1104.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1104.lean)
- [erdosproblems.com/1104](https://www.erdosproblems.com/1104)
