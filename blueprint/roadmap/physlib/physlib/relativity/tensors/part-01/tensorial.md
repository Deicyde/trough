---
declaration: module
origin: cited
lean: TensorSpecies.Tensorial, TensorSpecies.Tensorial.self, TensorSpecies.Tensorial.self_toTensor_apply, TensorSpecies.Tensorial.numIndices, TensorSpecies.Tensorial.smulAction, TensorSpecies.Tensorial.mulAction, TensorSpecies.Tensorial.smul_eq, TensorSpecies.Tensorial.toTensor_smul
statement: formalized
proof: formalized
---

# Tensorial class

The module `Physlib.Relativity.Tensors.Tensorial`, [Physlib/Relativity/Tensors/Tensorial.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean): 26 declarations (3 instances with no name), 6 with a docstring.

## i. Overview

> We define a class called `Tensorial`.
> This class is used to enable the use of index notation on a type `M` via a linear equivalence to a
> tensor of a `TensorSpecies`.
>
> We define the class `Tensorial` here, and provide an API around its use.

## ii. Key results

> - `Tensorial` : The class used to allow index notation on a type `M`.
> - `Tensorial.numIndices` : The number of indices of an element of an `M`
>   carrying a tensorial instance.
> - `Tensorial.mulAction` : The action of the group `G` on a
>   type `M` carrying a tensorial instance.
> - `Tensorial.prod` : The product of two tensorial instances is a tensorial instance.

## iv. References

> * None.

## A. Defining the tensorial class

> We first define the `Tensorial` class.

**`TensorSpecies.Tensorial`**, a class, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L77).

> The tensorial class is used to define a tensor structure on a type `M` through a
> linear equivalence with a module `S.Tensor c` for `S` a tensor species.

```lean
class Tensorial {n : outParam ℕ}

    {k : outParam Type} [CommRing k] {C : outParam Type} {G : outParam Type} [Group G]
    {V :outParam (C → Type)} [∀ c, AddCommGroup (V c)] [∀ c, Module k (V c)]
    {basisIdx : outParam (C → Type)} [∀ c, Fintype (basisIdx c)] [∀ c, DecidableEq (basisIdx c)]
    {rep : outParam ((c : C) → Representation k G (V c))}
    {b : outParam ((c : C) → Module.Basis (basisIdx c) k (V c))}
    (S : outParam (TensorSpecies k C G V basisIdx rep b))
    (c :outParam (Fin n → C)) (M : Type)
    [AddCommMonoid M] [Module k M] where
  /-- The equivalence between `M` and `S.Tensor c` in a tensorial instance. -/
  toTensor : M ≃ₗ[k] S.Tensor c
```

### A.1. Tensors carry a tensorial instance

> The module of tensors of a tensor species carries a canonical tensorial instance,
> through the equivalence.

**`TensorSpecies.Tensorial.self`**, an instance, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L102).

```lean
noncomputable instance self {n : ℕ} (S : TensorSpecies k C G V basisIdx rep b) (c : Fin n → C) :
    Tensorial S c (S.Tensor c)
```

**`TensorSpecies.Tensorial.self_toTensor_apply`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L107).

```lean
lemma self_toTensor_apply {n : ℕ} (S : TensorSpecies k C G V basisIdx rep b)
    (c : Fin n → C) (t : S.Tensor c) :
    Tensorial.toTensor t = t
```

### A.2. The number of indices

**`TensorSpecies.Tensorial.numIndices`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L120).

> The number of indices of a elements `t : M` where `M` carries a tensorial instance.

```lean
noncomputable def numIndices (t : M) [Tensorial S c M] : ℕ
```

## B. The action of the group on a module with a tensorial instance

> We now define the action of the group `G` on a type `M` carrying a tensorial instance.

**`TensorSpecies.Tensorial.smulAction`**, an instance, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L131).

```lean
noncomputable instance (priority := high) smulAction [Tensorial S c M] : SMul G M
```

**`TensorSpecies.Tensorial.mulAction`**, an instance, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L134).

```lean
noncomputable instance mulAction [Tensorial S c M] : MulAction G M
```

### B.1. Relation between the action and the equivalence to tensors

**`TensorSpecies.Tensorial.smul_eq`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L150).

```lean
lemma smul_eq {g : G} {t : M} [Tensorial S c M] :
    g • t = toTensor.symm (g • toTensor t)
```

**`TensorSpecies.Tensorial.toTensor_smul`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L155).

```lean
lemma toTensor_smul {g : G} {t : M} [Tensorial S c M] :
    toTensor (g • t) = g • toTensor t
```

