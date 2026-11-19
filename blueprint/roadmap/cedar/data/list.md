---
catalog: module
lean: List.insertCanonical, List.canonicalize, List.mergeCanonical, List.sizeOf_snd_lt_sizeOf_list, List.attach₂, List.attach₃, List.map₁, List.map₂, List.map₃, List.mapM₁, List.mapM₂, List.mapM₃, List.mapUnion, List.mapUnion₁, List.mapUnion₂, List.mapUnion₃, List.isSortedBy, List.isSorted, List.ternaryAny
statement: formalized
proof: formalized
---

# List

`Cedar.Data.List`, in [Cedar/Data/List.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean).

> This file contains utilities for working with lists that are canonical or
> equivalent modulo ordering and duplicates.  A canonical list is sorted and
> duplicate-free according to a strict total order <.

`List.insertCanonical` (definition, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean#L34))

```lean
public def insertCanonical [LT β] [DecidableLT β] (f : α → β) (x : α) (xs : List α) : List α
```

`List.canonicalize` (definition, [line 51](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean#L51))

> If the ordering relation < on β is strict, then `canonicalize` returns a
> canonical representation of the input list, which is sorted and free of
> duplicates.

```lean
public def canonicalize [LT β] [DecidableLT β] (f : α → β) : List α → List α
```

`List.mergeCanonical` (definition, [line 59](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean#L59))

> Merge two lists. If the ordering relation < on α is strict and both inputs are
> canonical, then the result is canonical.

```lean
public def mergeCanonical [LT α] [DecidableLT α] : List α → List α → List α
```

`List.sizeOf_snd_lt_sizeOf_list` (theorem, [line 70](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean#L70))

```lean
public theorem sizeOf_snd_lt_sizeOf_list {α : Type u} {β : Type v} [SizeOf α] [SizeOf β] {x : α × β} {xs : List (α × β)} :
  x ∈ xs → sizeOf x.snd < 1 + sizeOf xs
```

`List.attach₂` (definition, [line 84](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean#L84))

```lean
public def attach₂ {α : Type u} {β : Type v} [SizeOf α] [SizeOf β] (xs : List (α × β)) :
List { x : α × β // sizeOf x.snd < 1 + sizeOf xs }
```

`List.attach₃` (definition, [line 89](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean#L89))

```lean
public def attach₃ {α : Type u} {β : Type v} [SizeOf α] [SizeOf β] (xs : List (α × β)) :
List { x : α × β // sizeOf x.snd < 1 + (1 + sizeOf xs) }
```

`List.map₁` (definition, [line 98](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean#L98))

```lean
public def map₁ {α : Type w} {β : Type u} (xs : List α) (f : {x : α // x ∈ xs} → β) : List β
```

`List.map₂` (definition, [line 101](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean#L101))

```lean
public def map₂ {α : Type w} {β : Type u} [SizeOf α] [SizeOf β] (xs : List (α × β)) (f : {x : α × β // sizeOf x.snd < 1 + sizeOf xs} → γ) : List γ
```

`List.map₃` (definition, [line 104](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean#L104))

```lean
public def map₃ {α : Type w} {β : Type u} [SizeOf α] [SizeOf β] (xs : List (α × β)) (f : {x : α × β // sizeOf x.snd < 1 + (1 + sizeOf xs)} → γ) : List γ
```

`List.mapM₁` (definition, [line 107](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean#L107))

```lean
public def mapM₁ {m : Type u → Type v} [Monad m] {α : Type w} {β : Type u}
  (xs : List α) (f : {x : α // x ∈ xs} → m β) : m (List β)
```

`List.mapM₂` (definition, [line 111](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean#L111))

```lean
public def mapM₂ {m : Type u → Type v} [Monad m] {γ : Type u} [SizeOf α] [SizeOf β]
  (xs : List (α × β)) (f : {x : α × β // sizeOf x.snd < 1 + sizeOf xs} → m γ) : m (List γ)
```

`List.mapM₃` (definition, [line 115](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean#L115))

```lean
public def mapM₃ {m : Type u → Type v} [Monad m] {γ : Type u} [SizeOf α] [SizeOf β]
  (xs : List (α × β)) (f : { x : α × β // sizeOf x.snd < 1 + (1 + sizeOf xs) } → m γ) : m (List γ)
```

`List.mapUnion` (definition, [line 126](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean#L126))

> Generalization of `List.flatMap` from the standard library:
> works for `f` returning various collection types, not just `List`.
>
> That said, if your `f` does return `List`, you may want to use `flatMap`
> instead, as there is a large library of lemmas about it in the standard library.

```lean
public def mapUnion {α β} [Union α] [EmptyCollection α] (f : β → α) (bs : List β) : α
```

`List.mapUnion₁` (definition, [line 129](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean#L129))

```lean
public def mapUnion₁ {α β} [Union α] [EmptyCollection α]
  (xs : List β) (f : {x : β // x ∈ xs} → α) : α
```

`List.mapUnion₂` (definition, [line 133](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean#L133))

```lean
public def mapUnion₂ {α β γ} [Union α] [EmptyCollection α] [SizeOf β] [SizeOf γ]
  (xs : List (β × γ)) (f : {x : β × γ // sizeOf x.snd < 1 + sizeOf xs} → α) : α
```

`List.mapUnion₃` (definition, [line 137](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean#L137))

```lean
public def mapUnion₃ [Union α] [EmptyCollection α] [SizeOf β] [SizeOf γ]
  (xs : List (β × γ)) (f : {x : β × γ // sizeOf x.snd < 1 + (1 + sizeOf xs) } → α) : α
```

`List.isSortedBy` (definition, [line 141](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean#L141))

```lean
public def isSortedBy {α β} [LT β] [DecidableLT β] (l : List α) (f : α → β) : Bool
```

`List.isSorted` (definition, [line 151](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean#L151))

```lean
public def isSorted {α} [LT α] [DecidableLT α] (l : List α) : Bool
```

`List.ternaryAny` (definition, [line 161](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean#L161))

```lean
public def ternaryAny  {α} (l : List α) (p : α → Option Bool) : Option Bool
```

## Depends on

Its statements use no other Cedar module's declarations.

## Sources

- [Cedar/Data/List.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/List.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Data.List.json)
