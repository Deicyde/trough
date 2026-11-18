---
declaration: module
origin: cited
lean: Lorentz.Vector.indexEquiv, Lorentz.Vector.tensorial, Lorentz.Vector.toTensor_symm_apply, Lorentz.Vector.toTensor_symm_pure, Lorentz.Vector.toTensor_symm_basis, Lorentz.Vector.toTensor_basis_eq_tensor_basis, Lorentz.Vector.basis_eq_map_tensor_basis, Lorentz.Vector.tensor_basis_map_eq_basis_reindex
statement: formalized
proof: formalized
---

# Tensorial nature of Lorentz vectors

The module `Physlib.Relativity.Tensors.RealTensor.Vector.Tensorial`, [Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean): 24 declarations, 4 with a docstring.

> We define the tensorial instance on `Lorentz.Vector`, and show
> prove properties related to the Lorentz group action and the basis.

## Tensorial

**`Lorentz.Vector.indexEquiv`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L46).

> The equivalence between the type of indices of a Lorentz vector and
> `Fin 1 ⊕ Fin d`.

```lean
def indexEquiv {d : ℕ} :
    ComponentIdx (S := (realLorentzTensor d)) ![Color.up] ≃ Fin 1 ⊕ Fin d
```

**`Lorentz.Vector.tensorial`**, an instance, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L50).

```lean
instance tensorial {d : ℕ} : Tensorial (realLorentzTensor d) ![.up] (Vector d)
```

**`Lorentz.Vector.toTensor_symm_apply`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L65).

```lean
lemma toTensor_symm_apply {d : ℕ} (p : ℝT[d, .up]) :
    (toTensor (self := tensorial)).symm p =
    (Equiv.piCongrLeft' _ indexEquiv <|
    Finsupp.equivFunOnFinite <|
    (Tensor.basis (S := (realLorentzTensor d)) _).repr p)
```

**`Lorentz.Vector.toTensor_symm_pure`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L71).

```lean
lemma toTensor_symm_pure {d : ℕ} (p : Pure (realLorentzTensor d) ![.up]) (i : Fin 1 ⊕ Fin d) :
    (toTensor (self := tensorial)).symm p.toTensor i =
    ((Lorentz.contrBasis d).repr (p 0)) (indexEquiv.symm i 0)
```

## Basis

**`Lorentz.Vector.toTensor_symm_basis`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L86).

```lean
lemma toTensor_symm_basis {d : ℕ} (μ : Fin 1 ⊕ Fin d) :
    (toTensor (self := tensorial)).symm (Tensor.basis ![Color.up] (indexEquiv.symm μ)) =
    basis μ
```

**`Lorentz.Vector.toTensor_basis_eq_tensor_basis`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L93).

```lean
lemma toTensor_basis_eq_tensor_basis {d : ℕ} (μ : Fin 1 ⊕ Fin d) :
    toTensor (basis μ) = Tensor.basis ![Color.up] (indexEquiv.symm μ)
```

**`Lorentz.Vector.basis_eq_map_tensor_basis`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L98).

```lean
lemma basis_eq_map_tensor_basis {d} : basis =
    ((Tensor.basis
    (S := realLorentzTensor d) ![Color.up]).map toTensor.symm).reindex indexEquiv
```

**`Lorentz.Vector.tensor_basis_map_eq_basis_reindex`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L105).

```lean
lemma tensor_basis_map_eq_basis_reindex {d} :
    (Tensor.basis (S := realLorentzTensor d) ![Color.up]).map toTensor.symm =
    basis.reindex indexEquiv.symm
```

**`Lorentz.Vector.tensor_basis_repr_toTensor_apply`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L112).

```lean
lemma tensor_basis_repr_toTensor_apply {d : ℕ} (p : Vector d) (μ : ComponentIdx ![Color.up]) :
    (Tensor.basis ![Color.up]).repr (toTensor p) μ =
    p (indexEquiv μ)
```

## Tensor products of vectors

**`Lorentz.Vector.toScalar_eval_eval_eq_tensorProduct_repr`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L134).

> Evaluating both indices of an element of `Vector d ⊗ Vector d` gives its coefficient
> in the tensor-product basis.

