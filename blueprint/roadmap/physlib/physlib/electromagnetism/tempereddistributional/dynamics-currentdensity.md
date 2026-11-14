---
declaration: module
origin: cited
lean: Electromagnetism.TempDistLorentzCurrentDensity, Electromagnetism.TempDistLorentzCurrentDensity.chargeDensity, Electromagnetism.TempDistLorentzCurrentDensity.currentDensity
statement: formalized
proof: formalized
---

# The Lorentz Current Density (TemperedDistributional/Dynamics/CurrentDensity)

The module `Physlib.Electromagnetism.TemperedDistributional.Dynamics.CurrentDensity`, [Physlib/Electromagnetism/TemperedDistributional/Dynamics/CurrentDensity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/CurrentDensity.lean): 3 declarations, 3 with a docstring.

## i. Overview

> In this module we define the Lorentz current density
> and its decomposition into charge density and current density.
> The Lorentz current density is often called the four-current and given then the symbol `J`.
>
> The current density is given in terms of the charge density `ρ` and the current density
> ` \vec j` as `J = (c ρ, \vec j)`.

## ii. Key results

> - `TempDistLorentzCurrentDensity` : The type of Lorentz current densities
>   as distributions.

## iv. References

> * None.

## A. The Lorentz current density as a distribution

**`Electromagnetism.TempDistLorentzCurrentDensity`**, an abbrev, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/CurrentDensity.lean#L56).

> The Lorentz current density, also called four-current as a distribution.

```lean
abbrev TempDistLorentzCurrentDensity (d : ℕ := 3)
```

### A.1. The underlying charge density

**`Electromagnetism.TempDistLorentzCurrentDensity.chargeDensity`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/CurrentDensity.lean#L67).

> The charge density underlying a Lorentz current density which is a distribution.

```lean
noncomputable def chargeDensity {d : ℕ} (c : SpeedOfLight) :
    (TempDistLorentzCurrentDensity d) →ₗ[ℝ] (Time × Space d) →d[ℝ] ℝ
```

### A.2. The underlying current density

**`Electromagnetism.TempDistLorentzCurrentDensity.currentDensity`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/CurrentDensity.lean#L84).

> The underlying (non-Lorentz) current density associated with a distributive
> Lorentz current density.

```lean
noncomputable def currentDensity (c : SpeedOfLight) :
    TempDistLorentzCurrentDensity d →ₗ[ℝ] (Time × Space d) →d[ℝ] EuclideanSpace ℝ (Fin d)
```

## Depends on

- [Time slice](../../spaceandtime/spacetime/timeslice.md)

## Sources

- [Physlib/Electromagnetism/TemperedDistributional/Dynamics/CurrentDensity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/CurrentDensity.lean)
