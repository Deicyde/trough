---
catalog: module
lean: Cslib.HasHContext, Cslib.HasContext, Cslib.HasContext.Context
statement: formalized
proof: formalized
---

# Context

`Cslib.Foundations.Syntax.Context`, in [Cslib/Foundations/Syntax/Context.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Syntax/Context.lean), by Fabrizio Montesi.

> Typeclasses for contexts, with heterogeneous and homogeneous variants.

`Cslib.HasHContext` (class, [line 18](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Syntax/Context.lean#L18))

> Class for types with a canonical notion of heterogeneous single-hole contexts.

```lean
class HasHContext (α β : Type*) where
  /-- The type of contexts. -/
  {Context : Type*}
  /-- Replaces the hole in the context with a value, resulting in a new value. -/
  fill (c : Context) (b : β) : α
```

`Cslib.HasContext` (abbreviation, [line 28](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Syntax/Context.lean#L28))

> Class for types (`α`) that have a canonical notion of homogeneous single-hole contexts
> (`Context`).

```lean
abbrev HasContext (α : Type*)
```

`Cslib.HasContext.Context` (definition, [line 31](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Syntax/Context.lean#L31))

```lean
def HasContext.Context (α : Type*) [HasContext α] : Type*
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Syntax/Context.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Syntax/Context.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.Syntax.Context.json)
