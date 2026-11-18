---
declaration: module
origin: cited
lean: Cosmology.FLRW.comovingDistance, Cosmology.FLRW.deriv_comovingDistance, Cosmology.FLRW.redshift, Cosmology.FLRW.one_add_redshift, Cosmology.FLRW.deriv_redshift, Cosmology.FLRW.deriv_scaleFactor_eq_mul_hubbleConstant, Cosmology.FLRW.deriv_comovingDistance_eq_mul_deriv_redshift, Cosmology.FLRW.properDistance
statement: formalized
proof: formalized
---

# Distances and redshift in FLRW cosmology

The module `Physlib.Cosmology.FLRW.Distances`, [Physlib/Cosmology/FLRW/Distances.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean): 18 declarations, 17 with a docstring.

## i. Overview

> The distances of this file are defined for an FLRW model. They have their meaning at the times
> of the interval of the model.
>
> The comoving distance of a source emitting at the time `t` and observed at `t₀` is
> `χ = c ∫_t^{t₀} dτ / a(τ)`, so that `∂ₜ χ = - c / a`. The redshift is `1 + z = a(t₀) / a(t)`,
> with `∂ₜ z = -(1 + z) H`. Combining the two gives `∂ₜ χ = (c / (a(t₀) H)) ∂ₜ z`. For
> `a(t₀) = 1`, this is the change of variables `dχ = c dz / H` behind the distance integrals in the
> redshift.
>
> The proper distance `D = a χ` obeys the Hubble-Lemaître law `∂ₜ D = H D`. The recession velocity
> equals `c` exactly at the Hubble radius `R_H = c / H`.
>
> The transverse comoving distance `r(χ)` is the function `S` of the spatial geometry of the model.
> Its closed forms are written in the curvature parameter `K` of that geometry, with curvature
> radius `1 / √|K|`.
>
> The particle and event horizons at `t` integrate `c / a` over the times of the interval of the
> model before and after `t`. The particle horizon of the Einstein-de Sitter model
> `FLRW.einsteinDeSitter` is computed.

## ii. Key results

> - `FLRW.comovingDistance`, `FLRW.deriv_comovingDistance`: `∂ₜ χ = - c / a`.
> - `FLRW.redshift`, `FLRW.deriv_redshift`: `∂ₜ z = -(1 + z) H`.
> - `FLRW.deriv_comovingDistance_eq_mul_deriv_redshift`: `∂ₜ χ = (c / (a(t₀) H)) ∂ₜ z`.
> - `FLRW.properDistance`, `FLRW.deriv_properDistance`: the Hubble-Lemaître law.
> - `FLRW.hubbleRadius`, `FLRW.deriv_properDistance_eq_iff`: the recession velocity at the Hubble
>   radius.
> - `FLRW.transverseComovingDistance` and its three closed forms.
> - `FLRW.particleHorizon`, `FLRW.eventHorizon`, `FLRW.particleHorizon_einsteinDeSitter`.

## A. The comoving distance

**`Cosmology.FLRW.comovingDistance`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean#L73).

> The line-of-sight comoving distance `χ = c ∫_t^{t₀} dτ / a(τ)` of a source emitting at `t`
> and observed at `t₀`.

```lean
noncomputable def comovingDistance (c : SpeedOfLight) (t t₀ : Time) : ℝ
```

**`Cosmology.FLRW.deriv_comovingDistance`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean#L77).

> For `t` and `t₀` in the interval of the model, `∂ₜ χ = - c / a`.

```lean
lemma deriv_comovingDistance {c : SpeedOfLight} {t₀ t : Time} (ht₀ : t₀ ∈ U.I) (ht : t ∈ U.I) :
    ∂ₜ (fun s => U.comovingDistance c s t₀) t = -(c : ℝ) / U.a t
```

## B. The redshift and the change of variables

**`Cosmology.FLRW.redshift`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean#L101).

> The redshift `z` of a source emitting at `t` and observed at `t₀`, with
> `1 + z = a(t₀) / a(t)`.

```lean
noncomputable def redshift (t₀ t : Time) : ℝ
```

**`Cosmology.FLRW.one_add_redshift`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean#L103).

```lean
lemma one_add_redshift (t₀ t : Time) : 1 + U.redshift t₀ t = U.a t₀ / U.a t
```

**`Cosmology.FLRW.deriv_redshift`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean#L108).

> For `t` in the interval of the model, `∂ₜ z = -(1 + z) H`.

```lean
lemma deriv_redshift {t₀ t : Time} (ht : t ∈ U.I) :
    ∂ₜ (U.redshift t₀) t = -(1 + U.redshift t₀ t) * hubbleConstant U.a t
```

**`Cosmology.FLRW.deriv_scaleFactor_eq_mul_hubbleConstant`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean#L120).

> For `t` in the interval of the model, `∂ₜ a = a H`.

```lean
lemma deriv_scaleFactor_eq_mul_hubbleConstant {t : Time} (ht : t ∈ U.I) :
    ∂ₜ U.a t = U.a t * hubbleConstant U.a t
```

**`Cosmology.FLRW.deriv_comovingDistance_eq_mul_deriv_redshift`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean#L129).

> For `t` and `t₀` in the interval of the model with `H(t) ≠ 0`,
> `∂ₜ χ = (c / (a(t₀) H)) ∂ₜ z`. For `a(t₀) = 1`, this is the change of variables
> `dχ = c dz / H`.

