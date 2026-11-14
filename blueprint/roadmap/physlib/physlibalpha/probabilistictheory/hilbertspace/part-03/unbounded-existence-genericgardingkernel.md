---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.gardingVectorAt, ProbabilisticTheory.QuantumMechanics.gardingVectorAt_translate, ProbabilisticTheory.QuantumMechanics.gardingVectorAt_hasDerivAt
statement: formalized
proof: formalized
---

# Gårding vectors of smooth kernels

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.Existence.GenericGardingKernel`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GenericGardingKernel.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GenericGardingKernel.lean): 3 declarations, 3 with a docstring.

> Gårding vectors of a general kernel and the differentiability of their orbits.

## i. Overview

> For a kernel `k` on `ℝ`, the Gårding vector of `ψ` is `∫ k(t) U t ψ dt`. Translating it by `U s`
> translates the kernel. If `k` is differentiable with a locally dominated derivative, the orbit of
> the Gårding vector is differentiable at `0`, with derivative the Gårding vector of `-k'`.

## ii. Key results

> - `gardingVectorAt` : the Gårding vector of `ψ` for a kernel `k`.
> - `gardingVectorAt_translate` : translating a Gårding vector translates the kernel.
> - `gardingVectorAt_hasDerivAt` : the orbit of a Gårding vector is differentiable at `0`.

## iv. References

> * None.

## A. Gårding vectors and translation

**`ProbabilisticTheory.QuantumMechanics.gardingVectorAt`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GenericGardingKernel.lean#L67).

> The Gårding vector of `ψ` against a generic (real-valued) kernel `k`, generalizing
> `analyticGardingVector U ε ψ = gardingVectorAt U (gaussianKernel ε) ψ`.

```lean
def gardingVectorAt (k : ℝ → ℝ) (ψ : H) : H
```

**`ProbabilisticTheory.QuantumMechanics.gardingVectorAt_translate`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GenericGardingKernel.lean#L71).

> Translating a Gårding vector by `U s` translates the kernel by `s`.

```lean
lemma gardingVectorAt_translate (k : ℝ → ℝ) (ψ : H)
    (hk_integrable : Integrable (fun t : ℝ => (k t : ℂ) • U t ψ)) (s : ℝ) :
    U s (gardingVectorAt U k ψ) = ∫ u : ℝ, (k (u - s) : ℂ) • U u ψ
```

## B. Differentiability of the orbit

**`ProbabilisticTheory.QuantumMechanics.gardingVectorAt_hasDerivAt`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GenericGardingKernel.lean#L94).

> If `k` is differentiable with a locally dominated continuous derivative `k'`, the orbit of the
> Gårding vector of `k` is differentiable at `0`, with derivative the Gårding vector of `-k'`.

```lean
lemma gardingVectorAt_hasDerivAt (hUunit : ∀ t, U t ∈ unitary (H →L[ℂ] H))
    (hUcont : ∀ ξ : H, Continuous (fun t : ℝ => U t ξ)) (k k' : ℝ → ℝ)
    (hk_cont : Continuous k) (hk'_cont : Continuous k') (hk_deriv : ∀ t, HasDerivAt k (k' t) t)
    (ψ : H) (hk_integrable : Integrable (fun t : ℝ => (k t : ℂ) • U t ψ))
    (bound : ℝ → ℝ) (hbound_int : Integrable bound)
    (hbound : ∀ u : ℝ, ∀ x ∈ Metric.ball (0 : ℝ) 1, |k' (u - x)| * ‖ψ‖ ≤ bound u) :
    HasDerivAt (fun s : ℝ => U s (gardingVectorAt U k ψ))
      (∫ u : ℝ, ((-(k' u) : ℝ) : ℂ) • U u ψ) 0
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GenericGardingKernel.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GenericGardingKernel.lean)
