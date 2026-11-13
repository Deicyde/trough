---
declaration: module
origin: cited
lean: MeasureTheory.FiniteMeasure.pontryaginMeasureTransform, MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_apply, MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_zero, MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_zero_measure, MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_smul, MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_add, MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_dirac
statement: formalized
proof: formalized
---

# Fourier–Stieltjes transform of measures on a Pontryagin dual

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.Fourier.Pontryagin.Measure`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Measure.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Measure.lean): 7 declarations, 7 with a docstring.

> Integrating character evaluations against a finite positive measure on the Pontryagin dual defines a
> complex-valued function on the original additive group.

## i. Overview

> Integrating character evaluations against a finite positive measure on the Pontryagin dual
> defines a complex-valued function on the original additive group. The transform records the
> measure's mass at the identity and respects addition, scaling, and point masses.

## ii. Key results

> This file proves the statement described in the overview.

## iv. References

> * Standard material; the statements and proofs are original to this formalization.

## A. Development

**`MeasureTheory.FiniteMeasure.pontryaginMeasureTransform`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Measure.lean#L49).

> The Fourier–Stieltjes transform of a finite measure on the Pontryagin dual of an
> additive group.

```lean
noncomputable def _root_.MeasureTheory.FiniteMeasure.pontryaginMeasureTransform
    (μ : FiniteMeasure (PontryaginDual (Multiplicative G))) (g : G) : ℂ
```

**`MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_apply`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Measure.lean#L54).

> The transform evaluated at a group element is the integral of character evaluations.

```lean
lemma _root_.MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_apply
    (μ : FiniteMeasure (PontryaginDual (Multiplicative G))) (g : G) :
    μ.pontryaginMeasureTransform g =
      ∫ χ, (χ (Multiplicative.ofAdd g) : ℂ) ∂μ.toMeasure
```

**`MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_zero`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Measure.lean#L63).

> At the identity, the transform records the total mass of the measure.

```lean
lemma _root_.MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_zero
    (μ : FiniteMeasure (PontryaginDual (Multiplicative G))) :
    μ.pontryaginMeasureTransform 0 = (μ.toMeasure.real Set.univ : ℂ)
```

**`MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_zero_measure`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Measure.lean#L70).

> The transform of the zero measure vanishes.

```lean
lemma _root_.MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_zero_measure :
    (0 : FiniteMeasure (PontryaginDual (Multiplicative G))).pontryaginMeasureTransform = 0
```

**`MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_smul`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Measure.lean#L77).

> The transform commutes with nonnegative scalar multiplication of finite measures.

```lean
lemma _root_.MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_smul
    (c : NNReal) (μ : FiniteMeasure (PontryaginDual (Multiplicative G))) :
    (c • μ).pontryaginMeasureTransform = c • μ.pontryaginMeasureTransform
```

**`MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_add`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Measure.lean#L87).

> The transform commutes with addition of finite measures.

```lean
lemma _root_.MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_add
    (μ ν : FiniteMeasure (PontryaginDual (Multiplicative G))) :
    (μ + ν).pontryaginMeasureTransform =
      μ.pontryaginMeasureTransform + ν.pontryaginMeasureTransform
```

**`MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_dirac`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Measure.lean#L101).

> The transform of a point mass is its character.

```lean
lemma _root_.MeasureTheory.FiniteMeasure.pontryaginMeasureTransform_dirac
    (χ : PontryaginDual (Multiplicative G)) (g : G) :
    FiniteMeasure.pontryaginMeasureTransform
      (⟨Measure.dirac χ, inferInstance⟩ : FiniteMeasure
        (PontryaginDual (Multiplicative G))) g =
      (χ (Multiplicative.ofAdd g) : ℂ)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [Evaluation of Pontryagin characters](analysis-fourier-pontryagin-dualeval.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Measure.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/Fourier/Pontryagin/Measure.lean)
