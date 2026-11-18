---
catalog: module
lean: Cslib.RelationAlgebraHom, Cslib.RelationAlgebraEquiv, Cslib.RelationAlgebraHom.ext, Cslib.RelationAlgebraHom.id, Cslib.RelationAlgebraHom.comp, Cslib.RelationAlgebraHom.id_apply, Cslib.RelationAlgebraHom.comp_apply, Cslib.RelationAlgebraEquiv.ext, Cslib.RelationAlgebraEquiv.refl, Cslib.RelationAlgebraEquiv.symm, Cslib.RelationAlgebraEquiv.trans, Cslib.RelationAlgebraEquiv.toHom, Cslib.RelationAlgebraEquiv.refl_apply, Cslib.RelationAlgebraEquiv.trans_apply, Cslib.RelationAlgebraEquiv.toHom_apply, Cslib.RelationAlgebraEquiv.symm_apply_apply, Cslib.RelationAlgebraEquiv.apply_symm_apply
statement: formalized
proof: formalized
---

# Morphisms and isomorphisms of relation algebras

`Cslib.Foundations.RelationAlgebra.Hom`, in [Cslib/Foundations/RelationAlgebra/Hom.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Hom.lean), by Chris Henson.

`Cslib.RelationAlgebraHom` (structure, [line 24](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Hom.lean#L24))

> The type of relation algebra homomorphisms from `α` to `β`, preserving both the Boolean algebra
> and composition operations

```lean
structure RelationAlgebraHom (α β : Type*) [RelationAlgebra α] [RelationAlgebra β]
    extends BoundedLatticeHom α β, StarMonoidHom α β
```

`Cslib.RelationAlgebraEquiv` (structure, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Hom.lean#L32))

> The type of relation algebra equivalence from `α` to `β`, preserving both the Boolean algebra
> and composition operations

```lean
structure RelationAlgebraEquiv (α β : Type*) [RelationAlgebra α] [RelationAlgebra β]
    extends toOrderIso : OrderIso α β, StarMulEquiv α β
```

`Cslib.RelationAlgebraHom.ext` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Hom.lean#L59))

```lean
theorem ext {f g : RelationAlgebraHom α β} (h : ∀ a, f a = g a) : f = g
```

`Cslib.RelationAlgebraHom.id` (definition, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Hom.lean#L63))

> `id` as a `RelationAlgebraHom`

```lean
protected def id (α : Type*) [RelationAlgebra α] : RelationAlgebraHom α α
```

`Cslib.RelationAlgebraHom.comp` (definition, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Hom.lean#L67))

> Composition of `RelationAlgebraHom`

```lean
def comp (f : RelationAlgebraHom β γ) (g : RelationAlgebraHom α β) : RelationAlgebraHom α γ
```

`Cslib.RelationAlgebraHom.id_apply` (theorem, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Hom.lean#L72))

```lean
theorem id_apply (a : α) : RelationAlgebraHom.id α a = a
```

`Cslib.RelationAlgebraHom.comp_apply` (theorem, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Hom.lean#L75))

```lean
theorem comp_apply (f : RelationAlgebraHom β γ) (g : RelationAlgebraHom α β) (a : α) :
    f.comp g a = f (g a)
```

`Cslib.RelationAlgebraEquiv.ext` (theorem, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Hom.lean#L101))

```lean
theorem ext {f g : RelationAlgebraEquiv α β} (h : ∀ a, f a = g a) : f = g
```

`Cslib.RelationAlgebraEquiv.refl` (definition, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Hom.lean#L105))

> The reflexive `RelationAlgebraEquiv`

```lean
protected def refl (α : Type*) [RelationAlgebra α] : RelationAlgebraEquiv α α
```

`Cslib.RelationAlgebraEquiv.symm` (definition, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Hom.lean#L109))

> The symmetric `RelationAlgebraEquiv`

```lean
def symm (f : RelationAlgebraEquiv α β) : RelationAlgebraEquiv β α
```

`Cslib.RelationAlgebraEquiv.trans` (definition, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Hom.lean#L113))

> The transitive `RelationAlgebraEquiv`

```lean
def trans (f : RelationAlgebraEquiv α β) (g : RelationAlgebraEquiv β γ) :
    RelationAlgebraEquiv α γ
```

`Cslib.RelationAlgebraEquiv.toHom` (definition, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Hom.lean#L118))

> The `RelationAlgebraHom` underlying an `RelationAlgebraEquiv`

```lean
def toHom (f : RelationAlgebraEquiv α β) : RelationAlgebraHom α β
```

`Cslib.RelationAlgebraEquiv.refl_apply` (theorem, [line 122](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Hom.lean#L122))

```lean
theorem refl_apply (a : α) : RelationAlgebraEquiv.refl α a = a
```

`Cslib.RelationAlgebraEquiv.trans_apply` (theorem, [line 125](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Hom.lean#L125))

```lean
theorem trans_apply (f : RelationAlgebraEquiv α β) (g : RelationAlgebraEquiv β γ) (a : α) :
    f.trans g a = g (f a)
```

`Cslib.RelationAlgebraEquiv.toHom_apply` (theorem, [line 129](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Hom.lean#L129))

```lean
theorem toHom_apply (f : RelationAlgebraEquiv α β) (a : α) : f.toHom a = f a
```

`Cslib.RelationAlgebraEquiv.symm_apply_apply` (theorem, [line 132](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Hom.lean#L132))

```lean
theorem symm_apply_apply (f : RelationAlgebraEquiv α β) (a : α) : f.symm (f a) = a
```

`Cslib.RelationAlgebraEquiv.apply_symm_apply` (theorem, [line 136](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Hom.lean#L136))

```lean
theorem apply_symm_apply (f : RelationAlgebraEquiv α β) (b : β) : f (f.symm b) = b
```

## Depends on

- [Relation algebras](basic.md)

## Sources

- [Cslib/Foundations/RelationAlgebra/Hom.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/RelationAlgebra/Hom.lean)
