---
declaration: section
origin: cited
lean: CategoryTheory.OverShriek.overShriek_sheafify_iso, CategoryTheory.overShriekSheafifyYonedaIso, CategoryTheory.OverShriek.isEquivalence_sheafFunctorToOver, CategoryTheory.OverShriek.sheafEquivalence, CategoryTheory.OverShriek.sheafFunctorToOverForgetIsoOfAdjunction, CategoryTheory.OverShriek.preservesLimitsOfShape_of_isConnected, CategoryTheory.OverShriek.reflectsMonomorphisms_and_reflectsEpimorphisms, CategoryTheory.OverShriek.overShriek_overPullback_iso
statement: formalized
proof: formalized
---

# 7.25 Localization

Section 7.25 of the Stacks Project, [Tag 00XZ](https://stacks.math.columbia.edu/tag/00XZ). 8 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03CD, a lemma

[Tag 03CD](https://stacks.math.columbia.edu/tag/03CD) in the Stacks Project.

**`CategoryTheory.OverShriek.overShriek_sheafify_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/LowerShriekCoproducts.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/LowerShriekCoproducts.lean#L245).

> **Stacks 03CD**, packaged as the existence of the isomorphism
> `j_{U!}(G^#) ≅ (∐_{φ : V ⟶ U} G(V →φ U))^#`.

```lean
theorem overShriek_sheafify_iso :
    Nonempty
      (((Over.forget U).sheafPullback (Type v) (J.over U) J).obj
          ((presheafToSheaf (J.over U) (Type v)).obj G) ≅
        (presheafToSheaf J (Type v)).obj (presheaf G))
```

## Tag 03HU, a lemma

[Tag 03HU](https://stacks.math.columbia.edu/tag/03HU) in the Stacks Project.

**`CategoryTheory.overShriekSheafifyYonedaIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/LowerShriekRepresentable.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/LowerShriekRepresentable.lean#L50).

> **Stacks 03HU.** For an object `X/U` of the localized site `C/U`, the lower shriek
> `j_{U!} = (Over.forget U).sheafPullback` of the sheaf `h_{X/U}^#` associated to the presheaf on
> `C/U` represented by `X/U` is the sheaf `h_X^#` associated to the presheaf on `C` represented by
> the underlying object `X = j_U(X/U)`.

```lean
noncomputable def overShriekSheafifyYonedaIso (X : Over U) :
    ((Over.forget U).sheafPullback (Type v) (J.over U) J).obj
        ((presheafToSheaf (J.over U) (Type v)).obj (yoneda.obj X)) ≅
      (presheafToSheaf J (Type v)).obj (yoneda.obj X.left)
```

## Tag 00Y1, a lemma

[Tag 00Y1](https://stacks.math.columbia.edu/tag/00Y1) in the Stacks Project.

**`CategoryTheory.OverShriek.isEquivalence_sheafFunctorToOver`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/SheavesOverRepresentable.lean, line 515](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/SheavesOverRepresentable.lean#L515). The attribute's comment: “the functor j\_\{U!} : Sh(C/U) ⥤ Sh(C)/h\_U^# is an equivalence”.

> **Stacks 00Y1.** The functor `Φ_sh : Sh(C/U) ⥤ Sh(C)/h_U^#` induced by `j_{U!}` is full,
> faithful and essentially surjective, i.e. an equivalence.

```lean
instance isEquivalence_sheafFunctorToOver : (sheafFunctorToOver (U := U) J).IsEquivalence
```

**`CategoryTheory.OverShriek.sheafEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/SheavesOverRepresentable.lean, line 522](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/SheavesOverRepresentable.lean#L522). The attribute's comment: “the resulting equivalence of categories Sh(C/U) ≌ Sh(C)/h\_U^#”.

> **Stacks 00Y1**, as an equivalence of categories `Sh(C/U) ≌ Sh(C)/h_U^#`. Its functor is
> `sheafFunctorToOver`, the sheaf level `j_{U!}` viewed as a functor into the slice
> (`sheafEquivalence_functor`), and its inverse is isomorphic to the fibre functor
> `(F, φ) ↦ F_φ`.

```lean
def sheafEquivalence :
    Sheaf (J.over U) (Type v) ≌ Over ((presheafToSheaf J (Type v)).obj (yoneda.obj U))
```

**`CategoryTheory.OverShriek.sheafFunctorToOverForgetIsoOfAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/SheavesOverRepresentable.lean, line 561](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/SheavesOverRepresentable.lean#L561). The attribute's comment: “j\_\{U!} is Sh(C/U) ≌ Sh(C)/h\_U^# followed by Over.forget, for any left adjoint”.

> **Stacks 00Y1, in the form the source restates it in**: `j_{U!}` *is* the equivalence
> `Φ : Sh(C/U) ≌ Sh(C)/h_U^#` followed by `Over.forget : Sh(C)/h_U^# ⥤ Sh(C)`.
>
> Here `j_{U!}` is an arbitrary left adjoint `L` of the restriction functor `j_U^{-1}`, so this is a
> statement about `j_{U!}` rather than about one model of it: `sheafFunctorToOverForgetIso` identifies
> `Φ ⋙ Over.forget` with the left adjoint obtained from `Over.forget U`, and two left adjoints of one
> functor are canonically isomorphic.
>
> The adjunction `adj` is also what makes that left adjoint exist (`J.overPullback` being the
> pushforward along `Over.forget U`), so no adjointness hypothesis beyond `adj` is assumed.

```lean
def sheafFunctorToOverForgetIsoOfAdjunction
    {L : Sheaf (J.over U) (Type v) ⥤ Sheaf J (Type v)} (adj : L ⊣ J.overPullback (Type v) U) :
    sheafFunctorToOver (U := U) J ⋙ Over.forget _ ≅ L
```

## Tag 04BB, a lemma

[Tag 04BB](https://stacks.math.columbia.edu/tag/04BB) in the Stacks Project.

**`CategoryTheory.OverShriek.preservesLimitsOfShape_of_isConnected`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/Localization.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/Localization.lean#L162). The attribute's comment: “j\_\{U!} commutes with fibre products and equalizers, and more generally with connected limits; in particular it preserves subsheaf inclusions.”. References: SGA 4 III (5.1), “fibre products clause”; SGA 4 III (1.9.2), “more general”.

> **Stacks 04BB.** Let `C` be a site and let `U` be an object of `C`. Let `L` be a left adjoint
> of the restriction functor `j_U^{-1} = J.overPullback : Sh(C) ⥤ Sh(C/U)`, i.e. let `L` be
> `j_{U!}`. Then `L` commutes with limits of every connected shape `K`; in particular it commutes
> with fibre products (`K = WalkingCospan`) and equalizers (`K = WalkingParallelPair`), and hence
> carries subsheaf inclusions to subsheaf inclusions.

```lean
public theorem preservesLimitsOfShape_of_isConnected {C : Type u} [Category.{v} C]
    (J : GrothendieckTopology C) (U : C) [HasWeakSheafify J (Type v)]
    [HasWeakSheafify (J.over U) (Type v)] [J.WEqualsLocallyBijective (Type v)]
    {L : Sheaf (J.over U) (Type v) ⥤ Sheaf J (Type v)} (adj : L ⊣ J.overPullback (Type v) U)
    {K : Type w} [Category.{w'} K] [IsConnected K] :
    Limits.PreservesLimitsOfShape K L
```

## Tag 0E8E, a lemma

[Tag 0E8E](https://stacks.math.columbia.edu/tag/0E8E) in the Stacks Project.

**`CategoryTheory.OverShriek.reflectsMonomorphisms_and_reflectsEpimorphisms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/Localization.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/Localization.lean#L264). The attribute's comment: “j\_\{U!} reflects injections and surjections of sheaves of sets.”.

> **Stacks 0E8E.** Let `C` be a site and let `U` be an object of `C`. Let `L` be a left adjoint
> of the restriction functor `j_U^{-1} = J.overPullback : Sh(C) ⥤ Sh(C/U)`, i.e. let `L` be
> `j_{U!}`. Then `L` reflects monomorphisms and epimorphisms, that is (Stacks 00WN), if `j_{U!}φ` is
> an injection of sheaves of sets then so is `φ`, and if `j_{U!}φ` is a surjection of sheaves of
> sets then so is `φ`.

```lean
public theorem reflectsMonomorphisms_and_reflectsEpimorphisms {C : Type u} [Category.{v} C]
    (J : GrothendieckTopology C) (U : C) [HasWeakSheafify J (Type v)]
    [HasWeakSheafify (J.over U) (Type v)] [J.WEqualsLocallyBijective (Type v)]
    {L : Sheaf (J.over U) (Type v) ⥤ Sheaf J (Type v)} (adj : L ⊣ J.overPullback (Type v) U) :
    L.ReflectsMonomorphisms ∧ L.ReflectsEpimorphisms
```

## Tag 03EE, a lemma

[Tag 03EE](https://stacks.math.columbia.edu/tag/03EE) in the Stacks Project.

**`CategoryTheory.OverShriek.overShriek_overPullback_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/LowerShriekProduct.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/LowerShriekProduct.lean#L113).

> **Stacks 03EE**, packaged as the existence of the isomorphism
> `j_{U!}j_U^{-1}F ≅ F × h_U^#`.

```lean
theorem overShriek_overPullback_iso (F : Sheaf J (Type v)) :
    Nonempty
      (((Over.forget U).sheafPullback (Type v) (J.over U) J).obj
          ((J.overPullback (Type v) U).obj F) ≅
        F ⨯ (presheafToSheaf J (Type v)).obj (yoneda.obj U))
```

## Tag 03EH, a lemma

[Tag 03EH](https://stacks.math.columbia.edu/tag/03EH) in the Stacks Project.

**`comp_forget_eq_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/RelocalizationTriangle.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/RelocalizationTriangle.lean#L68). The attribute's comment: “triangle”. References: SGA 4 I (5.10), “commutative triangle”; SGA 3 I (1.6).

> Commutativity of the relocalization triangle: `j_U ∘ j = j_V`, i.e.
> `Over.map f ⋙ Over.forget U = Over.forget V`.

```lean
theorem comp_forget_eq_forget :
    Over.map f ⋙ Over.forget U = Over.forget V
```

**`map_eq_forget_iteratedSlice`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/RelocalizationTriangle.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/RelocalizationTriangle.lean#L89). The attribute's comment: “j = j\_\{V/U}”. References: SGA 3 I (1.6), “partial”.

> Under the identification `(C/U)/(V/U) ≅ C/V` given by
> `Over.iteratedSliceEquiv (Over.mk f)`, the relocalization functor
> `j = Over.map f` agrees with the localization functor
> `j_{V/U} = Over.forget (Over.mk f)`.

```lean
theorem map_eq_forget_iteratedSlice :
    (Over.iteratedSliceEquiv (Over.mk f)).functor ⋙ Over.map f =
      Over.forget (Over.mk f)
```

**`inverseImage_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/RelocalizationTriangle.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/RelocalizationTriangle.lean#L113). The attribute's comment: “j\_V^\{-1} = j^\{-1} ∘ j\_U^\{-1}”.

> (Inverse image, strict equality.)
> `j_V^{-1} = j^{-1} ∘ j_U^{-1}` as functors `Sheaf J A ⟶ Sheaf (J.over V) A`.
>
> This is the strict equality of `sheafPushforwardContinuous` functors, valid
> because the underlying functors satisfy `Over.map f ⋙ Over.forget U =
> Over.forget V` strictly.

```lean
theorem inverseImage_eq :
    (Over.forget V).sheafPushforwardContinuous A (J.over V) J =
      (Over.forget U).sheafPushforwardContinuous A (J.over U) J ⋙
        (Over.map f).sheafPushforwardContinuous A (J.over V) (J.over U)
```

**`leftAdjointIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/RelocalizationTriangle.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/RelocalizationTriangle.lean#L133). The attribute's comment: “j\_\{V!} = j\_\{U!} ∘ j\_!”.

> (Lower-shriek, natural isomorphism.)
> `j_{V!} ≅ j_{U!} ∘ j_!` as functors `Sheaf (J.over V) A ⟶ Sheaf J A`.
>
> Constructed from `inverseImage_eq` via uniqueness of left adjoints: each of
> `sheafPullback` is a chosen left adjoint to the corresponding
> `sheafPushforwardContinuous`, and the composition `j_!  ∘ j_U_!` is left
> adjoint to `j_U^{-1} ∘ j^{-1} = j_V^{-1}` by `inverseImage_eq`.

```lean
noncomputable def leftAdjointIso :
    (Over.forget V).sheafPullback A (J.over V) J ≅
      (Over.map f).sheafPullback A (J.over V) (J.over U) ⋙
        (Over.forget U).sheafPullback A (J.over U) J
```

**`leftAdjointIso_hom_app_comp_map_comp_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/RelocalizationTriangle.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/RelocalizationTriangle.lean#L169). The attribute's comment: “j\_\{V!} = j\_\{U!} ∘ j\_! carries one transpose to the other”.

> **Stacks 03EH carries one transpose to the other.**  A morphism `u : T ⟶ j_V^{-1}Z`
> transposes across `j_{V!} ⊣ j_V^{-1}` on the one hand and across `(j_! ∘ j_{U!}) ⊣ j_V^{-1}` on
> the other, and the two transposes differ by `leftAdjointIso`.
>
> This is what `leftAdjointIso` *means*: it is a `Adjunction.leftAdjointUniq`, so on its own it is
> only an isomorphism of two chosen left adjoints, and the statement that identifies it is the
> agreement of the transposes it induces.  It is also the only form in which the triangle can be
> used inside an equation of morphisms out of a lower shriek, where one side is written with
> `j_{V!}` and the other with `j_{U!} ∘ j_!`.
>
> `Adjunction.leftAdjointUniq_hom_app_counit` is the case `u = 𝟙`; the general case is that one
> followed by the naturality of `leftAdjointIso`.

```lean
theorem leftAdjointIso_hom_app_comp_map_comp_counit {T : Sheaf (J.over V) A} {Z : Sheaf J A}
    (u : T ⟶ ((Over.forget V).sheafPushforwardContinuous A (J.over V) J).obj Z) :
    ((Over.forget V).sheafPullback A (J.over V) J).map u ≫
        ((Over.forget V).sheafAdjunctionContinuous A (J.over V) J).counit.app Z =
      (leftAdjointIso J f A).hom.app T ≫
        ((Over.map f).sheafPullback A (J.over V) (J.over U) ⋙
            (Over.forget U).sheafPullback A (J.over U) J).map u ≫
          (((Over.map f).sheafAdjunctionContinuous A (J.over V) (J.over U)).comp
            ((Over.forget U).sheafAdjunctionContinuous A (J.over U) J)).counit.app Z
```

## Tag 04IL, a lemma

[Tag 04IL](https://stacks.math.columbia.edu/tag/04IL) in the Stacks Project.

**`CategoryTheory.OverShriek.shriekCompSheafFunctorToOverIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/Relocalize.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/Relocalize.lean#L355). The attribute's comment: “(2): under the identification of 00Y1, j\_! is postcomposition with h\_f^#”.

> **Stacks 04IL (2).**  Under the identification of Stacks 00Y1, used in the forward direction
> `Φ_U = sheafFunctorToOver J : Sh(C/U) ⥤ Sh(C)/h_U^#`, the relocalization lower shriek `j_!` becomes
> postcomposition with `h_f^# : h_V^# ⟶ h_U^#`:
> ```
>   j_!(H --φ--> h_V^#) = (H --φ ≫ h_f^#--> h_U^#) .
> ```
>
> This is Stacks' proof of (2): the identification sends `G` to `j_{V!}G ⟶ j_{V!}(*) = h_V^#`, so
> `j_!G` is sent to `j_{U!}j_!G ⟶ j_{U!}(*) = h_U^#`, and `j_{U!}j_! = j_{V!}` — carried out here at
> the presheaf level, where the two structural maps to `h_U` are literally the same
> (`relocalizePresheafFunctorToOverIso`), and then transported through sheafification.

```lean
def shriekCompSheafFunctorToOverIso :
    (Over.map f).sheafPullback (Type v) (J.over V) (J.over U) ⋙ sheafFunctorToOver (U := U) J ≅
      sheafFunctorToOver (U := V) J ⋙
        Over.map ((presheafToSheaf J (Type v)).map (yoneda.map f))
```

**`CategoryTheory.OverShriek.inverseImageCompSheafFunctorToOverIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/Relocalize.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/Relocalize.lean#L400). The attribute's comment: “(1): under the identification of 00Y1, j^\{-1} is base change along h\_f^#”.

> **Stacks 04IL (1).**  Under the identification of Stacks 00Y1, used in the forward direction
> `Φ_U = sheafFunctorToOver J`, the relocalization inverse image `j^{-1}` becomes base change along
> `h_f^# : h_V^# ⟶ h_U^#`:
> ```
>   j^{-1}(H --φ--> h_U^#) = (H ×_{φ, h_U^#, h_f^#} h_V^# ⟶ h_V^#) .
> ```
>
> This is the proof Stacks suggests: "the reader can now prove (1) by using that `j^{-1}` is the
> right adjoint to `j_!` and using that the rule in (1) is the right adjoint to the rule in (2)".
> Concretely, `Over.map h_f^# ⋙ Φ_U^{-1}` — which is `j_!` transported, by (2) — is left adjoint both
> to `j^{-1} ⋙ Φ_V` and to `Φ_U ⋙ Over.pullback h_f^#`, so the two agree by uniqueness of right
> adjoints.

```lean
def inverseImageCompSheafFunctorToOverIso :
    (Over.map f).sheafPushforwardContinuous (Type v) (J.over V) (J.over U) ⋙
        sheafFunctorToOver (U := V) J ≅
      sheafFunctorToOver (U := U) J ⋙
        Over.pullback ((presheafToSheaf J (Type v)).map (yoneda.map f))
```

**`CategoryTheory.OverShriek.homEquiv_symm_inverseImageCompSheafFunctorToOverIso_inv_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/Relocalize.lean, line 427](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/Relocalize.lean#L427). The attribute's comment: “(1): the comparison of inverse images is the one its counit prescribes”.

> **Stacks 04IL (1) is the comparison its counit prescribes.**  Transposing the inverse of the
> comparison across the adjunction `Φ_V^{-1} ⋙ j_! ⊣ j^{-1} ⋙ Φ_V` — the one whose left adjoint
> Stacks 04IL (2) identifies with `Over.map h_f^# ⋙ Φ_U^{-1}` — returns, up to that identification,
> the counit of base change along `h_f^#` read through Stacks 00Y1 at `U`.
>
> Both sides are morphisms out of `Φ_V^{-1}(Φ_U(j^{-1}... ) ×_{h_U^#} h_V^#)`, and the comparison is
> an `Adjunction.rightAdjointUniq`, so this is `Adjunction.homEquiv_symm_rightAdjointUniq_hom_app`
> for the two adjunctions it is built from, read in the inverse direction by
> `Adjunction.rightAdjointUniq_inv_app` and corrected by `Adjunction.ofNatIsoLeft` for the
> identification of the two left adjoints.
>
> This is the form in which the comparison enters an equation that has been transposed across a
> lower shriek: on one side of such an equation the base change of Stacks 03EH appears, on the
> other the relocalization counit, and nothing but this lemma relates them.

```lean
theorem homEquiv_symm_inverseImageCompSheafFunctorToOverIso_inv_app
    (Z : Sheaf (J.over U) (Type v)) :
    (((sheafEquivalence (U := V) J).symm.toAdjunction.comp
          ((Over.map f).sheafAdjunctionContinuous (Type v) (J.over V) (J.over U))).homEquiv
        ((sheafFunctorToOver (U := U) J ⋙
          Over.pullback ((presheafToSheaf J (Type v)).map (yoneda.map f))).obj Z) Z).symm
        ((inverseImageCompSheafFunctorToOverIso f J).inv.app Z) =
      (inverseCompShriekRelocalizeIso f J).hom.app
          ((sheafFunctorToOver (U := U) J ⋙
            Over.pullback ((presheafToSheaf J (Type v)).map (yoneda.map f))).obj Z) ≫
        ((Over.mapPullbackAdj ((presheafToSheaf J (Type v)).map (yoneda.map f))).comp
          (sheafEquivalence (U := U) J).symm.toAdjunction).counit.app Z
```

**`CategoryTheory.OverShriek.left_inverseImageCompSheafFunctorToOverIso_inv_app_comp_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/RelocalizeCounit.lean, line 848](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/RelocalizeCounit.lean#L848). The attribute's comment: “(1) carries the counit of j\_\{V!} to the counit of j\_\{U!}”.

> **Stacks 04IL (1) carries the counit of `j_{V!} ⊣ j_V^{-1}` to that of
> `j_{U!} ⊣ j_U^{-1}`.**  The inverse of Stacks 04IL (1) at a restricted sheaf `j_U^{-1}A`, read
> through `Over.forget h_V^#` and followed by Stacks 00Y1's identification at `V` and the counit
> `ε^V`, is the first projection of the base change along `h_f^#` followed by Stacks 00Y1's
> identification at `U` and the counit `ε^U`.
>
> The two counits belong to two different localizations of the site, and Stacks 04IL (1) is what
> relates them.

```lean
theorem left_inverseImageCompSheafFunctorToOverIso_inv_app_comp_counit
    (A : Sheaf J (Type v)) :
    ((inverseImageCompSheafFunctorToOverIso f J).inv.app
            ((J.overPullback (Type v) U).obj A)).left ≫
        (sheafFunctorToOverForgetIso (U := V) J).hom.app ((J.overPullback (Type v) V).obj A) ≫
          ((Over.forget V).sheafAdjunctionContinuous (Type v) (J.over V) J).counit.app A =
      pullback.fst
            ((sheafFunctorToOver (U := U) J).obj ((J.overPullback (Type v) U).obj A)).hom
            ((presheafToSheaf J (Type v)).map (yoneda.map f)) ≫
          (sheafFunctorToOverForgetIso (U := U) J).hom.app ((J.overPullback (Type v) U).obj A) ≫
            ((Over.forget U).sheafAdjunctionContinuous (Type v) (J.over U) J).counit.app A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.25, Tag 00XZ](https://stacks.math.columbia.edu/tag/00XZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
