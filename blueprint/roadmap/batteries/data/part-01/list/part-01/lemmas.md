---
catalog: module
lean: List.instNeZeroNatLengthCons, List.isEmpty_append, List.count_getElem_take_succ, List.count_getElem_take_lt_count, List.any_congr_mem, List.find?_zipIdx, List.next?_nil, List.next?_cons, List.dropLast_eq_eraseIdx, List.set_eq_modify, List.set_eq_take_cons_drop, List.modify_eq_set_getElem?, List.modify_eq_set_get, List.getElem?_set_eq_of_lt, List.getElem?_set_of_lt, List.getElem?_set_of_lt', List.length_tail_add_one, List.extractP_eq_find?_eraseP, List.erase_eq_self_iff_forall_bne, List.replaceF_nil, List.replaceF_cons, List.replaceF_cons_of_some, List.replaceF_cons_of_none, List.replaceF_of_forall_none, List.exists_of_replaceF, List.exists_or_eq_self_of_replaceF, List.length_replaceF, List.disjoint_symm, List.disjoint_comm, List.disjoint_left, List.disjoint_right, List.disjoint_iff_ne, List.disjoint_of_subset_left, List.disjoint_of_subset_right, List.disjoint_of_disjoint_cons_left, List.disjoint_of_disjoint_cons_right, List.disjoint_nil_left, List.disjoint_nil_right, List.singleton_disjoint, List.disjoint_singleton, List.disjoint_append_left, List.disjoint_append_right, List.disjoint_cons_left, List.disjoint_cons_right, List.disjoint_of_disjoint_append_left_left, List.disjoint_of_disjoint_append_left_right, List.disjoint_of_disjoint_append_right_left, List.disjoint_of_disjoint_append_right_right, List.union_def, List.nil_union, List.cons_union, List.mem_union_iff, List.inter_def, List.mem_inter_iff, List.pair_mem_product, List.forIn_eq_bindList, List.mapM_eq_ok_iff_forall₂, List.exists_mapM_eq_ok_iff, List.mapM_eq_error_iff, List.mapM_eq_some_iff_forall₂, List.exists_mapM_eq_some_iff, List.isSome_mapM, List.mapM_eq_none_iff, List.allSome_eq_some_iff_forall₂, List.exists_allSome_eq_some_iff, List.isSome_allSome, List.allSome_eq_none_iff, List.diff_nil, List.diff_cons, List.diff_cons_right, List.diff_erase, List.nil_diff, List.cons_diff, List.cons_diff_of_mem, List.cons_diff_of_not_mem, List.diff_eq_foldl, List.diff_append, List.diff_sublist, List.diff_subset, List.mem_diff_of_mem, List.Sublist.diff_right, List.Sublist.erase_diff_erase_sublist, List.disjoint_take_drop, List.pairwise_cons_cons, List.Pairwise.isChain, List.rel_of_isChain_cons_cons, List.IsChain.rel, List.isChain_of_isChain_cons, List.IsChain.of_cons, List.isChain_cons_of_isChain_cons_cons, List.isChain_of_isChain_cons_cons, List.IsChain.imp, List.IsChain.cons_of_imp, List.IsChain.cons_of_imp_of_cons, List.IsChain.cons_of_imp_of_imp, List.isChain_iff_pairwise, List.IsChain.pairwise, List.isChain_iff_getElem, List.IsChain.getElem, List.isChain_range', List.isChain_lt_range', List.filterMap_range_getElem?, List.foldrIdx_nil, List.foldrIdx_cons, List.foldrIdx_start, List.foldrIdx_const, List.foldrIdx_eq_foldr_zipIdx, List.foldlIdx_nil, List.foldlIdx_cons, List.foldlIdx_start, List.foldlIdx_const, List.foldlIdx_eq_foldl_zipIdx, List.findIdxs_nil, List.findIdxs_cons, List.findIdxs_singleton, List.findIdxs_start, List.findIdxs_eq_filterMap_zipIdx, List.mem_findIdxs_iff_getElem_sub_pos, List.mem_findIdxs_iff_exists_getElem_pos, List.mem_findIdxs_iff_pos_getElem, List.ge_of_mem_findIdxs, List.lt_add_of_mem_findIdxs, List.findIdxs_eq_nil_iff, List.length_findIdxs, List.pairwise_findIdxs, List.isChain_findIdxs, List.nodup_findIdxs, List.findIdxs_map, List.findIdxs_append, List.findIdxs_take, List.le_getElem_findIdxs, List.getElem_findIdxs_lt, List.getElem_filter_eq_getElem_getElem_findIdxs_sub, List.getElem_filter_eq_getElem_getElem_findIdxs, List.getElem_getElem_findIdxs_sub, List.getElem_getElem_findIdxs, List.getElem_zero_findIdxs_eq_findIdx_add, List.getElem_zero_findIdxs_eq_findIdx, List.findIdx_add_mem_findIdxs, List.findIdx_mem_findIdxs, List.findIdxsValues_eq_zip_filter_findIdxs, List.unzip_findIdxsValues, List.findIdxNth_nil, List.findIdxNth_cons, List.findIdxNth_cons_zero, List.findIdxNth_cons_succ, List.findIdxNth_cons_of_neg, List.findIdxNth_cons_of_pos, List.findIdxNth_cons_zero_of_pos, List.findIdxNth_cons_succ_of_pos, List.getElem_findIdxs_eq_findIdxNth_add, List.getElem_findIdxs_eq_findIdxNth, List.pos_findIdxNth_getElem, List.findIdxNth_zero, List.findIdxNth_lt_length_iff, List.findIdxNth_eq_length_iff, List.findIdxNth_le_length, List.findIdxNth_lt_length_of_lt_countP, List.findIdxNth_eq_length_of_ge_countP, List.findIdxNth_le_findIdxNth_iff, List.findIdxNth_lt_findIdxNth_iff, List.findIdxNth_eq_findIdxNth_iff, List.findIdxNth_lt_findIdxNth_iff_of_lt_countP, List.findIdxNth_mono, List.findIdxNth_eq_findIdxNth_iff_of_left_lt_countP, List.findIdxNth_eq_findIdxNth_iff_of_right_lt_countP, List.findIdxNth_eq_findIdxNth_of_ge_countP_ge_countP, List.eraseIdx_idxOf_eq_erase, List.idxOf_eq_getD_idxOf?, List.idxsOf_nil, List.idxsOf_cons, List.idxsOf_start, List.idxsOf_eq_filterMap_zipIdx, List.mem_idxsOf_iff_getElem_sub_pos, List.mem_idxsOf_iff_exists_getElem_pos, List.mem_idxsOf_iff_getElem_pos, List.ge_of_mem_idxsOf, List.lt_add_of_mem_idxsOf, List.idxsOf_eq_nil_iff, List.length_idxsOf, List.pairwise_idxsOf, List.isChain_idxsOf, List.nodup_idxsOf, List.idxsOf_map, List.idxsOf_append, List.idxsOf_take, List.le_getElem_idxsOf, List.getElem_idxsOf_lt, List.getElem_getElem_idxsOf_sub, List.getElem_getElem_idxsOf_sub_of_lawful, List.getElem_getElem_idxsOf, List.getElem_getElem_idxsOf_of_lawful, List.mem_idxsOf_getElem, List.getElem_zero_idxsOf_eq_idxOf_add, List.getElem_zero_idxsOf_eq_idxOf, List.idxOf_add_mem_idxsOf, List.idxOf_mem_idxsOf, List.idxOfNth_nil, List.idxOfNth_cons, List.idxOfNth_cons_zero, List.idxOfNth_cons_succ, List.idxOfNth_cons_of_not_beq, List.idxOfNth_cons_of_beq, List.idxOfNth_cons_zero_of_beq, List.idxOfNth_cons_succ_of_beq, List.getElem_idxOf_eq_idxOfNth_add, List.getElem_idxOf_eq_idxOfNth, List.getElem_idxOfNth_beq, List.getElem_idxOfNth_eq, List.idxOfNth_zero, List.idxOfNth_lt_length_iff, List.idxOfNth_eq_length_iff, List.idxOfNth_le_length, List.idxOfNth_lt_length_of_lt_count, List.idxOfNth_eq_length_of_ge_count, List.idxOfNth_lt_idxOfNth_iff, List.idxOfNth_eq_idxOfNth_iff, List.idxOfNth_lt_idxOfNth_iff_of_lt_count, List.idxOfNth_mono, List.idxOfNth_eq_idxOfNth_iff_of_left_lt_count, List.idxOfNth_eq_idxOfNth_iff_of_right_lt_count, List.idxOfNth_eq_idxOfNth_of_ge_countP_ge_countP, List.countPBefore_nil, List.countPBefore_cons, List.countPBefore_cons_zero, List.countPBefore_cons_succ, List.countPBefore_zero, List.countPBefore_succ, List.countPBefore_cons_succ_of_neg, List.countPBefore_cons_succ_of_pos, List.countPBefore_eq_countP_take, List.countPBefore_of_ge_length, List.countPBefore_length, List.findIdxNth_countPBefore_of_lt_length_of_pos, List.countPBefore_findIdxNth_of_lt_countP, List.pos_iff_exists_findIdxNth, List.countPBefore_le_countP, List.countPBefore_mono, List.countPBefore_lt_countP_of_lt_length_of_pos, List.countBefore_nil, List.countBefore_cons, List.countBefore_zero, List.countBefore_cons_succ, List.countBefore_cons_succ_of_not_beq, List.countBefore_cons_succ_of_beq, List.countBefore_eq_count_take, List.countBefore_idxOfNth_of_lt_count, List.idxOfNth_countBefore_of_lt_length_of_beq, List.idxOfNth_countBefore_getElem, List.beq_iff_exists_findIdxNth, List.countBefore_le_count, List.countBefore_lt_count_of_lt_length_of_beq, List.countBefore_lt_count_getElem, List.countBefore_of_ge_length, List.insertP_loop, List.insertP_nil, List.insertP_cons_pos, List.insertP_cons_neg, List.length_insertP, List.mem_insertP, List.dropPrefix?_nil, List.dropPrefix?_eq_some_iff, List.dropPrefix?_append_of_beq, List.dropSuffix?_eq_some_iff, List.dropSuffix?_nil, List.dropInfix?_go_eq_some_iff, List.dropInfix?_eq_some_iff, List.dropInfix?_nil, List.isSome_isPrefixOf?_eq_isPrefixOf, List.isPrefixOf?_eq_some_iff_append_eq, List.append_eq_of_isPrefixOf?_eq_some, List.isSome_isSuffixOf?_eq_isSuffixOf, List.isSuffixOf?_eq_some_iff_append_eq, List.append_eq_of_isSuffixOf?_eq_some, List.get_finRange, List.finRange_eq_nil_iff, List.finRange_eq_pmap_range, List.map_get_finRange, List.map_getElem_finRange, List.map_coe_finRange_eq_range, List.prod_one_cons, List.prod_pair, List.prod_concat, List.prod_flatten, List.sum_zero_cons, List.sum_pair, List.sum_concat, List.sum_flatten, List.take_succ_drop, List.max!_eq_max?_getD, List.max!_eq_max_of_ne_nil, List.max!_nil, List.min!_eq_min?_getD, List.min!_eq_min_of_ne_nil, List.min!_nil, List.swapAt_def, List.swap_nil, List.swap_cons, List.swap_cons_zero_left, List.swap_cons_zero_right, List.swap_eq, List.swap_eq_of_ge_left, List.swap_eq_of_ge_right, List.swap_eq_of_lt, List.swap_self, List.swap_comm, List.length_swap, List.getElem_swap_left, List.getElem_swap_right, List.getElem_swap_of_ne, List.getElem_swap_left_of_lt, List.getElem_swap_right_of_lt, List.getElem_swap, List.swap_swap, List.swap_swap_flip
statement: formalized
proof: formalized
---

