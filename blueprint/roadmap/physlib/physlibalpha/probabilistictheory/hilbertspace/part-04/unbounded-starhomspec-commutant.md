---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.starHomCommutant, ProbabilisticTheory.QuantumMechanics.mem_starHomCommutant_iff, ProbabilisticTheory.QuantumMechanics.starHomCommutant_isClosed, ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_commute_of_commute, ProbabilisticTheory.QuantumMechanics.starHomSpectralMeasure_commute_of_commute
statement: formalized
proof: formalized
---

# The commutant of a representation of continuous functions

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.StarHomSpec.Commutant`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Commutant.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Commutant.lean): 5 declarations, 3 with a docstring.

> Every bounded operator commuting with the range of `Φ` commutes with its spectral measure.

## i. Overview

> The spectral measure of `Φ` commutes with every unitary operator commuting with the range of `Φ`.
> A bounded operator commuting with the range of `Φ` lies in the commutant of the range, a closed
> ⋆-subalgebra of `B(H)` and hence a C⋆-algebra, which is spanned by its unitary elements. So the
> spectral measure commutes with every operator commuting with the range of `Φ`.

## ii. Key results

> - `starHomSpectralMeasure_commute_of_commute` : the spectral measure of `Φ` commutes with every
>   bounded operator commuting with the range of `Φ`.

## iv. References

> * None.

**`ProbabilisticTheory.QuantumMechanics.starHomCommutant`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Commutant.lean#L57).

> The commutant of the range of `Φ`, a ⋆-subalgebra of the bounded operators.

```lean
def starHomCommutant : StarSubalgebra ℂ (H →L[ℂ] H)
```

**`ProbabilisticTheory.QuantumMechanics.mem_starHomCommutant_iff`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Commutant.lean#L61).

```lean
lemma mem_starHomCommutant_iff {T : H →L[ℂ] H} :
    T ∈ starHomCommutant Φ ↔ ∀ f : C(X, ℂ), Commute (Φ f) T
```

**`ProbabilisticTheory.QuantumMechanics.starHomCommutant_isClosed`**, an instance, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Commutant.lean#L72).

```lean
instance starHomCommutant_isClosed : IsClosed (starHomCommutant Φ : Set (H →L[ℂ] H))
```

## A. Arbitrary operators in the commutant

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralOperator_commute_of_commute`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Commutant.lean#L82).

> **The spectral operators commute with the commutant**: every bounded operator commuting with
> the range of `Φ` commutes with each spectral operator of `Φ`. A bounded operator commuting with the
> range is a combination of four unitary operators in the C⋆-algebra of such operators, and the
> spectral operators commute with unitaries commuting with the range.

```lean
lemma starHomSpectralOperator_commute_of_commute {T : H →L[ℂ] H}
    (hT : ∀ f : C(X, ℂ), Commute (Φ f) T) (S : Set X) :
    starHomSpectralOperator Φ S * T = T * starHomSpectralOperator Φ S
```

**`ProbabilisticTheory.QuantumMechanics.starHomSpectralMeasure_commute_of_commute`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Commutant.lean#L104).

> **The spectral measure commutes with the commutant**: every bounded operator commuting with
> the range of `Φ` commutes with each spectral projection of `Φ`.

```lean
lemma starHomSpectralMeasure_commute_of_commute {T : H →L[ℂ] H}
    (hT : ∀ f : C(X, ℂ), Commute (Φ f) T) (S : Set X) :
    starHomSpectralMeasure Φ S * ContinuousLinearMapWOT.ofCLM T =
      ContinuousLinearMapWOT.ofCLM T * starHomSpectralMeasure Φ S
```

## Depends on

- [The spectral measure of a representation of continuous functions](unbounded-starhomspec-spectralmeasure.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Commutant.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/StarHomSpec/Commutant.lean)
