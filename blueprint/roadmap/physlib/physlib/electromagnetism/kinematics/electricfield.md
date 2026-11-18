---
declaration: module
origin: cited
lean: Electromagnetism.ElectromagneticPotential.electricField, Electromagnetism.ElectromagneticPotential.electricField_eq, Electromagnetism.ElectromagneticPotential.ofScalarPotential_electricField, Electromagnetism.ElectromagneticPotential.ofElectromagneticField_electricField, Electromagnetism.ElectromagneticPotential.electricField_eq_toFieldStrength_eval, Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_inl_inr_eq_electricField, Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_inr_inl_eq_electricField, Electromagnetism.ElectromagneticPotential.electricField_contDiff
statement: formalized
proof: formalized
---

# The Electric Field (Kinematics/ElectricField)

The module `Physlib.Electromagnetism.Kinematics.ElectricField`, [Physlib/Electromagnetism/Kinematics/ElectricField.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ElectricField.lean): 14 declarations, 3 with a docstring.

## i. Overview

> The electric field is defined in terms of the electromagnetic potential `A` as
> `E = - ∇ φ - ∂ₜ \vec A`.
>
> In this module we define the electric field, and prove lemmas about it.

## ii. Key results

> - `electricField` : The electric field from the electromagnetic potential.
> - `electricField_eq_toFieldStrength_eval` : The electric field expressed in terms of the
>   components of the field strength tensor.

## iv. References

> * None.

## A. Definition of the Electric Field

**`Electromagnetism.ElectromagneticPotential.electricField`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ElectricField.lean#L67).

> The electric field from the electromagnetic potential.

```lean
noncomputable def electricField {d} (c : SpeedOfLight := 1)
    (A : ElectromagneticPotential d) : ElectricField d
```

**`Electromagnetism.ElectromagneticPotential.electricField_eq`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ElectricField.lean#L71).

```lean
lemma electricField_eq {c : SpeedOfLight} (A : ElectromagneticPotential d) :
    A.electricField c = fun t x =>
      - ∇ (A.scalarPotential c t) x - ∂ₜ (fun t => A.vectorPotential c t x) t
```

## B. Relation to constructors

**`Electromagnetism.ElectromagneticPotential.ofScalarPotential_electricField`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ElectricField.lean#L83).

> A scalar-only potential produces the negative spatial gradient as its electric field.

```lean
lemma ofScalarPotential_electricField {d} (c : SpeedOfLight)
    (φ : Time → Space d → ℝ) :
    (ofScalarPotential c φ).electricField c = fun t x => - ∇ (φ t) x
```

**`Electromagnetism.ElectromagneticPotential.ofElectromagneticField_electricField`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ElectricField.lean#L93).

> The electric field of the electromagnetic potential created from the electric field
> `E` and the magnetic field `B` is `E`, as long as Gauss's law for magnetism and
> Faraday's law are satisfied.

```lean
lemma ofElectromagneticField_electricField {c : SpeedOfLight}
    (E : Time → Space 3 → EuclideanSpace ℝ (Fin 3)) (B : Time → Space 3 → EuclideanSpace ℝ (Fin 3))
    (E_contDiff : ContDiff ℝ 1 ↿E) (B_contDiff : ContDiff ℝ 2 ↿B)
    (B_grad : ∀ t, ∇ ⬝ (B t) = 0) (faraday : ∀ t x, curl (E t) x = - ∂ₜ (B · x) t) :
    (ofElectromagneticField c E B).electricField c = E
```

## B. Relation to the field strength tensor

> The electric field can be expressed in terms of the field strength tensor as
> `E_i = - c * F_0^i`.

**`Electromagnetism.ElectromagneticPotential.electricField_eq_toFieldStrength_eval`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ElectricField.lean#L140).

```lean
lemma electricField_eq_toFieldStrength_eval {c : SpeedOfLight}
    (A : ElectromagneticPotential d) (t : Time)
    (x : Space d) (i : Fin d) (hA : Differentiable ℝ A) :
    A.electricField c t x i = - c *
    toScalar {A.toFieldStrength ((toTimeAndSpace c).symm (t, x)) | [Sum.inl 0] [Sum.inr i]}ᵀ
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_inl_inr_eq_electricField`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ElectricField.lean#L180).

```lean
lemma toFieldStrength_eval_inl_inr_eq_electricField {c : SpeedOfLight}
    (A : ElectromagneticPotential d)
    (x : SpaceTime d) (i : Fin d) (hA : Differentiable ℝ A) :
    toScalar {A.toFieldStrength x | [Sum.inl 0] [Sum.inr i]}ᵀ =
    - (1 /c) * A.electricField c (x.time c) x.space i
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_inr_inl_eq_electricField`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ElectricField.lean#L188).

