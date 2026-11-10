---
declaration: section
origin: cited
lean: MorphismOfTopoi.over, MorphismOfTopoi.inverseImageCompToOverIso, MorphismOfTopoi.toOverCompPushforwardIso, CategoryTheory.SliceTopos.underlyingIso_hom_app_comp_hom, relocalizeMorphismTopoiPullbackIso, CategoryTheory.SliceTopos.isPullback_sheafFunctorToOver_overMap_overPost
statement: formalized
proof: formalized
---

# 7.31 Localization and morphisms of topoi

Section 7.31 of the Stacks Project, [Tag 04IT](https://stacks.math.columbia.edu/tag/04IT). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04H1, a lemma

[Tag 04H1](https://stacks.math.columbia.edu/tag/04H1) in the Stacks Project.

**`MorphismOfTopoi.over`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/OverPushforward.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SliceTopos/OverPushforward.lean#L61). The attribute's comment: “the morphism f' and the description of (f')⁻¹”. References: SGA 4 V (5.1).

> **Stacks 04H1.** Let `f : E ⟶ D` be a morphism of topoi and `G` an object of `D`.  Localizing
> `E` at `F = f⁻¹G` and `D` at `G` gives a morphism of topoi `f' : E/F ⟶ D/G` whose inverse image
> is `Over.post f⁻¹`, i.e.
> ```
> (f')⁻¹(H ⟶ G) = (f⁻¹H ⟶ f⁻¹G) ,
> ```
> which is the property characterizing `f'`.  Its pushforward is
> `(K ⟶ F) ↦ (f_*K ×_{f_*f⁻¹G} G ⟶ G)`, the right adjoint supplied by
> `CategoryTheory.Over.postAdjunctionLeft`, and its inverse image is left exact because `f⁻¹` is.

```lean
noncomputable def over : MorphismOfTopoi (Over (f.inverseImage.obj G)) (Over G)
```

**`MorphismOfTopoi.inverseImageCompToOverIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/OverPushforward.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SliceTopos/OverPushforward.lean#L75). The attribute's comment: “commutativity of the square, on inverse images”.

> **Stacks 04H1**, commutativity of the square on inverse images: `j_F⁻¹ ∘ f⁻¹ = (f')⁻¹ ∘ j_G⁻¹`,
> where `j_G⁻¹ = toOver G` and `j_F⁻¹ = toOver (f⁻¹G)`.  Concretely, `f⁻¹` carries the product
> `H ⊗ G` over `G` to the product `f⁻¹H ⊗ f⁻¹G` over `f⁻¹G`; this is where the left exactness of
> `f⁻¹` enters.

```lean
noncomputable def inverseImageCompToOverIso :
    f.inverseImage ⋙ toOver (f.inverseImage.obj G) ≅ toOver G ⋙ (f.over G).inverseImage
```

**`MorphismOfTopoi.toOverCompPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/OverPushforward.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SliceTopos/OverPushforward.lean#L91). The attribute's comment: “f'_* j_F^{-1} = j_G^{-1} f_*”.

> **Stacks 04H1**: `f'_* ∘ j_F⁻¹ = j_G⁻¹ ∘ f_*`.
>
> Both sides are right adjoints — of `(f')⁻¹ ⋙ j_{F!}` and of `j_{G!} ⋙ f⁻¹` respectively — and
> those two left adjoints are equal on the nose by `Over.post_forget_eq_forget_comp`, so the
> identity follows from uniqueness of right adjoints.

```lean
noncomputable def toOverCompPushforwardIso :
    toOver (f.inverseImage.obj G) ⋙ (f.over G).pushforward ≅ f.pushforward ⋙ toOver G
```

## Tag 04IU, a lemma

[Tag 04IU](https://stacks.math.columbia.edu/tag/04IU) in the Stacks Project.

**`CategoryTheory.SliceTopos.underlyingIso_hom_app_comp_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/LocalizationAndMorphismsOfTopoi.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SliceTopos/LocalizationAndMorphismsOfTopoi.lean#L435).

> **Stacks 04IU.**  Let `u : C ⥤ D` be a continuous functor between sites defining a morphism of
> sites, with induced morphism of topoi `f : Sh(D) ⟶ Sh(C)`, let `V` be an object of `C` and put
> `U = u V`.  Localizing the morphism of sites at `V` (Stacks 03CF) gives
> `f' : Sh(D/U) ⟶ Sh(C/V)` with `(f')⁻¹ = u'_s` for `u' = Over.post u`; localizing the morphism of
> topoi at the sheaf `h_V^#` (Stacks 04H1) gives `f'' : Sh(D)/f⁻¹h_V^# ⟶ Sh(C)/h_V^#` with
> `(f'')⁻¹ = Over.post f⁻¹`.  Through the equivalences `Φ_V, Φ_U` of Stacks 00Y1 and the
> identification `f⁻¹h_V^# ≅ h_U^#` of Stacks 04D3 the two agree:
> ```
>   (f')⁻¹ ⋙ Φ_U  ≅  Φ_V ⋙ (f'')⁻¹ ⋙ Over.map (04D3) .
> ```
> Both sides become `j_{U!}(f')⁻¹ ≅ f⁻¹j_{V!}` after `Over.forget h_U^#`, canonically and for free,
> by `underlyingIso`; the content of the lemma, stated here, is that that canonical isomorphism
> respects the structure maps to `h_U^#`, the one on the right being computed with Stacks 04D3's
> identification.  Feeding this equation to `Over.natIsoOfForgetIso` produces the displayed
> isomorphism of functors, hence the agreement of the diagram of Stacks 04H1 with the diagram of
> Stacks 03CF via the identifications `j_F = j_U`, `j_G = j_V` of Stacks 04IQ.

```lean
public theorem underlyingIso_hom_app_comp_hom {C : Type u} [SmallCategory C] {D : Type u}
    [SmallCategory D] {J : GrothendieckTopology C} {K : GrothendieckTopology D} {u : C ⥤ D}
    [u.IsContinuous J K]
    (hu : u.IsMorphismOfSites J K) (V : C) (H : Sheaf (J.over V) (Type u)) :
    (underlyingIso J K u V).hom.app H ≫
        ((sheafFunctorToOver (U := V) J ⋙
            (hu.morphismOfTopoi.over
                ((presheafToSheaf J (Type u)).obj (yoneda.obj V))).inverseImage ⋙
            Over.map (sheafPullbackSheafifyYonedaIso u J K V).hom).obj H).hom =
      (((Over.post (X := V) u).sheafPullback (Type u) (J.over V) (K.over (u.obj V)) ⋙
          sheafFunctorToOver (U := u.obj V) K).obj H).hom
```

## Tag 04IV, a lemma

[Tag 04IV](https://stacks.math.columbia.edu/tag/04IV) in the Stacks Project.

**`relocalizeMorphismTopoiPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/RelocalizationPullback.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SliceTopos/RelocalizationPullback.lean#L123).

> Let `F : D ⥤ C` be a functor preserving the pullback of `φ` and `b`.
> Given `φ : H ⟶ G`, `b : G' ⟶ G` in `D` and `a : Fbar' ⟶ Fbar`,
> `s : Fbar ⟶ F.obj G`, `s' : Fbar' ⟶ F.obj G'` in `C` satisfying
> `a ≫ s = s' ≫ F.map b`, there is a canonical isomorphism
> `(F.obj H ×_{F.obj G} Fbar) ×_{Fbar} Fbar'  ≅  F.obj (H ×_G G') ×_{F.obj G'} Fbar'`.
>
> This is the formal pullback identity at the end of the proof, with the
> topos-theoretic inverse image `f⁻¹` replaced by the generic
> pullback-preserving functor `F`.

```lean
noncomputable def relocalizeMorphismTopoiPullbackIso :
    pullback (pullback.snd (F.map φ) s) a ≅
      pullback (F.map (pullback.snd φ b)) s'
```

## Tag 04IW, a lemma

[Tag 04IW](https://stacks.math.columbia.edu/tag/04IW) in the Stacks Project.

**`CategoryTheory.SliceTopos.isPullback_sheafFunctorToOver_overMap_overPost`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/LocalizationAndMorphismsOfTopoi.lean, line 698](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SliceTopos/LocalizationAndMorphismsOfTopoi.lean#L698).

> **Stacks 04IW.**  Let `u : C ⥤ D` be a continuous functor between sites defining a morphism of
> sites, with induced morphism of topoi `f : Sh(D) ⟶ Sh(C)`, let `V` be an object of `C`, `U` an
> object of `D` and `c : U ⟶ u V`.  Localizing the morphism of sites at `c` (Stacks 04IN) gives
> `f_c : Sh(D/U) ⟶ Sh(C/V)` with `(f_c)⁻¹ = (Over.post u)_s ⋙ (Over.map c)^s`; localizing the
> morphism of topoi at `s : h_U^# ⟶ f⁻¹h_V^#`, the morphism induced by `c` (Stacks 04IV), gives
> `f_s : Sh(D)/h_U^# ⟶ Sh(C)/h_V^#`, characterised by
> `(f_s)⁻¹(H ⟶ h_V^#) = (f⁻¹H ×_{f⁻¹h_V^#, s} h_U^# ⟶ h_U^#)`.
>
> Through the equivalences `Φ_V, Φ_U` of Stacks 00Y1 — the identifications `j_G = j_V`, `j_F = j_U`
> of Stacks 04IQ — the two agree: for every sheaf `H` on `C/V` the square
> ```
>     Φ_U((f_c)⁻¹H) ---------> f⁻¹(j_{V!}H)
>         |                          |
>         |                          | f⁻¹(structure map)
>         v                          v
>       h_U^# ---------s---------> f⁻¹h_V^#
> ```
> is cartesian, the top edge being the canonical comparison map assembled from Stacks 04IL (1)
> (Stacks 04IS), which identifies `j_{U/u(V)}⁻¹ ⋙ Φ_U` with `Φ_{u(V)} ⋙ Over.pullback h_c^#`, and
> `underlyingIso` (Stacks 04IU, Stacks 03CF), which identifies `j_{u(V)!}(f')⁻¹H` with `f⁻¹j_{V!}H`.
> Equivalently: `Φ_U((f_c)⁻¹H) ≅ (f_s)⁻¹(Φ_V H)` in `Sh(D)/h_U^#`, i.e. the diagram of topoi of
> Stacks 04IN agrees with the diagram of topoi of Stacks 04IV.

```lean
public theorem isPullback_sheafFunctorToOver_overMap_overPost {C : Type u} [SmallCategory C]
    {D : Type u} [SmallCategory D] {J : GrothendieckTopology C} {K : GrothendieckTopology D}
    {u : C ⥤ D} [u.IsContinuous J K] [HasFiniteLimits C] [PreservesFiniteLimits u]
    (V : C) {U : D} (c : U ⟶ u.obj V) (H : Sheaf (J.over V) (Type u)) :
    IsPullback
      (((inverseImageCompSheafFunctorToOverIso c K).hom.app
            (((Over.post (X := V) u).sheafPullback (Type u) (J.over V)
              (K.over (u.obj V))).obj H)).left ≫
          pullback.fst
              ((sheafFunctorToOver (U := u.obj V) K).obj
                (((Over.post (X := V) u).sheafPullback (Type u) (J.over V)
                  (K.over (u.obj V))).obj H)).hom
              ((presheafToSheaf K (Type u)).map (yoneda.map c)) ≫
            (underlyingIso J K u V).hom.app H)
      (((sheafFunctorToOver (U := U) K).obj
        (((Over.map c).sheafPushforwardContinuous (Type u) (K.over U) (K.over (u.obj V))).obj
          (((Over.post (X := V) u).sheafPullback (Type u) (J.over V)
            (K.over (u.obj V))).obj H))).hom)
      ((u.sheafPullback (Type u) J K).map ((sheafFunctorToOver (U := V) J).obj H).hom)
      ((presheafToSheaf K (Type u)).map (yoneda.map c) ≫
        (sheafPullbackSheafifyYonedaIso u J K V).inv)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.31, Tag 04IT](https://stacks.math.columbia.edu/tag/04IT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
