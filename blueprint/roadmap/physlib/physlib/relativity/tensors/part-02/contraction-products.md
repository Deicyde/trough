---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.Pure.contrPCoeff_natAdd, TensorSpecies.Tensor.Pure.contrPCoeff_castAdd, TensorSpecies.Tensor.Pure.prodP_dropPair, TensorSpecies.Tensor.Pure.prodP_contrP_snd, TensorSpecies.Tensor.prodT_contrT_snd, TensorSpecies.Tensor.contrT_prodT_snd, TensorSpecies.Tensor.prodT_contrT_fst
statement: formalized
proof: formalized
---

# The interaction of contractions and products

The module `Physlib.Relativity.Tensors.Contraction.Products`, [Physlib/Relativity/Tensors/Contraction/Products.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Products.lean): 7 declarations, 1 with a docstring.

## Products and contractions

**`TensorSpecies.Tensor.Pure.contrPCoeff_natAdd`**, a lemma, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Products.lean#L35).

```lean
lemma Pure.contrPCoeff_natAdd {n n1 : ℕ} {c : Fin (n + 1 + 1) → C}
    {c1 : Fin n1 → C}
    (i j : Fin (n + 1 + 1)) (hij : i ≠ j ∧ S.τ (c i) = c j)
    (p : Pure S c) (p1 : Pure S c1) :
    contrPCoeff (Fin.natAdd n1 i) (Fin.natAdd n1 j)
    (by simp_all [Fin.ext_iff]) (p1.prodP p) = contrPCoeff i j hij p
```

**`TensorSpecies.Tensor.Pure.contrPCoeff_castAdd`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Products.lean#L51).

```lean
lemma Pure.contrPCoeff_castAdd {n n1 : ℕ} {c : Fin (n + 1 + 1) → C}
    {c1 : Fin n1 → C}
    (i j : Fin (n + 1 + 1)) (hij : i ≠ j ∧ S.τ (c i) = c j)
    (p : Pure S c) (p1 : Pure S c1) :
    contrPCoeff (Fin.castAdd n1 i) (Fin.castAdd n1 j)
    (by simp_all [Fin.ext_iff]) (p.prodP p1) = contrPCoeff i j hij p
```

**`TensorSpecies.Tensor.Pure.prodP_dropPair`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Products.lean#L68).

```lean
lemma Pure.prodP_dropPair {n n1 : ℕ} {c : Fin (n + 1 + 1) → C}
    {c1 : Fin n1 → C}
    (i j : Fin (n + 1 + 1)) (hij : i ≠ j ∧ S.τ (c i) = c j)
    (p : Pure S c) (p1 : Pure S c1) :
    p1.prodP (dropPair i j hij.1 p) = permP _ (IsReindexing.append_succSuccAbove_natAdd i j)
    (dropPair (Fin.natAdd n1 i) (Fin.natAdd n1 j)
    (by simp_all [Fin.ext_iff]) (p1.prodP p))
```

**`TensorSpecies.Tensor.Pure.prodP_contrP_snd`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Products.lean#L93).

```lean
lemma Pure.prodP_contrP_snd {n n1 : ℕ} {c : Fin (n + 1 + 1) → C}
    {c1 : Fin n1 → C}
    (i j : Fin (n + 1 + 1)) (hij : i ≠ j ∧ S.τ (c i) = c j)
    (p : Pure S c) (p1 : Pure S c1) :
    prodT p1.toTensor (contrP i j hij p) =
    ((permT id (IsReindexing.append_succSuccAbove_natAdd i j)) <|
    contrP (Fin.natAdd n1 i) (Fin.natAdd n1 j) (by simpa using hij) <|
    prodP p1 p)
```

**`TensorSpecies.Tensor.prodT_contrT_snd`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Products.lean#L111).

```lean
lemma prodT_contrT_snd {n n1 : ℕ} {c : Fin (n + 1 + 1) → C}
    {c1 : Fin n1 → C}
    (i j : Fin (n + 1 + 1)) (hij : i ≠ j ∧ S.τ (c i) = c j)
    (t : Tensor S c) (t1 : Tensor S c1) :
    prodT t1 (contrT n i j hij t) =
    ((permT id (IsReindexing.append_succSuccAbove_natAdd i j)) <|
    contrT _ (Fin.natAdd n1 i) (Fin.natAdd n1 j)
      (by simpa using hij) <| prodT t1 t)
```

**`TensorSpecies.Tensor.contrT_prodT_snd`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Products.lean#L147).

```lean
lemma contrT_prodT_snd {n n1 : ℕ} {c : Fin (n + 1 + 1) → C}
    {c1 : Fin n1 → C} (i j : Fin (n + 1 + 1)) (hij : i ≠ j ∧ S.τ (c i) = c j)
    (t : Tensor S c) (t1 : Tensor S c1) :
    (contrT _ (i.natAdd n1) (j.natAdd n1) (by simpa using hij) <| prodT t1 t) =
    ((permT id (IsReindexing.on_id_symm (IsReindexing.append_succSuccAbove_natAdd i j))) <|
      (prodT t1 (contrT n i j hij t)))
```

**`TensorSpecies.Tensor.prodT_contrT_fst`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Products.lean#L159).

> A contraction internal to the left factor commutes past the outer product with a right
> spectator. The mirror of `prodT_contrT_snd`, obtained from it by `prodT_swap`, so the right-hand
> side contracts the swapped product `prodT t1 t` and carries a block swap.

```lean
lemma prodT_contrT_fst {n n1 : ℕ} {c : Fin (n + 1 + 1) → C}
    {c1 : Fin n1 → C}
    (i j : Fin (n + 1 + 1)) (hij : i ≠ j ∧ S.τ (c i) = c j)
    (t : Tensor S c) (t1 : Tensor S c1) :
    prodT (contrT n i j hij t) t1 =
    permT _ IsReindexing.append_swap
      (permT id (IsReindexing.append_succSuccAbove_natAdd i j) <|
      contrT _
        (Fin.natAdd n1 i)
        (Fin.natAdd n1 j)
        (by simpa using hij) <|
      prodT t1 t)
```

## Depends on

- [Contractions on tensors](contraction-basic.md)
- [The product of tensors](../part-01/product.md)

## Sources

- [Physlib/Relativity/Tensors/Contraction/Products.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Products.lean)
