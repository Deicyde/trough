---
declaration: section
origin: cited
lean: Deformation.Artin.factorizationEquivalence, Deformation.Artin.artinianLocalAlgCatEquiv, Deformation.Artin.predeformationCategory, Deformation.Artin.ArtinianLocalFactorization, Deformation.Artin.predeformationCategory_isPredeformationCategory, Deformation.Artin.mapPredeformationCategory, Deformation.Artin.isSmoothOnPredeformationCategories_of_isFormallySmoothOnObjects, Deformation.Artin.isSmoothOnPredeformationCategories_of_isRelativelyFormallySmooth
statement: formalized
proof: formalized
---

# 98.3 Predeformation categories

Section 98.3 of the Stacks Project, [Tag 07T2](https://stacks.math.columbia.edu/tag/07T2). 7 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07T2, the section

[Tag 07T2](https://stacks.math.columbia.edu/tag/07T2) in the Stacks Project.

**`Deformation.Artin.factorizationEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Predeformation/Factorization.lean, line 398](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Predeformation/Factorization.lean#L398). The attribute's comment: “the category 𝒞\_Λ is equivalent to the opposite of the category of factorizations Spec k ⟶ Spec A ⟶ S of the point, with A Artinian local and its residue field identified with k”.

> **The category `𝒞_Λ` is equivalent to the opposite of the category of factorizations
> `Spec k ⟶ Spec A ⟶ S` of the given point by the spectrum of an Artinian local ring with
> residue field identified with `k`.**

```lean
public def factorizationEquivalence :
    ArtinianLocalAlgCat.{u, u, u} Λ k ≌ (ArtinianLocalFactorization S k x)ᵒᵖ
```

**`Deformation.Artin.artinianLocalAlgCatEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Predeformation/Factorization.lean, line 422](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Predeformation/Factorization.lean#L422). The attribute's comment: “the category 𝒞\_Λ is independent, up to canonical equivalence, of the choice of the affine open Spec Λ ⊂ S the point factors through”.

> **The category `𝒞_Λ` does not depend, up to canonical equivalence, on the choice of the
> affine open `Spec Λ ⊂ S` through which the point factors.** Both are equivalent to the
> opposite of the category of factorizations of the point, which refers only to the point.

```lean
public def artinianLocalAlgCatEquiv :
    ArtinianLocalAlgCat.{u, u, u} Λ k ≌ ArtinianLocalAlgCat.{u, u, u} Λ' k
```

Declarations registered for the tag:

- [`Deformation.Artin.predeformationCategory`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Predeformation.lean#L225), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/Artin/Predeformation.lean, line 271](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Predeformation.lean#L271) (StacksFrontier): “the construction of the category 𝓕\_\{𝓧,k,x₀} of deformations of x₀, its objects and its reversed morphisms, together with its projection to 𝒞\_Λ”.

## Tag 07T3, an equation

[Tag 07T3](https://stacks.math.columbia.edu/tag/07T3) in the Stacks Project.

**`Deformation.Artin.ArtinianLocalFactorization`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Predeformation.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Predeformation.lean#L72).

> A factorization `Spec(k) ⟶ Spec(A) ⟶ S` of a finite-type field-valued point
> of a locally Noetherian scheme, where `A` is an Artinian local ring and the first arrow
> identifies `k` with its residue field.

```lean
public structure ArtinianLocalFactorization (S : Scheme.{u}) (k : Type u) [Field k]
    (x : Spec (CommRingCat.of k) ⟶ S) [IsLocallyNoetherian S] [LocallyOfFiniteType x]
    [QuasiCompact x]
```

## Tag 07T4, an equation

[Tag 07T4](https://stacks.math.columbia.edu/tag/07T4) in the Stacks Project.

**`Deformation.Artin.predeformationCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Predeformation.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Predeformation.lean#L225).

> The predeformation category `𝓕_{𝓧,k,x₀}` and its canonical functor to `𝒞_Λ`.

```lean
public noncomputable def predeformationCategory :
    PredeformationConstruction iΛ q x₀ hx₀
```

## Tag 07T5, a lemma

[Tag 07T5](https://stacks.math.columbia.edu/tag/07T5) in the Stacks Project.

**`Deformation.Artin.predeformationCategory_isPredeformationCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ArtinCriteria/Predeformation.lean, line 646](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ArtinCriteria/Predeformation.lean#L646).

> The canonical deformation category of a point of a fibred category is a
> predeformation category.

```lean
public theorem predeformationCategory_isPredeformationCategory
    (hp : p.IsFiberedInGroupoids) :
    let C := Deformation.Artin.predeformationCategory iΛ
      (p ⋙ Over.post B.inclusion) x₀ hx₀
    letI : Category C.carrier := C.category
    Deformation.IsPredeformationCategory C.projection
```

## Tag 07WJ, an equation

[Tag 07WJ](https://stacks.math.columbia.edu/tag/07WJ) in the Stacks Project.

**`Deformation.Artin.mapPredeformationCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Predeformation.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Predeformation.lean#L439).

> A morphism over the base induces a canonical functor of predeformation
> categories over `𝒞_Λ`.

```lean
public def mapPredeformationCategory :
    InducedPredeformationFunctor iΛ qX qY F hF x₀ hx₀
```

## Tag 07WK, a lemma

[Tag 07WK](https://stacks.math.columbia.edu/tag/07WK) in the Stacks Project.

**`Deformation.Artin.isSmoothOnPredeformationCategories_of_isFormallySmoothOnObjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/SmoothPredeformation.lean, line 523](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/SmoothPredeformation.lean#L523). The attribute's comment: “formally smooth on objects”.

> **Stacks 07WK**, case (1). A 1-morphism of categories fibred in groupoids over the big
> fppf category of `S` which is formally smooth on objects induces a smooth functor of
> predeformation categories at every finite type field-valued point of the source.
>
> This is also the formally-smooth-on-objects clause of Stacks 07XW — the condition the
> openness-of-versality statement is about — so both tags are registered here, on the declaration
> that carries the proof.

```lean
public theorem isSmoothOnPredeformationCategories_of_isFormallySmoothOnObjects
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) [IsLocallyNoetherian S]
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} (p : 𝒳 ⟶ 𝒴)
    (hp : Stack.IsFormallySmoothOnObjects B S hS 𝒳 𝒴 p) :
    IsSmoothOnPredeformationCategories B S hS 𝒳.val.p 𝒴.val.p
      (CatFiberedInGroupoids.homFunctor p)
      (CatFiberedInGroupoids.homFunctor_comp_p p)
```

**`Deformation.Artin.isSmoothOnPredeformationCategories_of_isRelativelyFormallySmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/SmoothPredeformation.lean, line 847](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/SmoothPredeformation.lean#L847). The attribute's comment: “representably formally smooth”.

> **Stacks 07WK**, case (2). A 1-morphism of categories fibred in groupoids over the big fppf
> category of `S` which is representable by algebraic spaces and formally smooth induces a smooth
> functor of predeformation categories at every finite type field-valued point of the source.

```lean
public theorem isSmoothOnPredeformationCategories_of_isRelativelyFormallySmooth
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) [IsLocallyNoetherian S]
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} (p : 𝒳 ⟶ 𝒴)
    (hrep : Stack.IsRepresentableByAlgebraicSpaces B S hS p.hom)
    (hform : BigFppfOver.IsRelativelyFormallySmooth B S hS p) :
    IsSmoothOnPredeformationCategories B S hS 𝒳.val.p 𝒴.val.p
      (CatFiberedInGroupoids.homFunctor p)
      (CatFiberedInGroupoids.homFunctor_comp_p p)
```

**`Deformation.Artin.isSmoothOnPredeformationCategories_of_formallySmooth_or_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/SmoothPredeformationCases.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/SmoothPredeformationCases.lean#L52).

> **Stacks 07WK.** Let `S` be a locally Noetherian scheme and `F : 𝒳 → 𝒴` a 1-morphism of
> categories fibred in groupoids over the big fppf category of `S` which is (1) formally smooth on
> objects, or (2) representable by algebraic spaces and formally smooth, or (3) representable by
> algebraic spaces and smooth. Then for every finite type field `k` over `S` and every object `x₀`
> of `𝒳` over `Spec k` the induced functor of predeformation categories is smooth.

```lean
theorem isSmoothOnPredeformationCategories_of_formallySmooth_or_smooth
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) [IsLocallyNoetherian S]
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} (p : 𝒳 ⟶ 𝒴)
    (h : Stack.IsFormallySmoothOnObjects B S hS 𝒳 𝒴 p ∨
      (Stack.IsRepresentableByAlgebraicSpaces B S hS p.hom ∧
        BigFppfOver.IsRelativelyFormallySmooth B S hS p) ∨
      Stack.IsRelativelySmooth B S hS p) :
    IsSmoothOnPredeformationCategories B S hS 𝒳.val.p 𝒴.val.p
      (CatFiberedInGroupoids.homFunctor p)
      (CatFiberedInGroupoids.homFunctor_comp_p p)
```

Declarations registered for the tag:

- [`Deformation.Artin.isSmoothOnPredeformationCategories_of_isRelativelySmooth'`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/RepresentableSmoothVersality.lean#L57), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/Artin/Versality/RepresentablySmoothPredeformation.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/RepresentablySmoothPredeformation.lean#L37) (StacksFrontier): “representably smooth”.

## Tag 07WL, a lemma

[Tag 07WL](https://stacks.math.columbia.edu/tag/07WL) in the Stacks Project.

**`Deformation.Artin.fibreProductOfPredeformationCategories`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Predeformation/FibreProduct.lean, line 1248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Predeformation/FibreProduct.lean#L1248).

> Let `𝒲` be a 2-fibre product of `𝒳 ⟶ 𝒴` and `𝒵 ⟶ 𝒴` in categories fibred in groupoids over
> schemes over `S`, and let `w₀` be an object of `𝒲` over `Spec k` with images `x₀`, `z₀`,
> `y₀ = F(x₀)`. Then the square of predeformation categories `𝓕_{𝒲,k,w₀} ⟶ 𝓕_{𝒵,k,z₀}`,
> `𝓕_{𝒳,k,x₀} ⟶ 𝓕_{𝒴,k,y₀}` is a 2-fibre product of predeformation categories.

```lean
public def fibreProductOfPredeformationCategories (hG : G ⋙ qY = qZ)
    (hψ : ∀ w : W, qY.IsHomLift (𝟙 (qW.obj w)) (ψ.hom.app w))
    (hqW : qW.IsFiberedInGroupoids) (_hqX : qX.IsFiberedInGroupoids)
    (_hqZ : qZ.IsFiberedInGroupoids) (_hqY : qY.IsFiberedInGroupoids)
    (hfp : (TwoFibreProductOver.lift qX qZ qY F G qW A B hA hB ψ hψ).IsEquivalence) :
    PredeformationFibreProductData iΛ qW qX qZ qY A B F G hA hB hF ψ w₀ hw₀
```

**`Deformation.Artin.fibreProductOfPredeformationCategoriesOfEssSurj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Predeformation/FibreProduct.lean, line 1263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Predeformation/FibreProduct.lean#L1263). The attribute's comment: “the essential surjectivity of the ambient comparison functor supplied directly”.

> The square of predeformation categories of a 2-fibre product is a 2-fibre product, given the
> essential surjectivity of the ambient comparison functor strictly over the base in place of the
> fibredness of `qW`.

```lean
public def fibreProductOfPredeformationCategoriesOfEssSurj (hG : G ⋙ qY = qZ)
    (hψ : ∀ w : W, qY.IsHomLift (𝟙 (qW.obj w)) (ψ.hom.app w))
    (hess : ∀ (U : Over S) (t : TwoFibreProductOver qX qZ qY F G),
      (TwoFibreProductOver.structureFunctor qX qZ qY F G).obj t = U →
      ∃ w : W, qW.obj w = U ∧ ∃ e :
        (TwoFibreProductOver.lift qX qZ qY F G qW A B hA hB ψ hψ).obj w ≅ t,
        (TwoFibreProductOver.structureFunctor qX qZ qY F G).IsHomLift (𝟙 U) e.hom)
    (hfp : (TwoFibreProductOver.lift qX qZ qY F G qW A B hA hB ψ hψ).IsEquivalence) :
    PredeformationFibreProductData iΛ qW qX qZ qY A B F G hA hB hF ψ w₀ hw₀
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.3, Tag 07T2](https://stacks.math.columbia.edu/tag/07T2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
