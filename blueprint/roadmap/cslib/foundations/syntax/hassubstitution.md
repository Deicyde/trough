---
catalog: module
lean: Cslib.HasSubstitution, Cslib.unexpandHasSubstitutionSubst
statement: formalized
proof: formalized
---

# HasSubstitution

`Cslib.Foundations.Syntax.HasSubstitution`, in [Cslib/Foundations/Syntax/HasSubstitution.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Syntax/HasSubstitution.lean), by Fabrizio Montesi.

> Notation typeclass for substitution.

`Cslib.HasSubstitution` (class, [line 18](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Syntax/HasSubstitution.lean#L18))

> Typeclass for substitution relations and access to their notation.

```lean
class HasSubstitution (α : Type u) (β : Type v) (γ : Type w) where
  /-- Substitution function. Replaces `x` in `t` with `t'`. -/
  subst (t : α) (x : β) (t' : γ) : α
```

`Cslib.unexpandHasSubstitutionSubst` (definition, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Syntax/HasSubstitution.lean#L37))

> Pretty-printer support for `HasSubstitution.subst`.

```lean
meta def unexpandHasSubstitutionSubst : Lean.PrettyPrinter.Unexpander
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Syntax/HasSubstitution.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Syntax/HasSubstitution.lean)
