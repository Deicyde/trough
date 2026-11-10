---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSite.isLimit_adicQuotientSystem_iff_of_slicedObjectsSituation, AlgebraicGeometry.RingedSite.isLimit_adicQuotientSystem_iff, AlgebraicGeometry.RingedSite.isLimit_adicQuotientSystem_iff_of_sliceTestingFamily, AlgebraicGeometry.RingedSite.isDerivedComplete_iff_homology_of_slicedObjectsSituation, AlgebraicGeometry.RingedSite.isDerivedComplete_iff_homology, AlgebraicGeometry.RingedSite.isDerivedComplete_iff_homology_of_sliceTestingFamily, AlgebraicGeometry.RingedSite.isDerivedComplete_limit_adicQuotientTower, AlgebraicGeometry.RingedSite.isWeakSerreClass_isDerivedComplete_constant
statement: formalized
proof: formalized
---

# 61.21 Derived completion and weakly contractible objects

Section 61.21 of the Stacks Project, [Tag 099P](https://stacks.math.columbia.edu/tag/099P). 1 tag here is carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 099Q, a proposition

[Tag 099Q](https://stacks.math.columbia.edu/tag/099Q) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isLimit_adicQuotientSystem_iff_of_slicedObjectsSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/AdicCompletionCriterion.lean, line 1059](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/AdicCompletionCriterion.lean#L1059). The attribute's comment: “completion_criterion”.

> Ordinary completeness is derived completeness plus separatedness.

```lean
theorem isLimit_adicQuotientSystem_iff_of_slicedObjectsSituation
    (X : RingedSite.{u, v, max u v})
    [HasSheafify X.J AddCommGrpCat.{max u v}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{max u v}]
    (hX : Stacks.WeaklyContractible.SlicedObjectsSituation.{w, v, u, max u v} X.C X.J)
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hI : ∀ U : X.C, hX.B U →
      (I.toSubmodule.obj (op U)).FG)
    (F : SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    Nonempty (IsLimit (Cone.mk F (adicQuotientSystem X I F).quotientMap)) ↔
      AlgebraicGeometry.RingedSite.IsDerivedComplete X I
        ((DerivedCategory.singleFunctor
          (SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj F) ∧
        (⨅ n : ℕ, idealPowerProduct X I F n) = ⊥
```

**`AlgebraicGeometry.RingedSite.isLimit_adicQuotientSystem_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/AdicCompletionCriterion.lean, line 1398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/AdicCompletionCriterion.lean#L1398). The attribute's comment: “completion_criterion”.

> Ordinary completeness is derived completeness plus separatedness.

```lean
theorem isLimit_adicQuotientSystem_iff
    (X : RingedSite.{u, v, max u v})
    [Small.{v} X.C] [HasSheafify X.J (Type v)]
    [HasSheafify X.J AddCommGrpCat.{max u v}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{max u v}]
    (hX : X.J.HasEnoughWeaklyContractibleObjects)
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hI : ∀ U : X.C, X.J.IsWeaklyContractible U →
      (I.toSubmodule.obj (op U)).FG)
    (F : SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    Nonempty (IsLimit (Cone.mk F (adicQuotientSystem X I F).quotientMap)) ↔
      AlgebraicGeometry.RingedSite.IsDerivedComplete X I
        ((DerivedCategory.singleFunctor
          (SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj F) ∧
        (⨅ n : ℕ, idealPowerProduct X I F n) = ⊥
```

**`AlgebraicGeometry.RingedSite.isLimit_adicQuotientSystem_iff_of_sliceTestingFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/AdicCompletionCriterionSliceTesting.lean, line 741](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/AdicCompletionCriterionSliceTesting.lean#L741). The attribute's comment: “completion_criterion”.

> Ordinary completeness is derived completeness plus separatedness.

```lean
theorem isLimit_adicQuotientSystem_iff_of_sliceTestingFamily
    (X : RingedSite.{u, v, max u v w})
    [HasSheafify X.J AddCommGrpCat.{max u v w}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{max u v w}]
    (B : Stacks.WeaklyContractible.SliceTestingFamily.{max u v w} X.C X.J)
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hI : ∀ U : X.C, B.B U →
      (I.toSubmodule.obj (op U)).FG)
    (F : SheafOfModules.{max u v w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    Nonempty (IsLimit (Cone.mk F (adicQuotientSystemOfSize X I F).quotientMap)) ↔
      AlgebraicGeometry.RingedSite.IsDerivedComplete.{u, v, max u v w, max u v w} X I
        ((DerivedCategory.singleFunctor
          (SheafOfModules.{max u v w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj F) ∧
        (⨅ n : ℕ, idealPowerProductOfSize X I F n) = ⊥
```

**`AlgebraicGeometry.RingedSite.isDerivedComplete_iff_homology_of_slicedObjectsSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteCohomology.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteCohomology.lean#L125). The attribute's comment: “cohomology_criterion”.

> A complex is derived complete precisely when each cohomology sheaf is.

```lean
theorem isDerivedComplete_iff_homology_of_slicedObjectsSituation
    (X : RingedSite.{u, v, max u v})
    [HasSheafify X.J AddCommGrpCat.{max u v}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{max u v}]
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hJ : Stacks.WeaklyContractible.SlicedObjectsSituation.{w, v, u, max u v} X.C X.J)
    (K : DerivedCategory (SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    AlgebraicGeometry.RingedSite.IsDerivedComplete X I K ↔
      ∀ p : ℤ, AlgebraicGeometry.RingedSite.IsDerivedComplete X I
        ((DerivedCategory.singleFunctor
          (SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj
          ((DerivedCategory.homologyFunctor
            (SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) p).obj K))
```

**`AlgebraicGeometry.RingedSite.isDerivedComplete_iff_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteCohomology.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteCohomology.lean#L160). The attribute's comment: “cohomology_criterion”.

> A complex is derived complete precisely when each cohomology sheaf is.

```lean
theorem isDerivedComplete_iff_homology
    (X : RingedSite.{u, v, max u v})
    [Small.{v} X.C] [HasSheafify X.J (Type v)]
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (hJ : X.J.HasEnoughWeaklyContractibleObjects)
    (K : DerivedCategory
      (SheafOfModules.{max u v} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)))) :
    AlgebraicGeometry.RingedSite.IsDerivedComplete X I K ↔
      ∀ p : ℤ, AlgebraicGeometry.RingedSite.IsDerivedComplete X I
        ((DerivedCategory.singleFunctor
          (SheafOfModules.{max u v} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))) 0).obj
          ((DerivedCategory.homologyFunctor
            (SheafOfModules.{max u v} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))) p).obj K))
```

**`AlgebraicGeometry.RingedSite.isDerivedComplete_iff_homology_of_sliceTestingFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteCohomologySliceTesting.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteCohomologySliceTesting.lean#L52). The attribute's comment: “cohomology_criterion”.

> A complex is derived complete precisely when each cohomology sheaf is.

```lean
theorem isDerivedComplete_iff_homology_of_sliceTestingFamily
    (X : RingedSite.{u, v, max u v w})
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (h : Stacks.WeaklyContractible.SliceTestingFamily.{max u v w} X.C X.J)
    (K : DerivedCategory
      (SheafOfModules.{max u v w} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)))) :
    AlgebraicGeometry.RingedSite.IsDerivedComplete.{u, v, max u v w, max u v w} X I K ↔
      ∀ p : ℤ, AlgebraicGeometry.RingedSite.IsDerivedComplete.{u, v, max u v w, max u v w} X I
        ((DerivedCategory.singleFunctor
          (SheafOfModules.{max u v w} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))) 0).obj
          ((DerivedCategory.homologyFunctor
            (SheafOfModules.{max u v w} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
            p).obj K))
```

**`AlgebraicGeometry.RingedSite.isDerivedComplete_limit_adicQuotientTower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteCompletedStructureSheaf.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteCompletedStructureSheaf.lean#L76). The attribute's comment: “completed_structure_sheaf”.

> **The completion `limₙ 𝒪/ℐⁿ` of the structure sheaf is derived complete along `ℐ`.** Every
> term of the tower of adic quotients is derived complete, and an inverse limit of derived-complete
> sheaves of modules is derived complete.

```lean
theorem isDerivedComplete_limit_adicQuotientTower
    (X : RingedSite.{u, u, u}) [Small.{u} X.C] [HasSheafify X.J (Type u)]
    (hX : X.J.HasEnoughWeaklyContractibleObjects)
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    AlgebraicGeometry.RingedSite.IsDerivedComplete X I
      ((DerivedCategory.singleFunctor
        (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj
        (limit (adicQuotientTower X I)))
```

**`AlgebraicGeometry.RingedSite.isWeakSerreClass_isDerivedComplete_constant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteConstantNoetherian.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteConstantNoetherian.lean#L190). The attribute's comment: “(1)”.

> **[Stacks, Tag 099Q] (1).** On a site with enough weakly contractible objects, the derived
> complete sheaves of `Λ`-modules form a weak Serre subcategory of `Mod(𝒞, Λ)`.

```lean
theorem isWeakSerreClass_isDerivedComplete_constant (hJ : J.HasEnoughWeaklyContractibleObjects)
    (I : Ideal Λ) :
    ObjectProperty.IsWeakSerreClass
      (fun F : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf (constant J Λ).O) =>
        IsDerivedComplete (constant J Λ) (constantIdealSheaf J Λ I)
          ((DerivedCategory.singleFunctor _ 0).obj F))
```

**`AlgebraicGeometry.RingedSite.isDerivedComplete_limit_constant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteConstantNoetherian.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteConstantNoetherian.lean#L202). The attribute's comment: “(4)”.

> **[Stacks, Tag 099Q] (4).** On a site with enough weakly contractible objects, the limit of an
> inverse system `… → ℱ₃ → ℱ₂ → ℱ₁` of derived complete sheaves of `Λ`-modules is derived
> complete.

```lean
theorem isDerivedComplete_limit_constant (hJ : J.HasEnoughWeaklyContractibleObjects)
    (I : Ideal Λ)
    (F : ℕᵒᵖ ⥤ SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf (constant J Λ).O))
    (hF : ∀ n : ℕ, IsDerivedComplete (constant J Λ) (constantIdealSheaf J Λ I)
      ((DerivedCategory.singleFunctor _ 0).obj (F.obj (op n)))) :
    IsDerivedComplete (constant J Λ) (constantIdealSheaf J Λ I)
      ((DerivedCategory.singleFunctor _ 0).obj (limit F))
```

**`AlgebraicGeometry.RingedSite.isDerivedComplete_iff_homology_constant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteConstantNoetherian.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteConstantNoetherian.lean#L215). The attribute's comment: “(5)”.

> **[Stacks, Tag 099Q] (5).** On a site with enough weakly contractible objects, an object `K`
> of `D(𝒞, Λ)` is derived complete if and only if each cohomology sheaf `Hᵖ(K)` is derived
> complete.

```lean
theorem isDerivedComplete_iff_homology_constant (hJ : J.HasEnoughWeaklyContractibleObjects)
    (I : Ideal Λ)
    (K : DerivedCategory (SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (constant J Λ).O))) :
    IsDerivedComplete (constant J Λ) (constantIdealSheaf J Λ I) K ↔
      ∀ p : ℤ, IsDerivedComplete (constant J Λ) (constantIdealSheaf J Λ I)
        ((DerivedCategory.singleFunctor _ 0).obj ((DerivedCategory.homologyFunctor _ p).obj K))
```

**`AlgebraicGeometry.RingedSite.isLimit_adicQuotientSystem_iff_constant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteConstantNoetherian.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteConstantNoetherian.lean#L229). The attribute's comment: “(2)”.

> **[Stacks, Tag 099Q] (2).** On a site with enough weakly contractible objects, a sheaf `ℱ` of
> `Λ`-modules satisfies `ℱ = lim ℱ/Iⁿℱ` — the maps `ℱ ⟶ ℱ/Iⁿℱ` form a limit cone — if and only if
> `ℱ` is derived complete and `⋂ Iⁿℱ = 0`. Only the finite generation of `I` is used of the
> Noetherian hypothesis.

```lean
theorem isLimit_adicQuotientSystem_iff_constant (hJ : J.HasEnoughWeaklyContractibleObjects)
    {I : Ideal Λ} (hI : I.FG)
    (F : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf (constant J Λ).O)) :
    Nonempty (IsLimit (Cone.mk F
      (adicQuotientSystem (constant J Λ) (constantIdealSheaf J Λ I) F).quotientMap)) ↔
      IsDerivedComplete (constant J Λ) (constantIdealSheaf J Λ I)
        ((DerivedCategory.singleFunctor _ 0).obj F) ∧
        (⨅ n : ℕ, idealPowerProduct (constant J Λ) (constantIdealSheaf J Λ I) F n) = ⊥
```

**`AlgebraicGeometry.RingedSite.isDerivedComplete_constantCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteConstantNoetherian.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteConstantNoetherian.lean#L244). The attribute's comment: “(3)”.

> **[Stacks, Tag 099Q] (3).** On a site with enough weakly contractible objects, the sheaf
> `Λ̲^∧ = lim (Λ/Iⁿ)̲` is derived complete. Only the finite generation of `I` is used of the
> Noetherian hypothesis.

```lean
theorem isDerivedComplete_constantCompletion (hJ : J.HasEnoughWeaklyContractibleObjects)
    {I : Ideal Λ} (hI : I.FG) :
    IsDerivedComplete (constant J Λ) (constantIdealSheaf J Λ I)
      ((DerivedCategory.singleFunctor _ 0).obj
        (limit (Stacks.ConstantSheaf.adicQuotientSystem I ⋙ constantModuleFunctor J Λ)))
```

**`AlgebraicGeometry.RingedSite.isBoundedAbove_iff_constant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteConstantNoetherian.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteConstantNoetherian.lean#L316). The attribute's comment: “(6)”.

> **[Stacks, Tag 099Q] (6).** On a site with enough weakly contractible objects, a derived
> complete object `K` of `D(𝒞, Λ)` is bounded above if and only if `K ⊗^𝐋_Λ (Λ/I)̲` is bounded
> above.

```lean
theorem isBoundedAbove_iff_constant [IsNoetherianRing Λ]
    (hJ : J.HasEnoughWeaklyContractibleObjects) (I : Ideal Λ)
    (K : DerivedCategory (SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (constant J Λ).O)))
    (hK : IsDerivedComplete (constant J Λ) (constantIdealSheaf J Λ I) K) :
    Stacks.DerivedCategory.IsBoundedAbove K ↔
      Stacks.DerivedCategory.IsBoundedAbove
        (((Stacks.SheafOfModules.derivedTensorProductFunctor (constant J Λ)).obj K).obj
          ((DerivedCategory.singleFunctor _ 0).obj
            ((constantModuleFunctor J Λ).obj (ModuleCat.of Λ (Λ ⧸ I)))))
```

**`AlgebraicGeometry.RingedSite.isBounded_of_hasFiniteTorDimension_constant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteConstantNoetherian.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteConstantNoetherian.lean#L364). The attribute's comment: “(7)”.

> **[Stacks, Tag 099Q] (7).** On a site with enough weakly contractible objects, a derived
> complete object `K` of `D(𝒞, Λ)` is bounded if `K ⊗^𝐋_Λ Λ/I`, as an object of `D(𝒞, Λ/I)`, has
> finite Tor dimension, for any derived tensor product `T₁` on `D(𝒞, Λ/I)` against which Tor
> dimension is measured.

```lean
theorem isBounded_of_hasFiniteTorDimension_constant [IsNoetherianRing Λ]
    (hJ : J.HasEnoughWeaklyContractibleObjects) (I : Ideal Λ)
    (K : DerivedCategory (SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (constant J Λ).O)))
    (hK : IsDerivedComplete (constant J Λ) (constantIdealSheaf J Λ I) K)
    (T₁ : Stacks.SheafOfModules.DerivedTensorProduct.{u, u, u, u + 1}
      (Stacks.Sites.adicQuotientRingedSite (constant J Λ) (constantIdealSheaf J Λ I) 1))
    (h : HasFiniteTorDimension.{u, u, u, u + 1} T₁
      ((Stacks.Cohomology.derivedCoefficientChange
        (Stacks.Sites.toAdicQuotient (constantIdealSheaf J Λ I) 1)).obj K)) :
    ∃ a b : ℤ, K.IsGE a ∧ K.IsLE b
```

**`AlgebraicGeometry.RingedSite.isDerivedComplete_limit_of_slicedObjectsSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteInverseLimit.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteInverseLimit.lean#L193). The attribute's comment: “inverse_limits, at a sliced situation of testing objects”.

> **The inverse limit of a countable system of derived-complete sheaves of modules is derived
> complete**, on a ringed site equipped with a covering collection of objects which test
> surjectivity of sheaves of sets valued in the module universe, on the site and on each of its
> slices.
>
> The weakly contractible objects enter only through that collection, so the statement reaches a
> site whose objects outnumber its morphisms — the small pro-étale site of a scheme among them —
> where weak contractibility cannot be tested at the morphism universe at all.

```lean
public theorem isDerivedComplete_limit_of_slicedObjectsSituation
    (X : RingedSite.{u, v, max u v})
    [HasSheafify X.J AddCommGrpCat.{max u v}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{max u v}]
    (hX : Stacks.WeaklyContractible.SlicedObjectsSituation.{w, v, u, max u v}
      X.C X.J)
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (F : ℕᵒᵖ ⥤ SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (hF : ∀ n : ℕ, AlgebraicGeometry.RingedSite.IsDerivedComplete X I
      ((DerivedCategory.singleFunctor
        (SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj
        (F.obj ⟨n⟩))) :
    AlgebraicGeometry.RingedSite.IsDerivedComplete X I
      ((DerivedCategory.singleFunctor
        (SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj
        (limit F))
```

**`AlgebraicGeometry.RingedSite.isDerivedComplete_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteInverseLimit.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteInverseLimit.lean#L264). The attribute's comment: “inverse_limits”.

> The inverse limit of a countable system of derived-complete sheaves is derived complete.

```lean
public theorem isDerivedComplete_limit
    (X : RingedSite.{u, v, max u v})
    [Small.{v} X.C] [HasSheafify X.J (Type v)]
    (hX : X.J.HasEnoughWeaklyContractibleObjects)
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (F : ℕᵒᵖ ⥤ SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (hF : ∀ n : ℕ, AlgebraicGeometry.RingedSite.IsDerivedComplete X I
      ((DerivedCategory.singleFunctor
        (SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj
        (F.obj ⟨n⟩))) :
    AlgebraicGeometry.RingedSite.IsDerivedComplete X I
      ((DerivedCategory.singleFunctor
        (SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj
        (limit F))
```

**`AlgebraicGeometry.RingedSite.isDerivedComplete_limit_of_sliceTestingFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteInverseLimitSliceTesting.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteInverseLimitSliceTesting.lean#L64). The attribute's comment: “inverse_limits”.

> **The inverse limit of a countable system of derived-complete sheaves is derived
> complete**, on a ringed site with a slice testing family of weakly contractible objects at the
> universe of the module sections.

```lean
public theorem isDerivedComplete_limit_of_sliceTestingFamily
    (X : RingedSite.{u, v, max u v w})
    (B : Stacks.WeaklyContractible.SliceTestingFamily.{max u v w} X.C X.J)
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (F : ℕᵒᵖ ⥤ SheafOfModules.{max u v w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (hF : ∀ n : ℕ, AlgebraicGeometry.RingedSite.IsDerivedComplete.{u, v, max u v w, max u v w} X I
      ((DerivedCategory.singleFunctor
        (SheafOfModules.{max u v w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj
        (F.obj ⟨n⟩))) :
    AlgebraicGeometry.RingedSite.IsDerivedComplete.{u, v, max u v w, max u v w} X I
      ((DerivedCategory.singleFunctor
        (SheafOfModules.{max u v w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj
        (limit F))
```

**`AlgebraicGeometry.RingedSite.derivedCompleteSheaves_isWeakSerreClass_of_slicedObjectsSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteWeakSerre.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteWeakSerre.lean#L56). The attribute's comment: “weak_serre”.

> Derived-complete sheaves of modules form a weak Serre subcategory on a site
> with enough weakly contractible objects.

```lean
theorem derivedCompleteSheaves_isWeakSerreClass_of_slicedObjectsSituation
    (X : RingedSite.{u, v, max u v})
    [HasSheafify X.J AddCommGrpCat.{max u v}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{max u v}]
    (hX : Stacks.WeaklyContractible.SlicedObjectsSituation.{w, v, u, max u v} X.C X.J)
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    ObjectProperty.IsWeakSerreClass
      (fun F : SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O) =>
        AlgebraicGeometry.RingedSite.IsDerivedComplete X I
          ((DerivedCategory.singleFunctor
            (SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj F))
```

**`AlgebraicGeometry.RingedSite.derivedCompleteSheaves_isWeakSerreClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteWeakSerre.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteWeakSerre.lean#L215). The attribute's comment: “weak_serre”.

> Derived-complete sheaves of modules form a weak Serre subcategory on a site
> with enough weakly contractible objects.

```lean
theorem derivedCompleteSheaves_isWeakSerreClass
    (X : RingedSite.{u, v, max u v})
    [Small.{v} X.C]
    [HasSheafify X.J (Type v)]
    [HasSheafify X.J AddCommGrpCat.{max u v}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{max u v}]
    (hX : X.J.HasEnoughWeaklyContractibleObjects)
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    ObjectProperty.IsWeakSerreClass
      (fun F : SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O) =>
        AlgebraicGeometry.RingedSite.IsDerivedComplete X I
          ((DerivedCategory.singleFunctor
            (SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
            0).obj F))
```

**`AlgebraicGeometry.RingedSite.derivedCompleteSheaves_isWeakSerreClass_of_sliceTestingFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteWeakSerreSliceTesting.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/DerivedCompleteWeakSerreSliceTesting.lean#L69). The attribute's comment: “weak_serre”.

> Derived-complete sheaves of modules form a weak Serre subcategory on a site
> with enough weakly contractible objects.

```lean
theorem derivedCompleteSheaves_isWeakSerreClass_of_sliceTestingFamily
    (X : RingedSite.{u, v, max u v w})
    [HasSheafify X.J AddCommGrpCat.{max u v w}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{max u v w}]
    (B : Stacks.WeaklyContractible.SliceTestingFamily.{max u v w} X.C X.J)
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    ObjectProperty.IsWeakSerreClass
      (fun F : SheafOfModules.{max u v w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O) =>
        AlgebraicGeometry.RingedSite.IsDerivedComplete.{u, v, max u v w, max u v w} X I
          ((DerivedCategory.singleFunctor
            (SheafOfModules.{max u v w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj
              F))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.21, Tag 099P](https://stacks.math.columbia.edu/tag/099P)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
