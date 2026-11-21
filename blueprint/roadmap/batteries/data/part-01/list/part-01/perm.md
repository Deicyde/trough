---
catalog: module
lean: List.nil_subperm, List.Perm.subperm_left, List.Perm.subperm_right, List.Sublist.subperm, List.Perm.subperm, List.Subperm.refl, List.Subperm.trans, List.Subperm.cons_self, List.Subperm.cons_right, List.Subperm.length_le, List.Subperm.perm_of_length_le, List.Subperm.antisymm, List.Subperm.subset, List.Subperm.filter, List.subperm_nil, List.singleton_subperm_iff, List.Subperm.countP_le, List.Subperm.count_le, List.subperm_cons, List.cons_subperm_of_not_mem_of_mem, List.subperm_append_left, List.subperm_append_right, List.Subperm.exists_of_length_lt, List.subperm_of_subset, List.Nodup.perm_iff_eq_of_sublist, List.subperm_cons_erase, List.erase_subperm, List.Subperm.erase, List.Perm.diff_right, List.Perm.diff_left, List.Perm.diff, List.Subperm.diff_right, List.erase_cons_subperm_cons_erase, List.subperm_cons_diff, List.subset_cons_diff, List.subperm_append_diff_self_of_count_le, List.subperm_ext_iff, List.isSubperm_iff, List.decidableSubperm, List.Subperm.cons_left, List.Perm.union_right, List.Perm.union_left, List.Perm.union, List.Perm.inter_right, List.Perm.inter_left, List.Perm.inter, List.Perm.flatten_congr, List.perm_insertP, List.Perm.insertP, List.getD_set_perm_cons, List.cons_uncurry_swapAt_perm_cons, List.swap_perm, List.mem_swap, List.Subperm.idxInj, List.coe_idxInj, List.Subperm.getElem_idxInj_eq_getElem, List.Subperm.idxInj_injective, List.Subperm.idxInj_inj, List.Perm.idxBij, List.Perm.subperm_idxBij, List.Perm.coe_idxBij, List.Perm.getElem_idxBij_eq_getElem, List.Perm.getElem_idxBij_symm_eq_getElem, List.Perm.idxBij_leftInverse_idxBij_symm, List.Perm.idxBij_rightInverse_idxBij_symm, List.Perm.idxBij_symm_rightInverse_idxBij, List.Perm.idxBij_symm_leftInverse_idxBij, List.Perm.idxBij_idxBij_symm, List.Perm.idxBij_symm_idxBij, List.Perm.idxBij_injective, List.Perm.idxBij_surjective
statement: formalized
proof: formalized
---

# List Permutations

`Batteries.Data.List.Perm`, in [Batteries/Data/List/Perm.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean), by Leonardo de Moura, Jeremy Avigad, Mario Carneiro.

> This file introduces the `List.Perm` relation, which is true if two lists are permutations of one
> another.
>
> ## Notation
>
> The notation `~` is used for permutation equivalence.

`List.nil_subperm` (theorem, [line 30](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L30))

```lean
theorem nil_subperm {l : List α} : [] <+~ l
```

`List.Perm.subperm_left` (theorem, [line 32](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L32))

```lean
theorem Perm.subperm_left {l l₁ l₂ : List α} (p : l₁ ~ l₂) : l <+~ l₁ ↔ l <+~ l₂
```

`List.Perm.subperm_right` (theorem, [line 38](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L38))

```lean
theorem Perm.subperm_right {l₁ l₂ l : List α} (p : l₁ ~ l₂) : l₁ <+~ l ↔ l₂ <+~ l
```

`List.Sublist.subperm` (theorem, [line 41](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L41))

```lean
theorem Sublist.subperm {l₁ l₂ : List α} (s : l₁ <+ l₂) : l₁ <+~ l₂
```

`List.Perm.subperm` (theorem, [line 43](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L43))

```lean
theorem Perm.subperm {l₁ l₂ : List α} (p : l₁ ~ l₂) : l₁ <+~ l₂
```

`List.Subperm.refl` (theorem, [line 45](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L45))

```lean
theorem Subperm.refl (l : List α) : l <+~ l
```

`List.Subperm.trans` (theorem, [line 47](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L47))

```lean
theorem Subperm.trans {l₁ l₂ l₃ : List α} (s₁₂ : l₁ <+~ l₂) (s₂₃ : l₂ <+~ l₃) : l₁ <+~ l₃
```

`List.Subperm.cons_self` (theorem, [line 52](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L52))

```lean
theorem Subperm.cons_self : l <+~ a :: l
```

`List.Subperm.cons_right` (theorem, [line 54](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L54))

