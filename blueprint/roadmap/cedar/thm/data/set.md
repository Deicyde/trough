---
catalog: module
lean: Cedar.Data.Set.WellFormed, Cedar.Data.Set.if_wellformed_then_exists_make, Cedar.Data.Set.wf_iff_sorted, Cedar.Data.Set.mapOrErr_eq_match, Cedar.Data.Set.contains_prop_bool_equiv, Cedar.Data.Set.not_contains_prop_bool_equiv, Cedar.Data.Set.mem_elts_iff_mem_set, Cedar.Data.Set.mem_set_iff_mem_mk, Cedar.Data.Set.mem_mk_hd, Cedar.Data.Set.mem_mk_tl, Cedar.Data.Set.mem_cons, Cedar.Data.Set.mem_set_implies_elts_non_empty, Cedar.Data.Set.empty_eq_mk_nil, Cedar.Data.Set.elts_empty, Cedar.Data.Set.not_mem_empty, Cedar.Data.Set.empty_wf, Cedar.Data.Set.map_empty, Cedar.Data.Set.all_empty, Cedar.Data.Set.any_empty, Cedar.Data.Set.isEmpty_empty, Cedar.Data.Set.isEmpty_iff_eq_empty, Cedar.Data.Set.isEmpty_make, Cedar.Data.Set.isEmpty_make_eq_false, Cedar.Data.Set.non_empty_iff_exists, Cedar.Data.Set.empty_iff_not_exists, Cedar.Data.Set.singleton_wf, Cedar.Data.Set.mem_singleton, Cedar.Data.Set.mem_singleton_self, Cedar.Data.Set.make_wf, Cedar.Data.Set.make_elts, Cedar.Data.Set.make_sorted, Cedar.Data.Set.mem_make, Cedar.Data.Set.make_mk_eqv, Cedar.Data.Set.make_make_eqv, Cedar.Data.Set.elts_make_eqv, Cedar.Data.Set.make_nil, Cedar.Data.Set.make_eq_empty, Cedar.Data.Set.make_singleton_nonempty, Cedar.Data.Set.eq_means_eqv, Cedar.Data.Set.any_make, Cedar.Data.Set.make_elts_make, Cedar.Data.Set.elts_make_implies_equiv, Cedar.Data.Set.make_cons, Cedar.Data.Set.inter_def, Cedar.Data.Set.mem_inter_iff, Cedar.Data.Set.inter_wf, Cedar.Data.Set.inter_empty_left, Cedar.Data.Set.inter_empty_right, Cedar.Data.Set.inter_self, Cedar.Data.Set.intersects_def, Cedar.Data.Set.intersects_iff_exists, Cedar.Data.Set.union_wf, Cedar.Data.Set.make_cons_eq_singleton_union, Cedar.Data.Set.append_eq_union, Cedar.Data.Set.mem_union, Cedar.Data.Set.prop_union_iff_prop_and, Cedar.Data.Set.union_comm, Cedar.Data.Set.union_assoc, Cedar.Data.Set.union_empty_right, Cedar.Data.Set.union_empty_left, Cedar.Data.Set.union_idempotent, Cedar.Data.Set.elts_subset_then_subset, Cedar.Data.Set.subset_def, Cedar.Data.Set.subset_empty, Cedar.Data.Set.superset_empty_subset_empty, Cedar.Data.Set.subset_iff_subset_elts, Cedar.Data.Set.subset_iff_eq, Cedar.Data.Set.subset_trans, Cedar.Data.Set.subset_refl, Cedar.Data.Set.mem_subset_mem, Cedar.Data.Set.subset_union, Cedar.Data.Set.union_subset, Cedar.Data.Set.union_subset_eq, Cedar.Data.Set.wellFormed_correct, Cedar.Data.Set.map_wf, Cedar.Data.Set.map_id, Cedar.Data.Set.mem_map, Cedar.Data.Set.map_congr, Cedar.Data.Set.isEmpty_map, Cedar.Data.Set.map_make, Cedar.Data.Set.map_def, Cedar.Data.Set.map_union, Cedar.Data.Set.filter_wf, Cedar.Data.Set.mem_filter, Cedar.Data.Set.difference_wf, Cedar.Data.Set.mem_difference, Cedar.Data.Set.difference_subset, Cedar.Data.Set.all_eq_true, Cedar.Data.Set.all_eq_false, Cedar.Data.Set.any_eq_true, Cedar.Data.Set.any_eq_false, Cedar.Data.Set.map₁_eq_map, Cedar.Data.Set.all₁_eq_all, Cedar.Data.Set.any₁_eq_any, Cedar.Data.Set.mem_product, Cedar.Data.Set.product_empty, Cedar.Data.Set.empty_product
statement: formalized
proof: formalized
---

