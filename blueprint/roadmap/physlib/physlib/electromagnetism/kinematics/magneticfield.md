---
declaration: module
origin: cited
lean: Electromagnetism.ElectromagneticPotential.magneticField, Electromagnetism.ElectromagneticPotential.magneticField_eq, Electromagnetism.ElectromagneticPotential.magneticField_coord_eq_toFieldStrength_eval, Electromagnetism.ElectromagneticPotential.magneticField_div_eq_zero, Electromagnetism.ElectromagneticPotential.ofScalarPotential_magneticField, Electromagnetism.ElectromagneticPotential.ofElectromagneticField_magneticField, Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_eq_electric_magnetic, Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_eq_electric_magnetic_of_spaceTime
statement: formalized
proof: formalized
---

# The Magnetic Field (Kinematics/MagneticField)

The module `Physlib.Electromagnetism.Kinematics.MagneticField`, [Physlib/Electromagnetism/Kinematics/MagneticField.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean): 23 declarations, 4 with a docstring.

## i. Overview

> In 3-spatial dimensions from the electromagnetic potential we can define the magnetic field
> ` \vec B` as `(∇ ⨯ (A.vectorPotential t)) x`.
> In this module we define this magnetic field from the electromagnetic potential.
>
> In general dimensions we define the magnetic field matrix from the spatial components of the
> field strength matrix. This is an antisymmetric matrix.

## ii. Key results

> - `ElectromagneticPotential.magneticField` : The magnetic field from the electromagnetic potential
>   in 3 spatial dimensions.
> - `ElectromagneticPotential.magneticFieldMatrix` : The magnetic field matrix from the
>   electromagnetic potential in general spatial dimensions.
> - `ElectromagneticPotential.time_deriv_magneticFieldMatrix` : The time derivative of the magnetic
>   field matrix in terms of the vector potential. (Aka Faraday's law).

## iv. References

> * None.

## A. The magnetic field

**`Electromagnetism.ElectromagneticPotential.magneticField`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L79).

> The magnetic field from the electromagnetic potential.

```lean
noncomputable def magneticField (c : SpeedOfLight := 1) (A : ElectromagneticPotential) :
    MagneticField
```

**`Electromagnetism.ElectromagneticPotential.magneticField_eq`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L83).

```lean
lemma magneticField_eq {c : SpeedOfLight} (A : ElectromagneticPotential) :
    A.magneticField c = fun t x => (∇ ⨯ (A.vectorPotential c t)) x
```

### A.1. Relation between the magnetic field and the field strength tensor

**`Electromagnetism.ElectromagneticPotential.magneticField_coord_eq_toFieldStrength_eval`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L92).

```lean
lemma magneticField_coord_eq_toFieldStrength_eval {i : Fin 3} {c : SpeedOfLight}
    (A : ElectromagneticPotential) (t : Time)
    (x : Space) (hA : Differentiable ℝ A) :
    A.magneticField c t x i = - toScalar {A.toFieldStrength ((toTimeAndSpace c).symm (t, x)) |
      [Sum.inr (i+1)] [Sum.inr (i+2)]}ᵀ
```

### A.2. Divergence of the magnetic field

**`Electromagnetism.ElectromagneticPotential.magneticField_div_eq_zero`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L116).

```lean
lemma magneticField_div_eq_zero (A : ElectromagneticPotential)
    (hA : ContDiff ℝ 2 A) (t : Time) : Space.div (A.magneticField c t) = 0
```

### A.4. The magnetic field on constructors

**`Electromagnetism.ElectromagneticPotential.ofScalarPotential_magneticField`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L130).

> A scalar-only potential produces no magnetic field.

```lean
lemma ofScalarPotential_magneticField (c : SpeedOfLight)
    (φ : Time → Space 3 → ℝ) :
    (ofScalarPotential c φ).magneticField c = 0
```

**`Electromagnetism.ElectromagneticPotential.ofElectromagneticField_magneticField`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L139).

> The magnetic field of the electromagnetic potential created from the electric field
> `E` and the magnetic field `B` is `B`, as long as Gauss's law is satisfied.

```lean
lemma ofElectromagneticField_magneticField {c : SpeedOfLight}
    (E : ElectricField) (B : MagneticField) (B_contDiff : ∀ t, ContDiff ℝ 1 (B t))
    (B_grad : ∀ t, ∇ ⬝ (B t) = 0) :
    (ofElectromagneticField c E B).magneticField c = B
```

