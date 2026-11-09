---
declaration: theorem
origin: cited
lean: Erdos1164.erdos_1164, Erdos1164.erdos_1164.variants.dembo_peres_rosen_zeitouni
statement: formalized
---

# Erdős Problem 1164

> *References:*
> - [erdosproblems.com/1164](https://www.erdosproblems.com/1164)
> - [Va99] Various, *Some of Paul's favorite problems*. Booklet produced for the conference
>   "Paul Erdős and his mathematics", Budapest, July 1999 (1999).
> - [ErTa60] Erdős, P. and Taylor, S. J., *Some problems concerning the structure of random walk
>   paths*. Acta Math. Acad. Sci. Hungar. 11 (1960), 137--162.
>   [PDF](https://www.renyi.hu/~p_erdos/1960-17.pdf)
> - [Re90] Révész, P., *Random walk in random and non-random environments*. World Scientific,
>   Singapore (1990).
> - [DPRZ04] Dembo, A., Peres, Y., Rosen, J. and Zeitouni, O., *Cover times for Brownian motion and
>   random walks in two dimensions*. Ann. of Math. (2) 160 (2004), 433--464.
>   [arXiv:math/0107191](https://arxiv.org/abs/math/0107191)

*Quoted from [FormalConjectures/ErdosProblems/1164.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1164.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1164](https://www.erdosproblems.com/1164).

The file states 2 research or textbook statements: 2 solved. It also has 1 API statement, counted here but not shown.

## `Erdos1164.erdos_1164`

Solved: stated here without proof.

> Let $R_n$ be the maximal integer such that almost every random walk from the origin in
> $\mathbb{Z}^2$ visits every $x\in\mathbb{Z}^2$ with $\lVert x\rVert\leq R_n$ in at most $n$ steps.
>
> Is it true that
>
> $$\log R_n \asymp \sqrt{\log n}?$$
>
> A problem of Erdős and Taylor, see [ErTa60, p. 153] and [Va99, 6.76]. This is true, as proved
> independently by Révész [Re90] and Kesten, see [DPRZ04, Section 1.3], which reports that they
> proved the following. The probability that the disc of radius $n$ is covered by time
> $e^{t(\log n)^2}$ has $\liminf_{n\to\infty}$ at least $e^{-b/t}$ and $\limsup_{n\to\infty}$ at
> most $e^{-a/t}$ for every $t>0$, where $0\lt a\lt b\lt \infty$ are constants. The exact limit is in
> `erdos_1164.variants.dembo_peres_rosen_zeitouni`.
>
> We take the simple random walk (`IsSimpleRandomWalkSteps`). Read literally, $R_n$ would be $0$:
> for every $n$ some walk misses a neighbour of the origin, and such walks have positive
> probability. So $R_n=R_n(\omega)$ is the random variable `coveringRadius`, and
> $\log R_n\asymp\sqrt{\log n}$ means tightness: for every $\varepsilon>0$ there are constants
> $c>0$ and $C$ such that $c\sqrt{\log n}\leq\log R_n\leq C\sqrt{\log n}$ with probability at least
> $1-\varepsilon$ for all large $n$. This is the sense of the results above and of
> `erdos_1164.variants.dembo_peres_rosen_zeitouni`, which are about probabilities, not almost sure
> bounds. [ErTa60, p. 153] asks an almost sure question about the time needed to cover the disc of
> radius $n$; we follow the results in probability reported in [DPRZ04, Section 1.3].

```lean
theorem erdos_1164 {Ω : Type*} [MeasureSpace Ω] [IsProbabilityMeasure (ℙ : Measure Ω)]
    {X : ℕ → Ω → ℤ × ℤ} (hX : IsSimpleRandomWalkSteps X) :
    ∀ ε : ℝ, 0 < ε → ∃ c C : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop,
      1 - ε ≤ (ℙ {ω | c * Real.sqrt (Real.log n) ≤ Real.log (coveringRadius X n ω) ∧
        Real.log (coveringRadius X n ω) ≤ C * Real.sqrt (Real.log n)}).toReal
```

Category `research solved`; AMS [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/1164.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1164.lean#L111).

## `Erdos1164.erdos_1164.variants.dembo_peres_rosen_zeitouni`

Solved: stated here without proof.

> Dembo, Peres, Rosen and Zeitouni [DPRZ04, Theorem 1.4] proved a conjecture of Kesten and Révész:
> if $T_n$ is the time it takes the simple random walk in $\mathbb{Z}^2$ to cover the disc of
> radius $n$, then
>
> $$\lim_{n\to\infty}\mathbb{P}\left(\log T_n\leq t(\log n)^2\right)=e^{-4/t}$$
>
> for every $t>0$.
>
> The disc is $D_n=D(0,n)\cap\mathbb{Z}^2$ (`openDisc`). Since $T_n$ is an integer,
> $\log T_n\leq t(\log n)^2$ holds if and only if $T_n\leq\lfloor e^{t(\log n)^2}\rfloor$, that is,
> if the disc is covered by that time.

```lean
theorem erdos_1164.variants.dembo_peres_rosen_zeitouni {Ω : Type*} [MeasureSpace Ω]
    [IsProbabilityMeasure (ℙ : Measure Ω)] {X : ℕ → Ω → ℤ × ℤ}
    (hX : IsSimpleRandomWalkSteps X) (t : ℝ) (ht : 0 < t) :
    Tendsto (fun n : ℕ ↦
      (ℙ {ω | Covers X ⌊Real.exp (t * Real.log n ^ 2)⌋₊ ω (openDisc n)}).toReal)
      atTop (𝓝 (Real.exp (-4 / t)))
```

Category `research solved`; AMS [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/1164.lean, line 130](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1164.lean#L130).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1164.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1164.lean)
- [erdosproblems.com/1164](https://www.erdosproblems.com/1164)
