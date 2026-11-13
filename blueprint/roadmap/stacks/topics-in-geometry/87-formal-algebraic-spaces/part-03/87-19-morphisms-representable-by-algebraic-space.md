---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.IsLocallyOfFiniteType.of_isRepresentableEtale, AlgebraicGeometry.Space.isRepresentableByAlgebraicSpacesULift_comp, CategoryTheory.Functor.relativelyRepresentable.isMultiplicative, AlgebraicGeometry.Space.isRepresentableByAlgebraicSpacesULift_of_isPullback, CategoryTheory.Functor.relativelyRepresentable.isStableUnderBaseChange, AlgebraicGeometry.FormalSpace.isRepresentableByAlgebraicSpacesULift_of_comp_of_isFormalAlgebraicSpace, AlgebraicGeometry.FormalSpace.isRepresentableByAlgebraicSpacesULift_of_comp_of_isAffineFormal, AlgebraicGeometry.FormalSpace.isRepresentableByAlgebraicSpacesULift_of_comp_of_mono
statement: formalized
proof: formalized
---

# 87.19 Morphisms representable by algebraic spaces

Section 87.19 of the Stacks Project, [Tag 0AJG](https://stacks.math.columbia.edu/tag/0AJG). 15 tags here are carried by 59 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AJG, the section

[Tag 0AJG](https://stacks.math.columbia.edu/tag/0AJG) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsLocallyOfFiniteType.of_isRepresentableEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RepresentableEtaleFiniteType.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RepresentableEtaleFiniteType.lean#L99). The attribute's comment: “the theory of morphisms of algebraic spaces available to a morphism representable by algebraic spaces, in the instance this library uses it: a representable etale morphism is locally of finite type in the sense of Definition 0AM4”.

> **Stacks 0AJG.** A morphism of fppf sheaves on the big fppf site of `S` which is
> representable by algebraic spaces and étale is locally of finite type in the sense of
> Stacks 0AM4. This is the instance of the theory of morphisms representable by algebraic spaces
> that the rig-surjectivity theory of Stacks 0AQS and Stacks 0AQV asks for: étaleness of the
> morphism of algebraic spaces cut out by a represented base change already makes it locally of
> finite type.

```lean
theorem IsLocallyOfFiniteType.of_isRepresentableEtale {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hf : IsRepresentableEtale B S hS f) :
    IsLocallyOfFiniteType B S hS f
```

## Tag 0APY, a lemma

[Tag 0APY](https://stacks.math.columbia.edu/tag/0APY) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentableByAlgebraicSpacesULift_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Representable.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Representable.lean#L380). The attribute's comment: “representable by algebraic spaces in an arbitrary value universe”.

> A composition of morphisms representable by algebraic spaces is
> representable by algebraic spaces, for presheaves on the big fppf site of `S` with values in
> `Type (max w u)`.

```lean
theorem isRepresentableByAlgebraicSpacesULift_comp
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (max w u)} (a : F ⟶ G) (b : G ⟶ H)
    (ha : IsRepresentableByAlgebraicSpacesULift.{w} B S hS a)
    (hb : IsRepresentableByAlgebraicSpacesULift.{w} B S hS b) :
    IsRepresentableByAlgebraicSpacesULift.{w} B S hS (a ≫ b)
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.relativelyRepresentable.isMultiplicative`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.relativelyRepresentable.isMultiplicative#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/Representable.lean, line 395](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Representable.lean#L395) (StacksFrontier): “representable by schemes”.

## Tag 0APZ, a lemma

[Tag 0APZ](https://stacks.math.columbia.edu/tag/0APZ) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentableByAlgebraicSpacesULift_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Representable.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Representable.lean#L101). The attribute's comment: “representable by algebraic spaces”.

> A base change of a morphism representable by algebraic spaces is
> representable by algebraic spaces: in a cartesian square of presheaves on the big fppf site
> of `S` with values in `Type (max w u)` whose right-hand column `a` is representable by
> algebraic spaces, the left-hand column `a'` is representable by algebraic spaces too.

```lean
theorem isRepresentableByAlgebraicSpacesULift_of_isPullback
    {F G G' H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (max w u)}
    (p : H ⟶ F) (a' : H ⟶ G') (a : F ⟶ G) (g : G' ⟶ G) (h : IsPullback p a' a g)
    (ha : IsRepresentableByAlgebraicSpacesULift.{w} B S hS a) :
    IsRepresentableByAlgebraicSpacesULift.{w} B S hS a'
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.relativelyRepresentable.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.relativelyRepresentable.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/Representable.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Representable.lean#L110) (StacksFrontier): “representable by schemes”.

## Tag 0AQ0, a lemma

[Tag 0AQ0](https://stacks.math.columbia.edu/tag/0AQ0) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRepresentableByAlgebraicSpacesULift_of_comp_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean, line 388](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FiniteType.lean#L388). The attribute's comment: “for a second morphism whose source is an arbitrary formal algebraic space”.

> Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of fppf sheaves on the big fppf site of `S`
> with `Y` a formal algebraic space. If `f ≫ g` is representable by algebraic spaces then so is
> `f`.

```lean
theorem isRepresentableByAlgebraicSpacesULift_of_comp_of_isFormalAlgebraicSpace
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hY : IsFormalAlgebraicSpace B S hS Y)
    (hcomp : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (f.hom ≫ g.hom)) :
    Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom
```

**`AlgebraicGeometry.FormalSpace.isRepresentableByAlgebraicSpacesULift_of_comp_of_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RepresentableCancellation.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RepresentableCancellation.lean#L161). The attribute's comment: “for a second morphism whose source is an affine formal algebraic space”.

> **Stacks 0AQ0** when the intermediate sheaf is an affine formal algebraic space. Let
> `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of fppf sheaves on the big fppf site of `S` with `Y`
> an affine formal algebraic space. If `f ≫ g` is representable by algebraic spaces then so is
> `f`, the relative diagonal of `g` being representable by Stacks 0AN2.

```lean
theorem isRepresentableByAlgebraicSpacesULift_of_comp_of_isAffineFormal
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y)
    (hcomp : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (f.hom ≫ g.hom)) :
    Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom
```

**`AlgebraicGeometry.FormalSpace.isRepresentableByAlgebraicSpacesULift_of_comp_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RepresentableCancellation.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RepresentableCancellation.lean#L172). The attribute's comment: “for a second morphism which is a monomorphism of fppf sheaves”.

> **Stacks 0AQ0** when the second morphism is a monomorphism. Its relative diagonal is then
> an isomorphism, hence representable by objects of the site.

```lean
theorem isRepresentableByAlgebraicSpacesULift_of_comp_of_mono {X Y Z : FppfSheaf B S hS}
    (f : X ⟶ Y) (g : Y ⟶ Z) [Mono g]
    (hcomp : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (f.hom ≫ g.hom)) :
    Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom
```

## Tag 0AN4, a lemma

[Tag 0AN4](https://stacks.math.columbia.edu/tag/0AN4) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRepresentable_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RepresentableLocalityTFAE.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RepresentableLocalityTFAE.lean#L102). The attribute's comment: “the equivalence of conditions (1) to (5); the sixth item of the source, add more here, is a placeholder”.

> **Stacks 0AN4.** For a morphism `f : X ⟶ Y` of formal algebraic spaces over `S` the
> following are equivalent:
> 1. `f` is representable by algebraic spaces;
> 2. there is a commutative square `U ⟶ V` over `f` with `U`, `V` formal algebraic spaces,
>    vertical arrows representable by algebraic spaces, `U ⟶ X` surjective étale and `U ⟶ V`
>    representable by algebraic spaces;
> 3. every commutative square `U ⟶ V` over `f` with `U`, `V` formal algebraic spaces and
>    vertical arrows representable by algebraic spaces has `U ⟶ V` representable by algebraic
>    spaces;
> 4. there is a covering `{Yⱼ ⟶ Y}` as in Definition 0AIM and for each `j` a covering
>    `{Xⱼᵢ ⟶ Yⱼ ×_Y X}` as in Definition 0AIM with every `Xⱼᵢ ⟶ Yⱼ` representable by algebraic
>    spaces;
> 5. there is a covering `{Xᵢ ⟶ X}` as in Definition 0AIM and for each `i` a factorization
>    `Xᵢ ⟶ Yᵢ ⟶ Y` with `Yᵢ` an affine formal algebraic space, `Yᵢ ⟶ Y` and `Xᵢ ⟶ Yᵢ`
>    representable by algebraic spaces.
>
> The source's sixth item, *add more here*, is a placeholder and not a condition.

```lean
theorem isRepresentable_tfae {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsFormalAlgebraicSpace B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y) :
    List.TFAE [Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom,
      IsRepresentableOnSomeSquare B S hS f,
      IsRepresentableOnEverySquare B S hS f,
      IsRepresentableAfterTargetCover B S hS f,
      IsRepresentableOnFactoredAtlas B S hS f]
```

## Tag 0AJH, a lemma

[Tag 0AJH](https://stacks.math.columbia.edu/tag/0AJH) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_of_representable_over_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RepresentableOverAffineCharts.lean, line 586](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RepresentableOverAffineCharts.lean#L586). The attribute's comment: “the full statement, with no hypothesis beyond the source's: the set-theoretic condition of Stacks 0AIS on the source is proved, not assumed”.

> **Stacks 0AJH.** Let `S` be a scheme, let `Y` be an affine formal algebraic space over `S`,
> and let `f : X ⟶ Y` be a morphism of sheaves on the big fppf site of `S` which is representable
> by algebraic spaces. Then `X` is a formal algebraic space over `S`.
>
> The affine étale charts of one stage `X₀ = Y₀ ×_Y X` are transported to `X` along the
> representable thickening `X₀ ⟶ X`; the stages of a transported chart over the stages `Y_μ` of
> `Y` are algebraic spaces over the affine `Y_μ` whose base change to `Y₀` is affine, hence affine
> by the thickening case of Stacks 07VT
> (`AlgebraicGeometry.Space.isAffineSpace_of_isClosedSubspace_of_isSurjective_terminal`), so each
> transported chart is an affine formal algebraic space, and the charts cover `X`.

```lean
theorem isFormalAlgebraicSpace_of_representable_over_isAffineFormal
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) (hY : IsAffineFormalAlgebraicSpace B S hS Y)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom) :
    IsFormalAlgebraicSpace B S hS X
```

## Tag 0AJI, a lemma

[Tag 0AJI](https://stacks.math.columbia.edu/tag/0AJI) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_of_isRepresentableByAlgebraicSpacesULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocallyNoetherianSource.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/LocallyNoetherianSource.lean#L65).

> **Stacks 0AJI.** If `Y` is a formal algebraic space over `S` and `f : X ⟶ Y` is a morphism
> of fppf sheaves representable by algebraic spaces, then `X` is a formal algebraic space over
> `S`.
>
> This is `AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_of_representable_over_formal`
> with its hypotheses proved: the set-theoretic condition of `X` and of the base changed atlas
> members by
> `satisfiesSetTheoreticCondition_of_isRepresentableByAlgSpacesULift_of_isFormalAlgebraicSpace`
> and Stacks 0AIU by its corrected form
> `isFormalAlgebraicSpace_of_colimit_isRepresentableThickeningULift`.

```lean
theorem isFormalAlgebraicSpace_of_isRepresentableByAlgebraicSpacesULift
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hY : IsFormalAlgebraicSpace B S hS Y)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom) :
    IsFormalAlgebraicSpace B S hS X
```

## Tag 0AKN, a lemma

[Tag 0AKN](https://stacks.math.columbia.edu/tag/0AKN) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.relative_isAffineHom_of_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/AllTestObjects.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/AllTestObjects.lean#L250).

> **Stacks 0AKN.** Let `S` be a scheme contained in a big fppf site `B` and let `f : X ⟶ Y`
> be a morphism of affine formal algebraic spaces over `S` which is representable by algebraic
> spaces. Then `f` is representable by schemes and affine: every base change of `f` along a
> morphism to `Y` from a sheaf represented by an object of the site is represented by an object of
> the site, and the induced morphism of underlying schemes is affine.

```lean
theorem relative_isAffineHom_of_isRepresentableByAlgebraicSpaces
    {X Y : Sheaf (BigFppfOver.topology B S hS) (Type (u + 1))} (f : X ⟶ Y)
    (hX : _root_.AlgebraicGeometry.IsAffineFormalAlgebraicSpace B S hS X)
    (hY : _root_.AlgebraicGeometry.IsAffineFormalAlgebraicSpace B S hS Y)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom) :
    (MorphismProperty.inverseImage (@IsAffineHom.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) f
```

**`AlgebraicGeometry.FormalSpace.exists_affine_baseChange_of_isRepresentableByAlgebraicSpaces'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/MorphismOfAffines.lean, line 691](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/MorphismOfAffines.lean#L691). The attribute's comment: “representability by schemes together with affineness, over every test object of the site whose underlying scheme is affine”.

> **Stacks 0AKN** over the test objects with affine underlying scheme. Let `f : X ⟶ Y` be a
> morphism of affine formal algebraic spaces over `S` which is representable by algebraic spaces,
> and let `g` be a morphism to `Y` from a sheaf represented by an object `U` of the site with
> affine underlying scheme. Then the fibre product of `f` and `g` is represented by an object of
> the site with affine underlying scheme, and the induced morphism to `U` is an affine morphism of
> schemes: `f` is representable by schemes and affine over `U`.
>
> Of the two sheaves only the presentations by affine thickenings are used, not the set-theoretic
> condition of Stacks 0AIS which together with them makes them affine formal algebraic spaces; so
> the conclusion is available for the formal spectrum of a weakly admissible topological ring over
> any site containing its quotient spectra, with no condition on the size of the site.

```lean
theorem exists_affine_baseChange_of_isRepresentableByAlgebraicSpaces'
    {X Y : Sheaf (BigFppfOver.topology B S hS) (Type (u + 1))} (f : X ⟶ Y)
    (hX : HasThickeningPresentation B S hS X)
    (hY : HasThickeningPresentation B S hS Y)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (U : BigFppfOver B S hS) (hU : IsAffine ((BigFppfOver.toScheme B S hS).obj U))
    (g : (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj U ⟶ Y) :
    ∃ (V : BigFppfOver B S hS)
      (p : (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj V ⟶ X) (q : V ⟶ U),
      IsPullback p ((Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).map q) f g ∧
        IsAffine ((BigFppfOver.toScheme B S hS).obj V) ∧
        IsAffineHom ((BigFppfOver.toScheme B S hS).map q)
```

**`AlgebraicGeometry.FormalSpace.relative_isAffineHom_of_hasThickeningPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/MorphismOfAffines.lean, line 787](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/MorphismOfAffines.lean#L787). The attribute's comment: “both assertions of the source -- representability by schemes and affineness -- over an arbitrary test object of the site”.

> **Stacks 0AKN.** A morphism `f : X ⟶ Y` of affine formal algebraic spaces over `S` which is
> representable by algebraic spaces is representable by schemes, and the morphism of schemes
> underlying each of its represented base changes is affine. Nothing is assumed of the test
> objects: this is the source's assertion over every object of the site.
>
> Over a test object with affine underlying scheme the conclusion is
> `AlgebraicGeometry.FormalSpace.exists_affine_baseChange_of_isRepresentableByAlgebraicSpaces`,
> and it carries in addition that the representing object is affine, which an arbitrary test
> object cannot have. The passage to an arbitrary test object `U` is affine-locality on the
> target, carried out in the value universe of the site: the fibre product `X ×_Y U` is an
> algebraic space over `S`, because `f` is representable by algebraic spaces and `U` is
> representable, hence pointwise `u`-small, so it is the universe lift of an algebraic space `Z₀`
> in the value universe of the site and the projection to `U` descends with it. The affine form
> above, read over each morphism of the site into `U` with affine source, is exactly the
> affine-base-change condition of that descended projection, which relative Tag 03JH for a
> morphism out of an algebraic space —
> `AlgebraicGeometry.Space.exists_representing_over_of_holdsOnAffineBaseChange_of_isAlgebraicSpace`
> — glues into a single object of the site with affine projection to `U`, affineness of a
> morphism of schemes being Zariski-local at the target.
>
> As in the affine form, of the two sheaves only the presentations by affine thickenings are used
> and not the set-theoretic condition of Stacks 0AIS.

```lean
theorem relative_isAffineHom_of_hasThickeningPresentation
    {X Y : Sheaf (BigFppfOver.topology B S hS) (Type (u + 1))} (f : X ⟶ Y)
    (hX : HasThickeningPresentation B S hS X)
    (hY : HasThickeningPresentation B S hS Y)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom) :
    (MorphismProperty.inverseImage
      (@IsAffineHom.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative
        (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) f
```

## Tag 0AN5, a lemma

[Tag 0AN5](https://stacks.math.columbia.edu/tag/0AN5) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.formalSpectrumMap_tfae_of_isAffineFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TautFormalSpectrumTfae.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TautFormalSpectrumTfae.lean#L273). The attribute's comment: “the equivalence of (1), (2) and (3), with Spf(B) an affine formal algebraic space as in Definition 0AIF”.

> **Stacks 0AN5.** Let `S` be a scheme and `φ : A ⟶ C` a continuous homomorphism of weakly
> admissible topological rings over `S`, the formal spectrum `Spf C` being an affine formal
> algebraic space as in Definition 0AIF. The following are equivalent:
>
> 1. `Spf φ : Spf C ⟶ Spf A` is representable by algebraic spaces;
> 2. `Spf φ` is representable (by objects of the site);
> 3. `φ` is taut.
>
> *The hypothesis `hE`.* Definition 0AIF of the source defines `Spf(B)` to be "the affine formal
> algebraic space `colim Spec(B/I)`", and an affine formal algebraic space satisfies, by
> Definition 0AI7, the set-theoretic condition of Remark 0AIS; the source's proof of (1) ⟺ (2)
> is Lemma 0AKN, a statement about morphisms of affine formal algebraic spaces. In this library
> `formalSpectrum E` is the colimit alone, and `hE` records that it is an affine formal algebraic
> space in the sense of Definition 0AI7 (`AlgebraicGeometry.IsAffineFormalAlgebraicSpace`). This
> is the source's own notion of `Spf(B)`, not an extra condition: for weakly admissible `C` it is
> equivalent to the coproduct of the stages lying in the site
> (`AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_formalSpectrum_iff_hasLargeSite`),
> the proviso of Remark 0AIE. Nothing is asked of `Spf A`, of the cutoff of the site, or of the
> stages of either ring.
>
> *Why it cannot be dropped.* Over a site whose cutoff is singular there are taut homomorphisms
> with `Spf φ` not representable
> (`AlgebraicGeometry.FormalSpace.exists_isTaut_not_relativelyRepresentable_of_cof_lt`), and the
> formal spectrum of the target of such a homomorphism is not an affine formal algebraic space
> (`AlgebraicGeometry.FormalSpace.exists_not_isAffineFormalAlgebraicSpace_formalSpectrum_of_cof_lt`).
>
> *Proof.* (1) ⟹ (3) is
> `AlgebraicGeometry.FormalSpace.isTaut_of_isRepresentableByAlgebraicSpaces_formalSpectrumMap` and
> (2) ⟹ (1) is
> `AlgebraicGeometry.FormalSpace.isRepresentableByAlgebraicSpacesULift_formalSpectrumMap`, both
> with no set-theoretic input. (3) ⟹ (2) is
> `AlgebraicGeometry.FormalSpace.relative_isAffineHom_formalSpectrumMap_of_isTaut`: a point of
> `Spf A` out of an affine object factors through a stage `Spec(A/I)` (Stacks 0AIA), over which the
> base change is `Spec(C/J(I))` with `J(I)` the closure of `φ(I)C`, open by tautness; the charts
> over the affine opens of an arbitrary test object glue inside the site because each stage of
> `Spf C` is bounded by the coproduct of all of them, an object of the site by `hE`.

```lean
theorem formalSpectrumMap_tfae_of_isAffineFormalAlgebraicSpace
    (hA : TopologicalRing.IsWeaklyAdmissible A) (hC : TopologicalRing.IsWeaklyAdmissible C)
    (D : QuotientSystem B S hS A) (E : QuotientSystem B S hS C)
    (hE : IsAffineFormalAlgebraicSpace B S hS (formalSpectrum E)) (f : ContinuousHom D E) :
    List.TFAE
      [Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (formalSpectrumMap hA f).hom,
        (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).relativelyRepresentable
          (formalSpectrumMap hA f),
        RingHom.IsTaut f.toRingHom]
```

## Tag 0AKP, a lemma

[Tag 0AKP](https://stacks.math.columbia.edu/tag/0AKP) in the Stacks Project.

**`AlgebraicGeometry.isAffineFormalAlgebraicSpace_of_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/RepresentableAffine.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/RepresentableAffine.lean#L99). The attribute's comment: “affine\_source”.

> The source of a representable affine map of fppf sheaves to an affine
> formal algebraic space is an affine formal algebraic space.

```lean
theorem isAffineFormalAlgebraicSpace_of_affine
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : Sheaf (BigFppfOver.topology B S hS) (Type (u + 1))}
    (f : X ⟶ Y)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y)
    (hf : (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda
        (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@IsAffineHom.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) f) :
    IsAffineFormalAlgebraicSpace B S hS X
```

**`AlgebraicGeometry.isCountablyIndexed_of_affine'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/RepresentableAffine.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/RepresentableAffine.lean#L204). The attribute's comment: “countably\_indexed\_source”.

> The source of a representable affine map to a countably indexed sheaf is
> countably indexed.

```lean
theorem isCountablyIndexed_of_affine'
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : Sheaf (BigFppfOver.topology B S hS) (Type (u + 1))}
    (f : X ⟶ Y)
    (hf : (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda
        (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@IsAffineHom.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f)
    (hY_countable : FormalSpace.IsCountablyIndexed B S hS Y) :
    FormalSpace.IsCountablyIndexed B S hS X
```

**`AlgebraicGeometry.FormalSpace.isCountablyIndexed_of_relative_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffinePullbackPresentation.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AffinePullbackPresentation.lean#L295). The attribute's comment: “countably\_indexed\_source”.

> The source of a representable affine morphism of fppf sheaves whose target is countably
> indexed is itself countably indexed.

```lean
theorem isCountablyIndexed_of_relative_isAffineHom
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hf : (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@IsAffineHom.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f)
    (hY : IsCountablyIndexed B S hS Y) :
    IsCountablyIndexed B S hS X
```

**`AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_of_relative_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineSource.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineSource.lean#L165). The attribute's comment: “affine\_source”.

> **Stacks 0AKP, part (1).** The source of a representable affine morphism of fppf sheaves
> whose target is an affine formal algebraic space is itself an affine formal algebraic space.

```lean
theorem isAffineFormalAlgebraicSpace_of_relative_isAffineHom
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hf : (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@IsAffineHom.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y) :
    IsAffineFormalAlgebraicSpace B S hS X
```

**`AlgebraicGeometry.FormalSpace.isCountablyIndexedAndClassical_of_relative_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineSourceTypes.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineSourceTypes.lean#L194). The attribute's comment: “classical\_source”.

> **Stacks 0AKP, part (3).** The source of a representable affine morphism of fppf sheaves
> whose target is a countably indexed and classical affine formal algebraic space is itself
> countably indexed and classical.
>
> Countable indexing of the source is part (2) of the same tag. For the classical half the
> morphism is the formal spectrum of a continuous taut homomorphism of presenting rings, and
> pre-admissibility ascends along such a homomorphism by Stacks 0GX8; the presenting ring of the
> source is complete and separated, being weakly admissible.

```lean
theorem isCountablyIndexedAndClassical_of_relative_isAffineHom
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hf : (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@IsAffineHom.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f)
    (hY : IsCountablyIndexed B S hS Y ∧ IsClassical B S hS Y) :
    IsCountablyIndexed B S hS X ∧ IsClassical B S hS X
```

**`AlgebraicGeometry.FormalSpace.isWeaklyAdic_of_relative_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineSourceTypes.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineSourceTypes.lean#L220). The attribute's comment: “weakly\_adic\_source”.

> **Stacks 0AKP, part (4).** The source of a representable affine morphism of fppf sheaves
> whose target is a weakly adic affine formal algebraic space is itself weakly adic.
>
> A weakly adic affine formal algebraic space is countably indexed by item (5) of Stacks 0AIK, so
> the morphism is the formal spectrum of a continuous taut homomorphism of presenting rings; weak
> pre-adicness ascends along such a homomorphism by Stacks 0GXI, and the presenting ring of the
> source is complete and separated, being weakly admissible.

```lean
theorem isWeaklyAdic_of_relative_isAffineHom
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hf : (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@IsAffineHom.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f)
    (hY : IsWeaklyAdic B S hS Y) :
    IsWeaklyAdic B S hS X
```

**`AlgebraicGeometry.FormalSpace.isAdicStar_of_relative_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineSourceTypes.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineSourceTypes.lean#L252). The attribute's comment: “adic\_star\_source”.

> **Stacks 0AKP, part (5).** The source of a representable affine morphism of fppf sheaves
> whose target is an adic\* affine formal algebraic space is itself adic\*.
>
> An adic\* affine formal algebraic space is countably indexed by items (2) and (3) and (5) of
> Stacks 0AIK, so the morphism is the formal spectrum of a continuous taut homomorphism of
> presenting rings; Stacks 0APU makes the target of such a homomorphism adic with a finitely
> generated ideal of definition as soon as its source is and the target is complete and
> separated, which the presenting ring of the source is, being weakly admissible. The finitely
> generated ideal of definition the hypothesis supplies defines the topology adically because the
> ring is pre-adic.

```lean
theorem isAdicStar_of_relative_isAffineHom
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hf : (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@IsAffineHom.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f)
    (hY : IsAdicStar B S hS Y) :
    IsAdicStar B S hS X
```

**`AlgebraicGeometry.FormalSpace.isNoetherian_of_relative_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineSourceTypes.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineSourceTypes.lean#L291). The attribute's comment: “noetherian\_source”.

> **Stacks 0AKP, part (6).** The source of a representable affine morphism of fppf sheaves
> which is locally of finite type and whose target is a Noetherian affine formal algebraic space
> is itself Noetherian.
>
> A Noetherian affine formal algebraic space is countably indexed by items (1), (2), (3) and (5)
> of Stacks 0AIK, so the morphism is the formal spectrum of a continuous taut homomorphism
> `φ : A → C` of presenting rings. An ideal of definition of the Noetherian ring `A` is finitely
> generated, so Stacks 0APU produces a finitely generated ideal `J ⊆ C` defining the topology of
> `C` adically; `C` is then `J`-adically complete, and Stacks 05GH reduces Noetherianness of `C`
> to that of `C ⧸ J`. The closed extended ideals form a fundamental system of neighbourhoods of
> zero by tautness, so `J` contains the closure `J(I)` of `I C` for a weak ideal of definition
> `I ⊆ A`; the stage half of Stacks 0ANT makes `A ⧸ I → C ⧸ J(I)` of finite type, hence
> `C ⧸ J(I)` Noetherian, and `C ⧸ J` is a quotient of it.

```lean
theorem isNoetherian_of_relative_isAffineHom
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hf : (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@IsAffineHom.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f)
    (hft : IsLocallyOfFiniteType B S hS f)
    (hY : IsNoetherian B S hS Y) :
    IsNoetherian B S hS X
```

**`AlgebraicGeometry.FormalSpace.isCountablyIndexed_and_isClassical_of_relative_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeDescentAlongAffine.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeDescentAlongAffine.lean#L148). The attribute's comment: “classical\_source”.

> **Stacks 0AKP, part (3).** The source of a representable affine morphism of fppf sheaves
> whose target is a countably indexed classical affine formal algebraic space is itself countably
> indexed and classical.
>
> Countable indexing passes to the source by part (2) of Stacks 0AKP, and admissibility of the
> presenting ring ascends along the taut homomorphism inducing the morphism, by Stacks 0GX8.

```lean
theorem isCountablyIndexed_and_isClassical_of_relative_isAffineHom
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hf : (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@IsAffineHom.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f)
    (hYc : IsCountablyIndexed B S hS Y) (hYcl : IsClassical B S hS Y) :
    IsCountablyIndexed B S hS X ∧ IsClassical B S hS X
```

**`AlgebraicGeometry.FormalSpace.isNoetherian_of_relative_isAffineHom'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeDescentAlongAffine.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeDescentAlongAffine.lean#L175). The attribute's comment: “noetherian\_source”. References: EGA I (10.13.2), “special case”.

> **Stacks 0AKP, part (6).** The source of a representable affine morphism of fppf sheaves
> which is locally of finite type and whose target is a Noetherian affine formal algebraic space
> is itself Noetherian.
>
> By the equivalence of conditions (1) and (3) of Stacks 0AKM a Noetherian affine formal
> algebraic space is an adic\* one with a presentation by Noetherian affine schemes. Part (5)
> above gives the first half for the source, and the presentation pulls back to a Noetherian one
> because each stage of the source is of finite type over the corresponding Noetherian stage of
> the target.

```lean
theorem isNoetherian_of_relative_isAffineHom'
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hf : (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@IsAffineHom.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f)
    (hft : IsLocallyOfFiniteType B S hS f)
    (hYn : IsNoetherian B S hS Y) :
    IsNoetherian B S hS X
```

**`AlgebraicGeometry.FormalSpace.isAdicStar_of_relative_isAffineHom'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeDescentAlongAffine.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeDescentAlongAffine.lean#L200). The attribute's comment: “adic\_star\_source”.

> **Stacks 0AKP, part (5).** The source of a representable affine morphism of fppf sheaves
> whose target is an adic\* affine formal algebraic space is itself adic\*.
>
> The powers of an ideal of definition of an adic ring are a fundamental system of open ideals,
> so the target is countably indexed and part (2) of Stacks 0AKP carries that to the source. The
> presenting ring of the source is complete and separated, so by Stacks 0APU the taut
> homomorphism inducing the morphism makes it adic with a finitely generated ideal of
> definition.

```lean
theorem isAdicStar_of_relative_isAffineHom'
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hf : (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@IsAffineHom.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f)
    (hYa : IsAdicStar B S hS Y) :
    IsAdicStar B S hS X
```

**`AlgebraicGeometry.FormalSpace.isWeaklyAdic_of_relative_isAffineHom'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeDescentAlongAffine.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeDescentAlongAffine.lean#L231). The attribute's comment: “weakly\_adic\_source”.

> **Stacks 0AKP, part (4).** The source of a representable affine morphism of fppf sheaves
> whose target is a weakly adic affine formal algebraic space is itself weakly adic.
>
> A weakly adic ring has the closed powers of a single ideal as a fundamental system of open
> ideals, so the target is countably indexed and part (2) of Stacks 0AKP carries that to the
> source; weak pre-adicness of the presenting ring then ascends along the taut homomorphism
> inducing the morphism, by Stacks 0GXI.

```lean
theorem isWeaklyAdic_of_relative_isAffineHom'
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hf : (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@IsAffineHom.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f)
    (hYw : IsWeaklyAdic B S hS Y) :
    IsWeaklyAdic B S hS X
```

## Tag 0AKQ, a lemma

[Tag 0AKQ](https://stacks.math.columbia.edu/tag/0AKQ) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isCountablyIndexed_of_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean, line 341](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean#L341). The attribute's comment: “clause (1); Stacks 0AKN is the library's `relative_isAffineHom_of_isRepresentableByAlgebraicSpaces` and parts (1) and (2) of Stacks 0AKP are the library's `isAffineFormalAlgebraicSpace_of_relative_isAffineHom` and `isCountablyIndexed_of_relative_isAffineHom`”.

> **Stacks 0AKQ, clause (1).** Let `f : X ⟶ Y` be a morphism of affine formal algebraic
> spaces over `S` which is representable by algebraic spaces. If `Y` is countably indexed then
> so is `X`.

```lean
theorem isCountablyIndexed_of_isRepresentable {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (hYc : IsCountablyIndexed B S hS Y) :
    IsCountablyIndexed B S hS X
```

**`AlgebraicGeometry.FormalSpace.isCountablyIndexedAndClassical_of_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean#L356). The attribute's comment: “clause (2); Stacks 0AKN is the library's `relative_isAffineHom_of_isRepresentableByAlgebraicSpaces` and clause (3) of Stacks 0AKP is the library's `isCountablyIndexedAndClassical_of_relative_isAffineHom`”.

> **Stacks 0AKQ, clause (2).** Let `f : X ⟶ Y` be a morphism of affine formal algebraic
> spaces over `S` which is representable by algebraic spaces. If `Y` is countably indexed and
> classical then so is `X`.

```lean
theorem isCountablyIndexedAndClassical_of_isRepresentable {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (hYc : IsCountablyIndexed B S hS Y ∧ IsClassical B S hS Y) :
    IsCountablyIndexed B S hS X ∧ IsClassical B S hS X
```

**`AlgebraicGeometry.FormalSpace.isWeaklyAdic_of_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean, line 371](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean#L371). The attribute's comment: “clause (3); Stacks 0AKN is the library's `relative_isAffineHom_of_isRepresentableByAlgebraicSpaces` and clause (4) of Stacks 0AKP is the library's `isWeaklyAdic_of_relative_isAffineHom`”.

> **Stacks 0AKQ, clause (3).** Let `f : X ⟶ Y` be a morphism of affine formal algebraic
> spaces over `S` which is representable by algebraic spaces. If `Y` is weakly adic then so is
> `X`.

```lean
theorem isWeaklyAdic_of_isRepresentable {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (hYc : IsWeaklyAdic B S hS Y) :
    IsWeaklyAdic B S hS X
```

**`AlgebraicGeometry.FormalSpace.isAdicStar_of_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean#L386). The attribute's comment: “clause (4); Stacks 0AKN is the library's `relative_isAffineHom_of_isRepresentableByAlgebraicSpaces` and clause (5) of Stacks 0AKP is the library's `isAdicStar_of_relative_isAffineHom`”.

> **Stacks 0AKQ, clause (4).** Let `f : X ⟶ Y` be a morphism of affine formal algebraic
> spaces over `S` which is representable by algebraic spaces. If `Y` is adic\* then so is
> `X`.

```lean
theorem isAdicStar_of_isRepresentable {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (hYc : IsAdicStar B S hS Y) :
    IsAdicStar B S hS X
```

**`AlgebraicGeometry.FormalSpace.isNoetherian_of_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean#L401). The attribute's comment: “clause (5); Stacks 0AKN is the library's `relative_isAffineHom_of_isRepresentableByAlgebraicSpaces` and clause (6) of Stacks 0AKP is the library's `isNoetherian_of_relative_isAffineHom`”.

> **Stacks 0AKQ, clause (5).** Let `f : X ⟶ Y` be a morphism of affine formal algebraic
> spaces over `S` which is representable by algebraic spaces and locally of finite type. If `Y`
> is Noetherian then so is `X`.

```lean
theorem isNoetherian_of_isRepresentable {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (hft : IsLocallyOfFiniteType B S hS f)
    (hYc : IsNoetherian B S hS Y) :
    IsNoetherian B S hS X
```

**`AlgebraicGeometry.FormalSpace.isCountablyIndexed_of_isRepresentable'`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferRefined.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferRefined.lean#L74). The attribute's comment: “clause (1); Stacks 0AKN is the library's `relative_isAffineHom_of_isRepresentableByAlgebraicSpaces` and parts (1) and (2) of Stacks 0AKP are the library's `isAffineFormalAlgebraicSpace_of_relative_isAffineHom` and `isCountablyIndexed_of_relative_isAffineHom`”.

> **Stacks 0AKQ, clause (1).** Let `f : X ⟶ Y` be a morphism of affine formal algebraic
> spaces over `S` which is representable by algebraic spaces. If `Y` is countably indexed then
> so is `X`.

```lean
alias isCountablyIndexed_of_isRepresentable'
```

**`AlgebraicGeometry.FormalSpace.isCountablyIndexedAndClassical_of_isRepresentable'`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferRefined.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferRefined.lean#L82). The attribute's comment: “clause (2); Stacks 0AKN is the library's `relative_isAffineHom_of_isRepresentableByAlgebraicSpaces` and clause (3) of Stacks 0AKP is the library's `isCountablyIndexedAndClassical_of_relative_isAffineHom`”.

> **Stacks 0AKQ, clause (2).** Let `f : X ⟶ Y` be a morphism of affine formal algebraic
> spaces over `S` which is representable by algebraic spaces. If `Y` is countably indexed and
> classical then so is `X`.

```lean
alias isCountablyIndexedAndClassical_of_isRepresentable'
```

**`AlgebraicGeometry.FormalSpace.isWeaklyAdic_of_isRepresentable'`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferRefined.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferRefined.lean#L91). The attribute's comment: “clause (3); Stacks 0AKN is the library's `relative_isAffineHom_of_isRepresentableByAlgebraicSpaces` and clause (4) of Stacks 0AKP is the library's `isWeaklyAdic_of_relative_isAffineHom`”.

> **Stacks 0AKQ, clause (3).** Let `f : X ⟶ Y` be a morphism of affine formal algebraic
> spaces over `S` which is representable by algebraic spaces. If `Y` is weakly adic then so is
> `X`.

```lean
alias isWeaklyAdic_of_isRepresentable'
```

**`AlgebraicGeometry.FormalSpace.isAdicStar_of_isRepresentable'`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferRefined.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferRefined.lean#L99). The attribute's comment: “clause (4); Stacks 0AKN is the library's `relative_isAffineHom_of_isRepresentableByAlgebraicSpaces` and clause (5) of Stacks 0AKP is the library's `isAdicStar_of_relative_isAffineHom`”.

> **Stacks 0AKQ, clause (4).** Let `f : X ⟶ Y` be a morphism of affine formal algebraic
> spaces over `S` which is representable by algebraic spaces. If `Y` is adic\* then so is
> `X`.

```lean
alias isAdicStar_of_isRepresentable'
```

**`AlgebraicGeometry.FormalSpace.isNoetherian_of_isRepresentable'`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferRefined.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferRefined.lean#L107). The attribute's comment: “clause (5); Stacks 0AKN is the library's `relative_isAffineHom_of_isRepresentableByAlgebraicSpaces` and clause (6) of Stacks 0AKP is the library's `isNoetherian_of_relative_isAffineHom`”.

> **Stacks 0AKQ, clause (5).** Let `f : X ⟶ Y` be a morphism of affine formal algebraic
> spaces over `S` which is representable by algebraic spaces and locally of finite type. If `Y`
> is Noetherian then so is `X`.

```lean
alias isNoetherian_of_isRepresentable'
```

## Tag 0AN6, an example

[Tag 0AN6](https://stacks.math.columbia.edu/tag/0AN6) in the Stacks Project.

**`TopologicalRing.CompletionOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean#L74). The attribute's comment: “completion\_over”.

> The completion of `A` over `B` is the inverse limit, over the weak ideals of definition
> `J` of `B`, of the rings `A / JA`.

```lean
public def CompletionOver {B : Type u} {A : Type v} [CommRing B] [CommRing A]
    [TopologicalSpace B] (f : B →+* A) :
    Subring (∀ J : WeakIdealOfDefinitionIndex B, A ⧸ extendedIdeal f J)
```

**`TopologicalRing.CompletionOver.limitTopology`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean#L90). The attribute's comment: “completion\_over”.

> The inverse-limit topology on the completion over `B`, with every quotient ring in the
> defining inverse system carrying the discrete topology.

```lean
public noncomputable instance limitTopology {B : Type u} {A : Type v} [CommRing B]
    [CommRing A] [TopologicalSpace B] (f : B →+* A) :
    TopologicalSpace (CompletionOver f)
```

**`TopologicalRing.CompletionOver.canonicalMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean#L114). The attribute's comment: “completion\_over”.

> The canonical ring homomorphism from `B` to the completion of `A` over `B`.

```lean
public def canonicalMap {B : Type u} {A : Type v} [CommRing B] [CommRing A]
    [TopologicalSpace B] (f : B →+* A) : B →+* CompletionOver f
```

**`TopologicalRing.CompletionOver.projection_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean#L211). The attribute's comment: “kernel\_closure”.

> Every projection from the relative completion to a defining quotient is surjective.

```lean
public theorem projection_surjective {B : Type u} {A : Type v} [CommRing B] [CommRing A]
    [TopologicalSpace B] (f : B →+* A) (J : WeakIdealOfDefinitionIndex B) :
    Function.Surjective (projection f J)
```

**`TopologicalRing.CompletionOver.isOpen_ker_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean#L220). The attribute's comment: “kernel\_closure”.

> The kernel of a projection from the relative completion is open.

```lean
public theorem isOpen_ker_projection {B : Type u} {A : Type v} [CommRing B] [CommRing A]
    [TopologicalSpace B] (f : B →+* A) (J : WeakIdealOfDefinitionIndex B) :
    IsOpen (RingHom.ker (projection f J) : Set (CompletionOver f))
```

**`TopologicalRing.CompletionOver.ker_projection_eq_closure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean#L233). The attribute's comment: “kernel\_closure”.

> The kernel of a projection from the relative completion is the closure of the ideal
> extended from the corresponding weak ideal of definition of the base ring.

```lean
public theorem ker_projection_eq_closure {B : Type u} {A : Type v} [CommRing B] [CommRing A]
    [TopologicalSpace B] (f : B →+* A) (J : WeakIdealOfDefinitionIndex B) :
    RingHom.ker (projection f J) = Ideal.closure (J.1.map (canonicalMap f))
```

**`TopologicalRing.projection_ker_isWeakIdealOfDefinition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean, line 340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean#L340). The attribute's comment: “weakly\_admissible”.

> The kernel of every projection to `A / JA` is a weak ideal of definition of the completion.

```lean
public theorem projection_ker_isWeakIdealOfDefinition (f : B →+* A)
    (J : WeakIdealOfDefinitionIndex B) :
    TopologicalRing.IsWeakIdealOfDefinition (RingHom.ker (projection f J))
```

**`TopologicalRing.completionOver_isWeaklyAdmissible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean, line 382](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean#L382). The attribute's comment: “weakly\_admissible”.

> Completion over a weakly admissible topological ring is weakly admissible.

```lean
public theorem completionOver_isWeaklyAdmissible (f : B →+* A)
    (hB : TopologicalRing.IsWeaklyAdmissible B) :
    TopologicalRing.IsWeaklyAdmissible (CompletionOver f)
```

**`TopologicalRing.completeSpace_completionOver`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean, line 414](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean#L414). The attribute's comment: “complete\_linearly\_topologized”.

> The completion over a ring is complete for its canonical additive
> uniformity.

```lean
public noncomputable instance completeSpace_completionOver (f : B →+* A) :
    @CompleteSpace (CompletionOver f)
      (IsTopologicalAddGroup.rightUniformSpace (CompletionOver f))
```

**`TopologicalRing.t2Space_completionOver`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean, line 441](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean#L441). The attribute's comment: “complete\_linearly\_topologized”.

> The inverse-limit topology on the completion is separated.

```lean
public noncomputable instance t2Space_completionOver (f : B →+* A) :
    T2Space (CompletionOver f)
```

**`TopologicalRing.continuous_canonicalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean, line 462](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean#L462). The attribute's comment: “taut”.

> The canonical map to the completion over a topological ring is continuous.

```lean
public theorem continuous_canonicalMap {B : Type u} {A : Type v}
    [CommRing B] [TopologicalSpace B] [IsTopologicalRing B] [CommRing A]
    (f : B →+* A) : Continuous (canonicalMap f)
```

**`TopologicalRing.isTaut_canonicalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean, line 492](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean#L492). The attribute's comment: “taut”.

> The canonical map to the completion over a weakly preadmissible ring is taut.

```lean
public theorem isTaut_canonicalMap {B : Type u} {A : Type v}
    [CommRing B] [TopologicalSpace B] [CommRing A]
    (f : B →+* A) (hB : TopologicalRing.IsWeaklyPreAdmissible B) :
    RingHom.IsTaut (canonicalMap f)
```

Declarations registered for the tag:

- [`TopologicalRing.completionOverIsLinearTopology`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean#L275), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/CompletionOver.lean#L408) (StacksFrontier): “complete\_linearly\_topologized”.

## Tag 0AN7, a remark

[Tag 0AN7](https://stacks.math.columbia.edu/tag/0AN7) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_formalSpectrumMap_constants_not_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SharpnessOfRepresentabilityExamples.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SharpnessOfRepresentabilityExamples.lean#L128). The attribute's comment: “(1): for `A = k` a field with the discrete topology and `B = k⟦t⟧` with the `t`-adic topology, `Spf (φ) : Spf(k⟦t⟧) → Spf(k)` of the inclusion of constants is a morphism of affine formal algebraic spaces which is not representable, and not even representable by algebraic spaces”.

> **Stacks 0AN7 (1).** Let `k` be a field with the discrete topology and let `k⟦t⟧` carry the
> `t`-adic topology; both are weakly admissible and the inclusion of constants `φ : k → k⟦t⟧` is
> continuous. Then, over the base `S = Spec k` of a suitable big fppf site, the formal spectra
> `Spf k` and `Spf k⟦t⟧` are affine formal algebraic spaces and
> `Spf (φ) : Spf k⟦t⟧ ⟶ Spf k` is neither representable nor representable by algebraic spaces.

```lean
theorem exists_formalSpectrumMap_constants_not_representable
    (k : Type u) [Field k] [TopologicalSpace k] [DiscreteTopology k] :
    ∃ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
      (D : QuotientSystem B S hS k)
      (E : QuotientSystem B S hS (TopologicalRing.TAdicPowerSeries k))
      (f : ContinuousHom D E),
      f.toRingHom = TopologicalRing.constantsToTAdicPowerSeries k ∧
      IsAffineFormalAlgebraicSpace B S hS (formalSpectrum D) ∧
      IsAffineFormalAlgebraicSpace B S hS (formalSpectrum E) ∧
      ¬ (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).relativelyRepresentable
        (formalSpectrumMap (TopologicalRing.isWeaklyAdmissible_discreteTopology k) f) ∧
      ¬ Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS
        (formalSpectrumMap (TopologicalRing.isWeaklyAdmissible_discreteTopology k) f).hom
```

**`AlgebraicGeometry.FormalSpace.exists_representable_formalSpectrum_not_mcQuillan`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SharpnessOfRepresentabilityExamples.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SharpnessOfRepresentabilityExamples.lean#L180). The attribute's comment: “(2): a representable morphism `f : Y → X` of affine formal algebraic spaces with `X = Spf(A)` McQuillan and `Y` not McQuillan, the example of Examples, Section 0ANY”.

> **Stacks 0AN7 (2).** There are a weakly admissible topological ring `A` over a base `S` and a
> representable morphism `f : Y ⟶ Spf A` of affine formal algebraic spaces such that the target
> `Spf A` is McQuillan but the source `Y` is not. This is the example of Examples, Section 0ANY,
> i.e. Stacks 0CBE, with its McQuillan target identified with a formal spectrum. The source is not
> McQuillan in the sense of condition (4) of Stacks 0AIC, and not in the sense of condition (1)
> either: it is isomorphic to the formal spectrum of no weakly admissible topological ring.

```lean
theorem exists_representable_formalSpectrum_not_mcQuillan :
    ∃ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
      (A : Type u) (_ : CommRing A) (_ : TopologicalSpace A) (_ : IsTopologicalRing A)
      (_ : IsLinearTopology A A) (D : QuotientSystem B S hS A) (Y : FppfSheaf B S hS)
      (f : Y ⟶ formalSpectrum D),
      TopologicalRing.IsWeaklyAdmissible A ∧
      IsAffineFormalAlgebraicSpace B S hS Y ∧
      IsAffineFormalAlgebraicSpace B S hS (formalSpectrum D) ∧
      HasSomeSurjectivePresentation B S hS (formalSpectrum D) ∧
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).relativelyRepresentable f ∧
      ¬ HasSomeSurjectivePresentation B S hS Y ∧
      ¬ ∃ (A' : Type u) (_ : CommRing A') (_ : TopologicalSpace A') (_ : IsTopologicalRing A')
        (_ : IsLinearTopology A' A') (D' : QuotientSystem B S hS A'),
        TopologicalRing.IsWeaklyAdmissible A' ∧ Nonempty (Y ≅ formalSpectrum D')
```

## Tag 0AN8, a lemma

[Tag 0AN8](https://stacks.math.columbia.edu/tag/0AN8) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isEssentiallySurjectiveSpf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EssentiallySurjectiveSpf.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/EssentiallySurjectiveSpf.lean#L178). The attribute's comment: “essential surjectivity, and only for a quotient system satisfying the site condition of Stacks 0AIF, that the site hold the atlas of quotient spectra: the source leaves that condition implicit, its sites being indexed by a cutoff it may enlarge, and a quotient system by itself places only the individual quotient spectra in the site, not their coproduct. Nothing is asked of the coefficient ring beyond the source's own hypotheses”.

> **Essential surjectivity of `Spf` on étale algebras.** For a McQuillan affine formal algebraic
> space `Spf R` over `S`, every affine formal algebraic space `V` over `S` carrying a morphism
> `V ⟶ Spf R` which is representable by algebraic spaces and étale is `Spf` of the completion `A^∧`
> of an étale `R`-algebra `A`, compatibly with the morphisms to `Spf R`.

```lean
theorem isEssentiallySurjectiveSpf : IsEssentiallySurjectiveSpf' 𝔅 S hS
```

**`AlgebraicGeometry.FormalSpace.etaleFormalSpectrum_correspondence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleCompletionSpectrum.lean, line 899](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleCompletionSpectrum.lean#L899).

> **Stacks 0AN8.** Let `Y = Spf R` be a McQuillan affine formal algebraic space over `S`, for a
> weakly admissible topological ring `R`. Sending the completion `A^∧ = lim A ⧸ JA` of an étale
> `R`-algebra `A` to `Spf A^∧ ⟶ Y` is an equivalence between the opposite of the category of such
> completions and the category of morphisms `X ⟶ Y` of affine formal algebraic spaces which are
> representable by algebraic spaces and étale:
>
> 1. the functor is well defined: `Spf A^∧ ⟶ Spf R` is representable by algebraic spaces and
>    étale;
> 2. it is fully faithful: a morphism `Spf A₁^∧ ⟶ Spf A₂^∧` over `Spf R` is `Spf` of a unique
>    continuous `R`-algebra map `A₂^∧ → A₁^∧`;
> 3. it is essentially surjective: every affine formal algebraic space `X` with a morphism
>    `X ⟶ Spf R` representable by algebraic spaces and étale is, over `Spf R`, the formal spectrum
>    of the completion of an étale `R`-algebra; in particular `X` is McQuillan.
>
> The hypothesis that `Spf R` is an affine formal algebraic space is part of `Y` being a McQuillan
> affine formal algebraic space; only the third clause uses it.

```lean
theorem etaleFormalSpectrum_correspondence (hR : TopologicalRing.IsWeaklyAdmissible R)
    (D : QuotientSystem 𝔅 S hS R)
    (hY : IsAffineFormalAlgebraicSpace 𝔅 S hS (formalSpectrum D)) :
    (∀ {A : Type u} [CommRing A] (f : R →+* A), f.Etale →
      ∀ (E : QuotientSystem 𝔅 S hS (TopologicalRing.CompletionOver f)) (g : ContinuousHom D E),
        g.toRingHom = TopologicalRing.CompletionOver.canonicalMap f →
          IsRepresentableEtale 𝔅 S hS (formalSpectrumMap hR g)) ∧
    (∀ {A₁ A₂ : Type u} [CommRing A₁] [CommRing A₂] {f₁ : R →+* A₁} {f₂ : R →+* A₂}
      {E₁ : QuotientSystem 𝔅 S hS (TopologicalRing.CompletionOver f₁)}
      {E₂ : QuotientSystem 𝔅 S hS (TopologicalRing.CompletionOver f₂)}
      (g₁ : ContinuousHom D E₁) (g₂ : ContinuousHom D E₂)
      (φ : formalSpectrum E₁ ⟶ formalSpectrum E₂),
        φ ≫ formalSpectrumMap hR g₂ = formalSpectrumMap hR g₁ →
          ∃! h : ContinuousHom E₂ E₁, formalSpectrumMap
            (TopologicalRing.completionOver_isWeaklyAdmissible f₂ hR) h = φ ∧
              h.toRingHom.comp g₂.toRingHom = g₁.toRingHom) ∧
    (∀ {X : FppfSheaf 𝔅 S hS}, IsAffineFormalAlgebraicSpace 𝔅 S hS X →
      ∀ p : X ⟶ formalSpectrum D, IsRepresentableEtale 𝔅 S hS p →
        ∃ (A : Type u) (_ : CommRing A) (f : R →+* A), f.Etale ∧
          ∃ (E : QuotientSystem 𝔅 S hS (TopologicalRing.CompletionOver f))
            (g : ContinuousHom D E), g.toRingHom = TopologicalRing.CompletionOver.canonicalMap f ∧
              ∃ i : X ≅ formalSpectrum E, p = i.hom ≫ formalSpectrumMap hR g)
```

**`AlgebraicGeometry.FormalSpace.etale_stageMap_canonicalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleCompletionStageBaseChange.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleCompletionStageBaseChange.lean#L105). The attribute's comment: “the first step of the proof read in the site: for an étale ring map `B → A` and a weak ideal of definition `J` of `B`, the morphism `Spec (A^∧ ⧸ K) ⟶ Spec (B ⧸ J)` of quotient stages of `Spf A^∧ ⟶ Spf B` induced by the canonical map `B → A^∧` is étale. The assertions about the morphism of formal spectra itself — representability, étaleness, full faithfulness, essential surjectivity, the equivalence of categories and the McQuillan conclusion — are not included”.

> **Stacks 0AN8**, the first step of the proof read in the site. For an étale ring map
> `f : B →+* A` and a weak ideal of definition `J` of `B`, the morphism of quotient stages
> `Spec (A^∧ ⧸ K) ⟶ Spec (B ⧸ J)` induced by the canonical map `B → A^∧` is étale, where `K` is
> the closure of the ideal extended along the canonical map — equivalently the kernel of the
> projection `A^∧ → A ⧸ JA`. These are the stages of `Spf A^∧ ⟶ Spf B`.

```lean
theorem etale_stageMap_canonicalMap (f : B →+* A) (hf : f.Etale)
    (D : QuotientSystem 𝔅 S hS B)
    (E : QuotientSystem 𝔅 S hS (TopologicalRing.CompletionOver f))
    (g : ContinuousHom D E)
    (hg : g.toRingHom = TopologicalRing.CompletionOver.canonicalMap f)
    (J : { J : Ideal B // TopologicalRing.IsWeakIdealOfDefinition J })
    (K : { K : Ideal (TopologicalRing.CompletionOver f) //
      TopologicalRing.IsWeakIdealOfDefinition K })
    (hK : K.1 = (J.1.map g.toRingHom).closure)
    (hJK : J.1 ≤ Ideal.comap g.toRingHom K.1) :
    AlgebraicGeometry.Etale ((BigFppfOver.toScheme 𝔅 S hS).map
      ((BigAffineFppf.inclusion 𝔅 S hS).map (g.stageMap J K hJK)))
```

**`AlgebraicGeometry.FormalSpace.exists_isPullback_etale_formalSpectrumMap_completionOver_of_compactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleCompletionStageBaseChange.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleCompletionStageBaseChange.lean#L194). The attribute's comment: “the base change identification of the proof: for an étale ring map `B → A` and a point of `Spf B` out of a quasi-compact object `T` of the site, `T ×_{Spf B} Spf A^∧` is represented by the object `T ×_{Spec (B ⧸ J)} Spec (A ⧸ JA)` of the site and its projection to `T` is étale. The assertions about the morphism `Spf A^∧ ⟶ Spf B` itself — étaleness at an arbitrary scheme-valued point, full faithfulness, essential surjectivity, the equivalence of categories and the McQuillan conclusion — are not included”.

> **Stacks 0AN8**, the base change identification of its proof. For an étale ring map
> `f : B →+* A` over a weakly admissible `B` and every point `T ⟶ Spf B` whose source is a
> quasi-compact object of the site, the base change `T ×_{Spf B} Spf A^∧` is represented by an
> object `V` of the site, namely `T ×_{Spec (B ⧸ J)} Spec (A ⧸ JA)`, and the projection
> `V ⟶ T` is étale.
>
> The point factors through a stage `Spec (B ⧸ J) ⟶ Spf B` by **Stacks 0AIA**, in the form
> `exists_factorsThroughStage_of_compactSpace`, and the base change along the factorisation is
> `exists_isPullback_etale_formalSpectrumMap_completionOver_of_factorsThroughStage`.

```lean
theorem exists_isPullback_etale_formalSpectrumMap_completionOver_of_compactSpace
    (f : B →+* A) (hf : f.Etale) (hB : TopologicalRing.IsWeaklyAdmissible B)
    (D : QuotientSystem 𝔅 S hS B)
    (E : QuotientSystem 𝔅 S hS (TopologicalRing.CompletionOver f))
    (g : ContinuousHom D E)
    (hg : g.toRingHom = TopologicalRing.CompletionOver.canonicalMap f)
    (U : BigFppfOver 𝔅 S hS) (hU : CompactSpace ((BigFppfOver.toScheme 𝔅 S hS).obj U))
    (a : (Sheaf.sheafifiedYoneda (BigFppfOver.topology 𝔅 S hS)).obj U ⟶ formalSpectrum D) :
    ∃ (V : BigFppfOver 𝔅 S hS) (q : V ⟶ U)
      (r : (Sheaf.sheafifiedYoneda (BigFppfOver.topology 𝔅 S hS)).obj V ⟶ formalSpectrum E),
      IsPullback r ((Sheaf.sheafifiedYoneda (BigFppfOver.topology 𝔅 S hS)).map q)
        (formalSpectrumMap hB g) a ∧
      AlgebraicGeometry.Etale ((BigFppfOver.toScheme 𝔅 S hS).map q)
```

**`AlgebraicGeometry.FormalSpace.isEquivalence_etaleCompletionCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SmallEtaleSite/EtaleCompletionEquivalence.lean, line 412](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SmallEtaleSite/EtaleCompletionEquivalence.lean#L412). The attribute's comment: “the equivalence of categories, with the functor `A^∧ ↦ Spf (A^∧)` and the McQuillan conclusion. The equivalence is realized on the opposite of the category of the algebras `A^∧`, a morphism of that category being a continuous `R`-algebra homomorphism and `Spf` being contravariant; Stacks 0DEF writes the same identification with the opposite taken on the geometric side, and `mcQuillanAffineEtaleEquivalence` moves it there. The quotient system `D` is how this library says that `R` is a topological `S`-algebra, the structure morphisms of the quotient spectra being data here, and without it `Spf R` is not defined; its large-site condition `QuotientSystem.HasLargeSite` says that the chosen big fppf site contains the atlas of `Spf R`, which is what Stacks 0AIF consumes to make `Spf R` an affine formal algebraic space, so it is part of the source's hypothesis that `Y` is one, and is a condition on the site rather than on `R`. It passes to every `A^∧` through Stacks 0ANM. No bound on the cardinality of `R` is assumed”.

> **Stacks 0AN8.** Let `S` be a scheme contained in a big fppf site `B` and let `R` be a
> weakly admissible topological ring presented over `S` by a quotient system `D` whose atlas
> `∐_J Spec (R ⧸ J)` lies in the site, so that `Y = Spf R` is a McQuillan affine formal algebraic
> space over `S`. Then the functor sending an étale `R`-algebra `A` to the morphism
> `Spf (A^∧) ⟶ Spf R` is an equivalence between the opposite of the category of the topological
> `R`-algebras `A^∧ = lim A/JA` and the category of the morphisms `X ⟶ Spf R` of affine formal
> algebraic spaces which are representable by algebraic spaces and étale; in particular every
> such `X` is McQuillan, being `Spf` of the weakly admissible topological ring `A^∧`.
>
> The hypotheses are the source's. The quotient system `D` is how this library says that `R` is a
> topological `S`-algebra — the structure morphisms `Spec (R ⧸ J) ⟶ S` are data here, where the
> source has them from `R` being a topological `S`-algebra — and without it `Spf R` is not
> defined. Its large-site condition `D.HasLargeSite` says that the chosen big fppf site contains
> the atlas of `Spf R`, which is what Stacks 0AIF needs to make `Spf R` an affine formal algebraic
> space at all; so it is part of the hypothesis that `Y` is one, and it is a condition on the site
> rather than on `R`. Through Stacks 0ANM it passes to every `A^∧` with nothing further
> assumed.

```lean
theorem isEquivalence_etaleCompletionCharts :
    (etaleCompletionCharts hR D hD).IsEquivalence ∧
      ∀ W : AffineEtaleFormalCharts B S hS (formalSpectrum D),
        ∃ Y : EtaleCompletion R,
          TopologicalRing.IsWeaklyAdmissible Y.completion ∧
            Nonempty (W.obj.left ≅ formalSpectrum (Y.quotientSystem hR D hD))
```

**`TopologicalRing.existsUnique_algEquiv_of_isWeakIdealOfDefinition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/EtaleLiftRigidity.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/EtaleLiftRigidity.lean#L97). The attribute's comment: “the rigidity step of the essential surjectivity half: for a weak ideal of definition `J₀` and an open ideal `J`, two étale `R ⧸ J`-algebras with identified reductions modulo the image of `J₀` are uniquely isomorphic compatibly with that identification. This is the uniqueness that produces the family `φ_J` of the source's proof; the construction of the étale lift, the identification of the stagewise base changes of a representable étale morphism with the spectra of étale algebras, the equivalence of categories and the McQuillan conclusion are not included”.

> **Stacks 0AN8, the rigidity step `φ_J` of the essential surjectivity half.** Let `J₀` be a
> weak ideal of definition of a topologized commutative ring `R` and let `J` be an open ideal of
> `R`. Two étale `R ⧸ J`-algebras whose reductions modulo the image of `J₀` are identified are
> uniquely isomorphic over `R ⧸ J` compatibly with that identification.
>
> The image of `J₀` in `R ⧸ J` consists of nilpotent elements, a power of a topologically
> nilpotent element lying in the open ideal `J`, so this is rigidity of étale lifts along a
> locally nilpotent ideal. In the source's proof `J ⊆ J₀` and the two étale `R ⧸ J`-algebras both
> reduce to the fixed étale `R ⧸ J₀`-algebra `A₀`.

```lean
theorem existsUnique_algEquiv_of_isWeakIdealOfDefinition {J₀ J : Ideal R}
    (hJ₀ : IsWeakIdealOfDefinition J₀) (hJ : IsOpen (J : Set R))
    (S T : Type*) [CommRing S] [CommRing T] [Algebra (R ⧸ J) S] [Algebra (R ⧸ J) T]
    [Algebra.Etale (R ⧸ J) S] [Algebra.Etale (R ⧸ J) T]
    (e : (S ⧸ (J₀.map (Ideal.Quotient.mk J)).map (algebraMap (R ⧸ J) S)) ≃ₐ[R ⧸ J]
      T ⧸ (J₀.map (Ideal.Quotient.mk J)).map (algebraMap (R ⧸ J) T)) :
    ∃! φ : S ≃ₐ[R ⧸ J] T,
      (Ideal.Quotient.mkₐ (R ⧸ J)
          ((J₀.map (Ideal.Quotient.mk J)).map (algebraMap (R ⧸ J) T))).comp φ.toAlgHom =
        e.toAlgHom.comp (Ideal.Quotient.mkₐ (R ⧸ J)
          ((J₀.map (Ideal.Quotient.mk J)).map (algebraMap (R ⧸ J) S)))
```

**`TopologicalRing.etale_quotientMap_weakIdealOfDefinition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/EtaleModWeakIdeal.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/EtaleModWeakIdeal.lean#L92). The attribute's comment: “first step of the proof: for an étale ring map `B → A` and a weak ideal of definition `J` of `B`, the ring map `B ⧸ J → A ⧸ JA` of quotient stages is étale. The assertions about morphisms of formal spectra — representability, étaleness, full faithfulness, essential surjectivity, the equivalence of categories and the McQuillan conclusion — are not included”.

> **Stacks 0AN8**, first step of the proof.  For an étale ring map `f : B →+* A` and a weak
> ideal of definition `J` of `B`, the induced map `B ⧸ J → A ⧸ JA` is étale.

```lean
public theorem etale_quotientMap_weakIdealOfDefinition {f : B →+* A} (hf : f.Etale)
    (J : WeakIdealOfDefinitionIndex B) :
    (Ideal.quotientMap (extendedIdeal f J) f Ideal.le_comap_map).Etale
```

**`TopologicalRing.exists_etale_surjection_weakIdealOfDefinition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/EtaleModWeakIdeal.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/EtaleModWeakIdeal.lean#L125). The attribute's comment: “the étale-lift step of the essential surjectivity half: for a weak ideal of definition `J₀` of `B` and an étale `B ⧸ J₀`-algebra `A₀`, there is an étale `B`-algebra `C` together with a surjection `C → A₀` compatible with the structure maps whose kernel is the extended ideal `J₀ C`, so that `A₀` is the quotient stage `C ⧸ J₀ C`. This is the existence of the étale lift only; the comparison family `φ_J`, the identification of the stagewise base changes of a representable étale morphism with the spectra of étale algebras, the colimit assembly of the essential surjectivity half, the assertions about morphisms of formal spectra — representability, étaleness, full faithfulness — the equivalence of categories and the McQuillan conclusion are not included”.

> **Stacks 0AN8**, the étale-lift step of the essential surjectivity half.  Let `J₀` be a weak
> ideal of definition of a linearly topologized ring `B` and let `A₀` be an étale `B ⧸ J₀`-algebra.
> Then `A₀` is the quotient stage attached to `J₀` of an étale `B`-algebra: there is an étale
> `B`-algebra `C` and a surjection `ψ : C → A₀` of rings whose kernel is the extended ideal `J₀ C`
> and which is compatible with the two structure maps, so that `A₀ ≅ C ⧸ J₀ C` over `B ⧸ J₀`.
>
> This is the step of the source's proof that produces the étale `B`-algebra from the étale
> `B ⧸ J₀`-algebra `A₀` cut out by the fixed weak ideal of definition `J₀`; the source invokes
> Algebra, Lemma 10.143.10, which this library carries as Stacks 04D1
> (`etale_lift_along_surjection`).  Only the existence of the lift is asserted.  The comparison
> family `φ_J` that the source obtains from uniqueness of étale lifts is
> `TopologicalRing.existsUnique_algEquiv_of_isWeakIdealOfDefinition`; the identification of the
> stagewise base changes of a representable étale morphism with the spectra of étale algebras, the
> colimit assembly `X = Spf A^∧`, and the equivalence of categories are not part of this
> statement.
>
> The conclusion is phrased as a surjection with a named kernel rather than as an isomorphism
> `A₀ ≅ C ⧸ J₀ C`, which is the shape Stacks 04D1 is stated in here; the kernel is spelled with
> this module's `extendedIdeal`.

```lean
public theorem exists_etale_surjection_weakIdealOfDefinition
    (J₀ : WeakIdealOfDefinitionIndex B) (A₀ : Type w) [CommRing A₀]
    [Algebra (B ⧸ (J₀.1 : Ideal B)) A₀] [Algebra.Etale (B ⧸ (J₀.1 : Ideal B)) A₀] :
    ∃ (C : Type u) (_ : CommRing C) (_ : Algebra B C), Algebra.Etale B C ∧
      ∃ ψ : C →+* A₀, Function.Surjective ψ ∧
        RingHom.ker ψ = extendedIdeal (algebraMap B C) J₀ ∧
        ψ.comp (algebraMap B C) =
          (algebraMap (B ⧸ (J₀.1 : Ideal B)) A₀).comp
            (Ideal.Quotient.mk (J₀.1 : Ideal B))
```

**`TopologicalRing.CompletionOver.etale_quotientMap_canonicalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/EtaleModWeakIdeal.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/EtaleModWeakIdeal.lean#L167). The attribute's comment: “first step of the proof, on the stages of the completion: for an étale ring map `B → A` and a weak ideal of definition `J` of `B`, the map `B ⧸ J → A^∧ ⧸ ker (A^∧ → A ⧸ JA)` of quotient stages of the canonical map `B → A^∧` is étale. The assertions about morphisms of formal spectra — representability, étaleness, full faithfulness, essential surjectivity, the equivalence of categories and the McQuillan conclusion — are not included”.

> **Stacks 0AN8**, first step of the proof, on the stages of the completion.  For an étale ring
> map `f : B →+* A` and a weak ideal of definition `J` of `B`, the map
> `B ⧸ J → A^∧ ⧸ ker (A^∧ → A ⧸ JA)` induced by the canonical map `B → A^∧` is étale; the quotient
> stages of `Spf A^∧ ⟶ Spf B` are the spectra of these maps.

```lean
public theorem etale_quotientMap_canonicalMap {f : B →+* A} (hf : f.Etale)
    (J : WeakIdealOfDefinitionIndex B) :
    (Ideal.quotientMap (RingHom.ker (projection f J)) (canonicalMap f)
      (le_comap_ker_projection f J)).Etale
```

## Tag 0AN9, a lemma

[Tag 0AN9](https://stacks.math.columbia.edu/tag/0AN9) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.etaleFormalSpectrumMap_surjective_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSurjective.lean, line 371](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleSurjective.lean#L371).

> Let `R` be a weakly admissible topological ring, let `A` be an étale `R`-algebra and let
> `R → A^∧` be the canonical map to the completion of `A` over `R`, presented by quotient systems
> over a base scheme `S` of a big fppf site. The following are equivalent:
>
> 1. the induced morphism `Spf A^∧ ⟶ Spf R` of formal spectra is surjective;
> 2. `R → A` is faithfully flat;
> 3. `R ⧸ J → A ⧸ JA` is faithfully flat for every weak ideal of definition `J` of `R`;
> 4. `R ⧸ J → A ⧸ JA` is faithfully flat for some weak ideal of definition `J` of `R`.

```lean
public theorem etaleFormalSpectrumMap_surjective_tfae (f : R →+* A)
    (hA : letI : Algebra R A := f.toAlgebra; Algebra.Etale R A)
    (hB : TopologicalRing.IsWeaklyAdmissible R)
    (D : QuotientSystem B S hS R)
    (E : QuotientSystem B S hS (TopologicalRing.CompletionOver f))
    (g : ContinuousHom D E)
    (hg : g.toRingHom = TopologicalRing.CompletionOver.canonicalMap f) :
    List.TFAE
      [ IsSurjective B S hS (formalSpectrumMap hB g),
        f.FaithfullyFlat,
        ∀ J : TopologicalRing.WeakIdealOfDefinitionIndex R,
          (Ideal.quotientMap (J.1.map f) f Ideal.le_comap_map).FaithfullyFlat,
        ∃ J : TopologicalRing.WeakIdealOfDefinitionIndex R,
          (Ideal.quotientMap (J.1.map f) f Ideal.le_comap_map).FaithfullyFlat ]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.19, Tag 0AJG](https://stacks.math.columbia.edu/tag/0AJG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