## B. The components of the field strength tensor in terms of the electric and magnetic fields

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_eq_electric_magnetic`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L159).

```lean
lemma toFieldStrength_eval_eq_electric_magnetic {c} (A : ElectromagneticPotential) (t : Time)
    (x : Space) (hA : Differentiable ℝ A) (μ ν : Fin 1 ⊕ Fin 3) :
    toScalar {A.toFieldStrength ((toTimeAndSpace c).symm (t, x)) | [μ] [ν]}ᵀ =
    match μ, ν with
    | Sum.inl 0, Sum.inl 0 => 0
    | Sum.inl 0, Sum.inr i => - A.electricField c t x i / c
    | Sum.inr i, Sum.inl 0 => A.electricField c t x i / c
    | Sum.inr i, Sum.inr j =>
    match i, j with
    | 0, 0 => 0
    | 0, 1 => - A.magneticField c t x 2
    | 0, 2 => A.magneticField c t x 1
    | 1, 0 => A.magneticField c t x 2
    | 1, 1 => 0
    | 1, 2 => - A.magneticField c t x 0
    | 2, 0 => - A.magneticField c t x 1
    | 2, 1 => A.magneticField c t x 0
    | 2, 2 => 0
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_eq_electric_magnetic_of_spaceTime`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L189).

```lean
lemma toFieldStrength_eval_eq_electric_magnetic_of_spaceTime (c : SpeedOfLight)
    (A : ElectromagneticPotential)
    (x : SpaceTime) (hA : Differentiable ℝ A) (μ ν : Fin 1 ⊕ Fin 3) :
    let tx := SpaceTime.toTimeAndSpace c x
    toScalar {A.toFieldStrength x | [μ] [ν]}ᵀ =
    match μ, ν with
    | Sum.inl 0, Sum.inl 0 => 0
    | Sum.inl 0, Sum.inr i => - A.electricField c tx.1 tx.2 i / c
    | Sum.inr i, Sum.inl 0 => A.electricField c tx.1 tx.2 i / c
    | Sum.inr i, Sum.inr j =>
    match i, j with
    | 0, 0 => 0
    | 0, 1 => - A.magneticField c tx.1 tx.2 2
    | 0, 2 => A.magneticField c tx.1 tx.2 1
    | 1, 0 => A.magneticField c tx.1 tx.2 2
    | 1, 1 => 0
    | 1, 2 => - A.magneticField c tx.1 tx.2 0
    | 2, 0 => - A.magneticField c tx.1 tx.2 1
    | 2, 1 => A.magneticField c tx.1 tx.2 0
    | 2, 2 => 0
```

## C. Magnetic field matrix

**`Electromagnetism.ElectromagneticPotential.magneticFieldMatrix`**, a def, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L222).

> The matrix corresponding to the magnetic field in general dimensions.
> In `3` space-dimensions this reduces to a vector.

```lean
noncomputable def magneticFieldMatrix (c : SpeedOfLight := 1) (A : ElectromagneticPotential d) :
    Time → Space d → (Fin d × Fin d) → ℝ
```

**`Electromagnetism.ElectromagneticPotential.magneticFieldMatrix_eq`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L226).

```lean
lemma magneticFieldMatrix_eq {c : SpeedOfLight} (A : ElectromagneticPotential d) :
    A.magneticFieldMatrix c = fun t x ij =>
      toScalar {A.toFieldStrength ((toTimeAndSpace c).symm (t, x)) |
        [Sum.inr ij.1] [Sum.inr ij.2]}ᵀ
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_inr_inr_eq_magneticFieldMatrix`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L231).

```lean
lemma toFieldStrength_eval_inr_inr_eq_magneticFieldMatrix {c : SpeedOfLight}
    (A : ElectromagneticPotential d)
    (x : SpaceTime d) (i j : Fin d) :
    toScalar {A.toFieldStrength x | [Sum.inr i] [Sum.inr j]}ᵀ =
    A.magneticFieldMatrix c (x.time c) x.space (i, j)
```

### C.1. Antisymmetry of the magnetic field matrix

**`Electromagnetism.ElectromagneticPotential.magneticFieldMatrix_antisymm`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L244).

```lean
lemma magneticFieldMatrix_antisymm {c : SpeedOfLight}
    (A : ElectromagneticPotential d) (t : Time)
    (x : Space d) (i j : Fin d) :
    A.magneticFieldMatrix c t x (i, j) = - A.magneticFieldMatrix c t x (j, i)
```

**`Electromagnetism.ElectromagneticPotential.magneticFieldMatrix_diag_eq_zero`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L251).

```lean
lemma magneticFieldMatrix_diag_eq_zero {c : SpeedOfLight}
    (A : ElectromagneticPotential d) (t : Time)
    (x : Space d) (i : Fin d) :
    A.magneticFieldMatrix c t x (i, i) = 0
```

### C.2. Magnetic field in terms of the magnetic field matrix

**`Electromagnetism.ElectromagneticPotential.magneticField_eq_magneticFieldMatrix`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L263).

```lean
lemma magneticField_eq_magneticFieldMatrix {c : SpeedOfLight} (A : ElectromagneticPotential)
    (hA : Differentiable ℝ A) :
    A.magneticField c = fun t x => WithLp.toLp 2 fun i =>
      - A.magneticFieldMatrix c t x ((i+1), (i+2))
