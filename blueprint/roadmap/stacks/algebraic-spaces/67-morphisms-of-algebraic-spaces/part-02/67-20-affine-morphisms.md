---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isAffineHom_tfae_of_isAlgebraicSpace, AlgebraicGeometry.Space.presheaf_isAffineHom_iff, AlgebraicGeometry.Space.IsAffineHom, AlgebraicGeometry.Space.isAffineHom_comp, AlgebraicGeometry.Space.IsAffineHom.of_isPullback, AlgebraicGeometry.Space.isAffineHom_of_isClosedImmersion, AlgebraicGeometry.Space.affineOverBaseChangeAlgebraHom_naturality, AlgebraicGeometry.Space.affineOverBaseChangeMap_comp_projection
statement: formalized
proof: formalized
---

# 67.20 Affine morphisms

Section 67.20 of the Stacks Project, [Tag 03WD](https://stacks.math.columbia.edu/tag/03WD). 12 tags here are carried by 27 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03WE, a lemma

[Tag 03WE](https://stacks.math.columbia.edu/tag/03WE) in the Stacks Project.

**`AlgebraicGeometry.Space.isAffineHom_tfae_of_isAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AffineHomEtaleDescent.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AffineHomEtaleDescent.lean#L71). The attribute's comment: “items (1) and (2): affine as a representable morphism iff every base change to”.

> **Stacks 03WG.** For a morphism `f : X ⟶ Y` of algebraic spaces over `S` the following are
> equivalent: `f` is representable and affine as a morphism of presheaves; `f` is affine in the
> sense of Stacks 03WF; for every affine object of the site étale over `Y` the base change of `f`
> is represented by an affine object of the site; there is a surjective étale scheme chart of `Y`
> along which the base change of `f` is affine; and there is a Zariski covering of `Y` over whose
> members the base changes of `f` are affine.
>
> This is `AlgebraicGeometry.Space.isAffineHom_tfae` with its descent hypothesis discharged by
> `AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isAffineHom`.

```lean
theorem isAffineHom_tfae_of_isAlgebraicSpace
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) :
    List.TFAE [
      (yoneda.relativelyRepresentable f ∧
        (MorphismProperty.inverseImage
          (@_root_.AlgebraicGeometry.IsAffineHom.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf f),
      IsAffineHom B S hS f,
      (∀ (V : BigAffineFppf B S hS)
        (g : yoneda.obj ((BigAffineFppf.inclusion B S hS).obj V) ⟶ Y),
        IsEtale B S hS g →
          ∃ (W : BigAffineFppf B S hS)
            (p : yoneda.obj ((BigAffineFppf.inclusion B S hS).obj W) ⟶ X)
            (q : (BigAffineFppf.inclusion B S hS).obj W ⟶
              (BigAffineFppf.inclusion B S hS).obj V),
            IsPullback p (yoneda.map q) f g),
      (∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
        IsSurjective B S hS g ∧
        IsEtale B S hS g ∧
        IsAffineHom B S hS (pullback.snd f g)),
      (∃ (I : Type u) (U : I → Subfunctor Y),
        IsZariskiCover B S hS I U ∧
        ∀ i, IsAffineHom B S hS (pullback.snd f (U i).ι))]
```

**`AlgebraicGeometry.Space.presheaf_isAffineHom_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AffineHomEtaleDescent.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AffineHomEtaleDescent.lean#L116).

> **Stacks 03WE.** Let `f : X ⟶ Y` be a representable morphism of algebraic spaces over a
> scheme `S`. Then `f` is affine in the sense of Stacks 03HA — every represented base change of
> `f` is an affine morphism of schemes — if and only if for every affine object `Z` of the site
> and every morphism `yoneda.obj Z ⟶ Y` the fibre product `X ×_Y Z` is represented by an affine
> object of the site.
>
> The right-hand side is `AlgebraicGeometry.Space.IsAffineHom`, Stacks 03WF, with its
> abbreviation unfolded, so that the quantifier over the test object stands in the statement: it
> ranges over *all* morphisms from an affine object of the site, not over the étale ones alone.
> That is what separates it from condition (3) of
> `AlgebraicGeometry.Space.isAffineHom_tfae_of_isAlgebraicSpace`, which is the same condition
> restricted to the étale test morphisms.
>
> The equivalence is the one between conditions (1) and (2) of that theorem, whose condition (1)
> conjoins representability to the Stacks 03HA condition; representability is the hypothesis `hf`
> of the source here, and `MorphismProperty.presheaf` carries it on the left anyway.

```lean
theorem presheaf_isAffineHom_iff
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : yoneda.relativelyRepresentable f) :
    (MorphismProperty.inverseImage
        (@_root_.AlgebraicGeometry.IsAffineHom.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf f ↔
      ∀ (Z : BigAffineFppf B S hS)
        (g : yoneda.obj ((BigAffineFppf.inclusion B S hS).obj Z) ⟶ Y),
        ∃ (W : BigAffineFppf B S hS)
          (p : yoneda.obj ((BigAffineFppf.inclusion B S hS).obj W) ⟶ X)
          (q : (BigAffineFppf.inclusion B S hS).obj W ⟶
            (BigAffineFppf.inclusion B S hS).obj Z),
          IsPullback p (yoneda.map q) f g
```

## Tag 03WF, a definition

[Tag 03WF](https://stacks.math.columbia.edu/tag/03WF) in the Stacks Project.

**`AlgebraicGeometry.Space.IsAffineHom`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Affine.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Affine.lean#L40).

> A morphism of algebraic spaces is affine if each base change to an affine scheme is
> represented by an affine scheme.

```lean
abbrev IsAffineHom {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : F ⟶ G) : Prop
```

## Tag 03WG, a lemma

[Tag 03WG](https://stacks.math.columbia.edu/tag/03WG) in the Stacks Project.

**`AlgebraicGeometry.Space.isAffineHom_tfae_of_isAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AffineHomEtaleDescent.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AffineHomEtaleDescent.lean#L71).

> **Stacks 03WG.** For a morphism `f : X ⟶ Y` of algebraic spaces over `S` the following are
> equivalent: `f` is representable and affine as a morphism of presheaves; `f` is affine in the
> sense of Stacks 03WF; for every affine object of the site étale over `Y` the base change of `f`
> is represented by an affine object of the site; there is a surjective étale scheme chart of `Y`
> along which the base change of `f` is affine; and there is a Zariski covering of `Y` over whose
> members the base changes of `f` are affine.
>
> This is `AlgebraicGeometry.Space.isAffineHom_tfae` with its descent hypothesis discharged by
> `AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isAffineHom`.

```lean
theorem isAffineHom_tfae_of_isAlgebraicSpace
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) :
    List.TFAE [
      (yoneda.relativelyRepresentable f ∧
        (MorphismProperty.inverseImage
          (@_root_.AlgebraicGeometry.IsAffineHom.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf f),
      IsAffineHom B S hS f,
      (∀ (V : BigAffineFppf B S hS)
        (g : yoneda.obj ((BigAffineFppf.inclusion B S hS).obj V) ⟶ Y),
        IsEtale B S hS g →
          ∃ (W : BigAffineFppf B S hS)
            (p : yoneda.obj ((BigAffineFppf.inclusion B S hS).obj W) ⟶ X)
            (q : (BigAffineFppf.inclusion B S hS).obj W ⟶
              (BigAffineFppf.inclusion B S hS).obj V),
            IsPullback p (yoneda.map q) f g),
      (∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
        IsSurjective B S hS g ∧
        IsEtale B S hS g ∧
        IsAffineHom B S hS (pullback.snd f g)),
      (∃ (I : Type u) (U : I → Subfunctor Y),
        IsZariskiCover B S hS I U ∧
        ∀ i, IsAffineHom B S hS (pullback.snd f (U i).ι))]
```

## Tag 03WH, a lemma

[Tag 03WH](https://stacks.math.columbia.edu/tag/03WH) in the Stacks Project.

**`AlgebraicGeometry.Space.isAffineHom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Affine.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Affine.lean#L50).

> The composition of affine morphisms is affine.

```lean
theorem isAffineHom_comp
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : F ⟶ G) (g : G ⟶ H)
    (hf : IsAffineHom B S hS f) (hg : IsAffineHom B S hS g) :
    IsAffineHom B S hS (f ≫ g)
```

## Tag 03WI, a lemma

[Tag 03WI](https://stacks.math.columbia.edu/tag/03WI) in the Stacks Project.

**`AlgebraicGeometry.Space.IsAffineHom.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineHomTfae.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineHomTfae.lean#L76).

> Affineness of a morphism of algebraic spaces over `S` is stable under base change: if `f'`
> sits in a Cartesian square over `f`, then `f'` is affine as soon as `f` is.

```lean
theorem IsAffineHom.of_isPullback {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {f : X ⟶ Y} {g : Y' ⟶ Y} {k : X' ⟶ X} {f' : X' ⟶ Y'} (sq : IsPullback k f' f g)
    (hf : IsAffineHom B S hS f) : IsAffineHom B S hS f'
```

## Tag 07U2, a lemma

[Tag 07U2](https://stacks.math.columbia.edu/tag/07U2) in the Stacks Project.

**`AlgebraicGeometry.Space.isAffineHom_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersions.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersions.lean#L91). References: EGA II (1.2.2).

> A closed immersion of algebraic spaces is affine.

```lean
theorem isAffineHom_of_isClosedImmersion
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : F ⟶ G)
    (hf : IsClosedImmersion B S hS f) :
    IsAffineHom B S hS f
```

## Tag 081V, a lemma

[Tag 081V](https://stacks.math.columbia.edu/tag/081V) in the Stacks Project.

**`AlgebraicGeometry.Space.affineOverBaseChangeAlgebraHom_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineOverBaseChangeAlgebraNaturality.lean, line 482](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineOverBaseChangeAlgebraNaturality.lean#L482). The attribute's comment: “naturality in Z of the base-change comparison g^*(f\_* 𝒪\_Z) ⟶ f'\_* 𝒪\_\{Y ×\_X Z}”.

> **The base-change comparison of `𝒪_Y`-algebras is natural in the algebraic space affine over
> `X`.**  For a morphism `φ : Z₁ ⟶ Z₂` of algebraic spaces affine over `X`, the square
>
> ```
> g^* (f₂_* 𝒪_{Z₂}) ⟶ (f₂')_* 𝒪_{Y ×_X Z₂}
>        ↓                       ↓
> g^* (f₁_* 𝒪_{Z₁}) ⟶ (f₁')_* 𝒪_{Y ×_X Z₁}
> ```
>
> of `𝒪_Y`-algebras commutes, the vertical maps being the pullback of the direct-image map of `φ`
> and the direct-image map of its base change.

```lean
theorem affineOverBaseChangeAlgebraHom_naturality (g : Y ⟶ X) {Z₁ Z₂ : AffineOver B S hS X}
    (φ : Z₁ ⟶ Z₂) :
    (algebraPullback B S hS g).map (pushforwardAlgebraMap B S hS φ.hom) ≫
        affineOverBaseChangeAlgebraHom B S hS g Z₁ =
      affineOverBaseChangeAlgebraHom B S hS g Z₂ ≫
        pushforwardAlgebraMap B S hS (affineOverBaseChangeMap B S hS g φ).hom
```

**`AlgebraicGeometry.Space.affineOverBaseChangeMap_comp_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineOverBaseChangeFunctor.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineOverBaseChangeFunctor.lean#L149). The attribute's comment: “naturality of the projections of the geometric base change Y ×\_X Z ⟶ Z in Z; the anti-equivalence of the tag and its compatibility with base change are not proved”.

> **The projections of the geometric base change are natural in the affine algebraic space
> being base-changed.**
>
> This has exactly the type of the `affineBaseChange_projection_naturality` field of
> `AlgebraicGeometry.Space.BaseChangeCompatibility`, and is proved with no anti-equivalence and
> no base-change compatibility: it is the defining property of
> `AlgebraicGeometry.Space.affineOverBaseChangeMap`.

```lean
theorem affineOverBaseChangeMap_comp_projection (g : Y ⟶ X) {Z Z' : AffineOver B S hS X}
    (φ : Z ⟶ Z') :
    (affineOverBaseChangeMap B S hS g φ).hom.left ≫
        affineOverBaseChangeProjection B S hS g Z' =
      affineOverBaseChangeProjection B S hS g Z ≫ φ.hom.left
```

**`AlgebraicGeometry.Space.affineOverBaseChangeFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineOverBaseChangeFunctor.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineOverBaseChangeFunctor.lean#L166). The attribute's comment: “base change of the algebraic spaces affine over X as a functor; the anti-equivalence of the tag and its compatibility with base change are not proved”.

> **Base change of the algebraic spaces affine over `X`, as a functor
> `AffineOver X ⥤ AffineOver Y`.**
>
> On objects it is `AlgebraicGeometry.Space.affineOverBaseChange` and on morphisms
> `AlgebraicGeometry.Space.affineOverBaseChangeMap`.  This has exactly the type of the
> `affineBaseChange` field of `AlgebraicGeometry.Space.BaseChangeCompatibility`, of which
> `StacksFrontier.AlgebraicGeometry.Spaces.BoundedDirectImageAlgebraFactorization` constructs only
> the action on objects.

```lean
def affineOverBaseChangeFunctor (g : Y ⟶ X) :
    AffineOver B S hS X ⥤ AffineOver B S hS Y
```

**`AlgebraicGeometry.Space.faithful_affinePushforwardAlgebraFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffinePushforwardAlgebraFunctorFullyFaithful.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffinePushforwardAlgebraFunctorFullyFaithful.lean#L56). The attribute's comment: “faithfulness of the direct image functor f ↦ f\_* 𝒪\_Y from the algebraic spaces affine over X; the corrected anti-equivalence and the base-change compatibility as a whole are affineAlgebraAntiEquivalence\_bounded”.

> **The direct-image functor `f ↦ f_* 𝒪_Y` of Stacks 081V is faithful.**
>
> This is the faithfulness half of the anti-equivalence clause of the tag, and no more: the functor
> is not shown full by this statement — that is
> `AlgebraicGeometry.Space.full_affinePushforwardAlgebraFunctor` below — nor essentially surjective,
> and nothing is proved about the tag's compatibility with base change.
> `AlgebraicGeometry.Space.eq_of_pushforwardRingMap_eq` is the content;
> `AlgebraicGeometry.Space.faithful_affinePushforwardAlgebraFunctor_iff` is what strips the two full
> subcategories and the opposite category off it.
>
> Restricting the target to the bounded quasi-coherent algebras changes nothing, by
> `AlgebraicGeometry.Space.faithful_boundedPushforwardAlgebraFunctor_iff`.

```lean
theorem faithful_affinePushforwardAlgebraFunctor (X : AlgebraicSpaces B S hS) :
    (quasicoherentPushforwardAlgebraFunctor B S hS X).Faithful
```

**`AlgebraicGeometry.Space.full_affinePushforwardAlgebraFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffinePushforwardAlgebraFunctorFullyFaithful.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffinePushforwardAlgebraFunctorFullyFaithful.lean#L77). The attribute's comment: “fullness of the direct image functor f ↦ f\_* 𝒪\_Y from the algebraic spaces affine over X; the corrected anti-equivalence and the base-change compatibility as a whole are affineAlgebraAntiEquivalence\_bounded”.

> **The direct-image functor `f ↦ f_* 𝒪_Y` of Stacks 081V is full.**
>
> This is the fullness half of the anti-equivalence clause of the tag, and no more: nothing is
> proved here about the functor's essential surjectivity, which would need the relative spectrum of
> a quasi-coherent algebra, nor about the tag's compatibility with base change.
> `AlgebraicGeometry.Space.exists_pushforwardAlgebraMap_eq` is the content;
> `AlgebraicGeometry.Space.full_affinePushforwardAlgebraFunctor_iff` is what strips the two full
> subcategories and the opposite category off it.
>
> Faithfulness is `AlgebraicGeometry.Space.faithful_affinePushforwardAlgebraFunctor`, so the two
> together make the functor fully faithful, and clause (a) of
> `AlgebraicGeometry.Space.isEquivalence_boundedPushforwardAlgebraFunctor_iff_bijective` — that
> `f ↦ f_*` be bijective — is delivered.

```lean
theorem full_affinePushforwardAlgebraFunctor (X : AlgebraicSpaces B S hS) :
    (quasicoherentPushforwardAlgebraFunctor B S hS X).Full
```

**`AlgebraicGeometry.Space.algebraPullback_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlgebraPullbackQuasicoherent.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlgebraPullbackQuasicoherent.lean#L166). The attribute's comment: “the algebraPullback\_isQuasicoherent clause”.

> **The pullback of a quasi-coherent algebra sheaf along a morphism of algebraic spaces is
> quasi-coherent.**
>
> This is the `algebraPullback_isQuasicoherent` field of
> `AlgebraicGeometry.Space.BaseChangeCompatibility`, at
> `AlgebraicGeometry.Space.algebraPullback`.

```lean
theorem algebraPullback_isQuasicoherent (g : Y ⟶ X)
    (A : AlgebraSheaf.{u, u} B S hS X.1 X.2) (hA : A.IsQuasicoherent) :
    ((algebraPullback B S hS g).obj A).IsQuasicoherent
```

**`AlgebraicGeometry.Space.boundedPushforwardAlgebraFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BoundedAffineAlgebraAntiEquivalence.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BoundedAffineAlgebraAntiEquivalence.lean#L176). The attribute's comment: “the direct image functor f ↦ f\_* 𝒪\_Y from the algebraic spaces affine over X, in the corrected form with the target restricted to the quasi-coherent 𝒪\_X-algebras whose sections at every étale chart of X number fewer than the big fppf site's cutoff — the bound the direct image of an affine morphism satisfies by construction, and which the tag's unrestricted target fails (not\_essSurj\_affinePushforwardAlgebraFunctor\_of\_cutoff\_le\_mk\_sections). This registration is the functor itself; its faithfulness, fullness and essential surjectivity are faithful\_affinePushforwardAlgebraFunctor, full\_affinePushforwardAlgebraFunctor and essSurj\_boundedPushforwardAlgebraFunctor (via boundedRelativeSpec, Stacks 081W), and the base-change compatibility is the subject of the other 081V registrations”. References: SGA 3 III (0.1.7), “more general”.

> The contravariant functor `f ↦ f_* 𝒪_Y` from the algebraic spaces affine over `X` to the
> quasi-coherent sheaves of commutative `𝒪_X`-algebras *whose sections at every étale chart of `X`
> are fewer than the cutoff of the ambient big fppf site*.

```lean
def boundedPushforwardAlgebraFunctor (X : AlgebraicSpaces B S hS) :
    (AffineOver B S hS X)ᵒᵖ ⥤ BoundedQuasicoherentAlgebra B S hS X
```

**`AlgebraicGeometry.Space.affineAlgebraAntiEquivalence_bounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BoundedAffineAlgebraAntiEquivalenceProof.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BoundedAffineAlgebraAntiEquivalenceProof.lean#L107). The attribute's comment: “corrected form: f ↦ f\_* 𝒪\_Y is an anti-equivalence from the algebraic spaces affine over X onto the quasi-coherent 𝒪\_X-algebras with fewer than the big fppf site's cutoff many sections over every étale chart (the unrestricted target is refuted by not\_nonempty\_affineAlgebraAntiEquivalence\_of\_hasNonzeroAffineChart, and the bounded algebras are exactly the essential image by essImage\_boundedPushforwardAlgebraFunctor\_iff), and it commutes with arbitrary base change g : Y ⟶ X, naturally in the affine space”.

> For every algebraic space `X`, the direct image
> `f ↦ f_* 𝒪_Y` is an anti-equivalence from the algebraic spaces affine over `X` onto the
> quasi-coherent `𝒪_X`-algebras with fewer than the big fppf site's cutoff many sections over every
> étale chart; and for every morphism `g : Y ⟶ X` of algebraic spaces the direct image commutes with
> base change along `g`, naturally in the affine space.

```lean
theorem affineAlgebraAntiEquivalence_bounded :
    (∀ X : AlgebraicSpaces B S hS, (boundedPushforwardAlgebraFunctor B S hS X).IsEquivalence) ∧
      ∀ {X Y : AlgebraicSpaces B S hS} (g : Y ⟶ X),
        Nonempty (quasicoherentPushforwardAlgebraFunctor B S hS X ⋙
            quasicoherentAlgebraPullback B S hS g ≅
          (affineOverBaseChangeFunctor B S hS g).op ⋙
            quasicoherentPushforwardAlgebraFunctor B S hS Y)
```

**`AlgebraicGeometry.Space.pushforwardAlgebraMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DirectImageAlgebraMorphism.lean, line 626](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DirectImageAlgebraMorphism.lean#L626). The attribute's comment: “the direct image f ↦ f\_* 𝒪\_Y on morphisms, as a map of 𝒪\_X-algebras”.

> **The contravariant action of `f ↦ f_* 𝒪_Y` on morphisms, as a morphism of
> `𝒪_X`-algebras.**  A morphism `f : Y ⟶ Z` of algebraic spaces over `X` induces
> `f_* : Z.hom_* 𝒪_Z ⟶ Y.hom_* 𝒪_Y`, and that map of sheaves of commutative rings carries the
> structure-algebra map of the first to the structure-algebra map of the second.
>
> This is one piece of Stacks 081V: the functor of the anti-equivalence on morphisms.  It is
> functorial, by `AlgebraicGeometry.Space.pushforwardAlgebraMap_id` and
> `AlgebraicGeometry.Space.pushforwardAlgebraMap_comp`, and
> `AlgebraicGeometry.Space.pushforwardAlgebraFunctor` is the functor they assemble; the
> anti-equivalence itself is not constructed, see the implementation notes of this file.

```lean
def pushforwardAlgebraMap (f : Y ⟶ Z) :
    pushforwardAlgebra B S hS Z ⟶ pushforwardAlgebra B S hS Y
```

**`AlgebraicGeometry.Space.pushforwardAlgebraFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DirectImageAlgebraMorphism.lean, line 780](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DirectImageAlgebraMorphism.lean#L780). The attribute's comment: “the direct image functor f ↦ f\_* 𝒪\_Y”.

> **The direct-image functor of Stacks 081V.**  The contravariant functor from the algebraic
> spaces over `X` to the sheaves of commutative `𝒪_X`-algebras which sends `f : Y ⟶ X` to
> `f_* 𝒪_Y` and a morphism over `X` to the map it induces on direct images.
>
> This is the functor of Stacks 081V on the whole over-category rather than on
> `AlgebraicGeometry.Space.AffineOver X`, and with values in all algebra sheaves rather than in
> `AlgebraicGeometry.Space.QuasicoherentAlgebra X`: quasi-coherence of `f_* 𝒪_Y` for a
> quasi-compact, quasi-separated `f` is Stacks 03M9, which is stated nowhere in this development,
> so restricting the codomain is not available.  It is *not* shown to be an anti-equivalence; see
> the implementation notes of this file.

```lean
noncomputable def pushforwardAlgebraFunctor :
    (Over X)ᵒᵖ ⥤ AlgebraSheaf.{u, u} B S hS X.1 X.2
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.affineQuasicoherentPushforwardAlgebraFunctor`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineQuasicoherentPushforwardAlgebra.lean#L83), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/AffinePushforwardQuasicoherentAlgebra.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffinePushforwardQuasicoherentAlgebra.lean#L87) (StacksFrontier): “the direct image functor f ↦ f\_* 𝒪\_Y on the algebraic spaces affine over X, with values in the quasi-coherent 𝒪\_X-algebras”.

## Tag 081W, a definition

[Tag 081W](https://stacks.math.columbia.edu/tag/081W) in the Stacks Project.

**`AlgebraicGeometry.Space.relativeSpectrum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeSpectrum.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeSpectrum.lean#L232). The attribute's comment: “the relative spectrum Spec\_X(A) of an arbitrary quasi-coherent O\_X-algebra A on an algebraic space X, with no further hypothesis: the algebraic space affine over X corresponding to A under 081V. It lives on an enlargement relativeSpectrumSite A of the big fppf site of X (Stacks 03FO; necessary, since an algebra with at least B.cutoff sections over a chart is the direct image of no space affine over X in the same site: not\_essSurj\_affinePushforwardAlgebraFunctor\_of\_cutoff\_le\_mk\_sections), over X read there by 03FP; its direct image is A read there (pushforwardAlgebraRelativeSpectrumIso, relativeSpectrumRestrictIso) and it is unique up to unique isomorphism with that property (existsUnique\_iso\_relativeSpectrum)”.

> **Stacks 081W.** The relative spectrum `\underline{Spec}_X(𝒜)` of an arbitrary quasi-coherent
> sheaf of `𝒪_X`-algebras `𝒜` on an algebraic space `X`: the algebraic space affine over `X`
> corresponding to `𝒜` under the anti-equivalence of Stacks 081V.
>
> **Where it lives.** It is an algebraic space of the big fppf site
> `AlgebraicGeometry.Space.relativeSpectrumSite 𝒜`, a big fppf site containing the site `B` of `X`,
> and it is affine over `AlgebraicGeometry.Space.relativeSpectrumBase 𝒜`, which is `X` read in that
> site (Stacks 03FP, `AlgebraicGeometry.changeBigSite`). It cannot in general live in `B` itself:
> an algebra with at least `B.cutoff` sections over an étale chart is the direct image of no
> algebraic space of `B` affine over `X`
> (`AlgebraicGeometry.Space.not_essSurj_affinePushforwardAlgebraFunctor_of_cutoff_le_mk_sections`,
> `AlgebraicGeometry.Space.exists_quasicoherentAlgebra_cutoff_le_mk_sections`), so the site is
> enlarged, as Stacks 03FO allows, past the cardinality of the sections of `𝒜`.
>
> **What it is.** It is the object of Stacks 081V over the enlarged site corresponding to
> `AlgebraicGeometry.Space.relativeSpectrumAlgebra 𝒜`, which is `𝒜` read on the small étale site of
> `X` enlarged (its sections over the charts of `X` are those of `𝒜`,
> `AlgebraicGeometry.Space.relativeSpectrumRestrictIso`): its direct image is that algebra
> (`AlgebraicGeometry.Space.pushforwardAlgebraRelativeSpectrumIso`) and it is unique up to unique
> isomorphism with that property (`AlgebraicGeometry.Space.existsUnique_iso_relativeSpectrum`).
> When `𝒜` is bounded it is the relative spectrum `AlgebraicGeometry.Space.boundedRelativeSpec`
> built inside the site of `X`, read in the enlarged site
> (`AlgebraicGeometry.Space.nonempty_iso_changeBigSite_boundedRelativeSpec`).
>
> No hypothesis is placed on `𝒜` beyond quasi-coherence. This is the only declaration registered
> as Stacks 081W; the bounded construction `AlgebraicGeometry.Space.boundedRelativeSpec` and the
> value `AlgebraicGeometry.Space.relativeSpec` of a given anti-equivalence are not.

```lean
def relativeSpectrum (A : QuasicoherentAlgebra B S hS X) :
    AffineOver (relativeSpectrumSite A) S (contains_relativeSpectrumSite A)
      (relativeSpectrumBase A)
```

## Tag 081X, a remark

[Tag 081X](https://stacks.math.columbia.edu/tag/081X) in the Stacks Project.

**`AlgebraicGeometry.Space.directImageSpec_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DirectImageSpecFactorization.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DirectImageSpecFactorization.lean#L101). The attribute's comment: “quasi-coherence of f\_* 𝒪\_Y, the factorization Y → Spec\_X(f\_* 𝒪\_Y) → X, and its canonicity”. References: SGA 3 VIB (11.1), “partial”.

> **The canonical factorization through the relative spectrum of `f_* 𝒪_Y`.**  Let `f : Y ⟶ X`
> be a quasi-compact, quasi-separated morphism of algebraic spaces.  Then `f_* 𝒪_Y` is a
> quasi-coherent `𝒪_X`-algebra, and `f` factors as `Y ⟶ \underline{Spec}_X(f_* 𝒪_Y) ⟶ X` through
> the canonical morphism `AlgebraicGeometry.Space.toDirectImageSpec`, which is the unique morphism
> over `X` whose direct-image map is the identification `\underline{Spec}_X(f_* 𝒪_Y)_* 𝒪 ≅ f_* 𝒪_Y`.
>
> The relative spectrum is that of `AlgebraicGeometry.Space.boundedRelativeSpec`, and the size
> condition it needs is proved for `f_* 𝒪_Y` by
> `AlgebraicGeometry.Space.sectionsBelowCutoff_pushforwardAlgebra`, so nothing beyond the
> hypotheses of Stacks 081X is assumed.

```lean
theorem directImageSpec_factorization :
    (pushforwardAlgebra B S hS (Over.mk f)).IsQuasicoherent ∧
      (toDirectImageSpec B S hS f hfqc hfqs).left ≫ (directImageSpec B S hS f hfqc hfqs).obj.hom =
        f ∧
      ∀ g : Over.mk f ⟶ (directImageSpec B S hS f hfqc hfqs).obj,
        g = toDirectImageSpec B S hS f hfqc hfqs ↔
          pushforwardAlgebraMap B S hS g = (directImageSpecIso B S hS f hfqc hfqs).hom
```

## Tag 08AI, a lemma

[Tag 08AI](https://stacks.math.columbia.edu/tag/08AI) in the Stacks Project.

**`AlgebraicGeometry.Space.isEquivalence_affineQuasicoherentDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineDirectImageEquivalence.lean, line 514](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineDirectImageEquivalence.lean#L514). The attribute's comment: “the functor F ↦ f\_*F from quasi-coherent 𝒪\_Y-modules to quasi-coherent f\_*𝒪\_Y-modules is an equivalence of categories, for an affine morphism”.

> **Stacks 08AI, first assertion.**  Let `f : Y ⟶ X` be an affine morphism of algebraic spaces
> over `S` and `𝒜 = f_*𝒪_Y`.  The functor `ℱ ↦ f_*ℱ` from quasi-coherent `𝒪_Y`-modules to
> quasi-coherent `𝒜`-modules is an equivalence of categories.
>
> The functor is `AlgebraicGeometry.Space.affineQuasicoherentDirectImage`, which is the direct image
> of Stacks 03D1 on the nose (`AlgebraicGeometry.Space.affineQuasicoherentDirectImage_comp_ι`); its
> quasi-inverse is `𝒢 ↦ 𝒪_Y ⊗_{f⁻¹𝒜} f⁻¹𝒢`.  The second assertion of the tag is
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_restrictScalars_structureSharp_iff`.

```lean
theorem isEquivalence_affineQuasicoherentDirectImage (hf : IsAffineHom B S hS f.hom) :
    (affineQuasicoherentDirectImage B S hS f hf).IsEquivalence
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_restrictScalars_structureSharp_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DirectImageAlgebraQuasicoherenceCriterion.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DirectImageAlgebraQuasicoherenceCriterion.lean#L87). The attribute's comment: “an 𝒜-module is quasi-coherent as an 𝒪\_X-module if and only if it is quasi-coherent as an 𝒜-module”.

> **Stacks 08AI, second assertion.**  Let `f : Y ⟶ X` be an affine morphism of algebraic spaces
> over `S` and let `𝒜 = f_*𝒪_Y`.  An `𝒜`-module is quasi-coherent as an `𝒪_X`-module — that is,
> after restriction of scalars along the structure map `f♯ : 𝒪_X ⟶ 𝒜` of Stacks 03G8 — if and only
> if it is quasi-coherent as an `𝒜`-module.
>
> This is `AlgebraicGeometry.Space.isQuasicoherentOnSite_restrictScalars_iff` at `A = f_*𝒪_Y`,
> whose quasi-coherence as an `𝒪_X`-module is
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_restrictScalars_structureRingSheafDirectImage`,
> the first assertion of Stacks 07U8 at the structure sheaf.

```lean
theorem isQuasicoherentOnSite_restrictScalars_structureSharp_iff (f : Y ⟶ X)
    (hf : IsAffineHom B S hS f.hom)
    (M : SheafOfModules.{u} (structureRingSheafDirectImage B S hS f)) :
    ((SheafOfModules.restrictScalars.{u} (structureSharp B S hS f)).obj
        M).IsQuasicoherentOnSite ↔ M.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.quasicoherentDirectImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDirectImageAffine.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentDirectImageAffine.lean#L102). The attribute's comment: “the functor F ↦ f\_*F on quasi-coherent modules”.

> **Stacks 08AI, the functor.** Direct image as a functor `QCoh(𝒪_Y) ⥤ QCoh(A)`, granted
> that it preserves quasi-coherence. This is the functor `F ↦ f_*F` whose invertibility is the
> first sentence of the tag.

```lean
noncomputable def quasicoherentDirectImage (f : Y ⟶ X)
    (hqc : DirectImagePreservesQuasicoherence B S hS f) :
    QuasicoherentSheaves.{u, u} B S hS Y.1 Y.2 ⥤
      (SheafOfModules.isQuasicoherentOnSite (affineDirectImageAlgebra B S hS f)).FullSubcategory
```

## Tag 08GB, a lemma

[Tag 08GB](https://stacks.math.columbia.edu/tag/08GB) in the Stacks Project.

**`AlgebraicGeometry.Space.isAffineHom_of_isAffineHom_comp_of_isAffineHom_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/AffineDiagonal.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/AffineDiagonal.lean#L96). The attribute's comment: “part (1)”.

> Let `X ⟶ Y ⟶ T` be morphisms of presheaves on the big fppf site of `S`. If the composite
> `X ⟶ T` is affine and the relative diagonal of `Y ⟶ T` is affine, then `X ⟶ Y` is affine.

```lean
theorem isAffineHom_of_isAffineHom_comp_of_isAffineHom_diagonal
    {X Y T : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y) (g : Y ⟶ T)
    (hfg : IsAffineHom B S hS (f ≫ g))
    (hΔ : IsAffineHom B S hS (pullback.diagonal g)) :
    IsAffineHom B S hS f
```

**`AlgebraicGeometry.Space.isAffineHom_of_isAffineHom_comp_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/AffineDiagonal.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/AffineDiagonal.lean#L110). The attribute's comment: “part (2)”.

> Let `X ⟶ Y ⟶ T` be morphisms of presheaves on the big fppf site of `S`. If the composite
> `X ⟶ T` is affine and `Y ⟶ T` is separated, then `X ⟶ Y` is affine.

```lean
theorem isAffineHom_of_isAffineHom_comp_of_isSeparated
    {X Y T : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y) (g : Y ⟶ T)
    (hfg : IsAffineHom B S hS (f ≫ g)) (hg : IsSeparated B S hS g) :
    IsAffineHom B S hS f
```

**`AlgebraicGeometry.Space.isAffineHom_of_affine_source_of_isAffineHom_diag`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/AffineDiagonal.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/AffineDiagonal.lean#L223). The attribute's comment: “part (3)”. References: EGA II (1.6.3).

> A morphism from an affine object of the big fppf site of `S` to a presheaf whose absolute
> diagonal, in the sense of Stacks 03BS, is affine is affine.

```lean
theorem isAffineHom_of_affine_source_of_isAffineHom_diag
    {Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (X : BigAffineFppf B S hS)
    (f : yoneda.obj ((BigAffineFppf.inclusion B S hS).obj X) ⟶ Y)
    (hΔ : IsAffineHom B (⊤_ Scheme.{u}) hZ (diag (viewOverIntegers B S hS hZ Y))) :
    IsAffineHom B S hS f
```

**`AlgebraicGeometry.Space.isAffineHom_of_affine_source_of_isAbsolutelySeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/AffineDiagonal.lean, line 266](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/AffineDiagonal.lean#L266). The attribute's comment: “part (4)”. References: EGA II (1.6.3).

> A morphism from an affine object of the big fppf site of `S` to a separated algebraic space,
> in the absolute sense of Stacks 03BS, is affine: its absolute diagonal is a closed immersion,
> hence affine by Stacks 07U2.

```lean
theorem isAffineHom_of_affine_source_of_isAbsolutelySeparated
    {Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (X : BigAffineFppf B S hS)
    (f : yoneda.obj ((BigAffineFppf.inclusion B S hS).obj X) ⟶ Y)
    (hsep : IsAbsolutelySeparated B S hS hZ Y) :
    IsAffineHom B S hS f
```

## Tag 09TF, a lemma

[Tag 09TF](https://stacks.math.columbia.edu/tag/09TF) in the Stacks Project.

**`AlgebraicGeometry.Space.isAffineHom_of_isArtinianRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/AffineArtinian.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/AffineArtinian.lean#L113).

> **Stacks 09TF.** A morphism from the spectrum of an Artinian ring to a quasi-separated
> algebraic space is affine.
>
> Following the source: for an étale morphism from an affine scheme `V ⟶ X`, the fibre product
> `Spec(A) ×_X V` is quasi-compact because `X` is quasi-separated, and étale over `Spec(A)`, whose
> topology is discrete; so it is a scheme with finite discrete underlying space, hence affine.

```lean
theorem isAffineHom_of_isArtinianRing
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    (F : (AlgebraicGeometry.BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : AlgebraicGeometry.IsAlgebraicSpace B S hS F)
    (hqs : AlgebraicGeometry.Space.IsAbsolutelyQuasiSeparated B S hS hZ F)
    (A : CommRingCat.{u}) [IsArtinianRing A]
    (hA : B.Contains (Spec A)) (p : B.obj hA ⟶ B.obj hS)
    (f : yoneda.obj (Over.mk p) ⟶ F) :
    AlgebraicGeometry.Space.IsAffineHom B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.20, Tag 03WD](https://stacks.math.columbia.edu/tag/03WD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
