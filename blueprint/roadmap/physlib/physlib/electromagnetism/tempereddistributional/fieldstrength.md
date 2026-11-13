---
declaration: module
origin: cited
lean: Electromagnetism.TempDistElectromagneticPotential.fieldStrengthAux, Electromagnetism.TempDistElectromagneticPotential.fieldStrengthAux_eq_add, Electromagnetism.TempDistElectromagneticPotential.toTensor_fieldStrengthAux, Electromagnetism.TempDistElectromagneticPotential.toTensor_fieldStrengthAux_basis_repr, Electromagnetism.TempDistElectromagneticPotential.fieldStrengthAux_tensor_basis_eq_basis, Electromagnetism.TempDistElectromagneticPotential.fieldStrengthAux_basis_repr_apply, Electromagnetism.TempDistElectromagneticPotential.fieldStrengthAux_basis_repr_apply_eq_single, Electromagnetism.TempDistElectromagneticPotential.fieldStrengthAux_eq_basis
statement: formalized
proof: formalized
---

# The Field Strength Tensor

The module `Physlib.Electromagnetism.TemperedDistributional.FieldStrength`, [Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean): 16 declarations, 2 with a docstring.

## i. Overview

> In this module we define the field strength tensor in terms of the electromagnetic potential.

## ii. Key results

> - `TempDistElectromagneticPotential.fieldStrength` : The field strength for
>   electromagnetic potentials which are distributions.

## iv. References

> * None.

## A. Field strength for distributions

### A.1. Auxiliary definition of field strength for distributions, with no linearity

**`Electromagnetism.TempDistElectromagneticPotential.fieldStrengthAux`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean#L66).

> An auxiliary definition for the field strength of an electromagnetic potential
> based on a distribution. On Schwartz maps this has the same value as the field strength
> tensor, but no linearity or continuous properties built in.

```lean
noncomputable def fieldStrengthAux {d} (A : TempDistElectromagneticPotential d)
    (ε : 𝓢(SpaceTime d, ℝ)) : Lorentz.Vector d ⊗[ℝ] Lorentz.Vector d
```

**`Electromagnetism.TempDistElectromagneticPotential.fieldStrengthAux_eq_add`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean#L72).

```lean
lemma fieldStrengthAux_eq_add {d} (A : TempDistElectromagneticPotential d) (ε : 𝓢(SpaceTime d, ℝ)) :
    fieldStrengthAux A ε =
    Tensorial.toTensor.symm
      (permT id (IsReindexing.auto) {(η d | μ μ' ⊗ distTensorDeriv A ε | μ' ν)}ᵀ)
    - Tensorial.toTensor.symm (permT ![1, 0] (IsReindexing.auto)
      {(η d | μ μ' ⊗ distTensorDeriv A ε | μ' ν)}ᵀ)
```

**`Electromagnetism.TempDistElectromagneticPotential.toTensor_fieldStrengthAux`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean#L86).

```lean
lemma toTensor_fieldStrengthAux {d} (A : TempDistElectromagneticPotential d)
    (ε : 𝓢(SpaceTime d, ℝ)) :
    Tensorial.toTensor (fieldStrengthAux A ε) =
    (permT id (IsReindexing.auto) {(η d | μ μ' ⊗ distTensorDeriv A ε | μ' ν)}ᵀ)
    - (permT ![1, 0] (IsReindexing.auto)
      {(η d | μ μ' ⊗ distTensorDeriv A ε | μ' ν)}ᵀ)
```

**`Electromagnetism.TempDistElectromagneticPotential.toTensor_fieldStrengthAux_basis_repr`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean#L95).

```lean
lemma toTensor_fieldStrengthAux_basis_repr {d} (A : TempDistElectromagneticPotential d)
    (ε : 𝓢(SpaceTime d, ℝ))
    (b : ComponentIdx (S := realLorentzTensor d) (Fin.append ![Color.up] ![Color.up])) :
    (Tensor.basis _).repr (Tensorial.toTensor (fieldStrengthAux A ε)) b =
    ∑ κ, (η (b 0) κ * SpaceTime.distDeriv κ A ε (b 1) -
      η (b 1) κ * SpaceTime.distDeriv κ A ε (b 0))
```

**`Electromagnetism.TempDistElectromagneticPotential.fieldStrengthAux_tensor_basis_eq_basis`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean#L125).

```lean
lemma fieldStrengthAux_tensor_basis_eq_basis {d} (A : TempDistElectromagneticPotential d)
    (ε : 𝓢(SpaceTime d, ℝ))
    (b : ComponentIdx (S := realLorentzTensor d) (Fin.append ![Color.up] ![Color.up])) :
    (Tensor.basis _).repr (Tensorial.toTensor (A.fieldStrengthAux ε)) b =
    (Lorentz.Vector.basis.tensorProduct Lorentz.Vector.basis).repr (A.fieldStrengthAux ε)
      (b 0, b 1)
```

**`Electromagnetism.TempDistElectromagneticPotential.fieldStrengthAux_basis_repr_apply`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean#L147).

```lean
lemma fieldStrengthAux_basis_repr_apply {d} {μν : (Fin 1 ⊕ Fin d) × (Fin 1 ⊕ Fin d)}
    (A : TempDistElectromagneticPotential d) (ε : 𝓢(SpaceTime d, ℝ)) :
    (Lorentz.Vector.basis.tensorProduct Lorentz.Vector.basis).repr (A.fieldStrengthAux ε) μν =
    ∑ κ, ((η μν.1 κ * distDeriv κ A ε μν.2) - η μν.2 κ * distDeriv κ A ε μν.1)
```

