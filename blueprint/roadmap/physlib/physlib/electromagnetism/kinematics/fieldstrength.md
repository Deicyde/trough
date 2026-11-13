---
declaration: module
origin: cited
lean: Electromagnetism.ElectromagneticPotential.toFieldStrength, Electromagnetism.ElectromagneticPotential.toFieldStrength_eq_deriv, Electromagnetism.ElectromagneticPotential.toFieldStrength_eq_tensorDeriv, Electromagnetism.ElectromagneticPotential.toFieldStrength_eq_add, Electromagnetism.ElectromagneticPotential.toFieldStrength_eq_sub_tensorDeriv, Electromagnetism.ElectromagneticPotential.toTensor_toFieldStrength, Electromagnetism.ElectromagneticPotential.toFieldStrength_eq_sum_basis_eval, Electromagnetism.ElectromagneticPotential.toFieldStrength_eq_sum_basis
statement: formalized
proof: formalized
---

# The Field Strength Tensor

The module `Physlib.Electromagnetism.Kinematics.FieldStrength`, [Physlib/Electromagnetism/Kinematics/FieldStrength.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean): 30 declarations, 9 with a docstring.

## i. Overview

> In this module we define the field strength tensor in terms of the electromagnetic potential.
>
> We define the tensor and prove various properties of it. Its components are accessed
> through index evaluation, `toScalar {A.toFieldStrength x | [μ] [ν]}ᵀ`.

## ii. Key results

> - `toFieldStrength` : The field strength tensor from an electromagnetic potential.
> - `toFieldStrength_eval_apply_eq_single` : The components of the field strength tensor
>   in terms of derivatives of the potential, `F^{μν} = η^{μμ} ∂_μ A^ν - η^{νν} ∂_ν A^μ`.

## iv. References

> * None.

## A. The field strength tensor

> We define the field strength tensor `F^{μν}` in terms of the derivative of the
> electromagnetic potential `A^μ`. We then prove that this tensor transforms correctly
> under Lorentz transformations.

**`Electromagnetism.ElectromagneticPotential.toFieldStrength`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L73).

> The field strength from an electromagnetic potential, as a tensor `F^{μν}`.

```lean
noncomputable def toFieldStrength {d} (A : ElectromagneticPotential d) :
    SpaceTime d → Lorentz.Vector d ⊗[ℝ] Lorentz.Vector d
```

### A.1. Tensor equalities

> These equalities for the field strength tensor are in
> terms of tensor expressions and index notation. In practice,
> we don't expect them to be used explicitly. They are useful for proving some
> of the API within this module.

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eq_deriv`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L90).

```lean
lemma toFieldStrength_eq_deriv {d} (A : ElectromagneticPotential d) (x : SpaceTime d) :
    toFieldStrength A x =
    Tensorial.toTensor.symm (permT id IsReindexing.auto {(η d | μ μ' ⊗ A.deriv x | μ' ν)
    + - (η d | ν ν' ⊗ A.deriv x | ν' μ)}ᵀ)
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eq_tensorDeriv`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L96).

```lean
lemma toFieldStrength_eq_tensorDeriv {d} {A : ElectromagneticPotential d}
    (hA : Differentiable ℝ A) (x : SpaceTime d) :
    toFieldStrength A x =
    Tensorial.toTensor.symm (permT id IsReindexing.auto {(η d | μ μ' ⊗ tensorDeriv A x | μ' ν)
    + - (η d | ν ν' ⊗ tensorDeriv A x | ν' μ)}ᵀ)
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eq_add`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L103).

```lean
lemma toFieldStrength_eq_add {d} (A : ElectromagneticPotential d) (x : SpaceTime d) :
    toFieldStrength A x =
    Tensorial.toTensor.symm (permT id (IsReindexing.auto) {(η d | μ μ' ⊗ A.deriv x | μ' ν)}ᵀ)
    - Tensorial.toTensor.symm (permT ![1, 0] (IsReindexing.auto)
      {(η d | μ μ' ⊗ A.deriv x | μ' ν)}ᵀ)
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eq_sub_tensorDeriv`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L111).

```lean
lemma toFieldStrength_eq_sub_tensorDeriv {d} {A : ElectromagneticPotential d}
    (hA : Differentiable ℝ A) (x : SpaceTime d) :
    toFieldStrength A x =
    Tensorial.toTensor.symm (permT id IsReindexing.auto {η d | μ μ' ⊗ tensorDeriv A x | μ' ν}ᵀ)
    - Tensorial.toTensor.symm (permT ![1, 0] IsReindexing.auto
    {η d | μ μ' ⊗ tensorDeriv A x | μ' ν}ᵀ)
