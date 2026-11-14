---
declaration: module
origin: cited
lean: Fin.append_castAdd_natAdd_eq_id, Fin.append_succAbove_const_eq_cycleIcc, TensorSpecies.Tensor.IsReindexing, TensorSpecies.Tensor.IsReindexing.injective, TensorSpecies.Tensor.IsReindexing.surjective, TensorSpecies.Tensor.IsReindexing.auto, TensorSpecies.Tensor.IsReindexing.on_id, TensorSpecies.Tensor.IsReindexing.on_id_symm
statement: formalized
proof: formalized
---

# Reindexing of tensor components

The module `Physlib.Relativity.Tensors.Reindexing`, [Physlib/Relativity/Tensors/Reindexing.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean): 47 declarations, 22 with a docstring.

> In this file we give results related to the reindexing of tensors.
> If a tensor has indices specified by a list of colors `c : Fin n → C`, then reindexing the
> tensor corresponds to a bijection `σ : Fin m → Fin n` such that `c ∘ σ = c1` for some other
> list of colors `c1 : Fin m → C`. A reindexing might take a tensor ψⁱⱼ to a tensor ψʲᵢ
> by reordering the indices, or it might take a tensor ψⁱⱼᵏ to a tensor ψⁱᵏ.
>
> We are interested in the interaction of reindexing with the following operations on tensors:
> - `Fin.append` corresponds to the product of tensors.
> - `Fin.succAbove` corresponds to the evaluation of a tensor at a given index.
> - `Fin.succSuccAbove` corresponds to the contraction of a tensor at two given indices.

## Index maps

> The finite index maps out of which the reindexings below are built: `Fin.append` for products and
> `Fin.succAbove` for a deleted slot. The lemmas on `Fin.succSuccAbove`, for a deleted pair, are in
> `Physlib.Relativity.Tensors.Contraction.SuccSuccAbove`.

**`Fin.append_castAdd_natAdd_eq_id`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L44).

> Splitting `Fin (m + n)` into its two blocks and reassembling them is the identity.

```lean
lemma append_castAdd_natAdd_eq_id {m n : ℕ} :
    Fin.append (Fin.castAdd n) (Fin.natAdd m) = (id : Fin (m + n) → Fin (m + n))
```

**`Fin.append_succAbove_const_eq_cycleIcc`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L50).

> Moving slot `i` to the end is the cycle `[i, last]`: the block map that lists the
> `i.succAbove` survivors in order and then `i` is `Fin.cycleIcc i (Fin.last n)`.

```lean
lemma append_succAbove_const_eq_cycleIcc {n : ℕ} (i : Fin (n + 1)) :
    Fin.append i.succAbove (fun _ : Fin 1 => i) = ⇑(Fin.cycleIcc i (Fin.last n))
```

**`TensorSpecies.Tensor.IsReindexing`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L76).

> Given two lists of indices `c : Fin n → C` and `c1 : Fin m → C` a map
>   `σ : Fin m → Fin n` satisfies the condition `IsReindexing c c1 σ` if it is:
> - A bijection
> - Forms a commutative triangle with `c` and `c1`.

```lean
def IsReindexing {n m : ℕ} (c : Fin n → C) (c1 : Fin m → C)
    (σ : Fin m → Fin n) : Prop
```

## Properties of the underlying function

**`TensorSpecies.Tensor.IsReindexing.injective`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L88).

```lean
lemma injective {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ) : Function.Injective σ
```

**`TensorSpecies.Tensor.IsReindexing.surjective`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L91).

```lean
lemma surjective {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ) : Function.Surjective σ
```

**`TensorSpecies.Tensor.IsReindexing.auto`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L95).

```lean
lemma auto {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ := by {simp [IsReindexing]; try decide}) :
    IsReindexing c c1 σ
```

**`TensorSpecies.Tensor.IsReindexing.on_id`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L101).