# List/Lemmas

`Batteries.Data.List.Lemmas`, in [Batteries/Data/List/Lemmas.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean), by Parikshit Khanna, Jeremy Avigad, Leonardo de Moura, Floris van Doorn, Mario Carneiro.

`List.instNeZeroNatLengthCons` (instance, [line 17](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L17))

```lean
instance instNeZeroNatLengthCons {a : α} {l : List α} : NeZero (a :: l).length
```

> ### isEmpty

`List.isEmpty_append` (theorem, [line 22](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L22))

```lean
theorem isEmpty_append {xs ys : List α} :
    (xs ++ ys).isEmpty = (xs.isEmpty && ys.isEmpty)
```

> ### count

`List.count_getElem_take_succ` (theorem, [line 28](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L28))

```lean
theorem count_getElem_take_succ [BEq α] [EquivBEq α] {xs : List α}
    {i : Nat} {hi} : (xs.take (i + 1)).count xs[i] = (xs.take i).count xs[i] + 1
```

`List.count_getElem_take_lt_count` (theorem, [line 32](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L32))

```lean
theorem count_getElem_take_lt_count [BEq α] [EquivBEq α] {xs : List α}
    {i : Nat} {hi} : (xs.take i).count (xs[i]'hi) < xs.count xs[i]
```

> ### any

`List.any_congr_mem` (theorem, [line 39](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L39))

```lean
theorem any_congr_mem {xs : List α} {p q : α → Bool} (h : ∀ a ∈ xs, p a = q a) :
    xs.any p = xs.any q
```

> ### zip

> ### zipIdx

`List.find?_zipIdx` (theorem, [line 51](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L51))

```lean
theorem find?_zipIdx {xs : List α} {p : α → Bool} {k : Nat} :
    (xs.zipIdx k).find? (fun ⟨x, _⟩ => p x) =
      (xs.findIdx? p).bind fun i => xs[i]?.map (·, i + k)
```

> ### next?

`List.next?_nil` (theorem, [line 64](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L64))

```lean
theorem next?_nil : @next? α [] = none
```

`List.next?_cons` (theorem, [line 65](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L65))

```lean
theorem next?_cons (a l) : @next? α (a :: l) = some (a, l)
```

> ### dropLast

`List.dropLast_eq_eraseIdx` (theorem, [line 69](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L69))

```lean
theorem dropLast_eq_eraseIdx {xs : List α} {i : Nat} (last_idx : i + 1 = xs.length) :
    xs.dropLast = List.eraseIdx xs i
```

> ### set

`List.set_eq_modify` (theorem, [line 76](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L76))

```lean
theorem set_eq_modify (a : α) : ∀ n (l : List α), l.set n a = l.modify n (fun _ => a)
```

`List.set_eq_take_cons_drop` (theorem, [line 81](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L81))

```lean
theorem set_eq_take_cons_drop (a : α) {n l} (h : n < length l) :
    set l n a = take n l ++ a :: drop (n + 1) l
```

`List.modify_eq_set_getElem?` (theorem, [line 85](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L85))

```lean
theorem modify_eq_set_getElem? (f : α → α) :
    ∀ n (l : List α), l.modify n f = ((fun a => l.set n (f a)) <$> l[n]?).getD l
```

`List.modify_eq_set_get` (theorem, [line 92](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L92))

```lean
theorem modify_eq_set_get (f : α → α) {n} {l : List α} (h) :
    l.modify n f = l.set n (f (l.get ⟨n, h⟩))
```

`List.getElem?_set_eq_of_lt` (theorem, [line 96](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L96))

```lean
theorem getElem?_set_eq_of_lt (a : α) {n} {l : List α} (h : n < length l) :
    (set l n a)[n]? = some a
```

`List.getElem?_set_of_lt` (theorem, [line 99](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L99))

```lean
theorem getElem?_set_of_lt (a : α) {m n} (l : List α) (h : n < length l) :
    (set l m a)[n]? = if m = n then some a else l[n]?
```

`List.getElem?_set_of_lt'` (theorem, [line 103](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L103))

```lean
theorem getElem?_set_of_lt' (a : α) {m n} (l : List α) (h : m < length l) :
    (set l m a)[n]? = if m = n then some a else l[n]?
```

> ### tail

`List.length_tail_add_one` (theorem, [line 109](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L109))

```lean
theorem length_tail_add_one (l : List α) (h : 0 < length l) :
    (length (tail l)) + 1 = length l
```

> ### eraseP

`List.extractP_eq_find?_eraseP` (theorem, [line 114](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L114))

```lean
theorem extractP_eq_find?_eraseP
    (l : List α) : extractP p l = (find? p l, eraseP p l)
```

> ### erase

`List.erase_eq_self_iff_forall_bne` (theorem, [line 123](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L123))

```lean
theorem erase_eq_self_iff_forall_bne [BEq α] (a : α) (xs : List α) :
    xs.erase a = xs ↔ ∀ (x : α), x ∈ xs → ¬x == a
```

> ### replaceF

`List.replaceF_nil` (theorem, [line 129](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L129))

```lean
theorem replaceF_nil : [].replaceF p = []
```

`List.replaceF_cons` (theorem, [line 131](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L131))

```lean
theorem replaceF_cons (a : α) (l : List α) :
    (a :: l).replaceF p = match p a with
      | none => a :: replaceF p l
      | some a' => a' :: l
```

`List.replaceF_cons_of_some` (theorem, [line 136](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L136))

```lean
theorem replaceF_cons_of_some {l : List α} (p) (h : p a = some a') :
    (a :: l).replaceF p = a' :: l
```

`List.replaceF_cons_of_none` (theorem, [line 140](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L140))

```lean
theorem replaceF_cons_of_none {l : List α} (p) (h : p a = none) :
    (a :: l).replaceF p = a :: l.replaceF p
```

`List.replaceF_of_forall_none` (theorem, [line 143](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L143))

```lean
theorem replaceF_of_forall_none {l : List α} (h : ∀ a, a ∈ l → p a = none) : l.replaceF p = l
```

`List.exists_of_replaceF` (theorem, [line 148](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L148))

```lean
theorem exists_of_replaceF : ∀ {l : List α} {a a'} (_ : a ∈ l) (_ : p a = some a'),
    ∃ a a' l₁ l₂,
      (∀ b ∈ l₁, p b = none) ∧ p a = some a' ∧ l = l₁ ++ a :: l₂ ∧ l.replaceF p = l₁ ++ a' :: l₂
```

`List.exists_or_eq_self_of_replaceF` (theorem, [line 162](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L162))

```lean
theorem exists_or_eq_self_of_replaceF (p) (l : List α) :
    l.replaceF p = l ∨ ∃ a a' l₁ l₂,
      (∀ b ∈ l₁, p b = none) ∧ p a = some a' ∧ l = l₁ ++ a :: l₂ ∧ l.replaceF p = l₁ ++ a' :: l₂
```

`List.length_replaceF` (theorem, [line 172](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L172))

```lean
theorem length_replaceF : length (replaceF f l) = length l
```

> ### disjoint

`List.disjoint_symm` (theorem, [line 177](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L177))

```lean
theorem disjoint_symm (d : Disjoint l₁ l₂) : Disjoint l₂ l₁
```

`List.disjoint_comm` (theorem, [line 179](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L179))

```lean
theorem disjoint_comm : Disjoint l₁ l₂ ↔ Disjoint l₂ l₁
```

`List.disjoint_left` (theorem, [line 181](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L181))

```lean
theorem disjoint_left : Disjoint l₁ l₂ ↔ ∀ ⦃a⦄, a ∈ l₁ → a ∉ l₂
```

`List.disjoint_right` (theorem, [line 183](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L183))

```lean
theorem disjoint_right : Disjoint l₁ l₂ ↔ ∀ ⦃a⦄, a ∈ l₂ → a ∉ l₁
```

`List.disjoint_iff_ne` (theorem, [line 185](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L185))

```lean
theorem disjoint_iff_ne : Disjoint l₁ l₂ ↔ ∀ a ∈ l₁, ∀ b ∈ l₂, a ≠ b
```

`List.disjoint_of_subset_left` (theorem, [line 188](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L188))

```lean
theorem disjoint_of_subset_left (ss : l₁ ⊆ l) (d : Disjoint l l₂) : Disjoint l₁ l₂
```

`List.disjoint_of_subset_right` (theorem, [line 191](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L191))

```lean
theorem disjoint_of_subset_right (ss : l₂ ⊆ l) (d : Disjoint l₁ l) : Disjoint l₁ l₂
```

`List.disjoint_of_disjoint_cons_left` (theorem, [line 194](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L194))

```lean
theorem disjoint_of_disjoint_cons_left {l₁ l₂} : Disjoint (a :: l₁) l₂ → Disjoint l₁ l₂
```

`List.disjoint_of_disjoint_cons_right` (theorem, [line 197](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L197))

```lean
theorem disjoint_of_disjoint_cons_right {l₁ l₂} : Disjoint l₁ (a :: l₂) → Disjoint l₁ l₂
```

`List.disjoint_nil_left` (theorem, [line 200](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L200))

```lean
theorem disjoint_nil_left (l : List α) : Disjoint [] l
```

`List.disjoint_nil_right` (theorem, [line 202](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L202))

```lean
theorem disjoint_nil_right (l : List α) : Disjoint l []
```

`List.singleton_disjoint` (theorem, [line 205](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L205))

```lean
theorem singleton_disjoint : Disjoint [a] l ↔ a ∉ l
```

`List.disjoint_singleton` (theorem, [line 207](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L207))

```lean
theorem disjoint_singleton : Disjoint l [a] ↔ a ∉ l
```

`List.disjoint_append_left` (theorem, [line 210](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L210))

```lean
theorem disjoint_append_left : Disjoint (l₁ ++ l₂) l ↔ Disjoint l₁ l ∧ Disjoint l₂ l
```

`List.disjoint_append_right` (theorem, [line 213](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L213))

```lean
theorem disjoint_append_right : Disjoint l (l₁ ++ l₂) ↔ Disjoint l l₁ ∧ Disjoint l l₂
```

`List.disjoint_cons_left` (theorem, [line 216](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L216))

```lean
theorem disjoint_cons_left : Disjoint (a::l₁) l₂ ↔ (a ∉ l₂) ∧ Disjoint l₁ l₂
```

`List.disjoint_cons_right` (theorem, [line 219](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L219))

```lean
theorem disjoint_cons_right : Disjoint l₁ (a :: l₂) ↔ (a ∉ l₁) ∧ Disjoint l₁ l₂
```

`List.disjoint_of_disjoint_append_left_left` (theorem, [line 222](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L222))

```lean
theorem disjoint_of_disjoint_append_left_left (d : Disjoint (l₁ ++ l₂) l) : Disjoint l₁ l
```

`List.disjoint_of_disjoint_append_left_right` (theorem, [line 225](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L225))

```lean
theorem disjoint_of_disjoint_append_left_right (d : Disjoint (l₁ ++ l₂) l) : Disjoint l₂ l
```

`List.disjoint_of_disjoint_append_right_left` (theorem, [line 228](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L228))

```lean
theorem disjoint_of_disjoint_append_right_left (d : Disjoint l (l₁ ++ l₂)) : Disjoint l l₁
```

`List.disjoint_of_disjoint_append_right_right` (theorem, [line 231](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L231))

