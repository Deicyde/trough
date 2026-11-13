---
declaration: section
origin: cited
lean: SheafOfModules.injective_val, SheafOfModules.forget_preservesInjectiveObjects, Stacks.Adequate.affineSectionsAcyclic_of_sections, Stacks.Cohomology.SiteDerivedForget.rightDerivedForgetEvaluationIso, Stacks.Cohomology.SiteDerivedForget.rightDerivedForgetEvaluationIso_cocycles, Stacks.Cohomology.SiteDerivedForget.rightDerivedForgetRestrictedEvaluationIso, Stacks.Cohomology.SiteDerivedForget.rightDerivedForgetRestrictedEvaluationIso_eq, Stacks.Cohomology.SiteDerivedForget.rightDerivedForgetEvaluationIso_naturality
statement: formalized
proof: formalized
---

# 21.12 Cohomology of modules

Section 21.12 of the Stacks Project, [Tag 03FA](https://stacks.math.columbia.edu/tag/03FA). 6 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03FB, a lemma

[Tag 03FB](https://stacks.math.columbia.edu/tag/03FB) in the Stacks Project.

**`SheafOfModules.injective_val`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Injective.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Injective.lean#L84). The attribute's comment: “an injective sheaf of modules, viewed as a presheaf of modules”.

> **An injective sheaf of modules is injective as a presheaf of modules.** This is the step of
> [Stacks, Tag 01EP] which uses Stacks Tag 015Z.

```lean
instance SheafOfModules.injective_val (I : SheafOfModules.{v} R) [Injective I] :
    Injective I.val
```

**`SheafOfModules.forget_preservesInjectiveObjects`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Injective.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Injective.lean#L102). The attribute's comment: “the forgetful functor to presheaves of modules preserves injective objects”.

> **The forgetful functor from sheaves of `R`-modules to presheaves of `R`-modules preserves
> injective objects.** This is the functorial form of the statement that an injective sheaf of
> modules is injective as a presheaf of modules.

```lean
instance SheafOfModules.forget_preservesInjectiveObjects :
    (SheafOfModules.forget.{v} R).PreservesInjectiveObjects
```

## Tag 06YK, a lemma

[Tag 06YK](https://stacks.math.columbia.edu/tag/06YK) in the Stacks Project.

**`Stacks.Adequate.affineSectionsAcyclic_of_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequatorVanishing.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/AdequatorVanishing.lean#L289). The attribute's comment: “the module-valued half for the affine-section functor: its right derived functors are computed on sections over the algebras of the site, evaluation of presheaves of modules being exact”.

> **[Stacks, Tag 06YK] for the affine-section functor.** The affine-section functor is right
> acyclic at a sheaf of modules as soon as its module-valued sections over every algebra of the
> site are, evaluation of presheaves of modules being exact.

```lean
public theorem affineSectionsAcyclic_of_sections (A : CommRingCat.{u}) (f : Spec A ⟶ S)
    (F : SheafOfModules.{max u m} B.structureSheaf)
    (hsec : ∀ (k : ℕ), 0 < k →
      ∀ X : (AdequateFunctor.AlgebrasInSite A (schemeSizeBelow B.cutoff))ᵒᵖᵒᵖ,
      IsZero (((affineSectionsFunctor.{u, max u m} B A f ⋙
        PresheafOfModules.evaluation
          (AdequateFunctor.algebraRingDiagramOn
            (AdequateFunctor.siteAlgebraInclusion A (schemeSizeBelow B.cutoff)))
          X).rightDerived k).obj F)) :
    AffineSectionsAcyclic.{u, m} B A f F
```

**`Stacks.Cohomology.SiteDerivedForget.rightDerivedForgetEvaluationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/ModuleValuedDerivedSections.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/ModuleValuedDerivedSections.lean#L275). The attribute's comment: “module-valued derived sections”. References: SGA 4 V (2.4.2), “(X), special case”.

> Evaluation at `U` of the derived inclusion of module sheaves into module presheaves
> is canonically the module-valued right derived functor of sections over `U`.

```lean
public noncomputable def rightDerivedForgetEvaluationIso (X : RingedSite.{u, u, u})
    (U : X.C) (p : ℕ) :
    (SheafOfModules.forget (Stacks.SheafOfModules.Tensor.ringSheaf X.O)).rightDerived p ⋙
        PresheafOfModules.evaluation (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj (op U) ≅
      (SheafOfModules.evaluation (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
        (op U)).rightDerived p
```

**`Stacks.Cohomology.SiteDerivedForget.rightDerivedForgetEvaluationIso_cocycles`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/ModuleValuedDerivedSections.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/ModuleValuedDerivedSections.lean#L291). The attribute's comment: “canonical comparison on injective resolutions”.

> The comparison is the one induced by evaluating the cocycles of an injective
> resolution. In particular it is independent of the chosen resolution.

```lean
public theorem rightDerivedForgetEvaluationIso_cocycles (X : RingedSite.{u, u, u})
    (U : X.C) (p : ℕ) (F : SheafOfModules (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (I : InjectiveResolution F) :
    let P := SheafOfModules.forget (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
    let E := SheafOfModules.evaluation (Stacks.SheafOfModules.Tensor.ringSheaf X.O) (op U)
    let G := PresheafOfModules.evaluation (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj (op U)
    let K := (P.mapHomologicalComplex (ComplexShape.up ℕ)).obj I.cocomplex
    (rightDerivedForgetEvaluationIso X U p).hom.app F =
      (G.mapIso (I.isoRightDerivedObj P p)).hom ≫
      (G.mapIso ((HomologicalComplex.homologyFunctorIso _ _ p).app K)).hom ≫
      ((K.sc p).mapHomologyIso G).inv ≫
      ((HomologicalComplex.homologyFunctorIso _ _ p).app
        ((G.mapHomologicalComplex _).obj K)).inv ≫
      (I.isoRightDerivedObj E p).inv
```

**`Stacks.Cohomology.SiteDerivedForget.rightDerivedForgetRestrictedEvaluationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/ModuleValuedDerivedSections.lean, line 312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/ModuleValuedDerivedSections.lean#L312). The attribute's comment: “derived sections after scalar restriction”.

> The derived inclusion followed by evaluation at `U` and restriction of scalars to
> `O(V)` agrees with derived sections at `U` viewed as `O(V)`-modules.

```lean
public noncomputable def rightDerivedForgetRestrictedEvaluationIso
    (X : RingedSite.{u, u, u}) {U V : X.C} (f : U ⟶ V) (p : ℕ) :
    (SheafOfModules.forget (Stacks.SheafOfModules.Tensor.ringSheaf X.O)).rightDerived p ⋙
        (PresheafOfModules.evaluation (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj (op U) ⋙
          ModuleCat.restrictScalars
            ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj.map f.op).hom) ≅
      (SheafOfModules.evaluation (Stacks.SheafOfModules.Tensor.ringSheaf X.O) (op U) ⋙
        ModuleCat.restrictScalars
          ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj.map f.op).hom).rightDerived p
```

**`Stacks.Cohomology.SiteDerivedForget.rightDerivedForgetRestrictedEvaluationIso_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/ModuleValuedDerivedSections.lean, line 358](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/ModuleValuedDerivedSections.lean#L358). The attribute's comment: “scalar-restriction coherence”.

> The restricted comparison is obtained from the same module-valued comparison,
> not chosen independently after restriction of scalars.

```lean
public theorem rightDerivedForgetRestrictedEvaluationIso_eq
    (X : RingedSite.{u, u, u}) {U V : X.C} (f : U ⟶ V) (p : ℕ)
    (F : SheafOfModules (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    (rightDerivedForgetRestrictedEvaluationIso X f p).hom.app F =
      (ModuleCat.restrictScalars
        ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj.map f.op).hom).map
        ((rightDerivedForgetEvaluationIso X U p).hom.app F) ≫
      (rightDerivedEvaluationRestrictScalarsIso X f p F).hom
```

**`Stacks.Cohomology.SiteDerivedForget.rightDerivedForgetEvaluationIso_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/ModuleValuedDerivedSections.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/ModuleValuedDerivedSections.lean#L386). The attribute's comment: “module-valued restriction compatibility”.

> The module-valued comparison commutes with restriction from `V` to `U`, with the
> target sections viewed as modules over the ring of sections on `V`.

```lean
public theorem rightDerivedForgetEvaluationIso_naturality (X : RingedSite.{u, u, u})
    (p : ℕ) (F : SheafOfModules (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    {U V : X.C} (f : U ⟶ V) :
    (PresheafOfModules.restriction (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj f.op).app
        (((SheafOfModules.forget
          (Stacks.SheafOfModules.Tensor.ringSheaf X.O)).rightDerived p).obj F) ≫
      (rightDerivedForgetRestrictedEvaluationIso X f p).hom.app F =
    (rightDerivedForgetEvaluationIso X V p).hom.app F ≫
      (NatTrans.rightDerived
        (Functor.whiskerLeft (SheafOfModules.forget (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
          (PresheafOfModules.restriction
            (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj f.op)) p).app F
```

**`Stacks.Cohomology.SiteDerivedForget.rightDerivedForgetCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/ModuleValuedDerivedSections.lean, line 618](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/ModuleValuedDerivedSections.lean#L618). The attribute's comment: “higher derived functors”. References: SGA 4 IV (4.8), “more general”; SGA 4 V (2.4.2), “special case”.

> The right derived functor of the inclusion of module sheaves in module presheaves, viewed as
> a presheaf of abelian groups, is canonically the cohomology presheaf. This is natural both in the
> coefficient sheaf and in objects of the site.

```lean
public noncomputable def rightDerivedForgetCohomologyIso (X : RingedSite.{u, u, u}) (p : ℕ) :
    (SheafOfModules.forget (Stacks.SheafOfModules.Tensor.ringSheaf X.O)).rightDerived p ⋙
        PresheafOfModules.toPresheaf (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj ≅
      SheafOfModules.toSheaf (Stacks.SheafOfModules.Tensor.ringSheaf X.O) ⋙
        Sheaf.cohomologyPresheafFunctor X.J p
```

**`Stacks.Cohomology.SiteDerivedForget.rightDerivedForgetCohomologyIso_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/ModuleValuedDerivedSections.lean, line 634](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/ModuleValuedDerivedSections.lean#L634). The attribute's comment: “compatibility with restriction”.

> The canonical identification of the derived presheaf with the cohomology presheaf commutes
> with restriction along any morphism of the site.

```lean
public theorem rightDerivedForgetCohomologyIso_naturality (X : RingedSite.{u, u, u}) (p : ℕ)
    (F : SheafOfModules (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) {U V : X.C} (f : U ⟶ V) :
    (((PresheafOfModules.toPresheaf (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj).obj
      (((SheafOfModules.forget
        (Stacks.SheafOfModules.Tensor.ringSheaf X.O)).rightDerived p).obj F)).map f.op) ≫
        ((rightDerivedForgetCohomologyIso X p).hom.app F).app (op U) =
      ((rightDerivedForgetCohomologyIso X p).hom.app F).app (op V) ≫
        (((Sheaf.cohomologyPresheafFunctor X.J p).obj
          ((SheafOfModules.toSheaf
            (Stacks.SheafOfModules.Tensor.ringSheaf X.O)).obj F)).map f.op)
```

Declarations registered for the tag:

- [`SheafOfModules.Finite.forgetPreservesFiniteLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.Finite.forgetPreservesFiniteLimits#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/ModuleValuedDerivedSections.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/ModuleValuedDerivedSections.lean#L116) (StacksFrontier): “left exactness”.

## Tag 03FC, a lemma

[Tag 03FC](https://stacks.math.columbia.edu/tag/03FC) in the Stacks Project.

**`Stacks.CechSite.moduleCechCohomology_zero_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/InjectiveModuleVanishing.lean, line 522](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/InjectiveModuleVanishing.lean#L522). The attribute's comment: “degree zero”.

> **Stacks Project, Tag 03FC (degree zero).** Degree-zero Čech cohomology of a sheaf of
> modules for a covering is its underlying additive group of sections over the covered object.

```lean
public theorem moduleCechCohomology_zero_iso :
    Nonempty
      (cechCohomology E
          ((SheafOfModules.toSheaf (Stacks.SheafOfModules.Tensor.ringSheaf X.O)).obj I).obj 0 ≅
        ((SheafOfModules.toSheaf (Stacks.SheafOfModules.Tensor.ringSheaf X.O)).obj I).obj.obj
          (op U))
```

**`Stacks.CechSite.injective_moduleCechCohomology_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/InjectiveModuleVanishing.lean, line 536](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/InjectiveModuleVanishing.lean#L536). The attribute's comment: “positive degrees”.

> **Stacks Project, Tag 03FC (positive degrees).** The positive-degree Čech cohomology of
> an injective sheaf of modules vanishes for every family of morphisms.

```lean
public theorem injective_moduleCechCohomology_isZero (p : ℕ) (hp : 0 < p) :
    IsZero
      (cechCohomology E
        ((SheafOfModules.toSheaf (Stacks.SheafOfModules.Tensor.ringSheaf X.O)).obj I).obj p)
```

**`Stacks.CechSite.moduleCechCohomology_zero_iso_sheafOfRings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/InjectiveModuleVanishing.lean, line 588](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/InjectiveModuleVanishing.lean#L588). The attribute's comment: “degree zero”.

> **Stacks Project, Tag 03FC (degree zero).** Degree-zero Čech cohomology of a sheaf of
> modules for a covering is its underlying additive group of sections over the covered object.

```lean
public theorem moduleCechCohomology_zero_iso_sheafOfRings :
    Nonempty
      (cechCohomology E ((SheafOfModules.toSheaf O).obj I).obj 0 ≅
        ((SheafOfModules.toSheaf O).obj I).obj.obj (op U))
```

**`Stacks.CechSite.injective_moduleCechCohomology_isZero_sheafOfRings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/InjectiveModuleVanishing.lean, line 600](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/InjectiveModuleVanishing.lean#L600). The attribute's comment: “positive degrees”.

> **Stacks Project, Tag 03FC (positive degrees).** The positive-degree Čech cohomology of
> an injective sheaf of modules vanishes for every family of morphisms.

```lean
public theorem injective_moduleCechCohomology_isZero_sheafOfRings (p : ℕ) (hp : 0 < p) :
    IsZero
      (cechCohomology E ((SheafOfModules.toSheaf O).obj I).obj p)
```

## Tag 03FD, a lemma

[Tag 03FD](https://stacks.math.columbia.edu/tag/03FD) in the Stacks Project.

**`AlgebraicGeometry.Space.moduleCohomologyForgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleCohomologyAbelianComparison.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ModuleCohomologyAbelianComparison.lean#L396). The attribute's comment: “on the small étale site of an algebraic space”.

> **Stacks 03FD on the small étale site of an algebraic space.**  The cohomology of an
> `𝒪_X`-module `ℱ`, computed in `𝒪_X`-modules and read in abelian groups, is the cohomology of its
> underlying abelian sheaf (with sections raised to `u + 1`), naturally in `ℱ`.

```lean
def moduleCohomologyForgetIso (n : ℕ) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    (globalSectionsFunctor.{u + 1, u, u, u}
          (Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS X.1 X.2).O)).rightDerived n ⋙
        forget₂ _ AddCommGrpCat.{u + 1} ≅
      moduleToAbelianSheaf B S hS X ⋙
        (Sheaf.Γ (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u + 1}).rightDerived n
```

**`ModuleSheafCohomology.moduleSheafCohomologyIsoUnderlying`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/GlobalSections/ModuleCohomologyComparison.lean, line 1089](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/GlobalSections/ModuleCohomologyComparison.lean#L1089). References: SGA 4 V (3.5).

> **Stacks 03FD.** For a sheaf of rings `R` on a site, deriving sections in the category of
> `R`-module sheaves and then forgetting to abelian groups gives the same cohomology as first
> forgetting to an abelian sheaf and deriving there. The comparison is natural in the module
> sheaf, holds globally and over every object of the site, and is compatible in degree zero with
> the canonical maps to right-derived functors.

```lean
public theorem moduleSheafCohomologyIsoUnderlying (R : Sheaf J RingCat.{u}) :
    ∃ eSite : ∀ i : ℕ,
        (SheafOfModules.toSheaf.{u} R ⋙ Sheaf.Γ J Ab.{u}).rightDerived i ≅
          SheafOfModules.toSheaf.{u} R ⋙ (Sheaf.Γ J Ab.{u}).rightDerived i,
      (SheafOfModules.toSheaf.{u} R ⋙ Sheaf.Γ J Ab.{u}).toRightDerivedZero ≫
          (eSite 0).hom =
        Functor.whiskerLeft (SheafOfModules.toSheaf.{u} R)
          (Sheaf.Γ J Ab.{u}).toRightDerivedZero ∧
      ∀ U : C,
        ∃ eU : ∀ i : ℕ,
            (SheafOfModules.toSheaf.{u} R ⋙
                (sheafSections J Ab.{u}).obj (op U)).rightDerived i ≅
              SheafOfModules.toSheaf.{u} R ⋙
                ((sheafSections J Ab.{u}).obj (op U)).rightDerived i,
          (SheafOfModules.toSheaf.{u} R ⋙
                (sheafSections J Ab.{u}).obj (op U)).toRightDerivedZero ≫
              (eU 0).hom =
            Functor.whiskerLeft (SheafOfModules.toSheaf.{u} R)
              ((sheafSections J Ab.{u}).obj (op U)).toRightDerivedZero
```

## Tag 060L, a lemma

[Tag 060L](https://stacks.math.columbia.edu/tag/060L) in the Stacks Project.

**`Stacks.Cohomology.SheafProducts.isIso_piComparison_cohomology_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfAProduct.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfAProduct.lean#L42). The attribute's comment: “degree zero”.

> **Degree-zero cohomology commutes with arbitrary products of abelian sheaves**: for a family
> `(F i)` of abelian sheaves on a site and an object `U`, the canonical map
> `H^0(U, ∏ F) ⟶ ∏ H^0(U, F i)` is an isomorphism.

```lean
public theorem isIso_piComparison_cohomology_zero {I : Type x}
    (F : I → Sheaf J AddCommGrpCat.{v}) (U : C) [HasProduct F]
    [HasProduct fun i ↦
      (Sheaf.cohomologyPresheafFunctor J 0 ⋙
        (evaluation Cᵒᵖ AddCommGrpCat.{w'}).obj (op U)).obj (F i)] :
    IsIso (piComparison
      (Sheaf.cohomologyPresheafFunctor J 0 ⋙
        (evaluation Cᵒᵖ AddCommGrpCat.{w'}).obj (op U)) F)
```

**`Stacks.Cohomology.SheafProducts.mono_piComparison_cohomology_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfAProduct.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfAProduct.lean#L67). The attribute's comment: “degree one”.

> **Degree-one cohomology of a product of abelian sheaves injects into the product**: for a
> family `(F i)` of abelian sheaves on a site and an object `U`, the canonical map
> `H^1(U, ∏ F) ⟶ ∏ H^1(U, F i)` is a monomorphism.

```lean
public theorem mono_piComparison_cohomology_one {I : Type x}
    (F : I → Sheaf J AddCommGrpCat.{v}) (U : C) [HasProduct F]
    [HasProduct fun i ↦
      (Sheaf.cohomologyPresheafFunctor J 1 ⋙
        (evaluation Cᵒᵖ AddCommGrpCat.{w'}).obj (op U)).obj (F i)] :
    Mono (piComparison
      (Sheaf.cohomologyPresheafFunctor J 1 ⋙
        (evaluation Cᵒᵖ AddCommGrpCat.{w'}).obj (op U)) F)
```

## Tag 093X, a lemma

[Tag 093X](https://stacks.math.columbia.edu/tag/093X) in the Stacks Project.

**`Stacks.Injectives.injective_restriction_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/InjectiveRestrictionAlongAMono.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/InjectiveRestrictionAlongAMono.lean#L135).

> On a ringed site, restriction of an injective sheaf of modules over the
> structure sheaf along a monomorphism of objects of the site is surjective.

```lean
public theorem injective_restriction_surjective (X : AlgebraicGeometry.RingedSite.{u, u, u})
    {U' U : X.C} (a : U' ⟶ U)
    [Mono a]
    (I : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) [Injective I] :
    Function.Surjective (I.val.presheaf.map a.op)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.12, Tag 03FA](https://stacks.math.columbia.edu/tag/03FA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
