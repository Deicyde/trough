---
declaration: module
origin: cited
lean: PauliMatrix.indexEquiv, PauliMatrix.tensorial, PauliMatrix.toTensor_symm_apply, PauliMatrix.toTensor_symm_basis, PauliMatrix.toTensor_basis_expand, PauliMatrix.toTensor_eq_pauli, PauliMatrix.pauliContrComponent, PauliMatrix.pauliContrDownComponent
statement: formalized
proof: formalized
---

# Pauli matrices as a tensor

The module `Physlib.Relativity.Bispinors.Pauli.ToTensor`, [Physlib/Relativity/Bispinors/Pauli/ToTensor.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean): 29 declarations, 18 with a docstring.

## Tensorial structure

> The tensorial structure on the type
> `Fin 1 ⊕ Fin 3 → Matrix (Fin 2) (Fin 2) ℂ`
> and properties thereof.

**`PauliMatrix.indexEquiv`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L49).

> The equivalence between the type of indices of a [.up, .upL, .upR] tensor and
> `(Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2`.

```lean
def indexEquiv : ComponentIdx (S := complexLorentzTensor) ![.up, .upL, .upR] ≃
    (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2
```

**`PauliMatrix.tensorial`**, an instance, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L58).

```lean
instance tensorial : TensorSpecies.Tensorial complexLorentzTensor
    ![.up, .upL, .upR] (Fin 1 ⊕ Fin 3 → Matrix (Fin 2) (Fin 2) ℂ)
```

**`PauliMatrix.toTensor_symm_apply`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L74).

```lean
lemma toTensor_symm_apply (p : ℂT[.up, .upL, .upR]) :
    (toTensor (self := tensorial)).symm p =
    ((Equiv.piCongrRight fun _ => Equiv.curry _ _ _) <|
    (Equiv.curry _ _ _) <|
    Equiv.piCongrLeft' _ indexEquiv <|
    Finsupp.equivFunOnFinite <|
    (Tensor.basis (S := complexLorentzTensor) _).repr p)
```

**`PauliMatrix.toTensor_symm_basis`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L82).

```lean
lemma toTensor_symm_basis (b : ComponentIdx (S := complexLorentzTensor) ![.up, .upL, .upR]) :
    (toTensor (self := tensorial)).symm (Tensor.basis ![Color.up, Color.upL, Color.upR] b) =
    fun μ α β => if indexEquiv b = (μ, α, β) then 1 else 0
```

## Pauli matrices as a tensor

**`PauliMatrix.toTensor_basis_expand`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L105).

```lean
lemma toTensor_basis_expand : σ^^^ =
    Tensor.basis ![Color.up, Color.upL, Color.upR]
      (fun | 0 => (Sum.inl 0 : Fin 1 ⊕ Fin 3) | 1 => (0 : Fin 2) | 2 => (0 : Fin 2))
    + Tensor.basis ![Color.up, Color.upL, Color.upR]
      (fun | 0 => (Sum.inl 0 : Fin 1 ⊕ Fin 3) | 1 => (1 : Fin 2) | 2 => (1 : Fin 2))
    + Tensor.basis ![Color.up, Color.upL, Color.upR]
      (fun | 0 => (Sum.inr 0 : Fin 1 ⊕ Fin 3) | 1 => (0 : Fin 2) | 2 => (1 : Fin 2))
    + Tensor.basis ![Color.up, Color.upL, Color.upR]
      (fun | 0 => (Sum.inr 0 : Fin 1 ⊕ Fin 3) | 1 => (1 : Fin 2) | 2 => (0 : Fin 2))
    - I • Tensor.basis ![Color.up, Color.upL, Color.upR]
      (fun | 0 => (Sum.inr 1 : Fin 1 ⊕ Fin 3) | 1 => (0 : Fin 2) | 2 => (1 : Fin 2))
    + I • Tensor.basis ![Color.up, Color.upL, Color.upR]
      (fun | 0 => (Sum.inr 1 : Fin 1 ⊕ Fin 3) | 1 => (1 : Fin 2) | 2 => (0 : Fin 2))
    + Tensor.basis ![Color.up, Color.upL, Color.upR]
      (fun | 0 => (Sum.inr 2 : Fin 1 ⊕ Fin 3) | 1 => (0 : Fin 2) | 2 => (0 : Fin 2))
    - Tensor.basis ![Color.up, Color.upL, Color.upR]
      (fun | 0 => (Sum.inr 2 : Fin 1 ⊕ Fin 3) | 1 => (1 : Fin 2) | 2 => (1 : Fin 2))
```