**`TensorSpecies.Tensorial.smul_toTensor_symm`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L160).

```lean
lemma smul_toTensor_symm {g : G} {t : Tensor S c} [self : Tensorial S c M] :
    g • (toTensor (self := self).symm t) = toTensor.symm (g • t)
```

### B.2. Linear properties of the action

**`TensorSpecies.Tensorial.distribMulAction`**, an instance, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L171).

```lean
noncomputable instance (priority := high) distribMulAction [Tensorial S c M] :
    DistribMulAction G M
```

### B.3. The action as a linear map

**`TensorSpecies.Tensorial.smulLinearMap`**, a def, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L187).

> The action of the group on a `Tensorial` instance as a linear map.

```lean
noncomputable def smulLinearMap (g : G) [Tensorial S c M] : M →ₗ[k] M
```

**`TensorSpecies.Tensorial.smulLinearMap_apply`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L196).

```lean
lemma smulLinearMap_apply {g : G} [Tensorial S c M] (m : M) :
    smulLinearMap g m = g • m
```

### B.4. The SMulCommClass property

**An instance with no name**, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L205).

```lean
instance [Tensorial S c M] : SMulCommClass k G M
```

**An instance with no name**, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L210).

```lean
instance [Tensorial S c M] : SMulCommClass G k M
```

## C. Properties of the basis

> We now prove some properties of the basis induced on a `Tensorial` instance.

**`TensorSpecies.Tensorial.basis_toTensor_apply`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L220).

```lean
lemma basis_toTensor_apply [Tensorial S c M] (m : M) :
    (Tensor.basis c).repr (toTensor m) = ((Tensor.basis c).map toTensor.symm).repr m
```

## D. Products of tensorial instances

**`TensorSpecies.Tensorial.prod`**, an instance, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L231).

```lean
noncomputable instance (priority := high) prod [Tensorial S c M] {n2 : ℕ} {c2 : Fin n2 → C}
    {M₂ : Type} [AddCommMonoid M₂] [Module k M₂] [Tensorial S c2 M₂] :
    Tensorial S (Fin.append c c2) (M ⊗[k] M₂)
```

### D.1. The equivalence to tensors on products

**`TensorSpecies.Tensorial.toTensor_tprod`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L243).

```lean
lemma toTensor_tprod {n2 : ℕ} {c2 : Fin n2 → C} {M₂ : Type}
    [Tensorial S c M] [AddCommMonoid M₂] [Module k M₂]
    [Tensorial S c2 M₂] (m : M) (m2 : M₂) :
    toTensor (m ⊗ₜ[k] m2) = Tensor.prodT (toTensor m) (toTensor m2)
```

### D.2. The group action on products

**`TensorSpecies.Tensorial.smul_prod`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L254).

```lean
lemma smul_prod {n2 : ℕ} {c2 : Fin n2 → C} {M₂ : Type}
    [Tensorial S c M] [AddCommMonoid M₂] [Module k M₂]
    [Tensorial S c2 M₂] (g : G) (m : M) (m2 : M₂) :
    g • (m ⊗ₜ[k] m2) = (g • m) ⊗ₜ[k] (g • m2)
```

### D.3. The basis on products

**`TensorSpecies.Tensorial.basis_map_prod`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L270).

```lean
lemma basis_map_prod {n2 : ℕ} {c2 : Fin n2 → C} {M₂ : Type}
    [Tensorial S c M] [AddCommMonoid M₂] [Module k M₂]
    [Tensorial S c2 M₂] :
    (Tensor.basis (S := S) (Fin.append c c2)).map
      (toTensor (M := (M ⊗[k] M₂))).symm =
    (((Tensor.basis (S := S) c).map (toTensor (M := M)).symm).tensorProduct
    ((Tensor.basis (S := S) c2).map (toTensor (M := M₂)).symm)).reindex
    (ComponentIdx.prod.symm)
```

**`TensorSpecies.Tensorial.prod_basis_of_map_reindex`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L289).

