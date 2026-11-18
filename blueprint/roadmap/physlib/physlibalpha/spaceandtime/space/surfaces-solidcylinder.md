---
declaration: module
origin: cited
lean: Space.solidCylinder, Space.solidCylinder_eq, Space.solidCylinder_injective, Space.solidCylinder_continuous, Space.solidCylinder_measurableEmbedding, Space.norm_solidCylinder, Space.solidCylinderMeasure, Space.solidCylinderMeasure_hasTemperateGrowth
statement: formalized
proof: formalized
---

# Solid cylinder surface in `Space 3`

The module `PhyslibAlpha.SpaceAndTime.Space.Surfaces.SolidCylinder`, [PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidCylinder.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidCylinder.lean): 13 declarations, 3 with a docstring.

> The solid unit cylinder in `Space 3` with its measure, distribution and positive volume.

## i. Overview

> The solid cylinder is the closed unit disk in `Space 2` extruded along the third coordinate.
> It is the solid analogue of the spherical cylinder, in the same way that the solid sphere is the
> solid analogue of the spherical shell. Like the solid sphere it is a region of positive ambient
> volume, so the measure associated with it is built from the ambient volume of the cross-sectional
> disk (the solid-sphere measure in `Space 2`) extruded along the axis, rather than a pushforward of
> a lower-dimensional surface measure. The measure-zero requirement is therefore not applicable here
> and is replaced by a statement that the solid cylinder has positive ambient volume.

## ii. Key results

> - `solidCylinder` : the embedding of a cross-sectional disk extruded along the axis.
> - `solidCylinderMeasure` : the measure corresponding to integration over the solid cylinder.
> - `solidCylinderDist` : the distribution corresponding to integration over the solid cylinder.
> - `solidCylinderMeasure_univ_pos` : the solid cylinder has positive measure.

## iv. References

> * None.

## A. The definition of the solid cylinder surface

**`Space.solidCylinder`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidCylinder.lean#L64).

> The map embedding a cross-sectional disk extruded along the axis into `Space 3`. The disk is
> cut out by the solid-cylinder measure, which is supported on the closed unit disk.

```lean
def solidCylinder : Space 2 × ℝ → Space 3
```

**`Space.solidCylinder_eq`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidCylinder.lean#L67).

```lean
lemma solidCylinder_eq :
    solidCylinder = (slice 2).symm ∘ (fun x : Space 2 × ℝ => (x.2, x.1))
```

**`Space.solidCylinder_injective`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidCylinder.lean#L70).

```lean
lemma solidCylinder_injective : Function.Injective solidCylinder
```

**`Space.solidCylinder_continuous`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidCylinder.lean#L77).

```lean
lemma solidCylinder_continuous : Continuous solidCylinder
```

**`Space.solidCylinder_measurableEmbedding`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidCylinder.lean#L81).

```lean
lemma solidCylinder_measurableEmbedding : MeasurableEmbedding solidCylinder
```

**`Space.norm_solidCylinder`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidCylinder.lean#L85).

```lean
lemma norm_solidCylinder (x : Space 2 × ℝ) :
    ‖solidCylinder x‖ = √(‖x.2‖ ^ 2 + ‖x.1‖ ^ 2)
```

## B. The measure associated with the solid cylinder

**`Space.solidCylinderMeasure`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidCylinder.lean#L98).

> The measure on `Space 3` corresponding to integration over a solid cylinder, i.e. the
> pushforward of the product of the solid-sphere (closed unit disk) measure on `Space 2` with the
> line measure along the axis.

```lean
def solidCylinderMeasure : Measure (Space 3)
```

**`Space.solidCylinderMeasure_hasTemperateGrowth`**, an instance, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidCylinder.lean#L101).

```lean
instance solidCylinderMeasure_hasTemperateGrowth :
    solidCylinderMeasure.HasTemperateGrowth
```

**`Space.solidCylinderMeasure_sFinite`**, an instance, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidCylinder.lean#L126).

```lean
instance solidCylinderMeasure_sFinite : SFinite solidCylinderMeasure
```

## C. The distribution associated with the solid cylinder

**`Space.solidCylinderDist`**, a def, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidCylinder.lean#L139).

> The distribution on `Space 3` corresponding to integration over a solid cylinder.
> One can roughly think of this distribution as taking a test function `f` to its integral against
> a mass, charge or current density spread over a solid cylinder.

```lean
def solidCylinderDist : (Space 3) →d[ℝ] ℝ
```

**`Space.solidCylinderDist_apply_eq_integral_solidCylinderMeasure`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidCylinder.lean#L142).

```lean
lemma solidCylinderDist_apply_eq_integral_solidCylinderMeasure (f : 𝓢(Space 3, ℝ)) :
    solidCylinderDist f = ∫ x, f x ∂solidCylinderMeasure
```

**`Space.solidCylinderDist_apply_eq_integral_disk_volume`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidCylinder.lean#L146).

```lean
lemma solidCylinderDist_apply_eq_integral_disk_volume (f : 𝓢(Space 3, ℝ)) :
    solidCylinderDist f =
    ∫ x, f (solidCylinder x) ∂((solidSphereMeasure 2).prod (volume (α := ℝ)))
```

## D. The solid cylinder has positive ambient volume

**`Space.solidCylinderMeasure_univ_pos`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidCylinder.lean#L158).

```lean
lemma solidCylinderMeasure_univ_pos : 0 < solidCylinderMeasure Set.univ
```

## Depends on

- [Slices of space](../../../physlib/spaceandtime/space/part-01/slice.md)
- [Solid sphere surfaces in `Space d`](surfaces-solidsphere.md)

## Sources

- [PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidCylinder.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidCylinder.lean)
