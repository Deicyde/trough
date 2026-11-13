---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.FlatFppf.isIso_derivedAbelianLowerShriekAdjunction_counit_constantSheaf_of_isTerminal, AlgebraicGeometry.Stack.FlatFppf.isIso_derivedAbelianLowerShriekAdjunction_counit_constantSheaf_schemeStack, AlgebraicGeometry.Stack.derivedAbelianLowerShriek_constantSheaf, AlgebraicGeometry.Stack.FlatFppf.derivedGlobalSectionsRestrictionIso, AlgebraicGeometry.Stack.LisseEtale.derivedGlobalSectionsRestrictionIso, AlgebraicGeometry.Stack.FlatFppf.derivedModuleGlobalSectionsRestrictionIso, AlgebraicGeometry.Stack.FlatFppf.derivedModuleSectionsRestrictionIso, AlgebraicGeometry.Stack.LisseEtale.derivedModuleGlobalSectionsRestrictionIso
statement: formalized
proof: formalized
---

# 104.4 Cohomology and the lisse-étale and flat-fppf sites

Section 104.4 of the Stacks Project, [Tag 0H0Y](https://stacks.math.columbia.edu/tag/0H0Y). 2 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H0Z, a lemma

[Tag 0H0Z](https://stacks.math.columbia.edu/tag/0H0Z) in the Stacks Project.

**`AlgebraicGeometry.Stack.FlatFppf.isIso_derivedAbelianLowerShriekAdjunction_counit_constantSheaf_of_isTerminal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfTerminalConstantSheaf.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfTerminalConstantSheaf.lean#L51). The attribute's comment: “for the `Lg_!` of 07AS part (3), the flat-fppf site of an algebraic stack whose flat-fppf site has a terminal object whose image is terminal in the fppf site”.

> For an algebraic stack `𝒳` whose flat-fppf site has a terminal object `e` whose image is
> terminal in the fppf site, the counit of the derived adjunction `Lg_! ⊣ g⁻¹` is invertible at the
> constant sheaf `ℤ` of `𝒳_{fppf}` in degree zero, so the canonical comparison `Lg_! ℤ ⟶ ℤ` is an
> isomorphism. The proof does not use the terminal object, so the statement carries no hypothesis
> about it.

```lean
theorem isIso_derivedAbelianLowerShriekAdjunction_counit_constantSheaf_of_isTerminal :
    IsIso ((derivedAbelianLowerShriekAdjunction B S hS 𝒳
          (abelianLowerShriekAcyclic B S hS 𝒳)).counit.app
        ((DerivedCategory.singleFunctor _ 0).obj
          ((constantSheaf (fppfTopology B S hS 𝒳) AddCommGrpCat.{u + 1}).obj
            (AddCommGrpCat.of (ULift.{u + 1} ℤ)))))
```

**`AlgebraicGeometry.Stack.FlatFppf.isIso_derivedAbelianLowerShriekAdjunction_counit_constantSheaf_schemeStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemeStackTerminalSubsite.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SchemeStackTerminalSubsite.lean#L86). The attribute's comment: “for the `Lg_!` of 07AS part (3), the flat-fppf site of the stack of a scheme”.

> For the stack of a scheme `U`, the counit of the derived adjunction `Lg_! ⊣ g⁻¹` is invertible
> at the constant sheaf `ℤ` of `(Sch/U)_{fppf}` in degree zero, so the canonical comparison
> `Lg_! ℤ ⟶ ℤ` is an isomorphism.

```lean
theorem isIso_derivedAbelianLowerShriekAdjunction_counit_constantSheaf_schemeStack :
    IsIso ((derivedAbelianLowerShriekAdjunction B S hS (schemeStack.{u, w} B S hS U)
          (abelianLowerShriekAcyclic B S hS (schemeStack.{u, w} B S hS U))).counit.app
        ((DerivedCategory.singleFunctor _ 0).obj
          ((constantSheaf (fppfTopology B S hS (schemeStack.{u, w} B S hS U))
            AddCommGrpCat.{u + 1}).obj (AddCommGrpCat.of (ULift.{u + 1} ℤ)))))
```

**`AlgebraicGeometry.Stack.derivedAbelianLowerShriek_constantSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteConstantSheafLowerShriek.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteConstantSheafLowerShriek.lean#L234). The attribute's comment: “both cases of the statement, for every algebraic stack and with nothing assumed: the `Lg_!` of 07AS part (1) (lisse-étale) and of 07AS part (3) (flat-fppf). For each, the first clause is `Lg_!(ℤ[0]) ≅ ℤ[0]` and the second is invertibility of the canonical map, the counit of `Lg_! ⊣ g⁻¹` at `ℤ[0]`. Both `Lg_!` are the unconditional ones of 07AS (1) and (3); the cohomology comparison of 07AK that the proof runs on is the unconditional `AlgebraicGeometry.Stack.LisseEtale.globalCohomologyIso` resp. `AlgebraicGeometry.Stack.FlatFppf.globalCohomologyIso`, so neither `g_!ℤ = ℤ` nor the acyclicity of 0D6X is a hypothesis”.

> **Stacks 0H0Z.** Let `𝒳` be an algebraic stack. Then `Lg_! ℤ = ℤ`, both for the `Lg_!` of
> Stacks 07AS part (1) — `D(𝒳_{lisse,étale}) ⟶ D(𝒳_{étale})` — and for the `Lg_!` of part (3) —
> `D(𝒳_{flat,fppf}) ⟶ D(𝒳_{fppf})`.
>
> For each of the two sites the statement has two clauses: the derived lower shriek of the constant
> sheaf `ℤ` of the subsite in degree zero is isomorphic to the constant sheaf `ℤ` of `𝒳` in degree
> zero, and the canonical map realizing this — the counit of `Lg_! ⊣ g⁻¹` at `ℤ[0]`, whose source is
> `Lg_!(g⁻¹ℤ) = Lg_! ℤ` — is an isomorphism. Nothing is assumed beyond `𝒳` being algebraic.

```lean
theorem derivedAbelianLowerShriek_constantSheaf :
    (Nonempty ((LisseEtale.derivedAbelianLowerShriek.{u, w} B S hS 𝒳).obj
        ((DerivedCategory.singleFunctor _ 0).obj
          ((constantSheaf (LisseEtale.inclusionTopology.{u, w} B S hS 𝒳)
            AddCommGrpCat.{u + 1}).obj (AddCommGrpCat.of (ULift.{u + 1} ℤ)))) ≅
      (DerivedCategory.singleFunctor _ 0).obj
        ((constantSheaf (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
          AddCommGrpCat.{u + 1}).obj (AddCommGrpCat.of (ULift.{u + 1} ℤ)))) ∧
      IsIso ((LisseEtale.derivedAbelianLowerShriekAdjunction.{u, w} B S hS 𝒳).counit.app
        ((DerivedCategory.singleFunctor _ 0).obj
          ((constantSheaf (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
            AddCommGrpCat.{u + 1}).obj (AddCommGrpCat.of (ULift.{u + 1} ℤ)))))) ∧
    (Nonempty ((FlatFppf.derivedAbelianLowerShriekFunctor B S hS 𝒳).obj
        ((DerivedCategory.singleFunctor _ 0).obj
          ((constantSheaf (FlatFppf.inclusionTopology B S hS 𝒳) AddCommGrpCat.{u + 1}).obj
            (AddCommGrpCat.of (ULift.{u + 1} ℤ)))) ≅
      (DerivedCategory.singleFunctor _ 0).obj
        ((constantSheaf (FlatFppf.fppfTopology B S hS 𝒳) AddCommGrpCat.{u + 1}).obj
          (AddCommGrpCat.of (ULift.{u + 1} ℤ)))) ∧
      IsIso ((FlatFppf.derivedAbelianLowerShriekFunctorAdjunction B S hS 𝒳).counit.app
        ((DerivedCategory.singleFunctor _ 0).obj
          ((constantSheaf (FlatFppf.fppfTopology B S hS 𝒳) AddCommGrpCat.{u + 1}).obj
            (AddCommGrpCat.of (ULift.{u + 1} ℤ))))))
```

## Tag 0H10, a lemma

[Tag 0H10](https://stacks.math.columbia.edu/tag/0H10) in the Stacks Project.

**`AlgebraicGeometry.Stack.FlatFppf.derivedGlobalSectionsRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DerivedGlobalSectionsOnSmoothAndFlatSites.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DerivedGlobalSectionsOnSmoothAndFlatSites.lean#L87). The attribute's comment: “part (2)(a) for complexes, at the flat-fppf site, with NO hypothesis: RΓ(𝒳\_\{flat,fppf}, g⁻¹K) = RΓ(𝒳\_\{fppf}, K), from Lg\_! ℤ = ℤ (Tag 0H0Z, proved)”.

> **Stacks 0H10, part (2)(a), for complexes, with no hypothesis.** Let `𝒳` be an algebraic
> stack and let `g : Sh(𝒳_{flat,fppf}) ⟶ Sh(𝒳_{fppf})` be the comparison morphism of topoi of
> Stacks 08MZ, whose inverse image is restriction to the flat objects. For every `K` in the
> unbounded derived category of abelian sheaves on `𝒳_{fppf}`,
>
> `RΓ(𝒳_{flat,fppf}, g⁻¹K) = RΓ(𝒳_{fppf}, K)`,
>
> naturally in `K`, where on each side `RΓ` is the total right derived functor of global sections
> (`Sheaf.Γ`, the right adjoint of the constant sheaf functor).
>
> The proof is the source's: global sections are corepresented by `ℤ`, and `Lg_! ℤ = ℤ`
> (Stacks 0H0Z, `isIso_derivedAbelianLowerShriekFunctorAdjunction_counit_constantSheaf`)
> turns the derived adjunction `Lg_! ⊣ g⁻¹` of Stacks 07AS (3) into the comparison.

```lean
def derivedGlobalSectionsRestrictionIso :
    Stacks.Cohomology.DerivedLowerShriek.derivedAbelianRestriction.{u + 1}
          (inclusionTopology B S hS 𝒳) (fppfTopology B S hS 𝒳) (objectProperty B S hS 𝒳).ι ⋙
        derivedGlobalSectionsOnFlatSite B S hS 𝒳 ≅
      AlgebraicGeometry.Stack.derivedGlobalSections.{u, u + 1} B S hS 𝒳.val
```

**`AlgebraicGeometry.Stack.LisseEtale.derivedGlobalSectionsRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DerivedGlobalSectionsOnSmoothAndFlatSites.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DerivedGlobalSectionsOnSmoothAndFlatSites.lean#L147). The attribute's comment: “part (1)(a) for complexes, at the lisse-étale site, with NO hypothesis: RΓ(𝒳\_\{lisse,étale}, g⁻¹K) = RΓ(𝒳\_\{étale}, K), from Lg\_! ℤ = ℤ (Tag 0H0Z, proved)”.

> **Stacks 0H10, part (1)(a), for complexes, with no hypothesis.** Let `𝒳` be an algebraic
> stack and let `g : Sh(𝒳_{lisse,étale}) ⟶ Sh(𝒳_{étale})` be the comparison morphism of topoi of
> Stacks 08MZ, whose inverse image is restriction to the smooth objects. For every `K` in the
> unbounded derived category of abelian sheaves on `𝒳_{étale}`,
>
> `RΓ(𝒳_{lisse,étale}, g⁻¹K) = RΓ(𝒳_{étale}, K)`,
>
> naturally in `K`, where on each side `RΓ` is the total right derived functor of global sections
> (`Sheaf.Γ`, the right adjoint of the constant sheaf functor).
>
> The proof is the source's: global sections are corepresented by `ℤ`, and `Lg_! ℤ = ℤ`
> (Stacks 0H0Z, `LisseEtale.isIso_derivedAbelianLowerShriekAdjunction_counit_constantSheaf`)
> turns the derived adjunction `Lg_! ⊣ g⁻¹` of Stacks 07AS (1) into the comparison.

```lean
def derivedGlobalSectionsRestrictionIso :
    derivedAbelianRestriction.{u, w} B S hS 𝒳 ⋙ derivedGlobalSections B S hS 𝒳 ≅
      derivedGlobalSectionsEtale B S hS 𝒳
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedModuleGlobalSectionsRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DerivedModuleSectionsOnSmoothAndFlatSites.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DerivedModuleSectionsOnSmoothAndFlatSites.lean#L119). The attribute's comment: “part (2)(a) for sheaves of modules (the closing sentence of the statement), with NO hypothesis: derived global sections on the flat-fppf site of g^*K, computed on complexes of modules, are those of K on the fppf site”.

> **Stacks 0H10, part (2)(a), for sheaves of modules.** For every `K` in the unbounded derived
> category of sheaves of `𝒪_𝒳`-modules on `𝒳_{fppf}`,
> `RΓ(𝒳_{flat,fppf}, g^*K) = RΓ(𝒳_{fppf}, K)`, naturally in `K`, both sides computed on complexes
> of modules; `𝒪_{𝒳_{flat,fppf}} = g⁻¹𝒪_𝒳` and `g^* = g⁻¹`.

```lean
def derivedModuleGlobalSectionsRestrictionIso :
    haveI := hasPointwiseRightKanExtension_inclusion_ab.{u, w, u + 1} B S hS 𝒳
    (Stacks.Cohomology.DerivedLowerShriek.BigSite.moduleInverseImage (inclusionTopology B S hS 𝒳)
        (fppfTopology B S hS 𝒳)
        (objectProperty B S hS 𝒳).ι (ambientRingStructureSheaf B S hS 𝒳)).mapDerivedCategory ⋙
        derivedModuleOf (restrictedRing (inclusionTopology B S hS 𝒳) (fppfTopology B S hS 𝒳)
          (objectProperty B S hS 𝒳).ι (ambientRingStructureSheaf B S hS 𝒳))
          (Sheaf.Γ (inclusionTopology B S hS 𝒳) AddCommGrpCat.{u + 1}) ≅
      derivedModuleOf (ambientRingStructureSheaf B S hS 𝒳)
        (Sheaf.Γ (fppfTopology B S hS 𝒳) AddCommGrpCat.{u + 1})
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedModuleSectionsRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DerivedModuleSectionsOnSmoothAndFlatSites.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DerivedModuleSectionsOnSmoothAndFlatSites.lean#L147). The attribute's comment: “part (2)(b) for sheaves of modules (the closing sentence of the statement), with NO hypothesis; cohomology over an object is the derived functor of sections over it”.

> **Stacks 0H10, part (2)(b), for sheaves of modules.** For every object `x` of the flat-fppf
> site and every `K` in the unbounded derived category of sheaves of `𝒪_𝒳`-modules on
> `𝒳_{fppf}`, `RΓ(x, g^*K) = RΓ(x, K)`, naturally in `K`, both sides computed on complexes of
> modules, cohomology over `x` being the derived functor of sections over `x`.

```lean
def derivedModuleSectionsRestrictionIso
    (x : ObjectProperty.FullSubcategory (objectProperty B S hS 𝒳)) :
    haveI := hasPointwiseRightKanExtension_inclusion_ab.{u, w, u + 1} B S hS 𝒳
    (Stacks.Cohomology.DerivedLowerShriek.BigSite.moduleInverseImage (inclusionTopology B S hS 𝒳)
        (fppfTopology B S hS 𝒳)
        (objectProperty B S hS 𝒳).ι (ambientRingStructureSheaf B S hS 𝒳)).mapDerivedCategory ⋙
        derivedModuleOf (restrictedRing (inclusionTopology B S hS 𝒳) (fppfTopology B S hS 𝒳)
          (objectProperty B S hS 𝒳).ι (ambientRingStructureSheaf B S hS 𝒳))
          (abelianSections.{u + 1} (inclusionTopology B S hS 𝒳) x) ≅
      derivedModuleOf (ambientRingStructureSheaf B S hS 𝒳)
        (abelianSections.{u + 1} (fppfTopology B S hS 𝒳) ((objectProperty B S hS 𝒳).ι.obj x))
```

**`AlgebraicGeometry.Stack.LisseEtale.derivedModuleGlobalSectionsRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DerivedModuleSectionsOnSmoothAndFlatSites.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DerivedModuleSectionsOnSmoothAndFlatSites.lean#L228). The attribute's comment: “part (1)(a) for sheaves of modules (the closing sentence of the statement), with NO hypothesis: derived global sections on the lisse-étale site of g^*K, computed on complexes of modules, are those of K on the étale site”.

> **Stacks 0H10, part (1)(a), for sheaves of modules.** For every `K` in the unbounded derived
> category of sheaves of `𝒪_𝒳`-modules on `𝒳_{étale}`,
> `RΓ(𝒳_{lisse,étale}, g^*K) = RΓ(𝒳_{étale}, K)`, naturally in `K`, both sides computed on
> complexes of modules; `𝒪_{𝒳_{lisse,étale}} = g⁻¹𝒪_𝒳` and `g^* = g⁻¹`.

```lean
def derivedModuleGlobalSectionsRestrictionIso :
    haveI := isContinuous_inclusion.{u, w} B S hS 𝒳 (closedUnderSmoothMorphisms.{u, w} B S hS 𝒳)
    haveI := isCocontinuous_inclusion.{u, w} B S hS 𝒳
      (closedUnderSmoothMorphisms.{u, w} B S hS 𝒳)
    (Stacks.Cohomology.DerivedLowerShriek.BigSite.moduleInverseImage
        (inclusionTopology.{u, w} B S hS 𝒳)
        (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        (smoothObject.{u, w} B S hS 𝒳).ι (ambientRingStructureSheaf B S hS 𝒳)).mapDerivedCategory ⋙
        derivedModuleOf (restrictedRing (inclusionTopology.{u, w} B S hS 𝒳)
          (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
          (smoothObject.{u, w} B S hS 𝒳).ι (ambientRingStructureSheaf B S hS 𝒳))
          (Sheaf.Γ (inclusionTopology.{u, w} B S hS 𝒳) AddCommGrpCat.{u + 1}) ≅
      derivedModuleOf (ambientRingStructureSheaf B S hS 𝒳)
        (Sheaf.Γ (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
          AddCommGrpCat.{u + 1})
```

**`AlgebraicGeometry.Stack.LisseEtale.derivedModuleSectionsRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DerivedModuleSectionsOnSmoothAndFlatSites.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DerivedModuleSectionsOnSmoothAndFlatSites.lean#L262). The attribute's comment: “part (1)(b) for sheaves of modules (the closing sentence of the statement), with NO hypothesis; cohomology over an object is the derived functor of sections over it”.

> **Stacks 0H10, part (1)(b), for sheaves of modules.** For every object `x` of the
> lisse-étale site and every `K` in the unbounded derived category of sheaves of `𝒪_𝒳`-modules on
> `𝒳_{étale}`, `RΓ(x, g^*K) = RΓ(x, K)`, naturally in `K`, both sides computed on complexes of
> modules, cohomology over `x` being the derived functor of sections over `x`.

```lean
def derivedModuleSectionsRestrictionIso (x : LisseEtale.{u, w} B S hS 𝒳) :
    haveI := isContinuous_inclusion.{u, w} B S hS 𝒳 (closedUnderSmoothMorphisms.{u, w} B S hS 𝒳)
    haveI := isCocontinuous_inclusion.{u, w} B S hS 𝒳
      (closedUnderSmoothMorphisms.{u, w} B S hS 𝒳)
    (Stacks.Cohomology.DerivedLowerShriek.BigSite.moduleInverseImage
        (inclusionTopology.{u, w} B S hS 𝒳)
        (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        (smoothObject.{u, w} B S hS 𝒳).ι (ambientRingStructureSheaf B S hS 𝒳)).mapDerivedCategory ⋙
        derivedModuleOf (restrictedRing (inclusionTopology.{u, w} B S hS 𝒳)
          (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
          (smoothObject.{u, w} B S hS 𝒳).ι (ambientRingStructureSheaf B S hS 𝒳))
          (abelianSections.{u + 1} (inclusionTopology.{u, w} B S hS 𝒳) x) ≅
      derivedModuleOf (ambientRingStructureSheaf B S hS 𝒳)
        (abelianSections.{u + 1} (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
          ((smoothObject.{u, w} B S hS 𝒳).ι.obj x))
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedSectionsRestrictionIsoOfFlatObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DerivedSectionsOverSmoothAndFlatObjects.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DerivedSectionsOverSmoothAndFlatObjects.lean#L133). The attribute's comment: “part (2)(b) for complexes, at the flat-fppf site, with NO hypothesis: the half of Tag 0794 that `AlgebraicGeometry.Stack.FlatFppf.derivedSectionsRestrictionIso` carries as `hgen` is `AlgebraicGeometry.Stack.FlatFppf.derivedLowerShriekComputesFlatGenerator`. Cohomology over an object is the derived functor of sections over it (equal to cohomology of the slice site by Tag 03F3)”.

> **Stacks 0H10, part (2)(b), for complexes, with no hypothesis.** Let `𝒳` be an algebraic
> stack and let `g : Sh(𝒳_{flat,fppf}) ⟶ Sh(𝒳_{fppf})` be the comparison morphism of topoi of
> Stacks 08MZ, whose inverse image is restriction to the flat objects. For every object `x` of the
> flat-fppf site and every `K` in the unbounded derived category of abelian sheaves on
> `𝒳_{fppf}`,
>
> `RΓ(𝒳_{flat,fppf}/x, g⁻¹K) = RΓ(x, K)`,
>
> naturally in `K`, where on each side cohomology over `x` is the right derived functor of sections
> over `x` on the respective site (the convention of Stacks 0DD8 here; it is cohomology of the
> slice site by Stacks 03F3). This is `derivedSectionsRestrictionIso` with its hypothesis `hgen`
> proved, by `derivedLowerShriekComputesFlatGenerator`.

```lean
def derivedSectionsRestrictionIsoOfFlatObject
    (x : ObjectProperty.FullSubcategory (objectProperty B S hS 𝒳)) :
    Stacks.Cohomology.DerivedLowerShriek.derivedAbelianRestriction.{u + 1}
          (inclusionTopology B S hS 𝒳) (fppfTopology B S hS 𝒳) (objectProperty B S hS 𝒳).ι ⋙
        derivedSections B S hS 𝒳 x ≅
      derivedSectionsFppf B S hS 𝒳 ((objectProperty B S hS 𝒳).ι.obj x)
```

**`AlgebraicGeometry.Stack.LisseEtale.derivedSectionsRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DerivedSectionsOverSmoothAndFlatObjects.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DerivedSectionsOverSmoothAndFlatObjects.lean#L227). The attribute's comment: “part (1)(b) for complexes, at the lisse-étale site, with NO hypothesis. Cohomology over an object is the derived functor of sections over it (equal to cohomology of the slice site by Tag 03F3)”.

> **Stacks 0H10, part (1)(b), for complexes, with no hypothesis.** Let `𝒳` be an algebraic
> stack and let `g : Sh(𝒳_{lisse,étale}) ⟶ Sh(𝒳_{étale})` be the comparison morphism of topoi of
> Stacks 08MZ, whose inverse image is restriction to the smooth objects. For every object `x` of
> the lisse-étale site and every `K` in the unbounded derived category of abelian sheaves on
> `𝒳_{étale}`,
>
> `RΓ(𝒳_{lisse,étale}/x, g⁻¹K) = RΓ(x, K)`,
>
> naturally in `K`, where on each side cohomology over `x` is the right derived functor of sections
> over `x` on the respective site (the convention of Stacks 0DD8 here; it is cohomology of the
> slice site by Stacks 03F3).
>
> This is Stacks 0DD8 (1) on sites that need not be small,
> `Stacks.Cohomology.DerivedLowerShriek.BigSite.derivedAbelianSectionsRestrictionIso`, at the
> lisse-étale inclusion: continuity and cocontinuity come from
> `AlgebraicGeometry.Stack.LisseEtale.closedUnderSmoothMorphisms`, the existence and absoluteness
> of `Lg_!` from `AlgebraicGeometry.Stack.LisseEtale.abelianLowerShriekAcyclic`, and the counit at
> the generator from `derivedLowerShriekComputesSmoothGenerator`.

```lean
def derivedSectionsRestrictionIso (x : LisseEtale.{u, w} B S hS 𝒳) :
    derivedAbelianRestriction.{u, w} B S hS 𝒳 ⋙ derivedSections B S hS 𝒳 x ≅
      derivedSectionsEtale B S hS 𝒳 ((smoothObject.{u, w} B S hS 𝒳).ι.obj x)
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedSectionsRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedSections.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedSections.lean#L147). The attribute's comment: “part (2)(b) for complexes, at the flat-fppf site, with cohomology over an object taken as the derived functor of sections over it; conditional only on the half of Stacks 0794 that computes Lg\_! on a generator”.

> **Stacks 0H10, part (2)(b), for complexes.** Let `𝒳` be an algebraic stack and let
> `g : Sh(𝒳_{flat,fppf}) ⟶ Sh(𝒳_{fppf})` be the comparison morphism of topoi of Stacks 08MZ, whose
> inverse image is restriction to the flat objects. For every object `x` of the flat-fppf site and
> every `K` in the unbounded derived category of abelian sheaves on `𝒳_{fppf}`,
>
> `RΓ(x, g⁻¹K) = RΓ(x, K)`,
>
> naturally in `K`, where on each side cohomology over `x` is the right derived functor of sections
> over `x` on the respective site (the convention of Stacks 0DD8 and Stacks 03YU here; see the
> module docstring on why not the slice site).
>
> The closure condition of Stacks 07AK (1), the existence of `g_!` and `g_*`, Grothendieck
> abelianness of both categories of abelian sheaves, and the acyclicity statement of Stacks 07AC
> that Stacks 07AS (3) needs are all discharged, with no hypothesis on `𝒳`. The single carried
> input is `hgen`.

```lean
def derivedSectionsRestrictionIso
    (x : ObjectProperty.FullSubcategory (objectProperty B S hS 𝒳))
    (hgen : DerivedLowerShriekComputesFlatGenerator B S hS 𝒳 x) :
    Stacks.Cohomology.DerivedLowerShriek.derivedAbelianRestriction.{u + 1}
          (inclusionTopology B S hS 𝒳)
          (fppfTopology B S hS 𝒳) (objectProperty B S hS 𝒳).ι ⋙
        derivedSections B S hS 𝒳 x ≅
      derivedSectionsFppf B S hS 𝒳 ((objectProperty B S hS 𝒳).ι.obj x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 104.4, Tag 0H0Y](https://stacks.math.columbia.edu/tag/0H0Y)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