# Set properties

`Cedar.Thm.Data.Set`, in [Cedar/Thm/Data/Set.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean).

> This file proves useful properties of canonical list-based sets defined in
> `Cedar.Data.Set`.

> ### Well-formed sets

`Cedar.Data.Set.WellFormed` (definition, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L36))

```lean
public def WellFormed {α} [LT α] [DecidableLT α] (s : Set α)
```

`Cedar.Data.Set.if_wellformed_then_exists_make` (theorem, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L39))

```lean
public theorem if_wellformed_then_exists_make [LT α] [DecidableLT α] (s : Set α) :
  WellFormed s → ∃ list, s = Set.make list
```

`Cedar.Data.Set.wf_iff_sorted` (theorem, [line 45](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L45))

```lean
public theorem wf_iff_sorted {α} [LT α] [DecidableLT α] [StrictLT α]  (s : Set α) :
  s.WellFormed ↔ s.elts.Sorted
```

`Cedar.Data.Set.mapOrErr_eq_match` (theorem, [line 62](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L62))

> Equation lemma for `Set.mapOrErr`, for clients that cannot unfold it.

```lean
public theorem mapOrErr_eq_match {α β ε} [DecidableEq β] [LT β] [DecidableRel (α := β) (· < ·)] (f : α → Except ε β) (s : Set α) (err : ε) :
  s.mapOrErr f err = match s.elts.mapM f with | .ok elts => .ok (make elts) | .error _ => .error err
```

> ### contains and mem

`Cedar.Data.Set.contains_prop_bool_equiv` (theorem, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L69))

```lean
public theorem contains_prop_bool_equiv [DecidableEq α] {v : α} {s : Set α} :
  s.contains v = true ↔ v ∈ s
```

`Cedar.Data.Set.not_contains_prop_bool_equiv` (theorem, [line 77](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L77))

```lean
public theorem not_contains_prop_bool_equiv [DecidableEq α] {v : α} {s : Set α} :
  s.contains v = false ↔ v ∉ s
```

`Cedar.Data.Set.mem_elts_iff_mem_set` (theorem, [line 92](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L92))

```lean
public theorem mem_elts_iff_mem_set {α : Type u} (v : α) (s : Set α) :
  v ∈ s.elts ↔ v ∈ s
```

`Cedar.Data.Set.mem_set_iff_mem_mk` (theorem, [line 99](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L99))

```lean
public theorem mem_set_iff_mem_mk {α : Type u} (v : α) (xs : List α) :
  v ∈ xs ↔ v ∈ mk xs
```

`Cedar.Data.Set.mem_mk_hd` (theorem, [line 106](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L106))

```lean
public theorem mem_mk_hd {α : Type u} (hd : α) (tl : List α) :
  hd ∈ Set.mk (hd :: tl)
```

`Cedar.Data.Set.mem_mk_tl` (theorem, [line 112](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L112))

```lean
public theorem mem_mk_tl {α : Type u} (a : α) (hd : α) (tl : List α) :
  a ∈ Set.mk tl → a ∈ Set.mk (hd :: tl)
```

`Cedar.Data.Set.mem_cons` (theorem, [line 119](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L119))

```lean
public theorem mem_cons {a : α} {hd : α} {tl : List α} :
  a ∈ Set.mk (hd :: tl) ↔ a = hd ∨ a ∈ tl
```

`Cedar.Data.Set.mem_set_implies_elts_non_empty` (theorem, [line 124](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L124))

