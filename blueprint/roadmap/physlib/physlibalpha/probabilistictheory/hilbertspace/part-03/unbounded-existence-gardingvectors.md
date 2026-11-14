---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.gaussianKernel, ProbabilisticTheory.QuantumMechanics.gaussianKernel_pos, ProbabilisticTheory.QuantumMechanics.gaussianKernel_integral, ProbabilisticTheory.QuantumMechanics.gaussianKernel_smul_integrable, ProbabilisticTheory.QuantumMechanics.analyticGardingVector, ProbabilisticTheory.QuantumMechanics.standardGaussianKernel, ProbabilisticTheory.QuantumMechanics.standardGaussianKernel_pos, ProbabilisticTheory.QuantumMechanics.standardGaussianKernel_eq_gaussianKernel_one
statement: formalized
proof: formalized
---

# Gårding vectors

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.Existence.GardingVectors`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean): 22 declarations, 16 with a docstring.

> Gårding vectors: heat-kernel smoothings along a unitary group, dense in the domain.

## i. Overview

> Smoothing a vector `ψ` along the orbit of a unitary group against the heat kernel `gₑ(t) = (π
> ε)^(-1/2) exp(-t² / ε)` gives the Gårding vector `∫ gₑ(t) U t ψ dt`. As `ε → 0` the Gårding vectors
> converge to `ψ`. Each Gårding vector lies in the domain of the candidate generator, which acts on it
> by smoothing against the derivative of the kernel.

## ii. Key results

> - `gaussianKernel` : the heat kernel.
> - `analyticGardingVector` : the Gårding vector of `ψ`.
> - `analyticGardingVector_tendsto` : Gårding vectors converge to `ψ` as `ε → 0`.
> - `stoneCandidateGenerator_analyticGardingVector` : the generator acts on a Gårding vector by
>   smoothing against the derivative of the kernel.

## iv. References

> * None.

**`ProbabilisticTheory.QuantumMechanics.gaussianKernel`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L62).

> The heat kernel `(π ε)^(-1/2) exp(-t² / ε)`, a Gaussian of variance `ε / 2` with integral `1`.

```lean
def gaussianKernel (ε t : ℝ) : ℝ
```

**`ProbabilisticTheory.QuantumMechanics.gaussianKernel_pos`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L64).

```lean
lemma gaussianKernel_pos {ε : ℝ} (hε : 0 < ε) (t : ℝ) : 0 < gaussianKernel ε t
```

**`ProbabilisticTheory.QuantumMechanics.gaussianKernel_integral`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L69).

```lean
lemma gaussianKernel_integral {ε : ℝ} (hε : 0 < ε) :
    ∫ t : ℝ, gaussianKernel ε t = 1
```

**`ProbabilisticTheory.QuantumMechanics.gaussianKernel_smul_integrable`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L82).

> The heat kernel is integrable against any bounded continuous function, in particular against
> `t ↦ U t ψ` (bounded because `U t` is unitary, `‖U t ψ‖ = ‖ψ‖`).

```lean
lemma gaussianKernel_smul_integrable (hUunit : ∀ t, U t ∈ unitary (H →L[ℂ] H))
    (hUcont : ∀ ξ : H, Continuous (fun t : ℝ => U t ξ))
    {ε : ℝ} (hε : 0 < ε) (ψ : H) :
    Integrable (fun t : ℝ => (gaussianKernel ε t : ℂ) • U t ψ)
```

**`ProbabilisticTheory.QuantumMechanics.analyticGardingVector`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L106).

> The Gårding vector of `ψ` mollified against the heat kernel of width `ε`.

```lean
def analyticGardingVector (ε : ℝ) (ψ : H) : H
```

**`ProbabilisticTheory.QuantumMechanics.standardGaussianKernel`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L109).

> The heat kernel with `ε = 1`.

```lean
def standardGaussianKernel (x : ℝ) : ℝ
```

**`ProbabilisticTheory.QuantumMechanics.standardGaussianKernel_pos`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L111).

```lean
lemma standardGaussianKernel_pos (x : ℝ) : 0 < standardGaussianKernel x
```

**`ProbabilisticTheory.QuantumMechanics.standardGaussianKernel_eq_gaussianKernel_one`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L114).

```lean
lemma standardGaussianKernel_eq_gaussianKernel_one :
    standardGaussianKernel = gaussianKernel 1
