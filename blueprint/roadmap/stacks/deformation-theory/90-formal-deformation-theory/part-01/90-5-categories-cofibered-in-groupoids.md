---
declaration: section
origin: cited
lean: Deformation.IsCofiberedInGroupoids, Deformation.isCofiberedInGroupoids_twoFibreProductBasedCategory, Deformation.cofiberedProduct, Deformation.isCofiberedInGroupoids_cofiberedProduct, Deformation.isomorphismClasses, Deformation.twoFibreProductBasedCategory_comp_baseProjection
statement: formalized
proof: formalized
---

# 90.5 Categories cofibered in groupoids

Section 90.5 of the Stacks Project, [Tag 06GA](https://stacks.math.columbia.edu/tag/06GA). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06GJ, a definition

[Tag 06GJ](https://stacks.math.columbia.edu/tag/06GJ) in the Stacks Project.

**`Deformation.IsCofiberedInGroupoids`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Cofibered.lean#L60).

> A functor `p : F ⥤ C` is *cofibered in groupoids* when the opposite
> functor `p.op : Fᵒᵖ ⥤ Cᵒᵖ` is fibered in groupoids.

```lean
public abbrev IsCofiberedInGroupoids {F : Type u₁} [Category.{v₁} F]
    {C : Type u₂} [Category.{v₂} C] (p : F ⥤ C) : Prop
```

## Tag 06GK, remarks

[Tag 06GK](https://stacks.math.columbia.edu/tag/06GK) in the Stacks Project.

**`Deformation.isCofiberedInGroupoids_twoFibreProductBasedCategory`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Applications/TwoFibreProductBaseChangeSmooth.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Applications/TwoFibreProductBaseChangeSmooth.lean#L93). The attribute's comment: “(13) the 2-fibre product of categories cofibered in groupoids over 𝒞\_Λ is given by the construction of their 2-fibre product as categories over 𝒞\_Λ”.

> A `2`-fibre product of categories cofibered in groupoids over `𝒞_Λ` is cofibered in
> groupoids: the construction of the `2`-fibre product as categories over `𝒞_Λ` serves as the
> `2`-fibre product in the `(2, 1)`-category of categories cofibered in groupoids over `𝒞_Λ`.

```lean
public lemma isCofiberedInGroupoids_twoFibreProductBasedCategory
    (p₁ : BasedFunctor 𝓗₁ 𝓖) (p₂ : BasedFunctor 𝓗₂ 𝓖)
    (h𝓗₁ : IsCofiberedInGroupoids 𝓗₁.p) (h𝓗₂ : IsCofiberedInGroupoids 𝓗₂.p)
    (h𝓖 : IsCofiberedInGroupoids 𝓖.p) :
    IsCofiberedInGroupoids (twoFibreProductBasedCategory p₁ p₂).p
```

**`Deformation.cofiberedProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/Product.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Cofibered/Product.lean#L81). The attribute's comment: “(14) products of categories cofibered in groupoids”.

> The *product* of two categories cofibered in groupoids `𝓕` and `𝓖` over `𝒞_Λ` is their
> `2`-fibre product `𝓕 ×_{𝒞_Λ} 𝓖`, taken over `𝒞_Λ` itself: the `2`-fibre product of the two
> structure morphisms of `𝓕` and `𝓖` into the base category read through the identity functor as a
> category cofibered in groupoids over itself.

```lean
public def cofiberedProduct (𝓕 : BasedCategory.{v₁, u₁} (ArtinianLocalAlgCat.{u, w, w} Λ k))
    (𝓖 : BasedCategory.{v₂, u₂} (ArtinianLocalAlgCat.{u, w, w} Λ k)) :
    BasedCategory (ArtinianLocalAlgCat.{u, w, w} Λ k)
```

**`Deformation.isCofiberedInGroupoids_cofiberedProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/Product.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Cofibered/Product.lean#L217). The attribute's comment: “(14) the product is again a category cofibered in groupoids”.

> The product of two categories cofibered in groupoids over `𝒞_Λ` is again cofibered in
> groupoids.

```lean
public theorem isCofiberedInGroupoids_cofiberedProduct
    (h𝓕 : IsCofiberedInGroupoids 𝓕.p) (h𝓖 : IsCofiberedInGroupoids 𝓖.p) :
    IsCofiberedInGroupoids (cofiberedProduct 𝓕 𝓖).p
```

## Tag 07W5, an item

[Tag 07W5](https://stacks.math.columbia.edu/tag/07W5) in the Stacks Project.

**`Deformation.isomorphismClasses`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/IsomorphismClasses.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Smooth/IsomorphismClasses.lean#L475).

> The associated covariant functor of fibrewise isomorphism classes.

```lean
noncomputable abbrev isomorphismClasses : C ⥤ Type u₁
```

## Tag 0DZJ, an item

[Tag 0DZJ](https://stacks.math.columbia.edu/tag/0DZJ) in the Stacks Project.

**`Deformation.cofiberedProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/Product.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Cofibered/Product.lean#L81). The attribute's comment: “the product of two categories cofibered in groupoids over 𝒞\_Λ is their 2-fibre product over 𝒞\_Λ”.

> The *product* of two categories cofibered in groupoids `𝓕` and `𝓖` over `𝒞_Λ` is their
> `2`-fibre product `𝓕 ×_{𝒞_Λ} 𝓖`, taken over `𝒞_Λ` itself: the `2`-fibre product of the two
> structure morphisms of `𝓕` and `𝓖` into the base category read through the identity functor as a
> category cofibered in groupoids over itself.

```lean
public def cofiberedProduct (𝓕 : BasedCategory.{v₁, u₁} (ArtinianLocalAlgCat.{u, w, w} Λ k))
    (𝓖 : BasedCategory.{v₂, u₂} (ArtinianLocalAlgCat.{u, w, w} Λ k)) :
    BasedCategory (ArtinianLocalAlgCat.{u, w, w} Λ k)
```

**`Deformation.isCofiberedInGroupoids_cofiberedProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/Product.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Cofibered/Product.lean#L217). The attribute's comment: “the product of two categories cofibered in groupoids is cofibered in groupoids”.

> The product of two categories cofibered in groupoids over `𝒞_Λ` is again cofibered in
> groupoids.

```lean
public theorem isCofiberedInGroupoids_cofiberedProduct
    (h𝓕 : IsCofiberedInGroupoids 𝓕.p) (h𝓖 : IsCofiberedInGroupoids 𝓖.p) :
    IsCofiberedInGroupoids (cofiberedProduct 𝓕 𝓖).p
```

**`Deformation.twoFibreProductBasedCategory_comp_baseProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Cofibered/Product.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Cofibered/Product.lean#L233). The attribute's comment: “the 2-fibre product over 𝒞\_Λ along the structure morphisms is the product”.

> Given morphisms `p₁ : 𝓗 → 𝓕` and `p₂ : 𝓖 → 𝓕` of categories cofibered in groupoids over `𝒞_Λ`,
> the `2`-fibre product of `𝓗` and `𝓖` formed over `𝒞_Λ` — that is, over the two composites of `p₁`
> and `p₂` with the structure morphism of `𝓕` — is the product `𝓗 ×_{𝒞_Λ} 𝓖`.

```lean
public theorem twoFibreProductBasedCategory_comp_baseProjection
    (p₁ : BasedFunctor 𝓗 𝓕) (p₂ : BasedFunctor 𝓖 𝓕) :
    twoFibreProductBasedCategory (BasedFunctor.comp p₁ (baseProjection 𝓕.p))
        (BasedFunctor.comp p₂ (baseProjection 𝓕.p)) = cofiberedProduct 𝓗 𝓖
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.5, Tag 06GA](https://stacks.math.columbia.edu/tag/06GA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
