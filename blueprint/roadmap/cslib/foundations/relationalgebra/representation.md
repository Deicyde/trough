---
catalog: module
lean: SetRel.mul_eq_comp, SetRel.one_eq_id, SetRel.star_eq_inv, SetRel.mem_mul, SetRel.mem_one, SetRel.mem_star, Cslib.RelationAlgebra.Representation, Cslib.RelationAlgebra.Representable, Cslib.RelationAlgebra.Representable.of_injective
statement: formalized
proof: formalized
---

# Representable relation algebras

`Cslib.Foundations.RelationAlgebra.Representation`, in [Cslib/Foundations/RelationAlgebra/Representation.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Representation.lean), by Chris Henson.

> One of the primary notions of interest in the study of relation algebras is the notion of
> *representation* by a relation algebra of concrete relations.
>
> Recall Stone's representation for Boolean algebras which (at a low level of
> generality) states that every Boolean algebra has an isomorphism into a particular "field of sets".
> Tarski's hope was that an analogous property would hold for abstract relation algebras, with the
> isomorphism desired being into a relation algebra of concrete relations. This turns out to be false,
> with the classification and conditions for the representation of a relation algebra thus being a
> matter of much interest.

`SetRel.mul_eq_comp` (theorem, [line 54](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Representation.lean#L54))

```lean
theorem _root_.SetRel.mul_eq_comp : R * S = R.comp S
```

`SetRel.one_eq_id` (theorem, [line 56](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Representation.lean#L56))

```lean
theorem _root_.SetRel.one_eq_id : (1 : SetRel α α) = SetRel.id
```

`SetRel.star_eq_inv` (theorem, [line 58](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Representation.lean#L58))

```lean
theorem _root_.SetRel.star_eq_inv : star R = R.inv
```

`SetRel.mem_mul` (theorem, [line 61](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Representation.lean#L61))

```lean
theorem _root_.SetRel.mem_mul : (a, c) ∈ R * S ↔ ∃ b, (a, b) ∈ R ∧ (b, c) ∈ S
```

`SetRel.mem_one` (theorem, [line 64](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Representation.lean#L64))

```lean
theorem _root_.SetRel.mem_one : (a, b) ∈ (1 : SetRel α α) ↔ a = b
```

`SetRel.mem_star` (theorem, [line 67](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Representation.lean#L67))

```lean
theorem _root_.SetRel.mem_star : (a, b) ∈ star R ↔ (b, a) ∈ R
```

`Cslib.RelationAlgebra.Representation` (structure, [line 70](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Representation.lean#L70))

> A representation of a relation algebra is an injective morphism into a product of relations.

```lean
structure Representation (α : Type u) [RelationAlgebra α] (ι : Type v) (β : ι → Type w) where
  /-- A `RelationAlgebraHom` into a product of relations. -/
  hom : RelationAlgebraHom α (∀ i, SetRel (β i) (β i))
  injective : Function.Injective hom
```

`Cslib.RelationAlgebra.Representable` (definition, [line 76](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Representation.lean#L76))

> A relation algebra is representable if a `Representation` exists.

```lean
def Representable (α : Type u) [RelationAlgebra α] : Prop
```

`Cslib.RelationAlgebra.Representable.of_injective` (theorem, [line 80](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Representation.lean#L80))

> A relation algebra that embeds into a representable relation algebra is representable.

```lean
theorem Representable.of_injective {α α' : Type u} [RelationAlgebra α] [RelationAlgebra α']
    (f : RelationAlgebraHom α α') (hf : Function.Injective f) (h : Representable α') :
    Representable α
```

## Depends on

- [Products of relation algebras](pi.md)

## Sources

- [Cslib/Foundations/RelationAlgebra/Representation.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Representation.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.RelationAlgebra.Representation.json)