```lean
public theorem mem_set_implies_elts_non_empty {α : Type u} (v : α) (s : Set α) :
  v ∈ s → ¬(s.elts = [])
```

> ### empty

`Cedar.Data.Set.empty_eq_mk_nil` (theorem, [line 134](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L134))

```lean
public theorem empty_eq_mk_nil {α} :
  (Set.empty : Set α) = Set.mk []
```

`Cedar.Data.Set.elts_empty` (theorem, [line 139](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L139))

```lean
public theorem elts_empty {α} :
  (Set.empty : Set α).elts = []
```

`Cedar.Data.Set.not_mem_empty` (theorem, [line 144](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L144))

> Like `List.not_mem_nil`, lifted to Sets

```lean
public theorem not_mem_empty {α : Type u} (v : α) :
  ¬ v ∈ Set.empty
```

`Cedar.Data.Set.empty_wf` (theorem, [line 152](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L152))

```lean
public theorem empty_wf {α : Type u} [LT α] [DecidableLT α] :
  Set.WellFormed (Set.empty : Set α)
```

`Cedar.Data.Set.map_empty` (theorem, [line 159](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L159))

```lean
public theorem map_empty [LT β] [DecidableLT β] (f : α → β) :
  Set.empty.map f = Set.empty
```

`Cedar.Data.Set.all_empty` (theorem, [line 165](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L165))

```lean
public theorem all_empty (f : α → Bool) :
  Set.empty.all f = true
```

`Cedar.Data.Set.any_empty` (theorem, [line 170](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L170))

```lean
public theorem any_empty (f : α → Bool) :
  Set.empty.any f = false
```

> ### isEmpty

`Cedar.Data.Set.isEmpty_empty` (theorem, [line 177](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L177))

```lean
public theorem isEmpty_empty [LT α] [DecidableLT α] [DecidableEq α] :
  (Set.empty : Set α).isEmpty
```

`Cedar.Data.Set.isEmpty_iff_eq_empty` (theorem, [line 181](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L181))

```lean
public theorem isEmpty_iff_eq_empty [DecidableEq α] {s : Set α} :
  s.isEmpty ↔ s = Set.empty
```

`Cedar.Data.Set.isEmpty_make` (theorem, [line 186](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L186))

```lean
public theorem isEmpty_make [DecidableEq α] [LT α] [DecidableLT α] {xs : List α} :
  (Set.make xs).isEmpty ↔ xs = []
```

`Cedar.Data.Set.isEmpty_make_eq_false` (theorem, [line 202](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L202))

```lean
public theorem isEmpty_make_eq_false [DecidableEq α] [LT α] [DecidableLT α] (xs : List α) :
  (Set.make xs).isEmpty = false ↔ xs ≠ []
```

`Cedar.Data.Set.non_empty_iff_exists` (theorem, [line 214](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L214))

```lean
public theorem non_empty_iff_exists [DecidableEq α] (s : Set α) :
  (¬ s.isEmpty) ↔ ∃ a, a ∈ s
```

`Cedar.Data.Set.empty_iff_not_exists` (theorem, [line 235](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L235))

> Corollary of `non_empty_iff_exists`

```lean
public theorem empty_iff_not_exists [DecidableEq α] (s : Set α) :
  s.isEmpty ↔ ¬ ∃ a, a ∈ s
```

> ### singleton

`Cedar.Data.Set.singleton_wf` (theorem, [line 248](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L248))

```lean
public theorem singleton_wf [DecidableEq α] [LT α] [DecidableLT α] (a : α) :
  WellFormed (Set.singleton a)
```

`Cedar.Data.Set.mem_singleton` (theorem, [line 255](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L255))

```lean
public theorem mem_singleton [DecidableEq α] (a b : α) :
  a ∈ Set.singleton b ↔ a = b
```

`Cedar.Data.Set.mem_singleton_self` (theorem, [line 260](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L260))

```lean
public theorem mem_singleton_self [DecidableEq α] (a : α) :
  a ∈ Set.singleton a
```

> ### make

`Cedar.Data.Set.make_wf` (theorem, [line 266](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L266))

