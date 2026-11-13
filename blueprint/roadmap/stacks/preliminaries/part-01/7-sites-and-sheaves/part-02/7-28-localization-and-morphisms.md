---
declaration: section
origin: cited
lean: CategoryTheory.Functor.isContinuous_overPost_of_isContinuous, CategoryTheory.Functor.isMorphismOfSites_overPost_of_isMorphismOfSites, CategoryTheory.sheafPushforwardContinuous_overPost_eq, CategoryTheory.sheafPullbackOverPostIso, CategoryTheory.SliceTopos.overPullbackCompSheafPullbackOverPostIso, CategoryTheory.SliceTopos.overPullbackCompSheafPullbackOverPostIso_hom, CategoryTheory.SliceTopos.sheafFunctorToOverCompOverPostSheafifyYonedaIso, CategoryTheory.Functor.isContinuous_overPost_of_flat
statement: formalized
proof: formalized
---

# 7.28 Localization and morphisms

Section 7.28 of the Stacks Project, [Tag 04I8](https://stacks.math.columbia.edu/tag/04I8). 7 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03CF, a lemma

[Tag 03CF](https://stacks.math.columbia.edu/tag/03CF) in the Stacks Project.

**`CategoryTheory.Functor.isContinuous_overPost_of_isContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SlicePost/MorphismOfSitesGeneral.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SlicePost/MorphismOfSitesGeneral.lean#L145). The attribute's comment: “Clause (a), continuity half: `u' = Over.post u` is continuous whenever `u` is, with no finite-limit or flatness hypothesis. This supersedes the flatness-based `Functor.isContinuous_overPost_of_flat`.”.

> **Stacks 03CF, continuity of `u'`, in the generality of 03CF.** If `u : C ⥤ D` is continuous
> then so is the localized functor `Over.post u : Over V ⥤ Over (u.obj V)`.
>
> By Stacks 00Y1 every sheaf on `D/U` is the fibre sheaf of a `K`-sheaf over `h_U^#`
> (`OverShriek.sheafUnit`), and the restriction of such a fibre sheaf along `Over.post u` is the
> fibre presheaf cut out on `C/V` by the restrictions along `u`, which is a sheaf by
> `OverShriek.isSheaf_fiber_overPost`.

```lean
theorem Functor.isContinuous_overPost_of_isContinuous {C : Type u} [SmallCategory C] {D : Type u}
    [SmallCategory D] (J : GrothendieckTopology C) (K : GrothendieckTopology D) (u : C ⥤ D)
    [u.IsContinuous J K] (V : C) :
    (Over.post (X := V) u).IsContinuous (J.over V) (K.over (u.obj V))
```

**`CategoryTheory.Functor.isMorphismOfSites_overPost_of_isMorphismOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SlicePost/MorphismOfSitesGeneral.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SlicePost/MorphismOfSitesGeneral.lean#L286). The attribute's comment: “Clause (a): the localized functor `u' = Over.post u` defines a morphism of sites `D/u(V) → C/V` whenever `u` does, which is 03CF's hypothesis. Stacks derives it from clause (c) via 00Y1; `Functor.isMorphismOfSites_overPost` is the variant under 03EF's finite-limit and left-exactness hypotheses.”.

> **Stacks 03CF, clause (a), in the generality of 03CF.** If `u : C ⥤ D` defines a morphism of
> sites `f : D → C` and `V : C`, then the localized functor `u' = Over.post u : Over V ⥤ Over (u V)`
> defines a morphism of sites `f' : D/u(V) → C/V`.
>
> Continuity is `Functor.isContinuous_overPost_of_isContinuous`.  Exactness of `u'_s` is checked on
> the terminal object and on fibre products: the former by
> `Functor.preservesTerminal_sheafPullback_of_isTerminal`, since `Over.post u` carries `𝟙_V` to
> `𝟙_{u V}`; the latter by `sheafPullbackOverPostIso`, `u'_s ⋙ j_{U!} ≅ j_{V!} ⋙ u_s`, together
> with the fact that `j_{V!}` preserves and `j_{U!}` reflects connected limits (Stacks 00Y1) and
> that `u_s` is left exact by hypothesis.

```lean
theorem Functor.isMorphismOfSites_overPost_of_isMorphismOfSites {C : Type u} [SmallCategory C]
    {D : Type u} [SmallCategory D] (J : GrothendieckTopology C) (K : GrothendieckTopology D)
    (u : C ⥤ D) (V : C) (h : u.IsMorphismOfSites J K) :
    (Over.post (X := V) u).IsMorphismOfSites (J.over V) (K.over (u.obj V))
```

**`CategoryTheory.sheafPushforwardContinuous_overPost_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SlicePost/Pushforward.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SlicePost/Pushforward.lean#L109). The attribute's comment: “Clause (d): the identity `f'_* j_U^{-1} = j_V^{-1} f_*`, for sheaves valued in any category; also the last sentence of 03EF. Clause (a) is in Sites/SlicePost/MorphismOfSitesGeneral.lean, clause (b) in Sites/SliceTopos/InverseImage.lean and clause (c) in Sites/SliceTopos/InverseImageYoneda.lean, all three in 03CF's own generality.”.

> **Stacks 03CF, last assertion**: `f'_* j_U^{-1} = j_V^{-1} f_*`, as a strict equality of
> functors `Sheaf K A ⥤ Sheaf (J.over V) A` for an arbitrary target category `A`.
>
> In Lean's left-to-right composition order the left-hand side below is `f'_* ∘ j_U^{-1}` and the
> right-hand side is `j_V^{-1} ∘ f_*`.  Both are precomposition with the opposite of a functor
> `Over V ⥤ D`, and the two functors agree on the nose by `Over.post_forget_eq_forget_comp`; this is
> Stacks' remark that the identity "holds even for presheaves".
>
> Clause (a) of Stacks 03CF, that `f'` is a morphism of sites, is
> `Functor.isMorphismOfSites_overPost_of_isMorphismOfSites` in
> `StacksFrontier/CategoryTheory/Sites/SlicePost/MorphismOfSitesGeneral.lean`, in the generality of
> 03CF.  Clauses (b) and (c) are proved in
> `StacksFrontier/CategoryTheory/Sites/SliceTopos/InverseImage.lean`, also in 03CF's own generality.

```lean
theorem sheafPushforwardContinuous_overPost_eq :
    (Over.forget (u.obj V)).sheafPushforwardContinuous A (K.over (u.obj V)) K ⋙
        (Over.post (X := V) u).sheafPushforwardContinuous A (J.over V) (K.over (u.obj V)) =
      u.sheafPushforwardContinuous A J K ⋙
        (Over.forget V).sheafPushforwardContinuous A (J.over V) J
```

**`CategoryTheory.sheafPullbackOverPostIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SlicePost/Pushforward.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SlicePost/Pushforward.lean#L133). The attribute's comment: “The isomorphism `j_{U!}(f')^{-1} ≅ f^{-1}j_{V!}` of the proof of 03CF, deduced from clause (d) by uniqueness of left adjoints; it is the input to clauses (b) and (c), which are `overPullbackCompSheafPullbackOverPostIso` and `sheafFunctorToOverCompOverPostSheafifyYonedaIso`.”.

> **The lower-shriek form of Stacks 03CF's computation**: `(f')^{-1} j_{U!} ≅ j_{V!} f^{-1}`.
>
> This is the isomorphism `j_{U!}(f')^{-1}H ≅ f^{-1}j_{V!}H` displayed in the proof of Stacks 03CF,
> obtained here not from Stacks 00WY but by taking left adjoints in
> `sheafPushforwardContinuous_overPost_eq`: `(f')^{-1} ⋙ j_{U!}` is left adjoint to
> `j_U^{-1} ⋙ f'_*` and `j_{V!} ⋙ f^{-1}` is left adjoint to `f_* ⋙ j_V^{-1}`, and those two right
> adjoints are equal.  Uniqueness of left adjoints does the rest.

```lean
noncomputable def sheafPullbackOverPostIso :
    (Over.post (X := V) u).sheafPullback A (J.over V) (K.over (u.obj V)) ⋙
        (Over.forget (u.obj V)).sheafPullback A (K.over (u.obj V)) K ≅
      (Over.forget V).sheafPullback A (J.over V) J ⋙ u.sheafPullback A J K
```

**`CategoryTheory.SliceTopos.overPullbackCompSheafPullbackOverPostIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/InverseImage.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SliceTopos/InverseImage.lean#L293). The attribute's comment: “Clause (b): the square of topoi commutes, `(f')⁻¹ j_V⁻¹ ≅ j_U⁻¹ f⁻¹`. Proved in 03CF's own generality, from `u.IsMorphismOfSites` alone. Clause (a) is `Functor.isMorphismOfSites_overPost_of_isMorphismOfSites`; clause (d) is `sheafPushforwardContinuous_overPost_eq`.”.

> **Stacks 03CF, clause (b): the square of topoi commutes.**
> ```
>   (f')⁻¹ j_V⁻¹ = j_U⁻¹ f⁻¹ .
> ```
> Unlike clause (d) this pairs *two inverse images*, so it is not a statement about right adjoints
> and does not follow from `sheafPushforwardContinuous_overPost_eq`. It follows from clause (c)
> instead: `Φ_U` is fully faithful, so it is enough to prove the square after applying it, and there
> Stacks 04IQ (`OverShriek.overPullbackCompSheafFunctorToOverIso`) turns both `j_V⁻¹ Φ_V` and
> `j_U⁻¹ Φ_U` into `toOver`, i.e. into "product with `h_V^#`" and "product with `h_U^#`". What is
> left is `toOverCompOverPostIso`, that `f⁻¹` carries one product to the other.
>
> The statement does not mention the identification `f⁻¹h_V^# ≅ h_U^#`, so — unlike clause (c) — it
> does not depend on which identification is used.

```lean
def overPullbackCompSheafPullbackOverPostIso (hu : u.IsMorphismOfSites J K) :
    J.overPullback (Type u) V ⋙
        (Over.post (X := V) u).sheafPullback (Type u) (J.over V) (K.over (u.obj V)) ≅
      u.sheafPullback (Type u) J K ⋙ K.overPullback (Type u) (u.obj V)
```

**`CategoryTheory.SliceTopos.overPullbackCompSheafPullbackOverPostIso_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/InverseImage.lean, line 582](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SliceTopos/InverseImage.lean#L582). The attribute's comment: “Clause (b) is the Beck-Chevalley mate of clause (d), which is what makes its components computable.”.

> **Stacks 03CF's clause (b) is the Beck–Chevalley mate of its clause (d).**
>
> The comparison `(f')^{-1}j_V^{-1} ≅ j_U^{-1}f^{-1}` built from Stacks 00Y1 coincides with the mate
> of the strict identity `f'_*j_U^{-1} = j_V^{-1}f_*`.  Since `j_{U!} ⊣ j_U^{-1}` is a bijection the
> two transformations may be compared through their adjuncts, and those agree by
> `shriek_overPullbackCompSheafPullbackOverPostIso_hom_app_comp_counit` and
> `overPullbackCompSheafPullbackOverPostMate_comp_counit`.
>
> This is what gives clause (b) computable components: every statement about the comparison can now
> be read off the unit and counit composite defining the mate.

```lean
theorem overPullbackCompSheafPullbackOverPostIso_hom (hu : u.IsMorphismOfSites J K) :
    (overPullbackCompSheafPullbackOverPostIso J K u V hu).hom =
      overPullbackCompSheafPullbackOverPostMate J K u V
```

**`CategoryTheory.SliceTopos.sheafFunctorToOverCompOverPostSheafifyYonedaIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/InverseImageYoneda.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SliceTopos/InverseImageYoneda.lean#L252). The attribute's comment: “Clause (c): under 00Y1's identifications `Sh(C/V) = Sh(C)/h_V^#` and `Sh(D/U) = Sh(D)/h_U^#`, `(f')⁻¹` sends `(H ⟶ h_V^#)` to `(f⁻¹H ⟶ h_U^#)`, with the identification `f⁻¹h_V^# ≅ h_U^#` of 04D3 (`sheafPullbackSheafifyYonedaIso`), for `u` any morphism of sites. Clause (a) is `Functor.isMorphismOfSites_overPost_of_isMorphismOfSites`, clause (b) `overPullbackCompSheafPullbackOverPostIso`, clause (d) `sheafPushforwardContinuous_overPost_eq`.”.

> **Stacks 03CF, clause (c), with Stacks 04D3's identification.**  Under the identifications
> `Sh(C/V) = Sh(C)/h_V^#` and `Sh(D/U) = Sh(D)/h_U^#` of Stacks 00Y1, the inverse image `(f')⁻¹`
> of the localized morphism of sites is the rule
> ```
>   (f')⁻¹ (H ⟶ h_V^#) = (f⁻¹H ⟶ f⁻¹h_V^# ≅ h_U^#) ,
> ```
> where `f⁻¹h_V^# ≅ h_U^#` is Lemma 04D3's `sheafPullbackSheafifyYonedaIso`, exactly as in Stacks.
> (Stacks writes `u : D → C` for the continuous functor; here `u : C ⥤ D`, `V : C`, `U = u(V)`.)

```lean
def sheafFunctorToOverCompOverPostSheafifyYonedaIso (hu : u.IsMorphismOfSites J K) :
    (Over.post (X := V) u).sheafPullback (Type u) (J.over V) (K.over (u.obj V)) ⋙
        sheafFunctorToOver (U := u.obj V) K ≅
      sheafFunctorToOver (U := V) J ⋙ Over.post (u.sheafPullback (Type u) J K) ⋙
        Over.map (sheafPullbackSheafifyYonedaIso u J K V).hom
```

## Tag 03EF, a lemma

[Tag 03EF](https://stacks.math.columbia.edu/tag/03EF) in the Stacks Project.

**`CategoryTheory.Functor.isContinuous_overPost_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SlicePost/Continuous.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SlicePost/Continuous.lean#L92). The attribute's comment: “Continuity of `u' : D/V ⥤ C/U` under 03EF's hypotheses: 03EF assumes `u` left exact between sites with all finite limits, whence `Over.post u` is flat and this lemma applies. This is the continuity half of `Functor.isMorphismOfSites_overPost`.”.

> Let `u : C ⥤ D` be a continuous functor of sites such that
> `Over.post u : Over V ⥤ Over (u.obj V)` is representably flat. Then `Over.post u` is continuous for
> the localized topologies `J.over V` and `K.over (u.obj V)`.

```lean
theorem isContinuous_overPost_of_flat (u : C ⥤ D) [u.IsContinuous J K] (V : C)
    [RepresentablyFlat (Over.post (X := V) u)] :
    (Over.post (X := V) u).IsContinuous (J.over V) (K.over (u.obj V))
```

**`CategoryTheory.starCompOverPostIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SlicePost/MorphismOfSites.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SlicePost/MorphismOfSites.lean#L77). The attribute's comment: “Commutativity of the diagram of 03EF: the two composites `C ⥤ Over (u.obj V)` of continuous functors around the square are isomorphic, which since morphisms of sites compose by composing their continuous functors (03CC) is what it means for the square of morphisms of sites to commute. The complete statement of 03EF, including that its diagram of topoi is 03CF's, is `SliceTopos.localizationDiagram`.”.

> For a functor `u : C ⥤ D` preserving binary products and `V : C`, the isomorphism
> `Over.star V ⋙ Over.post u ≅ u ⋙ Over.star (u.obj V)` of functors `C ⥤ Over (u.obj V)`, whose
> component at `X` is `Limits.prodComparison u V X : u.obj (V ⨯ X) ⟶ u.obj V ⨯ u.obj X`.

```lean
noncomputable def starCompOverPostIso [HasBinaryProducts C] [HasBinaryProducts D] (u : C ⥤ D)
    [PreservesLimitsOfShape (Discrete WalkingPair) u] (V : C) :
    Over.star V ⋙ Over.post (X := V) u ≅ u ⋙ Over.star (u.obj V)
```

**`CategoryTheory.Functor.isMorphismOfSites_overPost`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SlicePost/MorphismOfSites.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SlicePost/MorphismOfSites.lean#L109). The attribute's comment: “The left vertical arrow of 03EF's diagram: `u' = Over.post u` is a morphism of sites `D/U → C/V` under 03EF's hypotheses. This is 03CF's clause (a) in the special case where 03EF's hypotheses hold; clause (a) in the generality of 03CF is `Functor.isMorphismOfSites_overPost_of_isMorphismOfSites` in Sites/SlicePost/MorphismOfSitesGeneral.lean, proved there through 00Y1 as Stacks does.”. References: SGA 4 VI (7.4.13.6), “special case”.

> If `C` and `D` have all finite limits and `u : C ⥤ D` is continuous and commutes with finite
> limits, then for `V : C` the localized functor `Over.post u : Over V ⥤ Over (u.obj V)` defines a
> morphism of sites `D/U → C/V`, where `U = u.obj V`.

```lean
theorem isMorphismOfSites_overPost [HasFiniteLimits C] [HasFiniteLimits D] (u : C ⥤ D)
    [u.IsContinuous J K] [PreservesFiniteLimits u] (V : C) :
    (Over.post (X := V) u).IsMorphismOfSites (J.over V) (K.over (u.obj V))
```

**`CategoryTheory.Functor.isMorphismOfSites_star`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SlicePost/MorphismOfSites.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SlicePost/MorphismOfSites.lean#L120). The attribute's comment: “The two horizontal arrows `j_U` and `j_V` of 03EF's diagram: the localization functors `X ↦ X ⨯ U` of 03CE are morphisms of sites. Stated once, for an arbitrary site and object; the diagram of 03EF instantiates it at `(C, J, V)` and at `(D, K, u.obj V)`.”.

> On a site with binary products, the localization functor `Over.star X : C ⥤ Over X`,
> `Y ↦ (Y ⨯ X ⟶ X)`, defines a morphism of sites `C/X → C`.

```lean
theorem isMorphismOfSites_star [HasBinaryProducts C] (X : C) :
    (Over.star X).IsMorphismOfSites J (J.over X)
```

**`CategoryTheory.sheafPushforwardContinuousStarOverPostIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SlicePost/MorphismOfSites.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SlicePost/MorphismOfSites.lean#L145). The attribute's comment: “The induced diagram of morphisms of topoi commutes, on the pushforward side, for sheaves valued in any category. That this diagram is 03CF's diagram of topoi, and the complete statement of 03EF, is `SliceTopos.localizationDiagram` in Sites/SliceTopos/LocalizationDiagram.lean.”.

> The isomorphism
>
> ```
>   (Over.post u)_* ⋙ (Over.star V)_* ≅ (Over.star U)_* ⋙ u_* ,
> ```
>
> of functors `Sheaf (K.over U) A ⥤ Sheaf J A`, for `U = u.obj V` and any category `A`, induced by
> `starCompOverPostIso`: the square of pushforwards on sheaves commutes.

```lean
noncomputable def sheafPushforwardContinuousStarOverPostIso [HasBinaryProducts C]
    [HasBinaryProducts D] (u : C ⥤ D) [PreservesLimitsOfShape (Discrete WalkingPair) u] (V : C)
    [u.IsContinuous J K]
    [(Over.post (X := V) u).IsContinuous (J.over V) (K.over (u.obj V))]
    (A : Type*) [Category A] :
    (Over.post (X := V) u).sheafPushforwardContinuous A (J.over V) (K.over (u.obj V)) ⋙
        (Over.star V).sheafPushforwardContinuous A J (J.over V) ≅
      (Over.star (u.obj V)).sheafPushforwardContinuous A K (K.over (u.obj V)) ⋙
        u.sheafPushforwardContinuous A J K
```

**`CategoryTheory.SliceTopos.localizationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/LocalizationDiagram.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SliceTopos/LocalizationDiagram.lean#L96). The attribute's comment: “The complete statement: `u`, `u' = Over.post u` and both `Over.star` are morphisms of sites, the square of sites commutes (03CC), its diagram of topoi is 03CF's (the `Over.star` morphisms of topoi are the localization morphisms `j_V`, `j_U` on both the inverse- and the direct-image side, by 03CE), both squares of inverse images commute, and `f'_* j_U⁻¹ = j_V⁻¹ f_*`.”.

> **Stacks 03EF.** Let `u : C ⥤ D` be a continuous, left exact functor between small sites
> `(C, J)` and `(D, K)` with all finite limits, let `V : C` and `U = u.obj V`. Then:
>
> 1. `u` is a morphism of sites `f` (Stacks 00X6);
> 2. `u' = Over.post u : C/V ⥤ D/U`, `V'/V ↦ u(V')/U`, is a morphism of sites `f'`;
> 3. `Over.star V : C ⥤ C/V` and `Over.star U : D ⥤ D/U` (`X ↦ X × V`, `Y ↦ Y × U`, Stacks 03CE)
>    are morphisms of sites `j_V`, `j_U`;
> 4. the square of morphisms of sites commutes: `Over.star V ⋙ u' ≅ u ⋙ Over.star U`, which by
>    Stacks 03CC is commutativity of the square of morphisms of sites;
> 5. the associated diagram of morphisms of topoi is the diagram of Stacks 03CF: its vertical
>    arrows are the morphisms of topoi of `u` and `u'` in both diagrams; its horizontal arrows,
>    the morphisms of topoi of the morphisms of sites `Over.star`, are the localization morphisms
>    `j_V`, `j_U` of 03CF, as their inverse images are restriction along `Over.forget` and their
>    direct images are `j_{V*}`, `j_{U*}` (`(Over.forget _).sheafPushforwardCocontinuous`);
>    03CF's square commutes, `(f')⁻¹ j_V⁻¹ ≅ j_U⁻¹ f⁻¹`, and so does the inverse-image square of
>    the morphisms of sites, `(Over.star V)_s ⋙ u'_s ≅ u_s ⋙ (Over.star U)_s`;
> 6. `f'_* j_U⁻¹ = j_V⁻¹ f_*`.

```lean
theorem localizationDiagram [HasFiniteLimits C] [HasFiniteLimits D] [u.IsContinuous J K]
    [PreservesFiniteLimits u] :
    u.IsMorphismOfSites J K ∧
      (Over.post (X := V) u).IsMorphismOfSites (J.over V) (K.over (u.obj V)) ∧
      (Over.star V).IsMorphismOfSites J (J.over V) ∧
      (Over.star (u.obj V)).IsMorphismOfSites K (K.over (u.obj V)) ∧
      Nonempty (Over.star V ⋙ Over.post (X := V) u ≅ u ⋙ Over.star (u.obj V)) ∧
      Nonempty ((Over.star V).sheafPullback (Type u) J (J.over V) ≅
        J.overPullback (Type u) V) ∧
      Nonempty ((Over.forget V).sheafPushforwardCocontinuous (Type u) (J.over V) J ≅
        (Over.star V).sheafPushforwardContinuous (Type u) J (J.over V)) ∧
      Nonempty ((Over.star (u.obj V)).sheafPullback (Type u) K (K.over (u.obj V)) ≅
        K.overPullback (Type u) (u.obj V)) ∧
      Nonempty ((Over.forget (u.obj V)).sheafPushforwardCocontinuous (Type u)
          (K.over (u.obj V)) K ≅
        (Over.star (u.obj V)).sheafPushforwardContinuous (Type u) K (K.over (u.obj V))) ∧
      Nonempty (J.overPullback (Type u) V ⋙
          (Over.post (X := V) u).sheafPullback (Type u) (J.over V) (K.over (u.obj V)) ≅
        u.sheafPullback (Type u) J K ⋙ K.overPullback (Type u) (u.obj V)) ∧
      Nonempty ((Over.star V).sheafPullback (Type u) J (J.over V) ⋙
          (Over.post (X := V) u).sheafPullback (Type u) (J.over V) (K.over (u.obj V)) ≅
        u.sheafPullback (Type u) J K ⋙
          (Over.star (u.obj V)).sheafPullback (Type u) K (K.over (u.obj V))) ∧
      (Over.forget (u.obj V)).sheafPushforwardContinuous (Type u) (K.over (u.obj V)) K ⋙
          (Over.post (X := V) u).sheafPushforwardContinuous (Type u) (J.over V)
            (K.over (u.obj V)) =
        u.sheafPushforwardContinuous (Type u) J K ⋙
          (Over.forget V).sheafPushforwardContinuous (Type u) (J.over V) J
```

## Tag 04IN, a lemma

[Tag 04IN](https://stacks.math.columbia.edu/tag/04IN) in the Stacks Project.

**`MorphismOfTopoi.relocalize`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/RelocalizationMorphism.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/RelocalizationMorphism.lean#L163). The attribute's comment: “the morphism of topoi f\_c and the factorization f\_c = f' ∘ j\_\{U/u(V)}”.

> **Stacks 04IN.** Let `f : E ⟶ D` be a morphism of topoi, `V` an object of `D`, `U` an object
> of `E` and `c : U ⟶ f⁻¹V`.  The morphism of topoi `f_c : E/U ⟶ D/V` is the composition
> ```
>   f_c = f' ∘ j_{U/f⁻¹V}
> ```
> of the relocalization morphism `j_{U/f⁻¹V} : E/U ⟶ E/f⁻¹V` of Stacks 03EH with the morphism
> `f' : E/f⁻¹V ⟶ D/V` of Stacks 04H1 (03CF); this factorization is Stacks 04IN's second
> assertion, and holds here by construction.  Consequently
> ```
>   (f_c)⁻¹ = Over.post f⁻¹ ⋙ Over.pullback c ,
> ```
> see `relocalize_inverseImage_obj`.

```lean
noncomputable def relocalize {V : D} {U : E} (c : U ⟶ f.inverseImage.obj V)
    {p : Over U ⥤ Over (f.inverseImage.obj V)} (adj : Over.pullback c ⊣ p) :
    MorphismOfTopoi (Over U) (Over V)
```

**`MorphismOfTopoi.relocalize_inverseImage_obj`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/RelocalizationMorphism.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/RelocalizationMorphism.lean#L175). The attribute's comment: “the description of (f\_c)^\{-1} as a fibre product”.

> **Stacks 04IN**, the description of `(f_c)⁻¹`: an object `φ : H ⟶ V` of `D/V` is sent to the
> fibre product
> ```
>   (f⁻¹H ×_{f⁻¹φ, f⁻¹V, c} U ⟶ U) ,
> ```
> the base change along `c` of `f⁻¹φ`.

```lean
lemma relocalize_inverseImage_obj {V : D} {U : E} (c : U ⟶ f.inverseImage.obj V)
    {p : Over U ⥤ Over (f.inverseImage.obj V)} (adj : Over.pullback c ⊣ p) (H : Over V) :
    (f.relocalize c adj).inverseImage.obj H =
      Over.mk (pullback.snd (f.inverseImage.map H.hom) c)
```

**`MorphismOfTopoi.relocalizeInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/RelocalizationMorphism.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/RelocalizationMorphism.lean#L191). The attribute's comment: “commutativity of the first square, on inverse images”.

> **Stacks 04IN**, commutativity of the first square: `j_U⁻¹ ∘ f⁻¹ = (f_c)⁻¹ ∘ j_V⁻¹`, where
> `j_U⁻¹ = toOver U` and `j_V⁻¹ = toOver V`.
>
> The proof is the one Stacks gives: the square of Stacks 04H1 for `f'`, namely
> `f⁻¹ ⋙ toOver (f⁻¹V) ≅ toOver V ⋙ (f')⁻¹`, is whiskered with the base change
> `j_{U/f⁻¹V}⁻¹ = Over.pullback c`, and the left-hand side collapses by
> `toOverCompPullbackIso`, the identity `j_{U/f⁻¹V}⁻¹ ∘ j_{f⁻¹V}⁻¹ = j_U⁻¹` of Stacks 03EH.

```lean
noncomputable def relocalizeInverseImageIso {V : D} {U : E} (c : U ⟶ f.inverseImage.obj V)
    {p : Over U ⥤ Over (f.inverseImage.obj V)} (adj : Over.pullback c ⊣ p) :
    f.inverseImage ⋙ toOver U ≅ toOver V ⋙ (f.relocalize c adj).inverseImage
```

**`MorphismOfTopoi.relocalizeCompPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/RelocalizationMorphism.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/RelocalizationMorphism.lean#L214). The attribute's comment: “commutativity of the last square, on inverse images”.

> **Stacks 04IN**, commutativity of the last square: given `b : V' ⟶ V`, `a : U' ⟶ U` and
> `c' : U' ⟶ f⁻¹V'` with `c' ≫ f⁻¹b = a ≫ c`, the square
> ```
>   E/U' --j_{U'/U}--> E/U
>    |f_{c'}            |f_c
>   D/V' --j_{V'/V}--> D/V
> ```
> commutes, i.e. `(f_c)⁻¹ ∘ j_{U'/U}⁻¹ = j_{V'/V}⁻¹ ∘ (f_{c'})⁻¹` on inverse images.
>
> This is Stacks' equality
> ```
>   f⁻¹H ×_{f⁻¹V, c} U ×_U U' = f⁻¹(H ×_V V') ×_{f⁻¹V', c'} U' ,
> ```
> obtained here by Beck–Chevalley for `Over.post f⁻¹` (`Over.postPullbackIso`, which uses that
> `f⁻¹` is left exact), the composition rule `Over.pullbackComp` for base change, and the
> hypothesis `c' ≫ f⁻¹b = a ≫ c`.

```lean
noncomputable def relocalizeCompPullbackIso {V V' : D} (b : V' ⟶ V) {U U' : E} (a : U' ⟶ U)
    (c : U ⟶ f.inverseImage.obj V) (c' : U' ⟶ f.inverseImage.obj V')
    (hc : c' ≫ f.inverseImage.map b = a ≫ c)
    {p : Over U ⥤ Over (f.inverseImage.obj V)} (adj : Over.pullback c ⊣ p)
    {p' : Over U' ⥤ Over (f.inverseImage.obj V')} (adj' : Over.pullback c' ⊣ p') :
    Over.pullback b ⋙ (f.relocalize c' adj').inverseImage ≅
      (f.relocalize c adj).inverseImage ⋙ Over.pullback a
```

## Tag 03EG, a lemma

[Tag 03EG](https://stacks.math.columbia.edu/tag/03EG) in the Stacks Project.

**`overPost_comp_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/LocalizationComposite.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/LocalizationComposite.lean#L103). The attribute's comment: “the square of categories commutes: `u' ⋙ j_V = j_U ⋙ u`”.

> **Stacks 03EG**, the square of categories.  With `V = u(U)`, the localized functor
> `u' = Over.post u : C/U ⥤ D/V` and the localization functors `j_U = Over.forget U` and
> `j_V = Over.forget V` form a commutative square, `u' ⋙ j_V = j_U ⋙ u`.  Stacks calls this
> "clear"; in Lean the two composites are equal by `rfl`.

```lean
theorem overPost_comp_forget :
    (Over.post u : Over U ⥤ Over (u.obj U)) ⋙ Over.forget (u.obj U) = Over.forget U ⋙ u
```

**`isCocontinuous_overPost`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/LocalizationComposite.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/LocalizationComposite.lean#L118). The attribute's comment: “the left vertical arrow `u'` is cocontinuous”.

> **Stacks 03EG**, the mathematical content.  If `u : C ⥤ D` is cocontinuous then so is the
> localized functor `u' = Over.post u : C/U ⥤ D/u(U)`, for the localized topologies `J.over U` and
> `K.over (u.obj U)`.
>
> Stacks proves this by transferring refinement data verbatim: a covering of `u(U')/u(U)` in
> `D/u(U)` is in particular a covering of `u(U')` in `D`, cocontinuity of `u` refines its
> `u`-image by a covering `{U'_i → U'}` of `C`, and the very same index map and comparison
> morphisms exhibit the refinement after every object is viewed over `U`, resp. over `u(U)`.  In
> Mathlib's sieve-theoretic formulation this is
> `CategoryTheory.GrothendieckTopology.instIsCocontinuousOverObjPostOver`.

```lean
theorem isCocontinuous_overPost :
    (Over.post u : Over U ⥤ Over (u.obj U)).IsCocontinuous (J.over U) (K.over (u.obj U))
```

**`sheafPushforwardCocontinuousOverPostIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/LocalizationComposite.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/LocalizationComposite.lean#L133). The attribute's comment: “the square of topoi commutes: `f'_* ⋙ j_{V*} ≅ j_{U*} ⋙ f_*`”.

> **Stacks 03EG**, the square of topoi.  Let `f : Sh(C) ⟶ Sh(D)` and
> `f' : Sh(C/U) ⟶ Sh(D/u(U))` be the morphisms of topoi attached to `u` and to
> `u' = Over.post u` by Stacks 00XO, and let `j_U : Sh(C/U) ⟶ Sh(C)` and
> `j_V : Sh(D/u(U)) ⟶ Sh(D)` be those attached to the localization functors.  Then the square of
> topoi commutes: there is a natural isomorphism `f'_* ⋙ j_{V*} ≅ j_{U*} ⋙ f_*` of functors
> `Sh(C/U) ⥤ Sh(D)`.
>
> Both composites compute the direct image of one and the same functor `C/U ⥤ D`, since
> `u' ⋙ j_V = j_U ⋙ u` by `overPost_comp_forget`; the isomorphism is therefore obtained by
> comparing each side with that direct image using Stacks 03L5.

```lean
noncomputable def sheafPushforwardCocontinuousOverPostIso :
    (Over.post u : Over U ⥤ Over (u.obj U)).sheafPushforwardCocontinuous (Type u)
          (J.over U) (K.over (u.obj U)) ⋙
        (Over.forget (u.obj U)).sheafPushforwardCocontinuous (Type u) (K.over (u.obj U)) K ≅
      (Over.forget U).sheafPushforwardCocontinuous (Type u) (J.over U) J ⋙
        u.sheafPushforwardCocontinuous (Type u) J K
```

## Tag 0D5R, a lemma

[Tag 0D5R](https://stacks.math.columbia.edu/tag/0D5R) in the Stacks Project.

**`CategoryTheory.Functor.exists_grothendieckTopology_costructuredArrow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/AndMorphisms.lean, line 551](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/AndMorphisms.lean#L551). The attribute's comment: “The site of pairs `(U, ψ : u(U) → V)` for a cocontinuous `u`: `j` is continuous and cocontinuous, `u'` is cocontinuous, the resulting square of topoi commutes and `f'_* j⁻¹ = j_V⁻¹ f_*`. For sheaves of sets on small sites.”. References: SGA 3 IV (4.5.1), “partial, special case”; SGA 4 III (5.2), “special case”.

> Let `(C, J)` and `(D, K)` be sites, let `u : C ⥤ D` be cocontinuous and let
> `V` be an object of `D`. Let `{}^u_V I = CostructuredArrow u V` be the category of pairs
> `(U, ψ : u(U) ⟶ V)` of Section 00XF, with the two projections `j = CostructuredArrow.proj u V`,
> `(U, ψ) ↦ U`, and `u' = CostructuredArrow.toOver u V`, `(U, ψ) ↦ (ψ : u(U) ⟶ V)`. Then the square
> ```
>   {}^u_V I --j--> C
>      |            |
>      u'           u
>      v            v
>     D/V --j_V---> D
> ```
> commutes, and declaring a sieve of `(U, ψ)` to be covering when its image under `j` is a covering
> sieve of `U`:
>
> 1. this is a Grothendieck topology `H` on `{}^u_V I`, i.e. `{}^u_V I` is a site;
> 2. `j` is continuous and cocontinuous;
> 3. `u'` is cocontinuous;
> 4. the induced square of topoi commutes, `j_* ⋙ f_* ≅ f'_* ⋙ j_{V*}`, where `f` and `f'` are the
>    morphisms of topoi of Stacks 00XO attached to the cocontinuous functors `u` and `u'`; and
> 5. `f'_* ∘ j⁻¹ = j_V⁻¹ ∘ f_*`, where the inverse images of the continuous and cocontinuous functors
>    `j` and `j_V` are restriction (Stacks 00XR).

```lean
public theorem exists_grothendieckTopology_costructuredArrow {C : Type u} [SmallCategory C]
    {D : Type u} [SmallCategory D] (J : GrothendieckTopology C) (K : GrothendieckTopology D)
    (u : C ⥤ D) [u.IsCocontinuous J K] (V : D) :
    CostructuredArrow.proj u V ⋙ u = CostructuredArrow.toOver u V ⋙ Over.forget V ∧
      ∃ H : GrothendieckTopology (CostructuredArrow u V),
        (∀ (X : CostructuredArrow u V) (S : Sieve X),
            S ∈ H X ↔ Sieve.functorPushforward (CostructuredArrow.proj u V) S ∈ J X.left) ∧
          ∃ (_ : (CostructuredArrow.proj u V).IsContinuous H J) (_ :
            (CostructuredArrow.proj u V).IsCocontinuous H J) (_ :
            (CostructuredArrow.toOver u V).IsCocontinuous H (K.over V)),
            Nonempty
                ((CostructuredArrow.proj u V).sheafPushforwardCocontinuous (Type u) H J ⋙
                    u.sheafPushforwardCocontinuous (Type u) J K ≅
                  (CostructuredArrow.toOver u V).sheafPushforwardCocontinuous (Type u) H
                      (K.over V) ⋙
                    (Over.forget V).sheafPushforwardCocontinuous (Type u) (K.over V) K) ∧
              Nonempty
                ((CostructuredArrow.proj u V).sheafPushforwardContinuous (Type u) H J ⋙
                    (CostructuredArrow.toOver u V).sheafPushforwardCocontinuous (Type u) H
                      (K.over V) ≅
                  u.sheafPushforwardCocontinuous (Type u) J K ⋙
                    (Over.forget V).sheafPushforwardContinuous (Type u) (K.over V) K)
```

## Tag 0FN1, a lemma

[Tag 0FN1](https://stacks.math.columbia.edu/tag/0FN1) in the Stacks Project.

**`CategoryTheory.Functor.nonempty_sheafPushforwardContinuousCompCocontinuousIso_and_leftAdjointCompPullbackIso_of_final`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/AndMorphisms.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/AndMorphisms.lean#L214). The attribute's comment: “Beck–Chevalley for a commutative square of sites whose vertical functors are cocontinuous and whose horizontal functors are continuous: if the comparison functors `{}^{u'}_{V'} I ⥤ {}^u_{v(V')} I` are all cofinal then `f'_* (g')⁻¹ = g⁻¹ f_*`, and `g'_! (f')⁻¹ = f⁻¹ g_!` whenever the relevant left adjoints exist — a hypothesis of the second conjunct only, the first equality being the cofinality content and using no adjoint. For coefficients in an arbitrary category, the source's sheaves of sets being the case `A = Type u`; cocontinuity of the horizontal functors is not needed once their inverse images are read as restriction (Stacks 00XR).”.

> Let `(C', J')`, `(C, J)`, `(D', K')`, `(D, K)` be sites and consider a square
> of functors
> ```
>   C' --v'--> C
>   |          |
>   u'         u
>   v          v
>   D' --v---> D
> ```
> with `u' ⋙ v = v' ⋙ u`, where `u` and `u'` are cocontinuous — giving rise to morphisms of topoi `f`
> and `f'` with `f_* = {}_su`, `f'_* = {}_su'` (Stacks 00XO) — and `v` and `v'` are continuous, so
> that `g⁻¹ = v^p` and `(g')⁻¹ = (v')^p` are restriction (Stacks 00XR). Assume that for every object
> `V'` of `D'` the comparison functor
> ```
>   {}^{u'}_{V'} I ⥤ {}^u_{v(V')} I,   (U', ψ) ↦ (v'(U'), v(ψ) : u(v'(U')) = v(u'(U')) ⟶ v(V')),
> ```
> on the categories of Section 00XF is cofinal, i.e. final. Then `f'_* ∘ (g')⁻¹ ≅ g⁻¹ ∘ f_*`, and
> moreover `g'_! ∘ (f')⁻¹ ≅ f⁻¹ ∘ g_!` whenever the two restrictions have left adjoints `g_!`, `g'_!`
> and the two pushforwards have left adjoints `f⁻¹`, `(f')⁻¹`. This holds for sheaves with values
> in an arbitrary category `A`.

```lean
public theorem
  nonempty_sheafPushforwardContinuousCompCocontinuousIso_and_leftAdjointCompPullbackIso_of_final
    {C' : Type u₁} [Category.{v₁} C'] {C : Type u₂} [Category.{v₂} C] {D' : Type u₃}
    [Category.{v₃} D'] {D : Type u₄} [Category.{v₄} D] (A : Type u₅) [Category.{v₅} A]
    (J' : GrothendieckTopology C') (J : GrothendieckTopology C) (K' : GrothendieckTopology D')
    (K : GrothendieckTopology D) (u' : C' ⥤ D') (u : C ⥤ D) (v' : C' ⥤ C) (v : D' ⥤ D)
    [u.IsCocontinuous J K] [u'.IsCocontinuous J' K'] [v.IsContinuous K' K] [v'.IsContinuous J' J]
    [∀ F : Cᵒᵖ ⥤ A, u.op.HasPointwiseRightKanExtension F]
    [∀ F : C'ᵒᵖ ⥤ A, u'.op.HasPointwiseRightKanExtension F] (hsq : u' ⋙ v = v' ⋙ u)
    (hfinal :
      ∀ V' : D',
        (CostructuredArrow.map₂ (S := u') (T := V') (U := u) (V := v.obj V') (F := v') (G := v)
            (eqToHom hsq.symm) (𝟙 (v.obj V'))).Final) :
    Nonempty
        (v'.sheafPushforwardContinuous A J' J ⋙ u'.sheafPushforwardCocontinuous A J' K' ≅
          u.sheafPushforwardCocontinuous A J K ⋙ v.sheafPushforwardContinuous A K' K) ∧
      ∀ [(u.sheafPushforwardCocontinuous A J K).IsRightAdjoint]
        [(u'.sheafPushforwardCocontinuous A J' K').IsRightAdjoint]
        [(v'.sheafPushforwardContinuous A J' J).IsRightAdjoint]
        [(v.sheafPushforwardContinuous A K' K).IsRightAdjoint],
        Nonempty
          ((u'.sheafPushforwardCocontinuous A J' K').leftAdjoint ⋙ v'.sheafPullback A J' J ≅
            v.sheafPullback A K' K ⋙ (u.sheafPushforwardCocontinuous A J K).leftAdjoint)
```

## Tag 0FN2, a lemma

[Tag 0FN2](https://stacks.math.columbia.edu/tag/0FN2) in the Stacks Project.

**`CategoryTheory.Functor.sheafPushforwardContinuous_comp_eq_and_nonempty_sheafPullbackCompIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/AndMorphisms.lean, line 699](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/AndMorphisms.lean#L699). The attribute's comment: “Exchange for a commutative square of sites whose horizontal functors `u`, `u'` are continuous and whose vertical functors `v`, `v'` are continuous (in the source, continuous and cocontinuous): `f'_* (g')⁻¹ = g⁻¹ f_*` on the nose, and `g'_! (f')⁻¹ ≅ f⁻¹ g_!`. For coefficients in an arbitrary category; cocontinuity of `v`, `v'` is not needed once their inverse images are read as restriction (Stacks 00XR).”.

> Let `(C', J')`, `(C, J)`, `(D', K')`, `(D, K)` be sites and consider a square
> of functors
> ```
>   C' --v'--> C
>   ↑          ↑
>   u'         u
>   D' --v---> D
> ```
> with `v ⋙ u = u' ⋙ v'`, where `u` and `u'` are continuous — giving rise to morphisms of sites `f`
> and `f'` with `f_* = u^s`, `f'_* = (u')^s` and `f⁻¹ = u_s`, `(f')⁻¹ = (u')_s` (Stacks 00X0) — and
> `v` and `v'` are continuous, so that `g⁻¹ = v^p` and `(g')⁻¹ = (v')^p` are restriction and `g_!`,
> `g'_!` are their left adjoints (Stacks 00XR, for `v`, `v'` also cocontinuous). Then
> `f'_* ∘ (g')⁻¹ = g⁻¹ ∘ f_*` and `g'_! ∘ (f')⁻¹ ≅ f⁻¹ ∘ g_!`.

```lean
public theorem sheafPushforwardContinuous_comp_eq_and_nonempty_sheafPullbackCompIso {C' : Type u₁}
    [Category.{v₁} C'] {C : Type u₂} [Category.{v₂} C] {D' : Type u₃} [Category.{v₃} D']
    {D : Type u₄} [Category.{v₄} D] (A : Type u₅) [Category.{v₅} A] (J' : GrothendieckTopology C')
    (J : GrothendieckTopology C) (K' : GrothendieckTopology D') (K : GrothendieckTopology D)
    (u : D ⥤ C) (u' : D' ⥤ C') (v : D' ⥤ D) (v' : C' ⥤ C) [u.IsContinuous K J]
    [u'.IsContinuous K' J'] [v.IsContinuous K' K] [v'.IsContinuous J' J]
    [(u.sheafPushforwardContinuous A K J).IsRightAdjoint]
    [(u'.sheafPushforwardContinuous A K' J').IsRightAdjoint]
    [(v.sheafPushforwardContinuous A K' K).IsRightAdjoint]
    [(v'.sheafPushforwardContinuous A J' J).IsRightAdjoint] (hsq : v ⋙ u = u' ⋙ v') :
    v'.sheafPushforwardContinuous A J' J ⋙ u'.sheafPushforwardContinuous A K' J' =
        u.sheafPushforwardContinuous A K J ⋙ v.sheafPushforwardContinuous A K' K ∧
      Nonempty
        (u'.sheafPullback A K' J' ⋙ v'.sheafPullback A J' J ≅
          v.sheafPullback A K' K ⋙ u.sheafPullback A K J)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.28, Tag 04I8](https://stacks.math.columbia.edu/tag/04I8)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
