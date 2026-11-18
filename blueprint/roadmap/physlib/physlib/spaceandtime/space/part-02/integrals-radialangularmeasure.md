---
declaration: module
origin: cited
lean: Space.radialAngularMeasure, Space.radialAngularMeasure_eq_volume_withDensity, Space.radialAngularMeasure_zero_eq_volume, Space.integral_radialAngularMeasure, Space.lintegral_radialMeasure, Space.lintegral_radialMeasure_eq_spherical_mul, Space.radialAngularMeasure_closedBall, Space.radialAngularMeasure_real_closedBall
statement: formalized
proof: formalized
---

# The radial angular measure on Space

The module `Physlib.SpaceAndTime.Space.Integrals.RadialAngularMeasure`, [Physlib/SpaceAndTime/Space/Integrals/RadialAngularMeasure.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/RadialAngularMeasure.lean): 13 declarations (2 instances with no name), 1 with a docstring; 1 private, not shown.

## i. Overview

> The normal measure on `Space d` is `r^(d-1) dr dΩ` in spherical coordinates,
> where `dΩ` is the angular measure on the unit sphere. The radial angular measure
> is the measure `dr dΩ`, cancelling the radius contribution from the measure in spherical
> coordinates.
>
> …

## ii. Key results

> - `radialAngularMeasure`: The radial angular measure on `Space d`.

## iv. References

> * None.

## A. The definition of the radial angular measure

**`Space.radialAngularMeasure`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/RadialAngularMeasure.lean#L63).

> The measure on `Space d` weighted by `1 / ‖x‖ ^ (d - 1)`.

```lean
def radialAngularMeasure {d : ℕ} : Measure (Space d)
```

### A.1. Basic equalities

**`Space.radialAngularMeasure_eq_volume_withDensity`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/RadialAngularMeasure.lean#L72).

```lean
lemma radialAngularMeasure_eq_volume_withDensity {d : ℕ} : radialAngularMeasure =
    volume.withDensity (fun x : Space d => ENNReal.ofReal (1 / ‖x‖ ^ (d - 1)))
```

**`Space.radialAngularMeasure_zero_eq_volume`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/RadialAngularMeasure.lean#L77).

```lean
lemma radialAngularMeasure_zero_eq_volume :
    radialAngularMeasure (d := 0) = volume
```

### A.2. SFinite property

**An instance with no name**, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/RadialAngularMeasure.lean#L87).

```lean
instance (d : ℕ) : SFinite (radialAngularMeasure (d := d))
```

## B. Integrals with respect to radialAngularMeasure

**`Space.integral_radialAngularMeasure`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/RadialAngularMeasure.lean#L97).

```lean
lemma integral_radialAngularMeasure {d : ℕ} (f : Space d → F) :
    ∫ x, f x ∂radialAngularMeasure = ∫ x, (1 / ‖x‖ ^ (d - 1)) • f x
```

**`Space.lintegral_radialMeasure`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/RadialAngularMeasure.lean#L104).

```lean
lemma lintegral_radialMeasure {d : ℕ} (f : Space d → ENNReal) (hf : Measurable f) :
    ∫⁻ x, f x ∂radialAngularMeasure = ∫⁻ x, ENNReal.ofReal (1 / ‖x‖ ^ (d - 1)) * f x
```

**`Space.lintegral_radialMeasure_eq_spherical_mul`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/RadialAngularMeasure.lean#L111).

```lean
lemma lintegral_radialMeasure_eq_spherical_mul (d : ℕ) [NeZero d]
    (f : Space d → ENNReal) (hf : Measurable f) :
    ∫⁻ x, f x ∂radialAngularMeasure = ∫⁻ x, f (x.2.1 • x.1.1)
      ∂(volume (α := Space d).toSphere.prod (Measure.volumeIoiPow 0))
```

## C. The radialAngularMeasure on balls

**`Space.radialAngularMeasure_closedBall`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/RadialAngularMeasure.lean#L133).

```lean
lemma radialAngularMeasure_closedBall (r : ℝ) :
    radialAngularMeasure (Metric.closedBall (0 : Space 3) r) = ENNReal.ofReal (4 * π * r)
```

**`Space.radialAngularMeasure_real_closedBall`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/RadialAngularMeasure.lean#L163).

```lean
lemma radialAngularMeasure_real_closedBall (r : ℝ) (hr : 0 < r) :
    radialAngularMeasure.real (Metric.closedBall (0 : Space 3) r) = 4 * π * r
```

## D. Integrability conditions

**`Space.integrable_radialAngularMeasure_iff`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/RadialAngularMeasure.lean#L175).

```lean
lemma integrable_radialAngularMeasure_iff {d : ℕ} {f : Space d → F} :
    Integrable f (radialAngularMeasure (d := d)) ↔
      Integrable (fun x => (1 / ‖x‖ ^ (d - 1)) • f x) volume
```

**`Space.integrable_radialAngularMeasure_of_spherical`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/RadialAngularMeasure.lean#L185).

```lean
lemma integrable_radialAngularMeasure_of_spherical {d : ℕ} [NeZero d] (f : Space d → F)
    (hae : StronglyMeasurable f)
    (hf : Integrable (fun x => f (x.2.1 • x.1.1))
    (volume (α := Space d).toSphere.prod (Measure.volumeIoiPow 0))) :
    Integrable f radialAngularMeasure
```

## E. HasTemperateGrowth of measures

### E.1. Integrability of powers

**`Space.radialAngularMeasure_integrable_pow_neg_two`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/RadialAngularMeasure.lean#L222).

```lean
lemma radialAngularMeasure_integrable_pow_neg_two {d : ℕ} :
    Integrable (fun x : Space d => (1 + ‖x‖) ^ (- (d + 1) : ℝ))
      radialAngularMeasure
```

### E.2. radialAngularMeasure has temperate growth

**An instance with no name**, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/RadialAngularMeasure.lean#L249).

```lean
instance (d : ℕ) : Measure.HasTemperateGrowth (radialAngularMeasure (d := d))
```

## Depends on

- [The structure of a module on Space](../part-01/module.md)

## Proof depends on

- [Integrals in Space](integrals-basic.md)

## Sources

- [Physlib/SpaceAndTime/Space/Integrals/RadialAngularMeasure.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/RadialAngularMeasure.lean)
