---
declaration: module
origin: cited
lean: Electromagnetism.LorentzCurrentDensity, Electromagnetism.LorentzCurrentDensity.chargeDensity, Electromagnetism.LorentzCurrentDensity.chargeDensity_eq_timeSlice, Electromagnetism.LorentzCurrentDensity.chargeDensity_zero, Electromagnetism.LorentzCurrentDensity.chargeDensity_differentiable, Electromagnetism.LorentzCurrentDensity.chargeDensity_differentiable_space, Electromagnetism.LorentzCurrentDensity.chargeDensity_contDiff, Electromagnetism.LorentzCurrentDensity.currentDensity
statement: formalized
proof: formalized
---

# The Lorentz Current Density (Electromagnetism/Dynamics/CurrentDensity)

The module `Physlib.Electromagnetism.Dynamics.CurrentDensity`, [Physlib/Electromagnetism/Dynamics/CurrentDensity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/CurrentDensity.lean): 17 declarations, 3 with a docstring.

## i. Overview

> In this module we define the Lorentz current density
> and its decomposition into charge density and current density.
> The Lorentz current density is often called the four-current and given then the symbol `J`.
>
> The current density is given in terms of the charge density `ρ` and the current density
> ` \vec j` as `J = (c ρ, \vec j)`.

## ii. Key results

> - `LorentzCurrentDensity` : The type of Lorentz current densities.
> - `LorentzCurrentDensity.chargeDensity` : The charge density associated with a
>   Lorentz current density.
> - `LorentzCurrentDensity.currentDensity` : The current density associated with a
>   Lorentz current density.

## iv. References

> * None.

## A. The Lorentz Current Density

> The Lorentz current density is a Lorentz Vector field on spacetime.

**`Electromagnetism.LorentzCurrentDensity`**, an abbrev, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/CurrentDensity.lean#L68).

> The Lorentz current density, also called four-current.

```lean
abbrev LorentzCurrentDensity (d : ℕ := 3)
```

## B. The underlying charge

**`Electromagnetism.LorentzCurrentDensity.chargeDensity`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/CurrentDensity.lean#L79).

> The underlying charge density associated with a Lorentz current density.

```lean
noncomputable def chargeDensity (c : SpeedOfLight := 1)
    (J : LorentzCurrentDensity d) : Time → Space d → ℝ
```

**`Electromagnetism.LorentzCurrentDensity.chargeDensity_eq_timeSlice`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/CurrentDensity.lean#L83).

```lean
lemma chargeDensity_eq_timeSlice {d : ℕ} {c : SpeedOfLight} {J : LorentzCurrentDensity d} :
    J.chargeDensity c = timeSlice c (fun x => (1 / (c : ℝ)) • J x (Sum.inl 0))
```

### B.1. Charge density of zero Lorentz current density

**`Electromagnetism.LorentzCurrentDensity.chargeDensity_zero`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/CurrentDensity.lean#L93).

```lean
lemma chargeDensity_zero {d : ℕ} {c : SpeedOfLight}:
    chargeDensity c (0 : LorentzCurrentDensity d) = 0
```

### B.2. Differentiability of the charge density

**`Electromagnetism.LorentzCurrentDensity.chargeDensity_differentiable`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/CurrentDensity.lean#L103).

```lean
lemma chargeDensity_differentiable {d : ℕ} {c : SpeedOfLight} {J : LorentzCurrentDensity d}
    (hJ : Differentiable ℝ J) : Differentiable ℝ ↿(J.chargeDensity c)
```

**`Electromagnetism.LorentzCurrentDensity.chargeDensity_differentiable_space`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/CurrentDensity.lean#L113).

```lean
lemma chargeDensity_differentiable_space {d : ℕ} {c : SpeedOfLight} {J : LorentzCurrentDensity d}
    (hJ : Differentiable ℝ J) (t : Time) :
    Differentiable ℝ (fun x => J.chargeDensity c t x)
```

### B.3. Smoothness of the charge density

**`Electromagnetism.LorentzCurrentDensity.chargeDensity_contDiff`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/CurrentDensity.lean#L127).

```lean
lemma chargeDensity_contDiff {d : ℕ} {c : SpeedOfLight} {J : LorentzCurrentDensity d}
    (hJ : ContDiff ℝ n J) : ContDiff ℝ n ↿(J.chargeDensity c)
```

