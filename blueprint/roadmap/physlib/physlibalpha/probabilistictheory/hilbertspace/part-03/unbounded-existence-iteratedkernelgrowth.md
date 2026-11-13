---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.hermite_aeval_le_poly_growth, ProbabilisticTheory.QuantumMechanics.gaussianKernel_iteratedDeriv_shift_bound, ProbabilisticTheory.QuantumMechanics.integrable_abs_pow_mul_exp_neg_mul_sq, ProbabilisticTheory.QuantumMechanics.integrable_one_add_abs_pow_mul_exp_neg_mul_sq, ProbabilisticTheory.QuantumMechanics.gaussianKernel_contDiff, ProbabilisticTheory.QuantumMechanics.gaussianKernel_iteratedDeriv_continuous, ProbabilisticTheory.QuantumMechanics.gaussianKernel_iteratedDeriv_hasDerivAt, ProbabilisticTheory.QuantumMechanics.gaussianKernel_iteratedDeriv_smul_integrable
statement: formalized
proof: formalized
---

# Pointwise bounds on the derivatives of the heat kernel

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.Existence.IteratedKernelGrowth`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/IteratedKernelGrowth.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/IteratedKernelGrowth.lean): 9 declarations, 9 with a docstring.

> Pointwise domination of the shifted derivatives of the heat kernel.

## i. Overview

> Every derivative of the heat kernel, shifted by at most `1`, is dominated by an integrable function
> `C (1 + |u|)ⁿ exp(-c u²)`. So the Gårding vectors of all derivatives of the heat kernel have
> differentiable orbits.

## ii. Key results

> - `hermite_aeval_le_poly_growth` : `|Hₙ(y)| ≤ Cₙ (1 + |y|)ⁿ`.
> - `gaussianKernel_iteratedDeriv_shift_bound` : the local domination bound.
> - `gardingVectorAt_iteratedKernel_hasDerivAt` : the orbit of the Gårding vector of the `n`-th
>   derivative of the heat kernel is differentiable at `0`.

## iv. References

> * None.

## A. Polynomial growth of the Hermite polynomials

**`ProbabilisticTheory.QuantumMechanics.hermite_aeval_le_poly_growth`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/IteratedKernelGrowth.lean#L61).

> `|Hₙ(y)| ≤ Cₙ (1 + |y|)ⁿ`, with `Cₙ` the sum of the absolute values of the coefficients of `Hₙ`.

```lean
lemma hermite_aeval_le_poly_growth (n : ℕ) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ y : ℝ, |aeval y (hermite n)| ≤ C * (1 + |y|) ^ n
```

## B. Local domination of the kernel derivatives

**`ProbabilisticTheory.QuantumMechanics.gaussianKernel_iteratedDeriv_shift_bound`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/IteratedKernelGrowth.lean#L95).

> For `x² ≤ 1`, the `(n + 1)`-th derivative of the heat kernel at `u - x` is dominated by `C (1 +
> |u|)ⁿ⁺¹ exp(-c u²)`, uniformly in `x`.

```lean
lemma gaussianKernel_iteratedDeriv_shift_bound (n : ℕ) {ε : ℝ} (hε : 0 < ε) :
    ∃ D : ℝ, 0 ≤ D ∧ ∀ {x : ℝ}, x ^ 2 ≤ 1 → ∀ u : ℝ,
      |iteratedDeriv (n + 1) (gaussianKernel ε) (u - x)| ≤
        D * ((1 + |u|) ^ (n + 1) * Real.exp (-(u ^ 2) / (2 * ε)))
```

## C. Integrability of the dominating functions

**`ProbabilisticTheory.QuantumMechanics.integrable_abs_pow_mul_exp_neg_mul_sq`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/IteratedKernelGrowth.lean#L164).

> `|u|^n` times a Gaussian weight is integrable — the `abs`-of-argument variant of
> `integrable_pow_mul_exp_neg_mul_sq`, obtained via `Integrable.abs` since `|u^n * exp(-cu²)| =
> |u|^n * exp(-cu²)`.

```lean
lemma integrable_abs_pow_mul_exp_neg_mul_sq (n : ℕ) {c : ℝ} (hc : 0 < c) :
    Integrable (fun u : ℝ => |u| ^ n * Real.exp (-(c * u ^ 2)))
