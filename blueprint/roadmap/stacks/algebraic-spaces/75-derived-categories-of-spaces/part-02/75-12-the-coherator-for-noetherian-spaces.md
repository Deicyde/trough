---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_filtered_colimit_pushforwards_artinian, AlgebraicGeometry.Space.exists_filtered_colimit_artinian_pushforwards_retract_of_isNoetherian, AlgebraicGeometry.Space.injective_quasicoherentPushforward_obj_of_isFlat, AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_injective_isNoetherian, AlgebraicGeometry.Space.isZero_etaleRestrictionCohomology_of_injective_of_isNoetherian, AlgebraicGeometry.Space.exists_quasicoherentPushforwardExtension_comparison, AlgebraicGeometry.Space.quasicoherentDerivedComparison_isEquivalence_of_isNoetherian, AlgebraicGeometry.Space.exists_equivalence_functor_eq_and_inverse_eq_derivedCoherator_of_isNoetherian
statement: formalized
proof: formalized
---

# 75.12 The coherator for Noetherian spaces

Section 75.12 of the Stacks Project, [Tag 09TH](https://stacks.math.columbia.edu/tag/09TH). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09TI, a lemma

[Tag 09TI](https://stacks.math.columbia.edu/tag/09TI) in the Stacks Project.

**`AlgebraicGeometry.exists_filtered_colimit_pushforwards_artinian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/InjectiveQcoh/ArtinianPushforwardColimit.lean, line 735](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/InjectiveQcoh/ArtinianPushforwardColimit.lean#L735).

> **Stacks Project, Tag 09TI.** An injective quasi-coherent module on a
> Noetherian affine scheme is a filtered colimit of pushforwards of coherent
> modules from Artinian affine schemes.

```lean
public theorem exists_filtered_colimit_pushforwards_artinian
    (S : Scheme.{u}) [IsAffine S] [IsLocallyNoetherian S]
    (J : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory)
    [Injective J] :
    ∃ (I : Type u) (inst : SmallCategory I),
      letI := inst
      ∃ (_ : IsFiltered I)
        (D : I ⥤ (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory)
        (φ : D ⟶ (Functor.const I).obj J),
        (∀ i, ∃ (R : CommRingCat.{u}) (hR : IsArtinianRing R),
          letI := hR
          ∃ (f : Spec R ⟶ S) (G : (Spec R).Modules),
            G.IsCoherent ∧
              Nonempty ((D.obj i).obj ≅ (Scheme.Modules.pushforward f).obj G)) ∧
          Nonempty (IsColimit (Cocone.mk J φ))
```

## Tag 09TJ, a lemma

[Tag 09TJ](https://stacks.math.columbia.edu/tag/09TJ) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_filtered_colimit_artinian_pushforwards_retract_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/InjectiveQcoh/UnconditionalArtinianPresentation.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/InjectiveQcoh/UnconditionalArtinianPresentation.lean#L114). The attribute's comment: “Over an arbitrary base scheme `S`, which generalizes the affine base of the source. The containment `hZ` of the terminal scheme in the big fppf site is the site condition under which the absolute quasi-separatedness in `IsNoetherian` is phrased. Direct summand is `CategoryTheory.Retract`, and the colimit is a cocone with a colimit proof.”.

> **Stacks 09TJ.**  Let `X` be a Noetherian algebraic space over a scheme `S` of a big fppf
> site.  Every injective object `J` of the category `QCoh(𝒪_X)` of quasi-coherent modules on the
> small étale site of `X` is a direct summand — a retract — of a filtered colimit of quasi-coherent
> modules `(Z_i ⟶ X)_*𝒢_i` with `Z_i` the spectrum of an Artinian ring and `𝒢_i` coherent on
> `Z_i`.
>
> The proof is the source's: `J` is a retract of `j_*J'` for an injective `J'` of `QCoh(𝒪_U)` at
> the affine surjective étale chart `j : U ⟶ X` of Stacks 03H6, and `J'` is a filtered colimit of
> Artinian direct images over `U` by Stacks 09TI at the chart.  The chart reduction is
> `AlgebraicGeometry.Space.exists_filtered_colimit_artinian_pushforwards_retract`; its inputs at the
> chart are all proved, by `AlgebraicGeometry.Space.chartArtinianPresentation_of_isAffine` and
> `AlgebraicGeometry.Space.preservesFilteredColimitsOfSize_chartQuasicoherentPushforward_of_isAffine`.
>
> The base scheme `S` is arbitrary, which generalizes the affine base of the source.  The
> hypothesis `hZ`, that the site contains the terminal scheme, is the site condition under which
> the quasi-separatedness in the definition `AlgebraicGeometry.Space.IsNoetherian` of a Noetherian
> algebraic space is phrased.

```lean
theorem exists_filtered_colimit_artinian_pushforwards_retract_of_isNoetherian
    (hZ : B.Contains (⊤_ Scheme.{u})) (X : AlgebraicSpaces B S hS)
    (hX : IsNoetherian B S hS hZ X.1)
    (J : QuasicoherentSheaves.{u, u} B S hS X.1 X.2) [Injective J] :
    ∃ (I : Type u) (inst : SmallCategory I),
      letI := inst
      ∃ (_ : IsFiltered I) (D : I ⥤ QuasicoherentSheaves.{u, u} B S hS X.1 X.2)
        (c : Cocone D),
        (∀ i, IsArtinianPushforward B S hS X (D.obj i).obj) ∧
          Nonempty (IsColimit c) ∧ Nonempty (Retract J c.pt)
```

## Tag 09TK, a lemma

[Tag 09TK](https://stacks.math.columbia.edu/tag/09TK) in the Stacks Project.

**`AlgebraicGeometry.Space.injective_quasicoherentPushforward_obj_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InjectiveQuasicoherentPushforwardOfFlat.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/InjectiveQuasicoherentPushforwardOfFlat.lean#L112).

> **Stacks 09TK.**  Let `f : X ⟶ Y` be a flat, quasi-compact and quasi-separated morphism of
> algebraic spaces over `S`.  If `J` is an injective object of `QCoh(𝒪_X)`, then `f_*J` is an
> injective object of `QCoh(𝒪_Y)`.
>
> Since `f` is quasi-compact and quasi-separated, `f_*` preserves quasi-coherence (Stacks 03M9);
> its left adjoint `f^*` transforms injections into injections because `f` is flat, so the
> criterion of Stacks 015Z applies.

```lean
theorem injective_quasicoherentPushforward_obj_of_isFlat (f : X ⟶ Y)
    (hf : IsFlat B S hS f.hom) (hfqc : IsQuasiCompact B S hS f.hom)
    (hfqs : IsQuasiSeparated B S hS f.hom)
    (J : QuasicoherentSheaves.{u, u} B S hS X.1 X.2) [Injective J] :
    Injective ((quasicoherentPushforward B S hS f
      (pushforwardPreservesQuasicoherence_of_qcqs B S hS f hfqc hfqs)).obj J)
```

## Tag 09TL, a lemma

[Tag 09TL](https://stacks.math.columbia.edu/tag/09TL) in the Stacks Project.

**`AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_injective_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/InjectiveQcoh/ChartLocalHigherDirectImage.lean, line 343](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/InjectiveQcoh/ChartLocalHigherDirectImage.lean#L343). The attribute's comment: “part (2)”.

> **Stacks 09TL, part (2).**  Let `X` be a Noetherian algebraic space over a scheme `S`, let
> `𝒥` be an injective object of `QCoh(𝒪_X)` and let `f : X ⟶ Y` be a morphism of algebraic spaces
> with `Y` quasi-separated.  Then `R^p f_*𝒥 = 0` for `p > 0`.
>
> This is
> `AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_injective_of_isNoetherian`
> with its input `hdetect` discharged by
> `AlgebraicGeometry.Space.chartLocalCohomologyDetectsHigherDirectImage`.

```lean
theorem isZero_rightDerived_modulePushforward_injective_isNoetherian
    (hZ : B.Contains (⊤_ Scheme.{u})) {X Y : AlgebraicSpaces B S hS}
    (hX : IsNoetherian B S hS hZ X.1)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS hZ Y.1)
    (J : QuasicoherentSheaves.{u, u} B S hS X.1 X.2) [Injective J]
    (f : X ⟶ Y) (p : ℕ) (hp : 0 < p) :
    IsZero (((modulePushforward B S hS f).rightDerived p).obj J.obj)
```

**`AlgebraicGeometry.Space.isZero_etaleRestrictionCohomology_of_injective_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/InjectiveQcoh/UnconditionalArtinianPresentation.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/InjectiveQcoh/UnconditionalArtinianPresentation.lean#L137). The attribute's comment: “part (1)”.

> **Stacks 09TL, part (1).**  Let `X` be a Noetherian algebraic space over a scheme `S` of a
> big fppf site and let `𝒥` be an injective object of `QCoh(𝒪_X)`.  Then `H^p(U, 𝒥|_U) = 0` for
> `p > 0` and every quasi-compact and quasi-separated algebraic space `U` étale over `X`.

```lean
theorem isZero_etaleRestrictionCohomology_of_injective_of_isNoetherian
    (hZ : B.Contains (⊤_ Scheme.{u})) {X U : AlgebraicSpaces B S hS}
    (hX : IsNoetherian B S hS hZ X.1)
    (J : QuasicoherentSheaves.{u, u} B S hS X.1 X.2) [Injective J]
    (g : U ⟶ X) (hg : IsEtale B S hS g.hom)
    (hUqc : IsQuasiCompactSpace B S hS U.1)
    (hUqs : IsAbsolutelyQuasiSeparated B S hS hZ U.1)
    (p : ℕ) (hp : 0 < p) :
    IsZero ((etaleRestrictionCohomology B S hS g hg p).obj J)
```

## Tag 09TM, a lemma

[Tag 09TM](https://stacks.math.columbia.edu/tag/09TM) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_quasicoherentPushforwardExtension_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianCoherator/NoetherianExtension.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianCoherator/NoetherianExtension.lean#L122).

> **Stacks 09TM.**  Let `f : X ⟶ Y` be a morphism of Noetherian algebraic spaces over `S`.
> Then `f_*` on quasi-coherent modules has a right derived extension
> `Φ : D(QCoh(𝒪_X)) ⥤ D(QCoh(𝒪_Y))` — the total right derived functor
> `AlgebraicGeometry.Space.quasicoherentPushforwardExtension` of `f_* : QCoh(𝒪_X) ⥤ QCoh(𝒪_Y)`,
> with derivation unit `AlgebraicGeometry.Space.quasicoherentPushforwardExtensionUnit` — such that
> the square formed with the comparison functors `D(QCoh) ⥤ D_QCoh` of Stacks 08F1 and with `Rf_*`
> commutes: for every right derived functor `Rf_*` of the direct image of all modules, the two
> composites `D(QCoh(𝒪_X)) ⥤ D_QCoh(𝒪_Y) ⊆ D(𝒪_Y)` are isomorphic.

```lean
theorem exists_quasicoherentPushforwardExtension_comparison (hZ : B.Contains (⊤_ Scheme.{u}))
    {X Y : AlgebraicSpaces B S hS} (hX : IsNoetherian B S hS hZ X.1)
    (hY : IsNoetherian B S hS hZ Y.1) (f : X ⟶ Y) :
    ∃ hpush : PushforwardPreservesQuasicoherence B S hS f,
      (quasicoherentPushforwardExtension B S hS f hpush).IsRightDerivedFunctor
          (quasicoherentPushforwardExtensionUnit B S hS f hpush)
          (HomotopyCategory.quasiIso (QuasicoherentSheaves.{u, u} B S hS X.1 X.2)
            (ComplexShape.up ℤ)) ∧
        ∀ (RF : DerivedCategory (Modules.{u, u} B S hS X.1 X.2) ⥤
            DerivedCategory (Modules.{u, u} B S hS Y.1 Y.2))
          (α : (modulePushforward B S hS f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
            DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF),
          RF.IsRightDerivedFunctor α
              (HomotopyCategory.quasiIso (Modules.{u, u} B S hS X.1 X.2) (ComplexShape.up ℤ)) →
            Nonempty (quasicoherentDerivedComparisonSchemeUniverse B S hS X.1 X.2 ⋙
                (DerivedCategoryB.derivedCategoryB
                  (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
                    (Stacks.SheafOfModules.Tensor.ringSheaf
                      (smallEtaleRingedSite B S hS X.1 X.2).O))).ι ⋙ RF ≅
              quasicoherentPushforwardExtension B S hS f hpush ⋙
                quasicoherentDerivedComparisonSchemeUniverse B S hS Y.1 Y.2 ⋙
                  (DerivedCategoryB.derivedCategoryB
                    (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
                      (Stacks.SheafOfModules.Tensor.ringSheaf
                        (smallEtaleRingedSite B S hS Y.1 Y.2).O))).ι)
```

## Tag 09TN, a proposition

[Tag 09TN](https://stacks.math.columbia.edu/tag/09TN) in the Stacks Project.

**`AlgebraicGeometry.Space.quasicoherentDerivedComparison_isEquivalence_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/NoetherianDerivedCoheratorEquivalence.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/NoetherianDerivedCoheratorEquivalence.lean#L116). The attribute's comment: “equivalence”.

> **[Stacks, Tag 09TN], the equivalence.**  Let `X` be a Noetherian algebraic space over `S`.
> Then the comparison functor `i_X : D(QCoh(𝒪_X)) ⥤ D_QCoh(𝒪_X)` of Stacks 08F1 is an
> equivalence.

```lean
theorem quasicoherentDerivedComparison_isEquivalence_of_isNoetherian :
    (quasicoherentDerivedComparison B S hS X.1 X.2).IsEquivalence
```

**`AlgebraicGeometry.Space.exists_equivalence_functor_eq_and_inverse_eq_derivedCoherator_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/NoetherianDerivedCoheratorEquivalence.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/NoetherianDerivedCoheratorEquivalence.lean#L202). The attribute's comment: “equivalence with quasi-inverse RQ\_X”.

> **[Stacks, Tag 09TN].**  Let `X` be a Noetherian algebraic space over `S`, `C_X` a coherator
> of `X` and `RQ_X` a total right derived functor of it.  Then the comparison functor
> `i_X : D(QCoh(𝒪_X)) ⥤ D_QCoh(𝒪_X)` of Stacks 08F1 is an equivalence with quasi-inverse `RQ_X`
> restricted to `D_QCoh(𝒪_X)`: there is an equivalence whose functor is `i_X` and whose inverse is
> `J ⋙ RQ_X`, for `J : D_QCoh(𝒪_X) ⥤ D(𝒪_X)` the inclusion.

```lean
theorem exists_equivalence_functor_eq_and_inverse_eq_derivedCoherator_of_isNoetherian
    (X : AlgebraicSpaces B S hS) (hN : IsNoetherian B S hS hZ X.1)
    (CF : Modules.{u, u} B S hS X.1 X.2 ⥤ QuasicoherentSheaves.{u, u} B S hS X.1 X.2)
    (adjF : (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))).ι ⊣ CF)
    (RQ : DerivedCategory (Modules.{u, u} B S hS X.1 X.2) ⥤
      DerivedCategory (QuasicoherentSheaves.{u, u} B S hS X.1 X.2))
    (RQUnit : letI := adjF.right_adjoint_additive
      CF.mapHomologicalComplex (ComplexShape.up ℤ) ⋙
        DerivedCategory.Q (C := QuasicoherentSheaves.{u, u} B S hS X.1 X.2) ⟶
      DerivedCategory.Q (C := Modules.{u, u} B S hS X.1 X.2) ⋙ RQ)
    (hRQ : letI := adjF.right_adjoint_additive
      RQ.IsRightDerivedFunctor RQUnit
        (HomologicalComplex.quasiIso (Modules.{u, u} B S hS X.1 X.2) (ComplexShape.up ℤ))) :
    ∃ e : DerivedCategory (QuasicoherentSheaves.{u, u} B S hS X.1 X.2) ≌
        QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2,
      e.functor = quasicoherentDerivedComparison B S hS X.1 X.2 ∧
        e.inverse =
          (DerivedCategoryB.derivedCategoryB
            (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
              ((Stacks.SheafOfModules.Tensor.ringSheaf
                (smallEtaleRingedSite B S hS X.1 X.2).O)))).ι ⋙ RQ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.12, Tag 09TH](https://stacks.math.columbia.edu/tag/09TH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
