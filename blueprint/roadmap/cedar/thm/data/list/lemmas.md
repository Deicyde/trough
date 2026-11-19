---
catalog: module
lean: List.any_of_mem, List.all_pmap_subtype, List.map_congr, List.map_eq_doubleton, List.map_pmap_subtype, List.map_pmap_subtype_snd, List.attach_def, List.mem_attach₂, List.mem_attach₂_iff, List.all_attach₂, List.all_attach₂_snd, List.map₁_eq_map, List.map₂_eq_map, List.map₃_eq_map, List.map₂_eq_map_snd, List.map₃_eq_map_snd, List.exists_iff_mem_flatMap, Cedar.List.forall₂_nil_left_iff, Cedar.List.forall₂_nil_right_iff, Cedar.List.Forall₂.imp, Cedar.List.forall₂_cons_left_iff, Cedar.List.forall₂_cons_right_iff, List.forall₂_singleton_right_iff, List.forall₂_pair_right_iff, List.forall₂_implies_all_left, List.forall₂_implies_all_right, List.forall₂_iff_map_eq, List.forall₂_fun_subset_implies, List.forall₂_fun_equiv_implies, List.map_preserves_forall₂, List.forall₂_swap, List.forall₂_compose_mapM_right, List.forall₂_eq_implies_filterMap, List.forall₂_trans_ish, List.forall₂_find?_some, List.forall₂_find?_none, List.mapM_some, List.mapM_isSome, List.mapM₁_def, List.mapM₁_eq_mapM, List.mapM₂_eq_mapM, List.mapM₂_eq_map_snd, List.mapM₃_eq_mapM, List.mapM_implies_nil, List.mapM_head_tail, List.mapM'_preserves_length, List.mapM_preserves_length, List.not_mem_implies_not_mem_mapM_key_id, List.mapM'_ok_iff_forall₂, List.mapM'_some_iff_forall₂, List.mapM_ok_iff_forall₂, List.mapM_some_iff_forall₂, List.mapM_implies_forall₂, List.mapM_implies_forall₂_option, List.mapM'_ok_implies_all_ok, List.mapM_ok_implies_all_ok, List.all_ok_implies_mapM'_ok, List.all_ok_implies_mapM_ok, List.mapM'_ok_implies_all_from_ok, List.mapM_ok_implies_all_from_ok, List.all_from_ok_implies_mapM'_ok, List.all_from_ok_implies_mapM_ok, List.mapM'_error_implies_exists_error, List.mapM_error_implies_exists_error, List.filterMapM_error_implies_exists_error, List.element_error_implies_mapM'_error, List.element_error_implies_mapM_error, List.element_to_option_none_implies_mapM_none, List.mapM'_ok_eq_filterMap, List.mapM_ok_eq_filterMap, List.mapM'_some_implies_all_some, List.mapM_some_implies_all_some, List.mem_mapM_some_implies_exists_unmapped_helper, List.mem_mapM_some_implies_exists_unmapped, List.all_some_implies_mapM'_some, List.all_some_implies_mapM_some, List.mapM'_some_implies_all_from_some, List.mapM_some_implies_all_from_some, List.all_from_some_implies_mapM'_some, List.all_from_some_implies_mapM_some, List.mapM'_none_iff_exists_none, List.mapM_none_iff_exists_none, List.mapM'_some_eq_filterMap, List.mapM_some_eq_filterMap, List.mapM'_some_subset, List.mapM_some_subset, List.forall₂_implies_mapM_eq, List.mapM'_congr, List.mapM_congr, List.to_option_distr_mapM', List.to_option_distr_mapM, List.mapM_to_option_congr, List.foldl_pmap_subtype, List.foldl_congr, List.foldlM_of_assoc_some, List.foldlM_of_assoc_none', List.foldlM_of_assoc_none, List.foldlM_of_assoc, List.find?_pair_map, List.find?_fst_map_implies_find?, List.find?_implies_find?_fst_map, List.find?_implies_append_find?, List.not_find?_some_iff_find?_none, List.find?_exact_iff_mem, Cedar.List.filterMap_congr, List.filterMap_empty_iff_all_none, List.filterMap_nonempty_iff_exists_some, List.f_implies_g_then_subset, List.mapM_forM, List.forM_mapM, List.forM_ok_implies_all_ok, List.forM_ok_implies_all_ok', List.all_ok_implies_forM_ok, List.removeAll_singleton_cons_of_neq, List.removeAll_singleton_cons_of_eq, List.mem_removeAll_singleton_of_eq, List.removeAll_singleton_equiv, List.length_removeAll_le, List.mem_pmap_subtype, List.find?_compose, List.mem_implies_mem_eraseDups, List.mem_eraseDups_implies_mem, List.mem_iff_mem_eraseDups, List.mapM_preserves_SortedBy, List.map_restricted_id, List.findSome?_unique, List.find?_unique_entry, List.find?_stronger_pred, List.mem_of_map_implies_exists_unmapped, List.mem_map_iff_find?, List.mem_implies_find?, List.filterMap_eq_filterMap, List.find?_filter_if_find?, List.find?_filter_sorted, List.anyM_some_implies_any, List.ternary_any_some_implies_any
statement: formalized
proof: formalized
---

# Properties of Lists

`Cedar.Thm.Data.List.Lemmas`, in [Cedar/Thm/Data/List/Lemmas.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean).

> This file contains useful lemmas about standard list functions and
> our custom variations on these.

> ### any

`List.any_of_mem` (theorem, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L38))

```lean
public theorem any_of_mem {f : α → Bool} {x : α} {xs : List α}
  (h₁ : x ∈ xs)
  (h₂ : f x) :
  any xs f = true
```

> ### all

`List.all_pmap_subtype` (theorem, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L57))

> Copied from Mathlib. We can delete this if it gets added to Batteries.

```lean
public theorem all_pmap_subtype
  {p : α → Prop}
  (f : α → Bool)
  (as : List α)
  (h : ∀ a, a ∈ as → p a)
  : List.all (List.pmap Subtype.mk as h) (λ x : { a : α // p a } => f x.val)
    =
    List.all as f
```

> ### map, map₁, map₂, map₃, and `attach` variants

`List.map_congr` (theorem, [line 73](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L73))

> Copied from Mathlib. We can delete this if it gets added to Batteries.

```lean
public theorem map_congr {f g : α → β} : ∀ {l : List α},
  (∀ x ∈ l, f x = g x) → map f l = map g l
```

`List.map_eq_doubleton` (theorem, [line 85](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L85))

> Similar to the standard library's `map_eq_singleton_iff`, but for doubleton.
>
> We could probably make this an iff but currently don't need to.

```lean
public theorem map_eq_doubleton {f : α → β} {xs : List α} {y₁ y₂ : β} :
  xs.map f = [y₁, y₂] →
  ∃ x₁ x₂, xs = [x₁, x₂]
```

`List.map_pmap_subtype` (theorem, [line 98](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L98))

> Copied from Mathlib. We can delete this if it gets added to Batteries.

```lean
public theorem map_pmap_subtype
  {p : α → Prop}
  (f : α → β)
  (as : List α)
  (h : ∀ a, a ∈ as → p a)
  : List.map (λ x : { a : α // p a } => f x.val) (List.pmap Subtype.mk as h)
    =
    List.map f as
```

