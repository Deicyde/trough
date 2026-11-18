---
declaration: module
origin: cited
lean: SpaceTime.timeSlice, SpaceTime.timeSlice_contDiff, SpaceTime.timeSlice_differentiable, SpaceTime.timeSlice_symm_contDiff, SpaceTime.timeSlice_symm_differentiable, SpaceTime.timeSliceLinearEquiv, SpaceTime.timeSliceLinearEquiv_apply, SpaceTime.timeSliceLinearEquiv_symm_apply
statement: formalized
proof: formalized
---

# Time slice

The module `Physlib.SpaceAndTime.SpaceTime.TimeSlice`, [Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean): 16 declarations, 3 with a docstring.

> Time slicing functions on spacetime, turning them into a function
> `Time → Space d → M`.
>
> This is useful when going from relativistic physics (defined using `SpaceTime`)
> to non-relativistic physics (defined using `Space` and `Time`).

**`SpaceTime.timeSlice`**, a def, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L34).

> The timeslice of a function `SpaceTime d → M` forming a function
> `Time → Space d → M`.

```lean
def timeSlice {d : ℕ} {M : Type} (c : SpeedOfLight := 1) :
    (SpaceTime d → M) ≃ (Time → Space d → M)
```

**`SpaceTime.timeSlice_contDiff`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L46).

```lean
lemma timeSlice_contDiff {d : ℕ} {M : Type} [NormedAddCommGroup M]
    [NormedSpace ℝ M]
    {n} (c : SpeedOfLight) (f : SpaceTime d → M) (h : ContDiff ℝ n f) :
    ContDiff ℝ n ↿(timeSlice c f)
```

**`SpaceTime.timeSlice_differentiable`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L56).

```lean
lemma timeSlice_differentiable {d : ℕ} {M : Type} [NormedAddCommGroup M]
    [NormedSpace ℝ M] (c : SpeedOfLight)
    (f : SpaceTime d → M) (h : Differentiable ℝ f) :
    Differentiable ℝ ↿(timeSlice c f)
```

**`SpaceTime.timeSlice_symm_contDiff`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L66).

```lean
lemma timeSlice_symm_contDiff {d : ℕ} {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {n} (c : SpeedOfLight) (f : Time → Space d → M) (h : ContDiff ℝ n ↿f) :
    ContDiff ℝ n ((timeSlice c).symm f)
```

**`SpaceTime.timeSlice_symm_differentiable`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L75).

```lean
lemma timeSlice_symm_differentiable {d : ℕ} {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (c : SpeedOfLight)
    (f : Time → Space d → M) (h : Differentiable ℝ ↿f) :
    Differentiable ℝ ↿((timeSlice c).symm f)
```

**`SpaceTime.timeSliceLinearEquiv`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L86).

> The timeslice of a function `SpaceTime d → M` forming a function
> `Time → Space d → M`, as a linear equivalence.

```lean
def timeSliceLinearEquiv {d : ℕ} {M : Type} [AddCommGroup M] [Module ℝ M]
    (c : SpeedOfLight := 1) :
    (SpaceTime d → M) ≃ₗ[ℝ] (Time → Space d → M)
```

**`SpaceTime.timeSliceLinearEquiv_apply`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L101).

```lean
lemma timeSliceLinearEquiv_apply {d : ℕ} {M : Type} [AddCommGroup M] [Module ℝ M]
    (c : SpeedOfLight) (f : SpaceTime d → M) : timeSliceLinearEquiv c f = timeSlice c f
```

**`SpaceTime.timeSliceLinearEquiv_symm_apply`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L105).

```lean
lemma timeSliceLinearEquiv_symm_apply {d : ℕ} {M : Type} [AddCommGroup M] [Module ℝ M]
    (c : SpeedOfLight) (f : Time → Space d → M) :
    (timeSliceLinearEquiv c).symm f = (timeSlice c).symm f
```

## B. Time slices of distributions

**`SpaceTime.distTimeSlice`**, a def, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L119).

> The time slice of a distribution on `SpaceTime d` to form a distribution
> on `Time × Space d`.

```lean
noncomputable def distTimeSlice {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (c : SpeedOfLight := 1) :
    ((SpaceTime d) →d[ℝ] M) ≃L[ℝ] ((Time × Space d) →d[ℝ] M)
```

**`SpaceTime.distTimeSlice_apply`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L145).

```lean
lemma distTimeSlice_apply {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (c : SpeedOfLight) (f : (SpaceTime d) →d[ℝ] M)
    (κ : 𝓢(Time × Space d, ℝ)) : distTimeSlice c f κ =
    f (compCLMOfContinuousLinearEquiv ℝ (toTimeAndSpace c) κ)
```

**`SpaceTime.distTimeSlice_symm_apply`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L150).

```lean
lemma distTimeSlice_symm_apply {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (c : SpeedOfLight) (f : (Time × (Space d)) →d[ℝ] M)
    (κ : 𝓢(SpaceTime d, ℝ)) : (distTimeSlice c).symm f κ =
    f (compCLMOfContinuousLinearEquiv ℝ (toTimeAndSpace c).symm κ)
```

### B.1. Time slices and derivatives

**`SpaceTime.distTimeSlice_distDeriv_inl`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L161).

```lean
lemma distTimeSlice_distDeriv_inl {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {c : SpeedOfLight}
    (f : (SpaceTime d) →d[ℝ] M) :
    distTimeSlice c (distDeriv (Sum.inl 0) f) =
    (1/c.val) • Space.distTimeDeriv (distTimeSlice c f)
```

**`SpaceTime.distDeriv_inl_distTimeSlice_symm`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L186).

```lean
lemma distDeriv_inl_distTimeSlice_symm {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {c : SpeedOfLight}
    (f : (Time × Space d) →d[ℝ] M) :
    distDeriv (Sum.inl 0) ((distTimeSlice c).symm f) =
    (1/c.val) • (distTimeSlice c).symm (Space.distTimeDeriv f)
```

**`SpaceTime.distTimeSlice_symm_distTimeDeriv_eq`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L198).

```lean
lemma distTimeSlice_symm_distTimeDeriv_eq {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {c : SpeedOfLight}
    (f : (Time × Space d) →d[ℝ] M) :
    (distTimeSlice c).symm (Space.distTimeDeriv f) =
    c.val • distDeriv (Sum.inl 0) ((distTimeSlice c).symm f)
```

**`SpaceTime.distTimeSlice_distDeriv_inr`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L206).

```lean
lemma distTimeSlice_distDeriv_inr {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {c : SpeedOfLight}
    (i : Fin d) (f : (SpaceTime d) →d[ℝ] M) :
    distTimeSlice c (distDeriv (Sum.inr i) f) =
    Space.distSpaceDeriv i (distTimeSlice c f)
```

**`SpaceTime.distDeriv_inr_distTimeSlice_symm`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L227).

```lean
lemma distDeriv_inr_distTimeSlice_symm {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {c : SpeedOfLight}
    (i : Fin d) (f : (Time × Space d) →d[ℝ] M) :
    distDeriv (Sum.inr i) ((distTimeSlice c).symm f) =
    (distTimeSlice c).symm (Space.distSpaceDeriv i f)
```

## Depends on

- [Derivatives on SpaceTime](derivatives.md)
- [Functions and distributions on Time and Space d](../timeandspace/basic.md)

## Sources

- [Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean)
