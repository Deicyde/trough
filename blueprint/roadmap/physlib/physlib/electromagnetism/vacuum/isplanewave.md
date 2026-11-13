---
declaration: module
origin: cited
lean: Electromagnetism.ElectromagneticPotential.IsPlaneWave, Electromagnetism.ElectromagneticPotential.IsPlaneWave.electricFunction, Electromagnetism.ElectromagneticPotential.IsPlaneWave.electricField_eq_electricFunction, Electromagnetism.ElectromagneticPotential.IsPlaneWave.magneticFunction, Electromagnetism.ElectromagneticPotential.IsPlaneWave.magneticFieldMatrix_eq_magneticFunction, Electromagnetism.ElectromagneticPotential.IsPlaneWave.electricFunction_eq_electricField, Electromagnetism.ElectromagneticPotential.IsPlaneWave.magneticFunction_eq_magneticFieldMatrix, Electromagnetism.ElectromagneticPotential.IsPlaneWave.electricFunction_unique
statement: formalized
proof: formalized
---

# Electromagnetic wave equation

The module `Physlib.Electromagnetism.Vacuum.IsPlaneWave`, [Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean): 23 declarations, 3 with a docstring.

## i. Overview

> In this module we define a proposition `IsPlaneWave` on electromagnetic potentials
> which is true if the potential corresponds to a plane wave.
> From this we derive various properties of plane waves including
> the orthogonality of the electric field, magnetic field and direction of propagation,
> in general dimensions.

## ii. Key results

> - `IsPlaneWave` : The proposition defining plane waves.
> - `IsPlaneWave.electricFunction` : The electric function corresponding to a plane wave.
> - `IsPlaneWave.magneticFunction` : The magnetic function corresponding to a plane wave.
> - `IsPlaneWave.magneticFieldMatrix_eq_propogator_cross_electricField` :
>     The magnetic field expressed in terms of the electric field and direction of propagation.
> - `IsPlaneWave.electricField_eq_propogator_cross_magneticFieldMatrix` :
>     The electric field expressed in terms of the magnetic field and direction of propagation.

## iv. References

> * None.

## A. The property of being a plane wave

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L75).

> The proposition on a electromagnetic potential which is true if
> it corresponds to a plane wave.

```lean
def IsPlaneWave {d : ℕ} (𝓕 : FreeSpace)
    (A : ElectromagneticPotential d) (s : Direction d) : Prop
```

### A.1. The electric and magnetic functions from a plane wave

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.electricFunction`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L88).

> The corresponding electric field function from `ℝ` to `EuclideanSpace ℝ (Fin d)`
> of a plane wave.

```lean
noncomputable def electricFunction {d : ℕ} {𝓕 : FreeSpace}
    {A : ElectromagneticPotential d} {s : Direction d}
    (hA : IsPlaneWave 𝓕 A s) : ℝ → EuclideanSpace ℝ (Fin d)
```

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.electricField_eq_electricFunction`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L93).

```lean
lemma electricField_eq_electricFunction {d : ℕ} {𝓕 : FreeSpace}
    {A : ElectromagneticPotential d} {s : Direction d}
    (P : IsPlaneWave 𝓕 A s) (t : Time) (x : Space d) :
    A.electricField 𝓕.c t x =
    P.electricFunction (⟪x, s.unit⟫_ℝ - 𝓕.c * t)
```

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.magneticFunction`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L102).

> The corresponding magnetic field function from `ℝ` to
> `Fin d × Fin d → ℝ` of a plane wave.

```lean
noncomputable def magneticFunction {d : ℕ} {𝓕 : FreeSpace}
    {A : ElectromagneticPotential d} {s : Direction d}
    (hA : IsPlaneWave 𝓕 A s) : ℝ → Fin d × Fin d → ℝ
```

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.magneticFieldMatrix_eq_magneticFunction`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L107).

```lean
lemma magneticFieldMatrix_eq_magneticFunction {d : ℕ}
    {𝓕 : FreeSpace} {A : ElectromagneticPotential d} {s : Direction d}
    (P : IsPlaneWave 𝓕 A s) (t : Time) (x : Space d) :
    A.magneticFieldMatrix 𝓕.c t x =
    P.magneticFunction (⟪x, s.unit⟫_ℝ - 𝓕.c * t)
```

