---
declaration: section
origin: cited
lean: Stacks.Cohomology.CompositeRightDerived.cohomology, Stacks.Cohomology.SectionCohomology.cohomologyIso, CategoryTheory.Functor.sectionsEquivHom, Stacks.Cohomology.SiteSections.siteCohomologyIso, Stacks.Cohomology.CompositeRightDerived.siteCohomology, CategoryTheory.InjectiveResolution.isoRightDerivedObj, Stacks.Cohomology.SiteModuleCohomology.siteModuleCohomology, Stacks.Cohomology.SiteModules.cohomologyFunctor
statement: formalized
proof: formalized
---

# 21.2 Cohomology of sheaves

Section 21.2 of the Stacks Project, [Tag 01FT](https://stacks.math.columbia.edu/tag/01FT). 7 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 071C, an equation

[Tag 071C](https://stacks.math.columbia.edu/tag/071C) in the Stacks Project.

**`Stacks.Cohomology.CompositeRightDerived.cohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/CompositeRightDerivedFunctors.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/CompositeRightDerivedFunctors.lean#L302). The attribute's comment: “the functor H^i(U, -) = R^i Γ(U, -)”.

> The `p`-th cohomology functor over an object,
> `H^p(U, -) = R^p \Gamma(U, -) : Sheaf J Ab \to Ab`.

```lean
noncomputable def cohomology (J : GrothendieckTopology C) (U : C) (p : ℕ) :
    Sheaf J (Ab.{u}) ⥤ Ab.{u}
```

**`Stacks.Cohomology.SectionCohomology.cohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/SectionCohomologyInjective.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/SectionCohomologyInjective.lean#L57). The attribute's comment: “H^i(U, F) = H^i(Γ(U, I^•)) for any injective resolution F[0] → I^•”.

> **Stacks Project, Tag 071C.** The source's displayed equation: the `i`-th cohomology group
> `H^i(U, F)` of an abelian sheaf `F` over an object `U` of the site, the `i`-th right derived
> functor of the sections functor `Γ(U, -)` evaluated at `F`, is canonically the `i`-th
> cohomology of the complex of sections `Γ(U, I^•)` of any injective resolution `I` of `F`.

```lean
def cohomologyIso (U : C) (F : Sheaf J Ab.{u}) (I : InjectiveResolution F) (i : ℕ) :
    (cohomology J U i).obj F ≅
      (((sections J U).mapHomologicalComplex (ComplexShape.up ℕ)).obj I.cocomplex).homology i
```

## Tag 071D, an equation

[Tag 071D](https://stacks.math.columbia.edu/tag/071D) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.sectionsEquivHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sectionsEquivHom#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch21.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch21.lean#L17) (StacksFrontier): “global sections of a presheaf of sets as morphisms from the final presheaf (the constant presheaf on a singleton)”.

## Tag 071E, an equation

[Tag 071E](https://stacks.math.columbia.edu/tag/071E) in the Stacks Project.

**`Stacks.Cohomology.SiteSections.siteCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/SiteCohomologyByInjectiveResolution.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/SiteCohomologyByInjectiveResolution.lean#L43).

> **Stacks Project, Tag 071E.** The source's displayed equation: the `i`-th cohomology group
> of an abelian sheaf `F` on the site `C` is canonically the `i`-th cohomology of the complex of
> global sections of any injective resolution of `F`.

```lean
def siteCohomologyIso (F : Sheaf J Ab.{u}) (I : InjectiveResolution F) (i : ℕ) :
    (siteCohomology J i).obj F ≅
      (((siteSections J).mapHomologicalComplex (ComplexShape.up ℕ)).obj I.cocomplex).homology i
```

**`Stacks.Cohomology.CompositeRightDerived.siteCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/CompositeRightDerivedFunctors.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/HigherDirectImage/CompositeRightDerivedFunctors.lean#L316). The attribute's comment: “the functor H^i(C, -) = R^i Γ(C, -), the tag's "in other words"”. References: SGA 4½ Arcata (1.6.5).

> **Stacks Project, Tag 071E.** The `p`-th cohomology functor over the whole site,
> `H^p(C, -) = R^p \Gamma(C, -) : Sheaf J Ab \to Ab`.
>
> This is the definition the tag's displayed equation makes: the global sections functor here is
> `Γ(C, -) = Mor_{PSh(C)}(e, -)` of [Stacks Project, Tag 071D], and the tag's own gloss of the
> equation is "in other words, it is the `i`-th right derived functor of the global sections
> functor". The computation of it from a chosen injective resolution is
> `Stacks.Cohomology.SiteSections.siteCohomologyIso`.

```lean
noncomputable def siteCohomology (J : GrothendieckTopology C) (p : ℕ) :
    Sheaf J (Ab.{u}) ⥤ Ab.{u}
```

## Tag 071F, an equation

[Tag 071F](https://stacks.math.columbia.edu/tag/071F) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.InjectiveResolution.isoRightDerivedObj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.InjectiveResolution.isoRightDerivedObj#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Cohomology/HigherDirectImage/ByInjectiveResolution.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Sites/Cohomology/HigherDirectImage/ByInjectiveResolution.lean#L44) (StacksCore): “The canonical computation by a chosen injective resolution.”. References: EGA 0 (11.5.2.4), “special case”.

## Tag 071G, an equation

[Tag 071G](https://stacks.math.columbia.edu/tag/071G) in the Stacks Project.

**`Stacks.Cohomology.SiteModuleCohomology.siteModuleCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/TruncationTowerVocabulary.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/TruncationTowerVocabulary.lean#L89). The attribute's comment: “the right derived functors of `Γ(U, -)`, computed from an injective resolution”.

> **Cohomology of a sheaf of modules over an object of a ringed site (Stacks 071G).**  The
> `p`-th cohomology `Hᵖ(U, F)` is the `p`-th right derived functor of the sections functor
> `Γ(U, -) = SheafOfModules.evaluation O (op U)`, evaluated at `F`; it is a module over the ring
> `O(U)` of sections of the structure sheaf over `U`.

```lean
def siteModuleCohomology (O : Sheaf J RingCat.{wRing})
    [HasSheafify J AddCommGrpCat.{wModule}]
    [J.WEqualsLocallyBijective AddCommGrpCat.{wModule}]
    [EnoughInjectives (SheafOfModules.{wModule} O)]
    (U : C) (p : ℕ) (F : SheafOfModules.{wModule} O) :
    ModuleCat.{wModule} (O.obj.obj (op U))
```

## Tag 071H, an equation

[Tag 071H](https://stacks.math.columbia.edu/tag/071H) in the Stacks Project.

**`Stacks.Cohomology.SiteModules.cohomologyFunctor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfModules.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfModules.lean#L172). The attribute's comment: “cohomology of modules on the whole site”. References: EGA 0 (12.1.2), “more general”.

> **Stacks Project, Tag 071H.** The cohomology of sheaves of modules on a small site, with
> scalars in the ring of global sections of the structure sheaf.

```lean
abbrev cohomologyFunctor {C : Type u} [SmallCategory C] {J : GrothendieckTopology C}
    (R : Sheaf J RingCat.{u}) (i : ℕ) :
    SheafOfModules.{u} R ⥤ ModuleCat.{u} (RingCat.sectionsSubring R.obj)
```

**`Stacks.Cohomology.SiteModules.globalModuleCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfModules.lean, line 418](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfModules.lean#L418).

> **Stacks Project, Tag 071H.** Cohomology of `O`-modules on the whole site, valued in
> `Γ(C, O)`-modules. The independent module universe is enlarged to contain the site and the
> structure rings.

```lean
def globalModuleCohomology (n : ℕ) :
    SheafOfModules.{max u v r w} O ⥤ ModuleCat.{max u v r w} (GlobalSectionRing O)
```

**`Stacks.Cohomology.SiteModules.globalModuleCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfModules.lean, line 426](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfModules.lean#L426).

> **Stacks Project, Tag 071H.** The source's equation: global module cohomology is
> canonically the cohomology of the sectionwise global sections of any injective resolution,
> over the ring `Γ(C, O)`.

```lean
def globalModuleCohomologyIso (M : SheafOfModules.{max u v r w} O)
    (I : InjectiveResolution M) (n : ℕ) :
    (globalModuleCohomology.{u, v, r, w} O n).obj M ≅
      (((globalSectionsFunctor O).mapHomologicalComplex (ComplexShape.up ℕ)).obj
        I.cocomplex).homology n
```

**`Stacks.Cohomology.SiteModules.exists_universal_cohomologyDeltaFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfModules.lean, line 455](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfModules.lean#L455). The attribute's comment: “the universal cohomological delta-functor”.

> **Stacks Project, Tag 071H.** The cohomology functors, with their given action on
> morphisms, form a universal cohomological `δ`-functor.

```lean
theorem exists_universal_cohomologyDeltaFunctor {C : Type u} [SmallCategory C]
    {J : GrothendieckTopology C} (R : Sheaf J RingCat.{u}) :
    ∃ H : DeltaFunctor (SheafOfModules.{u} R)
        (ModuleCat.{u} (RingCat.sectionsSubring R.obj)),
      (∀ i, H.functor i = cohomologyFunctor R i) ∧ H.IsUniversal
```

Declarations registered for the tag:

- [`CategoryTheory.InjectiveResolution.isoRightDerivedObj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.InjectiveResolution.isoRightDerivedObj#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfModules.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfModules.lean#L446) (StacksFrontier): “The canonical computation from a chosen injective resolution.”. References: EGA 0 (11.5.2.4), “special case”.
- [`CategoryTheory.InjectiveResolution.isoRightDerivedObj_hom_naturality`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.InjectiveResolution.isoRightDerivedObj_hom_naturality#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfModules.lean, line 449](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfModules.lean#L449) (StacksFrontier): “Naturality of the canonical computation, including change of resolution.”.

## Tag 071I, an equation

[Tag 071I](https://stacks.math.columbia.edu/tag/071I) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.rightDerived`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.rightDerived#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfModules.lean, line 468](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfModules.lean#L468) (StacksFrontier): “the higher direct image functors”. References: EGA 0 (11.4.3), “partial”; EGA 0 (12.2.1), “more general”; EGA 0 (13.2.4), “more general”; EGA 0 (13.6.1); SGA 1 XI (4.8), “more general”; SGA 2 VIII (1.2); SGA 3 I (5.2), “more general”; SGA 4 V (2.4.2); SGA 4 V (6.0), “more general”; SGA 4½ Arcata (1.6.5), “more general”; SGA 4½ Arcata (2.3.3), “more general”; SGA 4½ Etat 0 (4.1.5), “special case”.
- [`CategoryTheory.InjectiveResolution.isoRightDerivedObj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.InjectiveResolution.isoRightDerivedObj#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfModules.lean, line 482](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfModules.lean#L482) (StacksFrontier): “computation using an injective resolution”. References: EGA 0 (11.5.2.4), “special case”.
- [`CategoryTheory.InjectiveResolution.isoRightDerivedObj_hom_naturality`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.InjectiveResolution.isoRightDerivedObj_hom_naturality#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfModules.lean, line 485](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/CohomologyOfModules.lean#L485) (StacksFrontier): “naturality of the injective-resolution computation”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.2, Tag 01FT](https://stacks.math.columbia.edu/tag/01FT)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