```lean
lemma toFieldStrength_eval_inr_inl_eq_electricField {c : SpeedOfLight}
    (A : ElectromagneticPotential d)
    (x : SpaceTime d) (i : Fin d) (hA : Differentiable ℝ A) :
    toScalar {A.toFieldStrength x | [Sum.inr i] [Sum.inl 0]}ᵀ =
    (1 /c) * A.electricField c (x.time c) x.space i
```

## C. Smoothness of the electric field

**`Electromagnetism.ElectromagneticPotential.electricField_contDiff`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ElectricField.lean#L203).

```lean
lemma electricField_contDiff {n} {c : SpeedOfLight} {A : ElectromagneticPotential d}
    (hA : ContDiff ℝ (n + 1) A) : ContDiff ℝ n ↿(A.electricField c)
```

**`Electromagnetism.ElectromagneticPotential.electricField_apply_contDiff_space`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ElectricField.lean#L217).

```lean
lemma electricField_apply_contDiff_space {n} {A : ElectromagneticPotential d}
    {c : SpeedOfLight}
    (hA : ContDiff ℝ (n + 1) A) (t : Time) :
    ContDiff ℝ n (fun x => A.electricField c t x i)
```

## D. Differentiability of the electric field

**`Electromagnetism.ElectromagneticPotential.electricField_differentiable_time`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ElectricField.lean#L230).

```lean
lemma electricField_differentiable_time {A : ElectromagneticPotential d} {c : SpeedOfLight}
    (hA : ContDiff ℝ 2 A) (x : Space d) : Differentiable ℝ (A.electricField c · x)
```

## E. Time derivative of the vector potential in terms of the electric field

**`Electromagnetism.ElectromagneticPotential.time_deriv_vectorPotential_eq_electricField`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ElectricField.lean#L240).

```lean
lemma time_deriv_vectorPotential_eq_electricField {d} {c : SpeedOfLight}
    (A : ElectromagneticPotential d)
    (t : Time) (x : Space d) :
    ∂ₜ (fun t => A.vectorPotential c t x) t =
    - A.electricField c t x - ∇ (A.scalarPotential c t) x
```

**`Electromagnetism.ElectromagneticPotential.time_deriv_comp_vectorPotential_eq_electricField`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ElectricField.lean#L248).

```lean
lemma time_deriv_comp_vectorPotential_eq_electricField {d} {A : ElectromagneticPotential d}
    {c : SpeedOfLight}
    (hA : Differentiable ℝ A)
    (t : Time) (x : Space d) (i : Fin d) :
    ∂ₜ (fun t => A.vectorPotential c t x i) t =
    - A.electricField c t x i - ∂[i] (A.scalarPotential c t) x
```

## F. Derivatives of the electric field in terms of field strength tensor

**`Electromagnetism.ElectromagneticPotential.time_deriv_electricField_eq_toFieldStrength_eval`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ElectricField.lean#L267).

```lean
lemma time_deriv_electricField_eq_toFieldStrength_eval {d} {A : ElectromagneticPotential d}
    {c : SpeedOfLight} (hA : ContDiff ℝ 2 A) (t : Time) (x : Space d) (i : Fin d) :
    ∂ₜ (fun t => A.electricField c t x) t i =
    - c ^ 2 * ∂_ (Sum.inl 0) (fun x => toScalar {A.toFieldStrength x | [Sum.inl 0] [Sum.inr i]}ᵀ)
    ((toTimeAndSpace c).symm (t, x))
```

**`Electromagnetism.ElectromagneticPotential.div_electricField_eq_toFieldStrength_eval`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ElectricField.lean#L283).

```lean
lemma div_electricField_eq_toFieldStrength_eval {d} {A : ElectromagneticPotential d}
    {c : SpeedOfLight} (hA : ContDiff ℝ 2 A) (t : Time) (x : Space d) :
    (∇ ⬝ A.electricField c t) x = c * ∑ (μ : (Fin 1 ⊕ Fin d)),
      (∂_ μ (fun x => toScalar {A.toFieldStrength x | [μ] [Sum.inl 0]}ᵀ)
        ((toTimeAndSpace c).symm (t, x)))
```

## Depends on

- [A. Electromagnetism](../basic.md)
- [The Field Strength Tensor (Kinematics/FieldStrength)](fieldstrength.md)
- [The Scalar Potential (Kinematics/ScalarPotential)](scalarpotential.md)

## Sources

- [Physlib/Electromagnetism/Kinematics/ElectricField.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/ElectricField.lean)
