---
declaration: module
origin: cited
lean: ProbabilisticTheory.EffectValuedMeasure.ofReal_iUnion, ProbabilisticTheory.EffectValuedMeasure.toMeasure, ProbabilisticTheory.EffectValuedMeasure.toMeasure_apply, ProbabilisticTheory.EffectValuedMeasure.isProbabilityMeasure_toMeasure, ProbabilisticTheory.EffectValuedMeasure.toProbabilityMeasure, ProbabilisticTheory.EffectValuedMeasure.scalarize, ProbabilisticTheory.EffectValuedMeasure.coe_scalarize_apply, ProbabilisticTheory.EffectValuedMeasure.probabilityLaw
statement: formalized
proof: formalized
---

# The Born rule for effect-valued measures

The module `PhyslibAlpha.ProbabilisticTheory.Measurement.BornRule`, [PhyslibAlpha/ProbabilisticTheory/Measurement/BornRule.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BornRule.lean): 10 declarations, 5 with a docstring.

> An effect-valued measure sends each normal state to a probability law on its outcomes.

## i. Overview

> A state is a normal channel `ω : 𝓢[ℝ, E]`, so it pushes an effect-valued measure `μ` on `E`
> forward to one, `μ.map ω`, on `ℝ`. An effect-valued measure on `ℝ` is just a probability measure.
> So `μ` sends every normal state to a probability distribution over its outcomes:
> `μ.probabilityLaw ω`, giving event `s` probability `ω (μ s)`.

## ii. Key results

> - `EffectValuedMeasure.toProbabilityMeasure` : an effect-valued measure on `ℝ` is a
>   probability measure.
> - `EffectValuedMeasure.probabilityLaw` : the outcome distribution of `μ` in the state `ω`.

## iv. References

> * None.

## A. Effect-valued measures on `ℝ` are probability measures

**`ProbabilisticTheory.EffectValuedMeasure.ofReal_iUnion`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BornRule.lean#L54).

```lean
lemma ofReal_iUnion (ν : EffectValuedMeasure Ω ℝ) ⦃s : ℕ → Set Ω⦄ (hs : ∀ n, MeasurableSet (s n))
    (hd : Pairwise (Disjoint on s)) :
    ENNReal.ofReal (ν (⋃ n, s n) (.iUnion hs)) = ∑' n, ENNReal.ofReal (ν (s n) (hs n))
```

**`ProbabilisticTheory.EffectValuedMeasure.toMeasure`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BornRule.lean#L63).

> An effect-valued measure on `ℝ` as a measure.

```lean
noncomputable def toMeasure (ν : EffectValuedMeasure Ω ℝ) : Measure Ω
```

**`ProbabilisticTheory.EffectValuedMeasure.toMeasure_apply`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BornRule.lean#L67).

```lean
lemma toMeasure_apply (ν : EffectValuedMeasure Ω ℝ) (s : Set Ω) (hs : MeasurableSet s) :
    ν.toMeasure s = ENNReal.ofReal (ν s hs)
```

**`ProbabilisticTheory.EffectValuedMeasure.isProbabilityMeasure_toMeasure`**, an instance, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BornRule.lean#L71).

```lean
instance isProbabilityMeasure_toMeasure (ν : EffectValuedMeasure Ω ℝ) :
    IsProbabilityMeasure ν.toMeasure
```

**`ProbabilisticTheory.EffectValuedMeasure.toProbabilityMeasure`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BornRule.lean#L76).

> An effect-valued measure on `ℝ` as a probability measure.

```lean
noncomputable def toProbabilityMeasure (ν : EffectValuedMeasure Ω ℝ) : ProbabilityMeasure Ω
```

## B. The Born rule

**`ProbabilisticTheory.EffectValuedMeasure.scalarize`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BornRule.lean#L84).

> The effect-valued measure on `ℝ` obtained by pushing `μ` forward along the normal state `ω`.

```lean
def scalarize (μ : EffectValuedMeasure Ω E) (ω : 𝓢[ℝ, E]) (hω : ω.IsNormal) :
    EffectValuedMeasure Ω ℝ
```

**`ProbabilisticTheory.EffectValuedMeasure.coe_scalarize_apply`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BornRule.lean#L89).

```lean
lemma coe_scalarize_apply (μ : EffectValuedMeasure Ω E) (ω : 𝓢[ℝ, E]) (hω : ω.IsNormal)
    (s : Set Ω) (hs : MeasurableSet s) : (μ.scalarize ω hω s hs : ℝ) = ω (μ s hs)
```

**`ProbabilisticTheory.EffectValuedMeasure.probabilityLaw`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BornRule.lean#L93).

> The outcome distribution of the effect-valued measure `μ` in the normal state `ω`.

```lean
noncomputable def probabilityLaw (μ : EffectValuedMeasure Ω E) (ω : 𝓢[ℝ, E]) (hω : ω.IsNormal) :
    ProbabilityMeasure Ω
```

**`ProbabilisticTheory.EffectValuedMeasure.probabilityLaw_apply`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BornRule.lean#L98).

```lean
lemma probabilityLaw_apply (μ : EffectValuedMeasure Ω E) (ω : 𝓢[ℝ, E]) (hω : ω.IsNormal)
    (s : Set Ω) (hs : MeasurableSet s) :
    (μ.probabilityLaw ω hω : Measure Ω) s = ENNReal.ofReal (ω (μ s hs))
```

## C. Relabeling outcomes

**`ProbabilisticTheory.EffectValuedMeasure.probabilityLaw_mapOutcome`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BornRule.lean#L110).

> Relabeling outcomes pushes each Born law forward along the relabeling map.

```lean
lemma probabilityLaw_mapOutcome (N : EffectValuedMeasure Ω' E) (f : Ω' → Ω)
    (hf : Measurable f) (ω : 𝓢[ℝ, E]) (hω : ω.IsNormal) :
    (N.mapOutcome f hf).probabilityLaw ω hω = (N.probabilityLaw ω hω).map f
```

## Depends on

- [Pushing an effect-valued measure forward along a channel](pushforward.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Measurement/BornRule.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/BornRule.lean)
