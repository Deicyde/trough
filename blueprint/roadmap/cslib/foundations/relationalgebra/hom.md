---
catalog: module
lean: Cslib.RelationAlgebraHom, Cslib.RelationAlgebraEquiv, Cslib.RelationAlgebraHom.Simps.apply, Cslib.RelationAlgebraHom.ext, Cslib.RelationAlgebraHom.mono, Cslib.RelationAlgebraHom.id, Cslib.RelationAlgebraHom.comp, Cslib.RelationAlgebraHom.id_apply, Cslib.RelationAlgebraHom.comp_apply, Cslib.RelationAlgebraHom.isIntegral_of_injective, Cslib.RelationAlgebraEquiv.ext, Cslib.RelationAlgebraEquiv.symm, Cslib.RelationAlgebraEquiv.Simps.apply, Cslib.RelationAlgebraEquiv.Simps.symm_apply, Cslib.RelationAlgebraEquiv.refl, Cslib.RelationAlgebraEquiv.trans, Cslib.RelationAlgebraEquiv.toHom, Cslib.RelationAlgebraEquiv.symm_apply_apply, Cslib.RelationAlgebraEquiv.apply_symm_apply, Cslib.RelationAlgebraEquiv.ofBijective, Cslib.RelationAlgebraEquiv.toHom_bijective, Cslib.RelationAlgebraEquiv.toHom_injective, Cslib.RelationAlgebraEquiv.inj, Cslib.RelationAlgebraEquiv.toHom_surjective, Cslib.RelationAlgebraEquiv.ofHomInv, Cslib.RelationAlgebraEquiv.isAtom_apply_iff, Cslib.RelationAlgebraEquiv.star_apply_eq_iff, Cslib.RelationAlgebraEquiv.apply_le_compl_one_iff, Cslib.RelationAlgebraEquiv.apply_le_one_iff, Cslib.RelationAlgebraEquiv.apply_mem_identityAtoms_iff, Cslib.RelationAlgebraEquiv.apply_mem_symmetricDiversityAtoms_iff, Cslib.RelationAlgebraEquiv.apply_mem_nonsymmetricDiversityAtoms_iff, Cslib.RelationAlgebraEquiv.ncard_identityAtoms, Cslib.RelationAlgebraEquiv.ncard_symmetricDiversityAtoms, Cslib.RelationAlgebraEquiv.ncard_nonsymmetricDiversityAtoms, Cslib.RelationAlgebraEquiv.setRelOfEquiv
statement: formalized
proof: formalized
---

# Morphisms and isomorphisms of relation algebras

`Cslib.Foundations.RelationAlgebra.Hom`, in [Cslib/Foundations/RelationAlgebra/Hom.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean), by Chris Henson.

`Cslib.RelationAlgebraHom` (structure, [line 25](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L25))

> The type of relation algebra homomorphisms from `α` to `β`, preserving both the Boolean algebra
> and composition operations

```lean
structure RelationAlgebraHom (α β : Type*) [RelationAlgebra α] [RelationAlgebra β]
    extends BoundedLatticeHom α β, StarMonoidHom α β
```

`Cslib.RelationAlgebraEquiv` (structure, [line 33](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L33))

> The type of relation algebra equivalence from `α` to `β`, preserving both the Boolean algebra
> and composition operations

```lean
structure RelationAlgebraEquiv (α β : Type*) [RelationAlgebra α] [RelationAlgebra β]
    extends toOrderIso : OrderIso α β, StarMulEquiv α β
```

`Cslib.RelationAlgebraHom.Simps.apply` (definition, [line 60](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L60))

> See Note [custom simps projection].

```lean
def Simps.apply (f : RelationAlgebraHom α β) : α → β
```

`Cslib.RelationAlgebraHom.ext` (theorem, [line 65](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L65))

```lean
theorem ext {f g : RelationAlgebraHom α β} (h : ∀ a, f a = g a) : f = g
```

`Cslib.RelationAlgebraHom.mono` (theorem, [line 68](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L68))

```lean
protected theorem mono (f : RelationAlgebraHom α β) : Monotone f
```

`Cslib.RelationAlgebraHom.id` (definition, [line 71](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L71))

> `id` as a `RelationAlgebraHom`

```lean
protected def id (α : Type*) [RelationAlgebra α] : RelationAlgebraHom α α
```

