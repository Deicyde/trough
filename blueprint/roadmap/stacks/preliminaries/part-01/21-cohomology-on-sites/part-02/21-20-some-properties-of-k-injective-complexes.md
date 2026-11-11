---
declaration: section
origin: cited
lean: Stacks.Cohomology.Localization.isKInjective_overMap, Stacks.Cohomology.Localization.isKInjective_over, Stacks.Cohomology.Localization.cohomologyOverObjectIsoRestriction, Stacks.Cohomology.SiteCohomologyPresheaf.sheafificationCohomologyPresheafIso, Stacks.Cohomology.SiteCohomologyPresheaf.sheafificationCohomologyPresheafIso_comp, Stacks.Cohomology.SiteCohomologyPresheaf.cohomologyPresheafEvaluationIso, Stacks.Cohomology.SiteCohomologyPresheaf.cohomologyPresheafEvaluationIso_naturality, Stacks.Cohomology.SiteCohomologyPresheaf.cohomologyPresheafSliceIso
statement: formalized
proof: formalized
---

# 21.20 Some properties of K-injective complexes

Section 21.20 of the Stacks Project, [Tag 08FH](https://stacks.math.columbia.edu/tag/08FH). 11 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08FI, a lemma

[Tag 08FI](https://stacks.math.columbia.edu/tag/08FI) in the Stacks Project.

**`Stacks.Cohomology.Localization.isKInjective_overMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/KInjectiveRestrictionAlongOverMap.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/KInjectiveRestrictionAlongOverMap.lean#L118). The attribute's comment: “for the restriction between two slices, along `Over.map`”.

> **Stacks 08FI for the slice-to-slice restriction.** Restriction of sheaves of modules along
> `Over.map f`, for an arrow `f : V ⟶ U` of the site, carries K-injective complexes to K-injective
> complexes.
>
> Restriction along `Over.map f` is restriction to the slice of `C/U` at `Over.mk f` followed by the
> transport of that iterated slice to `C/V`. The first preserves K-injectivity by the library's form of
> Stacks 08FI for `SheafOfModules.overFunctor`, extension by zero being an exact left adjoint of it,
> and the second by `isKInjective_sliceBackward`.

```lean
theorem isKInjective_overMap
    (I : CochainComplex (SheafOfModules.{u} (O.over U)) ℤ) [I.IsKInjective] :
    CochainComplex.IsKInjective
      ((((_root_.SheafOfModules.overMap.{u} O f)).mapHomologicalComplex
        (ComplexShape.up ℤ)).obj I)
```

**`Stacks.Cohomology.Localization.isKInjective_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/RestrictionOfModules.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/RestrictionOfModules.lean#L111).

> **Stacks 08FI.** Restriction to the slice site over an object preserves K-injective
> complexes of sheaves of modules. Extension by zero is an exact left adjoint of the restriction,
> so the adjoint criterion for K-injectivity applies.

```lean
theorem isKInjective_over {C : Type u} [Category.{u} C]
    (J : GrothendieckTopology C) (R : Sheaf J RingCat.{u}) (U : C)
    (I : CochainComplex (SheafOfModules.{u} R) ℤ) [I.IsKInjective] :
    CochainComplex.IsKInjective
      (((SheafOfModules.overFunctor.{u} R U).mapHomologicalComplex
        (ComplexShape.up ℤ)).obj I)
```

## Tag 0D6F, a lemma

[Tag 0D6F](https://stacks.math.columbia.edu/tag/0D6F) in the Stacks Project.

**`Stacks.Cohomology.Localization.cohomologyOverObjectIsoRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/RestrictionOfModules.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/RestrictionOfModules.lean#L364).

> Cohomology over `U` agrees naturally with cohomology of the restricted
> derived module on the slice site `C/U`.

```lean
noncomputable def cohomologyOverObjectIsoRestriction
    (X : RingedSite.{u, u, u}) (U : X.C)
    [HasDerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))]
    [HasDerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U))]
    [HasDerivedCategory AddCommGrpCat.{u}] (p : ℤ) :
    derivedSectionsOverObject X U ⋙ DerivedCategory.homologyFunctor AddCommGrpCat.{u} p ≅
    derivedRestriction X U ⋙ derivedSectionsOnSlice X U ⋙
        DerivedCategory.homologyFunctor AddCommGrpCat.{u} p
