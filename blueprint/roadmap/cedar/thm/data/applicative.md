---
catalog: module
lean: applicative_none, applicative_of_none, applicative_some, applicative_step
statement: formalized
proof: formalized
---

# Applicative

`Cedar.Thm.Data.Applicative`, in [Cedar/Thm/Data/Applicative.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Applicative.lean).

`applicative_none` (theorem, [line 31](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Applicative.lean#L31))

```lean
public theorem applicative_none  {α β : Type} (f : Option (α → β)) (o : Option α) :
  f = none →
  f <*> o = none
```

`applicative_of_none` (theorem, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Applicative.lean#L39))

```lean
public theorem applicative_of_none {α β : Type} (f : Option (α → β )) (o : Option α) :
  o = none →
  f <*> o = none
```

`applicative_some` (theorem, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Applicative.lean#L47))

```lean
public theorem applicative_some {α β : Type} (f' : α → β) (v : α) :
  (some f') <*> (some v) = some (f' v)
```

`applicative_step` (theorem, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Applicative.lean#L52))

```lean
public theorem applicative_step {α β : Type} (f : α →  β) (x : α) :
  (some f) <*> (some x) = some (f x)
```

## Depends on

Its statements use no other Cedar module's declarations.

## Sources

- [Cedar/Thm/Data/Applicative.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Applicative.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Data.Applicative.json)