```lean
theorem disjoint_of_disjoint_append_right_right (d : Disjoint l (l₁ ++ l₂)) : Disjoint l l₂
```

> ### union

`List.union_def` (theorem, [line 240](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L240))

```lean
theorem union_def (l₁ l₂ : List α)  : l₁ ∪ l₂ = foldr .insert l₂ l₁
```

`List.nil_union` (theorem, [line 242](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L242))

```lean
theorem nil_union (l : List α) : nil ∪ l = l
```

`List.cons_union` (theorem, [line 244](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L244))

```lean
theorem cons_union (a : α) (l₁ l₂ : List α) :
    (a :: l₁) ∪ l₂ = (l₁ ∪ l₂).insert a
```

`List.mem_union_iff` (theorem, [line 247](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L247))

```lean
theorem mem_union_iff [LawfulBEq α] {x : α} {l₁ l₂ : List α} :
    x ∈ l₁ ∪ l₂ ↔ x ∈ l₁ ∨ x ∈ l₂
```

> ### inter

`List.inter_def` (theorem, [line 254](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L254))

```lean
theorem inter_def [BEq α] (l₁ l₂ : List α)  : l₁ ∩ l₂ = filter (elem · l₂) l₁
```

`List.mem_inter_iff` (theorem, [line 256](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L256))

```lean
theorem mem_inter_iff [BEq α] [LawfulBEq α] {x : α} {l₁ l₂ : List α} :
    x ∈ l₁ ∩ l₂ ↔ x ∈ l₁ ∧ x ∈ l₂
```

> ### product

`List.pair_mem_product` (theorem, [line 264](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L264))

> List.prod satisfies a specification of cartesian product on lists.

```lean
theorem pair_mem_product {xs : List α} {ys : List β} {x : α} {y : β} :
    (x, y) ∈ product xs ys ↔ x ∈ xs ∧ y ∈ ys
```

> ### monadic operations

`List.forIn_eq_bindList` (theorem, [line 271](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L271))

```lean
theorem forIn_eq_bindList [Monad m] [LawfulMonad m]
    (f : α → β → m (ForInStep β)) (l : List α) (init : β) :
    forIn l init f = ForInStep.run <$> (ForInStep.yield init).bindList f l
```

`List.mapM_eq_ok_iff_forall₂` (theorem, [line 277](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L277))

```lean
theorem mapM_eq_ok_iff_forall₂ {f : α → Except ε β} {l : List α} {bs : List β} :
    l.mapM f = .ok bs ↔ Forall₂ (fun a b => f a = .ok b) l bs
```

`List.exists_mapM_eq_ok_iff` (theorem, [line 281](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L281))

```lean
theorem exists_mapM_eq_ok_iff {f : α → Except ε β} {l : List α} :
    (∃ bs, l.mapM f = .ok bs) ↔ ∀ a ∈ l, ∃ b, f a = .ok b
```

`List.mapM_eq_error_iff` (theorem, [line 287](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L287))

> `mapM f` fails with `e` iff some element `a` fails with `e` and every element before it
> succeeds; `a` is the first failing element, since `mapM` stops at the first error.

```lean
theorem mapM_eq_error_iff {f : α → Except ε β} {l : List α} {e : ε} :
    l.mapM f = .error e ↔
      ∃ l₁ a l₂, l = l₁ ++ a :: l₂ ∧ (∀ x ∈ l₁, ∃ b, f x = .ok b) ∧ f a = .error e
```

`List.mapM_eq_some_iff_forall₂` (theorem, [line 298](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L298))

```lean
theorem mapM_eq_some_iff_forall₂ {f : α → Option β} {l : List α} {bs : List β} :
    l.mapM f = some bs ↔ Forall₂ (fun a b => f a = some b) l bs
```

`List.exists_mapM_eq_some_iff` (theorem, [line 302](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L302))

```lean
theorem exists_mapM_eq_some_iff {f : α → Option β} {l : List α} :
    (∃ bs, l.mapM f = some bs) ↔ ∀ a ∈ l, ∃ b, f a = some b
```

`List.isSome_mapM` (theorem, [line 306](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L306))

```lean
theorem isSome_mapM {f : α → Option β} {l : List α} :
    (l.mapM f).isSome ↔ ∀ a ∈ l, (f a).isSome
```

`List.mapM_eq_none_iff` (theorem, [line 310](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L310))

```lean
theorem mapM_eq_none_iff {f : α → Option β} {l : List α} :
    l.mapM f = none ↔ ∃ a ∈ l, f a = none
```

`List.allSome_eq_some_iff_forall₂` (theorem, [line 314](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L314))

```lean
theorem allSome_eq_some_iff_forall₂ {l : List (Option α)} {as : List α} :
    l.allSome = some as ↔ Forall₂ (fun o a => o = some a) l as
```

`List.exists_allSome_eq_some_iff` (theorem, [line 318](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L318))

```lean
theorem exists_allSome_eq_some_iff {l : List (Option α)} :
    (∃ as, l.allSome = some as) ↔ ∀ o ∈ l, ∃ a, o = some a
```

`List.isSome_allSome` (theorem, [line 322](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L322))

```lean
theorem isSome_allSome {l : List (Option α)} : l.allSome.isSome ↔ ∀ o ∈ l, o.isSome
```

`List.allSome_eq_none_iff` (theorem, [line 325](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L325))

```lean
theorem allSome_eq_none_iff {l : List (Option α)} : l.allSome = none ↔ none ∈ l
```

> ### diff

`List.diff_nil` (theorem, [line 333](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L333))

```lean
theorem diff_nil (l : List α) : l.diff [] = l
```

`List.diff_cons` (theorem, [line 337](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L337))

```lean
theorem diff_cons (l₁ l₂ : List α) (a : α) : l₁.diff (a :: l₂) = (l₁.erase a).diff l₂
```

`List.diff_cons_right` (theorem, [line 340](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L340))

```lean
theorem diff_cons_right (l₁ l₂ : List α) (a : α) : l₁.diff (a :: l₂) = (l₁.diff l₂).erase a
```

`List.diff_erase` (theorem, [line 343](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L343))

```lean
theorem diff_erase (l₁ l₂ : List α) (a : α) : (l₁.diff l₂).erase a = (l₁.erase a).diff l₂
```

`List.nil_diff` (theorem, [line 346](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L346))

```lean
theorem nil_diff (l : List α) : [].diff l = []
```

`List.cons_diff` (theorem, [line 349](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L349))

```lean
theorem cons_diff (a : α) (l₁ l₂ : List α) :
    (a :: l₁).diff l₂ = if a ∈ l₂ then l₁.diff (l₂.erase a) else a :: l₁.diff l₂
```

`List.cons_diff_of_mem` (theorem, [line 360](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L360))

```lean
theorem cons_diff_of_mem {a : α} {l₂ : List α} (h : a ∈ l₂) (l₁ : List α) :
    (a :: l₁).diff l₂ = l₁.diff (l₂.erase a)
```

`List.cons_diff_of_not_mem` (theorem, [line 363](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L363))

```lean
theorem cons_diff_of_not_mem {a : α} {l₂ : List α} (h : a ∉ l₂) (l₁ : List α) :
    (a :: l₁).diff l₂ = a :: l₁.diff l₂
```

`List.diff_eq_foldl` (theorem, [line 366](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L366))

```lean
theorem diff_eq_foldl : ∀ l₁ l₂ : List α, l₁.diff l₂ = foldl List.erase l₁ l₂
```

`List.diff_append` (theorem, [line 370](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L370))

```lean
theorem diff_append (l₁ l₂ l₃ : List α) : l₁.diff (l₂ ++ l₃) = (l₁.diff l₂).diff l₃
```

`List.diff_sublist` (theorem, [line 373](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L373))

```lean
theorem diff_sublist : ∀ l₁ l₂ : List α, l₁.diff l₂ <+ l₁
  | _, [] => .refl _
  | l₁, a :: l₂ =>
    calc
      l₁.diff (a :: l₂) = (l₁.erase a).diff l₂
```

`List.diff_subset` (theorem, [line 381](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L381))

```lean
theorem diff_subset (l₁ l₂ : List α) : l₁.diff l₂ ⊆ l₁
```

`List.mem_diff_of_mem` (theorem, [line 383](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L383))

```lean
theorem mem_diff_of_mem {a : α} : ∀ {l₁ l₂ : List α}, a ∈ l₁ → a ∉ l₂ → a ∈ l₁.diff l₂
```

`List.Sublist.diff_right` (theorem, [line 389](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L389))

```lean
theorem Sublist.diff_right : ∀ {l₁ l₂ l₃ : List α}, l₁ <+ l₂ → l₁.diff l₃ <+ l₂.diff l₃
```

`List.Sublist.erase_diff_erase_sublist` (theorem, [line 393](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L393))

```lean
theorem Sublist.erase_diff_erase_sublist {a : α} :
    ∀ {l₁ l₂ : List α}, l₁ <+ l₂ → (l₂.erase a).diff (l₁.erase a) <+ l₂.diff l₁
```

> ### drop

`List.disjoint_take_drop` (theorem, [line 407](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L407))

```lean
theorem disjoint_take_drop : ∀ {l : List α}, l.Nodup → m ≤ n → Disjoint (l.take m) (l.drop n)
```

> ### Pairwise

`List.pairwise_cons_cons` (theorem, [line 421](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L421))

```lean
theorem pairwise_cons_cons :
    Pairwise R (a :: b :: l) ↔ R a b ∧ Pairwise R (a :: l) ∧ Pairwise R (b :: l)
```

`List.Pairwise.isChain` (theorem, [line 425](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L425))

```lean
protected theorem Pairwise.isChain (p : Pairwise R l) : IsChain R l
```

> ### IsChain

`List.rel_of_isChain_cons_cons` (theorem, [line 430](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L430))

```lean
theorem rel_of_isChain_cons_cons (p : IsChain R (a :: b :: l)) : R a b
```

`List.IsChain.rel` (alias, [line 433](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L433))

```lean
alias IsChain.rel
```

`List.isChain_of_isChain_cons` (theorem, [line 435](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L435))

```lean
theorem isChain_of_isChain_cons (p : IsChain R (b :: l)) : IsChain R l
```

`List.IsChain.of_cons` (alias, [line 437](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L437))

```lean
alias IsChain.of_cons
```

`List.isChain_cons_of_isChain_cons_cons` (theorem, [line 440](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L440))

```lean
theorem isChain_cons_of_isChain_cons_cons : IsChain R (a :: b :: l) →
    IsChain R (b :: l)
```

`List.isChain_of_isChain_cons_cons` (theorem, [line 444](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L444))

```lean
theorem isChain_of_isChain_cons_cons : IsChain R (a :: b :: l) →
    IsChain R l
```

`List.IsChain.imp` (theorem, [line 448](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L448))

```lean
theorem IsChain.imp (H : ∀ ⦃a b : α⦄, R a b → S a b)
    (p : IsChain R l) : IsChain S l
```

`List.IsChain.cons_of_imp` (theorem, [line 451](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L451))

```lean
theorem IsChain.cons_of_imp (h : ∀ c, R a c → R b c) :
    IsChain R (a :: l) → IsChain R (b :: l)
```

`List.IsChain.cons_of_imp_of_cons` (alias, [line 455](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L455))

```lean
alias IsChain.cons_of_imp_of_cons
```

`List.IsChain.cons_of_imp_of_imp` (theorem, [line 457](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L457))

```lean
theorem IsChain.cons_of_imp_of_imp (HRS : ∀ ⦃a b : α⦄, R a b → S a b)
    (Hab : ∀ ⦃c⦄, R a c → S b c) (h : IsChain R (a :: l)) : IsChain S (b :: l)
```