```

**`Electromagnetism.ElectromagneticPotential.toTensor_toFieldStrength`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L120).

```lean
lemma toTensor_toFieldStrength {d} (A : ElectromagneticPotential d) (x : SpaceTime d) :
    Tensorial.toTensor (toFieldStrength A x) =
    (permT id (IsReindexing.auto) {(η d | μ μ' ⊗ A.deriv x | μ' ν)}ᵀ)
    - (permT ![1, 0] (IsReindexing.auto) {(η d | μ μ' ⊗ A.deriv x | μ' ν)}ᵀ)
```

### A.2. Vector equalities

> These equalities for the field strength tensor are in terms of vector basis.
> They match some of the familiar forms one might expect to see the field strength
> tensor in.

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eq_sum_basis_eval`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L138).

> The statement that `F = F^{μν} eᵤ ⊗ eᵥ` written explicitly, with
> the components extracted via `toScalar`.

```lean
lemma toFieldStrength_eq_sum_basis_eval {d} {A : ElectromagneticPotential d} :
    A.toFieldStrength = fun x => ∑ μ, ∑ ν, toScalar {A.toFieldStrength x| [μ] [ν]}ᵀ •
      Vector.basis μ ⊗ₜ[ℝ] Vector.basis ν
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eq_sum_basis`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L147).

> The statement that `F = F^{μν} eᵤ ⊗ eᵥ` written explicitly, with
> the components given by `∑ κ, (η μ κ * ∂_ κ A x ν - η ν κ * ∂_ κ A x μ)`.

```lean
lemma toFieldStrength_eq_sum_basis {d} {A : ElectromagneticPotential d}
    (hA : Differentiable ℝ A) (x : SpaceTime d) :
    A.toFieldStrength x = ∑ μ, ∑ ν, (∑ κ, (η μ κ * ∂_ κ A x ν - η ν κ * ∂_ κ A x μ)) •
      Lorentz.Vector.basis μ ⊗ₜ Lorentz.Vector.basis ν
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eq_sum_basis_single`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L171).

> The statement that `F = F^{μν} eᵤ ⊗ eᵥ` written explicitly, with
> with the components given by `(η μ μ * ∂_ μ A x ν - η ν ν * ∂_ ν A x μ)`.

```lean
lemma toFieldStrength_eq_sum_basis_single {d} {A : ElectromagneticPotential d}
    (hA : Differentiable ℝ A) (x : SpaceTime d) :
    A.toFieldStrength x = ∑ μ, ∑ ν, (η μ μ * ∂_ μ A x ν - η ν ν * ∂_ ν A x μ) •
      Lorentz.Vector.basis μ ⊗ₜ Lorentz.Vector.basis ν
```

## A.3. The group action acting on the field strength tensor

> We show that the field strength tensor is equivariant under the action of the Lorentz group.
> That is transforming the potential and then taking the field strength is the same
> as taking the field strength and then transforming the resulting tensor.

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_equivariant`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L194).

```lean
lemma toFieldStrength_equivariant {d} (A : ElectromagneticPotential d) (Λ : LorentzGroup d)
    (hf : Differentiable ℝ A) (x : SpaceTime d) :
    (Λ • A).toFieldStrength x = Λ • A.toFieldStrength (Λ⁻¹ • x)
```

## A.4. Differentiability and smoothness of the field strength tensor

**`Electromagnetism.ElectromagneticPotential.differentiable_toFieldStrength`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L208).

```lean
lemma differentiable_toFieldStrength {d} {A : ElectromagneticPotential d} (hA : ContDiff ℝ 2 A) :
    Differentiable ℝ A.toFieldStrength
```

**`Electromagnetism.ElectromagneticPotential.differentiable_toFieldStrength_of_smooth`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L217).

```lean
lemma differentiable_toFieldStrength_of_smooth {d}
    {A : ElectromagneticPotential d} (hA : ContDiff ℝ ∞ A) :
    Differentiable ℝ A.toFieldStrength
```

**`Electromagnetism.ElectromagneticPotential.contDiff_toFieldStrength`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L223).

```lean
lemma contDiff_toFieldStrength {d} {n : WithTop ℕ∞} {A : ElectromagneticPotential d}
    (hA : ContDiff ℝ (n + 1) A) : ContDiff ℝ n A.toFieldStrength
