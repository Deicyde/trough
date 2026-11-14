---
declaration: module
origin: cited
lean: PauliMatrix.pauliCo_contr_pauliContr, PauliMatrix.pauliCoDown_trace_pauliCo, PauliMatrix.pauliCo_trace_pauliCoDown, PauliMatrix.pauliContr_mul_pauliContrDown_add, PauliMatrix.auliContrDown_pauliContr_mul_add, PauliMatrix.pauliContr_mul_dualWeyl_eq_ofGaussianInt, PauliMatrix.dualWeyl_mul_pauliContr_eq_ofGaussianInt, PauliMatrix.leviCivita_mul_pauliDual
statement: formalized
proof: formalized
---

# Physlib.Relativity.Bispinors.Pauli.Relations

The module `Physlib.Relativity.Bispinors.Pauli.Relations`, [Physlib/Relativity/Bispinors/Pauli/Relations.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Relations.lean): 10 declarations, 6 with a docstring.

## Contraction of indices of Pauli matrix.

> The results in this file include contractions, anticommutators, and triple-product identities
> for the Pauli four-vectors.
>
> The current way this result is proved is by using tensor tree manipulations.
> There is likely a more direct path to this result.

## References

> * Dreiner, Haber and Martin, *Two-component spinor techniques and Feynman rules for quantum
>   field theory and supersymmetry*, arXiv:0812.1594, equations (2.54) and (2.55), in the
>   conventions `g = diag(+1, -1, -1, -1)` and `ε⁰¹²³ = +1`. [ref: Dreiner:2008tw]

**`PauliMatrix.pauliCo_contr_pauliContr`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Relations.lean#L41).

> The statement that ` σᵥᵃᵇ σᵛᵃ'ᵇ' = 2 εᵃᵃ' εᵇᵇ'`.

```lean
lemma pauliCo_contr_pauliContr :
    {σ_^^ | ν α β ⊗ σ^^^ | ν α' β' = (2 : ℂ) •ₜ εL | α α' ⊗ εR | β β'}ᵀ
```

**`PauliMatrix.pauliCoDown_trace_pauliCo`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Relations.lean#L80).

```lean
lemma pauliCoDown_trace_pauliCo : {(σ___ | μ β α ⊗ σ_^^ | ν α β) = (2 •ₜ η' | μ ν)}ᵀ
```

**`PauliMatrix.pauliCo_trace_pauliCoDown`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Relations.lean#L95).

```lean
lemma pauliCo_trace_pauliCoDown: {σ_^^ | μ α β ⊗ σ___ | ν β α = 2 •ₜ η' | μ ν}ᵀ
```

**`PauliMatrix.pauliContr_mul_pauliContrDown_add`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Relations.lean#L110).

```lean
lemma pauliContr_mul_pauliContrDown_add :
    {((σ^^^ | μ α β ⊗ σ^__ | ν β α') + (σ^^^ | ν α β ⊗ σ^__ | μ β α')) =
    2 •ₜ η | μ ν ⊗ δL | α α'}ᵀ
```

**`PauliMatrix.auliContrDown_pauliContr_mul_add`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Relations.lean#L125).

```lean
lemma auliContrDown_pauliContr_mul_add :
    {((σ^__ | μ β α ⊗ σ^^^ | ν α β') + (σ^__ | ν β α ⊗ σ^^^ | μ α β')) =
    2 •ₜ η | μ ν ⊗ δR' | β β'}ᵀ
```

## Triple products

**`PauliMatrix.pauliContr_mul_dualWeyl_eq_ofGaussianInt`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Relations.lean#L148).

> Gaussian integer components of a contraction of `σ^^^` with a copy whose Weyl indices
> are dualized.

```lean
lemma pauliContr_mul_dualWeyl_eq_ofGaussianInt :
    {σ^^^ | μ α β ⊗ σ^^^ | ν τ(α') τ(β)}ᵀ = ofGaussianInt (fun b =>
      ∑ x : Fin 2, pauliContrComponent (b 0) (b 1) x *
        pauliContrDownComponent (b 2) x (b 3))
```