**`PauliMatrix.toTensor_eq_pauli`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L128).

```lean
lemma toTensor_eq_pauli :
    σ^^^ = fromConstTriple (S := complexLorentzTensor)
      (c1 := Color.up) (c2 := Color.upL) (c3 := Color.upR) ComplexVector.pauli
```

**`PauliMatrix.pauliContrComponent`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L141).

> Gaussian integer components of the contravariant Pauli four-vector.

```lean
def pauliContrComponent (mu : Fin 1 ⊕ Fin 3) (a b : Fin 2) : GaussianInt
```

**`PauliMatrix.pauliContrDownComponent`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L150).

> Gaussian integer components of the contravariant conjugate Pauli four-vector.

```lean
def pauliContrDownComponent (mu : Fin 1 ⊕ Fin 3) (a b : Fin 2) : GaussianInt
```

**`PauliMatrix.toTensor_eq_ofGaussianInt`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L158).

```lean
lemma toTensor_eq_ofGaussianInt : σ^^^ = ofGaussianInt (fun b =>
    pauliContrComponent (b 0) (b 1) (b 2))
```

**`PauliMatrix.toTensor_dualLeft_eq_ofGaussianInt`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L175).

> Gaussian integer components of `σ^^^` after dualizing its left-handed Weyl index.

```lean
lemma toTensor_dualLeft_eq_ofGaussianInt :
    {σ^^^ | μ τ(α) β}ᵀ =
      ofGaussianInt (fun b =>
        ∑ x : Fin 2, pauliContrComponent (b 0) x (b 2) *
          (if x.val = 0 ∧ Fin.val (b 1) = 1 then 1 else
            if Fin.val (b 1) = 0 ∧ x.val = 1 then -1 else 0))
```

**`PauliMatrix.toTensor_dualWeyl_eq_ofGaussianInt`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L195).

> Gaussian integer components of `σ^^^` after dualizing both Weyl indices.

```lean
lemma toTensor_dualWeyl_eq_ofGaussianInt :
    {σ^^^ | μ τ(α) τ(β)}ᵀ =
      ofGaussianInt (fun b =>
        pauliContrDownComponent (b 0) (b 2) (b 1))
```

**`PauliMatrix.toTensor_dualLorentz_eq_ofGaussianInt`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L214).

> Gaussian integer components of `σ^^^` after dualizing its Lorentz index.

```lean
lemma toTensor_dualLorentz_eq_ofGaussianInt :
    {σ^^^ | τ(μ) α β}ᵀ =
      ofGaussianInt (fun b => pauliContrDownComponent (b 0) (b 1) (b 2))
```

**`PauliMatrix.toTensor_dualLorentzLeft_eq_ofGaussianInt`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L232).

> Gaussian integer components of `σ^^^` after dualizing its Lorentz and left-handed Weyl
> indices.

```lean
lemma toTensor_dualLorentzLeft_eq_ofGaussianInt :
    {σ^^^ | τ(μ) τ(α) β}ᵀ = ofGaussianInt (fun b =>
      ∑ x : Fin 2, pauliContrDownComponent (b 0) x (b 2) *
        (if x.val = 0 ∧ Fin.val (b 1) = 1 then 1 else
          if Fin.val (b 1) = 0 ∧ x.val = 1 then -1 else 0))
```

**`PauliMatrix.toTensor_dualAll_eq_ofGaussianInt`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L252).

> Gaussian integer components of `σ^^^` after dualizing all three indices.

```lean
lemma toTensor_dualAll_eq_ofGaussianInt :
    {σ^^^ | τ(μ) τ(α) τ(β)}ᵀ =
      ofGaussianInt (fun b => pauliContrComponent (b 0) (b 2) (b 1))
```

**`PauliMatrix.smul_eq_self`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L270).

```lean
lemma smul_eq_self (Λ : SL(2,ℂ)) : Λ • pauliMatrix = pauliMatrix
```

**`PauliMatrix.toTensor_smul_eq_self`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L275).

```lean
lemma toTensor_smul_eq_self (Λ : SL(2,ℂ)) : Λ • σ^^^ = σ^^^
```

## Variations of the pauli tensor

**`PauliMatrix.pauliCo`**, an abbrev, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L286).

