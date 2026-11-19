---
catalog: module
lean: Cedar.Data.Map.WellFormed, Cedar.Data.Map.if_wellformed_then_exists_make, Cedar.Data.Map.wf_iff_sorted, Cedar.Data.Map.wf_implies_tail_wf, Cedar.Data.Map.wf_empty, Cedar.Data.Map.wf_singleton, Cedar.Data.Map.key_maps_to_one_value, Cedar.Data.Map.eq_iff_toList_eq, Cedar.Data.Map.eq_iff_toList_equiv, Cedar.Data.Map.keys_wf, Cedar.Data.Map.toList_empty, Cedar.Data.Map.toList_nil_iff_empty, Cedar.Data.Map.mk_toList_id, Cedar.Data.Map.toList_mk_id, Cedar.Data.Map.deprecated_toList_def, Cedar.Data.Map.in_list_in_map, Cedar.Data.Map.in_list_in_keys, Cedar.Data.Map.in_list_in_values, Cedar.Data.Map.in_keys_iff_in_map, Cedar.Data.Map.in_keys_iff_contains, Cedar.Data.Map.in_values_exists_key, Cedar.Data.Map.in_keys_exists_value, Cedar.Data.Map.values_cons, Cedar.Data.Map.contains_eq_isSome_find?, Cedar.Data.Map.contains_iff_some_find?, Cedar.Data.Map.find?_some_implies_contains, Cedar.Data.Map.not_find?_of_empty, Cedar.Data.Map.not_contains_of_empty, Cedar.Data.Map.make_wf, Cedar.Data.Map.mk_wf, Cedar.Data.Map.make_eq_mk_canonicalize, Cedar.Data.Map.make_eq_mk, Cedar.Data.Map.toList_make_eq_canonicalize, Cedar.Data.Map.make_singleton, Cedar.Data.Map.mem_make_mem_list, Cedar.Data.Map.mem_values_make, Cedar.Data.Map.mem_list_mem_make, Cedar.Data.Map.make_nil_is_empty, Cedar.Data.Map.make_cons, Cedar.Data.Map.make_of_make_is_id, Cedar.Data.Map.find?_empty, Cedar.Data.Map.singleton_find?, Cedar.Data.Map.singleton_contains, Cedar.Data.Map.find?_eq_toList_find?, Cedar.Data.Map.find?_mem_toList, Cedar.Data.Map.in_list_iff_find?_some, Cedar.Data.Map.find?_notmem_keys, Cedar.Data.Map.find?_ext, Cedar.Data.Map.find?_none_all_absent, Cedar.Data.Map.in_list_implies_contains, Cedar.Data.Map.all_absent_find?_none, Cedar.Data.Map.find?_none_iff_all_absent, Cedar.Data.Map.list_find?_some_iff_map_find?_some, Cedar.Data.Map.list_find?_mapM_implies_exists_mapped, Cedar.Data.Map.list_find?_mapM_implies_exists_unmapped, Cedar.Data.Map.find?_mapM_key_id, Cedar.Data.Map.find?_filterMap_key_id, Cedar.Data.Map.filterMap_key_id_key_none_implies_find?_none, Cedar.Data.Map.mapOnValues_wf, Cedar.Data.Map.mapOnValues_empty, Cedar.Data.Map.mapOnValues_tail, Cedar.Data.Map.mapOnValues_doubleton, Cedar.Data.Map.find?_mapOnValues, Cedar.Data.Map.find?_mapOnValues_some, Cedar.Data.Map.find?_mapOnValues_some', Cedar.Data.Map.find?_mapOnValues_none, Cedar.Data.Map.mapOnValues_eq_make_map, Cedar.Data.Map.mem_toList_find?, Cedar.Data.Map.contains_mapOnValues, Cedar.Data.Map.keys_mapOnValues, Cedar.Data.Map.values_mapOnValues, Cedar.Data.Map.mapOnValues_mapOnValues, Cedar.Data.Map.mapOnValues_congr, Cedar.Data.Map.mapOnValues_restricted_id, Cedar.Data.Map.mapOnValues_mk, Cedar.Data.Map.mapOnValues_make, Cedar.Data.Map.mapOnValues₂_eq_mapOnValues, Cedar.Data.Map.findOrErr_returns, Cedar.Data.Map.findOrErr_mapOnValues, Cedar.Data.Map.findOrErr_ok_iff_find?_some, Cedar.Data.Map.findOrErr_err_iff_find?_none, Cedar.Data.Map.findOrErr_eq_match, Cedar.Data.Map.findOrErr_ok_implies_in_toList, Cedar.Data.Map.findOrErr_ok_iff_in_toList, Cedar.Data.Map.find?_some_implies_in_values, Cedar.Data.Map.findOrErr_ok_implies_in_values, Cedar.Data.Map.find?_some_iff_in_values, Cedar.Data.Map.findOrErr_ok_iff_in_values, Cedar.Data.Map.findOrErr_err_iff_not_in_keys, Cedar.Data.Map.in_toList_in_mapOnValues, Cedar.Data.Map.find?_none_iff_findorErr_errors, Cedar.Data.Map.in_mapOnValues_in_toList, Cedar.Data.Map.in_mapOnValues_in_toList', Cedar.Data.Map.mapMOnValues₂_eq_mapMOnValues, Cedar.Data.Map.mapMOnValues_empty, Cedar.Data.Map.mapMOnValues_mapOnValues, Cedar.Data.Map.mapMOnValues_some, Cedar.Data.Map.mapMOnValues_isSome, Cedar.Data.Map.mapMOnValues_preserves_keys, Cedar.Data.Map.mapMOnValues_some_wf, Cedar.Data.Map.mapMOnValues_ok_wf, Cedar.Data.Map.mapMOnValues_cons, Cedar.Data.Map.mapOnValues_eq_of_mapMOnValues_some, Cedar.Data.Map.mapMOnValues_some_implies_all_some, Cedar.Data.Map.mapMOnValues_some_implies_all_from_some, Cedar.Data.Map.mapMOnValues_none_iff_exists_none, Cedar.Data.Map.mapMOnValues_ok_implies_all_ok, Cedar.Data.Map.mapMOnValues_ok_implies_all_from_ok, Cedar.Data.Map.all_ok_implies_mapMOnValues_ok, Cedar.Data.Map.mapMOnValues_error_implies_exists_error, Cedar.Data.Map.wellFormed_correct, Cedar.Data.Map.make_find?_eq_list_find?, Cedar.Data.Map.make_toList_map_find?, Cedar.Data.Map.list_find?_iff_make_find?, Cedar.Data.Map.list_find?_iff_mk_find?, Cedar.Data.Map.map_make_append_find_disjoint, Cedar.Data.Map.make_map_values_find, Cedar.Data.Map.map_toList_findSome?, Cedar.Data.Map.map_find?_to_list_find?, Cedar.Data.Map.map_make_append_find_disjoint', Cedar.Data.Map.map_find?_implies_find?_weaker_pred, Cedar.Data.Map.map_keys_empty_implies_map_empty, Cedar.Data.Map.toList_congr, Cedar.Data.Map.find?_append, Cedar.Data.Map.contains_append, Cedar.Data.Map.find?_append_right, Cedar.Data.Map.find?_append_left, Cedar.Data.Map.filter_wf, Cedar.Data.Map.find?_filter_if_find?, Cedar.Data.Map.find?_filter_iff_find, Cedar.Data.Map.filter_contains_if_find_matching, Cedar.Data.Map.find_matching_iff_filter_contains, Cedar.Data.Map.filter_not_contains
statement: formalized
proof: formalized
---