**`PauliMatrix.dualWeyl_mul_pauliContr_eq_ofGaussianInt`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Relations.lean#L158).

> Gaussian integer components of the reverse contraction of a Weyl-dualized `σ^^^` with
> `σ^^^`.

```lean
lemma dualWeyl_mul_pauliContr_eq_ofGaussianInt :
    {σ^^^ | μ τ(α) τ(β) ⊗ σ^^^ | ν α β'}ᵀ = ofGaussianInt (fun b =>
      ∑ x : Fin 2, pauliContrDownComponent (b 0) (b 1) x *
        pauliContrComponent (b 2) x (b 3))
```

**`PauliMatrix.leviCivita_mul_pauliDual`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Relations.lean#L168).

> Contracting `ε4ℂ` with a Lorentz-dualized `σ^^^` agrees with contracting it with
> `pauliCo`.

```lean
lemma leviCivita_mul_pauliDual :
    ({ε4ℂ | μ ν ρ κ ⊗ σ^^^ | τ(κ) α β =
      ε4ℂ | μ ν ρ κ ⊗ σ_^^ | κ α β}ᵀ : Prop)
```

**`PauliMatrix.pauliContr_mul_pauliContrDown_mul_pauliContr`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Relations.lean#L186).

> The three-Pauli identity
> `σ^μ barσ^ν σ^ρ = g^{μν} σ^ρ - g^{μρ} σ^ν + g^{νρ} σ^μ + i ε^{μνρκ} σ_κ`,
> with barred and lowered forms expressed through index dualization `τ`.

```lean
lemma pauliContr_mul_pauliContrDown_mul_pauliContr : ({
    σ^^^ | μ α β ⊗ σ^^^ | ν τ(α') τ(β) ⊗ σ^^^ | ρ α' β' =
      ((((η | μ ν ⊗ σ^^^ | ρ α β') + (-((η | μ ρ ⊗ σ^^^ | ν α β'))))
        + (η | ν ρ ⊗ σ^^^ | μ α β'))
        + (Complex.I •ₜ (ε4ℂ | μ ν ρ κ ⊗ σ^^^ | τ(κ) α β')))
    }ᵀ : Prop)
```

**`PauliMatrix.pauliContrDown_mul_pauliContr_mul_pauliContrDown`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Relations.lean#L217).

> The conjugate three-Pauli identity
> `barσ^μ σ^ν barσ^ρ = g^{μν} barσ^ρ - g^{μρ} barσ^ν + g^{νρ} barσ^μ - i ε^{μνρκ} barσ_κ`,
> with barred and lowered forms expressed through index dualization `τ`.

```lean
lemma pauliContrDown_mul_pauliContr_mul_pauliContrDown : ({
    σ^^^ | μ τ(α) τ(β) ⊗ σ^^^ | ν α β' ⊗ σ^^^ | ρ τ(α') τ(β') =
      ((((η | μ ν ⊗ σ^^^ | ρ τ(α') τ(β))
        + (-((η | μ ρ ⊗ σ^^^ | ν τ(α') τ(β)))))
        + (η | ν ρ ⊗ σ^^^ | μ τ(α') τ(β)))
        + ((-Complex.I) •ₜ (ε4ℂ | μ ν ρ κ ⊗ σ^^^ | τ(κ) τ(α') τ(β))))
    }ᵀ : Prop)
```

## Depends on

- [Pauli matrices as a tensor](pauli-totensor.md)
- [Physlib.Relativity.Tensors.ComplexTensor.Units.Basic](../tensors/part-01/complextensor-units-basic.md)
- [The Levi-Civita tensor as a complex Lorentz tensor](../tensors/part-03/levicivita-complex.md)

## Sources

- [Physlib/Relativity/Bispinors/Pauli/Relations.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Relations.lean)
