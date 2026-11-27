---
declaration: theorem
origin: cited
lean: Green35.green_35.lower, Green35.green_35.upper, Green35.variants.c_2_lower, Green35.variants.c_inf_lower, Green35.variants.c_inf_upper, Green35.variants.c_inf_upper_ae25, Green35.variants.c_inf_upper_ggtw25, Green35.variants.c_inf_lower_young
statement: formalized
---

# Ben Green's Open Problem 35

> Estimate the infimum of the $L^p$ norm of the self-convolution of a nonnegative integrable
> function supported on $[0,1]$ with total integral $1$.
>
> We model a function `f : [0,1] → ℝ≥0` as a function `f : ℝ → ℝ` that is nonnegative, integrable,
> supported on `[0,1]`, and has total integral `1`.
>
> *References:*
> - [Ben Green's Open Problem 35](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.35)
> - [Gr01](https://people.maths.ox.ac.uk/greenbj/papers/number-of-squares-and-Bh%5Bg%5D.pdf)
>   B. J. Green, *The number of squares and $B_h[g]$-sets*, Acta Arith. 100 (2001), no. 4, 365-390.
> - [CS17](https://arxiv.org/abs/1403.7988)
>   A. Cloninger and S. Steinerberger, *On suprema of autoconvolutions with an application to Sidon
>   sets*, Proc. Amer. Math. Soc. 145 (2017), no. 8, 3191-3200.
> - [MV10](https://arxiv.org/abs/0907.1379)
>   M. Matolcsi and C. Vinuesa, *Improved bounds on the supremum of autoconvolutions*,
>   J. Math. Anal. Appl. 372 (2010), 439-447.
> - [AE25](https://arxiv.org/abs/2506.13131)
>   A. Novikov et al., *AlphaEvolve: A coding agent for scientific and algorithmic discovery*,
>   arXiv:2506.13131 (2025), Appendix B.1.
> - [GGTW25](https://arxiv.org/abs/2511.02864)
>   B. Georgiev, J. Gómez-Serrano, T. Tao and A. Z. Wagner, *Mathematical exploration and discovery
>   at scale*, arXiv:2511.02864 (2025), Section 6.2.
> - [YD26](https://arxiv.org/abs/2601.16175)
>   M. Yuksekgonul et al., *Learning to Discover at Test Time*, arXiv:2601.16175 (2026).
>
> The constants of [CS17], [MV10], [AE25], [GGTW25] and [YD26] are stated for functions supported on
> $[-1/4, 1/4]$; rescaling to $[0, 1]$ halves them.

*Quoted from [FormalConjectures/GreensOpenProblems/35.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/GreensOpenProblems/35.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 8 research or textbook statements: 1 open, 6 solved and 1 textbook result.

## `Green35.green_35.lower`

Open: stated without proof.

> Lower bound for $c(p)$ for $1 < p \le \infty$, improving the known value $\sqrt{4/7}$ at
> $p = 2$ or the known value $0.64$ at $p = \infty$.

```lean
theorem green_35.lower :
    (∀ p, 1 < p → green_35.lower.answer p ≤ c p) ∧
      (ENNReal.ofReal (Real.sqrt (4 / 7)) < green_35.lower.answer 2 ∨
        0.64 < green_35.lower.answer ∞)
```

Category `research open`; AMS [26 Real functions](../../by-subject/part-01/26-real-functions/README.md), [28 Measure and integration](../../by-subject/part-01/28-measure-and-integration/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/GreensOpenProblems/35.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/GreensOpenProblems/35.lean#L72).

## `Green35.green_35.upper`

Solved: stated here without proof.

> Upper bound for $c(p)$ for $1 < p \le \infty$. The TTT-Discover construction gives
> $c(\infty) \le 0.751435$ after rescaling to $[0,1]$ [YD26].
> The answer is informative only at $p = \infty$ and is `⊤` otherwise.

```lean
theorem green_35.upper :
    (∀ p, 1 < p → c p ≤ green_35.upper.answer p) ∧ green_35.upper.answer ∞ < 0.7516
```

Category `research solved`; AMS [26 Real functions](../../by-subject/part-01/26-real-functions/README.md), [28 Measure and integration](../../by-subject/part-01/28-measure-and-integration/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/GreensOpenProblems/35.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/GreensOpenProblems/35.lean#L85).

## `Green35.variants.c_2_lower`

Solved: stated here without proof.

> Lower bound for $c(2)$ from Green's first paper ([Gr01]); the constant is `sqrt(4/7)` (about 0.7559).

```lean
theorem c_2_lower : ENNReal.ofReal (Real.sqrt (4 / 7)) ≤ c 2
```

Category `research solved`; AMS [26 Real functions](../../by-subject/part-01/26-real-functions/README.md), [28 Measure and integration](../../by-subject/part-01/28-measure-and-integration/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/GreensOpenProblems/35.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/GreensOpenProblems/35.lean#L94).

## `Green35.variants.c_inf_lower`

Solved: stated here without proof.

> Best-known lower bound for $c(\infty)$ due to Cloninger and Steinerberger ([CS17]).

```lean
theorem c_inf_lower : 0.64 ≤ c ∞
```

Category `research solved`; AMS [26 Real functions](../../by-subject/part-01/26-real-functions/README.md), [28 Measure and integration](../../by-subject/part-01/28-measure-and-integration/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/GreensOpenProblems/35.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/GreensOpenProblems/35.lean#L99).

## `Green35.variants.c_inf_upper`

Solved: stated here without proof.

> Upper bound for $c(\infty)$ due to Matolcsi and Vinuesa ([MV10]); their step function has
> autoconvolution supremum $1.50972\ldots$, which rescales to $0.75486\ldots$.

```lean
theorem c_inf_upper : c ∞ ≤ 0.7549
```

Category `research solved`; AMS [26 Real functions](../../by-subject/part-01/26-real-functions/README.md), [28 Measure and integration](../../by-subject/part-01/28-measure-and-integration/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/GreensOpenProblems/35.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/GreensOpenProblems/35.lean#L105).

## `Green35.variants.c_inf_upper_ae25`

Solved: stated here without proof.

> Upper bound for $c(\infty)$ found by AlphaEvolve ([AE25]) and recorded in Green's 2025
> update; the step function there has autoconvolution supremum at most $1.5053$, which rescales to
> $0.75265$.

```lean
theorem c_inf_upper_ae25 : c ∞ ≤ 0.75265
```

Category `research solved`; AMS [26 Real functions](../../by-subject/part-01/26-real-functions/README.md), [28 Measure and integration](../../by-subject/part-01/28-measure-and-integration/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/GreensOpenProblems/35.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/GreensOpenProblems/35.lean#L112).

## `Green35.variants.c_inf_upper_ggtw25`

Solved: stated here without proof.

> Best-known upper bound for $c(\infty)$ ([GGTW25], §6.2): a step function with autoconvolution
> supremum at most $1.5032$, which rescales to $0.7516$.

```lean
theorem c_inf_upper_ggtw25 : c ∞ ≤ 0.7516
```

Category `research solved`; AMS [26 Real functions](../../by-subject/part-01/26-real-functions/README.md), [28 Measure and integration](../../by-subject/part-01/28-measure-and-integration/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/GreensOpenProblems/35.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/GreensOpenProblems/35.lean#L118).

## `Green35.variants.c_inf_lower_young`

Textbook result, stated without proof.

> A comparison bound from Young's inequality.

```lean
theorem c_inf_lower_young : (c 2) ^ 2 ≤ c ∞
```

Category `textbook`; AMS [26 Real functions](../../by-subject/part-01/26-real-functions/README.md), [28 Measure and integration](../../by-subject/part-01/28-measure-and-integration/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/GreensOpenProblems/35.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/GreensOpenProblems/35.lean#L123).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/35.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/GreensOpenProblems/35.lean)
- [Ben Green's Open Problem 35](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.35)
