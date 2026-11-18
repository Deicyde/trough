---
declaration: module
origin: cited
lean: Cosmology.FLRW.einsteinDeSitter, Cosmology.FLRW.einsteinDeSitter_a, Cosmology.FLRW.friedmannSolution_einsteinDeSitter
statement: formalized
proof: formalized
---

# The Einstein-de Sitter model

The module `Physlib.Cosmology.FLRW.SpecificCases.EinsteinDeSitter`, [Physlib/Cosmology/FLRW/SpecificCases/EinsteinDeSitter.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/SpecificCases/EinsteinDeSitter.lean): 3 declarations, 3 with a docstring.

## i. Overview

> The Einstein-de Sitter solution `einsteinDeSitterScaleFactor t₀`, `a(t) = (t / t₀) ^ (2/3)`, of
> `Physlib.Cosmology.FLRW.Solutions` as an FLRW model: the flat power-law model of
> `Physlib.Cosmology.FLRW.SpecificCases.PowerLaw` with `n = 2/3`, on the interval `t > 0`. Filled
> with its cosmic fluid `CosmicFluid.powerLaw (2/3) 0 G c`, dust of density
> `3 n² / (8 π G t²) = 1 / (6 π G t²)` with `n = 2/3` and zero pressure, it solves the Friedmann
> equations without cosmological constant.

## ii. Key results

> - `FLRW.einsteinDeSitter`: the Einstein-de Sitter model.
> - `FLRW.einsteinDeSitter_a`: its scale factor is `einsteinDeSitterScaleFactor t₀`.
> - `FLRW.friedmannSolution_einsteinDeSitter`: filled with dust, it solves the Friedmann
>   equations.

## iv. References

> * None.

## A. The Einstein-de Sitter model

**`Cosmology.FLRW.einsteinDeSitter`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/SpecificCases/EinsteinDeSitter.lean#L52).

> The Einstein-de Sitter model, the flat power-law model with `n = 2/3`.

```lean
noncomputable def FLRW.einsteinDeSitter (t₀ : Time) (ht₀ : 0 < t₀.val) : FLRW
```

**`Cosmology.FLRW.einsteinDeSitter_a`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/SpecificCases/EinsteinDeSitter.lean#L56).

> The scale factor of the Einstein-de Sitter model is `einsteinDeSitterScaleFactor t₀`.

```lean
lemma FLRW.einsteinDeSitter_a {t₀ : Time} (ht₀ : 0 < t₀.val) :
    (FLRW.einsteinDeSitter t₀ ht₀).a = einsteinDeSitterScaleFactor t₀
```

**`Cosmology.FLRW.friedmannSolution_einsteinDeSitter`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/SpecificCases/EinsteinDeSitter.lean#L62).

> The Einstein-de Sitter model, filled with dust of density `3 n² / (8 π G t²)` with `n = 2/3`,
> that is `1 / (6 π G t²)`, and zero pressure, solves the Friedmann equations without cosmological
> constant on its interval.

```lean
lemma FLRW.friedmannSolution_einsteinDeSitter {t₀ : Time} (ht₀ : 0 < t₀.val)
    {G : ℝ} {c : SpeedOfLight} (hG : 0 < G) :
    (FLRW.einsteinDeSitter t₀ ht₀).FriedmannSolution
      (CosmicFluid.powerLaw (2 / 3) 0 G c) 0 G c
```

## Depends on

- [Exact solutions of the Friedmann equations](solutions.md)
- [The flat power-law models](specificcases-powerlaw.md)

## Sources

- [Physlib/Cosmology/FLRW/SpecificCases/EinsteinDeSitter.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/SpecificCases/EinsteinDeSitter.lean)