## C. The underlying current density

**`Electromagnetism.LorentzCurrentDensity.currentDensity`**, a def, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/CurrentDensity.lean#L144).

> The underlying (non-Lorentz) current density associated with a Lorentz current density.

```lean
noncomputable def currentDensity (c : SpeedOfLight := 1) (J : LorentzCurrentDensity d) :
    Time → Space d → EuclideanSpace ℝ (Fin d)
```

**`Electromagnetism.LorentzCurrentDensity.currentDensity_eq_timeSlice`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/CurrentDensity.lean#L148).

```lean
lemma currentDensity_eq_timeSlice {d : ℕ} {J : LorentzCurrentDensity d} :
    J.currentDensity c = timeSlice c (fun x => WithLp.toLp 2
      fun i => J x (Sum.inr i))
```

### C.1. current density of zero Lorentz current density

**`Electromagnetism.LorentzCurrentDensity.currentDensity_zero`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/CurrentDensity.lean#L159).

```lean
lemma currentDensity_zero {d : ℕ} {c : SpeedOfLight}:
    currentDensity c (0 : LorentzCurrentDensity d) = 0
```

### C.2. Differentiability of the current density

**`Electromagnetism.LorentzCurrentDensity.currentDensity_differentiable`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/CurrentDensity.lean#L169).

```lean
lemma currentDensity_differentiable {d : ℕ} {c : SpeedOfLight} {J : LorentzCurrentDensity d}
    (hJ : Differentiable ℝ J) : Differentiable ℝ ↿(J.currentDensity c)
```

**`Electromagnetism.LorentzCurrentDensity.currentDensity_apply_differentiable`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/CurrentDensity.lean#L178).

```lean
lemma currentDensity_apply_differentiable {d : ℕ} {c : SpeedOfLight} {J : LorentzCurrentDensity d}
    (hJ : Differentiable ℝ J) (i : Fin d) :
    Differentiable ℝ ↿(fun t x => J.currentDensity c t x i)
```

**`Electromagnetism.LorentzCurrentDensity.currentDensity_differentiable_space`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/CurrentDensity.lean#L186).

```lean
lemma currentDensity_differentiable_space {d : ℕ} {c : SpeedOfLight} {J : LorentzCurrentDensity d}
    (hJ : Differentiable ℝ J) (t : Time) :
    Differentiable ℝ (fun x => J.currentDensity c t x)
```

**`Electromagnetism.LorentzCurrentDensity.currentDensity_apply_differentiable_space`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/CurrentDensity.lean#L194).

```lean
lemma currentDensity_apply_differentiable_space {d : ℕ} {c : SpeedOfLight}
    {J : LorentzCurrentDensity d}
    (hJ : Differentiable ℝ J) (t : Time) (i : Fin d) :
    Differentiable ℝ (fun x => J.currentDensity c t x i)
```

**`Electromagnetism.LorentzCurrentDensity.currentDensity_differentiable_time`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/CurrentDensity.lean#L205).

```lean
lemma currentDensity_differentiable_time {d : ℕ} {c : SpeedOfLight} {J : LorentzCurrentDensity d}
    (hJ : Differentiable ℝ J) (x : Space d) :
    Differentiable ℝ (fun t => J.currentDensity c t x)
```

**`Electromagnetism.LorentzCurrentDensity.currentDensity_apply_differentiable_time`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/CurrentDensity.lean#L213).

```lean
lemma currentDensity_apply_differentiable_time {d : ℕ} {c : SpeedOfLight}
    {J : LorentzCurrentDensity d}
    (hJ : Differentiable ℝ J) (x : Space d) (i : Fin d) :
    Differentiable ℝ (fun t => J.currentDensity c t x i)
```

### C.3. Smoothness of the current density

**`Electromagnetism.LorentzCurrentDensity.currentDensity_ContDiff`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/CurrentDensity.lean#L230).

```lean
lemma currentDensity_ContDiff {d : ℕ} {c : SpeedOfLight} {J : LorentzCurrentDensity d}
    (hJ : ContDiff ℝ n J) : ContDiff ℝ n ↿(J.currentDensity c)
```

## Depends on

- [Time slice](../../spaceandtime/spacetime/timeslice.md)

## Sources

- [Physlib/Electromagnetism/Dynamics/CurrentDensity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/CurrentDensity.lean)