```lean
lemma on_id {n : ℕ} {c c1 : Fin n → C} :
    IsReindexing c c1 (id : Fin n → Fin n) ↔ ∀ i, c i = c1 i
```

**`TensorSpecies.Tensor.IsReindexing.on_id_symm`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L105).

```lean
lemma on_id_symm {n : ℕ} {c c1 : Fin n → C} (h : IsReindexing c1 c id) :
    IsReindexing c c1 (id : Fin n → Fin n)
```

**`TensorSpecies.Tensor.IsReindexing.inv`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L111).

> For a map `σ` satisfying `IsReindexing c c1 σ`, the inverse of that map.

```lean
def inv {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    (σ : Fin m → Fin n) (h : IsReindexing c c1 σ) : Fin n → Fin m
```

**`TensorSpecies.Tensor.IsReindexing.toEquiv`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L118).

> For a map `σ : Fin m → Fin n` satisfying `IsReindexing c c1 σ`,
> that map lifted to an equivalence between
> `Fin n` and `Fin m`.

```lean
def toEquiv {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ) :
    Fin n ≃ Fin m
```

**`TensorSpecies.Tensor.IsReindexing.apply_inv_apply`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L126).

```lean
lemma apply_inv_apply {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    (σ : Fin m → Fin n) (h : IsReindexing c c1 σ) (x : Fin m) :
    h.inv σ (σ x) = x
```

**`TensorSpecies.Tensor.IsReindexing.inv_apply_apply`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L132).

```lean
lemma inv_apply_apply {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    (σ : Fin m → Fin n) (h : IsReindexing c c1 σ) (x : Fin n) :
    σ (h.inv σ x) = x
```

**`TensorSpecies.Tensor.IsReindexing.swap_of_eq`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L140).

> The swap `![1, 0]` reindexes two rank-two colour lists whose colours match crosswise; `swap`
> with the target colours given by equations.

```lean
lemma swap_of_eq {c c1 : Fin 2 → C} (h0 : c 1 = c1 0) (h1 : c 0 = c1 1) :
    IsReindexing c c1 ![1, 0]
```

**`TensorSpecies.Tensor.IsReindexing.inv_eq_self_of_pointwise_eq`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L147).

```lean
lemma inv_eq_self_of_pointwise_eq {n : ℕ} {c c1 : Fin n → C} {σ : Fin n → Fin n}
    (h : IsReindexing c c1 σ) (hσ : ∀ x, σ x = x) (x : Fin n) :
    h.inv σ x = x
```

**`TensorSpecies.Tensor.IsReindexing.inv_id_eq`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L154).

```lean
lemma inv_id_eq {n : ℕ} {c c1 : Fin n → C}
    (h : IsReindexing c c1 (id : Fin n → Fin n)) (x : Fin n) :
    h.inv (id : Fin n → Fin n) x = x
```

**`TensorSpecies.Tensor.IsReindexing.inv_cast_eq`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L159).

```lean
lemma inv_cast_eq {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C} (e : m = n)
    (h : IsReindexing c c1 (Fin.cast e)) (x : Fin n) :
    h.inv (Fin.cast e) x = Fin.cast e.symm x
```

**`TensorSpecies.Tensor.IsReindexing.inv_equiv_symm_eq`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L166).

```lean
lemma inv_equiv_symm_eq {n : ℕ} {c c1 : Fin n → C} (e : Equiv.Perm (Fin n))
    (h : IsReindexing c c1 ⇑e.symm) (x : Fin n) :
    h.inv ⇑e.symm x = e x
```

**`TensorSpecies.Tensor.IsReindexing.preserve_color`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L173).

```lean
lemma preserve_color {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ) :
    ∀ (x : Fin m), c1 x = (c ∘ σ) x
```

**`TensorSpecies.Tensor.IsReindexing.inv_perserve_color`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L183).

```lean
lemma inv_perserve_color {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ) (x : Fin n) :
    c1 (h.inv σ x) = c x
```

