---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.Pure.prodP, TensorSpecies.Tensor.Pure.prodP_apply_castAdd, TensorSpecies.Tensor.Pure.prodP_apply_natAdd, TensorSpecies.Tensor.Pure.prodP_apply_finSumFinEquiv, TensorSpecies.Tensor.Pure.prodP_basisVector, TensorSpecies.Tensor.Pure.prodP_component, TensorSpecies.Tensor.Pure.prodP_equivariant, TensorSpecies.Tensor.Pure.prodP_zero_right
statement: formalized
proof: formalized
---

# The product of tensors

The module `Physlib.Relativity.Tensors.Product`, [Physlib/Relativity/Tensors/Product.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean): 31 declarations, 4 with a docstring.

## i. Overview

> In this module we define the tensor product of
> - index components of tensors,
> - pure tensors, and
> - tensors.
> We prove a number of properties about these products, for example,
> permutation of the factors, equivariance, and associativity.

## ii. Key results

> - `Pure.prodP` : The tensor product of two pure tensors.
> - `prodT` : The tensor product of two tensors.
>
> The following results exist for both `prodP` and `prodT` :
> - `prodT_swap` : Swapping the order of the product of two tensors.
> - `prodT_permT_left` : Permuting the indices of the left tensor commute with the product.
> - `prodT_permT_right` : Permuting the indices of the right tensor commute with the product.
> - `prodT_equivariant` : The product of two tensors is equivariant.
> - `prodT_assoc` : The product of three tensors is associative.
> - `prodT_assoc'` : The product of three tensors is associative in the other direction.

## iv. References

> * Tooby-Smith, Formalization of physics index notation in Lean 4, arXiv:2411.07667.
>   [ref: tooby\_smith\_2024\_index\_notation]

## B. Products of pure tensors

### B.1. Indexing pure tensors by `Fin n1 ⊕ Fin n2` rather than `Fin (n1 + n2)`

### B.2. The product of two pure tensors

**`TensorSpecies.Tensor.Pure.prodP`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L109).

> Given two pure tensors `p1 : Pure S c` and `p2 : Pure S c`, `prodP p p2` is the tensor
> product of those tensors returning an element in
> `Pure S (Sum.elim c c1 ∘ ⇑finSumFinEquiv.symm)`.

```lean
def Pure.prodP {n1 n2} {c : Fin n1 → C} {c1 : Fin n2 → C}
    (p1 : Pure S c) (p2 : Pure S c1) : Pure S (Fin.append c c1)
```

### B.3. The vectors making up product of two pure tensors

**`TensorSpecies.Tensor.Pure.prodP_apply_castAdd`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L121).

```lean
lemma Pure.prodP_apply_castAdd {n1 n2} {c : Fin n1 → C} {c1 : Fin n2 → C}
    (p1 : Pure S c) (p2 : Pure S c1) (i : Fin n1) :
    Pure.prodP p1 p2 (Fin.castAdd n2 i) =
    LinearEquiv.cast (R := k) (by simp) (p1 i)
```

**`TensorSpecies.Tensor.Pure.prodP_apply_natAdd`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L128).

```lean
lemma Pure.prodP_apply_natAdd {n1 n2} {c : Fin n1 → C} {c1 : Fin n2 → C}
    (p1 : Pure S c) (p2 : Pure S c1) (i : Fin n2) :
    Pure.prodP p1 p2 (Fin.natAdd n1 i) =
    LinearEquiv.cast (R := k) (by simp) (p2 i)
```

**`TensorSpecies.Tensor.Pure.prodP_apply_finSumFinEquiv`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L134).

```lean
lemma Pure.prodP_apply_finSumFinEquiv {n1 n2} {c : Fin n1 → C} {c1 : Fin n2 → C}
    (p1 : Pure S c) (p2 : Pure S c1) (i : Fin n1 ⊕ Fin n2) :
    Pure.prodP p1 p2 (finSumFinEquiv i) =
    match i with
    | Sum.inl i => LinearEquiv.cast (R := k) (by simp) (p1 i)
    | Sum.inr i => LinearEquiv.cast (R := k) (by simp) (p2 i)
```

### B.4. The product of two pure basis vectors

**`TensorSpecies.Tensor.Pure.prodP_basisVector`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L155).