`List.isChain_iff_pairwise` (theorem, [line 461](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L461))

```lean
theorem isChain_iff_pairwise [Trans R R R] : IsChain R l ↔ Pairwise R l
```

`List.IsChain.pairwise` (theorem, [line 467](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L467))

```lean
protected theorem IsChain.pairwise [Trans R R R] (c : IsChain R l) :
    Pairwise R l
```

`List.isChain_iff_getElem` (theorem, [line 470](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L470))

```lean
theorem isChain_iff_getElem {l : List α} :
    IsChain R l ↔ ∀ (i : Nat) (_hi : i + 1 < l.length), R l[i] l[i + 1]
```

`List.IsChain.getElem` (theorem, [line 475](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L475))

```lean
theorem IsChain.getElem {l : List α} (c : IsChain R l) (i : Nat) (hi : i + 1 < l.length) :
    R l[i] l[i + 1]
```

> ### range', range

`List.isChain_range'` (theorem, [line 480](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L480))

```lean
theorem isChain_range' (s : Nat) : ∀ n step : Nat,
    IsChain (fun a b => b = a + step) (range' s n step)
```

`List.isChain_lt_range'` (theorem, [line 486](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L486))

```lean
theorem isChain_lt_range' (s n : Nat) (h : 0 < step) :
    IsChain (· < ·) (range' s n step)
```

`List.filterMap_range_getElem?` (theorem, [line 490](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L490))

```lean
theorem filterMap_range_getElem? {xs : List α} :
    (range xs.length).filterMap (xs[·]?) = xs
```

> ### foldrIdx

`List.foldrIdx_nil` (theorem, [line 500](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L500))

```lean
theorem foldrIdx_nil : ([] : List α).foldrIdx f i s = i
```

`List.foldrIdx_cons` (theorem, [line 502](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L502))

```lean
theorem foldrIdx_cons :
    (x :: xs : List α).foldrIdx f i s = f s x (foldrIdx f i xs (s + 1))
```

`List.foldrIdx_start` (theorem, [line 505](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L505))

```lean
theorem foldrIdx_start :
    (xs : List α).foldrIdx f i s = (xs : List α).foldrIdx (f <| · + s) i
```

`List.foldrIdx_const` (theorem, [line 509](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L509))

```lean
theorem foldrIdx_const : (xs : List α).foldrIdx (Function.const Nat f) i s = xs.foldr f i
```

`List.foldrIdx_eq_foldr_zipIdx` (theorem, [line 512](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L512))

```lean
theorem foldrIdx_eq_foldr_zipIdx : (xs : List α).foldrIdx f i s =
    (xs.zipIdx s).foldr (fun ab => f ab.2 ab.1) i
```

> ### foldlIdx

`List.foldlIdx_nil` (theorem, [line 518](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L518))

```lean
theorem foldlIdx_nil : ([] : List α).foldlIdx f i s = i
```

`List.foldlIdx_cons` (theorem, [line 520](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L520))

```lean
theorem foldlIdx_cons :
    (x :: xs : List α).foldlIdx f i s = foldlIdx f (f s i x) xs (s + 1)
```

`List.foldlIdx_start` (theorem, [line 523](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L523))

```lean
theorem foldlIdx_start :
    (xs : List α).foldlIdx f i s = (xs : List α).foldlIdx (f <| · + s) i
```

`List.foldlIdx_const` (theorem, [line 527](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L527))

```lean
theorem foldlIdx_const : (xs : List α).foldlIdx (Function.const Nat f) i s = xs.foldl f i
```

`List.foldlIdx_eq_foldl_zipIdx` (theorem, [line 530](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L530))

```lean
theorem foldlIdx_eq_foldl_zipIdx : (xs : List α).foldlIdx f i s =
    (xs.zipIdx s).foldl (fun b ab => f ab.2 b ab.1) i
```

> ### findIdxs

`List.findIdxs_nil` (theorem, [line 536](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L536))

```lean
theorem findIdxs_nil : ([] : List α).findIdxs p s = []
```

`List.findIdxs_cons` (theorem, [line 538](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L538))

```lean
theorem findIdxs_cons :
    (x :: xs : List α).findIdxs p s =
    if p x then s :: xs.findIdxs p (s + 1) else xs.findIdxs p (s + 1)
```

`List.findIdxs_singleton` (theorem, [line 543](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L543))

```lean
theorem findIdxs_singleton :
    [x].findIdxs p s = if p x then [s] else []
```

`List.findIdxs_start` (theorem, [line 546](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L546))

```lean
theorem findIdxs_start :
    (xs : List α).findIdxs p s = (xs.findIdxs p).map (· + s)
```

`List.findIdxs_eq_filterMap_zipIdx` (theorem, [line 550](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L550))

```lean
theorem findIdxs_eq_filterMap_zipIdx : (xs : List α).findIdxs p s =
    ((xs.zipIdx s).filterMap fun ab => bif p ab.1 then ab.2 else none)
```

`List.mem_findIdxs_iff_getElem_sub_pos` (theorem, [line 555](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L555))

```lean
theorem mem_findIdxs_iff_getElem_sub_pos :
    i ∈ (xs : List α).findIdxs p s ↔ s ≤ i ∧
    ∃ (hix : i - s < xs.length), p xs[i - s]
```

`List.mem_findIdxs_iff_exists_getElem_pos` (theorem, [line 560](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L560))

```lean
theorem mem_findIdxs_iff_exists_getElem_pos :
    i ∈ (xs : List α).findIdxs p ↔ ∃ (hix : i < xs.length), p xs[i]
```

`List.mem_findIdxs_iff_pos_getElem` (theorem, [line 563](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L563))

```lean
theorem mem_findIdxs_iff_pos_getElem (hi : i < (xs : List α).length) :
    i ∈ xs.findIdxs p ↔ p xs[i]
```

`List.ge_of_mem_findIdxs` (theorem, [line 566](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L566))

```lean
theorem ge_of_mem_findIdxs : ∀ y ∈ (xs : List α).findIdxs p s, s ≤ y
```

`List.lt_add_of_mem_findIdxs` (theorem, [line 568](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L568))

```lean
theorem lt_add_of_mem_findIdxs :
    ∀ y ∈ (xs : List α).findIdxs p s, y < xs.length + s
```

`List.findIdxs_eq_nil_iff` (theorem, [line 571](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L571))

```lean
theorem findIdxs_eq_nil_iff :
    (xs : List α).findIdxs p s = [] ↔ ∀ x ∈ xs, p x = false
```

`List.length_findIdxs` (theorem, [line 575](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L575))

```lean
theorem length_findIdxs : ((xs : List α).findIdxs p s).length = xs.countP p
```

`List.pairwise_findIdxs` (theorem, [line 579](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L579))

```lean
theorem pairwise_findIdxs : ((xs : List α).findIdxs p s).Pairwise (· < ·)
```

`List.isChain_findIdxs` (theorem, [line 583](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L583))

```lean
theorem isChain_findIdxs : ((xs : List α).findIdxs p s).IsChain (· < ·)
```

`List.nodup_findIdxs` (theorem, [line 587](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L587))

```lean
theorem nodup_findIdxs : ((xs : List α).findIdxs p s).Nodup
```

`List.findIdxs_map` (theorem, [line 590](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L590))

```lean
theorem findIdxs_map :
    ((xs : List α).map f).findIdxs p s = xs.findIdxs (p ∘ f) s
```

`List.findIdxs_append` (theorem, [line 595](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L595))

```lean
theorem findIdxs_append :
    ((xs : List α) ++ ys).findIdxs p s = xs.findIdxs p s ++ ys.findIdxs p (s + xs.length)
```

`List.findIdxs_take` (theorem, [line 600](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L600))

```lean
theorem findIdxs_take :
    ((xs : List α).take n).findIdxs p s = (xs.findIdxs p s).take ((xs.take n).countP p)
```

`List.le_getElem_findIdxs` (theorem, [line 605](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L605))

```lean
theorem le_getElem_findIdxs (h : i < ((xs : List α).findIdxs p s).length) :
    s ≤ (xs.findIdxs p s)[i]
```

`List.getElem_findIdxs_lt` (theorem, [line 611](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L611))

```lean
theorem getElem_findIdxs_lt (h : i < ((xs : List α).findIdxs p s).length) :
    (xs.findIdxs p s)[i] < xs.length + s
```

`List.getElem_filter_eq_getElem_getElem_findIdxs_sub` (theorem, [line 616](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L616))

```lean
theorem getElem_filter_eq_getElem_getElem_findIdxs_sub (s : Nat)
    (h : i < ((xs : List α).filter p).length) :
    (xs.filter p)[i] = xs[(xs.findIdxs p s)[i]'(by grind) - s]'(by grind)
```

`List.getElem_filter_eq_getElem_getElem_findIdxs` (theorem, [line 621](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L621))

```lean
theorem getElem_filter_eq_getElem_getElem_findIdxs
    (h : i < ((xs : List α).filter p).length) :
    (xs.filter p)[i] = xs[(xs.findIdxs p)[i]'(by grind)]'(by grind)
```

`List.getElem_getElem_findIdxs_sub` (theorem, [line 628](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L628))

```lean
theorem getElem_getElem_findIdxs_sub (s : Nat)
    (h : i < ((xs : List α).findIdxs p s).length) :
    haveI : (findIdxs p xs s)[i] - s < xs.length := by grind
    p xs[(xs.findIdxs p s)[i] - s]
```

`List.getElem_getElem_findIdxs` (theorem, [line 634](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L634))

```lean
theorem getElem_getElem_findIdxs
    (h : i < ((xs : List α).findIdxs p).length) :
    haveI : (findIdxs p xs)[i] < xs.length := by grind
    p xs[(xs.findIdxs p)[i]]
```

`List.getElem_zero_findIdxs_eq_findIdx_add` (theorem, [line 640](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L640))

```lean
theorem getElem_zero_findIdxs_eq_findIdx_add (h : 0 < ((xs : List α).findIdxs p s).length) :
    (xs.findIdxs p s)[0] = xs.findIdx p + s
```

`List.getElem_zero_findIdxs_eq_findIdx` (theorem, [line 644](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L644))

```lean
theorem getElem_zero_findIdxs_eq_findIdx (h : 0 < ((xs : List α).findIdxs p).length) :
    (xs.findIdxs p)[0] = xs.findIdx p
```

`List.findIdx_add_mem_findIdxs` (theorem, [line 647](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L647))

```lean
theorem findIdx_add_mem_findIdxs (s : Nat)
    (h : (xs : List α).findIdx p < xs.length) : xs.findIdx p + s ∈ xs.findIdxs p s
```

`List.findIdx_mem_findIdxs` (theorem, [line 651](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L651))

```lean
theorem findIdx_mem_findIdxs (h : (xs : List α).findIdx p < xs.length) :
    xs.findIdx p ∈ xs.findIdxs p
```

> ### findIdxsValues

`List.findIdxsValues_eq_zip_filter_findIdxs` (theorem, [line 657](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L657))

```lean
theorem findIdxsValues_eq_zip_filter_findIdxs :
    (xs : List α).findIdxsValues p s = (xs.findIdxs p s).zip (xs.filter p)
```

`List.unzip_findIdxsValues` (theorem, [line 662](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L662))

```lean
theorem unzip_findIdxsValues :
    ((xs : List α).findIdxsValues p s).unzip = (xs.findIdxs p s, xs.filter p)
```

> ### findIdxNth

`List.findIdxNth_nil` (theorem, [line 668](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L668))

```lean
theorem findIdxNth_nil : ([] : List α).findIdxNth p n = 0
```

