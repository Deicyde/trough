---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.integralCLM, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bound_of_continuous, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.integralCLM_eq_of_forall_eq, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.integralCLM_add, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.integralCLM_mul, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.integralCLM_const, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.integralCLM_star, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.continuousCalculus
statement: formalized
proof: formalized
---

# The continuous functional calculus of a spectral measure

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.ContinuousCalculus`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ContinuousCalculus.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ContinuousCalculus.lean): 8 declarations, 3 with a docstring.

> Integrating continuous functions on a compact space against a spectral measure is a unital
> ⋆-homomorphism into the bounded operators.

## i. Overview

> For a weak spectral measure `P` on a compact Borel space `X`, the integral `f ↦ ∫ f dP` of a
> continuous function is a unital ⋆-homomorphism `C(X, ℂ) → B(H)`. This repackages the algebra of the
> bounded integral so that it can be composed with other ⋆-homomorphisms, and so that the spectrum
> of an integral can be controlled by the spectrum of the integrand.

## ii. Key results

> - `WOTSpectralMeasure.continuousCalculus` : the ⋆-homomorphism `f ↦ ∫ f dP`.

## iv. References

> * None.

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.integralCLM`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ContinuousCalculus.lean#L59).

> The bounded integral of a continuous function, as a bounded operator.

```lean
def integralCLM (f : C(X, ℂ)) : H →L[ℂ] H
```

## A. The ⋆-homomorphism

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.bound_of_continuous`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ContinuousCalculus.lean#L66).

```lean
lemma bound_of_continuous (f : C(X, ℂ)) : ∃ C, ∀ z, ‖f z‖ ≤ C
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.integralCLM_eq_of_forall_eq`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ContinuousCalculus.lean#L70).

> The integral of a measurable bounded function that agrees with a continuous function.

```lean
lemma integralCLM_eq_of_forall_eq (f : C(X, ℂ)) {F : X → ℂ} (hF : Measurable F)
    (hbF : ∃ C, ∀ z, ‖F z‖ ≤ C) (h : ∀ z, f z = F z) :
    P.integralCLM f = ContinuousLinearMapWOT.toCLM (P.boundedIntegral F hF hbF)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.integralCLM_add`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ContinuousCalculus.lean#L76).

```lean
lemma integralCLM_add (f g : C(X, ℂ)) :
    P.integralCLM (f + g) = P.integralCLM f + P.integralCLM g
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.integralCLM_mul`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ContinuousCalculus.lean#L86).

```lean
lemma integralCLM_mul (f g : C(X, ℂ)) :
    P.integralCLM (f * g) = P.integralCLM f * P.integralCLM g
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.integralCLM_const`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ContinuousCalculus.lean#L100).

```lean
lemma integralCLM_const (c : ℂ) : P.integralCLM (ContinuousMap.const X c) = c • 1
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.integralCLM_star`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ContinuousCalculus.lean#L107).

```lean
lemma integralCLM_star (f : C(X, ℂ)) : P.integralCLM (star f) = star (P.integralCLM f)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.continuousCalculus`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ContinuousCalculus.lean#L117).

> **The continuous functional calculus of a spectral measure**: `f ↦ ∫ f dP` is a unital
> ⋆-homomorphism from the continuous functions to the bounded operators.

```lean
def continuousCalculus : C(X, ℂ) →⋆ₐ[ℂ] (H →L[ℂ] H)
```

## Depends on

- [Integrating bounded functions against a spectral measure](unbounded-boundedintegral.md)

## Proof depends on

- [The bounded functional calculus of a spectral measure](unbounded-boundedintegralalgebra.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ContinuousCalculus.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ContinuousCalculus.lean)
