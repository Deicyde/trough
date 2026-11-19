---
catalog: module
lean: List.mapUnion₁_eq_mapUnion, List.mapUnion₂_eq_mapUnion, List.mapUnion₃_eq_mapUnion, List.mapUnion_nil, List.mapUnion_wf, List.mapUnion_cons, List.mapUnion_singleton, List.mapUnion_pair, List.mapUnion_map, List.mem_foldl_union_iff_mem_or_exists, List.foldl_union_wf, List.mem_mapUnion_iff_mem_exists, List.mem_mem_implies_mem_mapUnion, List.mem_implies_subset_mapUnion, List.mapUnion_filterMap, List.mapUnion_congr, List.mapUnion_eq_mapUnion_id_map, List.mapUnion_eq_of_map_eq, List.mapUnion_append, List.mapUnion_union_mapUnion, List.mapUnion_union_mapUnion', List.mapUnion_comm, List.map_eqv_implies_mapUnion_eq
statement: formalized
proof: formalized
---

# Lemmas about List.mapUnion operator

`Cedar.Thm.Data.MapUnion`, in [Cedar/Thm/Data/MapUnion.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean).

> ### List.mapUnion generically (`f` returning any collection type)

`List.mapUnion₁_eq_mapUnion` (theorem, [line 48](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L48))

```lean
public theorem mapUnion₁_eq_mapUnion [Union β] [EmptyCollection β] (f : α → β) (as : List α) :
  as.mapUnion₁ (λ x : { a : α // a ∈ as } => f x.val) = as.mapUnion f
```

`List.mapUnion₂_eq_mapUnion` (theorem, [line 53](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L53))

```lean
public theorem mapUnion₂_eq_mapUnion [SizeOf α] [SizeOf β] [Union γ] [EmptyCollection γ] (f : (α × β) → γ) (xs : List (α × β)) :
  xs.mapUnion₂ (λ x : { x : α × β // sizeOf x.snd < 1 + sizeOf xs } => f x.1) = xs.mapUnion f
```

`List.mapUnion₃_eq_mapUnion` (theorem, [line 58](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L58))

```lean
public theorem mapUnion₃_eq_mapUnion [SizeOf α] [SizeOf β] [Union γ] [EmptyCollection γ] (f : (α × β) → γ) (xs : List (α × β)) :
  xs.mapUnion₃ (λ x : { x : α × β // sizeOf x.snd < 1 + (1 + sizeOf xs) } => f x.1) = xs.mapUnion f
```

`List.mapUnion_nil` (theorem, [line 64](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L64))

```lean
public theorem mapUnion_nil [Union β] [EmptyCollection β] (f : α → β) :
  [].mapUnion f = ∅
```

> ### List.mapUnion for sets (`f` returning `Set`)

`List.mapUnion_wf` (theorem, [line 70](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L70))

```lean
public theorem mapUnion_wf {α β} [LT α] [StrictLT α] [DecidableLT α] {f : β → Set α} {xs : List β} :
  (∀ x ∈ xs, (f x).WellFormed) →
  (xs.mapUnion f).WellFormed
```

`List.mapUnion_cons` (theorem, [line 100](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L100))

```lean
public theorem mapUnion_cons {α β} [LT α] [StrictLT α] [DecidableLT α] {f : β → Set α} {hd : β} {tl : List β} :
  (hd :: tl).mapUnion f = f hd ∪ tl.mapUnion f
```

`List.mapUnion_singleton` (theorem, [line 114](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L114))

```lean
public theorem mapUnion_singleton {α β} [LT α] [StrictLT α] [DecidableLT α] {f : β → Set α} {x : β} :
  [x].mapUnion f = f x
```

`List.mapUnion_pair` (theorem, [line 119](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L119))

```lean
public theorem mapUnion_pair {α β} [LT α] [StrictLT α] [DecidableLT α] {f : β → Set α} {x y : β} :
  [x, y].mapUnion f = f x ∪ f y
```

`List.mapUnion_map` (theorem, [line 125](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L125))

```lean
public theorem mapUnion_map [LT α] [StrictLT α] [DecidableLT α] {f : β → Set α} {g : γ → β} {xs : List γ} :
  List.mapUnion f (xs.map g) = xs.mapUnion (f ∘ g)
```

`List.mem_foldl_union_iff_mem_or_exists` (theorem, [line 130](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L130))

```lean
public theorem mem_foldl_union_iff_mem_or_exists {α β} [LT α] [StrictLT α] [DecidableLT α] {f : β → Set α} {xs : List β} {init : Set α} {a : α} :
  a ∈ List.foldl (λ as b => as ∪ f b) init xs ↔ (a ∈ init ∨ ∃ s ∈ xs, a ∈ f s)
```

`List.foldl_union_wf` (theorem, [line 149](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L149))

> A fold of unions is well-formed if it starts from a well-formed set and adds well-formed sets.

```lean
public theorem foldl_union_wf {α β} [LT α] [StrictLT α] [DecidableLT α] {f : β → Set α} {xs : List β} {init : Set α} :
  init.WellFormed → (∀ x ∈ xs, (f x).WellFormed) →
  (List.foldl (λ as b => as ∪ f b) init xs).WellFormed
```