# Map properties

`Cedar.Thm.Data.Map`, in [Cedar/Thm/Data/Map.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean).

> This file proves useful properties of canonical list-based maps defined in
> `Cedar.Data.Map`.

> ### Well-formed maps

`Cedar.Data.Map.WellFormed` (definition, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L38))

```lean
public def WellFormed {α β} [LT α] [DecidableLT α] (m : Map α β)
```

`Cedar.Data.Map.if_wellformed_then_exists_make` (theorem, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L41))

```lean
public theorem if_wellformed_then_exists_make [LT α] [DecidableLT α] (m : Map α β) :
  WellFormed m → ∃ list, m = Map.make list
```

`Cedar.Data.Map.wf_iff_sorted` (theorem, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L47))

```lean
public theorem wf_iff_sorted {α β} [LT α] [DecidableLT α] [StrictLT α] {m : Map α β} :
  m.WellFormed ↔ m.toList.SortedBy Prod.fst
```

`Cedar.Data.Map.wf_implies_tail_wf` (theorem, [line 62](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L62))

```lean
public theorem wf_implies_tail_wf {α β} [LT α] [DecidableLT α] [StrictLT α]
  {hd : α × β} {tl : List (α × β)}
  (hwf : (mk (hd :: tl)).WellFormed) :
  (mk tl).WellFormed
```

`Cedar.Data.Map.wf_empty` (theorem, [line 77](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L77))

```lean
public theorem wf_empty {α β} [LT α] [DecidableLT α] :
  (Map.empty : Map α β).WellFormed
```

`Cedar.Data.Map.wf_singleton` (theorem, [line 81](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L81))

```lean
public theorem wf_singleton [LT α] [DecidableLT α] (a : α) (b : β) :
  (Map.mk [(a, b)]).WellFormed
```

`Cedar.Data.Map.key_maps_to_one_value` (theorem, [line 90](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L90))

> In well-formed maps, if there are two pairs with the same key, then they have
> the same value

```lean
public theorem key_maps_to_one_value [DecidableEq α] [LT α] [DecidableLT α] [StrictLT α] (k : α) (v₁ v₂ : β) (m : Map α β) :
  m.WellFormed →
  (k, v₁) ∈ m.toList →
  (k, v₂) ∈ m.toList →
  v₁ = v₂
```

`Cedar.Data.Map.eq_iff_toList_eq` (theorem, [line 108](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L108))

> If two maps have exactly equal (k,v) sets, then the maps are equal
>
> This doesn't require WellFormed, but we use it in the proof of
> `eq_iff_toList_equiv` below

```lean
public theorem eq_iff_toList_eq {m₁ m₂ : Map α β} :
  m₁.toList = m₂.toList ↔ m₁ = m₂
```

`Cedar.Data.Map.eq_iff_toList_equiv` (theorem, [line 120](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L120))

> If two well-formed maps have equivalent (k,v) sets, then the maps are actually
> equal

```lean
public theorem eq_iff_toList_equiv [LT α] [DecidableLT α] [StrictLT α] {m₁ m₂ : Map α β}
  (wf₁ : m₁.WellFormed)
  (wf₂ : m₂.WellFormed) :
  m₁.toList ≡ m₂.toList ↔ m₁ = m₂
```

> ### empty, contains, mem, toList, keys, values

`Cedar.Data.Map.keys_wf` (theorem, [line 138](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L138))

```lean
public theorem keys_wf [LT α] [DecidableLT α] [StrictLT α] (m : Map α β) :
  m.WellFormed → m.keys.WellFormed
```

`Cedar.Data.Map.toList_empty` (theorem, [line 152](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L152))

```lean
public theorem toList_empty {α β} :
  (Map.empty : Map α β).toList = []
```

`Cedar.Data.Map.toList_nil_iff_empty` (theorem, [line 157](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L157))

```lean
public theorem toList_nil_iff_empty {m : Map α β} :
  m.toList = [] ↔ m = Map.empty
```

`Cedar.Data.Map.mk_toList_id` (theorem, [line 168](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L168))

```lean
public theorem mk_toList_id (m : Map α β) :
  mk m.toList = m
```

`Cedar.Data.Map.toList_mk_id` (theorem, [line 173](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L173))

```lean
public theorem toList_mk_id (kvs : List (α × β)) :
  (mk kvs).toList = kvs
```

`Cedar.Data.Map.deprecated_toList_def` (theorem, [line 183](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L183))

> As a crutch to accommodate some pre-existing usage, we provide this theorem. …

```lean
public theorem deprecated_toList_def (m : Map α β) :
  m.toList = m.1
```

`Cedar.Data.Map.in_list_in_map` (theorem, [line 187](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L187))

```lean
public theorem in_list_in_map {α : Type u} (k : α) (v : β) (m : Map α β) :
  (k, v) ∈ m.toList → k ∈ m
```

`Cedar.Data.Map.in_list_in_keys` (theorem, [line 194](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L194))

```lean
public theorem in_list_in_keys {k : α} {v : β} {m : Map α β} :
  (k, v) ∈ m.toList → k ∈ m.keys
```

`Cedar.Data.Map.in_list_in_values` (theorem, [line 201](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L201))

```lean
public theorem in_list_in_values {k : α} {v : β} {m : Map α β} :
  (k, v) ∈ m.toList → v ∈ m.values
```

`Cedar.Data.Map.in_keys_iff_in_map` (theorem, [line 208](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L208))

```lean
public theorem in_keys_iff_in_map {k : α} {m : Map α β} :
  k ∈ m.keys ↔ k ∈ m
```

`Cedar.Data.Map.in_keys_iff_contains` (theorem, [line 212](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L212))

```lean
public theorem in_keys_iff_contains [BEq α] [LawfulBEq α] {k : α} {m : Map α β} :
  (k ∈ m.keys ↔ m.contains k)
```

`Cedar.Data.Map.in_values_exists_key` (theorem, [line 222](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L222))

> kinda the converse of `in_list_in_values`

```lean
public theorem in_values_exists_key {m : Map α β} {v : β} :
  v ∈ m.values → ∃ k, (k, v) ∈ m.toList
```

`Cedar.Data.Map.in_keys_exists_value` (theorem, [line 230](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L230))

```lean
public theorem in_keys_exists_value {m : Map α β} {k : α} :
  k ∈ m.keys → ∃ v, (k, v) ∈ m.toList
```

`Cedar.Data.Map.values_cons` (theorem, [line 235](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L235))

```lean
public theorem values_cons {m : Map α β} :
  m.toList = (k, v) :: tl →
  m.values = v :: (mk tl).values
```

`Cedar.Data.Map.contains_eq_isSome_find?` (theorem, [line 244](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L244))

> Characterizes `contains` in terms of `find?`, for clients that cannot unfold `contains`.

```lean
public theorem contains_eq_isSome_find? {α β} [BEq α] (m : Map α β) (k : α) :
  m.contains k = (m.find? k).isSome
```

`Cedar.Data.Map.contains_iff_some_find?` (theorem, [line 248](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L248))

