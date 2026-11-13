---
declaration: section
origin: cited
lean: MorphismOfTopoi.over, MorphismOfTopoi.inverseImageCompToOverIso, MorphismOfTopoi.toOverCompPushforwardIso, CategoryTheory.SliceTopos.underlyingIso_hom_app_comp_hom, MorphismOfTopoi.sheafRelocalize, MorphismOfTopoi.sheafRelocalize_eq_comp, MorphismOfTopoi.sheafRelocalize_inverseImage_obj, MorphismOfTopoi.sheafRelocalizeInverseImageIso
statement: formalized
proof: formalized
---

# 7.31 Localization and morphisms of topoi

Section 7.31 of the Stacks Project, [Tag 04IT](https://stacks.math.columbia.edu/tag/04IT). 4 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04H1, a lemma

[Tag 04H1](https://stacks.math.columbia.edu/tag/04H1) in the Stacks Project.

**`MorphismOfTopoi.over`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/OverPushforward.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SliceTopos/OverPushforward.lean#L61). The attribute's comment: “the morphism f' and the description of (f')⁻¹”. References: SGA 4 V (5.1).

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

**`MorphismOfTopoi.inverseImageCompToOverIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/OverPushforward.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SliceTopos/OverPushforward.lean#L75). The attribute's comment: “commutativity of the square, on inverse images”.

> **Stacks 04H1**, commutativity of the square on inverse images: `j_F⁻¹ ∘ f⁻¹ = (f')⁻¹ ∘ j_G⁻¹`,
> where `j_G⁻¹ = toOver G` and `j_F⁻¹ = toOver (f⁻¹G)`.  Concretely, `f⁻¹` carries the product
> `H ⊗ G` over `G` to the product `f⁻¹H ⊗ f⁻¹G` over `f⁻¹G`; this is where the left exactness of
> `f⁻¹` enters.

```lean
noncomputable def inverseImageCompToOverIso :
    f.inverseImage ⋙ toOver (f.inverseImage.obj G) ≅ toOver G ⋙ (f.over G).inverseImage
```

**`MorphismOfTopoi.toOverCompPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/OverPushforward.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SliceTopos/OverPushforward.lean#L91). The attribute's comment: “f'\_* j\_F^\{-1} = j\_G^\{-1} f\_*”.

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

**`CategoryTheory.SliceTopos.underlyingIso_hom_app_comp_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/LocalizationAndMorphismsOfTopoi.lean, line 435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SliceTopos/LocalizationAndMorphismsOfTopoi.lean#L435).

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

**`MorphismOfTopoi.sheafRelocalize`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/RelocalizationSheafTopoi.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SliceTopos/RelocalizationSheafTopoi.lean#L166). The attribute's comment: “the morphism of topoi f\_s : Sh(C)/F ⟶ Sh(D)/G”.

> **Stacks 04IV**, the morphism of topoi `f_s`.  Let `f : Sh(C) ⟶ Sh(D)` be a morphism of
> topoi, `G` a sheaf on `D`, `F` a sheaf on `C` and `s : F ⟶ f⁻¹G`.  The morphism of topoi
> `f_s : Sh(C)/F ⟶ Sh(D)/G` is
> ```
>   f_s = f' ∘ j_{F/f⁻¹G} ,
> ```
> the composite of the relocalization morphism `j_{F/f⁻¹G}` (Stacks 04IR,
> `sheafOverRelocalization s`) with the morphism `f'` of Stacks 04H1 (`f.over G`).  Both
> pushforwards are constructed: that of `f'` from `f_*`, that of `j_{F/f⁻¹G}` as the right adjoint
> of base change along `s`.

```lean
noncomputable def sheafRelocalize {G : Sheaf K (Type u')} {F : Sheaf J (Type u)}
    (s : F ⟶ f.inverseImage.obj G) : MorphismOfTopoi (Over F) (Over G)
```

**`MorphismOfTopoi.sheafRelocalize_eq_comp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/RelocalizationSheafTopoi.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SliceTopos/RelocalizationSheafTopoi.lean#L174). The attribute's comment: “the factorization f\_s = f' ∘ j\_\{F/f⁻¹G}”.

> **Stacks 04IV**, the factorization `f_s = f' ∘ j_{F/f⁻¹G}`, where `f' = f.over G` is the
> morphism of Stacks 04H1 and `j_{F/f⁻¹G} = sheafOverRelocalization s` is the relocalization
> morphism of Stacks 04IR.

```lean
lemma sheafRelocalize_eq_comp {G : Sheaf K (Type u')} {F : Sheaf J (Type u)}
    (s : F ⟶ f.inverseImage.obj G) :
    f.sheafRelocalize s = (f.over G).comp (sheafOverRelocalization s)
```

**`MorphismOfTopoi.sheafRelocalize_inverseImage_obj`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/RelocalizationSheafTopoi.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SliceTopos/RelocalizationSheafTopoi.lean#L184). The attribute's comment: “the description of (f\_s)⁻¹ as a fibre product”.

> **Stacks 04IV**, the description of `(f_s)⁻¹`: an object `φ : H ⟶ G` of `Sh(D)/G` is sent to
> ```
>   (f⁻¹H ×_{f⁻¹φ, f⁻¹G, s} F ⟶ F) .
> ```

```lean
lemma sheafRelocalize_inverseImage_obj {G : Sheaf K (Type u')} {F : Sheaf J (Type u)}
    (s : F ⟶ f.inverseImage.obj G) (H : Over G) :
    (f.sheafRelocalize s).inverseImage.obj H =
      Over.mk (pullback.snd (f.inverseImage.map H.hom) s)
```

**`MorphismOfTopoi.sheafRelocalizeInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/RelocalizationSheafTopoi.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SliceTopos/RelocalizationSheafTopoi.lean#L193). The attribute's comment: “commutativity of the square j\_G ∘ f\_s = f ∘ j\_F, on inverse images”.

> **Stacks 04IV**, commutativity of the first square `j_G ∘ f_s = f ∘ j_F`, on inverse images:
> `j_F⁻¹ ∘ f⁻¹ ≅ (f_s)⁻¹ ∘ j_G⁻¹`, where `j_F⁻¹ = toOver F` and `j_G⁻¹ = toOver G`.

```lean
noncomputable def sheafRelocalizeInverseImageIso {G : Sheaf K (Type u')}
    {F : Sheaf J (Type u)} (s : F ⟶ f.inverseImage.obj G) :
    f.inverseImage ⋙ toOver F ≅ toOver G ⋙ (f.sheafRelocalize s).inverseImage
```

**`MorphismOfTopoi.sheafRelocalizeCompPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/RelocalizationSheafTopoi.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SliceTopos/RelocalizationSheafTopoi.lean#L208). The attribute's comment: “commutativity of the last square j\_\{G'/G} ∘ f\_\{s'} = f\_s ∘ j\_\{F'/F}”.

> **Stacks 04IV**, commutativity of the last square: given `b : G' ⟶ G`, `a : F' ⟶ F` and
> `s' : F' ⟶ f⁻¹G'` with `s ∘ a = f⁻¹b ∘ s'`, the square of topoi
> ```
>   Sh(C)/F' --j_{F'/F}--> Sh(C)/F
>      |f_{s'}                |f_s
>   Sh(D)/G' --j_{G'/G}--> Sh(D)/G
> ```
> commutes: the inverse images of `j_{G'/G} ∘ f_{s'}` and of `f_s ∘ j_{F'/F}` are isomorphic.
> This is the formal identity `f⁻¹H ×_{f⁻¹G} F ×_F F' = f⁻¹(H ×_G G') ×_{f⁻¹G'} F'`.

```lean
noncomputable def sheafRelocalizeCompPullbackIso {G G' : Sheaf K (Type u')} (b : G' ⟶ G)
    {F F' : Sheaf J (Type u)} (a : F' ⟶ F) (s : F ⟶ f.inverseImage.obj G)
    (s' : F' ⟶ f.inverseImage.obj G') (hs : a ≫ s = s' ≫ f.inverseImage.map b) :
    ((sheafOverRelocalization b).comp (f.sheafRelocalize s')).inverseImage ≅
      ((f.sheafRelocalize s).comp (sheafOverRelocalization a)).inverseImage
```

## Tag 04IW, a lemma

[Tag 04IW](https://stacks.math.columbia.edu/tag/04IW) in the Stacks Project.

**`CategoryTheory.SliceTopos.isPullback_sheafFunctorToOver_overMap_overPost_of_isMorphismOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/LocalizationAndMorphismsOfTopoi.lean, line 808](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SliceTopos/LocalizationAndMorphismsOfTopoi.lean#L808).

> **Stacks 04IW.**  Let `u : C ⥤ D` be a continuous functor between sites defining a morphism of
> sites (`hu`), with induced morphism of topoi `f : Sh(D) ⟶ Sh(C)`, let `V` be an object of `C`, `U`
> an object of `D` and `c : U ⟶ u V`.  Localizing the morphism of sites at `c` (Stacks 04IN) gives
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
>
> The hypotheses are exactly the source's: `u` continuous and `hu : u.IsMorphismOfSites J K`; no
> finite limits in `C` and no exactness of `u` are assumed.  `hu` is used through Stacks 04IU, whose
> statement involves the morphism of topoi `f` it defines.

```lean
public theorem isPullback_sheafFunctorToOver_overMap_overPost_of_isMorphismOfSites
    {C : Type u} [SmallCategory C] {D : Type u} [SmallCategory D] {J : GrothendieckTopology C}
    {K : GrothendieckTopology D} {u : C ⥤ D} [u.IsContinuous J K]
    (hu : u.IsMorphismOfSites J K) (V : C) {U : D} (c : U ⟶ u.obj V)
    (H : Sheaf (J.over V) (Type u)) :
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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