**`TensorSpecies.Tensor.IsReindexing.toEquiv_symm_perserve_color`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L194).

```lean
lemma toEquiv_symm_perserve_color {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ) (x : Fin m) :
    c (h.toEquiv.symm x) = c1 x
```

## Constructors

**`TensorSpecies.Tensor.IsReindexing.swap`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L208).

```lean
lemma swap {n : ℕ} {c : Fin n → C} (i j : Fin n) :
    IsReindexing c (c ∘ Equiv.swap i j) (Equiv.swap i j)
```

**`TensorSpecies.Tensor.IsReindexing.symm`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L213).

> The inverse of a map satisfying `IsReindexing c c1 σ` is a reindexing of `c1` by `c`.

```lean
lemma symm {n m : ℕ} {c : Fin n → C} {c1 : Fin m → C}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ) : IsReindexing c1 c (h.inv σ)
```

**`TensorSpecies.Tensor.IsReindexing.symm_of_id`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L217).

```lean
lemma symm_of_id {n : ℕ} {c c1 : Fin n → C} (h : IsReindexing c c1 id) :
    IsReindexing c1 c id
```

**`TensorSpecies.Tensor.IsReindexing.comp`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L223).

> The composition of two maps satisfying `IsReindexing` also satisfies the `IsReindexing`.

```lean
lemma comp {n n1 n2 : ℕ} {c : Fin n → C} {c1 : Fin n1 → C}
    {c2 : Fin n2 → C} {σ : Fin n1 → Fin n} {σ2 : Fin n2 → Fin n1}
    (h : IsReindexing c c1 σ) (h2 : IsReindexing c1 c2 σ2) : IsReindexing c c2 (σ ∘ σ2)
```

**`TensorSpecies.Tensor.IsReindexing.append_congr_left`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L228).

```lean
lemma append_congr_left {n n' n2 : ℕ} {c : Fin n → C} {c' : Fin n' → C}
    {σ : Fin n' → Fin n} (c2 : Fin n2 → C) (h : IsReindexing c c' σ) :
    IsReindexing (Fin.append c c2) (Fin.append c' c2)
      (Fin.append (Fin.castAdd n2 ∘ σ) (Fin.natAdd n))
```

**`TensorSpecies.Tensor.IsReindexing.append_congr_right`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L244).

```lean
lemma append_congr_right {n n' n2 : ℕ} {c : Fin n → C} {c' : Fin n' → C}
    {σ : Fin n' → Fin n} (c2 : Fin n2 → C) (h : IsReindexing c c' σ) :
    IsReindexing (Fin.append c2 c) (Fin.append c2 c')
      (Fin.append (Fin.castAdd n) (Fin.natAdd n2 ∘ σ))
```

**`TensorSpecies.Tensor.IsReindexing.append_zero_right`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L260).

```lean
lemma append_zero_right {n} {c : Fin n → C}
    {c1 : Fin 0 → C} : IsReindexing c (Fin.append c c1) id
```

**`TensorSpecies.Tensor.IsReindexing.append_swap`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L269).

```lean
lemma append_swap {n n2 : ℕ} {c : Fin n → C} {c2 : Fin n2 → C} :
    IsReindexing (Fin.append c c2) (Fin.append c2 c)
      (Fin.append (Fin.natAdd n) (Fin.castAdd n2))
```

**`TensorSpecies.Tensor.IsReindexing.append_assoc_right`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L284).

```lean
lemma append_assoc_right   {n1 n2 n3 : ℕ} {c : Fin n1 → C} {c2 : Fin n2 → C} {c3 : Fin n3 → C} :
    IsReindexing (Fin.append c (Fin.append c2 c3)) (Fin.append (Fin.append c c2) c3)
      (Fin.cast (by grind))
```

**`TensorSpecies.Tensor.IsReindexing.append_assoc_left`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L289).

