---
declaration: module
origin: cited
lean: Space.sphericalCylinder, Space.sphericalCylinder_eq, Space.sphericalCylinder_injective, Space.sphericalCylinder_continuous, Space.sphericalCylinder_measurableEmbedding, Space.norm_sphericalCylinder, Space.sphericalCylinderMeasure, Space.sphericalCylinderMeasure_hasTemperateGrowth
statement: formalized
proof: formalized
---

# Spherical cylinder surface in `Space 3`

The module `PhyslibAlpha.SpaceAndTime.Space.Surfaces.SphericalCylinder`, [PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalCylinder.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalCylinder.lean): 12 declarations, 3 with a docstring.

> The unit spherical cylinder in `Space 3` with its measure and distribution.

## i. Overview

> The spherical cylinder is the unit circular shell in `Space 2` extruded along the
> third coordinate. The embedding `sphericalCylinder` pushes forward the product of the sphere
> measure and the volume on the axis to give `sphericalCylinderMeasure`, and integrating against it
> gives the distribution `sphericalCylinderDist`.

## ii. Key results

> - `sphericalCylinder` : the embedding of the unit circle extruded along the axis.
> - `sphericalCylinderMeasure` : the measure corresponding to integration over the cylinder.
> - `sphericalCylinderDist` : the distribution corresponding to integration over the cylinder.

## iv. References

> * None.

## A. The definition of the spherical cylinder surface

**`Space.sphericalCylinder`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalCylinder.lean#L58).

> The map embedding the unit circular shell extruded along the axis into `Space 3`.

```lean
def sphericalCylinder : Metric.sphere (0 : Space 2) 1 × ℝ → Space 3
```

**`Space.sphericalCylinder_eq`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalCylinder.lean#L61).

```lean
lemma sphericalCylinder_eq :
    sphericalCylinder = (slice 2).symm ∘ (fun x => (x.2, sphericalShell 2 x.1))
```

**`Space.sphericalCylinder_injective`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalCylinder.lean#L64).

```lean
lemma sphericalCylinder_injective : Function.Injective sphericalCylinder
```

**`Space.sphericalCylinder_continuous`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalCylinder.lean#L71).

```lean
lemma sphericalCylinder_continuous : Continuous sphericalCylinder
```

**`Space.sphericalCylinder_measurableEmbedding`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalCylinder.lean#L76).

```lean
lemma sphericalCylinder_measurableEmbedding : MeasurableEmbedding sphericalCylinder
```

**`Space.norm_sphericalCylinder`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalCylinder.lean#L80).

```lean
lemma norm_sphericalCylinder (x : Metric.sphere (0 : Space 2) 1 × ℝ) :
    ‖sphericalCylinder x‖ = √(‖x.2‖ ^ 2 + 1)
```

## B. The measure associated with the spherical cylinder

**`Space.sphericalCylinderMeasure`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalCylinder.lean#L92).

> The measure on `Space 3` corresponding to integration over a spherical cylinder.

```lean
def sphericalCylinderMeasure : Measure (Space 3)
```

**`Space.sphericalCylinderMeasure_hasTemperateGrowth`**, an instance, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalCylinder.lean#L96).

```lean
instance sphericalCylinderMeasure_hasTemperateGrowth :
    sphericalCylinderMeasure.HasTemperateGrowth
```

**`Space.sphericalCylinderMeasure_sFinite`**, an instance, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalCylinder.lean#L120).

```lean
instance sphericalCylinderMeasure_sFinite : SFinite sphericalCylinderMeasure
```

## C. The distribution associated with the spherical cylinder

**`Space.sphericalCylinderDist`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalCylinder.lean#L132).

> The distribution on `Space 3` corresponding to integration over a spherical cylinder.

```lean
def sphericalCylinderDist : (Space 3) →d[ℝ] ℝ
```

**`Space.sphericalCylinderDist_apply_eq_integral_sphericalCylinderMeasure`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalCylinder.lean#L135).

```lean
lemma sphericalCylinderDist_apply_eq_integral_sphericalCylinderMeasure (f : 𝓢(Space 3, ℝ)) :
    sphericalCylinderDist f = ∫ x, f x ∂sphericalCylinderMeasure
```

**`Space.sphericalCylinderDist_apply_eq_integral_sphere_volume`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalCylinder.lean#L139).

```lean
lemma sphericalCylinderDist_apply_eq_integral_sphere_volume (f : 𝓢(Space 3, ℝ)) :
    sphericalCylinderDist f =
    ∫ x, f (sphericalCylinder x)
      ∂((MeasureTheory.Measure.toSphere volume).prod (volume (α := ℝ)))
```

## Depends on

- [Slices of space](../../../physlib/spaceandtime/space/part-01/slice.md)
- [Spherical surfaces on Space](surfaces-sphericalshell.md)

## Sources

- [PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalCylinder.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalCylinder.lean)
