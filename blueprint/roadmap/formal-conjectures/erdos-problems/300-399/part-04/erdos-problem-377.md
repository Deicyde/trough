---
declaration: theorem
origin: cited
lean: Erdos377.erdos_377, Erdos377.erdos_377.variants.limit.i, Erdos377.erdos_377.variants.limit.ii, Erdos377.erdos_377.variants.ae, Erdos377.erdos_377.variants.ub
statement: formalized
---

# Erdős Problem 377

> *Reference:* [erdosproblems.com/377](https://www.erdosproblems.com/377)

*Quoted from [FormalConjectures/ErdosProblems/377.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/377.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/377](https://www.erdosproblems.com/377).

The file states 5 research or textbook statements: 1 open and 4 solved.

## `Erdos377.erdos_377`

Open: stated without proof.

> Is there some absolute constant $C > 0$ such that
>
> $$
>   \sum_{p \leq n} 1_{p\nmid {2n \choose n}}\frac{1}{p} \leq C
> $$
>
> for all $n$?

```lean
theorem erdos_377 :
    ∃ C > (0 : ℝ), ∀ (n : ℕ), sumInvPrimesNotDvdCentralBinom n ≤ C
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/377.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/377.lean#L49).

## `Erdos377.erdos_377.variants.limit.i`

Solved: stated here without proof.

> Erdos, Graham, Ruzsa, and Straus proved that if
>
> $$
>   f(n) = \sum_{p \leq n} 1_{p\nmid {2n \choose n}}\frac{1}{p}
> $$
>
> and
>
> $$
>   \gamma_0 = \sum_{k = 2}^{\infty} \frac{\log k}{2^k}
> $$
>
> then
>
> $$
>   \lim_{x\to\infty} \frac{1}{x}\sum_{n\leq x} f(n) = \gamma_0
> $$
>
> [EGRS75] Erdős, P. and Graham, R. L. and Ruzsa, I. Z. and Straus, E. G., _On the prime factors of $\binom{2n}{n}$_. Math. Comp. (1975), 83-92.

```lean
theorem erdos_377.variants.limit.i (γ₀ : ℝ)
    (hγ₀ : γ₀ = ∑' (k : ℕ), (k + 2 : ℝ).log / 2 ^ (k + 2)) :
    Tendsto (fun (x : ℕ) => (1 : ℝ) / x * ∑ n ∈ Finset.Icc 1 x, sumInvPrimesNotDvdCentralBinom n)
      atTop (𝓝 γ₀)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/377.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/377.lean#L70).

## `Erdos377.erdos_377.variants.limit.ii`

Solved: stated here without proof.

> Erdos, Graham, Ruzsa, and Straus proved that if
>
> $$
>   f(n) = \sum_{p \leq n} 1_{p\nmid {2n \choose n}}\frac{1}{p}
> $$
>
> and
>
> $$
>   \gamma_0 = \sum_{k = 2}^{\infty} \frac{\log k}{2^k}
> $$
>
> then
>
> $$
>   \lim_{x\to\infty} \frac{1}{x}\sum_{n\leq x} f(n)^2 = \gamma_0^2
> $$
>
> [EGRS75] Erdős, P. and Graham, R. L. and Ruzsa, I. Z. and Straus, E. G., _On the prime factors of $\binom{2n}{n}$_. Math. Comp. (1975), 83-92.

```lean
theorem erdos_377.variants.limit.ii (γ₀ : ℝ)
    (hγ₀ : γ₀ = ∑' (k : ℕ), (k + 2 : ℝ).log / 2 ^ (k + 2)) :
    Tendsto (fun (x : ℕ) =>
      (1 : ℝ) / x * ∑ n ∈ Finset.Icc 1 x, sumInvPrimesNotDvdCentralBinom n ^ 2)
      atTop (𝓝 (γ₀ ^ 2))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/377.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/377.lean#L93).

## `Erdos377.erdos_377.variants.ae`

Solved: stated here without proof.

> Erdos, Graham, Ruzsa, and Straus proved that if
>
> $$
>   f(n) = \sum_{p \leq n} 1_{p\nmid {2n \choose n}}\frac{1}{p}
> $$
>
> and
>
> $$
>   \gamma_0 = \sum_{k = 2}^{\infty} \frac{\log k}{2^k}
> $$
>
> then for almost all integers $f(m) = \gamma_0 + o(1)$, i.e. for every $\varepsilon > 0$ the set of
> $n$ with $|f(n) - \gamma_0| < \varepsilon$ has natural density one.
>
> [EGRS75] Erdős, P. and Graham, R. L. and Ruzsa, I. Z. and Straus, E. G., _On the prime factors of $\binom{2n}{n}$_. Math. Comp. (1975), 83-92.

```lean
theorem erdos_377.variants.ae (γ₀ : ℝ) (hγ₀ : γ₀ = ∑' (k : ℕ), (k + 2 : ℝ).log / 2 ^ (k + 2)) :
    ∀ ε > (0 : ℝ), {n : ℕ | |sumInvPrimesNotDvdCentralBinom n - γ₀| < ε}.HasDensity 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/377.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/377.lean#L115).

## `Erdos377.erdos_377.variants.ub`

Solved: stated here without proof.

> Erdos, Graham, Ruzsa, and Straus proved that if
>
> $$
>   f(n) = \sum_{p \leq n} 1_{p\nmid {2n \choose n}}\frac{1}{p}
> $$
>
> then there is some constant $c < 1$ such that for all large $n$
>
> $$
>   f(n) \leq c \log\log n.
> $$
>
> [EGRS75] Erdős, P. and Graham, R. L. and Ruzsa, I. Z. and Straus, E. G., _On the prime factors of $\binom{2n}{n}$_. Math. Comp. (1975), 83-92.

```lean
theorem erdos_377.variants.ub : ∃ c < (1 : ℝ),
      ∀ᶠ n in atTop, sumInvPrimesNotDvdCentralBinom n ≤ c * (n : ℝ).log.log
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/377.lean, line 132](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/377.lean#L132).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/377.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/377.lean)
- [erdosproblems.com/377](https://www.erdosproblems.com/377)
