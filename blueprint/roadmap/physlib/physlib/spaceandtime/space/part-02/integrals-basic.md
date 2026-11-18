---
declaration: module
origin: cited
lean: Space.volume_eq_addHaar, Space.volume_metricBall_three, Space.volume_metricBall_two, Space.volume_metricBall_two_real, Space.volume_metricBall_three_real, Space.integral_one_dim_eq_integral_real, Space.integral_volume_eq_spherical, Space.integrable_spherical_of_integrable
statement: formalized
proof: formalized
---

# Integrals in Space

The module `Physlib.SpaceAndTime.Space.Integrals.Basic`, [Physlib/SpaceAndTime/Space/Integrals/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/Basic.lean): 13 declarations (1 instance with no name), none with a docstring.

## i. Overview

> In this module we give general properties of integrals over `Space d`.
> We focus here on the volume measure, which is the usual measure on `Space d`, i.e.
> `dx dy dz`.

## ii. Key results

> - `volume_eq_addHaar` : The volume measure on `Space d` is the same as the Haar measure
>   associated with the basis of `Space d`.
> - `integral_volume_eq_spherical` : The integral of a function over `Space d` with
>   respect to the volume measure can be expressed as an integral over the unit sphere and
>   the positive reals.
> - `lintegral_volume_eq_spherical` : The lower Lebesgue integral of a function over `Space d`
>   with respect to the volume measure can be expressed as a lower Lebesgue integral over the unit
>   sphere and the positive reals.

## A. Properties of the volume measure

**`Space.volume_eq_addHaar`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/Basic.lean#L47).

```lean
lemma volume_eq_addHaar {d} : (volume (α := Space d)) = Space.basis.toBasis.addHaar
```

**`Space.volume_metricBall_three`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/Basic.lean#L51).

```lean
lemma volume_metricBall_three :
    volume (Metric.ball (0 : Space 3) 1) = ENNReal.ofReal (4 / 3 * Real.pi)
```

**`Space.volume_metricBall_two`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/Basic.lean#L60).

```lean
lemma volume_metricBall_two :
    volume (Metric.ball (0 : Space 2) 1) = ENNReal.ofReal Real.pi
```

**`Space.volume_metricBall_two_real`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/Basic.lean#L67).

```lean
lemma volume_metricBall_two_real :
    (volume.real (Metric.ball (0 : Space 2) 1)) = Real.pi
```

**`Space.volume_metricBall_three_real`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/Basic.lean#L76).

```lean
lemma volume_metricBall_three_real :
    (volume.real (Metric.ball (0 : Space 3) 1)) = 4 / 3 * Real.pi
```

## B. Integrals over one-dimensional space

**`Space.integral_one_dim_eq_integral_real`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/Basic.lean#L90).

```lean
lemma integral_one_dim_eq_integral_real {f : Space 1 → ℝ} :
    ∫ x, f x ∂volume = ∫ x, f (oneEquiv.symm x) ∂volume
```

## C. Integrals over volume to spherical

**`Space.integral_volume_eq_spherical`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/Basic.lean#L99).

```lean
lemma integral_volume_eq_spherical (d : ℕ) [NeZero d] (f : Space d → F)
    [NormedAddCommGroup F] [NormedSpace ℝ F] :
    ∫ x, f x ∂volume = ∫ x, f (x.2.1 • x.1.1) ∂(volume (α := Space d).toSphere.prod
        (Measure.volumeIoiPow (Module.finrank ℝ (Space d) - 1)))
```

**`Space.integrable_spherical_of_integrable`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/Basic.lean#L128).

```lean
lemma integrable_spherical_of_integrable {d : ℕ} {F : Type*}
    [NormedAddCommGroup F] [NormedSpace ℝ F] {f : Space d → F}
    (hf : Integrable f volume) :
    Integrable
      (fun x : ↑(Metric.sphere (0 : Space d) 1) × Set.Ioi (0 : ℝ) =>
        f (x.2.1 • x.1.1))
      (volume (α := Space d).toSphere.prod
        (Measure.volumeIoiPow (Module.finrank ℝ (Space d) - 1)))
```

**`Space.integral_volume_eq_spherical_iterated`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/Basic.lean#L157).

```lean
lemma integral_volume_eq_spherical_iterated {d : ℕ} [NeZero d] {F : Type*}
    [NormedAddCommGroup F] [NormedSpace ℝ F] (f : Space d → F)
    (hf : Integrable f volume) :
    ∫ x : Space d, f x =
      ∫ n : ↑(Metric.sphere (0 : Space d) 1),
        ∫ r : Set.Ioi (0 : ℝ), f (r.1 • n.1)
          ∂(Measure.volumeIoiPow (Module.finrank ℝ (Space d) - 1))
        ∂(volume (α := Space d).toSphere)
```

**An instance with no name**, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/Basic.lean#L172).

```lean
instance : SFinite (@Measure.comap ↑(Set.Ioi 0) ℝ Subtype.instMeasurableSpace
        Real.measureSpace.toMeasurableSpace Subtype.val volume)
```

**`Space.integral_volume_eq_spherical_integral`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/Basic.lean#L199).

```lean
lemma integral_volume_eq_spherical_integral {d : ℕ} [NeZero d] {F : Type*}
    [NormedAddCommGroup F] [NormedSpace ℝ F] (f : Space d → F)
    (hf : Integrable f volume) :
    ∫ x : Space d, f x =
      ∫ n : ↑(Metric.sphere (0 : Space d) 1),
        ∫ r : Set.Ioi (0 : ℝ), (r.1 ^ (d - 1)) • f (r.1 • n.1)
          ∂(.comap Subtype.val volume)
        ∂(volume (α := Space d).toSphere)
```

## D. Lower Lebesgue integral over volume to spherical

**`Space.lintegral_volume_eq_spherical`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/Basic.lean#L222).

```lean
lemma lintegral_volume_eq_spherical (d : ℕ) [NeZero d]
    (f : Space d → ENNReal) (hf : Measurable f) :
    ∫⁻ x, f x ∂volume = ∫⁻ x, f (x.2.1 • x.1.1) ∂(volume (α := Space d).toSphere.prod
        (Measure.volumeIoiPow (Module.finrank ℝ (Space d) - 1)))
```

**`Space.lintegral_volume_eq_spherical_mul`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/Basic.lean#L248).

```lean
lemma lintegral_volume_eq_spherical_mul (d : ℕ) [NeZero d]
    (f : Space d → ENNReal) (hf : Measurable f) :
    ∫⁻ x, f x ∂volume = ∫⁻ x, f (x.2.1 • x.1.1) * .ofReal (x.2.1 ^ (d - 1))
      ∂(volume (α := Space d).toSphere.prod (Measure.volumeIoiPow 0))
```

## Depends on

- [The structure of a module on Space](../part-01/module.md)

## Proof depends on

- [Basic integration results](../../../mathematics/formathlib/integration-basic.md)

## Sources

- [Physlib/SpaceAndTime/Space/Integrals/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Integrals/Basic.lean)