```lean
public theorem contains_iff_some_find? {α β} [BEq α] {m : Map α β} {k : α} :
  m.contains k ↔ ∃ v, m.find? k = .some v
```

`Cedar.Data.Map.find?_some_implies_contains` (theorem, [line 252](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L252))

```lean
public theorem find?_some_implies_contains {α β} [BEq α] {m : Map α β} {k : α} {v : β} :
  m.find? k = .some v → m.contains k
```

`Cedar.Data.Map.not_find?_of_empty` (theorem, [line 260](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L260))

```lean
public theorem not_find?_of_empty [BEq α] {k : α} :
  (Map.empty : Map α β).find? k = none
```

`Cedar.Data.Map.not_contains_of_empty` (theorem, [line 264](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L264))

```lean
public theorem not_contains_of_empty {α β} [BEq α] (k : α) :
  ¬ (Map.empty : Map α β).contains k
```

> ### make and mk

`Cedar.Data.Map.make_wf` (theorem, [line 270](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L270))

```lean
public theorem make_wf [LT α] [StrictLT α] [DecidableLT α] (xs : List (α × β)) :
  WellFormed (Map.make xs)
```

`Cedar.Data.Map.mk_wf` (theorem, [line 275](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L275))

```lean
public theorem mk_wf [LT α] [StrictLT α] [DecidableLT α] {xs : List (α × β)} :
  xs.SortedBy Prod.fst → (Map.mk xs).WellFormed
```

`Cedar.Data.Map.make_eq_mk_canonicalize` (theorem, [line 283](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L283))

```lean
public theorem make_eq_mk_canonicalize [LT α] [StrictLT α] [DecidableLT α] {xs : List (α × β)} :
  Map.make xs = Map.mk (List.canonicalize Prod.fst xs)
```

`Cedar.Data.Map.make_eq_mk` (theorem, [line 287](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L287))

```lean
public theorem make_eq_mk [LT α] [StrictLT α] [DecidableLT α] {xs : List (α × β)} :
  xs.SortedBy Prod.fst ↔ Map.make xs = Map.mk xs
```

`Cedar.Data.Map.toList_make_eq_canonicalize` (theorem, [line 298](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L298))

```lean
public theorem toList_make_eq_canonicalize [LT α] [StrictLT α] [DecidableLT α] (xs : List (α × β)) :
  (Map.make xs).toList = List.canonicalize Prod.fst xs
```

`Cedar.Data.Map.make_singleton` (theorem, [line 302](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L302))

```lean
public theorem make_singleton [LT α] [DecidableLT α] [StrictLT α] (k : α) (v : β) :
  Map.make [(k, v)] = Map.mk [(k, v)]
```

`Cedar.Data.Map.mem_make_mem_list` (theorem, [line 315](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L315))

> Note that the converse of this is not true:
> counterexample `xs = [(1, false), (1, true)]`.
> (The property here would not hold for either `x = (1, false)` or `x = (1, true)`.)
>
> For a limited converse, see `mem_list_mem_make` below.

```lean
public theorem mem_make_mem_list [LT α] [StrictLT α] [DecidableLT α] {xs : List (α × β)} :
  x ∈ (Map.make xs).toList → x ∈ xs
```

`Cedar.Data.Map.mem_values_make` (theorem, [line 327](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L327))

> Very similar to `mem_make_mem_list` above

```lean
public theorem mem_values_make [LT α] [StrictLT α] [DecidableLT α] {xs : List (α × β)} :
  v ∈ (Map.make xs).values → v ∈ xs.map Prod.snd
```

`Cedar.Data.Map.mem_list_mem_make` (theorem, [line 346](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L346))

> This limited converse of `mem_make_mem_list` requires that the input list is
> SortedBy Prod.fst.

```lean
public theorem mem_list_mem_make [LT α] [StrictLT α] [DecidableLT α] {xs : List (α × β)} :
  xs.SortedBy Prod.fst →
  x ∈ xs → x ∈ (Map.make xs).toList
```

`Cedar.Data.Map.make_nil_is_empty` (theorem, [line 357](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L357))

```lean
public theorem make_nil_is_empty {α β} [LT α] [DecidableLT α] :
  (Map.make [] : Map α β) = Map.empty
```

`Cedar.Data.Map.make_cons` (theorem, [line 365](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L365))

> Note that the converse of this is not true:
> counterexample `xs = [(1, false)]`, `ys = []`, `ab = (1, false)`.

```lean
public theorem make_cons [LT α] [DecidableLT α] {xs ys : List (α × β)} {ab : α × β} :
  make xs = make ys → make (ab :: xs) = make (ab :: ys)
```

`Cedar.Data.Map.make_of_make_is_id` (theorem, [line 372](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L372))

```lean
public theorem make_of_make_is_id [LT α] [DecidableLT α] [StrictLT α] (xs : List (α × β)) :
  Map.make (Map.toList (Map.make xs)) = Map.make xs
```

> ### find?, findOrErr, and mapOnValues

`Cedar.Data.Map.find?_empty` (theorem, [line 383](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L383))

```lean
public theorem find?_empty {α β} [DecidableEq α] (k : α) :
  (Map.empty : Map α β).find? k = none
```

`Cedar.Data.Map.singleton_find?` (theorem, [line 388](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L388))

```lean
public theorem singleton_find? [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] (k : α) (v : β) :
  (Map.make [(k, v)]).find? k = .some v
```

`Cedar.Data.Map.singleton_contains` (theorem, [line 393](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L393))

```lean
public theorem singleton_contains  [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] (k k' : α) (v : β) :
  (Map.make [(k', v)]).contains k ↔ k' == k
```

`Cedar.Data.Map.find?_eq_toList_find?` (theorem, [line 406](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L406))

> `Map.find?` returns the value of the first entry with the key.

```lean
public theorem find?_eq_toList_find? {α β} [BEq α] (m : Map α β) (k : α) :
  m.find? k = (m.toList.find? (·.fst == k)).map Prod.snd
```

`Cedar.Data.Map.find?_mem_toList` (theorem, [line 415](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L415))

> Converse is available at `in_list_iff_find?_some` (requires `wf` though)
>
> Inverse is available at `find?_notmem_keys` (requires `wf` though)

```lean
public theorem find?_mem_toList {α β} [LT α] [DecidableLT α] [DecidableEq α] {m : Map α β} {k : α} {v : β}
  (h₁ : m.find? k = .some v) :
  (k, v) ∈ m.toList
```

`Cedar.Data.Map.in_list_iff_find?_some` (theorem, [line 431](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L431))

> The `mpr` direction of this does not need the `wf` precondition and, in fact,
> is available separately as `find?_mem_toList` above

```lean
public theorem in_list_iff_find?_some [DecidableEq α] [LT α] [DecidableLT α] [StrictLT α] {k : α} {v : β} {m : Map α β}
  (wf : m.WellFormed) :
  (k, v) ∈ m.toList ↔ m.find? k = some v
```

`Cedar.Data.Map.find?_notmem_keys` (theorem, [line 456](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L456))

> Inverse of `find?_mem_toList`, except that this requires `wf`

```lean
public theorem find?_notmem_keys [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] {m : Map α β} {k : α}
  (wf : m.WellFormed) :
  m.find? k = none ↔ k ∉ m.keys
```