```lean
lemma Pure.prodP_basisVector {n n1 : ℕ} {c : Fin n → C} {c1 : Fin n1 → C}
    (φ : ComponentIdx c) (φ1 : ComponentIdx (S := S) c1) :
    Pure.prodP (Pure.basisVector c φ) (Pure.basisVector c1 φ1) =
    Pure.basisVector _ (ComponentIdx.prod.symm (φ, φ1))
```

### B.5. The basis components of the product of two pure tensors

**`TensorSpecies.Tensor.Pure.prodP_component`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L182).

```lean
lemma Pure.prodP_component {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    (p : Pure S c) (p1 : Pure S c1)
    (φ : ComponentIdx (Fin.append c c1)) :
    (p.prodP p1).component φ = p.component (ComponentIdx.prod φ).1 *
    p1.component (ComponentIdx.prod φ).2
```

### B.6. Equivariance of the product of two pure tensors

**`TensorSpecies.Tensor.Pure.prodP_equivariant`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L214).

```lean
lemma Pure.prodP_equivariant {n1 n2} {c : Fin n1 → C} {c1 : Fin n2 → C}
    (g : G) (p : Pure S c) (p1 : Pure S c1) :
    prodP (g • p) (g • p1) = g • prodP p p1
```

### B.7. Product with a tensor with no indices on the right

**`TensorSpecies.Tensor.Pure.prodP_zero_right`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L242).

```lean
lemma Pure.prodP_zero_right {n} {c : Fin n → C}
    {c1 : Fin 0 → C} (p : Pure S c) (p0 : Pure S c1) :
    prodP p p0 = permP id IsReindexing.append_zero_right p
```

### B.8. Swapping the order of the product of two pure tensors

**`TensorSpecies.Tensor.Pure.prodP_swap`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L258).

```lean
lemma Pure.prodP_swap {n n1} {c : Fin n → C} {c1 : Fin n1 → C} (p : Pure S c) (p1 : Pure S c1) :
    Pure.prodP p p1 = permP _ IsReindexing.append_swap (Pure.prodP p1 p)
```

### B.9. Permuting the indices of the left tensor in a product

**`TensorSpecies.Tensor.Pure.prodP_permP_left`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L274).

```lean
lemma Pure.prodP_permP_left {n n'} {c : Fin n → C} {c' : Fin n' → C}
    (σ : Fin n' → Fin n) (h : IsReindexing c c' σ) (p : Pure S c) (p2 : Pure S c2) :
    Pure.prodP (permP σ h p) p2 = permP _ (h.append_congr_left c2) (Pure.prodP p p2)
```

### B.10. Permuting the indices of the right tensor in a product

**`TensorSpecies.Tensor.Pure.prodP_permP_right`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L292).

```lean
lemma Pure.prodP_permP_right {n n'} {c : Fin n → C} {c' : Fin n' → C}
    (σ : Fin n' → Fin n) (h : IsReindexing c c' σ) (p : Pure S c) (p2 : Pure S c2) :
    prodP p2 (permP σ h p) = permP _ (h.append_congr_right c2) (Pure.prodP p2 p)
```

### B.11. Associativity of the product of three pure tensors in one direction

**`TensorSpecies.Tensor.Pure.prodP_assoc`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L308).

```lean
lemma Pure.prodP_assoc {n n1 n2} {c : Fin n → C}
    {c1 : Fin n1 → C} {c2 : Fin n2 → C}
    (p : Pure S c) (p1 : Pure S c1) (p2 : Pure S c2) :
    prodP (prodP p p1) p2 =
    permP _ IsReindexing.append_assoc_right (prodP p (prodP p1 p2))
```

### B.12. Associativity of the product of three pure tensors in the other direction

**`TensorSpecies.Tensor.Pure.prodP_assoc'`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L328).

```lean
lemma Pure.prodP_assoc' {n n1 n2} {c : Fin n → C}
    {c1 : Fin n1 → C} {c2 : Fin n2 → C}
    (p : Pure S c) (p1 : Pure S c1) (p2 : Pure S c2) :
    prodP p (prodP p1 p2) = permP _ IsReindexing.append_assoc_left (prodP (prodP p p1) p2)
```

### B.13. Linearity of the product

**`TensorSpecies.Tensor.Pure.prodP_update_left`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L350).

```lean
lemma Pure.prodP_update_left {n1 n2} {c : Fin n1 → C} {c1 : Fin n2 → C}
    (p1 : Pure S c) (p2 : Pure S c1) (i : Fin n1) (x : V (c i)) :
    Pure.prodP (Pure.update p1 i x) p2
    = Pure.update (Pure.prodP p1 p2) (Fin.castAdd n2 i)
      (LinearEquiv.cast (R := k) (by simp) x)
```