`List.findIdxNth_cons` (theorem, [line 671](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L671))

```lean
theorem findIdxNth_cons {a : α} :
    (a :: xs).findIdxNth p n =
    if n = 0 then if p a then 0 else xs.findIdxNth p 0 + 1
    else if p a then xs.findIdxNth p (n - 1) + 1
    else xs.findIdxNth p n + 1
```

`List.findIdxNth_cons_zero` (theorem, [line 680](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L680))

```lean
theorem findIdxNth_cons_zero {a : α} :
    (a :: xs).findIdxNth p 0 = if p a then 0 else xs.findIdxNth p 0 + 1
```

`List.findIdxNth_cons_succ` (theorem, [line 683](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L683))

```lean
theorem findIdxNth_cons_succ {a : α} :
    (a :: xs).findIdxNth p (n + 1) =
    if p a then xs.findIdxNth p n + 1 else xs.findIdxNth p (n + 1) + 1
```

`List.findIdxNth_cons_of_neg` (theorem, [line 687](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L687))

```lean
theorem findIdxNth_cons_of_neg {a : α} (h : p a = false) :
    (a :: xs).findIdxNth p n = xs.findIdxNth p n + 1
```

`List.findIdxNth_cons_of_pos` (theorem, [line 690](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L690))

```lean
theorem findIdxNth_cons_of_pos {a : α} (h : p a) :
    (a :: xs).findIdxNth p n = if n = 0 then 0 else
    xs.findIdxNth p (n - 1) + 1
```

`List.findIdxNth_cons_zero_of_pos` (theorem, [line 694](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L694))

```lean
theorem findIdxNth_cons_zero_of_pos {a : α} (h : p a) :
    (a :: xs).findIdxNth p 0 = 0
```

`List.findIdxNth_cons_succ_of_pos` (theorem, [line 697](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L697))

```lean
theorem findIdxNth_cons_succ_of_pos {a : α} (h : p a) :
    (a :: xs).findIdxNth p (n + 1) = xs.findIdxNth p n + 1
```

`List.getElem_findIdxs_eq_findIdxNth_add` (theorem, [line 700](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L700))

```lean
theorem getElem_findIdxs_eq_findIdxNth_add {xs : List α} {h : n < (xs.findIdxs p s).length} :
    (xs.findIdxs p s)[n] = xs.findIdxNth p n + s
```

`List.getElem_findIdxs_eq_findIdxNth` (theorem, [line 705](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L705))

```lean
theorem getElem_findIdxs_eq_findIdxNth {xs : List α} {h : n < (xs.findIdxs p).length} :
    (xs.findIdxs p)[n] = xs.findIdxNth p n
```

`List.pos_findIdxNth_getElem` (theorem, [line 708](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L708))

```lean
theorem pos_findIdxNth_getElem {xs : List α} {h : xs.findIdxNth p n < xs.length} :
    p xs[xs.findIdxNth p n]
```

`List.findIdxNth_zero` (theorem, [line 713](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L713))

```lean
theorem findIdxNth_zero : (xs : List α).findIdxNth p 0 = xs.findIdx p
```

`List.findIdxNth_lt_length_iff` (theorem, [line 717](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L717))

```lean
theorem findIdxNth_lt_length_iff {xs : List α} :
    xs.findIdxNth p n < xs.length ↔ n < xs.countP p
```

`List.findIdxNth_eq_length_iff` (theorem, [line 722](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L722))

```lean
theorem findIdxNth_eq_length_iff {xs : List α} :
    xs.findIdxNth p n = xs.length ↔ xs.countP p ≤ n
```

`List.findIdxNth_le_length` (theorem, [line 727](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L727))

```lean
theorem findIdxNth_le_length {xs : List α} :
    xs.findIdxNth p n ≤ xs.length
```

`List.findIdxNth_lt_length_of_lt_countP` (theorem, [line 730](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L730))

```lean
theorem findIdxNth_lt_length_of_lt_countP {xs : List α} (h : n < xs.countP p) :
    xs.findIdxNth p n < xs.length
```

`List.findIdxNth_eq_length_of_ge_countP` (theorem, [line 733](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L733))

```lean
theorem findIdxNth_eq_length_of_ge_countP {xs : List α} :
    xs.countP p ≤ n → xs.findIdxNth p n = xs.length
```

`List.findIdxNth_le_findIdxNth_iff` (theorem, [line 736](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L736))

```lean
theorem findIdxNth_le_findIdxNth_iff {xs : List α} :
    xs.findIdxNth p n ≤ xs.findIdxNth p m ↔ countP p xs ≤ m ∨ n ≤ m
```

`List.findIdxNth_lt_findIdxNth_iff` (theorem, [line 742](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L742))

```lean
theorem findIdxNth_lt_findIdxNth_iff {xs : List α} :
    xs.findIdxNth p n < xs.findIdxNth p m ↔ n < xs.countP p ∧ n < m
```

`List.findIdxNth_eq_findIdxNth_iff` (theorem, [line 746](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L746))

```lean
theorem findIdxNth_eq_findIdxNth_iff {xs : List α} :
    xs.findIdxNth p n = xs.findIdxNth p m ↔
    (xs.countP p ≤ m ∨ n ≤ m) ∧ (xs.countP p ≤ n ∨ m ≤ n)
```

`List.findIdxNth_lt_findIdxNth_iff_of_lt_countP` (theorem, [line 751](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L751))

```lean
theorem findIdxNth_lt_findIdxNth_iff_of_lt_countP {xs : List α} (hn : n < xs.countP p) :
    xs.findIdxNth p n < xs.findIdxNth p m ↔ n < m
```

`List.findIdxNth_mono` (theorem, [line 755](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L755))

```lean
theorem findIdxNth_mono {xs : List α} (hnm : n ≤ m):
    xs.findIdxNth p n ≤ xs.findIdxNth p m
```

`List.findIdxNth_eq_findIdxNth_iff_of_left_lt_countP` (theorem, [line 759](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L759))

```lean
theorem findIdxNth_eq_findIdxNth_iff_of_left_lt_countP {xs : List α} (hn : n < xs.countP p) :
    xs.findIdxNth p n = xs.findIdxNth p m ↔ n = m
```

`List.findIdxNth_eq_findIdxNth_iff_of_right_lt_countP` (theorem, [line 763](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L763))

```lean
theorem findIdxNth_eq_findIdxNth_iff_of_right_lt_countP {xs : List α} (hm : m < xs.countP p) :
    xs.findIdxNth p n = xs.findIdxNth p m ↔ n = m
```

`List.findIdxNth_eq_findIdxNth_of_ge_countP_ge_countP` (theorem, [line 767](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L767))

```lean
theorem findIdxNth_eq_findIdxNth_of_ge_countP_ge_countP {xs : List α} (hn : xs.countP p ≤ n)
    (hm : xs.countP p ≤ m) : xs.findIdxNth p n = xs.findIdxNth p m
```

> ### idxOf

`List.eraseIdx_idxOf_eq_erase` (theorem, [line 773](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L773))

```lean
theorem eraseIdx_idxOf_eq_erase [BEq α] (a : α) (l : List α) :
    l.eraseIdx (l.idxOf a) = l.erase a
```

`List.idxOf_eq_getD_idxOf?` (theorem, [line 777](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L777))

```lean
theorem idxOf_eq_getD_idxOf? [BEq α] (a : α) (l : List α) :
    l.idxOf a = (l.idxOf? a).getD l.length
```

> ### idxsOf

`List.idxsOf_nil` (theorem, [line 783](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L783))

```lean
theorem idxsOf_nil [BEq α] : ([] : List α).idxsOf x s = []
```

`List.idxsOf_cons` (theorem, [line 785](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L785))

```lean
theorem idxsOf_cons [BEq α] : (x :: xs : List α).idxsOf y s =
    if x == y then s :: xs.idxsOf y (s + 1) else xs.idxsOf y (s + 1)
```

`List.idxsOf_start` (theorem, [line 788](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L788))

```lean
theorem idxsOf_start [BEq α] :
    (xs : List α).idxsOf x s = (xs.idxsOf x).map (· + s)
```

`List.idxsOf_eq_filterMap_zipIdx` (theorem, [line 791](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L791))

```lean
theorem idxsOf_eq_filterMap_zipIdx [BEq α] : (xs : List α).idxsOf x s =
    ((xs.zipIdx s).filterMap fun ab => bif ab.1 == x then ab.2 else none)
```

`List.mem_idxsOf_iff_getElem_sub_pos` (theorem, [line 796](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L796))

```lean
theorem mem_idxsOf_iff_getElem_sub_pos [BEq α] :
    i ∈ (xs : List α).idxsOf x s ↔ s ≤ i ∧
    ∃ (hix : i - s < xs.length), xs[i - s] == x
```

`List.mem_idxsOf_iff_exists_getElem_pos` (theorem, [line 800](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L800))

```lean
theorem mem_idxsOf_iff_exists_getElem_pos [BEq α] :
    i ∈ (xs : List α).idxsOf x ↔ ∃ (hix : i < xs.length), xs[i] == x
```

`List.mem_idxsOf_iff_getElem_pos` (theorem, [line 803](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L803))

```lean
theorem mem_idxsOf_iff_getElem_pos [BEq α] (hi : i < (xs : List α).length) :
    i ∈ xs.idxsOf x ↔ xs[i] == x
```

`List.ge_of_mem_idxsOf` (theorem, [line 806](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L806))

```lean
theorem ge_of_mem_idxsOf [BEq α] : ∀ y ∈ (xs : List α).idxsOf x s, s ≤ y
```

`List.lt_add_of_mem_idxsOf` (theorem, [line 808](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L808))

```lean
theorem lt_add_of_mem_idxsOf [BEq α] :
    ∀ y ∈ (xs : List α).idxsOf x s, y < xs.length + s
```

`List.idxsOf_eq_nil_iff` (theorem, [line 811](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L811))

```lean
theorem idxsOf_eq_nil_iff [BEq α] :
    (xs : List α).idxsOf x s = [] ↔ ∀ y ∈ xs, (y == x) = false
```

`List.length_idxsOf` (theorem, [line 814](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L814))

```lean
theorem length_idxsOf [BEq α] :
    ((xs : List α).idxsOf x s).length = xs.count x
```

`List.pairwise_idxsOf` (theorem, [line 818](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L818))

```lean
theorem pairwise_idxsOf [BEq α] : ((xs : List α).idxsOf x s).Pairwise (· < ·)
```

`List.isChain_idxsOf` (theorem, [line 822](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L822))

```lean
theorem isChain_idxsOf [BEq α] : ((xs : List α).idxsOf x s).IsChain (· < ·)
```

`List.nodup_idxsOf` (theorem, [line 826](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L826))

```lean
theorem nodup_idxsOf [BEq α] : ((xs : List α).idxsOf x s).Nodup
```

`List.idxsOf_map` (theorem, [line 830](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L830))

```lean
theorem idxsOf_map [BEq α] {f : β → α} :
    ((xs : List β).map f).idxsOf x s = xs.findIdxs (f · == x) s
```

`List.idxsOf_append` (theorem, [line 834](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L834))

```lean
theorem idxsOf_append [BEq α] :
    ((xs : List α) ++ ys).idxsOf x s = xs.idxsOf x s ++ ys.idxsOf x (s + xs.length)
```

`List.idxsOf_take` (theorem, [line 839](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L839))

```lean
theorem idxsOf_take [BEq α] :
    ((xs : List α).take n).idxsOf x s = (xs.idxsOf x s).take ((xs.take n).count x)
```

`List.le_getElem_idxsOf` (theorem, [line 844](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L844))

