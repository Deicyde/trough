---
catalog: module
lean: Option.mapD, Option.mapD_some, Option.mapD_none
statement: formalized
proof: formalized
---

# Additional Option functions and lemmas

`Cedar.Thm.Data.Option`, in [Cedar/Thm/Data/Option.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Option.lean).

`Option.mapD` (definition, [line 25](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Option.lean#L25))

```lean
public def mapD {α β} (f : α → β) (default : β) : Option α → β
```

`Option.mapD_some` (theorem, [line 30](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Option.lean#L30))

```lean
public theorem mapD_some {α β} (f : α → β) (default : β) (a : α) :
  (Option.some a).mapD f default = f a
```

`Option.mapD_none` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Option.lean#L35))

```lean
public theorem mapD_none {α β} (f : α → β) (default : β) :
  Option.none.mapD f default = default
```

## Depends on

Its statements use no other Cedar module's declarations.

## Sources

- [Cedar/Thm/Data/Option.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/Option.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Data.Option.json)