```

### A.5. Components of the field strength tensor

> The components `F^{μν}` of the field strength tensor are accessed through index evaluation,
> `toScalar {A.toFieldStrength x | [μ] [ν]}ᵀ`. This is the canonical way to refer to the
> components of the field strength tensor, and is what should be used downstream.

#### A.5.1. Index evaluation

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_eq_tensor_basis_repr`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L243).

> Evaluating both tensor indices of the field strength gives the coefficient in the
> tensor basis.

```lean
lemma toFieldStrength_eval_eq_tensor_basis_repr {d} (A : ElectromagneticPotential d)
    (x : SpaceTime d) (μ ν : Fin 1 ⊕ Fin d) :
    toScalar {A.toFieldStrength x | [μ] [ν]}ᵀ =
    (Tensor.basis _).repr (Tensorial.toTensor (toFieldStrength A x)) (fun | 0 => μ | 1 => ν)
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_tensor_basis_repr_eq_eval`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L251).

> The coefficient of the field strength tensor in the tensor basis is given by
> index evaluation.

```lean
lemma toFieldStrength_tensor_basis_repr_eq_eval {d} (A : ElectromagneticPotential d)
    (x : SpaceTime d)
    (b : ComponentIdx (S := realLorentzTensor d) (Fin.append ![Color.up] ![Color.up])) :
    (Tensor.basis _).repr (Tensorial.toTensor (toFieldStrength A x)) b =
    toScalar {A.toFieldStrength x | [b 0] [b 1]}ᵀ
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_apply`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L263).

> The evaluated components of the field strength tensor in terms of derivatives of the
> electromagnetic potential.

```lean
lemma toFieldStrength_eval_apply {d} (A : ElectromagneticPotential d)
    (x : SpaceTime d) (μ ν : Fin 1 ⊕ Fin d) :
    toScalar {A.toFieldStrength x | [μ] [ν]}ᵀ =
    ∑ κ, (η μ κ * ∂_ κ A x ν - η ν κ * ∂_ κ A x μ)
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_apply_eq_single`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L276).

> The evaluated components of the field strength tensor after using diagonal form of the
> Minkowski metric.

```lean
lemma toFieldStrength_eval_apply_eq_single {d} (A : ElectromagneticPotential d)
    (x : SpaceTime d) (μ ν : Fin 1 ⊕ Fin d) :
    toScalar {A.toFieldStrength x | [μ] [ν]}ᵀ =
    η μ μ * ∂_ μ A x ν - η ν ν * ∂_ ν A x μ
```

#### A.5.2. Differentiability of the components

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_differentiable`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L294).

```lean
lemma toFieldStrength_eval_differentiable {d} {A : ElectromagneticPotential d}
    {μ ν : Fin 1 ⊕ Fin d} (hA : ContDiff ℝ 2 A) :
    Differentiable ℝ (fun x => toScalar {A.toFieldStrength x | [μ] [ν]}ᵀ)
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_differentiable_space`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L301).

```lean
lemma toFieldStrength_eval_differentiable_space {d} {A : ElectromagneticPotential d}
    {μ ν : Fin 1 ⊕ Fin d} (hA : ContDiff ℝ 2 A) (t : Time) {c : SpeedOfLight} :
    Differentiable ℝ (fun x =>
      toScalar {A.toFieldStrength ((toTimeAndSpace c).symm (t, x)) | [μ] [ν]}ᵀ)
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_differentiable_time`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L310).

```lean
lemma toFieldStrength_eval_differentiable_time {d} {A : ElectromagneticPotential d}
    {μ ν : Fin 1 ⊕ Fin d} (hA : ContDiff ℝ 2 A) (x : Space d) {c : SpeedOfLight} :
    Differentiable ℝ (fun t =>
      toScalar {A.toFieldStrength ((toTimeAndSpace c).symm (t, x)) | [μ] [ν]}ᵀ)
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_contDiff`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L319).

```lean
lemma toFieldStrength_eval_contDiff {d} {n : WithTop ℕ∞} {A : ElectromagneticPotential d}
    {μ ν : Fin 1 ⊕ Fin d} (hA : ContDiff ℝ (n + 1) A) :
    ContDiff ℝ n (fun x => toScalar {A.toFieldStrength x | [μ] [ν]}ᵀ)
```

### A.6. The antisymmetry of the field strength tensor

> We show that the field strength tensor is antisymmetric.

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_antisymm`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L333).