`List.mem_mapUnion_iff_mem_exists` (theorem, [line 160](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L160))

```lean
public theorem mem_mapUnion_iff_mem_exists {α β} [LT α] [StrictLT α] [DecidableLT α] {f : β → Set α} {xs : List β} :
  ∀ e, e ∈ xs.mapUnion f ↔ ∃ s ∈ xs, e ∈ f s
```

`List.mem_mem_implies_mem_mapUnion` (theorem, [line 171](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L171))

```lean
public theorem mem_mem_implies_mem_mapUnion {α β} [LT α] [StrictLT α] [DecidableLT α] {f : β → Set α} {xs : List β} {e : α} {s : β} :
  e ∈ f s → s ∈ xs → e ∈ xs.mapUnion f
```

`List.mem_implies_subset_mapUnion` (theorem, [line 178](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L178))

```lean
public theorem mem_implies_subset_mapUnion {α β} [LT α] [StrictLT α] [DecidableLT α] [DecidableEq α] (f : β → Set α) {xs : List β} {s : β} :
  s ∈ xs → f s ⊆ xs.mapUnion f
```

`List.mapUnion_filterMap` (theorem, [line 186](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L186))

```lean
public theorem mapUnion_filterMap {α β γ} [LT α] [StrictLT α] [DecidableLT α] [DecidableEq α] {f : β → Set α} {g : γ → Option β} {xs : List γ} :
  (xs.filterMap g).mapUnion f =
  xs.mapUnion λ x => (g x).mapD f Set.empty
```

`List.mapUnion_congr` (theorem, [line 210](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L210))

```lean
public theorem mapUnion_congr {α β} [LT α] [StrictLT α] [DecidableLT α] [DecidableEq α] (f g : β → Set α) {xs : List β} :
  (∀ b ∈ xs, f b = g b) → xs.mapUnion f = xs.mapUnion g
```

`List.mapUnion_eq_mapUnion_id_map` (theorem, [line 228](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L228))

```lean
public theorem mapUnion_eq_mapUnion_id_map {α β} [LT α] [StrictLT α] [DecidableLT α] [DecidableEq α] (f : β → Set α) {xs : List β} :
  xs.mapUnion f = (xs.map f).mapUnion id
```

`List.mapUnion_eq_of_map_eq` (theorem, [line 240](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L240))

```lean
public theorem mapUnion_eq_of_map_eq {α β γ} [LT α] [StrictLT α] [DecidableLT α] [DecidableEq α] {f : β → Set α} {g : γ → Set α} {xs : List β} {ys : List γ} :
  xs.map f = ys.map g → xs.mapUnion f = ys.mapUnion g
```

`List.mapUnion_append` (theorem, [line 257](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L257))

```lean
public theorem mapUnion_append {α β} [LT α] [StrictLT α] [DecidableLT α] {f : β → Set α} {xs ys : List β} :
  (xs ++ ys).mapUnion f = xs.mapUnion f ++ ys.mapUnion f
```

`List.mapUnion_union_mapUnion` (theorem, [line 273](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L273))

> Corollary of `mapUnion_append`, stated in reverse for some reason, and using `∪` instead of `++` (which are synonyms in the case of Data.Set)

```lean
public theorem mapUnion_union_mapUnion {α β} [LT α] [StrictLT α] [DecidableLT α] (f : β → Set α) (xs ys : List β) :
  List.mapUnion f xs ∪ List.mapUnion f ys = List.mapUnion f (xs ++ ys)
```

`List.mapUnion_union_mapUnion'` (theorem, [line 283](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L283))

> `mapUnion_union_mapUnion` applies when you have the same function `f` and different input lists.
> `mapUnion_union_mapUnion'` applies when you have different functions `f`/`g` and the same input list.

```lean
public theorem mapUnion_union_mapUnion' {α β} [LT α] [StrictLT α] [DecidableLT α] {f g : β → Set α} {xs : List β} :
  List.mapUnion f xs ∪ List.mapUnion g xs = List.mapUnion (λ x => f x ∪ g x) xs
```

`List.mapUnion_comm` (theorem, [line 327](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L327))

```lean
public theorem mapUnion_comm {α β} [LT α] [StrictLT α] [DecidableLT α] [DecidableEq α] {f : β → Set α} {xs ys : List β} :
  (xs ++ ys).mapUnion f = (ys ++ xs).mapUnion f
```

`List.map_eqv_implies_mapUnion_eq` (theorem, [line 396](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean#L396))

```lean
public theorem map_eqv_implies_mapUnion_eq {α β γ} [LT α] [StrictLT α] [DecidableLT α] [DecidableEq α] {f : β → Set α} {g : γ → Set α} {xs : List β} {ys : List γ} :
  xs.map f ≡ ys.map g → xs.mapUnion f = ys.mapUnion g
```

## Depends on

- [Additional Option functions and lemmas](option.md)
- [Set properties](set.md)

## Sources

- [Cedar/Thm/Data/MapUnion.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/MapUnion.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Data.MapUnion.json)
