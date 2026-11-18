---
declaration: module
origin: cited
lean: SpaceTime, SpaceTime.coord, SpaceTime.coord_apply, SpaceTime.coordCLM, SpaceTime.space, SpaceTime.space_toCoord_symm, SpaceTime.space_equivariant, SpaceTime.time
statement: formalized
proof: formalized
---

# Spacetime

The module `Physlib.SpaceAndTime.SpaceTime.Basic`, [Physlib/SpaceAndTime/SpaceTime/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean): 38 declarations (6 instances with no name), 9 with a docstring.

## i. Overview

> In this file we define the type `SpaceTime d` which corresponds to `d+1` dimensional
> spacetime. This is equipped with an instance of the action of a Lorentz group,
> corresponding to Minkowski-spacetime.
>
> It is defined through `Lorentz.Vector d`, and carries the tensorial instance,
> allowing it to be used in tensorial expressions.

## ii. Key results

> - `SpaceTime d` : The type corresponding to `d+1` dimensional spacetime.
> - `space_equivariant` : Spatial projection intertwines the Lorentz and Euclidean actions
>   of the same rotation about the coordinate origin.
> - `toTimeAndSpace` : A continuous linear equivalence between `SpaceTime d`
>   and `Time × Space d`.

## iv. References

> * None.

## A. The definition of `SpaceTime d`

**`SpaceTime`**, an abbrev, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L85).

> `SpaceTime d` corresponds to `d+1` dimensional space-time.
> This is equipped with an instance of the action of a Lorentz group,
> corresponding to Minkowski-spacetime.

```lean
abbrev SpaceTime (d : ℕ := 3)
```

## C. Continuous linear map to coordinates

**`SpaceTime.coord`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L105).

> For a given `μ : Fin (1 + d)` `coord μ p` is the coordinate of
> `p` in the direction `μ`.
>
> This is denoted `𝔁 μ p`, where `𝔁` is typed with `\MCx`.

```lean
def coord {d : ℕ} (μ : Fin (1 + d)) : SpaceTime d →ₗ[ℝ] ℝ
```

**`SpaceTime.coord_apply`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L115).

```lean
lemma coord_apply {d : ℕ} (μ : Fin (1 + d)) (y : SpaceTime d) :
    𝔁 μ y = y (finSumFinEquiv.symm μ)
```

**`SpaceTime.coordCLM`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L120).

> The continuous linear map from a point in space time to one of its coordinates.

```lean
def coordCLM (μ : Fin 1 ⊕ Fin d) : SpaceTime d →L[ℝ] ℝ
```

## D. Measures on `SpaceTime d`

### D.1. Instance of a measurable space

**An instance with no name**, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L142).

```lean
instance {d : ℕ} : MeasurableSpace (SpaceTime d)
```

### D.2. Instance of a borel space

**An instance with no name**, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L150).

```lean
instance {d : ℕ} : BorelSpace (SpaceTime d)
```

### D.4. Instance of a measure space

**An instance with no name**, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L159).

```lean
instance {d : ℕ} : MeasureSpace (SpaceTime d)
```

### D.5. Volume measure is positive on non-empty open sets

**An instance with no name**, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L168).

```lean
instance {d : ℕ} : (volume (α := SpaceTime d)).IsOpenPosMeasure
```

### D.6. Volume measure is a finite measure on compact sets

**An instance with no name**, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L177).

```lean
instance {d : ℕ} : IsFiniteMeasureOnCompacts (volume (α := SpaceTime d))
```

### D.7. Volume measure is an additive Haar measure

**An instance with no name**, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L186).

```lean
instance {d : ℕ} : Measure.IsAddHaarMeasure (volume (α := SpaceTime d))
```

## B. Maps to and from `Space` and `Time`

### B.1. Linear map to `Space d`

**`SpaceTime.space`**, a def, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L202).

> The space part of spacetime.

```lean
def space {d : ℕ} : SpaceTime d →L[ℝ] Space d
```

