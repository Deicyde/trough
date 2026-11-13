---
declaration: section
origin: cited
lean: CategoryTheory.OverShriek.isIso_ofRestricted_unit, StacksLocalizationProducts.bijective_left_comp_prodSnd, StacksLocalizationProducts.isMorphismOfSites_star, StacksLocalizationProducts.sheafPushforwardOverForgetIso, StacksLocalizationProducts.sheafPullbackStarIso, StacksLocalizationProducts.sheafPushforwardObjEquiv, StacksRelocalization.isMorphismOfSites_overPullback, StacksRelocalization.sheafPushforwardOverMapIso
statement: formalized
proof: formalized
---

# 7.27 More localization

Section 7.27 of the Stacks Project, [Tag 04IM](https://stacks.math.columbia.edu/tag/04IM). 5 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03HT, a lemma

[Tag 03HT](https://stacks.math.columbia.edu/tag/03HT) in the Stacks Project.

**`CategoryTheory.OverShriek.isIso_ofRestricted_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/MoreLocalization.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/MoreLocalization.lean#L205). The attribute's comment: “j\_\{U!}G(V) = ∐\_\{φ : V ⟶ U} G(V →φ U) for a subcanonical topology.”.

> Let `C` be a site, let `U` be an object of `C` whose representable presheaf `h_U` is a sheaf
> (for instance because the topology is subcanonical), and let `G` be a sheaf of sets on `C/U`. Let
> `L` be a left adjoint of the restriction functor `j_U^{-1} = J.overPullback : Sh(C) ⥤ Sh(C/U)`,
> i.e. let `L` be `j_{U!}`. Then the canonical map from the coproduct presheaf
> `V ↦ ∐_{φ : V ⟶ U} G(V →φ U)` to the presheaf underlying `j_{U!}G`, which over `V` sends a pair
> `(φ, s)` to the section `s` of `j_{U!}G`, is an isomorphism:
> `j_{U!}G(V) = ∐_{φ ∈ Hom_C(V, U)} G(V →φ U)`.

```lean
public theorem isIso_ofRestricted_unit {C : Type u} [Category.{v} C] (J : GrothendieckTopology C)
    (U : C) (hU : Presieve.IsSheaf J (yoneda.obj U))
    {L : Sheaf (J.over U) (Type v) ⥤ Sheaf J (Type v)} (adj : L ⊣ J.overPullback (Type v) U)
    (G : Sheaf (J.over U) (Type v)) :
    IsIso (ofRestricted G.obj (F := (L.obj G).obj) (adj.unit.app G).hom)
```

## Tag 03CE, a lemma

[Tag 03CE](https://stacks.math.columbia.edu/tag/03CE) in the Stacks Project.

**`StacksLocalizationProducts.bijective_left_comp_prodSnd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/PushforwardAdjunction.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/PushforwardAdjunction.lean#L122). References: SGA 3 I (1.6), “i\_S ⊣ p\_S hom bijection”.

> **Stacks 03CE(1).** The right adjoint of the localization functor
> `j_U = Over.forget U : C/U ⥤ C` is `v : X ↦ X × U / U`: for `Y/U` in `C/U` and `X` in `C` the
> map sending a morphism `Y ⟶ X × U / U` over `U` to its underlying morphism followed by the
> projection to `X` is a bijection `Mor_{C/U}(Y/U, X × U/U) ≃ Mor_C(Y, X)`.
>
> This is the counit description `Over.forgetAdjStar_counit_app` of Mathlib's adjunction
> `Over.forgetAdjStar U : Over.forget U ⊣ Over.star U`.

```lean
theorem bijective_left_comp_prodSnd (Y : Over U) (X : C) :
    Function.Bijective fun g : Y ⟶ (Over.star U).obj X => g.left ≫ prod.snd
```

**`StacksLocalizationProducts.isMorphismOfSites_star`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/PushforwardAdjunction.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/PushforwardAdjunction.lean#L138).

> **Stacks 03CE(2), first half.** The functor `v = Over.star U : C ⥤ C/U` defines a morphism of
> sites `C/U → C`: it is continuous, and the induced pullback on sheaves of sets is exact.
>
> Exactness holds because `v` is a right adjoint, hence representably flat, so this is the criterion
> `CategoryTheory.Functor.isMorphismOfSites_of_representablyFlat` (Stacks 00X5).

```lean
theorem isMorphismOfSites_star : (Over.star U).IsMorphismOfSites J (J.over U)
```

**`StacksLocalizationProducts.sheafPushforwardOverForgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/PushforwardAdjunction.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/PushforwardAdjunction.lean#L145).

> **Stacks 03CE(2), second half.** The pushforward `j_{U*}` of the morphism of topoi attached to
> the continuous and cocontinuous functor `j_U` agrees with the pushforward `v^s` of the morphism of
> sites given by `v = Over.star U`; that is, the two morphisms of topoi coincide.

```lean
noncomputable def sheafPushforwardOverForgetIso :
    (Over.forget U).sheafPushforwardCocontinuous (Type u) (J.over U) J ≅
      (Over.star U).sheafPushforwardContinuous (Type u) J (J.over U)
```

**`StacksLocalizationProducts.sheafPullbackStarIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/PushforwardAdjunction.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/PushforwardAdjunction.lean#L153).

> **Stacks 03CE(2), second half.** Dually, the pullback `v_s = f⁻¹` of the morphism of sites
> given by `v = Over.star U` is the restriction functor `j_U⁻¹` along `j_U = Over.forget U`.

```lean
noncomputable def sheafPullbackStarIso :
    (Over.star U).sheafPullback (Type u) J (J.over U) ≅
      (Over.forget U).sheafPushforwardContinuous (Type u) (J.over U) J
```

**`StacksLocalizationProducts.sheafPushforwardObjEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/PushforwardAdjunction.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/PushforwardAdjunction.lean#L161).

> **Stacks 03CE(3).** For a sheaf `F` on `C/U` the sections of `j_{U*}F` over an object `X` of
> `C` are the sections of `F` over `X × U / U`.

```lean
noncomputable def sheafPushforwardObjEquiv (F : Sheaf (J.over U) (Type u)) (X : C) :
    (((Over.forget U).sheafPushforwardCocontinuous (Type u) (J.over U) J).obj F).obj.obj (op X) ≃
      F.obj.obj (op ((Over.star U).obj X))
```

## Tag 09W9, a lemma

[Tag 09W9](https://stacks.math.columbia.edu/tag/09W9) in the Stacks Project.

**`StacksRelocalization.isMorphismOfSites_overPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/OverPullbackMorphism.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/OverPullbackMorphism.lean#L43). References: SGA 4 IV (5.5), “loc(f) (5.5.2)”.

> The functor `v = Over.pullback f : C/V ⥤ C/U`, given on objects by `X/V ↦ X ×_V U / U`,
> defines a morphism of sites `C/U → C/V`: it is continuous, and the induced pullback on sheaves of
> sets is exact.

```lean
theorem isMorphismOfSites_overPullback :
    (Over.pullback f).IsMorphismOfSites (J.over V) (J.over U)
```

**`StacksRelocalization.sheafPushforwardOverMapIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/OverPullbackMorphism.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/OverPullbackMorphism.lean#L51).

> The pushforward `j_*` of the morphism of topoi attached to the continuous and cocontinuous
> functor `j = Over.map f` agrees with the pushforward `v^s` of the morphism of sites given by
> `v = Over.pullback f`; that is, the two morphisms of topoi coincide.

```lean
noncomputable def sheafPushforwardOverMapIso :
    (Over.map f).sheafPushforwardCocontinuous (Type u) (J.over U) (J.over V) ≅
      (Over.pullback f).sheafPushforwardContinuous (Type u) (J.over V) (J.over U)
```

**`StacksRelocalization.sheafPullbackOverPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/OverPullbackMorphism.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/OverPullbackMorphism.lean#L59). References: SGA 4 IV (5.5), “f^* = restriction”.

> The pullback `v_s = f⁻¹` of the morphism of sites given by `v = Over.pullback f` is the
> restriction functor `j⁻¹` along `j = Over.map f`.

```lean
noncomputable def sheafPullbackOverPullbackIso :
    (Over.pullback f).sheafPullback (Type u) (J.over V) (J.over U) ≅
      (Over.map f).sheafPushforwardContinuous (Type u) (J.over U) (J.over V)
```

**`StacksRelocalization.sheafPushforwardObjEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/OverPullbackMorphism.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/OverPullbackMorphism.lean#L67). References: SGA 4 IV (5.5), “f\_* formula (5.5.3)”.

> For a sheaf `F` on `C/U` the sections of `j_*F` over an object `X/V` of `C/V` are the sections
> of `F` over `X ×_V U / U`.

```lean
noncomputable def sheafPushforwardObjEquiv (F : Sheaf (J.over U) (Type u)) (X : Over V) :
    (((Over.map f).sheafPushforwardCocontinuous (Type u) (J.over U) (J.over V)).obj F).obj.obj
        (op X) ≃
      F.obj.obj (op ((Over.pullback f).obj X))
```

## Tag 00Y2, a lemma

[Tag 00Y2](https://stacks.math.columbia.edu/tag/00Y2) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.isIso_unit_and_sheafAdjunctionCocontinuous_counit_of_isSubterminal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/MoreLocalization.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/MoreLocalization.lean#L91). The attribute's comment: “if every object of `C` has at most one morphism to `U`, the canonical maps `F ⟶ j_U^{-1}j_{U!}F` and `j_U^{-1}j_{U*}F ⟶ F` are isomorphisms, for coefficients in an arbitrary category `A`”. References: SGA 4 VIII (5.7), “open immersion case”; SGA 4 I (5.6), “special case”.

> Let `C` be a site, and let `U` be an object of `C` such that every object of `C` has at most
> one morphism to `U`, i.e. `U` is subterminal. Let `L` be a left adjoint of
> `j_U^{-1} = J.overPullback A U : Sh(C) ⥤ Sh(C/U)`, i.e. let `L` be `j_{U!}`, and let
> `j_{U*} = {}_pj_U` be the pushforward along the cocontinuous localization functor. Then the
> canonical maps `F ⟶ j_U^{-1}j_{U!}F` and `j_U^{-1}j_{U*}F ⟶ F` are isomorphisms for every sheaf
> `F` on `C/U`: they are the unit of `j_{U!} ⊣ j_U^{-1}` and the counit of `j_U^{-1} ⊣ j_{U*}`.
> Equivalently, `j_{U!}` and `j_{U*}` are fully faithful.

```lean
public theorem isIso_unit_and_sheafAdjunctionCocontinuous_counit_of_isSubterminal {C : Type u}
    [Category.{v} C] (J : GrothendieckTopology C) (U : C) (hU : IsSubterminal U) (A : Type w)
    [Category.{w'} A] [∀ (F : (Over U)ᵒᵖ ⥤ A), (Over.forget U).op.HasPointwiseRightKanExtension F]
    {L : Sheaf (J.over U) A ⥤ Sheaf J A} (adj : L ⊣ J.overPullback A U) :
    IsIso adj.unit ∧
      IsIso ((Over.forget U).sheafAdjunctionCocontinuous A (J.over U) J).counit
```

## Tag 0EYV, a lemma

[Tag 0EYV](https://stacks.math.columbia.edu/tag/0EYV) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.overMapPullbackSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/MoreLocalization.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/MoreLocalization.lean#L332). The attribute's comment: “The relocalization morphisms of a commutative square form a commutative square of topoi: the two composites `j_{V'/V}^{-1} ⋙ j_{U'/V'}^{-1}` and `j_{U/V}^{-1} ⋙ j_{U'/U}^{-1}` of inverse images are canonically isomorphic.”.

> The square of topoi attached to a commutative square
>
> ```
>   U' --a--> U
>   |b        |c
>   V' --d--> V
> ```
>
> of `C` by the relocalization morphisms commutes, in the form of the commutation isomorphism
> `j_{V'/V}^{-1} ⋙ j_{U'/V'}^{-1} ≅ j_{U/V}^{-1} ⋙ j_{U'/U}^{-1}` between the two composite inverse
> images.

```lean
public def overMapPullbackSquare (sq : CommSq a b c d) :
    J.overMapPullback A d ⋙ J.overMapPullback A b ≅
      J.overMapPullback A c ⋙ J.overMapPullback A a
```

**`CategoryTheory.GrothendieckTopology.isIso_overMapPushforwardBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/MoreLocalization.lean, line 432](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/MoreLocalization.lean#L432). The attribute's comment: “For a cartesian square, the base change transformation `j_{V'/V}^{-1} ∘ j_{U/V,*} ⟶ j_{U'/V',*} ∘ j_{U'/U}^{-1}` of the relocalization morphisms is an isomorphism.”.

> If the square
>
> ```
>   U' --a--> U
>   |b        |c
>   V' --d--> V
> ```
>
> of `C` is cartesian, then the relocalization morphisms satisfy base change,
> `j_{V'/V}^{-1} ∘ j_{U/V, *} = j_{U'/V', *} ∘ j_{U'/U}^{-1}`: the base change transformation
> `overMapPushforwardBaseChange` is an isomorphism.

```lean
public theorem isIso_overMapPushforwardBaseChange (hsq : IsPullback a b c d)
    [∀ (F : (Over U)ᵒᵖ ⥤ A), (Over.map c).op.HasPointwiseRightKanExtension F]
    [∀ (F : (Over U')ᵒᵖ ⥤ A), (Over.map b).op.HasPointwiseRightKanExtension F] :
    IsIso (J.overMapPushforwardBaseChange A hsq.toCommSq)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.27, Tag 04IM](https://stacks.math.columbia.edu/tag/04IM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
