---
declaration: module
origin: cited
lean: Space.halfPlaneDomain, Space.halfPlane, Space.halfPlane_eq, Space.halfPlane_injective, Space.halfPlane_continuous, Space.halfPlane_measurableEmbedding, Space.norm_halfPlane, Space.halfPlaneMeasure
statement: formalized
proof: formalized
---

# Half-plane surface in `Space 3`

The module `PhyslibAlpha.SpaceAndTime.Space.Surfaces.HalfPlane`, [PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean): 18 declarations, 5 with a docstring.

> The half-plane in `Space 3` with its measure, distribution and vanishing ambient volume.

## i. Overview

> The half-plane is the coordinate plane in `Space 3` with nonnegative second
> coordinate. It is the image of the domain `halfPlaneDomain` in `Space 2` under the coordinate
> plane embedding `halfPlane`. Pushing forward the restricted volume gives the measure
> `halfPlaneMeasure`, and integrating against it gives the distribution `halfPlaneDist`. The
> half-plane lies in a proper linear subspace, so it has ambient volume zero.

## ii. Key results

> - `halfPlaneDomain` : the domain of the half-plane inside `Space 2`.
> - `halfPlane` : the coordinate plane embedding of `Space 2` into `Space 3`.
> - `halfPlaneMeasure` : the measure corresponding to integration over the half-plane.
> - `halfPlaneDist` : the distribution corresponding to integration over the half-plane.
> - `volume_halfPlane_image_domain` : the half-plane has ambient volume zero.

## iv. References

> * None.

## A. The definition of the half-plane surface

**`Space.halfPlaneDomain`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean#L62).

> The domain of the half-plane inside `Space 2`.

```lean
def halfPlaneDomain : Set (Space 2)
```

**`Space.halfPlane`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean#L65).

> The coordinate plane embedding used for the half-plane surface in `Space 3`.

```lean
def halfPlane : Space 2 → Space 3
```

**`Space.halfPlane_eq`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean#L67).

```lean
lemma halfPlane_eq : halfPlane = (slice (2 : Fin 3)).symm ∘ (fun x : Space 2 => (0, x))
```

**`Space.halfPlane_injective`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean#L69).

```lean
lemma halfPlane_injective : Function.Injective halfPlane
```

**`Space.halfPlane_continuous`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean#L76).

```lean
lemma halfPlane_continuous : Continuous halfPlane
```

**`Space.halfPlane_measurableEmbedding`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean#L80).

```lean
lemma halfPlane_measurableEmbedding : MeasurableEmbedding halfPlane
```

**`Space.norm_halfPlane`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean#L84).

```lean
lemma norm_halfPlane (x : Space 2) : ‖halfPlane x‖ = ‖x‖
```

## B. The measure associated with the half-plane

**`Space.halfPlaneMeasure`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean#L95).

> The measure on `Space 3` corresponding to integration over a half-plane.

```lean
def halfPlaneMeasure : Measure (Space 3)
```

**`Space.halfPlaneMeasure_hasTemperateGrowth`**, an instance, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean#L98).

```lean
instance halfPlaneMeasure_hasTemperateGrowth :
    halfPlaneMeasure.HasTemperateGrowth
```

**`Space.halfPlaneMeasure_sFinite`**, an instance, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean#L110).

```lean
instance halfPlaneMeasure_sFinite : SFinite halfPlaneMeasure
```

## C. The distribution associated with the half-plane

**`Space.halfPlaneDist`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean#L121).

> The distribution on `Space 3` corresponding to integration over a half-plane.

```lean
def halfPlaneDist : (Space 3) →d[ℝ] ℝ
```

**`Space.halfPlaneDist_apply_eq_integral_halfPlaneMeasure`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean#L124).

```lean
lemma halfPlaneDist_apply_eq_integral_halfPlaneMeasure (f : 𝓢(Space 3, ℝ)) :
    halfPlaneDist f = ∫ x, f x ∂halfPlaneMeasure
```

**`Space.halfPlaneDist_apply_eq_integral_volume`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean#L128).

```lean
lemma halfPlaneDist_apply_eq_integral_volume (f : 𝓢(Space 3, ℝ)) :
    halfPlaneDist f = ∫ x, f (halfPlane x) ∂(volume.restrict halfPlaneDomain)
```

## D. The half-plane has ambient volume zero

**`Space.halfPlaneSubmodule`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean#L140).

> The coordinate plane containing the half-plane in `Space 3`.

```lean
def halfPlaneSubmodule : Submodule ℝ (Space 3)
```

**`Space.halfPlane_mem_halfPlaneSubmodule`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean#L150).

```lean
lemma halfPlane_mem_halfPlaneSubmodule (x : Space 2) : halfPlane x ∈ halfPlaneSubmodule
```

**`Space.halfPlane_image_domain_subset_halfPlaneSubmodule`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean#L153).

```lean
lemma halfPlane_image_domain_subset_halfPlaneSubmodule :
    halfPlane '' halfPlaneDomain ⊆ (halfPlaneSubmodule : Set (Space 3))
```

**`Space.halfPlaneSubmodule_ne_top`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean#L158).

```lean
lemma halfPlaneSubmodule_ne_top : halfPlaneSubmodule ≠ ⊤
```

**`Space.volume_halfPlane_image_domain`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean#L165).

```lean
lemma volume_halfPlane_image_domain :
    volume (halfPlane '' halfPlaneDomain : Set (Space 3)) = 0
```

## Depends on

- [Distributions](../../../physlib/mathematics/distribution/tempereddistribution.md)
- [Slices of space](../../../physlib/spaceandtime/space/part-01/slice.md)

## Proof depends on

- [Integrals in Space](../../../physlib/spaceandtime/space/part-02/integrals-basic.md)

## Sources

- [PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/HalfPlane.lean)