#### A.1.1. Electric function and magnetic function in terms of E and B fields

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.electricFunction_eq_electricField`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L120).

```lean
lemma electricFunction_eq_electricField {d : ℕ}
    {𝓕 : FreeSpace} {A : ElectromagneticPotential d}
    {s : Direction d} (P : IsPlaneWave 𝓕 A s) :
    P.electricFunction = fun u =>
    A.electricField 𝓕.c ⟨(- u)/𝓕.c.1⟩ (0 : Space d)
```

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.magneticFunction_eq_magneticFieldMatrix`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L130).

```lean
lemma magneticFunction_eq_magneticFieldMatrix {d : ℕ}
    {𝓕 : FreeSpace} {A : ElectromagneticPotential d}
    {s : Direction d} (P : IsPlaneWave 𝓕 A s) :
    P.magneticFunction = fun u =>
    A.magneticFieldMatrix 𝓕.c ⟨(- u)/𝓕.c.1⟩ (0 : Space d)
```

#### A.1.2. Uniqueness of the electric function

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.electricFunction_unique`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L146).

```lean
lemma electricFunction_unique {d : ℕ} {𝓕 : FreeSpace}
    {A : ElectromagneticPotential d} {s : Direction d}
    (P : IsPlaneWave 𝓕 A s) (E1 : ℝ → EuclideanSpace ℝ (Fin d))
    (hE₁ : A.electricField 𝓕.c = planeWave E1 𝓕.c s) :
    E1 = P.electricFunction
```

#### A.1.3. Uniqueness of the magnetic function

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.magneticFunction_unique`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L162).

```lean
lemma magneticFunction_unique {d : ℕ} {𝓕 : FreeSpace}
    {A : ElectromagneticPotential d} {s : Direction d}
    (P : IsPlaneWave 𝓕 A s)
    (B1 : ℝ → Fin d × Fin d → ℝ)
    (hB₁ : ∀ t x, A.magneticFieldMatrix 𝓕.c t x =
      B1 (⟪x, s.unit⟫_ℝ - 𝓕.c * t)) :
    B1 = P.magneticFunction
```

### A.2. Differentiability conditions

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.electricFunction_differentiable`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L179).

```lean
lemma electricFunction_differentiable {d : ℕ}
    {𝓕 : FreeSpace} {A : ElectromagneticPotential d}
    {s : Direction d} (P : IsPlaneWave 𝓕 A s) (hA : ContDiff ℝ 2 A) :
    Differentiable ℝ P.electricFunction
```

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.magneticFunction_differentiable`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L191).

```lean
lemma magneticFunction_differentiable {d : ℕ}
    {𝓕 : FreeSpace} {A : ElectromagneticPotential d}
    {s : Direction d} (P : IsPlaneWave 𝓕 A s) (hA : ContDiff ℝ 2 A)
    (ij : Fin d × Fin d) :
    Differentiable ℝ (fun u => P.magneticFunction u ij)
```

### A.3. Time derivative of electric and magnetic fields of a plane wave

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.electricField_time_deriv`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L212).

```lean
lemma electricField_time_deriv {d : ℕ}
    {𝓕 : FreeSpace} {A : ElectromagneticPotential d}
    {s : Direction d} (P : IsPlaneWave 𝓕 A s) (hA : ContDiff ℝ 2 A) (t : Time)
    (x : Space d) :
    ∂ₜ (A.electricField 𝓕.c · x) t = - 𝓕.c.val •
    fderiv ℝ P.electricFunction (⟪x, s.unit⟫_ℝ - 𝓕.c.val * t.val) 1
```

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.magneticFieldMatrix_time_deriv`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L223).

