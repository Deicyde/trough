---
declaration: module
origin: cited
lean: ProbabilisticTheory.EffectValuedMeasure.map_simpleIntegral, ProbabilisticTheory.EffectValuedMeasure.instNormedAddCommGroupE, ProbabilisticTheory.EffectValuedMeasure.instNormedAddCommGroupF, ProbabilisticTheory.EffectValuedMeasure.map_integral
statement: formalized
proof: formalized
---

# Channels and integrals

The module `PhyslibAlpha.ProbabilisticTheory.Measurement.BoundedScalarization`, [PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedScalarization.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedScalarization.lean): 4 declarations, 2 with a docstring.

> Normal channels commute with integration against effect-valued measures.

## i. Overview

> A normal channel maps an effect-valued measure to an effect-valued measure, and it commutes with
> integration of bounded functions.

## ii. Key results

> - `EffectValuedMeasure.map_simpleIntegral` : for simple functions.
> - `EffectValuedMeasure.map_integral` : for bounded measurable functions.

## iv. References

> * None.

## A. Simple integrals

**`ProbabilisticTheory.EffectValuedMeasure.map_simpleIntegral`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedScalarization.lean#L51).

> Pushing an effect-valued measure through a normal channel commutes with its simple integral.

```lean
lemma map_simpleIntegral (μ : EffectValuedMeasure Ω E) (φ : Channel E F) (hφ : φ.IsNormal)
    {ι : Type*} [Fintype ι] (c : ι → ℝ) (s : ι → Set Ω) (hs : IsPartition s) :
    φ (simpleIntegral μ c s hs) = simpleIntegral (μ.map φ hφ) c s hs
```

## B. Bounded integrals

**`ProbabilisticTheory.EffectValuedMeasure.instNormedAddCommGroupE`**, an instance, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedScalarization.lean#L68).

```lean
noncomputable local instance instNormedAddCommGroupE : NormedAddCommGroup E
```

**`ProbabilisticTheory.EffectValuedMeasure.instNormedAddCommGroupF`**, an instance, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedScalarization.lean#L72).

```lean
noncomputable local instance instNormedAddCommGroupF : NormedAddCommGroup F
```

**`ProbabilisticTheory.EffectValuedMeasure.map_integral`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedScalarization.lean#L80).

> A normal channel commutes with the bounded effect-valued integral.  The only analytic input is
> order-unit contractivity of a unital positive map; normality is used solely to make `μ.map φ hφ`
> an effect-valued measure.

```lean
lemma map_integral {f : Ω → ℝ} {M : ℝ} (hf : Measurable f) (hM : ∀ x, |f x| ≤ M)
    (μ : EffectValuedMeasure Ω E) (φ : Channel E F) (hφ : φ.IsNormal) :
    φ (integral hf hM μ) = integral hf hM (μ.map φ hφ)
```

## Depends on

- [Integrating bounded functions against an effect-valued measure](boundedintegral.md)
- [Pushing an effect-valued measure forward along a channel](pushforward.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedScalarization.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BoundedScalarization.lean)