`List.map_pmap_subtype_snd` (theorem, [line 116](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L116))

> Not actually a special case of `map_pmap_subtype` -- you can use this in
> places you can't use `map_pmap_subtype` because the LHS function (being
> mapped) doesn't fit the `map_pmap_subtype` form but does fit this form (where
> the application of `f` is not the outermost AST node of the function,
> basically)

```lean
public theorem map_pmap_subtype_snd
  {p : (α × β) → Prop}
  (f : β → γ)
  (xs : List (α × β))
  (h : ∀ pair ∈ xs, p pair)
  : List.map (λ x : { pair : (α × β) // p pair } => (x.val.fst, f x.val.snd)) (List.pmap Subtype.mk xs h)
    =
    xs.map λ pair => (pair.fst, f pair.snd)
```

`List.attach_def` (theorem, [line 127](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L127))

```lean
public theorem attach_def {as : List α} :
  as.attach = pmap Subtype.mk as λ _ => id
```

`List.mem_attach₂` (theorem, [line 132](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L132))

```lean
public theorem mem_attach₂ [SizeOf α] [SizeOf β] {as : List (α × β)} {pair : {x : α × β // sizeOf x.snd < 1 + sizeOf as}} :
  pair ∈ as.attach₂ → (pair.val.fst, pair.val.snd) ∈ as
```

`List.mem_attach₂_iff` (theorem, [line 140](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L140))

```lean
public theorem mem_attach₂_iff [SizeOf α] [SizeOf β] {xs : List (α × β)} {pair : {x : α × β // sizeOf x.snd < 1 + sizeOf xs}} :
  pair ∈ xs.attach₂ ↔ pair.val ∈ xs
```

`List.all_attach₂` (theorem, [line 151](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L151))

```lean
public theorem all_attach₂ [SizeOf α] [SizeOf β] {as : List (α × β)} {f : (α × β) → Bool} :
  as.attach₂.all (λ ⟨pair, _⟩ => f pair) = as.all f
```

`List.all_attach₂_snd` (theorem, [line 158](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L158))

```lean
public theorem all_attach₂_snd [SizeOf α] [SizeOf β] {as : List (α × β)} {f : β → Bool} :
  as.attach₂.all (λ ⟨(_, b), _⟩ => f b) = as.all λ (_, b) => f b
```

`List.map₁_eq_map` (theorem, [line 164](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L164))

```lean
public theorem map₁_eq_map (f : α → β) (as : List α) :
  as.map₁ (λ x : {x // x ∈ as} => f x.val) =
  as.map f
```

`List.map₂_eq_map` (theorem, [line 170](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L170))

```lean
public theorem map₂_eq_map {α : Type u} {β : Type v} [SizeOf α] [SizeOf β] {xs : List (α × β)} (f : (α × β) → γ) :
  xs.map₂ (λ x : { x : α × β // sizeOf x.snd < 1 + sizeOf xs } => f x.1) =
  xs.map f
```

`List.map₃_eq_map` (theorem, [line 176](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L176))

```lean
public theorem map₃_eq_map {α : Type u} {β : Type v} [SizeOf α] [SizeOf β] {xs : List (α × β)} (f : (α × β) → γ) :
  xs.map₃ (λ x : { x : α × β // sizeOf x.snd < 1 + (1 + sizeOf xs) } => f x.1) =
  xs.map f
```

`List.map₂_eq_map_snd` (theorem, [line 188](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L188))

> Not actually a special case of `map₂_eq_map` -- you can use this in places you
> can't use `map₂_eq_map` because the LHS function (being mapped) doesn't fit
> the `map₂_eq_map` form but does fit this form (where the application of `f` is
> not the outermost AST node of the function, basically)

```lean
public theorem map₂_eq_map_snd {α : Type u} {β : Type v} [SizeOf α] [SizeOf β] {xs : List (α × β)} (f : β → γ) :
  xs.map₂ (λ x : {x : α × β // sizeOf x.snd < 1 + sizeOf xs } => match x with | ⟨(a, b), _⟩ => (a, f b)) =
  xs.map λ (a, b) => (a, f b)
```

`List.map₃_eq_map_snd` (theorem, [line 197](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L197))

> same as `map₂_eq_map_snd` but for `map₃`

```lean
public theorem map₃_eq_map_snd [SizeOf α] [SizeOf β] {xs : List (α × β)} (f : β → γ) :
  xs.map₃ (λ x : {x : α × β // sizeOf x.snd < 1 + (1 + sizeOf xs) } => match x with | ⟨(a, b), _⟩ => (a, f b)) =
  xs.map λ (a, b) => (a, f b)
```

> ### flatMap

`List.exists_iff_mem_flatMap` (theorem, [line 210](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L210))

> As of this writing, the standard-library lemma `List.exists_of_mem_flatMap` is a
> `→`, but it's trivial to extend it to `↔` and makes some things easier, so we do
> that here

```lean
public theorem exists_iff_mem_flatMap {α β} [DecidableEq β] {f : α → List β} {xs : List α} {b : β} :
  b ∈ List.flatMap f xs ↔ ∃ a ∈ xs, b ∈ f a
```

> ### Forall₂

> The following lemmas are copied from Mathlib. They live in `Cedar.List` rather
> than `List` so that a file can import both Cedar and Mathlib without a
> duplicate-declaration error. Code inside the `Cedar` namespace can still refer
> to them as `List.<name>`, since Lean resolves names in enclosing namespaces first.

`Cedar.List.forall₂_nil_left_iff` (theorem, [line 231](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L231))

> Copied from Mathlib

```lean
public theorem forall₂_nil_left_iff {l} : Forall₂ R nil l ↔ l = nil
```

`Cedar.List.forall₂_nil_right_iff` (theorem, [line 237](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L237))

> Copied from Mathlib

```lean
public theorem forall₂_nil_right_iff {l} : Forall₂ R l nil ↔ l = nil
```

`Cedar.List.Forall₂.imp` (theorem, [line 243](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L243))

> Copied from Mathlib

```lean
public theorem Forall₂.imp (H : ∀ a b, R a b → S a b) {l₁ l₂} (h : Forall₂ R l₁ l₂) : Forall₂ S l₁ l₂
```

`Cedar.List.forall₂_cons_left_iff` (theorem, [line 249](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L249))

> Copied from Mathlib

```lean
public theorem forall₂_cons_left_iff {a l u} :
    Forall₂ R (a :: l) u ↔ ∃ b u', R a b ∧ Forall₂ R l u' ∧ u = b :: u'
```

`Cedar.List.forall₂_cons_right_iff` (theorem, [line 262](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L262))

> Copied from Mathlib

```lean
public theorem forall₂_cons_right_iff {b l u} :
    Forall₂ R u (b :: l) ↔ ∃ a u', R a b ∧ Forall₂ R u' l ∧ u = a :: u'
```

`List.forall₂_singleton_right_iff` (theorem, [line 278](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L278))

```lean
public theorem forall₂_singleton_right_iff {α β} {R : α → β → Prop} {xs : List α} {y : β} :
  Forall₂ R xs [y] ↔ ∃ x, R x y ∧ xs = [x]
```