`Cedar.Data.Map.find?_ext` (theorem, [line 484](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L484))

> Two well-formed maps are equal if they have the same `find?` for every key.

```lean
public theorem find?_ext [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] {m₁ m₂ : Map α β}
  (wf₁ : m₁.WellFormed)
  (wf₂ : m₂.WellFormed)
  (h : ∀ k, m₁.find? k = m₂.find? k) :
  m₁ = m₂
```

`Cedar.Data.Map.find?_none_all_absent` (theorem, [line 501](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L501))

```lean
public theorem find?_none_all_absent [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] {m : Map α β} {k : α} :
  m.find? k = none → ∀ v, ¬ (k, v) ∈ m.toList
```

`Cedar.Data.Map.in_list_implies_contains` (theorem, [line 513](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L513))

```lean
public theorem in_list_implies_contains {α β}
  [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α]
  {m : Map α β} {k : α} {v : β} :
  (k, v) ∈ m.toList → m.contains k
```

`Cedar.Data.Map.all_absent_find?_none` (theorem, [line 527](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L527))

```lean
public theorem all_absent_find?_none [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] {m : Map α β} {k : α} :
  (∀ v, (k, v) ∉ m.toList) → m.find? k = none
```

`Cedar.Data.Map.find?_none_iff_all_absent` (theorem, [line 553](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L553))

```lean
public theorem find?_none_iff_all_absent [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] {m : Map α β} {k : α} :
  m.find? k = none ↔ ∀ v, ¬ (k, v) ∈ m.toList
```

`Cedar.Data.Map.list_find?_some_iff_map_find?_some` (theorem, [line 558](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L558))

```lean
public theorem list_find?_some_iff_map_find?_some {α β: Type} [BEq α] [LawfulBEq α] {l: List (α × β)} {k : α} {v : β} :
  l.find? (λ x => x.1 == k) = .some (k, v) ↔
  (Map.mk l).find? k = .some v
```

`Cedar.Data.Map.list_find?_mapM_implies_exists_mapped` (theorem, [line 592](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L592))

```lean
public theorem list_find?_mapM_implies_exists_mapped {α β γ : Type} [BEq α] [LawfulBEq α] {ls : List (α × β)} (fn : β → Option γ) {ys: List (α × γ)} {k: α} {x : β} :
  List.mapM (fun x =>
              (fn x.2).bind
                (fun v => some (x.fst, v))) ls = some ys →
  ls.find? (λ x => x.1 == k) = .some (k, x) →
  ∃y, fn x = .some y ∧  ys.find? (λ x => x.1 == k) = .some (k, y)
```

`Cedar.Data.Map.list_find?_mapM_implies_exists_unmapped` (theorem, [line 640](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L640))

```lean
public theorem list_find?_mapM_implies_exists_unmapped {α β γ : Type} [BEq α] [LawfulBEq α] {ls : List (α × β)} (fn : β → Option γ) {ys: List (α × γ)} {k: α} {y: γ} :
  List.mapM (fun x =>
              (fn x.2).bind
                (fun v => some (x.fst, v))) ls = some ys →
  ys.find? (λ x => x.1 == k) = .some (k, y) →
  ∃ x, fn x = some y ∧ (ls.find? (λ x => x.1 == k) = .some (k, x))
```

`Cedar.Data.Map.find?_mapM_key_id` (theorem, [line 692](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L692))

```lean
public theorem find?_mapM_key_id {α β : Type} [BEq α] [LawfulBEq α] {ks : List α} {kvs : List (α × β)} {fn : α → Option β} {k: α}
  (h₁ : ks.mapM (λ k => do (k, ←fn k)) = some kvs)
  (h₂ : k ∈ ks) :
  (Map.mk kvs).find? k = fn k
```

`Cedar.Data.Map.find?_filterMap_key_id` (theorem, [line 717](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L717))

```lean
public theorem find?_filterMap_key_id {α β : Type} [BEq α] [LawfulBEq α] {ks : List α} {fn : α → Option β} {k: α}
  (h₂ : k ∈ ks) :
  (Map.mk (ks.filterMap (λ k => do (k, ←fn k)))).find? k = fn k
```

`Cedar.Data.Map.filterMap_key_id_key_none_implies_find?_none` (theorem, [line 730](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L730))

```lean
public theorem filterMap_key_id_key_none_implies_find?_none {α β : Type} [DecidableEq α] [LT α] [StrictLT α] [DecidableLT α] {ks : List α} {fn : α → Option β} {k: α}
  (h₁ : fn k = none) :
  (Map.make (ks.filterMap (λ k => do some (k, ←fn k)))).find? k = none
```

`Cedar.Data.Map.mapOnValues_wf` (theorem, [line 777](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L777))

```lean
public theorem mapOnValues_wf [DecidableEq α] [LT α] [DecidableLT α] [StrictLT α] {f : β → γ} {m : Map α β} :
  m.WellFormed ↔ (m.mapOnValues f).WellFormed
```

`Cedar.Data.Map.mapOnValues_empty` (theorem, [line 787](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L787))

```lean
public theorem mapOnValues_empty {α β γ} [LT α] [DecidableLT α] [DecidableEq α] {f : β → γ} :
  (empty : Map α β).mapOnValues f = empty
```

`Cedar.Data.Map.mapOnValues_tail` (theorem, [line 792](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L792))

```lean
public theorem mapOnValues_tail {f : β → γ} {hd₁ hd₂ : α × β} {tl₁ tl₂ : List (α × β)} :
  Map.mapOnValues f (Map.mk (hd₁ :: tl₁)) = Map.mapOnValues f (Map.mk (hd₂ :: tl₂)) →
  Map.mapOnValues f (Map.mk tl₁) = Map.mapOnValues f (Map.mk tl₂)
```

`Cedar.Data.Map.mapOnValues_doubleton` (theorem, [line 802](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L802))

> Ideally we wouldn't need this, but it's currently necessary because of the kludgy way
> that `EntityTag.mk` uses `Map` without relying on its proper constructors

```lean
public theorem mapOnValues_doubleton {f : β → γ} {s₁ s₂ : String} (b₁ b₂ : β) :
  Map.mapOnValues f (Map.mk [(s₁, b₁), (s₂, b₂)]) = Map.mk [(s₁, f b₁), (s₂, f b₂)]
```

`Cedar.Data.Map.find?_mapOnValues` (theorem, [line 807](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L807))

```lean
public theorem find?_mapOnValues {α β γ} [LT α] [DecidableLT α] [DecidableEq α] (f : β → γ) (m : Map α β) (k : α)  :
  (m.mapOnValues f).find? k = (m.find? k).map f
```

`Cedar.Data.Map.find?_mapOnValues_some` (theorem, [line 813](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L813))

```lean
public theorem find?_mapOnValues_some {α β γ} [LT α] [DecidableLT α] [DecidableEq α] (f : β → γ) {m : Map α β} {k : α} {v : β} :
  m.find? k = .some v →
  (m.mapOnValues f).find? k = .some (f v)
```

`Cedar.Data.Map.find?_mapOnValues_some'` (theorem, [line 821](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L821))

```lean
public theorem find?_mapOnValues_some' {α β γ} [LT α] [DecidableLT α] [DecidableEq α] (f : β → γ) {m : Map α β} {k : α} {v : γ} :
  (m.mapOnValues f).find? k = .some v →
  (∃ v', m.find? k = .some v' ∧ v = f v')
```

