---
catalog: module
lean: Cslib.HasWellFormed
statement: formalized
proof: formalized
---

# HasWellFormed

`Cslib.Foundations.Syntax.HasWellFormed`, in [Cslib/Foundations/Syntax/HasWellFormed.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Syntax/HasWellFormed.lean), by Fabrizio Montesi.

> Notation typeclass for well-formedness.

`Cslib.HasWellFormed` (class, [line 18](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Syntax/HasWellFormed.lean#L18))

> Typeclass for types equipped with a well-formedness predicate.

```lean
class HasWellFormed (α : Type u) where
  /-- Establishes whether `x` is well-formed. -/
  wf (x : α) : Prop
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Syntax/HasWellFormed.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Syntax/HasWellFormed.lean)