`List.forall₂_pair_right_iff` (theorem, [line 292](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L292))

```lean
public theorem forall₂_pair_right_iff {α β} {R : α → β → Prop} {xs : List α} {y₁ y₂ : β} :
  Forall₂ R xs [y₁, y₂] ↔ ∃ x₁ x₂, R x₁ y₁ ∧ R x₂ y₂ ∧ xs = [x₁, x₂]
```

`List.forall₂_implies_all_left` (theorem, [line 311](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L311))

> Note the converse is not true:
> counterexample `R` is `=`, `xs` is `[1]`, `ys` is `[1, 2]`

```lean
public theorem forall₂_implies_all_left {α β} {R : α → β → Prop} {xs : List α} {ys : List β} :
  List.Forall₂ R xs ys →
  ∀ x ∈ xs, ∃ y ∈ ys, R x y
```

`List.forall₂_implies_all_right` (theorem, [line 330](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L330))

```lean
public theorem forall₂_implies_all_right {α β} {R : α → β → Prop} {xs : List α} {ys : List β} :
  List.Forall₂ R xs ys →
  ∀ y ∈ ys, ∃ x ∈ xs, R x y
```

`List.forall₂_iff_map_eq` (theorem, [line 349](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L349))

```lean
public theorem forall₂_iff_map_eq {α β γ} {f : α → γ} {g : β → γ} {xs : List α} {ys : List β} :
  List.Forall₂ (λ x y => f x = g y) xs ys ↔
  xs.map f = ys.map g
```

`List.forall₂_fun_subset_implies` (theorem, [line 370](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L370))

```lean
public theorem forall₂_fun_subset_implies {R : α → β → Prop} {xs xs' : List α} {ys ys' : List β} :
  List.Forall₂ R xs ys →
  List.Forall₂ R xs' ys' →
  (∀ {x y y'}, R x y → R x y' → y = y') →
  xs ⊆ xs' →
  ys ⊆ ys'
```

`List.forall₂_fun_equiv_implies` (theorem, [line 390](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L390))

> The converse (ys ≡ ys' → xs ≡ xs') doesn't hold without requiring R to be
> injective (as well as functional).

```lean
public theorem forall₂_fun_equiv_implies {R : α → β → Prop} {xs xs' : List α} {ys ys' : List β} :
  List.Forall₂ R xs ys →
  List.Forall₂ R xs' ys' →
  (∀ {x y y'}, R x y → R x y' → y = y') →
  xs ≡ xs' →
  ys ≡ ys'
```

`List.map_preserves_forall₂` (theorem, [line 404](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L404))

```lean
public theorem map_preserves_forall₂
  {f : α → α'}
  {g : β → β'}
  {p₁ : α → β → Prop}
  {p₂ : α' → β' → Prop}
  {xs : List α} {ys : List β}
  (h : ∀ x y, p₁ x y → p₂ (f x) (g y))
  (hforall₂ : List.Forall₂ p₁ xs ys) :
  List.Forall₂ p₂ (xs.map f) (ys.map g)
```

`List.forall₂_swap` (theorem, [line 423](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L423))

```lean
public theorem forall₂_swap
  {R : α → β → Prop} {xs : List α} {ys : List β}
  (hforall₂ : List.Forall₂ (λ y x => R x y) ys xs) :
  List.Forall₂ R xs ys
```

`List.forall₂_compose_mapM_right` (theorem, [line 440](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L440))

> Applying `mapM` on the RHS list of `Forall₂`
> leads to new `Forall₂` relation if certain
> conditions are met.

```lean
public theorem forall₂_compose_mapM_right
  {l₁ : List α} {l₂ : List β} {l₃ : List γ}
  {R₁ : α → β → Prop}
  {R₂ : α → γ → Prop}
  {f : β → Option γ}
  (h : List.Forall₂ R₁ l₁ l₂)
  (hmapM : List.mapM f l₂ = .some l₃)
  (hf : ∀ a b, R₁ a b → ∃ c, f b = .some c ∧ R₂ a c) :
  List.Forall₂ R₂ l₁ l₃
```

`List.forall₂_eq_implies_filterMap` (theorem, [line 473](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L473))

```lean
public theorem forall₂_eq_implies_filterMap
  {l₁ : List α} {l₂ : List β} {p : α → β → Prop}
  {f : α → Option β}
  (h : List.Forall₂ p l₁ l₂)
  (hp : ∀ a b, p a b → f a = .some b) :
  l₁.filterMap f = l₂
```

`List.forall₂_trans_ish` (theorem, [line 489](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L489))

> kind of a transitivity property, if you squint

```lean
public theorem forall₂_trans_ish {xs : List α} {ys : List β} {zs : List γ} {Q : α → β → Prop} {R : α → γ → Prop} {S : β → γ → Prop}
  (h₁ : List.Forall₂ Q xs ys)
  (h₂ : List.Forall₂ R xs zs) :
  (∀ {a b c}, Q a b → R a c → S b c) →
  List.Forall₂ S ys zs
```

`List.forall₂_find?_some` (theorem, [line 509](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L509))

> In key-preserving related lists, an entry found for a key has a related entry found for it.

```lean
public theorem forall₂_find?_some {α β} [DecidableEq α]
  {r : α × β → α × β → Prop} {xs ys : List (α × β)} {k : α} {x : α × β}
  (hkeys : ∀ x y, r x y → y.fst = x.fst)
  (hrel : List.Forall₂ r xs ys)
  (hfind : xs.find? (·.fst == k) = some x) :
  ∃ y, ys.find? (·.fst == k) = some y ∧ r x y
```

`List.forall₂_find?_none` (theorem, [line 528](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L528))

> In key-preserving related lists, a key absent from one list is absent from the other.

```lean
public theorem forall₂_find?_none {α β} [DecidableEq α]
  {r : α × β → α × β → Prop} {xs ys : List (α × β)} {k : α}
  (hkeys : ∀ x y, r x y → y.fst = x.fst)
  (hrel : List.Forall₂ r xs ys)
  (hfind : xs.find? (·.fst == k) = none) :
  ys.find? (·.fst == k) = none
```

> ### mapM, mapM', mapM₁, and mapM₂

`List.mapM_some` (theorem, [line 546](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L546))

```lean
public theorem mapM_some {xs : List α} :
  xs.mapM some = some xs
```

`List.mapM_isSome` (theorem, [line 556](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L556))

> `mapM` succeeds exactly when every application succeeds.

```lean
public theorem mapM_isSome {xs : List α} {f : α → Option β} :
    (xs.mapM f).isSome = xs.all (fun value => (f value).isSome)
```

`List.mapM₁_def` (theorem, [line 600](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L600))

> Equation lemma for `List.mapM₁`, for clients that cannot unfold it.

```lean
public theorem mapM₁_def [Monad m] {α β} (xs : List α) (f : {x : α // x ∈ xs} → m β) :
  xs.mapM₁ f = xs.attach.mapM f
```

`List.mapM₁_eq_mapM` (theorem, [line 604](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L604))

```lean
public theorem mapM₁_eq_mapM [Monad m] [LawfulMonad m]
  (f : α → m β)
  (as : List α) :
  List.mapM₁ as (λ x : { x // x ∈ as } => f x.val) =
  List.mapM f as
```

