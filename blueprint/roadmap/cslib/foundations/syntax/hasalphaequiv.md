---
catalog: module
lean: Cslib.HasAlphaEquiv
statement: formalized
proof: formalized
---

# HasAlphaEquiv

`Cslib.Foundations.Syntax.HasAlphaEquiv`, in [Cslib/Foundations/Syntax/HasAlphaEquiv.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Syntax/HasAlphaEquiv.lean), by Fabrizio Montesi.

> Notation typeclass for α-equivalence.

`Cslib.HasAlphaEquiv` (class, [line 18](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Syntax/HasAlphaEquiv.lean#L18))

> Typeclass for the α-equivalence notation `x =α y`.

```lean
class HasAlphaEquiv (β : Type u) where
  /-- α-equivalence relation for type β. -/
  AlphaEquiv : β → β → Prop
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Syntax/HasAlphaEquiv.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Syntax/HasAlphaEquiv.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.Syntax.HasAlphaEquiv.json)
