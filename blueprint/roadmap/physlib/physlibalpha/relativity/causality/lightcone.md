---
declaration: module
origin: cited
lean: Minkowski.causallyFollows_iff_displacement, Minkowski.causallyFollows_iff_norm, Minkowski.causalRelation, Minkowski.norm_space_eq_spatialPart, Minkowski.precedes_iff_time_space, Minkowski.isClosed_causalFuture_zero, Minkowski.causalFuture_eq_add, Minkowski.isClosed_causalFuture
statement: formalized
proof: formalized
---

# Light cones in time and space

The module `PhyslibAlpha.Relativity.Causality.LightCone`, [PhyslibAlpha/Relativity/Causality/LightCone.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Causality/LightCone.lean): 17 declarations, 17 with a docstring.

> Causal future and past of sets in time and space and in Minkowski spacetime.

## i. Overview

> Causal future and past of sets in time and space and in Minkowski spacetime. Causal futures of
> compact sets are closed and causal diamonds are compact.

## ii. Key results

> - `causalFuture` : The causal future of a set of spacetime points, in units where the speed of light
>   is `1`.
> - `causalPast` : The causal past of a set of spacetime points.
> - `precedes_iff_time_space` : In any speed-of-light units the existing geometric causal relation has
>   the familiar elapsed-time and spatial-distance characterization.
> - `causallyFollows_iff_norm` : The existing Lorentzian causal order is equivalently the spatial norm
>   bounded by elapsed Lorentz time.

## iv. References

> None.

## A. Minkowski causal geometry for Green operators

> Lemmas: `causallyFollows_iff_displacement`, `causallyFollows_iff_norm`, `norm_space_eq_spatialPart`,
> `precedes_iff_time_space`, `isClosed_causalFuture_zero`, `causalFuture_eq_add`,
> `isClosed_causalFuture`, `causalPast_eq_add_neg`, `isClosed_causalPast`,
> `component_bound_of_causalDiamond` and more.

## B. Causal support of the retarded solution

> - `causalFuture` : The causal future of a set of spacetime points, in units where the speed of light
>   is `1`.
> - `causalPast` : The causal past of a set of spacetime points.
>
> Lemmas: `isClosed_causalFuture`.

**`Minkowski.causallyFollows_iff_displacement`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Causality/LightCone.lean#L74).

> Causal precedence depends only on the displacement between events.

```lean
lemma causallyFollows_iff_displacement (p q : SpaceTime d) :
    causallyFollows p q ↔ causallyFollows 0 (q - p)
```

**`Minkowski.causallyFollows_iff_norm`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Causality/LightCone.lean#L81).

> The existing Lorentzian causal order is equivalently the spatial norm bounded by elapsed
> Lorentz time. Nonnegative elapsed time follows from this inequality.

```lean
lemma causallyFollows_iff_norm (p q : SpaceTime d) :
    causallyFollows p q ↔ ‖(q - p).spatialPart‖ ≤ (q - p).timeComponent
```

**`Minkowski.causalRelation`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Causality/LightCone.lean#L94).

> Minkowski causal geometry reuses the existing Lorentzian future relation.

```lean
def causalRelation (d : ℕ) : CausalRelation (SpaceTime d)
```

**`Minkowski.norm_space_eq_spatialPart`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Causality/LightCone.lean#L110).

> Physlib's physical-space norm agrees with the Euclidean norm of the Lorentz spatial part.

```lean
lemma norm_space_eq_spatialPart (p : SpaceTime d) : ‖p.space‖ = ‖p.spatialPart‖
```

**`Minkowski.precedes_iff_time_space`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Causality/LightCone.lean#L117).

> In any speed-of-light units the existing geometric causal relation has the familiar
> elapsed-time and spatial-distance characterization. This is an application representation.

```lean
lemma precedes_iff_time_space (c : SpeedOfLight) (p q : SpaceTime d) :
    (causalRelation d).Precedes p q ↔
      (p.time c).val ≤ (q.time c).val ∧
        ‖q.space - p.space‖ ≤ (c : ℝ) * ((q.time c).val - (p.time c).val)
```

**`Minkowski.isClosed_causalFuture_zero`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Causality/LightCone.lean#L136).

> The future causal cone at the origin is closed.

```lean
lemma isClosed_causalFuture_zero : IsClosed ((causalRelation d).causalFuture {0})
```