```lean
theorem Subperm.cons_right {α : Type _} {l l' : List α} (x : α) (h : l <+~ l') : l <+~ x :: l'
```

`List.Subperm.length_le` (theorem, [line 57](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L57))

```lean
theorem Subperm.length_le {l₁ l₂ : List α} : l₁ <+~ l₂ → length l₁ ≤ length l₂
```

`List.Subperm.perm_of_length_le` (theorem, [line 60](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L60))

```lean
theorem Subperm.perm_of_length_le {l₁ l₂ : List α} : l₁ <+~ l₂ → length l₂ ≤ length l₁ → l₁ ~ l₂
```

`List.Subperm.antisymm` (theorem, [line 63](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L63))

```lean
theorem Subperm.antisymm {l₁ l₂ : List α} (h₁ : l₁ <+~ l₂) (h₂ : l₂ <+~ l₁) : l₁ ~ l₂
```

`List.Subperm.subset` (theorem, [line 66](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L66))

```lean
theorem Subperm.subset {l₁ l₂ : List α} : l₁ <+~ l₂ → l₁ ⊆ l₂
```

`List.Subperm.filter` (theorem, [line 69](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L69))

```lean
theorem Subperm.filter (p : α → Bool) ⦃l l' : List α⦄ (h : l <+~ l') :
    filter p l <+~ filter p l'
```

`List.subperm_nil` (theorem, [line 74](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L74))

```lean
theorem subperm_nil : l <+~ [] ↔ l = []
```

`List.singleton_subperm_iff` (theorem, [line 77](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L77))

```lean
theorem singleton_subperm_iff {α} {l : List α} {a : α} : [a] <+~ l ↔ a ∈ l
```

`List.Subperm.countP_le` (theorem, [line 81](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L81))

```lean
theorem Subperm.countP_le (p : α → Bool) {l₁ l₂ : List α} : l₁ <+~ l₂ → countP p l₁ ≤ countP p l₂
```

`List.Subperm.count_le` (theorem, [line 84](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L84))

```lean
theorem Subperm.count_le [BEq α] {l₁ l₂ : List α} (s : l₁ <+~ l₂) (a) :
    count a l₁ ≤ count a l₂
```

`List.subperm_cons` (theorem, [line 87](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L87))

```lean
theorem subperm_cons (a : α) {l₁ l₂ : List α} : a :: l₁ <+~ a :: l₂ ↔ l₁ <+~ l₂
```

`List.cons_subperm_of_not_mem_of_mem` (theorem, [line 94](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L94))

> Weaker version of `Subperm.cons_left`

```lean
theorem cons_subperm_of_not_mem_of_mem {a : α} {l₁ l₂ : List α} (h₁ : a ∉ l₁) (h₂ : a ∈ l₂)
    (s : l₁ <+~ l₂) : a :: l₁ <+~ l₂
```

`List.subperm_append_left` (theorem, [line 115](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L115))

```lean
theorem subperm_append_left {l₁ l₂ : List α} : ∀ l, l ++ l₁ <+~ l ++ l₂ ↔ l₁ <+~ l₂
```

`List.subperm_append_right` (theorem, [line 119](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L119))

```lean
theorem subperm_append_right {l₁ l₂ : List α} (l) : l₁ ++ l <+~ l₂ ++ l ↔ l₁ <+~ l₂
```

`List.Subperm.exists_of_length_lt` (theorem, [line 122](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L122))

```lean
theorem Subperm.exists_of_length_lt {l₁ l₂ : List α} (s : l₁ <+~ l₂) (h : length l₁ < length l₂) :
    ∃ a, a :: l₁ <+~ l₂
```

`List.subperm_of_subset` (theorem, [line 138](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L138))

```lean
theorem subperm_of_subset (d : Nodup l₁) (H : l₁ ⊆ l₂) : l₁ <+~ l₂
```

`List.Nodup.perm_iff_eq_of_sublist` (theorem, [line 145](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L145))

```lean
theorem Nodup.perm_iff_eq_of_sublist {l₁ l₂ l : List α} (d : Nodup l)
    (s₁ : l₁ <+ l) (s₂ : l₂ <+ l) : l₁ ~ l₂ ↔ l₁ = l₂
```

`List.subperm_cons_erase` (theorem, [line 163](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L163))

```lean
theorem subperm_cons_erase [BEq α] [LawfulBEq α] (a : α) (l : List α) : l <+~ a :: l.erase a
```

`List.erase_subperm` (theorem, [line 169](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L169))

```lean
theorem erase_subperm [BEq α] (a : α) (l : List α) : l.erase a <+~ l
```

