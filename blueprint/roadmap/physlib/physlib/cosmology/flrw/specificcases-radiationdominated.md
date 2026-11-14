---
declaration: module
origin: cited
lean: Cosmology.FLRW.radiationDominated, Cosmology.FLRW.radiationDominated_a, Cosmology.FLRW.friedmannSolution_radiationDominated
statement: formalized
proof: formalized
---

# The radiation-dominated model

The module `Physlib.Cosmology.FLRW.SpecificCases.RadiationDominated`, [Physlib/Cosmology/FLRW/SpecificCases/RadiationDominated.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/SpecificCases/RadiationDominated.lean): 3 declarations, 3 with a docstring.

## i. Overview

> The radiation-dominated solution `radiationScaleFactor t₀`, `a(t) = (t / t₀) ^ (1/2)`, of
> `Physlib.Cosmology.FLRW.Solutions` as an FLRW model: the flat power-law model of
> `Physlib.Cosmology.FLRW.SpecificCases.PowerLaw` with `n = 1/2`, on the interval `t > 0`. Filled
> with its cosmic fluid `CosmicFluid.powerLaw (1/2) (1/3) G c`, radiation of density
> `3 n² / (8 π G t²) = 3 / (32 π G t²)` with `n = 1/2` and pressure `ρ c² / 3`, it solves the
> Friedmann equations without cosmological constant.

## ii. Key results

> - `FLRW.radiationDominated`: the radiation-dominated model.
> - `FLRW.radiationDominated_a`: its scale factor is `radiationScaleFactor t₀`.
> - `FLRW.friedmannSolution_radiationDominated`: filled with radiation, it solves the Friedmann
>   equations.

## iv. References

> * None.

## A. The radiation-dominated model

**`Cosmology.FLRW.radiationDominated`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/SpecificCases/RadiationDominated.lean#L52).

> The radiation-dominated model, the flat power-law model with `n = 1/2`.

```lean
noncomputable def FLRW.radiationDominated (t₀ : Time) (ht₀ : 0 < t₀.val) : FLRW
```

**`Cosmology.FLRW.radiationDominated_a`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/SpecificCases/RadiationDominated.lean#L56).

> The scale factor of the radiation-dominated model is `radiationScaleFactor t₀`.

```lean
lemma FLRW.radiationDominated_a {t₀ : Time} (ht₀ : 0 < t₀.val) :
    (FLRW.radiationDominated t₀ ht₀).a = radiationScaleFactor t₀
```

**`Cosmology.FLRW.friedmannSolution_radiationDominated`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/SpecificCases/RadiationDominated.lean#L62).

> The radiation-dominated model, filled with radiation of density `3 n² / (8 π G t²)` with
> `n = 1/2`, that is `3 / (32 π G t²)`, and pressure `ρ c² / 3`, solves the Friedmann equations
> without cosmological constant on its interval.

```lean
lemma FLRW.friedmannSolution_radiationDominated {t₀ : Time} (ht₀ : 0 < t₀.val)
    {G : ℝ} {c : SpeedOfLight} (hG : 0 < G) :
    (FLRW.radiationDominated t₀ ht₀).FriedmannSolution
      (CosmicFluid.powerLaw (1 / 2) (1 / 3) G c) 0 G c
```

## Depends on

- [Exact solutions of the Friedmann equations](solutions.md)
- [The flat power-law models](specificcases-powerlaw.md)

## Sources

- [Physlib/Cosmology/FLRW/SpecificCases/RadiationDominated.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/SpecificCases/RadiationDominated.lean)
