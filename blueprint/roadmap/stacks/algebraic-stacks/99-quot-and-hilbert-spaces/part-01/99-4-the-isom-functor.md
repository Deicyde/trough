---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.HomSituation.isomSubfunctor, AlgebraicGeometry.Space.HomSituation.isomFunctor, AlgebraicGeometry.Space.HomSituation.isSheafFor_isomFunctor_of_isFpqcCovering, AlgebraicGeometry.Space.HomSituation.bijective_isomMorOfSpaceIsom, AlgebraicGeometry.Space.HomSituation.isAffineFinitePresentationAlgebraicSpaceOver_isomFunctor_of_hasProperSupport
statement: formalized
proof: formalized
---

# 99.4 The Isom functor

Section 99.4 of the Stacks Project, [Tag 08K7](https://stacks.math.columbia.edu/tag/08K7). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08K7, the section

[Tag 08K7](https://stacks.math.columbia.edu/tag/08K7) in the Stacks Project.

**`AlgebraicGeometry.Space.HomSituation.isomSubfunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeIsom.lean, line 355](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeIsom.lean#L355). The attribute's comment: “the Isom functor as a subfunctor of the Hom functor”.

> **Stacks 08K7.**  The relative Isom functor `Isom(F, G) ⊆ Hom(F, G)` as a subfunctor of the
> relative Hom functor of Stacks 08JT: its sections at a test scheme `T` over the base are the
> invertible `𝒪_{X_T}`-homomorphisms `F_T ⟶ G_T`.
>
> It is a subfunctor because invertibility is stable under pullback,
> `AlgebraicGeometry.Space.HomSituation.isIsomAt_homMap`.  The ambient relative Hom functor is
> taken at the pseudofunctoriality of the direct images of Stacks 03LU,
> `AlgebraicGeometry.Space.modulePushforwardCoherence`.

```lean
def isomSubfunctor : Subfunctor (s.homFunctor (modulePushforwardCoherence B S hS))
```

**`AlgebraicGeometry.Space.HomSituation.isomFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeIsom.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeIsom.lean#L373). The attribute's comment: “the Isom functor”.

> **Stacks 08K7.**  The relative Isom functor `Isom(F, G) : (Sch/base)ᵒᵖ ⥤ Sets`, whose value
> at a test scheme `T` over the base is the set of invertible `𝒪_{X_T}`-homomorphisms
> `F_T ⟶ G_T` and whose action on a morphism of test schemes is pullback of homomorphisms.  Its
> inclusion into the relative Hom functor is `CategoryTheory.Subfunctor.ι`.

```lean
def isomFunctor : (s.SchemesOver)ᵒᵖ ⥤ Type (u + 1)
```

## Tag 08K8, a lemma

[Tag 08K8](https://stacks.math.columbia.edu/tag/08K8) in the Stacks Project.

**`AlgebraicGeometry.Space.HomSituation.isSheafFor_isomFunctor_of_isFpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeIsomFpqcSheaf.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeIsomFpqcSheaf.lean#L142). The attribute's comment: “the functor Isom(F, G) of Situation 08JT satisfies the sheaf property for every fpqc covering”.

> **Stacks 08K8.**  In Situation 08JT the relative Isom functor `Isom(F, G)` satisfies the
> sheaf property for the fpqc topology: for every fpqc covering `{U i ⟶ T}` of schemes over the
> base, every compatible family of invertible homomorphisms `F_{U i} ⟶ G_{U i}` has a unique
> amalgamation, an invertible homomorphism `F_T ⟶ G_T`.
>
> This is the proof of the source.  `Hom(F, G)` satisfies the sheaf property, Stacks 08JV in the
> form of `AlgebraicGeometry.Space.HomSituation.isSheafFor_homFunctor_of_isFpqcCovering`, so it
> remains that a homomorphism `F_T ⟶ G_T` whose base changes to the `U i` are isomorphisms is an
> isomorphism; the base changes `{X_{U i} ⟶ X_T}` form an fpqc covering of `X_T` by Stacks 03MR,
> and invertibility descends along it by Stacks 04W8,
> `AlgebraicGeometry.Space.reflectsIsoAlongFpqcCovering`, the base-changed modules being
> quasi-coherent by Stacks 03GA.

```lean
theorem isSheafFor_isomFunctor_of_isFpqcCovering {I : Type v} {T : s.SchemesOver}
    {U : I → s.SchemesOver} (g : ∀ i, U i ⟶ T)
    (hg : IsFpqcCovering B S hS fun i ↦ ((schemeSpaceFunctor B S hS).map (g i).left).hom) :
    Presieve.IsSheafFor s.isomFunctor (Presieve.ofArrows U g)
```

## Tag 0D3T, a lemma

[Tag 0D3T](https://stacks.math.columbia.edu/tag/0D3T) in the Stacks Project.

**`AlgebraicGeometry.Space.HomSituation.bijective_isomMorOfSpaceIsom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Hom/IsomFunctorMorphismsEquiv.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Hom/IsomFunctorMorphismsEquiv.lean#L67). The attribute's comment: “the whole identification, in Situation 08JT: for any algebraic space T over S, the map (h, u) |-> the morphism T -> Isom(F, G) is a bijection from all pairs of h : T -> base and an isomorphism u : F\_T -> G\_T of the pullbacks to X x\_\{base, h} T onto all morphisms from T into Isom(F, G); the pseudofunctoriality of direct images and both descent clauses are supplied by library results, so the statement takes no hypothesis”.

> Let `T` be an algebraic space over `S`. The assignment `(h, u) ↦ isomMorOfSpaceIsom (h, u)`
> is a bijection from the pairs of a morphism `h : T ⟶ base` and an isomorphism `u : F_T ⟶ G_T` of
> the modules pulled back to `X ×_{base, h} T` onto the morphisms of presheaves `T ⟶ Isom(F, G)` on
> the big fppf site of `S`:
>
> `Mor(T, Isom(F, G)) = {(h, u) | h : T ⟶ base, u : F_T ⟶ G_T an isomorphism}`.
>
> Here `Isom(F, G)` is the presheaf built from the pseudofunctoriality of direct images
> `AlgebraicGeometry.Space.modulePushforwardCoherence`.

```lean
theorem bijective_isomMorOfSpaceIsom (T : AlgebraicSpaces B S hS) :
    Function.Bijective (fun p : (Σ h : T ⟶ s.base,
        {u : s.spaceHomAt (Over.mk h) // s.IsIsomOverAt u}) =>
      s.isomMorOfSpaceIsom (modulePushforwardCoherence B S hS) p.1 p.2.1 p.2.2)
```

## Tag 08K9, a proposition

[Tag 08K9](https://stacks.math.columbia.edu/tag/08K9) in the Stacks Project.

**`AlgebraicGeometry.Space.HomSituation.isAffineFinitePresentationAlgebraicSpaceOver_isomFunctor_of_hasProperSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeIsomAffineFinitePresentation.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeIsomAffineFinitePresentation.lean#L56). The attribute's comment: “Isom(F, G) is an algebraic space affine of finite presentation over B, for f of finite presentation and F, G of finite presentation, flat over B, with support proper over B”.

> In Situation 08JT assume that `f : X ⟶ B` is of finite presentation and that `𝓕` and `𝒢`
> are finitely presented `𝒪_X`-modules, flat over `B`, with support proper over `B`. Then the
> functor `Isom(𝓕, 𝒢)` is an algebraic space affine of finite presentation over `B`.

```lean
theorem isAffineFinitePresentationAlgebraicSpaceOver_isomFunctor_of_hasProperSupport
    (s : HomSituation B S hS) (hfp : IsFinitePresentation B S hS s.f.hom)
    (hF : s.F.IsFinitePresentationOnSite) (hG : s.G.IsFinitePresentationOnSite)
    (hFflat : IsFlatOver B S hS s.X.2 s.f.hom s.F)
    (hGflat : IsFlatOver B S hS s.X.2 s.f.hom s.G)
    (hFsupp : HasProperSupport B S hS s.X.2 s.base.2 s.f.hom
      (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation B S hS hfp.1)
      ((SheafOfModules.toSheaf _).obj s.F))
    (hGsupp : HasProperSupport B S hS s.X.2 s.base.2 s.f.hom
      (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation B S hS hfp.1)
      ((SheafOfModules.toSheaf _).obj s.G)) :
    IsAffineFinitePresentationAlgebraicSpaceOver s.base s.isomFunctor
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 99.4, Tag 08K7](https://stacks.math.columbia.edu/tag/08K7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
