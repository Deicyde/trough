---
declaration: module
origin: cited
lean: Space.solidSphere, Space.solidSphere_injective, Space.solidSphere_continuous, Space.solidSphere_measurableEmbedding, Space.norm_solidSphere_le, Space.solidSphereMeasure, Space.solidSphereMeasure_isFiniteMeasure, Space.solidSphereMeasure_hasTemperateGrowth
statement: formalized
proof: formalized
---

# Solid sphere surfaces in `Space d`

The module `PhyslibAlpha.SpaceAndTime.Space.Surfaces.SolidSphere`, [PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidSphere.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidSphere.lean): 13 declarations, 3 with a docstring.

> The closed unit ball in `Space d` with its measure, distribution and positive volume.

## i. Overview

> The solid sphere is the closed unit ball in `Space d`. Unlike the line or the spherical
> shell, it is a region of positive ambient volume, so the measure associated with it is the
> ambient volume restricted to the ball rather than a pushforward of a lower-dimensional measure.
> The requirement that the surface has ambient measure zero is therefore not applicable here, and
> is replaced by a statement that the solid sphere has positive ambient volume.

## ii. Key results

> - `solidSphere` : the inclusion of the closed unit ball into `Space d`.
> - `solidSphereMeasure` : the measure corresponding to integration over the solid sphere.
> - `solidSphereDist` : the distribution corresponding to integration over the solid sphere.
> - `solidSphere_volume_pos`, `solidSphereMeasure_univ_pos` : the solid sphere has positive volume.

## iv. References

> * None.

## A. The definition of the solid sphere surface

**`Space.solidSphere`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidSphere.lean#L59).

> The inclusion into `Space d` of its closed unit ball `B^d` (the subtype coercion `x ↦ x.1`).

```lean
def solidSphere (d : ℕ) : Metric.closedBall (0 : Space d) 1 → Space d
```

**`Space.solidSphere_injective`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidSphere.lean#L61).

```lean
lemma solidSphere_injective (d : ℕ) : Function.Injective (solidSphere d)
```

**`Space.solidSphere_continuous`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidSphere.lean#L66).

```lean
lemma solidSphere_continuous (d : ℕ) : Continuous (solidSphere d)
```

**`Space.solidSphere_measurableEmbedding`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidSphere.lean#L68).

```lean
lemma solidSphere_measurableEmbedding (d : ℕ) : MeasurableEmbedding (solidSphere d)
```

**`Space.norm_solidSphere_le`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidSphere.lean#L74).

```lean
lemma norm_solidSphere_le (d : ℕ) (x : Metric.closedBall (0 : Space d) 1) :
    ‖solidSphere d x‖ ≤ 1
```

## B. The measure associated with the solid sphere

**`Space.solidSphereMeasure`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidSphere.lean#L88).

> The measure on `Space d` corresponding to integration over a solid sphere, i.e. the
> ambient volume measure restricted to the closed unit ball.

```lean
def solidSphereMeasure (d : ℕ) : Measure (Space d)
```

**`Space.solidSphereMeasure_isFiniteMeasure`**, an instance, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidSphere.lean#L91).

```lean
instance solidSphereMeasure_isFiniteMeasure (d : ℕ) :
    IsFiniteMeasure (solidSphereMeasure d)
```

**`Space.solidSphereMeasure_hasTemperateGrowth`**, an instance, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidSphere.lean#L96).

```lean
instance solidSphereMeasure_hasTemperateGrowth (d : ℕ) :
    (solidSphereMeasure d).HasTemperateGrowth
```

## C. The distribution associated with the solid sphere

**`Space.solidSphereDist`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidSphere.lean#L109).

> The distribution on `Space d` corresponding to integration over a solid sphere.
> One can roughly think of this distribution as taking a test function `f` to its integral against
> a mass, charge or current density spread over a solid ball.

```lean
def solidSphereDist (d : ℕ) : (Space d) →d[ℝ] ℝ
```

**`Space.solidSphereDist_apply_eq_integral_solidSphereMeasure`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidSphere.lean#L112).

```lean
lemma solidSphereDist_apply_eq_integral_solidSphereMeasure (d : ℕ) (f : 𝓢(Space d, ℝ)) :
    solidSphereDist d f = ∫ x, f x ∂solidSphereMeasure d
```

**`Space.solidSphereDist_apply_eq_integral_closedBall`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidSphere.lean#L116).

```lean
lemma solidSphereDist_apply_eq_integral_closedBall (d : ℕ) (f : 𝓢(Space d, ℝ)) :
    solidSphereDist d f = ∫ x in Metric.closedBall (0 : Space d) 1, f x
```

## D. The solid sphere has positive ambient volume

**`Space.solidSphere_volume_pos`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidSphere.lean#L126).

```lean
lemma solidSphere_volume_pos (d : ℕ) :
    0 < volume (Metric.closedBall (0 : Space d) 1)
```

**`Space.solidSphereMeasure_univ_pos`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidSphere.lean#L132).

```lean
lemma solidSphereMeasure_univ_pos (d : ℕ) : 0 < solidSphereMeasure d Set.univ
```

## Depends on

- [Distributions](../../../physlib/mathematics/distribution/tempereddistribution.md)
- [The structure of a module on Space](../../../physlib/spaceandtime/space/part-01/module.md)

## Sources

- [PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidSphere.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SolidSphere.lean)