**`Minkowski.causalFuture_eq_add`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Causality/LightCone.lean#L147).

> Futures are translations of the existing future cone, combined over the source set.

```lean
lemma causalFuture_eq_add (K : Set (SpaceTime d)) :
    (causalRelation d).causalFuture K = K + (causalRelation d).causalFuture {0}
```

**`Minkowski.isClosed_causalFuture`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Causality/LightCone.lean#L163).

> Causal futures of compact source sets are closed.

```lean
lemma isClosed_causalFuture {K : Set (SpaceTime d)} (hK : IsCompact K) :
    IsClosed ((causalRelation d).causalFuture K)
```

**`Minkowski.causalPast_eq_add_neg`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Causality/LightCone.lean#L169).

> Causal pasts are translations of the negated future cone.

```lean
lemma causalPast_eq_add_neg (K : Set (SpaceTime d)) :
    (causalRelation d).causalPast K = K + -((causalRelation d).causalFuture {0})
```

**`Minkowski.isClosed_causalPast`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Causality/LightCone.lean#L192).

> Causal pasts of compact source sets are closed.

```lean
lemma isClosed_causalPast {K : Set (SpaceTime d)} (hK : IsCompact K) :
    IsClosed ((causalRelation d).causalPast K)
```

**`Minkowski.component_bound_of_causalDiamond`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Causality/LightCone.lean#L198).

> Every component in a causal diamond is bounded by the bounds on its endpoint sets.

```lean
lemma component_bound_of_causalDiamond {A B : ℝ} (hA : 0 ≤ A) (hB : 0 ≤ B)
    {k x l : SpaceTime d} (hk : ‖k‖ ≤ A) (hl : ‖l‖ ≤ B)
    (hkx : (causalRelation d).Precedes k x) (hxl : (causalRelation d).Precedes x l)
    (i : Fin 1 ⊕ Fin d) : |x i| ≤ 2 * A + B
```

**`Minkowski.hasCompactCausalDiamonds`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Causality/LightCone.lean#L232).

> Minkowski causal diamonds between compact endpoint sets are compact in every spatial
> dimension.

```lean
lemma hasCompactCausalDiamonds (d : ℕ) : (causalRelation d).HasCompactCausalDiamonds
```

**`Minkowski.local_causalPast_bound`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Causality/LightCone.lean#L252).

> Each event has a compact future observation bound whose causal past is a neighborhood.

```lean
lemma local_causalPast_bound (p : SpaceTime d) :
    ∃ K : Set (SpaceTime d), IsCompact K ∧ (causalRelation d).causalPast K ∈ 𝓝 p
```

**`Minkowski.local_causalFuture_bound`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Causality/LightCone.lean#L273).

> Each event has a compact past observation bound whose causal future is a neighborhood.

```lean
lemma local_causalFuture_bound (p : SpaceTime d) :
    ∃ K : Set (SpaceTime d), IsCompact K ∧ (causalRelation d).causalFuture K ∈ 𝓝 p
```

**`TimeSpace.causalFuture`**, a def, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Causality/LightCone.lean#L303).

> The causal future of a set of spacetime points, in units where the speed of light is `1`.

```lean
def causalFuture (K : Set (ℝ × E)) : Set (ℝ × E)
```

**`TimeSpace.isClosed_causalFuture`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Causality/LightCone.lean#L308).

> The causal future of a compact source region is closed.

```lean
lemma isClosed_causalFuture {K : Set (ℝ × E)} (hK : IsCompact K) :
    IsClosed (causalFuture K)
```

**`TimeSpace.causalPast`**, a def, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Causality/LightCone.lean#L325).

> The causal past of a set of spacetime points.

```lean
def causalPast (K : Set (ℝ × E)) : Set (ℝ × E)
```

## Depends on

- [Physlib.Relativity.Causality.Basic](../../../physlib/relativity/causality/basic.md)
- [Spacetime](../../../physlib/spaceandtime/spacetime/basic.md)
- [Causal support geometry](../../mathematics/part-02/order/causalrelation.md)

## Proof depends on

- [Vectors in the causal future of the origin](../../../physlib/relativity/causality/causallyfollows.md)

## Sources

- [PhyslibAlpha/Relativity/Causality/LightCone.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Causality/LightCone.lean)
