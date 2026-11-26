---
declaration: module
origin: cited
lean: SpaceTime.timeSlice, SpaceTime.timeSlice_contDiff, SpaceTime.timeSlice_differentiable, SpaceTime.timeSlice_symm_contDiff, SpaceTime.timeSlice_symm_differentiable, SpaceTime.timeSliceLinearEquiv, SpaceTime.timeSliceLinearEquiv_apply, SpaceTime.timeSliceLinearEquiv_symm_apply
statement: formalized
proof: formalized
---

# Time slice

The module `Physlib.SpaceAndTime.SpaceTime.TimeSlice`, [Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean): 17 declarations, 4 with a docstring.

> Time slicing functions on spacetime, turning them into a function
> `Time → Space d → M`.
>
> This is useful when going from relativistic physics (defined using `SpaceTime`)
> to non-relativistic physics (defined using `Space` and `Time`).

**`SpaceTime.timeSlice`**, a def, [line 36](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L36).

> The timeslice of a function `SpaceTime d → M` forming a function
> `Time → Space d → M`.

```lean
def timeSlice {d : ℕ} {M : Type} (c : SpeedOfLight := 1) :
    (SpaceTime d → M) ≃ (Time → Space d → M)
```

**`SpaceTime.timeSlice_contDiff`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L48).

```lean
lemma timeSlice_contDiff {d : ℕ} {M : Type} [NormedAddCommGroup M]
    [NormedSpace ℝ M]
    {n} (c : SpeedOfLight) (f : SpaceTime d → M) (h : ContDiff ℝ n f) :
    ContDiff ℝ n ↿(timeSlice c f)
```

**`SpaceTime.timeSlice_differentiable`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L58).

```lean
lemma timeSlice_differentiable {d : ℕ} {M : Type} [NormedAddCommGroup M]
    [NormedSpace ℝ M] (c : SpeedOfLight)
    (f : SpaceTime d → M) (h : Differentiable ℝ f) :
    Differentiable ℝ ↿(timeSlice c f)
```

**`SpaceTime.timeSlice_symm_contDiff`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L68).

```lean
lemma timeSlice_symm_contDiff {d : ℕ} {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {n} (c : SpeedOfLight) (f : Time → Space d → M) (h : ContDiff ℝ n ↿f) :
    ContDiff ℝ n ((timeSlice c).symm f)
```

**`SpaceTime.timeSlice_symm_differentiable`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L77).

```lean
lemma timeSlice_symm_differentiable {d : ℕ} {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (c : SpeedOfLight)
    (f : Time → Space d → M) (h : Differentiable ℝ ↿f) :
    Differentiable ℝ ↿((timeSlice c).symm f)
```

**`SpaceTime.timeSliceLinearEquiv`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L88).

> The timeslice of a function `SpaceTime d → M` forming a function
> `Time → Space d → M`, as a linear equivalence.

```lean
def timeSliceLinearEquiv {d : ℕ} {M : Type} [AddCommGroup M] [Module ℝ M]
    (c : SpeedOfLight := 1) :
    (SpaceTime d → M) ≃ₗ[ℝ] (Time → Space d → M)
```

**`SpaceTime.timeSliceLinearEquiv_apply`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L103).

```lean
lemma timeSliceLinearEquiv_apply {d : ℕ} {M : Type} [AddCommGroup M] [Module ℝ M]
    (c : SpeedOfLight) (f : SpaceTime d → M) : timeSliceLinearEquiv c f = timeSlice c f
```

**`SpaceTime.timeSliceLinearEquiv_symm_apply`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L107).

```lean
lemma timeSliceLinearEquiv_symm_apply {d : ℕ} {M : Type} [AddCommGroup M] [Module ℝ M]
    (c : SpeedOfLight) (f : Time → Space d → M) :
    (timeSliceLinearEquiv c).symm f = (timeSlice c).symm f
```

## B. Time slices of distributions

**`SpaceTime.distTimeSlice`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L122).

> The time slice of a distribution on `SpaceTime d` to form a distribution
> on `Time × Space d`.

