---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.Measurement, PhyslibAlpha.ProbabilisticTheory.Measurement.ext, PhyslibAlpha.ProbabilisticTheory.Measurement.coe_apply, PhyslibAlpha.ProbabilisticTheory.Measurement.toEffectValuedMeasure, PhyslibAlpha.ProbabilisticTheory.Measurement.toEffectValuedMeasure_apply, PhyslibAlpha.ProbabilisticTheory.Measurement.map_empty, PhyslibAlpha.ProbabilisticTheory.Measurement.map_univ, PhyslibAlpha.ProbabilisticTheory.Measurement.isNormal_comp
statement: formalized
proof: formalized
---

# Measurements

The module `PhyslibAlpha.ProbabilisticTheory.Measurement.Basic`, [PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean): 18 declarations (1 instance with no name), 9 with a docstring.

> Measurements as normal channels from the classical outcome system, and their Born laws.

## i. Overview

> A measurement with outcomes in `Ω` turns the system into a classical record: its outcome. So a
> measurement is a channel from the system into the classical system of outcomes. In the Heisenberg
> picture used here, it sends each observable `f` of the outcome, a bounded measurable function on
> `Ω`, to the observable of the system whose expectation is the expectation of `f` after the
> measurement. It is normal: it respects limits of increasing sequences.
>
> The indicator of an event goes to the effect testing whether the outcome lands in it; these effects
> form an effect-valued measure. In a normal state `ω` of the system, the outcome record is in the
> normal state `ω ∘ M` of the classical system, which is a probability distribution over the outcomes:
> the Born law. Measuring the outcome of a classical system itself is the identity channel.

## ii. Key results

> - `Measurement Ω E` : a measurement with outcomes in `Ω`, a normal channel from the classical system
>   of outcomes.
> - `Measurement.toEffectValuedMeasure` : the effects of the events of a measurement.
> - `Measurement.probabilityLaw` : the Born law of a measurement in a normal state.
> - `Measurement.integral_probabilityLaw` : the average of `f` under the Born law is the expectation
>   of `M f`.
> - `Measurement.map` : measuring after a normal channel.
> - `BoundedMeasurable.outcome` : measuring the outcome of a classical system.

## iv. References

> * None.

## A. Measurements

