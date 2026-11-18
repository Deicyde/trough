---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.ComponentIdx.prod, TensorSpecies.Tensor.ComponentIdx.prod_apply_fst, TensorSpecies.Tensor.ComponentIdx.prod_apply_snd, TensorSpecies.Tensor.ComponentIdx.prod_symm_natAdd, TensorSpecies.Tensor.ComponentIdx.prod_symm_castAdd, TensorSpecies.Tensor.ComponentIdx.prod_symm_heq_castAdd, TensorSpecies.Tensor.ComponentIdx.prod_symm_heq_natAdd
statement: formalized
proof: formalized
---

# Products of component indices

The module `Physlib.Relativity.Tensors.ComponentIdx.Product`, [Physlib/Relativity/Tensors/ComponentIdx/Product.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Product.lean): 7 declarations, 3 with a docstring.

## i. Overview

> This file contains the component-index API induced by appending two lists of tensor colors.
>
> The main construction identifies component indices for appended color lists with pairs
> of component indices for each side of the append.

## ii. Key results

> - `TensorSpecies.Tensor.ComponentIdx.prod` is the equivalence between
>   `ComponentIdx (Fin.append c c1)` and `ComponentIdx c × ComponentIdx c1`.

## iv. References

> * None.

## A. Product equivalence

**`TensorSpecies.Tensor.ComponentIdx.prod`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Product.lean#L55).

> The equivalence between `ComponentIdx (Fin.append c c1)` and
> `ComponentIdx c × ComponentIdx c1` formed by products.

```lean
def ComponentIdx.prod {n1 n2 : ℕ} {c : Fin n1 → C} {c1 : Fin n2 → C} :
    ComponentIdx (S := S) (Fin.append c c1) ≃
      ComponentIdx (S := S) c × ComponentIdx (S := S) c1
```

**`TensorSpecies.Tensor.ComponentIdx.prod_apply_fst`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Product.lean#L68).

```lean
lemma ComponentIdx.prod_apply_fst {n1 n2 : ℕ} {c : Fin n1 → C} {c1 : Fin n2 → C}
    (p : ComponentIdx (S := S) (Fin.append c c1)) (i : Fin n1) :
    p.prod.1 i =
      basisIdxCongr (by simp) (p (Fin.castAdd n2 i))
```

**`TensorSpecies.Tensor.ComponentIdx.prod_apply_snd`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Product.lean#L73).

```lean
lemma ComponentIdx.prod_apply_snd {n1 n2 : ℕ} {c : Fin n1 → C} {c1 : Fin n2 → C}
    (p : ComponentIdx (S := S) (Fin.append c c1)) (i : Fin n2) :
    p.prod.2 i =
      basisIdxCongr (by simp) (p (Fin.natAdd n1 i))
```

**`TensorSpecies.Tensor.ComponentIdx.prod_symm_natAdd`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Product.lean#L79).

```lean
lemma ComponentIdx.prod_symm_natAdd {n1 n2 : ℕ} {c : Fin n1 → C} {c1 : Fin n2 → C}
    (p : ComponentIdx (S := S) c) (q : ComponentIdx (S := S) c1) (i : Fin n2) :
    ComponentIdx.prod.symm (p, q) (Fin.natAdd n1 i) =
      basisIdxCongr (by simp) (q i)
```

**`TensorSpecies.Tensor.ComponentIdx.prod_symm_castAdd`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Product.lean#L85).

```lean
lemma ComponentIdx.prod_symm_castAdd {n1 n2 : ℕ} {c : Fin n1 → C} {c1 : Fin n2 → C}
    (p : ComponentIdx (S := S) c) (q : ComponentIdx (S := S) c1) (i : Fin n1) :
    ComponentIdx.prod.symm (p, q) (Fin.castAdd n2 i) =
      basisIdxCongr (by simp) (p i)
```

**`TensorSpecies.Tensor.ComponentIdx.prod_symm_heq_castAdd`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Product.lean#L92).

> `ComponentIdx.prod_symm_castAdd` at a slot only propositionally equal to `Fin.castAdd n2 a`,
> up to `HEq`.

```lean
lemma ComponentIdx.prod_symm_heq_castAdd {n1 n2 : ℕ} {c : Fin n1 → C} {c1 : Fin n2 → C}
    (p : ComponentIdx (S := S) c) (q : ComponentIdx (S := S) c1) {x : Fin (n1 + n2)} {a : Fin n1}
    (hx : x = Fin.castAdd n2 a) : ComponentIdx.prod.symm (p, q) x ≍ p a
```

**`TensorSpecies.Tensor.ComponentIdx.prod_symm_heq_natAdd`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Product.lean#L101).

> `ComponentIdx.prod_symm_natAdd` at a slot only propositionally equal to `Fin.natAdd n1 a`,
> up to `HEq`.

```lean
lemma ComponentIdx.prod_symm_heq_natAdd {n1 n2 : ℕ} {c : Fin n1 → C} {c1 : Fin n2 → C}
    (p : ComponentIdx (S := S) c) (q : ComponentIdx (S := S) c1) {x : Fin (n1 + n2)} {a : Fin n2}
    (hx : x = Fin.natAdd n1 a) : ComponentIdx.prod.symm (p, q) x ≍ q a
```

## Depends on

- [Component indices](componentidx-basic.md)

## Sources

- [Physlib/Relativity/Tensors/ComponentIdx/Product.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Product.lean)
