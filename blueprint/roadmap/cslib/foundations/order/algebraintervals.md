---
catalog: module
lean: Set.Iic.instCoheytingAlgebra, Set.Ici.instHeytingAlgebra, Set.Iic.instBooleanAlgebra
statement: formalized
proof: formalized
---

# Algebra instances on intervals

`Cslib.Foundations.Order.AlgebraIntervals`, in [Cslib/Foundations/Order/AlgebraIntervals.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Order/AlgebraIntervals.lean), by Thomas Waring.

> This file defines `SDiff (Set.Iic a)` and `HImp (Set.Ici a)` for an element `a : α` in,
> respectively, a co-Heyting or Heyting algebra. In the case that `α` is a (generalized) Boolean
> algebra, this makes `Set.Iic a` a Boolean algebra.
>
> Note that further instances of this sort can be defined, but the `SDiff` and `HImp` operations
> cease to commute with the coercions. As it stands, only the instances necessary for downstream use
> are defined.

`Set.Iic.instCoheytingAlgebra` (instance, [line 29](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Order/AlgebraIntervals.lean#L29))

```lean
instance Set.Iic.instCoheytingAlgebra [GeneralizedCoheytingAlgebra α] {a : α} :
    CoheytingAlgebra (Set.Iic a)
```

`Set.Ici.instHeytingAlgebra` (instance, [line 37](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Order/AlgebraIntervals.lean#L37))

```lean
instance Set.Ici.instHeytingAlgebra [GeneralizedHeytingAlgebra α] {a : α} :
    HeytingAlgebra (Set.Ici a)
```

`Set.Iic.instBooleanAlgebra` (instance, [line 45](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Order/AlgebraIntervals.lean#L45))

```lean
instance Set.Iic.instBooleanAlgebra [GeneralizedBooleanAlgebra α] {a : α} :
    BooleanAlgebra (Set.Iic a)
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Order/AlgebraIntervals.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Order/AlgebraIntervals.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.Order.AlgebraIntervals.json)