**`Electromagnetism.TempDistElectromagneticPotential.fieldStrengthAux_basis_repr_apply_eq_single`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean#L158).

```lean
lemma fieldStrengthAux_basis_repr_apply_eq_single {d} {μν : (Fin 1 ⊕ Fin d) × (Fin 1 ⊕ Fin d)}
    (A : TempDistElectromagneticPotential d) (ε : 𝓢(SpaceTime d, ℝ)) :
    (Lorentz.Vector.basis.tensorProduct Lorentz.Vector.basis).repr (A.fieldStrengthAux ε) μν =
    ((η μν.1 μν.1 * distDeriv μν.1 A ε μν.2) - η μν.2 μν.2 * distDeriv μν.2 A ε μν.1)
```

**`Electromagnetism.TempDistElectromagneticPotential.fieldStrengthAux_eq_basis`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean#L176).

```lean
lemma fieldStrengthAux_eq_basis {d} (A : TempDistElectromagneticPotential d)
    (ε : 𝓢(SpaceTime d, ℝ)) :
    (A.fieldStrengthAux ε) = ∑ μ, ∑ ν,
      ((η μ μ * distDeriv μ A ε ν) - η ν ν * distDeriv ν A ε μ)
      • Lorentz.Vector.basis μ ⊗ₜ[ℝ] Lorentz.Vector.basis ν
```

### A.2. The definition of the field strength

**`Electromagnetism.TempDistElectromagneticPotential.fieldStrength`**, a def, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean#L197).

> The field strength of an electromagnetic potential which is a distribution.

```lean
noncomputable def fieldStrength {d} :
    TempDistElectromagneticPotential d →ₗ[ℝ]
    (SpaceTime d) →d[ℝ] Lorentz.Vector d ⊗[ℝ] Lorentz.Vector d
```

**`Electromagnetism.TempDistElectromagneticPotential.fieldStrength_eq_fieldStrengthAux`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean#L232).

```lean
lemma fieldStrength_eq_fieldStrengthAux {d} (A : TempDistElectromagneticPotential d)
    (ε : 𝓢(SpaceTime d, ℝ)) :
    A.fieldStrength ε = A.fieldStrengthAux ε
```

### A.3. Field strength written in terms of a basis

**`Electromagnetism.TempDistElectromagneticPotential.fieldStrength_eq_basis`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean#L241).

```lean
lemma fieldStrength_eq_basis {d} (A : TempDistElectromagneticPotential d)
    (ε : 𝓢(SpaceTime d, ℝ)) :
    A.fieldStrength ε = ∑ μ, ∑ ν,
      ((η μ μ * distDeriv μ A ε ν) - η ν ν * distDeriv ν A ε μ)
      • Lorentz.Vector.basis μ ⊗ₜ[ℝ] Lorentz.Vector.basis ν
```

**`Electromagnetism.TempDistElectromagneticPotential.fieldStrength_basis_repr_eq_single`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean#L249).

```lean
lemma fieldStrength_basis_repr_eq_single {d} {μν : (Fin 1 ⊕ Fin d) × (Fin 1 ⊕ Fin d)}
    (A : TempDistElectromagneticPotential d) (ε : 𝓢(SpaceTime d, ℝ)) :
    (Lorentz.Vector.basis.tensorProduct Lorentz.Vector.basis).repr (A.fieldStrength ε) μν =
    ((η μν.1 μν.1 * distDeriv μν.1 A ε μν.2) - η μν.2 μν.2 * distDeriv μν.2 A ε μν.1)
```

**`Electromagnetism.TempDistElectromagneticPotential.fieldStrength_diag_zero`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean#L257).

```lean
lemma fieldStrength_diag_zero {d} (A : TempDistElectromagneticPotential d)
    (ε : 𝓢(SpaceTime d, ℝ)) (μ : Fin 1 ⊕ Fin d) :
    (Lorentz.Vector.basis.tensorProduct Lorentz.Vector.basis).repr
    (A.fieldStrength ε) (μ, μ) = 0
```

**`Electromagnetism.TempDistElectromagneticPotential.distDeriv_fieldStrength_diag_zero`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean#L265).

```lean
lemma distDeriv_fieldStrength_diag_zero {d} (A : TempDistElectromagneticPotential d)
    (ε : 𝓢(SpaceTime d, ℝ)) (μ ν : Fin 1 ⊕ Fin d) :
    (Lorentz.Vector.basis.tensorProduct Lorentz.Vector.basis).repr
    (distDeriv ν A.fieldStrength ε) (μ, μ) = 0
```

**`Electromagnetism.TempDistElectromagneticPotential.fieldStrength_antisymmetric_basis`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean#L272).

```lean
lemma fieldStrength_antisymmetric_basis {d} (A : TempDistElectromagneticPotential d)
    (ε : 𝓢(SpaceTime d, ℝ)) (μ ν : Fin 1 ⊕ Fin d) :
    (Vector.basis.tensorProduct Vector.basis).repr
    (A.fieldStrength ε) (μ, ν) = - (Vector.basis.tensorProduct Vector.basis).repr
    (A.fieldStrength ε) (ν, μ)
```

### A.4. Equivariance of the field strength for distributions

**`Electromagnetism.TempDistElectromagneticPotential.fieldStrength_equivariant`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean#L286).

```lean
lemma fieldStrength_equivariant {d} (A : TempDistElectromagneticPotential d)
    (Λ : LorentzGroup d) :
    (Λ • A).fieldStrength = Λ • A.fieldStrength
```

## Depends on

- [The Electromagnetic Potential](basic.md)

## Sources

- [Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/FieldStrength.lean)
