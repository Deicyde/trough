---
declaration: module
origin: cited
lean: Electromagnetism.ElectromagneticPotential.constantEB, Electromagnetism.ElectromagneticPotential.constantEB_smooth, Electromagnetism.ElectromagneticPotential.constantEB_scalarPotential, Electromagnetism.ElectromagneticPotential.constantEB_vectorPotential, Electromagnetism.ElectromagneticPotential.constantEB_vectorPotential_time_deriv, Electromagnetism.ElectromagneticPotential.constantEB_vectorPotential_space_deriv, Electromagnetism.ElectromagneticPotential.constantEB_electricField, Electromagnetism.ElectromagneticPotential.constantEB_magneticFieldMatrix
statement: formalized
proof: formalized
---

# The constant electric and magnetic fields

The module `Physlib.Electromagnetism.Vacuum.Constant`, [Physlib/Electromagnetism/Vacuum/Constant.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/Constant.lean): 9 declarations, 1 with a docstring.

## i. Overview

> In this module we define the electromagnetic potential which gives rise to a
> given constant electric and magnetic field matrix.
>
> We will show that this electromagnetic potential is an extrema of the free-space
> electromagnetic action.

## ii. Key results

## iv. References

> * None.

## A. The definition of the potential

> The electromagnetic potential which gives rise to a constant electric field `E₀`
> and a constant magnetic field matrix `B₀`.

**`Electromagnetism.ElectromagneticPotential.constantEB`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/Constant.lean#L70).

> An electric potential which gives a given constant E-field and B-field.

```lean
noncomputable def constantEB {d : ℕ} (c : SpeedOfLight)
    (E₀ : EuclideanSpace ℝ (Fin d)) (B₀ : Fin d × Fin d → ℝ)
    (B₀_antisymm : ∀ i j, B₀ (i, j) = - B₀ (j, i)) : ElectromagneticPotential d
```

## B. Smoothness of the potential

> The potential is smooth.

**`Electromagnetism.ElectromagneticPotential.constantEB_smooth`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/Constant.lean#L86).

```lean
lemma constantEB_smooth {c : SpeedOfLight}
    {E₀ : EuclideanSpace ℝ (Fin d)} {B₀ : Fin d × Fin d → ℝ}
    {B₀_antisymm : ∀ i j, B₀ (i, j) = - B₀ (j, i)} :
    ContDiff ℝ ∞ (constantEB c E₀ B₀ B₀_antisymm)
```

## C. The scalar potential

> The scalar potential of the electromagnetic potential is given by `-⟪E₀, x⟫`.

**`Electromagnetism.ElectromagneticPotential.constantEB_scalarPotential`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/Constant.lean#L119).

```lean
lemma constantEB_scalarPotential {c : SpeedOfLight}
    {E₀ : EuclideanSpace ℝ (Fin d)} {B₀ : Fin d × Fin d → ℝ}
    {B₀_antisymm : ∀ i j, B₀ (i, j) = - B₀ (j, i)} :
    (constantEB c E₀ B₀ B₀_antisymm).scalarPotential c = fun _ x =>
      -⟪E₀, Space.basis.repr x⟫_ℝ
```

## D. The vector potential

> The vector potential of the electromagnetic potential is `(1 / 2) * ∑ j, B₀ (i, j) * x j `.

**`Electromagnetism.ElectromagneticPotential.constantEB_vectorPotential`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/Constant.lean#L136).

```lean
lemma constantEB_vectorPotential {c : SpeedOfLight}
    {E₀ : EuclideanSpace ℝ (Fin d)} {B₀ : Fin d × Fin d → ℝ}
    {B₀_antisymm : ∀ i j, B₀ (i, j) = - B₀ (j, i)} :
    (constantEB c E₀ B₀ B₀_antisymm).vectorPotential c = fun _ x => WithLp.toLp 2 fun i =>
      (1 / 2) * ∑ j, B₀ (i, j) * x j
```

### D.1. Time derivative of the vector potential

**`Electromagnetism.ElectromagneticPotential.constantEB_vectorPotential_time_deriv`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/Constant.lean#L153).

```lean
lemma constantEB_vectorPotential_time_deriv {c : SpeedOfLight}
    {E₀ : EuclideanSpace ℝ (Fin d)} {B₀ : Fin d × Fin d → ℝ}
    {B₀_antisymm : ∀ i j, B₀ (i, j) = - B₀ (j, i)} (t : Time) (x : Space d) :
    ∂ₜ ((constantEB c E₀ B₀ B₀_antisymm).vectorPotential c · x) t = 0
```

### D.2. Space derivative of the vector potential

**`Electromagnetism.ElectromagneticPotential.constantEB_vectorPotential_space_deriv`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/Constant.lean#L166).

```lean
lemma constantEB_vectorPotential_space_deriv {c : SpeedOfLight}
    {E₀ : EuclideanSpace ℝ (Fin d)} {B₀ : Fin d × Fin d → ℝ}
    {B₀_antisymm : ∀ i j, B₀ (i, j) = - B₀ (j, i)} (t : Time) (x : Space d) (i j : Fin d) :
    Space.deriv i ((constantEB c E₀ B₀ B₀_antisymm).vectorPotential c t · j) x =
    (1 / 2) * B₀ (j, i)
```

## E. The electric field

**`Electromagnetism.ElectromagneticPotential.constantEB_electricField`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/Constant.lean#L195).

```lean
lemma constantEB_electricField {c : SpeedOfLight}
    {E₀ : EuclideanSpace ℝ (Fin d)} {B₀ : Fin d × Fin d → ℝ}
    {B₀_antisymm : ∀ i j, B₀ (i, j) = - B₀ (j, i)} :
    (constantEB c E₀ B₀ B₀_antisymm).electricField c = fun _ _ => E₀
```

## F. The magnetic field

**`Electromagnetism.ElectromagneticPotential.constantEB_magneticFieldMatrix`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/Constant.lean#L217).

```lean
lemma constantEB_magneticFieldMatrix {c : SpeedOfLight}
    {E₀ : EuclideanSpace ℝ (Fin d)} {B₀ : Fin d × Fin d → ℝ}
    {B₀_antisymm : ∀ i j, B₀ (i, j) = - B₀ (j, i)} :
    (constantEB c E₀ B₀ B₀_antisymm).magneticFieldMatrix c = fun _ _ => B₀
```

## G. Is extrema

**`Electromagnetism.ElectromagneticPotential.constantEB_isExtrema`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/Constant.lean#L239).

```lean
lemma constantEB_isExtrema {𝓕 : FreeSpace}
    {E₀ : EuclideanSpace ℝ (Fin d)} {B₀ : Fin d × Fin d → ℝ}
    {B₀_antisymm : ∀ i j, B₀ (i, j) = - B₀ (j, i)} :
    IsExtrema 𝓕 (constantEB 𝓕.c E₀ B₀ B₀_antisymm) 0
```

## Depends on

- [Extrema of the Lagrangian density](../dynamics/isextrema.md)

## Sources

- [Physlib/Electromagnetism/Vacuum/Constant.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/Constant.lean)
