---
declaration: module
origin: cited
lean: ProbabilisticTheory.Measurement.Compatible, ProbabilisticTheory.Measurement.compatible_refl, ProbabilisticTheory.Measurement.compatible_symm, ProbabilisticTheory.Measurement.Compatible.mono, ProbabilisticTheory.Measurement.compatible_of_postprocessing_left, ProbabilisticTheory.Measurement.compatible_of_postprocessing_right, ProbabilisticTheory.Measurement.Joint, ProbabilisticTheory.Measurement.JointlyMeasurable
statement: formalized
proof: formalized
---

# Compatibility of measurements

The module `PhyslibAlpha.ProbabilisticTheory.Measurement.Compatibility`, [PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean): 25 declarations, 20 with a docstring.

> Compatible and jointly measurable measurements, with an order criterion for binary ones.

## i. Overview

> Two measurements are compatible when both can be obtained from one measurement by classical
> post-processing of its outcome: performing the common measurement answers both.
>
> A joint measurement of two measurements is a measurement of pairs of outcomes whose marginals are
> the two measurements. Jointly measurable measurements are compatible. The binary measurements of
> two effects `e` and `f` are jointly measurable exactly when some `g` lies above `0` and `e + f - 1`
> and below `e` and `f`: `g` is the effect of both outcomes being `true`.

## ii. Key results

> - `Measurement.Compatible` : compatibility of measurements.
> - `Measurement.Compatible.mono` : compatibility is preserved by post-processing.
> - `Measurement.Joint` : a joint measurement of two measurements.
> - `Measurement.JointlyMeasurable.compatible` : jointly measurable measurements are
>   compatible.
> - `Effect.jointlyMeasurable_binaryMeasurement_iff` : the order criterion for joint measurability of
>   two binary measurements.

## iv. References

> * None.

## A. Compatibility of measurements

**`ProbabilisticTheory.Measurement.Compatible`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L68).

> Two measurements are compatible when they are both operational post-processings of a common
> measurement.

```lean
def Compatible (M : Measurement Ω E) (N : Measurement Ω' E) : Prop
```

**`ProbabilisticTheory.Measurement.compatible_refl`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L72).

> Every measurement is compatible with itself.

```lean
lemma compatible_refl (M : Measurement Ω E) : Compatible M M
```

**`ProbabilisticTheory.Measurement.compatible_symm`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L76).

> Compatibility of measurements is symmetric.

```lean
lemma compatible_symm {M : Measurement Ω E} {N : Measurement Ω' E}
    (h : Compatible M N) : Compatible N M
```

**`ProbabilisticTheory.Measurement.Compatible.mono`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L82).

> Replacing compatible measurements by post-processings preserves compatibility.

```lean
lemma Compatible.mono {M : Measurement Ω E} {N : Measurement Ω' E}
    {M' : Measurement Ω₁ E} {N' : Measurement Ω₂ E} (h : Compatible M N)
    (hM : M' ≤ₚ M) (hN : N' ≤ₚ N) : Compatible M' N'
```

**`ProbabilisticTheory.Measurement.compatible_of_postprocessing_left`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L89).

> A measurement is compatible with each of its operational post-processings.

```lean
lemma compatible_of_postprocessing_left {M : Measurement Ω E}
    {N : Measurement Ω' E} (h : M ≤ₚ N) : Compatible M N
```

**`ProbabilisticTheory.Measurement.compatible_of_postprocessing_right`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L94).

> A measurement is compatible with each measurement of which it is a post-processing.

```lean
lemma compatible_of_postprocessing_right {M : Measurement Ω E}
    {N : Measurement Ω' E} (h : N ≤ₚ M) : Compatible M N
```

## B. Joint measurements

**`ProbabilisticTheory.Measurement.Joint`**, a structure, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L112).

> A joint measurement of `M` and `N`: a measurement with outcome pairs whose marginals are `M`
> and `N`.

```lean
structure Joint (M : Measurement Ω E) (N : Measurement Ω' E) where
  /-- The joint measurement. -/
  joint : Measurement (Ω × Ω') E
  /-- Its first marginal is `M`. -/
  fst_marginal : joint.mapOutcome Prod.fst measurable_fst = M
  /-- Its second marginal is `N`. -/
  snd_marginal : joint.mapOutcome Prod.snd measurable_snd = N
```

**`ProbabilisticTheory.Measurement.JointlyMeasurable`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L121).

> Two measurements are jointly measurable when they have a joint measurement.

```lean
def JointlyMeasurable (M : Measurement Ω E) (N : Measurement Ω' E) : Prop
```

**`ProbabilisticTheory.Measurement.JointlyMeasurable.compatible`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L125).

> Jointly measurable measurements are compatible.

```lean
lemma JointlyMeasurable.compatible {M : Measurement Ω E}
    {N : Measurement Ω' E} (h : JointlyMeasurable M N) : Compatible M N
```

## C. Binary compatibility

**`ProbabilisticTheory.Effect.binaryJointAtom`**, a def, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L145).

> The four effects of a joint measurement of the binary measurements of `e` and `f` whose
> `(true, true)` effect is `g`.

```lean
def binaryJointAtom (e f : Effect E) (g : E) : Bool × Bool → E
```

**`ProbabilisticTheory.Effect.IsBinaryJointEffect`**, a def, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L152).

