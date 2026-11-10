---
declaration: section
origin: cited
lean: Stacks.Cohomology.exists_rightDerivedLimit_isDerivedLimit, Stacks.Cohomology.DerivedGlobalSections.isDerivedLimit_map_derivedGlobalSections, Stacks.Cohomology.DerivedGlobalSections.exists_shortExact_limOne_cohomology_derivedGlobalSections, Stacks.Cohomology.DerivedGlobalSections.isDerivedLimit_map_derivedSections, Stacks.Cohomology.DerivedGlobalSections.exists_shortExact_limOne_cohomology_derivedSections, Stacks.Cohomology.DerivedSectionsMilnor.isDerivedLimit_map_derivedSectionsOverObject, Stacks.Cohomology.DerivedSectionsMilnor.exists_shortExact_limOne_cohomology_derivedSections, Stacks.Cohomology.DerivedPushforwardOnRingedTopoi.isDerivedLimit_map_derivedPushforward
statement: formalized
proof: formalized
---

# 21.23 Derived and homotopy limits

Section 21.23 of the Stacks Project, [Tag 0940](https://stacks.math.columbia.edu/tag/0940). 12 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0941, a lemma

[Tag 0941](https://stacks.math.columbia.edu/tag/0941) in the Stacks Project.

**`Stacks.Cohomology.exists_rightDerivedLimit_isDerivedLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/DerivedLimitsOfInverseSystems.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Recovery21/DerivedLimitsOfInverseSystems.lean#L375).

> **Stacks Project Tag 0941.** The value of the right derived functor of ordinary inverse limit
> at `K` exists and is a derived limit of the tower of the derived evaluations `Kₙ`.

```lean
theorem exists_rightDerivedLimit_isDerivedLimit
    [IsGrothendieckAbelian.{wG} A]
    [HasLimitsOfShape ℕᵒᵖ A]
    (K : DerivedCategory (ℕᵒᵖ ⥤ A)) :
    ∃ (h : HasProduct fun n : ℕ => (derivedEvaluationTower K).obj ⟨n⟩),
      ∃ c : Cocone
        (MorphismProperty.Under.forget
            (HomotopyCategory.quasiIso (ℕᵒᵖ ⥤ A) (ComplexShape.up ℤ)) ⊤
            (DerivedCategory.Qh.objPreimage K) ⋙
          Under.forget (DerivedCategory.Qh.objPreimage K) ⋙
          ((lim : (ℕᵒᵖ ⥤ A) ⥤ A).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
            DerivedCategory.Qh)),
      (((lim : (ℕᵒᵖ ⥤ A) ⥤ A).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
          DerivedCategory.Qh).IsRightDerivedValueAt
        (HomotopyCategory.quasiIso (ℕᵒᵖ ⥤ A) (ComplexShape.up ℤ))
        (DerivedCategory.Qh.objPreimage K) c) ∧
      @IsDerivedLimit (DerivedCategory A) _ _ _ _ _ _
        (derivedEvaluationTower K) h c.pt
```

## Tag 0D6K, a lemma

[Tag 0D6K](https://stacks.math.columbia.edu/tag/0D6K) in the Stacks Project.

**`Stacks.Cohomology.DerivedGlobalSections.isDerivedLimit_map_derivedGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/DerivedGlobalSectionsUnbounded.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/DerivedGlobalSectionsUnbounded.lean#L114). The attribute's comment: “global derived sections commute with derived limits”.

> **Stacks Project, Tag 0D6K.** `RΓ(C, -)` commutes with `Rlim`: global derived sections of
> a ringed site carry a derived inverse limit to a derived inverse limit.

```lean
public theorem isDerivedLimit_map_derivedGlobalSections
    (K : ℕᵒᵖ ⥤ DerivedCategory
      (SheafOfModules.{max u v w z} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    [HasProduct fun n : ℕ ↦ K.obj ⟨n⟩]
    (L : DerivedCategory
      (SheafOfModules.{max u v w z} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hL : IsDerivedLimit K L) :
    ∃ h : HasProduct (fun n : ℕ ↦ (derivedGlobalSections.{u, v, w, z} X).obj (K.obj ⟨n⟩)),
      @IsDerivedLimit
        (DerivedCategory (ModuleCat.{max u v w z}
          (RingCat.sectionsSubring (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj)))
        _ _ _ _ _ _ (K ⋙ derivedGlobalSections.{u, v, w, z} X) h
        ((derivedGlobalSections.{u, v, w, z} X).obj L)
```

**`Stacks.Cohomology.DerivedGlobalSections.exists_shortExact_limOne_cohomology_derivedGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/DerivedGlobalSectionsUnbounded.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/DerivedGlobalSectionsUnbounded.lean#L136). The attribute's comment: “short exact sequence over the whole site”.

> **Stacks Project, Tag 0D6K.** The canonical Milnor short exact sequence for the cohomology
> of the whole ringed site: the first derived inverse limit of the degree-`m - 1` cohomologies
> includes into the degree-`m` cohomology of `RΓ(C, Rlim Kₙ)`, with quotient the inverse limit
> of the degree-`m` cohomologies.

```lean
public theorem exists_shortExact_limOne_cohomology_derivedGlobalSections
    (K : ℕᵒᵖ ⥤ DerivedCategory
      (SheafOfModules.{max u v w z} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (L : DerivedCategory
      (SheafOfModules.{max u v w z} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    [HasProduct fun n : ℕ ↦ K.obj ⟨n⟩]
    (p : L ⟶ ∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩)
    (hL : ∃ δ : (∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
      Triangle.mk p (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) (n + 1) ≫
            K.map (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory
          (SheafOfModules.{max u v w z} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (m : ℤ) :
    let RGamma := derivedGlobalSections.{u, v, w, z} X
    let A := ModuleCat.{max u v w z}
      (RingCat.sectionsSubring (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj)
    let Hprev := DerivedCategory.homologyFunctor A (m - 1)
    let Hcur := DerivedCategory.homologyFunctor A m
    let Fprev := K ⋙ RGamma ⋙ Hprev
    let Fcur := K ⋙ RGamma ⋙ Hcur
    let E := K ⋙ RGamma
    let dprev : (∏ᶜ fun n : ℕ ↦ Fprev.obj ⟨n⟩) ⟶
        (∏ᶜ fun n : ℕ ↦ Fprev.obj ⟨n⟩) := Pi.lift fun n : ℕ ↦
      Pi.π (fun n : ℕ ↦ Fprev.obj ⟨n⟩) n -
        Pi.π (fun n : ℕ ↦ Fprev.obj ⟨n⟩) (n + 1) ≫
          Fprev.map (homOfLE (Nat.le_succ n)).op
    ∃ (h : HasProduct fun n : ℕ ↦ E.obj ⟨n⟩),
      letI := h
      ∃ (a : RGamma.obj L ⟶ ∏ᶜ fun n : ℕ ↦ E.obj ⟨n⟩)
        (b : (∏ᶜ fun n : ℕ ↦ E.obj ⟨n⟩) ⟶ (RGamma.obj L)⟦(1 : ℤ)⟧),
      let T := Triangle.mk a (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦ E.obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦ E.obj ⟨n⟩) (n + 1) ≫
            E.map (homOfLE (Nat.le_succ n)).op) b
      T ∈ distTriang (DerivedCategory A) ∧
      (∀ n : ℕ, a ≫ Pi.π (fun n : ℕ ↦ E.obj ⟨n⟩) n =
        RGamma.map (p ≫ Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n)) ∧
      ∃ (ePrev : Hprev.obj (∏ᶜ fun n : ℕ ↦ E.obj ⟨n⟩) ≅
          ∏ᶜ fun n : ℕ ↦ Fprev.obj ⟨n⟩)
        (i : cokernel dprev ⟶ Hcur.obj (RGamma.obj L))
      (q : Hcur.obj (RGamma.obj L) ⟶ limit Fcur)
      (zero : i ≫ q = 0),
      (ePrev.hom = piComparison Hprev (fun n : ℕ ↦ E.obj ⟨n⟩) ∧
        cokernel.π dprev ≫ i =
          ePrev.inv ≫ (DerivedCategory.homologyFunctor A 0).homologySequenceδ
            T (m - 1) m (by omega) ∧
        (ShortComplex.mk i q zero).ShortExact ∧
        ∀ n : ℕ, q ≫ limit.π Fcur ⟨n⟩ =
          Hcur.map (RGamma.map (p ≫ Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n)))
```

**`Stacks.Cohomology.DerivedGlobalSections.isDerivedLimit_map_derivedSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/DerivedGlobalSectionsUnbounded.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/DerivedGlobalSectionsUnbounded.lean#L239). The attribute's comment: “derived sections over an object commute with derived limits”.

> **Stacks Project, Tag 0D6K.** `RΓ(U, -)` commutes with `Rlim`: derived sections over an
> object of a ringed site carry a derived inverse limit to a derived inverse limit.

```lean
public theorem isDerivedLimit_map_derivedSections
    (K : ℕᵒᵖ ⥤ DerivedCategory
      (SheafOfModules.{max u v w z} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    [HasProduct fun n : ℕ ↦ K.obj ⟨n⟩]
    (L : DerivedCategory
      (SheafOfModules.{max u v w z} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hL : IsDerivedLimit K L) :
    ∃ h : HasProduct (fun n : ℕ ↦ (derivedSections.{u, v, w, z} X U).obj (K.obj ⟨n⟩)),
      @IsDerivedLimit
        (DerivedCategory
          (ModuleCat.{max u v w z} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj.obj U)))
        _ _ _ _ _ _ (K ⋙ derivedSections.{u, v, w, z} X U) h
        ((derivedSections.{u, v, w, z} X U).obj L)
```

**`Stacks.Cohomology.DerivedGlobalSections.exists_shortExact_limOne_cohomology_derivedSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/DerivedGlobalSectionsUnbounded.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/DerivedGlobalSectionsUnbounded.lean#L265). The attribute's comment: “short exact sequence over an object”.

> **Stacks Project, Tag 0D6K.** The canonical Milnor short exact sequence for the cohomology
> over an object `U` of a ringed site: the first derived inverse limit of the degree-`m - 1`
> cohomologies includes into the degree-`m` cohomology of `RΓ(U, Rlim Kₙ)`, with quotient the
> inverse limit of the degree-`m` cohomologies.

```lean
public theorem exists_shortExact_limOne_cohomology_derivedSections
    (K : ℕᵒᵖ ⥤ DerivedCategory
      (SheafOfModules.{max u v w z} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (L : DerivedCategory
      (SheafOfModules.{max u v w z} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    [HasProduct fun n : ℕ ↦ K.obj ⟨n⟩]
    (p : L ⟶ ∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩)
    (hL : ∃ δ : (∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
      Triangle.mk p (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) (n + 1) ≫
            K.map (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory
          (SheafOfModules.{max u v w z} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (m : ℤ) :
    let RGamma := derivedSections.{u, v, w, z} X U
    let A := ModuleCat.{max u v w z} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj.obj U)
    let Hprev := DerivedCategory.homologyFunctor A (m - 1)
    let Hcur := DerivedCategory.homologyFunctor A m
    let Fprev := K ⋙ RGamma ⋙ Hprev
    let Fcur := K ⋙ RGamma ⋙ Hcur
    let E := K ⋙ RGamma
    let dprev : (∏ᶜ fun n : ℕ ↦ Fprev.obj ⟨n⟩) ⟶
        (∏ᶜ fun n : ℕ ↦ Fprev.obj ⟨n⟩) := Pi.lift fun n : ℕ ↦
      Pi.π (fun n : ℕ ↦ Fprev.obj ⟨n⟩) n -
        Pi.π (fun n : ℕ ↦ Fprev.obj ⟨n⟩) (n + 1) ≫
          Fprev.map (homOfLE (Nat.le_succ n)).op
    ∃ (h : HasProduct fun n : ℕ ↦ E.obj ⟨n⟩),
      letI := h
      ∃ (a : RGamma.obj L ⟶ ∏ᶜ fun n : ℕ ↦ E.obj ⟨n⟩)
        (b : (∏ᶜ fun n : ℕ ↦ E.obj ⟨n⟩) ⟶ (RGamma.obj L)⟦(1 : ℤ)⟧),
      let T := Triangle.mk a (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦ E.obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦ E.obj ⟨n⟩) (n + 1) ≫
            E.map (homOfLE (Nat.le_succ n)).op) b
      T ∈ distTriang (DerivedCategory A) ∧
      (∀ n : ℕ, a ≫ Pi.π (fun n : ℕ ↦ E.obj ⟨n⟩) n =
        RGamma.map (p ≫ Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n)) ∧
      ∃ (ePrev : Hprev.obj (∏ᶜ fun n : ℕ ↦ E.obj ⟨n⟩) ≅
          ∏ᶜ fun n : ℕ ↦ Fprev.obj ⟨n⟩)
        (i : cokernel dprev ⟶ Hcur.obj (RGamma.obj L))
      (q : Hcur.obj (RGamma.obj L) ⟶ limit Fcur)
      (zero : i ≫ q = 0),
      (ePrev.hom = piComparison Hprev (fun n : ℕ ↦ E.obj ⟨n⟩) ∧
        cokernel.π dprev ≫ i =
          ePrev.inv ≫ (DerivedCategory.homologyFunctor A 0).homologySequenceδ
            T (m - 1) m (by omega) ∧
        (ShortComplex.mk i q zero).ShortExact ∧
        ∀ n : ℕ, q ≫ limit.π Fcur ⟨n⟩ =
          Hcur.map (RGamma.map (p ≫ Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n)))
```

**`Stacks.Cohomology.DerivedSectionsMilnor.isDerivedLimit_map_derivedSectionsOverObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/DerivedSectionsAndInverseLimits.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/DerivedSectionsAndInverseLimits.lean#L169). The attribute's comment: “derived sections over an object commute with derived limits”.

> **Stacks Project Tag 0D6K.** Derived sections over an object of a ringed site carry a
> derived inverse limit to a derived inverse limit.
>
> Sections over an object are additive and preserve countable products, so Tag 08U1 applies.

```lean
theorem isDerivedLimit_map_derivedSectionsOverObject (X : RingedSite.{u, u, u}) (U : X.C)
    [HasSheafify X.J AddCommGrpCat.{u}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{u}]
    [IsGrothendieckAbelian.{g} (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))]
    (K : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    [HasProduct fun n : ℕ ↦ K.obj ⟨n⟩]
    (L : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hL : IsDerivedLimit K L) :
    ∃ h : HasProduct fun n : ℕ ↦ (K ⋙ derivedSectionsOverObject X U).obj ⟨n⟩,
      letI := h
      IsDerivedLimit (K ⋙ derivedSectionsOverObject X U)
        ((derivedSectionsOverObject X U).obj L)
```

**`Stacks.Cohomology.DerivedSectionsMilnor.exists_shortExact_limOne_cohomology_derivedSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/DerivedSectionsAndInverseLimits.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/DerivedSectionsAndInverseLimits.lean#L198). The attribute's comment: “short exact sequence over an object”.

> **Stacks Project Tag 0D6K.** The canonical Milnor short exact sequence for cohomology over
> an object of a ringed site: the first derived inverse limit of the degree-`m - 1` cohomologies
> includes into the degree-`m` cohomology of derived sections of the derived limit, with quotient
> the inverse limit of the degree-`m` cohomologies.

```lean
theorem exists_shortExact_limOne_cohomology_derivedSections (X : RingedSite.{u, u, u}) (U : X.C)
    [HasSheafify X.J AddCommGrpCat.{u}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{u}]
    [IsGrothendieckAbelian.{g} (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))]
    (K : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    [HasProduct fun n : ℕ ↦ K.obj ⟨n⟩]
    (L : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (p : L ⟶ ∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩)
    (hL : ∃ δ : (∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
      Triangle.mk p (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) (n + 1) ≫
            K.map (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang
          (DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (m : ℤ) :
    let RG := derivedSectionsOverObject X U
    let Hprev := DerivedCategory.homologyFunctor AddCommGrpCat.{u} (m - 1)
    let Hcur := DerivedCategory.homologyFunctor AddCommGrpCat.{u} m
    let E := K ⋙ RG
    let Fprev := E ⋙ Hprev
    let Fcur := E ⋙ Hcur
    let dprev : (∏ᶜ fun n : ℕ ↦ Fprev.obj ⟨n⟩) ⟶ (∏ᶜ fun n : ℕ ↦ Fprev.obj ⟨n⟩) :=
      Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦ Fprev.obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦ Fprev.obj ⟨n⟩) (n + 1) ≫
            Fprev.map (homOfLE (Nat.le_succ n)).op
    ∃ h : HasProduct fun n : ℕ ↦ E.obj ⟨n⟩,
      letI := h
      ∃ (a : RG.obj L ⟶ ∏ᶜ fun n : ℕ ↦ E.obj ⟨n⟩)
        (b : (∏ᶜ fun n : ℕ ↦ E.obj ⟨n⟩) ⟶ (RG.obj L)⟦(1 : ℤ)⟧),
        let T := Triangle.mk a (Pi.lift fun n : ℕ ↦
          Pi.π (fun n : ℕ ↦ E.obj ⟨n⟩) n -
            Pi.π (fun n : ℕ ↦ E.obj ⟨n⟩) (n + 1) ≫
              E.map (homOfLE (Nat.le_succ n)).op) b
        T ∈ distTriang (DerivedCategory AddCommGrpCat.{u}) ∧
        (∀ n : ℕ, a ≫ Pi.π (fun n : ℕ ↦ E.obj ⟨n⟩) n =
          RG.map (p ≫ Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n)) ∧
        ∃ (ePrev : Hprev.obj (∏ᶜ fun n : ℕ ↦ E.obj ⟨n⟩) ≅ ∏ᶜ fun n : ℕ ↦ Fprev.obj ⟨n⟩)
          (i : cokernel dprev ⟶ Hcur.obj (RG.obj L))
          (q : Hcur.obj (RG.obj L) ⟶ limit Fcur)
          (zero : i ≫ q = 0),
          ePrev.hom = piComparison Hprev (fun n : ℕ ↦ E.obj ⟨n⟩) ∧
            cokernel.π dprev ≫ i =
              ePrev.inv ≫ DerivedCategory.HomologySequence.δ T (m - 1) m ∧
            (ShortComplex.mk i q zero).ShortExact ∧
            ∀ n : ℕ, q ≫ limit.π Fcur ⟨n⟩ =
              Hcur.map (RG.map (p ≫ Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n))
```

## Tag 0A07, a lemma

[Tag 0A07](https://stacks.math.columbia.edu/tag/0A07) in the Stacks Project.

**`Stacks.Cohomology.DerivedPushforwardOnRingedTopoi.isDerivedLimit_map_derivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/DerivedLimits.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/DerivedLimits.lean#L92).

> **Stacks Project, Tag 0A07.**  Derived pushforward along a morphism of ringed topoi commutes
> with derived limits: it carries an object exhibited as the derived limit of a countable inverse
> system to the derived limit of the pushed-forward system.

```lean
theorem isDerivedLimit_map_derivedPushforward
    (K : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    [HasProduct fun n : ℕ ↦ K.obj ⟨n⟩]
    (L : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hL : IsDerivedLimit K L) :
    ∃ h : HasProduct (fun n : ℕ ↦ (derivedPushforward f).obj (K.obj ⟨n⟩)),
      @IsDerivedLimit
        (DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)))
        _ _ _ _ _ _
        (K ⋙ derivedPushforward f) h ((derivedPushforward f).obj L)
```

## Tag 0BKW, a remark

[Tag 0BKW](https://stacks.math.columbia.edu/tag/0BKW) in the Stacks Project.

**`Stacks.Cohomology.DerivedLimitDiagram.cohomologyDerivedLimitDiagram_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/ComparisonDiagramUnconditional.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/ComparisonDiagramUnconditional.lean#L195). The attribute's comment: “the commuting square and the short exact sequences over the objects of the site”.

> **Stacks Project, Tag 0BKW.** Let `(C, O)` be a ringed site, let `(Kₙ)` be an inverse system
> in `D(O)` and let `K` be a derived limit of it, presented by the structural map `p : K ⟶ ∏ Kₙ` of
> its distinguished product triangle.  Fix a degree `m`, write `P` for the cohomology presheaf
> functor `M ↦ (U ↦ Hᵐ(U, M))`, `H` for the cohomology sheaf functor, `S` for sheafification and
> `e` for the Tag 0BKV identification `S ∘ P ≅ H`.  Then:
>
> * there are comparison maps `a : P K ⟶ lim P Kₙ`, `b : H K ⟶ lim H Kₙ` and
>   `c : S (lim P Kₙ) ⟶ lim H Kₙ`, each determined by its composites with the limit projections,
>   and the square `S a ≫ c = e ≫ b` commutes; and
> * for every object `U` of `C` there is a short exact sequence
>
>   `0 ⟶ R¹lim Hᵐ⁻¹(U, Kₙ) ⟶ Hᵐ(U, K) ⟶ lim Hᵐ(U, Kₙ) ⟶ 0`,
>
>   whose surjection is determined by its composites with the limit projections and whose `R¹lim`
>   is the cokernel of the difference map `(xₙ) ↦ (xₙ - fₙ₊₁(xₙ₊₁))`.
>
> The third comparison map is *not* asserted to be invertible: sheafification does not in general
> commute with this inverse limit, which is the caveat of the remark.
>
> Nothing is assumed: sheafification, local bijectivity, Grothendieck abelianness, the right
> derived functor presenting cohomology and the countable product presenting the derived limit are
> all theorems at this module universe, and are supplied here.

```lean
theorem cohomologyDerivedLimitDiagram_unconditional
    (K : ℕᵒᵖ ⥤ DerivedCategory
      (SheafOfModules.{max u v r w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (L : DerivedCategory
      (SheafOfModules.{max u v r w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (p : L ⟶ ∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩)
    (hp : ∃ δ : (∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
      Triangle.mk p (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) (n + 1) ≫
            K.map (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory
          (SheafOfModules.{max u v r w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (m : ℤ) :
    let P := DerivedLimitSections.derivedSectionsPresheafMax.{u, v, r, w} X ⋙
      DerivedCategory.homologyFunctor
        (PresheafOfModules.{max u v r w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj) m
    let H := DerivedCategory.homologyFunctor
      (SheafOfModules.{max u v r w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) m
    let S := sheafificationMax.{u, v, r, w} X
    let e := sheafificationCohomologyPresheafIsoMax.{u, v, r, w} X m
    (∃ (a : P.obj L ⟶ limit (K ⋙ P))
      (b : H.obj L ⟶ limit (K ⋙ H))
      (c : S.obj (limit (K ⋙ P)) ⟶ limit (K ⋙ H)),
      (∀ n : ℕ,
        a ≫ limit.π (K ⋙ P) ⟨n⟩ =
          P.map (p ≫ Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n)) ∧
      (∀ n : ℕ,
        b ≫ limit.π (K ⋙ H) ⟨n⟩ =
          H.map (p ≫ Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n)) ∧
      (∀ n : ℕ,
        c ≫ limit.π (K ⋙ H) ⟨n⟩ =
          S.map (limit.π (K ⋙ P) ⟨n⟩) ≫ e.hom.app (K.obj ⟨n⟩)) ∧
      (S.map a ≫ c = e.hom.app L ≫ b)) ∧
    ∀ U : X.C,
      let RG := derivedSectionsMax.{u, v, r, w} X U
      let Mprev := DerivedCategory.homologyFunctor
        (ModuleCat.{max u v r w} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj.obj (.op U)))
          (m - 1)
      let Mcur := DerivedCategory.homologyFunctor
        (ModuleCat.{max u v r w} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj.obj (.op U))) m
      let E := K ⋙ RG
      let Fprev := E ⋙ Mprev
      let Fcur := E ⋙ Mcur
      let dprev : (∏ᶜ fun n : ℕ ↦ Fprev.obj ⟨n⟩) ⟶ (∏ᶜ fun n : ℕ ↦ Fprev.obj ⟨n⟩) :=
        Pi.lift fun n : ℕ ↦
          Pi.π (fun n : ℕ ↦ Fprev.obj ⟨n⟩) n -
            Pi.π (fun n : ℕ ↦ Fprev.obj ⟨n⟩) (n + 1) ≫
              Fprev.map (homOfLE (Nat.le_succ n)).op
      ∃ (i : cokernel dprev ⟶ Mcur.obj (RG.obj L))
        (q : Mcur.obj (RG.obj L) ⟶ limit Fcur)
        (zero : i ≫ q = 0),
        (ShortComplex.mk i q zero).ShortExact ∧
        ∀ n : ℕ, q ≫ limit.π Fcur ⟨n⟩ =
          Mcur.map (RG.map (p ≫ Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n))
```

## Tag 0BKY, a lemma

[Tag 0BKY](https://stacks.math.columbia.edu/tag/0BKY) in the Stacks Project.

**`Stacks.Cohomology.SiteInverseLimits.isDerivedLimit_single_limit_of_acyclic_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/InverseLimitOfAcyclicTower.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/InverseLimitOfAcyclicTower.lean#L371). The attribute's comment: “ordinary limit is a derived limit”.

> If the terms of a countable inverse system of modules on a ringed site are acyclic on a class
> of objects covering every object, and the first derived inverse limit of their sections vanishes
> there, then the ordinary inverse limit, placed in degree zero, is a derived inverse limit of the
> system.

```lean
theorem isDerivedLimit_single_limit_of_acyclic_cover
    (F : ℕᵒᵖ ⥤ SheafOfModules.{z} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (B : ObjectProperty X.C) (hB : X.J.HasEnoughObjects B)
    (hcoh : ∀ U, B U →
      letI : (SheafOfModules.evaluation.{z}
          (Stacks.SheafOfModules.Tensor.ringSheaf X.O) (op U)).Additive :=
        Stacks.SheafOfModules.evaluationAdditive.{z}
          (R := (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) (op U);
      ∀ n p : ℕ, 0 < p →
      IsZero (((sectionsFunctor.{u, v, w, z} X U).rightDerived p).obj (F.obj ⟨n⟩)))
    (hlimOne : ∀ U, B U →
      IsZero (Rlim.firstDerivedLimit (sectionsSystem.{u, v, w, z} X F U))) :
    ∃ h : HasProduct (fun n : ℕ =>
        (F ⋙ DerivedCategory.singleFunctor
          (SheafOfModules.{z} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj ⟨n⟩),
      @IsDerivedLimit
        (DerivedCategory (SheafOfModules.{z} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
        _ _ _ _ _ _
        (F ⋙ DerivedCategory.singleFunctor
          (SheafOfModules.{z} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0) h
        ((DerivedCategory.singleFunctor
          (SheafOfModules.{z} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj
          (limit F))
```

**`Stacks.Cohomology.SiteInverseLimits.isZero_cohomology_limit_of_acyclic_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/InverseLimitOfAcyclicTower.lean, line 437](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/InverseLimitOfAcyclicTower.lean#L437). The attribute's comment: “acyclicity of the ordinary limit”.

> Under the same hypotheses, the ordinary inverse limit has vanishing positive-degree
> cohomology on every member of the covering class.

```lean
theorem isZero_cohomology_limit_of_acyclic_cover
    (F : ℕᵒᵖ ⥤ SheafOfModules.{z} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (B : ObjectProperty X.C) (hB : X.J.HasEnoughObjects B)
    (hcoh : ∀ U, B U →
      letI : (SheafOfModules.evaluation.{z}
          (Stacks.SheafOfModules.Tensor.ringSheaf X.O) (op U)).Additive :=
        Stacks.SheafOfModules.evaluationAdditive.{z}
          (R := (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) (op U);
      ∀ n p : ℕ, 0 < p →
      IsZero (((sectionsFunctor.{u, v, w, z} X U).rightDerived p).obj (F.obj ⟨n⟩)))
    (hlimOne : ∀ U, B U →
      IsZero (Rlim.firstDerivedLimit (sectionsSystem.{u, v, w, z} X F U)))
    (U : X.C) (hU : B U) (p : ℕ) (hp : 0 < p) :
    letI : (SheafOfModules.evaluation.{z}
        (Stacks.SheafOfModules.Tensor.ringSheaf X.O) (op U)).Additive :=
      Stacks.SheafOfModules.evaluationAdditive.{z}
        (R := (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) (op U);
    IsZero (((sectionsFunctor.{u, v, w, z} X U).rightDerived p).obj (limit F))
```

## Tag 0D6L, a lemma

[Tag 0D6L](https://stacks.math.columbia.edu/tag/0D6L) in the Stacks Project.

**`Stacks.Cohomology.DerivedLimitSections.cohomology_derivedLimit_projection_mono_on_sections_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/SectionsInjectivityUnconditional.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/SectionsInjectivityUnconditional.lean#L135).

> **Stacks Project, Tag 0D6L.** Let `(C, O)` be a ringed site, let `(Kₙ)` be an inverse system
> in `D(O)` with derived limit `L`, let `V` be an object of `C` and let `m` be an integer.  Suppose
> there are an index `N` and a cofinal system of coverings of `V` such that over every member
> `Vᵢ` of every covering in the system
>
> * `R¹ lim Hᵐ⁻¹(Vᵢ, Kₙ) = 0`, and
> * `Hᵐ(Vᵢ, Kₙ) ⟶ Hᵐ(Vᵢ, K_N)` is injective for `n ≥ N`.
>
> Then `Hᵐ(L)(V) ⟶ Hᵐ(K_N)(V)` is injective.
>
> Nothing is assumed: sheafification, local bijectivity, Grothendieck abelianness, the right
> derived functor presenting cohomology and the countable product presenting the derived limit are
> all theorems at this module universe, and are supplied above.

```lean
theorem cohomology_derivedLimit_projection_mono_on_sections_unconditional
    (K : ℕᵒᵖ ⥤ DerivedCategory
      (SheafOfModules.{max u v r w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (L : DerivedCategory
      (SheafOfModules.{max u v r w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (p : L ⟶ ∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩)
    (hL : ∃ δ : (∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
      Triangle.mk p (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) (n + 1) ≫
            K.map (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory
          (SheafOfModules.{max u v r w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (V : X.C) (m : ℤ) (N : ℕ)
    (Cov : CofinalCoveringSystem X.J V)
    (hlimOne : ∀ 𝒰 : PreZeroHypercover.{max u v} V, Cov.cov 𝒰 →
      ∀ i : 𝒰.I₀,
        let F := K ⋙ derivedSectionsPresheafMax.{u, v, r, w} X ⋙
          DerivedCategory.homologyFunctor
            (PresheafOfModules.{max u v r w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj)
              (m - 1) ⋙
          PresheafOfModules.evaluation
            (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj (.op (𝒰.X i))
        IsZero (cokernel (Pi.lift fun n : ℕ ↦
          Pi.π (fun n : ℕ ↦ F.obj ⟨n⟩) n -
            Pi.π (fun n : ℕ ↦ F.obj ⟨n⟩) (n + 1) ≫
              F.map (homOfLE (Nat.le_succ n)).op)))
    (hinj : ∀ 𝒰 : PreZeroHypercover.{max u v} V, Cov.cov 𝒰 →
      ∀ i : 𝒰.I₀,
        let F := K ⋙ derivedSectionsPresheafMax.{u, v, r, w} X ⋙
          DerivedCategory.homologyFunctor
            (PresheafOfModules.{max u v r w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj) m ⋙
          PresheafOfModules.evaluation
            (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj (.op (𝒰.X i))
        ∀ (n : ℕ) (hn : N ≤ n), Mono (F.map (homOfLE hn).op)) :
    Mono ((SheafOfModules.evaluation (Stacks.SheafOfModules.Tensor.ringSheaf X.O) (.op V)).map
      ((DerivedCategory.homologyFunctor
          (SheafOfModules.{max u v r w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) m).map
        (p ≫ Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) N)))
```

## Tag 0D6M, a lemma

[Tag 0D6M](https://stacks.math.columbia.edu/tag/0D6M) in the Stacks Project.

**`Stacks.Cohomology.isIso_to_isDerivedLimit_truncationGETower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/TruncationTowerConvergence.lean, line 1305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/TruncationTowerConvergence.lean#L1305).

> **Stacks Project, Tag 0D6M.** Under local, eventually vanishing cohomology bounds, the
> canonical map from a derived object to any derived limit of its truncations from below is an
> isomorphism.

```lean
theorem isIso_to_isDerivedLimit_truncationGETower
    {C : Type u} [Category.{v} C] {J : GrothendieckTopology C}
    (O : Sheaf J RingCat.{wRing})
    [HasSheafify J AddCommGrpCat.{wModule}]
    [J.WEqualsLocallyBijective AddCommGrpCat.{wModule}]
    [EnoughInjectives (SheafOfModules.{wModule} O)]
    (E : DerivedCategory (SheafOfModules.{wModule} O))
    (B : Set C)
    (basisCover : ∀ U : C, ∃ 𝒰 : PreZeroHypercover.{max u v} U,
      𝒰.sieve₀ ∈ J U ∧ ∀ i, B (𝒰.X i))
    (degreeBound : ∀ V : C, B V → ℤ → ℤ)
    (Cov : ∀ V : C, B V → Set (PreZeroHypercover.{max u v} V))
    (Cov_isCover : ∀ (V : C) (hV : B V) (𝒰 : PreZeroHypercover.{max u v} V),
      Cov V hV 𝒰 → 𝒰.sieve₀ ∈ J V)
    (Cov_cofinal : ∀ (V : C) (hV : B V) (𝒰 : PreZeroHypercover.{max u v} V),
      𝒰.sieve₀ ∈ J V →
        ∃ 𝒱 : PreZeroHypercover.{max u v} V, Cov V hV 𝒱 ∧ Nonempty (𝒱.Hom 𝒰))
    (vanishing : ∀ (V : C) (hV : B V) (𝒰 : PreZeroHypercover.{max u v} V),
      Cov V hV 𝒰 → ∀ (i : 𝒰.I₀) (p : ℕ) (m : ℤ),
        degreeBound V hV m < (p : ℤ) →
          IsZero (moduleCohomology O (𝒰.X i) p
            ((DerivedCategory.homologyFunctor (SheafOfModules.{wModule} O)
              (m - (p : ℤ))).obj E)))
    [HasProduct fun n : ℕ ↦
      (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} O) E).obj ⟨n⟩]
    (L : DerivedCategory (SheafOfModules.{wModule} O))
    (c : E ⟶ L)
    (q : L ⟶ ∏ᶜ fun n : ℕ ↦
      (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} O) E).obj ⟨n⟩)
    (δ : (∏ᶜ fun n : ℕ ↦
      (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} O) E).obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧)
    (hL : Triangle.mk q (Pi.lift fun n : ℕ ↦
      Pi.π (fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} O) E).obj ⟨n⟩) n -
        Pi.π (fun n : ℕ ↦
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} O) E).obj ⟨n⟩) (n + 1) ≫
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} O) E).map
            (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory (SheafOfModules.{wModule} O)))
    (hc : ∀ n : ℕ, c ≫ q ≫
      Pi.π (fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} O) E).obj ⟨n⟩) n =
        (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app E) :
    IsIso c
```

**`Stacks.Cohomology.isIso_to_isDerivedLimit_truncGETower_of_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/TruncationTowerConvergenceUnconditional.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/TruncationTowerConvergenceUnconditional.lean#L100).

> **Stacks Project, Tag 0D6M.** Let `O` be a sheaf of rings on a site `C`, let `E` be an
> object of the derived category of sheaves of `O`-modules, and let `B` be a set of objects of
> `C` large enough that every object is covered by members of `B`.  Suppose each `V ∈ B` carries
> a degree bound `p(V, -) : ℤ → ℤ` and a cofinal system of coverings of `V` on whose members
> `Hᵖ(Vᵢ, H^{m - p}(E)) = 0` whenever `p > p(V, m)`.  Then the canonical map from `E` to the
> derived limit of the truncation tower `n ↦ τ_{≥ -n} E` is an isomorphism.
>
> Nothing is assumed: sheafification, enough injectives and the countable products presenting the
> derived limit are all theorems at this module universe, and are supplied as instances above.

```lean
theorem isIso_to_isDerivedLimit_truncGETower_of_vanishing
    (O : Sheaf J RingCat.{r})
    (E : DerivedCategory (SheafOfModules.{max u v r w} O))
    (B : Set C)
    (basisCover : ∀ U : C, ∃ 𝒰 : PreZeroHypercover.{max u v} U,
      𝒰.sieve₀ ∈ J U ∧ ∀ i, B (𝒰.X i))
    (degreeBound : ∀ V : C, B V → ℤ → ℤ)
    (Cov : ∀ V : C, B V → Set (PreZeroHypercover.{max u v} V))
    (Cov_isCover : ∀ (V : C) (hV : B V) (𝒰 : PreZeroHypercover.{max u v} V),
      Cov V hV 𝒰 → 𝒰.sieve₀ ∈ J V)
    (Cov_cofinal : ∀ (V : C) (hV : B V) (𝒰 : PreZeroHypercover.{max u v} V),
      𝒰.sieve₀ ∈ J V →
        ∃ 𝒱 : PreZeroHypercover.{max u v} V, Cov V hV 𝒱 ∧ Nonempty (𝒱.Hom 𝒰))
    (vanishing : ∀ (V : C) (hV : B V) (𝒰 : PreZeroHypercover.{max u v} V),
      Cov V hV 𝒰 → ∀ (i : 𝒰.I₀) (p : ℕ) (m : ℤ),
        degreeBound V hV m < (p : ℤ) →
          IsZero (@moduleCohomology C instC J O hasSheafifyMax.{u, v, r, w}
            wEqualsLocallyBijectiveMax.{u, v, r, w}
            (SiteModules.moduleSheavesEnoughInjectives.{u, v, r, w} O)
            (𝒰.X i) p
            ((DerivedCategory.homologyFunctor (SheafOfModules.{max u v r w} O)
              (m - (p : ℤ))).obj E)))
    (L : DerivedCategory (SheafOfModules.{max u v r w} O))
    (c : E ⟶ L)
    (q : L ⟶ ∏ᶜ fun n : ℕ ↦
      (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩)
    (δ : (∏ᶜ fun n : ℕ ↦
      (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩) ⟶
        L⟦(1 : ℤ)⟧)
    (hL : Triangle.mk q (Pi.lift fun n : ℕ ↦
      Pi.π (fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩) n -
        Pi.π (fun n : ℕ ↦
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩)
            (n + 1) ≫
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).map
            (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory (SheafOfModules.{max u v r w} O)))
    (hc : ∀ n : ℕ, c ≫ q ≫
      Pi.π (fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩) n =
        (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app E) :
    IsIso c
```

## Tag 0D6N, a lemma

[Tag 0D6N](https://stacks.math.columbia.edu/tag/0D6N) in the Stacks Project.

**`Stacks.Cohomology.isIso_to_isDerivedLimit_truncationGETower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/TruncationTowerConvergence.lean, line 1305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/TruncationTowerConvergence.lean#L1305). The attribute's comment: “the constant-bound case, by taking the degree bound at V to be max d_V m”.

> **Stacks Project, Tag 0D6M.** Under local, eventually vanishing cohomology bounds, the
> canonical map from a derived object to any derived limit of its truncations from below is an
> isomorphism.

```lean
theorem isIso_to_isDerivedLimit_truncationGETower
    {C : Type u} [Category.{v} C] {J : GrothendieckTopology C}
    (O : Sheaf J RingCat.{wRing})
    [HasSheafify J AddCommGrpCat.{wModule}]
    [J.WEqualsLocallyBijective AddCommGrpCat.{wModule}]
    [EnoughInjectives (SheafOfModules.{wModule} O)]
    (E : DerivedCategory (SheafOfModules.{wModule} O))
    (B : Set C)
    (basisCover : ∀ U : C, ∃ 𝒰 : PreZeroHypercover.{max u v} U,
      𝒰.sieve₀ ∈ J U ∧ ∀ i, B (𝒰.X i))
    (degreeBound : ∀ V : C, B V → ℤ → ℤ)
    (Cov : ∀ V : C, B V → Set (PreZeroHypercover.{max u v} V))
    (Cov_isCover : ∀ (V : C) (hV : B V) (𝒰 : PreZeroHypercover.{max u v} V),
      Cov V hV 𝒰 → 𝒰.sieve₀ ∈ J V)
    (Cov_cofinal : ∀ (V : C) (hV : B V) (𝒰 : PreZeroHypercover.{max u v} V),
      𝒰.sieve₀ ∈ J V →
        ∃ 𝒱 : PreZeroHypercover.{max u v} V, Cov V hV 𝒱 ∧ Nonempty (𝒱.Hom 𝒰))
    (vanishing : ∀ (V : C) (hV : B V) (𝒰 : PreZeroHypercover.{max u v} V),
      Cov V hV 𝒰 → ∀ (i : 𝒰.I₀) (p : ℕ) (m : ℤ),
        degreeBound V hV m < (p : ℤ) →
          IsZero (moduleCohomology O (𝒰.X i) p
            ((DerivedCategory.homologyFunctor (SheafOfModules.{wModule} O)
              (m - (p : ℤ))).obj E)))
    [HasProduct fun n : ℕ ↦
      (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} O) E).obj ⟨n⟩]
    (L : DerivedCategory (SheafOfModules.{wModule} O))
    (c : E ⟶ L)
    (q : L ⟶ ∏ᶜ fun n : ℕ ↦
      (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} O) E).obj ⟨n⟩)
    (δ : (∏ᶜ fun n : ℕ ↦
      (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} O) E).obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧)
    (hL : Triangle.mk q (Pi.lift fun n : ℕ ↦
      Pi.π (fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} O) E).obj ⟨n⟩) n -
        Pi.π (fun n : ℕ ↦
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} O) E).obj ⟨n⟩) (n + 1) ≫
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} O) E).map
            (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory (SheafOfModules.{wModule} O)))
    (hc : ∀ n : ℕ, c ≫ q ≫
      Pi.π (fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} O) E).obj ⟨n⟩) n =
        (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app E) :
    IsIso c
```

**`Stacks.Cohomology.isIso_to_isDerivedLimit_truncGETower_of_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/TruncationTowerConvergenceUnconditional.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/TruncationTowerConvergenceUnconditional.lean#L100). The attribute's comment: “the constant-bound case, by taking the degree bound at V to be max d_V m”.

> **Stacks Project, Tag 0D6M.** Let `O` be a sheaf of rings on a site `C`, let `E` be an
> object of the derived category of sheaves of `O`-modules, and let `B` be a set of objects of
> `C` large enough that every object is covered by members of `B`.  Suppose each `V ∈ B` carries
> a degree bound `p(V, -) : ℤ → ℤ` and a cofinal system of coverings of `V` on whose members
> `Hᵖ(Vᵢ, H^{m - p}(E)) = 0` whenever `p > p(V, m)`.  Then the canonical map from `E` to the
> derived limit of the truncation tower `n ↦ τ_{≥ -n} E` is an isomorphism.
>
> Nothing is assumed: sheafification, enough injectives and the countable products presenting the
> derived limit are all theorems at this module universe, and are supplied as instances above.

```lean
theorem isIso_to_isDerivedLimit_truncGETower_of_vanishing
    (O : Sheaf J RingCat.{r})
    (E : DerivedCategory (SheafOfModules.{max u v r w} O))
    (B : Set C)
    (basisCover : ∀ U : C, ∃ 𝒰 : PreZeroHypercover.{max u v} U,
      𝒰.sieve₀ ∈ J U ∧ ∀ i, B (𝒰.X i))
    (degreeBound : ∀ V : C, B V → ℤ → ℤ)
    (Cov : ∀ V : C, B V → Set (PreZeroHypercover.{max u v} V))
    (Cov_isCover : ∀ (V : C) (hV : B V) (𝒰 : PreZeroHypercover.{max u v} V),
      Cov V hV 𝒰 → 𝒰.sieve₀ ∈ J V)
    (Cov_cofinal : ∀ (V : C) (hV : B V) (𝒰 : PreZeroHypercover.{max u v} V),
      𝒰.sieve₀ ∈ J V →
        ∃ 𝒱 : PreZeroHypercover.{max u v} V, Cov V hV 𝒱 ∧ Nonempty (𝒱.Hom 𝒰))
    (vanishing : ∀ (V : C) (hV : B V) (𝒰 : PreZeroHypercover.{max u v} V),
      Cov V hV 𝒰 → ∀ (i : 𝒰.I₀) (p : ℕ) (m : ℤ),
        degreeBound V hV m < (p : ℤ) →
          IsZero (@moduleCohomology C instC J O hasSheafifyMax.{u, v, r, w}
            wEqualsLocallyBijectiveMax.{u, v, r, w}
            (SiteModules.moduleSheavesEnoughInjectives.{u, v, r, w} O)
            (𝒰.X i) p
            ((DerivedCategory.homologyFunctor (SheafOfModules.{max u v r w} O)
              (m - (p : ℤ))).obj E)))
    (L : DerivedCategory (SheafOfModules.{max u v r w} O))
    (c : E ⟶ L)
    (q : L ⟶ ∏ᶜ fun n : ℕ ↦
      (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩)
    (δ : (∏ᶜ fun n : ℕ ↦
      (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩) ⟶
        L⟦(1 : ℤ)⟧)
    (hL : Triangle.mk q (Pi.lift fun n : ℕ ↦
      Pi.π (fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩) n -
        Pi.π (fun n : ℕ ↦
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩)
            (n + 1) ≫
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).map
            (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory (SheafOfModules.{max u v r w} O)))
    (hc : ∀ n : ℕ, c ≫ q ≫
      Pi.π (fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩) n =
        (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app E) :
    IsIso c
```

## Tag 08U3, a lemma

[Tag 08U3](https://stacks.math.columbia.edu/tag/08U3) in the Stacks Project.

**`Stacks.Cohomology.isIso_to_isDerivedLimit_truncGETower_of_degreeBound`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/TruncationConvergenceUnderBounds.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/TruncationConvergenceUnderBounds.lean#L87). The attribute's comment: “variant: the single-universe form, for a ringed site whose module category has enough injectives and the countable product of the truncation tower; the tag, with neither of these, is Stacks.Cohomology.DegreeBound.isIso_to_isDerivedLimit_truncGETower_of_degreeBound”.

> Degree-dependent bounds for cohomology on a locally covering class imply that the canonical
> map to the derived limit of the lower-truncation tower is an isomorphism.
>
> This is a variant of [Stacks, Tag 08U3]: the enough-injectives and product hypotheses below are
> not hypotheses of the source, and they are avoidable.  The full statement is
> `Stacks.Cohomology.DegreeBound.isIso_to_isDerivedLimit_truncGETower_of_degreeBound`, which
> discharges them by taking the module universe large enough to contain the site and the structure
> rings.  This single-universe form is kept for the consumers that are already stated at it.

```lean
theorem isIso_to_isDerivedLimit_truncGETower_of_degreeBound
    (S : AlgebraicGeometry.RingedSite.{u, u, u})
    [HasSheafify S.J AddCommGrpCat.{u}]
    [S.J.WEqualsLocallyBijective AddCommGrpCat.{u}]
    [EnoughInjectives (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.O))]
    (E : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.O)))
    (degreeBound : ℤ → ℤ) (B : Set S.C)
    (basisCover : ∀ U : S.C, ∃ 𝒰 : PreZeroHypercover.{u} U,
      𝒰.sieve₀ ∈ S.J U ∧ ∀ i, B (𝒰.X i))
    (vanishing : ∀ (V : S.C), B V → ∀ (p : ℕ) (m : ℤ),
      degreeBound m < (p : ℤ) →
        IsZero (moduleCohomology (Stacks.SheafOfModules.Tensor.ringSheaf S.O) V p
          ((DerivedCategory.homologyFunctor
            (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.O))
            (m - (p : ℤ))).obj E)))
    (L : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.O)))
    [HasProduct fun n : ℕ ↦
      (Stacks.DerivedLimit.truncGETower
        (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.O)) E).obj ⟨n⟩]
    (q : L ⟶ ∏ᶜ fun n : ℕ ↦
      (Stacks.DerivedLimit.truncGETower
        (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.O)) E).obj ⟨n⟩)
    (hL : ∃ δ :
      (∏ᶜ fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower
          (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.O)) E).obj ⟨n⟩) ⟶
          L⟦(1 : ℤ)⟧,
      Triangle.mk q (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦
          (Stacks.DerivedLimit.truncGETower
            (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.O)) E).obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦
            (Stacks.DerivedLimit.truncGETower
              (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.O)) E).obj ⟨n⟩)
              (n + 1) ≫
            (Stacks.DerivedLimit.truncGETower
              (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.O)) E).map
              (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang
          (DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.O))))
    (c : E ⟶ L)
    (hc : ∀ n : ℕ, c ≫ q ≫ Pi.π
      (fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower
          (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.O)) E).obj ⟨n⟩) n =
      (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app E) :
    IsIso c
```

**`Stacks.Cohomology.DegreeBound.isIso_to_isDerivedLimit_truncGETower_of_degreeBound`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/TruncationConvergenceUnderBoundsUnconditional.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/TruncationConvergenceUnderBoundsUnconditional.lean#L80).

> **Stacks Project, Tag 08U3.** Let `O` be a sheaf of rings on a site `C` and let `E` be an
> object of the derived category of sheaves of `O`-modules.  Suppose there are a function
> `p(-) : ℤ → ℤ` and a set `B` of objects of `C` such that every object of `C` has a covering whose
> members are elements of `B`, and such that `H^p(V, H^{m - p}(E)) = 0` for all `p > p(m)` and all
> `V ∈ B`.  Then the canonical map `E ⟶ R lim τ_{≥ -n} E` is an isomorphism.
>
> Nothing else is assumed: sheafification, enough injectives and the countable products presenting
> the derived limit are all theorems at this module universe.

```lean
theorem isIso_to_isDerivedLimit_truncGETower_of_degreeBound
    (O : Sheaf J RingCat.{r})
    (E : DerivedCategory (SheafOfModules.{max u v r w} O))
    (degreeBound : ℤ → ℤ) (B : Set C)
    (basisCover : ∀ U : C, ∃ 𝒰 : PreZeroHypercover.{max u v} U,
      𝒰.sieve₀ ∈ J U ∧ ∀ i, B (𝒰.X i))
    (vanishing : ∀ (V : C), B V → ∀ (p : ℕ) (m : ℤ), degreeBound m < (p : ℤ) →
      IsZero (@moduleCohomology C instC J O hasSheafifyMax.{u, v, r, w}
        wEqualsLocallyBijectiveMax.{u, v, r, w}
        (SiteModules.moduleSheavesEnoughInjectives.{u, v, r, w} O) V p
        ((DerivedCategory.homologyFunctor (SheafOfModules.{max u v r w} O)
          (m - (p : ℤ))).obj E)))
    (L : DerivedCategory (SheafOfModules.{max u v r w} O))
    (c : E ⟶ L)
    (q : L ⟶ ∏ᶜ fun n : ℕ ↦
      (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩)
    (hL : ∃ δ : (∏ᶜ fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩) ⟶
          L⟦(1 : ℤ)⟧,
      Triangle.mk q (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦
            (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩)
              (n + 1) ≫
            (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).map
              (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory (SheafOfModules.{max u v r w} O)))
    (hc : ∀ n : ℕ, c ≫ q ≫
      Pi.π (fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩) n =
        (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app E) :
    IsIso c
```

## Tag 0D6P, a lemma

[Tag 0D6P](https://stacks.math.columbia.edu/tag/0D6P) in the Stacks Project.

**`Stacks.Cohomology.UniformBound.isIso_to_isDerivedLimit_truncGETower_of_vanishing_uniform`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/TruncationConvergenceUniformBoundUnconditional.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/TruncationConvergenceUniformBoundUnconditional.lean#L57).

> Let `O` be a sheaf of rings on a site `C` and let `E` be an object of the derived category of
> sheaves of `O`-modules.  Suppose there are an integer `d ≥ 0` and a set `B` of objects of `C`
> such that every object of `C` has a covering whose members are elements of `B`, and such that
> `H^p(V, H^q(E)) = 0` for all `p > d`, all `q < 0` and all `V ∈ B`.  Then the canonical map
> `E ⟶ R lim τ_{≥ -n} E` is an isomorphism.
>
> Here `R lim τ_{≥ -n} E` is an object `L` with a distinguished triangle
> `L ⟶ ∏ τ_{≥ -n} E ⟶ ∏ τ_{≥ -n} E ⟶ L[1]`, and `c : E ⟶ L` is the map whose composites with
> the product projections are the truncation maps `E ⟶ τ_{≥ -n} E`.

```lean
theorem isIso_to_isDerivedLimit_truncGETower_of_vanishing_uniform
    (O : Sheaf J RingCat.{r})
    (E : DerivedCategory (SheafOfModules.{max u v r w} O))
    (d : ℤ) (hd : 0 ≤ d) (B : Set C)
    (basisCover : ∀ U : C, ∃ 𝒰 : PreZeroHypercover.{max u v} U,
      𝒰.sieve₀ ∈ J U ∧ ∀ i, B (𝒰.X i))
    (vanishing : ∀ (V : C), B V → ∀ (p : ℕ), d < (p : ℤ) → ∀ (q : ℤ), q < 0 →
      IsZero (@moduleCohomology C instC J O hasSheafifyMax.{u, v, r, w}
        wEqualsLocallyBijectiveMax.{u, v, r, w}
        (SiteModules.moduleSheavesEnoughInjectives.{u, v, r, w} O) V p
        ((DerivedCategory.homologyFunctor (SheafOfModules.{max u v r w} O) q).obj E)))
    (L : DerivedCategory (SheafOfModules.{max u v r w} O))
    (c : E ⟶ L)
    (q : L ⟶ ∏ᶜ fun n : ℕ ↦
      (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩)
    (hL : ∃ δ : (∏ᶜ fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩) ⟶
          L⟦(1 : ℤ)⟧,
      Triangle.mk q (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦
            (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩)
              (n + 1) ≫
            (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).map
              (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory (SheafOfModules.{max u v r w} O)))
    (hc : ∀ n : ℕ, c ≫ q ≫
      Pi.π (fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v r w} O) E).obj ⟨n⟩) n =
        (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app E) :
    IsIso c
```

## Tag 0BKZ, a lemma

[Tag 0BKZ](https://stacks.math.columbia.edu/tag/0BKZ) in the Stacks Project.

**`AlgebraicGeometry.isIso_hypercohomologyEdge_app_of_isAffineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/AffineOpenHypercohomologyEdge.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/AffineOpenHypercohomologyEdge.lean#L72). The attribute's comment: “at the affine opens of a scheme, for an object with quasi-coherent cohomology”. References: EGA III (1.3.1), “more general”.

> **The hypercohomology edge morphism over an affine open of a scheme is invertible**, at an
> object of `D(𝒪_X)` whose cohomology sheaves are all quasi-coherent, in every degree and with no
> boundedness hypothesis.
>
> This is [Stacks, Tag 0BKZ] at the basis of affine opens of `X`: the basis has enough objects,
> and the cohomology sheaves are acyclic over every member of it by Serre vanishing.

```lean
theorem isIso_hypercohomologyEdge_app_of_isAffineOpen
    (hE : ∀ q : ℤ, ((DerivedCategory.homologyFunctor X.Modules q).obj E).IsQuasicoherent)
    (U : X.Opens) (hU : U ∈ X.affineOpens) (q : ℤ) :
    IsIso ((Stacks.Cohomology.HypercohomologyEdge.hypercohomologyEdge
      X.ringCatSheaf U q).app E)
```

**`Stacks.Cohomology.HypercohomologyEdge.isIso_hypercohomologyEdge_app_of_acyclic_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/HypercohomologyEdge/AcyclicObject.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/HypercohomologyEdge/AcyclicObject.lean#L162).

> **Stacks Project Tag 0BKZ.** If the cohomology sheaves of an object of the unbounded derived
> category of `O`-modules have no higher cohomology over the members of a class of objects covering
> the site, then over each member its degree-`q` hypercohomology is the module of sections of its
> degree-`q` cohomology sheaf: the hypercohomology edge morphism is invertible there, in every
> degree.

```lean
theorem isIso_hypercohomologyEdge_app_of_acyclic_cover (U : C)
    (K : DerivedCategory (SheafOfModules.{wModule} O))
    (B : ObjectProperty C) (hB : J.HasEnoughObjects B)
    (hvan : ∀ V : C, B V → ∀ p : ℕ, 0 < p → ∀ m : ℤ,
      IsZero (((SheafOfModules.evaluation O (.op V)).rightDerived p).obj
        ((DerivedCategory.homologyFunctor (SheafOfModules.{wModule} O) m).obj K)))
    (hU : B U) (q : ℤ) :
    IsIso ((hypercohomologyEdge O U q).app K)
```

## Tag 0A09, a lemma

[Tag 0A09](https://stacks.math.columbia.edu/tag/0A09) in the Stacks Project.

**`Stacks.Cohomology.DerivedLimitAcyclic.isLimit_cohomology_of_isDerivedLimit_of_acyclic_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/CohomologyCommutesWithDerivedLimit.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/CohomologyCommutesWithDerivedLimit.lean#L80).

> **Stacks Project Tag 0A09.** Cohomology commutes with a derived inverse limit if there is a
> class of objects covering the site on which all positive cohomology of the cohomology sheaves
> vanishes and the towers of their sections have vanishing first derived inverse limit.
>
> The conclusion records the canonical limiting cone: the legs of the cone on the system of
> degree-`q` cohomology sheaves are induced by the projections of a derived-limit triangle for
> `L`.

```lean
theorem isLimit_cohomology_of_isDerivedLimit_of_acyclic_cover
    (K : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (L : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hL : IsDerivedLimit K L)
    (B : ObjectProperty X.C)
    (hB : X.J.HasEnoughObjects B)
    (hacyclic : ∀ U, B U → ∀ q : ℤ, ∀ n : ℕ, ∀ r : ℕ, 0 < r →
      haveI := evaluation_additive (Stacks.SheafOfModules.Tensor.ringSheaf X.O) U
      IsZero (((SheafOfModules.evaluation
            (Stacks.SheafOfModules.Tensor.ringSheaf X.O) (op U)).rightDerived r).obj
        ((DerivedCategory.homologyFunctor
            (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) q).obj
          (K.obj ⟨n⟩))))
    (hlimOne : ∀ U, B U → ∀ q : ℤ,
      IsZero (Rlim.firstDerivedLimit
        (K ⋙ DerivedCategory.homologyFunctor
            (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) q ⋙
          sectionsOverObject X U)))
    (q : ℤ) :
    ∃ p : L ⟶ ∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩,
      (∃ δ : (∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
        Triangle.mk p (Pi.lift fun n : ℕ ↦
          Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n -
            Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) (n + 1) ≫
              K.map (homOfLE (Nat.le_succ n)).op) δ ∈
          distTriang
            (DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))) ∧
      ∃ τ : (Functor.const ℕᵒᵖ).obj
          ((DerivedCategory.homologyFunctor
              (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) q).obj L) ⟶
          K ⋙ DerivedCategory.homologyFunctor
            (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) q,
        (∀ n : ℕ, τ.app ⟨n⟩ =
          (DerivedCategory.homologyFunctor
              (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) q).map
            (p ≫ Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n)) ∧
        Nonempty (IsLimit (Cone.mk _ τ))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.23, Tag 0940](https://stacks.math.columbia.edu/tag/0940)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