```lean
theorem le_getElem_idxsOf [BEq α] (h : i < ((xs : List α).idxsOf x s).length) :
    s ≤ (xs.idxsOf x s)[i]
```

`List.getElem_idxsOf_lt` (theorem, [line 848](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L848))

```lean
theorem getElem_idxsOf_lt [BEq α] (h : i < ((xs : List α).idxsOf x s).length) :
    (xs.idxsOf x s)[i] < xs.length + s
```

`List.getElem_getElem_idxsOf_sub` (theorem, [line 853](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L853))

```lean
theorem getElem_getElem_idxsOf_sub [BEq α] (s : Nat)
    (h : i < ((xs : List α).idxsOf x s).length) :
    haveI : (idxsOf x xs s)[i] - s < xs.length := by grind
    xs[(xs.idxsOf x s)[i] - s] == x
```

`List.getElem_getElem_idxsOf_sub_of_lawful` (theorem, [line 861](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L861))

```lean
theorem getElem_getElem_idxsOf_sub_of_lawful [BEq α] [LawfulBEq α] (s : Nat)
    (h : i < ((xs : List α).idxsOf x s).length) :
    haveI : (idxsOf x xs s)[i] - s < xs.length := by grind
    xs[(xs.idxsOf x s)[i] - s] = x
```

`List.getElem_getElem_idxsOf` (theorem, [line 866](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L866))

```lean
theorem getElem_getElem_idxsOf [BEq α] (h : i < ((xs : List α).idxsOf x).length) :
    haveI : (idxsOf x xs)[i] < xs.length := by grind
    xs[(xs.idxsOf x)[i]] == x
```

`List.getElem_getElem_idxsOf_of_lawful` (theorem, [line 871](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L871))

```lean
theorem getElem_getElem_idxsOf_of_lawful [BEq α] [LawfulBEq α]
    (h : i < ((xs : List α).idxsOf x).length) :
    haveI : (idxsOf x xs)[i] < xs.length := by grind
  xs[(xs.idxsOf x)[i]] = x
```

`List.mem_idxsOf_getElem` (theorem, [line 876](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L876))

```lean
theorem mem_idxsOf_getElem [BEq α] [EquivBEq α] (h : i < (xs : List α).length) :
    i ∈ xs.idxsOf xs[i]
```

`List.getElem_zero_idxsOf_eq_idxOf_add` (theorem, [line 882](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L882))

```lean
theorem getElem_zero_idxsOf_eq_idxOf_add [BEq α] (h : 0 < ((xs : List α).idxsOf x s).length) :
    (xs.idxsOf x s)[0] = xs.idxOf x + s
```

`List.getElem_zero_idxsOf_eq_idxOf` (theorem, [line 886](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L886))

```lean
theorem getElem_zero_idxsOf_eq_idxOf [BEq α] (h : 0 < ((xs : List α).idxsOf x).length) :
    (xs.idxsOf x)[0] = xs.idxOf x
```

`List.idxOf_add_mem_idxsOf` (theorem, [line 889](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L889))

```lean
theorem idxOf_add_mem_idxsOf [BEq α] (s : Nat) (h : (xs : List α).idxOf x < xs.length) :
    xs.idxOf x + s ∈ xs.idxsOf x s
```

`List.idxOf_mem_idxsOf` (theorem, [line 894](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L894))

```lean
theorem idxOf_mem_idxsOf [BEq α] (h : (xs : List α).idxOf x < xs.length) :
    xs.idxOf x ∈ xs.idxsOf x
```

> ### idxOfNth

`List.idxOfNth_nil` (theorem, [line 899](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L899))

```lean
theorem idxOfNth_nil [BEq α] : ([] : List α).idxOfNth x n = 0
```

`List.idxOfNth_cons` (theorem, [line 902](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L902))

```lean
theorem idxOfNth_cons [BEq α] {a : α} :
    (a :: xs).idxOfNth x n =
    if n = 0 then if a == x then 0 else xs.idxOfNth x 0 + 1
    else if a == x then xs.idxOfNth x (n - 1) + 1
    else xs.idxOfNth x n + 1
```

`List.idxOfNth_cons_zero` (theorem, [line 908](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L908))

```lean
theorem idxOfNth_cons_zero [BEq α] {a : α} :
    (a :: xs).idxOfNth x 0 = if a == x then 0 else xs.idxOfNth x 0 + 1
```

`List.idxOfNth_cons_succ` (theorem, [line 911](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L911))

```lean
theorem idxOfNth_cons_succ [BEq α] {a : α} :
    (a :: xs).idxOfNth x (n + 1) =
    if a == x then xs.idxOfNth x n + 1
    else xs.idxOfNth x (n + 1) + 1
```

`List.idxOfNth_cons_of_not_beq` (theorem, [line 916](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L916))

```lean
theorem idxOfNth_cons_of_not_beq {a : α} [BEq α] (h : (a == x) = false) :
    (a :: xs).idxOfNth x n = xs.idxOfNth x n + 1
```

`List.idxOfNth_cons_of_beq` (theorem, [line 919](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L919))

```lean
theorem idxOfNth_cons_of_beq {a : α} [BEq α] (h : a == x) :
    (a :: xs).idxOfNth x n = if n = 0 then 0 else xs.idxOfNth x (n - 1) + 1
```

`List.idxOfNth_cons_zero_of_beq` (theorem, [line 922](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L922))

```lean
theorem idxOfNth_cons_zero_of_beq {a : α} [BEq α] (h : a == x) :
    (a :: xs).idxOfNth x 0 = 0
```

`List.idxOfNth_cons_succ_of_beq` (theorem, [line 925](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L925))

```lean
theorem idxOfNth_cons_succ_of_beq {a : α} [BEq α] (h : a == x) :
    (a :: xs).idxOfNth x (n + 1) = xs.idxOfNth x n + 1
```

`List.getElem_idxOf_eq_idxOfNth_add` (theorem, [line 928](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L928))

```lean
theorem getElem_idxOf_eq_idxOfNth_add {xs : List α} [BEq α] {h : n < (xs.idxsOf x s).length} :
    (xs.idxsOf x s)[n] = xs.idxOfNth x n + s
```

`List.getElem_idxOf_eq_idxOfNth` (theorem, [line 933](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L933))

```lean
theorem getElem_idxOf_eq_idxOfNth {xs : List α} [BEq α] {h : n < (xs.idxsOf x).length} :
    (xs.idxsOf x)[n] = xs.idxOfNth x n
```

`List.getElem_idxOfNth_beq` (theorem, [line 936](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L936))

```lean
theorem getElem_idxOfNth_beq {xs : List α} [BEq α] {h : xs.idxOfNth x n < xs.length} :
    xs[xs.idxOfNth x n] == x
```

`List.getElem_idxOfNth_eq` (theorem, [line 942](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L942))

```lean
theorem getElem_idxOfNth_eq {xs : List α} [BEq α] [LawfulBEq α] {h : xs.idxOfNth x n < xs.length} :
    xs[xs.idxOfNth x n] = x
```

`List.idxOfNth_zero` (theorem, [line 945](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L945))

```lean
theorem idxOfNth_zero [BEq α] : (xs : List α).idxOfNth x 0 = xs.idxOf x
```

`List.idxOfNth_lt_length_iff` (theorem, [line 949](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L949))

```lean
theorem idxOfNth_lt_length_iff [BEq α] {xs : List α} :
    xs.idxOfNth x n < xs.length ↔ n < xs.count x
```

`List.idxOfNth_eq_length_iff` (theorem, [line 953](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L953))

```lean
theorem idxOfNth_eq_length_iff [BEq α] {xs : List α} :
    xs.idxOfNth x n = xs.length ↔ xs.count x ≤ n
```

`List.idxOfNth_le_length` (theorem, [line 956](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L956))

```lean
theorem idxOfNth_le_length [BEq α] {xs : List α} :
    xs.idxOfNth x n ≤ xs.length
```

`List.idxOfNth_lt_length_of_lt_count` (theorem, [line 961](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L961))

```lean
theorem idxOfNth_lt_length_of_lt_count {xs : List α} [BEq α] :
    n < xs.count x → xs.idxOfNth x n < xs.length
```

`List.idxOfNth_eq_length_of_ge_count` (theorem, [line 964](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L964))

```lean
theorem idxOfNth_eq_length_of_ge_count {xs : List α} [BEq α] :
    xs.count x ≤ n → xs.idxOfNth x n = xs.length
```

`List.idxOfNth_lt_idxOfNth_iff` (theorem, [line 967](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L967))

```lean
theorem idxOfNth_lt_idxOfNth_iff [BEq α] {xs : List α} :
    xs.idxOfNth x n < xs.idxOfNth x m ↔ n < xs.count x ∧ n < m
```

`List.idxOfNth_eq_idxOfNth_iff` (theorem, [line 970](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L970))

```lean
theorem idxOfNth_eq_idxOfNth_iff [BEq α] {xs : List α} :
    xs.idxOfNth x n = xs.idxOfNth x m ↔
    (xs.count x ≤ m ∨ n ≤ m) ∧ (xs.count x ≤ n ∨ m ≤ n)
```

`List.idxOfNth_lt_idxOfNth_iff_of_lt_count` (theorem, [line 974](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L974))

```lean
theorem idxOfNth_lt_idxOfNth_iff_of_lt_count [BEq α] {xs : List α} (hn : n < xs.count x) :
    xs.idxOfNth x n < xs.idxOfNth x m ↔ n < m
```

`List.idxOfNth_mono` (theorem, [line 977](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L977))

```lean
theorem idxOfNth_mono [BEq α] {xs : List α} (hnm : n ≤ m):
    xs.idxOfNth x n ≤ xs.idxOfNth x m
```

`List.idxOfNth_eq_idxOfNth_iff_of_left_lt_count` (theorem, [line 980](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L980))

```lean
theorem idxOfNth_eq_idxOfNth_iff_of_left_lt_count [BEq α] {xs : List α}
    (hn : n < xs.count x) : xs.idxOfNth x n = xs.idxOfNth x m ↔ n = m
```

`List.idxOfNth_eq_idxOfNth_iff_of_right_lt_count` (theorem, [line 984](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L984))

```lean
theorem idxOfNth_eq_idxOfNth_iff_of_right_lt_count [BEq α] {xs : List α}
    (hm : m < xs.count x) : xs.idxOfNth x n = xs.idxOfNth x m ↔ n = m
```

`List.idxOfNth_eq_idxOfNth_of_ge_countP_ge_countP` (theorem, [line 988](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L988))

```lean
theorem idxOfNth_eq_idxOfNth_of_ge_countP_ge_countP [BEq α] {xs : List α}
    (hn : xs.count x ≤ n) (hm : xs.count x ≤ m) : xs.idxOfNth x n = xs.idxOfNth x m
```

> ### countPBefore

`List.countPBefore_nil` (theorem, [line 994](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L994))

```lean
theorem countPBefore_nil : ([] : List α).countPBefore p n = 0
```

`List.countPBefore_cons` (theorem, [line 997](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L997))

```lean
theorem countPBefore_cons {a : α} :
    (a :: xs).countPBefore p i =
    if i = 0 then 0 else if p a then xs.countPBefore p (i - 1) + 1
    else xs.countPBefore p (i - 1)
```

`List.countPBefore_cons_zero` (theorem, [line 1005](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1005))

```lean
theorem countPBefore_cons_zero {a : α} :
    (a :: xs).countPBefore p 0 = 0
```

`List.countPBefore_cons_succ` (theorem, [line 1008](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1008))

```lean
theorem countPBefore_cons_succ {a : α} :
    (a :: xs).countPBefore p (i + 1) =
    if p a then xs.countPBefore p i + 1 else xs.countPBefore p i
```

