---
declaration: module
origin: cited
lean: SpaceTime.timeSlice, SpaceTime.timeSlice_contDiff, SpaceTime.timeSlice_differentiable, SpaceTime.timeSlice_symm_contDiff, SpaceTime.timeSlice_symm_differentiable, SpaceTime.timeSliceLinearEquiv, SpaceTime.timeSliceLinearEquiv_apply, SpaceTime.timeSliceLinearEquiv_symm_apply
statement: formalized
proof: formalized
---

# Time slice

The module `Physlib.SpaceAndTime.SpaceTime.TimeSlice`, [Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean): 17 declarations, 4 with a docstring.

> Time slicing functions on spacetime, turning them into a function
> `Time → Space d → M`.
>
> This is useful when going from relativistic physics (defined using `SpaceTime`)
> to non-relativistic physics (defined using `Space` and `Time`).

**`SpaceTime.timeSlice`**, a def, [line 35](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L35).

> The timeslice of a function `SpaceTime d → M` forming a function
> `Time → Space d → M`.

```lean
def timeSlice {d : ℕ} {M : Type} (c : SpeedOfLight := 1) :
    (SpaceTime d → M) ≃ (Time → Space d → M)
```

**`SpaceTime.timeSlice_contDiff`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L47).

```lean
lemma timeSlice_contDiff {d : ℕ} {M : Type} [NormedAddCommGroup M]
    [NormedSpace ℝ M]
    {n} (c : SpeedOfLight) (f : SpaceTime d → M) (h : ContDiff ℝ n f) :
    ContDiff ℝ n ↿(timeSlice c f)
```

**`SpaceTime.timeSlice_differentiable`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L57).

```lean
lemma timeSlice_differentiable {d : ℕ} {M : Type} [NormedAddCommGroup M]
    [NormedSpace ℝ M] (c : SpeedOfLight)
    (f : SpaceTime d → M) (h : Differentiable ℝ f) :
    Differentiable ℝ ↿(timeSlice c f)
```

**`SpaceTime.timeSlice_symm_contDiff`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L67).

```lean
lemma timeSlice_symm_contDiff {d : ℕ} {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {n} (c : SpeedOfLight) (f : Time → Space d → M) (h : ContDiff ℝ n ↿f) :
    ContDiff ℝ n ((timeSlice c).symm f)
```

**`SpaceTime.timeSlice_symm_differentiable`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L76).

```lean
lemma timeSlice_symm_differentiable {d : ℕ} {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (c : SpeedOfLight)
    (f : Time → Space d → M) (h : Differentiable ℝ ↿f) :
    Differentiable ℝ ↿((timeSlice c).symm f)
```

**`SpaceTime.timeSliceLinearEquiv`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L87).

> The timeslice of a function `SpaceTime d → M` forming a function
> `Time → Space d → M`, as a linear equivalence.

```lean
def timeSliceLinearEquiv {d : ℕ} {M : Type} [AddCommGroup M] [Module ℝ M]
    (c : SpeedOfLight := 1) :
    (SpaceTime d → M) ≃ₗ[ℝ] (Time → Space d → M)
```

**`SpaceTime.timeSliceLinearEquiv_apply`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L102).

```lean
lemma timeSliceLinearEquiv_apply {d : ℕ} {M : Type} [AddCommGroup M] [Module ℝ M]
    (c : SpeedOfLight) (f : SpaceTime d → M) : timeSliceLinearEquiv c f = timeSlice c f
```

**`SpaceTime.timeSliceLinearEquiv_symm_apply`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L106).

```lean
lemma timeSliceLinearEquiv_symm_apply {d : ℕ} {M : Type} [AddCommGroup M] [Module ℝ M]
    (c : SpeedOfLight) (f : Time → Space d → M) :
    (timeSliceLinearEquiv c).symm f = (timeSlice c).symm f
```

## B. Time slices of distributions

**`SpaceTime.distTimeSlice`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L121).

> The time slice of a distribution on `SpaceTime d` to form a distribution
> on `Time × Space d`.

```lean
noncomputable def distTimeSlice{F} [NormedAddCommGroup F] [NormedSpace ℝ F]
    (c : SpeedOfLight := 1) :
    Distribution (⟨Set.univ (α := SpaceTime d), isOpen_univ⟩) F ⊤ →L[ℝ]
    Distribution (⟨Set.univ (α := Time × Space d), isOpen_univ⟩) F ⊤
```

**`SpaceTime.tempDistTimeSlice`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L129).

> The time slice of a tempered distribution on `SpaceTime d` to form a distribution
> on `Time × Space d`.

```lean
noncomputable def tempDistTimeSlice {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (c : SpeedOfLight := 1) :
    ((SpaceTime d) →d[ℝ] M) ≃L[ℝ] ((Time × Space d) →d[ℝ] M)
```

**`SpaceTime.distTimeSlice_apply`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L155).

```lean
lemma distTimeSlice_apply {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (c : SpeedOfLight) (f : (SpaceTime d) →d[ℝ] M)
    (κ : 𝓢(Time × Space d, ℝ)) : tempDistTimeSlice c f κ =
    f (compCLMOfContinuousLinearEquiv ℝ (toTimeAndSpace c) κ)
```

**`SpaceTime.distTimeSlice_symm_apply`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L160).

```lean
lemma distTimeSlice_symm_apply {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (c : SpeedOfLight) (f : (Time × (Space d)) →d[ℝ] M)
    (κ : 𝓢(SpaceTime d, ℝ)) : (tempDistTimeSlice c).symm f κ =
    f (compCLMOfContinuousLinearEquiv ℝ (toTimeAndSpace c).symm κ)
```

### B.1. Time slices and derivatives

**`SpaceTime.distTimeSlice_distDeriv_inl`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L171).

```lean
lemma distTimeSlice_distDeriv_inl {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {c : SpeedOfLight}
    (f : (SpaceTime d) →d[ℝ] M) :
    tempDistTimeSlice c (distDeriv (Sum.inl 0) f) =
    (1/c.val) • Space.distTimeDeriv (tempDistTimeSlice c f)
```

**`SpaceTime.distDeriv_inl_distTimeSlice_symm`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L196).

```lean
lemma distDeriv_inl_distTimeSlice_symm {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {c : SpeedOfLight}
    (f : (Time × Space d) →d[ℝ] M) :
    distDeriv (Sum.inl 0) ((tempDistTimeSlice c).symm f) =
    (1/c.val) • (tempDistTimeSlice c).symm (Space.distTimeDeriv f)
```

**`SpaceTime.distTimeSlice_symm_distTimeDeriv_eq`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L208).

```lean
lemma distTimeSlice_symm_distTimeDeriv_eq {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {c : SpeedOfLight}
    (f : (Time × Space d) →d[ℝ] M) :
    (tempDistTimeSlice c).symm (Space.distTimeDeriv f) =
    c.val • distDeriv (Sum.inl 0) ((tempDistTimeSlice c).symm f)
```

**`SpaceTime.distTimeSlice_distDeriv_inr`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L216).

```lean
lemma distTimeSlice_distDeriv_inr {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {c : SpeedOfLight}
    (i : Fin d) (f : (SpaceTime d) →d[ℝ] M) :
    tempDistTimeSlice c (distDeriv (Sum.inr i) f) =
    Space.distSpaceDeriv i (tempDistTimeSlice c f)
```

**`SpaceTime.distDeriv_inr_distTimeSlice_symm`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean#L237).

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

- [Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/SpaceTime/TimeSlice.lean)
