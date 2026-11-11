---
declaration: section
origin: cited
lean: CategoryTheory.IsDiscrete, CategoryTheory.CatFiberedInSets, CategoryTheory.Functor.IsFiberedInSets.twoFibreProd, elementsCategory, CategoryTheory.Functor.twoMorphisms_are_identity, CategoryTheory.overEquivElementsOp, CategoryTheory.overEquivElementsOpForget, CategoryTheory.Over.eq_of_hom_left_id
statement: formalized
proof: formalized
---

# 4.38 Categories fibred in sets

Section 4.38 of the Stacks Project, [Tag 0042](https://stacks.math.columbia.edu/tag/0042). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02Y0, a definition

[Tag 02Y0](https://stacks.math.columbia.edu/tag/02Y0) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.IsDiscrete`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.IsDiscrete#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L45) (StacksFrontier).

## Tag 04S8, a definition

[Tag 04S8](https://stacks.math.columbia.edu/tag/04S8) in the Stacks Project.

**`CategoryTheory.CatFiberedInSets`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSets/TwoCategory.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInSets/TwoCategory.lean#L149).

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

**`CategoryTheory.Functor.IsFiberedInSets.twoFibreProd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSets/TwoFibreProduct.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInSets/TwoFibreProduct.lean#L147).

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

**`elementsCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSets/OfPresheaf.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInSets/OfPresheaf.lean#L53). References: SGA 7 VI (1.1(a)), “set-valued F”.

> **Stacks 04TM.** The category `𝒮_F` attached to a presheaf `F : Cᵒᵖ ⥤ Type*`: objects are
> the pairs `(U, x)` with `x ∈ F(U)`, and a morphism `(V, y) ⟶ (U, x)` is an `f : V ⟶ U` of `C`
> with `f^* x = y`. This is Mathlib's category of elements of `F`.

```lean
def elementsCategory {C : Type*} [Category C] (F : Cᵒᵖ ⥤ Type*) :
    Category F.Elements
```

## Tag 02Y2, a lemma

[Tag 02Y2](https://stacks.math.columbia.edu/tag/02Y2) in the Stacks Project.

**`CategoryTheory.Functor.twoMorphisms_are_identity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSets/TwoCategoryIsCategory.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInSets/TwoCategoryIsCategory.lean#L137).

> A 2-morphism over `𝒞` between two 1-morphisms into a category fibred in sets is an
> identity: the two 1-morphisms are equal.

```lean
theorem twoMorphisms_are_identity
    {𝒮 : Type u₂} [Category.{v₂} 𝒮] {𝒮' : Type u₃} [Category.{v₃} 𝒮']
    (p : 𝒮 ⥤ 𝒞) (p' : 𝒮' ⥤ 𝒞) [p'.IsFiberedInSets]
    (F G : 𝒮 ⥤ 𝒮') (hF : F ⋙ p' = p) (hG : G ⋙ p' = p)
    (η : F ⟶ G)
    (hη : ∀ x, HEq (p'.map (η.app x)) (𝟙 (p.obj x))) :
    F = G
```

## Tag 0044, an example

[Tag 0044](https://stacks.math.columbia.edu/tag/0044) in the Stacks Project.

**`CategoryTheory.overEquivElementsOp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Elements.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Elements.lean#L95).

> **`C/X` is the category of elements of `h_X`.** The slice category `C/X` is equivalent to
> the category `S_{h_X} = ((h_X).Elements)ᵒᵖ` attached to the representable presheaf
> `h_X = Mor_C(-, X)`.
>
> Both round trips are the identity functor on the nose, so the unit and counit are
> identities.

```lean
def overEquivElementsOp : Over X ≌ ((yoneda.obj X).Elements)ᵒᵖ
```

**`CategoryTheory.overEquivElementsOpForget`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Elements.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Elements.lean#L113).

> **The equivalence of `overEquivElementsOp` is an equivalence over `C`.** It carries the
> structure functor `C/X → C` to the structure functor `S_{h_X} → C`, which is
> `(Functor.Elements.π h_X).leftOp`. This is the sense in which `C/X` is *canonically
> equivalent over `C`* to `S_{h_X}`.

```lean
def overEquivElementsOpForget :
    (overEquivElementsOp X).functor ⋙ (Functor.Elements.π (yoneda.obj X)).leftOp
      ≅ Over.forget X
```

**`CategoryTheory.Over.eq_of_hom_left_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Elements.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Elements.lean#L268).

> **The fibre categories of `C/X → C` have only identities (existence part).** If there is
> a morphism `Over.mk f ⟶ Over.mk g` of `C/X` lying over the identity of `U`, then `f = g`.

```lean
theorem eq_of_hom_left_id {U : C} {f g : U ⟶ X} (φ : Over.mk f ⟶ Over.mk g)
    (hφ : φ.left = 𝟙 U) : f = g
```

**`CategoryTheory.Over.hom_eq_id_of_left_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Elements.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Elements.lean#L277).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
