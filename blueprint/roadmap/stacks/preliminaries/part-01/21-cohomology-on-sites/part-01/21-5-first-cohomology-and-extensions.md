---
declaration: section
origin: cited
lean: Stacks.Cohomology.SiteModules.extOneEquivFirstCohomology, Stacks.Cohomology.SiteModules.extOneEquivFirstCohomology_extClass, Stacks.Cohomology.SiteModules.extOneEquivFirstCohomology_unique, Stacks.Cohomology.SiteModules.extOneEquivFirstCohomology_naturality, ModuleSheafCohomology.moduleSheafCohomologyIsoUnderlying
statement: formalized
proof: formalized
---

# 21.5 First cohomology and extensions

Section 21.5 of the Stacks Project, [Tag 03F0](https://stacks.math.columbia.edu/tag/03F0). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03F1, a lemma

[Tag 03F1](https://stacks.math.columbia.edu/tag/03F1) in the Stacks Project.

**`Stacks.Cohomology.SiteModules.extOneEquivFirstCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FirstCohomologyAndExtensions.lean, line 368](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FirstCohomologyAndExtensions.lean#L368). The attribute's comment: “canonical bijection”.

> **Stacks 03F1.** For a ringed site `(C, O)` and a sheaf of `O`-modules `M`, first
> extensions of the structure sheaf by `M` are canonically first cohomology.

```lean
def extOneEquivFirstCohomology (R : Sheaf J RingCat.{u}) (M : SheafOfModules.{u} R) :
    Ext (SheafOfModules.unit R) M 1 ≃+ (cohomologyFunctor R 1).obj M
```

**`Stacks.Cohomology.SiteModules.extOneEquivFirstCohomology_extClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FirstCohomologyAndExtensions.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FirstCohomologyAndExtensions.lean#L392). The attribute's comment: “image of an extension”.

> **Stacks 03F1.** The class of the extension `0 → M → E → O → 0` goes to the image of the
> unit global section under the connecting morphism of the extension.

```lean
theorem extOneEquivFirstCohomology_extClass (R : Sheaf J RingCat.{u})
    (M : SheafOfModules.{u} R) (E : SheafOfModules.{u} R) (f : M ⟶ E)
    (g : E ⟶ SheafOfModules.unit R) (w : f ≫ g = 0)
    (hS : (ShortComplex.mk f g w).ShortExact) :
    extOneEquivFirstCohomology R M hS.extClass =
      (eqToHom (universalCohomologyDeltaFunctor_functor R 1)).app M
        ((universalCohomologyDeltaFunctor R).δ hS 0
        ((cohomologyZeroMap R).app (SheafOfModules.unit R)
            (SheafOfModules.unitHomEquiv (SheafOfModules.unit R) (𝟙 _))))
```

**`Stacks.Cohomology.SiteModules.extOneEquivFirstCohomology_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FirstCohomologyAndExtensions.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FirstCohomologyAndExtensions.lean#L464). The attribute's comment: “uniqueness”.

> **Stacks 03F1.** The connecting-image formula determines the identification uniquely.

```lean
theorem extOneEquivFirstCohomology_unique (R : Sheaf J RingCat.{u})
    (M : SheafOfModules.{u} R)
    (e : Ext (SheafOfModules.unit R) M 1 ≃+ (cohomologyFunctor R 1).obj M)
    (he : ∀ (E : SheafOfModules.{u} R) (f : M ⟶ E)
      (g : E ⟶ SheafOfModules.unit R) (w : f ≫ g = 0)
      (hS : (ShortComplex.mk f g w).ShortExact),
      e hS.extClass =
        (eqToHom (universalCohomologyDeltaFunctor_functor R 1)).app M
          ((universalCohomologyDeltaFunctor R).δ hS 0
            ((cohomologyZeroMap R).app (SheafOfModules.unit R)
              (SheafOfModules.unitHomEquiv (SheafOfModules.unit R) (𝟙 _))))) :
    e = extOneEquivFirstCohomology R M
```

**`Stacks.Cohomology.SiteModules.extOneEquivFirstCohomology_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FirstCohomologyAndExtensions.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/FirstCohomologyAndExtensions.lean#L485). The attribute's comment: “naturality”.

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

**`ModuleSheafCohomology.moduleSheafCohomologyIsoUnderlying`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/GlobalSections/ModuleCohomologyComparison.lean, line 1090](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/GlobalSections/ModuleCohomologyComparison.lean#L1090). The attribute's comment: “the degree one case”. References: SGA 4 V (3.5).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