```lean
public theorem make_wf [LT α] [DecidableLT α] [StrictLT α] (xs : List α) :
  WellFormed (Set.make xs)
```

`Cedar.Data.Set.make_elts` (theorem, [line 271](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L271))

```lean
public theorem make_elts [LT α] [DecidableLT α] {s : Set α} :
  WellFormed s → Set.make s.elts = s
```

`Cedar.Data.Set.make_sorted` (theorem, [line 275](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L275))

```lean
public theorem make_sorted {α} [LT α] [DecidableLT α] [StrictLT α] {xs : List α} :
  xs.Sorted → Set.make xs = Set.mk xs
```

`Cedar.Data.Set.mem_make` (theorem, [line 284](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L284))

```lean
public theorem mem_make [LT α] [DecidableLT α] [StrictLT α] (x : α) (xs : List α) :
  x ∈ Set.make xs ↔ x ∈ xs
```

`Cedar.Data.Set.make_mk_eqv` (theorem, [line 295](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L295))

```lean
public theorem make_mk_eqv [LT α] [DecidableLT α] [StrictLT α] {xs ys : List α} :
  Set.make xs = Set.mk ys → xs ≡ ys
```

`Cedar.Data.Set.make_make_eqv` (theorem, [line 303](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L303))

```lean
public theorem make_make_eqv [LT α] [DecidableLT α] [StrictLT α] {xs ys : List α} :
  Set.make xs = Set.make ys ↔ xs ≡ ys
```

`Cedar.Data.Set.elts_make_eqv` (theorem, [line 319](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L319))

```lean
public theorem elts_make_eqv [LT α] [DecidableLT α] [StrictLT α] {xs : List α} :
  Set.elts (Set.make xs) ≡ xs
```

`Cedar.Data.Set.make_nil` (theorem, [line 330](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L330))

```lean
public theorem make_nil [LT α] [DecidableLT α] [StrictLT α] :
  Set.make [] (α := α) = Set.empty
```

`Cedar.Data.Set.make_eq_empty` (theorem, [line 336](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L336))

```lean
public theorem make_eq_empty [LT α] [DecidableLT α] [DecidableEq α] {xs : List α} :
  Set.make xs = Set.empty ↔ xs = []
```

`Cedar.Data.Set.make_singleton_nonempty` (theorem, [line 342](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L342))

```lean
public theorem make_singleton_nonempty [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] (a : α) :
  Set.make [a] ≠ Set.empty
```

`Cedar.Data.Set.eq_means_eqv` (theorem, [line 347](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L347))

```lean
public theorem eq_means_eqv [LT α] [DecidableLT α] [StrictLT α] {s₁ s₂ : Set α} :
  WellFormed s₁ → WellFormed s₂ →
  (s₁ = s₂ ↔ s₁.elts ≡ s₂.elts)
```

`Cedar.Data.Set.any_make` (theorem, [line 367](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L367))

```lean
public theorem any_make [LT α] [DecidableLT α] [StrictLT α] (f : α → Bool) (xs : List α) :
  (Set.make xs).any f = xs.any f
```

`Cedar.Data.Set.make_elts_make` (theorem, [line 389](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L389))

```lean
public theorem make_elts_make [LT α] [DecidableLT α] [StrictLT α] (xs : List α) :
  Set.make (Set.elts (Set.make xs)) = Set.make xs
```

`Cedar.Data.Set.elts_make_implies_equiv` (theorem, [line 397](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L397))

```lean
public theorem elts_make_implies_equiv [LT α] [DecidableLT α] [StrictLT α] {xs ys : List α} :
  Set.elts (Set.make xs) = ys → ys ≡ xs
```

`Cedar.Data.Set.make_cons` (theorem, [line 409](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L409))

> Note that the converse of this is not true:
> counterexample `xs = [1]`, `ys = []`, `a = 1`.

```lean
public theorem make_cons [LT α] [DecidableLT α] {xs ys : List α} {a : α} :
  make xs = make ys → make (a :: xs) = make (a :: ys)
```

> ### inter and union

`Cedar.Data.Set.inter_def` (theorem, [line 417](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L417))

