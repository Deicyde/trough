---
catalog: module
lean: Cslib.RelationAlgebra.SquareRelations, Cslib.RelationAlgebra.Representation, Cslib.RelationAlgebra.Representable
statement: formalized
proof: formalized
---

# Representable relation algebras

`Cslib.Foundations.RelationAlgebra.Representation`, in [Cslib/Foundations/RelationAlgebra/Representation.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Representation.lean), by Chris Henson.

> One of the primary notions of interest in the study of relation algebras is the notion of
> *representation* by a relation algebra of concrete relations.
>
> Recall Stone's representation for Boolean algebras which (at a low level of
> generality) states that every Boolean algebra has an isomorphism into a particuliar "field of sets".
> Tarski's hope was that an analogous property would hold for abstract relation algebras, with the
> isomorphism desired being into a relation algebra of concrete relations. This turns out to be false,
> with the clasification and conditions for the representation of a relation algebra thus being a
> matter of much interest.

`Cslib.RelationAlgebra.SquareRelations` (definition, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Representation.lean#L35))

> Relations over a type `α`. This definition exists because we need to prevent some instances from
> from Mathlib being included.

```lean
def SquareRelations (α : Type u) : Type u
```

`Cslib.RelationAlgebra.Representation` (structure, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Representation.lean#L67))

> A representation of a relation algebra is an injective morphism into a product of relations.

```lean
structure Representation (α : Type u) [RelationAlgebra α] (ι : Type v) (β : ι → Type w) where
  /-- A `RelationAlgebraHom` into a product of relations. -/
  hom : RelationAlgebraHom α (∀ i, SquareRelations (β i))
  injective : Function.Injective hom
```

`Cslib.RelationAlgebra.Representable` (definition, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Representation.lean#L73))

> A relation algebra is representable if a `Representation` exists.

```lean
def Representable (α : Type u) [RelationAlgebra α] : Prop
```

## Depends on

- [Products of relation algebras](pi.md)

## Sources

- [Cslib/Foundations/RelationAlgebra/Representation.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Representation.lean)
