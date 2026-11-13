---
declaration: module
origin: cited
lean: Lorentz.CoVector.indexEquiv, Lorentz.CoVector.tensorial, Lorentz.CoVector.toTensor_symm_apply, Lorentz.CoVector.toTensor_symm_pure, Lorentz.CoVector.toTensor_symm_basis, Lorentz.CoVector.toTensor_basis_eq_tensor_basis, Lorentz.CoVector.basis_eq_map_tensor_basis, Lorentz.CoVector.tensor_basis_map_eq_basis_reindex
statement: formalized
proof: formalized
---

# Tensorial nature of Lorentz covectors

The module `Physlib.Relativity.Tensors.RealTensor.CoVector.Tensorial`, [Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean): 18 declarations, 2 with a docstring.

> We define the tensorial instance on `Lorentz.coVector`, and show
> prove properties related to the Lorentz group action and the basis.

## Tensorial

**`Lorentz.CoVector.indexEquiv`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean#L45).

> The equivalence between the type of indices of a Lorentz vector and
> `Fin 1 ⊕ Fin d`.

```lean
def indexEquiv {d : ℕ} :
    ComponentIdx (S := (realLorentzTensor d)) ![Color.down] ≃ Fin 1 ⊕ Fin d
```

**`Lorentz.CoVector.tensorial`**, an instance, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean#L49).

```lean
instance tensorial {d : ℕ} : Tensorial (realLorentzTensor d) ![.down] (CoVector d)
```

**`Lorentz.CoVector.toTensor_symm_apply`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean#L64).

```lean
lemma toTensor_symm_apply {d : ℕ} (p : ℝT[d, .down]) :
    (toTensor (self := tensorial)).symm p =
    (Equiv.piCongrLeft' _ indexEquiv <|
    Finsupp.equivFunOnFinite <|
    (Tensor.basis (S := (realLorentzTensor d)) _).repr p)
```

**`Lorentz.CoVector.toTensor_symm_pure`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean#L70).

```lean
lemma toTensor_symm_pure {d : ℕ} (p : Pure (realLorentzTensor d) ![.down]) (i : Fin 1 ⊕ Fin d) :
    (toTensor (self := tensorial)).symm p.toTensor i =
    ((Lorentz.coBasis d).repr (p 0)) (indexEquiv.symm i 0)
```

## Basis

**`Lorentz.CoVector.toTensor_symm_basis`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean#L86).

```lean
lemma toTensor_symm_basis {d : ℕ} (μ : Fin 1 ⊕ Fin d) :
    (toTensor (self := tensorial)).symm (Tensor.basis ![Color.down] (indexEquiv.symm μ)) =
    basis μ
```

**`Lorentz.CoVector.toTensor_basis_eq_tensor_basis`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean#L93).

```lean
lemma toTensor_basis_eq_tensor_basis {d : ℕ} (μ : Fin 1 ⊕ Fin d) :
    toTensor (basis μ) = Tensor.basis ![Color.down] (indexEquiv.symm μ)
```

**`Lorentz.CoVector.basis_eq_map_tensor_basis`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean#L98).

```lean
lemma basis_eq_map_tensor_basis {d} : basis =
    ((Tensor.basis (S := realLorentzTensor d) ![Color.down]).map
    toTensor.symm).reindex indexEquiv
```

**`Lorentz.CoVector.tensor_basis_map_eq_basis_reindex`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean#L105).

```lean
lemma tensor_basis_map_eq_basis_reindex {d} :
    (Tensor.basis (S := realLorentzTensor d) ![Color.down]).map toTensor.symm =
    basis.reindex indexEquiv.symm
```

**`Lorentz.CoVector.tensor_basis_repr_toTensor_apply`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean#L112).

```lean
lemma tensor_basis_repr_toTensor_apply {d : ℕ} (p : CoVector d) (μ : ComponentIdx ![Color.down]) :
    (Tensor.basis ![Color.down]).repr (toTensor p) μ =
    p (indexEquiv μ)
```

## The action of the Lorentz group

**`Lorentz.CoVector.smul_eq_sum`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean#L135).

```lean
lemma smul_eq_sum {d : ℕ} (i : Fin 1 ⊕ Fin d) (Λ : LorentzGroup d) (p : CoVector d) :
    (Λ • p) i = ∑ j, Λ⁻¹.1 j i * p j
```

**`Lorentz.CoVector.smul_eq_mulVec`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean#L156).

```lean
lemma smul_eq_mulVec {d} (Λ : LorentzGroup d) (p : CoVector d) :
    Λ • p = (LorentzGroup.transpose Λ⁻¹).1 *ᵥ p
```

**`Lorentz.CoVector.smul_add`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean#L164).

```lean
lemma smul_add {d : ℕ} (Λ : LorentzGroup d) (p q : CoVector d) :
    Λ • (p + q) = Λ • p + Λ • q
```

**`Lorentz.CoVector.smul_sub`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean#L168).

```lean
lemma smul_sub {d : ℕ} (Λ : LorentzGroup d) (p q : CoVector d) :
    Λ • (p - q) = Λ • p - Λ • q
```

**`Lorentz.CoVector.smul_zero`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean#L172).

```lean
lemma smul_zero {d : ℕ} (Λ : LorentzGroup d) :
    Λ • (0 : CoVector d) = 0
```

**`Lorentz.CoVector.smul_neg`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean#L176).

```lean
lemma smul_neg {d : ℕ} (Λ : LorentzGroup d) (p : CoVector d) :
    Λ • (-p) = - (Λ • p)
```

**`Lorentz.CoVector.actionCLM`**, a def, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean#L181).

> The Lorentz action on vectors as a continuous linear map.

```lean
def actionCLM {d : ℕ} (Λ : LorentzGroup d) :
    CoVector d →L[ℝ] CoVector d
```

**`Lorentz.CoVector.actionCLM_apply`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean#L190).

```lean
lemma actionCLM_apply {d : ℕ} (Λ : LorentzGroup d) (p : CoVector d) :
    actionCLM Λ p = Λ • p
```

**`Lorentz.CoVector.smul_basis`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean#L193).

```lean
lemma smul_basis {d : ℕ} (Λ : LorentzGroup d) (μ : Fin 1 ⊕ Fin d) :
    Λ • basis μ = ∑ ν, Λ⁻¹.1 μ ν • basis ν
```

## Depends on

- [Physlib.Relativity.Tensors.RealTensor.Basic](realtensor-basic.md)
- [Lorentz co vectors](realtensor-covector-basic.md)
- [Tensorial class](../part-01/tensorial.md)

## Sources

- [Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Tensorial.lean)