`List.Subperm.erase` (theorem, [line 171](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L171))

```lean
theorem Subperm.erase [BEq α] [LawfulBEq α] (a : α) (h : l₁ <+~ l₂) : l₁.erase a <+~ l₂.erase a
```

`List.Perm.diff_right` (theorem, [line 175](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L175))

```lean
theorem Perm.diff_right [BEq α] [LawfulBEq α] (t : List α) (h : l₁ ~ l₂) :
    l₁.diff t ~ l₂.diff t
```

`List.Perm.diff_left` (theorem, [line 185](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L185))

```lean
theorem Perm.diff_left [BEq α] [LawfulBEq α] (l : List α) (h : t₁ ~ t₂) :
    l.diff t₁ = l.diff t₂
```

`List.Perm.diff` (theorem, [line 197](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L197))

```lean
theorem Perm.diff [BEq α] [LawfulBEq α] {l₁ l₂ t₁ t₂ : List α} (hl : l₁ ~ l₂) (ht : t₁ ~ t₂) :
    l₁.diff t₁ ~ l₂.diff t₂
```

`List.Subperm.diff_right` (theorem, [line 201](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L201))

```lean
theorem Subperm.diff_right [BEq α] [LawfulBEq α] (h : l₁ <+~ l₂) (t : List α) :
    l₁.diff t <+~ l₂.diff t
```

`List.erase_cons_subperm_cons_erase` (theorem, [line 213](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L213))

```lean
theorem erase_cons_subperm_cons_erase [BEq α] [LawfulBEq α] (a b : α) (l : List α) :
    (a :: l).erase b <+~ a :: l.erase b
```

`List.subperm_cons_diff` (theorem, [line 221](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L221))

```lean
theorem subperm_cons_diff [BEq α] [LawfulBEq α] {a : α} {l₁ l₂ : List α} :
    (a :: l₁).diff l₂ <+~ a :: l₁.diff l₂
```

`List.subset_cons_diff` (theorem, [line 229](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L229))

```lean
theorem subset_cons_diff [BEq α] [LawfulBEq α] {a : α} {l₁ l₂ : List α} :
    (a :: l₁).diff l₂ ⊆ a :: l₁.diff l₂
```

`List.subperm_append_diff_self_of_count_le` (theorem, [line 234](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L234))

> The list version of `add_tsub_cancel_of_le` for multisets.

```lean
theorem subperm_append_diff_self_of_count_le [BEq α] [LawfulBEq α] {l₁ l₂ : List α}
    (h : ∀ x ∈ l₁, count x l₁ ≤ count x l₂) : l₁ ++ l₂.diff l₁ ~ l₂
```

`List.subperm_ext_iff` (theorem, [line 252](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L252))

> The list version of `Multiset.le_iff_count`.

```lean
theorem subperm_ext_iff [BEq α] [LawfulBEq α] {l₁ l₂ : List α} :
    l₁ <+~ l₂ ↔ ∀ x ∈ l₁, count x l₁ ≤ count x l₂
```

`List.isSubperm_iff` (theorem, [line 259](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L259))

```lean
theorem isSubperm_iff [BEq α] [LawfulBEq α] {l₁ l₂ : List α} : l₁.isSubperm l₂ ↔ l₁ <+~ l₂
```

`List.decidableSubperm` (instance, [line 262](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L262))

```lean
instance decidableSubperm [BEq α] [LawfulBEq α] :
    DecidableRel ((· <+~ ·) : List α → List α → Prop)
```

`List.Subperm.cons_left` (theorem, [line 266](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L266))

```lean
theorem Subperm.cons_left [BEq α] [LawfulBEq α] (h : l₁ <+~ l₂) (x : α)
    (hx : count x l₁ < count x l₂) : x :: l₁ <+~ l₂
```

`List.Perm.union_right` (theorem, [line 277](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L277))

```lean
theorem Perm.union_right [BEq α] [LawfulBEq α] (t₁ : List α) (h : l₁ ~ l₂) :
    l₁ ∪ t₁ ~ l₂ ∪ t₁
```

`List.Perm.union_left` (theorem, [line 285](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L285))

```lean
theorem Perm.union_left [BEq α] [LawfulBEq α] (l : List α) (h : t₁ ~ t₂) : l ∪ t₁ ~ l ∪ t₂
```

`List.Perm.union` (theorem, [line 290](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L290))

```lean
theorem Perm.union [BEq α] [LawfulBEq α] {l₁ l₂ t₁ t₂ : List α} (p₁ : l₁ ~ l₂) (p₂ : t₁ ~ t₂) :
    l₁ ∪ t₁ ~ l₂ ∪ t₂
```