```

## Tag 0BKV, a lemma

[Tag 0BKV](https://stacks.math.columbia.edu/tag/0BKV) in the Stacks Project.

**`Stacks.Cohomology.SiteCohomologyPresheaf.sheafificationCohomologyPresheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/SheafificationOfTheCohomologyPresheaf.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/SheafificationOfTheCohomologyPresheaf.lean#L293). The attribute's comment: “associated sheaf”.

> Sheafifying the presheaf `U ↦ H^q(U, K)` gives the `q`-th cohomology sheaf of `K`,
> naturally in the derived object `K`.

```lean
def sheafificationCohomologyPresheafIso (q : ℤ) :
    derivedSectionsPresheaf X ⋙
          DerivedCategory.homologyFunctor (PresheafOfModules.{w}
            (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj) q ⋙
          PresheafOfModules.sheafification (𝟙 (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj) ≅
        DerivedCategory.homologyFunctor (SheafOfModules.{w}
          (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) q
```

**`Stacks.Cohomology.SiteCohomologyPresheaf.sheafificationCohomologyPresheafIso_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/SheafificationOfTheCohomologyPresheaf.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/SheafificationOfTheCohomologyPresheaf.lean#L320). The attribute's comment: “canonical comparison”.

> Characterization of the associated-sheaf isomorphism: on a complex, it agrees with the
> canonical exact-sheafification comparison after the unit of the total right derived
> presheaf-sections functor.

```lean
theorem sheafificationCohomologyPresheafIso_comp (q : ℤ)
    (I : HomotopyCategory (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
      (.up ℤ)) :
    (DerivedCategory.homologyFunctor (PresheafOfModules.{w}
      (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj) q ⋙
        PresheafOfModules.sheafification (𝟙 (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj)).map
        (((homotopySectionsPresheaf X).totalRightDerivedUnit DerivedCategory.Qh
          (HomotopyCategory.quasiIso (SheafOfModules.{w}
            (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) (.up ℤ))).app I) ≫
      (sheafificationCohomologyPresheafIso X q).hom.app (DerivedCategory.Qh.obj I) =
        (homotopySheafificationHomologyIso X q).hom.app I ≫
          (DerivedCategory.homologyFunctorFactorsh
            (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) q).inv.app I
```

**`Stacks.Cohomology.SiteCohomologyPresheaf.cohomologyPresheafEvaluationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/SheafificationOfTheCohomologyPresheaf.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/SheafificationOfTheCohomologyPresheaf.lean#L402). The attribute's comment: “values on objects”.

> Evaluation of the hypercohomology presheaf at `U` is the established cohomology functor
> `H^q(U, -)`.

```lean
public def cohomologyPresheafEvaluationIso (X : RingedSite.{u, u, u}) (U : X.C) (q : ℤ) :
    derivedSectionsPresheaf X ⋙
        DerivedCategory.homologyFunctor (PresheafOfModules.{u}
          (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj) q ⋙
        PresheafOfModules.evaluation (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj
          (Opposite.op U) ⋙
        forget₂ (ModuleCat.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj.obj
          (Opposite.op U))) AddCommGrpCat.{u} ≅
      derivedSectionsOverObject X U ⋙
        DerivedCategory.homologyFunctor AddCommGrpCat.{u} q
```

**`Stacks.Cohomology.SiteCohomologyPresheaf.cohomologyPresheafEvaluationIso_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/SheafificationOfTheCohomologyPresheaf.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/SheafificationOfTheCohomologyPresheaf.lean#L435). The attribute's comment: “restriction maps”.

> The evaluation identifications commute with the restriction maps.

```lean
public theorem cohomologyPresheafEvaluationIso_naturality (X : RingedSite.{u, u, u})
    {U V : X.C} (g : U ⟶ V)
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
      (q : ℤ) :
    (cohomologyPresheaf X K q).presheaf.map g.op ≫
        (cohomologyPresheafEvaluationIso X U q).hom.app K =
      (cohomologyPresheafEvaluationIso X V q).hom.app K ≫
        (hypercohomologyRestriction X g q).app K
```

**`Stacks.Cohomology.SiteCohomologyPresheaf.cohomologyPresheafSliceIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/SheafificationOfTheCohomologyPresheaf.lean, line 497](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/SheafificationOfTheCohomologyPresheaf.lean#L497). The attribute's comment: “cohomology on the slice site”.

> The same evaluation, expressed using cohomology on the localized site `C/U`; its second
> factor is the comparison of Tag 0D6F.

```lean
public def cohomologyPresheafSliceIso (X : RingedSite.{u, u, u}) (U : X.C) (q : ℤ) :
    derivedSectionsPresheaf X ⋙
        DerivedCategory.homologyFunctor (PresheafOfModules.{u}
          (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj) q ⋙
        PresheafOfModules.evaluation (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj
          (Opposite.op U) ⋙
        forget₂ (ModuleCat.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj.obj
          (Opposite.op U))) AddCommGrpCat.{u} ≅
      derivedRestriction X U ⋙ derivedSectionsOnSlice X U ⋙
        DerivedCategory.homologyFunctor AddCommGrpCat.{u} q
```

## Tag 0D6G, a lemma

[Tag 0D6G](https://stacks.math.columbia.edu/tag/0D6G) in the Stacks Project.

**`Stacks.Cohomology.Localization.derivedPushforwardOverFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/DerivedDirectImageAndRestriction.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/DerivedDirectImageAndRestriction.lean#L377).

> **Stacks 0D6G.** For a morphism of ringed sites `f : (C, O_C) ⟶ (D, O_D)` given by the
> continuous functor `u : D ⥤ C`, an object `V` of `D` and `U = u(V)`, restricting the unbounded
> derived direct image `Rf_*` to the localized site `D/V` is the derived direct image `Rg_*` along
> the localized morphism `g : (C/U, O_U) ⟶ (D/V, O_V)` of Stacks 04J0 of the restriction to
> `C/U`.

```lean
noncomputable def derivedPushforwardOverFunctorIso :
    derivedPushforward.{u} f.toRingedToposSiteHom ⋙ derivedRestriction Y V ≅
      derivedRestriction X (f.u.obj V) ⋙ derivedLocalizedPushforward f V
```

## Tag 0D6H, a lemma

[Tag 0D6H](https://stacks.math.columbia.edu/tag/0D6H) in the Stacks Project.

**`Stacks.Cohomology.LerayUnbounded.derivedGlobalSectionsPushforwardIsoGeneral`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/LerayForUnboundedGlobalSectionsGeneral.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/LerayForUnboundedGlobalSectionsGeneral.lean#L282). The attribute's comment: “the clause on global sections, as functors into the derived category of modules over the global sections of the structure sheaf of the target, for an arbitrary morphism of ringed sites; the clause on sections over an object of the target site is derivedSectionsOverObjectPushforwardIsoGeneral”.

> **Stacks 0D6H, the global-sections clause, for an arbitrary morphism of ringed sites.** Let
> `f : (C, O_C) ⟶ (D, O_D)` be a morphism of ringed sites given by the continuous functor
> `u : D ⥤ C`. Then `RΓ(D, -) ∘ Rf_* = RΓ(C, -)` as functors `D(O_C) ⟶ D(Γ(O_D))`, the right hand
> side being the derived global sections on `C` with scalars restricted along the induced ring map
> `Γ(O_D) ⟶ Γ(O_C)`.
>
> No flatness: this is `derivedGlobalSectionsPushforwardIso` with its hypothesis discharged by
> `computesSecond_pushforwardTopos_globalSections`. The source's other clause, the one on sections
> over an object of `D`, is
> `Stacks.Cohomology.LerayUnbounded.derivedSectionsOverObjectPushforwardIsoGeneral`.

```lean
noncomputable def derivedGlobalSectionsPushforwardIsoGeneral :
    derivedPushforward.{u} f.toRingedToposSiteHom ⋙ derivedGlobalSections Y ≅
      derivedGlobalSectionsRestricted f
```

**`Stacks.Cohomology.LerayUnbounded.derivedSectionsOverObjectPushforwardIsoGeneral`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/LerayForUnboundedSectionsGeneral.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/LerayForUnboundedSectionsGeneral.lean#L256). The attribute's comment: “the clause on sections over an object of the target site, for an arbitrary morphism of ringed sites; the clause on global sections into the derived category of modules over the global sections of the structure sheaf of the target is derivedGlobalSectionsPushforwardIsoGeneral”.

> **Stacks 0D6H, the clause on sections over an object, for an arbitrary morphism of ringed
> sites.** Let `f : (C, O_C) ⟶ (D, O_D)` be a morphism of ringed sites given by the continuous
> functor `u : D ⥤ C`, let `V` be an object of `D` and put `U = u(V)`. Then
> `RΓ(V, -) ∘ Rf_* = RΓ(U, -)` as functors `D(O_C) ⟶ D(Ab)`.
>
> No flatness: this is `derivedSectionsOverObjectPushforwardIso` with its hypothesis discharged by
> `computesSecond_pushforwardTopos_sectionsOverObject`. The source's other clause, the one about
> global sections into `D(Γ(O_D))`, is
> `Stacks.Cohomology.LerayUnbounded.derivedGlobalSectionsPushforwardIsoGeneral`.

```lean
noncomputable def derivedSectionsOverObjectPushforwardIsoGeneral :
    derivedPushforward.{u} f.toRingedToposSiteHom ⋙ derivedSectionsOverObject Y V ≅
      derivedSectionsOverObject X (f.u.obj V)
```

**`Stacks.Cohomology.Localization.derivedGlobalSectionsOverPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/LerayForTheSliceMorphism.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/LerayForTheSliceMorphism.lean#L140). The attribute's comment: “the clause `RGamma(V, -) . Rf_* = RGamma(U, -)` on sections over an object, for ABELIAN sheaves and for the SLICE morphism of topoi `Sh(C/X) -> Sh(C/Y)` of a morphism `f : X -> Y` of the site, at the final object `V = id Y` of `C/Y`, where `u = Over.pullback f` and `u(V) = id X`. Unconditional: no analogue of the `h093Y` K-injectivity hypothesis, nor of the flatness, of `Stacks.Cohomology.LerayUnbounded.derivedSectionsOverObjectPushforwardIso` and `...IsoOfFlat`, which carry this tag for sheaves of MODULES on ringed sites. Assumed instead is `Limits.HasPullbacksAlong f`, base change of the single morphism `f`, used only to present `f_*` as restriction along `Over.pullback f`. NOT covered: the clause on global sections into `D(Gamma(O_D))` for a general morphism of ringed sites, and sections over a non-final object of `C/Y`”.

> **Stacks 0D6H for the slice morphism, on abelian sheaves.** For a morphism `f : X ⟶ Y` of a
> site `C`, the unbounded derived global sections on `C/Y` of the unbounded derived direct image
> along `f` are the unbounded derived global sections on `C/X`:
> `RΓ(Y, -) ∘ Rf_* ≅ RΓ(X, -)`.
>
> Both sides are total right derived functors of one and the same functor on the unbounded homotopy
> category of abelian sheaves on `C/X`, by `overPushforwardGlobalSectionsIso`; the comparison for
> `Rf_*` is invertible on a K-injective complex, and the comparison for `RΓ(Y, -)` is invertible at
> `f_*I`, which is again K-injective by `overPushforward_map_isKInjective`. Uniqueness of right
> derived functors then identifies the two, which is
> `Stacks.Cohomology.LerayUnbounded.derivedCompIso`.

```lean
def derivedGlobalSectionsOverPushforwardIso {X Y : C} (f : X ⟶ Y) [HasPullbacksAlong f] :
    DerivedFunctor.totalRightDerived (overPushforward J f) ⋙
        DerivedFunctor.totalRightDerived
          ((sheafSections (J.over Y) Ab.{max u v}).obj (op (Over.mk (𝟙 Y)))) ≅
      DerivedFunctor.totalRightDerived
        ((sheafSections (J.over X) Ab.{max u v}).obj (op (Over.mk (𝟙 X))))
```

## Tag 0D6I, a lemma

[Tag 0D6I](https://stacks.math.columbia.edu/tag/0D6I) in the Stacks Project.

**`Stacks.Cohomology.UnboundedHigherDirectImageOnSites.cohomologySheavesOfTheDerivedDirectImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/CohomologySheavesOfTheDerivedDirectImageUnconditional.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/CohomologySheavesOfTheDerivedDirectImageUnconditional.lean#L160). The attribute's comment: “the i-th cohomology sheaf of Rf\_*K is the sheaf associated to the presheaf V ↦ H^i(u(V), K) = H^i(V, Rf\_*K), naturally in K, for an arbitrary morphism of ringed sites: the associated-sheaf clause and both readings of the value of the presheaf on an object”.

> **Stacks 0D6I.** Let `f : (C, O_C) ⟶ (D, O_D)` be a morphism of ringed sites corresponding to
> the continuous functor `u : D ⥤ C` and let `i : ℤ`. Then the `i`-th cohomology sheaf of `Rf_* K`
> is the sheaf associated to the presheaf
>
> `V ↦ H^i(u(V), K) = H^i(V, Rf_* K)`,
>
> naturally in the object `K` of `D(O_C)`.
>
> The presheaf is `derivedPushforwardCohomologyPresheaf`, which carries its restriction maps, and
> the three components are the three assertions the source makes about it: that its sheafification
> is the cohomology sheaf of `Rf_* K`, and that its value on `V` is `H^i(u(V), K)` and is
> `H^i(V, Rf_* K)` — the two sides of the source's displayed equality, whose composite
> `H^i(u(V), K) ≅ H^i(V, Rf_* K)` is `cohomologyOverObjectPushforwardIsoGeneral`.
>
> Everything is stated as an isomorphism of functors on `D(O_C)`, so the naturality in `K` that
> the source leaves implicit is part of the statement. There is no hypothesis beyond the source's:
> the sheafification clause is Stacks 0BKV on the target site composed with `Rf_*`, and the
> displayed equality is `H^i` of the clause of Stacks 0D6H on sections over an object, which
> `Stacks.Cohomology.LerayUnbounded.derivedSectionsOverObjectPushforwardIsoGeneral` proves for an
> arbitrary morphism of ringed sites.

```lean
def cohomologySheavesOfTheDerivedDirectImage (i : ℤ) :
    (derivedPushforward.{u} f.toRingedToposSiteHom ⋙
          DerivedCategory.homologyFunctor
            (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) i ≅
        derivedPushforward.{u} f.toRingedToposSiteHom ⋙ derivedSectionsPresheaf Y ⋙
          DerivedCategory.homologyFunctor
            (PresheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O).obj) i ⋙
          PresheafOfModules.sheafification (𝟙 (Stacks.SheafOfModules.Tensor.ringSheaf Y.O).obj)) ×
      (∀ V : Y.C,
          derivedPushforward.{u} f.toRingedToposSiteHom ⋙ derivedSectionsPresheaf Y ⋙
              DerivedCategory.homologyFunctor
                (PresheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O).obj) i ⋙
              PresheafOfModules.evaluation (Stacks.SheafOfModules.Tensor.ringSheaf Y.O).obj
                (Opposite.op V) ⋙
              forget₂
                (ModuleCat.{u}
                  ((Stacks.SheafOfModules.Tensor.ringSheaf Y.O).obj.obj (Opposite.op V)))
                AddCommGrpCat.{u} ≅
            derivedSectionsOverObject X (f.u.obj V) ⋙
              DerivedCategory.homologyFunctor AddCommGrpCat.{u} i) ×
      (∀ V : Y.C,
          derivedPushforward.{u} f.toRingedToposSiteHom ⋙ derivedSectionsPresheaf Y ⋙
              DerivedCategory.homologyFunctor
                (PresheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O).obj) i ⋙
              PresheafOfModules.evaluation (Stacks.SheafOfModules.Tensor.ringSheaf Y.O).obj
                (Opposite.op V) ⋙
              forget₂
                (ModuleCat.{u}
                  ((Stacks.SheafOfModules.Tensor.ringSheaf Y.O).obj.obj (Opposite.op V)))
                AddCommGrpCat.{u} ≅
            derivedPushforward.{u} f.toRingedToposSiteHom ⋙ derivedSectionsOverObject Y V ⋙
              DerivedCategory.homologyFunctor AddCommGrpCat.{u} i)
```

## Tag 0D6J, a lemma

[Tag 0D6J](https://stacks.math.columbia.edu/tag/0D6J) in the Stacks Project.

**`Stacks.Cohomology.ForgetModule.pushforwardForgetComparison_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/ForgettingTheModuleStructureForTheDirectImage.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/ForgettingTheModuleStructureForTheDirectImage.lean#L389). The attribute's comment: “part (3): the unbounded derived direct image along a morphism of ringed sites”.

> **Stacks 0D6J, part (3).** Let `f : (C, O_C) ⟶ (D, O_D)` be a morphism of ringed sites. For
> `K` in the unbounded derived category `D(O_C)` the canonical map `Rf_*K ⟶ Rf_*(K_ab)` from the
> image in `D(Z_D)` of the unbounded derived direct image of `K` to the unbounded derived direct
> image of the underlying abelian complex of `K` is an isomorphism, naturally in `K`.

```lean
theorem pushforwardForgetComparison_isIso : IsIso (pushforwardForgetComparison f)
```

**`Stacks.Cohomology.ForgetModule.sectionsForgetComparison_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/ForgettingTheModuleStructure.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/ForgettingTheModuleStructure.lean#L247). The attribute's comment: “part (2): sections over an object of the site”.

> **Stacks 0D6J, part (2).** For every object `U` of the site, the canonical map
> `RΓ(U, K) ⟶ RΓ(U, K_ab)` from unbounded derived sections of a sheaf of modules to derived
> sections of the underlying abelian sheaf is an isomorphism, naturally in `K`.

```lean
theorem sectionsForgetComparison_isIso (U : X.C) :
    IsIso (sectionsForgetComparison X U)
```

**`Stacks.Cohomology.ForgetModule.globalSectionsForgetComparison_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/ForgettingTheModuleStructure.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/ForgettingTheModuleStructure.lean#L362). The attribute's comment: “part (1): global sections of the site”.

> **Stacks 0D6J, part (1).** The canonical map `RΓ(C, K) ⟶ RΓ(C, K_ab)` from unbounded
> derived global sections of a sheaf of modules to derived global sections of the underlying
> abelian sheaf is an isomorphism, naturally in `K`.

```lean
theorem globalSectionsForgetComparison_isIso :
    IsIso (globalSectionsForgetComparison X)
```

## Tag 08FJ, a lemma

[Tag 08FJ](https://stacks.math.columbia.edu/tag/08FJ) in the Stacks Project.

**`Stacks.Cohomology.Localization.derivedExtensionByZeroRestrictionAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/RestrictionOfModules.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/RestrictionOfModules.lean#L235).

> **Stacks 08FJ.** On the unbounded derived categories of modules over a ringed site,
> extension by zero along the localization at an object is left adjoint to restriction to the
> localized site. The adjunction is the canonical one: it is obtained by localizing the
> degreewise underived adjunction, so its unit and counit are the images of the underived unit
> and counit under the localization comparisons.

```lean
noncomputable def derivedExtensionByZeroRestrictionAdjunction
    (X : RingedSite.{u, u, u}) (U : X.C)
    [HasDerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))]
    [HasDerivedCategory
      (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U))] :
    let R := (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
    let jShriek := SheafOfModules.pullback.{u}
      (F := Over.forget U) (𝟙 (R.over U) : (R.over U) ⟶ (R.over U))
    let restriction := SheafOfModules.overFunctor R U
    jShriek.mapDerivedCategory ⊣ restriction.mapDerivedCategory
```

## Tag 0GL1, a lemma

[Tag 0GL1](https://stacks.math.columbia.edu/tag/0GL1) in the Stacks Project.

**`Stacks.DerivedTensor.ExtensionByZero.derivedTensorExtensionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ExtensionByZeroTensor.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ExtensionByZeroTensor.lean#L357).

> **Stacks 0GL1.** Let `(C, O)` be a ringed site, `U` an object of `C` and `j_!` extension by
> zero from the localized site `C/U`. For `L` in `D(O_U)` and `K` in `D(O)`,
>
> `j_!L ⊗^L_O K = j_!(L ⊗^L_{O_U} K|_U)`.

```lean
def derivedTensorExtensionIso (L : DerivedCategory (Modules (X.O.over U)))
    (K : DerivedCategory (Modules X.O)) :
    ((baseDerivedTensor X).tensor.obj ((extension X U).mapDerivedCategory.obj L)).obj K ≅
      (extension X U).mapDerivedCategory.obj
        (((sliceDerivedTensor X U).tensor.obj L).obj
          ((restriction X U).mapDerivedCategory.obj K))
```

## Tag 093Y, a lemma

[Tag 093Y](https://stacks.math.columbia.edu/tag/093Y) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.pushforwardModules_isKInjective_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/FlatRingedToposPushforwardKInjective.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/FlatRingedToposPushforwardKInjective.lean#L121). References: SGA 4 V (4.9), “more general”.

> **Stacks 093Y.** Let `(f, f♯) : (Sh(C), O_C) ⟶ (Sh(D), O_D)` be a *flat* morphism of ringed
> topoi — flat in the sense of Stacks 04JB, that the ring map `f♯ : f⁻¹O_D ⟶ O_C` is flat — and
> let `I` be a K-injective complex of `O_C`-modules. Then the degreewise direct image `f_*I` is a
> K-injective complex of `O_D`-modules.
>
> The proof is the source's. The adjunction `f^* ⊣ f_*` of Stacks 03D7 identifies
> `Hom_{K(O_D)}(F, f_*I)` with `Hom_{K(O_C)}(f^*F, I)`; flatness makes `f^*` exact (Stacks 04JC),
> so it carries an acyclic `F` to an acyclic `f^*F`, on which K-injectivity of `I` makes every
> morphism into `I` null-homotopic. That is Stacks 08BJ applied to this adjunction.

```lean
theorem pushforwardModules_isKInjective_of_isFlat
    (f : RingedToposHom X Y) (hf : f.IsFlat)
    (I : CochainComplex (SheafOfModules.{w}
        (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ) [I.IsKInjective] :
    CochainComplex.IsKInjective
      ((f.pushforwardModules.mapHomologicalComplex (ComplexShape.up ℤ)).obj I)
```

## Tag 093Z, a lemma

[Tag 093Z](https://stacks.math.columbia.edu/tag/093Z) in the Stacks Project.

**`Stacks.Sheaves.KInjectiveInternalHom.isKInjective_homSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InternalHomKInjective.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InternalHomKInjective.lean#L60).

> **Stacks Project, Tag 093Z.** Internal Hom from `O'` takes K-injective complexes of
> `O`-modules to K-injective complexes of `O'`-modules.

```lean
theorem isKInjective_homSheaf (φ : O ⟶ O')
    (I : CochainComplex (SheafOfModules.{u} O) ℤ) [I.IsKInjective] :
    letI := (RingedSpaceModuleAdjunction.restrictScalarsHomAdjunction φ).right_adjoint_additive
    CochainComplex.IsKInjective
      (((RingedSpaceModuleAdjunction.homSheaf φ).mapHomologicalComplex (.up ℤ)).obj I)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.20, Tag 08FH](https://stacks.math.columbia.edu/tag/08FH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
