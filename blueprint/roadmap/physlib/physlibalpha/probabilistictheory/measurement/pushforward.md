---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.mapEffect, ProbabilisticTheory.UnitalPositiveLinearMap.coe_mapEffect, ProbabilisticTheory.UnitalPositiveLinearMap.mapEffect_zero, ProbabilisticTheory.UnitalPositiveLinearMap.mapEffect_one, ProbabilisticTheory.EffectValuedMeasure.map, ProbabilisticTheory.EffectValuedMeasure.coe_map_apply
statement: formalized
proof: formalized
---

# Pushing an effect-valued measure forward along a channel

The module `PhyslibAlpha.ProbabilisticTheory.Measurement.Pushforward`, [PhyslibAlpha/ProbabilisticTheory/Measurement/Pushforward.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Pushforward.lean): 6 declarations, 2 with a docstring.

> Pushing an effect-valued measure forward along a normal channel.

## i. Overview

> A channel sends effects to effects. Applying a normal channel `φ : Channel E F` to every effect of
> an effect-valued measure `μ` on `E` therefore gives one, `μ.map φ`, on `F`, with the same outcomes.

## ii. Key results

> - `EffectValuedMeasure.map` : pushing an effect-valued measure forward along a normal channel.

## iv. References

> * None.

## A. Channels send effects to effects

**`ProbabilisticTheory.UnitalPositiveLinearMap.mapEffect`**, a def, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Pushforward.lean#L47).

> A channel sends effects to effects.

```lean
def mapEffect (φ : Channel E F) (e : Effect E) : Effect F
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.coe_mapEffect`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Pushforward.lean#L51).

```lean
lemma coe_mapEffect (φ : Channel E F) (e : Effect E) : (φ.mapEffect e : F) = φ e
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.mapEffect_zero`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Pushforward.lean#L54).

```lean
lemma mapEffect_zero (φ : Channel E F) : φ.mapEffect 0 = 0
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.mapEffect_one`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Pushforward.lean#L57).

```lean
lemma mapEffect_one (φ : Channel E F) : φ.mapEffect 1 = 1
```

## B. Pushing an effect-valued measure forward

**`ProbabilisticTheory.EffectValuedMeasure.map`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Pushforward.lean#L66).

> Pushing an effect-valued measure forward along a normal channel.

```lean
def map (μ : EffectValuedMeasure Ω E) (φ : Channel E F) (hφ : φ.IsNormal) :
    EffectValuedMeasure Ω F
```

**`ProbabilisticTheory.EffectValuedMeasure.coe_map_apply`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Pushforward.lean#L75).

```lean
lemma coe_map_apply (μ : EffectValuedMeasure Ω E) (φ : Channel E F) (hφ : φ.IsNormal)
    (s : Set Ω) (hs : MeasurableSet s) : (μ.map φ hφ s hs : F) = φ (μ s hs)
```

## Depends on

- [Normal channels](../channel/normal.md)
- [Effect-valued measures](effectvaluedmeasure.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Measurement/Pushforward.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Pushforward.lean)