#### B.1.1. Explicit expansion of map to space

**`SpaceTime.space_toCoord_symm`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L219).

```lean
lemma space_toCoord_symm {d : ℕ} (f : Fin 1 ⊕ Fin d → ℝ) :
    space f = fun i => f (Sum.inr i)
```

#### B.1.2. Equivariance of the to space under rotations

**`SpaceTime.space_equivariant`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L233).

> Spatial projection intertwines a rotation's Lorentz action on spacetime with its
> Euclidean action on space, using the same special orthogonal matrix on both sides.
> These are rotations about the coordinate origin; no boosts or translations are included.

```lean
lemma space_equivariant {d : ℕ}
    (R : Matrix.specialOrthogonalGroup (Fin d) ℝ) (x : SpaceTime d) :
    space ((LorentzGroup.ofSpecialOrthogonal R : LorentzGroup d) • x) =
      EuclideanGroup.ofRotation R • space x
```

### B.2. Linear map to `Time`

**`SpaceTime.time`**, a def, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L251).

> The time part of spacetime.

```lean
def time {d : ℕ} (c : SpeedOfLight := 1) : SpaceTime d →ₗ[ℝ] Time
```

#### B.2.1. Explicit expansion of map to time in terms of coordinates

**`SpaceTime.time_val_toCoord_symm`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L269).

```lean
lemma time_val_toCoord_symm {d : ℕ} (c : SpeedOfLight) (f : Fin 1 ⊕ Fin d → ℝ) :
    (time c f).val = f (Sum.inl 0) / c
```

### B.3. `toTimeAndSpace`: Continuous linear equivalence to `Time × Space d`

**`SpaceTime.toTimeAndSpace`**, a def, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L281).

> A continuous linear equivalence between `SpaceTime d` and
> `Time × Space d`.

```lean
def toTimeAndSpace {d : ℕ} (c : SpeedOfLight := 1) : SpaceTime d ≃L[ℝ] Time × Space d
```

**`SpaceTime.toTimeAndSpace_symm_apply_time_space`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L312).

```lean
lemma toTimeAndSpace_symm_apply_time_space {d : ℕ} {c : SpeedOfLight} (x : SpaceTime d) :
    (toTimeAndSpace c).symm (x.time c, x.space) = x
```

**`SpaceTime.space_toTimeAndSpace_symm`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L317).

```lean
lemma space_toTimeAndSpace_symm {d : ℕ} {c : SpeedOfLight} (t : Time) (s : Space d) :
    ((toTimeAndSpace c).symm (t, s)).space = s
```

**`SpaceTime.time_toTimeAndSpace_symm`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L322).

```lean
lemma time_toTimeAndSpace_symm {d : ℕ} {c : SpeedOfLight} (t : Time) (s : Space d) :
    ((toTimeAndSpace c).symm (t, s)).time c = t
```

**`SpaceTime.toTimeAndSpace_symm_apply_inl`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L327).

```lean
lemma toTimeAndSpace_symm_apply_inl {d : ℕ} {c : SpeedOfLight} (t : Time) (s : Space d) :
    (toTimeAndSpace c).symm (t, s) (Sum.inl 0) = c * t
```

**`SpaceTime.toTimeAndSpace_symm_apply_inr`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L331).

```lean
lemma toTimeAndSpace_symm_apply_inr {d : ℕ} {c : SpeedOfLight} (t : Time) (x : Space d)
    (i : Fin d) :
    (toTimeAndSpace c).symm (t, x) (Sum.inr i) = x i
```

#### B.3.1. Derivative of `toTimeAndSpace`

**`SpaceTime.toTimeAndSpace_fderiv`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L341).

```lean
lemma toTimeAndSpace_fderiv {d : ℕ} {c : SpeedOfLight} (x : SpaceTime d) :
    fderiv ℝ (toTimeAndSpace c) x = (toTimeAndSpace c).toContinuousLinearMap
```

