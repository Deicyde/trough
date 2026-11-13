---
declaration: section
origin: cited
lean: CategoryTheory.Functor.IsRepresentable, AlgebraicGeometry.AffineSpace.toSpecMvPolyIntEquiv, AlgebraicGeometry.AffineSpace.toSpecMvPolyIntEquiv_comp, AlgebraicGeometry.Covers, CategoryTheory.Presheaf.IsSheaf, CategoryTheory.Subfunctor, CategoryTheory.MorphismProperty.presheaf, AlgebraicGeometry.Space.isRepresentable_of_openCover
statement: formalized
proof: formalized
---

# 26.15 A representability criterion

Section 26.15 of the Stacks Project, [Tag 01JF](https://stacks.math.columbia.edu/tag/01JF). 5 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01JG, a definition

[Tag 01JG](https://stacks.math.columbia.edu/tag/01JG) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.IsRepresentable`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.IsRepresentable#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L323) (StacksFrontier): “representable presheaf, on any category; here the category of schemes”. References: EGA 0 (8.1.8); EGA 0 (19.0.1); SGA 3 I (1.1); SGA 3 IV (3.3.2); SGA 4 I (1.4.1).

## Tag 01JH, an example

[Tag 01JH](https://stacks.math.columbia.edu/tag/01JH) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.AffineSpace.toSpecMvPolyIntEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.AffineSpace.toSpecMvPolyIntEquiv#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 326](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L326) (StacksFrontier): “for `n = Unit`, `Spec ℤ[x]` represents `T ↦ Γ(T, 𝒪_T)`; the universal family is the image of `x`”. References: EGA I (3.3.15), “partial”; EGA IV (17.11.3), “base Spec ℤ”; SGA 1 II (4.8), “base Spec Z”.
- [`AlgebraicGeometry.AffineSpace.toSpecMvPolyIntEquiv_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.AffineSpace.toSpecMvPolyIntEquiv_comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 328](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L328) (StacksFrontier): “naturality of the identification in `T`”. References: EGA I (3.3.15), “partial”.

## Tag 01JI, a definition

[Tag 01JI](https://stacks.math.columbia.edu/tag/01JI) in the Stacks Project.

**`AlgebraicGeometry.Covers`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/FunctorOfPoints.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/FunctorOfPoints.lean#L68). The attribute's comment: “part (4): covering by subfunctors”.

> An indexed family of subfunctors covers a functor if each section belongs,
> after restriction to an indexed open covering, to the corresponding subfunctor.

```lean
public abbrev Covers {C : Type u} [Category.{v} C] (toTop : C ⥤ TopCat.{u'})
    (isOpenImmersion : MorphismProperty C) (F : Cᵒᵖ ⥤ Type w) {I : Type v'}
    (H : I → Subfunctor F) : Prop
```

Declarations registered for the tag:

- [`CategoryTheory.Presheaf.IsSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Presheaf.IsSheaf#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/FunctorOfPoints.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/FunctorOfPoints.lean#L49) (StacksFrontier): “part (1): Zariski sheaf property”. References: EGA 0 (3.1.2); EGA 0 (3.1.4); SGA 3 IV (4.3.1), “more general”; SGA 3 IV (4.3.18); SGA 4 II (2.1), “more general”; SGA 4 II (2.7); SGA 4 II (6.1); SGA 4 II (6.2); SGA 4 II (6.3.2), “partial”; SGA 4½ Arcata (1.2.3), “more general”; SGA 7 VI (3.1(a)), “partial”.
- [`CategoryTheory.Subfunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Subfunctor#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/FunctorOfPoints.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/FunctorOfPoints.lean#L61) (StacksFrontier): “part (2): subfunctors”. References: SGA 3 I (1.2); SGA 3 IV (4.1.1), “more general”.
- [`CategoryTheory.MorphismProperty.presheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.presheaf#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/FunctorOfPoints.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/FunctorOfPoints.lean#L62) (StacksFrontier): “part (3): representability by open immersions”.

## Tag 01JJ, a lemma

[Tag 01JJ](https://stacks.math.columbia.edu/tag/01JJ) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentable_of_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SiteGluing.lean, line 639](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SiteGluing.lean#L639). The attribute's comment: “big fppf site over a scheme”.

> **Stacks 01JJ for the big fppf site over `S`.** A sheaf on the big fppf site over `S`
> which admits a jointly locally surjective family of relatively representable open immersions
> from representable presheaves is representable, by an object of that site.
>
> This is the statement Mathlib's
> `AlgebraicGeometry.Scheme.LocalRepresentability.isRepresentable` does not give: Mathlib glues
> in `Scheme` with no size control, so its representing object need not satisfy the site's size
> cutoff. The hypothesis on the index type is one set-theoretic condition which makes the glued
> scheme an object of the site; an at most countable family satisfies it automatically, since
> uncountable cofinality of the cutoff is a field of `AlgebraicGeometry.BigFppfSite`. It is not
> the weakest such condition:
> `AlgebraicGeometry.Space.isRepresentable_of_openCover_of_contains` asks only that the glued
> scheme lie in the site, however that is established.

```lean
theorem isRepresentable_of_openCover (hι : #ι < B.cutoff.ord.cof)
    [HasCoproduct fun i => yoneda.obj (X i)]
    (hsurj : Presheaf.IsLocallySurjective (BigFppfOver.topology B S hS) (Sigma.desc f)) :
    G.obj.IsRepresentable
```

## Tag 01JK, a remark

[Tag 01JK](https://stacks.math.columbia.edu/tag/01JK) in the Stacks Project.

**`AlgebraicGeometry.lrsRepresentableByScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/MorphismsIntoGluing/RepresentableByScheme.lean, line 831](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/MorphismsIntoGluing/RepresentableByScheme.lean#L831).

> A Zariski sheaf on locally ringed spaces, covered by subfunctors represented
> by schemes and relatively represented by open immersions, is itself represented
> by a scheme.

```lean
public theorem lrsRepresentableByScheme
    (F : LocallyRingedSpace.{u}ᵒᵖ ⥤ Type u)
    (hF : Presheaf.IsSheaf lrsZariskiTopology F)
    {I : Type v} [Small.{u} I] (H : I → Subfunctor F)
    (hrep : ∀ i, ∃ S : Scheme.{u}, Nonempty ((H i).toFunctor.RepresentableBy
      S.toLocallyRingedSpace))
    (hopen : ∀ i, (MorphismProperty.presheaf
      lrsIsOpenImmersion.{u}) (H i).ι)
    (hcover : Covers LocallyRingedSpace.forgetToTop
      lrsIsOpenImmersion.{u} F H) :
    ∃ S : Scheme.{u}, Nonempty (F.RepresentableBy S.toLocallyRingedSpace)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 26.15, Tag 01JF](https://stacks.math.columbia.edu/tag/01JF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