```lean
lemma magneticFieldMatrix_time_deriv {d : ℕ}
    {𝓕 : FreeSpace} {A : ElectromagneticPotential d}
    {s : Direction d} (P : IsPlaneWave 𝓕 A s) (hA : ContDiff ℝ 2 A) (t : Time)
    (x : Space d) (i j : Fin d) :
    ∂ₜ (A.magneticFieldMatrix 𝓕.c · x (i, j)) t = - 𝓕.c.val •
    fderiv ℝ (fun u => P.magneticFunction u (i, j)) (⟪x, s.unit⟫_ℝ - 𝓕.c.val * t.val) 1
```

### A.4. Space derivative of electric and magnetic fields of a plane wave

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.electricField_space_deriv`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L245).

```lean
lemma electricField_space_deriv {d : ℕ}
    {𝓕 : FreeSpace} {A : ElectromagneticPotential d}
    {s : Direction d} (P : IsPlaneWave 𝓕 A s) (hA : ContDiff ℝ 2 A) (t : Time)
    (x : Space d) (i : Fin d) :
    ∂[i] (A.electricField 𝓕.c t ·) x = s.unit i •
    fderiv ℝ P.electricFunction (⟪x, s.unit⟫_ℝ - 𝓕.c.val * t.val) 1
```

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.magneticFieldMatrix_space_deriv`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L257).

```lean
lemma magneticFieldMatrix_space_deriv {d : ℕ}
    {𝓕 : FreeSpace} {A : ElectromagneticPotential d}
    {s : Direction d} (P : IsPlaneWave 𝓕 A s) (hA : ContDiff ℝ 2 A) (t : Time)
    (x : Space d) (i j : Fin d) (k : Fin d) :
    ∂[k] (A.magneticFieldMatrix 𝓕.c t · (i, j)) x = s.unit k •
    fderiv ℝ (fun u => P.magneticFunction u (i, j))
      (⟪x, s.unit⟫_ℝ - 𝓕.c.val * t.val) 1
```

### A.5. Space derivative in terms of time derivative

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.electricField_space_deriv_eq_time_deriv`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L282).

```lean
lemma electricField_space_deriv_eq_time_deriv {d : ℕ} {𝓕 : FreeSpace}
    {A : ElectromagneticPotential d}
    {s : Direction d} (P : IsPlaneWave 𝓕 A s) (hA : ContDiff ℝ 2 A) (t : Time)
    (x : Space d) (i : Fin d) (k : Fin d) :
    ∂[k] (A.electricField 𝓕.c t · i) x = - (s.unit k / 𝓕.c.val) •
    ∂ₜ (A.electricField 𝓕.c · x i) t
```

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.magneticFieldMatrix_space_deriv_eq_time_deriv`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L295).

```lean
lemma magneticFieldMatrix_space_deriv_eq_time_deriv {d : ℕ}
    {𝓕 : FreeSpace} {A : ElectromagneticPotential d}
    {s : Direction d} (P : IsPlaneWave 𝓕 A s) (hA : ContDiff ℝ 2 A) (t : Time)
    (x : Space d) (i j : Fin d) (k : Fin d) :
    ∂[k] (A.magneticFieldMatrix 𝓕.c t · (i, j)) x = - (s.unit k / 𝓕.c.val) •
    ∂ₜ (A.magneticFieldMatrix 𝓕.c · x (i, j)) t
```

## B. The magnetic field in terms of the electric field

### B.1. Time derivative of the magnetic field in terms of electric field

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.time_deriv_magneticFieldMatrix_eq_electricField_mul_propogator`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L319).

```lean
lemma time_deriv_magneticFieldMatrix_eq_electricField_mul_propogator {d : ℕ}
    {𝓕 : FreeSpace} {A : ElectromagneticPotential d}
    {s : Direction d} (P : IsPlaneWave 𝓕 A s) (hA : ContDiff ℝ 2 A)
    (t : Time) (x : Space d) (i j : Fin d) :
    ∂ₜ (A.magneticFieldMatrix 𝓕.c · x (i, j)) t =
    ∂ₜ (fun t => s.unit j / 𝓕.c * A.electricField 𝓕.c t x i
    - s.unit i / 𝓕.c * A.electricField 𝓕.c t x j) t
```

### B.2. Space derivative of the magnetic field in terms of electric field

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.space_deriv_magneticFieldMatrix_eq_electricField_mul_propogator`**, a lemma, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L343).

