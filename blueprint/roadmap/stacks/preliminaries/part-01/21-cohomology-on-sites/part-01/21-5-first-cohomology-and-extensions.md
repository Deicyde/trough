---
declaration: section
origin: cited
lean: Stacks.Cohomology.SiteModules.extOneEquivFirstCohomology, Stacks.Cohomology.SiteModules.extOneEquivFirstCohomology_extClass_eq_coboundary, Stacks.Cohomology.SiteModules.extOneEquivFirstCohomology_unique_coboundary, Stacks.Cohomology.SiteModules.extOneEquivFirstCohomology_naturality, ModuleSheafCohomology.moduleSheafCohomologyIsoUnderlying
statement: formalized
proof: formalized
---

# 21.5 First cohomology and extensions

Section 21.5 of the Stacks Project, [Tag 03F0](https://stacks.math.columbia.edu/tag/03F0). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03F1, a lemma

[Tag 03F1](https://stacks.math.columbia.edu/tag/03F1) in the Stacks Project.

**`Stacks.Cohomology.SiteModules.extOneEquivFirstCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FirstCohomologyAndExtensions.lean, line 410](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FirstCohomologyAndExtensions.lean#L410). The attribute's comment: “canonical bijection”.

> **Stacks 03F1.** For a ringed site `(C, O)` and a sheaf of `O`-modules `M`, first
> extensions of the structure sheaf by `M` are canonically first cohomology.

```lean
def extOneEquivFirstCohomology (R : Sheaf J RingCat.{u}) (M : SheafOfModules.{u} R) :
    Ext (SheafOfModules.unit R) M 1 ≃+ (cohomologyFunctor R 1).obj M
```

**`Stacks.Cohomology.SiteModules.extOneEquivFirstCohomology_extClass_eq_coboundary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FirstCohomologyAndExtensions.lean, line 534](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FirstCohomologyAndExtensions.lean#L534). The attribute's comment: “image of an extension is the coboundary of 1”.

> **Stacks 03F1.** The class of the extension `0 → M → E → O → 0` goes to the image of
> `1 ∈ Γ(C, O)` under the coboundary `Γ(C, O) → H^1(C, M)` of the long exact cohomology sequence
> of the extension: the connecting map of the canonical right-derived `δ`-functor
> `Stacks.DerivedIndexing.rightDerivedDeltaFunctorOfEnoughInjectives` of global sections,
> precomposed with the canonical identification `Γ(C, O) → H^0(C, O)`.

```lean
theorem extOneEquivFirstCohomology_extClass_eq_coboundary (R : Sheaf J RingCat.{u})
    (M : SheafOfModules.{u} R) (E : SheafOfModules.{u} R) (f : M ⟶ E)
    (g : E ⟶ SheafOfModules.unit R) (w : f ≫ g = 0)
    (hS : (ShortComplex.mk f g w).ShortExact) :
    extOneEquivFirstCohomology R M hS.extClass =
      (Stacks.DerivedIndexing.rightDerivedDeltaFunctorOfEnoughInjectives
          (globalSectionsFunctor R)).δ hS 0
        ((globalSectionsFunctor R).toRightDerivedZero.app (SheafOfModules.unit R)
          (SheafOfModules.unitHomEquiv (SheafOfModules.unit R) (𝟙 _)))
```

**`Stacks.Cohomology.SiteModules.extOneEquivFirstCohomology_unique_coboundary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FirstCohomologyAndExtensions.lean, line 551](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FirstCohomologyAndExtensions.lean#L551). The attribute's comment: “uniqueness”.

> **Stacks 03F1.** The canonical bijection is the only additive bijection
> `Ext^1(O, M) ≃+ H^1(C, M)` sending every extension to the image of `1 ∈ Γ(C, O)` under the
> coboundary of the long exact cohomology sequence.

```lean
theorem extOneEquivFirstCohomology_unique_coboundary (R : Sheaf J RingCat.{u})
    (M : SheafOfModules.{u} R)
    (e : Ext (SheafOfModules.unit R) M 1 ≃+ (cohomologyFunctor R 1).obj M)
    (he : ∀ (E : SheafOfModules.{u} R) (f : M ⟶ E)
      (g : E ⟶ SheafOfModules.unit R) (w : f ≫ g = 0)
      (hS : (ShortComplex.mk f g w).ShortExact),
      e hS.extClass =
        (Stacks.DerivedIndexing.rightDerivedDeltaFunctorOfEnoughInjectives
            (globalSectionsFunctor R)).δ hS 0
          ((globalSectionsFunctor R).toRightDerivedZero.app (SheafOfModules.unit R)
            (SheafOfModules.unitHomEquiv (SheafOfModules.unit R) (𝟙 _)))) :
    e = extOneEquivFirstCohomology R M
```

**`Stacks.Cohomology.SiteModules.extOneEquivFirstCohomology_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FirstCohomologyAndExtensions.lean, line 573](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FirstCohomologyAndExtensions.lean#L573). The attribute's comment: “naturality”.

> **Stacks 03F1.** The identification is natural in the coefficient module sheaf.

```lean
theorem extOneEquivFirstCohomology_naturality (R : Sheaf J RingCat.{u})
    {M N : SheafOfModules.{u} R} (f : M ⟶ N) (e : Ext (SheafOfModules.unit R) M 1) :
    extOneEquivFirstCohomology R N
        ((Ext.mk₀ f).postcomp (SheafOfModules.unit R) (Nat.add_zero 1) e) =
      (cohomologyFunctor R 1).map f (extOneEquivFirstCohomology R M e)
```

## Tag 03F2, a lemma

[Tag 03F2](https://stacks.math.columbia.edu/tag/03F2) in the Stacks Project.

**`ModuleSheafCohomology.moduleSheafCohomologyIsoUnderlying`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/GlobalSections/ModuleCohomologyComparison.lean, line 1089](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/GlobalSections/ModuleCohomologyComparison.lean#L1089). The attribute's comment: “the degree one case”. References: SGA 4 V (3.5).

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

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.5, Tag 03F0](https://stacks.math.columbia.edu/tag/03F0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
