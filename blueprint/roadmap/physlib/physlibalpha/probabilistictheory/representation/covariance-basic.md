---
declaration: module
origin: cited
lean: ProbabilisticTheory.Symmetry.instSMulEffect, ProbabilisticTheory.Symmetry.coe_smul_effect, ProbabilisticTheory.Symmetry.instMulActionEffect, ProbabilisticTheory.MeasurableAction, ProbabilisticTheory.measurableSet_smul, ProbabilisticTheory.EffectValuedMeasure.IsCovariant, ProbabilisticTheory.UnitalPositiveLinearMap.IsCovariant, ProbabilisticTheory.UnitalPositiveLinearMap.isCovariant_id
statement: formalized
proof: formalized
---

# Covariant measurements and channels

The module `PhyslibAlpha.ProbabilisticTheory.Representation.Covariance.Basic`, [PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Basic.lean): 9 declarations, 7 with a docstring.

> Symmetries acting on effects, measurable actions on outcomes, covariant measures and channels.

## i. Overview

> A measurement is covariant under a symmetry group when transforming the outcome transforms the
> effect: `μ (g • S) = ρ g • μ S`. A symmetry acts on effects, a group acts on outcomes by measurable
> bijections, and a channel is covariant when it intertwines two symmetry actions.

## ii. Key results

> - `Symmetry.instSMulEffect` : symmetries act on effects.
> - `MeasurableAction` : a group acting on outcomes by measurable bijections.
> - `EffectValuedMeasure.IsCovariant` : covariant effect-valued measures.
> - `UnitalPositiveLinearMap.IsCovariant` : covariant channels.

## iv. References

> * None.

**`ProbabilisticTheory.Symmetry.instSMulEffect`**, an instance, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Basic.lean#L53).

> A symmetry acts on effects the way it acts on `E` itself, via the underlying channel — the
> dual of `Symmetry`'s existing action on states.

```lean
instance Symmetry.instSMulEffect : SMul (Symmetry E) (Effect E)
```

**`ProbabilisticTheory.Symmetry.coe_smul_effect`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Basic.lean#L56).

```lean
lemma Symmetry.coe_smul_effect (φ : Symmetry E) (e : Effect E) :
    ((φ • e : Effect E) : E) = φ.1 (e : E)
```

**`ProbabilisticTheory.Symmetry.instMulActionEffect`**, an instance, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Basic.lean#L59).

```lean
instance Symmetry.instMulActionEffect : MulAction (Symmetry E) (Effect E)
```

**`ProbabilisticTheory.MeasurableAction`**, a class, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Basic.lean#L70).

> `G` acts on the measurable space `Ω`, and every group element moves points measurably. Since
> this holds for `g` and `g⁻¹` both, the action is by measurable *bijections*: `MeasurableSet.smul`
> below shows it moves measurable sets to measurable sets, not merely points.

```lean
class MeasurableAction (G Ω : Type*) [Group G] [MeasurableSpace Ω] [MulAction G Ω] : Prop where
  /-- Every group element acts as a measurable map. -/
  measurable_smul : ∀ g : G, Measurable (fun x : Ω => g • x)
```

**`ProbabilisticTheory.measurableSet_smul`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Basic.lean#L78).

> The image of a measurable set under the action of a group element is again measurable:
> `g • S` is the preimage of `S` under the (measurable) action of `g⁻¹`.

```lean
lemma measurableSet_smul {S : Set Ω} (hS : MeasurableSet S) (g : G) : MeasurableSet (g • S)
```

**`ProbabilisticTheory.EffectValuedMeasure.IsCovariant`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Basic.lean#L102).

> A measurement (POVM) `μ` is **covariant** under an action of `G` on the outcome space,
> transported to the physical system via `ρ : G →* Symmetry E`, when transforming the outcome set
> and transforming the assigned effect agree: `μ(g • S) = ρ(g) • μ(S)`. This is the abstract form of
> `E(gS) = α_g(E(S))` — a rotated detector pointed at a rotated direction reads out what a rotation
> of the original detector would have.

```lean
def EffectValuedMeasure.IsCovariant (ρ : G →* Symmetry E) (μ : EffectValuedMeasure Ω E) : Prop
```

## A. Covariant channels: the general intertwiner picture

> A channel between two systems is covariant when transporting the input and transporting the
> output agree: the channel intertwines the two actions.

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsCovariant`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Basic.lean#L120).

> A channel `φ : Channel E₁ E₂` is **covariant** under symmetry actions `ρ₁`, `ρ₂` of `G` on the
> two systems when transporting the input along `ρ₁ g` then applying `φ`, or applying `φ` then
> transporting the output along `ρ₂ g`, agree — the channel intertwines the two actions.

```lean
def UnitalPositiveLinearMap.IsCovariant (ρ₁ : G →* Symmetry E₁) (ρ₂ : G →* Symmetry E₂)
    (φ : Channel E₁ E₂) : Prop
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.isCovariant_id`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Basic.lean#L126).

> The identity channel is covariant under any action of `G`, against itself: it trivially
> intertwines an action with itself.

```lean
lemma UnitalPositiveLinearMap.isCovariant_id (ρ : G →* Symmetry E₁) :
    (UnitalPositiveLinearMap.id ℝ E₁).IsCovariant ρ ρ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsCovariant.comp`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Basic.lean#L132).

> Covariance is preserved by composition: a covariant channel followed by a covariant channel is
> covariant for the actions at the two ends, with the middle system's action cancelling out.

```lean
lemma UnitalPositiveLinearMap.IsCovariant.comp {ρ₁ : G →* Symmetry E₁} {ρ₂ : G →* Symmetry E₂}
    {ρ₃ : G →* Symmetry E₃} {ψ : Channel E₂ E₃} {φ : Channel E₁ E₂}
    (hψ : ψ.IsCovariant ρ₂ ρ₃) (hφ : φ.IsCovariant ρ₁ ρ₂) :
    (ψ.comp φ).IsCovariant ρ₁ ρ₃
```

## Depends on

- [Symmetries](../channel/symmetry.md)
- [Pushing an effect-valued measure forward along a channel](../measurement/pushforward.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Basic.lean)
