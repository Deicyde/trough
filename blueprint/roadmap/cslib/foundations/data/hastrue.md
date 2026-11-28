---
catalog: module
lean: Cslib.HasTrue, Cslib.HasTrue.true_bool, Cslib.HasTrue.true_prop, Cslib.HasTrue.true_ulift
statement: formalized
proof: formalized
---

# Types with a designated true value

`Cslib.Foundations.Data.HasTrue`, in [Cslib/Foundations/Data/HasTrue.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/HasTrue.lean), by Fabrizio Montesi.

> `HasTrue α` designates a value of `α` as true.

`Cslib.HasTrue` (class, [line 23](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/HasTrue.lean#L23))

> A type with a designated true value.

```lean
class HasTrue (α : Type u) where
  /-- The designated true value. -/
  true : α
```

`Cslib.HasTrue.true_bool` (theorem, [line 36](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/HasTrue.lean#L36))

```lean
theorem true_bool : (HasTrue.true : Bool) = Bool.true
```

`Cslib.HasTrue.true_prop` (theorem, [line 39](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/HasTrue.lean#L39))

```lean
theorem true_prop : (HasTrue.true : Prop) = True
```

`Cslib.HasTrue.true_ulift` (theorem, [line 42](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/HasTrue.lean#L42))

```lean
theorem true_ulift {α : Type u} [HasTrue α] :
    (HasTrue.true : ULift.{v} α) = .up HasTrue.true
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Data/HasTrue.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Data/HasTrue.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.Data.HasTrue.json)
