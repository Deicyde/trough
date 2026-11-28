---
catalog: module
lean: Set.Iic.instRelationAlgebra, Cslib.RelationAlgebraHom.restrictIic, Cslib.RelationAlgebraEquiv.restrictIic
statement: formalized
proof: formalized
---

# Relativization of a relation algebra

`Cslib.Foundations.RelationAlgebra.Relativization`, in [Cslib/Foundations/RelationAlgebra/Relativization.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Relativization.lean), by Thomas Waring.

> This file provides a relation algebra instance on `Set.Iic a`, for `a : α` a symmetric and
> transitive element of a relation algebra.
>
> ## References
>
> - [S. Givant, *Introduction to Relation Algebras: Relation Algebras, Volume 1*][Givant2017a],
> chapter 10.

`Set.Iic.instRelationAlgebra` (instance, [line 40](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Relativization.lean#L40))

> The **Relativization** of a relation algebra to a symmetric and transitive element `a`.

```lean
instance _root_.Set.Iic.instRelationAlgebra (a : α) [IsRelSymm a] [IsRelTrans a] :
    RelationAlgebra (Set.Iic a)
```

`Cslib.RelationAlgebraHom.restrictIic` (definition, [line 62](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Relativization.lean#L62))

> A homomorphism from `α` to `β` restricts to the relativization. If `b` is reducibly equal to
> `f a`, then `f.restrictIic (refl a)` can find the required instances on `b` by synthesis.

```lean
def RelationAlgebraHom.restrictIic (f : RelationAlgebraHom α β) {a : α} [IsRelSymm a]
    [IsRelTrans a] {b : β} [IsRelSymm b] [IsRelTrans b] (h : f a = b) :
    RelationAlgebraHom (Iic a) (Iic b)
```

`Cslib.RelationAlgebraEquiv.restrictIic` (definition, [line 77](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Relativization.lean#L77))

> An equivalence between `α` and `β` restricts to the relativization. If `b` is reducibly equal to
> `f a`, then `e.restrictIic (refl a)` can find the required instances on `b` by synthesis.

```lean
def RelationAlgebraEquiv.restrictIic (e : RelationAlgebraEquiv α β) {a : α} [IsRelSymm a]
    [IsRelTrans a] {b : β} [IsRelSymm b] [IsRelTrans b] (h : e a = b) :
    RelationAlgebraEquiv (Iic a) (Iic b)
```

## Depends on

- [Morphisms and isomorphisms of relation algebras](hom.md)
- [Element properties for relation algebras](specialelements.md)

## Proof depends on

- [Algebra instances on intervals](../order/algebraintervals.md)

## Sources

- [Cslib/Foundations/RelationAlgebra/Relativization.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Relativization.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.RelationAlgebra.Relativization.json)