#### B.3.2. Derivative of the inverse of `toTimeAndSpace`

**`SpaceTime.toTimeAndSpace_symm_fderiv`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L352).

```lean
lemma toTimeAndSpace_symm_fderiv {d : ℕ} {c : SpeedOfLight} (x : Time × Space d) :
    fderiv ℝ (toTimeAndSpace c).symm x = (toTimeAndSpace c).symm.toContinuousLinearMap
```

#### B.3.3. `toTimeAndSpace` acting on spatial basis vectors

**`SpaceTime.toTimeAndSpace_basis_inr`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L362).

```lean
lemma toTimeAndSpace_basis_inr {d : ℕ} {c : SpeedOfLight} (i : Fin d) :
    toTimeAndSpace c (Lorentz.Vector.basis (Sum.inr i))
    = (0, Space.basis i)
```

#### B.3.4. `toTimeAndSpace` acting on the temporal basis vectors

**`SpaceTime.toTimeAndSpace_basis_inl`**, a lemma, [line 376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L376).

```lean
lemma toTimeAndSpace_basis_inl {d : ℕ} {c : SpeedOfLight} :
    toTimeAndSpace (d := d) c (Lorentz.Vector.basis (Sum.inl 0)) = (⟨1/c.val⟩, 0)
```

**`SpaceTime.toTimeAndSpace_basis_inl'`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L383).

```lean
lemma toTimeAndSpace_basis_inl' {d : ℕ} {c : SpeedOfLight} :
    toTimeAndSpace (d := d) c (Lorentz.Vector.basis (Sum.inl 0)) = (1/c.val) • (1, 0)
```

### B.4. Time space basis

**`SpaceTime.timeSpaceBasis`**, a def, [line 396](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L396).

> The basis of `SpaceTime` where the first component is `(c, 0, 0, ...)` instead
> of `(1, 0, 0, ....).`

```lean
def timeSpaceBasis {d : ℕ} (c : SpeedOfLight := 1) :
    Module.Basis (Fin 1 ⊕ Fin d) ℝ (SpaceTime d)
```

#### B.4.1. Elements of the basis

**`SpaceTime.timeSpaceBasis_apply_inl`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L408).

```lean
lemma timeSpaceBasis_apply_inl {d : ℕ} (c : SpeedOfLight) :
    timeSpaceBasis (d := d) c (Sum.inl 0) = c.val • Lorentz.Vector.basis (Sum.inl 0)
```

**`SpaceTime.timeSpaceBasis_apply_inr`**, a lemma, [line 416](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L416).

```lean
lemma timeSpaceBasis_apply_inr {d : ℕ} (c : SpeedOfLight) (i : Fin d) :
    timeSpaceBasis (d := d) c (Sum.inr i) = Lorentz.Vector.basis (Sum.inr i)
```

#### B.4.2. Equivalence adjusting time basis vector

**`SpaceTime.timeSpaceBasisEquiv`**, a def, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L430).

> The equivalence on of `SpaceTime` taking `(1, 0, 0, ...)` to
> of `(c, 0, 0, ....)` and keeping all other components the same.

```lean
def timeSpaceBasisEquiv {d : ℕ} (c : SpeedOfLight) :
    SpaceTime d ≃L[ℝ] SpaceTime d
```

#### B.4.3. Determinant of the equivalence

**`SpaceTime.det_timeSpaceBasisEquiv`**, a lemma, [line 498](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L498).

```lean
lemma det_timeSpaceBasisEquiv {d : ℕ} (c : SpeedOfLight) :
    (timeSpaceBasisEquiv (d := d) c).det = c.val
```

#### B.4.4. Time space basis expressed in terms of the Lorentz basis

**`SpaceTime.timeSpaceBasis_eq_map_basis`**, a lemma, [line 517](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L517).

