---
declaration: module
origin: cited
lean: Cosmology.FLRW.FriedmannEquation.age, Cosmology.FLRW.FriedmannEquation.age_eq
statement: formalized
proof: formalized
---

# The age of the universe

The module `Physlib.Cosmology.FLRW.Age`, [Physlib/Cosmology/FLRW/Age.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Age.lean): 2 declarations, 2 with a docstring.

## i. Overview

> Integrating `dt = da / (a H)` from `a = 0` to the present value of the scale factor, with
> `H = H₀ E(a / a₀)` for a reduced Hubble function `E` (for instance `reducedHubble` of
> `Physlib.Cosmology.FLRW.ReducedHubble`), gives the age of the universe
> `t₀ = H₀⁻¹ ∫₀¹ dx / (x E(x))`. It is proportional to `1 / H₀`: the dimensionless integral depends
> only on the shape of `E`.
>
> The age is defined here for an arbitrary function `E`, as an interval integral; no convergence
> is asserted.

## ii. Key results

> - `age`: `t₀ = H₀⁻¹ ∫₀¹ dx / (x E(x))`.
> - `age_eq`: `t₀ ∝ 1 / H₀`.

## iv. References

> * None.

## A. The age of the universe

**`Cosmology.FLRW.FriedmannEquation.age`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Age.lean#L52).

> The age of the universe `t₀ = H₀⁻¹ ∫₀¹ dx / (x E(x))` for a reduced Hubble function `E`:
> the time elapsed since `a = 0`, obtained by integrating `dt = da / (a H)` with
> `H = H₀ E(a / a₀)` (interval integral; no convergence is asserted here).

```lean
noncomputable def age (H₀ : ℝ) (E : ℝ → ℝ) : ℝ
```

**`Cosmology.FLRW.FriedmannEquation.age_eq`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Age.lean#L56).

> The age is proportional to `1 / H₀`.

```lean
lemma age_eq (H₀ : ℝ) (E : ℝ → ℝ) : age H₀ E = (1 / H₀) * age 1 E
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Cosmology/FLRW/Age.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Age.lean)