`List.Perm.inter_right` (theorem, [line 294](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L294))

```lean
theorem Perm.inter_right [BEq α] (t₁ : List α) : l₁ ~ l₂ → l₁ ∩ t₁ ~ l₂ ∩ t₁
```

`List.Perm.inter_left` (theorem, [line 296](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L296))

```lean
theorem Perm.inter_left [BEq α] [LawfulBEq α] (l : List α) (p : t₁ ~ t₂) : l ∩ t₁ = l ∩ t₂
```

`List.Perm.inter` (theorem, [line 299](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L299))

```lean
theorem Perm.inter [BEq α] [LawfulBEq α] {l₁ l₂ t₁ t₂ : List α} (p₁ : l₁ ~ l₂) (p₂ : t₁ ~ t₂) :
    l₁ ∩ t₁ ~ l₂ ∩ t₂
```

`List.Perm.flatten_congr` (theorem, [line 303](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L303))

```lean
theorem Perm.flatten_congr :
    ∀ {l₁ l₂ : List (List α)} (_ : List.Forall₂ (· ~ ·) l₁ l₂), l₁.flatten ~ l₂.flatten
```

`List.perm_insertP` (theorem, [line 308](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L308))

```lean
theorem perm_insertP (p : α → Bool) (a l) : insertP p a l ~ a :: l
```

`List.Perm.insertP` (theorem, [line 316](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L316))

```lean
theorem Perm.insertP (p : α → Bool) (a) (h : l₁ ~ l₂) : insertP p a l₁ ~ insertP p a l₂
```

`List.getD_set_perm_cons` (theorem, [line 319](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L319))

```lean
theorem getD_set_perm_cons : ∀ (xs : List α) (i : Nat) (v : α),
    xs[i]?.getD v :: xs.set i v ~ v :: xs
```

`List.cons_uncurry_swapAt_perm_cons` (theorem, [line 326](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L326))

```lean
theorem cons_uncurry_swapAt_perm_cons : ∀ (xs : List α) (i : Nat) (v : α),
    List.cons.uncurry (swapAt xs i v) ~ v :: xs
```

`List.swap_perm` (theorem, [line 329](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L329))

```lean
theorem swap_perm : ∀ (xs : List α) (i j : Nat), xs.swap i j ~ xs
```

`List.mem_swap` (theorem, [line 337](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L337))

```lean
theorem mem_swap {xs : List α} (i j : Nat) {a : α} : a ∈ xs.swap i j ↔ a ∈ xs
```

> ### idxInj

`List.Subperm.idxInj` (definition, [line 350](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L350))

> `Subperm.idxInj` is an injective map from `Fin xs.length` to `Fin ys.length`
> which exists when we have `xs <+~ ys`: conceptually it represents an embedding of
> one list into the other. For example:
> ```
> (by decide : [1, 0, 1] <+~ [5, 0, 1, 3, 1]).idxInj 1 = 1
> ```

```lean
def Subperm.idxInj [BEq α] [ReflBEq α] {xs ys : List α} (h : xs <+~ ys) (i : Fin xs.length) :
    Fin ys.length
```

`List.coe_idxInj` (theorem, [line 356](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L356))

```lean
theorem coe_idxInj [BEq α] [ReflBEq α] {xs ys : List α} {h : xs <+~ ys}
    {i : Fin xs.length} :
    (h.idxInj i : Nat) = ys.idxOfNth xs[i] (xs.countBefore xs[i] i)
```

`List.Subperm.getElem_idxInj_eq_getElem` (theorem, [line 360](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L360))

```lean
theorem Subperm.getElem_idxInj_eq_getElem [BEq α] [LawfulBEq α] {xs ys : List α}
    (h : xs <+~ ys) {i : Fin xs.length} :
  ys[(h.idxInj i : Nat)] = xs[(i : Nat)]
```

`List.Subperm.idxInj_injective` (theorem, [line 364](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L364))

```lean
theorem Subperm.idxInj_injective [BEq α] [LawfulBEq α] {xs ys : List α}
    (h : xs <+~ ys) : h.idxInj.Injective
```

`List.Subperm.idxInj_inj` (theorem, [line 370](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L370))

```lean
theorem Subperm.idxInj_inj [BEq α] [LawfulBEq α] {xs ys : List α}
    {h : xs <+~ ys} (i j : Fin xs.length) :
  h.idxInj i = h.idxInj j ↔ i = j
```

> ### idxBij

`List.Perm.idxBij` (definition, [line 383](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L383))