```lean
lemma space_deriv_magneticFieldMatrix_eq_electricField_mul_propogator {d : ℕ}
    {𝓕 : FreeSpace} {A : ElectromagneticPotential d}
    {s : Direction d} (P : IsPlaneWave 𝓕 A s) (hA : ContDiff ℝ 2 A)
    (t : Time) (x : Space d) (i j k : Fin d) :
    ∂[k] (A.magneticFieldMatrix 𝓕.c t · (i, j)) x =
    ∂[k] (fun x => s.unit j / 𝓕.c * A.electricField 𝓕.c t x i
    - s.unit i / 𝓕.c * A.electricField 𝓕.c t x j) x
```

### B.3. Magnetic field equal propogator cross electric field up to constant

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.magneticFieldMatrix_eq_propogator_cross_electricField`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L370).

```lean
lemma magneticFieldMatrix_eq_propogator_cross_electricField {d : ℕ}
    {𝓕 : FreeSpace} {A : ElectromagneticPotential d}
    {s : Direction d} (P : IsPlaneWave 𝓕 A s) (hA : ContDiff ℝ 2 A) (i j : Fin d) :
    ∃ C, ∀ t x, A.magneticFieldMatrix 𝓕.c t x (i, j) =
    1/ 𝓕.c * (s.unit j * A.electricField 𝓕.c t x i -
      s.unit i * A.electricField 𝓕.c t x j) + C
```

## C. The electric field in terms of the magnetic field

### C.1. The time derivative of the electric field in terms of magnetic field

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.time_deriv_electricField_eq_magneticFieldMatrix`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L401).

```lean
lemma time_deriv_electricField_eq_magneticFieldMatrix {d : ℕ}
    {𝓕 : FreeSpace} {A : ElectromagneticPotential d}
    {s : Direction d} (P : IsPlaneWave 𝓕 A s) (hA : ContDiff ℝ ∞ A)
    (h : IsExtrema 𝓕 A 0)
    (t : Time) (x : Space d) (i : Fin d) :
    ∂ₜ (A.electricField 𝓕.c · x i) t =
    ∂ₜ (fun t => 𝓕.c * ∑ j, A.magneticFieldMatrix 𝓕.c t x (i, j) * s.unit j) t
```

### C.2. The space derivative of the electric field in terms of magnetic field

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.space_deriv_electricField_eq_magneticFieldMatrix`**, a lemma, [line 461](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L461).

```lean
lemma space_deriv_electricField_eq_magneticFieldMatrix {d : ℕ}
    {𝓕 : FreeSpace} {A : ElectromagneticPotential d}
    {s : Direction d} (P : IsPlaneWave 𝓕 A s) (hA : ContDiff ℝ ∞ A)
    (h : IsExtrema 𝓕 A 0)
    (t : Time) (x : Space d) (i k : Fin d) :
    ∂[k] (A.electricField 𝓕.c t · i) x =
    ∂[k] (fun x => 𝓕.c * ∑ j, A.magneticFieldMatrix 𝓕.c t x (i, j) * s.unit j) x
```

### C.3. Electric field equal propogator cross magnetic field up to constant

**`Electromagnetism.ElectromagneticPotential.IsPlaneWave.electricField_eq_propogator_cross_magneticFieldMatrix`**, a lemma, [line 507](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean#L507).

```lean
lemma electricField_eq_propogator_cross_magneticFieldMatrix {d : ℕ}
    {𝓕 : FreeSpace} {A : ElectromagneticPotential d}
    {s : Direction d} (P : IsPlaneWave 𝓕 A s) (hA : ContDiff ℝ ∞ A)
    (h : IsExtrema 𝓕 A 0) (i : Fin d) :
    ∃ C, ∀ t x, A.electricField 𝓕.c t x i =
    𝓕.c * ∑ j, A.magneticFieldMatrix 𝓕.c t x (i, j) * s.unit j + C
```

## Depends on

- [Wave equation](../../classicalmechanics/waveequation/basic.md)
- [Extrema of the Lagrangian density](../dynamics/isextrema.md)

## Sources

- [Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/IsPlaneWave.lean)