**`TensorSpecies.Tensor.Pure.prodP_update_right`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L375).

```lean
lemma Pure.prodP_update_right {n1 n2} {c : Fin n1 → C} {c1 : Fin n2 → C}
    (p1 : Pure S c) (p2 : Pure S c1) (i : Fin n2) (x : V (c1 i)) :
    Pure.prodP p1 (Pure.update p2 i x)
    = Pure.update (Pure.prodP p1 p2) (Fin.natAdd n1 i)
      (LinearEquiv.cast (R := k) (by simp) x)
```

**`TensorSpecies.Tensor.Pure.prodP_update_add_toTensor_left`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L399).

```lean
lemma Pure.prodP_update_add_toTensor_left {n1 n2} {c : Fin n1 → C} {c1 : Fin n2 → C}
    (p1 : Pure S c) (p2 : Pure S c1) (i : Fin n2) (x y : V (c1 i)) :
    (Pure.prodP p1 (Pure.update p2 i (x + y))).toTensor
    = (Pure.prodP p1 (Pure.update p2 i x)).toTensor
    + (Pure.prodP p1 (Pure.update p2 i y)).toTensor
```

## C. Products of tensors

### C.2. The product of two tensors

**`TensorSpecies.Tensor.prodT`**, a def, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L418).

> The tensor product of two tensors as a bi-linear map from
> `S.Tensor c` and `S.Tensor c1` to `S.Tensor (Fin.append c c1)`.

```lean
noncomputable def prodT {n1 n2} {c : Fin n1 → C} {c1 : Fin n2 → C} :
    S.Tensor c →ₗ[k] S.Tensor c1 →ₗ[k] S.Tensor (Fin.append c c1)
```

### C.3. The product of two pure tensors as a tensor

**`TensorSpecies.Tensor.prodT_pure`**, a lemma, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L443).

```lean
lemma prodT_pure {n1 n2} {c : Fin n1 → C} {c1 : Fin n2 → C}
    (t : Pure S c) (t1 : Pure S c1) :
    (t.toTensor).prodT (t1.toTensor) = (Pure.prodP t t1).toTensor
```

### C.4. The product of basis vectors

**`TensorSpecies.Tensor.prodT_basis`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L456).

```lean
lemma prodT_basis {n1 n2} {c : Fin n1 → C} {c1 : Fin n2 → C}
    (b : ComponentIdx c) (b1 : ComponentIdx (S := S) c1) :
    (basis c b).prodT (basis c1 b1) =
    (Pure.basisVector _ (ComponentIdx.prod.symm (b, b1))).toTensor
```

**`TensorSpecies.Tensor.prodT_basis'`**, a lemma, [line 462](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L462).

```lean
lemma prodT_basis' {n1 n2} {c : Fin n1 → C} {c1 : Fin n2 → C}
    (b : ComponentIdx c) (b1 : ComponentIdx (S := S) c1) :
    (basis c b).prodT (basis c1 b1) =
    basis (Fin.append c c1) (ComponentIdx.prod.symm (b, b1))
```

### C.5. The product as an equivalence

**`TensorSpecies.Tensor.tensorEquivProd`**, a def, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L477).

> The linear equivalence between `S.Tensor c ⊗[k] S.Tensor c1` and
> `S.Tensor (Fin.append c c1)`.

```lean
noncomputable def tensorEquivProd {n n2 : ℕ} {c : Fin n → C} {c1 : Fin n2 → C} :
    S.Tensor c ⊗[k] S.Tensor c1 ≃ₗ[k] S.Tensor (Fin.append c c1)
```

### C.6. Rewriting the basis for the product in terms of the tensor product basis

**`TensorSpecies.Tensor.basis_prod_eq`**, a lemma, [line 534](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L534).

> Rewriting basis for the product in terms of the tensor product basis.

```lean
lemma basis_prod_eq {n1 n2} {c : Fin n1 → C} {c1 : Fin n2 → C} :
    basis (S := S) (Fin.append c c1) =
    (((Tensor.basis (S := S) c).tensorProduct (Tensor.basis (S := S) c1)).reindex
    (ComponentIdx.prod.symm)).map tensorEquivProd
```

**`TensorSpecies.Tensor.prodT_basis_repr_apply`**, a lemma, [line 547](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L547).

