---
declaration: section
origin: cited
lean: gInv_isEquivalence, gStar_isEquivalence, IsSpecialCocontinuous, CategoryTheory.Sites.LocalizedToposSquare.isSpecialCocontinuous_overPost_and_isEquivalence, CategoryTheory.GrothendieckTopology.exists_isDenseSubsite_subcanonical, CategoryTheory.GrothendieckTopology.exists_isDenseSubsite_subcanonical_hasFiniteLimits_representable, MorphismOfTopoi.exists_isDenseSubsite_isMorphismOfSites_pushforward_iso, MorphismOfTopoi.exists_twoSided_isDenseSubsite_representablyFlat
statement: formalized
proof: formalized
---

# 7.29 Morphisms of topoi

Section 7.29 of the Stacks Project, [Tag 039Z](https://stacks.math.columbia.edu/tag/039Z). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03A0, a lemma

[Tag 03A0](https://stacks.math.columbia.edu/tag/03A0) in the Stacks Project.

**`gInv_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/ToposMorphismDefs.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/ToposMorphismDefs.lean#L223).

> **Stacks 03A0**, the pullback half. Let `C`, `D` be sites and `u : C ⥤ D` a functor such
> that
>
> 1. `u` is cocontinuous;
> 2. `u` is continuous, in the form `CoverPreserving J K u`;
> 3. given `a, b : U' ⟶ U` in `C` with `u a = u b`, there is a covering of `U'` in `C` along
>    which `a` and `b` agree;
> 4. given `c : u U' ⟶ u U` in `D`, there is a covering `{f i : U' i ⟶ U'}` in `C` and
>    morphisms `c i : U' i ⟶ U` with `u (c i) = u (f i) ≫ c`;
> 5. every object of `D` admits a covering by objects `u U i`.
>
> Then the morphism of topoi `g : Sh(C) ⟶ Sh(D)` attached to the cocontinuous functor `u` by
> Stacks 00XO is an equivalence: its pullback `g^{-1}` is an equivalence of categories. See
> `gStar_isEquivalence` for the direct image, and `gEquivalence` for the two packaged as an
> equivalence `Sh(D) ≌ Sh(C)`.

```lean
theorem gInv_isEquivalence : (gInv C D J K u).IsEquivalence
```

**`gStar_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/ToposMorphismDefs.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/ToposMorphismDefs.lean#L232).

> **Stacks 03A0**, the direct-image half. In the situation of `gInv_isEquivalence`, the
> direct image `g_*` of the morphism of topoi of Stacks 00XO is an equivalence of categories as
> well; together with `gInv_isEquivalence` this says that the morphism of topoi `g` is an
> equivalence.

```lean
theorem gStar_isEquivalence : (gStar C D J K u).IsEquivalence
```

## Tag 03CG, a definition

[Tag 03CG](https://stacks.math.columbia.edu/tag/03CG) in the Stacks Project.

**`IsSpecialCocontinuous`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/ToposMorphismComp.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/ToposMorphismComp.lean#L28).

> A functor `u : C ⥤ D` from a site `(C, J)` to a site `(D, K)` is a *special cocontinuous
> functor* if it is cocontinuous and makes `(C, J)` a dense subsite of `(D, K)`.

```lean
def IsSpecialCocontinuous {C : Type*} [Category C] {D : Type*} [Category D]
    (J : GrothendieckTopology C) (K : GrothendieckTopology D)
    (u : C ⥤ D) : Prop
```

## Tag 03CH, a lemma

[Tag 03CH](https://stacks.math.columbia.edu/tag/03CH) in the Stacks Project.

**`CategoryTheory.Sites.LocalizedToposSquare.isSpecialCocontinuous_overPost_and_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/LocalizedToposSquare.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/LocalizedToposSquare.lean#L116).

> **Stacks 03CH.** Let `u : C ⥤ D` be a special cocontinuous functor between sites, which
> is the instance `[u.IsDenseSubsite J K]` (equivalently `IsSpecialCocontinuous J K u`, by
> `isSpecialCocontinuous_iff_isDenseSubsite`), and let `U` be an object of `C`.  Then
>
> 1. the square of sites `j_{u(U)} ∘ u' = u ∘ j_U` commutes, where `j_U = Over.forget U`,
>    `j_{u(U)} = Over.forget (u.obj U)` and `u' = Over.post u : C/U ⥤ D/u(U)`;
> 2. the left vertical arrow `u'` is a special cocontinuous functor;
> 3. the square of topoi `Sh(C/U) → Sh(C) → Sh(D)`, `Sh(C/U) → Sh(D/u(U)) → Sh(D)` commutes,
>    formed with the morphisms of topoi of Stacks 00XO attached to the four cocontinuous
>    functors: the composite inverse images are isomorphic and so are the composite direct
>    images;
> 4. the vertical morphisms of topoi, attached to `u` and to `u'`, are equivalences: both their
>    inverse images and their direct images are equivalences of categories.
>
> Sites are small categories and topoi are categories of sheaves of sets in the same universe,
> as in the source.

```lean
theorem isSpecialCocontinuous_overPost_and_isEquivalence :
    Over.post (X := U) u ⋙ Over.forget (u.obj U) = Over.forget U ⋙ u ∧
      IsSpecialCocontinuous (J.over U) (K.over (u.obj U)) (Over.post (X := U) u) ∧
      Nonempty (gInv C D J K u ⋙ gInv (Over U) C (J.over U) J (Over.forget U) ≅
        gInv (Over (u.obj U)) D (K.over (u.obj U)) K (Over.forget (u.obj U)) ⋙
          gInv (Over U) (Over (u.obj U)) (J.over U) (K.over (u.obj U))
            (Over.post (X := U) u)) ∧
      Nonempty (gStar (Over U) C (J.over U) J (Over.forget U) ⋙ gStar C D J K u ≅
        gStar (Over U) (Over (u.obj U)) (J.over U) (K.over (u.obj U))
            (Over.post (X := U) u) ⋙
          gStar (Over (u.obj U)) D (K.over (u.obj U)) K (Over.forget (u.obj U))) ∧
      (gInv C D J K u).IsEquivalence ∧ (gStar C D J K u).IsEquivalence ∧
      (gInv (Over U) (Over (u.obj U)) (J.over U) (K.over (u.obj U))
        (Over.post (X := U) u)).IsEquivalence ∧
      (gStar (Over U) (Over (u.obj U)) (J.over U) (K.over (u.obj U))
        (Over.post (X := U) u)).IsEquivalence
```

## Tag 03A1, a lemma

[Tag 03A1](https://stacks.math.columbia.edu/tag/03A1) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.exists_isDenseSubsite_subcanonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/MorphismsOfTopoi.lean, line 766](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/MorphismsOfTopoi.lean#L766). The attribute's comment: “A full subcategory of `Sh(C)` with a set of objects which contains the sheafified representables and is closed under fibre products is a site, for the coverings whose coproduct is a surjection of sheaves; that site is subcanonical, `U ↦ h_U^#` is a special cocontinuous functor, and the induced equivalence of topoi matches the representables of the two sides. This is all five conclusions, with (5) stated for every object of the subcategory.”.

> Let `(C, J)` be a site and let `ι : C' ⥤ Sh(C)` be a full subcategory of the
> category of sheaves of sets on `C`, with a set of objects, which is closed under fibre products
> and contains the sheafified representables: `v : C ⥤ C'` is a functor with `v ⋙ ι ≅ h_{-}^#`.
> Declare a covering of `C'` to be a family `{F_i ⟶ F}` of morphisms with `∐ F_i ⟶ F` a surjection
> of sheaves. Then
>
> 1. these coverings are the coverings of a Grothendieck topology `K` on `C'`, i.e. `C'` is a site;
> 2. `K` is subcanonical, i.e. representable presheaves on `C'` are sheaves;
> 3. `v` is a special cocontinuous functor, i.e. `v.IsDenseSubsite J K`, hence the induced morphism
>    of topoi `g : Sh(C) ⟶ Sh(C')` is an equivalence;
> 4. `g⁻¹ h_F = F` for every object `F` of `C'`; and
> 5. `g_* F = h_F` for every object `F` of `C'`; along `v` this is
>    `g_* h_U^# = h_{v U} = h_{h_U^#}`.

```lean
public theorem exists_isDenseSubsite_subcanonical {C : Type u} [Category.{v} C]
    (J : GrothendieckTopology C) {D : Type max u v} [SmallCategory D]
    (ι : D ⥤ Sheaf J (Type max u v)) [ι.Full] [ι.Faithful] [HasPullbacks D]
    [PreservesLimitsOfShape WalkingCospan ι] (v : C ⥤ D) (e : v ⋙ ι ≅ Sheaf.sheafifiedYoneda J) :
    ∃ K : GrothendieckTopology D,
      (∀ {X : D} {α : Type max u v} (Y : α → D) (p : ∀ a, Y a ⟶ X) {c : Cofan fun a ↦ ι.obj (Y a)}
          (hc : IsColimit c),
          Sieve.ofArrows Y p ∈ K X ↔ Epi (Cofan.IsColimit.desc hc fun a ↦ ι.map (p a))) ∧
        ∃ (_ : K.Subcanonical) (_ : v.IsDenseSubsite J K),
          Nonempty (K.yoneda ⋙ v.sheafPushforwardContinuous (Type max u v) J K ≅ ι) ∧
            Nonempty (ι ⋙ v.sheafPushforwardCocontinuous (Type max u v) J K ≅ K.yoneda)
```

## Tag 03CI, a lemma

[Tag 03CI](https://stacks.math.columbia.edu/tag/03CI) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.exists_isDenseSubsite_subcanonical_hasFiniteLimits_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/MorphismsOfTopoi.lean, line 1432](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/MorphismsOfTopoi.lean#L1432). The attribute's comment: “Any topos is equivalent, by a special cocontinuous functor, to the topos of sheaves on a site which is subcanonical, has all finite limits, has all subsheaves of representables representable, and on which a prescribed set of sheaves becomes representable. This is conclusions (1), (3), (4) and (5); conclusion (2) holds for every topology and is `ofArrows_mem_iff_isLocallySurjective_sigmaDesc_uliftYoneda_map`. The functor is also recorded to preserve all finite limits that exist in the given site.”. References: SGA 4 IV (1.2), “i) => i')”.

> Let `(C, J)` be a site and let `F : ι → Sheaf J (Type max u v)` be a set of
> sheaves of sets on `C`. Then there is a site `(D, K)` and a special cocontinuous functor
> `G : C ⥤ D` (Stacks 03CG: a functor exhibiting `(C, J)` as a dense subsite of `(D, K)`), so
> that the induced morphism of topoi `g : Sh(C) → Sh(D)` is an equivalence, such that
>
> 1. `K` is subcanonical;
> 3. `D` has all finite limits, i.e. fibre products and a final object;
> 4. every subsheaf of a representable sheaf on `D` is representable; and
> 5. each `g_* (F i) = (G.sheafPushforwardCocontinuous _ J K).obj (F i)` is representable;
>
> moreover `G` preserves all finite limits that exist in `C`.

```lean
public theorem exists_isDenseSubsite_subcanonical_hasFiniteLimits_representable {C : Type u}
    [Category.{v} C] (J : GrothendieckTopology C) {ι : Type max u v}
    (F : ι → Sheaf J (Type max u v)) :
    ∃ (D : Type max u v) (_ : SmallCategory D) (K : GrothendieckTopology D) (G : C ⥤ D) (_ :
      G.IsDenseSubsite J K) (_ : K.Subcanonical) (_ : HasFiniteLimits D)
      (_ : PreservesFiniteLimits G),
      (∀ (V : D) (ℱ : Sheaf K (Type max u v)) (i : ℱ ⟶ K.yoneda.obj V),
          Mono i → ℱ.obj.IsRepresentable) ∧
        (∀ i,
          ((G.sheafPushforwardCocontinuous (Type max u v) J K).obj
              (F i)).obj.IsRepresentable)
```

## Tag 03A2, a lemma

[Tag 03A2](https://stacks.math.columbia.edu/tag/03A2) in the Stacks Project.

**`MorphismOfTopoi.exists_isDenseSubsite_isMorphismOfSites_pushforward_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/MorphismsOfTopoi.lean, line 1081](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/MorphismsOfTopoi.lean#L1081). The attribute's comment: “Every morphism of topoi is the composition of the equivalence induced by a special cocontinuous functor with the morphism of topoi induced by a morphism of sites. The conclusion also records, from Stacks 03CJ, that `u` preserves the final object.”.

> Let `(C, J)` and `(D, K)` be sites and let `f : Sh(C) → Sh(D)` be a morphism
> of topoi. Then there are a site `(C', J')` and functors `v : C ⥤ C'` and `u : D ⥤ C'` such that
>
> 1. `v` is a special cocontinuous functor, i.e. exhibits `(C, J)` as a dense subsite of
>    `(C', J')`, so that the morphism of topoi `g : Sh(C) → Sh(C')` it induces is an equivalence;
> 2. `u` commutes with fibre products *and with the final object*, is continuous, and defines a
>    morphism of sites `C' → D`, hence a morphism of topoi `h : Sh(C') → Sh(D)`; and
> 3. `f` agrees with `h ∘ g`, in the sense that `f_*` is isomorphic to the composition of the
>    pushforwards `g_* = v.sheafPushforwardCocontinuous` and `h_* = u.sheafPushforwardContinuous`.

```lean
public theorem exists_isDenseSubsite_isMorphismOfSites_pushforward_iso {C : Type u₁}
    [Category.{v₁} C] {D : Type u₁} [Category.{v₁} D] {J : GrothendieckTopology C}
    {K : GrothendieckTopology D}
    (f : MorphismOfTopoi (Sheaf J (Type max u₁ v₁)) (Sheaf K (Type max u₁ v₁))) :
    ∃ (C' : Type max u₁ v₁) (_ : SmallCategory C') (J' : GrothendieckTopology C') (v : C ⥤ C') (u :
      D ⥤ C') (_ : v.IsDenseSubsite J J') (_ : _root_.IsMorphismOfSites.{max u₁ v₁} u K J'),
      PreservesLimitsOfShape WalkingCospan u ∧
        PreservesLimitsOfShape (Discrete PEmpty.{1}) u ∧
          Nonempty
            (f.pushforward ≅
              v.sheafPushforwardCocontinuous (Type max u₁ v₁) J J' ⋙
                u.sheafPushforwardContinuous (Type max u₁ v₁) K J')
```

## Tag 03CJ, a remark

[Tag 03CJ](https://stacks.math.columbia.edu/tag/03CJ) in the Stacks Project.

**`MorphismOfTopoi.exists_twoSided_isDenseSubsite_representablyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/ToposReplacement.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/ToposReplacement.lean#L251). The attribute's comment: “Any morphism of topoi fits into a commutative square with two equivalences given by special cocontinuous functors and a morphism of topoi coming from a functor `u : D' ⥤ C'` to which Stacks 00X6 applies, with both `C'` and `D'` having all finite limits and subcanonical topologies, and with prescribed families of sheaves on `C` and on `D` becoming representable on `C'` and on `D'`.”.

> Let `(C, J)` and `(D, K)` be sites and let `f : Sh(C) → Sh(D)` be a morphism of topoi. Then
> there are sites `(C', J')` and `(D', K')`, special cocontinuous functors `v : C ⥤ C'` and
> `w : D ⥤ D'`, and a functor `u : D' ⥤ C'` such that
>
> 1. `v` and `w` exhibit `(C, J)` and `(D, K)` as dense subsites, so the morphisms of topoi
>    `g : Sh(C) → Sh(C')` and `e : Sh(D) → Sh(D')` they induce are equivalences (Stacks 03A0);
> 2. `J'` and `K'` are subcanonical and `C'` and `D'` have all finite limits;
> 3. `u` is continuous, preserves all finite limits, is representably flat and defines a morphism
>    of sites `C' → D'` — in other words Stacks 00X6 applies to `u`;
> 4. each `g_*(F i)` is a representable sheaf on `C'` and each `e_*(G j)` is a representable sheaf
>    on `D'`, for prescribed families of sheaves `F` on `C` and `G` on `D`; and
> 5. the square commutes: `f_* ⋙ e_*` is isomorphic to `g_* ⋙ h_*`, where `h : Sh(C') → Sh(D')`
>    is the morphism of topoi attached to the morphism of sites `u`.
>
> Conclusions (1)-(4) are the source's conclusions (1)-(4) and (5) is the commutativity of the
> square the source's remark is about.

```lean
theorem exists_twoSided_isDenseSubsite_representablyFlat {C : Type u} [SmallCategory C]
    {D : Type u} [SmallCategory D] {J : GrothendieckTopology C} {K : GrothendieckTopology D}
    (f : MorphismOfTopoi (Sheaf J (Type u)) (Sheaf K (Type u))) {ι : Type u}
    (F : ι → Sheaf J (Type u)) {κ : Type u} (G : κ → Sheaf K (Type u)) :
    ∃ (C' : Type u) (_ : SmallCategory C') (J' : GrothendieckTopology C') (D' : Type u)
      (_ : SmallCategory D') (K' : GrothendieckTopology D') (v : C ⥤ C') (w : D ⥤ D')
      (u : D' ⥤ C') (_ : v.IsDenseSubsite J J') (_ : w.IsDenseSubsite K K')
      (_ : HasFiniteLimits C') (_ : HasFiniteLimits D') (_ : J'.Subcanonical)
      (_ : K'.Subcanonical) (_ : u.IsContinuous K' J') (_ : PreservesFiniteLimits u)
      (_ : RepresentablyFlat u) (_ : u.IsMorphismOfSites K' J'),
      (∀ i, ((v.sheafPushforwardCocontinuous (Type u) J J').obj (F i)).obj.IsRepresentable) ∧
      (∀ j, ((w.sheafPushforwardCocontinuous (Type u) K K').obj (G j)).obj.IsRepresentable) ∧
      Nonempty
        (f.pushforward ⋙ w.sheafPushforwardCocontinuous (Type u) K K' ≅
          v.sheafPushforwardCocontinuous (Type u) J J' ⋙
            u.sheafPushforwardContinuous (Type u) K' J')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.29, Tag 039Z](https://stacks.math.columbia.edu/tag/039Z)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
