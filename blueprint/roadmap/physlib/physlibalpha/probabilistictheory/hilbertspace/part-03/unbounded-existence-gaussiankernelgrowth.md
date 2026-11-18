---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.hermite_derivative_succ, ProbabilisticTheory.QuantumMechanics.hermite_aeval_deriv_succ, ProbabilisticTheory.QuantumMechanics.hermite_aeval_succ, ProbabilisticTheory.QuantumMechanics.integrable_pow_mul_exp_neg_mul_sq, ProbabilisticTheory.QuantumMechanics.integrable_aeval_mul_gaussian, ProbabilisticTheory.QuantumMechanics.gaussian_hasDerivAt, ProbabilisticTheory.QuantumMechanics.hermite_gaussian_sq_integral_succ, ProbabilisticTheory.QuantumMechanics.hermite_gaussian_sq_integral
statement: formalized
proof: formalized
---

# Growth of the derivatives of the heat kernel

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.Existence.GaussianKernelGrowth`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GaussianKernelGrowth.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GaussianKernelGrowth.lean): 11 declarations, 11 with a docstring.

> Hermite polynomial bounds on the L¹ norms of the heat kernel's derivatives.

## i. Overview

> The `n`-th derivative of the heat kernel is a Hermite polynomial times a Gaussian. The probabilists'
> Hermite polynomials satisfy `∫ Hₙ(x)² exp(-x²/2) dx = √(2π) n!`, proved by one integration by parts
> per step using `Hₙ₊₁' = (n + 1) Hₙ`. Cauchy–Schwarz then bounds the `L¹` norm of the `n`-th
> derivative of the heat kernel by `C^(n + 1) √(n!)`.

## ii. Key results

> - `hermite_derivative_succ` : `Hₙ₊₁' = (n + 1) Hₙ`.
> - `hermite_gaussian_sq_integral` : `∫ Hₙ(x)² exp(-x²/2) dx = √(2π) n!`.
> - `gaussianKernel_iteratedDeriv_eq` : the derivatives of the heat kernel in terms of Hermite
>   polynomials.
> - `gaussianKernel_iteratedDeriv_L1_bound` : the `L¹` bound on the derivatives of the heat kernel.

## iv. References

> * None.

## A. The Hermite derivative identity

**`ProbabilisticTheory.QuantumMechanics.hermite_derivative_succ`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GaussianKernelGrowth.lean#L65).

> The polynomial identity `Hₙ₊₁' = (n+1) · Hₙ`, absent from Mathlib, proved directly from the
> defining recursion `hermite_succ : Hₙ₊₁ = X·Hₙ - Hₙ'` by induction.

```lean
lemma hermite_derivative_succ :
    ∀ n : ℕ, derivative (hermite (n + 1)) = C ((n : ℤ) + 1) * hermite n
```

**`ProbabilisticTheory.QuantumMechanics.hermite_aeval_deriv_succ`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GaussianKernelGrowth.lean#L88).

> The `aeval`/real-valued specialization of `hermite_derivative_succ`.

```lean
lemma hermite_aeval_deriv_succ (n : ℕ) (x : ℝ) :
    aeval x (derivative (hermite (n + 1))) = ((n : ℝ) + 1) * aeval x (hermite n)
```

**`ProbabilisticTheory.QuantumMechanics.hermite_aeval_succ`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GaussianKernelGrowth.lean#L94).

> The `aeval`/real-valued specialization of the defining recursion `hermite_succ`.

```lean
lemma hermite_aeval_succ (n : ℕ) (x : ℝ) :
    aeval x (hermite (n + 1)) = x * aeval x (hermite n) - aeval x (derivative (hermite n))
```

## B. Integrability against Gaussian weights

**`ProbabilisticTheory.QuantumMechanics.integrable_pow_mul_exp_neg_mul_sq`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GaussianKernelGrowth.lean#L107).

> A monomial times a Gaussian weight is integrable (the `n`-th-power case of
> `integrable_aeval_mul_gaussian`, via the real-exponent Gaussian-tail estimate specialized to a
> natural-number exponent through `Real.rpow_natCast`).

```lean
lemma integrable_pow_mul_exp_neg_mul_sq (n : ℕ) {c : ℝ} (hc : 0 < c) :
    Integrable (fun x : ℝ => x ^ n * Real.exp (-(c * x ^ 2)))
```

**`ProbabilisticTheory.QuantumMechanics.integrable_aeval_mul_gaussian`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GaussianKernelGrowth.lean#L118).