```lean
lemma toScalar_eval_eval_eq_tensorProduct_repr {d} (F : Vector d ⊗[ℝ] Vector d)
    (μ ν : Fin 1 ⊕ Fin d) :
    toScalar {F | [μ] [ν]}ᵀ = (basis.tensorProduct basis).repr F (μ, ν)
```

**`Lorentz.Vector.tensor_basis_repr_toTensor_prod_apply`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L143).

> The coefficient of an element of `Vector d ⊗ Vector d` in the tensor basis is its
> coefficient in the tensor-product basis.

```lean
lemma tensor_basis_repr_toTensor_prod_apply {d} (F : Vector d ⊗[ℝ] Vector d)
    (b : ComponentIdx (S := realLorentzTensor d) (Fin.append ![Color.up] ![Color.up])) :
    (Tensor.basis _).repr (toTensor F) b = (basis.tensorProduct basis).repr F (b 0, b 1)
```

## The action of the Lorentz group

**`Lorentz.Vector.smul_eq_sum`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L165).

```lean
lemma smul_eq_sum {d : ℕ} (i : Fin 1 ⊕ Fin d) (Λ : LorentzGroup d) (p : Vector d) :
    (Λ • p) i = ∑ j, Λ.1 i j * p j
```

**`Lorentz.Vector.smul_eq_mulVec`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L186).

```lean
lemma smul_eq_mulVec {d} (Λ : LorentzGroup d) (p : Vector d) :
    Λ • p = Λ.1 *ᵥ p
```

**`Lorentz.Vector.smul_add`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L193).

```lean
lemma smul_add {d : ℕ} (Λ : LorentzGroup d) (p q : Vector d) :
    Λ • (p + q) = Λ • p + Λ • q
```

**`Lorentz.Vector.smul_sub`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L197).

```lean
lemma smul_sub {d : ℕ} (Λ : LorentzGroup d) (p q : Vector d) :
    Λ • (p - q) = Λ • p - Λ • q
```

**`Lorentz.Vector.smul_zero`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L201).

```lean
lemma smul_zero {d : ℕ} (Λ : LorentzGroup d) :
    Λ • (0 : Vector d) = 0
```

**`Lorentz.Vector.smul_neg`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L205).

```lean
lemma smul_neg {d : ℕ} (Λ : LorentzGroup d) (p : Vector d) :
    Λ • (-p) = - (Λ • p)
```

**`Lorentz.Vector.neg_smul`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L209).

```lean
lemma neg_smul {d} (Λ : LorentzGroup d) (p : Vector d) :
    (-Λ) • p = - (Λ • p)
```

**`LorentzGroup.eq_of_action_vector_eq`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L214).

```lean
lemma _root_.LorentzGroup.eq_of_action_vector_eq {d : ℕ}
    {Λ Λ' : LorentzGroup d} (h : ∀ p : Vector d, Λ • p = Λ' • p) :
    Λ = Λ'
```

## B. The continuous action of the Lorentz group

**`Lorentz.Vector.actionCLM`**, a def, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L227).

> The Lorentz action on vectors as a continuous linear map.

```lean
def actionCLM {d : ℕ} (Λ : LorentzGroup d) :
    Vector d →L[ℝ] Vector d
```

**`Lorentz.Vector.actionCLM_apply`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L237).

```lean
lemma actionCLM_apply {d : ℕ} (Λ : LorentzGroup d) (p : Vector d) :
    actionCLM Λ p = Λ • p
```

**`Lorentz.Vector.actionCLM_injective`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L240).

```lean
lemma actionCLM_injective {d : ℕ} (Λ : LorentzGroup d) :
    Function.Injective (actionCLM Λ)
```

**`Lorentz.Vector.actionCLM_surjective`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L245).

```lean
lemma actionCLM_surjective {d : ℕ} (Λ : LorentzGroup d) :
    Function.Surjective (actionCLM Λ)
```

**`Lorentz.Vector.smul_basis`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean#L251).

```lean
lemma smul_basis {d : ℕ} (Λ : LorentzGroup d) (μ : Fin 1 ⊕ Fin d) :
    Λ • basis μ = ∑ ν, Λ.1 ν μ • basis ν
```

## Depends on

- [Physlib.Relativity.Tensors.RealTensor.Basic](../part-03/realtensor-basic.md)
- [Lorentz Vectors](../part-03/realtensor-vector-basic.md)
- [Tensorial class](../part-01/tensorial.md)

## Sources

- [Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Tensorial.lean)