```lean
lemma deriv_comovingDistance_eq_mul_deriv_redshift {c : SpeedOfLight} {t₀ t : Time}
    (ht₀ : t₀ ∈ U.I) (ht : t ∈ U.I) (hH : hubbleConstant U.a t ≠ 0) :
    ∂ₜ (fun s => U.comovingDistance c s t₀) t
      = (c : ℝ) / (U.a t₀ * hubbleConstant U.a t) * ∂ₜ (U.redshift t₀) t
```

## C. The proper distance and the Hubble radius

**`Cosmology.FLRW.properDistance`**, a def, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean#L145).

> The proper distance `D = a χ` at fixed comoving distance `χ`.

```lean
noncomputable def properDistance (χ : ℝ) (t : Time) : ℝ
```

**`Cosmology.FLRW.deriv_properDistance`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean#L148).

> The Hubble-Lemaître law `∂ₜ D = H D`, for `t` in the interval of the model.

```lean
lemma deriv_properDistance {χ : ℝ} {t : Time} (ht : t ∈ U.I) :
    ∂ₜ (U.properDistance χ) t = hubbleConstant U.a t * U.properDistance χ t
```

**`Cosmology.FLRW.hubbleRadius`**, a def, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean#L158).

> The Hubble radius `R_H = c / H`.

```lean
noncomputable def hubbleRadius (c : SpeedOfLight) (t : Time) : ℝ
```

**`Cosmology.FLRW.deriv_properDistance_eq_iff`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean#L163).

> For `t` in the interval of the model with `H(t) ≠ 0`, the recession velocity `∂ₜ D` equals
> `c` exactly at the Hubble radius.

```lean
lemma deriv_properDistance_eq_iff {χ : ℝ} {c : SpeedOfLight} {t : Time} (ht : t ∈ U.I)
    (hH : hubbleConstant U.a t ≠ 0) :
    ∂ₜ (U.properDistance χ) t = (c : ℝ) ↔ U.properDistance χ t = U.hubbleRadius c t
```

## D. The transverse comoving distance

**`Cosmology.FLRW.transverseComovingDistance`**, a def, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean#L176).

> The transverse comoving distance `r(χ) = S(χ)` for the spatial geometry of an FLRW model.

```lean
noncomputable def transverseComovingDistance (χ : ℝ) : ℝ
```

**`Cosmology.FLRW.transverseComovingDistance_of_curvature_pos`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean#L179).

> For a positive curvature parameter `K`, `r(χ) = (1 / √K) sin (√K χ)`.

```lean
lemma transverseComovingDistance_of_curvature_pos (hK : 0 < U.geometry.curvature) (χ : ℝ) :
    U.transverseComovingDistance χ
      = 1 / √U.geometry.curvature * Real.sin (√U.geometry.curvature * χ)
```

**`Cosmology.FLRW.transverseComovingDistance_of_curvature_eq_zero`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean#L198).

> For a zero curvature parameter, `r(χ) = χ`.

```lean
lemma transverseComovingDistance_of_curvature_eq_zero (hK : U.geometry.curvature = 0) (χ : ℝ) :
    U.transverseComovingDistance χ = χ
```

**`Cosmology.FLRW.transverseComovingDistance_of_curvature_neg`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean#L208).

> For a negative curvature parameter `K`, `r(χ) = (1 / √(-K)) sinh (√(-K) χ)`.

```lean
lemma transverseComovingDistance_of_curvature_neg (hK : U.geometry.curvature < 0) (χ : ℝ) :
    U.transverseComovingDistance χ
      = 1 / √(-U.geometry.curvature) * Real.sinh (√(-U.geometry.curvature) * χ)
```

## E. The horizons

**`Cosmology.FLRW.particleHorizon`**, a def, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean#L234).

> The particle horizon at `t`, the integral of `c / a` over the times of the interval of the
> model before `t`. It is a Lebesgue integral, equal to `0` when the integrand is not
> integrable.

```lean
noncomputable def particleHorizon (c : SpeedOfLight) (t : Time) : ℝ
```

**`Cosmology.FLRW.eventHorizon`**, a def, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean#L240).

> The event horizon at `t`, the integral of `c / a` over the times of the interval of the
> model after `t`. It is a Lebesgue integral, equal to `0` when the integrand is not
> integrable.

```lean
noncomputable def eventHorizon (c : SpeedOfLight) (t : Time) : ℝ
```

**`Cosmology.FLRW.particleHorizon_einsteinDeSitter`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean#L244).

> The particle horizon of the Einstein-de Sitter model at `t > 0` is `3 c t₀^(2/3) t^(1/3)`.

```lean
lemma particleHorizon_einsteinDeSitter {t₀ : Time} {c : SpeedOfLight} (ht₀ : 0 < t₀.val)
    {t : Time} (ht : 0 < t.val) :
    (einsteinDeSitter t₀ ht₀).particleHorizon c t
      = 3 * (c : ℝ) * t₀.val ^ (2 / 3 : ℝ) * t.val ^ (1 / 3 : ℝ)
```

## Depends on

- [The Einstein-de Sitter model](specificcases-einsteindesitter.md)

## Sources

- [Physlib/Cosmology/FLRW/Distances.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Distances.lean)
