---
declaration: module
origin: cited
lean: ProbabilisticTheory.Preparation.IsTrivial, ProbabilisticTheory.Preparation.isTrivial_of_effect, ProbabilisticTheory.Preparation.conditionalState_eq_of_isPure, ProbabilisticTheory.Preparation.setIntegral_prepare_of_isPure, ProbabilisticTheory.Preparation.isTrivial_of_isPure, ProbabilisticTheory.UnitalPositiveLinearMap.isPure_of_isTrivial, ProbabilisticTheory.UnitalPositiveLinearMap.isPure_iff_forall_isTrivial, ProbabilisticTheory.Preparation.NoSideInfo
statement: formalized
proof: formalized
---

# Purity is the absence of side information

The module `PhyslibAlpha.ProbabilisticTheory.State.PureMeasurement`, [PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean): 19 declarations, 19 with a docstring.

> A normal state is pure exactly when no preparation of it carries side information.

## i. Overview

> Roll a die and, depending on the roll, prepare a state; then perform a measurement. Someone who is
> only told the prepared state predicts the outcome with its Born law. Someone who is also told how
> the state was prepared, and sees the roll, may predict better: the roll is side information. It is
> useless exactly when the roll and the outcome are independent random variables.
>
> **A state is pure exactly when it has no side information:** however it is prepared, the roll and
> the outcome of any yes/no measurement are independent. Being handed the state is as good as being
> handed the state together with the procedure that prepared it. Conversely, every mixed state can be
> prepared by choosing between two states in such a way that some yes/no measurement detects the
> choice. For a pure state, the roll is also independent of the outcome of any measurement with a
> countably generated outcome space.
>
> Behind this lies a sharper statement: a state is pure exactly when every preparation of it is
> trivial, with every expectation value almost surely independent of the roll.

## ii. Key results

> - `Preparation.NoSideInfo` : the roll and the outcome of a measurement are independent.
> - `UnitalPositiveLinearMap.HasNoSideInfo` : however the state is prepared, the roll and the outcome
>   of any yes/no measurement are independent.
> - `UnitalPositiveLinearMap.isPure_iff_hasNoSideInfo` : a normal state is pure exactly when it has
>   no side information.
> - `UnitalPositiveLinearMap.isMixed_iff_exists_sideInfo` : a normal state is mixed exactly when it
>   can be prepared from two states so that some yes/no measurement detects the choice.
> - `Preparation.noSideInfo_of_isPure` : preparing a pure state, the roll is independent of the
>   outcome of every measurement with a countably generated outcome space.
> - `Preparation.noSideInfo_iff_postprocessEquivAE` : no side information means that the outcome law
>   given the roll is no more informative than the outcome law ignoring it.

## iv. References

> * None.

## A. Trivial preparations

**`ProbabilisticTheory.Preparation.IsTrivial`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean#L80).

> A preparation is trivial when, for every observable, almost every roll prepares a state with
> the same expectation value as the prepared state.

```lean
def IsTrivial (p : Preparation E X) : Prop
```

**`ProbabilisticTheory.Preparation.isTrivial_of_effect`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean#L84).

> A preparation is trivial as soon as it is trivial on effects.

```lean
lemma isTrivial_of_effect (p : Preparation E X)
    (h : ∀ e : Effect E, ∀ᵐ x ∂(p.law : Measure X), p.prepare x e = p.state e) :
    p.IsTrivial
```

## B. Preparations of pure states

**`ProbabilisticTheory.Preparation.conditionalState_eq_of_isPure`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean#L97).

> Conditioning a preparation of a pure state on an event whose probability is neither `0` nor `1`
> gives back the pure state.

```lean
lemma conditionalState_eq_of_isPure (p : Preparation E X) (hω : p.state.IsPure) {s : Set X}
    (hs : MeasurableSet s) (hpos : 0 < (p.law : Measure X).real s)
    (hposc : 0 < (p.law : Measure X).real sᶜ) : p.conditionalState s hpos = p.state
```

**`ProbabilisticTheory.Preparation.setIntegral_prepare_of_isPure`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean#L107).

> Preparing a pure state, the expectation value restricted to any event of rolls is the
> probability of the event times the expectation value.

```lean
lemma setIntegral_prepare_of_isPure (p : Preparation E X) (hω : p.state.IsPure) {s : Set X}
    (hs : MeasurableSet s) (A : E) :
    ∫ x in s, p.prepare x A ∂(p.law : Measure X) = (p.law : Measure X).real s * p.state A
```

**`ProbabilisticTheory.Preparation.isTrivial_of_isPure`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean#L126).

> Every preparation of a pure state is trivial.

```lean
lemma isTrivial_of_isPure (p : Preparation E X) (hω : p.state.IsPure) : p.IsTrivial
```

## C. Pure states from trivial preparations

**`ProbabilisticTheory.UnitalPositiveLinearMap.isPure_of_isTrivial`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean#L139).

> A normal state all of whose preparations from two states are trivial is pure.

```lean
lemma isPure_of_isTrivial (hω : ω.IsNormal)
    (h : ∀ p : Preparation E Bool, p.state = ω → p.IsTrivial) : ω.IsPure
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.isPure_iff_forall_isTrivial`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean#L149).

> A normal state is pure exactly when all its preparations are trivial.

```lean
lemma isPure_iff_forall_isTrivial (hω : ω.IsNormal) :
    ω.IsPure ↔ ∀ (X : Type) [MeasurableSpace X] (p : Preparation E X), p.state = ω →
      p.IsTrivial
```

## D. Side information

**`ProbabilisticTheory.Preparation.NoSideInfo`**, a def, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean#L163).

