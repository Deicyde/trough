---
declaration: theorem
origin: cited
lean: Erdos995.erdos_995, Erdos995.erdos_995.variants.erdos_lower_bound
statement: formalized
---

# Erdős Problem 995

> *References:*
> - [erdosproblems.com/995](https://www.erdosproblems.com/995)
> - [Er49] Erdős, P., On the strong law of large numbers, Trans. Amer. Math. Soc. (1949),
>   329-334.
>
> Let $n_1 < n_2 < \cdots$ be a lacunary sequence of integers and $f \in L^2([0,1])$ with
> $\int_0^1 f = 0$. Estimate the growth of
>
> $$S_N(\alpha) = \sum_{k \le N} f(\{\alpha n_k\})$$
>
> for almost all $\alpha$, where $\{\cdot\}$ denotes the fractional part. In particular, is it
> true that $S_N(\alpha) = o\!\left(N \sqrt{\log\log N}\right)$ for almost all $\alpha$?
>
> Erdős [Er49] constructed a lacunary sequence and a mean-zero $f \in L^2([0,1])$ for which, for
> every $\varepsilon > 0$, $\limsup_N S_N(\alpha) / (N (\log\log N)^{1/2 - \varepsilon}) = \infty$
> for almost all $\alpha$, and believed this lower bound to be close to the truth.
>
> The mean-zero hypothesis $\int_0^1 f = 0$ is the natural normalisation: otherwise the sum has a
> linear main term coming from the average of $f$.

*Quoted from [FormalConjectures/ErdosProblems/995.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/995.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/995](https://www.erdosproblems.com/995).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos995.erdos_995`

Open: stated without proof.

> Erdős Problem 995:
>
> For every lacunary sequence $(n_k)$ of integers and every $f \in L^2([0,1])$ with
> $\int_0^1 f = 0$, is it true that for almost all $\alpha$,
>
> $$\sum_{k < N} f(\{\alpha n_k\}) = o\!\left(N \sqrt{\log\log N}\right)?$$

```lean
theorem erdos_995 :
    ∀ (n : ℕ → ℕ), IsLacunary n → ∀ (f : ℝ → ℝ),
      MemLp f 2 (volume.restrict (Icc (0 : ℝ) 1)) →
      ∫ x in (0 : ℝ)..1, f x = 0 →
      ∀ᵐ α ∂(volume.restrict (Icc (0 : ℝ) 1)),
        partialSum n f α =o[atTop] fun N => (N : ℝ) * Real.sqrt (Real.log (Real.log N))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [42 Harmonic analysis on Euclidean spaces](../../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/ErdosProblems/995.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/995.lean#L60).

## `Erdos995.erdos_995.variants.erdos_lower_bound`

Solved: stated here without proof.

> Erdős [Er49] showed the growth cannot be pushed below $N (\log\log N)^{1/2}$ by more than an
> arbitrarily small power: there is a lacunary sequence and a mean-zero $f \in L^2([0,1])$ such
> that for every $\varepsilon > 0$, for almost all $\alpha$,
>
> $$\limsup_{N \to \infty} \frac{\sum_{k < N} f(\{\alpha n_k\})}{N (\log\log N)^{1/2 - \varepsilon}}
>   = \infty.$$

```lean
theorem erdos_995.variants.erdos_lower_bound :
    ∃ (n : ℕ → ℕ), IsLacunary n ∧ ∃ (f : ℝ → ℝ),
      MemLp f 2 (volume.restrict (Icc (0 : ℝ) 1)) ∧
      ∫ x in (0 : ℝ)..1, f x = 0 ∧
      ∀ ε > (0 : ℝ),
        ∀ᵐ α ∂(volume.restrict (Icc (0 : ℝ) 1)),
          atTop.limsup (fun N => (((partialSum n f α N) /
            ((N : ℝ) * (Real.log (Real.log N)) ^ ((1 : ℝ) / 2 - ε)) : ℝ) : EReal)) = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [42 Harmonic analysis on Euclidean spaces](../../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/ErdosProblems/995.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/995.lean#L76).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/995.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/995.lean)
- [erdosproblems.com/995](https://www.erdosproblems.com/995)