```lean
lemma timeSpaceBasis_eq_map_basis {d : ℕ} (c : SpeedOfLight) :
    timeSpaceBasis (d := d) c =
    Module.Basis.map (Lorentz.Vector.basis (d := d)) (timeSpaceBasisEquiv c).toLinearEquiv
```

#### B.4.5. The additive Haar measure associated to the time space basis

**`SpaceTime.timeSpaceBasis_addHaar`**, a lemma, [line 537](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L537).

```lean
lemma timeSpaceBasis_addHaar {d : ℕ} (c : SpeedOfLight := 1) :
    (timeSpaceBasis (d := d) c).addHaar = (ENNReal.ofReal (c⁻¹)) • volume
```

### B.5. Integrals over `SpaceTime d`

#### B.5.1. Measure preserving property of `toTimeAndSpace.symm`

**`SpaceTime.toTimeAndSpace_symm_measurePreserving`**, a lemma, [line 561](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L561).

```lean
lemma toTimeAndSpace_symm_measurePreserving {d : ℕ} (c : SpeedOfLight) :
    MeasurePreserving (toTimeAndSpace c).symm (volume.prod (volume (α := Space d)))
    (ENNReal.ofReal c⁻¹ • volume)
```

#### B.5.2. Integrals over `SpaceTime d` expressed as integrals over `Time` and `Space d`

**`SpaceTime.spaceTime_integral_eq_time_space_integral`**, a lemma, [line 576](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L576).

```lean
lemma spaceTime_integral_eq_time_space_integral {M} [NormedAddCommGroup M]
    [NormedSpace ℝ M] {d : ℕ} (c : SpeedOfLight)
    (f : SpaceTime d → M) :
    ∫ x : SpaceTime d, f x ∂(volume) =
    c.val • ∫ tx : Time × Space d, f ((toTimeAndSpace c).symm tx) ∂(volume.prod volume)
```

**`SpaceTime.spaceTime_integrable_iff_space_time_integrable`**, a lemma, [line 590](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L590).

```lean
lemma spaceTime_integrable_iff_space_time_integrable {M} [NormedAddCommGroup M]
    {d : ℕ} (c : SpeedOfLight)
    (f : SpaceTime d → M) :
    Integrable f volume ↔ Integrable (f ∘ ((toTimeAndSpace c).symm)) (volume.prod volume)
```

**`SpaceTime.spaceTime_integral_eq_time_integral_space_integral`**, a lemma, [line 603](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L603).

```lean
lemma spaceTime_integral_eq_time_integral_space_integral {M} [NormedAddCommGroup M]
    [NormedSpace ℝ M] {d : ℕ} (c : SpeedOfLight)
    (f : SpaceTime d → M)
    (h : Integrable f volume) :
    ∫ x : SpaceTime d, f x =
    c.val • ∫ t : Time, ∫ x : Space d, f ((toTimeAndSpace c).symm (t, x))
```

**`SpaceTime.spaceTime_integral_eq_space_integral_time_integral`**, a lemma, [line 612](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean#L612).

```lean
lemma spaceTime_integral_eq_space_integral_time_integral {M} [NormedAddCommGroup M]
    [NormedSpace ℝ M] {d : ℕ} (c : SpeedOfLight)
    (f : SpaceTime d → M)
    (h : Integrable f volume) :
    ∫ x : SpaceTime d, f x =
    c.val • ∫ x : Space d, ∫ t : Time, f ((toTimeAndSpace c).symm (t, x))
```

## Depends on

- [Rotations](../../relativity/lorentzgroup/rotations.md)
- [The Speed of Light](../../relativity/speedoflight.md)
- [The action of the Euclidean group on `Space`](../space/part-02/euclideangroup-action.md)
- [The structure of a module on Space](../space/part-01/module.md)
- [Time as an inner product space](../time/innerproductspace.md)

## Proof depends on

- [Integrals in Space](../space/part-02/integrals-basic.md)

## Sources

- [Physlib/SpaceAndTime/SpaceTime/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Basic.lean)
