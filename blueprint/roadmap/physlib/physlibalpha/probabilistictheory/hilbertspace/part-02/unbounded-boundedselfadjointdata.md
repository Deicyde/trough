---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.boundedSelfAdjointSpectralMeasure, ProbabilisticTheory.QuantumMechanics.boundedSelfAdjointSpectralMeasure_reconstruction, ProbabilisticTheory.QuantumMechanics.boundedSelfAdjointSpectralMeasure_commute_of_commute, ProbabilisticTheory.QuantumMechanics.exists_boundedSelfAdjointSpectralSupport
statement: formalized
proof: formalized
---

# Spectral measures of bounded self-adjoint operators

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.BoundedSelfAdjointData`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedSelfAdjointData.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedSelfAdjointData.lean): 4 declarations, 2 with a docstring.

> The real spectral measure of a bounded self-adjoint operator.

## i. Overview

> The spectral measure of a bounded normal operator lives on its complex spectrum. For a self-adjoint
> operator the spectrum is real, and pushing the measure forward along `Complex.re` gives a spectral
> measure on `ℝ` that reconstructs the operator.

## ii. Key results

> - `boundedSelfAdjointSpectralMeasure` : the real spectral measure of a bounded self-adjoint
>   operator.
> - `boundedSelfAdjointSpectralMeasure_reconstruction` : the operator is the integral of the identity.
> - `boundedSelfAdjointSpectralMeasure_commute_of_commute` : operators commuting with `T` commute with
>   its spectral projections.

## iv. References

> * None.

## A. The real spectral measure

**`ProbabilisticTheory.QuantumMechanics.boundedSelfAdjointSpectralMeasure`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedSelfAdjointData.lean#L62).

> The real spectral measure of a bounded self-adjoint operator: the spectral measure on its
> complex spectrum, pushed forward along `Complex.re`.

```lean
noncomputable def boundedSelfAdjointSpectralMeasure
    (A : H →L[ℂ] H) (hA : IsSelfAdjoint A) :
    QuantumMechanics.WOTSpectralMeasure ℝ H
```

**`ProbabilisticTheory.QuantumMechanics.boundedSelfAdjointSpectralMeasure_reconstruction`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedSelfAdjointData.lean#L68).

```lean
lemma boundedSelfAdjointSpectralMeasure_reconstruction
    (A : H →L[ℂ] H) (hA : IsSelfAdjoint A) (x y : H) :
    (boundedSelfAdjointSpectralMeasure A hA).complexWeakIntegral
        (fun r : ℝ => (r : ℂ)) x y = ⟪y, A x⟫_ℂ
```

## B. Commutation and bounded support

**`ProbabilisticTheory.QuantumMechanics.boundedSelfAdjointSpectralMeasure_commute_of_commute`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedSelfAdjointData.lean#L113).

> The spectral projections of a bounded self-adjoint operator commute with every unitary that
> commutes with it.

```lean
lemma boundedSelfAdjointSpectralMeasure_commute_of_commute
    (A : H →L[ℂ] H) (hA : IsSelfAdjoint A) {T : H →L[ℂ] H} (hAT : Commute A T)
    (hTunit : T ∈ unitary (H →L[ℂ] H)) (E : Set ℝ) :
    boundedSelfAdjointSpectralMeasure A hA E * ContinuousLinearMapWOT.ofCLM T =
      ContinuousLinearMapWOT.ofCLM T * boundedSelfAdjointSpectralMeasure A hA E
```

**`ProbabilisticTheory.QuantumMechanics.exists_boundedSelfAdjointSpectralSupport`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedSelfAdjointData.lean#L130).

```lean
lemma exists_boundedSelfAdjointSpectralSupport
    (A : H →L[ℂ] H) (hA : IsSelfAdjoint A) :
    ∃ C : ℝ, HasBoundedSpectralSupport
      (boundedSelfAdjointSpectralMeasure A hA) C
```

## Depends on

- [The spectral theorem, stated](unbounded-selfadjointspectraltheorem.md)
- [The spectral measure of a bounded normal operator](../part-04/unbounded-unitaryinfra-spectralmeasure.md)

## Proof depends on

- [The spectral measure of the Cayley transform](../part-03/unbounded-cayleyspectraldata-basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedSelfAdjointData.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedSelfAdjointData.lean)