`Cedar.Data.Map.find?_mapOnValues_none` (theorem, [line 844](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L844))

```lean
public theorem find?_mapOnValues_none {α β γ} [LT α] [DecidableLT α] [DecidableEq α] (f : β → γ) {m : Map α β} {k : α} :
  (m.mapOnValues f).find? k = .none ↔
  m.find? k = .none
```

`Cedar.Data.Map.mapOnValues_eq_make_map` (theorem, [line 849](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L849))

```lean
public theorem mapOnValues_eq_make_map {α β γ} [LT α] [StrictLT α] [DecidableLT α] (f : β → γ) {m : Map α β}
  (wf : m.WellFormed) :
  m.mapOnValues f = Map.make (m.toList.map λ kv => (kv.fst, f kv.snd))
```

`Cedar.Data.Map.mem_toList_find?` (theorem, [line 859](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L859))

```lean
public theorem mem_toList_find? {α β} [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] {m : Map α β} {k : α} {v : β}
  (h₁ : m.WellFormed)
  (h₂ : (k, v) ∈ m.toList) :
  m.find? k = .some v
```

`Cedar.Data.Map.contains_mapOnValues` (theorem, [line 877](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L877))

```lean
public theorem contains_mapOnValues {α β γ} [LT α] [DecidableLT α] [DecidableEq α] (f : β → γ) {m : Map α β} {k : α} :
  Map.contains (Map.mapOnValues f m) k = Map.contains m k
```

`Cedar.Data.Map.keys_mapOnValues` (theorem, [line 886](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L886))

```lean
public theorem keys_mapOnValues [LT α] [StrictLT α] [DecidableLT α] [DecidableEq α] (f : β → γ) (m : Map α β) :
  (m.mapOnValues f).keys = m.keys
```

`Cedar.Data.Map.values_mapOnValues` (theorem, [line 892](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L892))

```lean
public theorem values_mapOnValues [LT α] [StrictLT α] [DecidableLT α] [DecidableEq α] {f : β → γ} {m : Map α β} :
  (m.mapOnValues f).values = m.values.map f
```

`Cedar.Data.Map.mapOnValues_mapOnValues` (theorem, [line 899](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L899))

```lean
public theorem mapOnValues_mapOnValues [LT α] [StrictLT α] [DecidableLT α] [DecidableEq α] {f : β → γ} {g : γ → φ} {m : Map α β} :
  (m.mapOnValues f).mapOnValues g = m.mapOnValues (g ∘ f)
```

`Cedar.Data.Map.mapOnValues_congr` (theorem, [line 904](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L904))

> Like `List.map_congr`, but lifted to `Map.mapOnValues`

```lean
public theorem mapOnValues_congr {f g : β → γ} {m : Map α β} :
  (∀ v ∈ m.values, f v = g v) → m.mapOnValues f = m.mapOnValues g
```

`Cedar.Data.Map.mapOnValues_restricted_id` (theorem, [line 911](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L911))

```lean
public theorem mapOnValues_restricted_id  {f : β → β} {m : Map α β} :
  (∀ b ∈ m.values, f b = b) →
  m.mapOnValues f = m
```

`Cedar.Data.Map.mapOnValues_mk` (theorem, [line 922](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L922))

```lean
public theorem mapOnValues_mk {f : β → γ} {kvs : List (α × β)} :
  (Map.mk kvs).mapOnValues f = Map.mk (kvs.map λ (k, v) => (k, f v))
```

`Cedar.Data.Map.mapOnValues_make` (theorem, [line 927](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L927))

```lean
public theorem mapOnValues_make [LT α] [DecidableLT α] [StrictLT α] {f : β → γ} {kvs : List (α × β)} :
  (Map.make kvs).mapOnValues f = Map.make (kvs.map (Prod.map id f))
```

`Cedar.Data.Map.mapOnValues₂_eq_mapOnValues` (theorem, [line 933](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L933))

```lean
public theorem mapOnValues₂_eq_mapOnValues {α β γ} [SizeOf α] [SizeOf β] (m : Map α β) (f : β → γ) :
  m.mapOnValues₂ (λ x : { x : β // sizeOf x < sizeOf m } => f x.1) = m.mapOnValues f
```

`Cedar.Data.Map.findOrErr_returns` (theorem, [line 939](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L939))

> `findOrErr` cannot return any error other than `e`

```lean
public theorem findOrErr_returns [DecidableEq α] (m : Map α β) (k : α) (e : Error) :
  (∃ v, m.findOrErr k e = .ok v) ∨
  m.findOrErr k e = .error e
```

`Cedar.Data.Map.findOrErr_mapOnValues` (theorem, [line 947](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L947))

```lean
public theorem findOrErr_mapOnValues [LT α] [DecidableLT α] [DecidableEq α] {f : β → γ} {m : Map α β} {k : α} {e : Error} :
  (m.mapOnValues f).findOrErr k e = (m.findOrErr k e).map f
```

`Cedar.Data.Map.findOrErr_ok_iff_find?_some` (theorem, [line 955](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L955))

```lean
public theorem findOrErr_ok_iff_find?_some [LT α] [DecidableLT α] [DecidableEq α] {m : Map α β} {k : α} {v : β} {e : Error} :
  m.findOrErr k e = .ok v ↔ m.find? k = some v
```

`Cedar.Data.Map.findOrErr_err_iff_find?_none` (theorem, [line 962](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L962))

```lean
public theorem findOrErr_err_iff_find?_none [LT α] [DecidableLT α] [DecidableEq α] {m : Map α β} {k : α} {e : Error} :
  m.findOrErr k e = .error e ↔ m.find? k = none
```

`Cedar.Data.Map.findOrErr_eq_match` (theorem, [line 969](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L969))

> Equation lemma for `findOrErr`, for clients that cannot unfold it.

```lean
public theorem findOrErr_eq_match {α β ε} [BEq α] (m : Map α β) (k : α) (e : ε) :
  m.findOrErr k e = match m.find? k with | some v => .ok v | _ => .error e
```

`Cedar.Data.Map.findOrErr_ok_implies_in_toList` (theorem, [line 977](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L977))

> The converse requires the `wf` precondition, and is available in
> `findOrErr_ok_iff_in_toList` below

```lean
public theorem findOrErr_ok_implies_in_toList [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] {m : Map α β} {k : α} {v : β} {e : Error} :
  m.findOrErr k e = .ok v → (k, v) ∈ m.toList
```

`Cedar.Data.Map.findOrErr_ok_iff_in_toList` (theorem, [line 987](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L987))

> The `mp` direction of this does not need the `wf` precondition and, in fact,
> is available separately as `findOrErr_ok_implies_in_toList` above

```lean
public theorem findOrErr_ok_iff_in_toList [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] {m : Map α β} {k : α} {v : β} {e : Error}
  (wf : m.WellFormed) :
  m.findOrErr k e = .ok v ↔ (k, v) ∈ m.toList
```

`Cedar.Data.Map.find?_some_implies_in_values` (theorem, [line 1001](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1001))

> The converse requires the `wf` precondition, and is available in
> `find?_some_iff_in_values` below

