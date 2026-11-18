---
declaration: module
origin: cited
lean: Space.sphericalShell, Space.sphericalShell_injective, Space.sphericalShell_continuous, Space.sphericalShell_measurableEmbedding, Space.norm_sphericalShell, Space.sphericalShellMeasure, Space.sphericalShellMeasure_hasTemperateGrowth, Space.sphericalShellDist
statement: formalized
proof: formalized
---

# Spherical surfaces on Space

The module `PhyslibAlpha.SpaceAndTime.Space.Surfaces.SphericalShell`, [PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalShell.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalShell.lean): 10 declarations, 3 with a docstring.

> The unit sphere in `Space d` with its measure and the distribution of integration over it.

## i. Overview

> The spherical shell is the unit sphere `S^{d-1}` of `Space d`, included by `sphericalShell d`.
> Pushing forward the sphere measure gives `sphericalShellMeasure d`, and integrating against it
> gives the distribution `sphericalShellDist d`, which one can roughly think of as taking a test
> function to its integral against a mass, charge or current distribution on the shell.

## ii. Key results

> - `sphericalShell` : the inclusion of the unit sphere into `Space d`.
> - `sphericalShellMeasure` : the measure corresponding to integration over the spherical shell.
> - `sphericalShellDist` : the distribution corresponding to integration over the spherical shell.

## iv. References

> * None.

## A. The definition of the spherical shell surface

**`Space.sphericalShell`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalShell.lean#L58).

> The inclusion into `Space d` of its unit sphere `S^{d-1}` (the subtype coercion `x ↦ x.1`).

```lean
def sphericalShell (d : ℕ) : Metric.sphere (0 : Space d) 1 → Space d
```

**`Space.sphericalShell_injective`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalShell.lean#L60).

```lean
lemma sphericalShell_injective (d : ℕ) : Function.Injective (sphericalShell d)
```

**`Space.sphericalShell_continuous`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalShell.lean#L65).

```lean
lemma sphericalShell_continuous (d : ℕ) : Continuous (sphericalShell d)
```

**`Space.sphericalShell_measurableEmbedding`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalShell.lean#L67).

```lean
lemma sphericalShell_measurableEmbedding (d : ℕ) : MeasurableEmbedding (sphericalShell d)
```

**`Space.norm_sphericalShell`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalShell.lean#L73).

```lean
lemma norm_sphericalShell (d : ℕ) (x : Metric.sphere (0 : Space d) 1) :
    ‖sphericalShell d x‖ = 1
```

## B. The measure associated with the spherical shell

**`Space.sphericalShellMeasure`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalShell.lean#L84).

> The measure on `Space d` corresponding to integration around a spherical shell.

```lean
def sphericalShellMeasure (d : ℕ) : Measure (Space d)
```

**`Space.sphericalShellMeasure_hasTemperateGrowth`**, an instance, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalShell.lean#L87).

```lean
instance sphericalShellMeasure_hasTemperateGrowth (d : ℕ) :
    (sphericalShellMeasure d).HasTemperateGrowth
```

## C. The distribution associated with the spherical shell

**`Space.sphericalShellDist`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalShell.lean#L104).

> The distribution associated with a spherical shell.
> One can roughly think of this distribution as the distribution which
> takes test functions `f (r)` to `∫ d³r f(r) ρ(r)` where `ρ(r)` is the
> mass, charge or current etc. distribution.

```lean
def sphericalShellDist (d : ℕ) : (Space d) →d[ℝ] ℝ
```

**`Space.sphericalShellDist_apply_eq_integral_sphericalShellMeasure`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalShell.lean#L108).

```lean
lemma sphericalShellDist_apply_eq_integral_sphericalShellMeasure (d : ℕ) (f : 𝓢(Space d, ℝ)) :
    sphericalShellDist d f = ∫ x, f x ∂sphericalShellMeasure d
```

**`Space.sphericalShellDist_apply_eq_integral_sphere_volume`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalShell.lean#L112).

```lean
lemma sphericalShellDist_apply_eq_integral_sphere_volume (d : ℕ) (f : 𝓢(Space d, ℝ)) :
    sphericalShellDist d f =
    ∫ x, f (sphericalShell d x) ∂(MeasureTheory.Measure.toSphere volume)
```

## Depends on

- [Distributions](../../../physlib/mathematics/distribution/tempereddistribution.md)
- [The structure of a module on Space](../../../physlib/spaceandtime/space/part-01/module.md)

## Sources

- [PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalShell.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/Space/Surfaces/SphericalShell.lean)
