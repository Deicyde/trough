---
catalog: module
lean: Language.RightCongruence, Language.RightCongruence.eqvCls, Language.LeftCongruence, Language.LeftCongruence.eqvCls, Language.Congruence, Language.Congruence.eqvCls
statement: formalized
proof: formalized
---

# Right Congruence

`Cslib.Computability.Languages.Congruences.Basic`, in [Cslib/Computability/Languages/Congruences/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/Basic.lean), by Ching-Tsun Chou.

> This file contains basic definitions about left, right, and (two-sided) congruences
> on finite sequences.

`Language.RightCongruence` (class, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/Basic.lean#L28))

> A right congruence is an equivalence relation on finite sequences (represented by lists)
> that is preserved by concatenation on the right.  The equivalence relation is represented
> by a setoid to to enable ready access to the quotient construction.

```lean
class RightCongruence (α : Type*) extends eq : Setoid (List α) where
  right_cov : CovariantClass _ _ (fun x y => y ++ x) eq
```

`Language.RightCongruence.eqvCls` (abbreviation, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/Basic.lean#L34))

> The equivalence class (as a language) corresponding to an element of the quotient type.

```lean
abbrev eqvCls [c : RightCongruence α] (a : Quotient c.eq) : Language α
```

`Language.LeftCongruence` (class, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/Basic.lean#L42))

> A left congruence is an equivalence relation on finite sequences (represented by lists)
> that is preserved by concatenation on the left.  The equivalence relation is represented
> by a setoid to to enable ready access to the quotient construction.

```lean
class LeftCongruence (α : Type*) extends eq : Setoid (List α) where
  left_cov : CovariantClass _ _ (fun x y => x ++ y) eq
```

`Language.LeftCongruence.eqvCls` (abbreviation, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/Basic.lean#L48))

> The equivalence class (as a language) corresponding to an element of the quotient type.

```lean
abbrev eqvCls [c : LeftCongruence α] (a : Quotient c.eq) : Language α
```

`Language.Congruence` (class, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/Basic.lean#L55))

> A (two-sided) congruence is an equivalence relation on finite sequences (represented by lists)
> that is both a left-congruence and a right-congruence.

```lean
class Congruence (α : Type*) extends LeftCongruence α, RightCongruence α where
```

`Language.Congruence.eqvCls` (abbreviation, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/Basic.lean#L60))

> The equivalence class (as a language) corresponding to an element of the quotient type.

```lean
abbrev eqvCls [c : Congruence α] (a : Quotient c.eq) : Language α
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Computability/Languages/Congruences/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/Basic.lean)
