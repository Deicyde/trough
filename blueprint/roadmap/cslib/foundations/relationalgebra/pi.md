---
catalog: module
lean: Cslib.Pi.instRelationAlgebra, Cslib.RelationAlgebraHom.pi, Cslib.RelationAlgebraHom.pi_apply, Cslib.RelationAlgebraHom.eval, Cslib.RelationAlgebraHom.eval_apply, Cslib.RelationAlgebraHom.piEquiv
statement: formalized
proof: formalized
---

# Products of relation algebras

`Cslib.Foundations.RelationAlgebra.Pi`, in [Cslib/Foundations/RelationAlgebra/Pi.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Pi.lean), by Chris Henson.

> This module defines the relation algebra structure over products. This is a key component of
> the representation of a relation algebra.

`Cslib.Pi.instRelationAlgebra` (instance, [line 24](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Pi.lean#L24))

```lean
instance Pi.instRelationAlgebra {ι : Type*} {β : ι → Type*} [∀ i, RelationAlgebra (β i)] :
    RelationAlgebra (∀ i, β i)
```

`Cslib.RelationAlgebraHom.pi` (definition, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Pi.lean#L35))

> The product of `RelationAlgebraHom`s is a `RelationAlgebraHom` into a product.

```lean
def pi (f : ∀ i, RelationAlgebraHom α (β i)) : RelationAlgebraHom α (∀ i, β i)
```

`Cslib.RelationAlgebraHom.pi_apply` (theorem, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Pi.lean#L45))

```lean
theorem pi_apply (f : ∀ i, RelationAlgebraHom α (β i)) (a : α) (i : ι) : pi f a i = f i a
```

`Cslib.RelationAlgebraHom.eval` (definition, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Pi.lean#L50))

> The `RelationAlgebraHom` into a single fiber.

```lean
def eval (i : ι) : RelationAlgebraHom (∀ i, β i) (β i)
```

`Cslib.RelationAlgebraHom.eval_apply` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Pi.lean#L59))

```lean
theorem eval_apply (i : ι) (b : ∀ i, β i) : eval β i b = b i
```

`Cslib.RelationAlgebraHom.piEquiv` (definition, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Pi.lean#L65))

> The equivalence between products of `RelationAlgebraHom` and the `RelationAlgebraHom` into a
> product that is given by composition of `eval`.

```lean
def piEquiv : (∀ i, RelationAlgebraHom α (β i)) ≃ RelationAlgebraHom α (∀ i, β i)
```

## Depends on

- [Morphisms and isomorphisms of relation algebras](hom.md)

## Sources

- [Cslib/Foundations/RelationAlgebra/Pi.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Pi.lean)
