---
catalog: module
lean: Cslib.HasWellFormed
statement: formalized
proof: formalized
---

# HasWellFormed

`Cslib.Foundations.Syntax.HasWellFormed`, in [Cslib/Foundations/Syntax/HasWellFormed.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Syntax/HasWellFormed.lean), by Fabrizio Montesi.

> Notation typeclass for well-formedness.

`Cslib.HasWellFormed` (class, [line 18](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Syntax/HasWellFormed.lean#L18))

> Typeclass for types equipped with a well-formedness predicate.

```lean
class HasWellFormed (α : Type u) where
  /-- Establishes whether `x` is well-formed. -/
  wf (x : α) : Prop
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Syntax/HasWellFormed.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Syntax/HasWellFormed.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.Syntax.HasWellFormed.json)
