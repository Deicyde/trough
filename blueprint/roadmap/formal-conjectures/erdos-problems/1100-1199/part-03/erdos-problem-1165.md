---
declaration: theorem
origin: cited
lean: Erdos1165.erdos_1165, Erdos1165.erdos_1165.variants.hao_li_okada_zheng
statement: formalized
---

# Erdős Problem 1165

> *References:*
> - [erdosproblems.com/1165](https://www.erdosproblems.com/1165)
> - [Va99] Various, *Some of Paul's favorite problems*. Booklet produced for the conference
>   "Paul Erdős and his mathematics", Budapest, July 1999 (1999).
> - [HLOZ24] Hao, C., Li, X., Okada, I. and Zheng, Y., *Favorite sites for simple random walk in
>   two and more dimensions*. [arXiv:2409.00995](https://arxiv.org/abs/2409.00995) (2024).
> - [To01] Tóth, B., *No more than three favorite sites for simple random walk*.
>   Ann. Probab. 29 (2001), 484--503.

*Quoted from [FormalConjectures/ErdosProblems/1165.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1165.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1165](https://www.erdosproblems.com/1165).

The file states 2 research or textbook statements: 2 solved. It also has 2 API statements, counted here but not shown.

## `Erdos1165.erdos_1165`

Solved: stated here without proof.

> Given a random walk $s_0,s_1,\ldots$ in $\mathbb{Z}^2$, starting at the origin, let $f_n(x)$ count
> the number of $0\leq k\leq n$ such that $s_k=x$.
>
> Let
>
> $$F(n)=\{ x: f_n(x) = \max_y f_n(y)\}$$
>
> be the set of 'favourite values'. Find
>
> $$\mathbb{P}(\lvert F(n)\rvert=r\textrm{ infinitely often})$$
>
> for $r\geq 3$.
>
> A problem of Erdős and Révész [Va99, 6.77]. We take the simple random walk, on any probability
> space (`IsSimpleRandomWalkSteps`). Hao, Li, Okada and Zheng [HLOZ24, Theorem 1.1] showed that the
> probability is $1$ for $r=3$ and $0$ for $r\geq 4$, see `erdos_1165.variants.hao_li_okada_zheng`.
> The value of `erdos_1165.answer` for $r<3$ is not used.

```lean
theorem erdos_1165 {Ω : Type*} [MeasureSpace Ω] [IsProbabilityMeasure (ℙ : Measure Ω)]
    {X : ℕ → Ω → ℤ × ℤ} (hX : IsSimpleRandomWalkSteps X) (r : ℕ) (hr : 3 ≤ r) :
    ℙ {ω | ∃ᶠ n in atTop, (favouriteSites X n ω).encard = (r : ℕ∞)} = erdos_1165.answer r
```

Category `research solved`; AMS [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/1165.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1165.lean#L98).

## `Erdos1165.erdos_1165.variants.hao_li_okada_zheng`

Solved: stated here without proof.

> Hao, Li, Okada and Zheng [HLOZ24, Theorem 1.1] proved that, for the simple random walk on
> $\mathbb{Z}^2$, almost surely
>
> $$\limsup_{n\to\infty} \#K^{(2)}(n) = 3,$$
>
> where $K^{(2)}(n)$ is the set of favourite sites at time $n$. The cardinalities are natural
> numbers, so almost surely there are eventually at most three favourite sites, and exactly three
> infinitely often. Tóth [To01] proved the corresponding bound for the one-dimensional walk, see
> [HLOZ24, Section 1].

```lean
theorem erdos_1165.variants.hao_li_okada_zheng {Ω : Type*} [MeasureSpace Ω]
    [IsProbabilityMeasure (ℙ : Measure Ω)] {X : ℕ → Ω → ℤ × ℤ} (hX : IsSimpleRandomWalkSteps X) :
    ∀ᵐ ω, limsup (fun n ↦ (favouriteSites X n ω).encard) atTop = 3
```

Category `research solved`; AMS [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/1165.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1165.lean#L113).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1165.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1165.lean)
- [erdosproblems.com/1165](https://www.erdosproblems.com/1165)
