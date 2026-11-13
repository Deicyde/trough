---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isAlgebraicStack_pullbackStack, AlgebraicGeometry.Stack.isDeligneMumfordStack_pullbackStack, AlgebraicGeometry.Stack.pullbackStack_equivalenceOfSpace, AlgebraicGeometry.Stack.pullbackStack_representableBy, AlgebraicGeometry.Stack.ChangeOfBigSite.pullbackPseudofunctor, AlgebraicGeometry.Stack.ChangeOfBigSite.isEquivalence_mapFunctor_pullbackPseudofunctor, AlgebraicGeometry.Stack.hasChangeBigSitePresentation_of_isPullbackOfAlgebraicStack, AlgebraicGeometry.Stack.isPullbackOfAlgebraicStack_of_hasChangeBigSitePresentation
statement: formalized
proof: formalized
---

# 94.18 Change of big site

Section 94.18 of the Stacks Project, [Tag 04X1](https://stacks.math.columbia.edu/tag/04X1). 2 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04X2, a lemma

[Tag 04X2](https://stacks.math.columbia.edu/tag/04X2) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_pullbackStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBigSiteAlgebraicStack.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBigSiteAlgebraicStack.lean#L182). The attribute's comment: “part (3)”.

> **Stacks 04X2, part (3).** Let `B` be a big fppf site contained in a larger one `B'`, let `S`
> be a scheme of `B` and let `f` be the morphism of sites determined by the localized inclusion.
> The inverse image `f⁻¹𝒳` of an algebraic stack `𝒳` over the localized big fppf site of `S` is an
> algebraic stack over the enlarged localized big fppf site.

```lean
theorem isAlgebraicStack_pullbackStack {B B' : BigFppfSite.{u}}
    (h : IsContained (τ := .fppf) B B') (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val) :
    letI : 𝒳.val.p.IsFibered := 𝒳.isFiberedInGroupoids.isFibered
    IsAlgebraicStack.{u, w} B' S (largerContains h hS) (pullbackStack h S hS 𝒳.val)
```

**`AlgebraicGeometry.Stack.isDeligneMumfordStack_pullbackStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBigSiteAlgebraicStack.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBigSiteAlgebraicStack.lean#L217). The attribute's comment: “part (4)”.

> **Stacks 04X2, part (4).** Let `B` be a big fppf site contained in a larger one `B'`, let `S`
> be a scheme of `B` and let `f` be the morphism of sites determined by the localized inclusion.
> The inverse image `f⁻¹𝒳` of a Deligne-Mumford stack `𝒳` over the localized big fppf site of `S`
> is a Deligne-Mumford stack over the enlarged localized big fppf site.
> The inverse image is a stackification, whose morphisms are not small, so the conclusion is read
> with `AlgebraicGeometry.Stack.IsDeligneMumfordStackUniv`, the definition of Stacks 03YO for a
> total category in arbitrary universes.
>
> The source's route: a surjective étale atlas of `𝒳` presents it as the quotient stack `[U/R]` of a
> groupoid whose source map is étale (Stacks 04T5, and Stacks 04XC at étaleness), the inverse image
> of that groupoid has étale source map, `f⁻¹[U/R] = [f⁻¹U/f⁻¹R]` (Stacks 04WX), and the quotient
> stack of a groupoid in algebraic spaces with étale source map is presented étale-ly by a scheme
> atlas of its object space followed by the canonical projection (Stacks 04X0 at étaleness).

```lean
theorem isDeligneMumfordStack_pullbackStack {B B' : BigFppfSite.{u}}
    (h : IsContained (τ := .fppf) B B') (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h𝒳 : IsDeligneMumfordStack.{u, w} B S hS 𝒳.val) :
    letI : 𝒳.val.p.IsFibered := 𝒳.isFiberedInGroupoids.isFibered
    IsDeligneMumfordStackUniv.{u, w} B' S (largerContains h hS) (pullbackStack h S hS 𝒳.val)
```

**`AlgebraicGeometry.Stack.pullbackStack_equivalenceOfSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBigSiteRepresentableStack.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBigSiteRepresentableStack.lean#L256). The attribute's comment: “representability by an algebraic space: the inverse image of a stack represented by an algebraic space is represented by the inverse image of that same algebraic space”.

> **Stacks 04X2, representability by an algebraic space.** A stack over the localized big fppf
> site of `S` represented by an algebraic space `F` has inverse image represented by the inverse
> image of `F`, that is by `AlgebraicGeometry.changeBigSite` applied to `F`.

```lean
theorem pullbackStack_equivalenceOfSpace (S : Scheme.{u}) (hS : B.Contains S)
    (F : AlgebraicSpaces B S hS) (𝒳 : BasedCategory.{u, u + 1} (BigFppfOver B S hS))
    (e : StacksRepresentableCFG.EquivalenceOver 𝒳.p
      (presheafOfCategories (F.obj ⋙ typeToCat)).p) :
    letI : 𝒳.p.IsFibered :=
      (StacksRepresentableCFG.isFiberedInGroupoids_of_equivalenceOver e
        (fibredCategory B S hS F.obj).property).isFibered
    Nonempty (StacksRepresentableCFG.EquivalenceOver (pullbackStack h S hS 𝒳).p
      (presheafOfCategories
        (((changeBigSite B B' h S hS).obj F).obj ⋙ typeToCat)).p)
```

**`AlgebraicGeometry.Stack.pullbackStack_representableBy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBigSiteRepresentableStack.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBigSiteRepresentableStack.lean#L289). The attribute's comment: “representability by a scheme: the inverse image of a stack represented by a scheme of the smaller big fppf site is represented by that same scheme, read in the larger one”.

> **Stacks 04X2, representability by a scheme.** A stack over the localized big fppf site of `S`
> represented by a scheme `X` of the smaller site has inverse image represented by the *same*
> scheme, read as an object of the larger localized site.

```lean
theorem pullbackStack_representableBy (S : Scheme.{u}) (hS : B.Contains S)
    (X : BigFppfOver B S hS) (𝒳 : BasedCategory.{u, u + 1} (BigFppfOver B S hS))
    (e : StacksRepresentableCFG.RepresentableBy 𝒳.p X) :
    letI : 𝒳.p.IsFibered :=
      (StacksRepresentableCFG.isFiberedInGroupoids_of_equivalenceOver e
        (Functor.IsFiberedInGroupoids.over_forget X)).isFibered
    Nonempty (StacksRepresentableCFG.RepresentableBy (pullbackStack h S hS 𝒳).p
      ((inclusionOver h S hS).obj X : BigFppfOver B' S (largerContains h hS)))
```

## Tag 04X3, a lemma

[Tag 04X3](https://stacks.math.columbia.edu/tag/04X3) in the Stacks Project.

**`AlgebraicGeometry.Stack.ChangeOfBigSite.pullbackPseudofunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBigSitePseudofunctor.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBigSitePseudofunctor.lean#L287). The attribute's comment: “the functor of 2-categories”.

> **The 2-functor `𝒳 ↦ f⁻¹𝒳`** from the algebraic stacks over `S` for the smaller big fppf site
> to those for the larger one. Its value at `𝒳` is `pullbackObj`, equivalent over the larger site to
> the inverse image `AlgebraicGeometry.Stack.pullbackStack` of Stacks 04X2
> (`pullbackObjEquivalenceOver`), and its value at a 1-morphism `g : 𝒳 ⟶ 𝒴` is the 1-morphism
> `f⁻¹𝒳 ⟶ f⁻¹𝒴` through which `𝒳 ⟶ 𝒴 ⥤ f⁻¹𝒴` factors by the universal property of `𝒳 ⥤ f⁻¹𝒳`.

```lean
noncomputable def pullbackPseudofunctor :
    AlgebraicStacks.{u, w} B S hS ⥤ᵖ AlgebraicStacks.{u, w} B' S (largerContains h hS)
```

**`AlgebraicGeometry.Stack.ChangeOfBigSite.isEquivalence_mapFunctor_pullbackPseudofunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBigSitePseudofunctor.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBigSitePseudofunctor.lean#L299). The attribute's comment: “the equivalences of morphism categories”.

> **The 2-functor `𝒳 ↦ f⁻¹𝒳` induces equivalences of morphism categories**
> `Mor(𝒳, 𝒴) ≌ Mor(f⁻¹𝒳, f⁻¹𝒴)`.

```lean
theorem isEquivalence_mapFunctor_pullbackPseudofunctor (𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS) :
    ((pullbackPseudofunctor h S hS).mapFunctor 𝒳 𝒴).IsEquivalence
```

**`AlgebraicGeometry.Stack.hasChangeBigSitePresentation_of_isPullbackOfAlgebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBigSiteStackEssentialImage.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBigSiteStackEssentialImage.lean#L205). The attribute's comment: “the characterization of the essential image, 'only if' half: a category over the enlarged localized big fppf site equivalent to the inverse image of an algebraic stack over the smaller one has a presentation by the inverse image of a smooth groupoid in algebraic spaces over the smaller site”.

> **Stacks 04X3, the "only if" half of the characterization of the essential image.** If `𝒳'`
> is equivalent over the enlarged localized big fppf site to the inverse image of an algebraic stack
> `𝒳` over the smaller site, then `𝒳'` has a presentation `[U'/R']` with `U'`, `R'` the inverse
> images of `U`, `R`.
>
> Stacks 04T5 presents `𝒳` as the quotient stack `[U/R]` of a smooth groupoid, Stacks 04WX
> identifies `f⁻¹[U/R]` with `[f⁻¹U / f⁻¹R]`, the inverse image of an equivalence over the
> smaller site is an equivalence over the enlarged one, and the inverse image of a smooth groupoid
> is smooth. The presentation is the inverse-image groupoid itself, with the identity morphism.

```lean
theorem hasChangeBigSitePresentation_of_isPullbackOfAlgebraicStack
    (𝒳' : BasedCategory.{v, t} (BigFppfOver B' S (largerContains h hS)))
    (h𝒳' : IsPullbackOfAlgebraicStack.{u, w} h S hS 𝒳') :
    HasChangeBigSitePresentation h S hS 𝒳'
```

**`AlgebraicGeometry.Stack.isPullbackOfAlgebraicStack_of_hasChangeBigSitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBigSiteStackEssentialImage.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBigSiteStackEssentialImage.lean#L240). The attribute's comment: “the characterization of the essential image, 'if' half: a category over the enlarged localized big fppf site with a presentation by the inverse image of a smooth groupoid in algebraic spaces over the smaller site is equivalent to the inverse image of an algebraic stack over the smaller site”.

> **Stacks 04X3, the "if" half of the characterization of the essential image.** If `𝒳'` has a
> presentation `[U'/R']` with `U'`, `R'` the inverse images of `U`, `R`, then `𝒳'` is equivalent
> over the enlarged localized big fppf site to the inverse image of an algebraic stack over the
> smaller site.
>
> The isomorphism `G' ≅ f⁻¹G` identifies the quotient stacks (Stacks 046T) and makes `f⁻¹G` smooth;
> smoothness then descends to `G`
> (`AlgebraicGeometry.isSmooth_of_changeBigSiteGroupoid_isSmooth`). The quotient stack of `G` is
> an algebraic stack by Stacks 04TK; its small model
> `AlgebraicGeometry.Stack.AlgebraicStacks.smallModel` is an object of the 2-category of Stacks 03YP
> equivalent to it over the site; and Stacks 04WX identifies the inverse image of the quotient stack
> with the quotient stack of the inverse image.

```lean
theorem isPullbackOfAlgebraicStack_of_hasChangeBigSitePresentation
    (𝒳' : BasedCategory.{v, t} (BigFppfOver B' S (largerContains h hS)))
    (h𝒳' : HasChangeBigSitePresentation h S hS 𝒳') :
    IsPullbackOfAlgebraicStack.{u, w} h S hS 𝒳'
```

**`AlgebraicGeometry.Stack.isPullbackOfAlgebraicStack_iff_hasChangeBigSitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBigSiteStackEssentialImage.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBigSiteStackEssentialImage.lean#L264). The attribute's comment: “the characterization of the essential image”.

> **Stacks 04X3, the characterization of the essential image.** A category `𝒳'` over the
> enlarged localized big fppf site is equivalent to the inverse image `f⁻¹𝒳` of an algebraic stack
> `𝒳` over the smaller site if and only if it has a presentation `[U'/R']` with `U'`, `R'` the
> inverse images of `U`, `R` for a groupoid `(U, R, s, t, c)` in algebraic spaces over the smaller
> site.

```lean
theorem isPullbackOfAlgebraicStack_iff_hasChangeBigSitePresentation
    (𝒳' : BasedCategory.{v, t} (BigFppfOver B' S (largerContains h hS))) :
    IsPullbackOfAlgebraicStack.{u, w} h S hS 𝒳' ↔ HasChangeBigSitePresentation h S hS 𝒳'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 94.18, Tag 04X1](https://stacks.math.columbia.edu/tag/04X1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