```lean
public theorem find?_some_implies_in_values [LT α] [DecidableLT α] [DecidableEq α] {m : Map α β} {k : α} {v : β} :
  m.find? k = .some v → v ∈ m.values
```

`Cedar.Data.Map.findOrErr_ok_implies_in_values` (theorem, [line 1013](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1013))

> The converse requires the `wf` precondition, and is available in
> `findOrErr_ok_iff_in_values` below

```lean
public theorem findOrErr_ok_implies_in_values [LT α] [DecidableLT α] [DecidableEq α] {m : Map α β} {k : α} {v : β} {e : Error} :
  m.findOrErr k e = .ok v → v ∈ m.values
```

`Cedar.Data.Map.find?_some_iff_in_values` (theorem, [line 1023](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1023))

> The `mp` direction of this does not need the `wf` precondition and, in fact,
> is available separately as `find?_some_implies_in_values` above

```lean
public theorem find?_some_iff_in_values [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] {m : Map α β} {v : β}
  (wf : m.WellFormed) :
  (∃ k, m.find? k = .some v) ↔ v ∈ m.values
```

`Cedar.Data.Map.findOrErr_ok_iff_in_values` (theorem, [line 1044](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1044))

> The `mp` direction of this does not need the `wf` precondition and, in fact,
> is available separately as `findOrErr_ok_implies_in_values` above

```lean
public theorem findOrErr_ok_iff_in_values [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] {m : Map α β} {v : β} {e : Error}
  (wf : m.WellFormed) :
  (∃ k, m.findOrErr k e = .ok v) ↔ v ∈ m.values
```

`Cedar.Data.Map.findOrErr_err_iff_not_in_keys` (theorem, [line 1051](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1051))

```lean
public theorem findOrErr_err_iff_not_in_keys [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] {m : Map α β} {k : α} {e : Error}
  (wf : m.WellFormed) :
  m.findOrErr k e = .error e ↔ k ∉ m.keys
```

`Cedar.Data.Map.in_toList_in_mapOnValues` (theorem, [line 1062](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1062))

> The converse requires the extra precondition that `f` is injective, and is
> available as `in_mapOnValues_in_toList`

```lean
public theorem in_toList_in_mapOnValues [LT α] [DecidableLT α] [DecidableEq α] (f : β → γ) {m : Map α β} {k : α} {v : β} :
  (k, v) ∈ m.toList → (k, f v) ∈ (m.mapOnValues f).toList
```

`Cedar.Data.Map.find?_none_iff_findorErr_errors` (theorem, [line 1073](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1073))

> …

```lean
public theorem find?_none_iff_findorErr_errors [LT α] [DecidableLT α] [DecidableEq α] {m : Map α β} {k : α} (e : Error) :
  m.find? k = none ↔ m.findOrErr k e = .error e
```

`Cedar.Data.Map.in_mapOnValues_in_toList` (theorem, [line 1081](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1081))

> Converse of `in_toList_in_mapOnValues`; requires the extra precondition that `f` is injective

```lean
public theorem in_mapOnValues_in_toList [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] {f : β → γ} {m : Map α β} {k : α} {v : β} :
  (k, f v) ∈ (m.mapOnValues f).toList →
  (∀ v', f v = f v' → v = v') → -- require f to be injective
  (k, v) ∈ m.toList
```

`Cedar.Data.Map.in_mapOnValues_in_toList'` (theorem, [line 1096](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1096))

> Slightly different formulation of `in_mapOnValues_in_toList`

```lean
public theorem in_mapOnValues_in_toList' [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α] {f : β → γ} {m : Map α β} {k : α} {v' : γ} :
  (k, v') ∈ (m.mapOnValues f).toList →
  ∃ v, f v = v' ∧ (k, v) ∈ m.toList
```

> ### mapMOnValues

`Cedar.Data.Map.mapMOnValues₂_eq_mapMOnValues` (theorem, [line 1107](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1107))

```lean
public theorem mapMOnValues₂_eq_mapMOnValues {α β γ : Type 0} [LT α] [DecidableLT α] [SizeOf α] [SizeOf β] [Monad m] [LawfulMonad m] (map : Map α β) (f : β → m γ) :
  map.mapMOnValues₂ (λ x : { x : β // sizeOf x < sizeOf map } => f x.1) = map.mapMOnValues f
```

`Cedar.Data.Map.mapMOnValues_empty` (theorem, [line 1113](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1113))

```lean
public theorem mapMOnValues_empty [LT α] [DecidableLT α] [Monad m] [LawfulMonad m] (f : β → m γ) :
  (empty : Map α β).mapMOnValues f = pure empty
```

`Cedar.Data.Map.mapMOnValues_mapOnValues` (theorem, [line 1118](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1118))

```lean
public theorem mapMOnValues_mapOnValues [LT α] [DecidableLT α] [Monad m] [LawfulMonad m] (map : Map α β) (f : β → γ) (g : γ → m φ) :
  mapMOnValues g (map.mapOnValues f) = map.mapMOnValues (g ∘ f)
```

`Cedar.Data.Map.mapMOnValues_some` (theorem, [line 1128](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1128))

> Mapping every value to `some` preserves the map.

```lean
public theorem mapMOnValues_some {α β} [LT α] [DecidableLT α]
    (m : Map α β) :
    m.mapMOnValues some = some m
```

`Cedar.Data.Map.mapMOnValues_isSome` (theorem, [line 1139](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1139))

> Mapping map values succeeds exactly when every application succeeds.

```lean
public theorem mapMOnValues_isSome {α β γ} [LT α] [DecidableLT α]
    (m : Map α β) (f : β → Option γ) :
    (m.mapMOnValues f).isSome = m.values.all (fun value => (f value).isSome)
```

`Cedar.Data.Map.mapMOnValues_preserves_keys` (theorem, [line 1162](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1162))

