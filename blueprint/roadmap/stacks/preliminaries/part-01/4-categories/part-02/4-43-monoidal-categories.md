---
declaration: section
origin: cited
lean: CategoryTheory.AssociativityConstraint.unitEquivUnitPair, CategoryTheory.AssociativityConstraint.UnitPair.assoc_hom_comp_tensorMap_iso_id, CategoryTheory.AssociativityConstraint.UnitPair.eq_iso_inv_comp_tensorMap_comp_iso, CategoryTheory.AssociativityConstraint.UnitPair.comp_comm, CategoryTheory.AssociativityConstraint.UnitPair.endCommMonoid, CategoryTheory.AssociativityConstraint.UnitPair.existsUnique_iso, CategoryTheory.AssociativityConstraint.UnitPair.r_self_eq_iso, CategoryTheory.AssociativityConstraint.UnitPair.l_self_eq_iso
statement: formalized
proof: formalized
---

# 4.43 Monoidal categories

Section 4.43 of the Stacks Project, [Tag 0FFJ](https://stacks.math.columbia.edu/tag/0FFJ). 14 tags here are carried by 34 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0HAW, a lemma

[Tag 0HAW](https://stacks.math.columbia.edu/tag/0HAW) in the Stacks Project.

**`CategoryTheory.AssociativityConstraint.unitEquivUnitPair`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/UnitOfAssociativityConstraint.lean, line 343](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/UnitOfAssociativityConstraint.lean#L343). The attribute's comment: “the correspondence sends `(𝟏, l, r)` to `(𝟏, r_𝟏)`; its inverse sends `(𝟏, 1)` to the unit with `id_𝟏 ⊗ l_X = (1 ⊗ id_X) ∘ φ` and `r_X ⊗ id_𝟏 = (id_X ⊗ 1) ∘ φ⁻¹`”.

> **Stacks 0HAW.** For a category `C` with a functor `⊗ = T : C × C ⥤ C` and an associativity
> constraint `φ`, units `(𝟏, l, r)` correspond one-to-one to pairs `(𝟏, 1)` where
> `1 : 𝟏 ⊗ 𝟏 ≅ 𝟏` is an isomorphism such that `X ↦ 𝟏 ⊗ X` and `X ↦ X ⊗ 𝟏` are equivalences.
> The correspondence sends `(𝟏, l, r)` to `(𝟏, r_𝟏)` (`unitEquivUnitPair_apply_obj`,
> `unitEquivUnitPair_apply_iso`).

```lean
def unitEquivUnitPair : φ.MonoidalUnit ≃ UnitPair T
```

## Tag 0HAX, a lemma

[Tag 0HAX](https://stacks.math.columbia.edu/tag/0HAX) in the Stacks Project.

**`CategoryTheory.AssociativityConstraint.UnitPair.assoc_hom_comp_tensorMap_iso_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean#L113). The attribute's comment: “(1) `1 ⊗ id_𝟏 = id_𝟏 ⊗ 1`, with the associativity constraint written out”.

> Stacks Lemma 0HAX (1): `1 ⊗ id_𝟏 = id_𝟏 ⊗ 1`, as arrows `𝟏 ⊗ (𝟏 ⊗ 𝟏) ⟶ 𝟏 ⊗ 𝟏` once the
> associativity constraint is written out.

```lean
theorem assoc_hom_comp_tensorMap_iso_id :
    (φ.iso p.obj p.obj p.obj).hom ≫ tensorMap T p.iso.hom (𝟙 p.obj) =
      tensorMap T (𝟙 p.obj) p.iso.hom
```

**`CategoryTheory.AssociativityConstraint.UnitPair.eq_iso_inv_comp_tensorMap_comp_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean#L137). The attribute's comment: “(3) `a = 1 ∘ (a ⊗ id_𝟏) ∘ 1⁻¹ = 1 ∘ (id_𝟏 ⊗ a) ∘ 1⁻¹` for `a ∈ Mor(𝟏, 𝟏)`”.

> Stacks Lemma 0HAX (3): `a = 1 ∘ (a ⊗ id_𝟏) ∘ 1⁻¹ = 1 ∘ (id_𝟏 ⊗ a) ∘ 1⁻¹` for every
> `a ∈ Γ = Mor(𝟏, 𝟏)`.

```lean
theorem eq_iso_inv_comp_tensorMap_comp_iso (a : p.obj ⟶ p.obj) :
    a = p.iso.inv ≫ tensorMap T a (𝟙 p.obj) ≫ p.iso.hom ∧
      a = p.iso.inv ≫ tensorMap T (𝟙 p.obj) a ≫ p.iso.hom
```

**`CategoryTheory.AssociativityConstraint.UnitPair.comp_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean#L152). The attribute's comment: “(2) the monoid `Γ = Mor(𝟏, 𝟏)` is commutative”.

> Stacks Lemma 0HAX (2): composition of endomorphisms of `𝟏` is commutative.

```lean
theorem comp_comm (a b : p.obj ⟶ p.obj) : a ≫ b = b ≫ a
```

**`CategoryTheory.AssociativityConstraint.UnitPair.endCommMonoid`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean#L165). The attribute's comment: “(2) `Γ = Mor(𝟏, 𝟏)` is a commutative monoid”.

> Stacks Lemma 0HAX (2): `Γ = Mor(𝟏, 𝟏)` is a commutative monoid under composition.

```lean
def endCommMonoid : CommMonoid (End p.obj)
```

**`CategoryTheory.AssociativityConstraint.UnitPair.existsUnique_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean#L186). The attribute's comment: “(4) any other unit is isomorphic to `(𝟏, 1)` by a unique isomorphism”.

> Stacks Lemma 0HAX (4): any other pair `(𝟏', 1')` is isomorphic to `(𝟏, 1)` by a unique
> isomorphism, that is a unique `t : 𝟏' ≅ 𝟏` with `t ∘ 1' = 1 ∘ (t ⊗ t)`.

```lean
theorem existsUnique_iso (p' : UnitPair T) :
    ∃! t : p'.obj ≅ p.obj, p'.iso.hom ≫ t.hom = tensorMap T t.hom t.hom ≫ p.iso.hom
```

## Tag 0HAY, a lemma

[Tag 0HAY](https://stacks.math.columbia.edu/tag/0HAY) in the Stacks Project.

**`CategoryTheory.AssociativityConstraint.UnitPair.r_self_eq_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean#L59). The attribute's comment: “(1) the arrows `1` and `r_𝟏` agree”.

> Stacks Lemma 0HAY (1), for `r`: `r_𝟏 = 1 : 𝟏 ⊗ 𝟏 ≅ 𝟏`.

```lean
theorem r_self_eq_iso : p.r φ p.obj = p.iso
```

**`CategoryTheory.AssociativityConstraint.UnitPair.l_self_eq_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean#L66). The attribute's comment: “(1) the arrows `1` and `l_𝟏` agree”.

> Stacks Lemma 0HAY (1), for `l`: `l_𝟏 = 1 : 𝟏 ⊗ 𝟏 ≅ 𝟏`.

```lean
theorem l_self_eq_iso : p.l φ p.obj = p.iso
```

**`CategoryTheory.AssociativityConstraint.UnitPair.monoidalCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean#L78). The attribute's comment: “final statement: `(C, ⊗, φ, 𝟏, 1)` with `l`, `r` satisfies the assumptions of Mac Lane's coherence theorem, i.e. is a monoidal category”.

> The monoidal category structure on `C` with tensor product `T`, unit `𝟏`, associator `φ⁻¹`
> and unitors `l`, `r` attached to the pair `(𝟏, 1)`. This is the final statement of Stacks
> Lemma 0HAY: `(C, ⊗, φ, 𝟏, 1)` satisfies the assumptions of Mac Lane's coherence theorem
> (Natural associativity and commutativity, Theorem 5.2), namely the axioms of a monoidal
> category.

```lean
def monoidalCategory : MonoidalCategory C
```

**`CategoryTheory.AssociativityConstraint.UnitPair.coherence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean#L88). The attribute's comment: “final statement: Mac Lane's coherence theorem for `(C, ⊗, φ, 𝟏, 1)`, every diagram built from `φ`, `l`, `r` commutes”.

> Mac Lane's coherence theorem for `(C, ⊗, φ, 𝟏, 1)`, the conclusion of the theorem whose
> assumptions the final statement of Stacks Lemma 0HAY verifies: any two morphisms between
> the same objects of the free monoidal category on the objects of `C`, that is any two composites
> of tensor products of the constraints `φ`, `l`, `r` and their inverses with the same source and
> target, are sent to the same morphism of `C`.

```lean
theorem coherence {X Y : FreeMonoidalCategory C} (f g : X ⟶ Y) :
    letI := p.monoidalCategory φ
    FreeMonoidalCategory.projectMap id X Y f = FreeMonoidalCategory.projectMap id X Y g
```

**`CategoryTheory.AssociativityConstraint.UnitPair.assoc_hom_comp_tensorMap_l_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean#L95). The attribute's comment: “(2) `l_X ⊗ id_Y = l_{X ⊗ Y}`, with the associativity constraint written out”.

> Stacks Lemma 0HAY (2): `(l_X ⊗ id_Y) ∘ φ_{𝟏,X,Y} = l_{X ⊗ Y} : 𝟏 ⊗ (X ⊗ Y) ⟶ X ⊗ Y`.

```lean
theorem assoc_hom_comp_tensorMap_l_id (X Y : C) :
    (φ.iso p.obj X Y).hom ≫ tensorMap T (p.l φ X).hom (𝟙 Y) = (p.l φ (T.obj (X, Y))).hom
```

**`CategoryTheory.AssociativityConstraint.UnitPair.tensorMap_id_r_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/AssociativityConstraint.lean#L102). The attribute's comment: “(3) `id_X ⊗ r_Y = r_{X ⊗ Y}`, with the associativity constraint written out”.

> Stacks Lemma 0HAY (3): `id_X ⊗ r_Y = r_{X ⊗ Y} ∘ φ_{X,Y,𝟏} : X ⊗ (Y ⊗ 𝟏) ⟶ X ⊗ Y`.

```lean
theorem tensorMap_id_r_eq (X Y : C) :
    tensorMap T (𝟙 X) (p.r φ Y).hom = (φ.iso X Y p.obj).hom ≫ (p.r φ (T.obj (X, Y))).hom
```

## Tag 0FFL, a definition

[Tag 0FFL](https://stacks.math.columbia.edu/tag/0FFL) in the Stacks Project.

**`CategoryTheory.Functor.TensorStructure`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/KanExtension/ExtendTensor.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/KanExtension/ExtendTensor.lean#L102).

> **Stacks 0FFL.** A *functor of monoidal categories* `F : C ⥤ D`: an isomorphism
> `F(X) ⊗ F(Y) ⟶ F(X ⊗ Y)` functorial in `X` and `Y` such that for all `X, Y, Z` the diagram
> ```
> F(X) ⊗ (F(Y) ⊗ F(Z)) ⟶ F(X) ⊗ F(Y ⊗ Z) ⟶ F(X ⊗ (Y ⊗ Z))
>         |                                         |
> (F(X) ⊗ F(Y)) ⊗ F(Z) ⟶ F(X ⊗ Y) ⊗ F(Z) ⟶ F((X ⊗ Y) ⊗ Z)
> ```
> commutes (the vertical arrows being the associativity constraints), and such that `F(𝟙)` is a
> unit (`CategoryTheory.MonoidalCategory.IsUnitObject`). Mathlib's `CategoryTheory.Functor.Monoidal`
> additionally fixes a unit isomorphism `𝟙 ≅ F(𝟙)` compatible with the unitors, so it is stronger;
> `CategoryTheory.Functor.Monoidal.toTensorStructure` forgets that datum.

```lean
structure TensorStructure (F : C ⥤ D)
```

## Tag 0FFM, a lemma

[Tag 0FFM](https://stacks.math.columbia.edu/tag/0FFM) in the Stacks Project.

**`CategoryTheory.MonoidalCategory.invertible_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/InvertibleObject.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/InvertibleObject.lean#L116).

> For an object `X` of a monoidal category, the following are equivalent:
> 1. `tensorLeft X` is an equivalence;
> 2. `tensorRight X` is an equivalence;
> 3. `X` is invertible, i.e. it has a two-sided tensor inverse.

```lean
theorem invertible_tfae (X : C) :
    [ (tensorLeft X).IsEquivalence,
      (tensorRight X).IsEquivalence,
      IsInvertible X ].TFAE
```

## Tag 0FFN, a definition

[Tag 0FFN](https://stacks.math.columbia.edu/tag/0FFN) in the Stacks Project.

**`CategoryTheory.MonoidalCategory.HasInverse`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/InvertibleObject.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/InvertibleObject.lean#L38).

> A two-sided tensor inverse for an object `X` of a monoidal category: an object `inv`
> together with isomorphisms `X ⊗ inv ≅ 𝟙_ C` and `inv ⊗ X ≅ 𝟙_ C`.

```lean
structure HasInverse (X : C)
```

**`CategoryTheory.MonoidalCategory.IsInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/InvertibleObject.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/InvertibleObject.lean#L49).

> An object `X` of a monoidal category is *invertible* if it admits a two-sided tensor
> inverse, i.e. an object `X'` with `X ⊗ X' ≅ 𝟙_ C` and `X' ⊗ X ≅ 𝟙_ C`.

```lean
def IsInvertible (X : C) : Prop
```

## Tag 0FFP, a definition

[Tag 0FFP](https://stacks.math.columbia.edu/tag/0FFP) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.ExactPairing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ExactPairing#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch04.lean#L56) (StacksFrontier).

## Tag 0FFQ, a lemma

[Tag 0FFQ](https://stacks.math.columbia.edu/tag/0FFQ) in the Stacks Project.

**`CategoryTheory.tensorRightHomEquiv_whiskerRight_comp_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/DualHomBijections.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/DualHomBijections.lean#L59). The attribute's comment: “first bijection, natural in Z and Z'”.

> **Stacks Project, Tag 0FFQ**, first bijection. If `Y` is a left dual of `X` (in Mathlib,
> `[ExactPairing X Y]`), then `tensorRightHomEquiv Z' X Y Z : Mor(Z' ⊗ X, Z) ≃ Mor(Z', Z ⊗ Y)` is
> natural in `Z` and `Z'`: for `a : Z₂' ⟶ Z₁'` and `b : Z₁ ⟶ Z₂` it carries
> `(a ⊗ 1_X) ≫ f ≫ b` to `a ≫ e(f) ≫ (b ⊗ 1_Y)`.

```lean
theorem tensorRightHomEquiv_whiskerRight_comp_comp (X Y : C) [ExactPairing X Y] {Z₁' Z₂' Z₁ Z₂ : C}
    (a : Z₂' ⟶ Z₁') (f : Z₁' ⊗ X ⟶ Z₁) (b : Z₁ ⟶ Z₂) :
    tensorRightHomEquiv Z₂' X Y Z₂ (a ▷ X ≫ f ≫ b) =
      a ≫ tensorRightHomEquiv Z₁' X Y Z₁ f ≫ b ▷ Y
```

**`CategoryTheory.tensorLeftHomEquiv_whiskerLeft_comp_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/DualHomBijections.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/DualHomBijections.lean#L71). The attribute's comment: “second bijection, natural in Z and Z'”.

> **Stacks Project, Tag 0FFQ**, second bijection. If `Y` is a left dual of `X` (in Mathlib,
> `[ExactPairing X Y]`), then `tensorLeftHomEquiv Z' X Y Z : Mor(Y ⊗ Z', Z) ≃ Mor(Z', X ⊗ Z)` is
> natural in `Z` and `Z'`: for `a : Z₂' ⟶ Z₁'` and `b : Z₁ ⟶ Z₂` it carries
> `(1_Y ⊗ a) ≫ f ≫ b` to `a ≫ e(f) ≫ (1_X ⊗ b)`.

```lean
theorem tensorLeftHomEquiv_whiskerLeft_comp_comp (X Y : C) [ExactPairing X Y] {Z₁' Z₂' Z₁ Z₂ : C}
    (a : Z₂' ⟶ Z₁') (f : Y ⊗ Z₁' ⟶ Z₁) (b : Z₁ ⟶ Z₂) :
    tensorLeftHomEquiv Z₂' X Y Z₂ (Y ◁ a ≫ f ≫ b) =
      a ≫ tensorLeftHomEquiv Z₁' X Y Z₁ f ≫ X ◁ b
```

Declarations registered for the tag:

- [`CategoryTheory.tensorRightAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.tensorRightAdjunction#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Monoidal/DualHomBijections.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/DualHomBijections.lean#L82) (StacksFrontier): “first bijection as the adjunction tensorRight X ⊣ tensorRight Y”.
- [`CategoryTheory.tensorLeftAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.tensorLeftAdjunction#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Monoidal/DualHomBijections.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/DualHomBijections.lean#L84) (StacksFrontier): “second bijection as the adjunction tensorLeft Y ⊣ tensorLeft X”.

## Tag 0FFR, a remark

[Tag 0FFR](https://stacks.math.columbia.edu/tag/0FFR) in the Stacks Project.

**`CategoryTheory.Adjunction.IsTensorCompatible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean#L95).

> An adjunction `adj : tensorRight X ⊣ tensorRight Y`, i.e. a bijection
> `Mor(Z' ⊗ X, Z) ≃ Mor(Z', Z ⊗ Y)` functorial in `Z` and `Z'`, is *compatible with the tensor
> structure* if for all `W`, `Z`, `Z'` the square
>
> ```
>   Mor(Z' ⊗ X, Z)         →  Mor(Z', Z ⊗ Y)
>    | id_W ⊗ -                | id_W ⊗ -
>    v                         v
>   Mor(W ⊗ Z' ⊗ X, W ⊗ Z) →  Mor(W ⊗ Z', W ⊗ Z ⊗ Y)
> ```
>
> commutes, the two vertical maps being `f ↦ 𝟙 W ⊗ f` read through the associators.

```lean
def IsTensorCompatible (adj : tensorRight X ⊣ tensorRight Y) : Prop
```

**`CategoryTheory.Adjunction.unit_app_comp_tensorEvaluation_whiskerRight`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean#L152).

> The first identity that an adjunction `tensorRight X ⊣ tensorRight Y` supplies for free,
> with no compatibility with the tensor structure assumed: `(ε ⊗ 1_Y) ∘ η_Y = 1_Y`, where `η_Y` is
> the component of the unit at `Y`.

```lean
theorem unit_app_comp_tensorEvaluation_whiskerRight :
    adj.unit.app Y ≫ adj.tensorEvaluation ▷ Y = (λ_ Y).inv
```

**`CategoryTheory.Adjunction.tensorCoevaluation_whiskerRight_comp_counit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean#L165).

> The second identity that an adjunction `tensorRight X ⊣ tensorRight Y` supplies for free,
> with no compatibility with the tensor structure assumed: `ε_X ∘ (η ⊗ 1_X) = 1_X`, where `ε_X` is
> the component of the counit at `X`.

```lean
theorem tensorCoevaluation_whiskerRight_comp_counit_app :
    adj.tensorCoevaluation ▷ X ≫ adj.counit.app X = (λ_ X).hom
```

**`CategoryTheory.ExactPairing.isTensorCompatible_tensorRightAdjunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean#L179).

> The adjunction `tensorRight X ⊣ tensorRight Y` attached to an exact pairing is compatible
> with the tensor structure.

```lean
theorem ExactPairing.isTensorCompatible_tensorRightAdjunction (X Y : C) [ExactPairing X Y] :
    (tensorRightAdjunction X Y).IsTensorCompatible
```

**`CategoryTheory.Adjunction.IsTensorCompatible.exactPairing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean#L274).

> **The converse direction of Stacks 0FFR.** A tensor-compatible adjunction
> `tensorRight X ⊣ tensorRight Y` exhibits `Y` as a left dual of `X`: its candidate coevaluation
> and evaluation satisfy both triangle identities of an exact pairing.

```lean
def exactPairing (h : adj.IsTensorCompatible) : ExactPairing X Y
```

**`CategoryTheory.ExactPairing.existsUnique_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean#L290).

> **A left dual is unique up to unique isomorphism** (Stacks 0FFR, first assertion). If `Y₁`
> and `Y₂` are both left duals of `X`, i.e. `X` forms an exact pairing with each of them, there is
> exactly one isomorphism `e : Y₁ ≅ Y₂` compatible with the two pairings, that is, carrying the
> coevaluation `η₁ : 𝟙_ C ⟶ X ⊗ Y₁` to `η₂ : 𝟙_ C ⟶ X ⊗ Y₂` and the evaluation `ε₂ : Y₂ ⊗ X ⟶ 𝟙_ C`
> back to `ε₁ : Y₁ ⊗ X ⟶ 𝟙_ C`. The isomorphism is `CategoryTheory.rightDualIso`; uniqueness holds
> already among morphisms compatible with the coevaluations, by the bijection
> `tensorLeftHomEquiv`.

```lean
theorem ExactPairing.existsUnique_iso (X Y₁ Y₂ : C) [ExactPairing X Y₁] [ExactPairing X Y₂] :
    ∃! e : Y₁ ≅ Y₂, η_ X Y₁ ≫ X ◁ e.hom = η_ X Y₂ ∧ e.hom ▷ X ≫ ε_ X Y₂ = ε_ X Y₁
```

Declarations registered for the tag:

- [`CategoryTheory.rightDualIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.rightDualIso#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/RigidAdjunction.lean#L315) (StacksFrontier).

## Tag 0FFS, a lemma

[Tag 0FFS](https://stacks.math.columbia.edu/tag/0FFS) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.ExactPairing.tensor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ExactPairing.tensor#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Monoidal/Rigid.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/Rigid.lean#L193) (StacksFrontier).

## Tag 0HB0, a lemma

[Tag 0HB0](https://stacks.math.columbia.edu/tag/0HB0) in the Stacks Project.

**`CategoryTheory.CommutativityConstraint.symmetricCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/CommutativityConstraint.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/CommutativityConstraint.lean#L103). The attribute's comment: “final statement: `(C, ⊗, φ, ψ, 𝟏)` with `l`, `r` satisfies the assumptions of Mac Lane's coherence theorem, i.e. is a symmetric monoidal category”.

> The Mathlib symmetric monoidal structure with braiding `ψ` on the monoidal category
> `AssociativityConstraint.UnitPair.monoidalCategory`. This is the final statement of Stacks
> Lemma 0HB0: `(C, ⊗, φ, ψ, 𝟏)` satisfies the assumptions of Mac Lane's coherence theorem
> (Natural associativity and commutativity, Theorem 5.1).

```lean
noncomputable def symmetricCategory : letI := p.monoidalCategory φ; SymmetricCategory C
```

**`CategoryTheory.CommutativityConstraint.hom_comp_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/CommutativityConstraint.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/CommutativityConstraint.lean#L119). The attribute's comment: “(1) `1 ∘ ψ = 1 : 𝟏 ⊗ 𝟏 ⟶ 𝟏`”.

> Stacks Lemma 0HB0 (1): `1 ∘ ψ = 1 : 𝟏 ⊗ 𝟏 ⟶ 𝟏`.

```lean
theorem hom_comp_one : (ψ.iso p.obj p.obj).hom ≫ p.iso.hom = p.iso.hom
```

**`CategoryTheory.CommutativityConstraint.tensorMap_id_l_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/CommutativityConstraint.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/CommutativityConstraint.lean#L128). The attribute's comment: “(2) `id_X ⊗ l_Y = (l_X ⊗ id) ∘ (ψ ⊗ id_Y)`, with the associativity constraint written out”.

> Stacks Lemma 0HB0 (2): `id_X ⊗ l_Y = (l_X ⊗ id_Y) ∘ (ψ_{X,𝟏} ⊗ id_Y)` as arrows
> `X ⊗ 𝟏 ⊗ Y ⟶ X ⊗ Y`, with the associativity constraint `φ_{X,𝟏,Y}` written out.

```lean
theorem tensorMap_id_l_eq (X Y : C) :
    tensorMap T (𝟙 X) (p.l φ Y).hom =
      (φ.iso X p.obj Y).hom ≫ tensorMap T (ψ.iso X p.obj).hom (𝟙 Y) ≫
        tensorMap T (p.l φ X).hom (𝟙 Y)
```

## Tag 0FN8, a lemma

[Tag 0FN8](https://stacks.math.columbia.edu/tag/0FN8) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.BraidedCategory.exactPairing_swap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.BraidedCategory.exactPairing_swap#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch04.lean#L60) (StacksFrontier).

## Tag 0FFY, a definition

[Tag 0FFY](https://stacks.math.columbia.edu/tag/0FFY) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.Braided`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.Braided#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch04.lean#L58) (StacksFrontier).

## Tag 0GWJ, a remark

[Tag 0GWJ](https://stacks.math.columbia.edu/tag/0GWJ) in the Stacks Project.

**`InternalHom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean#L43). References: SGA 4 IV (10.2).

> **Definition 1 (Internal hom).**
> An internal hom on a monoidal category `C` consists of a bifunctor
> `hom : Cᵒᵖ ⥤ C ⥤ C` (contravariant in the first variable, covariant in the second)
> together with, for all objects `X, Y, Z`, a bijection
> `Φ X Y Z : Mor(X, hom(Y, Z)) ≃ Mor(X ⊗ Y, Z)` that is natural in `X`, in `Y`, and
> in `Z`.
>
> This is the opening clause of Stacks 0GWJ: `C` *has an internal hom* if for every pair `X, Y`
> there is an object `hom(X, Y)` with `Mor(X, hom(Y, Z)) = Mor(X ⊗ Y, Z)` functorially in
> `X, Y, Z`.

```lean
structure InternalHom (C : Type u) [Category.{v} C] [MonoidalCategory C]
```

**`InternalHom.ev`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean#L77). The attribute's comment: “(1)”. References: SGA 7 VIII (1.6), “more general”.

> **Construction of (1) Evaluation.**
> `ev_{X,Y} := Φ (id_{hom(X,Y)})`, the image of the identity under `Φ`.

```lean
def ev (X Y : C) : ih.homObj X Y ⊗ X ⟶ Y
```

**`InternalHom.comp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean#L85). The attribute's comment: “(2)”.

> **Construction of (2) Composition.**
> `c_{X,Y,Z}` is the image under `Φ⁻¹` (using `X` as the tensoring object) of the
> composite `hom(Y,Z) ⊗ hom(X,Y) ⊗ X → hom(Y,Z) ⊗ Y → Z` given by
> `(id ⊗ ev_{X,Y})` followed by `ev_{Y,Z}`.

```lean
def comp (X Y Z : C) : ih.homObj Y Z ⊗ ih.homObj X Y ⟶ ih.homObj X Z
```

**`InternalHom.tensorLeftMor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean#L93). The attribute's comment: “(3)”.

> **Construction of (3) Tensor on the left.**
> `t_{X,Y,Z}` is the image under `Φ⁻¹` of `id_Z ⊗ ev_{X,Y} : Z ⊗ hom(X,Y) ⊗ X → Z ⊗ Y`.

```lean
def tensorLeftMor (X Y Z : C) : Z ⊗ ih.homObj X Y ⟶ ih.homObj X (Z ⊗ Y)
```

**`InternalHom.coev`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean#L104). The attribute's comment: “(4)”.

> **Construction of (4) Unit / coevaluation.**
> `η_{X,Y} := ρ_Y⁻¹ ≫ (id_Y ⊗ u_X) ≫ t_{X,X,Y}`.

```lean
def coev (X Y : C) : Y ⟶ ih.homObj X (Y ⊗ X)
```

**`InternalHom.internalCurryMor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean#L112). The attribute's comment: “(5)”.

> **Construction of (5) Internalized currying (symmetric case).**
> `d_{X,Y,Z}` is the image under `Φ⁻¹` (using `hom(X,Y)` as the tensoring object) of the
> composite `hom(Y,Z) ⊗ X ⊗ hom(X,Y) → hom(Y,Z) ⊗ hom(X,Y) ⊗ X → hom(Y,Z) ⊗ Y → Z`,
> where the first arrow uses the braiding `σ_{X, hom(X,Y)}`.

```lean
def internalCurryMor [BraidedCategory C] (X Y Z : C) :
    ih.homObj Y Z ⊗ X ⟶ ih.homObj (ih.homObj X Y) Z
```

**`InternalHom.existsUnique_iso_compatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Monoidal/InternalHom.lean#L307). The attribute's comment: “uniqueness: the internal hom bifunctor is determined up to unique isomorphism”.

> **Stacks 0GWJ (uniqueness).** The internal hom bifunctor is determined up to unique
> isomorphism: for two internal homs `ih₁`, `ih₂` on `C` there is exactly one isomorphism of
> bifunctors `ih₁.hom ≅ ih₂.hom` compatible with the identifications
> `Mor(X, hom₁(Y, Z)) = Mor(X ⊗ Y, Z) = Mor(X, hom₂(Y, Z))`, namely `homIso ih₁ ih₂`.

```lean
theorem existsUnique_iso_compatible :
    ∃! i : ih₁.hom ≅ ih₂.hom, ∀ (X Y Z : C) (f : X ⟶ ih₁.homObj Y Z),
      ih₂.Φ X Y Z (f ≫ (i.hom.app (Opposite.op Y)).app Z) = ih₁.Φ X Y Z f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.43, Tag 0FFJ](https://stacks.math.columbia.edu/tag/0FFJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
