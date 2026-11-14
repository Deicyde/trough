---
declaration: module
origin: cited
lean: ContinuousOn.aestronglyMeasurable_of_measure_ne_top, Continuous.aestronglyMeasurable_of_sigmaFinite, MeasureTheory.AEFinStronglyMeasurable.aestronglyMeasurable_smul
statement: formalized
proof: formalized
---

# Continuous functions are a.e. strongly measurable for inner regular measures

The module `PhyslibAlpha.Mathematics.TauCeti.MeasureTheory.Function.StronglyMeasurable.InnerRegular`, [PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Function/StronglyMeasurable/InnerRegular.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Function/StronglyMeasurable/InnerRegular.lean): 3 declarations, 3 with a docstring.

> Mathlib's `ContinuousOn.aestronglyMeasurable` and `Continuous.aestronglyMeasurable` read almost
> everywhere strong measurability of a continuous function off second countability of its source or
> target.

## i. Overview

> Mathlib's `ContinuousOn.aestronglyMeasurable` and `Continuous.aestronglyMeasurable` read almost
> everywhere strong measurability of a continuous function off second countability of its source or
> target. This file gives the alternative source of separability: inner regularity of the measure.
> If `μ` is inner regular with respect to compact sets on measurable sets of finite measure
> (`MeasureTheory.Measure.InnerRegularCompactLTTop`), as every regular measure is (for instance the
> Haar measure `MeasureTheory.Measure.addHaar` of a locally compact group), then up to a null set each
> such set is a countable union of compact sets, whose images under a continuous function are
> separable.
>
> The main application is to integrands `f x • g x` with `f` integrable and `g` continuous, such as
> the orbits `g ↦ f g • π g v` integrated in the integrated form of a strongly continuous group
> representation. On a locally compact group that is not σ-compact a Haar measure is not σ-finite,
> and a continuous function need not be a.e. strongly measurable on the whole group; but an
> integrable `f` lives on a σ-finite set, and there the inner regular case applies.

## ii. Key results

> * `ContinuousOn.aestronglyMeasurable_of_measure_ne_top`: a function continuous on a measurable set
>   of finite measure is a.e. strongly measurable for the restriction of `μ` to that set.
> * `Continuous.aestronglyMeasurable_of_sigmaFinite`: a continuous function is a.e. strongly
>   measurable for a σ-finite inner regular measure.
> * `MeasureTheory.AEFinStronglyMeasurable.aestronglyMeasurable_smul`: the product `f • g` of an
>   a.e. finitely strongly measurable `f` (for instance an integrable one) and a continuous `g` is
>   a.e. strongly measurable.

## iv. References

> * Standard material; the statements and proofs are original to this formalization.

## A. Development

**`ContinuousOn.aestronglyMeasurable_of_measure_ne_top`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Function/StronglyMeasurable/InnerRegular.lean#L66).

> For a measure that is inner regular with respect to compact sets on sets of finite measure, a
> function continuous on a measurable set `s` of finite measure is a.e. strongly measurable for the
> restriction of the measure to `s`.

```lean
lemma ContinuousOn.aestronglyMeasurable_of_measure_ne_top {f : α → β} {s : Set α}
    (hf : ContinuousOn f s) (hs : MeasurableSet s) (hμs : μ s ≠ ∞) :
    AEStronglyMeasurable f (μ.restrict s)
```

**`Continuous.aestronglyMeasurable_of_sigmaFinite`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Function/StronglyMeasurable/InnerRegular.lean#L86).

> A continuous function is a.e. strongly measurable for a σ-finite measure that is inner regular
> with respect to compact sets on sets of finite measure. Compare `Continuous.aestronglyMeasurable`,
> which asks for second countability of the source or the target instead.

```lean
lemma Continuous.aestronglyMeasurable_of_sigmaFinite [SigmaFinite μ] {f : α → β}
    (hf : Continuous f) : AEStronglyMeasurable f μ
```

**`MeasureTheory.AEFinStronglyMeasurable.aestronglyMeasurable_smul`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Function/StronglyMeasurable/InnerRegular.lean#L97).

> The product of an a.e. finitely strongly measurable function `f`, for instance an integrable
> one, and a continuous function `g` is a.e. strongly measurable, for a measure that is inner regular
> with respect to compact sets on sets of finite measure. No σ-finiteness of the measure and no
> second countability is needed: `f` vanishes outside a σ-finite set, on which `g` is a.e. strongly
> measurable by `Continuous.aestronglyMeasurable_of_sigmaFinite`.

```lean
lemma MeasureTheory.AEFinStronglyMeasurable.aestronglyMeasurable_smul {𝕜 : Type*}
    [TopologicalSpace 𝕜] [T2Space 𝕜] [Zero 𝕜] [Zero β] [SMulWithZero 𝕜 β] [ContinuousSMul 𝕜 β]
    {f : α → 𝕜} (hf : AEFinStronglyMeasurable f μ) {g : α → β} (hg : Continuous g) :
    AEStronglyMeasurable (fun x ↦ f x • g x) μ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Function/StronglyMeasurable/InnerRegular.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/MeasureTheory/Function/StronglyMeasurable/InnerRegular.lean)
