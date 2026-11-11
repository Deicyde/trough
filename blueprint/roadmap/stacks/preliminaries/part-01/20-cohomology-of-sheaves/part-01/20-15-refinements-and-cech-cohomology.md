---
declaration: section
origin: cited
lean: Stacks.Cohomology.CechRefinement.cechDiagram, Stacks.Cohomology.CechRefinement.colimitToCohomology, Stacks.Cohomology.CechRefinement.ι_colimitToCohomology, Stacks.Cohomology.CechRefinement.cechToDerivedGlobalSections_naturality_of_refinement, Stacks.Cohomology.CechRefinement.cechCohomologyToCohomology_naturality_of_refinement
statement: formalized
proof: formalized
---

# 20.15 Refinements and Čech cohomology

Section 20.15 of the Stacks Project, [Tag 09UY](https://stacks.math.columbia.edu/tag/09UY). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09UZ, an equation

[Tag 09UZ](https://stacks.math.columbia.edu/tag/09UZ) in the Stacks Project.

**`Stacks.Cohomology.CechRefinement.cechDiagram`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechRefinements/ColimitOverRefinements.lean, line 498](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechRefinements/ColimitOverRefinements.lean#L498). The attribute's comment: “the diagram of Čech cohomology over refinements”.

> **Stacks Project, Tag 09UZ.** Čech cohomology of an abelian sheaf in a fixed degree, as a
> functor of the open covering: a refinement acts through the induced map of Čech complexes.

```lean
def cechDiagram : OpenCoverSet X ⥤ AddCommGrpCat.{max u v}
```

**`Stacks.Cohomology.CechRefinement.colimitToCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechRefinements/ColimitOverRefinements.lean, line 549](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechRefinements/ColimitOverRefinements.lean#L549). The attribute's comment: “the comparison from the colimit”.

> **Stacks Project, Tag 09UZ.** The canonical comparison from the Čech cohomology of a
> topological space — the colimit, over all open coverings, of the Čech cohomology of the
> covering — to sheaf cohomology.

```lean
def colimitToCohomology :
    colimit (cechDiagram G p) ⟶
      (CechSite.derivedSectionsFunctor.{max u v} (Opens.grothendieckTopology X)
          (⊤ : Opens X) ⋙
        DerivedCategory.Plus.homologyFunctor AddCommGrpCat.{max u v} p).obj G
```

**`Stacks.Cohomology.CechRefinement.ι_colimitToCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechRefinements/ColimitOverRefinements.lean, line 560](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechRefinements/ColimitOverRefinements.lean#L560). The attribute's comment: “compatibility with the fixed-covering comparison”.

> **Stacks Project, Tag 09UZ.** On each open covering, the comparison out of the colimit
> restricts to the fixed-covering comparison of Stacks 03AX.

```lean
theorem ι_colimitToCohomology (U : OpenCoverSet X) :
    colimit.ι (cechDiagram G p) U ≫ colimitToCohomology G p =
      (CechSite.cechCohomologyToCohomology.{v} (Opens.grothendieckTopology X) (hypercover U)
        (hypercover_mem_grothendieckTopology U) p).app G
```

## Tag 01FD, a lemma

[Tag 01FD](https://stacks.math.columbia.edu/tag/01FD) in the Stacks Project.

**`Stacks.Cohomology.CechRefinement.cechToDerivedGlobalSections_naturality_of_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechRefinements/CohomologyCompatibility.lean, line 1002](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechRefinements/CohomologyCompatibility.lean#L1002). The attribute's comment: “derived\_compatibility”. References: EGA 0 (12.1.4), “(12.1.4.2)”.

> **[Stacks, Tag 01FD].** Let `f : X ⟶ Y` be a morphism of ringed spaces, let `φ : f^* G ⟶ F`
> be an `f`-map of sheaves of modules, let `U` be an open covering of `X`, let `V` be an open
> covering of `Y` and let `c` be a refinement function, so that `U i ⊆ f⁻¹(V (c i))`. Then the
> Čech refinement map `γ` of [Stacks, Tag 01FD], followed by the comparison of [Stacks, Tag 01EQ]
> on `X` read over `Γ(Y, 𝒪_Y)`, agrees with the comparison of [Stacks, Tag 01EQ] on `Y` followed
> by the functorial map on derived global sections of [Stacks, Tag 01F9].
>
> All four corners are read in the bounded-below derived category of `Γ(Y, 𝒪_Y)`-modules, so the
> left-hand side carries the unit `Stacks.Cohomology.scalarRestrictionUnit` of derived restriction
> of scalars and the comparison `Stacks.Cohomology.derivedSectionsScalarComparison` of
> [Stacks, Tag 01EZ].

```lean
theorem cechToDerivedGlobalSections_naturality_of_refinement :
    DerivedCategory.Plus.Q.map
          (ObjectProperty.homMk (cechComplexRefinementMapInt f F G φ U V hU hV c hc) :
            (CechDerived.cechComplexPlusFunctor (ringCatSheaf Y) ⊤ V hV).obj G ⟶
              (restrictGlobalScalars f).mapCochainComplexPlus.obj
                ((CechDerived.cechComplexPlusFunctor (ringCatSheaf X) ⊤ U hU).obj F)) ≫
        (scalarRestrictionUnit f
              ((CechDerived.cechComplexPlusFunctor (ringCatSheaf X) ⊤ U hU).obj F) ≫
            (restrictGlobalScalars f).rightDerivedFunctorPlus.map
              ((CechDerived.cechToDerivedGlobalSections (ringCatSheaf X) ⊤ U hU).app F) ≫
            (derivedSectionsScalarComparison f).hom.app
              ((DerivedCategory.Plus.singleFunctor (Modules X) 0).obj F)) =
      (CechDerived.cechToDerivedGlobalSections (ringCatSheaf Y) ⊤ V hV).app G ≫
        derivedModuleGlobalSectionsMap f φ
```

**`Stacks.Cohomology.CechRefinement.cechCohomologyToCohomology_naturality_of_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechRefinements/CohomologyCompatibility.lean, line 1045](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechRefinements/CohomologyCompatibility.lean#L1045). The attribute's comment: “cohomology\_compatibility”. References: EGA 0 (12.1.4), “(12.1.4.2)”.

> **[Stacks, Tag 01FD] on cohomology.** The canonical maps from Čech cohomology to sheaf
> cohomology of [Stacks, Tag 01EQ] commute with an `f`-map and a refinement of the inverse-image
> covering: this is
> `Stacks.Cohomology.CechRefinement.cechToDerivedGlobalSections_naturality_of_refinement` read
> through the `p`-th homology of the bounded-below derived category. All four corners are modules
> over `Γ(Y, 𝒪_Y)`, so the source comparison carries the derived restriction-of-scalars unit.

```lean
theorem cechCohomologyToCohomology_naturality_of_refinement (p : ℤ) :
    (DerivedCategory.Plus.homologyFunctor
            (ModuleCat ((ringCatSheaf Y).obj.obj (op ⊤))) p).map
          (DerivedCategory.Plus.Q.map
            (ObjectProperty.homMk (cechComplexRefinementMapInt f F G φ U V hU hV c hc) :
              (CechDerived.cechComplexPlusFunctor (ringCatSheaf Y) ⊤ V hV).obj G ⟶
                (restrictGlobalScalars f).mapCochainComplexPlus.obj
                  ((CechDerived.cechComplexPlusFunctor (ringCatSheaf X) ⊤ U hU).obj F))) ≫
        (DerivedCategory.Plus.homologyFunctor
              (ModuleCat ((ringCatSheaf Y).obj.obj (op ⊤))) p).map
            (scalarRestrictionUnit f
              ((CechDerived.cechComplexPlusFunctor (ringCatSheaf X) ⊤ U hU).obj F)) ≫
          (DerivedCategory.Plus.homologyFunctor
                (ModuleCat ((ringCatSheaf Y).obj.obj (op ⊤))) p).map
              ((restrictGlobalScalars f).rightDerivedFunctorPlus.map
                ((CechDerived.cechToDerivedGlobalSections (ringCatSheaf X) ⊤ U hU).app F)) ≫
            (DerivedCategory.Plus.homologyFunctor
                (ModuleCat ((ringCatSheaf Y).obj.obj (op ⊤))) p).map
              ((derivedSectionsScalarComparison f).hom.app
                ((DerivedCategory.Plus.singleFunctor (Modules X) 0).obj F)) =
      (CechDerived.cechCohomologyToCohomology (ringCatSheaf Y) ⊤ V hV p).app G ≫
        (DerivedCategory.Plus.homologyFunctor
            (ModuleCat ((ringCatSheaf Y).obj.obj (op ⊤))) p).map
          (derivedModuleGlobalSectionsMap f φ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.15, Tag 09UY](https://stacks.math.columbia.edu/tag/09UY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
