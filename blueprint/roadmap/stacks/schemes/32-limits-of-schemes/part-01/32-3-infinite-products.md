---
declaration: section
origin: cited
lean: CategoryTheory.Limits.ProductsFromFiniteCofiltered.finiteSubproductsConeIsLimit, AlgebraicGeometry.hasProduct_of_isAffineHom, AlgebraicGeometry.isAffineHom_finiteSubproductsCone_π_app, AlgebraicGeometry.surjective_product_hom, AlgebraicGeometry.isIntegralHom_product
statement: formalized
proof: formalized
---

# 32.3 Infinite products

Section 32.3 of the Stacks Project, [Tag 0CNH](https://stacks.math.columbia.edu/tag/0CNH). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CNI, a lemma

[Tag 0CNI](https://stacks.math.columbia.edu/tag/0CNI) in the Stacks Project.

**`CategoryTheory.Limits.ProductsFromFiniteCofiltered.finiteSubproductsConeIsLimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/Descending/InfiniteProducts.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/Descending/InfiniteProducts.lean#L202). The attribute's comment: “limit of finite subproducts”.

> A product is canonically the inverse limit of its finite subproducts.

```lean
noncomputable def finiteSubproductsConeIsLimit [HasProduct X] :
    IsLimit (finiteSubproductsCone X)
```

**`AlgebraicGeometry.hasProduct_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/Descending/InfiniteProducts.lean, line 310](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/Descending/InfiniteProducts.lean#L310). The attribute's comment: “existence”.

> An arbitrary family of schemes affine over `S` has a product in the category of schemes
> over `S`.

```lean
theorem hasProduct_of_isAffineHom {I : Type u} (S : Scheme.{u})
    (T : I → Scheme.{u}) (f : ∀ i, T i ⟶ S) [∀ i, IsAffineHom (f i)] :
    HasProduct (fun i => Over.mk (f i))
```

**`AlgebraicGeometry.isAffineHom_finiteSubproductsCone_π_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/Descending/InfiniteProducts.lean, line 326](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/Descending/InfiniteProducts.lean#L326). The attribute's comment: “affine projections”.

> The canonical projection from the infinite product of a family of schemes affine over `S`
> onto any of its finite subproducts is affine.

```lean
theorem isAffineHom_finiteSubproductsCone_π_app {I : Type u} (S : Scheme.{u})
    (T : I → Scheme.{u}) (f : ∀ i, T i ⟶ S) [∀ i, IsAffineHom (f i)]
    [HasProduct (fun i => Over.mk (f i))] (J : (Finset (Discrete I))ᵒᵖ) :
    IsAffineHom ((finiteSubproductsCone (fun i => Over.mk (f i))).π.app J).left
```

## Tag 0CNJ, a lemma

[Tag 0CNJ](https://stacks.math.columbia.edu/tag/0CNJ) in the Stacks Project.

**`AlgebraicGeometry.surjective_product_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/Descending/InfiniteProductsSurjective.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/Descending/InfiniteProductsSurjective.lean#L94).

> **Stacks Project, Tag 0CNJ.** The structure morphism of the product over `S` of surjective
> affine morphisms is surjective.

```lean
theorem surjective_product_hom {I : Type u} (S : Scheme.{u})
    (T : I → Scheme.{u}) (f : ∀ i, T i ⟶ S) [∀ i, IsAffineHom (f i)]
    [∀ i, Surjective (f i)] :
    letI := hasProduct_of_isAffineHom S T f
    Surjective (∏ᶜ (fun i ↦ Over.mk (f i))).hom
```

## Tag 0CNK, a lemma

[Tag 0CNK](https://stacks.math.columbia.edu/tag/0CNK) in the Stacks Project.

**`AlgebraicGeometry.isIntegralHom_product`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/Descending/InfiniteProductsIntegral.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/Descending/InfiniteProductsIntegral.lean#L106).

> **Stacks Project, Tag 0CNK.** The product over a scheme of an arbitrary family of integral
> morphisms is integral over the base.

```lean
theorem isIntegralHom_product {I : Type u} (S : Scheme.{u})
    (T : I → Scheme.{u}) (f : ∀ i, T i ⟶ S) [∀ i, IsIntegralHom (f i)] :
    letI : HasProduct (fun i ↦ Over.mk (f i)) := hasProduct_of_isAffineHom S T f
    IsIntegralHom (∏ᶜ (fun i ↦ Over.mk (f i))).hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.3, Tag 0CNH](https://stacks.math.columbia.edu/tag/0CNH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