> This is not stated in terms of `Map.keys` because `Map.keys` produces a `Set`,
> and we want the even stronger property that it not only preserves the key-set,
> but also the key-order. (We'll use this to prove `mapMOnValues_some_wf`.)

```lean
public theorem mapMOnValues_preserves_keys [LT α] [DecidableLT α] [StrictLT α] {f : β → Option γ} {m₁ : Map α β} {m₂ : Map α γ} :
  m₁.mapMOnValues f = some m₂ →
  m₁.toList.map Prod.fst = m₂.toList.map Prod.fst
```

`Cedar.Data.Map.mapMOnValues_some_wf` (theorem, [line 1187](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1187))

```lean
public theorem mapMOnValues_some_wf [LT α] [DecidableLT α] [StrictLT α] {f : β → Option γ} {m₁ : Map α β} {m₂ : Map α γ} :
  m₁.WellFormed →
  (m₁.mapMOnValues f = some m₂) →
  m₂.WellFormed
```

`Cedar.Data.Map.mapMOnValues_ok_wf` (theorem, [line 1221](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1221))

```lean
public theorem mapMOnValues_ok_wf [LT α] [DecidableLT α] [StrictLT α] {f : β → Except ε γ} {m₁ : Map α β} {m₂ : Map α γ} :
  m₁.WellFormed →
  (m₁.mapMOnValues f = .ok m₂) →
  m₂.WellFormed
```

`Cedar.Data.Map.mapMOnValues_cons` (theorem, [line 1242](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1242))

```lean
public theorem mapMOnValues_cons {α : Type 0} [LT α] [DecidableLT α] {f : β → Option γ} {m : Map α β} {k : α} {v : β} {tl : List (α × β)}:
  m.toList = (k, v) :: tl →
  (m.mapMOnValues f = do
    let v' ← f v
    let tl' ← (mk tl).mapMOnValues f
    return mk ((k, v') :: tl'.toList))
```

`Cedar.Data.Map.mapOnValues_eq_of_mapMOnValues_some` (theorem, [line 1298](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1298))

> If a partial map of values succeeds, mapping a corresponding total function
> produces the same map.

```lean
public theorem mapOnValues_eq_of_mapMOnValues_some
    {α β γ} [LT α] [DecidableLT α]
    {m : Map α β} {out : Map α γ} {f : β → Option γ}
    (g : β → γ)
    (hmap : m.mapMOnValues f = some out)
    (hfg : ∀ input output, f input = some output → g input = output) :
    m.mapOnValues g = out
```

`Cedar.Data.Map.mapMOnValues_some_implies_all_some` (theorem, [line 1338](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1338))

```lean
public theorem mapMOnValues_some_implies_all_some {α : Type 0} [LT α] [DecidableLT α] {f : β → Option γ} {m₁ : Map α β} {m₂ : Map α γ} :
  m₁.mapMOnValues f = some m₂ →
  ∀ kv ∈ m₁.toList, ∃ v, (kv.fst, v) ∈ m₂.toList ∧ f kv.snd = some v
```

`Cedar.Data.Map.mapMOnValues_some_implies_all_from_some` (theorem, [line 1376](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1376))

```lean
public theorem mapMOnValues_some_implies_all_from_some [LT α] [DecidableLT α] {f : β → Option γ} {m₁ : Map α β} {m₂ : Map α γ} :
  m₁.mapMOnValues f = some m₂ →
  ∀ kv ∈ m₂.toList, ∃ v, (kv.fst, v) ∈ m₁.toList ∧ f v = kv.snd
```

`Cedar.Data.Map.mapMOnValues_none_iff_exists_none` (theorem, [line 1414](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1414))

```lean
public theorem mapMOnValues_none_iff_exists_none {α : Type 0} [LT α] [DecidableLT α] {f : β → Option γ} {m : Map α β} :
  m.mapMOnValues f = none ↔ ∃ v ∈ m.values, f v = none
```

`Cedar.Data.Map.mapMOnValues_ok_implies_all_ok` (theorem, [line 1466](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1466))

> Note that the converse is not true:
> counterexample `m₁` is `[(1, false)]`, `m₂` is `[(1, false), (2, true)]`, `f` is `Except.ok`
>
> But for a limited converse, see `all_ok_implies_mapMOnValues_ok`

```lean
public theorem mapMOnValues_ok_implies_all_ok [LT α] [DecidableLT α] {f : β → Except ε γ} {m₁ : Map α β} {m₂ : Map α γ} :
  m₁.mapMOnValues f = .ok m₂ →
  ∀ kv ∈ m₁.toList, ∃ v, (kv.fst, v) ∈ m₂.toList ∧ f kv.snd = .ok v
```

`Cedar.Data.Map.mapMOnValues_ok_implies_all_from_ok` (theorem, [line 1485](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1485))

```lean
public theorem mapMOnValues_ok_implies_all_from_ok [LT α] [DecidableLT α] {f : β → Except ε γ} {m₁ : Map α β} {m₂ : Map α γ} :
  m₁.mapMOnValues f = .ok m₂ →
  ∀ kv ∈ m₂.toList, ∃ v, (kv.fst, v) ∈ m₁.toList ∧ f v = .ok kv.snd
```

`Cedar.Data.Map.all_ok_implies_mapMOnValues_ok` (theorem, [line 1504](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1504))

```lean
public theorem all_ok_implies_mapMOnValues_ok [LT α] [DecidableLT α] {f : β → Except ε γ} {m₁ : Map α β} :
  (∀ kv ∈ m₁.toList, ∃ v, f kv.snd = .ok v) →
  ∃ m₂, m₁.mapMOnValues f = .ok m₂
```

`Cedar.Data.Map.mapMOnValues_error_implies_exists_error` (theorem, [line 1520](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1520))

```lean
public theorem mapMOnValues_error_implies_exists_error [LT α] [DecidableLT α] {f : β → Except ε γ} {m : Map α β} {e : ε} :
  m.mapMOnValues f = .error e → ∃ v ∈ m.values, f v = .error e
```

`Cedar.Data.Map.wellFormed_correct` (theorem, [line 1531](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1531))

```lean
public theorem wellFormed_correct {α β} [LT α] [StrictLT α] [DecidableLT α] {m : Map α β} :
  m.wellFormed = true ↔ m.WellFormed
```

`Cedar.Data.Map.make_find?_eq_list_find?` (theorem, [line 1562](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1562))

```lean
public theorem make_find?_eq_list_find?
  [DecidableEq α] [LT α] [DecidableLT α]
  [Cedar.Data.StrictLT α]
  {l : List (α × β)}
  {k : α} :
  (make l).find? k = (List.find? (λ x => x.fst == k) l).map Prod.snd
```

`Cedar.Data.Map.make_toList_map_find?` (theorem, [line 1584](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1584))

> Rebuilding a map from its entries with key-dependent values.

```lean
public theorem make_toList_map_find? {α β γ}
  [DecidableEq α] [LT α] [DecidableLT α] [StrictLT α]
  (m : Map α β) (g : α → β → γ) (k : α) :
  (Map.make (m.toList.map fun kv => (kv.fst, g kv.fst kv.snd))).find? k =
    (m.find? k).map (g k)
```

`Cedar.Data.Map.list_find?_iff_make_find?` (theorem, [line 1598](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1598))

```lean
public theorem list_find?_iff_make_find?
  [DecidableEq α] [LT α] [DecidableLT α]
  [Cedar.Data.StrictLT α]
  {l : List (α × β)}
  {k : α} {v : β} :
  List.find? (λ x => x.fst == k) l = some (k, v) ↔
  (make l).find? k = some v
```

`Cedar.Data.Map.list_find?_iff_mk_find?` (theorem, [line 1619](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1619))

```lean
public theorem list_find?_iff_mk_find?
  [DecidableEq α] [LT α] [DecidableLT α]
  [Cedar.Data.StrictLT α]
  {l : List (α × β)}
  {k : α} {v : β} :
  List.find? (λ x => x.fst == k) l = some (k, v) ↔
  (mk l).find? k = some v
```

`Cedar.Data.Map.map_make_append_find_disjoint` (theorem, [line 1648](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1648))

> If a key exists in `l₂` but not in `l₁`,
> then `Map.make (l₁ ++ l₂)` contains that key.

```lean
public theorem map_make_append_find_disjoint
  [LT α] [StrictLT α] [DecidableEq α] [DecidableLT α]
  [SizeOf α] [SizeOf β]
  {l₁ : List (α × β)} {l₂ : List (α × β)} {k : α}
  (hfind₁ : l₁.find? (λ ⟨k', _⟩ => k' == k) = none)
  (hfind₂ : (l₂.find? (λ ⟨k', _⟩ => k' == k)).isSome) :
  ∃ v,
    (Map.make (l₁ ++ l₂)).find? k = some v ∧
    (k, v) ∈ l₂
```

`Cedar.Data.Map.make_map_values_find` (theorem, [line 1688](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1688))

```lean
public theorem make_map_values_find
  [DecidableEq α] [LT α] [DecidableLT α]
  [Cedar.Data.StrictLT α]
  {l : List α}
  {f : α → β}
  {k : α}
  (hfind : k ∈ l) :
  (Map.make (l.map (λ x => (x, f x)))).find? k =
  .some (f k)
```

`Cedar.Data.Map.map_toList_findSome?` (theorem, [line 1707](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1707))

```lean
public theorem map_toList_findSome?
  [BEq α] [LawfulBEq α]
  {m : Map α β} {k : α} {v : β} {v' : γ}
  {f : α × β → Option γ}
  (hfind : Map.find? m k = .some v)
  (hf : ∀ kv, (∃ v', f kv = .some v') → kv.1 = k)
  (hkv : f (k, v) = .some v') :
  m.toList.findSome? f = .some v'
```

`Cedar.Data.Map.map_find?_to_list_find?` (theorem, [line 1755](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1755))

```lean
public theorem map_find?_to_list_find?
  [BEq α] [LawfulBEq α]
  {m : Map α β} {k : α} {v : β}
  (hfind : Map.find? m k = .some v) :
  List.find? (λ x => x.fst == k) (Map.toList m) = .some (k, v)
```

`Cedar.Data.Map.map_make_append_find_disjoint'` (theorem, [line 1772](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1772))

> A variant of `map_make_append_find_disjoint`.

```lean
public theorem map_make_append_find_disjoint'
  [LT α] [StrictLT α] [DecidableEq α] [DecidableLT α]
  [SizeOf α] [SizeOf β]
  {l₁ : List (α × β)} {l₂ : List (α × β)} {k : α} {v : β}
  (hfind₁ : l₁.find? (λ ⟨k', _⟩ => k' == k) = none)
  (hfind₂ : l₂.find? (λ ⟨k', _⟩ => k' == k) = .some (k, v))
  (heq : ∀ x₁ x₂, x₁ ∈ l₂ → x₂ ∈ l₂ → x₁.fst = x₂.fst → x₁ = x₂) :
  (Map.make (l₁ ++ l₂)).find? k = some v
```

`Cedar.Data.Map.map_find?_implies_find?_weaker_pred` (theorem, [line 1789](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1789))

```lean
public theorem map_find?_implies_find?_weaker_pred
  [BEq α] [LawfulBEq α]
  {m : Map α β} {k : α} {v : β} {f : α × β → Bool}
  (hfind : Map.find? m k = .some v)
  (hf : ∀ kv, f kv → kv.1 = k)
  (hkv : f (k, v)) :
  List.find? f (Map.toList m) = .some (k, v)
```

`Cedar.Data.Map.map_keys_empty_implies_map_empty` (theorem, [line 1818](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1818))

```lean
public theorem map_keys_empty_implies_map_empty
  {m : Map α β}
  (h : m.keys.toList = []) :
  m = Map.empty
```

`Cedar.Data.Map.toList_congr` (theorem, [line 1831](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1831))

> …

```lean
public theorem toList_congr
  {m₁ m₂ : Map α β}
  (h : m₁.toList = m₂.toList) :
  m₁ = m₂
```

`Cedar.Data.Map.find?_append` (theorem, [line 1839](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1839))

```lean
public theorem find?_append
  [LT α] [StrictLT α] [DecidableEq α] [DecidableLT α]
  {m₁ m₂ : Map α β} {k : α}:
  (m₁ ++ m₂).find? k = (m₁.find? k).or (m₂.find? k)
```

`Cedar.Data.Map.contains_append` (theorem, [line 1856](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1856))

```lean
public theorem contains_append
  [LT α] [StrictLT α] [DecidableLT α][DecidableEq α] {m₁ m₂ : Map α β} {k : α} :
  (m₁ ++ m₂).contains k ↔ m₁.contains k ∨ m₂.contains k
```

`Cedar.Data.Map.find?_append_right` (theorem, [line 1868](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1868))

```lean
public theorem find?_append_right
  [LT α] [StrictLT α] [DecidableEq α] [DecidableLT α]
  {m₁ m₂ : Map α β} {k : α} :
  m₁.contains k = false → (m₁ ++ m₂).find? k = m₂.find? k
```

`Cedar.Data.Map.find?_append_left` (theorem, [line 1879](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1879))

```lean
public theorem find?_append_left
  [LT α] [StrictLT α] [DecidableEq α] [DecidableLT α]
  {m₁ m₂ : Map α β} {k : α} :
  m₂.contains k = false → (m₁ ++ m₂).find? k = m₁.find? k
```

`Cedar.Data.Map.filter_wf` (theorem, [line 1890](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1890))

```lean
public theorem filter_wf [LT α] [DecidableLT α] [StrictLT α] (p : α → β → Bool) (m : Map α β) :
  WellFormed m →
  WellFormed (m.filter p)
```

`Cedar.Data.Map.find?_filter_if_find?` (theorem, [line 1897](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1897))

```lean
public theorem find?_filter_if_find? {α : Type u} {β : Type v} [BEq α] [LawfulBEq α]
  {k : α} {val : β} {m : Map α β} {p : α → β → Bool} :
  m.find? k = some val → p k val = true →
  ((m.filter p).find? k = some val)
```

`Cedar.Data.Map.find?_filter_iff_find` (theorem, [line 1931](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1931))

```lean
public theorem find?_filter_iff_find {α : Type u} {β : Type v} [BEq α] [LawfulBEq α] [DecidableEq α] [LT α] [StrictLT α] [DecidableLT α]
  {k : α} {val : β} {m : Map α β} {p : α → β → Bool} :
  m.WellFormed →
  ((m.find? k = some val ∧ p k val = true) ↔ ((m.filter p).find? k = some val))
```

`Cedar.Data.Map.filter_contains_if_find_matching` (theorem, [line 1952](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1952))

```lean
public theorem filter_contains_if_find_matching {α : Type u} {β : Type v} [BEq α] [LawfulBEq α]
  {k : α} {m : Map α β} {p : α → β → Bool} :
  (∃ v, m.find? k = some v ∧ p k v = true) → (m.filter p).contains k
```

`Cedar.Data.Map.find_matching_iff_filter_contains` (theorem, [line 1961](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1961))

```lean
public theorem find_matching_iff_filter_contains {α : Type u} {β : Type v} [BEq α] [LawfulBEq α] [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α]
  {k : α} {m : Map α β} (p : α → β → Bool) :
  m.WellFormed →
  ((∃ v, m.find? k = some v ∧ p k v = true) ↔ (m.filter p).contains k)
```

`Cedar.Data.Map.filter_not_contains` (theorem, [line 1971](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean#L1971))

```lean
public theorem filter_not_contains {α : Type u} {β : Type v} [BEq α] [LawfulBEq α] (k : α) (m : Map α β) :
  (m.filter (λ k' _ => k' != k)|>.contains k) = false
```

## Depends on

- [Map](../../data/map.md)
- [Set properties](set.md)

## Proof depends on

- [SizeOf](../../data/sizeof.md)

## Sources

- [Cedar/Thm/Data/Map.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Map.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Data.Map.json)