```lean
lemma append_assoc_left {n1 n2 n3 : ℕ} {c : Fin n1 → C} {c2 : Fin n2 → C} {c3 : Fin n3 → C} :
    IsReindexing (Fin.append (Fin.append c c2) c3) (Fin.append c (Fin.append c2 c3))
      (Fin.cast (by grind))
```

**`TensorSpecies.Tensor.IsReindexing.append_succAbove_natAdd`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L294).

```lean
lemma append_succAbove_natAdd {n n1 : ℕ} {c : Fin n → C} {c1 : Fin (n1 + 1) → C}
    (i : Fin (n1 + 1)) :
    IsReindexing (Fin.append c c1 ∘ (Fin.natAdd n i).succAbove)
      (Fin.append c (c1 ∘ i.succAbove)) id
```

**`TensorSpecies.Tensor.IsReindexing.append_succAbove_castAdd`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L316).

```lean
lemma append_succAbove_castAdd {n n1 : ℕ} {c : Fin (n + 1) → C} {c1 : Fin (n1 + 1) → C}
    (i : Fin (n + 1)) :
    IsReindexing (Fin.append c c1 ∘ (Fin.castAdd (n1 + 1) i).succAbove)
      (Fin.append (c ∘ i.succAbove) c1) (Fin.cast (by grind))
```

**`TensorSpecies.Tensor.IsReindexing.append_succSuccAbove_natAdd`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L345).

> Removing two entries from the right component of `Fin.append c1 c` commutes with the
> append: removing the `i`-th and `j`-th entries of `c` and then appending `c1` matches
> removing the corresponding entries of `Fin.append c1 c`, via the identity permutation.
> This is used for the commutation of taking a *product* of tensors
> with *contraction* of indices.

```lean
lemma append_succSuccAbove_natAdd {n n1 : ℕ} {c : Fin (n + 1 + 1) → C}
    {c1 : Fin n1 → C} (i j : Fin (n + 1 + 1)) :
    IsReindexing (Fin.append c1 c ∘ (Fin.natAdd n1 i).succSuccAbove (Fin.natAdd n1 j))
      (Fin.append c1 (c ∘ i.succSuccAbove j)) id
```

**`TensorSpecies.Tensor.IsReindexing.succAbove_of_eq_zero`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L356).

> Given a reindexing of `c` by `c1` via `σ` for which the index `i` is sent to `0`,
> removing the `i`-th entry of `c1` and the first entry of `c` yields a reindexing of
> `c ∘ Fin.succ` by `c1 ∘ i.succAbove` via the map sending `j` to the predecessor of
> `σ (i.succAbove j)`.

```lean
lemma succAbove_of_eq_zero {n n1 : ℕ} {c : Fin (n + 1) → C} {c1 : Fin (n1 + 1) → C}
    {σ : Fin (n1 + 1) → Fin (n + 1)} (i : Fin (n1 + 1))
    (h : IsReindexing c c1 σ) (hi : σ i = 0) :
    IsReindexing (c ∘ Fin.succ) (c1 ∘ i.succAbove)
      (fun j => (σ (i.succAbove j)).pred (by simp [← hi, h.injective.eq_iff]))
```

**`TensorSpecies.Tensor.IsReindexing.succAbove_of_neq_zero`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L379).

> Given a reindexing of `c` by `c1` via `σ` for which the index `i` is not sent to `0`,
> removing the `i`-th entry of `c1` and the `(σ i)`-th entry of `c` yields a reindexing of
> `c ∘ (σ i).succAbove` by `c1 ∘ i.succAbove` via the map
> `(σ i).pred.predAbove ∘ σ ∘ i.succAbove`.