```lean
public theorem inter_def {α} [LT α] [StrictLT α] [DecidableLT α] [DecidableEq α] {s₁ s₂ : Set α} :
  s₁ ∩ s₂ = s₁.intersect s₂
```

`Cedar.Data.Set.mem_inter_iff` (theorem, [line 423](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L423))

```lean
public theorem mem_inter_iff {α} [DecidableEq α] {x : α} {s₁ s₂ : Set α} :
  x ∈ s₁ ∩ s₂ ↔ x ∈ s₁ ∧ x ∈ s₂
```

`Cedar.Data.Set.inter_wf` (theorem, [line 431](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L431))

```lean
public theorem inter_wf {α} [LT α] [StrictLT α] [DecidableLT α] [DecidableEq α] {s₁ s₂ : Set α}
 (h₁ : WellFormed s₁) :
 WellFormed (s₁ ∩ s₂)
```

`Cedar.Data.Set.inter_empty_left` (theorem, [line 446](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L446))

```lean
public theorem inter_empty_left {α} [LT α] [StrictLT α] [DecidableLT α] [DecidableEq α] (s : Set α) :
 Set.empty ∩ s = Set.empty
```

`Cedar.Data.Set.inter_empty_right` (theorem, [line 453](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L453))

```lean
public theorem inter_empty_right {α} [LT α] [StrictLT α] [DecidableLT α] [DecidableEq α] (s : Set α) :
 s ∩ Set.empty = Set.empty
```

`Cedar.Data.Set.inter_self` (theorem, [line 461](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L461))

```lean
public theorem inter_self {α} [LT α] [StrictLT α] [DecidableLT α] [DecidableEq α] (s : Set α) :
 s ∩ s = s
```

`Cedar.Data.Set.intersects_def` (theorem, [line 479](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L479))

```lean
public theorem intersects_def {α} [LT α] [StrictLT α] [DecidableLT α] [DecidableEq α] {s₁ s₂ : Set α} :
 s₁.intersects s₂ = ¬ (s₁ ∩ s₂).isEmpty
```

`Cedar.Data.Set.intersects_iff_exists` (theorem, [line 501](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L501))

```lean
public theorem intersects_iff_exists {α} [LT α] [StrictLT α] [DecidableLT α] [DecidableEq α] {s₁ s₂ : Set α} :
 s₁.intersects s₂ ↔ ∃ a, a ∈ s₁ ∧ a ∈ s₂
```

`Cedar.Data.Set.union_wf` (theorem, [line 518](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L518))

```lean
public theorem union_wf [LT α] [DecidableLT α] [StrictLT α] {s₁ s₂ : Set α} :
  s₁.WellFormed → s₂.WellFormed → WellFormed (s₁ ∪ s₂)
```

`Cedar.Data.Set.make_cons_eq_singleton_union` (theorem, [line 524](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L524))

```lean
public theorem make_cons_eq_singleton_union [LT α] [DecidableLT α] [StrictLT α] (a : α) (xs : List α) :
  Set.make (a :: xs) = Set.singleton a ∪ Set.make xs
```

`Cedar.Data.Set.append_eq_union` (theorem, [line 532](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L532))

> The `++` notation on sets  is definitionally `∪`.

```lean
public theorem append_eq_union [LT α] [DecidableLT α] (s₁ s₂ : Set α) :
  s₁ ++ s₂ = s₁ ∪ s₂
```

`Cedar.Data.Set.mem_union` (theorem, [line 537](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L537))

```lean
public theorem mem_union [LT α] [DecidableLT α] [StrictLT α] (s₁ s₂ : Set α) (a : α) :
  a ∈ s₁ ∪ s₂ ↔ (a ∈ s₁ ∨ a ∈ s₂)
```

`Cedar.Data.Set.prop_union_iff_prop_and` (theorem, [line 542](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L542))

```lean
public theorem prop_union_iff_prop_and [LT α] [DecidableLT α] [StrictLT α] (p : α → Prop) (s₁ s₂ : Set α) :
  ((∀ a ∈ s₁, p a) ∧ (∀ a ∈ s₂, p a)) ↔ ∀ a ∈ (s₁ ∪ s₂), p a
```

