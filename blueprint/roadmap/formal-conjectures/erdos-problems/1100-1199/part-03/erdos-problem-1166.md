---
declaration: theorem
origin: cited
lean: Erdos1166.erdos_1166, Erdos1166.erdos_1166.variants.erdos_taylor, Erdos1166.erdos_1166.variants.dembo_peres_rosen_zeitouni
statement: formalized
---

# Erdős Problem 1166

> *References:*
> - [erdosproblems.com/1166](https://www.erdosproblems.com/1166)
> - [Va99] Various, *Some of Paul's favorite problems*. Booklet produced for the conference
>   "Paul Erdős and his mathematics", Budapest, July 1999 (1999).
> - [ErTa60] Erdős, P. and Taylor, S. J., *Some problems concerning the structure of random walk
>   paths*. Acta Math. Acad. Sci. Hungar. 11 (1960), 137--162.
>   [PDF](https://www.renyi.hu/~p_erdos/1960-17.pdf)
> - [DPRZ01] Dembo, A., Peres, Y., Rosen, J. and Zeitouni, O., *Thick points for planar Brownian
>   motion and the Erdős-Taylor conjecture on random walk*. Acta Math. 186 (2001), 239--270.
>   [doi:10.1007/BF02401841](https://doi.org/10.1007/BF02401841)
> - [HLOZ24] Hao, C., Li, X., Okada, I. and Zheng, Y., *Favorite sites for simple random walk in
>   two and more dimensions*. [arXiv:2409.00995](https://arxiv.org/abs/2409.00995) (2024).

*Quoted from [FormalConjectures/ErdosProblems/1166.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1166.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1166](https://www.erdosproblems.com/1166).

The file states 3 research or textbook statements: 3 solved. It also has 2 API statements, counted here but not shown.

## `Erdos1166.erdos_1166`

Solved: stated here without proof.

> Given a random walk $s_0,s_1,\ldots$ in $\mathbb{Z}^2$, starting at the origin, let $f_k(x)$ count
> the number of $0\leq l\leq k$ such that $s_l=x$.
>
> Let
>
> $$F(k)=\{ x: f_k(x) = \max_y f_k(y)\}$$
>
> be the set of 'favourite values'. Is it true that
>
> $$\left\lvert \bigcup_{k\leq n}F(k)\right\rvert \leq (\log n)^{O(1)}$$
>
> almost surely, for all but finitely many $n$?
>
> A problem of Erdős and Révész [Va99, 6.78]. The answer is yes. Almost surely there are at most
> three favourite sites at all large times [HLOZ24, Theorem 1.1], see
> `Erdos1165.erdos_1165.variants.hao_li_okada_zheng`, and the maximal local time is
> $O((\log n)^2)$ [ErTa60, p. 162], see `erdos_1166.variants.erdos_taylor`. A favourite
> site stays a favourite site for as long as the maximal local time does not change. So for each
> value of the maximal local time, the sites that are favourite at some time while it has that value
> are all favourite at the last such time, and there are at most three of them, up to finitely many
> exceptions. This gives the bound $O((\log n)^2)$ stated on the problem page.
>
> We take the simple random walk (`IsSimpleRandomWalkSteps`). We read $O(1)$ as a single exponent
> `C` that works for almost every walk. The cardinality is `Set.encard`, so an infinite union would
> not satisfy the bound.

```lean
theorem erdos_1166 {Ω : Type*} [MeasureSpace Ω] [IsProbabilityMeasure (ℙ : Measure Ω)]
    {X : ℕ → Ω → ℤ × ℤ} (hX : IsSimpleRandomWalkSteps X) :
    ∃ C : ℕ, ∀ᵐ ω, ∀ᶠ n : ℕ in atTop,
      ((⋃ k ≤ n, favouriteSites X k ω).encard : ℝ≥0∞) ≤ ENNReal.ofReal (Real.log n ^ C)
```

Category `research solved`; AMS [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/1166.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1166.lean#L105).

## `Erdos1166.erdos_1166.variants.erdos_taylor`

Solved: stated here without proof.

> Erdős and Taylor [ErTa60, p. 162] proved that, for the simple random walk on $\mathbb{Z}^2$, if
> $T_n$ is the maximal number of visits to a point in the first $n$ steps, then almost surely
>
> $$\frac{1}{4\pi}\leq\liminf_{n\to\infty}\frac{T_n}{(\log n)^2}
>   \leq\limsup_{n\to\infty}\frac{T_n}{(\log n)^2}\leq\frac{1}{\pi}.$$
>
> They conjectured that the limit exists and equals $1/\pi$, see
> `erdos_1166.variants.dembo_peres_rosen_zeitouni`.
>
> We use `maxLocalTime`, which also counts the visit at time $0$. This changes $T_n$ by at most one.
> The bounds are stated with $\varepsilon$ to avoid the junk values of `liminf` and `limsup`.

```lean
theorem erdos_1166.variants.erdos_taylor {Ω : Type*} [MeasureSpace Ω]
    [IsProbabilityMeasure (ℙ : Measure Ω)] {X : ℕ → Ω → ℤ × ℤ}
    (hX : IsSimpleRandomWalkSteps X) :
    ∀ᵐ ω, ∀ ε : ℝ, 0 < ε →
      (∀ᶠ n : ℕ in atTop, 1 / (4 * π) - ε ≤ (maxLocalTime X n ω : ℝ) / Real.log n ^ 2) ∧
      (∀ᶠ n : ℕ in atTop, (maxLocalTime X n ω : ℝ) / Real.log n ^ 2 ≤ 1 / π + ε)
```

Category `research solved`; AMS [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/1166.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1166.lean#L123).

## `Erdos1166.erdos_1166.variants.dembo_peres_rosen_zeitouni`

Solved: stated here without proof.

> Dembo, Peres, Rosen and Zeitouni [DPRZ01, Theorem 1.1] proved the conjecture of Erdős and Taylor:
> for the simple random walk on $\mathbb{Z}^2$, if $T_n^*$ is the maximal number of visits to a
> point in the first $n$ steps, then almost surely
>
> $$\lim_{n\to\infty}\frac{T_n^*}{(\log n)^2}=\frac{1}{\pi}.$$
>
> `maxLocalTime` counts the visit at time $0$. Whether this visit is counted changes $T_n^*$ by at
> most one, so the limit is the same.

```lean
theorem erdos_1166.variants.dembo_peres_rosen_zeitouni {Ω : Type*} [MeasureSpace Ω]
    [IsProbabilityMeasure (ℙ : Measure Ω)] {X : ℕ → Ω → ℤ × ℤ}
    (hX : IsSimpleRandomWalkSteps X) :
    ∀ᵐ ω, Tendsto (fun n : ℕ ↦ (maxLocalTime X n ω : ℝ) / Real.log n ^ 2) atTop (𝓝 (1 / π))
```

Category `research solved`; AMS [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/1166.lean, line 141](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1166.lean#L141).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1166.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1166.lean)
- [erdosproblems.com/1166](https://www.erdosproblems.com/1166)