```

**`Electromagnetism.ElectromagneticPotential.magneticField_curl_eq_magneticFieldMatrix`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L270).

```lean
lemma magneticField_curl_eq_magneticFieldMatrix{c : SpeedOfLight} (A : ElectromagneticPotential)
    (hA : ContDiff ℝ 2 A) (t : Time) :
    (∇ ⨯ A.magneticField c t) x i = ∑ j, Space.deriv j (A.magneticFieldMatrix c t · (j, i)) x
```

### C.3. Magnetic field matrix in terms of vector potentials

**`Electromagnetism.ElectromagneticPotential.magneticFieldMatrix_eq_vectorPotential`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L291).

```lean
lemma magneticFieldMatrix_eq_vectorPotential {c : SpeedOfLight} (A : ElectromagneticPotential d)
    (hA : Differentiable ℝ A) (t : Time) (x : Space d) (i j : Fin d) :
    A.magneticFieldMatrix c t x (i, j) = Space.deriv j (A.vectorPotential c t · i) x -
    Space.deriv i (A.vectorPotential c t · j) x
```

### C.4. Smoothness of the magnetic field matrix

**`Electromagnetism.ElectromagneticPotential.magneticFieldMatrix_contDiff`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L314).

```lean
lemma magneticFieldMatrix_contDiff {n} {c : SpeedOfLight} (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ (n + 1) A) (ij) :
    ContDiff ℝ n ↿(fun t x => A.magneticFieldMatrix c t x ij)
```

**`Electromagnetism.ElectromagneticPotential.magneticFieldMatrix_space_contDiff`**, a lemma, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L320).

```lean
lemma magneticFieldMatrix_space_contDiff {n} {c : SpeedOfLight} (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ (n + 1) A) (t : Time) (ij) :
    ContDiff ℝ n (fun x => A.magneticFieldMatrix c t x ij)
```

### C.5. Differentiablity of the magnetic field matrix

**`Electromagnetism.ElectromagneticPotential.magneticFieldMatrix_differentiable`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L332).

```lean
lemma magneticFieldMatrix_differentiable {c : SpeedOfLight} (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ 2 A) (ij) : Differentiable ℝ ↿(fun t x => A.magneticFieldMatrix c t x ij)
```

### C.6. Spatial derivative of the magnetic field matrix

**`Electromagnetism.ElectromagneticPotential.magneticFieldMatrix_space_deriv_eq`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L342).

```lean
lemma magneticFieldMatrix_space_deriv_eq {c : SpeedOfLight} (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ 2 A) (t : Time) (x : Space d) (i j k : Fin d) :
    ∂[k] (A.magneticFieldMatrix c t · (i, j)) x =
    ∂[i] (A.magneticFieldMatrix c t · (k, j)) x
    - ∂[j] (A.magneticFieldMatrix c t · (k, i)) x
```

### C.7. Temporal derivative of the magnetic field matrix

**`Electromagnetism.ElectromagneticPotential.time_deriv_magneticFieldMatrix`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L369).

```lean
lemma time_deriv_magneticFieldMatrix {d : ℕ} {c : SpeedOfLight} (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ 2 A) (t : Time) (x : Space d) (i j : Fin d) :
    ∂ₜ (A.magneticFieldMatrix c · x (i, j)) t =
    ∂[i] (A.electricField c t · j) x - ∂[j] (A.electricField c t · i) x
```

**`Electromagnetism.ElectromagneticPotential.time_deriv_time_deriv_magneticFieldMatrix`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L405).

```lean
lemma time_deriv_time_deriv_magneticFieldMatrix {d : ℕ} {c : SpeedOfLight}
    (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ 3 A) (t : Time) (x : Space d) (i j : Fin d) :
    ∂ₜ (∂ₜ (A.magneticFieldMatrix c · x (i, j))) t =
    ∂[i] (fun x => ∂ₜ (fun t => A.electricField c t x) t j) x -
    ∂[j] (fun x => ∂ₜ (fun t => A.electricField c t x) t i) x
```

### C.8. `curl` of the magnetic field matrix

**`Electromagnetism.ElectromagneticPotential.curl_magneticFieldMatrix_eq_electricField_toFieldStrength_eval`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean#L432).

```lean
lemma curl_magneticFieldMatrix_eq_electricField_toFieldStrength_eval {d : ℕ} {c : SpeedOfLight}
    (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ 2 A) (t : Time) (x : Space d) (i : Fin d) :
    ∑ j, Space.deriv j (A.magneticFieldMatrix c t · (j, i)) x =
    (1/c^2) * ∂ₜ (fun t => A.electricField c t x) t i +
    (∑ (μ : (Fin 1 ⊕ Fin d)), (∂_ μ (fun x => toScalar {A.toFieldStrength x | [μ] [Sum.inr i]}ᵀ)
    ((toTimeAndSpace c).symm (t, x))))
```

## Depends on

- [The Electric Field (Kinematics/ElectricField)](electricfield.md)

## Sources

- [Physlib/Electromagnetism/Kinematics/MagneticField.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/MagneticField.lean)