`List.countPBefore_zero` (theorem, [line 1012](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1012))

```lean
theorem countPBefore_zero :
    (xs : List α).countPBefore p 0 = 0
```

`List.countPBefore_succ` (theorem, [line 1016](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1016))

```lean
theorem countPBefore_succ :
    (xs : List α).countPBefore p (i + 1) =
    if h : xs = [] then 0
    else if p (xs.head h) then xs.tail.countPBefore p i + 1
    else xs.tail.countPBefore p i
```

`List.countPBefore_cons_succ_of_neg` (theorem, [line 1022](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1022))

```lean
theorem countPBefore_cons_succ_of_neg {a : α} (h : p a = false) :
    (a :: xs).countPBefore p (i + 1) = xs.countPBefore p i
```

`List.countPBefore_cons_succ_of_pos` (theorem, [line 1025](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1025))

```lean
theorem countPBefore_cons_succ_of_pos {a : α} (h : p a) :
    (a :: xs).countPBefore p (i + 1) = xs.countPBefore p i + 1
```

`List.countPBefore_eq_countP_take` (theorem, [line 1028](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1028))

```lean
theorem countPBefore_eq_countP_take : (xs : List α).countPBefore p i = (xs.take i).countP p
```

`List.countPBefore_of_ge_length` (theorem, [line 1031](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1031))

```lean
theorem countPBefore_of_ge_length {xs : List α} (hi : xs.length ≤ i) :
    xs.countPBefore p i = xs.countP p
```

`List.countPBefore_length` (theorem, [line 1035](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1035))

```lean
theorem countPBefore_length {xs : List α} :
    xs.countPBefore p xs.length = xs.countP p
```

`List.findIdxNth_countPBefore_of_lt_length_of_pos` (theorem, [line 1039](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1039))

```lean
theorem findIdxNth_countPBefore_of_lt_length_of_pos {xs : List α} {h : i < xs.length}
    (hip : p xs[i]) : xs.findIdxNth p (xs.countPBefore p i) = i
```

`List.countPBefore_findIdxNth_of_lt_countP` (theorem, [line 1044](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1044))

```lean
theorem countPBefore_findIdxNth_of_lt_countP {xs : List α} :
    n < xs.countP p → xs.countPBefore p (xs.findIdxNth p n) = n
```

`List.pos_iff_exists_findIdxNth` (theorem, [line 1048](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1048))

```lean
theorem pos_iff_exists_findIdxNth {xs : List α} {h : i < xs.length} :
    p xs[i] ↔ ∃ n, xs.findIdxNth p n = i
```

`List.countPBefore_le_countP` (theorem, [line 1051](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1051))

```lean
theorem countPBefore_le_countP {xs : List α} (p : α → Bool) :
    xs.countPBefore p i ≤ xs.countP p
```

`List.countPBefore_mono` (theorem, [line 1056](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1056))

```lean
theorem countPBefore_mono {xs : List α} (hij : i ≤ j) :
    xs.countPBefore p i ≤ xs.countPBefore p j
```

`List.countPBefore_lt_countP_of_lt_length_of_pos` (theorem, [line 1061](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1061))

```lean
theorem countPBefore_lt_countP_of_lt_length_of_pos {xs : List α} {h : i < xs.length}
    (hip : p xs[i]) : xs.countPBefore p i < xs.countP p
```

> ### countBefore

`List.countBefore_nil` (theorem, [line 1069](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1069))

```lean
theorem countBefore_nil [BEq α] : ([] : List α).countBefore x i = 0
```

`List.countBefore_cons` (theorem, [line 1072](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1072))

```lean
theorem countBefore_cons [BEq α] {a : α} :
    (a :: xs).countBefore x i =
    if i = 0 then 0 else if a == x then xs.countBefore x (i - 1) + 1
    else xs.countBefore x (i - 1)
```

`List.countBefore_zero` (theorem, [line 1077](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1077))

```lean
theorem countBefore_zero [BEq α] : (xs : List α).countBefore p 0 = 0
```

`List.countBefore_cons_succ` (theorem, [line 1079](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1079))

```lean
theorem countBefore_cons_succ {a : α} [BEq α] :
    (a :: xs).countBefore x (i + 1) = xs.countBefore x i + if a == x then 1 else 0
```

`List.countBefore_cons_succ_of_not_beq` (theorem, [line 1082](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1082))

```lean
theorem countBefore_cons_succ_of_not_beq [BEq α] {a : α} (h : (a == x) = false):
    (a :: xs).countBefore x (i + 1) = xs.countBefore x i
```

`List.countBefore_cons_succ_of_beq` (theorem, [line 1085](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1085))

```lean
theorem countBefore_cons_succ_of_beq {a : α} [BEq α] (h : a == x) :
    (a :: xs).countBefore x (i + 1) = xs.countBefore x i + 1
```

`List.countBefore_eq_count_take` (theorem, [line 1088](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1088))

```lean
theorem countBefore_eq_count_take [BEq α] :
    (xs : List α).countBefore x i = (xs.take i).count x
```

`List.countBefore_idxOfNth_of_lt_count` (theorem, [line 1093](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1093))

```lean
theorem countBefore_idxOfNth_of_lt_count [BEq α] {xs : List α} (hn : n < xs.count x) :
     xs.countBefore x (xs.idxOfNth x n) = n
```

`List.idxOfNth_countBefore_of_lt_length_of_beq` (theorem, [line 1097](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1097))

```lean
theorem idxOfNth_countBefore_of_lt_length_of_beq [BEq α] {xs : List α} {h : i < xs.length}
    (hip : xs[i] == x) : xs.idxOfNth x (xs.countBefore x i) = i
```

`List.idxOfNth_countBefore_getElem` (theorem, [line 1102](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1102))

```lean
theorem idxOfNth_countBefore_getElem [BEq α] [ReflBEq α] {xs : List α}
    {h : i < xs.length} : xs.idxOfNth xs[i] (xs.countBefore xs[i] i) = i
```

`List.beq_iff_exists_findIdxNth` (theorem, [line 1106](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1106))

```lean
theorem beq_iff_exists_findIdxNth [BEq α] {xs : List α} {h : i < xs.length} :
    xs[i] == x ↔ ∃ n, xs.idxOfNth x n = i
```

`List.countBefore_le_count` (theorem, [line 1109](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1109))

```lean
theorem countBefore_le_count [BEq α] {xs : List α} :
    xs.countBefore x i ≤ xs.count x
```

`List.countBefore_lt_count_of_lt_length_of_beq` (theorem, [line 1113](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1113))

```lean
theorem countBefore_lt_count_of_lt_length_of_beq [BEq α] {xs : List α} {h : i < xs.length}
    (hip : xs[i] == x) : xs.countBefore x i < xs.count x
```

`List.countBefore_lt_count_getElem` (theorem, [line 1118](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1118))

```lean
theorem countBefore_lt_count_getElem [BEq α] [ReflBEq α] {xs : List α} {h : i < xs.length} :
    xs.countBefore xs[i] i < xs.count xs[i]
```

`List.countBefore_of_ge_length` (theorem, [line 1124](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1124))

```lean
theorem countBefore_of_ge_length [BEq α] {xs : List α} (hi : xs.length ≤ i) :
    xs.countBefore x i = xs.count x
```

> ### insertP

`List.insertP_loop` (theorem, [line 1129](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1129))

```lean
theorem insertP_loop (a : α) (l r : List α) :
    insertP.loop p a l r = reverseAux r (insertP p a l)
```

`List.insertP_nil` (theorem, [line 1134](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1134))

```lean
theorem insertP_nil (p : α → Bool) (a) : insertP p a [] = [a]
```

`List.insertP_cons_pos` (theorem, [line 1136](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1136))

```lean
theorem insertP_cons_pos (p : α → Bool) (a b l) (h : p b) :
    insertP p a (b :: l) = a :: b :: l
```

`List.insertP_cons_neg` (theorem, [line 1140](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1140))

```lean
theorem insertP_cons_neg (p : α → Bool) (a b l) (h : ¬ p b) :
    insertP p a (b :: l) = b :: insertP p a l
```

`List.length_insertP` (theorem, [line 1144](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1144))

```lean
theorem length_insertP (p : α → Bool) (a l) : (insertP p a l).length = l.length + 1
```

`List.mem_insertP` (theorem, [line 1148](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1148))

```lean
theorem mem_insertP (p : α → Bool) (a l) : a ∈ insertP p a l
```

> ### dropPrefix?, dropSuffix?, dropInfix?

`List.dropPrefix?_nil` (theorem, [line 1156](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1156))

```lean
theorem dropPrefix?_nil [BEq α] {p : List α} : dropPrefix? p [] = some p
```

`List.dropPrefix?_eq_some_iff` (theorem, [line 1159](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1159))

```lean
theorem dropPrefix?_eq_some_iff [BEq α] {l p s : List α} :
    dropPrefix? l p = some s ↔ ∃ p', l = p' ++ s ∧ p' == p
```

`List.dropPrefix?_append_of_beq` (theorem, [line 1179](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1179))

```lean
theorem dropPrefix?_append_of_beq [BEq α] {l₁ l₂ : List α} (p : List α) (h : l₁ == l₂) :
    dropPrefix? (l₁ ++ p) l₂ = some p
```

`List.dropSuffix?_eq_some_iff` (theorem, [line 1183](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1183))

```lean
theorem dropSuffix?_eq_some_iff [BEq α] {l p s : List α} :
    dropSuffix? l s = some p ↔ ∃ s', l = p ++ s' ∧ s' == s
```

`List.dropSuffix?_nil` (theorem, [line 1194](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1194))

```lean
theorem dropSuffix?_nil [BEq α] {s : List α} : dropSuffix? s [] = some s
```

`List.dropInfix?_go_eq_some_iff` (theorem, [line 1197](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1197))

```lean
theorem dropInfix?_go_eq_some_iff [BEq α] {i l acc p s : List α} :
    dropInfix?.go i l acc = some (p, s) ↔ ∃ p',
      p = acc.reverse ++ p' ∧
      -- `i` is an infix up to `==`
      (∃ i', l = p' ++ i' ++ s ∧ i' == i) ∧
        -- and there is no shorter prefix for which that is the case
        (∀ p'' i'' s'', l = p'' ++ i'' ++ s'' → i'' == i → p''.length ≥ p'.length)
```

`List.dropInfix?_eq_some_iff` (theorem, [line 1264](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1264))

```lean
theorem dropInfix?_eq_some_iff [BEq α] {l i p s : List α} :
    dropInfix? l i = some (p, s) ↔
      -- `i` is an infix up to `==`
      (∃ i', l = p ++ i' ++ s ∧ i' == i) ∧
        -- and there is no shorter prefix for which that is the case
        (∀ p' i' s', l = p' ++ i' ++ s' → i' == i → p'.length ≥ p.length)
```

`List.dropInfix?_nil` (theorem, [line 1274](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1274))

```lean
theorem dropInfix?_nil [BEq α] {s : List α} : dropInfix? s [] = some ([], s)
```

> ### IsPrefixOf?, IsSuffixOf?

`List.isSome_isPrefixOf?_eq_isPrefixOf` (theorem, [line 1279](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1279))

```lean
theorem isSome_isPrefixOf?_eq_isPrefixOf [BEq α] (xs ys : List α) :
    (xs.isPrefixOf? ys).isSome = xs.isPrefixOf ys
```

`List.isPrefixOf?_eq_some_iff_append_eq` (theorem, [line 1288](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1288))