`List.mapM₂_eq_mapM` (theorem, [line 612](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L612))

```lean
public theorem mapM₂_eq_mapM [Monad m] [LawfulMonad m] [SizeOf α] [SizeOf β]
  (f : (α × β) → m γ)
  (as : List (α × β)) :
  List.mapM₂ as (λ x : { _x // _ } => f x.val) =
  List.mapM f as
```

`List.mapM₂_eq_map_snd` (theorem, [line 624](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L624))

> See notes on `map₂_eq_map_snd`. This has a similar relationship to `mapM₂_eq_mapM`
> as `map₂_eq_map_snd` does to `map₂_eq_map`.

```lean
public theorem mapM₂_eq_map_snd {α : Type u} {β : Type v} [SizeOf α] [SizeOf β] [Monad m] [LawfulMonad m] {xs : List (α × β)} (f : β → m γ) :
  (xs.mapM₂ (λ x : {x : α × β // sizeOf x.snd < 1 + sizeOf xs } => match x with | ⟨(a, b), _⟩ => do pure (a, ← f b))) =
  (xs.mapM λ (a, b) => do pure (a, ← f b))
```

`List.mapM₃_eq_mapM` (theorem, [line 631](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L631))

```lean
public theorem mapM₃_eq_mapM [Monad m] [LawfulMonad m] [SizeOf α] [SizeOf β]
  (f : (α × β) → m γ)
  (as : List (α × β)) :
  List.mapM₃ as (λ x : { x // sizeOf x.snd < 1 + (1 + sizeOf as) } => f x.val) =
  List.mapM f as
```

`List.mapM_implies_nil` (theorem, [line 639](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L639))

```lean
public theorem mapM_implies_nil {f : α → Except β γ} {as : List α}
  (h₁ : List.mapM f as = Except.ok []) :
  as = []
```

`List.mapM_head_tail` (theorem, [line 652](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L652))

```lean
public theorem mapM_head_tail {α β γ} {f : α → Except β γ} {x : α} {xs : List α} {y : γ} {ys : List γ} :
  (List.mapM f (x :: xs)) = Except.ok (y :: ys) →
  (List.mapM f xs) = Except.ok ys
```

`List.mapM'_preserves_length` (theorem, [line 662](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L662))

```lean
public theorem mapM'_preserves_length :
  List.mapM' f xs = Except.ok ys →
  xs.length = ys.length
```

`List.mapM_preserves_length` (theorem, [line 683](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L683))

```lean
public theorem mapM_preserves_length :
  List.mapM f xs = Except.ok ys →
  xs.length = ys.length
```

`List.not_mem_implies_not_mem_mapM_key_id` (theorem, [line 690](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L690))

```lean
public theorem not_mem_implies_not_mem_mapM_key_id {α β : Type} {ks : List α} {kvs : List (α × β)} {fn : α → Option β} {k: α}
  (hm : ks.mapM (λ k => do (k, ←fn k)) = some kvs)
  (hl : k ∉ ks) :
  ∀ v, (k, v) ∉ kvs
```

`List.mapM'_ok_iff_forall₂` (theorem, [line 713](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L713))

```lean
public theorem mapM'_ok_iff_forall₂ {α β γ} {f : α → Except γ β} {xs : List α} {ys : List β} :
  List.mapM' f xs = .ok ys ↔
  List.Forall₂ (λ x y => f x = .ok y) xs ys
```

`List.mapM'_some_iff_forall₂` (theorem, [line 756](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L756))

> Copy of mapM'_ok_iff_forall₂ but for option instead of exception

```lean
public theorem mapM'_some_iff_forall₂ {α β} {f : α → Option β} {xs : List α} {ys : List β} :
  List.mapM' f xs = .some ys ↔
  List.Forall₂ (λ x y => f x = .some y) xs ys
```

`List.mapM_ok_iff_forall₂` (theorem, [line 816](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L816))

```lean
public theorem mapM_ok_iff_forall₂ {α β γ} {f : α → Except γ β} {xs : List α} {ys : List β} :
  List.mapM f xs = .ok ys ↔
  List.Forall₂ (λ x y => f x = .ok y) xs ys
```

`List.mapM_some_iff_forall₂` (theorem, [line 823](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L823))

```lean
public theorem mapM_some_iff_forall₂ {α β} {f : α → Option β} {xs : List α} {ys : List β} :
  List.mapM f xs = .some ys ↔
  List.Forall₂ (λ x y => f x = .some y) xs ys
```

`List.mapM_implies_forall₂` (theorem, [line 836](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L836))

> Introduces `forall₂` through the input output relation
> of a `f` through `List.mapM`. This is slightly stronger
> than the forward direction of `mapM_ok_iff_forall₂`
> since it allowed an extra `x ∈ xs` condition in `h`.

```lean
public theorem mapM_implies_forall₂
  {f : α → Except ε β}
  {p : α → β → Prop}
  {xs : List α} {ys : List β}
  (h : ∀ x y, x ∈ xs → f x = .ok y → p x y)
  (hmapM : List.mapM f xs = .ok ys) :
  List.Forall₂ p xs ys
```

`List.mapM_implies_forall₂_option` (theorem, [line 870](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L870))

> Same as `mapM_implies_forall₂` but for `Option`

```lean
public theorem mapM_implies_forall₂_option
  {f : α → Option β}
  {p : α → β → Prop}
  {xs : List α} {ys : List β}
  (h : ∀ x y, x ∈ xs → f x = .some y → p x y)
  (hmapM : List.mapM f xs = .some ys) :
  List.Forall₂ p xs ys
```

`List.mapM'_ok_implies_all_ok` (theorem, [line 908](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L908))

> Note that the converse is not true:
> counterexample `xs` is `[1]`, `ys` is `[1, 2]`, `f` is `Except.ok`
>
> But for a limited converse, see `all_ok_implies_mapM'_ok`

```lean
public theorem mapM'_ok_implies_all_ok {α β γ} {f : α → Except γ β} {xs : List α} {ys : List β} :
  List.mapM' f xs = .ok ys →
  ∀ x ∈ xs, ∃ y ∈ ys, f x = .ok y
```

`List.mapM_ok_implies_all_ok` (theorem, [line 915](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L915))

```lean
public theorem mapM_ok_implies_all_ok {α β γ} {f : α → Except γ β} {xs : List α} {ys : List β} :
  List.mapM f xs = .ok ys →
  ∀ x ∈ xs, ∃ y ∈ ys, f x = .ok y
```

`List.all_ok_implies_mapM'_ok` (theorem, [line 922](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L922))

```lean
public theorem all_ok_implies_mapM'_ok {α β γ} {f : α → Except γ β} {xs : List α} :
  (∀ x ∈ xs, ∃ y, f x = .ok y) →
  ∃ ys, List.mapM' f xs = .ok ys
```

`List.all_ok_implies_mapM_ok` (theorem, [line 936](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L936))

```lean
public theorem all_ok_implies_mapM_ok {α β γ} {f : α → Except γ β} {xs : List α} :
  (∀ x ∈ xs, ∃ y, f x = .ok y) →
  ∃ ys, List.mapM f xs = .ok ys
```

