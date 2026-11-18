---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.spectrumRealPart, ProbabilisticTheory.QuantumMechanics.spectrumImagPart, ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_integral_spectrum_coe, ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_integral_spectrum_coe, ProbabilisticTheory.QuantumMechanics.cayleyBoundedOperator, ProbabilisticTheory.QuantumMechanics.cayleyBoundedOperator_apply, ProbabilisticTheory.QuantumMechanics.cayleyBoundedOperator_isStarNormal, ProbabilisticTheory.QuantumMechanics.cayleyBoundedOperator_mem_unitary
statement: formalized
proof: formalized
---

# The spectral measure of the Cayley transform

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.CayleySpectralData.Basic`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean): 31 declarations, 9 with a docstring.

> The spectral measure of the Cayley transform, pulled back to a spectral measure on ℝ.

## i. Overview

> The Cayley transform `U` of a self-adjoint operator `T` is a unitary. The continuous functional
> calculus gives it a spectral measure on the unit circle. Since `1` is not an eigenvalue of `U`, this
> measure gives no mass to `1`, so it pulls back along the inverse Cayley transform to a spectral
> measure on `ℝ`, the candidate spectral measure of `T`.

## ii. Key results

> - `cayleyBoundedOperator` : the Cayley transform of `T`, as a bounded operator.
> - `cayleyBoundedSpectralMeasure` : its spectral measure on `ℂ`.
> - `cayleyBoundedSpectralMeasure_singleton_one` : the spectral measure gives no mass to `1`.
> - `cayleyRealSpectralMeasure` : the pulled-back spectral measure on `ℝ`.

## iv. References

> * None.

**`ProbabilisticTheory.QuantumMechanics.spectrumRealPart`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L59).

> The real part of a spectral point of `U`, as a compactly supported continuous function on
> `spectrum ℂ U`.

```lean
def spectrumRealPart (U : H →L[ℂ] H) :
    CompactlySupportedContinuousMap (spectrum ℂ U) ℝ
```

**`ProbabilisticTheory.QuantumMechanics.spectrumImagPart`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L67).

> The imaginary part of a spectral point of `U`, as a compactly supported continuous function
> on `spectrum ℂ U`.

```lean
def spectrumImagPart (U : H →L[ℂ] H) :
    CompactlySupportedContinuousMap (spectrum ℂ U) ℝ
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_integral_spectrum_coe`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L73).

```lean
lemma cfcScalarMeasure_integral_spectrum_coe
    (U : H →L[ℂ] H) (hU : IsStarNormal U) (v : H) :
    ∫ z, (z.1 : ℂ) ∂cfcScalarMeasure U hU v =
      ((∫ z, spectrumRealPart U z ∂cfcScalarMeasure U hU v : ℝ) : ℂ) +
        Complex.I * ∫ z, spectrumImagPart U z ∂cfcScalarMeasure U hU v
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_integral_spectrum_coe`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L98).

```lean
lemma polarizedCfcScalarMeasure_integral_spectrum_coe
    (U : H →L[ℂ] H) (hU : IsStarNormal U) (x y : H) :
    ∫ᵛ z, (z.1 : ℂ) ∂[ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ);
      polarizedCfcScalarMeasure (hU := hU) U x y] =
      ⟪y, U x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.cayleyBoundedOperator`**, a def, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L185).

> The Cayley unitary of `T`, as a bounded continuous linear map.

```lean
def cayleyBoundedOperator (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) : H →L[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.cayleyBoundedOperator_apply`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L188).

```lean
lemma cayleyBoundedOperator_apply (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) (x : H) :
    cayleyBoundedOperator T hT x = cayleyContinuousLinearMap T hT x
```

**`ProbabilisticTheory.QuantumMechanics.cayleyBoundedOperator_isStarNormal`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L192).

```lean
lemma cayleyBoundedOperator_isStarNormal (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) :
    IsStarNormal (cayleyBoundedOperator T hT)
```

**`ProbabilisticTheory.QuantumMechanics.cayleyBoundedOperator_mem_unitary`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L204).

```lean
lemma cayleyBoundedOperator_mem_unitary (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) :
    cayleyBoundedOperator T hT ∈ unitary (H →L[ℂ] H)
```

**`ProbabilisticTheory.QuantumMechanics.cayleyBoundedSpectralMeasure`**, a def, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L226).

> The pushforward of the Cayley unitary's continuous functional calculus spectral measure
> along `spectrum ℂ U ↪ ℂ`.

```lean
noncomputable def cayleyBoundedSpectralMeasure (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) :
    QuantumMechanics.WOTSpectralMeasure ℂ H
```

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralMeasure_reconstruction_coe`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L232).

```lean
lemma cfcSpectralMeasure_reconstruction_coe
    (U : H →L[ℂ] H) (hU : IsStarNormal U) (x y : H) :
    (cfcSpectralMeasure U hU).complexWeakIntegral
        (fun z : spectrum ℂ U => (z.1 : ℂ)) x y = ⟪y, U x⟫_ℂ
```

