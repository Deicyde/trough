---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.reCompact, ProbabilisticTheory.QuantumMechanics.imCompact, ProbabilisticTheory.QuantumMechanics.realToComplex_reCompact_add_I_smul, ProbabilisticTheory.QuantumMechanics.starHomSpectralMeasure_diagonalMeasure, ProbabilisticTheory.QuantumMechanics.integral_starHomScalarMeasure_real, ProbabilisticTheory.QuantumMechanics.integral_starHomScalarMeasure, ProbabilisticTheory.QuantumMechanics.boundedIntegral_bound_of_continuous, ProbabilisticTheory.QuantumMechanics.starHomSpectralMeasure_boundedIntegral_real
statement: formalized
proof: formalized
---

# The functional calculus of a representation of continuous functions

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.StarHomSpec.Functional`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Functional.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Functional.lean): 10 declarations, 8 with a docstring.

> The bounded integral against the spectral measure of a ⋆-homomorphism `Φ` is `Φ`.

## i. Overview

> The spectral measure of a unital ⋆-homomorphism `Φ : C(X, ℂ) → B(H)` reconstructs `Φ` on real
> continuous functions. Since the bounded integral against a spectral measure is linear, it
> reconstructs `Φ` on all complex continuous functions: `∫ f dE = Φ f`.

## ii. Key results

> - `starHomSpectralMeasure_boundedIntegral_real` : the integral of a real continuous function.
> - `starHomSpectralMeasure_boundedIntegral` : the integral of a complex continuous function is
>   `Φ f`.

## iv. References

> * None.

## A. Real and imaginary parts

**`ProbabilisticTheory.QuantumMechanics.reCompact`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Functional.lean#L62).

> The real part of a continuous complex function on a compact space, as a compactly supported
> continuous real function.

```lean
def reCompact (f : C(X, ℂ)) : CompactlySupportedContinuousMap X ℝ
```

**`ProbabilisticTheory.QuantumMechanics.imCompact`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Functional.lean#L67).

> The imaginary part of a continuous complex function on a compact space, as a compactly
> supported continuous real function.

```lean
def imCompact (f : C(X, ℂ)) : CompactlySupportedContinuousMap X ℝ
```

**`ProbabilisticTheory.QuantumMechanics.realToComplex_reCompact_add_I_smul`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Functional.lean#L71).

```lean
lemma realToComplex_reCompact_add_I_smul (f : C(X, ℂ)) :
    realToComplex (reCompact f) + Complex.I • realToComplex (imCompact f) = f
```

## B. The diagonal measure

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralMeasure_diagonalMeasure`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Functional.lean#L84).

> The diagonal measure `S ↦ ‖E(S) x‖²` of the spectral measure of `Φ` is the Riesz measure of
> the vector state of `x`.

```lean
lemma starHomSpectralMeasure_diagonalMeasure (x : H) :
    (starHomSpectralMeasure Φ).diagonalMeasure x = starHomScalarMeasure Φ x
```

**`ProbabilisticTheory.QuantumMechanics.integral_starHomScalarMeasure_real`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Functional.lean#L95).

> The integral of a real continuous function against the Riesz measure of the vector state of
> `x` is the expectation of its operator.

```lean
lemma integral_starHomScalarMeasure_real (u : CompactlySupportedContinuousMap X ℝ) (x : H) :
    ∫ z, (u z : ℂ) ∂starHomScalarMeasure Φ x = ⟪x, starHomRealOperator Φ u x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.integral_starHomScalarMeasure`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Functional.lean#L102).

> The vector state of `x` in the representation `Φ` is integration against its Riesz measure:
> `⟪x, Φ f x⟫ = ∫ f dμₓ` for every continuous `f`.

```lean
lemma integral_starHomScalarMeasure (f : C(X, ℂ)) (x : H) :
    ∫ z, f z ∂starHomScalarMeasure Φ x = ⟪x, Φ f x⟫_ℂ
```

## C. The integral of a continuous function

**`ProbabilisticTheory.QuantumMechanics.boundedIntegral_bound_of_continuous`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Functional.lean#L129).

```lean
lemma boundedIntegral_bound_of_continuous (f : C(X, ℂ)) : ∃ C, ∀ z, ‖f z‖ ≤ C
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralMeasure_boundedIntegral_real`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Functional.lean#L134).

> The bounded integral of a real continuous function against the spectral measure of `Φ` is
> `Φ` of that function.

```lean
lemma starHomSpectralMeasure_boundedIntegral_real (u : CompactlySupportedContinuousMap X ℝ) :
    ContinuousLinearMapWOT.toCLM
      (WOTSpectralMeasure.boundedIntegral (starHomSpectralMeasure Φ)
        (fun z => (u z : ℂ)) (by fun_prop) ⟨‖u.toContinuousMap‖, fun z => by
          simpa using u.toContinuousMap.norm_coe_le_norm z⟩) = starHomRealOperator Φ u
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralMeasure_boundedIntegral`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Functional.lean#L154).

> **The spectral measure of `Φ` reconstructs `Φ`**: the bounded integral of a continuous
> function `f` against `starHomSpectralMeasure Φ` is `Φ f`.

```lean
lemma starHomSpectralMeasure_boundedIntegral (f : C(X, ℂ)) :
    ContinuousLinearMapWOT.toCLM
      (WOTSpectralMeasure.boundedIntegral (starHomSpectralMeasure Φ) f f.continuous.measurable
        (boundedIntegral_bound_of_continuous f)) = Φ f
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralMeasure_boundedIntegral_map`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Functional.lean#L200).

> **Change of spectral variable**: integrating a bounded measurable function `g` against the
> pushforward of the spectral measure of `Φ` along a measurable map `f` is integrating `g ∘ f`
> against the spectral measure itself.

```lean
lemma starHomSpectralMeasure_boundedIntegral_map {β : Type*} [MeasurableSpace β] [Nonempty β]
    {f : X → β} (hf : Measurable f) {g : β → ℂ} (hg : Measurable g)
    (hbg : ∃ C, ∀ b, ‖g b‖ ≤ C) :
    WOTSpectralMeasure.boundedIntegral ((starHomSpectralMeasure Φ).map f hf) g hg hbg =
      WOTSpectralMeasure.boundedIntegral (starHomSpectralMeasure Φ) (g ∘ f) (hg.comp hf)
        (by obtain ⟨C, hC⟩ := hbg; exact ⟨C, fun z => hC (f z)⟩)
```

## Depends on

- [The spectral measure of a representation of continuous functions](unbounded-starhomspec-spectralmeasure.md)

## Proof depends on

- [Integrating unbounded functions against a spectral measure](../part-03/unbounded-spectralintegral-construction.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Functional.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Functional.lean)
