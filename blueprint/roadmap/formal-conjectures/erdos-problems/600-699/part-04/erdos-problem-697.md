---
declaration: theorem
origin: cited
lean: Erdos697.density_exists, Erdos697.erdos_697.variants.delta_lt, Erdos697.erdos_697.parts.i, Erdos697.erdos_697.parts.ii
statement: formalized
---

# Erdős Problem 697

> *Reference:*
>  - [erdosproblems.com/697](https://www.erdosproblems.com/697)
>  - [Ha92] Hall, R. R., On some conjectures of Erdős in Astérisque. I. J. Number Theory (1992),
>     313--319.

*Quoted from [FormalConjectures/ErdosProblems/697.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/697.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/697](https://www.erdosproblems.com/697).

The file states 4 research or textbook statements: 4 solved.

## `Erdos697.density_exists`

Solved: stated here without proof.

> For each $m$ and $\alpha$, the density of the set of integers which are divisible by
> some $d \equiv 1 \pmod{m}$ with $1 < d < \exp (m ^ \alpha)$ exists.

```lean
theorem density_exists (m : ℕ) (α : ℝ) : ∃ δ, HasDensity
    {n : ℕ | ∃ d, d ≡ 1 [MOD m] ∧ (d : ℝ) ∈ Set.Ioo 1 (exp (m ^ α)) ∧ d ∣ n} δ
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/697.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/697.lean#L39).

## `Erdos697.erdos_697.variants.delta_lt`

Solved: stated here without proof.

> $\delta < \frac{m ^ \alpha + 1}{m}$. This shows that
> $lim_{m\rightarrow\infty} \delta (m, \alpha) = 0$ for $\alpha < 1$.
> At $m = 0$, both sides are 0, so the strict bound requires $m > 0$.
> #TODO: prove this theorem.

```lean
theorem erdos_697.variants.delta_lt (m : ℕ) (α : ℝ) (hm : 0 < m) : δ m α < (m ^ α + 1) / m
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/697.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/697.lean#L52).

## `Erdos697.erdos_697.parts.i`

Solved: stated here without proof.

> Let $\beta = \frac{1}{\log 2}$. Then $lim_{m\rightarrow\infty} \delta (m, \alpha) = 0$ if
> $\alpha < \beta$. This is proved in [Ha92].

```lean
theorem erdos_697.parts.i {α : ℝ} (hα : α < 1 / log (2 : ℝ)) : Tendsto (δ · α) atTop (𝓝 0)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/697.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/697.lean#L58).

## `Erdos697.erdos_697.parts.ii`

Solved: stated here without proof.

> $lim_{m\rightarrow\infty} \delta (m, \alpha) = 1$ if $\beta < \alpha$.
> This is proved in [Ha92].

```lean
theorem erdos_697.parts.ii {α : ℝ} (hα : 1 / log (2 : ℝ) < α) : Tendsto (δ · α) atTop (𝓝 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/697.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/697.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/697.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/697.lean)
- [erdosproblems.com/697](https://www.erdosproblems.com/697)