```lean
lemma prod_basis_of_map_reindex {n2 : ℕ} {c2 : Fin n2 → C} {M₂ : Type}
    [Tensorial S c M] [AddCommMonoid M₂] [Module k M₂]
    [Tensorial S c2 M₂] {ι ι2 : Type} {b : Module.Basis ι k M} {b2 : Module.Basis ι2 k M₂}
    {e : Tensor.ComponentIdx c ≃ ι} {e2 : Tensor.ComponentIdx c2 ≃ ι2}
    (h : b = ((Tensor.basis (S := S) c).map toTensor.symm).reindex e)
    (h2 : b2 = ((Tensor.basis (S := S) c2).map toTensor.symm).reindex e2) :
    b.tensorProduct b2 = ((Tensor.basis (S := S) (Fin.append c c2)).map
    (toTensor (S := S) (M := M ⊗[k] M₂)).symm).reindex
    (ComponentIdx.prod.trans (e.prodCongr e2))
```

**`TensorSpecies.Tensorial.prod_tensor_basis_eq_map_reindex`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L303).

```lean
lemma prod_tensor_basis_eq_map_reindex {n2 : ℕ} {c2 : Fin n2 → C} {M₂ : Type}
    [Tensorial S c M] [AddCommMonoid M₂] [Module k M₂]
    [Tensorial S c2 M₂] {ι ι2 : Type} {b : Module.Basis ι k M} {b2 : Module.Basis ι2 k M₂}
    {e : Tensor.ComponentIdx c ≃ ι} {e2 : Tensor.ComponentIdx c2 ≃ ι2}
    (h : b = ((Tensor.basis (S := S) c).map toTensor.symm).reindex e)
    (h2 : b2 = ((Tensor.basis (S := S) c2).map toTensor.symm).reindex e2) :
    Tensor.basis (S := S) (Fin.append c c2) =
    ((b.tensorProduct b2).map (toTensor (S := S) (M := M ⊗[k] M₂))).reindex
    (ComponentIdx.prod.trans (e.prodCongr e2)).symm
```

**`TensorSpecies.Tensorial.prod_eq_sum_eval`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L326).

> Double basis expansion of an element of a tensor product `M ⊗[k] M₂` of two `Tensorial`
> one-index spaces. Given bases `b`, `b2` of `M`, `M₂` coming from the single-index tensor bases,
> every `x : M ⊗[k] M₂` is the double sum over `i, j` of the iterated evaluation coefficient
> `toScalar (evalT 0 j (evalT 0 i (toTensor x)))` times `b i ⊗ₜ b2 j`.

```lean
lemma prod_eq_sum_eval {c c2 : C} {M₂ : Type}
    [Tensorial S ![c] M] [AddCommMonoid M₂] [Module k M₂]
    [Tensorial S ![c2] M₂] {b : Module.Basis (basisIdx c) k M}
    {b2 : Module.Basis (basisIdx c2) k M₂}
    (h : b = ((Tensor.basis (S := S) ![c]).map toTensor.symm).reindex ComponentIdx.single)
    (h2 : b2 = ((Tensor.basis (S := S) ![c2]).map toTensor.symm).reindex ComponentIdx.single)
    (x : M ⊗[k] M₂) : x = ∑ i : (basisIdx c), ∑ j : (basisIdx c2),
    toScalar (evalT 0 (basisIdxCongr (by rfl) j)
      (evalT 0 (basisIdxCongr (by rfl) i) (toTensor x))) • b i ⊗ₜ[k] b2 j
```

## E. Continuous properties

### E.1. Finite dimensionality

**An instance with no name**, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L372).

```lean
instance [Tensorial S c M] : FiniteDimensional k M
```

### E.2. The map to tensors as a continuous linear equivalence

**`TensorSpecies.Tensorial.toTensorCLM`**, a def, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L383).

> The map from a type carrying an Tensorial instance to tensors, as a
> continuous linear map.

```lean
def toTensorCLM [IsTopologicalAddGroup M]
    [ContinuousSMul k M] [Tensorial S c M] [T2Space M] : M ≃L[k] (S.Tensor c)
```

### E.3. The Lorentz action as a continuous linear equivalence

**`TensorSpecies.Tensorial.actionCLM`**, a def, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L404).

> The Lorentz action on types carrying a tensorial instance as a continuous linear
> map.

```lean
noncomputable def actionCLM (g : G) [IsTopologicalAddGroup M]
    [ContinuousSMul k M] [Tensorial S c M] [T2Space M] : M →L[k] M
```

**`TensorSpecies.Tensorial.actionCLM_apply`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean#L408).

```lean
lemma actionCLM_apply {g : G} [IsTopologicalAddGroup M]
    [ContinuousSMul k M] [Tensorial S c M] [T2Space M] (m : M) :
    actionCLM S g m = g • m
```

## Depends on

- [Evaluation of tensor indices](evaluation.md)

## Sources

- [Physlib/Relativity/Tensors/Tensorial.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Tensorial.lean)