> The Pauli matrices as the complex Lorentz tensor `σ_μ^α^{dot β}`.

```lean
abbrev pauliCo : ℂT[.down, .upL, .upR]
```

**`PauliMatrix.pauliCoDown`**, an abbrev, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L293).

> The Pauli matrices as the complex Lorentz tensor `σ_μ_{dot β}_α`.

```lean
abbrev pauliCoDown : ℂT[.down, .downR, .downL]
```

**`PauliMatrix.pauliContrDown`**, an abbrev, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L300).

> The Pauli matrices as the complex Lorentz tensor `σ^μ_{dot β}_α`.

```lean
abbrev pauliContrDown : ℂT[.up, .downR, .downL]
```

## Different forms

**`PauliMatrix.pauliCo_eq_ofGaussianInt`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L312).

```lean
lemma pauliCo_eq_ofGaussianInt : pauliCo = ofGaussianInt (fun b =>
    pauliContrDownComponent (b 0) (b 1) (b 2))
```

**`PauliMatrix.pauliCoDown_eq_ofGaussianInt`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L332).

```lean
lemma pauliCoDown_eq_ofGaussianInt : pauliCoDown = ofGaussianInt (fun b =>
    pauliContrComponent (b 0) (b 1) (b 2))
```

**`PauliMatrix.pauliContrDown_ofGaussianInt`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L364).

```lean
lemma pauliContrDown_ofGaussianInt : pauliContrDown = ofGaussianInt (fun b =>
    pauliContrDownComponent (b 0) (b 1) (b 2))
```

## Index dualization

**`PauliMatrix.toTensor_dualWeyl_eq_pauliContrDown`**, a lemma, [line 403](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L403).

> Dualizing both Weyl indices of `σ^^^` gives `σ^__`.

```lean
lemma toTensor_dualWeyl_eq_pauliContrDown :
    ({σ^^^ | μ τ(α) τ(β) = σ^__ | μ β α}ᵀ : Prop)
```

**`PauliMatrix.toTensor_dualAll_eq_pauliCoDown`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L410).

> Dualizing all three indices of `σ^^^` gives `σ___`.

```lean
lemma toTensor_dualAll_eq_pauliCoDown :
    ({σ^^^ | τ(μ) τ(α) τ(β) = σ___ | μ β α}ᵀ : Prop)
```

**`PauliMatrix.pauliDual_eq_pauliCo`**, a lemma, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L417).

> Lowering the Lorentz index of `σ^^^` with `τ` gives `σ_^^`.

```lean
lemma pauliDual_eq_pauliCo :
    ({σ^^^ | τ(μ) α β = σ_^^ | μ α β}ᵀ : Prop)
```

**`PauliMatrix.pauliContrDownDual_eq_pauliCoDown`**, a lemma, [line 424](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L424).

> Lowering the Lorentz index of `σ^__` with `τ` gives `σ___`.

```lean
lemma pauliContrDownDual_eq_pauliCoDown :
    ({σ^__ | τ(μ) β α = σ___ | μ β α}ᵀ : Prop)
```

## Group actions

**`PauliMatrix.smul_pauliCo`**, a lemma, [line 468](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L468).

> The tensor `pauliCo` is invariant under the action of `SL(2,ℂ)`.

```lean
lemma smul_pauliCo (g : SL(2,ℂ)) : g • pauliCo = pauliCo
```

**`PauliMatrix.smul_pauliCoDown`**, a lemma, [line 474](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L474).

> The tensor `pauliCoDown` is invariant under the action of `SL(2,ℂ)`.

```lean
lemma smul_pauliCoDown (g : SL(2,ℂ)) : g • pauliCoDown = pauliCoDown
```

**`PauliMatrix.smul_pauliContrDown`**, a lemma, [line 480](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean#L480).

> The tensor `pauliContrDown` is invariant under the action of `SL(2,ℂ)`.

```lean
lemma smul_pauliContrDown (g : SL(2,ℂ)) : g • pauliContrDown = pauliContrDown
```

## Depends on

- [Physlib.Relativity.Bispinors.Pauli.Basic](pauli-basic.md)
- [Physlib.Relativity.Tensors.ComplexTensor.Metrics.Basic](../tensors/part-01/complextensor-metrics-basic.md)

## Sources

- [Physlib/Relativity/Bispinors/Pauli/ToTensor.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/ToTensor.lean)