`Cedar.Data.Set.union_comm` (theorem, [line 562](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L562))

> Union is commutative even if its operands are not well-formed.

```lean
public theorem union_comm [LT α] [DecidableLT α] [StrictLT α] (s₁ s₂ : Set α) :
  s₁ ∪ s₂ = s₂ ∪ s₁
```

`Cedar.Data.Set.union_assoc` (theorem, [line 568](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L568))

> Union is associative even if its operands are not well-formed.

```lean
public theorem union_assoc [LT α] [DecidableLT α] [StrictLT α] (s₁ s₂ s₃ : Set α) :
  (s₁ ∪ s₂) ∪ s₃ = s₁ ∪ (s₂ ∪ s₃)
```

`Cedar.Data.Set.union_empty_right` (theorem, [line 574](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L574))

> Union with the empty set does not require well-formedness.

```lean
public theorem union_empty_right [LT α] [DecidableLT α] {s : Set α} :
  s ∪ Set.empty = s
```

`Cedar.Data.Set.union_empty_left` (theorem, [line 580](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L580))

> Union with the empty set does not require well-formedness.

```lean
public theorem union_empty_left [LT α] [DecidableLT α] {s : Set α} :
  Set.empty ∪ s = s
```

`Cedar.Data.Set.union_idempotent` (theorem, [line 586](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L586))

> Union with itself does not require well-formedness.

```lean
public theorem union_idempotent [LT α] [DecidableLT α] [StrictLT α] {s : Set α} :
  s ∪ s = s
```

> ### subset

`Cedar.Data.Set.elts_subset_then_subset` (theorem, [line 593](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L593))

```lean
public theorem elts_subset_then_subset [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] {xs ys : List α} :
  xs ⊆ ys → Set.make xs ⊆ Set.make ys
```

`Cedar.Data.Set.subset_def` (theorem, [line 606](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L606))

> Like `List.subset_def`, but lifted to Sets

```lean
public theorem subset_def [DecidableEq α] {s₁ s₂ : Set α} :
  s₁ ⊆ s₂ ↔ ∀ a, a ∈ s₁ → a ∈ s₂
```

`Cedar.Data.Set.subset_empty` (theorem, [line 621](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L621))

```lean
public theorem subset_empty [DecidableEq α] {s : Set α} :
  Set.empty ⊆ s
```

`Cedar.Data.Set.superset_empty_subset_empty` (theorem, [line 625](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L625))

```lean
public theorem superset_empty_subset_empty [DecidableEq α] {s₁ s₂ : Set α} :
  s₁ ⊆ s₂ → s₂.isEmpty → s₁.isEmpty
```

`Cedar.Data.Set.subset_iff_subset_elts` (theorem, [line 636](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L636))

```lean
public theorem subset_iff_subset_elts [DecidableEq α] {s₁ s₂ : Set α} :
  s₁ ⊆ s₂ ↔ s₁.elts ⊆ s₂.elts
```

`Cedar.Data.Set.subset_iff_eq` (theorem, [line 641](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L641))

```lean
public theorem subset_iff_eq [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] {s₁ s₂ : Set α} :
  WellFormed s₁ → WellFormed s₂ →
  ((s₁ ⊆ s₂ ∧ s₂ ⊆ s₁) ↔ s₁ = s₂)
```

`Cedar.Data.Set.subset_trans` (theorem, [line 648](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L648))

```lean
public theorem subset_trans [DecidableEq α] {s₁ s₂ s₃ : Set α} :
  s₁ ⊆ s₂ → s₂ ⊆ s₃ → s₁ ⊆ s₃
```

`Cedar.Data.Set.subset_refl` (theorem, [line 655](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L655))

```lean
public theorem subset_refl [DecidableEq α] {s : Set α} :
  s ⊆ s
```

`Cedar.Data.Set.mem_subset_mem` (theorem, [line 660](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L660))

```lean
public theorem mem_subset_mem [DecidableEq α] {a : α} {s₁ s₂ : Set α} :
  a ∈ s₁ → s₁ ⊆ s₂ → a ∈ s₂
```

