---
declaration: module
origin: cited
lean: Cosmology.FLRW.powerLaw, Cosmology.CosmicFluid.powerLaw, Cosmology.FLRW.friedmannSolution_powerLaw
statement: formalized
proof: formalized
---

# The flat power-law models

The module `Physlib.Cosmology.FLRW.SpecificCases.PowerLaw`, [Physlib/Cosmology/FLRW/SpecificCases/PowerLaw.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/SpecificCases/PowerLaw.lean): 3 declarations, 3 with a docstring.

## i. Overview

> The spatially flat power-law solutions `a(t) = (t / t₀) ^ n` of `Physlib.Cosmology.FLRW.Solutions`
> as FLRW models. The model `FLRW.powerLaw t₀ ht₀ n` lives on the interval `t > 0`, after the
> origin `t.val = 0` of the time chart (for `n > 0`, the Big Bang, where the scale factor vanishes),
> for a normalisation epoch `t₀ > 0`, and has flat spatial slices. Filled with the cosmic fluid
> `CosmicFluid.powerLaw n w G c`, of density `3 n² / (8 π G t²)` and pressure `w ρ c²`, it solves
> the Friedmann equations without cosmological constant when `n ≠ 0` and
> `1 + 3 w = 2 (1 - n) / n`. The radiation-dominated and Einstein-de Sitter models, the
> cases `n = 1/2` and `n = 2/3`, are in `Physlib.Cosmology.FLRW.SpecificCases.RadiationDominated`
> and `Physlib.Cosmology.FLRW.SpecificCases.EinsteinDeSitter`.

## ii. Key results

> - `FLRW.powerLaw`: the flat power-law model on the interval `t > 0`.
> - `CosmicFluid.powerLaw`: the cosmic fluid of the flat power-law solution.
> - `FLRW.friedmannSolution_powerLaw`: the model filled with this fluid solves the Friedmann
>   equations.

## iv. References

> * None.

## A. The power-law model

**`Cosmology.FLRW.powerLaw`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/SpecificCases/PowerLaw.lean#L58).

> The spatially flat power-law model `a(t) = (t / t₀) ^ n` on the interval `t > 0`, after the
> origin `t.val = 0` of the time chart (for `n > 0`, the Big Bang), for a normalisation epoch
> `t₀ > 0`.

```lean
noncomputable def FLRW.powerLaw (t₀ : Time) (ht₀ : 0 < t₀.val) (n : ℝ) : FLRW
```

## B. The cosmic fluid and the Friedmann equations

**`Cosmology.CosmicFluid.powerLaw`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/SpecificCases/PowerLaw.lean#L88).

> The cosmic fluid of the flat power-law solution: the density `ρ = 3 n² / (8 π G t²)` imposed by
> the first-order Friedmann equation, and the pressure `p = w ρ c²`.

```lean
noncomputable def CosmicFluid.powerLaw (n w G : ℝ) (c : SpeedOfLight) : CosmicFluid
```

**`Cosmology.FLRW.friedmannSolution_powerLaw`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/SpecificCases/PowerLaw.lean#L95).

> The flat power-law model with `n ≠ 0`, filled with the fluid `CosmicFluid.powerLaw n w G c`
> where `1 + 3 w = 2 (1 - n) / n`, solves the Friedmann equations without cosmological constant on
> its interval `t > 0`.

```lean
lemma FLRW.friedmannSolution_powerLaw {t₀ : Time} (ht₀ : 0 < t₀.val)
    {n w G : ℝ} {c : SpeedOfLight} (hG : 0 < G) (hn : n ≠ 0) (hw : 1 + 3 * w = 2 * (1 - n) / n) :
    (FLRW.powerLaw t₀ ht₀ n).FriedmannSolution (CosmicFluid.powerLaw n w G c) 0 G c
```

## Depends on

- [The Friedmann-Lemaître-Robertson-Walker metric](basic.md)

## Proof depends on

- [Exact solutions of the Friedmann equations](solutions.md)

## Sources

- [Physlib/Cosmology/FLRW/SpecificCases/PowerLaw.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/SpecificCases/PowerLaw.lean)