`Cslib.RelationAlgebraHom.comp` (definition, [line 75](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L75))

> Composition of `RelationAlgebraHom`

```lean
def comp (f : RelationAlgebraHom β γ) (g : RelationAlgebraHom α β) : RelationAlgebraHom α γ
```

`Cslib.RelationAlgebraHom.id_apply` (theorem, [line 80](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L80))

```lean
theorem id_apply (a : α) : RelationAlgebraHom.id α a = a
```

`Cslib.RelationAlgebraHom.comp_apply` (theorem, [line 83](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L83))

```lean
theorem comp_apply (f : RelationAlgebraHom β γ) (g : RelationAlgebraHom α β) (a : α) :
    f.comp g a = f (g a)
```

`Cslib.RelationAlgebraHom.isIntegral_of_injective` (theorem, [line 86](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L86))

```lean
theorem isIntegral_of_injective (f : RelationAlgebraHom α β) (hf : Function.Injective f)
    (h : RelationAlgebra.IsIntegral β) : RelationAlgebra.IsIntegral α
```

`Cslib.RelationAlgebraEquiv.ext` (theorem, [line 117](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L117))

```lean
theorem ext {f g : RelationAlgebraEquiv α β} (h : ∀ a, f a = g a) : f = g
```

`Cslib.RelationAlgebraEquiv.symm` (definition, [line 121](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L121))

> The symmetric `RelationAlgebraEquiv`

```lean
def symm (f : RelationAlgebraEquiv α β) : RelationAlgebraEquiv β α
```

`Cslib.RelationAlgebraEquiv.Simps.apply` (definition, [line 125](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L125))

> See Note [custom simps projection].

```lean
def Simps.apply (e : RelationAlgebraEquiv α β) : α → β
```

`Cslib.RelationAlgebraEquiv.Simps.symm_apply` (definition, [line 128](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L128))

> See Note [custom simps projection].

```lean
def Simps.symm_apply (e : RelationAlgebraEquiv α β) : β → α
```

`Cslib.RelationAlgebraEquiv.refl` (definition, [line 134](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L134))

> The reflexive `RelationAlgebraEquiv`

```lean
protected def refl (α : Type*) [RelationAlgebra α] : RelationAlgebraEquiv α α
```

`Cslib.RelationAlgebraEquiv.trans` (definition, [line 139](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L139))

> The transitive `RelationAlgebraEquiv`

```lean
def trans (f : RelationAlgebraEquiv α β) (g : RelationAlgebraEquiv β γ) :
    RelationAlgebraEquiv α γ
```

`Cslib.RelationAlgebraEquiv.toHom` (definition, [line 146](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L146))

> The `RelationAlgebraHom` underlying an `RelationAlgebraEquiv`

```lean
def toHom (f : RelationAlgebraEquiv α β) : RelationAlgebraHom α β
```

`Cslib.RelationAlgebraEquiv.symm_apply_apply` (theorem, [line 151](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L151))

```lean
theorem symm_apply_apply (f : RelationAlgebraEquiv α β) (a : α) : f.symm (f a) = a
```

`Cslib.RelationAlgebraEquiv.apply_symm_apply` (theorem, [line 155](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L155))

```lean
theorem apply_symm_apply (f : RelationAlgebraEquiv α β) (b : β) : f (f.symm b) = b
```

`Cslib.RelationAlgebraEquiv.ofBijective` (definition, [line 160](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L160))

> Promote a bijective homomorphism to an equivalence.

```lean
noncomputable def ofBijective {f : RelationAlgebraHom α β} (hf : Function.Bijective f) :
    RelationAlgebraEquiv α β
```

`Cslib.RelationAlgebraEquiv.toHom_bijective` (lemma, [line 168](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L168))

```lean
lemma toHom_bijective (e : RelationAlgebraEquiv α β) : Function.Bijective e.toHom
```

`Cslib.RelationAlgebraEquiv.toHom_injective` (lemma, [line 171](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L171))

```lean
lemma toHom_injective (e : RelationAlgebraEquiv α β) : Function.Injective e.toHom
```

`Cslib.RelationAlgebraEquiv.inj` (lemma, [line 174](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L174))

```lean
lemma inj {e : RelationAlgebraEquiv α β} {x y : α} : e x = e y ↔ x = y
```

`Cslib.RelationAlgebraEquiv.toHom_surjective` (lemma, [line 177](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L177))