> The roll carries no side information about the measurement `M`: the roll and the outcome of `M`
> are independent random variables.

```lean
def NoSideInfo (p : Preparation E X) (M : Measurement Ω E) : Prop
```

**`ProbabilisticTheory.Preparation.noSideInfo_iff_compProd_eq`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean#L168).

> The roll carries no side information about `M` exactly when the joint law of roll and outcome
> is the one obtained by ignoring the roll.

```lean
lemma noSideInfo_iff_compProd_eq (p : Preparation E X) (M : Measurement Ω E) :
    p.NoSideInfo M ↔
      (p.law : Measure X) ⊗ₘ p.outcome M = (p.law : Measure X) ⊗ₘ p.forgetfulOutcome M
```

**`ProbabilisticTheory.Preparation.noSideInfo_of_ae_eq`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean#L179).

> If the outcome law given the roll almost surely ignores the roll, the roll carries no side
> information.

```lean
lemma noSideInfo_of_ae_eq (p : Preparation E X) {M : Measurement Ω E}
    (h : p.outcome M =ᵐ[(p.law : Measure X)] p.forgetfulOutcome M) : p.NoSideInfo M
```

**`ProbabilisticTheory.Preparation.noSideInfo_iff_ae_eq`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean#L185).

> With a countably generated outcome space, the roll carries no side information exactly when the
> outcome law given the roll almost surely ignores the roll.

```lean
lemma noSideInfo_iff_ae_eq [MeasurableSpace.CountablyGenerated Ω] (p : Preparation E X)
    (M : Measurement Ω E) :
    p.NoSideInfo M ↔ p.outcome M =ᵐ[(p.law : Measure X)] p.forgetfulOutcome M
```

**`ProbabilisticTheory.Preparation.noSideInfo_iff_postprocessEquivAE`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean#L193).

> With a countably generated outcome space, the roll carries no side information exactly when the
> outcome law given the roll is no more informative than the outcome law ignoring it.

```lean
lemma noSideInfo_iff_postprocessEquivAE [MeasurableSpace.CountablyGenerated Ω]
    (p : Preparation E X) (M : Measurement Ω E) :
    p.NoSideInfo M ↔
      Kernel.MutuallyFactorAE (p.law : Measure X) (p.outcome M) (p.forgetfulOutcome M)
```

**`ProbabilisticTheory.Preparation.IsTrivial.outcome_ae_eq`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean#L205).

> In a trivial preparation, the outcome law of a measurement with a countably generated outcome
> space almost surely ignores the roll.

```lean
lemma IsTrivial.outcome_ae_eq [MeasurableSpace.CountablyGenerated Ω] {p : Preparation E X}
    (h : p.IsTrivial) (M : Measurement Ω E) :
    p.outcome M =ᵐ[(p.law : Measure X)] p.forgetfulOutcome M
```

**`ProbabilisticTheory.Preparation.ae_prepare_eq_of_noSideInfo`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean#L215).

> If the roll carries no side information about the yes/no measurement of `e`, almost every roll
> predicts the probability of `e` in the prepared state.

```lean
lemma ae_prepare_eq_of_noSideInfo (p : Preparation E X) (e : Effect E)
    (h : p.NoSideInfo (Effect.binaryMeasurement e)) :
    ∀ᵐ x ∂(p.law : Measure X), p.prepare x e = p.state e
```

**`ProbabilisticTheory.Preparation.isTrivial_iff_noSideInfo`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean#L227).

> A preparation is trivial exactly when the roll carries no side information about any yes/no
> measurement.

```lean
lemma isTrivial_iff_noSideInfo (p : Preparation E X) :
    p.IsTrivial ↔ ∀ e : Effect E, p.NoSideInfo (Effect.binaryMeasurement e)
```

**`ProbabilisticTheory.Preparation.noSideInfo_of_isPure`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean#L234).

> Preparing a pure state, the roll carries no side information about any measurement with a
> countably generated outcome space.

```lean
lemma noSideInfo_of_isPure [MeasurableSpace.CountablyGenerated Ω] (p : Preparation E X)
    (hω : p.state.IsPure) (M : Measurement Ω E) : p.NoSideInfo M
```

## E. Purity is the absence of side information

**`ProbabilisticTheory.UnitalPositiveLinearMap.HasNoSideInfo`**, a def, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean#L248).

> A state has no side information when, however it is prepared, the roll and the outcome of any
> yes/no measurement are independent.

```lean
def HasNoSideInfo (ω : 𝓢[ℝ, E]) : Prop
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.isPure_iff_hasNoSideInfo`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean#L255).

> **Purity is the absence of side information.** A normal state is pure exactly when, however it
> is prepared, the roll and the outcome of any yes/no measurement are independent: knowing how the
> state was prepared never helps to predict a measurement.

```lean
lemma isPure_iff_hasNoSideInfo (hω : ω.IsNormal) : ω.IsPure ↔ ω.HasNoSideInfo
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.isMixed_iff_exists_sideInfo`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean#L260).

> **A mixed state leaks side information.** A normal state is mixed exactly when it can be
> prepared by choosing between two states so that some yes/no measurement detects the choice.

```lean
lemma isMixed_iff_exists_sideInfo (hω : ω.IsNormal) :
    ω.IsMixed ↔ ∃ p : Preparation E Bool, p.state = ω ∧
      ∃ e : Effect E, ¬ p.NoSideInfo (Effect.binaryMeasurement e)
```

## Depends on

- [Binary measurements](../measurement/binary.md)
- [Preparation procedures](preparation.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/PureMeasurement.lean)