`Cedar.Data.Set.subset_union` (theorem, [line 667](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L667))

```lean
public theorem subset_union [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] (s₁ s₂ : Set α) :
  s₁ ⊆ s₁ ∪ s₂
```

`Cedar.Data.Set.union_subset` (theorem, [line 674](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L674))

```lean
public theorem union_subset [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] {s₁ s₂ s₃ : Set α} :
  s₁ ∪ s₂ ⊆ s₃ ↔ s₁ ⊆ s₃ ∧ s₂ ⊆ s₃
```

`Cedar.Data.Set.union_subset_eq` (theorem, [line 693](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L693))

```lean
public theorem union_subset_eq [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] {s₁ s₂ : Set α} :
  s₁.WellFormed → s₂.WellFormed → s₁ ⊆ s₂ → s₁ ∪ s₂ = s₂
```

`Cedar.Data.Set.wellFormed_correct` (theorem, [line 703](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L703))

```lean
public theorem wellFormed_correct {α} [LT α] [StrictLT α] [DecidableLT α] {s : Set α} :
  s.wellFormed = true ↔ s.WellFormed
```

> ### map

`Cedar.Data.Set.map_wf` (theorem, [line 718](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L718))

```lean
public theorem map_wf [LT β] [DecidableLT β] [StrictLT β] (f : α → β) (s : Set α) :
  (s.map f).WellFormed
```

`Cedar.Data.Set.map_id` (theorem, [line 722](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L722))

```lean
public theorem map_id [LT α] [DecidableLT α] (s : Set α) :
  s.WellFormed → s.map id = s
```

`Cedar.Data.Set.mem_map` (theorem, [line 730](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L730))

> Analogue of `List.mem_map` but for sets

```lean
public theorem mem_map [LT β] [DecidableLT β] [StrictLT β] {b : β} {f : α → β} {s : Set α} :
  b ∈ s.map f ↔ ∃ a ∈ s, f a = b
```

`Cedar.Data.Set.map_congr` (theorem, [line 736](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L736))

> Analogue of `List.map_congr`, but for sets

```lean
public theorem map_congr [LT β] [DecidableLT β] {f g : α → β} {s : Set α} :
  (∀ a ∈ s, f a = g a) → s.map f = s.map g
```

`Cedar.Data.Set.isEmpty_map` (theorem, [line 747](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L747))

```lean
public theorem isEmpty_map [DecidableEq α] [LT β] [DecidableLT β] [DecidableEq β] {f : α → β} {s : Set α} :
  (s.map f).isEmpty = s.isEmpty
```

`Cedar.Data.Set.map_make` (theorem, [line 760](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L760))

```lean
public theorem map_make [LT α] [DecidableLT α] [StrictLT α] [LT β] [DecidableLT β] [StrictLT β] {f : α → β} {xs : List α} :
  (Set.make xs).map f = Set.make (xs.map f)
```

`Cedar.Data.Set.map_def` (theorem, [line 768](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L768))

```lean
public theorem map_def [LT β] [DecidableLT β] (f : α → β) (s : Set α) :
  s.map f = Set.make (s.elts.map f)
```

`Cedar.Data.Set.map_union` (theorem, [line 773](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L773))

> `Set.map` distributes over `∪`.

```lean
public theorem map_union [LT α] [DecidableLT α] [StrictLT α] [LT β] [DecidableLT β] [StrictLT β]
  (f : α → β) (s₁ s₂ : Set α) :
  (s₁ ∪ s₂).map f = s₁.map f ∪ s₂.map f
```

> ### filter and differences

`Cedar.Data.Set.filter_wf` (theorem, [line 789](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L789))

```lean
public theorem filter_wf [LT α] [DecidableLT α] [StrictLT α] (p : α → Bool) (s : Set α) :
  WellFormed s →
  WellFormed (s.filter p)
```

`Cedar.Data.Set.mem_filter` (theorem, [line 797](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L797))

```lean
public theorem mem_filter [LT α] [DecidableLT α] [StrictLT α] (p : α → Bool) (s : Set α) (e : α):
  e ∈ s.filter p ↔ (e ∈ s ∧ p e)
```

