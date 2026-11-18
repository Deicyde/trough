---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_inner_projection', ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_variation_le_diagonal_add', ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_isFiniteVariation', ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_commute
statement: formalized
proof: formalized
---

# Operators commuting with a spectral measure

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.BoundedIntegralCommute`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralCommute.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralCommute.lean): 4 declarations, 2 with a docstring.

> An operator commuting with every spectral projection commutes with every bounded spectral integral.

## i. Overview

> The matrix-coefficient measures of a spectral measure have finite variation on every spectral
> variable space, not only on the real line. If `T` commutes with every spectral projection, the
> matrix-coefficient measure of `(T x, y)` agrees with that of `(x, T⋆ y)`. Integrating a bounded
> measurable function against these measures shows that `T` commutes with the integral.

## ii. Key results

> - `WOTSpectralMeasure.scalarMeasure_isFiniteVariation'` : matrix-coefficient measures have finite
>   variation.
> - `WOTSpectralMeasure.boundedIntegral_commute` : an operator commuting with the spectral
>   projections commutes with every bounded integral.

## iv. References

> * None.

## A. Finite variation of the matrix-coefficient measures

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_inner_projection'`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralCommute.lean#L60).

```lean
lemma scalarMeasure_inner_projection' (x y : H) (S : Set α) :
    ⟪y, μS S x⟫_ℂ = ⟪μS S y, μS S x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_variation_le_diagonal_add'`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralCommute.lean#L80).

```lean
lemma scalarMeasure_variation_le_diagonal_add' (x y : H) :
    (μS.scalarMeasure x y).variation ≤ μS.diagonalMeasure x + μS.diagonalMeasure y
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_isFiniteVariation'`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralCommute.lean#L96).

> The matrix-coefficient measures of a weak spectral measure have finite variation.

```lean
lemma scalarMeasure_isFiniteVariation' (x y : H) :
    IsFiniteMeasure (μS.scalarMeasure x y).variation
```

## B. Commutation with the bounded integrals

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_commute`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralCommute.lean#L105).

> An operator commuting with every spectral projection commutes with every bounded integral
> against the spectral measure.

```lean
lemma boundedIntegral_commute [Nonempty α] {T : H →L[ℂ] H}
    (hT : ∀ S, μS S * ContinuousLinearMapWOT.ofCLM T = ContinuousLinearMapWOT.ofCLM T * μS S)
    {f : α → ℂ} (hf : Measurable f) (hbf : ∃ C, ∀ z, ‖f z‖ ≤ C) :
    ContinuousLinearMapWOT.toCLM (boundedIntegral μS f hf hbf) * T =
      T * ContinuousLinearMapWOT.toCLM (boundedIntegral μS f hf hbf)
```

## Depends on

- [Integrating bounded functions against a spectral measure](unbounded-boundedintegral.md)

## Proof depends on

- [Integrating unbounded functions against a spectral measure](../part-03/unbounded-spectralintegral-construction.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralCommute.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralCommute.lean)
