---
declaration: section
origin: cited
lean: CategoryTheory.Bicategory.IsTwoOneCategory, CategoryTheory.Bicategory.isTwoOneCategory_pith_cat, CategoryTheory.isTwoOneCategory_pith_catGroupoids, CategoryTheory.isTwoOneCategory_pith_catFiberedInGroupoids, CategoryTheory.isTwoOneCategory_pith_basedStack
statement: formalized
proof: formalized
---

# 4.30 (2, 1)-categories

Section 4.30 of the Stacks Project, [Tag 02X8](https://stacks.math.columbia.edu/tag/02X8). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 003I, a definition

[Tag 003I](https://stacks.math.columbia.edu/tag/003I) in the Stacks Project.

**`CategoryTheory.Bicategory.IsTwoOneCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Bicategory/TwoOneCategory.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Bicategory/TwoOneCategory.lean#L57).

> A *(strict) `(2,1)`-category* is a `2`-category — that is, a strict bicategory — in which
> every `2`-morphism is an isomorphism, the latter spelled as Mathlib's
> `Bicategory.IsLocallyGroupoid`, i.e. each hom-category `a ⟶ b` is a groupoid.

```lean
def IsTwoOneCategory (B : Type u) [Bicategory.{w, v} B] : Prop
```

## Tag 003K, an example

[Tag 003K](https://stacks.math.columbia.edu/tag/003K) in the Stacks Project.

**`CategoryTheory.Bicategory.isTwoOneCategory_pith_cat`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Bicategory/Cat.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Bicategory/Cat.lean#L75).

> **Stacks 003K.** The `2`-category `Cat` of categories, functors and morphisms of functors
> (Stacks 003J) becomes a `(2,1)`-category once only the *isomorphisms* of functors are allowed as
> `2`-morphisms. The resulting `2`-category is `Bicategory.Pith Cat`; that its `2`-morphisms are
> precisely the isomorphisms of functors is `Pith.homEquivIso`.

```lean
lemma isTwoOneCategory_pith_cat : IsTwoOneCategory (Pith Cat.{v, u})
```

## Tag 003M, a remark

[Tag 003M](https://stacks.math.columbia.edu/tag/003M) in the Stacks Project.

**`CategoryTheory.isTwoOneCategory_pith_catGroupoids`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Bicategory/CatVariants.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Bicategory/CatVariants.lean#L96). The attribute's comment: “the 2-category of groupoids”.

> **Stacks 003M**, the variant for groupoids: the `2`-category of groupoids becomes a
> `(2,1)`-category once only the isomorphisms of functors are allowed as `2`-morphisms.

```lean
lemma isTwoOneCategory_pith_catGroupoids :
    IsTwoOneCategory (Pith CatGroupoids.{v₁, u₁})
```

**`CategoryTheory.isTwoOneCategory_pith_catFiberedInGroupoids`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Bicategory/CatVariants.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Bicategory/CatVariants.lean#L104). The attribute's comment: “the 2-category of categories fibred in groupoids over a fixed category”.

> **Stacks 003M**, the variant for categories fibred in groupoids over a fixed category: the
> `2`-category of categories fibred in groupoids over `𝒞` (Stacks 02XS) becomes a `(2,1)`-category
> once only the isomorphisms of `2`-morphisms are kept.

```lean
lemma isTwoOneCategory_pith_catFiberedInGroupoids (𝒞 : Type u₁) [Category.{v₁} 𝒞] :
    IsTwoOneCategory (Pith (CatFiberedInGroupoids.{v₁, v₂, u₁, u₂} 𝒞))
```

**`CategoryTheory.isTwoOneCategory_pith_basedStack`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Bicategory/CatVariants.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Bicategory/CatVariants.lean#L111). The attribute's comment: “the 2-category of stacks”.

> **Stacks 003M**, the variant for stacks: the `2`-category of stacks over a site (Stacks 02ZG)
> becomes a `(2,1)`-category once only the isomorphisms of `2`-morphisms are kept.

```lean
lemma isTwoOneCategory_pith_basedStack (𝒞 : Type u₁) [Category.{v₁} 𝒞]
    (J : GrothendieckTopology 𝒞) :
    IsTwoOneCategory (Pith (BasedStack.{v₁, v₂, u₁, u₂} 𝒞 J))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.30, Tag 02X8](https://stacks.math.columbia.edu/tag/02X8)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