```

**`ProbabilisticTheory.QuantumMechanics.standardGaussianKernel_integral`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L118).

```lean
lemma standardGaussianKernel_integral : ∫ x : ℝ, standardGaussianKernel x = 1
```

**`ProbabilisticTheory.QuantumMechanics.standardGaussianKernel_integrable`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L121).

```lean
lemma standardGaussianKernel_integrable : Integrable standardGaussianKernel
```

**`ProbabilisticTheory.QuantumMechanics.gaussianKernel_scale_eq_standardGaussianKernel`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L133).

> The rescaling identity at the level of the kernel itself: `√ε · gaussianKernel ε (√ε x) =
> standardGaussianKernel x`, i.e. the `ε`-dependence exactly cancels once the extra `√ε` from the
> change-of-variables Jacobian is absorbed.

```lean
lemma gaussianKernel_scale_eq_standardGaussianKernel {ε : ℝ} (hε : 0 < ε) (x : ℝ) :
    Real.sqrt ε * gaussianKernel ε (Real.sqrt ε * x) = standardGaussianKernel x
```

**`ProbabilisticTheory.QuantumMechanics.analyticGardingVector_eq_standardGaussian`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L147).

> The Gårding vector after the substitution `t = √ε x`.

```lean
lemma analyticGardingVector_eq_standardGaussian {ε : ℝ} (hε : 0 < ε) (ψ : H) :
    analyticGardingVector U ε ψ =
      ∫ x : ℝ, (standardGaussianKernel x : ℂ) • U (Real.sqrt ε * x) ψ
```

**`ProbabilisticTheory.QuantumMechanics.analyticGardingVector_tendsto`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L172).

> **Gårding vectors converge to `ψ` as `ε → 0`**, by dominated convergence after the substitution
> `t = √ε x`.

```lean
lemma analyticGardingVector_tendsto (hU0 : U 0 = 1)
    (hUcont : ∀ ξ : H, Continuous (fun t : ℝ => U t ξ)) (ψ : H) :
    Tendsto (fun ε : ℝ => analyticGardingVector U ε ψ) (𝓝[>] (0 : ℝ)) (𝓝 ψ)
```

## A. The generator on Gårding vectors

> Translating a Gårding vector by `U s` translates the kernel. Differentiating under the integral in
> `s` gives the action of the candidate generator.

**`ProbabilisticTheory.QuantumMechanics.analyticGardingVector_translate`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L227).

> Translating a Gårding vector by `U s` translates the kernel by `s`.

```lean
lemma analyticGardingVector_translate (hUunit : ∀ t, U t ∈ unitary (H →L[ℂ] H))
    (hUcont : ∀ ξ : H, Continuous (fun t : ℝ => U t ξ)) {ε : ℝ} (hε : 0 < ε) (ψ : H) (s : ℝ) :
    U s (analyticGardingVector U ε ψ) = ∫ u : ℝ, (gaussianKernel ε (u - s) : ℂ) • U u ψ
```

**`ProbabilisticTheory.QuantumMechanics.gaussianKernel_hasDerivAt`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L247).

> Explicit `HasDerivAt` for the heat kernel: `gaussianKernel ε` is differentiable everywhere,
> with derivative `gaussianKernel ε t * (-(2 * t) / ε)` (the usual `d/dt exp(-t²/ε) = (-2t/ε)
> exp(-t²/ε)` computation, scaled by the front normalization constant).

```lean
lemma gaussianKernel_hasDerivAt {ε : ℝ} (_hε : 0 < ε) (t : ℝ) :
    HasDerivAt (gaussianKernel ε) (gaussianKernel ε t * (-(2 * t) / ε)) t
```

**`ProbabilisticTheory.QuantumMechanics.gaussianKernel_deriv`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L260).

> Corollary of `gaussianKernel_hasDerivAt` as a `deriv` equation.

```lean
lemma gaussianKernel_deriv {ε : ℝ} (hε : 0 < ε) (t : ℝ) :
    deriv (gaussianKernel ε) t = gaussianKernel ε t * (-(2 * t) / ε)
