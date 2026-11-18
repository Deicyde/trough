---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.HasActionVariationDerivativeUnderIntegral, ClassicalFieldTheory.Local.HasPointwiseLinearizedDensityFormula, ClassicalFieldTheory.Local.actionVariation_hasDerivAt_of_dominated_loc_of_deriv_le, ClassicalFieldTheory.Local.HasDominatedVariationDerivativeNear, ClassicalFieldTheory.Local.hasDominatedVariationDerivativeNear_of_continuous_coordDeriv, ClassicalFieldTheory.Local.hasDerivAt_actionDensity_variedField_zero_of_contDiff, ClassicalFieldTheory.Local.hasDerivAt_actionDensity_variedField_of_contDiff, ClassicalFieldTheory.Local.hasPointwiseLinearizedDensityFormula_of_contDiff
statement: formalized
proof: formalized
---

# First variation density formulas

The module `PhyslibAlpha.ClassicalFieldTheory.Local.FirstVariation.Density`, [PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Density.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Density.lean): 11 declarations, 5 with a docstring; 3 private, not shown.

> Differentiation of the varied action density, pointwise and under the integral sign.

## i. Overview

> This module contains the pointwise and integral first-variation formulas before integration by
> parts: differentiation of the varied action density, dominated differentiation under the integral,
> and the corresponding packaged hypotheses.

## ii. Key results

> - `ClassicalFieldTheory.Local.hasPointwiseLinearizedDensityFormula_of_contDiff`
> - `ClassicalFieldTheory.Local.hasActionVariationDerivativeUnderIntegral_of_contDiff_of_regular`

## iv. References

> * J. Cortés and A. Haupt, Lecture Notes on Mathematical Methods of Classical Physics, Chapter 5,
>   Theorem 5.2. [ref: cortes\_haupt\_2016]

## A. Differentiation under the integral sign

**`ClassicalFieldTheory.Local.HasActionVariationDerivativeUnderIntegral`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Density.lean#L53).

> Differentiation of the varied action under the integral sign, packaged as a hypothesis.

```lean
def HasActionVariationDerivativeUnderIntegral (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) :
    Prop
```

**`ClassicalFieldTheory.Local.HasPointwiseLinearizedDensityFormula`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Density.lean#L61).

> Pointwise linearization of the action density before integration by parts.

```lean
def HasPointwiseLinearizedDensityFormula (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) : Prop
```

**`ClassicalFieldTheory.Local.actionVariation_hasDerivAt_of_dominated_loc_of_deriv_le`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Density.lean#L70).

> A direct bridge from Mathlib's dominated differentiation-under-the-integral theorem to the
> local action variation. This isolates the measure-theoretic input needed to prove
> `HasActionVariationDerivativeUnderIntegral`.

```lean
lemma actionVariation_hasDerivAt_of_dominated_loc_of_deriv_le
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m)))
    {F' : ℝ → Space d → ℝ} {bound : Space d → ℝ} {ε : ℝ} (hε : 0 < ε)
    (hmeas :
      ∀ᶠ s in nhds (0 : ℝ),
        AEStronglyMeasurable (actionDensity L (variedField f η s)) volume)
    (hfinite0 : Integrable (actionDensity L (variedField f η 0)))
    (hF'_meas : AEStronglyMeasurable (F' 0) volume)
    (hbound :
      ∀ᵐ x ∂volume, ∀ s ∈ Metric.ball (0 : ℝ) ε, ‖F' s x‖ ≤ bound x)
    (hbound_int : Integrable bound volume)
    (hderiv :
      ∀ᵐ x ∂volume, ∀ s ∈ Metric.ball (0 : ℝ) ε,
        HasDerivAt (fun r : ℝ => actionDensity L (variedField f η r) x) (F' s x) s) :
    HasDerivAt (actionVariation L f η) (∫ x, F' 0 x) 0
```

**`ClassicalFieldTheory.Local.HasDominatedVariationDerivativeNear`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Density.lean#L96).

> A dominated bound for the pointwise first variation along the varied-field family near
> `s = 0`. This packages the analytic domination needed to differentiate the action under the
> integral sign.