```lean
noncomputable def distTimeSlice{F} [NormedAddCommGroup F] [NormedSpace ℝ F]
    (c : SpeedOfLight := 1) :
    Distribution (⟨Set.univ (α := SpaceTime d), isOpen_univ⟩) F ⊤ ≃L[ℝ]
    Distribution (⟨Set.univ (α := Time × Space d), isOpen_univ⟩) F ⊤
```

**`SpaceTime.tempDistTimeSlice`**, a def, [line 146](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L146).

> The time slice of a tempered distribution on `SpaceTime d` to form a distribution
> on `Time × Space d`.

```lean
noncomputable def tempDistTimeSlice {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (c : SpeedOfLight := 1) :
    ((SpaceTime d) →d[ℝ] M) ≃L[ℝ] ((Time × Space d) →d[ℝ] M)
```

**`SpaceTime.tempDistTimeSlice_apply`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L172).

```lean
lemma tempDistTimeSlice_apply {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (c : SpeedOfLight) (f : (SpaceTime d) →d[ℝ] M)
    (κ : 𝓢(Time × Space d, ℝ)) : tempDistTimeSlice c f κ =
    f (compCLMOfContinuousLinearEquiv ℝ (toTimeAndSpace c) κ)
```

**`SpaceTime.tempDistTimeSlice_symm_apply`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L177).

```lean
lemma tempDistTimeSlice_symm_apply {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (c : SpeedOfLight) (f : (Time × (Space d)) →d[ℝ] M)
    (κ : 𝓢(SpaceTime d, ℝ)) : (tempDistTimeSlice c).symm f κ =
    f (compCLMOfContinuousLinearEquiv ℝ (toTimeAndSpace c).symm κ)
```

### B.1. Time slices and derivatives

**`SpaceTime.distTimeSlice_distDeriv_inl`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L188).

```lean
lemma distTimeSlice_distDeriv_inl {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {c : SpeedOfLight}
    (f : (SpaceTime d) →d[ℝ] M) :
    tempDistTimeSlice c (distDeriv (Sum.inl 0) f) =
    (1/c.val) • Space.distTimeDeriv (tempDistTimeSlice c f)
```

**`SpaceTime.distDeriv_inl_distTimeSlice_symm`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L213).

```lean
lemma distDeriv_inl_distTimeSlice_symm {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {c : SpeedOfLight}
    (f : (Time × Space d) →d[ℝ] M) :
    distDeriv (Sum.inl 0) ((tempDistTimeSlice c).symm f) =
    (1/c.val) • (tempDistTimeSlice c).symm (Space.distTimeDeriv f)
```

**`SpaceTime.distTimeSlice_symm_distTimeDeriv_eq`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L225).

```lean
lemma distTimeSlice_symm_distTimeDeriv_eq {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {c : SpeedOfLight}
    (f : (Time × Space d) →d[ℝ] M) :
    (tempDistTimeSlice c).symm (Space.distTimeDeriv f) =
    c.val • distDeriv (Sum.inl 0) ((tempDistTimeSlice c).symm f)
```

**`SpaceTime.distTimeSlice_distDeriv_inr`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L233).

```lean
lemma distTimeSlice_distDeriv_inr {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {c : SpeedOfLight}
    (i : Fin d) (f : (SpaceTime d) →d[ℝ] M) :
    tempDistTimeSlice c (distDeriv (Sum.inr i) f) =
    Space.distSpaceDeriv i (tempDistTimeSlice c f)
```

**`SpaceTime.distDeriv_inr_distTimeSlice_symm`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L254).

```lean
lemma distDeriv_inr_distTimeSlice_symm {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {c : SpeedOfLight}
    (i : Fin d) (f : (Time × Space d) →d[ℝ] M) :
    distDeriv (Sum.inr i) ((tempDistTimeSlice c).symm f) =
    (tempDistTimeSlice c).symm (Space.distSpaceDeriv i f)
```

## Depends on

- [Distribution](../../mathematics/formathlib/part-01/distribution.md)
- [Derivatives on SpaceTime](derivatives.md)
- [Functions and distributions on Time and Space d](../timeandspace/basic.md)

## Sources

- [Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean)