```lean
theorem isPrefixOf?_eq_some_iff_append_eq [BEq α] [LawfulBEq α] {xs ys zs : List α} :
    xs.isPrefixOf? ys = some zs ↔ xs ++ zs = ys
```

`List.append_eq_of_isPrefixOf?_eq_some` (theorem, [line 1294](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1294))

```lean
theorem append_eq_of_isPrefixOf?_eq_some [BEq α] [LawfulBEq α] {xs ys zs : List α}
    (h : xs.isPrefixOf? ys = some zs) : xs ++ zs = ys
```

`List.isSome_isSuffixOf?_eq_isSuffixOf` (theorem, [line 1297](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1297))

```lean
theorem isSome_isSuffixOf?_eq_isSuffixOf [BEq α] (xs ys : List α) :
    (xs.isSuffixOf? ys).isSome = xs.isSuffixOf ys
```

`List.isSuffixOf?_eq_some_iff_append_eq` (theorem, [line 1301](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1301))

```lean
theorem isSuffixOf?_eq_some_iff_append_eq [BEq α] [LawfulBEq α] {xs ys zs : List α} :
    xs.isSuffixOf? ys = some zs ↔ zs ++ xs = ys
```

`List.append_eq_of_isSuffixOf?_eq_some` (theorem, [line 1314](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1314))

```lean
theorem append_eq_of_isSuffixOf?_eq_some [BEq α] [LawfulBEq α] {xs ys zs : List α}
    (h : xs.isSuffixOf? ys = some zs) : zs ++ xs = ys
```

> ### finRange

`List.get_finRange` (theorem, [line 1319](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1319))

```lean
theorem get_finRange (i : Fin (finRange n).length) :
    (finRange n).get i = Fin.cast length_finRange i
```

`List.finRange_eq_nil_iff` (theorem, [line 1323](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1323))

```lean
theorem finRange_eq_nil_iff : finRange n = [] ↔ n = 0
```

`List.finRange_eq_pmap_range` (theorem, [line 1326](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1326))

```lean
theorem finRange_eq_pmap_range : finRange n = (range n).pmap Fin.mk (by simp)
```

`List.map_get_finRange` (theorem, [line 1330](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1330))

```lean
theorem map_get_finRange (l : List α) : (finRange l.length).map l.get = l
```

`List.map_getElem_finRange` (theorem, [line 1334](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1334))

```lean
theorem map_getElem_finRange (l : List α) : (finRange l.length).map (l[·.1]) = l
```

`List.map_coe_finRange_eq_range` (theorem, [line 1338](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1338))

```lean
theorem map_coe_finRange_eq_range : (finRange n).map (↑·) = List.range n
```

> ### sum/prod

`List.prod_one_cons` (theorem, [line 1343](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1343))

```lean
theorem prod_one_cons [Mul α] [One α] [Std.LawfulLeftIdentity (α := α) (· * ·) 1] {l : List α} :
    (1 :: l).prod = l.prod
```

`List.prod_pair` (theorem, [line 1346](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1346))

```lean
theorem prod_pair [Mul α] [One α] [Std.LawfulRightIdentity (α := α) (· * ·) 1] {a b : α} :
  [a, b].prod = a * b
```

`List.prod_concat` (theorem, [line 1349](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1349))

```lean
theorem prod_concat [Mul α] [One α] [Std.LawfulIdentity (α := α) (· * ·) 1]
    [Std.Associative (α := α) (· * ·)] {l : List α} {a : α} :
    (l.concat a).prod = l.prod * a
```

`List.prod_flatten` (theorem, [line 1354](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1354))

```lean
theorem prod_flatten [Mul α] [One α] [Std.LawfulIdentity (α := α) (· * ·) 1]
    [Std.Associative (α := α) (· * ·)] {l : List (List α)} :
    l.flatten.prod = (l.map prod).prod
```

`List.sum_zero_cons` (theorem, [line 1359](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1359))

```lean
theorem sum_zero_cons [Add α] [Zero α] [Std.LawfulLeftIdentity (α := α) (· + ·) 0] {l : List α} :
    (0 :: l).sum = l.sum
```

`List.sum_pair` (theorem, [line 1362](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1362))

```lean
theorem sum_pair [Add α] [Zero α] [Std.LawfulRightIdentity (α := α) (· + ·) 0] {a b : α} :
  [a, b].sum = a + b
```

`List.sum_concat` (theorem, [line 1365](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1365))

```lean
theorem sum_concat [Add α] [Zero α] [Std.LawfulIdentity (α := α) (· + ·) 0]
    [Std.Associative (α := α) (· + ·)] {l : List α} {a : α} :
    (l.concat a).sum = l.sum + a
```

`List.sum_flatten` (theorem, [line 1370](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1370))

```lean
theorem sum_flatten [Add α] [Zero α] [Std.LawfulIdentity (α := α) (· + ·) 0]
    [Std.Associative (α := α) (· + ·)] {l : List (List α)} :
    l.flatten.sum = (l.map sum).sum
```

`List.take_succ_drop` (theorem, [line 1375](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1375))

```lean
theorem take_succ_drop {l : List α} {n stop : Nat}
    (h : n < l.length - stop) :
    (l.drop stop |>.take (n + 1)) = (l.drop stop |>.take n) ++ [l[stop + n]'(by omega)]
```

> ### max!/min!

`List.max!_eq_max?_getD` (theorem, [line 1384](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1384))

```lean
theorem max!_eq_max?_getD [Inhabited α] {l : List α} [Max α] :
    l.max! = (l.max?).getD (default : α)
```

`List.max!_eq_max_of_ne_nil` (theorem, [line 1387](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1387))

```lean
theorem max!_eq_max_of_ne_nil [Inhabited α] [Max α] (l : List α) (hl : l ≠ []) :
    l.max! = l.max hl
```

`List.max!_nil` (theorem, [line 1394](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1394))

```lean
theorem max!_nil [Inhabited α] [Max α] : ([] : List α).max! = default
```

`List.min!_eq_min?_getD` (theorem, [line 1397](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1397))

```lean
theorem min!_eq_min?_getD [Inhabited α] {l : List α} [Min α] :
    l.min! = (l.min?).getD (default : α)
```

`List.min!_eq_min_of_ne_nil` (theorem, [line 1400](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1400))

```lean
theorem min!_eq_min_of_ne_nil [Inhabited α] [Min α] (l : List α) (hl : l ≠ []) :
    l.min! = l.min hl
```

`List.min!_nil` (theorem, [line 1407](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1407))

```lean
theorem min!_nil [Inhabited α] [Min α] : ([] : List α).min! = default
```

> ### swapAt

`List.swapAt_def` (theorem, [line 1411](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1411))

```lean
theorem swapAt_def : swapAt xs i v = (xs[i]?.getD v, xs.set i v)
```

> ### swap

`List.swap_nil` (theorem, [line 1415](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1415))

```lean
theorem swap_nil : ([] : List α).swap i j = []
```

`List.swap_cons` (theorem, [line 1417](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1417))

```lean
theorem swap_cons :
    (a :: xs).swap (i + 1) (j + 1) = a :: xs.swap i j
```

`List.swap_cons_zero_left` (theorem, [line 1420](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1420))

```lean
theorem swap_cons_zero_left :
    (a :: xs).swap 0 (j + 1) = xs[j]?.getD a :: xs.set j a
```

`List.swap_cons_zero_right` (theorem, [line 1423](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1423))

```lean
theorem swap_cons_zero_right :
    (a :: xs).swap (i + 1) 0 = xs[i]?.getD a :: xs.set i a
```

`List.swap_eq` (theorem, [line 1426](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1426))

```lean
theorem swap_eq {xs : List α}  :
    xs.swap i j = if h : i < xs.length ∧ j < xs.length then
    (xs.set i xs[j]).set j xs[i] else xs
```

`List.swap_eq_of_ge_left` (theorem, [line 1433](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1433))

```lean
theorem swap_eq_of_ge_left {xs : List α} (h : xs.length ≤ i) : xs.swap i j = xs
```

`List.swap_eq_of_ge_right` (theorem, [line 1436](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1436))

```lean
theorem swap_eq_of_ge_right {xs : List α} (h : xs.length ≤ j) : xs.swap i j = xs
```

`List.swap_eq_of_lt` (theorem, [line 1439](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1439))

```lean
theorem swap_eq_of_lt {xs : List α} (hi :  i < xs.length) (hj : j < xs.length) :
    xs.swap i j = (xs.set i xs[j]).set j xs[i]
```

`List.swap_self` (theorem, [line 1443](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1443))

```lean
theorem swap_self {xs : List α} {i : Nat} : xs.swap i i = xs
```

`List.swap_comm` (theorem, [line 1448](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1448))

```lean
theorem swap_comm {xs : List α} {i j : Nat} : xs.swap i j = xs.swap j i
```

`List.length_swap` (theorem, [line 1458](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1458))

```lean
theorem length_swap {xs : List α} : (xs.swap i j).length = xs.length
```

`List.getElem_swap_left` (theorem, [line 1465](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1465))

```lean
theorem getElem_swap_left {xs : List α} {i j : Nat} (hi : i < (xs.swap i j).length) :
    (xs.swap i j)[i] = if hj : j < xs.length then xs[j] else xs[i]'(length_swap ▸ hi)
```

`List.getElem_swap_right` (theorem, [line 1472](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1472))

```lean
theorem getElem_swap_right {xs : List α} {i j : Nat} (hj : j < (xs.swap i j).length) :
    (xs.swap i j)[j] = if hi : i < xs.length then xs[i] else xs[j]'(length_swap ▸ hj)
```

`List.getElem_swap_of_ne` (theorem, [line 1476](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1476))

```lean
theorem getElem_swap_of_ne {xs : List α} {i j k : Nat} (hik : k ≠ i) (hjk : k ≠ j)
    (hk : k < (xs.swap i j).length) : (xs.swap i j)[k] = xs[k]'(length_swap ▸ hk)
```

`List.getElem_swap_left_of_lt` (theorem, [line 1484](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1484))

```lean
theorem getElem_swap_left_of_lt {xs : List α} {i j : Nat} (hj : j < xs.length)
    (hi : i < (xs.swap i j).length) : (xs.swap i j)[i] = xs[j]
```

`List.getElem_swap_right_of_lt` (theorem, [line 1488](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1488))

```lean
theorem getElem_swap_right_of_lt {xs : List α} {i j : Nat} (hi : i < xs.length)
    (hj : j < (xs.swap i j).length) : (xs.swap i j)[j] = xs[i]
```

`List.getElem_swap` (theorem, [line 1493](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1493))

```lean
theorem getElem_swap {xs : List α} {i j k : Nat}
    (hk : k < (xs.swap i j).length) : (xs.swap i j)[k] =
    if h₁ : k = i ∧ j < xs.length then xs[j] else if h₂ : k = j ∧ i < xs.length then xs[i]
    else xs[k]'(length_swap ▸ hk)
```

`List.swap_swap` (theorem, [line 1504](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1504))

```lean
theorem swap_swap {xs : List α} {i j : Nat} : (xs.swap i j).swap i j = xs
```

`List.swap_swap_flip` (theorem, [line 1507](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean#L1507))

```lean
theorem swap_swap_flip {xs : List α} {i j : Nat} :
    (xs.swap i j).swap j i = xs
```

## Depends on

- [Additional definitions on `ForInStep`](../../../../control/forinstep/basic.md)
- [List/Basic](basic.md)

## Proof depends on

- [Additional theorems on `ForInStep`](../../../../control/forinstep/lemmas.md)

## Sources

- [Batteries/Data/List/Lemmas.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Lemmas.lean)
- [Declaration ledger](../../../../../../sources/batteries/Batteries.Data.List.Lemmas.json)
