---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsEtaleAt, AlgebraicGeometry.Space.isEtale_local_tfae, AlgebraicGeometry.Space.isEtale_comp, AlgebraicGeometry.Space.isEtale_of_isPullback, AlgebraicGeometry.Space.isLocallyQuasiFinite_of_isEtale, AlgebraicGeometry.Space.isSmooth_of_isEtale, AlgebraicGeometry.Space.isFlat_of_isEtale, AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_isEtale
statement: formalized
proof: formalized
---

# 67.39 Étale morphisms

Section 67.39 of the Stacks Project, [Tag 03XS](https://stacks.math.columbia.edu/tag/03XS). 12 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04RH, a definition

[Tag 04RH](https://stacks.math.columbia.edu/tag/04RH) in the Stacks Project.

**`AlgebraicGeometry.Space.IsEtaleAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/EtaleAtPoint.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/EtaleAtPoint.lean#L41).

> A morphism of algebraic spaces is étale at a point if it is étale on an open subspace
> containing that point.

```lean
abbrev IsEtaleAt (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (x : points B S hS X) : Prop
```

## Tag 03XT, a lemma

[Tag 03XT](https://stacks.math.columbia.edu/tag/03XT) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtale_local_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocalTfae.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocalTfae.lean#L129).

> **Stacks 03XT.** Nine equivalent criteria for a morphism `f : X ⟶ Y` of algebraic spaces
> over `S` to be étale: `f` is étale; `f` is étale at every point of `|X|`; the base change of
> `f` to every scheme is étale; the base change of `f` to every affine scheme is étale; the base
> change of `f` to one surjective étale scheme chart of `Y` is étale; the composite of `f` with
> one surjective étale scheme chart of `X` is étale; in every commuting square of étale scheme
> charts of `f` the morphism of schemes between the charts is étale; there is one such square
> with surjective chart of the source; and there are Zariski coverings `Y = ⋃ Yᵢ` and
> `f⁻¹(Yᵢ) = ⋃ Xᵢⱼ` with every `Xᵢⱼ ⟶ Yᵢ` étale.

```lean
theorem isEtale_local_tfae
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE [
      IsEtale B S hS f,
      ∀ x : points B S hS X, IsEtaleAt B S hS f x,
      ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
        IsEtale B S hS (pullback.snd f g),
      ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
        IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
          IsEtale B S hS (pullback.snd f g),
      ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
        IsSurjective B S hS g ∧ IsEtale B S hS g ∧ IsEtale B S hS (pullback.snd f g),
      ∃ (U : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X),
        IsSurjective B S hS p ∧ IsEtale B S hS p ∧ IsEtale B S hS (p ≫ f),
      ∀ (U V : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X) (q : yoneda.obj V ⟶ Y) (a : U ⟶ V),
        IsEtale B S hS p → IsEtale B S hS q → p ≫ f = yoneda.map a ≫ q →
          AlgebraicGeometry.Etale ((BigFppfOver.toScheme B S hS).map a),
      ∃ (U V : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X) (q : yoneda.obj V ⟶ Y) (a : U ⟶ V),
        IsEtale B S hS p ∧ IsEtale B S hS q ∧ IsSurjective B S hS p ∧
          p ≫ f = yoneda.map a ≫ q ∧
            AlgebraicGeometry.Etale ((BigFppfOver.toScheme B S hS).map a),
      ∃ (I : Type u) (Yopen : I → Subfunctor Y) (J : I → Type u)
        (Xopen : ∀ i, J i → Subfunctor (pullback f (Yopen i).ι)),
        IsZariskiCover B S hS I Yopen ∧ (∀ i, IsZariskiCover B S hS (J i) (Xopen i)) ∧
          ∀ i j, IsEtale B S hS ((Xopen i j).ι ≫ pullback.snd f (Yopen i).ι)
    ]
```

## Tag 0465, a lemma

[Tag 0465](https://stacks.math.columbia.edu/tag/0465) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtale_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleMorphisms.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleMorphisms.lean#L75). The attribute's comment: “the composition of two etale morphisms of algebraic spaces is etale”.

> The composite of two étale morphisms of presheaves on the big fppf site of `S` is étale.

```lean
theorem isEtale_comp {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : F ⟶ G} {g : G ⟶ H}
    (hf : IsEtale B S hS f) (hg : IsEtale B S hS g) : IsEtale B S hS (f ≫ g)
```

## Tag 0466, a lemma

[Tag 0466](https://stacks.math.columbia.edu/tag/0466) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtale_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleMorphisms.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleMorphisms.lean#L254). The attribute's comment: “the base change of an étale morphism of algebraic spaces is étale”. References: SGA 1 IX (1.3).

> A base change of an étale morphism of algebraic spaces over `S` is étale.

```lean
theorem isEtale_of_isPullback {X' X Z Y : AlgebraicSpaces B S hS}
    (p : X' ⟶ X) (f' : X' ⟶ Z) (f : X ⟶ Y) (g : Z ⟶ Y)
    (h : IsPullback p f' f g) (hf : IsEtale B S hS f.hom) :
    IsEtale B S hS f'.hom
```

## Tag 03XU, a lemma

[Tag 03XU](https://stacks.math.columbia.edu/tag/03XU) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiFinite.lean, line 455](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiFinite.lean#L455).

> **Stacks 03XU.** An étale morphism of algebraic spaces over `S` is locally quasi-finite: an
> étale morphism of schemes is locally of finite type and locally quasi-finite (Stacks 03II).
>
> Only the target has to be an algebraic space, where the source requires both.

```lean
theorem isLocallyQuasiFinite_of_isEtale
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hY : IsAlgebraicSpace B S hS Y)
    {f : X ⟶ Y} (hf : IsEtale B S hS f) :
    IsLocallyQuasiFinite B S hS f
```

## Tag 04XX, a lemma

[Tag 04XX](https://stacks.math.columbia.edu/tag/04XX) in the Stacks Project.

**`AlgebraicGeometry.Space.isSmooth_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothAtlas.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmoothAtlas.lean#L124).

> **Stacks 04XX.** An étale morphism of algebraic spaces over `S` is smooth: an étale
> morphism of schemes is smooth.

```lean
theorem isSmooth_of_isEtale
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hG : IsAlgebraicSpace B S hS G)
    {f : F ⟶ G} (hf : IsEtale B S hS f) :
    IsSmooth B S hS f
```

## Tag 0467, a lemma

[Tag 0467](https://stacks.math.columbia.edu/tag/0467) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothAtlas.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmoothAtlas.lean#L139).

> **Stacks 0467.** An étale morphism of algebraic spaces over `S` is flat: in every commuting
> square of étale charts the chart morphism of schemes is étale, by cancellation
> (`AlgebraicGeometry.Space.etale_of_comp_etale_chart`), and an étale morphism of schemes is
> flat.
>
> Nothing is asked of the target.

```lean
theorem isFlat_of_isEtale {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : F ⟶ G}
    (hf : IsEtale B S hS f) : IsFlat B S hS f
```

## Tag 0468, a lemma

[Tag 0468](https://stacks.math.columbia.edu/tag/0468) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothAtlas.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmoothAtlas.lean#L152).

> **Stacks 0468.** An étale morphism of algebraic spaces over `S` is locally of finite
> presentation: the chart morphism of schemes in every commuting square of étale charts is étale,
> hence locally of finite presentation.
>
> Nothing is asked of the target.

```lean
theorem isLocallyOfFinitePresentation_of_isEtale
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : F ⟶ G} (hf : IsEtale B S hS f) :
    IsLocallyOfFinitePresentation B S hS f
```

## Tag 06LT, a lemma

[Tag 06LT](https://stacks.math.columbia.edu/tag/06LT) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFiniteType_of_isEtale'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypePermanence.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypePermanence.lean#L45).

> An étale morphism of presheaves on the big fppf site of `S` is locally of finite type; neither
> the source nor the target has to be an algebraic space.

```lean
theorem isLocallyOfFiniteType_of_isEtale' (f : F ⟶ G) (hf : IsEtale B S hS f) :
    IsLocallyOfFiniteType B S hS f
```

**`AlgebraicGeometry.Space.isLocallyOfFiniteType_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiFinite.lean, line 442](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiFinite.lean#L442).

> **Stacks 06LT.** An étale morphism of algebraic spaces over `S` is locally of finite type:
> an étale morphism of schemes is.
>
> Only the target has to be an algebraic space, where the source requires both.

```lean
theorem isLocallyOfFiniteType_of_isEtale
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hY : IsAlgebraicSpace B S hS Y)
    {f : X ⟶ Y} (hf : IsEtale B S hS f) :
    IsLocallyOfFiniteType B S hS f
```

## Tag 06CR, a lemma

[Tag 06CR](https://stacks.math.columbia.edu/tag/06CR) in the Stacks Project.

**`AlgebraicGeometry.Space.isUnramified_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Etale.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Etale.lean#L88).

> **Stacks 06CR.** An étale morphism of algebraic spaces over `S` is unramified.
>
> In a commuting square of étale charts of `f` the morphism of schemes on top is étale, hence
> formally unramified and locally of finite type, hence unramified by
> [Stacks Project, Tag 02HE]. Nothing is asked of the target.

```lean
theorem isUnramified_of_isEtale {f : X ⟶ Y} (hf : IsEtale B S hS f) :
    IsUnramified B S hS f
```

## Tag 05W3, a lemma

[Tag 05W3](https://stacks.math.columbia.edu/tag/05W3) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtale_of_isEtale_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleMorphisms.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleMorphisms.lean#L378). The attribute's comment: “a morphism over Z between algebraic spaces étale over Z is étale”.

> A morphism between two algebraic spaces which are étale over a common algebraic space is
> itself étale.

```lean
theorem isEtale_of_isEtale_over {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (_hH : IsAlgebraicSpace B S hS H) (f : F ⟶ G) (g : F ⟶ H) (h : G ⟶ H)
    (hg : IsEtale B S hS g) (hh : IsEtale B S hS h) (hfg : f ≫ h = g) :
    IsEtale B S hS f
```

## Tag 06LU, a lemma

[Tag 06LU](https://stacks.math.columbia.edu/tag/06LU) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtale_of_isFlat_of_isUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Etale.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Etale.lean#L106).

> **Stacks 06LU.** A morphism of algebraic spaces over `S` which is locally of finite
> presentation, flat and unramified is étale.
>
> Lift an atlas `q` of the target through `f` by [Stacks Project, Tag 02X1] to a surjective
> étale chart `p` of the source over a morphism `α` of the site. The three hypotheses, read on
> that one square, say that the scheme morphism underlying `α` is locally of finite
> presentation, flat and unramified, hence formally unramified by [Stacks Project, Tag 02HE]
> and therefore étale. One such square suffices by condition (4) of
> [Stacks Project, Tag 03FS].

```lean
theorem isEtale_of_isFlat_of_isUnramified (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hlfp : IsLocallyOfFinitePresentation B S hS f) (hflat : IsFlat B S hS f)
    (hunr : IsUnramified B S hS f) :
    IsEtale B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.39, Tag 03XS](https://stacks.math.columbia.edu/tag/03XS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