`List.mapM'_ok_implies_all_from_ok` (theorem, [line 949](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L949))

> Note that the converse is not true:
> counterexample `ys` is `[1]`, `xs` is `[1, 2]`, `f` is `Except.ok`
>
> But for a limited converse, see `all_from_ok_implies_mapM'_ok`

```lean
public theorem mapM'_ok_implies_all_from_ok {α β γ} {f : α → Except γ β} {xs : List α} {ys : List β} :
  List.mapM' f xs = .ok ys →
  ∀ y ∈ ys, ∃ x ∈ xs, f x = .ok y
```

`List.mapM_ok_implies_all_from_ok` (theorem, [line 956](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L956))

```lean
public theorem mapM_ok_implies_all_from_ok {α β γ} {f : α → Except γ β} {xs : List α} {ys : List β} :
  List.mapM f xs = .ok ys →
  ∀ y ∈ ys, ∃ x ∈ xs, f x = .ok y
```

`List.all_from_ok_implies_mapM'_ok` (theorem, [line 963](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L963))

```lean
public theorem all_from_ok_implies_mapM'_ok {α β γ} {f : α → Except γ β} {ys : List β} :
  (∀ y ∈ ys, ∃ x, f x = .ok y) →
  ∃ xs, List.mapM' f xs = .ok ys
```

`List.all_from_ok_implies_mapM_ok` (theorem, [line 977](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L977))

```lean
public theorem all_from_ok_implies_mapM_ok {α β γ} {f : α → Except γ β} {ys : List β} :
  (∀ y ∈ ys, ∃ x, f x = .ok y) →
  ∃ xs, List.mapM f xs = .ok ys
```

`List.mapM'_error_implies_exists_error` (theorem, [line 993](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L993))

> The converse is not true:
> counterexample `xs` is `[1, 2]` and `f` is `Except.error`.
> In that case, `f 2 = .error 2` but `xs.mapM' f = .error 1`.
>
> But for a limited converse, see `element_error_implies_mapM_error`

```lean
public theorem mapM'_error_implies_exists_error {α β γ} {f : α → Except γ β} {xs : List α} {e : γ} :
  List.mapM' f xs = .error e → ∃ x ∈ xs, f x = .error e
```

`List.mapM_error_implies_exists_error` (theorem, [line 1017](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1017))

```lean
public theorem mapM_error_implies_exists_error {α β γ} {f : α → Except γ β} {xs : List α} {e : γ} :
  List.mapM f xs = .error e → ∃ x ∈ xs, f x = .error e
```

`List.filterMapM_error_implies_exists_error` (theorem, [line 1023](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1023))

```lean
public theorem filterMapM_error_implies_exists_error {α β ε} {f : α → Except ε (Option β)} {xs : List α} {e : ε} :
  List.filterMapM f xs = .error e → ∃ x ∈ xs, f x = .error e
```

`List.element_error_implies_mapM'_error` (theorem, [line 1049](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1049))

> If applying `f` to any of `xs` produces an error, then `xs.mapM' f` must also
> produce an error (not necessarily the same error)
>
> Limited converse of `mapM'_error_implies_exists_error`

```lean
public theorem element_error_implies_mapM'_error {x : α} {xs : List α} {f : α → Except ε β} {e : ε} :
  x ∈ xs →
  f x = .error e →
  ∃ e', xs.mapM' f = .error e'
```

`List.element_error_implies_mapM_error` (theorem, [line 1060](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1060))

```lean
public theorem element_error_implies_mapM_error {x : α} {xs : List α} {f : α → Except ε β} {e : ε} :
  x ∈ xs →
  f x = .error e →
  ∃ e', xs.mapM f = .error e'
```

`List.element_to_option_none_implies_mapM_none` (theorem, [line 1068](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1068))

```lean
public theorem element_to_option_none_implies_mapM_none {α β ε} {ls : List α} {x : α}
  {f : α → Except ε β}
  (h₁ : x ∈ ls)
  (h₂ : (f x).toOption = none) :
  (List.mapM f ls).toOption = none
```

`List.mapM'_ok_eq_filterMap` (theorem, [line 1078](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1078))

```lean
public theorem mapM'_ok_eq_filterMap {α β} {f : α → Except ε β} {xs : List α} {ys : List β} :
  xs.mapM' f = .ok ys →
  xs.filterMap (λ x => match f x with | .ok y => some y | .error _ => none) = ys
```

`List.mapM_ok_eq_filterMap` (theorem, [line 1097](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1097))

```lean
public theorem mapM_ok_eq_filterMap {α β} {f : α → Except ε β} {xs : List α} {ys : List β} :
  xs.mapM f = .ok ys →
  xs.filterMap (λ x => match f x with | .ok y => some y | .error _ => none) = ys
```

`List.mapM'_some_implies_all_some` (theorem, [line 1110](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1110))

> Note that the converse is not true:
> counterexample `xs` is `[1]`, `ys` is `[1, 2]`, `f` is `Option.some`
>
> But for a limited converse, see `all_some_implies_mapM'_some`

```lean
public theorem mapM'_some_implies_all_some {α β} {f : α → Option β} {xs : List α} {ys : List β} :
  List.mapM' f xs = .some ys →
  ∀ x ∈ xs, ∃ y ∈ ys, f x = .some y
```

`List.mapM_some_implies_all_some` (theorem, [line 1117](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1117))

```lean
public theorem mapM_some_implies_all_some {α β} {f : α → Option β} {xs : List α} {ys : List β} :
  List.mapM f xs = .some ys →
  ∀ x ∈ xs, ∃ y ∈ ys, f x = .some y
```

`List.mem_mapM_some_implies_exists_unmapped_helper` (theorem, [line 1124](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1124))

```lean
public theorem mem_mapM_some_implies_exists_unmapped_helper {α β} {y : β} {f : α → Option β} {xs : List α} {ys : List β} :
  Forall₂ (fun x y => f x = some y) xs ys →
  y ∈ ys →
  (∃ x, x ∈ xs ∧ f x = some y)
```

`List.mem_mapM_some_implies_exists_unmapped` (theorem, [line 1150](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1150))

```lean
public theorem mem_mapM_some_implies_exists_unmapped {α β} {y : β} {f : α → Option β} {xs : List α} {ys : List β} :
  List.mapM f xs = some ys →
  y ∈ ys →
  ∃ x, x ∈ xs ∧ f x = .some y
```

`List.all_some_implies_mapM'_some` (theorem, [line 1160](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1160))

```lean
public theorem all_some_implies_mapM'_some {α β} {f : α → Option β} {xs : List α} :
  (∀ x ∈ xs, ∃ y, f x = some y) →
  ∃ ys, List.mapM' f xs = some ys
```

`List.all_some_implies_mapM_some` (theorem, [line 1174](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1174))

```lean
public theorem all_some_implies_mapM_some {α β} {f : α → Option β} {xs : List α} :
  (∀ x ∈ xs, ∃ y, f x = some y) →
  ∃ ys, List.mapM f xs = some ys
```

`List.mapM'_some_implies_all_from_some` (theorem, [line 1187](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1187))

