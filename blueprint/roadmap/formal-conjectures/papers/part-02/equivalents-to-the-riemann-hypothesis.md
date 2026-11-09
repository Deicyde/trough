---
declaration: theorem
origin: cited
lean: RiemannHypothesis.robin_criterion, RiemannHypothesis.robin_criterion_rhs, RiemannHypothesis.lagarias_criterion, RiemannHypothesis.lagarias_criterion_rhs, RiemannHypothesis.li_criterion, RiemannHypothesis.li_criterion_rhs, RiemannHypothesis.beurling_nyman_criterion, RiemannHypothesis.beurling_nyman_criterion_rhs, RiemannHypothesis.weil_positivity_criterion, RiemannHypothesis.weil_positivity_criterion_rhs
statement: formalized
---

# Equivalents to the Riemann Hypothesis

> This file contains formal statements that are known to be equivalent to the Riemann Hypothesis,
> following the survey [Co26], §4. The statement of the Riemann Hypothesis itself is in
> `FormalConjectures.Millennium.RiemannHypothesis`.
>
> *References:*
> * [Co26] A. Connes, [The Riemann Hypothesis: Past, Present and a Letter Through
>   Time](https://arxiv.org/abs/2602.04022), 2026.

*Quoted from [FormalConjectures/Paper/RiemannHypothesisEquivalents.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannHypothesisEquivalents.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 10 research or textbook statements: 5 open and 5 solved. It also has 2 API statements, counted here but not shown.

## `RiemannHypothesis.robin_criterion`

Solved: stated here without proof.

> **Robin's Criterion**. The Riemann Hypothesis is equivalent to
> $$
>   \sigma(n) < e ^ {\gamma} n\log\log n
> $$
> for all $n > 5040$, where $\gamma$ is the Euler-Mascheroni constant and $\sigma(n)$ is
> the sum of divisors.

```lean
theorem robin_criterion :
    RiemannHypothesis ↔ ∀ n > 5040, σ 1 n < (exp eulerMascheroniConstant) * n * log (log n)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannHypothesisEquivalents.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannHypothesisEquivalents.lean#L46).

## `RiemannHypothesis.robin_criterion_rhs`

Open: stated without proof.

> The statement that Robin's criterion holds.

```lean
theorem robin_criterion_rhs {n : ℕ} (hn : n > 5040) :
    σ 1 n < exp eulerMascheroniConstant * n * log (log n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannHypothesisEquivalents.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannHypothesisEquivalents.lean#L52).

## `RiemannHypothesis.lagarias_criterion`

Solved: stated here without proof.

> **Lagarias' Criterion**. A refinement of Robin's criterion: the Riemann Hypothesis
> is equivalent to
> $$
>   \sigma(n) < H_n + e^{H_n}\log H_n
> $$
> for all $n \geq 2$, where $H_n = 1 + 1/2 + \cdots + 1/n$ is the $n$th harmonic number.
>
> Note that [Co26] states this for all $n \geq 1$, but at $n = 1$ both sides equal $1$; Lagarias'
> original formulation is the non-strict inequality for all $n \geq 1$, with equality only at
> $n = 1$.

```lean
theorem lagarias_criterion : RiemannHypothesis ↔
    ∀ n > 1, σ 1 n < harmonic n + exp (harmonic n) * log (harmonic n)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannHypothesisEquivalents.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannHypothesisEquivalents.lean#L67).

## `RiemannHypothesis.lagarias_criterion_rhs`

Open: stated without proof.

> The statement that Lagarias' criterion holds.

```lean
theorem lagarias_criterion_rhs {n : ℕ} (hn : 1 < n) :
    σ 1 n < harmonic n + exp (harmonic n) * log (harmonic n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannHypothesisEquivalents.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannHypothesisEquivalents.lean#L73).

## `RiemannHypothesis.li_criterion`

Solved: stated here without proof.

> **Li's Criterion**. The Riemann Hypothesis is equivalent to the positivity of
> $$
>   \lambda_n := \sum_{\rho}\left(1 - \left(1 - \frac{1}{\rho}\right)^n\right)
> $$
> for each $n > 0$.

```lean
theorem li_criterion : RiemannHypothesis ↔ ∀ n > 0, 0 < lambda n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannHypothesisEquivalents.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannHypothesisEquivalents.lean#L102).

## `RiemannHypothesis.li_criterion_rhs`

Open: stated without proof.

> The statement that Li's criterion holds.

```lean
theorem li_criterion_rhs {n : ℕ} (hn : 0 < n) : 0 < lambda n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannHypothesisEquivalents.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannHypothesisEquivalents.lean#L107).

## `RiemannHypothesis.beurling_nyman_criterion`

Solved: stated here without proof.

> **Beurling-Nyman Criterion**. The Riemann Hypothesis is equivalent to the statement that
> the set of finite linear combination $\sum_{\nu = 1}^n c_{\nu}\rho_{\theta_{\nu}}$ is dense
> in $L^2(0, 1)$, when ranging over $0 < \theta_{\nu}\leq 1$ and
> $\sum_{\nu = 1}^n c_{\nu}\theta_{\nu} = 0$.

```lean
theorem beurling_nyman_criterion : RiemannHypothesis ↔
    Dense { fractScalarInvSumL2 n c θ | (n) (c) (θ)
      (hθ : ∀ ν, θ ν ∈ Set.Ioc 0 1) (h : ∑ ν, c ν * θ ν = 0) }
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [28 Measure and integration](../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/Paper/RiemannHypothesisEquivalents.lean, line 136](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannHypothesisEquivalents.lean#L136).

## `RiemannHypothesis.beurling_nyman_criterion_rhs`

Open: stated without proof.

> The statement that the Beurling-Nyman criterion holds.

```lean
theorem beurling_nyman_criterion_rhs :
    Dense { fractScalarInvSumL2 n c θ | (n) (c) (θ)
      (hθ : ∀ ν, θ ν ∈ Set.Ioc 0 1) (h : ∑ ν, c ν * θ ν = 0) }
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [28 Measure and integration](../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/Paper/RiemannHypothesisEquivalents.lean, line 143](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannHypothesisEquivalents.lean#L143).

## `RiemannHypothesis.weil_positivity_criterion`

Solved: stated here without proof.

> **Weil's Positivity Criterion**. The Riemann Hypothesis is equivalent to the non-positivity of
> Weil factor sums on the convolution of test functions. In [Co26] this is expressed as
> $$
>   \sum_v W_v(g\star g^*) \leq 0
> $$
> for all compactly-supported smooth functions $g : \mathbb{R}_+^{\times} \to \mathbb{C}$ such that
> the Mellin transform of $g$ vanishes at $\pm i / 2$, where $g^*(x) := \bar{g}(x^{-1})$ and $W_v$
> are the multiplicative Weil factors defined in [Co26]. We formalise this as the corresponding
> additive statement (via $x = e^u$), since convolution in mathlib is additive, and restrict to
> real-valued test functions $g$, which suffices for the equivalence.

```lean
theorem weil_positivity_criterion :
    RiemannHypothesis ↔ ∀ g : C_c(ℝ, ℝ), ContDiff ℝ ∞ g → IsTestFunction g →
      weilArchimedean (g ⋆ fun x ↦ g (-x)) +
        ∑' p : Nat.Primes, weilNonArchimedean p (g ⋆ fun x ↦ g (-x)) ≤ 0
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md). Declared in [FormalConjectures/Paper/RiemannHypothesisEquivalents.lean, line 173](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannHypothesisEquivalents.lean#L173).

## `RiemannHypothesis.weil_positivity_criterion_rhs`

Open: stated without proof.

> The statement that the Weil criterion holds.

```lean
theorem weil_positivity_criterion_rhs {g : C_c(ℝ, ℝ)} (hg : ContDiff ℝ ∞ g)
    (h : IsTestFunction g) :
    weilArchimedean (g ⋆ fun x ↦ g (-x)) +
      ∑' p : Nat.Primes, weilNonArchimedean p (g ⋆ fun x ↦ g (-x)) ≤ 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md). Declared in [FormalConjectures/Paper/RiemannHypothesisEquivalents.lean, line 181](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannHypothesisEquivalents.lean#L181).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/RiemannHypothesisEquivalents.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannHypothesisEquivalents.lean)
- [The Riemann Hypothesis: Past, Present and a Letter Through
  Time](https://arxiv.org/abs/2602.04022)