## A. Spectral data from the functional calculus

> The Riesz--Markov construction is carried out on the compact spectrum.  The public spectral
> certificate should expose a measure on the ambient scalar field, since that is what the later
> functional-calculus and Cayley APIs consume.  This wrapper performs exactly that harmless subtype
> pushforward and does not impose any unitary or Cayley support hypothesis.

**`ProbabilisticTheory.QuantumMechanics.cfcSpectralMeasure_ambient_reconstruction`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L248).

```lean
lemma cfcSpectralMeasure_ambient_reconstruction
    (U : H →L[ℂ] H) (hU : IsStarNormal U) (x y : H) :
    ((cfcSpectralMeasure U hU).map
      (fun z : spectrum ℂ U => (z : ℂ)) measurable_subtype_coe).complexWeakIntegral
        id x y = ⟪y, U x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.cfcBoundedNormalSpectralData`**, a def, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L263).

> The generic bounded normal spectral certificate for `U`, from its continuous functional
> calculus.

```lean
noncomputable def cfcBoundedNormalSpectralData
    (U : H →L[ℂ] H) (hU : IsStarNormal U) :
    QuantumMechanics.WOTSpectralMeasure.BoundedNormalSpectralData U
```

> A unitary with no spectral mass at `1` is now the exact input expected by the Cayley inverse.
> The only extra work is the support calculation: the normal PVM is pushed forward from the compact
> spectrum, and the spectrum of a unitary lies on the unit circle.

**`ProbabilisticTheory.QuantumMechanics.cfcBoundedUnitarySpectralData`**, a def, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L275).

> The bounded unitary spectral certificate for a unitary with no spectral mass at `1`.

```lean
noncomputable def cfcBoundedUnitarySpectralData
    (u : H ≃ₗᵢ[ℂ] H)
    (h1 : (1 : ℂ) ∉ spectrum ℂ (u : H →L[ℂ] H)) :
    QuantumMechanics.WOTSpectralMeasure.BoundedUnitarySpectralData u
```

**`ProbabilisticTheory.QuantumMechanics.cayleyBoundedSpectralMeasure_reconstruction`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L330).

```lean
lemma cayleyBoundedSpectralMeasure_reconstruction
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) (x y : H) :
    (cayleyBoundedSpectralMeasure T hT).complexWeakIntegral id x y =
      ⟪y, cayleyBoundedOperator T hT x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.cayleyBoundedSpectralMeasure_scalarMeasure_isFinite`**, a lemma, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L347).

```lean
lemma cayleyBoundedSpectralMeasure_scalarMeasure_isFinite
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) (x y : H) :
    IsFiniteMeasure
      ((cayleyBoundedSpectralMeasure T hT).scalarMeasure x y).variation
```

**`ProbabilisticTheory.QuantumMechanics.atom_eigenvector_of_reconstruction`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L365).

```lean
lemma atom_eigenvector_of_reconstruction
    (E : QuantumMechanics.WOTSpectralMeasure ℂ H) (V : H →L[ℂ] H)
    (hrec : ∀ x y : H, E.complexWeakIntegral id x y = ⟪y, V x⟫_ℂ)
    {a : ℂ} (ha : MeasurableSet {a}) (x : H)
    (hfinite : ∀ y : H, IsFiniteMeasure (E.scalarMeasure x y).variation) :
    V (E {a} x) = a • E {a} x
```

**`ProbabilisticTheory.QuantumMechanics.cayleyBoundedSpectralMeasure_support_unit_circle`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L408).

```lean
lemma cayleyBoundedSpectralMeasure_support_unit_circle
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) (S : Set ℂ) (hS : MeasurableSet S) :
    cayleyBoundedSpectralMeasure T hT S =
      cayleyBoundedSpectralMeasure T hT (S ∩ {z | ‖z‖ = 1})
```

**`ProbabilisticTheory.QuantumMechanics.cayleyBoundedOperator_one_eigenspace_eq_bot`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L438).

```lean
lemma cayleyBoundedOperator_one_eigenspace_eq_bot
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) {x : H}
    (hx : cayleyBoundedOperator T hT x = x) : x = 0
```

**`ProbabilisticTheory.QuantumMechanics.cayleyBoundedSpectralMeasure_id_integrable`**, a lemma, [line 510](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L510).

```lean
lemma cayleyBoundedSpectralMeasure_id_integrable
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) (x y : H) :
    ((cayleyBoundedSpectralMeasure T hT).scalarMeasure x y).Integrable id
```

**`ProbabilisticTheory.QuantumMechanics.cayleyBoundedSpectralMeasure_singleton_one`**, a lemma, [line 537](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L537).

```lean
lemma cayleyBoundedSpectralMeasure_singleton_one
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) :
    cayleyBoundedSpectralMeasure T hT {1} = 0
```

**`ProbabilisticTheory.QuantumMechanics.cayleyBoundedSpectralMeasure_support_away_one`**, a lemma, [line 604](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L604).