> Note that the converse is not true:
> counterexample `ys` is `[1]`, `xs` is `[1, 2]`, `f` is `Option.some`
>
> But for a limited converse, see `all_from_some_implies_mapM'_some`

```lean
public theorem mapM'_some_implies_all_from_some {α β} {f : α → Option β} {xs : List α} {ys : List β} :
  List.mapM' f xs = .some ys →
  ∀ y ∈ ys, ∃ x ∈ xs, f x = .some y
```

`List.mapM_some_implies_all_from_some` (theorem, [line 1194](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1194))

```lean
public theorem mapM_some_implies_all_from_some {α β} {f : α → Option β} {xs : List α} {ys : List β} :
  List.mapM f xs = .some ys →
  ∀ y ∈ ys, ∃ x ∈ xs, f x = .some y
```

`List.all_from_some_implies_mapM'_some` (theorem, [line 1201](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1201))

```lean
public theorem all_from_some_implies_mapM'_some {α β} {f : α → Option β} {ys : List β} :
  (∀ y ∈ ys, ∃ x, f x = some y) →
  ∃ xs, List.mapM' f xs = some ys
```

`List.all_from_some_implies_mapM_some` (theorem, [line 1215](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1215))

```lean
public theorem all_from_some_implies_mapM_some {α β} {f : α → Option β} {ys : List β} :
  (∀ y ∈ ys, ∃ x, f x = some y) →
  ∃ xs, List.mapM f xs = some ys
```

`List.mapM'_none_iff_exists_none` (theorem, [line 1224](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1224))

```lean
public theorem mapM'_none_iff_exists_none {α β} {f : α → Option β} {xs : List α} :
  List.mapM' f xs = none ↔ ∃ x ∈ xs, f x = none
```

`List.mapM_none_iff_exists_none` (theorem, [line 1255](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1255))

```lean
public theorem mapM_none_iff_exists_none {α β} {f : α → Option β} {xs : List α} :
  List.mapM f xs = none ↔ ∃ x ∈ xs, f x = none
```

`List.mapM'_some_eq_filterMap` (theorem, [line 1261](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1261))

```lean
public theorem mapM'_some_eq_filterMap {α β} {f : α → Option β} {xs : List α} {ys : List β} :
  List.mapM' f xs = .some ys →
  List.filterMap f xs = ys
```

`List.mapM_some_eq_filterMap` (theorem, [line 1279](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1279))

```lean
public theorem mapM_some_eq_filterMap {α β} {f : α → Option β} {xs : List α} {ys : List β} :
  List.mapM f xs = .some ys →
  List.filterMap f xs = ys
```

`List.mapM'_some_subset` (theorem, [line 1286](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1286))

```lean
public theorem mapM'_some_subset {f : α → Option β} {xs xs' : List α} {ys : List β} :
  xs.mapM' f = some ys →
  xs' ⊆ xs →
  ∃ ys', xs'.mapM' f = some ys'
```

`List.mapM_some_subset` (theorem, [line 1306](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1306))

```lean
public theorem mapM_some_subset {f : α → Option β} {xs xs' : List α} {ys : List β} :
  xs.mapM f = some ys →
  xs' ⊆ xs →
  ∃ ys', xs'.mapM f = some ys'
```

`List.forall₂_implies_mapM_eq` (theorem, [line 1314](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1314))

```lean
public theorem forall₂_implies_mapM_eq {α₁ α₂ β ε} {xs : List α₁} {ys : List α₂} (f : α₁ → Except ε β) (g : α₂ → Except ε β):
  List.Forall₂ (fun x y => f x = g y) xs ys →
  List.mapM f xs =
  List.mapM g ys
```

`List.mapM'_congr` (theorem, [line 1328](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1328))

> our own variant of map_congr, for mapM'

```lean
public theorem mapM'_congr [Monad m] [LawfulMonad m] {f g : α → m β} : ∀ {l : List α},
  (∀ x ∈ l, f x = g x) → mapM' f l = mapM' g l
```

`List.mapM_congr` (theorem, [line 1338](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1338))

> our own variant of map_congr, for mapM

```lean
public theorem mapM_congr [Monad m] [LawfulMonad m] {f g : α → m β} : ∀ {l : List α},
  (∀ x ∈ l, f x = g x) → mapM f l = mapM g l
```

`List.to_option_distr_mapM'` (theorem, [line 1345](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1345))

```lean
public theorem to_option_distr_mapM' {α β ε} {l : List α} {f: α → Except ε β} :
  (List.mapM' f l).toOption = (List.mapM' (Except.toOption ∘ f) l)
```

`List.to_option_distr_mapM` (theorem, [line 1357](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1357))

```lean
public theorem to_option_distr_mapM {α β ε} {l : List α} {f: α → Except ε β} :
  (List.mapM f l).toOption = (List.mapM (Except.toOption ∘ f) l)
```

`List.mapM_to_option_congr` (theorem, [line 1363](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1363))

```lean
public theorem mapM_to_option_congr {α β ε₁ ε₂} {l : List α} {f: α → Except ε₁ β} {g: α → Except ε₂ β} :
  (∀ x ∈ l, (f x).toOption = (g x).toOption) →
  (List.mapM f l).toOption = (List.mapM g l).toOption
```

> ### foldl

`List.foldl_pmap_subtype` (theorem, [line 1372](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1372))

```lean
public theorem foldl_pmap_subtype
  {p : α → Prop}
  (f : β → α → β)
  (as : List α)
  (init : β)
  (h : ∀ a, a ∈ as → p a) :
  List.foldl (λ b (x : { a : α // p a }) => f b x.val) init (List.pmap Subtype.mk as h)
  =
  List.foldl f init as
```

`List.foldl_congr` (theorem, [line 1386](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1386))

```lean
public theorem foldl_congr {f g : β → α → β} {init : β} {l : List α} :
  (∀ b x, x ∈ l → f b x = g b x) → foldl f init l = foldl g init l
```

> ### foldlM

`List.foldlM_of_assoc_some` (theorem, [line 1403](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1403))

```lean
public theorem foldlM_of_assoc_some (f : α → α → Option α) (x₀ x₁ x₂ x₃ : α) (xs : List α)
  (h₁ : ∀ x₁ x₂ x₃,
    (do let x₄ ← f x₁ x₂ ; f x₄ x₃) =
    (do let x₄ ← f x₂ x₃ ; f x₁ x₄))
  (h₂ : f x₀ x₁ = some x₂)
  (h₃ : List.foldlM f x₂ xs = some x₃):
  (do let y ← List.foldlM f x₁ xs ; f x₀ y) = some x₃
```

`List.foldlM_of_assoc_none'` (theorem, [line 1438](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1438))

```lean
public theorem foldlM_of_assoc_none' (f : α → α → Option α) (x₀ x₁ x₂ : α) (xs : List α)
  (h₁ : ∀ x₁ x₂ x₃,
    (do let x₄ ← f x₁ x₂ ; f x₄ x₃) =
    (do let x₄ ← f x₂ x₃ ; f x₁ x₄))
  (h₂ : f x₀ x₁ = none)
  (h₃ : List.foldlM f x₁ xs = some x₂):
  f x₀ x₂ = none
```

`List.foldlM_of_assoc_none` (theorem, [line 1460](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1460))