> Conditions on `g` making every `binaryJointAtom e f g` an effect.

```lean
def IsBinaryJointEffect (e f : Effect E) (g : E) : Prop
```

**`ProbabilisticTheory.Effect.IsApproxBinaryJointEffect`**, a def, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L156).

> `g` is a joint effect for `e` and `f` up to `δ • 1`.

```lean
def IsApproxBinaryJointEffect (e f : Effect E) (δ : ℝ) (g : E) : Prop
```

**`ProbabilisticTheory.Effect.IsBinaryJointEffect.isApprox`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L159).

```lean
lemma IsBinaryJointEffect.isApprox {e f : Effect E} {g : E} (hg : IsBinaryJointEffect e f g)
    {δ : ℝ} (hδ : 0 ≤ δ) : IsApproxBinaryJointEffect e f δ g
```

**`ProbabilisticTheory.Effect.binaryJointAtom_mem`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L166).

```lean
lemma binaryJointAtom_mem {e f : Effect E} {g : E} (hg : IsBinaryJointEffect e f g) :
    ∀ p, binaryJointAtom e f g p ∈ (Effect E : Set E)
```

**`ProbabilisticTheory.Effect.sum_binaryJointAtom`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L178).

```lean
lemma sum_binaryJointAtom (e f : Effect E) (g : E) : ∑ p, binaryJointAtom e f g p = 1
```

**`ProbabilisticTheory.Effect.binaryJoint`**, a def, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L193).

> The joint measurement of the binary measurements of `e` and `f` with `(true, true)` effect
> `g`.

```lean
noncomputable def binaryJoint {e f : Effect E} {g : E} (hg : IsBinaryJointEffect e f g) :
    Joint (binaryMeasurement e) (binaryMeasurement f)
```

**`ProbabilisticTheory.Measurement.Joint.jointAtom`**, a def, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L215).

> The effect of the joint outcome `p`.

```lean
noncomputable def _root_.ProbabilisticTheory.Measurement.Joint.jointAtom
    (J : Joint (binaryMeasurement e) (binaryMeasurement f)) (p : Bool × Bool) : E
```

**`ProbabilisticTheory.Measurement.Joint.jointAtom_nonneg`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L221).

```lean
lemma _root_.ProbabilisticTheory.Measurement.Joint.jointAtom_nonneg (p : Bool × Bool) :
    0 ≤ J.jointAtom p
```

**`ProbabilisticTheory.Measurement.Joint.coe_joint_eq_sum`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L226).

```lean
lemma _root_.ProbabilisticTheory.Measurement.Joint.coe_joint_eq_sum (s : Set (Bool × Bool))
    (hs : MeasurableSet s) :
    (J.joint s hs : E) = ∑ p, if p ∈ s then J.jointAtom p else 0
```

**`ProbabilisticTheory.Measurement.Joint.jointAtom_fst`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L233).

> The first marginal: the joint outcomes with first entry `true` add up to `e`.

```lean
lemma _root_.ProbabilisticTheory.Measurement.Joint.jointAtom_fst :
    J.jointAtom (true, true) + J.jointAtom (true, false) = e
```

**`ProbabilisticTheory.Measurement.Joint.jointAtom_snd`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L242).

> The second marginal: the joint outcomes with second entry `true` add up to `f`.

```lean
lemma _root_.ProbabilisticTheory.Measurement.Joint.jointAtom_snd :
    J.jointAtom (true, true) + J.jointAtom (false, true) = f
```

**`ProbabilisticTheory.Measurement.Joint.jointAtom_sum`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L251).

> The four joint outcomes add up to the unit.

```lean
lemma _root_.ProbabilisticTheory.Measurement.Joint.jointAtom_sum :
    J.jointAtom (true, true) + J.jointAtom (true, false) +
    (J.jointAtom (false, true) + J.jointAtom (false, false)) = 1
```

**`ProbabilisticTheory.Measurement.Joint.isBinaryJointEffect_jointAtom`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L260).

> The `(true, true)` effect of a joint measurement of two binary measurements satisfies the
> joint-effect conditions.

```lean
lemma _root_.ProbabilisticTheory.Measurement.Joint.isBinaryJointEffect_jointAtom :
    IsBinaryJointEffect e f (J.jointAtom (true, true))
```

**`ProbabilisticTheory.Effect.jointlyMeasurable_binaryMeasurement_iff`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L277).

> The binary measurements of `e` and `f` are jointly measurable exactly when some `g` lies below
> `e` and `f` and above `0` and `e + f - 1`.

```lean
lemma jointlyMeasurable_binaryMeasurement_iff (e f : Effect E) :
    JointlyMeasurable (binaryMeasurement e) (binaryMeasurement f) ↔
      ∃ g : E, IsBinaryJointEffect e f g
```

**`ProbabilisticTheory.Effect.compatible_binaryMeasurement`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean#L283).

> Binary measurements of effects with a common lower bound as above are compatible.

```lean
lemma compatible_binaryMeasurement {e f : Effect E} {g : E} (hg : IsBinaryJointEffect e f g) :
    Compatible (binaryMeasurement e) (binaryMeasurement f)
```

## Depends on

- [Binary measurements](binary.md)
- [Post-processing of measurements](postprocessing.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Measurement/Compatibility.lean)