```

**`ProbabilisticTheory.QuantumMechanics.integrable_one_add_abs_pow_mul_exp_neg_mul_sq`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/IteratedKernelGrowth.lean#L174).

> `(1 + |u|)ⁿ exp(-c u²)` is integrable.

```lean
lemma integrable_one_add_abs_pow_mul_exp_neg_mul_sq (n : ℕ) {c : ℝ} (hc : 0 < c) :
    Integrable (fun u : ℝ => (1 + |u|) ^ n * Real.exp (-(c * u ^ 2)))
```

## D. Smoothness of the heat kernel

**`ProbabilisticTheory.QuantumMechanics.gaussianKernel_contDiff`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/IteratedKernelGrowth.lean#L205).

> `gaussianKernel ε` is smooth to every order (used to get `Continuous`/`Differentiable` facts
> about its iterated derivatives via the generic `ContDiff.continuous_iteratedDeriv`/
> `ContDiff.differentiable_iteratedDeriv`).

```lean
lemma gaussianKernel_contDiff {ε : ℝ} (_hε : 0 < ε) : ContDiff ℝ (⊤ : ℕ∞) (gaussianKernel ε)
```

**`ProbabilisticTheory.QuantumMechanics.gaussianKernel_iteratedDeriv_continuous`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/IteratedKernelGrowth.lean#L210).

> `iteratedDeriv n (gaussianKernel ε)` is continuous, for every `n`.

```lean
lemma gaussianKernel_iteratedDeriv_continuous (n : ℕ) {ε : ℝ} (hε : 0 < ε) :
    Continuous (iteratedDeriv n (gaussianKernel ε))
```

**`ProbabilisticTheory.QuantumMechanics.gaussianKernel_iteratedDeriv_hasDerivAt`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/IteratedKernelGrowth.lean#L216).

> The `n`-th derivative of the heat kernel has derivative the `(n + 1)`-th.

```lean
lemma gaussianKernel_iteratedDeriv_hasDerivAt (n : ℕ) {ε : ℝ} (hε : 0 < ε) (t : ℝ) :
    HasDerivAt (iteratedDeriv n (gaussianKernel ε))
      (iteratedDeriv (n + 1) (gaussianKernel ε) t) t
```

## E. Differentiable orbits of iterated-kernel Gårding vectors

**`ProbabilisticTheory.QuantumMechanics.gaussianKernel_iteratedDeriv_smul_integrable`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/IteratedKernelGrowth.lean#L236).

> The `n`-th derivative of the heat kernel is integrable against `t ↦ U t ψ`.

```lean
lemma gaussianKernel_iteratedDeriv_smul_integrable {H : Type*} [NormedAddCommGroup H]
    [InnerProductSpace ℂ H] [CompleteSpace H] {U : ℝ → H →L[ℂ] H}
    (hUunit : ∀ t, U t ∈ unitary (H →L[ℂ] H)) (hUcont : ∀ ξ : H, Continuous (fun t : ℝ => U t ξ))
    (n : ℕ) {ε : ℝ} (hε : 0 < ε) (ψ : H) :
    Integrable (fun t : ℝ => ((iteratedDeriv n (gaussianKernel ε) t : ℝ) : ℂ) • U t ψ)
```

**`ProbabilisticTheory.QuantumMechanics.gardingVectorAt_iteratedKernel_hasDerivAt`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/IteratedKernelGrowth.lean#L258).

> The orbit of the Gårding vector of the `n`-th derivative of the heat kernel is differentiable at
> `0`.

```lean
lemma gardingVectorAt_iteratedKernel_hasDerivAt {H : Type*} [NormedAddCommGroup H]
    [InnerProductSpace ℂ H] [CompleteSpace H] {U : ℝ → H →L[ℂ] H}
    (hUmul : ∀ s t, U (s + t) = U s * U t) (hUunit : ∀ t, U t ∈ unitary (H →L[ℂ] H))
    (hUcont : ∀ ξ : H, Continuous (fun t : ℝ => U t ξ)) (n : ℕ) {ε : ℝ} (hε : 0 < ε) (ψ : H) :
    HasDerivAt (fun s : ℝ => U s (gardingVectorAt U (iteratedDeriv n (gaussianKernel ε)) ψ))
      (∫ u : ℝ, ((-(iteratedDeriv (n + 1) (gaussianKernel ε) u) : ℝ) : ℂ) • U u ψ) 0
```

## Depends on

- [Gårding vectors](unbounded-existence-gardingvectors.md)
- [Gårding vectors of smooth kernels](unbounded-existence-genericgardingkernel.md)

## Proof depends on

- [Growth of the derivatives of the heat kernel](unbounded-existence-gaussiankernelgrowth.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/IteratedKernelGrowth.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/IteratedKernelGrowth.lean)