```lean
lemma succAbove_of_neq_zero {n n1 : ℕ} {c : Fin (n + 1) → C} {c1 : Fin (n1 + 1) → C}
    {σ : Fin (n1 + 1) → Fin (n + 1)} (i : Fin (n1 + 1))
    (h : IsReindexing c c1 σ) (hi : σ i ≠ 0) :
    IsReindexing (c ∘ (σ i).succAbove) (c1 ∘ i.succAbove)
      ((Fin.pred (σ i) hi).predAbove  ∘ σ ∘ i.succAbove)
```

**`TensorSpecies.Tensor.IsReindexing.succAbove`**, a lemma, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L418).

> Given a reindexing of `c` by `c1` via `σ`, removing the `i`-th entry of `c1` and the
> `(σ i)`-th entry of `c` yields a reindexing of `c ∘ (σ i).succAbove` by `c1 ∘ i.succAbove`.
> This unifies `succAbove_of_eq_zero` and `succAbove_of_neq_zero` via a case split on
> whether `σ i = 0`. This is used for the commutation of *permutation*
> of indices with *evaluation* of indices.

```lean
lemma succAbove {n n1 : ℕ} {c : Fin (n + 1) → C} {c1 : Fin (n1 + 1) → C}
    {σ : Fin (n1 + 1) → Fin (n + 1)} (i : Fin (n1 + 1))
    (h : IsReindexing c c1 σ) :
    IsReindexing (c ∘ (σ i).succAbove) (c1 ∘ i.succAbove)
      (if hi : σ i = 0 then fun j => (σ (i.succAbove j)).pred (by simp [← hi, h.injective.eq_iff])
      else (Fin.pred (σ i) hi).predAbove  ∘ σ ∘ i.succAbove)
```

**`TensorSpecies.Tensor.IsReindexing.succAbove_of_succAbove_eq`**, a lemma, [line 436](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L436).

> The conclusion of `succAbove` from an explicit survivor relabelling: if `σ'` fills the square
> `(σ i).succAbove ∘ σ' = σ ∘ i.succAbove`, carrying the complement of `i` to the complement of
> `σ i`, then it is a reindexing of the two shortened colour lists. The square forces `σ'` to be
> injective, hence bijective, so no bijectivity hypothesis is needed; this is why the statement is
> restricted to equal lengths.
>
> Where `succAbove` builds the relabelling from `σ` as a `dite` composite, the map here is the
> caller's, which is what lets it stand in the statement of a lemma the caller instantiates.

```lean
lemma succAbove_of_succAbove_eq {n : ℕ} {c c1 : Fin (n + 1) → C}
    {σ : Fin (n + 1) → Fin (n + 1)} {σ' : Fin n → Fin n} (i : Fin (n + 1))
    (h : IsReindexing c c1 σ) (hσ' : (σ i).succAbove ∘ σ' = σ ∘ i.succAbove) :
    IsReindexing (c ∘ (σ i).succAbove) (c1 ∘ i.succAbove) σ'
```

**`TensorSpecies.Tensor.IsReindexing.succSuccAbove`**, a lemma, [line 450](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L450).

> Given a reindexing of `c` by `c1` via `σ` and two distinct indices `i ≠ j`, removing the
> `i`-th and `j`-th entries of `c1` and the `(σ i)`-th and `(σ j)`-th entries of `c` yields a
> reindexing of `c ∘ (σ i).succSuccAbove (σ j)` by `c1 ∘ i.succSuccAbove j`.
> This is used for the commutation of *permutation* of indices with
> *contraction* of indices.

```lean
lemma succSuccAbove {n n1 : ℕ} {c : Fin (n + 1 + 1) → C}
    {c1 : Fin (n1 + 1 + 1) → C}
    (i j : Fin (n1 + 1 + 1)) (hij : i ≠ j)
    {σ : Fin (n1 + 1 + 1) → Fin (n + 1 + 1)} (hσ : IsReindexing c c1 σ) :
    IsReindexing (c ∘  (σ i).succSuccAbove (σ j))
      (c1 ∘ i.succSuccAbove j) (i.funPredPredAbove j hij σ hσ.1)
```