```lean
lemma toHom_surjective (e : RelationAlgebraEquiv α β) : Function.Surjective e.toHom
```

`Cslib.RelationAlgebraEquiv.ofHomInv` (definition, [line 182](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L182))

> Construct an equivalence from a homomorphism and an inverse.

```lean
def ofHomInv (f : RelationAlgebraHom α β) (g : RelationAlgebraHom β α)
    (hfg : ∀ b : β, f (g b) = b) (hgf : ∀ a : α, g (f a) = a) : RelationAlgebraEquiv α β
```

`Cslib.RelationAlgebraEquiv.isAtom_apply_iff` (theorem, [line 189](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L189))

```lean
theorem isAtom_apply_iff (e : RelationAlgebraEquiv α β) : IsAtom (e a) ↔ IsAtom a
```

`Cslib.RelationAlgebraEquiv.star_apply_eq_iff` (theorem, [line 193](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L193))

```lean
theorem star_apply_eq_iff (e : RelationAlgebraEquiv α β) : star (e a) = e a ↔ star a = a
```

`Cslib.RelationAlgebraEquiv.apply_le_compl_one_iff` (theorem, [line 197](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L197))

```lean
theorem apply_le_compl_one_iff (e : RelationAlgebraEquiv α β) {a : α} : e a ≤ 1ᶜ ↔ a ≤ 1ᶜ
```

`Cslib.RelationAlgebraEquiv.apply_le_one_iff` (theorem, [line 201](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L201))

```lean
theorem apply_le_one_iff (e : RelationAlgebraEquiv α β) {a : α} : e a ≤ 1 ↔ a ≤ 1
```

`Cslib.RelationAlgebraEquiv.apply_mem_identityAtoms_iff` (theorem, [line 207](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L207))

```lean
theorem apply_mem_identityAtoms_iff (e : RelationAlgebraEquiv α β) {a : α} :
    e a ∈ identityAtoms β ↔ a ∈ identityAtoms α
```

`Cslib.RelationAlgebraEquiv.apply_mem_symmetricDiversityAtoms_iff` (theorem, [line 212](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L212))

```lean
theorem apply_mem_symmetricDiversityAtoms_iff (e : RelationAlgebraEquiv α β) {a : α} :
    e a ∈ symmetricDiversityAtoms β ↔ a ∈ symmetricDiversityAtoms α
```

`Cslib.RelationAlgebraEquiv.apply_mem_nonsymmetricDiversityAtoms_iff` (theorem, [line 217](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L217))

```lean
theorem apply_mem_nonsymmetricDiversityAtoms_iff (e : RelationAlgebraEquiv α β) {a : α} :
    e a ∈ nonsymmetricDiversityAtoms β ↔ a ∈ nonsymmetricDiversityAtoms α
```

`Cslib.RelationAlgebraEquiv.ncard_identityAtoms` (theorem, [line 221](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L221))

```lean
theorem ncard_identityAtoms (e : RelationAlgebraEquiv α β) :
    (identityAtoms α).ncard = (identityAtoms β).ncard
```

`Cslib.RelationAlgebraEquiv.ncard_symmetricDiversityAtoms` (theorem, [line 225](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L225))

```lean
theorem ncard_symmetricDiversityAtoms (e : RelationAlgebraEquiv α β) :
    (symmetricDiversityAtoms α).ncard = (symmetricDiversityAtoms β).ncard
```

`Cslib.RelationAlgebraEquiv.ncard_nonsymmetricDiversityAtoms` (theorem, [line 229](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L229))

```lean
theorem ncard_nonsymmetricDiversityAtoms (e : RelationAlgebraEquiv α β) :
    (nonsymmetricDiversityAtoms α).ncard = (nonsymmetricDiversityAtoms β).ncard
```

`Cslib.RelationAlgebraEquiv.setRelOfEquiv` (definition, [line 236](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean#L236))

> An equivalence between types lifts to an equivalence between their algebras of relations.

```lean
def setRelOfEquiv (e : α ≃ β) : RelationAlgebraEquiv (SetRel α α) (SetRel β β)
```

## Depends on

- [Set-based relations](../data/setrel.md)
- [Relation algebras](basic.md)

## Sources

- [Cslib/Foundations/RelationAlgebra/Hom.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Hom.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.RelationAlgebra.Hom.json)
