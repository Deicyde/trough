---
catalog: module
lean: Cedar.Data.Map, Cedar.Data.Map.make, Cedar.Data.Map.empty, Cedar.Data.Map.toList, Cedar.Data.Map.keys, Cedar.Data.Map.values, Cedar.Data.Map.find?, Cedar.Data.Map.contains, Cedar.Data.Map.findOrErr, Cedar.Data.Map.find!, Cedar.Data.Map.filter, Cedar.Data.Map.size, Cedar.Data.Map.mapOnValues, Cedar.Data.Map.mapOnKeys, Cedar.Data.Map.mapMOnValues, Cedar.Data.Map.mapMOnKeys, Cedar.Data.Map.mapOnValues₂, Cedar.Data.Map.mapMOnValues₂, Cedar.Data.Map.wellFormed, Cedar.Data.Map.decLt
statement: formalized
proof: formalized
---

# Map

`Cedar.Data.Map`, in [Cedar/Data/Map.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean).

> This file defines a simple map data types, backed by a sorted duplicate-free
> list of key-value. Functions maps assume but don't require that their inputs are
> well-formed (sorted and duplicate-free). Separate theorems show that these
> functions produce well-formed outputs when given well-formed inputs.
>
> Use `Map.make` to construct well-formed maps from lists of key-value pairs.

`Cedar.Data.Map` (inductive type, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L34))

```lean
public inductive Map (α : Type u) (β : Type v) where
```

`Cedar.Data.Map.make` (definition, [line 43](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L43))

> Creates a well-formed map from the given list of pairs.

```lean
public def make {α β} [LT α] [DecidableLT α] (kvs : List (α × β)) : Map α β
```

`Cedar.Data.Map.empty` (definition, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L47))

> Empty map

```lean
public def empty {α β} : Map α β
```

`Cedar.Data.Map.toList` (definition, [line 50](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L50))

> Returns an ordered and duplicate free list provided the given map is well-formed.

```lean
public def toList {α : Type u} {β : Type v} (m : Map α β) : List (Prod α β)
```

`Cedar.Data.Map.keys` (definition, [line 53](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L53))

> Returns the keys of `m` as a set.

```lean
public def keys {α β} (m : Map α β) : Set α
```

`Cedar.Data.Map.values` (definition, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L57))

> Returns the values of `m` as a list.

```lean
public def values {α β} (m : Map α β) : List β
```

`Cedar.Data.Map.find?` (definition, [line 62](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L62))

> Returns the binding for `k` in `m`, if any.

```lean
public def find? {α β} [BEq α] (m : Map α β) (k : α) : Option β
```

`Cedar.Data.Map.contains` (definition, [line 68](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L68))

> Returns true if `m` contains a mapping for the key `k`.

```lean
public def contains {α β} [BEq α] (m : Map α β) (k : α) : Bool
```

`Cedar.Data.Map.findOrErr` (definition, [line 72](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L72))

> Returns the binding for `k` in `m` or `err` if none is found.

```lean
public def findOrErr {α β ε} [BEq α] (m : Map α β) (k : α) (err: ε) : Except ε β
```

`Cedar.Data.Map.find!` (definition, [line 78](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L78))

> Returns the binding for `k` in `m`, or panics if none is found.

```lean
public def find! {α β} [Repr α] [BEq α] [Inhabited β] (m : Map α β) (k : α) : β
```

`Cedar.Data.Map.filter` (definition, [line 84](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L84))

> Filters `m` using `f`.

```lean
public def filter {α β} (f : α → β → Bool) (m : Map α β) : Map α β
```

`Cedar.Data.Map.size` (definition, [line 87](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L87))

```lean
public def size {α β} (m : Map α β) : Nat
```

`Cedar.Data.Map.mapOnValues` (definition, [line 90](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L90))

```lean
public def mapOnValues {α β γ} (f : β → γ) (m : Map α β) : Map α γ
```

`Cedar.Data.Map.mapOnKeys` (definition, [line 93](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L93))

```lean
public def mapOnKeys {α β γ} [LT γ] [DecidableLT γ] (f : α → γ) (m : Map α β) : Map γ β
```

`Cedar.Data.Map.mapMOnValues` (definition, [line 96](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L96))

```lean
public def mapMOnValues {α β γ} [LT α] [DecidableLT α] [Monad m] (f : β → m γ) (map : Map α β) : m (Map α γ)
```

`Cedar.Data.Map.mapMOnKeys` (definition, [line 100](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L100))

```lean
public def mapMOnKeys {α β γ} [LT γ] [DecidableLT γ] [Monad m] (f : α → m γ) (map : Map α β) : m (Map γ β)
```

`Cedar.Data.Map.mapOnValues₂` (definition, [line 111](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L111))

```lean
public def mapOnValues₂ {α β γ} [SizeOf α] [SizeOf β] (m : Map α β) (f : {x : β // sizeOf x < sizeOf m} → γ) : Map α γ
```

`Cedar.Data.Map.mapMOnValues₂` (definition, [line 117](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L117))

```lean
public def mapMOnValues₂ {α β γ} [SizeOf α] [SizeOf β] [Monad m] (map : Map α β) (f : {x : β // sizeOf x < sizeOf map} → m γ) : m (Map α γ)
```

`Cedar.Data.Map.wellFormed` (definition, [line 124](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L124))

```lean
public def wellFormed {α β} [LT α] [DecidableLT α] (m : Map α β) : Bool
```

`Cedar.Data.Map.decLt` (instance, [line 132](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean#L132))

```lean
public instance decLt [LT (Prod α β)] [DecidableEq (Prod α β)] [DecidableLT (Prod α β)] : (n m : Map α β) → Decidable (n < m)
```

## Depends on

- [Canonical list-based sets](set.md)

## Sources

- [Cedar/Data/Map.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Map.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Data.Map.json)
