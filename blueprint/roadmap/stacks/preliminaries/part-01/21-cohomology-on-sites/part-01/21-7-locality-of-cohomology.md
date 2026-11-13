---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.preservesInjectiveObjects_etaleModulePullback_chartToSpace, Stacks.Cohomology.Localization.cohomologyOverObjectIsoSlice, Stacks.Cohomology.Localization.cohomologyOverObjectIsoSliceOfModule, Stacks.Cohomology.Localization.preservesInjectiveObjects_overFunctor, Stacks.Cohomology.Localization.injective_over, Stacks.Sites.ExtensionByZero.OverElements.preservesInjectiveObjects_pushforward_proj, Stacks.Sites.ExtensionByZero.OverElements.injective_pushforward_proj_obj, Stacks.Cohomology.BiggerSiteGlobal.sheafCohomologyIso
statement: formalized
proof: formalized
---

# 21.7 Locality of cohomology

Section 21.7 of the Stacks Project, [Tag 01FU](https://stacks.math.columbia.edu/tag/01FU). 5 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03F3, a lemma

[Tag 03F3](https://stacks.math.columbia.edu/tag/03F3) in the Stacks Project.

**`AlgebraicGeometry.Space.preservesInjectiveObjects_etaleModulePullback_chartToSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleModulePullbackChartInjectives.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleModulePullbackChartInjectives.lean#L239). The attribute's comment: “part (1), at the small étale site of an algebraic space”. References: SGA 4 V (4.11), “1) injective, etale site”.

> **Stacks 03F3, part (1), at the small étale site of an algebraic space.** Pullback of
> `𝒪_X`-modules along the structure morphism of an étale scheme chart `W` of an algebraic space
> `X` carries injective `𝒪_X`-modules to injective `𝒪_W`-modules.
>
> Indeed that pullback is restriction to the localization of the small étale site of `X` at `W`,
> which preserves injectives because its left adjoint, extension by zero, preserves
> monomorphisms, followed by the equivalence of Stacks 04M0 on sheaves of modules.

```lean
theorem preservesInjectiveObjects_etaleModulePullback_chartToSpace
    (W : SmallEtale B S hS X.1) :
    (etaleModulePullback.{u, u} B S hS (chartToSpace B S hS X W)
      (isEtale_chartToSpace B S hS X W)).PreservesInjectiveObjects
```

**`Stacks.Cohomology.Localization.cohomologyOverObjectIsoSlice`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/CohomologyOfModuleOverObject.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/CohomologyOfModuleOverObject.lean#L92). The attribute's comment: “part (2)”.

> **Stacks 03F3 (2).** For a ringed site `(C, O)` and an object `U` of `C`, the cohomology
> `H^p(U, F)` of a sheaf of `O`-modules over `U` is the cohomology `H^p(C/U, F|_U)` of its
> restriction on the site localized at `U`. Both sides place the module in degree zero and take
> the `p`-th homology of the corresponding derived sections; the isomorphism is natural in the
> module.

```lean
noncomputable def cohomologyOverObjectIsoSlice (X : RingedSite.{u, u, u}) (U : X.C) (p : ℤ) :
    DerivedCategory.singleFunctor (SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0 ⋙
        derivedSectionsOverObject X U ⋙
          DerivedCategory.homologyFunctor AddCommGrpCat.{u} p ≅
      SheafOfModules.overFunctor.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O) U ⋙
        DerivedCategory.singleFunctor (SheafOfModules.{u}
            ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U)) 0 ⋙
          derivedSectionsOnSlice X U ⋙
            DerivedCategory.homologyFunctor AddCommGrpCat.{u} p
```

**`Stacks.Cohomology.Localization.cohomologyOverObjectIsoSliceOfModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/CohomologyOfModuleOverObject.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/CohomologyOfModuleOverObject.lean#L120). The attribute's comment: “part (2), for one module”.

> **Stacks 03F3 (2)**, for one module: the cohomology of `F` over `U` is the cohomology of
> `F|_U` on the site localized at `U`.

```lean
noncomputable def cohomologyOverObjectIsoSliceOfModule (X : RingedSite.{u, u, u}) (U : X.C)
    (p : ℤ) (F : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    (DerivedCategory.homologyFunctor AddCommGrpCat.{u} p).obj
        ((derivedSectionsOverObject X U).obj
          ((DerivedCategory.singleFunctor (SheafOfModules.{u}
              (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj F)) ≅
      (DerivedCategory.homologyFunctor AddCommGrpCat.{u} p).obj
        ((derivedSectionsOnSlice X U).obj
          ((DerivedCategory.singleFunctor (SheafOfModules.{u}
              ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U)) 0).obj
            (F.over U)))
```

**`Stacks.Cohomology.Localization.preservesInjectiveObjects_overFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/RestrictionPreservesInjectives.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/RestrictionPreservesInjectives.lean#L54). The attribute's comment: “part (1)”. References: SGA 4 V (4.11), “1) injective case”; SGA 4 V (2.2), “special case”.

> **Stacks 03F3 (1).** Restriction of sheaves of modules to the site localized at an object
> preserves injective objects: its left adjoint, extension by zero, is exact.

```lean
theorem preservesInjectiveObjects_overFunctor :
    (SheafOfModules.overFunctor.{u} R U).PreservesInjectiveObjects
```

**`Stacks.Cohomology.Localization.injective_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/RestrictionPreservesInjectives.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/RestrictionPreservesInjectives.lean#L64). The attribute's comment: “part (1), for one module”. References: SGA 4 V (4.11), “1) injective case”.

> **Stacks 03F3 (1)**, for one module: the restriction `I|_U` of an injective sheaf of
> `R`-modules is an injective sheaf of `R_U`-modules.

```lean
theorem injective_over (I : SheafOfModules.{u} R) [Injective I] : Injective (I.over U)
```

**`Stacks.Sites.ExtensionByZero.OverElements.preservesInjectiveObjects_pushforward_proj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ElementSiteExtensionByZero.lean, line 494](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/ElementSiteExtensionByZero.lean#L494). The attribute's comment: “part (1), for the site of elements of a presheaf of sets”. References: SGA 4 V (4.11), “1) injective case”; SGA 4 V (2.3.2), “more general”.

> Restriction of sheaves of modules along the projection of the site of elements preserves
> injective objects.

```lean
theorem preservesInjectiveObjects_pushforward_proj :
    (SheafOfModules.pushforward.{u} (F := proj K)
      (𝟙 (restrictedRingSheaf K J JD R) :
        (restrictedRingSheaf K J JD R) ⟶
          (restrictedRingSheaf K J JD R))).PreservesInjectiveObjects
```

**`Stacks.Sites.ExtensionByZero.OverElements.injective_pushforward_proj_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ElementSiteExtensionByZero.lean, line 509](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/ElementSiteExtensionByZero.lean#L509). The attribute's comment: “part (1), for one module, at the site of elements of a presheaf of sets”. References: SGA 4 V (4.11), “1) injective case”; SGA 4 V (2.3.2), “more general”.

> The restriction of an injective sheaf of `R`-modules to the site of elements of `K` is
> injective.

```lean
theorem injective_pushforward_proj_obj (I : SheafOfModules.{u} R) [Injective I] :
    Injective ((SheafOfModules.pushforward.{u} (F := proj K)
      (𝟙 (restrictedRingSheaf K J JD R) :
        (restrictedRingSheaf K J JD R) ⟶ (restrictedRingSheaf K J JD R))).obj I)
```

## Tag 03YU, a lemma

[Tag 03YU](https://stacks.math.columbia.edu/tag/03YU) in the Stacks Project.

**`Stacks.Cohomology.BiggerSiteGlobal.sheafCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/BiggerSiteGlobalCohomology.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/BiggerSiteGlobalCohomology.lean#L190). The attribute's comment: “global cohomology, at independent site and coefficient universes”.

> **Stacks 03YU (1): restriction from a bigger site does not change global cohomology.** For
> terminal objects `e_C` of `C` and `e_D` of `D` with `u(e_C) = e_D`, and every degree `p`,
>
> `H^p(C, g⁻¹ F) ≅ H^p(D, F)`
>
> naturally in the abelian sheaf `F` on the bigger site `(D, K)`, where `H^p` is `Ext^p` out of the
> constant sheaf on `ℤ`.
>
> The two hypotheses on `g⁻¹` beyond continuity — right exactness and preservation of injective
> objects — are the content of Stacks 03A4 that this lemma consumes: they hold whenever `g⁻¹` has
> an exact left adjoint `g_!`, which for a fully faithful continuous and cocontinuous `u` between
> sites with fibre products is Stacks 03A4 itself.

```lean
def sheafCohomologyIso {eC : C} {eD : D} (heC : IsTerminal eC) (heD : IsTerminal eD)
    (hu : u.obj eC = eD) (p : ℕ) :
    u.sheafPushforwardContinuous AddCommGrpCat.{w} J K ⋙
        Sheaf.functorH.{max u w, w, v, u} J p ≅
      Sheaf.functorH.{max u w, w, v, u} K p
```

**`Stacks.Cohomology.BiggerSiteGlobal.sheafCohomologyIsoOfAcyclic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/BiggerSiteGlobalCohomology.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/BiggerSiteGlobalCohomology.lean#L272). The attribute's comment: “global cohomology, from acyclicity of the restriction of an injective sheaf”. References: SGA 4½ Arcata (2.3.5), “H^p(Y, special case”.

> **Restriction from a bigger site does not change global cohomology, from acyclicity.** For
> terminal objects `e_C` of `C` and `e_D` of `D` with `u(e_C) = e_D`, and every degree `p`,
>
> `H^p(C, g⁻¹ F) ≅ H^p(D, F)`
>
> naturally in the abelian sheaf `F` on the bigger site `(D, K)`, provided only that the
> restriction of an injective abelian sheaf has vanishing higher global cohomology on `(C, J)`.
>
> This is `Stacks.Cohomology.BiggerSiteGlobal.sheafCohomologyIso` with the hypothesis
> `[(u.sheafPushforwardContinuous …).PreservesInjectiveObjects]` replaced by the acyclicity
> statement it is only ever a route to. The replacement is what makes the lemma applicable to the
> inclusion of a subsite that is not closed under fibre products: there `g_!` is not exact, so
> restriction does not preserve injective objects, while the restriction of an injective sheaf is
> still acyclic — the content of Stacks 0D6X, by comparison of Čech complexes along `u`.
>
> The hypothesis is stated as the vanishing of `CategoryTheory.Sheaf.H` rather than as
> preservation of injectives precisely so that 0D6X can discharge it.
>
> The terminal objects are used only to produce the comparison of constant sheaves which
> `sheafCohomologyIsoOfConstantSheafIsoOfAcyclic` takes as a datum.

```lean
def sheafCohomologyIsoOfAcyclic {eC : C} {eD : D} (heC : IsTerminal eC) (heD : IsTerminal eD)
    (hu : u.obj eC = eD)
    (hacyclic : ∀ (I : Sheaf K AddCommGrpCat.{w}), Injective I → ∀ (n : ℕ)
      (a : Sheaf.H ((u.sheafPushforwardContinuous AddCommGrpCat.{w} J K).obj I) (n + 1)), a = 0)
    (p : ℕ) :
    u.sheafPushforwardContinuous AddCommGrpCat.{w} J K ⋙
        Sheaf.functorH.{max u w, w, v, u} J p ≅
      Sheaf.functorH.{max u w, w, v, u} K p
```

**`Stacks.Cohomology.BiggerSiteGlobal.cohomologyOverObjectIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/BiggerSiteGlobalCohomology.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/BiggerSiteGlobalCohomology.lean#L330). The attribute's comment: “cohomology over an object, at independent site and coefficient universes”.

> **Stacks 03YU (2): restriction from a bigger site does not change cohomology over an
> object.** For every `X : C` and every degree `p`,
>
> `H^p(C/X, g⁻¹ F) ≅ H^p(D/u(X), F)`
>
> naturally in the abelian sheaf `F` on the bigger site `(D, K)`, where cohomology over an object
> is the global cohomology of the sheaf restricted to the slice site.
>
> This is the global comparison `sheafCohomologyIso` applied to `Over.post u`, whose two slice
> sites have the terminal objects `𝟙 X` and `𝟙 u(X)`; the identification of the two ways of
> restricting to the slice is `overPullback_comp_sheafPushforwardContinuous`.

```lean
def cohomologyOverObjectIso (p : ℕ) :
    u.sheafPushforwardContinuous AddCommGrpCat.{w} J K ⋙
        J.overPullback AddCommGrpCat.{w} X ⋙
          Sheaf.functorH.{max u v w, w, v, max u v} (J.over X) p ≅
      K.overPullback AddCommGrpCat.{w} (u.obj X) ⋙
        Sheaf.functorH.{max u v w, w, v, max u v} (K.over (u.obj X)) p
```

**`Stacks.Cohomology.BiggerSiteGlobal.cohomologyOverObjectIsoOfAcyclic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/BiggerSiteGlobalCohomology.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/BiggerSiteGlobalCohomology.lean#L379). The attribute's comment: “cohomology over an object, from acyclicity of the restriction of an injective sheaf”.

> **Restriction from a bigger site does not change cohomology over an object, from
> acyclicity.** For every `X : C` and every degree `p`,
>
> `H^p(C/X, g⁻¹ F) ≅ H^p(D/u(X), F)`
>
> naturally in the abelian sheaf `F` on the bigger site `(D, K)`, provided only that the
> restriction to `C/X` of an injective abelian sheaf on `D/u(X)` has vanishing higher cohomology
> there.
>
> This is `Stacks.Cohomology.BiggerSiteGlobal.cohomologyOverObjectIso` with preservation of
> injective objects by restriction on the slice replaced by acyclicity, exactly as
> `sheafCohomologyIsoOfAcyclic` replaces it in the global statement; it is that statement applied
> to `Over.post u`, whose two slice sites have the terminal objects `𝟙 X` and `𝟙 u(X)`.

```lean
def cohomologyOverObjectIsoOfAcyclic
    (hacyclic : ∀ (I : Sheaf (K.over (u.obj X)) AddCommGrpCat.{w}), Injective I → ∀ (n : ℕ)
      (a : Sheaf.H (((Over.post (X := X) u).sheafPushforwardContinuous AddCommGrpCat.{w}
        (J.over X) (K.over (u.obj X))).obj I) (n + 1)), a = 0)
    (p : ℕ) :
    u.sheafPushforwardContinuous AddCommGrpCat.{w} J K ⋙
        J.overPullback AddCommGrpCat.{w} X ⋙
          Sheaf.functorH.{max u v w, w, v, max u v} (J.over X) p ≅
      K.overPullback AddCommGrpCat.{w} (u.obj X) ⋙
        Sheaf.functorH.{max u v w, w, v, max u v} (K.over (u.obj X)) p
```

**`Stacks.Cohomology.CompositeRightDerived.statement2_derived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/CompositeRightDerivedFunctors.lean, line 512](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/CompositeRightDerivedFunctors.lean#L512). The attribute's comment: “RΓ(U, g⁻¹F) ≅ RΓ(u(U), F)”.

> **Statement 2 (cohomology over an object), derived-category level.**
> For every object `U` of `C` there is a canonical isomorphism in `D^+(\mathbf Z)`
> `R\Gamma(U, g^{-1}\mathcal F) \cong R\Gamma(u(U), \mathcal F)`, functorially (i.e.
> as a natural isomorphism of functors `Sheaf K Ab ⥤ D^+(\mathbf Z)`).  Witnessed
> canonically by `derivedObjectIso`.

```lean
theorem statement2_derived (U : C) :
    Nonempty (gInvAb J K F ⋙ RGamma J U ≅ RGamma K (F.obj U))
```

**`Stacks.Cohomology.CompositeRightDerived.statement2_cohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/CompositeRightDerivedFunctors.lean, line 522](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/CompositeRightDerivedFunctors.lean#L522). The attribute's comment: “Hᵖ(U, g⁻¹F) ≅ Hᵖ(u(U), F)”.

> **Statement 2 (cohomology over an object), cohomology-group level.**
> For every object `U` of `C` and every `p`, a natural isomorphism of functors
> `Sheaf K Ab ⥤ Ab`, `H^p(U, g^{-1} -) \cong H^p(u(U), -)`.  Witnessed canonically by
> `cohomologyObjectIso`.

```lean
theorem statement2_cohomology (U : C) (p : ℕ) :
    Nonempty (gInvAb J K F ⋙ cohomology J U p ≅ cohomology K (F.obj U) p)
```

**`Stacks.Cohomology.CompositeRightDerived.statement1_derived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/CompositeRightDerivedFunctors.lean, line 533](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/CompositeRightDerivedFunctors.lean#L533). The attribute's comment: “RΓ(C, g⁻¹F) ≅ RΓ(D, F)”.

> **Statement 1 (cohomology over the whole site), derived-category level.**
> For terminal objects `e_C` of `C` and `e_D` of `D` with `u(e_C) = e_D`
> (hypothesis (e)), a canonical isomorphism in `D^+(\mathbf Z)`
> `R\Gamma(C, g^{-1}\mathcal F) \cong R\Gamma(D, \mathcal F)`, functorially.
> Witnessed canonically by `derivedSiteIso`.

```lean
theorem statement1_derived (eC : C) (eD : D) (heC : IsTerminal eC)
    (heD : IsTerminal eD) (hu : F.obj eC = eD) :
    Nonempty (gInvAb J K F ⋙ RGammaSite J ≅ RGammaSite K)
```

**`Stacks.Cohomology.CompositeRightDerived.statement1_cohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/CompositeRightDerivedFunctors.lean, line 545](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/CompositeRightDerivedFunctors.lean#L545). The attribute's comment: “Hᵖ(C, g⁻¹F) ≅ Hᵖ(D, F)”.

> **Statement 1 (cohomology over the whole site), cohomology-group level.**
> For terminal objects `e_C` of `C` and `e_D` of `D` with `u(e_C) = e_D`
> (hypothesis (e)) and every `p`, a natural isomorphism of functors
> `Sheaf K Ab ⥤ Ab`, `H^p(C, g^{-1} -) \cong H^p(D, -)`.  Witnessed canonically by
> `cohomologySiteIso`.

```lean
theorem statement1_cohomology (eC : C) (eD : D) (heC : IsTerminal eC)
    (heD : IsTerminal eD) (hu : F.obj eC = eD) (p : ℕ) :
    Nonempty (gInvAb J K F ⋙ siteCohomology J p ≅ siteCohomology K p)
```

## Tag 01FV, an equation

[Tag 01FV](https://stacks.math.columbia.edu/tag/01FV) in the Stacks Project.

**`Stacks.Cohomology.SiteModules.cohomologyRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/RestrictionMappings.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/RestrictionMappings.lean#L106). The attribute's comment: “restriction mapping”.

> The restriction mapping `Hⁿ(V, ℱ) ⟶ Hⁿ(U, ℱ)`, `ξ ↦ ξ|_U`, along a morphism `f : U ⟶ V` of the
> site, natural in the sheaf of `O`-modules `ℱ`. It is the map induced on cohomology by the
> restriction of sections, and it is `O(V)`-linear for the `O(V)`-module structure on `Hⁿ(U, ℱ)`
> through `O(V) ⟶ O(U)`.

```lean
def cohomologyRestriction (n : ℕ) {U V : C} (f : U ⟶ V) :
    (SheafOfModules.evaluation.{v} O (op V)).rightDerived n ⟶
      (SheafOfModules.evaluation.{v} O (op U)).rightDerived n ⋙
        ModuleCat.restrictScalars (O.obj.map f.op).hom
```

**`Stacks.Cohomology.SiteModules.cohomologyRestriction_app_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/RestrictionMappings.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/RestrictionMappings.lean#L118). The attribute's comment: “computed by an injective resolution”.

> The restriction mapping is computed from any injective resolution `ℱ ⟶ I^•`: it is the map
> induced on `Hⁿ` by the morphism of complexes `Γ(V, I^•) ⟶ Γ(U, I^•)` given by the restriction maps
> of the sheaves `I^p`, followed by the identification of `Hⁿ` of the restriction of scalars of
> `Γ(U, I^•)` with the restriction of scalars of `Hⁿ(U, ℱ)`.

```lean
theorem cohomologyRestriction_app_eq (n : ℕ) {U V : C} (f : U ⟶ V)
    {F : SheafOfModules.{v} O} (I : InjectiveResolution F) :
    (cohomologyRestriction O n f).app F =
      ((I.isoRightDerivedObj (SheafOfModules.evaluation O (op V)) n).hom ≫
        HomologicalComplex.homologyMap
          ((NatTrans.mapHomologicalComplex (sectionsRestriction O f) _).app I.cocomplex) n ≫
        (I.isoRightDerivedObj (SheafOfModules.evaluation O (op U) ⋙
          ModuleCat.restrictScalars (O.obj.map f.op).hom) n).inv) ≫
      ((SheafOfModules.evaluation O (op U)).rightDerivedCompIso _ n).hom.app F
```

**`Stacks.Cohomology.SiteModules.cohomologyPresheafFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/RestrictionMappings.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/RestrictionMappings.lean#L134). The attribute's comment: “presheaf of modules”.

> The functor sending a sheaf of `O`-modules `ℱ` to the presheaf of `O`-modules
> `H̲ⁿ(ℱ) : U ↦ Hⁿ(U, ℱ)`, defined as the `n`-th right derived functor of the inclusion of sheaves of
> `O`-modules into presheaves of `O`-modules.

```lean
def cohomologyPresheafFunctor (n : ℕ) : SheafOfModules.{v} O ⥤ PresheafOfModules.{v} O.obj
```

**`Stacks.Cohomology.SiteModules.cohomologyPresheafEvaluationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/RestrictionMappings.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/RestrictionMappings.lean#L144). The attribute's comment: “values of the presheaf”.

> The value of the presheaf `H̲ⁿ(ℱ)` at an object `U` of the site is the cohomology `Hⁿ(U, ℱ)`,
> as an `O(U)`-module and naturally in `ℱ`.

```lean
def cohomologyPresheafEvaluationIso (n : ℕ) (U : C) :
    (SheafOfModules.evaluation.{v} O (op U)).rightDerived n ≅
      cohomologyPresheafFunctor O n ⋙ PresheafOfModules.evaluation O.obj (op U)
```

**`Stacks.Cohomology.SiteModules.cohomologyPresheaf_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/RestrictionMappings.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/RestrictionMappings.lean#L152). The attribute's comment: “restriction maps of the presheaf”.

> Under the identification of its values with the cohomology modules, the restriction map of the
> presheaf `H̲ⁿ(ℱ)` along `f : U ⟶ V` is the restriction mapping `Hⁿ(V, ℱ) ⟶ Hⁿ(U, ℱ)`.

```lean
theorem cohomologyPresheaf_map (n : ℕ) {U V : C} (f : U ⟶ V) (F : SheafOfModules.{v} O) :
    (cohomologyPresheafEvaluationIso O n V).hom.app F ≫ (cohomologyPresheaf O n F).map f.op =
      (cohomologyRestriction O n f).app F ≫
        (ModuleCat.restrictScalars (O.obj.map f.op).hom).map
          ((cohomologyPresheafEvaluationIso O n U).hom.app F)
```

## Tag 01FW, a lemma

[Tag 01FW](https://stacks.math.columbia.edu/tag/01FW) in the Stacks Project.

**`Stacks.Cohomology.Locality.locality_of_cohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/CohomologyPresheafLocallyZero.lean, line 1354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/CohomologyPresheafLocallyZero.lean#L1354).

> **Stacks Project, Tag 01FW (Lemma 21.7.3).** Locality of cohomology.
>
> Let `(C, O)` be a ringed site (with `O = R : Sheaf J RingCat`), let `F` be a sheaf
> of `O`-modules, let `U` be an object of `C`, let `n > 0` and let
> `ξ ∈ H^n(U, F)`. Then there exists a covering `{U_i -> U}` of `U` such that the
> restriction `ξ|_{U_i}` vanishes in `H^n(U_i, F)` for every member `i` of the
> covering.

```lean
theorem locality_of_cohomology (R : Sheaf J RingCat) (F : SheafOfModules R)
    (n : ℕ) (hn : 0 < n) (U : C) (ξ : cohomology R F n U) :
    ∃ S : J.Cover U, ∀ g : S.Arrow,
      (restriction R F n g.f) ξ = 0
```

## Tag 072W, a lemma

[Tag 072W](https://stacks.math.columbia.edu/tag/072W) in the Stacks Project.

**`Stacks.Cohomology.ModuleHigherDirectImage.rightDerivedOfLEIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/ModuleHigherDirectImageSheafification.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/ModuleHigherDirectImageSheafification.lean#L205). The attribute's comment: “sheaves of modules, for a topology and a coarser one”.

> **Stacks 072W for the comparison of two topologies, on sheaves of modules.** The `p`-th higher
> direct image `R^pε_*` of the comparison `ε : (C_J, R) ⟶ (C_{J'}, R)` of a topology and a coarser
> one is the `J'`-sheafification of the cohomology presheaf `U ↦ H^p_J(U, -)`, the latter being the
> `p`-th right derived functor of the forgetful functor from sheaves of `R`-modules to presheaves of
> `R`-modules.

```lean
def rightDerivedOfLEIso (p : ℕ) :
    (SheafOfModules.ofLE.{u, v, r, m} h R).rightDerived p ≅
      (forgetOfLE.{u, v, r, m} h R).rightDerived p ⋙ sheafificationOfLE.{u, v, r, m} h R
```

**`higherDirectImage_iso_sheafify_cohomologyPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/SheafifiedCohomologyPresheaf.lean, line 430](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/SheafifiedCohomologyPresheaf.lean#L430). References: EGA 0 (12.4.3), “degree-0 complex”; EGA 0 (12.2.1), “partial”; SGA 4 V (5.1), “1)”; SGA 4 VIII (5.1), “more general”.

> **Stacks Tag `072W` (Lemma 21.7.4).**
> For a morphism of ringed sites `f : (C, O_C) -> (D, O_D)` given by a continuous functor
> `u : D -> C`, a sheaf of `O_C`-modules `F`, and `i >= 0`, the higher direct image
> `R^i f_* F` (Definition 3, the `i`-th right derived functor of `f_* = u^s`) is canonically
> isomorphic, *as a sheaf of `O_D`-modules*, to the sheafification `a (cohPresheafModule i F)`
> of the cohomology presheaf `V |-> H^i(u(V), F)` (Definition 4).
>
> A morphism of ringed sites carries more data than the proof uses: the right-adjointness of
> the continuous pushforward (so `f_* = u^s` has a left adjoint `f^{-1} = u_s`) and the
> exactness of that inverse image are what make `u` a morphism of sites, but the proof of Tag
> `072W` uses only the continuity of `u` (Definition 1, `pushforward_forget_eq`), so neither is
> assumed here. This matters in practice: on the big sites of schemes the continuous functor is
> base change along a morphism, whose continuity is available while the exactness of the
> inverse image is not.

```lean
theorem higherDirectImage_iso_sheafify_cohomologyPresheaf
    (i : ℕ) (F : SheafOfModules O𝒞) :
    Nonempty
      (((SheafOfModules.pushforward φ).rightDerived i).obj F ≅
        (moduleSheafification O𝒟).obj (cohPresheafModule u O𝒞 O𝒟 φ i F))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.7, Tag 01FU](https://stacks.math.columbia.edu/tag/01FU)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
