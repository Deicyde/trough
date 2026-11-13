---
declaration: section
origin: cited
lean: CategoryTheory.IsDiscrete, CategoryTheory.Functor.isFiberedInSets_iff, CategoryTheory.Functor.IsFiberedInSets, CategoryTheory.CatFiberedInSets, CategoryTheory.Functor.IsFiberedInSets.twoFibreProd, CategoryTheory.Functor.isFiberedInSets_presheafFiberedInSetsProjection, CategoryTheory.CatFiberedInSets.exists_eq_eqToHom, CategoryTheory.CatFiberedInSets.presheafEquivalence
statement: formalized
proof: formalized
---

# 4.38 Categories fibred in sets

Section 4.38 of the Stacks Project, [Tag 0042](https://stacks.math.columbia.edu/tag/0042). 7 tags here are carried by 10 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02Y0, a definition

[Tag 02Y0](https://stacks.math.columbia.edu/tag/02Y0) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.IsDiscrete`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.IsDiscrete#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch04.lean#L45) (StacksFrontier).

## Tag 0043, a definition

[Tag 0043](https://stacks.math.columbia.edu/tag/0043) in the Stacks Project.

**`CategoryTheory.Functor.isFiberedInSets_iff`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSets/TwoCategory.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInSets/TwoCategory.lean#L119). The attribute's comment: “The defining property: `p` is fibred in sets iff it is fibred in groupoids (003T) and every fibre category `p.Fiber U` is discrete.”.

> **Stacks 0043.** A functor is fibred in sets, i.e. every morphism of the base has a unique
> lift with a prescribed target, if and only if it is fibred in groupoids and all of its fibre
> categories are discrete. The right-hand side is Stacks' definition of a category fibred in sets
> (a category fibred in discrete categories); a category is discrete (`CategoryTheory.IsDiscrete`)
> when its only morphisms are identities.

```lean
lemma Functor.isFiberedInSets_iff (p : 𝒮 ⥤ 𝒞) :
    p.IsFiberedInSets ↔ p.IsFiberedInGroupoids ∧ ∀ U : 𝒞, IsDiscrete (p.Fiber U)
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.IsFiberedInSets`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInSets/TwoCategoryIsCategory.lean#L82), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FiberedInSets/Defs.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInSets/Defs.lean#L24) (StacksFrontier): “Stated through the equivalent unique-lift property; `Functor.isFiberedInSets_iff` identifies it with Stacks' definition: fibred in groupoids with discrete fibre categories.”.

## Tag 04S8, a definition

[Tag 04S8](https://stacks.math.columbia.edu/tag/04S8) in the Stacks Project.

**`CategoryTheory.CatFiberedInSets`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSets/TwoCategory.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInSets/TwoCategory.lean#L153).

> The 2-category of categories fibred in sets over `𝒞`: the full sub-2-category of the
> 2-category `BasedCategory 𝒞` of categories over `𝒞` spanned by the categories fibred in sets.
> Explicitly:
>
> 1. its objects are the categories `p : 𝒮 ⥤ 𝒞` over `𝒞` that are fibred in sets;
> 2. its 1-morphisms `(𝒮, p) ⟶ (𝒮', p')` are the functors `G : 𝒮 ⥤ 𝒮'` with `p' ∘ G = p`;
> 3. its 2-morphisms `t : G ⟶ H` are the morphisms of functors with `p'(t_x) = 𝟙 (p x)` for every
>    object `x` of `𝒮`.

```lean
abbrev CatFiberedInSets (𝒞 : Type u₁) [Category.{v₁} 𝒞]
```

## Tag 0047, a lemma

[Tag 0047](https://stacks.math.columbia.edu/tag/0047) in the Stacks Project.

**`CategoryTheory.Functor.IsFiberedInSets.twoFibreProd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSets/TwoFibreProduct.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInSets/TwoFibreProduct.lean#L147).

> **Stacks 0047 (Lemma 4.38.4).** The 2-category of categories fibred in sets over `𝒞` has
> 2-fibre products: if `𝒳`, `𝒴`, `𝒮` are fibred in sets over `𝒞` and `F : 𝒳 ⥤ 𝒮`, `G : 𝒴 ⥤ 𝒮`
> are 1-morphisms over `𝒞`, then the 2-fibre product `𝒳 ×_𝒮 𝒴` of Stacks `0040`, with its
> structure functor, is again fibred in sets over `𝒞`.

```lean
theorem Functor.IsFiberedInSets.twoFibreProd
    [pX.IsFiberedInSets] [pY.IsFiberedInSets] [pS.IsFiberedInSets]
    (hF : F ⋙ pS = pX) (hG : G ⋙ pS = pY) :
    (TwoFibreProd.proj pX pY pS F G).IsFiberedInSets
```

## Tag 04TM, an example

[Tag 04TM](https://stacks.math.columbia.edu/tag/04TM) in the Stacks Project.

**`CategoryTheory.Functor.isFiberedInSets_presheafFiberedInSetsProjection`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSets/OfPresheaf.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInSets/OfPresheaf.lean#L97). References: SGA 7 VI (1.1(a)), “set-valued F”.

> **Stacks 04TM.** For a presheaf `F : Cᵒᵖ ⥤ Type*`, the category `𝒮_F = (F.Elements)ᵒᵖ`, whose
> objects are the pairs `(U, x)` with `x ∈ F(U)` and whose morphisms `(V, y) ⟶ (U, x)` are the
> `f : V ⟶ U` with `f^* x = y`, is fibred in sets over `C` by `p_F : (U, x) ↦ U`: a morphism
> `f : V ⟶ U` and an object `(U, x)` have the unique lift `(V, f^* x) ⟶ (U, x)`.

```lean
instance isFiberedInSets_presheafFiberedInSetsProjection :
    (presheafFiberedInSetsProjection F).IsFiberedInSets
```

## Tag 02Y2, a lemma

[Tag 02Y2](https://stacks.math.columbia.edu/tag/02Y2) in the Stacks Project.

**`CategoryTheory.CatFiberedInSets.exists_eq_eqToHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSets/PresheafEquivalence.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInSets/PresheafEquivalence.lean#L228). The attribute's comment: “2-morphisms between categories fibred in sets are identities”.

> **Stacks 02Y2**, first assertion. The only 2-morphisms between categories fibred in sets are
> identities: a 2-morphism `t : G ⟶ H` of the 2-category of categories fibred in sets over `𝒞`
> forces `G = H`, and `t` is then the identity 2-morphism of `G` (written `eqToHom`). In other words,
> the 2-category of categories fibred in sets is a category.

```lean
theorem exists_eq_eqToHom {𝒳 𝒴 : CatFiberedInSets.{v₁, v₂, u₁, u₂} 𝒞} {G H : 𝒳 ⟶ 𝒴}
    (t : G ⟶ H) : ∃ h : G = H, t = eqToHom h
```

**`CategoryTheory.CatFiberedInSets.presheafEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSets/PresheafEquivalence.lean, line 361](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInSets/PresheafEquivalence.lean#L361). The attribute's comment: “presheaves of sets ≌ categories fibred in sets: F ↦ S\_F, p ↦ (U ↦ Ob(S\_U))”.

> **Stacks 02Y2**, the equivalence. Let `C` be a category. There is an equivalence of categories
> between the category of presheaves of sets on `C` and the category of categories fibred in sets
> over `C`. The functor from left to right is the construction `F ↦ 𝒮_F` of Stacks 04TM
> (`CategoryTheory.CatFiberedInSets.ofPresheaf`), and the functor from right to left sends
> `p : 𝒮 ⥤ C` to its presheaf of objects `U ↦ Ob(𝒮_U)`
> (`CategoryTheory.CatFiberedInSets.objPresheafFunctor`); see
> `CategoryTheory.CatFiberedInSets.presheafEquivalence_functor` and
> `CategoryTheory.CatFiberedInSets.presheafEquivalence_inverse`.

```lean
noncomputable def presheafEquivalence :
    (Cᵒᵖ ⥤ Type (max u w)) ≌ CatFiberedInSets.{v, v, u, max u w} C
```

## Tag 0044, an example

[Tag 0044](https://stacks.math.columbia.edu/tag/0044) in the Stacks Project.

**`CategoryTheory.overEquivElementsOp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Elements.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Elements.lean#L95).

> **`C/X` is the category of elements of `h_X`.** The slice category `C/X` is equivalent to
> the category `S_{h_X} = ((h_X).Elements)ᵒᵖ` attached to the representable presheaf
> `h_X = Mor_C(-, X)`.
>
> Both round trips are the identity functor on the nose, so the unit and counit are
> identities.

```lean
def overEquivElementsOp : Over X ≌ ((yoneda.obj X).Elements)ᵒᵖ
```

**`CategoryTheory.overEquivElementsOpForget`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Elements.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Elements.lean#L113).

> **The equivalence of `overEquivElementsOp` is an equivalence over `C`.** It carries the
> structure functor `C/X → C` to the structure functor `S_{h_X} → C`, which is
> `(Functor.Elements.π h_X).leftOp`. This is the sense in which `C/X` is *canonically
> equivalent over `C`* to `S_{h_X}`.

```lean
def overEquivElementsOpForget :
    (overEquivElementsOp X).functor ⋙ (Functor.Elements.π (yoneda.obj X)).leftOp
      ≅ Over.forget X
```

**`CategoryTheory.Over.eq_of_hom_left_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Elements.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Elements.lean#L269).

> **The fibre categories of `C/X → C` have only identities (existence part).** If there is
> a morphism `Over.mk f ⟶ Over.mk g` of `C/X` lying over the identity of `U`, then `f = g`.

```lean
theorem eq_of_hom_left_id {U : C} {f g : U ⟶ X} (φ : Over.mk f ⟶ Over.mk g)
    (hφ : φ.left = 𝟙 U) : f = g
```

**`CategoryTheory.Over.hom_eq_id_of_left_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Elements.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Elements.lean#L278).

> **The fibre categories of `C/X → C` have only identities (uniqueness part).** A morphism
> of `C/X` from an object to itself lying over the identity is the identity. Together with
> `CategoryTheory.Over.eq_of_hom_left_id` this says that the fibre category of `C/X → C` over
> `U` has the morphisms `h : U ⟶ X` as objects and only identities as morphisms.

```lean
theorem hom_eq_id_of_left_id {U : C} {f : U ⟶ X} (φ : Over.mk f ⟶ Over.mk f)
    (hφ : φ.left = 𝟙 U) : φ = 𝟙 (Over.mk f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.38, Tag 0042](https://stacks.math.columbia.edu/tag/0042)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
