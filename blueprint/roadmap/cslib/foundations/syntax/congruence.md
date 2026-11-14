---
catalog: module
lean: Cslib.Congruence, Cslib.Congruence.r, Cslib.DefaultCongruence, Cslib.DefaultCongruence.r, Cslib.LawfulCongruence
statement: formalized
proof: formalized
---

# Congruence

`Cslib.Foundations.Syntax.Congruence`, in [Cslib/Foundations/Syntax/Congruence.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Syntax/Congruence.lean), by Fabrizio Montesi.

> Typeclass for congruence over a context.

`Cslib.Congruence` (class, [line 23](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Syntax/Congruence.lean#L23))

> The relation `r` is a congruence on `α`. This class gives access to the `≡[r]` notation.
> To instantiate a canonical congruence for `α`, see `HasCongruence`.
>
> Congruence relations should also instantiate `LawfulCongruence` to prove that the relation respects
> the expected congruence laws.

```lean
class Congruence (r : α → α → Prop)
```

`Cslib.Congruence.r` (abbreviation, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Syntax/Congruence.lean#L27))

> `a ≡[r] b` means that the `a` and `b` are related by the congruence `r`.

```lean
abbrev Congruence.r (r : α → α → Prop) [Congruence r]
```

`Cslib.DefaultCongruence` (class, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Syntax/Congruence.lean#L33))

> The type `α` has a canonical congruence relation. This gives access to the `≡` notation.

```lean
class DefaultCongruence (α : Type*) (r : outParam (α → α → Prop))
```

`Cslib.DefaultCongruence.r` (abbreviation, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Syntax/Congruence.lean#L38))

> `a ≡ b` means that `a` and `b` are related by the canonical congruence relation for their
> type.

```lean
abbrev DefaultCongruence.r {α : Type*} {r : α → α → Prop} [DefaultCongruence α r] (a b : α)
```

`Cslib.LawfulCongruence` (class, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Syntax/Congruence.lean#L47))

> An equivalence relation on `α` preserved by all contexts.

```lean
class LawfulCongruence (r : α → α → Prop) [Congruence r] [HasContext α] extends
  IsEquiv α r, covariant : CovariantClass (HasContext.Context α) α (·<[·]) r
```

## Depends on

- [Context](context.md)

## Sources

- [Cslib/Foundations/Syntax/Congruence.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Syntax/Congruence.lean)
