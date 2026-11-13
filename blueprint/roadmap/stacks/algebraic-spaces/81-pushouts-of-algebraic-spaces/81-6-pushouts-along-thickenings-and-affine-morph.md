---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isPushout_algebraicSpaces_of_isThickening_of_isAffineHom, AlgebraicGeometry.Space.exists_hasPushout_isThickeningHom_inr_isPullback_appTop, AlgebraicGeometry.Space.pushout_spec_of_isThickeningHom, AlgebraicGeometry.Space.hasPushout_of_isThickeningHom_of_isAffineHom, AlgebraicGeometry.Space.pushout_inr_isThickeningHom, AlgebraicGeometry.Space.pushout_isPullback_appTop, AlgebraicGeometry.Space.pushoutGluing_spec_of_isThickeningHom, AlgebraicGeometry.Space.isPullback_right_of_isPullback_of_surjective_etale
statement: formalized
proof: formalized
---

# 81.6 Pushouts along thickenings and affine morphisms

Section 81.6 of the Stacks Project, [Tag 07SW](https://stacks.math.columbia.edu/tag/07SW). 9 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07SY, a lemma

[Tag 07SY](https://stacks.math.columbia.edu/tag/07SY) in the Stacks Project.

**`AlgebraicGeometry.Space.isPushout_algebraicSpaces_of_isThickening_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffine.lean, line 1087](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffine.lean#L1087).

> **Stacks 07SY.** The pushout `Y' = Y ⨿_X X'` of a thickening `X ⟶ X'` and an affine morphism
> `X ⟶ Y` of schemes over `S` is also a pushout in the category of algebraic spaces over `S`. The
> étale clause of Stacks 07RX enters through `Stacks.Pushout.etale_gluingFunctor_obj_iff` and
> Stacks 06AD through `Stacks.Thickenings.forall_isAffine_of_isThickening`.

```lean
public theorem isPushout_algebraicSpaces_of_isThickening_of_isAffineHom
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X X' Y Y' : BigFppfOver B S hS}
    (i : X ⟶ X') (f : X ⟶ Y) (a : X' ⟶ Y') (b : Y ⟶ Y')
    (hi : IsThickening ((BigFppfOver.toScheme B S hS).map i))
    [IsAffineHom ((BigFppfOver.toScheme B S hS).map f)]
    (hPushout : IsPushout ((BigFppfOver.toScheme B S hS).map i)
      ((BigFppfOver.toScheme B S hS).map f)
      ((BigFppfOver.toScheme B S hS).map a)
      ((BigFppfOver.toScheme B S hS).map b)) :
    IsPushout
      (ObjectProperty.homMk (yoneda.map i) :
        (⟨yoneda.obj X, isAlgebraicSpace_yoneda B S hS X⟩ : AlgebraicSpaces B S hS) ⟶
        (⟨yoneda.obj X', isAlgebraicSpace_yoneda B S hS X'⟩ : AlgebraicSpaces B S hS))
      (ObjectProperty.homMk (yoneda.map f) :
        (⟨yoneda.obj X, isAlgebraicSpace_yoneda B S hS X⟩ : AlgebraicSpaces B S hS) ⟶
        (⟨yoneda.obj Y, isAlgebraicSpace_yoneda B S hS Y⟩ : AlgebraicSpaces B S hS))
      (ObjectProperty.homMk (yoneda.map a) :
        (⟨yoneda.obj X', isAlgebraicSpace_yoneda B S hS X'⟩ : AlgebraicSpaces B S hS) ⟶
        (⟨yoneda.obj Y', isAlgebraicSpace_yoneda B S hS Y'⟩ : AlgebraicSpaces B S hS))
      (ObjectProperty.homMk (yoneda.map b) :
        (⟨yoneda.obj Y, isAlgebraicSpace_yoneda B S hS Y⟩ : AlgebraicSpaces B S hS) ⟶
        (⟨yoneda.obj Y', isAlgebraicSpace_yoneda B S hS Y'⟩ : AlgebraicSpaces B S hS))
```

## Tag 07VX, a lemma

[Tag 07VX](https://stacks.math.columbia.edu/tag/07VX) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_hasPushout_isThickeningHom_inr_isPullback_appTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTag.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTag.lean#L59).

> **Stacks 07VX.**  Let `i : X ⟶ X'` be a thickening and `f : X ⟶ Y` an affine morphism of
> algebraic spaces over `S`.  Then
>
> 1. there is a pushout `Y' = Y ⨿_X X'` in the category of algebraic spaces over `S`;
> 2. `Y ⟶ Y'` is a thickening, so `Y'` is a thickening of `Y`;
> 3. `𝒪_{Y'} = 𝒪_Y ×_{f_*𝒪_X} f'_*𝒪_{X'}` as sheaves on `Y_étale = (Y')_étale`, evaluated on each
>    of its objects: for a scheme `W` étale over `Y'` with base changes `W₁` to `X'`, `W₂` to `Y`
>    and `W₀` to `X`, the ring `Γ(W, 𝒪)` is the fibre product of `Γ(W₂, 𝒪)` and `Γ(W₁, 𝒪)` over
>    `Γ(W₀, 𝒪)`.
>
> The objects of the small étale site of `Y'` are the schemes étale over `Y'`, and the sections over
> `W` of `𝒪_Y`, `f_*𝒪_X` and `f'_*𝒪_{X'}` are the rings of functions on `W₂`, `W₀` and `W₁`.  Limits
> of sheaves are computed objectwise, so the objectwise statement (3) is the equality of sheaves of
> the source.

```lean
theorem exists_hasPushout_isThickeningHom_inr_isPullback_appTop
    {X X' Y : AlgebraicSpaces B S hS} (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsThickeningHom B S hS i) (hf : IsAffineHom B S hS f.hom) :
    ∃ _ : HasPushout i f,
      IsThickeningHom B S hS (pushout.inr i f) ∧
      ∀ {W W₁ W₂ W₀ : BigFppfOver B S hS} (w : yoneda.obj W ⟶ (pushout i f).1)
        (_hwE : IsEtale B S hS w)
        {u₁ : W₁ ⟶ W} {p₁ : yoneda.obj W₁ ⟶ X'.1}
        (_h₁ : IsPullback (yoneda.map u₁) p₁ w (pushout.inl i f).hom)
        {u₂ : W₂ ⟶ W} {p₂ : yoneda.obj W₂ ⟶ Y.1}
        (_h₂ : IsPullback (yoneda.map u₂) p₂ w (pushout.inr i f).hom)
        {iW : W₀ ⟶ W₁} {fW : W₀ ⟶ W₂} {p₀ : yoneda.obj W₀ ⟶ X.1}
        (_h₀₁ : IsPullback (yoneda.map iW) p₀ p₁ i.hom)
        (_h₀₂ : IsPullback (yoneda.map fW) p₀ p₂ f.hom)
        (hw₀ : iW ≫ u₁ = fW ≫ u₂),
        let Φ := BigFppfOver.toScheme B S hS
        IsPullback ((Φ.map u₂).app ⊤) ((Φ.map u₁).app ⊤) ((Φ.map fW).app ((Φ.map u₂) ⁻¹ᵁ ⊤))
          ((Φ.map iW).app ((Φ.map u₁) ⁻¹ᵁ ⊤) ≫ eqToHom (congrArg (fun O ↦ Γ(Φ.obj W₀, O))
            (congrArg (fun k : Φ.obj W₀ ⟶ Φ.obj W ↦ k ⁻¹ᵁ ⊤)
              (show Φ.map iW ≫ Φ.map u₁ = Φ.map fW ≫ Φ.map u₂ by
                rw [← Φ.map_comp, ← Φ.map_comp, hw₀]))))
```

**`AlgebraicGeometry.Space.pushout_spec_of_isThickeningHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTags.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTags.lean#L66).

> **[Stacks Project, Tag 07VX].** Let `i : X ⟶ X'` be a thickening of algebraic spaces over
> `S` and `f : X ⟶ Y` an affine morphism. The pushout `Y' = Y ⨿_X X'` exists in the category of
> algebraic spaces over `S`, the morphism `Y ⟶ Y'` is a thickening, and
> `𝒪_{Y'} = 𝒪_Y ×_{f_*𝒪_X} f'_*𝒪_{X'}` as sheaves on the small étale site of `Y'`: over every
> object `W ⟶ Y'` of that site — indeed over every scheme `W` flat over `Y'` — the ring of
> functions on `W` is the fibre product of the rings of functions on `W ×_{Y'} Y` and on
> `W ×_{Y'} X'` over the ring of functions on `W ×_{Y'} X`.

```lean
theorem pushout_spec_of_isThickeningHom :
    let hatlas : HasThickeningAffineAtlases B S hS :=
      hasThickeningAffineAtlases_of_chartLift B S hS (hasEtaleChartLifts B S hS)
    HasPushout i f ∧
      (letI := hasPushout_of_isThickening_of_isAffineHom B S hS hatlas i f hi hf
      IsThickeningHom B S hS (pushout.inr i f) ∧
      ∀ {W WX' WY WX : BigFppfOver B S hS} {cX' : WX' ⟶ W} {cY : WY ⟶ W} {jX' : WX ⟶ WX'}
        {jY : WX ⟶ WY} {w : schemeSpace W ⟶ pushout i f} {pX' : schemeSpace WX' ⟶ X'}
        {pY : schemeSpace WY ⟶ Y} {pX : schemeSpace WX ⟶ X}, IsFlat B S hS w.hom →
        IsPullback (schemeSpaceMap cX') pX' w (pushout.inl i f) →
        IsPullback (schemeSpaceMap cY) pY w (pushout.inr i f) →
        IsPullback (schemeSpaceMap jY) pX pY f → schemeSpaceMap jX' ≫ pX' = pX ≫ i →
        jY ≫ cY = jX' ≫ cX' →
        IsPullback (Scheme.Γ.map ((BigFppfOver.toScheme B S hS).map cY).op)
          (Scheme.Γ.map ((BigFppfOver.toScheme B S hS).map cX').op)
          (Scheme.Γ.map ((BigFppfOver.toScheme B S hS).map jY).op)
          (Scheme.Γ.map ((BigFppfOver.toScheme B S hS).map jX').op))
```

**`AlgebraicGeometry.Space.hasPushout_of_isThickeningHom_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTheorem.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTheorem.lean#L119). The attribute's comment: “existence of the pushout”.

> **Stacks 07VX, existence.** A thickening `i : X ⟶ X'` and an affine morphism `f : X ⟶ Y` of
> algebraic spaces over `S` have a pushout `Y' = Y ⨿_X X'` in the category of algebraic spaces over
> `S`.

```lean
theorem hasPushout_of_isThickeningHom_of_isAffineHom
    {X X' Y : AlgebraicSpaces B S hS} (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsThickeningHom B S hS i) (hf : IsAffineHom B S hS f.hom) : HasPushout i f
```

**`AlgebraicGeometry.Space.pushout_inr_isThickeningHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTheorem.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTheorem.lean#L126). The attribute's comment: “the pushout is a thickening of Y”.

> **Stacks 07VX, `Y' = Y ⨿_X X'` is a thickening of `Y`.**

```lean
theorem pushout_inr_isThickeningHom
    {X X' Y : AlgebraicSpaces B S hS} (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsThickeningHom B S hS i) (hf : IsAffineHom B S hS f.hom) [HasPushout i f] :
    IsThickeningHom B S hS (pushout.inr i f)
```

**`AlgebraicGeometry.Space.pushout_isPullback_appTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTheorem.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTheorem.lean#L142). The attribute's comment: “the structure sheaf”.

> **Stacks 07VX, the structure sheaf.** `𝒪_{Y'} = 𝒪_Y ×_{f_*𝒪_X} f'_*𝒪_{X'}` as sheaves on the
> small étale site of `Y'`, evaluated on each of its objects: for a scheme `W` étale over `Y'`
> with base changes `W₁` to `X'`, `W₂` to `Y` and `W₀` to `X`, the ring `Γ(W, 𝒪)` is the fibre
> product of `Γ(W₂, 𝒪)` and `Γ(W₁, 𝒪)` over `Γ(W₀, 𝒪)`.
>
> The objects of the small étale site of `Y'` are the schemes étale over `Y'`, and the sections over
> `W` of `𝒪_Y`, `f_*𝒪_X` and `f'_*𝒪_{X'}` are the rings of functions on `W₂`, `W₀` and `W₁`. Limits
> of sheaves are computed objectwise, so this objectwise statement is the same as the equality of
> sheaves of the source.

```lean
theorem pushout_isPullback_appTop
    {X X' Y : AlgebraicSpaces B S hS} (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsThickeningHom B S hS i) (hf : IsAffineHom B S hS f.hom) [HasPushout i f]
    {W W₁ W₂ W₀ : BigFppfOver B S hS} (w : yoneda.obj W ⟶ (pushout i f).1)
    (hwE : IsEtale B S hS w)
    {u₁ : W₁ ⟶ W} {p₁ : yoneda.obj W₁ ⟶ X'.1}
    (h₁ : IsPullback (yoneda.map u₁) p₁ w (pushout.inl i f).hom)
    {u₂ : W₂ ⟶ W} {p₂ : yoneda.obj W₂ ⟶ Y.1}
    (h₂ : IsPullback (yoneda.map u₂) p₂ w (pushout.inr i f).hom)
    {iW : W₀ ⟶ W₁} {fW : W₀ ⟶ W₂} {p₀ : yoneda.obj W₀ ⟶ X.1}
    (h₀₁ : IsPullback (yoneda.map iW) p₀ p₁ i.hom) (h₀₂ : IsPullback (yoneda.map fW) p₀ p₂ f.hom)
    (hw₀ : iW ≫ u₁ = fW ≫ u₂) :
    let Φ := BigFppfOver.toScheme B S hS
    IsPullback ((Φ.map u₂).app ⊤) ((Φ.map u₁).app ⊤) ((Φ.map fW).app ((Φ.map u₂) ⁻¹ᵁ ⊤))
      ((Φ.map iW).app ((Φ.map u₁) ⁻¹ᵁ ⊤) ≫ eqToHom (congrArg (fun O ↦ Γ(Φ.obj W₀, O))
        (congrArg (fun k : Φ.obj W₀ ⟶ Φ.obj W ↦ k ⁻¹ᵁ ⊤)
          (show Φ.map iW ≫ Φ.map u₁ = Φ.map fW ≫ Φ.map u₂ by
            rw [← Φ.map_comp, ← Φ.map_comp, hw₀]))))
```

## Tag 07VY, a lemma

[Tag 07VY](https://stacks.math.columbia.edu/tag/07VY) in the Stacks Project.

**`AlgebraicGeometry.Space.pushoutGluing_spec_of_isThickeningHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTags.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTags.lean#L91).

> **[Stacks Project, Tag 07VY].** Let `i : X ⟶ X'` be a thickening of algebraic spaces over
> `S`, `f : X ⟶ Y` an affine morphism and `Y' = Y ⨿_X X'`. The base-change functor
> `F : V' ↦ (V' ×_{Y'} Y, V' ×_{Y'} X', 1)` sends schemes over `Y'` to pairs of schemes; it has
> the left adjoint `G`, which sends a triple `(V, U', φ)` to the pushout `V ⨿_{V ×_Y X} U'` with
> its structure morphism to `Y'`; and `G` sends pairs of schemes to schemes.

```lean
theorem pushoutGluing_spec_of_isThickeningHom :
    let hatlas : HasThickeningAffineAtlases B S hS :=
      hasThickeningAffineAtlases_of_chartLift B S hS (hasEtaleChartLifts B S hS)
    letI := hasPushout_of_isThickening_of_isAffineHom B S hS hatlas i f hi hf
    (∀ Z : Over (pushout i f), Z.left.1.IsRepresentable →
        ((pushoutBaseChangeFunctor B S hS hatlas i f hi hf).obj Z).obj.left.left.1.IsRepresentable ∧
        ((pushoutBaseChangeFunctor B S hS hatlas i f hi hf).obj
          Z).obj.right.left.1.IsRepresentable) ∧
      Nonempty (pushoutGluingFunctor B S hS hatlas i f hi hf ⊣
        pushoutBaseChangeFunctor B S hS hatlas i f hi hf) ∧
      (∀ T : pushoutGluingData B S hS i f,
        ∃ (v : T.obj.left.left ⟶ ((pushoutGluingFunctor B S hS hatlas i f hi hf).obj T).left)
          (u' : T.obj.right.left ⟶ ((pushoutGluingFunctor B S hS hatlas i f hi hf).obj T).left),
          IsPushout (CategoryTheory.PushoutGluing.sourceMap i f T)
              (pullback.fst T.obj.right.hom i) v u' ∧
            v ≫ ((pushoutGluingFunctor B S hS hatlas i f hi hf).obj T).hom =
              T.obj.left.hom ≫ pushout.inr i f ∧
            u' ≫ ((pushoutGluingFunctor B S hS hatlas i f hi hf).obj T).hom =
              T.obj.right.hom ≫ pushout.inl i f) ∧
      (∀ T : pushoutGluingData B S hS i f, T.obj.left.left.1.IsRepresentable →
        T.obj.right.left.1.IsRepresentable →
        ((pushoutGluingFunctor B S hS hatlas i f hi hf).obj T).left.1.IsRepresentable)
```

## Tag 07VZ, a lemma

[Tag 07VZ](https://stacks.math.columbia.edu/tag/07VZ) in the Stacks Project.

**`AlgebraicGeometry.Space.isPullback_right_of_isPullback_of_surjective_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CartesianSquareDescent.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CartesianSquareDescent.lean#L157).

> **Stacks 07VZ.** Let `S` be a scheme and let `A, B, C, D, E, F` be algebraic spaces over `S`
> sitting in a commutative diagram with rows `A ⟶ C ⟶ E` and `B ⟶ D ⟶ F` and vertical maps
> `A ⟶ B`, `C ⟶ D`, `E ⟶ F`. If the square `A, B, C, D` and the outer rectangle `A, B, E, F` are
> cartesian and `B ⟶ D` is surjective and étale, then the square `C, D, E, F` is cartesian.

```lean
theorem isPullback_right_of_isPullback_of_surjective_etale
    (_hA : IsAlgebraicSpace B₀ S hS A) (hB : IsAlgebraicSpace B₀ S hS B)
    (hC : IsAlgebraicSpace B₀ S hS C) (hD : IsAlgebraicSpace B₀ S hS D)
    (hE : IsAlgebraicSpace B₀ S hS E) (_hF : IsAlgebraicSpace B₀ S hS F)
    (hcomm : cE ≫ eF = cD ≫ dF)
    (hleft : IsPullback aC aB cD bD)
    (houter : IsPullback (aC ≫ cE) aB eF (bD ≫ dF))
    (hsurj : IsSurjective B₀ S hS bD) (hetale : IsEtale B₀ S hS bD) :
    IsPullback cE cD eF dF
```

## Tag 07W0, a lemma

[Tag 07W0](https://stacks.math.columbia.edu/tag/07W0) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_pushoutGluingAdjunction_unit_of_isThickeningHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTags.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTags.lean#L165).

> **[Stacks Project, Tag 07W0].** Let `i : X ⟶ X'` be a thickening of algebraic spaces over
> `S`, `f : X ⟶ Y` an affine morphism, `Y' = Y ⨿_X X'`, and let `G ⊣ F` be the gluing adjunction
> of [Stacks Project, Tag 07VY], with `F : V' ↦ (V' ×_{Y'} Y, V' ×_{Y'} X', 1)` and `G` sending a
> triple `(V, U', φ)` to `V ⨿_{V ×_Y X} U'`. Then `F ∘ G` is isomorphic to the identity functor
> of the category of triples; indeed the unit `𝟭 ⟶ G ⋙ F` of the adjunction is an isomorphism.

```lean
theorem isIso_pushoutGluingAdjunction_unit_of_isThickeningHom :
    let hatlas : HasThickeningAffineAtlases B S hS :=
      hasThickeningAffineAtlases_of_chartLift B S hS (hasEtaleChartLifts B S hS)
    letI := hasPushout_of_isThickening_of_isAffineHom B S hS hatlas i f hi hf
    IsIso (pushoutGluingAdjunction B S hS hatlas i f hi hf).unit ∧
      Nonempty (pushoutGluingFunctor B S hS hatlas i f hi hf ⋙
          pushoutBaseChangeFunctor B S hS hatlas i f hi hf ≅
        𝟭 (pushoutGluingData B S hS i f))
```

## Tag 07W1, an equation

[Tag 07W1](https://stacks.math.columbia.edu/tag/07W1) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_etaleChartCube`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTags.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTags.lean#L190).

> **[Stacks Project, Tag 07W1]**, equation 81.6.5.1 of the proof of Stacks 07W0. Let
> `i : X ⟶ X'` be a thickening of algebraic spaces over `S` and `f : X ⟶ Y` an affine morphism.
> There is a cube whose back square is the pushout `Y' = Y ⨿_X X'` of algebraic spaces and whose
> front square is the pushout `P = V ⨿_U U'` of étale scheme charts, with `U ⟶ U'` a thickening
> and `U ⟶ V` affine, whose four lateral squares are cartesian and whose four northeast arrows
> are surjective and étale.

```lean
theorem exists_etaleChartCube
    {X X' Y : AlgebraicSpaces B S hS} (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsThickeningHom B S hS i) (hf : IsAffineHom B S hS f.hom) :
    ∃ (U U' V P : BigFppfOver B S hS) (Y' : AlgebraicSpaces B S hS)
      (aY : X' ⟶ Y') (bY : Y ⟶ Y') (k : U ⟶ U') (g : U ⟶ V) (aP : U' ⟶ P) (bP : V ⟶ P)
      (p : yoneda.obj U ⟶ X.1) (p' : yoneda.obj U' ⟶ X'.1) (q : yoneda.obj V ⟶ Y.1)
      (r : yoneda.obj P ⟶ Y'.1),
      IsPushout i f aY bY ∧
      IsPushout ((BigFppfOver.toScheme B S hS).map k) ((BigFppfOver.toScheme B S hS).map g)
        ((BigFppfOver.toScheme B S hS).map aP) ((BigFppfOver.toScheme B S hS).map bP) ∧
      Stacks.Thickenings.IsThickening ((BigFppfOver.toScheme B S hS).map k) ∧
      _root_.AlgebraicGeometry.IsAffineHom ((BigFppfOver.toScheme B S hS).map g) ∧
      IsPullback (yoneda.map k) p p' i.hom ∧
      IsPullback p (yoneda.map g) f.hom q ∧
      IsPullback (yoneda.map aP) p' r aY.hom ∧
      IsPullback (yoneda.map bP) q r bY.hom ∧
      IsSurjective B S hS p ∧ IsEtale B S hS p ∧
      IsSurjective B S hS p' ∧ IsEtale B S hS p' ∧
      IsSurjective B S hS q ∧ IsEtale B S hS q ∧
      IsSurjective B S hS r ∧ IsEtale B S hS r
```

## Tag 07W2, an equation

[Tag 07W2](https://stacks.math.columbia.edu/tag/07W2) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_etaleChartCube_gluingData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTags.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTags.lean#L221).

> **[Stacks Project, Tag 07W2]**, equation 81.6.5.2 of the proof of Stacks 07W0. Let
> `i : X ⟶ X'` be a thickening of algebraic spaces over `S`, `f : X ⟶ Y` an affine morphism and
> `(V, U', φ)` a triple over the span. There is a cube over the span `U' ⟵ U ⟶ V` of the triple
> whose back square is the pushout `G(V, U', φ) = V ⨿_U U'` of algebraic spaces and whose front
> square is the pushout `G₁ = V₁ ⨿_{U₁} U₁'` of étale scheme charts, whose four lateral squares
> are cartesian and whose four northeast arrows are surjective and étale; in particular
> `G₁ ⟶ G(V, U', φ)` is surjective étale.

```lean
theorem exists_etaleChartCube_gluingData
    {X X' Y : AlgebraicSpaces B S hS} (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsThickeningHom B S hS i) (hf : IsAffineHom B S hS f.hom)
    (T : pushoutGluingData B S hS i f) :
    ∃ (U₁ U₁' V₁ G₁ : BigFppfOver B S hS) (G : AlgebraicSpaces B S hS)
      (aG : T.obj.right.left ⟶ G) (bG : T.obj.left.left ⟶ G) (k : U₁ ⟶ U₁') (g : U₁ ⟶ V₁)
      (aG₁ : U₁' ⟶ G₁) (bG₁ : V₁ ⟶ G₁)
      (p : yoneda.obj U₁ ⟶ (pullback T.obj.right.hom i).1)
      (p' : yoneda.obj U₁' ⟶ T.obj.right.left.1)
      (q : yoneda.obj V₁ ⟶ T.obj.left.left.1) (r : yoneda.obj G₁ ⟶ G.1),
      IsPushout (pullback.fst T.obj.right.hom i)
        (CategoryTheory.PushoutGluing.sourceMap i f T) aG bG ∧
      IsPushout ((BigFppfOver.toScheme B S hS).map k) ((BigFppfOver.toScheme B S hS).map g)
        ((BigFppfOver.toScheme B S hS).map aG₁) ((BigFppfOver.toScheme B S hS).map bG₁) ∧
      Stacks.Thickenings.IsThickening ((BigFppfOver.toScheme B S hS).map k) ∧
      _root_.AlgebraicGeometry.IsAffineHom ((BigFppfOver.toScheme B S hS).map g) ∧
      IsPullback (yoneda.map k) p p' (pullback.fst T.obj.right.hom i).hom ∧
      IsPullback p (yoneda.map g)
        (CategoryTheory.PushoutGluing.sourceMap i f T).hom q ∧
      IsPullback (yoneda.map aG₁) p' r aG.hom ∧
      IsPullback (yoneda.map bG₁) q r bG.hom ∧
      IsSurjective B S hS p ∧ IsEtale B S hS p ∧
      IsSurjective B S hS p' ∧ IsEtale B S hS p' ∧
      IsSurjective B S hS q ∧ IsEtale B S hS q ∧
      IsSurjective B S hS r ∧ IsEtale B S hS r
```

## Tag 08KV, a lemma

[Tag 08KV](https://stacks.math.columbia.edu/tag/08KV) in the Stacks Project.

**`AlgebraicGeometry.Space.PushoutModules.isFiniteType_iff_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningPushoutFiniteModules.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningPushoutFiniteModules.lean#L179). The attribute's comment: “(a)”.

> **Stacks Project, Tag 08KV (a).**  Let `i : X ⟶ X'` be a thickening and `f : X ⟶ Y` an affine
> morphism of algebraic spaces over `S`, let `Y' = Y ⨿_X X'` be their pushout (Stacks 07VX) and
> `g : V' ⟶ Y'` a morphism, with `V = Y ×_{Y'} V'` and `U' = X' ×_{Y'} V'`.  If a quasi-coherent
> `𝒪_{V'}`-module `𝒢'` flat over `Y'` corresponds to the triple `(𝒢, ℱ', φ)` under the equivalence
> `AlgebraicGeometry.Space.PushoutModules.isEquivalence_flatRestrictionFunctor`, so that
> `𝒢 = (V ⟶ V')^*𝒢'` and `ℱ' = (U' ⟶ V')^*𝒢'`, then `𝒢'` is of finite type if and only if `𝒢` and
> `ℱ'` are of finite type.

```lean
theorem isFiniteType_iff_restrict :
    letI := hasPushout_of_isThickeningHom_of_isAffineHom B S hS i f hi hf
    ∀ {V' : AlgebraicSpaces B S hS} (g : V' ⟶ pushout i f)
      (M : (FlatQuasicoherentOver g).FullSubcategory),
      M.obj.IsFiniteType ↔
        (((FlatQuasicoherentTriple i f g).lift ((FlatQuasicoherentOver g).ι ⋙
          (TripleGluing.restrictFunctor (squareOverlap (commonToTarget i f g)
            (targetRestriction i f g) (commonToAmbient i f g) (ambientRestriction i f g)
            (commonToAmbient_comp_eq i f g))))
          fun M => flatQuasicoherentTriple_restrict i f g M.obj
            M.property).obj M).obj.target.IsFiniteType ∧
        (((FlatQuasicoherentTriple i f g).lift ((FlatQuasicoherentOver g).ι ⋙
          (TripleGluing.restrictFunctor (squareOverlap (commonToTarget i f g)
            (targetRestriction i f g) (commonToAmbient i f g) (ambientRestriction i f g)
            (commonToAmbient_comp_eq i f g))))
          fun M => flatQuasicoherentTriple_restrict i f g M.obj
            M.property).obj M).obj.ambient.IsFiniteType
```

**`AlgebraicGeometry.Space.PushoutModules.isFinitePresentationOnSite_iff_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningPushoutFiniteModules.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningPushoutFiniteModules.lean#L309). The attribute's comment: “(b)”.

> **Stacks Project, Tag 08KV (b).**  Let `i : X ⟶ X'` be a thickening and `f : X ⟶ Y` an affine
> morphism of algebraic spaces over `S`, let `Y' = Y ⨿_X X'` be their pushout (Stacks 07VX) and
> `g : V' ⟶ Y'` a morphism **locally of finite presentation**, with `V = Y ×_{Y'} V'` and
> `U' = X' ×_{Y'} V'`.  If a quasi-coherent `𝒪_{V'}`-module `𝒢'` flat over `Y'` corresponds to the
> triple `(𝒢, ℱ', φ)` under the equivalence
> `AlgebraicGeometry.Space.PushoutModules.isEquivalence_flatRestrictionFunctor`, so that
> `𝒢 = (V ⟶ V')^*𝒢'` and `ℱ' = (U' ⟶ V')^*𝒢'`, then `𝒢'` is of finite presentation if and only if
> `𝒢` and `ℱ'` are of finite presentation
> (Stacks 03DL (7), `SheafOfModules.IsFinitePresentationOnSite`).

```lean
theorem isFinitePresentationOnSite_iff_restrict :
    letI := hasPushout_of_isThickeningHom_of_isAffineHom B S hS i f hi hf
    ∀ {V' : AlgebraicSpaces B S hS} (g : V' ⟶ pushout i f),
      IsLocallyOfFinitePresentation B S hS g.hom →
      ∀ M : (FlatQuasicoherentOver g).FullSubcategory,
      (SheafOfModules.IsFinitePresentationOnSite M.obj ↔
        SheafOfModules.IsFinitePresentationOnSite
          (((FlatQuasicoherentTriple i f g).lift ((FlatQuasicoherentOver g).ι ⋙
            (TripleGluing.restrictFunctor (squareOverlap (commonToTarget i f g)
              (targetRestriction i f g) (commonToAmbient i f g) (ambientRestriction i f g)
              (commonToAmbient_comp_eq i f g))))
            fun M => flatQuasicoherentTriple_restrict i f g M.obj M.property).obj M).obj.target ∧
        SheafOfModules.IsFinitePresentationOnSite
          (((FlatQuasicoherentTriple i f g).lift ((FlatQuasicoherentOver g).ι ⋙
            (TripleGluing.restrictFunctor (squareOverlap (commonToTarget i f g)
              (targetRestriction i f g) (commonToAmbient i f g) (ambientRestriction i f g)
              (commonToAmbient_comp_eq i f g))))
            fun M => flatQuasicoherentTriple_restrict i f g M.obj
              M.property).obj M).obj.ambient)
```

**`AlgebraicGeometry.Space.PushoutModules.isEquivalence_flatRestrictionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningPushoutFlatModules.lean, line 357](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningPushoutFlatModules.lean#L357). The attribute's comment: “the equivalence”.

> **Stacks Project, Tag 08KV, the equivalence.**  Let `i : X ⟶ X'` be a thickening and
> `f : X ⟶ Y` an affine morphism of algebraic spaces over `S`, let `Y' = Y ⨿_X X'` be their pushout
> (Stacks 07VX) and let `g : V' ⟶ Y'` be a morphism, with `V = Y ×_{Y'} V'`, `U' = X' ×_{Y'} V'`
> and `U = X ×_{Y'} V'`.  The functor `𝒢' ↦ ((V ⟶ V')^*𝒢', (U' ⟶ V')^*𝒢', can)` is an
> **equivalence of categories** from the quasi-coherent `𝒪_{V'}`-modules flat over `Y'` onto the
> triples `(𝒢, ℱ', φ)` of a quasi-coherent `𝒪_V`-module `𝒢` flat over `Y`, a quasi-coherent
> `𝒪_{U'}`-module `ℱ'` flat over `X'` and an isomorphism `φ : (U ⟶ V)^*𝒢 ≅ (U ⟶ U')^*ℱ'`.
>
> The source writes "`ℱ'` … flat over `X`": `ℱ'` lives on `U' = X' ×_{Y'} V'`, which lies over
> `X'`, so the condition is flatness over `X'`, as in the scheme case Stacks 08KU.  The pushout is
> not assumed: it exists by Stacks 07VX
> (`AlgebraicGeometry.Space.hasPushout_of_isThickeningHom_of_isAffineHom`), which is the instance
> the statement binds.  The functor is written out as the lift to the two full subcategories of
> `CategoryTheory.TripleGluing.restrictFunctor` at the canonical comparison
> `AlgebraicGeometry.Space.PushoutModules.squareOverlap`; a quasi-inverse is the gluing functor
> `(𝒢, ℱ', φ) ↦ (V ⟶ V')_*𝒢 ×_{(U ⟶ V')_*ℱ} (U' ⟶ V')_*ℱ'`
> (`isEquivalence_flatRestrictionFunctor_of_hasPushout`).

```lean
theorem isEquivalence_flatRestrictionFunctor :
    letI := hasPushout_of_isThickeningHom_of_isAffineHom B S hS i f hi hf
    ∀ {V' : AlgebraicSpaces B S hS} (g : V' ⟶ pushout i f),
      ((((FlatQuasicoherentTriple i f g).lift ((FlatQuasicoherentOver g).ι ⋙
      (TripleGluing.restrictFunctor (squareOverlap (commonToTarget i f g) (targetRestriction i f g)
      (commonToAmbient i f g) (ambientRestriction i f g) (commonToAmbient_comp_eq i f g))))
        fun M => flatQuasicoherentTriple_restrict i f g M.obj M.property) :
        (FlatQuasicoherentOver g).FullSubcategory ⥤
        (FlatQuasicoherentTriple i f g).FullSubcategory)).IsEquivalence
```

**`AlgebraicGeometry.Space.PushoutModules.isEquivalence_flatRestrictionFunctor_and_finiteness_iff_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningPushoutModulesTag.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningPushoutModulesTag.lean#L77).

> Let `i : X ⟶ X'` be a thickening and `f : X ⟶ Y` an affine morphism of algebraic spaces over
> `S`, let `Y' = Y ⨿_X X'` be their pushout (Stacks 07VX) and let `g : V' ⟶ Y'` be a morphism, with
> `V = Y ×_{Y'} V'`, `U' = X' ×_{Y'} V'` and `U = X ×_{Y'} V'`.
>
> * The functor `𝒢' ↦ ((V ⟶ V')^*𝒢', (U' ⟶ V')^*𝒢', can)` is an **equivalence of categories**
>   from the quasi-coherent `𝒪_{V'}`-modules flat over `Y'` onto the triples `(𝒢, ℱ', φ)` of a
>   quasi-coherent `𝒪_V`-module `𝒢` flat over `Y`, a quasi-coherent `𝒪_{U'}`-module `ℱ'` flat over
>   `X'` and an isomorphism `φ : (U ⟶ V)^*𝒢 ≅ (U ⟶ U')^*ℱ'`.
> * Suppose `𝒢'` corresponds to the triple `(𝒢, ℱ', φ)`, so that `𝒢 = (V ⟶ V')^*𝒢'` and
>   `ℱ' = (U' ⟶ V')^*𝒢'`. Then
>   (a) `𝒢'` is of finite type if and only if `𝒢` and `ℱ'` are of finite type;
>   (b) if `g` is locally of finite presentation, then `𝒢'` is of finite presentation if and only
>   if `𝒢` and `ℱ'` are of finite presentation (Stacks 03DL (7),
>   `SheafOfModules.IsFinitePresentationOnSite`).
>
> The source writes "`ℱ'` … flat over `X`": `ℱ'` lives on `U' = X' ×_{Y'} V'`, which lies over
> `X'`, so the condition is flatness over `X'`, as in the scheme case Stacks 08KU.  The pushout is
> not assumed: it exists by Stacks 07VX
> (`AlgebraicGeometry.Space.hasPushout_of_isThickeningHom_of_isAffineHom`), which is the instance
> the statement binds.  The functor is written out as the lift to the two full subcategories of
> `CategoryTheory.TripleGluing.restrictFunctor` at the canonical comparison
> `AlgebraicGeometry.Space.PushoutModules.squareOverlap`; a quasi-inverse is the gluing functor
> `(𝒢, ℱ', φ) ↦ (V ⟶ V')_*𝒢 ×_{(U ⟶ V')_*ℱ} (U' ⟶ V')_*ℱ'`
> (`isEquivalence_flatRestrictionFunctor_of_hasPushout`).

```lean
theorem isEquivalence_flatRestrictionFunctor_and_finiteness_iff_restrict :
    letI := hasPushout_of_isThickeningHom_of_isAffineHom B S hS i f hi hf
    ∀ {V' : AlgebraicSpaces B S hS} (g : V' ⟶ pushout i f),
      ((((FlatQuasicoherentTriple i f g).lift ((FlatQuasicoherentOver g).ι ⋙
          (TripleGluing.restrictFunctor (squareOverlap (commonToTarget i f g)
            (targetRestriction i f g) (commonToAmbient i f g) (ambientRestriction i f g)
            (commonToAmbient_comp_eq i f g))))
        fun M => flatQuasicoherentTriple_restrict i f g M.obj M.property) :
        (FlatQuasicoherentOver g).FullSubcategory ⥤
          (FlatQuasicoherentTriple i f g).FullSubcategory)).IsEquivalence ∧
      (∀ (M : (FlatQuasicoherentOver g).FullSubcategory),
        M.obj.IsFiniteType ↔
          (((FlatQuasicoherentTriple i f g).lift ((FlatQuasicoherentOver g).ι ⋙
            (TripleGluing.restrictFunctor (squareOverlap (commonToTarget i f g)
              (targetRestriction i f g) (commonToAmbient i f g) (ambientRestriction i f g)
              (commonToAmbient_comp_eq i f g))))
            fun M => flatQuasicoherentTriple_restrict i f g M.obj
              M.property).obj M).obj.target.IsFiniteType ∧
          (((FlatQuasicoherentTriple i f g).lift ((FlatQuasicoherentOver g).ι ⋙
            (TripleGluing.restrictFunctor (squareOverlap (commonToTarget i f g)
              (targetRestriction i f g) (commonToAmbient i f g) (ambientRestriction i f g)
              (commonToAmbient_comp_eq i f g))))
            fun M => flatQuasicoherentTriple_restrict i f g M.obj
              M.property).obj M).obj.ambient.IsFiniteType) ∧
      (IsLocallyOfFinitePresentation B S hS g.hom →
        ∀ M : (FlatQuasicoherentOver g).FullSubcategory,
        (SheafOfModules.IsFinitePresentationOnSite M.obj ↔
          SheafOfModules.IsFinitePresentationOnSite
            (((FlatQuasicoherentTriple i f g).lift ((FlatQuasicoherentOver g).ι ⋙
              (TripleGluing.restrictFunctor (squareOverlap (commonToTarget i f g)
                (targetRestriction i f g) (commonToAmbient i f g) (ambientRestriction i f g)
                (commonToAmbient_comp_eq i f g))))
              fun M => flatQuasicoherentTriple_restrict i f g M.obj M.property).obj M).obj.target ∧
          SheafOfModules.IsFinitePresentationOnSite
            (((FlatQuasicoherentTriple i f g).lift ((FlatQuasicoherentOver g).ι ⋙
              (TripleGluing.restrictFunctor (squareOverlap (commonToTarget i f g)
                (targetRestriction i f g) (commonToAmbient i f g) (ambientRestriction i f g)
                (commonToAmbient_comp_eq i f g))))
              fun M => flatQuasicoherentTriple_restrict i f g M.obj
                M.property).obj M).obj.ambient))
```

## Tag 07W3, a lemma

[Tag 07W3](https://stacks.math.columbia.edu/tag/07W3) in the Stacks Project.

**`AlgebraicGeometry.Space.pushoutGluing_flat_of_isThickeningHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTags.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ThickeningAffinePushoutTags.lean#L125).

> **[Stacks Project, Tag 07W3].** Let `i : X ⟶ X'` be a thickening of algebraic spaces over
> `S`, `f : X ⟶ Y` an affine morphism, `Y' = Y ⨿_X X'` and `G ⊣ F` the gluing adjunction of
> [Stacks Project, Tag 07VY]. For a triple `(V, U', φ)`, the glued space `G(V, U', φ) ⟶ Y'` is
> (1) locally of finite type, (2) flat, (3) flat and locally of finite presentation, (4) smooth,
> (5) étale, if and only if both `V ⟶ Y` and `U' ⟶ X'` are. If `W'` is flat over `Y'` the counit
> `G(F(W')) ⟶ W'` is an isomorphism; the unit is an isomorphism; `F` sends spaces flat over `Y'`
> to flat triples and `G` sends flat triples to spaces flat over `Y'`; so `F` and `G` are mutually
> quasi-inverse between the spaces flat over `Y'` and the triples with `V ⟶ Y` and `U' ⟶ X'`
> flat.

```lean
theorem pushoutGluing_flat_of_isThickeningHom :
    let hatlas : HasThickeningAffineAtlases B S hS :=
      hasThickeningAffineAtlases_of_chartLift B S hS (hasEtaleChartLifts B S hS)
    letI := hasPushout_of_isThickening_of_isAffineHom B S hS hatlas i f hi hf
    (∀ T : pushoutGluingData B S hS i f,
      (IsLocallyOfFiniteType B S hS
          ((pushoutGluingFunctor B S hS hatlas i f hi hf).obj T).hom.hom ↔
        IsLocallyOfFiniteType B S hS T.obj.left.hom.hom ∧
          IsLocallyOfFiniteType B S hS T.obj.right.hom.hom) ∧
      (IsFlat B S hS ((pushoutGluingFunctor B S hS hatlas i f hi hf).obj T).hom.hom ↔
        IsFlat B S hS T.obj.left.hom.hom ∧ IsFlat B S hS T.obj.right.hom.hom) ∧
      ((IsFlat B S hS ((pushoutGluingFunctor B S hS hatlas i f hi hf).obj T).hom.hom ∧
          IsLocallyOfFinitePresentation B S hS
            ((pushoutGluingFunctor B S hS hatlas i f hi hf).obj T).hom.hom) ↔
        ((IsFlat B S hS T.obj.left.hom.hom ∧
            IsLocallyOfFinitePresentation B S hS T.obj.left.hom.hom) ∧
          (IsFlat B S hS T.obj.right.hom.hom ∧
            IsLocallyOfFinitePresentation B S hS T.obj.right.hom.hom))) ∧
      (IsSmooth B S hS ((pushoutGluingFunctor B S hS hatlas i f hi hf).obj T).hom.hom ↔
        IsSmooth B S hS T.obj.left.hom.hom ∧ IsSmooth B S hS T.obj.right.hom.hom) ∧
      (IsEtale B S hS ((pushoutGluingFunctor B S hS hatlas i f hi hf).obj T).hom.hom ↔
        IsEtale B S hS T.obj.left.hom.hom ∧ IsEtale B S hS T.obj.right.hom.hom)) ∧
    (∀ Z : Over (pushout i f), IsFlat B S hS Z.hom.hom →
      IsIso ((pushoutGluingAdjunction B S hS hatlas i f hi hf).counit.app Z)) ∧
    IsIso (pushoutGluingAdjunction B S hS hatlas i f hi hf).unit ∧
    (∀ Z : Over (pushout i f), IsFlat B S hS Z.hom.hom →
      IsFlat B S hS ((pushoutBaseChangeFunctor B S hS hatlas i f hi hf).obj Z).obj.left.hom.hom ∧
        IsFlat B S hS
          ((pushoutBaseChangeFunctor B S hS hatlas i f hi hf).obj Z).obj.right.hom.hom) ∧
    (∀ T : pushoutGluingData B S hS i f,
      IsFlat B S hS T.obj.left.hom.hom → IsFlat B S hS T.obj.right.hom.hom →
        IsFlat B S hS ((pushoutGluingFunctor B S hS hatlas i f hi hf).obj T).hom.hom)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 81.6, Tag 07SW](https://stacks.math.columbia.edu/tag/07SW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
