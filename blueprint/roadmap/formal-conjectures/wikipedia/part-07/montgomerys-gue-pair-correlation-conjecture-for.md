---
declaration: theorem
origin: cited
lean: MontgomeryPairCorrelationConjecture.montgomery_pair_correlation_conjecture, MontgomeryPairCorrelationConjecture.montgomery_pair_correlation_conjecture.variants.general_interval
statement: formalized
---

# Montgomery's GUE pair correlation conjecture for zeta zeros

> Hugh L. Montgomery (1973) studied vertical spacings among critical-line zeros $1/2 + i\gamma$ of
> $\zeta(s)$ assuming `RiemannHypothesis`, observing with Freeman Dyson that their predicted two-point
> density matches Gaussian Unitary Ensemble (GUE) eigenvalue pair statistics. Counting positive
> ordinates $0 < \gamma, \gamma' \le T$ with multiplicity, Montgomery conjectured that for fixed
> $0 < \alpha < \beta$,
>
> $$\lim_{T \to \infty}
>   \frac{\#\left\{(\gamma, \gamma') \in (0, T]^2 :
>     \frac{2\pi\alpha}{\log T} \le \gamma - \gamma' \le \frac{2\pi\beta}{\log T}\right\}}
>   {\frac{T}{2\pi} \log T}
>   = \int_\alpha^\beta \left(1 - \operatorname{sinc}(\pi u)^2\right) du,$$
>
> and more generally for all $\alpha \le \beta$ with an added point-mass term $\mathbf{1}_{0 \in
> [\alpha, \beta]}$.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Montgomery%27s_pair_correlation_conjecture)
> - H. L. Montgomery, *The pair correlation of zeros of the zeta function*, Proc. Sympos. Pure Math.
>   **24**, Amer. Math. Soc., 1973, 181–193.

*Quoted from [FormalConjectures/Wikipedia/MontgomeryPairCorrelationConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MontgomeryPairCorrelationConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 2 test statements and 3 API statements, counted here but not shown.

## `MontgomeryPairCorrelationConjecture.montgomery_pair_correlation_conjecture`

Open: stated without proof.

> Montgomery's Pair Correlation Conjecture (1973): given `RiemannHypothesis`, for every
> $0 < \alpha < \beta$, the normalized pair count of critical-line zeros of $\zeta(s)$ in $(0, T]$
> with normalized spacing in $[\alpha, \beta]$ converges to
> $\int_\alpha^\beta \left(1 - \operatorname{sinc}(\pi u)^2\right) du$ as $T \to \infty$.

```lean
theorem montgomery_pair_correlation_conjecture (hRH : RiemannHypothesis)
    (α β : ℝ) (hα : 0 < α) (hαβ : α < β) :
    Filter.Tendsto
      (fun T : ℝ => (zetaPairCorrelationCount T α β : ℝ) / ((T / (2 * Real.pi)) * Real.log T))
      Filter.atTop
      (nhds (∫ u in α..β, guePairKernel u))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/Wikipedia/MontgomeryPairCorrelationConjecture.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MontgomeryPairCorrelationConjecture.lean#L114).

## `MontgomeryPairCorrelationConjecture.montgomery_pair_correlation_conjecture.variants.general_interval`

Open: stated without proof.

> General-interval form of Montgomery's Pair Correlation Conjecture: given `RiemannHypothesis`,
> for any fixed $\alpha \le \beta$, the normalized pair count converges to
> $\int_\alpha^\beta \left(1 - \operatorname{sinc}(\pi u)^2\right) du + \mathbf{1}_{0 \in [\alpha,
> \beta]}$ as $T \to \infty$.

```lean
theorem montgomery_pair_correlation_conjecture.variants.general_interval
    (hRH : RiemannHypothesis) (α β : ℝ) (hαβ : α ≤ β) :
    Filter.Tendsto
      (fun T : ℝ => (zetaPairCorrelationCount T α β : ℝ) / ((T / (2 * Real.pi)) * Real.log T))
      Filter.atTop
      (nhds ((∫ u in α..β, guePairKernel u) + if (0 : ℝ) ∈ Set.Icc α β then 1 else 0))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/Wikipedia/MontgomeryPairCorrelationConjecture.lean, line 128](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MontgomeryPairCorrelationConjecture.lean#L128).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/MontgomeryPairCorrelationConjecture.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MontgomeryPairCorrelationConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Montgomery%27s_pair_correlation_conjecture)