**`TensorSpecies.Tensor.IsReindexing.succSuccAbove_comm`**, a lemma, [line 466](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L466).

> Removing two pairs of entries from `c` in either order gives the same colour list:
> removing the `i1`-th and `j1`-th entries and then the (shifted) `i2`-th and `j2`-th entries
> matches removing the `i2`-th and `j2`-th entries first and then the (shifted) `i1`-th and
> `j1`-th entries, via the identity permutation.
> This is used for the commutation of two *contractions*.

```lean
lemma succSuccAbove_comm {n : ℕ} {c : Fin (n + 1 + 1 + 1 + 1) → C}
    (i1 j1 : Fin (n + 1 + 1 + 1 + 1)) (i2 j2 : Fin (n + 1 + 1))
    (hij1 : i1 ≠ j1) (hij2 : i2 ≠ j2) :
    let i2' := (i1.succSuccAbove j1 i2);
    let j2' := (i1.succSuccAbove j1 j2);
    have hi2j2' : i2' ≠ j2' := by simp [i2', j2', hij2];
    let i1' := (predPredAbove i2' j2' hi2j2' i1 (by simp [i2', j2']));
    let j1' := (predPredAbove i2' j2' hi2j2' j1 (by simp [i2', j2']));
    IsReindexing ((c ∘ i2'.succSuccAbove j2') ∘ i1'.succSuccAbove j1')
      ((c ∘ i1.succSuccAbove j1) ∘ i2.succSuccAbove j2) id
```

**`TensorSpecies.Tensor.IsReindexing.succAbove_succSuccAbove_comm`**, a lemma, [line 489](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L489).

> Removing one entry and then a pair of entries from `c` in either order gives the same
> colour list: removing the `k`-th entry and then the (shifted) `i`-th and `j`-th entries
> matches removing the `i`-th and `j`-th entries first and then the (shifted) `k`-th entry,
> via the identity permutation.
> This is used for the commutation of a *contraction* with an *evaluation*.

```lean
lemma succAbove_succSuccAbove_comm {n : ℕ} {c : Fin (n + 1 + 1 + 1) → C}
    (k : Fin (n + 1 + 1 + 1)) (i j : Fin (n + 1 + 1)) (hij : i ≠ j) :
    let i' := k.succAbove i;
    let j' := k.succAbove j;
    have hij' : i' ≠ j' := by simp [i', j', hij];
    let k' := predPredAbove i' j' hij' k (by simp [i', j', Ne.symm]);
    IsReindexing ((c ∘ i'.succSuccAbove j') ∘ k'.succAbove)
      ((c ∘ k.succAbove) ∘ i.succSuccAbove j) id
```

**`TensorSpecies.Tensor.IsReindexing.succSuccAbove_succAbove_comm`**, a lemma, [line 507](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L507).

```lean
lemma succSuccAbove_succAbove_comm {n : ℕ} {c : Fin (n + 1 + 1 + 1) → C}
    (k : Fin (n + 1)) (i j : Fin (n + 1 + 1 + 1)) :
    -- The corresponding position of k in the full list.
    let k' := Fin.succSuccAbove i j k
    let k'' := Fin.predAbove 0 k'
    -- The position of i after removing k'
    let i' := k''.predAbove i
    -- The position of j after removing k'
    let j' := k''.predAbove j
    IsReindexing ((c ∘ k'.succAbove) ∘ i'.succSuccAbove j')
      ((c ∘ i.succSuccAbove j) ∘ k.succAbove) id
```

**`TensorSpecies.Tensor.IsReindexing.succAbove_succAbove_comm`**, a lemma, [line 527](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L527).

> Removing two single entries from `c` in either order gives the same colour list:
> removing the `k1`-th entry and then the (shifted) `k2`-th entry matches removing the
> `k2`-th entry first and then the (shifted) `k1`-th entry, via the identity permutation.
> This is used for the commutation of two *evaluations* of indices.

