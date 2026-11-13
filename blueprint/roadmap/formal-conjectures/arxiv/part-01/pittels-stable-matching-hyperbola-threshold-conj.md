---
declaration: theorem
origin: cited
lean: Arxiv.«2406.10319».pittel_hyperbola_threshold
statement: formalized
---

# Pittel's stable-matching hyperbola threshold conjecture

> *Reference:*
> [On Constrained Matchings, Stable Under Random Preferences](https://doi.org/10.1002/rsa.70036)
> by Boris Pittel, Section 6, Notes (2).
> The conjecture also appears in the [arXiv preprint, p. 26](https://arxiv.org/pdf/2406.10319#page=26).

*Quoted from [FormalConjectures/Arxiv/2406.10319/StableMatchingHyperbola.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2406.10319/StableMatchingHyperbola.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Arxiv.«2406.10319».pittel_hyperbola_threshold`

Open: stated without proof.

> Pittel conjectures a threshold $p_*(n)$ for the rank pairs across stable matchings to trace
> out a hyperbola. For all sufficiently large $n$, it lies between $\frac{9}{4}(\log n)^2/n$ and $1$.
>
> The fixed reciprocal arc $(t,t^{-1})$ for $t \in [2/3,3/2]$ specifies the curve to cover in this
> formulation. For each fixed $0\lt \delta<1$, compare probabilities at distance at least
> $\delta\min(p_*(n),1-p_*(n))$ from the threshold. The relative margin keeps both comparison
> ranges nonempty. On the upper range, the event holds with high probability uniformly at every
> positive tolerance. On the lower range, it fails with high probability uniformly at one positive
> tolerance for each $\delta$.

```lean
theorem pittel_hyperbola_threshold :
    ∃ pStar : ℕ → Set.Ioo (0 : ℝ) 1,
      let d (n : ℕ) := min (pStar n : ℝ) (1 - (pStar n : ℝ))
      (∀ᶠ (n : ℕ) in atTop, (9 / 4 : ℝ) * (Real.log n) ^ 2 / n < (pStar n : ℝ)) ∧
      ∀ δ ∈ Set.Ioo (0 : ℝ) 1,
        (∀ ε > 0, Tendsto (fun n ↦
          ⨆ p : {p : unitInterval // (pStar n : ℝ) + δ * d n ≤ (p : ℝ)},
            marketLaw n p.1 (hyperbolaEvent n p.1 ε)ᶜ) atTop (𝓝 0)) ∧
        ∃ ε > 0, Tendsto (fun n ↦
          ⨆ p : {p : unitInterval // (p : ℝ) ≤ (pStar n : ℝ) - δ * d n},
            marketLaw n p.1 (hyperbolaEvent n p.1 ε)) atTop (𝓝 0)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/Arxiv/2406.10319/StableMatchingHyperbola.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2406.10319/StableMatchingHyperbola.lean#L63).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2406.10319/StableMatchingHyperbola.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2406.10319/StableMatchingHyperbola.lean)
- [On Constrained Matchings, Stable Under Random Preferences](https://doi.org/10.1002/rsa.70036)