```lean
lemma prodT_basis_repr_apply {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    (t : Tensor S c) (t1 : Tensor S c1)
    (b : ComponentIdx (Fin.append c c1)) :
    (basis (Fin.append c c1)).repr (prodT t t1) b =
    (basis c).repr t (ComponentIdx.prod b).1 *
    (basis c1).repr t1 (ComponentIdx.prod b).2
```

### C.7. Equivariance of the product of two tensors

**`TensorSpecies.Tensor.prodT_equivariant`**, a lemma, [line 578](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L578).

```lean
lemma prodT_equivariant {n1 n2} {c : Fin n1 → C} {c1 : Fin n2 → C}
    (g : G) (t : S.Tensor c) (t1 : S.Tensor c1) :
    prodT (g • t) (g • t1) = g • prodT t t1
```

### C.8. The product with the default tensor with no indices on the right

**`TensorSpecies.Tensor.prodT_default_right`**, a lemma, [line 595](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L595).

```lean
lemma prodT_default_right {n} {c : Fin n → C}
    {c1 : Fin 0 → C} (t : S.Tensor c) :
    prodT t (Pure.toTensor default : S.Tensor c1) =
    permT id (IsReindexing.append_zero_right) t
```

**`TensorSpecies.Tensor.prodT_zero_right`**, a lemma, [line 606](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L606).

```lean
lemma prodT_zero_right {n} {c : Fin n → C}
    {c1 : Fin 0 → C} (t : S.Tensor c) (t1 : S.Tensor c1) :
    prodT t t1 = (toScalar t1) • permT id (IsReindexing.append_zero_right) t
```

### C.9. Swapping the order of the product of two tensors

**`TensorSpecies.Tensor.prodT_swap`**, a lemma, [line 623](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L623).

```lean
lemma prodT_swap {n n1} {c : Fin n → C} {c1 : Fin n1 → C} (t : S.Tensor c) (t1 : S.Tensor c1) :
    prodT t t1 = permT _ IsReindexing.append_swap (prodT t1 t)
```

### C.10. Permuting the indices of the left tensor in a product

**`TensorSpecies.Tensor.prodT_permT_left`**, a lemma, [line 640](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L640).

```lean
lemma prodT_permT_left {n n'} {c : Fin n → C} {c' : Fin n' → C}
    (σ : Fin n' → Fin n) (h : IsReindexing c c' σ) (t : S.Tensor c) (t2 : S.Tensor c2) :
    prodT (permT σ h t) t2 = permT _ (h.append_congr_left c2) (prodT t t2)
```

### C.11. Permuting the indices of the right tensor in a product

**`TensorSpecies.Tensor.prodT_permT_right`**, a lemma, [line 658](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L658).

```lean
lemma prodT_permT_right {n n'} {c : Fin n → C} {c' : Fin n' → C}
    (σ : Fin n' → Fin n) (h : IsReindexing c c' σ) (t : S.Tensor c) (t2 : S.Tensor c2) :
    prodT t2 (permT σ h t) = permT _ (h.append_congr_right c2) (prodT t2 t)
```

### C.12. Associativity of the product of three tensors in one direction

**`TensorSpecies.Tensor.prodT_assoc`**, a lemma, [line 675](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L675).

```lean
lemma prodT_assoc {n n1 n2} {c : Fin n → C}
    {c1 : Fin n1 → C} {c2 : Fin n2 → C} (t : S.Tensor c) (t1 : S.Tensor c1) (t2 : S.Tensor c2) :
    prodT (prodT t t1) t2 = permT _ IsReindexing.append_assoc_right (prodT t (prodT t1 t2))
```

### C.13. Associativity of the product of three tensors in the other direction

**`TensorSpecies.Tensor.prodT_assoc'`**, a lemma, [line 695](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean#L695).

```lean
lemma prodT_assoc' {n n1 n2} {c : Fin n → C}
    {c1 : Fin n1 → C} {c2 : Fin n2 → C} (t : S.Tensor c) (t1 : S.Tensor c1) (t2 : S.Tensor c2) :
    prodT t (prodT t1 t2) = permT _ IsReindexing.append_assoc_left (prodT (prodT t t1) t2)
```

## Depends on

- [Tensors](basic.md)
- [Products of component indices](../part-02/componentidx-product.md)

## Sources

- [Physlib/Relativity/Tensors/Product.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Product.lean)
