---
declaration: theorem
origin: cited
lean: Arxiv.«2605.18081».fisherInformationConvexity, Arxiv.«2605.18081».fisherInformationConvexity.variants.smooth
statement: formalized
---

# Convexity of Fisher information along the heat flow

> Can the functional $\mathcal{D}[f]$ be negative for an admissible density $f$? Equivalently, is
> the Fisher information of the Gaussian heat flow always convex in time? This is Problem (iii) of
> [ZFGW26, Section 7.3]; it is known in dimensions $d \le 4$ and left open for $d \ge 5$
> [ZFGW26, Section 7.2].
>
> References:
> - [ZFGW26] J. Zou, L. Fan, J. Gao and J. Wang, *A Hexagonal Counterexample to Log-Convexity of
>   Fisher Information Along the Heat Flow*, arXiv:2605.18081 (2026).
>   https://arxiv.org/abs/2605.18081
> - [Ki26] K. Kitamura, *Fisher information along the heat flow is not convex*, Lean 4
>   formalization (2026),
>   [GitHub repository](https://github.com/KitaKen1/fisher-information-nonconvexity/tree/a6ff274a04e5b6d813b6f06dc62d3d68a21ae31a).

*Quoted from [FormalConjectures/Arxiv/2605.18081/FisherInformationConvexity.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2605.18081/FisherInformationConvexity.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved.

## `Arxiv.«2605.18081».fisherInformationConvexity`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/fisher-information-nonconvexity/blob/fe6ade9846c53e5cb0dcbc00eca359c83f8d0f55/lean/Fisher41/FC/Main.lean#L37](https://github.com/KitaKen1/fisher-information-nonconvexity/blob/fe6ade9846c53e5cb0dcbc00eca359c83f8d0f55/lean/Fisher41/FC/Main.lean#L37).

> Is the Fisher information convex along the heat flow for every admissible density
> [ZFGW26, Section 7.3, Problem (iii)]? The answer is no [Ki26].

```lean
theorem fisherInformationConvexity :
    ¬ ∀ (d : ℕ) (f : EuclideanSpace ℝ (Fin d) → ℝ), IsAdmissible f →
      ConvexOn ℝ (Set.Ioi 0) (fun t => fisherInformation (heatFlow f t))
```

Category `research solved`; AMS [35 Partial differential equations](../../by-subject/part-02/35-partial-differential-equations/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/Arxiv/2605.18081/FisherInformationConvexity.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2605.18081/FisherInformationConvexity.lean#L84).

## `Arxiv.«2605.18081».fisherInformationConvexity.variants.smooth`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/fisher-information-nonconvexity/blob/fe6ade9846c53e5cb0dcbc00eca359c83f8d0f55/lean/Fisher41/FC/Main.lean#L48](https://github.com/KitaKen1/fisher-information-nonconvexity/blob/fe6ade9846c53e5cb0dcbc00eca359c83f8d0f55/lean/Fisher41/FC/Main.lean#L48).

> The same question for every smooth positive probability density with finite Fisher
> information. The answer is no [Ki26].

```lean
theorem fisherInformationConvexity.variants.smooth :
    ¬ ∀ (d : ℕ) (f : EuclideanSpace ℝ (Fin d) → ℝ), IsWeaklyAdmissible f →
      ConvexOn ℝ (Set.Ioi 0) (fun t => fisherInformation (heatFlow f t))
```

Category `research solved`; AMS [35 Partial differential equations](../../by-subject/part-02/35-partial-differential-equations/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/Arxiv/2605.18081/FisherInformationConvexity.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2605.18081/FisherInformationConvexity.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2605.18081/FisherInformationConvexity.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2605.18081/FisherInformationConvexity.lean)
- [https://arxiv.org/abs/2605.18081](https://arxiv.org/abs/2605.18081)
