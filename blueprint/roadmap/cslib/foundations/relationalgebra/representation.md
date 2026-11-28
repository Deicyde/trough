---
catalog: module
lean: Cslib.RelationAlgebra.Representation, Cslib.RelationAlgebra.Representable, Cslib.RelationAlgebra.Representation.compInjective, Cslib.RelationAlgebra.Representation.compEquiv, Cslib.RelationAlgebra.Representable.of_injective, Cslib.RelationAlgebra.Representable.of_equiv, Cslib.RelationAlgebraEquiv.representable_iff
statement: formalized
proof: formalized
---

# Representable relation algebras

`Cslib.Foundations.RelationAlgebra.Representation`, in [Cslib/Foundations/RelationAlgebra/Representation.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Representation.lean), by Chris Henson.

> One of the primary notions of interest in the study of relation algebras is the notion of
> *representation* by a relation algebra of concrete relations.
>
> Recall Stone's representation for Boolean algebras which (at a low level of
> generality) states that every Boolean algebra has an isomorphism into a particular "field of sets".
> Tarski's hope was that an analogous property would hold for abstract relation algebras, with the
> isomorphism desired being into a relation algebra of concrete relations. This turns out to be false,
> with the classification and conditions for the representation of a relation algebra thus being a
> matter of much interest.

`Cslib.RelationAlgebra.Representation` (structure, [line 37](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Representation.lean#L37))

> A representation of a relation algebra is an injective morphism into a product of relations.

```lean
structure Representation where
  /-- A `RelationAlgebraHom` into a product of relations. -/
  hom : RelationAlgebraHom α (∀ i, SetRel (β i) (β i))
  injective : Function.Injective hom
```

`Cslib.RelationAlgebra.Representable` (definition, [line 44](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Representation.lean#L44))

> A relation algebra is representable if a `Representation` exists.

```lean
def Representable : Prop
```

`Cslib.RelationAlgebra.Representation.compInjective` (definition, [line 47](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Representation.lean#L47))

> Representations can be precomposed with injective homomorphisms.

```lean
def Representation.compInjective (r : Representation α₂ ι β) (f : RelationAlgebraHom α₁ α₂)
    (hf : Function.Injective f) : Representation α₁ ι β
```

`Cslib.RelationAlgebra.Representation.compEquiv` (definition, [line 53](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Representation.lean#L53))

> Representations can be precomposed with equivalences.

```lean
def Representation.compEquiv (r : Representation α₂ ι β) (e : RelationAlgebraEquiv α₁ α₂) :
    Representation α₁ ι β
```

`Cslib.RelationAlgebra.Representable.of_injective` (theorem, [line 57](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Representation.lean#L57))

> A relation algebra that embeds into a representable relation algebra is representable.

```lean
theorem Representable.of_injective (f : RelationAlgebraHom α α₁) (hf : Function.Injective f)
    (h : Representable α₁) : Representable α
```

`Cslib.RelationAlgebra.Representable.of_equiv` (theorem, [line 63](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Representation.lean#L63))

> Representability is preserved by equivalence.

```lean
theorem Representable.of_equiv (e : RelationAlgebraEquiv α α₁) (h : Representable α₁) :
    Representable α
```

`Cslib.RelationAlgebraEquiv.representable_iff` (theorem, [line 67](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Representation.lean#L67))

```lean
theorem _root_.Cslib.RelationAlgebraEquiv.representable_iff (e : RelationAlgebraEquiv α α₁) :
    Representable α ↔ Representable α₁
```

## Depends on

- [Products of relation algebras](pi.md)

## Sources

- [Cslib/Foundations/RelationAlgebra/Representation.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Representation.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.RelationAlgebra.Representation.json)