> `Perm.idxBij` is a bijective map from `Fin xs.length` to `Fin ys.length`
> which exists when we have `xs.Perm ys`: conceptually it represents a permuting of
> one list into the other. For example:
> ```
> (by decide : [0, 1, 1, 3, 5] ~ [5, 0, 1, 3, 1]).idxBij 2 = 4
> ```

```lean
def Perm.idxBij [BEq α] [ReflBEq α] {xs ys : List α} (h : xs ~ ys) :
    Fin xs.length → Fin ys.length
```

`List.Perm.subperm_idxBij` (theorem, [line 387](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L387))

```lean
theorem Perm.subperm_idxBij [BEq α] [ReflBEq α] {xs ys : List α} (h : xs ~ ys) :
    h.subperm.idxInj = h.idxBij
```

`List.Perm.coe_idxBij` (theorem, [line 391](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L391))

```lean
theorem Perm.coe_idxBij [BEq α] [ReflBEq α] {xs ys : List α} (h : xs ~ ys)
    {i : Fin xs.length} : (h.idxBij i : Nat) = ys.idxOfNth xs[i] (xs.countBefore xs[i] i)
```

`List.Perm.getElem_idxBij_eq_getElem` (theorem, [line 394](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L394))

```lean
theorem Perm.getElem_idxBij_eq_getElem [BEq α] [LawfulBEq α] {xs ys : List α}
    (hxy : xs.Perm ys) (i : Fin xs.length) : ys[(hxy.idxBij i : Nat)] = xs[(i : Nat)]
```

`List.Perm.getElem_idxBij_symm_eq_getElem` (theorem, [line 398](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L398))

```lean
theorem Perm.getElem_idxBij_symm_eq_getElem [BEq α] [LawfulBEq α] {xs ys : List α}
    (hxy : xs.Perm ys) (i : Fin ys.length) : xs[(hxy.symm.idxBij i : Nat)] = ys[(i : Nat)]
```

`List.Perm.idxBij_leftInverse_idxBij_symm` (theorem, [line 402](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L402))

```lean
theorem Perm.idxBij_leftInverse_idxBij_symm [BEq α] [LawfulBEq α] {xs ys : List α} (h : xs ~ ys) :
    h.idxBij.LeftInverse h.symm.idxBij
```

`List.Perm.idxBij_rightInverse_idxBij_symm` (theorem, [line 405](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L405))

```lean
theorem Perm.idxBij_rightInverse_idxBij_symm [BEq α] [LawfulBEq α] {xs ys : List α} (h : xs ~ ys) :
    h.idxBij.RightInverse h.symm.idxBij
```

`List.Perm.idxBij_symm_rightInverse_idxBij` (theorem, [line 408](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L408))

```lean
theorem Perm.idxBij_symm_rightInverse_idxBij [BEq α] [LawfulBEq α] {xs ys : List α} (h : xs ~ ys) :
    h.symm.idxBij.RightInverse h.idxBij
```

`List.Perm.idxBij_symm_leftInverse_idxBij` (theorem, [line 411](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L411))

```lean
theorem Perm.idxBij_symm_leftInverse_idxBij [BEq α] [LawfulBEq α] {xs ys : List α} (h : xs ~ ys) :
    h.symm.idxBij.LeftInverse h.idxBij
```

`List.Perm.idxBij_idxBij_symm` (theorem, [line 414](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L414))

```lean
theorem Perm.idxBij_idxBij_symm [BEq α] [LawfulBEq α] {xs ys : List α} (h : xs ~ ys)
    {i : Fin ys.length} : h.idxBij (h.symm.idxBij i) = i
```

`List.Perm.idxBij_symm_idxBij` (theorem, [line 417](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L417))

```lean
theorem Perm.idxBij_symm_idxBij [BEq α] [LawfulBEq α] {xs ys : List α} (h : xs ~ ys)
    {i : Fin xs.length} : h.symm.idxBij (h.idxBij i) = i
```

`List.Perm.idxBij_injective` (theorem, [line 420](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L420))

```lean
theorem Perm.idxBij_injective [BEq α] [LawfulBEq α] {xs ys : List α} (h : xs ~ ys) :
    h.idxBij.Injective
```

`List.Perm.idxBij_surjective` (theorem, [line 423](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean#L423))

```lean
theorem Perm.idxBij_surjective [BEq α] [LawfulBEq α] {xs ys : List α} (h : xs ~ ys) :
    h.idxBij.Surjective
```

## Depends on

- [List/Basic](basic.md)

## Proof depends on

- [List/Lemmas](lemmas.md)

## Sources

- [Batteries/Data/List/Perm.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Perm.lean)
- [Declaration ledger](../../../../../../sources/batteries/Batteries.Data.List.Perm.json)
