---
catalog: module
lean: Cedar.Data.Set, Cedar.Data.Set.elts, Cedar.Data.Set.toList, Cedar.Data.Set.make, Cedar.Data.Set.empty, Cedar.Data.Set.isEmpty, Cedar.Data.Set.contains, Cedar.Data.Set.subset, Cedar.Data.Set.intersects, Cedar.Data.Set.intersect, Cedar.Data.Set.union, Cedar.Data.Set.filter, Cedar.Data.Set.difference, Cedar.Data.Set.map, Cedar.Data.Set.mapOrErr, Cedar.Data.Set.all, Cedar.Data.Set.any, Cedar.Data.Set.size, Cedar.Data.Set.singleton, Cedar.Data.Set.wellFormed, Cedar.Data.Set.singleton?, Cedar.Data.Set.foldl, Cedar.Data.Set.product, Cedar.Data.Set.decLt, Cedar.Data.Set.map₁, Cedar.Data.Set.all₁, Cedar.Data.Set.any₁
statement: formalized
proof: formalized
---

# Canonical list-based sets

`Cedar.Data.Set`, in [Cedar/Data/Set.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean).

> This file defines a simple set data type, backed by a sorted duplicate-free
> list. Functions on sets assume but don't require their inputs to be well-formed
> (sorted and duplicate-free). Separate theorems show that these functions produce
> well-formed outputs when given well-formed inputs.
>
> Use `Set.make` to construct well-formed sets from lists.

`Cedar.Data.Set` (inductive type, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L36))

```lean
public inductive Set (α : Type u) where
```

`Cedar.Data.Set.elts` (abbreviation, [line 42](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L42))

```lean
public abbrev elts {α : Type u} (s : Set α)
```

`Cedar.Data.Set.toList` (definition, [line 51](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L51))

> Creates an ordered/duplicate free list from a set provided the underlying
> set is well formed.

```lean
public def toList {α : Type u} (s : Set α) : List α
```

`Cedar.Data.Set.make` (definition, [line 54](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L54))

> Creates a well-formed set from the given list.

```lean
public def make [LT α] [DecidableLT α] (elts : List α) : Set α
```

`Cedar.Data.Set.empty` (definition, [line 58](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L58))

> Empty set ∅

```lean
public def empty {α} : Set α
```

`Cedar.Data.Set.isEmpty` (definition, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L61))

> s == ∅

```lean
public def isEmpty {α} [DecidableEq α] (s : Set α) : Bool
```

`Cedar.Data.Set.contains` (definition, [line 65](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L65))

> elt ∈ s

```lean
public def contains {α} [DecidableEq α] (s : Set α) (elt : α) : Bool
```

`Cedar.Data.Set.subset` (definition, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L69))

> s₁ ⊆ s₂

```lean
public def subset {α} [DecidableEq α] (s₁ s₂ : Set α) : Bool
```

`Cedar.Data.Set.intersects` (definition, [line 73](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L73))

> s₁ ∩ s₂ ≠ ∅

```lean
public def intersects {α} [DecidableEq α] (s₁ s₂ : Set α) : Bool
```

`Cedar.Data.Set.intersect` (definition, [line 77](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L77))

> s₁ ∩ s₂

```lean
public def intersect {α} [DecidableEq α] (s₁ s₂ : Set α) : Set α
```

`Cedar.Data.Set.union` (definition, [line 81](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L81))

> s₁ ∪ s₂

```lean
public def union {α} [LT α] [DecidableLT α] (s₁ s₂ : Set α) : Set α
```

`Cedar.Data.Set.filter` (definition, [line 88](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L88))

> Filters `s` using `f`.

```lean
public def filter {α} (f : α → Bool) (s : Set α) : Set α
```

`Cedar.Data.Set.difference` (definition, [line 92](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L92))

> s₁ \ s₂.

```lean
public def difference {α} [LT α] [DecidableLT α] [DecidableEq α] (s₁ s₂ : Set α) : Set α
```

`Cedar.Data.Set.map` (definition, [line 96](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L96))

> Maps `f` to `s`.

```lean
public def map {α β} [LT β] [DecidableLT β] (f : α → β) (s : Set α) : Set β
```

`Cedar.Data.Set.mapOrErr` (definition, [line 100](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L100))

> Maps `f` to `s` and returns the result of `err` if any error is encountered.

```lean
public def mapOrErr {α β ε} [DecidableEq β] [LT β] [DecidableRel (α := β) (· < ·)] (f : α → Except ε β) (s : Set α) (err : ε) : Except ε (Set β)
```

`Cedar.Data.Set.all` (definition, [line 106](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L106))

> Returns true if all elements of `s` satisfy `f`.

```lean
public def all {α} (f : α → Bool) (s : Set α) : Bool
```

`Cedar.Data.Set.any` (definition, [line 110](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L110))

> Returns true if some element of `s` satisfies `f`.

```lean
public def any {α} (f : α → Bool) (s : Set α) : Bool
```

`Cedar.Data.Set.size` (definition, [line 113](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L113))

```lean
public def size {α} (s : Set α) : Nat
```

`Cedar.Data.Set.singleton` (definition, [line 116](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L116))

```lean
public def singleton {α} (a : α) : Set α
```

`Cedar.Data.Set.wellFormed` (definition, [line 120](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L120))

> Checks if a set if well-formed

```lean
public def wellFormed {α} [LT α] [DecidableLT α] (s : Set α) : Bool
```

`Cedar.Data.Set.singleton?` (definition, [line 124](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L124))

> If `s` is a singleton set, returns the single element

```lean
public def singleton? [Inhabited α] (s : Set α) : Option α
```

`Cedar.Data.Set.foldl` (definition, [line 130](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L130))

```lean
public def foldl {α β} (f : α → β → α) (init : α) (s : Set β) : α
```

`Cedar.Data.Set.product` (definition, [line 133](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L133))

```lean
public def product {α β} (s₁ : Set α) (s₂ : Set β) : Set (α × β)
```

`Cedar.Data.Set.decLt` (instance, [line 141](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L141))

```lean
public instance decLt [LT α] [DecidableEq α] [DecidableLT α] : (n m : Set α) → Decidable (n < m)
```

`Cedar.Data.Set.map₁` (definition, [line 164](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L164))

```lean
public def map₁ {α} [LT β] [DecidableLT β] (s : Set α) (f : {a : α // a ∈ s} → β) : Set β
```

`Cedar.Data.Set.all₁` (definition, [line 167](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L167))

```lean
public def all₁ {α} (s : Set α) (f : {a : α // a ∈ s} → Bool) : Bool
```

`Cedar.Data.Set.any₁` (definition, [line 170](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean#L170))

```lean
public def any₁ {α} (s : Set α) (f : {a : α // a ∈ s} → Bool) : Bool
```

## Depends on

- [List](list.md)

## Sources

- [Cedar/Data/Set.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Set.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Data.Set.json)
