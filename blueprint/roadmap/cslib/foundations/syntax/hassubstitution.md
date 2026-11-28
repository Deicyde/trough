---
catalog: module
lean: Cslib.HasSubstitution, Cslib.unexpandHasSubstitutionSubst
statement: formalized
proof: formalized
---

# HasSubstitution

`Cslib.Foundations.Syntax.HasSubstitution`, in [Cslib/Foundations/Syntax/HasSubstitution.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Syntax/HasSubstitution.lean), by Fabrizio Montesi.

> Notation typeclass for substitution.

`Cslib.HasSubstitution` (class, [line 18](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Syntax/HasSubstitution.lean#L18))

> Typeclass for substitution relations and access to their notation.

```lean
class HasSubstitution (α : Type u) (β : Type v) (γ : Type w) where
  /-- Substitution function. Replaces `x` in `t` with `t'`. -/
  subst (t : α) (x : β) (t' : γ) : α
```

`Cslib.unexpandHasSubstitutionSubst` (definition, [line 37](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Syntax/HasSubstitution.lean#L37))

> Pretty-printer support for `HasSubstitution.subst`.

```lean
meta def unexpandHasSubstitutionSubst : Lean.PrettyPrinter.Unexpander
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Syntax/HasSubstitution.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Syntax/HasSubstitution.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.Syntax.HasSubstitution.json)