```lean
def HasDominatedVariationDerivativeNear (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m))) : Prop
```

**`ClassicalFieldTheory.Local.hasDominatedVariationDerivativeNear_of_continuous_coordDeriv`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Density.lean#L196).

> A concrete dominated bound for the varied first-variation density, obtained from continuity of
> the jet-coordinate coefficient family in `(s, x)`. The compact support of the iterated derivatives
> of the admissible variation supplies the integrable majorant.

```lean
lemma hasDominatedVariationDerivativeNear_of_continuous_coordDeriv
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m)))
    (hcont : ∀ I : DerivativeIndex d k, ∀ a : Fin m,
      Continuous (fun p : ℝ × Space d =>
        L.coordDeriv I a (jetAt k (variedField f η p.1) p.2))) :
    HasDominatedVariationDerivativeNear L f η
```

## B. Pointwise linearization

**`ClassicalFieldTheory.Local.hasDerivAt_actionDensity_variedField_zero_of_contDiff`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Density.lean#L258).

```lean
lemma hasDerivAt_actionDensity_variedField_zero_of_contDiff
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m)) (hf : ContDiff ℝ ∞ f) :
    ∀ η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m)), ∀ x : Space d,
      HasDerivAt (fun s : ℝ => actionDensity L (variedField f η s) x)
        (firstVariationDensity L f η x) 0
```

**`ClassicalFieldTheory.Local.hasDerivAt_actionDensity_variedField_of_contDiff`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Density.lean#L280).

```lean
lemma hasDerivAt_actionDensity_variedField_of_contDiff
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m)) (hf : ContDiff ℝ ∞ f)
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m))) (x : Space d) (s : ℝ) :
    HasDerivAt (fun r : ℝ => actionDensity L (variedField f η r) x)
      (firstVariationDensity L (variedField f η s) η x) s
```

**`ClassicalFieldTheory.Local.hasPointwiseLinearizedDensityFormula_of_contDiff`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Density.lean#L300).

```lean
lemma hasPointwiseLinearizedDensityFormula_of_contDiff
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m)) (hf : ContDiff ℝ ∞ f) :
    HasPointwiseLinearizedDensityFormula L f
```

**`ClassicalFieldTheory.Local.hasActionVariationDerivativeUnderIntegral_of_contDiff_of_dominatedVariation`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Density.lean#L306).

```lean
lemma hasActionVariationDerivativeUnderIntegral_of_contDiff_of_dominatedVariation
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m)) (hf : ContDiff ℝ ∞ f)
    (hdom : ∀ η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m)),
      HasFiniteActionVariation L f η →
      HasDominatedVariationDerivativeNear L f η) :
    HasActionVariationDerivativeUnderIntegral L f
```

**`ClassicalFieldTheory.Local.hasActionVariationDerivativeUnderIntegral_of_contDiff_of_continuous_coordDeriv`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Density.lean#L341).

```lean
lemma hasActionVariationDerivativeUnderIntegral_of_contDiff_of_continuous_coordDeriv
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m)) (hf : ContDiff ℝ ∞ f)
    (hcontVar : ∀ η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m)),
      ∀ I : DerivativeIndex d k, ∀ a : Fin m,
      Continuous (fun p : ℝ × Space d =>
        L.coordDeriv I a (jetAt k (variedField f η p.1) p.2))) :
    HasActionVariationDerivativeUnderIntegral L f
```

**`ClassicalFieldTheory.Local.hasActionVariationDerivativeUnderIntegral_of_contDiff_of_regular`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Density.lean#L352).

```lean
lemma hasActionVariationDerivativeUnderIntegral_of_contDiff_of_regular
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m)) (hf : ContDiff ℝ ∞ f)
    (hcontVar : ∀ η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m)),
      Lagrangian.ContinuousCoordDerivAlongFamily L (fun s : ℝ => variedField f η s)) :
    HasActionVariationDerivativeUnderIntegral L f
```

## Depends on

- [Local action functionals](action.md)
- [First variation core objects](firstvariation-basic.md)

## Proof depends on

- [First variation support lemmas](firstvariation-support.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Density.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Density.lean)