`Cedar.Data.Set.difference_wf` (theorem, [line 804](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L804))

```lean
public theorem difference_wf [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] (s₁ s₂ : Set α) :
  WellFormed s₁ →
  WellFormed (s₁.difference s₂)
```

`Cedar.Data.Set.mem_difference` (theorem, [line 810](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L810))

```lean
public theorem mem_difference [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] (s₁ s₂ : Set α) (e : α):
  e ∈ s₁.difference s₂ ↔ (e ∈ s₁ ∧ e ∉ s₂)
```

`Cedar.Data.Set.difference_subset` (theorem, [line 814](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L814))

```lean
public theorem difference_subset [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] (s₁ s₂ : Set α) :
  (s₁.difference s₂) ⊆ s₁
```

> ### all and any

`Cedar.Data.Set.all_eq_true` (theorem, [line 826](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L826))

> Like `List.all_eq_true`, but for `Set.all`

```lean
public theorem all_eq_true {f : α → Bool} {s : Set α} :
  s.all f = true ↔ ∀ x ∈ s, f x = true
```

`Cedar.Data.Set.all_eq_false` (theorem, [line 833](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L833))

> Like `List.all_eq_false`, but for `Set.all`

```lean
public theorem all_eq_false {f : α → Bool} {s : Set α} :
  s.all f = false ↔ ∃ x ∈ s, ¬ f x = true
```

`Cedar.Data.Set.any_eq_true` (theorem, [line 840](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L840))

> Like `List.any_eq_true`, but for `Set.any`

```lean
public theorem any_eq_true {f : α → Bool} {s : Set α} :
  s.any f = true ↔ ∃ x ∈ s, f x = true
```

`Cedar.Data.Set.any_eq_false` (theorem, [line 847](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L847))

> Like `List.any_eq_false`, but for `Set.any`

```lean
public theorem any_eq_false {f : α → Bool} {s : Set α} :
  s.any f = false ↔ ∀ x ∈ s, ¬ f x = true
```

> ### map₁, all₁, and any₁

`Cedar.Data.Set.map₁_eq_map` (theorem, [line 855](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L855))

```lean
public theorem map₁_eq_map [LT α] [DecidableLT α] [LT β] [DecidableLT β] (f : α → β) (s : Set α) :
  (s.map₁ λ ⟨elt, _⟩ => f elt) = s.map f
```

`Cedar.Data.Set.all₁_eq_all` (theorem, [line 860](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L860))

```lean
public theorem all₁_eq_all {s : Set α} {f : α → Bool} :
  (s.all₁ λ ⟨elt, _⟩ => f elt) = s.all f
```

`Cedar.Data.Set.any₁_eq_any` (theorem, [line 865](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L865))

```lean
public theorem any₁_eq_any {s : Set α} {f : α → Bool} :
  (s.any₁ λ ⟨elt, _⟩ => f elt) = s.any f
```

> ### product

`Cedar.Data.Set.mem_product` (theorem, [line 873](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L873))

> An element is in `s₁.product s₂` iff its components are in `s₁` and `s₂`.

```lean
public theorem mem_product {α β} {a : α} {b : β} {s₁ : Set α} {s₂ : Set β} :
  (a, b) ∈ s₁.product s₂ ↔ a ∈ s₁ ∧ b ∈ s₂
```

`Cedar.Data.Set.product_empty` (theorem, [line 887](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L887))

```lean
public theorem product_empty {α β} (s : Set α) :
  s.product (Set.empty : Set β) = Set.empty
```

`Cedar.Data.Set.empty_product` (theorem, [line 892](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean#L892))

```lean
public theorem empty_product {α β} (s : Set β) :
  (Set.empty : Set α).product s = Set.empty
```

## Depends on

- [Canonical list-based sets](../../data/set.md)
- [List properties](list/basic.md)

## Proof depends on

- [Properties of list canonicalization](list/canonical.md)
- [Properties of Lists](list/lemmas.md)

## Sources

- [Cedar/Thm/Data/Set.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Set.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Data.Set.json)
