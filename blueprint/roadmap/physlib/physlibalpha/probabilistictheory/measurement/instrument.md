---
declaration: module
origin: cited
lean: ProbabilisticTheory.Instrument, ProbabilisticTheory.Instrument.measurement, ProbabilisticTheory.Instrument.coe_measurement_effects, ProbabilisticTheory.Instrument.conditionalState, ProbabilisticTheory.Instrument.conditionalState_apply, ProbabilisticTheory.Instrument.conditionalState_isNormal
statement: formalized
proof: formalized
---

# Instruments

The module `PhyslibAlpha.ProbabilisticTheory.Measurement.Instrument`, [PhyslibAlpha/ProbabilisticTheory/Measurement/Instrument.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Instrument.lean): 6 declarations, 5 with a docstring.

> Finite-outcome instruments, their induced measurements and post-measurement states.

## i. Overview

> An instrument with finitely many outcomes describes both the outcome probabilities and the state
> after the measurement. It is a family of operations, one per outcome, whose values on the unit sum
> to `1`. Forgetting the post-measurement state gives a measurement, and conditioning a state on an
> outcome of nonzero probability gives the post-measurement state.

## ii. Key results

> - `Instrument` : finite-outcome instruments.
> - `Instrument.measurement` : the underlying measurement.
> - `Instrument.conditionalState` : the post-measurement state.

## iv. References

> * None.

## A. Instruments

**`ProbabilisticTheory.Instrument`**, a structure, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Instrument.lean#L52).

> A finite-outcome instrument: an operation for each outcome, whose images of the certain event
> exhaust it. The instrument loses no probability overall, even though a single operation may.

```lean
structure Instrument (E : Type*) [OrderUnitSpace E] (ι : Type*) [Fintype ι] where
  /-- The operation associated to each possible outcome. -/
  op : ι → Operation E
  /-- The outcome probabilities exhaust the certain event. -/
  sum_op_one_eq_one : ∑ i, (op i : E → E) 1 = 1
```

## B. The induced measurement

**`ProbabilisticTheory.Instrument.measurement`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Instrument.lean#L68).

> The measurement an instrument induces: only the outcome probabilities remain, given by each
> operation's image of the certain event.

```lean
noncomputable def measurement (𝓘 : Instrument E ι) : Measurement ι E
```

**`ProbabilisticTheory.Instrument.coe_measurement_effects`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Instrument.lean#L72).

> The effect of an outcome is the value of its operation on the unit.

```lean
lemma coe_measurement_effects (𝓘 : Instrument E ι) (i : ι) :
    ((𝓘.measurement {i} (measurableSet_singleton i) : Effect E) : E) =
      (𝓘.op i : E → E) 1
```

## C. Conditional states

**`ProbabilisticTheory.Instrument.conditionalState`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Instrument.lean#L84).

> The post-measurement (conditional) state after outcome `i`, given a prior state `ω` for which
> that outcome has nonzero probability: apply the operation, then renormalize by the outcome's
> probability, so the certain event is again sent to `1`.

```lean
noncomputable def conditionalState (𝓘 : Instrument E ι) (i : ι) (ω : 𝓢[ℝ, E])
    (hpos : 0 < ω ((𝓘.op i : E → E) 1)) : 𝓢[ℝ, E]
```

**`ProbabilisticTheory.Instrument.conditionalState_apply`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Instrument.lean#L89).

```lean
lemma conditionalState_apply (𝓘 : Instrument E ι) (i : ι) (ω : 𝓢[ℝ, E])
    (hpos : 0 < ω ((𝓘.op i : E → E) 1)) (a : E) :
    𝓘.conditionalState i ω hpos a =
      (ω ((𝓘.op i : E → E) 1))⁻¹ * ω ((𝓘.op i : E → E) a)
```

**`ProbabilisticTheory.Instrument.conditionalState_isNormal`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Instrument.lean#L97).

> A normal instrument operation sends a normal input state to a normal conditional state,
> whenever its outcome has nonzero probability.

```lean
lemma conditionalState_isNormal (𝓘 : Instrument E ι) (i : ι) (ω : 𝓢[ℝ, E])
    (hpos : 0 < ω ((𝓘.op i : E → E) 1)) (hOp : (𝓘.op i).IsNormal) (hω : ω.IsNormal) :
    (𝓘.conditionalState i ω hpos).IsNormal
```

## Depends on

- [Operations](../channel/operation.md)
- [Measurements with finitely many outcomes](finite.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Measurement/Instrument.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Instrument.lean)