> Any (integer) polynomial times a Gaussian weight is integrable — the integrability fact needed
> throughout `hermite_gaussian_sq_integral_succ`'s integration-by-parts argument. Proved by
> `Polynomial.induction_on'`, reducing to the monomial case.

```lean
lemma integrable_aeval_mul_gaussian (q : Polynomial ℤ) {c : ℝ} (hc : 0 < c) :
    Integrable (fun x : ℝ => aeval x q * Real.exp (-(c * x ^ 2)))
```

**`ProbabilisticTheory.QuantumMechanics.gaussian_hasDerivAt`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GaussianKernelGrowth.lean#L132).

> The derivative of the standard Gaussian, packaged as `HasDerivAt` (Mathlib only records the
> `deriv`-value form privately, inside the proof of `deriv_gaussian_eq_hermite_mul_gaussian`).

```lean
lemma gaussian_hasDerivAt (x : ℝ) :
    HasDerivAt (fun y : ℝ => Real.exp (-(y ^ 2 / 2))) (-x * Real.exp (-(x ^ 2 / 2))) x
```

## C. The norm of the Hermite polynomials

**`ProbabilisticTheory.QuantumMechanics.hermite_gaussian_sq_integral_succ`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GaussianKernelGrowth.lean#L149).

> `Iₙ₊₁ = (n + 1) Iₙ` for `Iₙ = ∫ Hₙ(x)² exp(-x²/2) dx`, by integration by parts.

```lean
lemma hermite_gaussian_sq_integral_succ (n : ℕ) :
    (∫ x : ℝ, (aeval x (hermite (n + 1))) ^ 2 * Real.exp (-(x ^ 2 / 2))) =
      ((n : ℝ) + 1) * ∫ x : ℝ, (aeval x (hermite n)) ^ 2 * Real.exp (-(x ^ 2 / 2))
```

**`ProbabilisticTheory.QuantumMechanics.hermite_gaussian_sq_integral`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GaussianKernelGrowth.lean#L220).

> **The norm of the Hermite polynomials**: `∫ Hₙ(x)² exp(-x²/2) dx = √(2π) n!`.

```lean
lemma hermite_gaussian_sq_integral (n : ℕ) :
    ∫ x : ℝ, (aeval x (hermite n)) ^ 2 * Real.exp (-(x ^ 2 / 2)) =
      Real.sqrt (2 * Real.pi) * n.factorial
```

**`ProbabilisticTheory.QuantumMechanics.hermite_gaussian_L1_bound`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GaussianKernelGrowth.lean#L238).

> The weighted `L¹` bound `∫ |Hₙ(x)| exp(-x²/2) dx ≤ √(2π) √(n!)`.

```lean
lemma hermite_gaussian_L1_bound (n : ℕ) :
    ∫ x : ℝ, |aeval x (hermite n)| * Real.exp (-(x ^ 2 / 2)) ≤
      Real.sqrt (2 * Real.pi) * Real.sqrt n.factorial
```

## D. Derivatives of the heat kernel

**`ProbabilisticTheory.QuantumMechanics.gaussianKernel_iteratedDeriv_eq`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GaussianKernelGrowth.lean#L316).

> The `n`-th derivative of the heat kernel is a rescaled Hermite polynomial times the kernel.

```lean
lemma gaussianKernel_iteratedDeriv_eq {ε : ℝ} (hε : 0 < ε) (n : ℕ) (t : ℝ) :
    iteratedDeriv n (gaussianKernel ε) t =
      (Real.pi * ε) ^ (-(1 : ℝ) / 2) * (Real.sqrt (2 / ε) ^ n *
        ((-1 : ℝ) ^ n * aeval (Real.sqrt (2 / ε) * t) (hermite n) *
          Real.exp (-((Real.sqrt (2 / ε) * t) ^ 2 / 2))))
```

**`ProbabilisticTheory.QuantumMechanics.gaussianKernel_iteratedDeriv_L1_bound`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GaussianKernelGrowth.lean#L344).

> **The `L¹` norm of the `n`-th derivative of the heat kernel** is at most `C^(n + 1) √(n!)`.

```lean
lemma gaussianKernel_iteratedDeriv_L1_bound {ε : ℝ} (hε : 0 < ε) :
    ∃ C : ℝ, 0 < C ∧ ∀ n : ℕ,
      Integrable (iteratedDeriv n (gaussianKernel ε)) ∧
      ∫ t : ℝ, |iteratedDeriv n (gaussianKernel ε) t| ≤ C ^ (n + 1) * Real.sqrt n.factorial
```

## Depends on

- [Gårding vectors](unbounded-existence-gardingvectors.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GaussianKernelGrowth.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GaussianKernelGrowth.lean)
