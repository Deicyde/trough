---
catalog: module
lean: Cslib.RelationAlgebraHom, Cslib.RelationAlgebraEquiv, Cslib.RelationAlgebraHom.ext, Cslib.RelationAlgebraHom.id, Cslib.RelationAlgebraHom.comp, Cslib.RelationAlgebraHom.id_apply, Cslib.RelationAlgebraHom.comp_apply, Cslib.RelationAlgebraHom.isIntegral_of_injective, Cslib.RelationAlgebraEquiv.ext, Cslib.RelationAlgebraEquiv.refl, Cslib.RelationAlgebraEquiv.symm, Cslib.RelationAlgebraEquiv.trans, Cslib.RelationAlgebraEquiv.toHom, Cslib.RelationAlgebraEquiv.refl_apply, Cslib.RelationAlgebraEquiv.trans_apply, Cslib.RelationAlgebraEquiv.toHom_apply, Cslib.RelationAlgebraEquiv.symm_apply_apply, Cslib.RelationAlgebraEquiv.apply_symm_apply
statement: formalized
proof: formalized
---

# Morphisms and isomorphisms of relation algebras

`Cslib.Foundations.RelationAlgebra.Hom`, in [Cslib/Foundations/RelationAlgebra/Hom.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean), by Chris Henson.

`Cslib.RelationAlgebraHom` (structure, [line 24](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean#L24))

> The type of relation algebra homomorphisms from `α` to `β`, preserving both the Boolean algebra
> and composition operations

```lean
structure RelationAlgebraHom (α β : Type*) [RelationAlgebra α] [RelationAlgebra β]
    extends BoundedLatticeHom α β, StarMonoidHom α β
```

`Cslib.RelationAlgebraEquiv` (structure, [line 32](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean#L32))

> The type of relation algebra equivalence from `α` to `β`, preserving both the Boolean algebra
> and composition operations

```lean
structure RelationAlgebraEquiv (α β : Type*) [RelationAlgebra α] [RelationAlgebra β]
    extends toOrderIso : OrderIso α β, StarMulEquiv α β
```

`Cslib.RelationAlgebraHom.ext` (theorem, [line 59](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean#L59))

```lean
theorem ext {f g : RelationAlgebraHom α β} (h : ∀ a, f a = g a) : f = g
```

`Cslib.RelationAlgebraHom.id` (definition, [line 63](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean#L63))

> `id` as a `RelationAlgebraHom`

```lean
protected def id (α : Type*) [RelationAlgebra α] : RelationAlgebraHom α α
```

`Cslib.RelationAlgebraHom.comp` (definition, [line 67](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean#L67))

> Composition of `RelationAlgebraHom`

```lean
def comp (f : RelationAlgebraHom β γ) (g : RelationAlgebraHom α β) : RelationAlgebraHom α γ
```

`Cslib.RelationAlgebraHom.id_apply` (theorem, [line 72](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean#L72))

```lean
theorem id_apply (a : α) : RelationAlgebraHom.id α a = a
```

`Cslib.RelationAlgebraHom.comp_apply` (theorem, [line 75](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean#L75))

```lean
theorem comp_apply (f : RelationAlgebraHom β γ) (g : RelationAlgebraHom α β) (a : α) :
    f.comp g a = f (g a)
```

`Cslib.RelationAlgebraHom.isIntegral_of_injective` (theorem, [line 78](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean#L78))

```lean
theorem isIntegral_of_injective (f : RelationAlgebraHom α β) (hf : Function.Injective f)
    (h : RelationAlgebra.IsIntegral β) : RelationAlgebra.IsIntegral α
```

`Cslib.RelationAlgebraEquiv.ext` (theorem, [line 109](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean#L109))

```lean
theorem ext {f g : RelationAlgebraEquiv α β} (h : ∀ a, f a = g a) : f = g
```

`Cslib.RelationAlgebraEquiv.refl` (definition, [line 113](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean#L113))

> The reflexive `RelationAlgebraEquiv`

```lean
protected def refl (α : Type*) [RelationAlgebra α] : RelationAlgebraEquiv α α
```

`Cslib.RelationAlgebraEquiv.symm` (definition, [line 117](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean#L117))

> The symmetric `RelationAlgebraEquiv`

```lean
def symm (f : RelationAlgebraEquiv α β) : RelationAlgebraEquiv β α
```

`Cslib.RelationAlgebraEquiv.trans` (definition, [line 121](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean#L121))

> The transitive `RelationAlgebraEquiv`

```lean
def trans (f : RelationAlgebraEquiv α β) (g : RelationAlgebraEquiv β γ) :
    RelationAlgebraEquiv α γ
```

`Cslib.RelationAlgebraEquiv.toHom` (definition, [line 126](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean#L126))

> The `RelationAlgebraHom` underlying an `RelationAlgebraEquiv`

```lean
def toHom (f : RelationAlgebraEquiv α β) : RelationAlgebraHom α β
```

`Cslib.RelationAlgebraEquiv.refl_apply` (theorem, [line 130](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean#L130))

```lean
theorem refl_apply (a : α) : RelationAlgebraEquiv.refl α a = a
```

`Cslib.RelationAlgebraEquiv.trans_apply` (theorem, [line 133](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean#L133))

```lean
theorem trans_apply (f : RelationAlgebraEquiv α β) (g : RelationAlgebraEquiv β γ) (a : α) :
    f.trans g a = g (f a)
```

`Cslib.RelationAlgebraEquiv.toHom_apply` (theorem, [line 137](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean#L137))

```lean
theorem toHom_apply (f : RelationAlgebraEquiv α β) (a : α) : f.toHom a = f a
```

`Cslib.RelationAlgebraEquiv.symm_apply_apply` (theorem, [line 140](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean#L140))

```lean
theorem symm_apply_apply (f : RelationAlgebraEquiv α β) (a : α) : f.symm (f a) = a
```

`Cslib.RelationAlgebraEquiv.apply_symm_apply` (theorem, [line 144](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean#L144))

```lean
theorem apply_symm_apply (f : RelationAlgebraEquiv α β) (b : β) : f (f.symm b) = b
```

## Depends on

- [Relation algebras](basic.md)

## Sources

- [Cslib/Foundations/RelationAlgebra/Hom.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/RelationAlgebra/Hom.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.RelationAlgebra.Hom.json)
