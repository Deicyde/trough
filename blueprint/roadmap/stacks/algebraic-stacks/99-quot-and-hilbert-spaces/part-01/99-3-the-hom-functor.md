---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.HomSituation.homSchemeFunctor, AlgebraicGeometry.Space.HomSituation.homSchemeFunctor_obj, AlgebraicGeometry.Space.HomSituation.homSchemeFunctor_map, AlgebraicGeometry.Space.HomSituation.homOverSpaceFunctor, AlgebraicGeometry.Space.HomSituation, AlgebraicGeometry.Space.HomSituation.existsUnique_homMap_of_restrictionsAgree, AlgebraicGeometry.Space.HomSituation.isSheafFor_homFunctor, AlgebraicGeometry.Space.HomSituation.isSheaf_homFunctor_fpqc
statement: formalized
proof: formalized
---

# 99.3 The Hom functor

Section 99.3 of the Stacks Project, [Tag 08JS](https://stacks.math.columbia.edu/tag/08JS). 10 tags here are carried by 26 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08JT, a situation

[Tag 08JT](https://stacks.math.columbia.edu/tag/08JT) in the Stacks Project.

**`AlgebraicGeometry.Space.HomSituation.homSchemeFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Hom/HomFunctorEtaleDescent.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Hom/HomFunctorEtaleDescent.lean#L214). The attribute's comment: “the Hom functor on the schemes over the base”.

> **Stacks 08JT.**  The relative Hom functor `Hom(F, G) : (Sch/base)ᵒᵖ ⥤ Sets`: its value at a
> test scheme `T` over the base is `Hom_{𝒪_{X_T}}(F_T, G_T)`, the homomorphisms of the two modules
> pulled back to `X_T = X ×_{base} T`, and its action on a morphism of test schemes is pullback of
> homomorphisms.  It is `AlgebraicGeometry.Space.HomSituation.homOverSpaceFunctor` restricted to
> the test schemes over the base; the pseudofunctoriality of the direct images of Stacks 03LU that
> makes it a functor is `AlgebraicGeometry.Space.modulePushforwardCoherence`.

```lean
def homSchemeFunctor : (s.SchemesOver)ᵒᵖ ⥤ Type (u + 1)
```

**`AlgebraicGeometry.Space.HomSituation.homSchemeFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Hom/HomFunctorEtaleDescent.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Hom/HomFunctorEtaleDescent.lean#L220). The attribute's comment: “the value of the Hom functor at a scheme over the base”.

> **Stacks 08JT.**  The value of the relative Hom functor at a test scheme `T` over the base
> is the set of `𝒪_{X_T}`-module homomorphisms `F_T ⟶ G_T`.

```lean
theorem homSchemeFunctor_obj (T : s.SchemesOver) :
    s.homSchemeFunctor.obj (Opposite.op T) = s.homAt T
```

**`AlgebraicGeometry.Space.HomSituation.homSchemeFunctor_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Hom/HomFunctorEtaleDescent.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Hom/HomFunctorEtaleDescent.lean#L227). The attribute's comment: “the action of the Hom functor on a morphism of schemes over the base”.

> **Stacks 08JT.**  The action of the relative Hom functor on a morphism of test schemes is
> pullback of homomorphisms.

```lean
theorem homSchemeFunctor_map {U T : s.SchemesOver} (g : U ⟶ T) :
    s.homSchemeFunctor.map (Opposite.op g) = TypeCat.ofHom (s.homMap g)
```

**`AlgebraicGeometry.Space.HomSituation.homOverSpaceFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Hom/HomFunctorMorphisms.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Hom/HomFunctorMorphisms.lean#L307). The attribute's comment: “the Hom functor indexed by the algebraic spaces over the base”.

> **The relative Hom functor of Stacks 08JT, indexed by the algebraic spaces over the
> base.**  Its value at `T ⟶ base` is `Hom_{𝒪_{X_T}}(F_T, G_T)` and its action is pullback of
> homomorphisms.  The relative Hom functor on the test *schemes* over the base is this one
> restricted along the inclusion of those into the algebraic spaces over the base.
>
> The pseudofunctoriality of the direct images of Stacks 03LU, which makes pullback of
> homomorphisms functorial, is supplied by `AlgebraicGeometry.Space.modulePushforwardCoherence`
> and so is not a hypothesis.

```lean
def homOverSpaceFunctor : (Over s.base)ᵒᵖ ⥤ Type (u + 1)
```

**`AlgebraicGeometry.Space.HomSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeHom.lean, line 464](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeHom.lean#L464). The attribute's comment: “the standing data”.

> **Stacks 08JT.**  The standing data of the relative Hom functor: a morphism `f : X ⟶ base`
> of algebraic spaces over `S` and two quasi-coherent `𝒪_X`-modules.

```lean
structure HomSituation (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
```

## Tag 08JV, a lemma

[Tag 08JV](https://stacks.math.columbia.edu/tag/08JV) in the Stacks Project.

**`AlgebraicGeometry.Space.HomSituation.existsUnique_homMap_of_restrictionsAgree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeHomFpqcDescent.lean, line 493](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeHomFpqcDescent.lean#L493). The attribute's comment: “the sheaf property elementwise, for an fpqc covering of test schemes; the same property as CategoryTheory.Presieve.IsSheafFor is isSheafFor\_homFunctor”.

> **Stacks 08JV.**  In the standing data of Stacks 08JT the relative Hom functor
> `Hom(F, G)` satisfies the sheaf property for the fpqc topology: for an fpqc covering
> `{U i ⟶ T}` of test schemes over the base, a family of homomorphisms `F_{U i} ⟶ G_{U i}` whose
> restrictions agree on the overlaps `X_{U i} ×_{X_T} X_{U j}` comes from a unique
> homomorphism `F_T ⟶ G_T`.
>
> This is the proof of the source.  The base changes `{X_{U i} ⟶ X_T}` form an fpqc covering of
> `X_T` by Stacks 03MR, part (3), in the form of
> `AlgebraicGeometry.Space.isFpqcCovering_baseChangeMap`, and a compatible family of
> homomorphisms of the inverse images of two quasi-coherent modules along an fpqc covering glues
> uniquely, which is the gluing half of Stacks 04W8,
> `AlgebraicGeometry.Space.existsUnique_restrictPullbackHom_eq_of_isFpqcCovering`.  The
> base-changed modules `F_T`,
> `G_T` are quasi-coherent by Stacks 03GA,
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePullback_of_isQuasicoherentOnSite`.

```lean
theorem existsUnique_homMap_of_restrictionsAgree
    {I : Type v} {T : s.SchemesOver} {U : I → s.SchemesOver} (g : ∀ i, U i ⟶ T)
    (hg : IsFpqcCovering B S hS fun i ↦ ((schemeSpaceFunctor B S hS).map (g i).left).hom)
    (α : ∀ i, s.homAt (U i))
    (hα : RestrictionsAgree (s.projection T) (fun i ↦ baseChangeMap s.f (g i))
      (fun i ↦ s.projection (U i)) (fun i ↦ baseChangeMap_comp_projection s.f (g i))
      (fun i ↦ s.toModuleHom (α i))) :
    ∃! β : s.homAt T, ∀ i, s.homMap (g i) β = α i
```

**`AlgebraicGeometry.Space.HomSituation.isSheafFor_homFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeHomFpqcDescent.lean, line 670](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeHomFpqcDescent.lean#L670). The attribute's comment: “the sheaf property for the presieve of an fpqc covering of test schemes”.

> **Stacks 08JV, as the sheaf condition for a presieve.**  In the standing data of
> Stacks 08JT the relative Hom functor `Hom(F, G)` is a sheaf for the presieve generated by an
> fpqc covering `{U i ⟶ T}` of test schemes over the base: every compatible family of sections
> has a unique amalgamation.
>
> This is `AlgebraicGeometry.Space.HomSituation.existsUnique_homMap_of_restrictionsAgree` with
> the compatibility of the family transported to the overlaps `X_{U i} ×_{X_T} X_{U j}` of the
> base changes.  That transport is the content added here: the overlap `U i ×_T U j` of two test
> schemes is again a test scheme, so a compatible family restricts compatibly to it, and the
> fibre product of the two base changes maps to the base change of that overlap by
> `AlgebraicGeometry.Space.HomSituation.overlapTestComparison`, which carries the two projections
> of the fibre product to the base changes of the two projections of the overlap.
>
> This is the form of the sheaf property that Stacks 08K8 consumes, as the hypothesis `hHom` of
> `AlgebraicGeometry.Space.HomSituation.isSheafFor_isomFunctor`.

```lean
theorem isSheafFor_homFunctor (hc : ModulePushforwardCoherence B S hS)
    {I : Type v} {T : s.SchemesOver} {U : I → s.SchemesOver} (g : ∀ i, U i ⟶ T)
    (hg : IsFpqcCovering B S hS fun i ↦ ((schemeSpaceFunctor B S hS).map (g i).left).hom) :
    Presieve.IsSheafFor (s.homFunctor hc) (Presieve.ofArrows U g)
```

**`AlgebraicGeometry.Space.HomSituation.isSheaf_homFunctor_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeHomFpqcSheaf.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeHomFpqcSheaf.lean#L52).

> **Stacks 08JV.**  In Situation 08JT the relative Hom functor `Hom(F, G)`, sending a scheme
> `T` over the base to `Hom_{𝒪_{X_T}}(F_T, G_T)`, satisfies the sheaf property for the fpqc
> topology on the schemes over the base.
>
> Its functoriality is the pseudofunctoriality of Stacks 03LU, which is
> `AlgebraicGeometry.Space.modulePushforwardCoherence`, proved with no hypothesis.

```lean
theorem isSheaf_homFunctor_fpqc :
    Presheaf.IsSheaf (fpqcTopology s.base) (s.homFunctor (modulePushforwardCoherence B S hS))
```

## Tag 0D3S, a lemma

[Tag 0D3S](https://stacks.math.columbia.edu/tag/0D3S) in the Stacks Project.

**`AlgebraicGeometry.Space.HomSituation.bijective_morOfSpaceHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Hom/HomFunctorEtaleDescent.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Hom/HomFunctorEtaleDescent.lean#L169). The attribute's comment: “Mor(T, Hom(F, G)) = \{(h, u)}: the construction (h, u) ↦ (a ↦ (h ∘ a, a^*u)) is a bijection from the pairs onto the morphisms T ⟶ Hom(F, G), for every algebraic space T”.

> For an algebraic space `T` over `S`, the morphisms of sheaves `T ⟶ Hom(F, G)` are the pairs
> `(h, u)` of a morphism `h : T ⟶ base` and a homomorphism `u : F_T ⟶ G_T` of the two modules pulled
> back to `X ×_{base, h} T`: the construction `(h, u) ↦ (a ↦ (h ∘ a, a^*u))`, which is
> `AlgebraicGeometry.Space.HomSituation.morOfSpaceHom`, is a bijection.

```lean
theorem bijective_morOfSpaceHom (T : AlgebraicSpaces B S hS) :
    Function.Bijective (s.morOfSpaceHom (modulePushforwardCoherence B S hS) (T := T))
```

## Tag 08JW, a remark

[Tag 08JW](https://stacks.math.columbia.edu/tag/08JW) in the Stacks Project.

**`AlgebraicGeometry.Space.HomSituation.baseChangedSituation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeHom.lean, line 652](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeHom.lean#L652). The attribute's comment: “the base-changed situation”.

> **Stacks 08JW.**  The relative Hom situation obtained by changing the base algebraic space
> along `p : base' ⟶ base`: its source is `X' = X ×_base base'`, its morphism the second
> projection, and its two modules the pullbacks of `F` and `G` along the first projection.

```lean
def baseChangedSituation : HomSituation B S hS
```

**`AlgebraicGeometry.Space.HomSituation.homFunctorBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeHom.lean, line 727](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeHom.lean#L727). The attribute's comment: “the identification Hom(F',G')(T) = Hom(F,G)(T), natural in T”.

> **Stacks 08JW.**  For a test scheme `T` over `base'` the two relative Hom sets agree:
> `Hom(F', G')(T) = Hom(F, G)(T)`, where on the right `T` is read as a scheme over `base`
> through `T ⟶ base' ⟶ base`.  The identification is natural in `T`, so it is an isomorphism of
> the two relative Hom functors.
>
> It has no hypotheses.  The coherence data for the direct images, which the Hom functor of
> either situation is formed from, is `AlgebraicGeometry.Space.modulePushforwardCoherence`, and
> the quasi-coherence of the two pullbacks, which forming the base-changed situation needs, is
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePullback_of_isQuasicoherentOnSite`.

```lean
def homFunctorBaseChange :
    (s.baseChangedSituation p).homFunctor (modulePushforwardCoherence B S hS) ≅
      (CostructuredArrow.map p).op ⋙ s.homFunctor (modulePushforwardCoherence B S hS)
```

## Tag 08K3, a lemma

[Tag 08K3](https://stacks.math.columbia.edu/tag/08K3) in the Stacks Project.

**`AlgebraicGeometry.Space.HomSituation.tripleRestrictionsAgree_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeHomFpqcDescent.lean, line 1033](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeHomFpqcDescent.lean#L1033). The attribute's comment: “the two parallel arrows agree on the image of the first arrow”.

> **Stacks 08K3, the first half of the exactness.**  The restrictions of a global
> homomorphism `F_T ⟶ G_T` to the base changes `X_{i, T}` of the members of a covering of the
> source satisfy the overlap condition: the two parallel arrows of the diagram agree on the image
> of the first arrow.
>
> Both restrictions are the restriction of the global homomorphism along the projection
> `X_{ijk, T} ⟶ X_T`, because both parallel arrows are morphisms over `X_T`.

```lean
theorem tripleRestrictionsAgree_restrict (β : s.homAt T) :
    s.TripleRestrictionsAgree a T b
      (fun i ↦ restrictPullbackHom (s.memberInclusion a T i) (s.memberInclusion_comp a T i)
        (s.toModuleHom β))
```

**`AlgebraicGeometry.Space.HomSituation.existsUnique_sourceHom_of_tripleRestrictionsAgree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeHomFpqcDescent.lean, line 1072](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeHomFpqcDescent.lean#L1072). The attribute's comment: “the first arrow is injective with image the equalizer of the other two”.

> **Stacks 08K3, the second half of the exactness.**  In the standing data of Stacks 08JT let
> `{X_i ⟶ X}` be an fppf covering and for all `i`, `j` let `{X_{ijk} ⟶ X_i ×_X X_j}` be an fppf
> covering.  For every test scheme `T` over the base, a family of homomorphisms
> `F_i ⟶ G_i` over the base changes `X_{i, T}` whose restrictions agree on the `X_{ijk, T}` comes
> from a unique homomorphism `F_T ⟶ G_T`.
>
> Together with `AlgebraicGeometry.Space.HomSituation.tripleRestrictionsAgree_restrict` this is
> the exactness of the diagram displayed by the source: the first arrow lands in the equalizer of
> the other two, is injective, and hits every element of that equalizer.
>
> This is the proof of the source.  The base change of an fppf covering is an fppf covering, so
> `{X_{i, T} ⟶ X_T}` and `{X_{ijk, T} ⟶ X_{i, T} ×_{X_T} X_{j, T}}` are fppf, hence fpqc,
> coverings — Stacks 03Y9 and Stacks 03MR, part (3).  Applying Stacks 04W8 to the second reduces
> the overlap condition to the overlaps themselves, and applying it to the first, in the form
> `AlgebraicGeometry.Space.existsUnique_restrictPullbackHom_eq_of_isFpqcCovering`, produces the
> unique global
> homomorphism.  The base-changed modules `F_T`, `G_T` are quasi-coherent by Stacks 03GA,
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePullback_of_isQuasicoherentOnSite`.

```lean
theorem existsUnique_sourceHom_of_tripleRestrictionsAgree
    (hrepr : QuasiCoherentDescent.ReprFpqcHomInjective.{u, v} B S hS)
    (ha : IsFppfCovering B S hS (fun i ↦ (Xi i).1) fun i ↦ (a i).hom)
    (hb : ∀ i j, IsFppfCovering B S hS (fun k ↦ (Xijk i j k).1) fun k ↦ (b i j k).hom)
    (α : ∀ i, (modulePullback B S hS (s.memberToSource a T i)).obj s.F ⟶
      (modulePullback B S hS (s.memberToSource a T i)).obj s.G)
    (hα : s.TripleRestrictionsAgree a T b α) :
    ∃! β : s.homAt T, ∀ i, restrictPullbackHom (s.memberInclusion a T i)
      (s.memberInclusion_comp a T i) (s.toModuleHom β) = α i
```

**`AlgebraicGeometry.Space.HomSituation.tripleRestrictionsAgree_iff_existsUnique_sourceHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeHomFpqcGluing.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeHomFpqcGluing.lean#L86).

> **Stacks 08K3.**  In Situation 08JT let `{X_i ⟶ X}` be an fppf covering and for all `i`, `j`
> let `{X_{ijk} ⟶ X_i ×_X X_j}` be an fppf covering, and write `F_i`, `G_i`, `F_{ijk}`,
> `G_{ijk}` for the pullbacks of `F` and `G`.  For every scheme `T` over the base, the diagram
> `Hom(F, G)(T) ⟶ ∏_i Hom(F_i, G_i)(T) ⇉ ∏_{ijk} Hom(F_{ijk}, G_{ijk})(T)` presents the first
> arrow as the equalizer of the other two: a family `(α i)` of homomorphisms over the base
> changes `X_{i, T}` is taken to the same element by the two parallel arrows exactly when it is
> the image of a unique `β : F_T ⟶ G_T`.
>
> The backward direction says that the first arrow lands in the equalizer; together with it the
> forward direction says that the first arrow is injective and its image is the equalizer.
>
> This is the proof of the source.  The base changes `{X_{i, T} ⟶ X_T}` and
> `{X_{ijk, T} ⟶ X_{i, T} ×_{X_T} X_{j, T}}` are fppf, hence fpqc, coverings (Stacks 03Y9);
> Stacks 04W8 applied to the second, in the form of its faithfulness half, reduces the condition
> to the overlaps themselves, and applied to the first, in the form
> `AlgebraicGeometry.Space.gluesModuleHomAlongFpqcCovering`, produces the unique global
> homomorphism.  The base-changed modules `F_T`, `G_T` are quasi-coherent by Stacks 03GA.

```lean
theorem tripleRestrictionsAgree_iff_existsUnique_sourceHom
    (ha : IsFppfCovering B S hS (fun i ↦ (Xi i).1) fun i ↦ (a i).hom)
    (hb : ∀ i j, IsFppfCovering B S hS (fun k ↦ (Xijk i j k).1) fun k ↦ (b i j k).hom)
    (α : ∀ i, (modulePullback B S hS (s.memberToSource a T i)).obj s.F ⟶
      (modulePullback B S hS (s.memberToSource a T i)).obj s.G) :
    s.TripleRestrictionsAgree a T b α ↔
      ∃! β : s.homAt T, ∀ i, restrictPullbackHom (s.memberInclusion a T i)
        (s.memberInclusion_comp a T i) (s.toModuleHom β) = α i
```

## Tag 08K4, a lemma

[Tag 08K4](https://stacks.math.columbia.edu/tag/08K4) in the Stacks Project.

**`AlgebraicGeometry.Space.HomSituation.isLimitPreservingHom_of_isEqualizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeHomLimitPreserving.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeHomLimitPreserving.lean#L247). The attribute's comment: “reduced to the equalizer presentation of Stacks 08K3; that presentation and the affine case, Stacks 05LI, are not proved”.

> **Stacks 08K4, reduced to an equalizer presentation of the relative Hom functor.**  The
> relative Hom functor of Stacks 08JT is limit preserving as soon as it is cut out, at every test
> scheme over the base, as the equalizer of two maps between limit-preserving presheaves.
>
> Stacks 08K3 supplies such a presentation from an affine scheme surjective and étale over the
> source and an affine scheme surjective and étale over its self-overlap, which exist because the
> structure morphism is quasi-compact and quasi-separated (Stacks 03H6), the two presheaves being
> the relative Hom functors of those charts; their limit preservation is the affine case, which is
> Stacks 05LI.  Neither the presentation nor the affine case is proved here, so both are asked for
> as data; accordingly the three hypotheses of Stacks 08K4 are not used.

```lean
theorem isLimitPreservingHom_of_isEqualizer (hc : ModulePushforwardCoherence B S hS)
    (s : HomSituation B S hS) {Q R : (s.SchemesOver)ᵒᵖ ⥤ Type (u + 1)}
    (a : s.homFunctor hc ⟶ Q) (b₁ b₂ : Q ⟶ R)
    (hinj : ∀ T, Function.Injective (a.app T))
    (hequalizes : ∀ (T : (s.SchemesOver)ᵒᵖ) (α : (s.homFunctor hc).obj T),
      b₁.app T (a.app T α) = b₂.app T (a.app T α))
    (hlift : ∀ (T : (s.SchemesOver)ᵒᵖ) (q : Q.obj T),
      b₁.app T q = b₂.app T q → ∃ α, a.app T α = q)
    (hQ : LimitPreserving.{u, u + 1, w, w', u + 1} s.testSchemeFunctor Q)
    (hR : LimitPreserving.{u, u + 1, w, w', u + 1} s.testSchemeFunctor R) :
    IsLimitPreservingHom.{u, w, w'} hc s
```

**`AlgebraicGeometry.Space.HomSituation.limitPreserving_homFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeHomLimitPreservingUnconditional.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeHomLimitPreservingUnconditional.lean#L134).

> **Stacks 08K4.**  In Situation 08JT, if `F` is of finite presentation and `f` is
> quasi-compact and quasi-separated, then the relative Hom functor `Hom(F, G)` is limit
> preserving: for every directed limit `T = lim T_i` of affine schemes over the base,
> `Hom(F, G)(T) = colim Hom(F, G)(T_i)`.

```lean
theorem limitPreserving_homFunctor (s : HomSituation B S hS)
    (hF : s.F.IsFinitePresentationOnSite) (hqc : IsQuasiCompact B S hS s.f.hom)
    (hqs : IsQuasiSeparated B S hS s.f.hom) :
    LimitPreserving.{u, u + 1, u, u} s.testSchemeFunctor
      (s.homFunctor (modulePushforwardCoherence B S hS))
```

## Tag 08K5, a lemma

[Tag 08K5](https://stacks.math.columbia.edu/tag/08K5) in the Stacks Project.

**`AlgebraicGeometry.Space.homFunctorClosedImmersionIso_of_isQuasicoherentOnSite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeHomClosedImmersionUnconditional.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeHomClosedImmersionUnconditional.lean#L90). The attribute's comment: “The whole statement, under exactly the source's hypotheses.”.

> **Stacks 08K5.**  Let `i : X' ⟶ X` be a closed immersion of algebraic spaces over an
> algebraic space `Y` over `S`, let `F` be a quasi-coherent `𝒪_X`-module and let `G'` be a
> quasi-coherent `𝒪_{X'}`-module.  Then
>
> `Hom(F, i_*G') = Hom(i^*F, G')`
>
> as functors on the test schemes over `Y`: the relative Hom functor of Stacks 08JT of the
> situation `(X ⟶ Y, F, i_*G')` is isomorphic to the one of the situation `(X' ⟶ Y, i^*F, G')`,
> both formed with the pseudofunctoriality `AlgebraicGeometry.Space.modulePushforwardCoherence`
> of Stacks 03LU.
>
> The two situations are formed with the quasi-coherence of `i_*G'` (Stacks 03M9) and of `i^*F`
> (Stacks 03GA), and the comparison is bijective by the base-change clause of Stacks 07U8 for
> the affine morphism `i`.

```lean
def homFunctorClosedImmersionIso_of_isQuasicoherentOnSite (p : X ⟶ Y) (i : X' ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (G' : Modules.{u, u} B S hS X'.1 X'.2) (hF : F.IsQuasicoherentOnSite)
    (hG' : G'.IsQuasicoherentOnSite) :
    (pushforwardHomSituation p i F G' hF
        (isQuasicoherentOnSite_modulePushforward_of_isClosedImmersion B S hS i hi G'
          hG')).homFunctor (modulePushforwardCoherence B S hS) ≅
      (pullbackHomSituation p i F G'
        (isQuasicoherentOnSite_modulePullback_of_isClosedImmersion B S hS i hi F hF)
        hG').homFunctor (modulePushforwardCoherence B S hS)
```

## Tag 08JX, a lemma

[Tag 08JX](https://stacks.math.columbia.edu/tag/08JX) in the Stacks Project.

**`AlgebraicGeometry.Space.isAffineFinitePresentationAlgebraicSpaceOver_degreeZeroSectionsFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/DegreeZeroSectionsRepresentable.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/DegreeZeroSectionsRepresentable.lean#L79). The attribute's comment: “part (1)”.

> **Stacks 08JX, part (1).**  Let `K` be a pseudo-coherent object of `D(𝒪_X)` on an algebraic
> space `X` such that `H⁻¹(Lg^*K) = 0` for every scheme `g : T → X`.  Then the functor
> `(g : T → X) ↦ H⁰(T, H⁰(Lg^*K))` on the schemes over `X` is an algebraic space affine and of
> finite presentation over `X`.
>
> The functor is the degree-zero sections functor of any K-flat complex `P₀` with flat terms
> representing `K`; its value at `g` is `H⁰(T, H⁰(Lg^*K))` by
> `AlgebraicGeometry.Space.degreeZeroSectionsEquiv`.

```lean
theorem isAffineFinitePresentationAlgebraicSpaceOver_degreeZeroSectionsFunctor
    (K : derivedModules B S hS X) (hK : IsPseudoCoherentObject K)
    (hvan : HasVanishingDegreeNegOneDerivedPullback (hasDerivedModulePullbacks B S hS) K)
    (P₀ : CochainComplex (toposModules B S hS X) ℤ)
    (hP₀ : IsKFlat (Y := smallEtaleRingedTopos B S hS X)
      ((HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj P₀))
    (e : DerivedCategory.Q.obj P₀ ≅ K) :
    IsAffineFinitePresentationAlgebraicSpaceOver X
      (degreeZeroSectionsFunctor (schemesOverCone X) P₀)
```

**`AlgebraicGeometry.Space.derivedPullbackSectionFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/DerivedPullbackSectionFunctor.lean, line 427](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/DerivedPullbackSectionFunctor.lean#L427). The attribute's comment: “the functor of part (2), `(g : T → B) ↦ H⁰(T, Lg^*K)`, on the test schemes over `B`; its value is `Hom_{D(𝒪_T)}(𝒪_T, Lg^*K)` by `derivedPullbackSectionFunctor_obj_equiv`. The datum `hc` -- Stacks 0D6D and the unit law for `L(-)^*` -- is built with no hypothesis by `AlgebraicGeometry.Space.derivedPullbackCoherence`. Its representability is `isAffineFinitePresentationSectionFunctor_of_hasVanishingNegativeDerivedPullback` and the two conclusions about `K` are `isPerfect_and_locally_hasTorAmplitude_of_hasVanishingNegativeDerivedPullback`.”.

> **The degree-zero hypercohomology functor of Stacks 08JX, part (2)**: the functor sending a
> test scheme `g : T → B` to `H⁰(T, Lg^*K)`, read as the derived Hom out of the pulled-back
> structure sheaf.
>
> `AlgebraicGeometry.Space.derivedPullbackSectionFunctor_obj_equiv` identifies its value at `T`
> with `Hom_{D(𝒪_T)}(𝒪_T, Lg^*K)`, which is that degree-zero hypercohomology group.

```lean
def derivedPullbackSectionFunctor (hc : DerivedPullbackCoherence B S hS hL)
    (K : derivedModules B S hS X) : (SchemesOver X)ᵒᵖ ⥤ Type (u + 1)
```

**`AlgebraicGeometry.Space.degreeZeroPullbackSections`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/DerivedPullbackSectionFunctor.lean, line 466](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/DerivedPullbackSectionFunctor.lean#L466). The attribute's comment: “the value at a test scheme `g : T → B` of the functor of part (1), the group `H⁰(T, H⁰(Lg^*K))`. Its restriction maps are not constructed here, for want of a comparison `g^*H⁰(E) ⟶ H⁰(Lg^*E)`; part (1) is proved on the degree-zero sections functor of a K-flat complex representing `K`, which takes these values by `AlgebraicGeometry.Space.degreeZeroSectionsEquiv`.”.

> **The value at a test scheme of the functor of Stacks 08JX, part (1)**: the group
> `H⁰(T, H⁰(Lg^*K))` of global sections of the degree-zero cohomology sheaf of the derived pullback
> of `K` along `g : T → B`.

```lean
abbrev degreeZeroPullbackSections (hL : BottomRankStratum.HasDerivedModulePullbacks B S hS)
    (K : derivedModules B S hS X) (T : SchemesOver X) : Type (u + 1)
```

**`AlgebraicGeometry.Space.HasVanishingDegreeNegOneDerivedPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/DerivedPullbackSectionFunctor.lean, line 485](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/DerivedPullbackSectionFunctor.lean#L485). The attribute's comment: “the hypothesis of part (1): `H⁻¹(Lg^*K) = 0` for every test scheme `g : T → B`. The hypothesis of part (2) is `AlgebraicGeometry.Space.HasVanishingNegativeDerivedPullback`.”.

> **The hypothesis of Stacks 08JX, part (1)**: for every test scheme `g : T → B` the
> cohomology sheaf `H⁻¹(Lg^*K)` is zero.

```lean
def HasVanishingDegreeNegOneDerivedPullback
    (hL : BottomRankStratum.HasDerivedModulePullbacks B S hS)
    (K : derivedModules B S hS X) : Prop
```

**`AlgebraicGeometry.Space.HasVanishingNegativeDerivedPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/DerivedPullbackSectionFunctor.lean, line 495](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/DerivedPullbackSectionFunctor.lean#L495). The attribute's comment: “the hypothesis of part (2): `Hⁱ(Lg^*K) = 0` for every test scheme `g : T → B` and every `i < 0`. The hypothesis of part (1) is `AlgebraicGeometry.Space.HasVanishingDegreeNegOneDerivedPullback`.”.

> **The hypothesis of Stacks 08JX, part (2)**: for every test scheme `g : T → B` the
> cohomology sheaves `Hⁱ(Lg^*K)` are zero for every `i < 0`.

```lean
def HasVanishingNegativeDerivedPullback
    (hL : BottomRankStratum.HasDerivedModulePullbacks B S hS)
    (K : derivedModules B S hS X) : Prop
```

**`AlgebraicGeometry.Space.isAffineFinitePresentationSectionFunctor_of_hasVanishingNegativeDerivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/DerivedSectionsFunctor.lean, line 1112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/DerivedSectionsFunctor.lean#L1112). The attribute's comment: “part (2), the conclusion that `(g : T → B) ↦ H⁰(T, Lg^*K)` is an algebraic space affine and of finite presentation over `B`”.

> **Stacks 08JX, part (2), the functor.**  Let `K` be a pseudo-coherent object of `D(𝒪_X)` on
> an algebraic space `X` such that `Hⁱ(Lg^*K) = 0` for every scheme `g : T → X` and every `i < 0`.
> Then the functor `(g : T → X) ↦ H⁰(T, Lg^*K)` on the schemes over `X` is an algebraic space
> affine and of finite presentation over `X`.
>
> As in the source, under this hypothesis `H⁰(T, Lg^*K) = H⁰(T, H⁰(Lg^*K))`
> (`AlgebraicGeometry.Space.derivedPullbackSectionFunctorIso`), so the statement is part (1).

```lean
theorem isAffineFinitePresentationSectionFunctor_of_hasVanishingNegativeDerivedPullback
    {X : AlgebraicSpaces B S hS} (K : derivedModules B S hS X) (hK : IsPseudoCoherentObject K)
    (hvan : HasVanishingNegativeDerivedPullback (hasDerivedModulePullbacks B S hS) K) :
    IsAffineFinitePresentationSectionFunctor (derivedPullbackCoherence B S hS) K
```

**`AlgebraicGeometry.Space.isPerfect_and_locally_hasTorAmplitude_of_hasVanishingNegativeDerivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PerfectOfVanishingPullbacks.lean, line 543](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PerfectOfVanishingPullbacks.lean#L543). The attribute's comment: “part (2), the conclusions that K is perfect and locally has tor amplitude in [0, b]”.

> **Stacks 08JX, part (2), the first two conclusions.**  Let `K` be a pseudo-coherent object of
> `D(𝒪_X)` on an algebraic space `X` such that `Hⁱ(Lg^*K) = 0` for every scheme `g : T → X` and
> every `i < 0`.  Then `K` is perfect, and `K` locally has tor amplitude in `[0, b]`: every étale
> chart of `X` is covered by charts `V` over which `K|_V` has tor amplitude in `[0, b_V]` for some
> `b_V ≥ 0`, against any derived tensor product on the slices.
>
> The proof is the source's: near every point a strictly perfect approximation of `K` has a free
> cokernel `Coker(P⁻¹ → P⁰)` (Stacks 068U, from the vanishing of `H⁻¹` on the fibres), so its
> canonical truncation `τ_{≥ 0}` is strictly perfect, and it represents `K` there because `K` has
> no cohomology in negative degrees
> (`AlgebraicGeometry.Space.exists_covering_slice_models`).

```lean
theorem isPerfect_and_locally_hasTorAmplitude_of_hasVanishingNegativeDerivedPullback
    (T : ∀ U : (smallEtaleRingedSite B S hS X.1 X.2).C,
      DerivedTensorProduct.{u + 1, u, u, u + 1} ((smallEtaleRingedSite B S hS X.1 X.2).over U)) :
    (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect K ∧
      ∀ U : (smallEtaleRingedSite B S hS X.1 X.2).C,
        ∃ P : Presieve U, Sieve.generate P ∈ (smallEtaleRingedSite B S hS X.1 X.2).J U ∧
          ∀ ⦃V : (smallEtaleRingedSite B S hS X.1 X.2).C⦄ (f : V ⟶ U), P f →
            ∃ b : ℤ, 0 ≤ b ∧ DerivedTensorProduct.HasTorAmplitude (T V)
              ((RingedSite.derivedRestriction.{u + 1, u, u, u + 1} _ V).obj K) 0 b
```

## Tag 08JY, a lemma

[Tag 08JY](https://stacks.math.columbia.edu/tag/08JY) in the Stacks Project.

**`AlgebraicGeometry.Space.HomSituation.isAffineFinitePresentationAlgebraicSpaceOverBase_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeHomNoetherianRepresentable.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeHomNoetherianRepresentable.lean#L69).

> In Situation 08JT assume that the base `B` is a Noetherian algebraic space, that `f : X ⟶ B` is
> locally of finite type and quasi-separated, that `𝓕` is an `𝒪_X`-module of finite type, and that
> `𝒢` is an `𝒪_X`-module of finite type, flat over `B`, with support proper over `B`. Then the
> functor `Hom(𝓕, 𝒢)` is an algebraic space affine and of finite presentation over `B`.

```lean
theorem isAffineFinitePresentationAlgebraicSpaceOverBase_of_isNoetherian
    (s : HomSituation B S hS) (hTop : B.Contains (⊤_ Scheme.{u}))
    (hB : IsNoetherian B S hS hTop s.base.1) (hf : IsLocallyOfFiniteType B S hS s.f.hom)
    (hfqs : IsQuasiSeparated B S hS s.f.hom) (hF : SheafOfModules.IsFiniteTypeOnSite s.F)
    (hG : SheafOfModules.IsFiniteTypeOnSite s.G) (hflat : IsFlatOver B S hS s.X.2 s.f.hom s.G)
    (hproper : HasProperSupportOver s.f s.G) :
    s.IsAffineFinitePresentationAlgebraicSpaceOverBase (modulePushforwardCoherence B S hS)
```

## Tag 08K6, a proposition

[Tag 08K6](https://stacks.math.columbia.edu/tag/08K6) in the Stacks Project.

**`AlgebraicGeometry.Space.HomSituation.isAffineAlgebraicSpaceOverBase_and_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeHomSpaceAffine.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeHomSpaceAffine.lean#L103). The attribute's comment: “both assertions: Hom(F, G) is an algebraic space affine over B for F étale-locally generated by fewer sections than the cutoff of the site (Stacks erratum: false for an unbounded quasi-coherent F), and affine of finite presentation over B for F of finite presentation”.

> **Stacks 08K6.** In Situation 08JT let `f : X ⟶ B` be of finite presentation and let `G` be an
> `𝒪_X`-module of finite presentation, flat over `B`, with support proper over `B`.  Then
> `Hom(F, G)` is an algebraic space affine over `B` for every quasi-coherent `F` étale-locally
> generated by fewer than `μ` sections, `μ` below the cutoff of the site; and if `F` is of finite
> presentation, then `Hom(F, G)` is an algebraic space affine and of finite presentation over `B`.
>
> The bound on `F` in the first assertion corrects the source (Stacks erratum): for an arbitrary
> quasi-coherent `F` the first assertion is false on every big fppf site, see
> `AlgebraicGeometry.Space.exists_homSituation_not_isAffineAlgebraicSpaceOverBase`.

```lean
theorem isAffineAlgebraicSpaceOverBase_and_finitePresentation
    (s : HomSituation B S hS)
    (hf : IsFinitePresentation B S hS s.f.hom)
    (hG : s.G.IsFinitePresentationOnSite) (hflat : IsFlatOver B S hS s.X.2 s.f.hom s.G)
    (hproper : HasProperSupportOver s.f s.G) :
    ((∃ μ < B.cutoff, IsEtaleLocallyGeneratedBelow B S hS μ s.F) →
        s.IsAffineAlgebraicSpaceOverBase (modulePushforwardCoherence B S hS)) ∧
      (s.F.IsFinitePresentationOnSite →
        s.IsAffineFinitePresentationAlgebraicSpaceOverBase (modulePushforwardCoherence B S hS))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 99.3, Tag 08JS](https://stacks.math.columbia.edu/tag/08JS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
