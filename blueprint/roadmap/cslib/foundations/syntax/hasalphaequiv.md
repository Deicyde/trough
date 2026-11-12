---
catalog: module
lean: Cslib.HasAlphaEquiv
statement: formalized
proof: formalized
---

# HasAlphaEquiv

`Cslib.Foundations.Syntax.HasAlphaEquiv`, in [Cslib/Foundations/Syntax/HasAlphaEquiv.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Syntax/HasAlphaEquiv.lean), by Fabrizio Montesi.

> Notation typeclass for α-equivalence.

`Cslib.HasAlphaEquiv` (class, [line 18](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Syntax/HasAlphaEquiv.lean#L18))

> Typeclass for the α-equivalence notation `x =α y`.

```lean
class HasAlphaEquiv (β : Type u) where
  /-- α-equivalence relation for type β. -/
  AlphaEquiv : β → β → Prop
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Syntax/HasAlphaEquiv.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Syntax/HasAlphaEquiv.lean)