```lean
lemma cayleyBoundedSpectralMeasure_support_away_one
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) (S : Set ℂ) (hS : MeasurableSet S) :
    cayleyBoundedSpectralMeasure T hT S =
      cayleyBoundedSpectralMeasure T hT (S ∩ {z | ‖z‖ = 1 ∧ z ≠ 1})
```

**`ProbabilisticTheory.QuantumMechanics.cayleyInverse_mul_one_sub_of_unit_circle`**, a lemma, [line 655](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L655).

```lean
lemma cayleyInverse_mul_one_sub_of_unit_circle
    {z : ℂ} (hz : ‖z‖ = 1) (hz1 : z ≠ 1) :
    (cayleyInverse z : ℂ) * (1 - z) = Complex.I * (1 + z)
```

**`ProbabilisticTheory.QuantumMechanics.cayley_domain_factorization`**, a lemma, [line 671](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L671).

```lean
lemma cayley_domain_factorization
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) (x : T.domain) :
    ∃ v : H,
      (x : H) = v - cayleyBoundedOperator T hT v ∧
        T x = Complex.I • (v + cayleyBoundedOperator T hT v)
```

### A.1. A bounded extension of the Cayley difference multiplier

> The function `1 - z` is bounded on the unit circle, where the spectral measure lives, but not on
> `ℂ`. It is extended by zero outside the closed unit disk.

**`ProbabilisticTheory.QuantumMechanics.cayleyDifferenceMultiplier`**, a def, [line 724](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L724).

> `z ↦ 1 - z` on the unit circle, extended by zero elsewhere so it is globally bounded.

```lean
def cayleyDifferenceMultiplier (z : ℂ) : ℂ
```

**`ProbabilisticTheory.QuantumMechanics.cayleyDifferenceMultiplier_measurable`**, a lemma, [line 727](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L727).

```lean
lemma cayleyDifferenceMultiplier_measurable :
    Measurable cayleyDifferenceMultiplier
```

**`ProbabilisticTheory.QuantumMechanics.cayleyDifferenceMultiplier_bounded`**, a lemma, [line 733](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L733).

```lean
lemma cayleyDifferenceMultiplier_bounded :
    ∃ C : ℝ, ∀ z : ℂ, ‖cayleyDifferenceMultiplier z‖ ≤ C
```

**`ProbabilisticTheory.QuantumMechanics.cayleyDifferenceMultiplier_eq_one_sub_of_unit_circle`**, a lemma, [line 741](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L741).

```lean
lemma cayleyDifferenceMultiplier_eq_one_sub_of_unit_circle {z : ℂ} (hz : ‖z‖ = 1) :
    cayleyDifferenceMultiplier z = 1 - z
```

**`ProbabilisticTheory.QuantumMechanics.boundedIntegral_cayleyDifferenceMultiplier_eq_sub`**, a lemma, [line 745](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L745).

```lean
lemma boundedIntegral_cayleyDifferenceMultiplier_eq_sub
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) :
    QuantumMechanics.WOTSpectralMeasure.boundedIntegral (cayleyBoundedSpectralMeasure T hT)
        cayleyDifferenceMultiplier cayleyDifferenceMultiplier_measurable
        cayleyDifferenceMultiplier_bounded =
      (1 : H →WOT[ℂ] H) -
        ContinuousLinearMapWOT.ofCLM (cayleyBoundedOperator T hT)
```

**`ProbabilisticTheory.QuantumMechanics.cayleyBoundedUnitarySpectralData`**, a def, [line 822](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L822).

> The bounded unitary spectral certificate for `T`'s Cayley unitary.

```lean
noncomputable def cayleyBoundedUnitarySpectralData
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) :
    QuantumMechanics.WOTSpectralMeasure.BoundedUnitarySpectralData
      (cayleyUnitary T hT)
```

**`ProbabilisticTheory.QuantumMechanics.cayleyRealSpectralMeasure`**, a def, [line 835](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L835).

> The real spectral measure of `T`, transported from its Cayley unitary's bounded unitary
> spectral data.

```lean
noncomputable def cayleyRealSpectralMeasure
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) :
    QuantumMechanics.WOTSpectralMeasure ℝ H
```

**`ProbabilisticTheory.QuantumMechanics.cayleyMap_cayleyRealSpectralMeasure`**, a lemma, [line 840](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean#L840).

```lean
lemma cayleyMap_cayleyRealSpectralMeasure
    (T : H →ₗ.[ℂ] H) (hT : IsSelfAdjoint T) :
    QuantumMechanics.WOTSpectralMeasure.cayleyMap (cayleyRealSpectralMeasure T hT) =
      cayleyBoundedSpectralMeasure T hT
```

## Depends on

- [Spectral data of bounded normal and unitary operators](../part-02/unbounded-cayley-certificate.md)
- [The spectral measure of a bounded normal operator](../part-04/unbounded-unitaryinfra-spectralmeasure.md)

## Proof depends on

- [Integrating unbounded functions against a spectral measure](unbounded-spectralintegral-construction.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/CayleySpectralData/Basic.lean)