```lean
public theorem foldlM_of_assoc_none (f : α → α → Option α) (x₀ x₁ x₂ : α) (xs : List α)
  (h₁ : ∀ x₁ x₂ x₃,
    (do let x₄ ← f x₁ x₂ ; f x₄ x₃) =
    (do let x₄ ← f x₂ x₃ ; f x₁ x₄))
  (h₂ : f x₀ x₁ = some x₂)
  (h₃ : List.foldlM f x₂ xs = none):
  (do let y ← List.foldlM f x₁ xs ; f x₀ y) = none
```

`List.foldlM_of_assoc` (theorem, [line 1494](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1494))

```lean
public theorem foldlM_of_assoc (f : α → α → Option α) (x₀ x₁ : α) (xs : List α)
  (h₁ : ∀ x₁ x₂ x₃,
    (do let x₄ ← f x₁ x₂ ; f x₄ x₃) =
    (do let x₄ ← f x₂ x₃ ; f x₁ x₄) ) :
  List.foldlM f x₀ (x₁ :: xs) =
  (do let y ← List.foldlM f x₁ xs ; f x₀ y)
```

> ### find?

`List.find?_pair_map` (theorem, [line 1524](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1524))

```lean
public theorem find?_pair_map {α β γ} [BEq α] (f : β → γ) (xs : List (α × β)) (k : α)  :
  Option.map (λ x => (x.fst, f x.snd)) (List.find? (λ x => x.fst == k) xs)  =
  List.find? (λ x => x.fst == k) (List.map (λ x => (x.fst, f x.snd)) xs)
```

`List.find?_fst_map_implies_find?` (theorem, [line 1551](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1551))

```lean
public theorem find?_fst_map_implies_find? {α β γ} [BEq α] {f : β → γ} {xs : List (α × β)} {k : α} {fx : α × γ}:
  List.find? (λ x => x.fst == k) (List.map (Prod.map id f) xs) = .some fx  →
  ∃ x, xs.find? (λ x => x.fst == k) = .some x ∧ fx = Prod.map id f x
```

`List.find?_implies_find?_fst_map` (theorem, [line 1571](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1571))

```lean
public theorem find?_implies_find?_fst_map
  {α β γ} [BEq α] [ReflBEq α]
  {l : List (α × β)}
  {k : α} {v : β}
  {f : α → β → γ}
  (h : List.find? (λ x => x.fst == k) l = some (k, v)) :
  List.find? (λ x => x.fst == k) (l.map λ (k, v) => (k, f k v)) = some (k, f k v)
```

`List.find?_implies_append_find?` (theorem, [line 1591](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1591))

```lean
public theorem find?_implies_append_find?
  {a b : List α}
  {v : α}
  {f : α → Bool}
  (h : List.find? f a = some v) :
  List.find? f (a ++ b) = some v
```

`List.not_find?_some_iff_find?_none` (theorem, [line 1600](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1600))

```lean
public theorem not_find?_some_iff_find?_none {α} {p : α → Bool} {xs : List α} :
  (∀ x ∈ xs, ¬xs.find? p = .some x) ↔ xs.find? p = .none
```

`List.find?_exact_iff_mem` (theorem, [line 1637](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1637))

```lean
public theorem find?_exact_iff_mem {α} [DecidableEq α] {l : List α}  {v : α}:
  (l.find? (λ x => x == v) = some v) ↔ v ∈ l
```

> ### filterMap

`Cedar.List.filterMap_congr` (theorem, [line 1675](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1675))

> our own variant of map_congr, for filterMap

```lean
public theorem filterMap_congr {f g : α → Option β} : ∀ {l : List α},
  (∀ x ∈ l, f x = g x) → filterMap f l = filterMap g l
```

`List.filterMap_empty_iff_all_none` (theorem, [line 1688](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1688))

```lean
public theorem filterMap_empty_iff_all_none {f : α → Option β} {xs : List α} :
  xs.filterMap f = [] ↔ ∀ x ∈ xs, f x = none
```

`List.filterMap_nonempty_iff_exists_some` (theorem, [line 1722](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1722))

```lean
public theorem filterMap_nonempty_iff_exists_some {f : α → Option β} {xs : List α} :
  xs.filterMap f ≠ [] ↔ ∃ x ∈ xs, (f x).isSome
```

`List.f_implies_g_then_subset` (theorem, [line 1739](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1739))

```lean
public theorem f_implies_g_then_subset {f g : α → Option β} {xs : List α} :
  (∀ a b, f a = some b → g a = some b) →
  xs.filterMap f ⊆ xs.filterMap g
```

> ### forM and mapM

`List.mapM_forM` (theorem, [line 1752](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1752))

```lean
public theorem mapM_forM {α β : Type} (f : α → Except β PUnit) (xs : List α) (ys : List PUnit) :
  xs.mapM f = Except.ok ys → xs.forM f = Except.ok ()
```

`List.forM_mapM` (theorem, [line 1779](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1779))

```lean
public theorem forM_mapM {α β : Type} (f : α → Except β PUnit) (xs : List α) :
  xs.forM f = Except.ok () → ∃ ys, xs.mapM f = Except.ok ys
```

`List.forM_ok_implies_all_ok` (theorem, [line 1807](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1807))

```lean
public theorem forM_ok_implies_all_ok {α β : Type} (xs : List α) (f : α → Except β Unit) :
  xs.forM f = Except.ok () → (∀ x ∈ xs, f x = Except.ok ())
```

`List.forM_ok_implies_all_ok'` (theorem, [line 1816](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1816))

```lean
public theorem forM_ok_implies_all_ok' {α β : Type} {xs : List α} {f : α → Except β Unit} :
  xs.forM f = Except.ok () → (∀ x ∈ xs, f x = Except.ok ())
```

`List.all_ok_implies_forM_ok` (theorem, [line 1820](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1820))

```lean
public theorem all_ok_implies_forM_ok {α β : Type} (xs : List α) (f : α → Except β Unit) :
   (∀ x ∈ xs, f x = Except.ok ()) → xs.forM f = Except.ok ()
```

> ### removeAll

`List.removeAll_singleton_cons_of_neq` (theorem, [line 1829](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1829))

```lean
public theorem removeAll_singleton_cons_of_neq [DecidableEq α] (x y : α) (xs : List α) :
  x ≠ y → (x :: xs).removeAll [y] = x :: (xs.removeAll [y])
```

`List.removeAll_singleton_cons_of_eq` (theorem, [line 1838](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1838))

```lean
public theorem removeAll_singleton_cons_of_eq [DecidableEq α] (x : α) (xs : List α) :
  (x :: xs).removeAll [x] = xs.removeAll [x]
```

`List.mem_removeAll_singleton_of_eq` (theorem, [line 1844](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1844))

```lean
public theorem mem_removeAll_singleton_of_eq [DecidableEq α] (x : α) (xs : List α) :
  x ∉ xs.removeAll [x]
```

`List.removeAll_singleton_equiv` (theorem, [line 1851](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1851))

```lean
public theorem removeAll_singleton_equiv [DecidableEq α] (x : α) (xs : List α) :
  x :: xs ≡ x :: (xs.removeAll [x])
```

`List.length_removeAll_le` (theorem, [line 1874](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1874))

