---
catalog: module
lean: Cedar.Relation.transGen_head, Cedar.Relation.transGen_tail, Cedar.Relation.transGen_mono, Cedar.Relation.Walk, Cedar.Relation.Walk.append, Cedar.Relation.Walk.of_transGen, Cedar.Relation.Walk.source_edge, Cedar.Relation.Walk.suffix, Cedar.Relation.Walk.nodup
statement: formalized
proof: formalized
---

# Paths along a relation

`Cedar.Thm.Data.Relation`, in [Cedar/Thm/Data/Relation.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Relation.lean).

> Facts about `Relation.TransGen`, and about walks: paths that record the vertex
> each of their edges leaves from.
>
> They live in `Cedar.Relation` rather than `Relation`, like the Mathlib copies in
> `Cedar.List`, so that a file can import both Cedar and Mathlib.

`Cedar.Relation.transGen_head` (theorem, [line 32](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Relation.lean#L32))

> A path starts with an edge.

```lean
public theorem transGen_head {α} {r : α → α → Prop} {a b : α}
  (h : Relation.TransGen r a b) : ∃ c, r a c
```

`Cedar.Relation.transGen_tail` (theorem, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Relation.lean#L40))

> A path ends with an edge.

```lean
public theorem transGen_tail {α} {r : α → α → Prop} {a b : α}
  (h : Relation.TransGen r a b) : ∃ c, r c b
```

`Cedar.Relation.transGen_mono` (theorem, [line 48](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Relation.lean#L48))

> A path stays a path along a larger relation.

```lean
public theorem transGen_mono {α} {r s : α → α → Prop} (hrs : ∀ a b, r a b → s a b)
  {a b : α} (h : Relation.TransGen r a b) : Relation.TransGen s a b
```

`Cedar.Relation.Walk` (inductive type, [line 56](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Relation.lean#L56))

> A path along `edge` from `x` to `y` whose edges leave from `srcs`, in order.

```lean
public inductive Walk {α} (edge : α → α → Prop) : α → α → List α → Prop
  | single {x y} : edge x y → Walk edge x y [x]
  | cons {x z y srcs} : edge x z → Walk edge z y srcs → Walk edge x y (x :: srcs)
```

`Cedar.Relation.Walk.append` (theorem, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Relation.lean#L61))

> Walks compose.

```lean
public theorem Walk.append {α} {edge : α → α → Prop} {x y z : α} {s₁ s₂ : List α}
  (h₁ : Walk edge x y s₁) (h₂ : Walk edge y z s₂) : Walk edge x z (s₁ ++ s₂)
```

`Cedar.Relation.Walk.of_transGen` (theorem, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Relation.lean#L69))

> Every path is a walk.

```lean
public theorem Walk.of_transGen {α} {edge : α → α → Prop} {x y : α}
  (h : Relation.TransGen edge x y) : ∃ srcs, Walk edge x y srcs
```

`Cedar.Relation.Walk.source_edge` (theorem, [line 79](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Relation.lean#L79))

> Every vertex a walk leaves from has an edge.

```lean
public theorem Walk.source_edge {α} {edge : α → α → Prop} {x y : α} {srcs : List α}
  (h : Walk edge x y srcs) : ∀ v ∈ srcs, ∃ w, edge v w
```

`Cedar.Relation.Walk.suffix` (theorem, [line 91](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Relation.lean#L91))

> A walk through `v` continues from `v` along a suffix of its sources.

```lean
public theorem Walk.suffix {α} {edge : α → α → Prop} {x y v : α} {srcs : List α}
  (h : Walk edge x y srcs) (hv : v ∈ srcs) :
  ∃ srcs', srcs' <:+ srcs ∧ Walk edge v y srcs'
```

`Cedar.Relation.Walk.nodup` (theorem, [line 106](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Relation.lean#L106))

> Every walk can be shortened to one that leaves from each vertex at most once.

```lean
public theorem Walk.nodup {α} {edge : α → α → Prop} {x y : α} {srcs : List α}
  (h : Walk edge x y srcs) :
  ∃ srcs', srcs'.Nodup ∧ srcs' ⊆ srcs ∧ Walk edge x y srcs'
```

## Depends on

Its statements use no other Cedar module's declarations.

## Sources

- [Cedar/Thm/Data/Relation.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Relation.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Data.Relation.json)