```lean
lemma succAbove_succAbove_comm {n : ℕ} {c : Fin (n + 1 + 1) → C}
    (k1 : Fin (n + 1 + 1)) (k2 : Fin (n + 1)) :
    let k2' := k1.succAbove k2;
    let k1' := k2.predAbove k1;
    IsReindexing ((c ∘ k2'.succAbove) ∘ k1'.succAbove)
      ((c ∘ k1.succAbove) ∘ k2.succAbove) id
```

**`TensorSpecies.Tensor.IsReindexing.append_succ_last`**, a lemma, [line 543](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L543).

> Splitting a list of colours `c : Fin (n + 1) → C` into its first `n` entries and its
> last entry recovers `c`: the identity permutation matches
> `Fin.append (c ∘ (Fin.last n).succAbove) ![c (Fin.last n)]` with `c`.

```lean
lemma append_succ_last {n : ℕ} (c : Fin (n + 1) → C) :
    IsReindexing (Fin.append (c ∘ (Fin.last n).succAbove) ![c (Fin.last n)]) c id
```

**`TensorSpecies.Tensor.IsReindexing.move_last`**, a lemma, [line 554](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L554).

> Splitting a list of colours `c : Fin (n + 1) → C` at an arbitrary slot `i`, rather than at the
> last one as in `append_succ_last`: the block map that lists the `i.succAbove` survivors and then
> `i` itself matches `c` with the survivors of `i` followed by the surviving entry `c1 1` of a
> rank-two list `c1` whose second entry is slot `i`'s colour.

```lean
lemma move_last {n : ℕ} {c : Fin (n + 1) → C} {c1 : Fin 2 → C} (i : Fin (n + 1))
    (hc : c i = c1 1) :
    IsReindexing c
      (Fin.append (c ∘ i.succAbove) (c1 ∘ (0 : Fin 2).succAbove))
      (Fin.append i.succAbove (fun _ : Fin 1 => i))
```

**`TensorSpecies.Tensor.IsReindexing.update_update_of_eq`**, a lemma, [line 570](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L570).

> Updating slot `i` of `c` to `d` and then back to `e = c i` returns `c`, no other slot moving:
> the colour cast a round trip of two contractions at slot `i` generates.

```lean
lemma update_update_of_eq {n : ℕ} {c : Fin n → C} {d e : C} (i : Fin n) (he : c i = e) :
    IsReindexing c (Function.update (Function.update c i d) i e) (id : Fin n → Fin n)
```

**`TensorSpecies.Tensor.IsReindexing.append_of_first`**, a lemma, [line 577](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L577).

> Splitting a list of colours `c : Fin (n + 1) → C` into its first entry and its remaining
> `n` entries recovers `c`: the canonical reindexing `Fin (1 + n) ≃ Fin (n + 1)` matches
> `Fin.append ![c 0] (c ∘ Fin.succAbove 0)` with `c`.

```lean
lemma append_of_first {n : ℕ} (c : Fin (n + 1) → C) :
    IsReindexing (Fin.append ![c 0] (c ∘ Fin.succAbove 0)) c (Fin.cast (by grind))
```

**`TensorSpecies.Tensor.IsReindexing.fin_cast_isReindexing`**, a lemma, [line 587](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean#L587).

> Casting the domain along an equality `n1 = n` of lengths is a reindexing of `c` by
> `c ∘ Fin.cast h`.

```lean
lemma fin_cast_isReindexing (n n1 : ℕ) {c : Fin n → C} (h : n1 = n) :
    IsReindexing c (c ∘ Fin.cast h) (Fin.cast h)
```

## Depends on

- [Defining succSuccAbove](../part-03/contraction-succsuccabove.md)

## Sources

- [Physlib/Relativity/Tensors/Reindexing.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Reindexing.lean)