```lean
public theorem length_removeAll_le {α : Type u_1} [BEq α] (xs ys : List α) :
  (xs.removeAll ys).length ≤ xs.length
```

`List.mem_pmap_subtype` (theorem, [line 1883](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1883))

```lean
public theorem mem_pmap_subtype
  {p : α → Prop}
  (as : List α)
  (h : ∀ a, a ∈ as → p a)
  (a : α)
  (ha : p a) :
  ⟨a, ha⟩ ∈ (List.pmap Subtype.mk as h) ↔
  a ∈ as
```

`List.find?_compose` (theorem, [line 1894](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1894))

```lean
public theorem find?_compose {α β} (f : α → β) (p₁ : β → Bool) (p₂ : α → Bool) {xs : List α} :
  (∀ x, (p₁ ∘ f) x = p₂ x) →
  List.find? (p₁ ∘ f) xs = List.find? p₂ xs
```

`List.mem_implies_mem_eraseDups` (theorem, [line 1913](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1913))

```lean
public theorem mem_implies_mem_eraseDups
  [BEq α] [LawfulBEq α]
  {xs : List α} {x : α}
  (hmem : x ∈ xs) :
  x ∈ xs.eraseDups
```

`List.mem_eraseDups_implies_mem` (theorem, [line 1944](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1944))

```lean
public theorem mem_eraseDups_implies_mem
  [BEq α] [LawfulBEq α]
  {xs : List α} {x : α}
  (hmem : x ∈ xs.eraseDups) :
  x ∈ xs
```

`List.mem_iff_mem_eraseDups` (theorem, [line 1970](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1970))

```lean
public theorem mem_iff_mem_eraseDups
  [BEq α] [LawfulBEq α]
  {xs : List α} {x : α} :
  x ∈ xs ↔ x ∈ xs.eraseDups
```

`List.mapM_preserves_SortedBy` (theorem, [line 1980](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L1980))

> `mapM` preserves `SortedBy` if the keys are preserved

```lean
public theorem mapM_preserves_SortedBy
  [LT γ]
  {l₁ : List α} {l₂ : List β}
  {f : α → Option β}
  {k₁ : α → γ}
  {k₂ : β → γ}
  (hsorted : List.SortedBy k₁ l₁)
  (hmapM : l₁.mapM f = .some l₂)
  (hkey : ∀ a b, f a = .some b → k₁ a = k₂ b) :
  List.SortedBy k₂ l₂
```

`List.map_restricted_id` (theorem, [line 2015](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L2015))

```lean
public theorem map_restricted_id
  {l : List α}
  {f : α → α}
  (hf : ∀ x ∈ l, f x = x) :
  l.map f = l
```

`List.findSome?_unique` (theorem, [line 2033](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L2033))

```lean
public theorem findSome?_unique
  [BEq α] [LawfulBEq α]
  {l : List α} {x : α} {y : β}
  {f : α → Option β}
  (hfind : x ∈ l)
  (hf : ∀ x', (∃ y', f x' = .some y') → x' = x)
  (hx : f x = .some y) :
  l.findSome? f = .some y
```

`List.find?_unique_entry` (theorem, [line 2059](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L2059))

```lean
public theorem find?_unique_entry
  {l : List α}
  {f : α → Bool}
  {v : α}
  (hf : ∀ x ∈ l, f x → x = v)
  (hmem : v ∈ l)
  (hv : f v) :
  List.find? f l = .some v
```

`List.find?_stronger_pred` (theorem, [line 2090](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L2090))

```lean
public theorem find?_stronger_pred
  {l : List α} {v : α}
  {f : α → Bool}
  {g : α → Bool}
  (hfind : List.find? f l = .some v)
  (hg : ∀ x ∈ l, g x → f x)
  (hv : g v) :
  List.find? g l = .some v
```

`List.mem_of_map_implies_exists_unmapped` (theorem, [line 2121](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L2121))

```lean
public theorem mem_of_map_implies_exists_unmapped
  {l : List α} {v₂ : β} {f : α → β}:
  v₂ ∈ (List.map f l) →
  ∃v₁, v₁ ∈ l ∧ v₂ = f v₁
```

`List.mem_map_iff_find?` (theorem, [line 2145](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L2145))

```lean
public theorem mem_map_iff_find? [BEq β] [LawfulBEq β] {k : β} {f : α → β} {kvs : List α} :
  k ∈ List.map f kvs ↔
  (List.find? (fun x => f x == k) kvs).isSome
```

`List.mem_implies_find?` (theorem, [line 2162](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L2162))

```lean
public theorem mem_implies_find?
  {l : List α} {k : α} {f : α → Bool}
  (hmem : k ∈ l)
  (hk : f k)
  (hf : ∀ k', f k' → k' = k) :
  List.find? f l = .some k
```

`List.filterMap_eq_filterMap` (theorem, [line 2188](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L2188))

```lean
public theorem filterMap_eq_filterMap
  {l₁ : List α} {l₂ : List β}
  {p : α → β → Prop} {f₁ : α → Option γ} {f₂ : β → Option γ}
  (h : List.Forall₂ p l₁ l₂)
  (hp : ∀ a b, p a b → f₁ a = f₂ b) :
  l₁.filterMap f₁ = l₂.filterMap f₂
```

`List.find?_filter_if_find?` (theorem, [line 2207](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L2207))

```lean
public theorem find?_filter_if_find? {α : Type u} {β : Type v} [BEq α] [LawfulBEq α] {k : α} {val : β} {l : List (α × β)} (p : α → β → Bool) :
  List.find? (fun x => x.fst == k) l = some (k, val) → p k val = true →
  List.find? (fun x => x.fst == k) (l.filter (fun kv => p kv.fst kv.snd)) = some (k, val)
```

`List.find?_filter_sorted` (theorem, [line 2225](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L2225))

```lean
public theorem find?_filter_sorted {α : Type u} {β : Type v} [BEq α] [LawfulBEq α] [DecidableEq α] [LT α] [Cedar.Data.StrictLT α] [DecidableLT α]
  (k : α) (val : β) (l : List (α × β)) (p : α → β → Bool) :
  l.SortedBy Prod.fst →
  List.find? (fun x => x.fst == k) (l.filter (fun kv => p kv.fst kv.snd)) = some (k, val) →
  List.find? (fun x => x.fst == k) l = some (k, val) ∧ p k val = true
```

`List.anyM_some_implies_any` (theorem, [line 2263](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L2263))

```lean
public theorem anyM_some_implies_any {α} {xs : List α} {b : Bool}  (f : α → Option Bool) (g : α → Bool) :
  (∀ x b, f x = some b → g x = b) → List.anyM f xs = some b → xs.any g = b
```

`List.ternary_any_some_implies_any` (theorem, [line 2292](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean#L2292))

```lean
public theorem ternary_any_some_implies_any {α} {xs : List α} {b : Bool} (f : α → Option Bool) (g : α → Bool) :
  (∀ x b, f x = some b → g x = b) →
  xs.ternaryAny f = some b →
  xs.any g = b
```

## Depends on

- [List properties](basic.md)

## Sources

- [Cedar/Thm/Data/List/Lemmas.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Lemmas.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Data.List.Lemmas.json)
