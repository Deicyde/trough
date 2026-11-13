---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_affine_etale_isLocallyOfFinitePresentation_separation_of_isAbsolutelyQuasiSeparated, AlgebraicGeometry.Space.exists_affine_elementary_etale_separation, AlgebraicGeometry.Space.exists_isClosed_separation_of_etale_cover, AlgebraicGeometry.Space.exists_affine_etale_isLocallyOfFinitePresentation_separation, AlgebraicGeometry.Space.exists_affineOpen_isLocallyOfFinitePresentation_separation_of_lfp_morphism, AlgebraicGeometry.Space.exists_affineOpen_isLocallyOfFinitePresentation_separation, AlgebraicGeometry.Space.isClosedMorphism_pullback_fst_of_affineSpaceTest, AlgebraicGeometry.Space.isClosedMorphism_pullback_fst_of_universallyClosed
statement: formalized
proof: formalized
---

# 70.20 Universally closed morphisms

Section 70.20 of the Stacks Project, [Tag 0CM7](https://stacks.math.columbia.edu/tag/0CM7). 3 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CM8, a lemma

[Tag 0CM8](https://stacks.math.columbia.edu/tag/0CM8) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_affine_etale_isLocallyOfFinitePresentation_separation_of_isAbsolutelyQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/AffineFinitePresentationFactorizationQuasiSeparated.lean, line 411](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/AffineFinitePresentationFactorizationQuasiSeparated.lean#L411). The attribute's comment: “the whole lemma, including the refinement for Z a scheme (V an affine open neighbourhood of z), under the extra hypothesis that Y is quasi-separated. For an arbitrary Y the refinement is open: it is equivalent to Z -> Y factoring Zariski locally through an affine scheme locally of finite presentation over Y, which is proved here only for Y quasi-separated”.

> **Stacks 0CM8, for `Y` quasi-separated.** Let `f : X ⟶ Y` be a quasi-compact morphism of
> algebraic spaces over `S` with `Y` quasi-separated.
>
> 1. For every morphism `g : Z ⟶ Y` of algebraic spaces, point `z` of `|Z|` and closed subset `T`
>    of `|X ×_Y Z|` whose image in `|Z|` misses `z`, there are an affine étale neighbourhood
>    `(V, v)` of `z`, an affine `Z'` and a factorization `V ⟶ Z' ⟶ Y` of `V ⟶ Y` whose second leg
>    `b` is locally of finite presentation, and a closed subset `T'` of `|X ×_Y Z'|` whose image in
>    `|Z'|` misses the image of `v` and which receives the inverse image of `T` along the
>    comparison morphisms `r` and `q` of the three fibre products.
> 2. If moreover `Z` is a scheme, represented by an object `Z₀` of the site, then `V` may be taken
>    to be an affine open neighbourhood of `z`: the étale neighbourhood is an open immersion
>    `V ⟶ Z₀` sending `v` to `z`, with all the conclusions of the first part.
>
> The first part is `exists_affine_etale_isLocallyOfFinitePresentation_separation`, which needs no
> hypothesis on `Y`. The second part is
> `exists_affineOpen_isLocallyOfFinitePresentation_separation_of_factorization`, whose input — a
> Zariski-local factorization of `Z₀ ⟶ Y` through an affine scheme locally of finite presentation
> over `Y` — is supplied for quasi-separated `Y` by
> `exists_affine_isLocallyOfFinitePresentation_factorization_of_isAbsolutelyQuasiSeparated`.

```lean
theorem exists_affine_etale_isLocallyOfFinitePresentation_separation_of_isAbsolutelyQuasiSeparated
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS hZ Y) (f : X ⟶ Y)
    (hf : IsQuasiCompact B S hS f) :
    (∀ {Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (_ : IsAlgebraicSpace B S hS Z) (g : Z ⟶ Y)
      (z : points B S hS Z) (T : Set (points B S hS (pullback f g))), IsClosed T →
      z ∉ pointsMap B S hS (pullback f g) (pullback.snd f g) '' T →
      ∃ (V Z' : BigFppfOver B S hS) (p : yoneda.obj V ⟶ Z)
        (v : points B S hS (yoneda.obj V)) (a : yoneda.obj V ⟶ yoneda.obj Z')
        (b : yoneda.obj Z' ⟶ Y) (T' : Set (points B S hS (pullback f b)))
        (r : pullback f (p ≫ g) ⟶ pullback f g) (q : pullback f (p ≫ g) ⟶ pullback f b),
        IsAffine ((BigFppfOver.toScheme B S hS).obj V) ∧
        IsAffine ((BigFppfOver.toScheme B S hS).obj Z') ∧
        IsEtale B S hS p ∧
        pointsMap B S hS (yoneda.obj V) p v = z ∧
        p ≫ g = a ≫ b ∧
        IsLocallyOfFinitePresentation B S hS b ∧
        IsClosed T' ∧
        pointsMap B S hS (yoneda.obj V) a v ∉
          pointsMap B S hS (pullback f b) (pullback.snd f b) '' T' ∧
        r ≫ pullback.fst f g = pullback.fst f (p ≫ g) ∧
        r ≫ pullback.snd f g = pullback.snd f (p ≫ g) ≫ p ∧
        IsPullback r (pullback.snd f (p ≫ g)) (pullback.snd f g) p ∧
        q ≫ pullback.fst f b = pullback.fst f (p ≫ g) ∧
        q ≫ pullback.snd f b = pullback.snd f (p ≫ g) ≫ a ∧
        pointsMap B S hS (pullback f (p ≫ g)) q ''
          (pointsMap B S hS (pullback f (p ≫ g)) r ⁻¹' T) ⊆ T') ∧
    (∀ {Z₀ : BigFppfOver B S hS} (g : yoneda.obj Z₀ ⟶ Y) (z : points B S hS (yoneda.obj Z₀))
      (T : Set (points B S hS (pullback f g))), IsClosed T →
      z ∉ pointsMap B S hS (pullback f g) (pullback.snd f g) '' T →
      ∃ (V Z' : BigFppfOver B S hS) (p : yoneda.obj V ⟶ yoneda.obj Z₀) (pV : V ⟶ Z₀)
        (v : points B S hS (yoneda.obj V)) (a : yoneda.obj V ⟶ yoneda.obj Z')
        (b : yoneda.obj Z' ⟶ Y) (T' : Set (points B S hS (pullback f b)))
        (r : pullback f (p ≫ g) ⟶ pullback f g) (q : pullback f (p ≫ g) ⟶ pullback f b),
        p = yoneda.map pV ∧
        AlgebraicGeometry.IsOpenImmersion ((BigFppfOver.toScheme B S hS).map pV) ∧
        (BigFppfOver.toScheme B S hS).map pV (pointsToScheme B S hS V v) =
          pointsToScheme B S hS Z₀ z ∧
        IsAffine ((BigFppfOver.toScheme B S hS).obj V) ∧
        IsAffine ((BigFppfOver.toScheme B S hS).obj Z') ∧
        IsEtale B S hS p ∧
        pointsMap B S hS (yoneda.obj V) p v = z ∧
        p ≫ g = a ≫ b ∧
        IsLocallyOfFinitePresentation B S hS b ∧
        IsClosed T' ∧
        pointsMap B S hS (yoneda.obj V) a v ∉
          pointsMap B S hS (pullback f b) (pullback.snd f b) '' T' ∧
        r ≫ pullback.fst f g = pullback.fst f (p ≫ g) ∧
        r ≫ pullback.snd f g = pullback.snd f (p ≫ g) ≫ p ∧
        IsPullback r (pullback.snd f (p ≫ g)) (pullback.snd f g) p ∧
        q ≫ pullback.fst f b = pullback.fst f (p ≫ g) ∧
        q ≫ pullback.snd f b = pullback.snd f (p ≫ g) ≫ a ∧
        pointsMap B S hS (pullback f (p ≫ g)) q ''
          (pointsMap B S hS (pullback f (p ≫ g)) r ⁻¹' T) ⊆ T')
```

**`AlgebraicGeometry.Space.exists_affine_elementary_etale_separation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/ElementaryEtaleSeparation.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/ElementaryEtaleSeparation.lean#L163). The attribute's comment: “the separation statement for Z a scheme, with V and Z' affine and the etale neighbourhood of z elementary -- the canonical morphism Spec kappa(z) -> Z factors through it -- and with clauses (1), (2) and (3) unchanged”.

> **Stacks 0CM8 for `Z` a scheme, with an elementary étale neighbourhood.** Let
> `f : X ⟶ Y` be a quasi-compact morphism of algebraic spaces over `S` with `Z` represented by
> an object `Z₀` of the site, let `z` be a point of `|Z₀|`, and let `T` be a closed subset of
> `|X ×_Y Z₀|` whose image in `|Z₀|` misses `z`. Then the conclusion of Tag 0CM8 holds with `V`
> and `Z'` affine and with the étale neighbourhood `p : V ⟶ Z₀` *elementary*: the canonical
> morphism `Spec κ(z) ⟶ Z₀` factors through it, so `v` and `z` have the same residue field.
>
> The source asks only for an étale neighbourhood. The elementary refinement holds for an
> arbitrary algebraic space `Y`, because the chart of `Y` can be chosen to receive the
> field-valued point of `z`.

```lean
theorem exists_affine_elementary_etale_separation
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {Z₀ : BigFppfOver B S hS}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (g : yoneda.obj Z₀ ⟶ Y) (hf : IsQuasiCompact B S hS f)
    (z : points B S hS (yoneda.obj Z₀))
    (T : Set (points B S hS (pullback f g))) (hT : IsClosed T)
    (hz : z ∉ pointsMap B S hS (pullback f g) (pullback.snd f g) '' T) :
    ∃ (V Z' : BigFppfOver B S hS) (p : yoneda.obj V ⟶ yoneda.obj Z₀) (pV : V ⟶ Z₀)
      (v : points B S hS (yoneda.obj V)) (a : yoneda.obj V ⟶ yoneda.obj Z')
      (b : yoneda.obj Z' ⟶ Y) (T' : Set (points B S hS (pullback f b)))
      (r : pullback f (p ≫ g) ⟶ pullback f g) (q : pullback f (p ≫ g) ⟶ pullback f b)
      (s : FieldValuedPoint.siteObject B S hS (yoneda.obj Z₀)
        (schemePointRepresentative B S hS Z₀ (pointsToScheme B S hS Z₀ z)) ⟶ V),
      p = yoneda.map pV ∧
      s ≫ pV = (schemePointRepresentative B S hS Z₀ (pointsToScheme B S hS Z₀ z)).siteHom ∧
      IsAffine ((BigFppfOver.toScheme B S hS).obj V) ∧
      IsAffine ((BigFppfOver.toScheme B S hS).obj Z') ∧
      IsEtale B S hS p ∧
      pointsMap B S hS (yoneda.obj V) p v = z ∧
      p ≫ g = a ≫ b ∧
      IsLocallyOfFinitePresentation B S hS b ∧
      IsClosed T' ∧
      pointsMap B S hS (yoneda.obj V) a v ∉
        pointsMap B S hS (pullback f b) (pullback.snd f b) '' T' ∧
      r ≫ pullback.fst f g = pullback.fst f (p ≫ g) ∧
      r ≫ pullback.snd f g = pullback.snd f (p ≫ g) ≫ p ∧
      IsPullback r (pullback.snd f (p ≫ g)) (pullback.snd f g) p ∧
      q ≫ pullback.fst f b = pullback.fst f (p ≫ g) ∧
      q ≫ pullback.snd f b = pullback.snd f (p ≫ g) ≫ a ∧
      pointsMap B S hS (pullback f (p ≫ g)) q ''
        (pointsMap B S hS (pullback f (p ≫ g)) r ⁻¹' T) ⊆ T'
```

**`AlgebraicGeometry.Space.exists_isClosed_separation_of_etale_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/UniversallyClosedSeparation.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/UniversallyClosedSeparation.lean#L203). The attribute's comment: “etale-descent step of the proof: clauses (2) and (3) descend along a cover of X whose represented base changes are etale and which is surjective on points; the reduction to the case of affine schemes and the appeal to Tag 05BD are not included”.

> **Stacks 0CM8**, the étale-descent step of the proof. Let `f : X ⟶ Y`, `b : Z' ⟶ Y` and
> `a : V ⟶ Z'` be morphisms of presheaves on the big fppf site of `S`, and let `c : W ⟶ X` be a
> morphism whose represented base changes are étale and which is surjective on points. There
> are comparison morphisms `γ`, `α₁`, `α₂`, `κ` filling the square
>
> ```
> W ×_Y V --α₁--> W ×_Y Z'
>    |               |
>    γ               κ
>    ↓               ↓
> X ×_Y V --α₂--> X ×_Y Z'
> ```
>
> along which clauses (2) and (3) of Tag 0CM8 descend: given a closed subset `T₀` of
> `|W ×_Y Z'|` receiving the inverse image of `T ⊆ |X ×_Y V|` and whose image in `|Z'|` misses
> `r`, there is a closed `T' ⊆ |X ×_Y Z'|` receiving `T` and whose image in `|Z'|` misses `r`.
> Clause (1), that `b` is locally of finite presentation, is a property of `b` alone and is
> untouched by the descent.

```lean
theorem exists_isClosed_separation_of_etale_cover
    (f : X ⟶ Y) (b : Z' ⟶ Y) (a : V ⟶ Z') (c : W ⟶ X)
    (hc : (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf c)
    (hcsurj : Function.Surjective (pointsMap B S hS W c)) :
    ∃ (γ : pullback (c ≫ f) (a ≫ b) ⟶ pullback f (a ≫ b))
      (α₁ : pullback (c ≫ f) (a ≫ b) ⟶ pullback (c ≫ f) b)
      (α₂ : pullback f (a ≫ b) ⟶ pullback f b)
      (κ : pullback (c ≫ f) b ⟶ pullback f b),
      γ ≫ pullback.fst f (a ≫ b) = pullback.fst (c ≫ f) (a ≫ b) ≫ c ∧
        γ ≫ pullback.snd f (a ≫ b) = pullback.snd (c ≫ f) (a ≫ b) ∧
        α₁ ≫ pullback.fst (c ≫ f) b = pullback.fst (c ≫ f) (a ≫ b) ∧
        α₁ ≫ pullback.snd (c ≫ f) b = pullback.snd (c ≫ f) (a ≫ b) ≫ a ∧
        α₂ ≫ pullback.fst f b = pullback.fst f (a ≫ b) ∧
        α₂ ≫ pullback.snd f b = pullback.snd f (a ≫ b) ≫ a ∧
        κ ≫ pullback.fst f b = pullback.fst (c ≫ f) b ≫ c ∧
        κ ≫ pullback.snd f b = pullback.snd (c ≫ f) b ∧
        ∀ (T : Set (points B S hS (pullback f (a ≫ b))))
          (T₀ : Set (points B S hS (pullback (c ≫ f) b))),
          @IsClosed _ (pointTopology B S hS (pullback (c ≫ f) b)) T₀ →
          pointsMap B S hS _ α₁ '' (pointsMap B S hS _ γ ⁻¹' T) ⊆ T₀ →
          ∀ r : points B S hS Z',
            r ∉ pointsMap B S hS _ (pullback.snd (c ≫ f) b) '' T₀ →
            ∃ T' : Set (points B S hS (pullback f b)),
              @IsClosed _ (pointTopology B S hS (pullback f b)) T' ∧
                T ⊆ pointsMap B S hS _ α₂ ⁻¹' T' ∧
                  r ∉ pointsMap B S hS _ (pullback.snd f b) '' T'
```

**`AlgebraicGeometry.Space.exists_affine_etale_isLocallyOfFinitePresentation_separation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/UniversallyClosedSeparation.lean, line 829](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/UniversallyClosedSeparation.lean#L829). The attribute's comment: “the separation statement, with V and Z' affine; the refinement for Z a scheme, where V may be taken to be an affine open neighbourhood of z, is not included”.

> **Stacks 0CM8.** Let `f : X ⟶ Y` be a quasi-compact morphism of algebraic spaces over `S`,
> let `g : Z ⟶ Y` be a morphism of algebraic spaces, let `z` be a point of `|Z|`, and let `T` be
> a closed subset of `|X ×_Y Z|` whose image in `|Z|` misses `z`. Then there are an affine étale
> neighbourhood `(V, v)` of `z`, an affine `Z'` and a factorization `V ⟶ Z' ⟶ Y` of `V ⟶ Y`
> whose second leg `b` is locally of finite presentation, and a closed subset `T'` of
> `|X ×_Y Z'|` whose image in `|Z'|` misses the image of `v` and which receives the inverse image
> of `T` along the two comparison morphisms `r` and `q` of the three fibre products.

```lean
theorem exists_affine_etale_isLocallyOfFinitePresentation_separation
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Z ⟶ Y)
    (hf : IsQuasiCompact B S hS f)
    (z : points B S hS Z) (T : Set (points B S hS (pullback f g))) (hT : IsClosed T)
    (hz : z ∉ pointsMap B S hS (pullback f g) (pullback.snd f g) '' T) :
    ∃ (V Z' : BigFppfOver B S hS) (p : yoneda.obj V ⟶ Z)
      (v : points B S hS (yoneda.obj V)) (a : yoneda.obj V ⟶ yoneda.obj Z')
      (b : yoneda.obj Z' ⟶ Y) (T' : Set (points B S hS (pullback f b)))
      (r : pullback f (p ≫ g) ⟶ pullback f g) (q : pullback f (p ≫ g) ⟶ pullback f b),
      IsAffine ((BigFppfOver.toScheme B S hS).obj V) ∧
      IsAffine ((BigFppfOver.toScheme B S hS).obj Z') ∧
      IsEtale B S hS p ∧
      pointsMap B S hS (yoneda.obj V) p v = z ∧
      p ≫ g = a ≫ b ∧
      IsLocallyOfFinitePresentation B S hS b ∧
      IsClosed T' ∧
      pointsMap B S hS (yoneda.obj V) a v ∉
        pointsMap B S hS (pullback f b) (pullback.snd f b) '' T' ∧
      r ≫ pullback.fst f g = pullback.fst f (p ≫ g) ∧
      r ≫ pullback.snd f g = pullback.snd f (p ≫ g) ≫ p ∧
      IsPullback r (pullback.snd f (p ≫ g)) (pullback.snd f g) p ∧
      q ≫ pullback.fst f b = pullback.fst f (p ≫ g) ∧
      q ≫ pullback.snd f b = pullback.snd f (p ≫ g) ≫ a ∧
      pointsMap B S hS (pullback f (p ≫ g)) q ''
        (pointsMap B S hS (pullback f (p ≫ g)) r ⁻¹' T) ⊆ T'
```

**`AlgebraicGeometry.Space.exists_affineOpen_isLocallyOfFinitePresentation_separation_of_lfp_morphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/UniversallyClosedSeparation.lean, line 1099](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/UniversallyClosedSeparation.lean#L1099). The attribute's comment: “the refinement for Z a scheme with Y an arbitrary algebraic space over S, for g : Z -> Y locally of finite presentation: the etale neighbourhood p : V -> Z is an open immersion onto an affine open neighbourhood of z, Z' is affine, and clauses (1), (2) and (3) hold -- b locally of finite presentation, the image of T' in |Z'| missing a(v), and T' receiving the inverse image of T. An affine open neighbourhood of z is then itself an affine scheme locally of finite presentation over Y, which is the factorization the refinement amounts to”.

> **Stacks 0CM8, the refinement for `Z` a scheme and `Y` an arbitrary algebraic space**, for a
> morphism `g : Z ⟶ Y` which is locally of finite presentation. Let `f : X ⟶ Y` be a
> quasi-compact morphism of algebraic spaces over `S` with `Z` represented by an object `Z₀` of
> the site, let `g : yoneda.obj Z₀ ⟶ Y` be locally of finite presentation, let `z` be a point of
> `|Z₀|`, and let `T` be a closed subset of `|X ×_Y Z₀|` whose image in `|Z₀|` misses `z`. Then
> the conclusion of Tag 0CM8 holds with the étale neighbourhood `p` an *open immersion* out of an
> affine `V` sending `v` to `z`: that is, `V` is an affine open neighbourhood of `z`, `Z'` is
> affine, and clauses (1), (2) and (3) — `b` locally of finite presentation, the image of `T'` in
> `|Z'|` missing the image of `v`, and `T'` receiving the inverse image of `T` — all hold, as
> does étaleness of `p`.
>
> Nothing is assumed of `Y` beyond being an algebraic space over `S`.

```lean
theorem exists_affineOpen_isLocallyOfFinitePresentation_separation_of_lfp_morphism
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {Z₀ : BigFppfOver B S hS}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (g : yoneda.obj Z₀ ⟶ Y)
    (hf : IsQuasiCompact B S hS f) (hg : IsLocallyOfFinitePresentation B S hS g)
    (z : points B S hS (yoneda.obj Z₀))
    (T : Set (points B S hS (pullback f g))) (hT : IsClosed T)
    (hz : z ∉ pointsMap B S hS (pullback f g) (pullback.snd f g) '' T) :
    ∃ (V Z' : BigFppfOver B S hS) (p : yoneda.obj V ⟶ yoneda.obj Z₀) (pV : V ⟶ Z₀)
      (v : points B S hS (yoneda.obj V)) (a : yoneda.obj V ⟶ yoneda.obj Z')
      (b : yoneda.obj Z' ⟶ Y) (T' : Set (points B S hS (pullback f b)))
      (r : pullback f (p ≫ g) ⟶ pullback f g) (q : pullback f (p ≫ g) ⟶ pullback f b),
      p = yoneda.map pV ∧
      AlgebraicGeometry.IsOpenImmersion ((BigFppfOver.toScheme B S hS).map pV) ∧
      (BigFppfOver.toScheme B S hS).map pV (pointsToScheme B S hS V v) =
        pointsToScheme B S hS Z₀ z ∧
      IsAffine ((BigFppfOver.toScheme B S hS).obj V) ∧
      IsAffine ((BigFppfOver.toScheme B S hS).obj Z') ∧
      IsEtale B S hS p ∧
      pointsMap B S hS (yoneda.obj V) p v = z ∧
      p ≫ g = a ≫ b ∧
      IsLocallyOfFinitePresentation B S hS b ∧
      IsClosed T' ∧
      pointsMap B S hS (yoneda.obj V) a v ∉
        pointsMap B S hS (pullback f b) (pullback.snd f b) '' T' ∧
      r ≫ pullback.fst f g = pullback.fst f (p ≫ g) ∧
      r ≫ pullback.snd f g = pullback.snd f (p ≫ g) ≫ p ∧
      IsPullback r (pullback.snd f (p ≫ g)) (pullback.snd f g) p ∧
      q ≫ pullback.fst f b = pullback.fst f (p ≫ g) ∧
      q ≫ pullback.snd f b = pullback.snd f (p ≫ g) ≫ a ∧
      pointsMap B S hS (pullback f (p ≫ g)) q ''
        (pointsMap B S hS (pullback f (p ≫ g)) r ⁻¹' T) ⊆ T'
```

**`AlgebraicGeometry.Space.exists_affineOpen_isLocallyOfFinitePresentation_separation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/UniversallyClosedSeparation.lean, line 1254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/UniversallyClosedSeparation.lean#L1254). The attribute's comment: “the refinement for Z a scheme with no hypothesis on g, for Y represented by an object of the site as well -- the situation the source's own proof reduces to before it produces the affine open neighbourhood: the etale neighbourhood p : V -> Z is an open immersion onto an affine open neighbourhood of z, Z' is affine, and clauses (1), (2) and (3) hold -- b locally of finite presentation, the image of T' in |Z'| missing a(v), and T' receiving the inverse image of T. The affine opens of Y supply the factorization of an affine open neighbourhood of z through an affine scheme locally of finite presentation over Y that the refinement amounts to”.

> **Stacks 0CM8, the refinement for `Z` a scheme**, with no hypothesis on `g`, in the
> situation the source's own proof reduces to, where `Y` is represented by an object of the site
> as well. Let `f : X ⟶ Y` be a quasi-compact morphism with `X` an algebraic space over `S` and
> `Y` and `Z` represented by objects `Y₀` and `Z₀` of the site, let `z` be a point of `|Z₀|`, and
> let `T` be a closed subset of `|X ×_Y Z₀|` whose image in `|Z₀|` misses `z`. Then the
> conclusion of Tag 0CM8 holds with `V` an affine *open* neighbourhood of `z`: the morphism
> `p : V ⟶ Z₀` is an open immersion sending `v` to `z`, `V` and `Z'` are affine, and clauses
> (1), (2) and (3) of the source hold unchanged.
>
> For `Y` an arbitrary algebraic space the refinement holds whenever `g` is locally of finite
> presentation, by
> `exists_affineOpen_isLocallyOfFinitePresentation_separation_of_lfp_morphism`, and in general
> from a Zariski-local factorization, by
> `exists_affineOpen_isLocallyOfFinitePresentation_separation_of_factorization`,
> which asks for the input in its sharpest form — an affine open neighbourhood of `z` whose
> morphism to `Y` factors through an affine scheme *locally of finite presentation* over `Y`.
> That input cannot be dispensed with: it is part of the refinement's own conclusion, by
> `AlgebraicGeometry.Space.exists_affine_isLocallyOfFinitePresentation_factorization_of_separation`.
> What `Y` being a scheme supplies is a Zariski-local factorization: for a general algebraic
> space the affine opens of `Y` are replaced by affine étale charts, and pulling a chart back
> along `Z₀ ⟶ Y` gives an étale morphism to `Z₀`, of which one needs a *section* near `z`. A
> point above `z` with the same residue field as `z` is not enough for that and is in any case
> always available, by
> `AlgebraicGeometry.Space.exists_affine_etale_chart_of_fieldValuedPoint`, for an arbitrary
> algebraic space and with no decency hypothesis; an étale morphism with trivial residue
> extension at a point has a section near it exactly when the map of local rings there is an
> isomorphism, by `AlgebraicGeometry.exists_isOpenImmersion_of_etale_of_isIso_stalkMap`, and that
> is the Henselian property of `𝒪_{Z₀, z}` rather than anything about `Y`. What does supply the
> factorization for an arbitrary `Y` and an arbitrary `g`, and which step of it this development
> is missing, is recorded in the note opening this section.

```lean
theorem exists_affineOpen_isLocallyOfFinitePresentation_separation
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {Y₀ Z₀ : BigFppfOver B S hS}
    (hX : IsAlgebraicSpace B S hS X)
    (f : X ⟶ yoneda.obj Y₀) (g : yoneda.obj Z₀ ⟶ yoneda.obj Y₀)
    (hf : IsQuasiCompact B S hS f)
    (z : points B S hS (yoneda.obj Z₀))
    (T : Set (points B S hS (pullback f g))) (hT : IsClosed T)
    (hz : z ∉ pointsMap B S hS (pullback f g) (pullback.snd f g) '' T) :
    ∃ (V Z' : BigFppfOver B S hS) (p : yoneda.obj V ⟶ yoneda.obj Z₀) (pV : V ⟶ Z₀)
      (v : points B S hS (yoneda.obj V)) (a : yoneda.obj V ⟶ yoneda.obj Z')
      (b : yoneda.obj Z' ⟶ yoneda.obj Y₀) (T' : Set (points B S hS (pullback f b)))
      (r : pullback f (p ≫ g) ⟶ pullback f g) (q : pullback f (p ≫ g) ⟶ pullback f b),
      p = yoneda.map pV ∧
      AlgebraicGeometry.IsOpenImmersion ((BigFppfOver.toScheme B S hS).map pV) ∧
      (BigFppfOver.toScheme B S hS).map pV (pointsToScheme B S hS V v) =
        pointsToScheme B S hS Z₀ z ∧
      IsAffine ((BigFppfOver.toScheme B S hS).obj V) ∧
      IsAffine ((BigFppfOver.toScheme B S hS).obj Z') ∧
      IsEtale B S hS p ∧
      pointsMap B S hS (yoneda.obj V) p v = z ∧
      p ≫ g = a ≫ b ∧
      IsLocallyOfFinitePresentation B S hS b ∧
      IsClosed T' ∧
      pointsMap B S hS (yoneda.obj V) a v ∉
        pointsMap B S hS (pullback f b) (pullback.snd f b) '' T' ∧
      r ≫ pullback.fst f g = pullback.fst f (p ≫ g) ∧
      r ≫ pullback.snd f g = pullback.snd f (p ≫ g) ≫ p ∧
      IsPullback r (pullback.snd f (p ≫ g)) (pullback.snd f g) p ∧
      q ≫ pullback.fst f b = pullback.fst f (p ≫ g) ∧
      q ≫ pullback.snd f b = pullback.snd f (p ≫ g) ≫ a ∧
      pointsMap B S hS (pullback f (p ≫ g)) q ''
        (pointsMap B S hS (pullback f (p ≫ g)) r ⁻¹' T) ⊆ T'
```

## Tag 0CM9, a lemma

[Tag 0CM9](https://stacks.math.columbia.edu/tag/0CM9) in the Stacks Project.

**`AlgebraicGeometry.Space.isClosedMorphism_pullback_fst_of_affineSpaceTest`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/UniversallyClosedAffineSpaceTest.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/UniversallyClosedAffineSpaceTest.lean#L295). The attribute's comment: “(3) implies (2)”.

> **Stacks 0CM9, (3) implies (2).** If `f : X ⟶ Y` passes the affine-space test over one
> surjective étale scheme atlas `V ⟶ Y` of the target, then the base change of `f` along every
> morphism to `Y` which is locally of finite presentation is closed.
>
> Closedness of `|Z ×_Y X| → |Z|` may be checked after the base change along the composite of an
> étale atlas of `Z ×_Y V` with the projection to `Z`, which is open and surjective on points;
> that composite exhibits the test object as a morphism of the site into `V` locally of finite
> presentation, where the previous statement applies.
>
> Quasi-compactness of `f` is not needed: it enters Tag 0CM9 only through the implication from
> the finitely presented tests back to universal closedness.

```lean
theorem isClosedMorphism_pullback_fst_of_affineSpaceTest
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y)
    (hgsurj : IsSurjective B S hS g) (hgetale : IsEtale B S hS g)
    (htest : ∀ n : ℕ, ∃ (W : BigFppfOver B S hS) (a : W ⟶ V), IsAffineSpaceOver B S hS V W n a ∧
      IsClosedMorphism B S hS (pullback.fst (yoneda.map a ≫ g) f))
    {Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hZ : IsAlgebraicSpace B S hS Z) (h : Z ⟶ Y)
    (hh : IsLocallyOfFinitePresentation B S hS h) :
    IsClosedMorphism B S hS (pullback.fst h f)
```

**`AlgebraicGeometry.Space.isClosedMorphism_pullback_fst_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/UniversallyClosedAffineSpaceTest.lean, line 355](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/UniversallyClosedAffineSpaceTest.lean#L355). The attribute's comment: “(1) implies (2)”.

> **Stacks 0CM9, (1) implies (2).** The base change of a universally closed morphism of
> algebraic spaces over `S` along a morphism which is locally of finite presentation is
> closed.

```lean
theorem isClosedMorphism_pullback_fst_of_universallyClosed (f : X ⟶ Y)
    (hf : UniversallyClosed B S hS f) {Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hZ : IsAlgebraicSpace B S hS Z) (h : Z ⟶ Y)
    (_hh : IsLocallyOfFinitePresentation B S hS h) :
    IsClosedMorphism B S hS (pullback.fst h f)
```

**`AlgebraicGeometry.Space.exists_affineSpaceTest_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/UniversallyClosedAffineSpaceTest.lean, line 367](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/UniversallyClosedAffineSpaceTest.lean#L367). The attribute's comment: “(1) implies (3)”.

> **Stacks 0CM9, (1) implies (3).** A universally closed morphism of algebraic spaces over
> `S` passes the affine-space test over every surjective étale scheme atlas of its target: each
> affine space over the atlas is an object of the site mapping to the target, so the base change
> of `f` along it is closed.

```lean
theorem exists_affineSpaceTest_of_universallyClosed (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : UniversallyClosed B S hS f) :
    ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
      IsSurjective B S hS g ∧ IsEtale B S hS g ∧
        ∀ n : ℕ, ∃ (W : BigFppfOver B S hS) (a : W ⟶ V), IsAffineSpaceOver B S hS V W n a ∧
          IsClosedMorphism B S hS (pullback.fst (yoneda.map a ≫ g) f)
```

**`AlgebraicGeometry.Space.universallyClosed_of_isClosedMorphism_of_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/UniversallyClosedAffineSpaceTest.lean, line 410](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/UniversallyClosedAffineSpaceTest.lean#L410). The attribute's comment: “(2) implies (1)”.

> **Stacks 0CM9, (2) implies (1).** A quasi-compact morphism of algebraic spaces over `S`
> whose base changes along the morphisms locally of finite presentation are closed is
> universally closed.
>
> Let `T ⊆ |X ×_Y Z|` be closed and let `z` be a point of `|Z|` outside the image of `T`. The
> separation statement of Tag 0CM8 produces an étale neighbourhood `(V, v)` of `z`, a
> factorization `V ⟶ Z' ⟶ Y` with `Z' ⟶ Y` locally of finite presentation, and a closed
> `T' ⊆ |X ×_Y Z'|` receiving the inverse image of `T` and missing the image of `v`. Since
> `|V| → |Z|` is open, `v` lies in the closure of the inverse image of the image of `T`, which
> by Tag 03H4 is the image of the inverse image of `T` in `|X ×_Y V|`; that image lands in the
> inverse image along `V ⟶ Z'` of the image of `T'`, a closed set by hypothesis. Hence the image
> of `v` lies in the image of `T'` after all, so `z` is not in the closure of the image of
> `T`.

```lean
theorem universallyClosed_of_isClosedMorphism_of_isLocallyOfFinitePresentation
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsQuasiCompact B S hS f)
    (htest : ∀ (Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS Z →
      ∀ h : Z ⟶ Y, IsLocallyOfFinitePresentation B S hS h →
        IsClosedMorphism B S hS (pullback.fst h f)) :
    UniversallyClosed B S hS f
```

**`AlgebraicGeometry.Space.universallyClosed_tfae_of_isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/UniversallyClosedAffineSpaceTest.lean, line 463](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/UniversallyClosedAffineSpaceTest.lean#L463).

> **Stacks 0CM9.** For a quasi-compact morphism `f : X ⟶ Y` of algebraic spaces over `S` the
> following are equivalent: `f` is universally closed; the base change of `f` along every
> morphism to `Y` which is locally of finite presentation is closed; and there is a surjective
> étale morphism to `Y` from a presheaf represented by an object `V` of the site such that for
> every `n` the base change of `f` along affine `n`-space over `V` is closed.
>
> The implication from the second condition to the first is the one using quasi-compactness of
> `f`, through the separation statement of Tag 0CM8.

```lean
theorem universallyClosed_tfae_of_isQuasiCompact (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsQuasiCompact B S hS f) :
    List.TFAE
      [UniversallyClosed B S hS f,
        ∀ (Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS Z →
          ∀ h : Z ⟶ Y, IsLocallyOfFinitePresentation B S hS h →
            IsClosedMorphism B S hS (pullback.fst h f),
        ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
          IsSurjective B S hS g ∧ IsEtale B S hS g ∧
            ∀ n : ℕ, ∃ (W : BigFppfOver B S hS) (a : W ⟶ V),
              IsAffineSpaceOver B S hS V W n a ∧
                IsClosedMorphism B S hS (pullback.fst (yoneda.map a ≫ g) f)]
```

## Tag 0CMA, a lemma

[Tag 0CMA](https://stacks.math.columbia.edu/tag/0CMA) in the Stacks Project.

**`AlgebraicGeometry.Space.isClosedMorphism_pullback_fst_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/ProperAffineSpaceTest.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/ProperAffineSpaceTest.lean#L90). The attribute's comment: “(1) implies (2)”.

> **Stacks 0CMA, (1) implies (2).** The base change of a proper morphism of algebraic spaces
> over `S` along a morphism which is locally of finite presentation is closed.
>
> A proper morphism is universally closed, so this is the corresponding implication of Tag
> 0CM9.

```lean
theorem isClosedMorphism_pullback_fst_of_isProper (f : X ⟶ Y) (hf : IsProper B S hS f)
    {Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hZ : IsAlgebraicSpace B S hS Z) (h : Z ⟶ Y)
    (hh : IsLocallyOfFinitePresentation B S hS h) :
    IsClosedMorphism B S hS (pullback.fst h f)
```

**`AlgebraicGeometry.Space.exists_affineSpaceTest_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/ProperAffineSpaceTest.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/ProperAffineSpaceTest.lean#L103). The attribute's comment: “(1) implies (3)”.

> **Stacks 0CMA, (1) implies (3).** A proper morphism of algebraic spaces over `S` passes the
> affine-space test over a surjective étale scheme atlas of its target: for every `n` the base
> change of `f` along affine `n`-space over the atlas is closed.
>
> A proper morphism is universally closed, so this is the corresponding implication of Tag
> 0CM9.

```lean
theorem exists_affineSpaceTest_of_isProper (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsProper B S hS f) :
    ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
      IsSurjective B S hS g ∧ IsEtale B S hS g ∧
        ∀ n : ℕ, ∃ (W : BigFppfOver B S hS) (a : W ⟶ V), IsAffineSpaceOver B S hS V W n a ∧
          IsClosedMorphism B S hS (pullback.fst (yoneda.map a ≫ g) f)
```

**`AlgebraicGeometry.Space.isProper_of_isClosedMorphism_pullback_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/ProperAffineSpaceTest.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/ProperAffineSpaceTest.lean#L121). The attribute's comment: “(2) implies (1)”.

> **Stacks 0CMA, (2) implies (1).** A separated morphism of finite type between algebraic
> spaces over `S` whose base changes along the morphisms locally of finite presentation are
> closed is proper.
>
> Properness is separatedness, finite type and universal closedness; the first two are the
> standing hypotheses and the third is supplied by Tag 0CM9, whose quasi-compactness hypothesis
> is the second conjunct of finite type.

```lean
theorem isProper_of_isClosedMorphism_pullback_fst (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hsep : IsSeparated B S hS f)
    (hft : IsFiniteType B S hS f)
    (htest : ∀ (Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS Z →
      ∀ h : Z ⟶ Y, IsLocallyOfFinitePresentation B S hS h →
        IsClosedMorphism B S hS (pullback.fst h f)) :
    IsProper B S hS f
```

**`AlgebraicGeometry.Space.isProper_of_affineSpaceTest`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/ProperAffineSpaceTest.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/ProperAffineSpaceTest.lean#L138). The attribute's comment: “(3) implies (1)”. References: EGA II (5.6.3), “more general”.

> **Stacks 0CMA, (3) implies (1).** A separated morphism of finite type between algebraic
> spaces over `S` which passes the affine-space test over one surjective étale scheme atlas of
> its target is proper.
>
> The affine-space test gives closedness of the base changes along the morphisms locally of
> finite presentation, by Tag 0CM9, and that in turn gives universal closedness.

```lean
theorem isProper_of_affineSpaceTest (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hsep : IsSeparated B S hS f)
    (hft : IsFiniteType B S hS f) (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y)
    (hgsurj : IsSurjective B S hS g) (hgetale : IsEtale B S hS g)
    (htest : ∀ n : ℕ, ∃ (W : BigFppfOver B S hS) (a : W ⟶ V), IsAffineSpaceOver B S hS V W n a ∧
      IsClosedMorphism B S hS (pullback.fst (yoneda.map a ≫ g) f)) :
    IsProper B S hS f
```

**`AlgebraicGeometry.Space.isProper_tfae_of_isSeparated_of_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/ProperAffineSpaceTest.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/ProperAffineSpaceTest.lean#L160).

> **Stacks 0CMA.** For a separated morphism `f : X ⟶ Y` of finite type between algebraic
> spaces over `S` the following are equivalent: `f` is proper; the base change of `f` along every
> morphism to `Y` which is locally of finite presentation is closed; and there is a surjective
> étale morphism to `Y` from a presheaf represented by an object `V` of the site such that for
> every `n` the base change of `f` along affine `n`-space over `V` is closed.
>
> This is the special case of Tag 0CM9 obtained by unfolding properness into separatedness,
> finite type and universal closedness.

```lean
theorem isProper_tfae_of_isSeparated_of_isFiniteType (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hsep : IsSeparated B S hS f)
    (hft : IsFiniteType B S hS f) :
    List.TFAE
      [IsProper B S hS f,
        ∀ (Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS Z →
          ∀ h : Z ⟶ Y, IsLocallyOfFinitePresentation B S hS h →
            IsClosedMorphism B S hS (pullback.fst h f),
        ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
          IsSurjective B S hS g ∧ IsEtale B S hS g ∧
            ∀ n : ℕ, ∃ (W : BigFppfOver B S hS) (a : W ⟶ V),
              IsAffineSpaceOver B S hS V W n a ∧
                IsClosedMorphism B S hS (pullback.fst (yoneda.map a ≫ g) f)]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.20, Tag 0CM7](https://stacks.math.columbia.edu/tag/0CM7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
