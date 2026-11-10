---
declaration: section
origin: cited
lean: Stacks.Cohomology.DerivedPushforwardSections.rightDerivedSectionsRestrictionIso, Stacks.Cohomology.DerivedPushforwardSections.rightDerivedSectionsRestrictionIso_hom_app, Stacks.Cohomology.ModuleComparison.rightDerivedFunctorPlus_sections_forget_iso, Stacks.Cohomology.ModuleComparison.rightDerivedFunctorPlus_sections_forget_iso_unit, Stacks.Cohomology.ModuleComparison.rightDerivedSectionsForgetIso_cocycles, Stacks.Cohomology.ModuleComparison.rightDerivedSectionsForgetIso, Stacks.Cohomology.ModuleComparison.rightDerivedSectionsForgetIso_zero, Stacks.Cohomology.ModuleComparison.canonicalSectionsForgetIso_naturality_open
statement: formalized
proof: formalized
---

# 20.13 The Leray spectral sequence

Section 20.13 of the Stacks Project, [Tag 01EY](https://stacks.math.columbia.edu/tag/01EY). 7 tags here are carried by 28 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01EZ, a lemma

[Tag 01EZ](https://stacks.math.columbia.edu/tag/01EZ) in the Stacks Project.

**`Stacks.Cohomology.DerivedPushforwardSections.rightDerivedSectionsRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/DerivedSectionsOfAPushforward.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/DerivedSectionsOfAPushforward.lean#L325). The attribute's comment: “the natural isomorphism”.

> **Stacks 01EZ.** For a morphism `f : X ⟶ Y` of ringed spaces and an open `V` of `Y`,
> let `U = f⁻¹(V)`. The composite of derived sections over `U` with derived restriction of
> scalars along `Γ(V, 𝒪_Y) → Γ(U, 𝒪_X)` is naturally isomorphic to the composite of
> derived pushforward along `f` with derived sections over `V`. Thus the corresponding square of
> bounded-below derived categories commutes.

```lean
public noncomputable def rightDerivedSectionsRestrictionIso
    {X Y : RingedSpace.{u, u}} (f : X ⟶ Y) (V : Opens Y.carrier) :
    (SheafOfModules.evaluation (structureSheafRing X)
          (op ((RingedSpaceModuleAdjunction.opensMap f).obj V))).rightDerivedFunctorPlus ⋙
        (ModuleCat.restrictScalars
          ((RingedSpaceModuleAdjunction.structureSheafHom f).hom.app
            (op V)).hom).rightDerivedFunctorPlus
      ≅
    (RingedSpaceModuleAdjunction.modulePushforward f).rightDerivedFunctorPlus ⋙
      (SheafOfModules.evaluation (structureSheafRing Y)
        (op V)).rightDerivedFunctorPlus
```

**`Stacks.Cohomology.DerivedPushforwardSections.rightDerivedSectionsRestrictionIso_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/DerivedSectionsOfAPushforward.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/DerivedSectionsOfAPushforward.lean#L352). The attribute's comment: “compatibility with the derived-functor units”.

> The derived comparison is induced by the identity on underived sections: its
> composite with the two derived-functor units is the comparison through pushforward.
> This equation fixes the canonical isomorphism, including its normalization on degree-zero
> cohomology.

```lean
theorem rightDerivedSectionsRestrictionIso_hom_app
    {X Y : RingedSpace.{u, u}} (f : X ⟶ Y) (V : Opens Y.carrier)
    (K : HomotopyCategory.Plus
      (SheafOfModules.{u} (structureSheafRing X))) :
    (ModuleCat.restrictScalars.{u}
        ((RingedSpaceModuleAdjunction.structureSheafHom f).hom.app
          (op V)).hom).rightDerivedFunctorPlusUnith.app
        ((SheafOfModules.evaluation.{u} (structureSheafRing X)
          (op ((RingedSpaceModuleAdjunction.opensMap f).obj V))).mapHomotopyCategoryPlus.obj
            K) ≫
        (ModuleCat.restrictScalars.{u}
          ((RingedSpaceModuleAdjunction.structureSheafHom f).hom.app
            (op V)).hom).rightDerivedFunctorPlus.map
          ((SheafOfModules.evaluation.{u} (structureSheafRing X)
            (op ((RingedSpaceModuleAdjunction.opensMap f).obj
              V))).rightDerivedFunctorPlusUnith.app K) ≫
        (rightDerivedSectionsRestrictionIso f V).hom.app (DerivedCategory.Plus.Qh.obj K) =
      DerivedCategory.Plus.Qh.map
          ((Functor.mapHomotopyCategoryPlusCompIso
              (F := SheafOfModules.evaluation.{u} (structureSheafRing X)
                (op ((RingedSpaceModuleAdjunction.opensMap f).obj V)))
              (G := ModuleCat.restrictScalars.{u}
                ((RingedSpaceModuleAdjunction.structureSheafHom f).hom.app (op V)).hom)
              (sectionsRestrictionIso f V)).hom.app K ≫
            (Functor.mapHomotopyCategoryPlusCompIso (Iso.refl
              (RingedSpaceModuleAdjunction.modulePushforward f ⋙
                SheafOfModules.evaluation.{u} (structureSheafRing Y)
                  (op V)))).inv.app K) ≫
        (SheafOfModules.evaluation.{u} (structureSheafRing Y)
          (op V)).rightDerivedFunctorPlusUnith.app
          ((RingedSpaceModuleAdjunction.modulePushforward f).mapHomotopyCategoryPlus.obj K) ≫
        (SheafOfModules.evaluation.{u} (structureSheafRing Y)
          (op V)).rightDerivedFunctorPlus.map
          ((RingedSpaceModuleAdjunction.modulePushforward f).rightDerivedFunctorPlusUnith.app
            K)
```

## Tag 01F0, a remark

[Tag 01F0](https://stacks.math.columbia.edu/tag/01F0) in the Stacks Project.

**`Stacks.Cohomology.DerivedPushforwardSections.rightDerivedSectionsRestrictionIso_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/DerivedSectionsOfAPushforward.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/DerivedSectionsOfAPushforward.lean#L352). The attribute's comment: “the comparison is induced by the identity on underived sections”.

> The derived comparison is induced by the identity on underived sections: its
> composite with the two derived-functor units is the comparison through pushforward.
> This equation fixes the canonical isomorphism, including its normalization on degree-zero
> cohomology.

```lean
theorem rightDerivedSectionsRestrictionIso_hom_app
    {X Y : RingedSpace.{u, u}} (f : X ⟶ Y) (V : Opens Y.carrier)
    (K : HomotopyCategory.Plus
      (SheafOfModules.{u} (structureSheafRing X))) :
    (ModuleCat.restrictScalars.{u}
        ((RingedSpaceModuleAdjunction.structureSheafHom f).hom.app
          (op V)).hom).rightDerivedFunctorPlusUnith.app
        ((SheafOfModules.evaluation.{u} (structureSheafRing X)
          (op ((RingedSpaceModuleAdjunction.opensMap f).obj V))).mapHomotopyCategoryPlus.obj
            K) ≫
        (ModuleCat.restrictScalars.{u}
          ((RingedSpaceModuleAdjunction.structureSheafHom f).hom.app
            (op V)).hom).rightDerivedFunctorPlus.map
          ((SheafOfModules.evaluation.{u} (structureSheafRing X)
            (op ((RingedSpaceModuleAdjunction.opensMap f).obj
              V))).rightDerivedFunctorPlusUnith.app K) ≫
        (rightDerivedSectionsRestrictionIso f V).hom.app (DerivedCategory.Plus.Qh.obj K) =
      DerivedCategory.Plus.Qh.map
          ((Functor.mapHomotopyCategoryPlusCompIso
              (F := SheafOfModules.evaluation.{u} (structureSheafRing X)
                (op ((RingedSpaceModuleAdjunction.opensMap f).obj V)))
              (G := ModuleCat.restrictScalars.{u}
                ((RingedSpaceModuleAdjunction.structureSheafHom f).hom.app (op V)).hom)
              (sectionsRestrictionIso f V)).hom.app K ≫
            (Functor.mapHomotopyCategoryPlusCompIso (Iso.refl
              (RingedSpaceModuleAdjunction.modulePushforward f ⋙
                SheafOfModules.evaluation.{u} (structureSheafRing Y)
                  (op V)))).inv.app K) ≫
        (SheafOfModules.evaluation.{u} (structureSheafRing Y)
          (op V)).rightDerivedFunctorPlusUnith.app
          ((RingedSpaceModuleAdjunction.modulePushforward f).mapHomotopyCategoryPlus.obj K) ≫
        (SheafOfModules.evaluation.{u} (structureSheafRing Y)
          (op V)).rightDerivedFunctorPlus.map
          ((RingedSpaceModuleAdjunction.modulePushforward f).rightDerivedFunctorPlusUnith.app
            K)
```

## Tag 01F1, a lemma

[Tag 01F1](https://stacks.math.columbia.edu/tag/01F1) in the Stacks Project.

**`Stacks.Cohomology.ModuleComparison.rightDerivedFunctorPlus_sections_forget_iso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/ModuleComparison/AcyclicityAndBoundedBelow.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/ModuleComparison/AcyclicityAndBoundedBelow.lean#L323). The attribute's comment: “bounded below complexes, part (1)”. References: EGA 0 (12.2.1), “H^p(U,F) comparison”.

> The comparison between module and abelian-sheaf cohomology is valid for bounded below
> complexes and is natural in the complex.

```lean
def rightDerivedFunctorPlus_sections_forget_iso (U : Opens X.carrier) :
    (SheafOfModules.evaluation (structureSheafRing X) (op U)).rightDerivedFunctorPlus ⋙
        (forget₂ (ModuleCat.{u} ((structureSheafRing X).obj.obj (op U)))
          AddCommGrpCat.{u}).rightDerivedFunctorPlus ≅
      (SheafOfModules.toSheaf (structureSheafRing X)).rightDerivedFunctorPlus ⋙
        ((sheafSections (Opens.grothendieckTopology X.carrier) AddCommGrpCat.{u}).obj
          (op U)).rightDerivedFunctorPlus
```

**`Stacks.Cohomology.ModuleComparison.rightDerivedFunctorPlus_sections_forget_iso_unit`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/ModuleComparison/AcyclicityAndBoundedBelow.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/ModuleComparison/AcyclicityAndBoundedBelow.lean#L335). The attribute's comment: “bounded below complexes, part (1), canonical comparison”.

> The bounded-below sections comparison is the canonical one: it intertwines the two
> units from ordinary sections.

```lean
lemma rightDerivedFunctorPlus_sections_forget_iso_unit (U : Opens X.carrier) :
    moduleSectionsDerivedUnit X U ≫
        Functor.whiskerLeft DerivedCategory.Plus.Qh
          (rightDerivedFunctorPlus_sections_forget_iso X U).hom =
      abelianSectionsDerivedUnit X U
```

**`Stacks.Cohomology.ModuleComparison.rightDerivedSectionsForgetIso_cocycles`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/ModuleComparison/CocycleFormula.lean, line 1365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/ModuleComparison/CocycleFormula.lean#L1365). The attribute's comment: “part (1), canonical comparison in every degree”.

> **Stacks 01F1, part (1), canonical comparison in every degree.**  In every degree the
> comparison sends a cocycle to the same cocycle in an abelian injective resolution, for any
> comparison `φ` of resolutions extending the identity and any induced map `c` on cocycles.
>
> Degree zero is `rightDerivedSectionsForgetIso_cocycles_zero`; in positive degree this is
> `rightDerivedSectionsForgetIso_cocycles_of_hom_app_eq` with its hypothesis discharged by
> `sectionsComparisonIso_hom_app_succ_eq`.

```lean
theorem rightDerivedSectionsForgetIso_cocycles (n : ℕ) (M : SheafOfModules.{u} R)
    (I : InjectiveResolution M)
    (J : InjectiveResolution ((SheafOfModules.toSheaf R).obj M))
    (φ : ((SheafOfModules.toSheaf R).mapHomologicalComplex
      (ComplexShape.up ℕ)).obj I.cocomplex ⟶ J.cocomplex)
    (hφ : (SheafOfModules.toSheaf R).map (I.ι.f 0) ≫ φ.f 0 = J.ι.f 0) :
    let E := SheafOfModules.evaluation R (op U)
    let G := forget₂ (ModuleCat.{u} (R.obj.obj (op U))) AddCommGrpCat.{u}
    let A := (sheafSections (Opens.grothendieckTopology X) AddCommGrpCat.{u}).obj (op U)
    let K := (E.mapHomologicalComplex (ComplexShape.up ℕ)).obj I.cocomplex
    let L := (A.mapHomologicalComplex (ComplexShape.up ℕ)).obj J.cocomplex
    ∀ (c : G.obj (K.cycles n) ⟶ L.cycles n)
      (_ : c ≫ L.iCycles n = G.map (K.iCycles n) ≫ A.map (φ.f n)),
      G.map (K.homologyπ n ≫ (I.isoRightDerivedObj E n).inv) ≫
          (rightDerivedSectionsForgetIso R U n).hom.app M ≫
          (J.isoRightDerivedObj A n).hom =
        c ≫ L.homologyπ n
```

**`Stacks.Cohomology.ModuleComparison.rightDerivedSectionsForgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/ModuleComparison/ComparisonAndDegreeZero.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/ModuleComparison/ComparisonAndDegreeZero.lean#L110). The attribute's comment: “part (1)”.

> Cohomology over an open subset `U`, computed by deriving module-valued sections and then
> forgetting the module structure, agrees canonically and naturally with cohomology computed after
> forgetting the coefficient sheaf to an abelian sheaf.
>
> This is `canonicalSectionsForgetIso`, in the shape in which Stacks 01F1 part (1) states it; the
> degree-zero normalization is `rightDerivedSectionsForgetIso_zero` and the compatibility with
> restriction is `canonicalSectionsForgetIso_naturality_open`.

```lean
def rightDerivedSectionsForgetIso (n : ℕ) :
    (SheafOfModules.evaluation R (op U)).rightDerived n ⋙
        forget₂ (ModuleCat.{u} (R.obj.obj (op U))) AddCommGrpCat.{u} ≅
      SheafOfModules.toSheaf R ⋙
        ((sheafSections (Opens.grothendieckTopology X) AddCommGrpCat.{u}).obj
          (op U)).rightDerived n
```

**`Stacks.Cohomology.ModuleComparison.rightDerivedSectionsForgetIso_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/ModuleComparison/ComparisonAndDegreeZero.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/ModuleComparison/ComparisonAndDegreeZero.lean#L155). The attribute's comment: “part (1), degree-zero normalization”.

> In degree zero the comparison `rightDerivedSectionsForgetIso` intertwines the canonical maps
> from ordinary sections to the zeroth right derived functors.

```lean
theorem rightDerivedSectionsForgetIso_zero :
    Functor.whiskerRight (SheafOfModules.evaluation R (op U)).toRightDerivedZero
          (forget₂ (ModuleCat.{u} (R.obj.obj (op U))) AddCommGrpCat.{u}) ≫
        (rightDerivedSectionsForgetIso R U 0).hom =
      Functor.whiskerLeft (SheafOfModules.toSheaf R)
        ((sheafSections (Opens.grothendieckTopology X) AddCommGrpCat.{u}).obj
          (op U)).toRightDerivedZero
```

**`Stacks.Cohomology.ModuleComparison.canonicalSectionsForgetIso_naturality_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/ModuleComparison/CompatibilityWithRestriction.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/ModuleComparison/CompatibilityWithRestriction.lean#L239). The attribute's comment: “part (1), compatibility with restriction”.

> **Stacks 01F1, part (1), compatibility with restriction.** The comparison of cohomology over
> an open subset commutes with restriction to a smaller open subset.  The left-hand restriction is
> derived from the underlying abelian-group-valued module sections; `rightDerivedEvaluationForgetIso`
> identifies it with module-valued cohomology.
>
> Through that identification the comparison is `ModuleSheafCohomology.sectionsComparisonIso`, and
> the statement is `sectionsComparisonIso_naturality` for the morphism `homOfLE h : U ⟶ V` of the
> site of opens, read at the module sheaf `M`.

```lean
theorem canonicalSectionsForgetIso_naturality_open {U V : Opens X} (h : U ≤ V) (n : ℕ)
    (M : SheafOfModules.{u} R) :
    (NatTrans.rightDerived
          (Functor.whiskerLeft (SheafOfModules.toSheaf R)
            (sectionsRestriction (Opens.grothendieckTopology X) (homOfLE h))) n).app M ≫
        (rightDerivedEvaluationForgetIso R U n).inv.app M ≫
        (canonicalSectionsForgetIso R U n).hom.app M =
      (rightDerivedEvaluationForgetIso R V n).inv.app M ≫
        (canonicalSectionsForgetIso R V n).hom.app M ≫
        (NatTrans.rightDerived
          (sectionsRestriction (Opens.grothendieckTopology X) (homOfLE h)) n).app
          ((SheafOfModules.toSheaf R).obj M)
```

**`Stacks.Cohomology.ModulePushforwardComparison.rightDerivedFunctorPlus_modulePushforward_forget_iso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/ModulePushforwardComparison/BoundedBelowComplexes.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/ModulePushforwardComparison/BoundedBelowComplexes.lean#L197). The attribute's comment: “bounded below complexes, part (2)”.

> The comparison between module and abelian-sheaf higher direct images is valid for
> bounded below complexes and is natural in the complex.

```lean
noncomputable def rightDerivedFunctorPlus_modulePushforward_forget_iso :
    (modulePushforward f).rightDerivedFunctorPlus ⋙
        (SheafOfModules.toSheaf (structureSheafRing Y)).rightDerivedFunctorPlus ≅
      (SheafOfModules.toSheaf (structureSheafRing X)).rightDerivedFunctorPlus ⋙
        ((opensMap f).sheafPushforwardContinuous AddCommGrpCat.{u}
          (Opens.grothendieckTopology Y.carrier)
          (Opens.grothendieckTopology X.carrier)).rightDerivedFunctorPlus
```

**`Stacks.Cohomology.ModulePushforwardComparison.rightDerivedFunctorPlus_modulePushforward_forget_iso_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/ModulePushforwardComparison/BoundedBelowComplexes.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/ModulePushforwardComparison/BoundedBelowComplexes.lean#L211). The attribute's comment: “bounded below complexes, part (2), canonical comparison”.

> The bounded-below higher-direct-image comparison is the canonical one: it intertwines
> the units from ordinary pushforward.

```lean
theorem rightDerivedFunctorPlus_modulePushforward_forget_iso_unit :
    modulePushforwardDerivedUnit f ≫
        Functor.whiskerLeft DerivedCategory.Plus.Qh
          (rightDerivedFunctorPlus_modulePushforward_forget_iso f).hom =
      abelianPushforwardDerivedUnit f
```

**`Stacks.Cohomology.ModulePushforwardComparison.rightDerived_modulePushforward_forget_iso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/ModulePushforwardComparison/HigherDirectImages.lean, line 482](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/ModulePushforwardComparison/HigherDirectImages.lean#L482). The attribute's comment: “part (2)”.

> **Stacks 01F1, part (2).**  Higher direct images of a sheaf of modules, computed in sheaves
> of modules and then forgotten to abelian sheaves, agree canonically and naturally with the
> higher direct images of the underlying abelian sheaf.
>
> In degree zero the isomorphism is the canonical one coming from left exactness of the two
> pushforwards, which is what makes `rightDerived_modulePushforward_forget_iso_zero` true; in
> positive degree it is `rightDerivedModulePushforwardCompIso` followed by
> `rightDerivedToSheafAbelianPushforwardIso`.

```lean
noncomputable def rightDerived_modulePushforward_forget_iso (n : ℕ) :
    (modulePushforward f).rightDerived n ⋙ SheafOfModules.toSheaf (structureSheafRing Y) ≅
      SheafOfModules.toSheaf (structureSheafRing X) ⋙
        ((opensMap f).sheafPushforwardContinuous AddCommGrpCat.{u}
          (Opens.grothendieckTopology Y.carrier)
          (Opens.grothendieckTopology X.carrier)).rightDerived n
```

**`Stacks.Cohomology.ModulePushforwardComparison.rightDerived_modulePushforward_forget_iso_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/ModulePushforwardComparison/HigherDirectImages.lean, line 498](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/ModulePushforwardComparison/HigherDirectImages.lean#L498). The attribute's comment: “part (2), degree-zero normalization”.

> **Stacks 01F1, part (2), degree-zero normalization.**  In degree zero the comparison
> intertwines the canonical maps from the ordinary pushforwards to the zeroth right derived
> functors.

```lean
theorem rightDerived_modulePushforward_forget_iso_zero :
    Functor.whiskerRight (modulePushforward f).toRightDerivedZero
          (SheafOfModules.toSheaf (structureSheafRing Y)) ≫
        (rightDerived_modulePushforward_forget_iso f 0).hom =
      Functor.whiskerLeft (SheafOfModules.toSheaf (structureSheafRing X))
        ((opensMap f).sheafPushforwardContinuous AddCommGrpCat.{u}
          (Opens.grothendieckTopology Y.carrier)
          (Opens.grothendieckTopology X.carrier)).toRightDerivedZero
```

**`Stacks.Cohomology.ModulePushforwardComparison.rightDerived_modulePushforward_forget_iso_cocycles`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/ModulePushforwardComparison/ResolutionLevelFormula.lean, line 628](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/ModulePushforwardComparison/ResolutionLevelFormula.lean#L628). The attribute's comment: “part (2), canonical comparison in every degree”.

> The higher-direct-image comparison is induced by a comparison from a module injective
> resolution to an abelian injective resolution extending the identity of the underlying abelian
> sheaf: in every degree its effect on cocycles is the one prescribed by any such comparison.  This
> fixes the comparison independently of all choices of resolutions and comparison maps.

```lean
theorem rightDerived_modulePushforward_forget_iso_cocycles (n : ℕ)
    (M : SheafOfModules.{u} (structureSheafRing X)) (I : InjectiveResolution M)
    (J : InjectiveResolution ((SheafOfModules.toSheaf (structureSheafRing X)).obj M))
    (φ : ((SheafOfModules.toSheaf (structureSheafRing X)).mapHomologicalComplex
      (ComplexShape.up ℕ)).obj I.cocomplex ⟶ J.cocomplex)
    (hφ : (SheafOfModules.toSheaf (structureSheafRing X)).map (I.ι.f 0) ≫ φ.f 0 = J.ι.f 0) :
    let E := modulePushforward f
    let G := SheafOfModules.toSheaf (structureSheafRing Y)
    let A := (opensMap f).sheafPushforwardContinuous AddCommGrpCat.{u}
      (Opens.grothendieckTopology Y.carrier) (Opens.grothendieckTopology X.carrier)
    let K := (E.mapHomologicalComplex (ComplexShape.up ℕ)).obj I.cocomplex
    let L := (A.mapHomologicalComplex (ComplexShape.up ℕ)).obj J.cocomplex
    ∀ (c : G.obj (K.cycles n) ⟶ L.cycles n)
      (_ : c ≫ L.iCycles n = G.map (K.iCycles n) ≫ A.map (φ.f n)),
      G.map (K.homologyπ n ≫ (I.isoRightDerivedObj E n).inv) ≫
          (rightDerived_modulePushforward_forget_iso f n).hom.app M ≫
          (J.isoRightDerivedObj A n).hom =
        c ≫ L.homologyπ n
```

## Tag 01F2, a lemma

[Tag 01F2](https://stacks.math.columbia.edu/tag/01F2) in the Stacks Project.

**`Stacks.Cohomology.LerayCard.leraySpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Leray/Assembled.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Leray/Assembled.lean#L249).

> **The Leray spectral sequence of a morphism of ringed spaces**, [Stacks, Tag 01F2]. For
> `f : X ⟶ Y` a morphism of ringed spaces, this is the functorial `E₂`-cohomological spectral
> sequence of `Γ(Y, 𝒪_Y)`-modules on `D⁺(Mod(𝒪_X))` whose second page is `H^p(Y, R^q f_* K)`
> naturally in `K`, which abuts to `H^{p+q}(X, K)` with scalars restricted along `f`, together
> with the low-degree Leray sequence for abelian sheaves on the underlying spaces.
>
> The abelian sheaves have coefficients in the universe of the space, `.{u, u}`, where
> [Stacks, Tag 01F2] allows `.{u, v}`; see the implementation notes of this module.

```lean
def leraySpectralSequence {X Y : RingedSpace.{u, u}} (f : X ⟶ Y) :
    LeraySpectralSequenceData.{u, u} f
```

**`Stacks.Cohomology.LerayModules.exists_spectralSequence_leray`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Leray/ModuleSheafSpectralSequence.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Leray/ModuleSheafSpectralSequence.lean#L96). The attribute's comment: “the whole statement: existence of the spectral sequence with second page `H^p(Y, R^q f_* K)` converging to `H^{p+q}(X, K)`, for `K` in `D⁺(Mod(𝒪_X))`. Functoriality in `K` is NOT asserted — the source does not state it”.

> **The Leray spectral sequence for sheaves of modules.**  Let `f : X ⟶ Y` be a morphism of
> ringed spaces and let `K` be an object of `D⁺(Mod(𝒪_X))`.  There is a filtered complex `L` of
> `Γ(Y, 𝒪_Y)`-modules with `H^n(L) ≅ H^n(X, K)` for all `n`, the right-hand side being the
> hypercohomology of `X` with scalars restricted along `f`, whose spectral sequence `E`,
> presented as in [Stacks, Tag 012M] by its pages `Z_r^{p,q}/D_r^{p,q}`, has
> `E_2^{p,q} ≅ H^p(Y, R^q f_* K)`, is bounded, induces a finite filtration on each `H^n(L)`, and
> converges to `H^*(L)`.

```lean
theorem exists_spectralSequence_leray
    (K : DerivedCategory.Plus (SheafOfModules.{u} (structureSheafRing X))) :
    ∃ L : FilteredObject (CochainComplex
        (ModuleCat.{u} ((structureSheafRing Y).obj.obj (op (⊤ : Opens Y.carrier)))) ℤ) ℤᵒᵖ,
      (∀ n : ℤ, Nonempty (L.X.homology n ≅
        (DerivedCategory.Plus.homologyFunctor
            (ModuleCat.{u} ((structureSheafRing Y).obj.obj (op (⊤ : Opens Y.carrier)))) n).obj
          (((SheafOfModules.evaluation (structureSheafRing X)
                (op ((opensMap f).obj (⊤ : Opens Y.carrier)))).rightDerivedFunctorPlus ⋙
              (ModuleCat.restrictScalars
                ((structureSheafHom f).hom.app
                  (op (⊤ : Opens Y.carrier))).hom).rightDerivedFunctorPlus).obj K))) ∧
      ∀ (Fil : ∀ (_p n : ℤ), Subobject (L.X.X n))
        (_ : ∀ p n : ℤ, Fil p n = Subobject.mk ((L.filtration.ι.app (op p)).f n))
        (Z : ∀ (_r _p n : ℤ), Subobject (L.X.X n))
        (_ : ∀ r p n : ℤ, Z r p n =
          Fil p n ⊓ (Subobject.pullback (L.X.d n (n + 1))).obj (Fil (p + r) (n + 1)))
        (D : ∀ (_r _p n : ℤ), Subobject (L.X.X n))
        (_ : ∀ r p n : ℤ, D r p n = Z (r - 1) (p + 1) n ⊔
          (Subobject.«exists» (L.X.d (n - 1) n)).obj (Z (r - 1) (p - r + 1) (n - 1)))
        (FH : ∀ (n _p : ℤ), Subobject (L.X.homology n))
        (_ : ∀ n p : ℤ, FH n p =
          imageSubobject (HomologicalComplex.homologyMap (L.filtration.ι.app (op p)) n)),
      ∃ (E : CohomologicalSpectralSequence
          (ModuleCat.{u} ((structureSheafRing Y).obj.obj (op (⊤ : Opens Y.carrier)))) 0)
        (_ : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q), (E.page r hr).X (p, q) ≅
          cokernel (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n))),
        (∀ p q : ℤ, Nonempty ((E.page 2 zero_le_two).X (p, q) ≅
          ((SheafOfModules.evaluation (structureSheafRing Y)
              (op (⊤ : Opens Y.carrier))).rightDerivedPlus p).obj
            ((DerivedCategory.Plus.homologyFunctor
                (SheafOfModules.{u} (structureSheafRing Y)) q).obj
              ((modulePushforward f).rightDerivedFunctorPlus.obj K)))) ∧
        (∀ n : ℤ, {p : ℤ | ¬ IsZero ((E.page 0).X (p, n - p))}.Finite) ∧
        (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ FH n a = ⊤ ∧ FH n b = ⊥) ∧
        (∀ p q : ℤ, ∃ b : ℤ, ∀ (r : ℤ) (hr : 0 ≤ r), b ≤ r →
          (E.page r hr).d (p, q) (p + r, q - r + 1) = 0) ∧
        (∀ p n : ℤ,
          IsGLB (Set.range fun r : ℕ =>
              Fil p n ⊓ (Subobject.pullback (L.X.d n (n + 1))).obj (Fil (p + r) (n + 1)) ⊔
                Fil (p + 1) n)
            (kernelSubobject (L.X.d n (n + 1)) ⊓ Fil p n ⊔ Fil (p + 1) n) ∧
          IsLUB (Set.range fun r : ℕ =>
              Fil p n ⊓ (Subobject.«exists» (L.X.d (n - 1) n)).obj (Fil (p - r) (n - 1)) ⊔
                Fil (p + 1) n)
            (imageSubobject (L.X.d (n - 1) n) ⊓ Fil p n ⊔ Fil (p + 1) n))
```

## Tag 01F4, a lemma

[Tag 01F4](https://stacks.math.columbia.edu/tag/01F4) in the Stacks Project.

**`Stacks.LeraySections.cohomologyIsoOfVanishingHigherDirectImages`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LeraySectionsCollapse/Leray.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LeraySectionsCollapse/Leray.lean#L230). The attribute's comment: “part (1)”. References: SGA 4½ Arcata (2.3.5), “H^p(X,F)=H^p(Y,f\_*F)”.

> **[Stacks, Tag 01F4] part (1).** If the higher direct images of a sheaf of
> `𝒪_X`-modules along a morphism of ringed spaces vanish, then its cohomology agrees in every
> degree with the cohomology of its direct image.

```lean
noncomputable def cohomologyIsoOfVanishingHigherDirectImages
    {F : SheafOfModules.{u} (structureSheafRing X)}
    (hF : ∀ q : ℕ, 0 < q → IsZero (((modulePushforward f).rightDerived q).obj F)) (p : ℕ) :
    (Hfunctor (structureSheafRing X) ⊤ p).obj F ≅
      (Hfunctor (structureSheafRing Y) ⊤ p).obj ((modulePushforward f).obj F)
```

**`Deformation.Artin.SectionsSheaf.isIso_edgeMap_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/SectionsEdgeMap.lean, line 630](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/SectionsEdgeMap.lean#L630). The attribute's comment: “(1) for a morphism of schemes, the isomorphism H^p(Y, f\_*F) ≅ H^p(X, F) being the edge map, which commutes with the connecting morphisms”.

> **Stacks 01F4, part (1), through the edge map.** If the higher direct images `R^q p_* G`
> vanish for `q > 0`, the edge map `|Hⁿ(Y, p_* G)| ⟶ |Hⁿ(X, G)|` is an isomorphism in every
> degree.

```lean
theorem isIso_edgeMap_app (G : SheafOfModules.{u} X.ringCatSheaf)
    (hG : ∀ q : ℕ, 0 < q → IsZero (((Scheme.Modules.pushforward p).rightDerived q).obj G))
    (n : ℕ) : IsIso ((edgeMap p π n).app G)
```

**`Stacks.Cohomology.LerayModules.isIso_cohomologyToSectionsHigherDirectImage_of_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Leray/BaseVanishingCollapse.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Leray/BaseVanishingCollapse.lean#L166). The attribute's comment: “part (2)”.

> **[Stacks, Tag 01F4] part (2).** Let `f : X ⟶ Y` be a morphism of ringed spaces and let `F`
> be a sheaf of `𝒪_X`-modules. If `H^p(Y, R^q f_* F) = 0` for every `p > 0` and every `q`, then
> the canonical map `H^q(X, F) ⟶ Γ(Y, R^q f_* F)` is an isomorphism for every `q`; in particular
> `H^q(X, F) = H^0(Y, R^q f_* F)`, which is what the source states.
>
> Global sections on `X` *are* the direct image followed by global sections on `Y`, so the
> cohomology of `X` is the homology of `Γ(Y, -)` applied to `K = f_*(I^•)` for an injective
> resolution `I` of `F`. The terms of `K` are `Γ(Y, -)`-acyclic by [Stacks, Tag 01EX] part (2)
> (`Stacks.LeraySections.rightAcyclic_secF_modulePushforward_obj`) and its cohomology objects are
> `Γ(Y, -)`-acyclic by hypothesis, so `Γ(Y, -)` commutes with taking homology in degree `q`:
> that is `Stacks.Cohomology.RightDerivedCoEdge.isIso_homologyToMapHomology_of_acyclic`, and the
> two transports in `cohomologyToSectionsHigherDirectImage` are isomorphisms.

```lean
theorem isIso_cohomologyToSectionsHigherDirectImage_of_vanishing
    (f : X ⟶ Y) (F : SheafOfModules.{u} (structureSheafRing X))
    (hvan : ∀ (p q : ℕ), 0 < p →
      IsZero (Hgroup (structureSheafRing Y) ⊤ p (((modulePushforward f).rightDerived q).obj F)))
    (q : ℕ) :
    IsIso (cohomologyToSectionsHigherDirectImage f F q)
```

## Tag 01F5, a lemma

[Tag 01F5](https://stacks.math.columbia.edu/tag/01F5) in the Stacks Project.

**`Stacks.Cohomology.RelativeLeray.derivedPushforwardPlusCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeLeraySpectralSequence/Basic.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeLeraySpectralSequence/Basic.lean#L206).

> **[Stacks, Tag 01F5]: `R(g ∘ f)_* ≅ Rf_* ⋙ Rg_*` as functors `D⁺(X) ⥤ D⁺(Z)`**, for
> arbitrary morphisms of ringed spaces `f : X ⟶ Y` and `g : Y ⟶ Z`. No hypothesis.
>
> The isomorphism is the **canonical** comparison of [Stacks, Tag 05T2],
> `CategoryTheory.Functor.rightDerivedFunctorPlusComp`, inverted — not an arbitrary
> identification — precomposed with the undeived composition formula
> [Stacks, Tag 0097] (1) for `(g ∘ f)_* = g_* ∘ f_*`. Invertibility is the criterion of
> [Stacks, Tag 015M], whose hypothesis is discharged by
> `rightAcyclic_modulePushforward_obj_of_injective`.

```lean
def derivedPushforwardPlusCompIso :
    (modulePushforward (f ≫ g)).rightDerivedFunctorPlus ≅
      (modulePushforward f).rightDerivedFunctorPlus ⋙
        (modulePushforward g).rightDerivedFunctorPlus
```

**`Stacks.Cohomology.DerivedDirectImageComposition.higherDirectImagesComparison_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/RecoveryA/DerivedDirectImageComposition.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/RecoveryA/DerivedDirectImageComposition.lean#L271).

> **Stacks Project, Tag 01F5.** The canonical comparison from the derived direct image of a
> composite to the composite of the derived direct images is an isomorphism.

```lean
theorem higherDirectImagesComparison_isIso {X Y Z : RingedSpace.{u}}
    [HasDerivedCategory.{wX} (Modules X)]
    [HasDerivedCategory.{wY} (Modules Y)]
    [HasDerivedCategory.{wZ} (Modules Z)]
    (f : X ⟶ Y) (g : Y ⟶ Z) :
    IsIso (higherDirectImagesComparison f g)
```

## Tag 01F6, a lemma

[Tag 01F6](https://stacks.math.columbia.edu/tag/01F6) in the Stacks Project.

**`Stacks.RelativeLerayPlus.relativeLeraySpectralSequencePlus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeLerayPlus/Basic.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeLerayPlus/Basic.lean#L189). The attribute's comment: “bounded below complexes”.

> **Relative Leray spectral sequence for bounded below complexes**, [Stacks, Tag 01F6].  For
> each bounded below complex of `𝒪_X`-modules there is a bounded spectral sequence with second
> page `R ᵖ g_*(H^q(R f_* K))`, vanishing in the left half plane, abutting to
> `H ⁿ(R (f ≫ g)_* K)` by a finite filtration.
>
> This is `exists_spectralSequence_relativeLerayPlus` with the spectral sequence chosen for each
> complex; the four propositional clauses are the content, and all four are proved there.

```lean
noncomputable def relativeLeraySpectralSequencePlus :
    RelativeLeraySpectralSequencePlusData f g
```

**`Stacks.Cohomology.RelativeLeray.exists_spectralSequence_relativeLeray`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeLeraySpectralSequence/Basic.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeLeraySpectralSequence/Basic.lean#L242). The attribute's comment: “the spectral sequence for a bounded below complex, not its functoriality”. References: EGA 0 (12.2.4); SGA 4 V (5.4), “ringed spaces”.

> **[Stacks, Tag 01F6] for a bounded below complex.** For morphisms of ringed spaces
> `f : X ⟶ Y` and `g : Y ⟶ Z` and an object `M` of `D⁺(X)` there is a filtered complex `K` of
> `𝒪_Z`-modules with `H^n(K) ≅ H^n(R(g ∘ f)_* M)` in every degree, whose filtration is finite in
> each degree and whose spectral sequence `E`, presented as in [Stacks, Tag 012M] by its pages
> `Z_r^{p,q}/D_r^{p,q}`, has
>
> `E₂^{p,q} ≅ R^p g_*(H^q(Rf_* M))`,
>
> is bounded, induces a finite filtration on each `H^n(K)`, and converges to `H^*(K)`.
>
> This is the source's *"there is a version for bounded below complexes of `𝒪_X`-modules"*, and it
> is the primary form: the module statement `exists_spectralSequence_relativeLeray_obj` is this one
> at `M := ℱ[0]`. It is [Stacks, Tag 015N] for the pair `(f_*, g_*)`, whose hypothesis is
> `rightAcyclic_modulePushforward_obj_of_injective`, with the abutment rewritten from
> `H^n(R(g_* ∘ f_*) M)` to `H^n(R(g ∘ f)_* M)` along
> `Stacks.Cohomology.RelativeMayerVietoris.pushforwardCompIso`.
>
> **The tag's functoriality in `ℱ` is not included**, which is why the attribute carries a clause;
> see the implementation notes.

```lean
theorem exists_spectralSequence_relativeLeray
    (M : DerivedCategory.Plus (SheafOfModules.{u} (structureSheafRing X))) :
    ∃ K : FilteredObject (CochainComplex (SheafOfModules.{u} (structureSheafRing Z)) ℤ) ℤᵒᵖ,
      (∀ n : ℤ, Nonempty (K.X.homology n ≅
        (DerivedCategory.Plus.homologyFunctor _ n).obj
          ((modulePushforward (f ≫ g)).rightDerivedFunctorPlus.obj M))) ∧
      K.filtration.IsDegreewiseFinite ∧
      ∀ (Fil : ∀ (_p n : ℤ), Subobject (K.X.X n))
        (_ : ∀ p n : ℤ, Fil p n = Subobject.mk ((K.filtration.ι.app (op p)).f n))
        (Zc : ∀ (_r _p n : ℤ), Subobject (K.X.X n))
        (_ : ∀ r p n : ℤ, Zc r p n =
          Fil p n ⊓ (Subobject.pullback (K.X.d n (n + 1))).obj (Fil (p + r) (n + 1)))
        (Dc : ∀ (_r _p n : ℤ), Subobject (K.X.X n))
        (_ : ∀ r p n : ℤ, Dc r p n = Zc (r - 1) (p + 1) n ⊔
          (Subobject.«exists» (K.X.d (n - 1) n)).obj (Zc (r - 1) (p - r + 1) (n - 1)))
        (FH : ∀ (n _p : ℤ), Subobject (K.X.homology n))
        (_ : ∀ n p : ℤ, FH n p =
          imageSubobject (HomologicalComplex.homologyMap (K.filtration.ι.app (op p)) n)),
      ∃ (E : CohomologicalSpectralSequence (SheafOfModules.{u} (structureSheafRing Z)) 0)
        (_ : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q), (E.page r hr).X (p, q) ≅
          cokernel (Subobject.ofLE _ _ (inf_le_right : Dc r p n ⊓ Zc r p n ≤ Zc r p n))),
        (∀ p q : ℤ, Nonempty ((E.page 2 zero_le_two).X (p, q) ≅
          ((modulePushforward g).rightDerivedPlus p).obj
            ((DerivedCategory.Plus.homologyFunctor _ q).obj
              ((modulePushforward f).rightDerivedFunctorPlus.obj M)))) ∧
        (∀ n : ℤ, {p : ℤ | ¬ IsZero ((E.page 0).X (p, n - p))}.Finite) ∧
        (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ FH n a = ⊤ ∧ FH n b = ⊥) ∧
        (∀ p q : ℤ, ∃ b : ℤ, ∀ (r : ℤ) (hr : 0 ≤ r), b ≤ r →
          (E.page r hr).d (p, q) (p + r, q - r + 1) = 0) ∧
        (∀ p n : ℤ,
          IsGLB (Set.range fun r : ℕ =>
              Fil p n ⊓ (Subobject.pullback (K.X.d n (n + 1))).obj (Fil (p + r) (n + 1)) ⊔
                Fil (p + 1) n)
            (kernelSubobject (K.X.d n (n + 1)) ⊓ Fil p n ⊔ Fil (p + 1) n) ∧
          IsLUB (Set.range fun r : ℕ =>
              Fil p n ⊓ (Subobject.«exists» (K.X.d (n - 1) n)).obj (Fil (p - r) (n - 1)) ⊔
                Fil (p + 1) n)
            (imageSubobject (K.X.d (n - 1) n) ⊓ Fil p n ⊔ Fil (p + 1) n))
```

**`Stacks.Cohomology.RelativeLeray.exists_spectralSequence_relativeLeray_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeLeraySpectralSequence/Basic.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeLeraySpectralSequence/Basic.lean#L306). The attribute's comment: “the spectral sequence for a module, not its functoriality”.

> **[Stacks, Tag 01F6], the relative Leray spectral sequence for a module.** For morphisms of
> ringed spaces `f : X ⟶ Y` and `g : Y ⟶ Z` and an `𝒪_X`-module `ℱ` there is a spectral sequence
> with
>
> `E₂^{p,q} ≅ R^p g_*(R^q f_* ℱ)`
>
> converging to `R^{p+q}(g ∘ f)_* ℱ`, in the presentation and convergence convention of
> [Stacks, Tag 012M] and [Stacks, Tag 015N]. No hypothesis on `f`, on `g` or on `ℱ`.
>
> This is `exists_spectralSequence_relativeLeray` at the complex `ℱ[0]`: the `E₂` term and the
> abutment of that statement are *definitionally* `R^p g_*(R^q f_* ℱ)` and `R^n(g ∘ f)_* ℱ` there,
> because `Functor.rightDerivedPlus i` is `singleFunctor 0 ⋙ rightDerivedFunctorPlus ⋙
> homologyFunctor i` by definition.
>
> **The tag's functoriality in `ℱ` is not included**; see the implementation notes.

```lean
theorem exists_spectralSequence_relativeLeray_obj
    (F : SheafOfModules.{u} (structureSheafRing X)) :
    ∃ K : FilteredObject (CochainComplex (SheafOfModules.{u} (structureSheafRing Z)) ℤ) ℤᵒᵖ,
      (∀ n : ℤ, Nonempty (K.X.homology n ≅
        ((modulePushforward (f ≫ g)).rightDerivedPlus n).obj F)) ∧
      K.filtration.IsDegreewiseFinite ∧
      ∀ (Fil : ∀ (_p n : ℤ), Subobject (K.X.X n))
        (_ : ∀ p n : ℤ, Fil p n = Subobject.mk ((K.filtration.ι.app (op p)).f n))
        (Zc : ∀ (_r _p n : ℤ), Subobject (K.X.X n))
        (_ : ∀ r p n : ℤ, Zc r p n =
          Fil p n ⊓ (Subobject.pullback (K.X.d n (n + 1))).obj (Fil (p + r) (n + 1)))
        (Dc : ∀ (_r _p n : ℤ), Subobject (K.X.X n))
        (_ : ∀ r p n : ℤ, Dc r p n = Zc (r - 1) (p + 1) n ⊔
          (Subobject.«exists» (K.X.d (n - 1) n)).obj (Zc (r - 1) (p - r + 1) (n - 1)))
        (FH : ∀ (n _p : ℤ), Subobject (K.X.homology n))
        (_ : ∀ n p : ℤ, FH n p =
          imageSubobject (HomologicalComplex.homologyMap (K.filtration.ι.app (op p)) n)),
      ∃ (E : CohomologicalSpectralSequence (SheafOfModules.{u} (structureSheafRing Z)) 0)
        (_ : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q), (E.page r hr).X (p, q) ≅
          cokernel (Subobject.ofLE _ _ (inf_le_right : Dc r p n ⊓ Zc r p n ≤ Zc r p n))),
        (∀ p q : ℤ, Nonempty ((E.page 2 zero_le_two).X (p, q) ≅
          ((modulePushforward g).rightDerivedPlus p).obj
            (((modulePushforward f).rightDerivedPlus q).obj F))) ∧
        (∀ n : ℤ, {p : ℤ | ¬ IsZero ((E.page 0).X (p, n - p))}.Finite) ∧
        (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ FH n a = ⊤ ∧ FH n b = ⊥) ∧
        (∀ p q : ℤ, ∃ b : ℤ, ∀ (r : ℤ) (hr : 0 ≤ r), b ≤ r →
          (E.page r hr).d (p, q) (p + r, q - r + 1) = 0) ∧
        (∀ p n : ℤ,
          IsGLB (Set.range fun r : ℕ =>
              Fil p n ⊓ (Subobject.pullback (K.X.d n (n + 1))).obj (Fil (p + r) (n + 1)) ⊔
                Fil (p + 1) n)
            (kernelSubobject (K.X.d n (n + 1)) ⊓ Fil p n ⊔ Fil (p + 1) n) ∧
          IsLUB (Set.range fun r : ℕ =>
              Fil p n ⊓ (Subobject.«exists» (K.X.d (n - 1) n)).obj (Fil (p - r) (n - 1)) ⊔
                Fil (p + 1) n)
            (imageSubobject (K.X.d (n - 1) n) ⊓ Fil p n ⊔ Fil (p + 1) n))
```

**`Stacks.Cohomology.RelativeLeray.spectralSequencePlusPageTwoIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/RelativeLeray/BoundedBelowComplexes.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/RelativeLeray/BoundedBelowComplexes.lean#L115). The attribute's comment: “bounded below complexes, the second page”.

> **The second page of the relative Leray spectral sequence of a bounded below complex** is
> `R ᵖ g_*(H^q(R f_* -))`, naturally in the complex.
>
> This is `Stacks.Cohomology.LerayCard.pageTwoNatIsoDerived` for `Φ = R g_*` precomposed with
> `R f_*`: the right-hand side of that isomorphism is `H^q(-)` followed by the `p`-th right derived
> functor of `g_*` computed on `D⁺`, and `Stacks.DerivedIndexing.rightDerivedIso` identifies the
> latter with `R ᵖ g_*` in Mathlib's `ℕ`-indexed spelling.

```lean
def spectralSequencePlusPageTwoIso (p : ℕ) (q : ℤ) :
    spectralSequencePlus f g ⋙ SpectralSequence.pageFunctor _ _ 2 2 ⋙
        HomologicalComplex.eval _ _ ((p : ℤ), q) ≅
      (modulePushforward f).rightDerivedFunctorPlus ⋙
        DerivedCategory.Plus.homologyFunctor (ModuleSheaves Y) q ⋙
          (modulePushforward g).rightDerived p
```

**`Stacks.Cohomology.RelativeLeray.abutsTo_spectralSequencePlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/RelativeLeray/BoundedBelowComplexes.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/RelativeLeray/BoundedBelowComplexes.lean#L139). The attribute's comment: “bounded below complexes, the convergence”. References: EGA 0 (12.2.4), “abutment, complexes”; SGA 4 V (5.4), “convergence, ringed sp”.

> **The relative Leray spectral sequence of a bounded below complex converges to the
> cohomology of the derived direct image along the composite.** For every bounded below complex
> `K` of `𝒪_X`-modules, `spectralSequencePlus f g` at `K` has an infinity page at every bidegree
> and the terms `E_∞^{p, n-p}` are the successive quotients of a finite decreasing filtration of
> `H ⁿ(R (f ≫ g)_* K)`.
>
> Convergence of the truncation-tower spectral sequence of a right derived functor is
> `Stacks.Cohomology.LerayTruncation.abutsTo_spectralSequence_cohomologySpectralObjectFunctor_obj`,
> with abutment `H ⁿ(R g_*(R f_* K))`; the identification of that with `H ⁿ(R (f ≫ g)_* K)` is
> [Stacks, Tag 01F5].

```lean
theorem abutsTo_spectralSequencePlus (K : DerivedCategory.Plus (ModuleSheaves X)) :
    SpectralSequence.AbutsTo ((spectralSequencePlus f g).obj K)
      (fun n ↦ (DerivedCategory.Plus.homologyFunctor (ModuleSheaves Z) n).obj
        ((modulePushforward (f ≫ g)).rightDerivedFunctorPlus.obj K))
```

**`Stacks.Cohomology.RelativeLeray.spectralSequencePageTwoIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/RelativeLeray/SheavesOfModules.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/RelativeLeray/SheavesOfModules.lean#L77). The attribute's comment: “sheaves of modules, the second page”.

> **The second page of the relative Leray spectral sequence of a sheaf of modules** is
> `R ᵖ g_*(R^q f_* -)`, naturally in the module.

```lean
def spectralSequencePageTwoIso (p q : ℕ) :
    spectralSequence f g ⋙ SpectralSequence.pageFunctor _ _ 2 2 ⋙
        HomologicalComplex.eval _ _ ((p : ℤ), (q : ℤ)) ≅
      (modulePushforward f).rightDerived q ⋙ (modulePushforward g).rightDerived p
```

**`Stacks.Cohomology.RelativeLeray.abutsTo_spectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/RelativeLeray/SheavesOfModules.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/RelativeLeray/SheavesOfModules.lean#L93). The attribute's comment: “sheaves of modules, the convergence”. References: EGA 0 (12.2.4), “abutment”; SGA 4 V (5.4), “convergence, ringed sp”; SGA 2 VIII (3.1), “partial”.

> **The relative Leray spectral sequence of a sheaf of modules converges to the higher direct
> images along the composite.** For every `𝒪_X`-module `ℱ`, the spectral sequence has an infinity
> page at every bidegree and the terms `E_∞^{p, n-p}` are the successive quotients of a finite
> decreasing filtration of `R ⁿ(g ∘ f)_* ℱ`.

```lean
theorem abutsTo_spectralSequence (M : ModuleSheaves X) :
    SpectralSequence.AbutsTo ((spectralSequence f g).obj M)
      (fun n ↦ ((modulePushforward (f ≫ g)).rightDerivedPlus n).obj M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.13, Tag 01EY](https://stacks.math.columbia.edu/tag/01EY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
