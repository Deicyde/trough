---
catalog: module
lean: Cedar.Data.List.sizeOf_attach₂, Cedar.Data.List.sizeOf_attach₃, Cedar.Data.Map.sizeOf_lt_of_value, Cedar.Data.Map.sizeOf_lt_of_find?, Cedar.Data.Map.sizeOf_lt_of_toList, Cedar.Data.Map.sizeOf_lt_of_values, Cedar.Data.Map.sizeOf_lt_of_tl, Cedar.Data.Set.sizeOf_lt_of_mem, Cedar.Data.Set.sizeOf_lt_of_elts, Cedar.Data.Set.sizeOf_mk
statement: formalized
proof: formalized
---

# SizeOf

`Cedar.Data.SizeOf`, in [Cedar/Data/SizeOf.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/SizeOf.lean).

> Lemmas involving `sizeOf`, which are located here rather than in `Cedar/Thm`
> because they are needed for some definitions in `Cedar/Spec` and/or
> `Cedar/Partial`, and our convention prevents files in `Cedar/Spec` or
> `Cedar/Partial` from depending on lemmas in `Cedar/Thm`.

> ## List

`Cedar.Data.List.sizeOf_attach₂` (theorem, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/SizeOf.lean#L34))

```lean
public theorem sizeOf_attach₂ [SizeOf α] [SizeOf β] {a : α} {b : β} {l : List (α × β)} :
  (a, b) ∈ l → sizeOf (a, b).snd < 1 + sizeOf l
```

`Cedar.Data.List.sizeOf_attach₃` (theorem, [line 43](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/SizeOf.lean#L43))

```lean
public theorem sizeOf_attach₃ [SizeOf α] [SizeOf β] {a : α} {b : β} {l : List (α × β)} :
  (a, b) ∈ l → sizeOf (a, b).snd < 1 + (1 + sizeOf l)
```

> ## Map

`Cedar.Data.Map.sizeOf_lt_of_value` (theorem, [line 58](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/SizeOf.lean#L58))

```lean
public theorem sizeOf_lt_of_value [SizeOf α] [SizeOf β] {m : Map α β} {k : α} {v : β}
  (h : (k, v) ∈ m.1) :
  sizeOf v < sizeOf m
```

`Cedar.Data.Map.sizeOf_lt_of_find?` (theorem, [line 72](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/SizeOf.lean#L72))

```lean
public theorem sizeOf_lt_of_find? [SizeOf α] [SizeOf β] [DecidableEq α] {m : Map α β} {k : α} {v : β}
  (h : m.find? k = some v) :
  sizeOf v < sizeOf m
```

`Cedar.Data.Map.sizeOf_lt_of_toList` (theorem, [line 85](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/SizeOf.lean#L85))

```lean
public theorem sizeOf_lt_of_toList [SizeOf α] [SizeOf β] (m : Map α β) :
  sizeOf m.toList < sizeOf m
```

`Cedar.Data.Map.sizeOf_lt_of_values` (theorem, [line 93](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/SizeOf.lean#L93))

```lean
public theorem sizeOf_lt_of_values [SizeOf α] [SizeOf β] {m : Map α β}
  (h : b ∈ m.values) :
  sizeOf b < sizeOf m
```

`Cedar.Data.Map.sizeOf_lt_of_tl` (theorem, [line 101](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/SizeOf.lean#L101))

```lean
public theorem sizeOf_lt_of_tl [SizeOf α] [SizeOf β] {m : Map α β} {tl : List (α × β)}
  (h : m.toList = (k, v) :: tl) :
  1 + sizeOf tl < sizeOf m
```

> ## Set

`Cedar.Data.Set.sizeOf_lt_of_mem` (theorem, [line 117](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/SizeOf.lean#L117))

```lean
public theorem sizeOf_lt_of_mem [SizeOf α] {s : Set α}
  (h : a ∈ s) :
  sizeOf a < sizeOf s
```

`Cedar.Data.Set.sizeOf_lt_of_elts` (theorem, [line 128](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/SizeOf.lean#L128))

```lean
public theorem sizeOf_lt_of_elts [SizeOf α] (s : Set α) :
  sizeOf s.elts < sizeOf s
```

`Cedar.Data.Set.sizeOf_mk` (theorem, [line 135](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/SizeOf.lean#L135))

```lean
public theorem sizeOf_mk [SizeOf α] (xs : List α) :
  sizeOf (Set.mk xs) = 1 + sizeOf xs
```

## Depends on

- [Map](map.md)

## Sources

- [Cedar/Data/SizeOf.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/SizeOf.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Data.SizeOf.json)