**`PhyslibAlpha.ProbabilisticTheory.Measurement`**, a structure, [line 61](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean#L61).

> A measurement with outcomes in `Ω`: a normal channel from the classical system of outcomes
> into the system.

```lean
structure Measurement (Ω : Type*) [MeasurableSpace Ω] (E : Type*) [OrderUnitSpace E] where
  /-- The channel sending observables of the outcome to observables of the system. -/
  toChannel : Channel (BoundedMeasurable Ω) E
  /-- The channel is normal. -/
  isNormal : toChannel.IsNormal
```

**`PhyslibAlpha.ProbabilisticTheory.Measurement.ext`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean#L72).

```lean
lemma ext {M N : Measurement Ω E} (h : M.toChannel = N.toChannel) : M = N
```

**An instance with no name**, [line 76](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean#L76).

> The effect testing whether the outcome lies in an event.

```lean
noncomputable instance :
    CoeFun (Measurement Ω E) fun _ => ∀ s : Set Ω, MeasurableSet s → Effect E
```

**`PhyslibAlpha.ProbabilisticTheory.Measurement.coe_apply`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean#L80).

```lean
lemma coe_apply (M : Measurement Ω E) (s : Set Ω) (hs : MeasurableSet s) :
    (M s hs : E) = M.toChannel (BoundedMeasurable.indicator s hs)
```

**`PhyslibAlpha.ProbabilisticTheory.Measurement.toEffectValuedMeasure`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean#L84).

> The effects of the events of a measurement form an effect-valued measure.

```lean
noncomputable def toEffectValuedMeasure (M : Measurement Ω E) : EffectValuedMeasure Ω E
```

**`PhyslibAlpha.ProbabilisticTheory.Measurement.toEffectValuedMeasure_apply`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean#L88).

```lean
lemma toEffectValuedMeasure_apply (M : Measurement Ω E) (s : Set Ω) (hs : MeasurableSet s) :
    M.toEffectValuedMeasure s hs = M s hs
```

**`PhyslibAlpha.ProbabilisticTheory.Measurement.map_empty`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean#L92).

```lean
lemma map_empty (M : Measurement Ω E) : M ∅ .empty = 0
```

**`PhyslibAlpha.ProbabilisticTheory.Measurement.map_univ`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean#L95).

```lean
lemma map_univ (M : Measurement Ω E) : M .univ .univ = 1
```

## B. The Born law

**`PhyslibAlpha.ProbabilisticTheory.Measurement.isNormal_comp`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean#L99).

```lean
lemma isNormal_comp (M : Measurement Ω E) {ω : 𝓢[ℝ, E]} (hω : ω.IsNormal) :
    (ω.comp M.toChannel).IsNormal
```

**`PhyslibAlpha.ProbabilisticTheory.Measurement.probabilityLaw`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean#L104).

> The Born law: the distribution of the outcome of `M` in the normal state `ω`.

```lean
noncomputable def probabilityLaw (M : Measurement Ω E) (ω : 𝓢[ℝ, E]) (hω : ω.IsNormal) :
    ProbabilityMeasure Ω
```

**`PhyslibAlpha.ProbabilisticTheory.Measurement.probabilityLaw_apply`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean#L109).

```lean
lemma probabilityLaw_apply (M : Measurement Ω E) (ω : 𝓢[ℝ, E]) (hω : ω.IsNormal)
    (s : Set Ω) (hs : MeasurableSet s) :
    (M.probabilityLaw ω hω : Measure Ω) s = ENNReal.ofReal (ω (M s hs))
```

**`PhyslibAlpha.ProbabilisticTheory.Measurement.integral_probabilityLaw`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean#L116).

> The average of an observable `f` of the outcome under the Born law is the expectation of
> `M f`.

```lean
lemma integral_probabilityLaw (M : Measurement Ω E) (ω : 𝓢[ℝ, E]) (hω : ω.IsNormal)
    (f : BoundedMeasurable Ω) : ∫ x, f x ∂(M.probabilityLaw ω hω : Measure Ω) = ω (M.toChannel f)
```

**`PhyslibAlpha.ProbabilisticTheory.Measurement.probabilityLaw_eq`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean#L121).

> The Born law of a measurement is the Born law of its effect-valued measure.

```lean
lemma probabilityLaw_eq (M : Measurement Ω E) (ω : 𝓢[ℝ, E]) (hω : ω.IsNormal) :
    M.probabilityLaw ω hω = M.toEffectValuedMeasure.probabilityLaw ω hω
```

## C. Measuring after a channel

**`PhyslibAlpha.ProbabilisticTheory.Measurement.map`**, a def, [line 131](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean#L131).

> Measuring `M` after the normal channel `φ`: the outcome observables go through `M`, then
> through `φ`.

```lean
def map (M : Measurement Ω E) (φ : Channel E F) (hφ : φ.IsNormal) : Measurement Ω F
```

**`PhyslibAlpha.ProbabilisticTheory.Measurement.coe_map_apply`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean#L136).

```lean
lemma coe_map_apply (M : Measurement Ω E) (φ : Channel E F) (hφ : φ.IsNormal) (s : Set Ω)
    (hs : MeasurableSet s) : (M.map φ hφ s hs : F) = φ (M s hs)
```

**`BoundedMeasurable.outcome`**, a def, [line 151](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean#L151).

> Measuring the outcome of a classical system.

```lean
def outcome : Measurement Ω (BoundedMeasurable Ω)
```

**`BoundedMeasurable.coe_outcome_apply`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean#L156).

```lean
lemma coe_outcome_apply (s : Set Ω) (hs : MeasurableSet s) :
    (outcome s hs : BoundedMeasurable Ω) = BoundedMeasurable.indicator s hs
```

**`BoundedMeasurable.probabilityLaw_outcome`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean#L160).

> The outcome of a classical system in a normal state is distributed by the state.

```lean
lemma probabilityLaw_outcome (ω : 𝓢[ℝ, BoundedMeasurable Ω]) (hω : ω.IsNormal) :
    outcome.probabilityLaw ω hω = toMeasure ω hω
```

## Depends on

- [States of a classical system](../classical/normalstates.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Measurement/Basic.lean)