```

**`ProbabilisticTheory.QuantumMechanics.gaussianKernel_deriv_continuous`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L265).

> `deriv (gaussianKernel ε)` is continuous.

```lean
lemma gaussianKernel_deriv_continuous {ε : ℝ} (hε : 0 < ε) :
    Continuous (deriv (gaussianKernel ε))
```

**`ProbabilisticTheory.QuantumMechanics.gaussianKernel_deriv_shift_bound`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L274).

> The shifted derivative of the heat kernel is dominated by `C (|u| + 1) exp(-u² / (2 ε))`.

```lean
lemma gaussianKernel_deriv_shift_bound {ε : ℝ} (hε : 0 < ε) {x : ℝ} (hx : x ^ 2 ≤ 1)
    (u : ℝ) :
    |deriv (gaussianKernel ε) (u - x)| ≤
      (2 * (Real.pi * ε) ^ (-(1 : ℝ) / 2) * Real.exp (1 / ε) / ε) *
        ((|u| + 1) * Real.exp (-(u ^ 2) / (2 * ε)))
```

**`ProbabilisticTheory.QuantumMechanics.gaussianKernel_deriv_bound_integrable`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L313).

> The `L¹` domination bound is itself integrable in `u`: it is `const * ((|u|+1) *
> Gaussian(u))`, and `|u| * Gaussian(u)` and `Gaussian(u)` are each classically integrable
> (`integrable_mul_exp_neg_mul_sq`, `integrable_exp_neg_mul_sq`).

```lean
lemma gaussianKernel_deriv_bound_integrable {ε : ℝ} (hε : 0 < ε) (c : ℝ) :
    Integrable (fun u : ℝ => c * ((|u| + 1) * Real.exp (-(u ^ 2) / (2 * ε))))
```

**`ProbabilisticTheory.QuantumMechanics.analyticGardingVector_hasDerivAt`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L335).

> The orbit of a Gårding vector is differentiable at `0`, with derivative the Gårding vector of
> `-g'`.

```lean
lemma analyticGardingVector_hasDerivAt
    (hUunit : ∀ t, U t ∈ unitary (H →L[ℂ] H))
    (hUcont : ∀ ξ : H, Continuous (fun t : ℝ => U t ξ)) {ε : ℝ} (hε : 0 < ε) (ψ : H) :
    HasDerivAt (fun s : ℝ => U s (analyticGardingVector U ε ψ))
      (∫ u : ℝ, ((-(deriv (gaussianKernel ε) u) : ℝ) : ℂ) • U u ψ) 0
```

**`ProbabilisticTheory.QuantumMechanics.analyticGardingVector_mem_stoneCandidateDomain`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L363).

> Gårding vectors lie in the domain of the candidate generator.

```lean
lemma analyticGardingVector_mem_stoneCandidateDomain (hUunit : ∀ t, U t ∈ unitary (H →L[ℂ] H))
    (hUcont : ∀ ξ : H, Continuous (fun t : ℝ => U t ξ)) {ε : ℝ} (hε : 0 < ε) (ψ : H) :
    analyticGardingVector U ε ψ ∈ (stoneCandidateGenerator (U := U) hUmul).domain
```

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_analyticGardingVector`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean#L370).

> The candidate generator acts on a Gårding vector by smoothing against the derivative of the
> kernel.

```lean
lemma stoneCandidateGenerator_analyticGardingVector (hUunit : ∀ t, U t ∈ unitary (H →L[ℂ] H))
    (hUcont : ∀ ξ : H, Continuous (fun t : ℝ => U t ξ)) {ε : ℝ} (hε : 0 < ε) (ψ : H) :
    stoneCandidateGenerator (U := U) hUmul
        ⟨analyticGardingVector U ε ψ, analyticGardingVector_mem_stoneCandidateDomain hUmul
          hUunit hUcont hε ψ⟩ =
      (Complex.I : ℂ) • ∫ u : ℝ, ((deriv (gaussianKernel ε) u : ℝ) : ℂ) • U u ψ
```

## Depends on

- [The candidate generator of a unitary group](unbounded-existence-candidategenerator.md)

## Proof depends on

- [Gårding vectors of smooth kernels](unbounded-existence-genericgardingkernel.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectors.lean)