```lean
lemma toFieldStrength_eval_antisymm {d} (A : ElectromagneticPotential d) (x : SpaceTime d)
    (μ ν : Fin 1 ⊕ Fin d) :
    toScalar {A.toFieldStrength x | [μ] [ν]}ᵀ = - toScalar {A.toFieldStrength x | [ν] [μ]}ᵀ
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_diag_eq_zero`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L339).

```lean
lemma toFieldStrength_eval_diag_eq_zero {d} (A : ElectromagneticPotential d) (x : SpaceTime d)
    (μ : Fin 1 ⊕ Fin d) :
    toScalar {A.toFieldStrength x | [μ] [μ]}ᵀ = 0
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_antisymmetric`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L344).

```lean
lemma toFieldStrength_antisymmetric {d} (A : ElectromagneticPotential d) (x : SpaceTime d) :
    {A.toFieldStrength x | μ ν = - (A.toFieldStrength x | ν μ)}ᵀ
```

### A.7. Equivariance of the components of the field strength tensor

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_equivariant`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L359).

```lean
lemma toFieldStrength_eval_equivariant {d} (A : ElectromagneticPotential d)
    (Λ : LorentzGroup d) (hf : Differentiable ℝ A) (x : SpaceTime d)
    (μ ν : Fin 1 ⊕ Fin d) :
    toScalar {(Λ • A).toFieldStrength x | [μ] [ν]}ᵀ =
    ∑ κ, ∑ ρ, (Λ.1 μ κ * Λ.1 ν ρ) * toScalar {A.toFieldStrength (Λ⁻¹ • x) | [κ] [ρ]}ᵀ
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_action_eq_sum`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L383).

> This lemma expresses the component form of the transformed field strength
> tensor: when a Lorentz transformation Λ acts on the potential A, the resulting field strength
> tensor's components are given by the standard tensor transformation rule involving the Lorentz
> matrix elements Λ^μ\_κ and Λ^ν\_ρ applied to the original field components.

```lean
lemma toFieldStrength_action_eq_sum {d} (A : ElectromagneticPotential d) (Λ : LorentzGroup d)
    (hf : Differentiable ℝ A) (x : SpaceTime d) :
    (Λ • A).toFieldStrength x = ∑ μ, ∑ ν,
      (∑ κ, ∑ ρ, Λ.1 μ κ * Λ.1 ν ρ * toScalar {A.toFieldStrength (Λ⁻¹ • x) | [κ] [ρ]}ᵀ) •
      Vector.basis μ ⊗ₜ[ℝ] Vector.basis ν
```

### A.8. Linearity of the field strength tensor

> We show that the field strength tensor is linear in the potential.

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_add`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L399).

```lean
lemma toFieldStrength_eval_add {d} (A1 A2 : ElectromagneticPotential d)
    (x : SpaceTime d) (hA1 : Differentiable ℝ A1) (hA2 : Differentiable ℝ A2)
    (μ ν : Fin 1 ⊕ Fin d) :
    toScalar {(A1 + A2).toFieldStrength x | [μ] [ν]}ᵀ =
    toScalar {A1.toFieldStrength x | [μ] [ν]}ᵀ + toScalar {A2.toFieldStrength x | [μ] [ν]}ᵀ
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_add`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L410).

```lean
lemma toFieldStrength_add {d} (A1 A2 : ElectromagneticPotential d)
    (x : SpaceTime d) (hA1 : Differentiable ℝ A1) (hA2 : Differentiable ℝ A2) :
    toFieldStrength (A1 + A2) x = toFieldStrength A1 x + toFieldStrength A2 x
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_eval_smul`**, a lemma, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L419).

```lean
lemma toFieldStrength_eval_smul {d} (c : ℝ) (A : ElectromagneticPotential d)
    (x : SpaceTime d) (hA : Differentiable ℝ A) (μ ν : Fin 1 ⊕ Fin d) :
    toScalar {(c • A).toFieldStrength x | [μ] [ν]}ᵀ =
    c * toScalar {A.toFieldStrength x | [μ] [ν]}ᵀ
```

**`Electromagnetism.ElectromagneticPotential.toFieldStrength_smul`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean#L429).

```lean
lemma toFieldStrength_smul {d} (c : ℝ) (A : ElectromagneticPotential d)
    (x : SpaceTime d) (hA : Differentiable ℝ A) :
    toFieldStrength (c • A) x = c • toFieldStrength A x
```

## Depends on

- [The Electromagnetic Potential](empotential.md)

## Sources

- [Physlib/Electromagnetism/Kinematics/FieldStrength.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/FieldStrength.lean)
