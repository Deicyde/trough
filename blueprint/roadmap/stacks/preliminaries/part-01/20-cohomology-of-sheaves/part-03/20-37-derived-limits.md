---
declaration: section
origin: cited
lean: Stacks.Cohomology.DerivedLimitSections.isDerivedLimit_map_derivedSections, Stacks.Cohomology.DerivedLimitSections.exists_shortExact_limOne_cohomology_derivedLimit, AlgebraicGeometry.GrothendieckExistence.isDerivedLimit_map_derivedSectionsLocallySmall, Stacks.Cohomology.DerivedSectionsOverBase.isDerivedLimit_map_derivedSectionsOver, Stacks.Cohomology.DerivedSectionsOverBase.exists_shortExact_homology_derivedSectionsOver, Stacks.Cohomology.DerivedLimits.isDerivedLimit_map_derivedSections, Stacks.Cohomology.DerivedLimits.exists_shortExact_limOne_cohomology_derivedLimit, Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.isDerivedLimit_map_derivedPushforward
statement: formalized
proof: formalized
---

# 20.37 Derived limits

Section 20.37 of the Stacks Project, [Tag 0BKN](https://stacks.math.columbia.edu/tag/0BKN). 11 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D60, a lemma

[Tag 0D60](https://stacks.math.columbia.edu/tag/0D60) in the Stacks Project.

**`Stacks.Cohomology.DerivedLimitSections.isDerivedLimit_map_derivedSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/SpaltensteinCriterion/DerivedSectionsLimit.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/SpaltensteinCriterion/DerivedSectionsLimit.lean#L209). The attribute's comment: “commutation with derived limits”.

> Derived sections over an open of a ringed space carry a countable derived inverse limit to a
> derived inverse limit: `RΓ(U, R\lim Kₙ) = R\lim RΓ(U, Kₙ)`.

```lean
theorem isDerivedLimit_map_derivedSections
    (RGamma : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)) ⥤
      DerivedCategory AddCommGrpCat.{u})
    (comparison : (sections X U).mapHomologicalComplex (ComplexShape.up ℤ) ⋙
      DerivedCategory.Q ⟶ DerivedCategory.Q ⋙ RGamma)
    (hRGamma : RGamma.IsRightDerivedFunctor comparison
      (HomologicalComplex.quasiIso (SheafOfModules.{u} (structureSheafRing X)) (ComplexShape.up ℤ)))
    (K : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    [HasProduct fun n : ℕ ↦ K.obj ⟨n⟩]
    (L : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) (hL : IsDerivedLimit K L) :
    ∃ h : HasProduct (fun n : ℕ ↦ RGamma.obj (K.obj ⟨n⟩)),
      @IsDerivedLimit (DerivedCategory AddCommGrpCat.{u}) _ _ _ _ _ _
        (K ⋙ RGamma) h (RGamma.obj L)
```

**`Stacks.Cohomology.DerivedLimitSections.exists_shortExact_limOne_cohomology_derivedLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/SpaltensteinCriterion/DerivedSectionsLimit.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/SpaltensteinCriterion/DerivedSectionsLimit.lean#L267). The attribute's comment: “short exact sequence”.

> For every open `U` of a ringed space and every degree `m`, the cohomology of a countable
> derived inverse limit lies in the Milnor short exact sequence
>
> `0 ⟶ R¹\lim H^{m-1}(U, Kₙ) ⟶ H^m(U, R\lim Kₙ) ⟶ \lim H^m(U, Kₙ) ⟶ 0`.
>
> Here `R¹\lim` is the cokernel of the difference map `1 - shift` on the product of the groups
> `H^{m-1}(U, Kₙ)`. The map to the inverse limit is characterised by its composites with the limit
> projections, which are the maps on cohomology induced by the given structural maps `L ⟶ Kₙ`.

```lean
theorem exists_shortExact_limOne_cohomology_derivedLimit
    (RGamma : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)) ⥤
      DerivedCategory AddCommGrpCat.{u})
    (comparison : (sections X U).mapHomologicalComplex (ComplexShape.up ℤ) ⋙
      DerivedCategory.Q ⟶ DerivedCategory.Q ⋙ RGamma)
    (hRGamma : RGamma.IsRightDerivedFunctor comparison
      (HomologicalComplex.quasiIso (SheafOfModules.{u} (structureSheafRing X)) (ComplexShape.up ℤ)))
    (K : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (L : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    [HasProduct fun n : ℕ ↦ K.obj ⟨n⟩]
    (p : L ⟶ ∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩)
    (hL : ∃ δ : (∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
      Triangle.mk p (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) (n + 1) ≫
            K.map (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory (SheafOfModules.{u} (structureSheafRing X))))
    (m : ℤ) :
    let Hprev := DerivedCategory.homologyFunctor AddCommGrpCat.{u} (m - 1)
    let Hcur := DerivedCategory.homologyFunctor AddCommGrpCat.{u} m
    let Fprev := K ⋙ RGamma ⋙ Hprev
    let Fcur := K ⋙ RGamma ⋙ Hcur
    let dprev : (∏ᶜ fun n : ℕ ↦ Fprev.obj ⟨n⟩) ⟶ (∏ᶜ fun n : ℕ ↦ Fprev.obj ⟨n⟩) :=
      Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦ Fprev.obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦ Fprev.obj ⟨n⟩) (n + 1) ≫
            Fprev.map (homOfLE (Nat.le_succ n)).op
    ∃ (i : cokernel dprev ⟶ Hcur.obj (RGamma.obj L))
      (q : Hcur.obj (RGamma.obj L) ⟶ limit Fcur) (zero : i ≫ q = 0),
      ((ShortComplex.mk i q zero).ShortExact ∧
        ∀ n : ℕ, q ≫ limit.π Fcur ⟨n⟩ =
          Hcur.map (RGamma.map (p ≫ Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n)))
```

**`AlgebraicGeometry.GrothendieckExistence.isDerivedLimit_map_derivedSectionsLocallySmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/GrothendieckExistence/DerivedLimitBounded.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/GrothendieckExistence/DerivedLimitBounded.lean#L204). The attribute's comment: “commutation with derived limits, for the Γ(X, U)-module valued derived sections over an open at the locally small model”.

> **[Stacks, Tag 0D60], first assertion, for `RΓ(U, -)` at the locally small model.** If `K` is a
> derived limit of an inverse system `(Kₙ)` in `D(𝒪_X)`, then `RΓ(U, K)` is a derived limit of the
> system `(RΓ(U, Kₙ))` in `D(Γ(X, U))`; the existence of the product of the images is part of the
> conclusion.
>
> This is [Stacks, Tag 08U1]: `𝒪_X`-modules are Grothendieck abelian, `Γ(X, U)`-modules have exact
> countable products, and sections over `U` preserve countable products, so the right derived
> functor of sections carries a derived-limit triangle to a derived-limit triangle. The instances of
> Tag 0D60 already in the library are stated either for `Ab`-valued derived sections over an open, or
> for module-valued derived sections over the base ring at `HasDerivedCategory.standard`; this one is
> `Γ(X, U)`-module valued at the locally small model, which is the model
> `Stacks.Duality.Coherator.AffineAmplitudeIn` is set at.

```lean
theorem isDerivedLimit_map_derivedSectionsLocallySmall (U : X.Opens)
    (L : ℕᵒᵖ ⥤ DerivedCategory X.Modules) [HasProduct fun n : ℕ => L.obj ⟨n⟩]
    (K : DerivedCategory X.Modules) (hK : IsDerivedLimit L K) :
    ∃ h : HasProduct fun n : ℕ => (derivedSectionsLocallySmall X U).obj (L.obj ⟨n⟩),
      @IsDerivedLimit (DerivedCategory (ModuleCat.{u} Γ(X, U))) _ _ _ _ _ _
        (L ⋙ derivedSectionsLocallySmall X U) h ((derivedSectionsLocallySmall X U).obj K)
```

**`Stacks.Cohomology.DerivedSectionsOverBase.isDerivedLimit_map_derivedSectionsOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/DerivedSectionsOverBase.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/DerivedSectionsOverBase.lean#L190). The attribute's comment: “commutation with derived limits, for derived sections over a base ring”.

> **Derived sections over a base ring commute with derived limits.** If a distinguished triangle
> exhibits `L` as the derived limit of a countable inverse system `(K_n)` of objects of `D(𝒪_X)`,
> then `RΓ(X, L)` is the derived limit of the system `(RΓ(X, K_n))` in `D(A)`; the existence of the
> product of the images is part of the conclusion.

```lean
theorem isDerivedLimit_map_derivedSectionsOver
    (K : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (L : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (hL : IsDerivedLimit K L) :
    ∃ h : HasProduct (fun n : ℕ ↦ (derivedSectionsOver X ρ).obj (K.obj ⟨n⟩)),
      @IsDerivedLimit (DerivedCategory (ModuleCat.{u} A)) _ _ _ _ _ _
        (K ⋙ derivedSectionsOver X ρ) h ((derivedSectionsOver X ρ).obj L)
```

**`Stacks.Cohomology.DerivedSectionsOverBase.exists_shortExact_homology_derivedSectionsOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/DerivedSectionsOverBase.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/DerivedSectionsOverBase.lean#L216). The attribute's comment: “short exact sequence, for derived sections over a base ring; both maps normalized”.

> **The Milnor short exact sequence for the cohomology of derived sections of a derived limit.**
> With `L` the derived limit of `(K_n)` in `D(𝒪_X)`, the cohomology modules `Hʳ(X, L)` of its derived
> sections over `A` fit into short exact sequences
>
> `0 ⟶ R¹lim Hʳ⁻¹(X, K_n) ⟶ Hʳ(X, L) ⟶ lim Hʳ(X, K_n) ⟶ 0`,
>
> where `R¹lim` is the cokernel of `1 - shift` on the product of the cohomologies. The inclusion
> descends the connecting morphism of the Milnor triangle and the projection is characterized by the
> limit projections.
>
> The product of the images is taken as a hypothesis here, as it is in the general Milnor sequence;
> `isDerivedLimit_map_derivedSectionsOver` provides it.

```lean
theorem exists_shortExact_homology_derivedSectionsOver
    (K : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (L : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (hL : IsDerivedLimit K L) :
    let F : ℕᵒᵖ ⥤ DerivedCategory (ModuleCat.{u} A) := K ⋙ derivedSectionsOver X ρ
    let Y : ℕ → DerivedCategory (ModuleCat.{u} A) := fun n ↦ F.obj (op n)
    let d : (∏ᶜ Y) ⟶ ∏ᶜ Y := Pi.lift fun n : ℕ ↦
      Pi.π Y n - Pi.π Y (n + 1) ≫ F.map (homOfLE (Nat.le_succ n)).op
    ∃ (a : (derivedSectionsOver X ρ).obj L ⟶ ∏ᶜ Y)
      (b : (∏ᶜ Y) ⟶ ((derivedSectionsOver X ρ).obj L)⟦(1 : ℤ)⟧),
      let T := Triangle.mk a d b
      T ∈ distTriang (DerivedCategory (ModuleCat.{u} A)) ∧
        ∀ r : ℤ,
          let H := DerivedCategory.homologyFunctor (ModuleCat.{u} A) r
          let H₁ := DerivedCategory.homologyFunctor (ModuleCat.{u} A) (r - 1)
          let homologySystem : ℕᵒᵖ ⥤ ModuleCat.{u} A := F ⋙ H
          let shiftedHomologySystem : ℕᵒᵖ ⥤ ModuleCat.{u} A := F ⋙ H₁
          let P : ModuleCat.{u} A :=
            ∏ᶜ fun n : ℕ ↦ shiftedHomologySystem.obj (op n)
          let δ : P ⟶ P := Pi.lift fun n : ℕ ↦
            Pi.π (fun n : ℕ ↦ shiftedHomologySystem.obj (op n)) n -
              Pi.π (fun n : ℕ ↦ shiftedHomologySystem.obj (op n)) (n + 1) ≫
                shiftedHomologySystem.map (homOfLE (Nat.le_succ n)).op
          ∃ (e : H₁.obj (∏ᶜ Y) ≅ P)
            (i : cokernel δ ⟶ H.obj ((derivedSectionsOver X ρ).obj L))
            (q : H.obj ((derivedSectionsOver X ρ).obj L) ⟶ limit homologySystem)
            (w : i ≫ q = 0),
            e.hom = piComparison H₁ Y ∧
              cokernel.π δ ≫ i = e.inv ≫
                DerivedCategory.HomologySequence.δ T (r - 1) r ∧
              (∀ n : ℕ, q ≫ limit.π homologySystem (op n) =
                H.map a ≫ H.map (Pi.π Y n)) ∧
              (ShortComplex.mk i q w).ShortExact
```

**`Stacks.Cohomology.DerivedLimits.isDerivedLimit_map_derivedSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimits.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimits.lean#L248). The attribute's comment: “commutation with derived limits”.

> **Stacks 0D60, first assertion.** Derived sections over an open carry a countable derived
> inverse limit to a derived inverse limit.

```lean
theorem isDerivedLimit_map_derivedSections
    (X : RingedSpace.{u, u})
    (U : Opens X.carrier)
    (RGamma : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)) ⥤
      DerivedCategory AddCommGrpCat.{u})
    (comparison :
      (SheafOfModules.toSheaf (structureSheafRing X) ⋙
          (sheafSections (Opens.grothendieckTopology X.carrier) AddCommGrpCat.{u}).obj
            (op U)).mapHomologicalComplex (ComplexShape.up ℤ) ⋙ DerivedCategory.Q ⟶
        DerivedCategory.Q ⋙ RGamma)
    (hRGamma : RGamma.IsRightDerivedFunctor comparison
      (HomologicalComplex.quasiIso (SheafOfModules.{u} (structureSheafRing X))
        (ComplexShape.up ℤ)))
    (K : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    [HasProduct fun n : ℕ ↦ K.obj ⟨n⟩]
    (L : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (hL : IsDerivedLimit K L) :
    ∃ h : HasProduct (fun n : ℕ ↦ RGamma.obj (K.obj ⟨n⟩)),
      @IsDerivedLimit
        (DerivedCategory AddCommGrpCat.{u}) _ _ _ _ _ _
        (K ⋙ RGamma) h (RGamma.obj L)
```

**`Stacks.Cohomology.DerivedLimits.exists_shortExact_limOne_cohomology_derivedLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimits.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimits.lean#L332). The attribute's comment: “short exact sequence”.

> **Stacks 0D60, second assertion.** For every open `U` and degree `m`, the cohomology of a
> derived inverse limit lies in the Milnor short exact sequence
> `0 ⟶ R¹ lim Hᵐ⁻¹(U,Kₙ) ⟶ Hᵐ(U,R lim Kₙ) ⟶ lim Hᵐ(U,Kₙ) ⟶ 0`.
>
> Here `R¹ lim` is represented by the cokernel of the standard difference map on the product of
> the underlying cohomology groups. The last map is characterized by its composites with the
> limit projections, which are induced by the structural maps `L ⟶ Kₙ`.

```lean
theorem exists_shortExact_limOne_cohomology_derivedLimit
    (X : RingedSpace.{u, u})
    (U : Opens X.carrier)
    (RGamma : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)) ⥤
      DerivedCategory AddCommGrpCat.{u})
    (comparison :
      (SheafOfModules.toSheaf (structureSheafRing X) ⋙
          (sheafSections (Opens.grothendieckTopology X.carrier) AddCommGrpCat.{u}).obj
            (op U)).mapHomologicalComplex (ComplexShape.up ℤ) ⋙ DerivedCategory.Q ⟶
        DerivedCategory.Q ⋙ RGamma)
    (hRGamma : RGamma.IsRightDerivedFunctor comparison
      (HomologicalComplex.quasiIso (SheafOfModules.{u} (structureSheafRing X))
        (ComplexShape.up ℤ)))
    (K : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (L : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    [HasProduct fun n : ℕ ↦ K.obj ⟨n⟩]
    (p : L ⟶ ∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩)
    (hL : ∃ δ : (∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
      Triangle.mk p (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) (n + 1) ≫
            K.map (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory (SheafOfModules.{u} (structureSheafRing X))))
    (m : ℤ) :
    let A := AddCommGrpCat.{u}
    let Hprev := DerivedCategory.homologyFunctor A (m - 1)
    let Hcur := DerivedCategory.homologyFunctor A m
    let Fprev := K ⋙ RGamma ⋙ Hprev
    let Fcur := K ⋙ RGamma ⋙ Hcur
    let dprev := Pi.lift fun n : ℕ ↦
      Pi.π (fun n : ℕ ↦ Fprev.obj ⟨n⟩) n -
        Pi.π (fun n : ℕ ↦ Fprev.obj ⟨n⟩) (n + 1) ≫
          Fprev.map (homOfLE (Nat.le_succ n)).op
    ∃ (i : cokernel dprev ⟶
        Hcur.obj (RGamma.obj L))
      (q : Hcur.obj (RGamma.obj L) ⟶ limit Fcur)
      (zero : i ≫ q = 0),
      ((ShortComplex.mk i q zero).ShortExact ∧
        ∀ n : ℕ, q ≫ limit.π Fcur ⟨n⟩ =
          Hcur.map (RGamma.map (p ≫ Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n)))
```

## Tag 0BKP, a lemma

[Tag 0BKP](https://stacks.math.columbia.edu/tag/0BKP) in the Stacks Project.

**`Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.isDerivedLimit_map_derivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/DerivedLimits.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/DerivedLimits.lean#L67).

> Derived pushforward along a morphism of ringed spaces commutes with derived limits: it carries
> an object exhibited as the derived limit of a countable inverse system to the derived limit of the
> pushed-forward system.

```lean
theorem isDerivedLimit_map_derivedPushforward
    (K : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    [HasProduct fun n : ℕ ↦ K.obj ⟨n⟩]
    (L : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (hL : IsDerivedLimit K L) :
    ∃ h : HasProduct (fun n : ℕ ↦ Rf.obj (K.obj ⟨n⟩)),
      @IsDerivedLimit (DerivedCategory (SheafOfModules.{u} (structureSheafRing Y))) _ _ _ _ _ _
        (K ⋙ Rf) h (Rf.obj L)
```

## Tag 0BKQ, a remark

[Tag 0BKQ](https://stacks.math.columbia.edu/tag/0BKQ) in the Stacks Project.

**`Stacks.Cohomology.DerivedLimits.sheafificationCohomologyPresheafSystemIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimitComparisonDiagram.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimitComparisonDiagram.lean#L168). The attribute's comment: “the cohomology sheaf H^m(K\_n) of each member of the inverse system is the sheafification of the cohomology presheaf U ↦ H^m(U, K\_n), naturally in n”.

> **Stacks 0BKQ, first assertion.** For an inverse system `(Kₙ)` in `D(O)` and a degree `m`,
> the cohomology sheaf `𝓗ᵐ_n = Hᵐ(Kₙ)` is the sheafification of the cohomology presheaf
> `underline 𝓗ᵐ_n : U ↦ Hᵐ(U, Kₙ)`, naturally in `n`: sheafifying the system of cohomology
> presheaves of the `Kₙ` gives the system of their cohomology sheaves, compatibly with the
> transition maps of the system.
>
> This is Tag 0BKJ applied to each `Kₙ`, read as an isomorphism of systems; the same statement for
> a derived limit `L` of the system -- that `𝓗ᵐ = Hᵐ(R lim Kₙ)` is the sheafification of
> `underline 𝓗ᵐ : U ↦ Hᵐ(U, R lim Kₙ)` -- is Tag 0BKJ at the single object `L`, i.e. the component
> `(sheafificationCohomologyPresheafIso O m).app L`. Both appear in
> `Stacks.Cohomology.DerivedLimits.cohomologyDerivedLimitDiagram`, which puts them into the
> remark's square.

```lean
def sheafificationCohomologyPresheafSystemIso {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
    [HasDerivedCategory.{wX} (SheafOfModules.{u} O)]
    [HasDerivedCategory.{wP} (PresheafOfModules.{u} O.obj)]
    (K : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{u} O)) (m : ℤ) :
    (K ⋙ derivedSectionsPresheaf O ⋙
          DerivedCategory.homologyFunctor (PresheafOfModules.{u} O.obj) m) ⋙
        PresheafOfModules.sheafification (𝟙 O.obj) ≅
      K ⋙ DerivedCategory.homologyFunctor (SheafOfModules.{u} O) m
```

**`Stacks.Cohomology.DerivedLimits.cohomologyDerivedLimitDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimitComparisonDiagram.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimitComparisonDiagram.lean#L198). The attribute's comment: “the cohomology sheaves of the system and of the derived limit are the sheafifications of the cohomology presheaves U ↦ H^m(U, K\_n) and U ↦ H^m(U, R lim K\_n), and the comparison square of the remark's diagram commutes”.

> **Stacks 0BKQ, first assertion and diagram.** Let `O` be a sheaf of rings on a space, let
> `(Kₙ)` be an inverse system in `D(O)` and let `L` be a derived limit of it, given by its
> structural map `p` and the defining distinguished triangle. Fix a degree `m`, and let `e` be the
> Tag 0BKJ identification of the sheafification `S` of the cohomology presheaf `underline 𝓗ᵐ` with
> the cohomology sheaf `𝓗ᵐ`; in particular `e.hom.app (K.obj ⟨n⟩)` says that `𝓗ᵐ_n` is the
> sheafification of `underline 𝓗ᵐ_n`, and `e.hom.app L` says the same for `L`.
>
> Then there are comparison maps `a` into the limit of the cohomology presheaves, `b` into the
> limit of the cohomology sheaves and `c` out of the sheafification of the former, each determined
> by its composites with the limit projections -- `a` and `b` by the maps induced by `p ≫ πₙ`, and
> `c` by the sheafified projections followed by `e` -- and the square
>
> `S a ≫ c = e L ≫ b`
>
> commutes. The map `c` is not asserted to be invertible: the source warns that `lim 𝓗ᵐ_n` need
> not be the sheafification of `lim underline 𝓗ᵐ_n`.

```lean
theorem cohomologyDerivedLimitDiagram {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
    [HasDerivedCategory.{wX} (SheafOfModules.{u} O)]
    [HasDerivedCategory.{wP} (PresheafOfModules.{u} O.obj)]
    (K : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{u} O))
    (L : DerivedCategory (SheafOfModules.{u} O))
    [HasProduct fun n : ℕ ↦ K.obj ⟨n⟩]
    (p : L ⟶ ∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩)
    (hp : ∃ δ : (∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
      Triangle.mk p (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) (n + 1) ≫
            K.map (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory (SheafOfModules.{u} O)))
    (m : ℤ) :
    let P := derivedSectionsPresheaf O ⋙
      DerivedCategory.homologyFunctor (PresheafOfModules.{u} O.obj) m
    let H := DerivedCategory.homologyFunctor (SheafOfModules.{u} O) m
    let S := PresheafOfModules.sheafification (𝟙 O.obj)
    let e := sheafificationCohomologyPresheafIso O m
    ∃ (a : P.obj L ⟶ limit (K ⋙ P))
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
      (S.map a ≫ c = e.hom.app L ≫ b)
```

**`Stacks.Cohomology.DerivedLimits.exists_shortExact_limOne_cohomology_derivedLimit_family`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimits.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimits.lean#L389). The attribute's comment: “the short exact sequences of Equation 0BKR over each open U: 0 → R¹ lim H^(m-1)(U, K\_n) → H^m(U, R lim K\_n) → lim H^m(U, K\_n) → 0”.

> **Stacks 0BKQ.** For a family of derived-sections functors indexed by the opens of a
> ringed space, the cohomology of a derived inverse limit lies in the Milnor short exact
> sequence over each open.
>
> The last map is pinned down by its composites with the limit projections; they are the maps
> on cohomology induced by the structural maps `L ⟶ Kₙ`.
>
> This is the last assertion of the remark. Its first assertion, that the cohomology sheaves of
> the system and of the derived limit are the sheafifications of the cohomology presheaves, and
> the square of its diagram, are
> `Stacks.Cohomology.DerivedLimits.sheafificationCohomologyPresheafSystemIso` and
> `Stacks.Cohomology.DerivedLimits.cohomologyDerivedLimitDiagram`.

```lean
theorem exists_shortExact_limOne_cohomology_derivedLimit_family
    (X : RingedSpace.{u, u})
    (K : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (L : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    [HasProduct fun n : ℕ => K.obj ⟨n⟩]
    (p : L ⟶ ∏ᶜ fun n : ℕ => K.obj ⟨n⟩)
    (hL : ∃ δ : (∏ᶜ fun n : ℕ => K.obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
      Triangle.mk p (Pi.lift fun n : ℕ =>
        Pi.π (fun n : ℕ => K.obj ⟨n⟩) n -
          Pi.π (fun n : ℕ => K.obj ⟨n⟩) (n + 1) ≫
            K.map (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory (SheafOfModules.{u} (structureSheafRing X))))
    (RGamma : ∀ _U : Opens X.carrier,
      DerivedCategory (SheafOfModules.{u} (structureSheafRing X)) ⥤
        DerivedCategory AddCommGrpCat.{u})
    (comparison : ∀ U : Opens X.carrier,
      ((SheafOfModules.toSheaf (structureSheafRing X) ⋙
          (sheafSections (Opens.grothendieckTopology X.carrier) AddCommGrpCat.{u}).obj
            (op U)).mapHomologicalComplex (ComplexShape.up ℤ) ⋙
        DerivedCategory.Q) ⟶ DerivedCategory.Q ⋙ RGamma U)
    (hRGamma : ∀ U : Opens X.carrier,
      (RGamma U).IsRightDerivedFunctor (comparison U)
        (HomologicalComplex.quasiIso
          (SheafOfModules.{u} (structureSheafRing X))
          (ComplexShape.up ℤ)))
    (U : Opens X.carrier) (m : ℤ) :
    let Fprev := K ⋙ RGamma U ⋙
      DerivedCategory.homologyFunctor AddCommGrpCat.{u} (m - 1)
    let Fcur := K ⋙ RGamma U ⋙
      DerivedCategory.homologyFunctor AddCommGrpCat.{u} m
    let dprev := Pi.lift fun n : ℕ =>
      Pi.π (fun n : ℕ => Fprev.obj ⟨n⟩) n -
        Pi.π (fun n : ℕ => Fprev.obj ⟨n⟩) (n + 1) ≫
          Fprev.map (homOfLE (Nat.le_succ n)).op
    ∃ (i : cokernel dprev ⟶
        (DerivedCategory.homologyFunctor AddCommGrpCat.{u} m).obj ((RGamma U).obj L))
      (q : (DerivedCategory.homologyFunctor AddCommGrpCat.{u} m).obj ((RGamma U).obj L) ⟶
        limit Fcur)
      (zero : i ≫ q = 0),
      ((ShortComplex.mk i q zero).ShortExact ∧
        ∀ n : ℕ, q ≫ limit.π Fcur ⟨n⟩ =
          (DerivedCategory.homologyFunctor AddCommGrpCat.{u} m).map
            ((RGamma U).map (p ≫ Pi.π (fun n : ℕ => K.obj ⟨n⟩) n)))
```

## Tag 0BKS, a lemma

[Tag 0BKS](https://stacks.math.columbia.edu/tag/0BKS) in the Stacks Project.

**`Stacks.Cohomology.SpaceInverseLimits.isDerivedLimit_single_limit_of_isBasis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/RecoveryB/InverseLimitAsDerivedLimit.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/RecoveryB/InverseLimitAsDerivedLimit.lean#L354). The attribute's comment: “derived limit”.

> If the terms of a countable inverse system of modules are acyclic on a basis and `R¹ lim`
> of their sections vanishes there, then the ordinary limit, placed in degree zero, is a derived
> inverse limit of the system.

```lean
public theorem isDerivedLimit_single_limit_of_isBasis (X : RingedSpace.{u, u})
    (F : Functor ℕᵒᵖ (SheafOfModules.{u} (structureSheafRing X)))
    (B : Set (Opens X.carrier)) (hB : Opens.IsBasis B)
    (hcoh : ∀ U ∈ B, ∀ n p : ℕ, 0 < p →
      IsZero (Hgroup (structureSheafRing X) U p (F.obj ⟨n⟩)))
    (hlimOne : ∀ U ∈ B, Epi (inverseLimitDifference (sectionsSystem X F U))) :
    ∃ h : HasProduct (fun n : ℕ =>
        (F ⋙ DerivedCategory.singleFunctor (SheafOfModules.{u} (structureSheafRing X)) 0).obj ⟨n⟩),
      @IsDerivedLimit (DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) _ _ _ _ _ _
        (F ⋙ DerivedCategory.singleFunctor (SheafOfModules.{u} (structureSheafRing X)) 0) h
        ((DerivedCategory.singleFunctor (SheafOfModules.{u} (structureSheafRing X)) 0).obj
          (limit F))
```

**`Stacks.Cohomology.SpaceInverseLimits.isZero_cohomology_limit_of_isBasis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/RecoveryB/InverseLimitAsDerivedLimit.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/RecoveryB/InverseLimitAsDerivedLimit.lean#L419). The attribute's comment: “higher cohomology”.

> Under the same hypotheses, the ordinary inverse limit has vanishing positive-degree
> cohomology on every member of the basis.

```lean
public theorem isZero_cohomology_limit_of_isBasis (X : RingedSpace.{u, u})
    (F : Functor ℕᵒᵖ (SheafOfModules.{u} (structureSheafRing X)))
    (B : Set (Opens X.carrier)) (hB : Opens.IsBasis B)
    (hcoh : ∀ U ∈ B, ∀ n p : ℕ, 0 < p →
      IsZero (Hgroup (structureSheafRing X) U p (F.obj ⟨n⟩)))
    (hlimOne : ∀ U ∈ B, Epi (inverseLimitDifference (sectionsSystem X F U)))
    (U : Opens X.carrier) (hU : U ∈ B) (p : ℕ) (hp : 0 < p) :
    IsZero (Hgroup (structureSheafRing X) U p (limit F))
```

## Tag 0D61, a lemma

[Tag 0D61](https://stacks.math.columbia.edu/tag/0D61) in the Stacks Project.

**`Stacks.Cohomology.DerivedLimitStalk.cohomology_derivedLimit_projection_mono_on_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimitStalkInjectivity.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimitStalkInjectivity.lean#L233).

> **Stacks Project, Tag 0D61.** A locally vanishing `R¹ lim` in degree `m - 1` and eventual
> injectivity on cohomology in degree `m`, over a fundamental system of open neighbourhoods of `x`,
> force the projection from a derived limit to the stage `n₀` to be injective on the stalk at `x`
> of the degree-`m` cohomology sheaf.
>
> Both numbered conditions of the source appear as binders, in the source's own position —
> universally quantified over the members `U` of the fundamental system `𝔘`: `hlimOne` is
> `R¹ lim Hᵐ⁻¹(U, Kₙ) = 0`, as the vanishing of the cokernel of the `1 - shift` endomorphism of the
> product, and `hinj` is the injectivity of `Hᵐ(U, Kₙ) ⟶ Hᵐ(U, K_{n₀})` for `n ≥ n₀`. The source's
> `n(x)` is `n₀` and its `𝔘ₓ` is `𝔘`, given here as arguments rather than existentially; the derived
> limit `R lim Kₙ` is `L` together with `p` and `hL`, which say that `p` is the structural map of
> the defining distinguished triangle, so `p ≫ Pi.π n₀` is the source's `R lim Kₙ ⟶ K_{n₀}` and not
> an arbitrary map.

```lean
public theorem cohomology_derivedLimit_projection_mono_on_stalk {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
    [HasDerivedCategory.{wX} (SheafOfModules.{u} O)]
    [HasDerivedCategory.{wP} (PresheafOfModules.{u} O.obj)]
    (K : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{u} O))
    (L : DerivedCategory (SheafOfModules.{u} O))
    (p : L ⟶ ∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩)
    (hL : ∃ δ : (∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
      Triangle.mk p (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) (n + 1) ≫
            K.map (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory (SheafOfModules.{u} O)))
    (x : X) (m : ℤ) (n₀ : ℕ) (𝔘 : Set (Opens X))
    (hbasis : (nhds x).HasBasis (fun U : Opens X ↦ U ∈ 𝔘) (fun U ↦ (U : Set X)))
    (hlimOne : ∀ U ∈ 𝔘,
      let F := K ⋙ derivedSectionsPresheaf O ⋙
        DerivedCategory.homologyFunctor (PresheafOfModules.{u} O.obj) (m - 1) ⋙
        PresheafOfModules.evaluation O.obj (Opposite.op U)
      IsZero (cokernel (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦ F.obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦ F.obj ⟨n⟩) (n + 1) ≫
            F.map (homOfLE (Nat.le_succ n)).op)))
    (hinj : ∀ U ∈ 𝔘,
      let F := K ⋙ derivedSectionsPresheaf O ⋙
        DerivedCategory.homologyFunctor (PresheafOfModules.{u} O.obj) m ⋙
        PresheafOfModules.evaluation O.obj (Opposite.op U)
      ∀ (n : ℕ) (hn : n₀ ≤ n), Mono (F.map (homOfLE hn).op)) :
    Mono ((TopCat.Presheaf.stalkFunctor AddCommGrpCat.{u} x).map
      ((SheafOfModules.forget O ⋙ PresheafOfModules.toPresheaf O.obj).map
        ((DerivedCategory.homologyFunctor (SheafOfModules.{u} O) m).map
          (p ≫ Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n₀))))
```

## Tag 0D62, a lemma

[Tag 0D62](https://stacks.math.columbia.edu/tag/0D62) in the Stacks Project.

**`Stacks.Cohomology.DerivedLimitStalk.exists_and_forall_isIso_to_derivedLimit_truncGETower_of_local_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimitStalkInjectivity.lean, line 685](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimitStalkInjectivity.lean#L685). The attribute's comment: “the derived limit and the canonical map of Remark 0H72 exist, and every such canonical map is an isomorphism”.

> **Stacks Project, Tag 0D62.** Let `E` be an object of the derived category of sheaves of
> `𝒪_X`-modules on a ringed space, and suppose every point `x` carries a function `p(x, -)` and a
> fundamental system `𝔘ₓ` of open neighbourhoods on whose members `Hᵖ(U, H^{m-p}(E))` vanishes
> whenever `p > p(x, m)`. Then the tower of truncations `τ_{≥ -n} E` from below has a derived
> limit `R lim τ_{≥ -n} E` with a canonical map of Remark 0H72 from `E`, and every such canonical
> map to every derived limit of the tower is an isomorphism.

```lean
public theorem exists_and_forall_isIso_to_derivedLimit_truncGETower_of_local_vanishing
    {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
    [HasDerivedCategory.{wX} (SheafOfModules.{u} O)]
    [HasDerivedCategory.{wP} (PresheafOfModules.{u} O.obj)]
    (E : DerivedCategory (SheafOfModules.{u} O))
    (hvanishing : ∀ x : X, ∃ (pb : ℤ → ℤ) (𝔘 : Set (Opens X)),
      (nhds x).HasBasis (fun U : Opens X ↦ U ∈ 𝔘) (fun U ↦ (U : Set X)) ∧
        ∀ U ∈ 𝔘, ∀ (p : ℕ) (m : ℤ), pb m < (p : ℤ) →
          IsZero ((PresheafOfModules.evaluation O.obj (Opposite.op U)).obj
            (cohomologyPresheaf O
              ((DerivedCategory.singleFunctor (SheafOfModules.{u} O) 0).obj
                ((DerivedCategory.homologyFunctor (SheafOfModules.{u} O)
                  (m - (p : ℤ))).obj E)) (p : ℤ)))) :
    (∃ (_ : HasProduct fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩)
      (L : DerivedCategory (SheafOfModules.{u} O)) (c : E ⟶ L)
      (pr : L ⟶ ∏ᶜ fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩),
      (∃ δ : (∏ᶜ fun n : ℕ ↦
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
        Triangle.mk pr (Pi.lift fun n : ℕ ↦
          Pi.π (fun n : ℕ ↦
            (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) n -
            Pi.π (fun n : ℕ ↦
              (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) (n + 1) ≫
              (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).map
                (homOfLE (Nat.le_succ n)).op) δ ∈
          distTriang (DerivedCategory (SheafOfModules.{u} O))) ∧
      (∀ n : ℕ, c ≫ pr ≫ Pi.π
        (fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) n =
        (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app E)) ∧
    ∀ (L : DerivedCategory (SheafOfModules.{u} O)) (c : E ⟶ L)
      (pr : L ⟶ ∏ᶜ fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩),
      (∃ δ : (∏ᶜ fun n : ℕ ↦
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
        Triangle.mk pr (Pi.lift fun n : ℕ ↦
          Pi.π (fun n : ℕ ↦
            (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) n -
            Pi.π (fun n : ℕ ↦
              (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) (n + 1) ≫
              (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).map
                (homOfLE (Nat.le_succ n)).op) δ ∈
          distTriang (DerivedCategory (SheafOfModules.{u} O))) →
      (∀ n : ℕ, c ≫ pr ≫ Pi.π
        (fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) n =
        (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app E) →
      IsIso c
```

## Tag 0D63, a lemma

[Tag 0D63](https://stacks.math.columbia.edu/tag/0D63) in the Stacks Project.

**`Stacks.Cohomology.DerivedLimitStalk.isIso_to_isDerivedLimit_truncGETower_of_local_bound`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimitLocalBound.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimitLocalBound.lean#L76).

> Let `E` be an object of the derived category of sheaves of `𝒪_X`-modules on a ringed space, and
> suppose every point `x` carries an integer `dₓ ≥ 0` and a fundamental system `𝔘ₓ` of open
> neighbourhoods on whose members `Hᵖ(U, Hᵠ(E))` vanishes whenever `p > dₓ` and `q < 0`. Then the
> canonical map from `E` to a derived limit of its tower of truncations `τ_{≥ -n} E` from below is an
> isomorphism.

```lean
public theorem isIso_to_isDerivedLimit_truncGETower_of_local_bound {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
    [HasDerivedCategory.{wX} (SheafOfModules.{u} O)]
    [HasDerivedCategory.{wP} (PresheafOfModules.{u} O.obj)]
    (E : DerivedCategory (SheafOfModules.{u} O))
    (hvanishing : ∀ x : X, ∃ (d : ℕ) (𝔘 : Set (Opens X)),
      (nhds x).HasBasis (fun U : Opens X ↦ U ∈ 𝔘) (fun U ↦ (U : Set X)) ∧
        ∀ U ∈ 𝔘, ∀ (p : ℕ) (q : ℤ), (d : ℤ) < (p : ℤ) → q < 0 →
          IsZero ((PresheafOfModules.evaluation O.obj (Opposite.op U)).obj
            (cohomologyPresheaf O
              ((DerivedCategory.singleFunctor (SheafOfModules.{u} O) 0).obj
                ((DerivedCategory.homologyFunctor (SheafOfModules.{u} O) q).obj E))
              (p : ℤ))))
    (L : DerivedCategory (SheafOfModules.{u} O)) (c : E ⟶ L)
    (pr : L ⟶ ∏ᶜ fun n : ℕ ↦
      (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩)
    (hL : ∃ δ : (∏ᶜ fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
      Triangle.mk pr (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦
            (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) (n + 1) ≫
            (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).map
              (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory (SheafOfModules.{u} O)))
    (hc : ∀ n : ℕ, c ≫ pr ≫ Pi.π
      (fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) n =
      (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app E) :
    IsIso c
```

## Tag 08U2, a lemma

[Tag 08U2](https://stacks.math.columbia.edu/tag/08U2) in the Stacks Project.

**`Stacks.Cohomology.DerivedLimitStalk.exists_isIso_to_derivedLimit_truncGETower_of_vanishing_on_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimitStalkInjectivity.lean, line 642](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimitStalkInjectivity.lean#L642). The attribute's comment: “the conclusion with the derived limit and the canonical map of Remark 0H72 constructed rather than quantified over”.

> **Stacks Project, Tag 08U2**, in the form the source states it: the canonical map
> `E ⟶ R lim τ_{≥ -n} E` *is* an isomorphism. The derived limit and the canonical map are
> constructed by `exists_presented_derivedLimit_truncGETower`.

```lean
theorem exists_isIso_to_derivedLimit_truncGETower_of_vanishing_on_cover {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
    [HasDerivedCategory.{wX} (SheafOfModules.{u} O)]
    [HasDerivedCategory.{wP} (PresheafOfModules.{u} O.obj)]
    (E : DerivedCategory (SheafOfModules.{u} O))
    (pb : ℤ → ℤ) (𝔅 : Set (Opens X))
    (hcov : ∀ V : Opens X, ∃ 𝒰 : Set (Opens X), 𝒰 ⊆ 𝔅 ∧ (V : Set X) = ⋃ U ∈ 𝒰, (U : Set X))
    (hvanishing : ∀ U ∈ 𝔅, ∀ (p : ℕ) (m : ℤ), pb m < (p : ℤ) →
      IsZero ((PresheafOfModules.evaluation O.obj (Opposite.op U)).obj
        (cohomologyPresheaf O
          ((DerivedCategory.singleFunctor (SheafOfModules.{u} O) 0).obj
            ((DerivedCategory.homologyFunctor (SheafOfModules.{u} O)
              (m - (p : ℤ))).obj E)) (p : ℤ)))) :
    ∃ (_ : HasProduct fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩)
      (L : DerivedCategory (SheafOfModules.{u} O)) (c : E ⟶ L)
      (pr : L ⟶ ∏ᶜ fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩),
      (∃ δ : (∏ᶜ fun n : ℕ ↦
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
        Triangle.mk pr (Pi.lift fun n : ℕ ↦
          Pi.π (fun n : ℕ ↦
            (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) n -
            Pi.π (fun n : ℕ ↦
              (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) (n + 1) ≫
              (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).map
                (homOfLE (Nat.le_succ n)).op) δ ∈
          distTriang (DerivedCategory (SheafOfModules.{u} O))) ∧
      (∀ n : ℕ, c ≫ pr ≫ Pi.π
        (fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) n =
        (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app E) ∧ IsIso c
```

**`Stacks.Cohomology.DerivedLimitStalk.exists_and_forall_isIso_to_derivedLimit_truncGETower_of_vanishing_on_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimitStalkInjectivity.lean, line 745](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimitStalkInjectivity.lean#L745). The attribute's comment: “the derived limit and the canonical map of Remark 0H72 exist, and every such canonical map is an isomorphism”.

> **Stacks Project, Tag 08U2.** Let `E` be an object of the derived category of sheaves of
> `𝒪_X`-modules on a ringed space, let `p(-)` be a function and let `𝔅` be a set of opens of `X`
> such that every open of `X` is a union of members of `𝔅` and `Hᵖ(U, H^{m-p}(E))` vanishes for
> `U ∈ 𝔅` and `p > p(m)`. Then the tower of truncations `τ_{≥ -n} E` from below has a derived
> limit `R lim τ_{≥ -n} E` with a canonical map of Remark 0H72 from `E`, and every such canonical
> map to every derived limit of the tower is an isomorphism.

```lean
public theorem exists_and_forall_isIso_to_derivedLimit_truncGETower_of_vanishing_on_cover
    {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
    [HasDerivedCategory.{wX} (SheafOfModules.{u} O)]
    [HasDerivedCategory.{wP} (PresheafOfModules.{u} O.obj)]
    (E : DerivedCategory (SheafOfModules.{u} O))
    (pb : ℤ → ℤ) (𝔅 : Set (Opens X))
    (hcov : ∀ V : Opens X, ∃ 𝒰 : Set (Opens X), 𝒰 ⊆ 𝔅 ∧ (V : Set X) = ⋃ U ∈ 𝒰, (U : Set X))
    (hvanishing : ∀ U ∈ 𝔅, ∀ (p : ℕ) (m : ℤ), pb m < (p : ℤ) →
      IsZero ((PresheafOfModules.evaluation O.obj (Opposite.op U)).obj
        (cohomologyPresheaf O
          ((DerivedCategory.singleFunctor (SheafOfModules.{u} O) 0).obj
            ((DerivedCategory.homologyFunctor (SheafOfModules.{u} O)
              (m - (p : ℤ))).obj E)) (p : ℤ)))) :
    (∃ (_ : HasProduct fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩)
      (L : DerivedCategory (SheafOfModules.{u} O)) (c : E ⟶ L)
      (pr : L ⟶ ∏ᶜ fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩),
      (∃ δ : (∏ᶜ fun n : ℕ ↦
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
        Triangle.mk pr (Pi.lift fun n : ℕ ↦
          Pi.π (fun n : ℕ ↦
            (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) n -
            Pi.π (fun n : ℕ ↦
              (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) (n + 1) ≫
              (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).map
                (homOfLE (Nat.le_succ n)).op) δ ∈
          distTriang (DerivedCategory (SheafOfModules.{u} O))) ∧
      (∀ n : ℕ, c ≫ pr ≫ Pi.π
        (fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) n =
        (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app E)) ∧
    ∀ (L : DerivedCategory (SheafOfModules.{u} O)) (c : E ⟶ L)
      (pr : L ⟶ ∏ᶜ fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩),
      (∃ δ : (∏ᶜ fun n : ℕ ↦
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
        Triangle.mk pr (Pi.lift fun n : ℕ ↦
          Pi.π (fun n : ℕ ↦
            (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) n -
            Pi.π (fun n : ℕ ↦
              (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) (n + 1) ≫
              (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).map
                (homOfLE (Nat.le_succ n)).op) δ ∈
          distTriang (DerivedCategory (SheafOfModules.{u} O))) →
      (∀ n : ℕ, c ≫ pr ≫ Pi.π
        (fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) n =
        (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app E) →
      IsIso c
```

## Tag 0D64, a lemma

[Tag 0D64](https://stacks.math.columbia.edu/tag/0D64) in the Stacks Project.

**`Stacks.Cohomology.DerivedLimitStalk.exists_and_forall_isIso_to_derivedLimit_truncGETower_of_dimension_bound`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimitDimensionBound.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/DerivedLimitDimensionBound.lean#L99). The attribute's comment: “the derived limit and the canonical map of Remark 0H72 exist, and every such canonical map is an isomorphism”.

> **Stacks Project, Tag 0D64.** Let `E` be an object of the derived category of sheaves of
> `𝒪_X`-modules on a ringed space, and suppose there are an integer `d ≥ 0` and a basis `𝔅` for the
> topology of `X` on whose members `Hᵖ(U, Hᵠ(E))` vanishes whenever `p > d` and `q < 0`. Then the
> tower of truncations `τ_{≥ -n} E` from below has a derived limit `R lim τ_{≥ -n} E` with a
> canonical map of Remark 0H72 from `E`, and every such canonical map to every derived limit of the
> tower is an isomorphism.

```lean
public theorem exists_and_forall_isIso_to_derivedLimit_truncGETower_of_dimension_bound
    {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
    [HasDerivedCategory.{wX} (SheafOfModules.{u} O)]
    [HasDerivedCategory.{wP} (PresheafOfModules.{u} O.obj)]
    (E : DerivedCategory (SheafOfModules.{u} O))
    (d : ℕ) (𝔅 : Set (Opens X)) (h𝔅 : Opens.IsBasis 𝔅)
    (hvanishing : ∀ U ∈ 𝔅, ∀ (p : ℕ) (q : ℤ), (d : ℤ) < (p : ℤ) → q < 0 →
      IsZero ((PresheafOfModules.evaluation O.obj (Opposite.op U)).obj
        (cohomologyPresheaf O
          ((DerivedCategory.singleFunctor (SheafOfModules.{u} O) 0).obj
            ((DerivedCategory.homologyFunctor (SheafOfModules.{u} O) q).obj E))
          (p : ℤ)))) :
    (∃ (_ : HasProduct fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩)
      (L : DerivedCategory (SheafOfModules.{u} O)) (c : E ⟶ L)
      (pr : L ⟶ ∏ᶜ fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩),
      (∃ δ : (∏ᶜ fun n : ℕ ↦
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
        Triangle.mk pr (Pi.lift fun n : ℕ ↦
          Pi.π (fun n : ℕ ↦
            (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) n -
            Pi.π (fun n : ℕ ↦
              (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) (n + 1) ≫
              (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).map
                (homOfLE (Nat.le_succ n)).op) δ ∈
          distTriang (DerivedCategory (SheafOfModules.{u} O))) ∧
      (∀ n : ℕ, c ≫ pr ≫ Pi.π
        (fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) n =
        (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app E)) ∧
    ∀ (L : DerivedCategory (SheafOfModules.{u} O)) (c : E ⟶ L)
      (pr : L ⟶ ∏ᶜ fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩),
      (∃ δ : (∏ᶜ fun n : ℕ ↦
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
        Triangle.mk pr (Pi.lift fun n : ℕ ↦
          Pi.π (fun n : ℕ ↦
            (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) n -
            Pi.π (fun n : ℕ ↦
              (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) (n + 1) ≫
              (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).map
                (homOfLE (Nat.le_succ n)).op) δ ∈
          distTriang (DerivedCategory (SheafOfModules.{u} O))) →
      (∀ n : ℕ, c ≫ pr ≫ Pi.π
        (fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} O) E).obj ⟨n⟩) n =
        (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app E) →
      IsIso c
```

## Tag 0BKT, a lemma

[Tag 0BKT](https://stacks.math.columbia.edu/tag/0BKT) in the Stacks Project.

**`Stacks.Algebraization.homologyIso_derivedSections_of_isAffineOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/AffineEdgeQuasicoherent.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/AffineEdgeQuasicoherent.lean#L77). The attribute's comment: “over an affine open of a scheme, for an object of `D(𝒪_X)` whose cohomology sheaves are all quasi-coherent: the acyclicity hypothesis of the tag is Serre vanishing on the affine opens, which quasi-coherence supplies, and the affine opens are a basis of the topology”. References: EGA III (1.3.1), “more general”; EGA III (4.1.7.21), “H^i(U”.

> **[Stacks, Tag 0BKT] over an affine open of a scheme.** For an object `L` of `D(𝒪_X)` with
> quasi-coherent cohomology sheaves and an affine open `U`, the hypercohomology `H^p(U, L)` is the
> module of sections over `U` of the cohomology sheaf `H^p(L)`.
>
> The cohomology sheaves are acyclic over the affine opens by Serre vanishing
> (`Stacks.Algebraization.isZero_rightDerived_evaluation_homology_of_isQuasicoherent`), and the
> affine opens are a basis, so
> `Stacks.Cohomology.AcyclicOpen.hypercohomologyIso` applies.

```lean
public def homologyIso_derivedSections_of_isAffineOpen (X : Scheme.{u})
    (L : DerivedCategory X.Modules)
    (hqc : ∀ q : ℤ, ((DerivedCategory.homologyFunctor X.Modules q).obj L).IsQuasicoherent)
    (U : X.affineOpens) (p : ℤ) :
    (DerivedCategory.homologyFunctor (ModuleCat.{u} Γ(X, U.1)) p).obj
        ((derivedSections (structureSheafRing X.toRingedSpace) U.1).obj L) ≅
      ModuleCat.of Γ(X, U.1) Γ((DerivedCategory.homologyFunctor X.Modules p).obj L, U.1)
```

**`Stacks.Cohomology.AcyclicOpen.isIso_hypercohomologyEdge_app_of_isBasis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/HypercohomologyOverAcyclicOpens.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/HypercohomologyOverAcyclicOpens.lean#L83).

> **Stacks Project Tag 0BKT.** If every cohomology sheaf of `K` has vanishing higher cohomology
> over the members of a basis of opens, then over each member of that basis the hypercohomology
> edge morphism `H^q(U, K) ⟶ Γ(U, H^q(K))` is invertible, in every degree.

```lean
theorem isIso_hypercohomologyEdge_app_of_isBasis
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (B : Set (Opens X.carrier)) (hB : Opens.IsBasis B)
    (hK : ∀ V ∈ B, ∀ p : ℕ, 0 < p → ∀ q : ℤ,
      IsZero (((SheafOfModules.evaluation (structureSheafRing X) (op V)).rightDerived p).obj
        ((DerivedCategory.homologyFunctor (SheafOfModules.{u} (structureSheafRing X)) q).obj K)))
    (U : Opens X.carrier) (hU : U ∈ B) (q : ℤ) :
    IsIso ((hypercohomologyEdge (structureSheafRing X) U q).app K)
```

## Tag 0BKU, a lemma

[Tag 0BKU](https://stacks.math.columbia.edu/tag/0BKU) in the Stacks Project.

**`Stacks.Cohomology.DerivedLimits.cohomology_isLimit_of_isDerivedLimit_of_isBasis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/CohomologyOfADerivedLimit.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietorisAndLimits/CohomologyOfADerivedLimit.lean#L75).

> **Stacks Project, Tag 0BKU.** Let `(K_n)` be an inverse system of objects of `D(𝒪_X)` and let
> `L` be a derived limit of it, exhibited by the structural map `p` and its distinguished triangle.
> If on a basis `B` of the topology the cohomology sheaves of the `K_n` are acyclic and the inverse
> systems of their sections have vanishing `R¹ lim`, then for every `q` the degree-`q` cohomology
> sheaf of `L` is the inverse limit of the degree-`q` cohomology sheaves of the `K_n`, through the
> maps induced by `p`.

```lean
theorem cohomology_isLimit_of_isDerivedLimit_of_isBasis
    (K : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (L : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    [hprod : HasProduct fun n : ℕ ↦ K.obj ⟨n⟩]
    (p : L ⟶ ∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩)
    (hL : ∃ δ : (∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
      Triangle.mk p (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) (n + 1) ≫
            K.map (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory (SheafOfModules.{u} (structureSheafRing X))))
    (B : Set (Opens X.carrier)) (hB : Opens.IsBasis B)
    (hacyclic : ∀ U ∈ B, ∀ q : ℤ, ∀ n : ℕ, ∀ r : ℕ, 0 < r →
      IsZero (((SheafOfModules.evaluation (structureSheafRing X) (op U)).rightDerived r).obj
        ((DerivedCategory.homologyFunctor (SheafOfModules.{u} (structureSheafRing X)) q).obj
          (K.obj ⟨n⟩))))
    (hlimOne : ∀ U ∈ B, ∀ q : ℤ,
      IsZero (Rlim.firstDerivedLimit
        (K ⋙ DerivedCategory.homologyFunctor (SheafOfModules.{u} (structureSheafRing X)) q ⋙
          SheafOfModules.evaluation (structureSheafRing X) (op U) ⋙
            forget₂ (ModuleCat.{u} ((structureSheafRing X).obj.obj (op U))) AddCommGrpCat.{u})))
    (q : ℤ) :
    ∃ τ : (Functor.const ℕᵒᵖ).obj
        ((DerivedCategory.homologyFunctor (SheafOfModules.{u} (structureSheafRing X)) q).obj L) ⟶
        K ⋙ DerivedCategory.homologyFunctor (SheafOfModules.{u} (structureSheafRing X)) q,
      (∀ n : ℕ, τ.app ⟨n⟩ =
        (DerivedCategory.homologyFunctor (SheafOfModules.{u} (structureSheafRing X)) q).map
          (p ≫ Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n)) ∧
      Nonempty (IsLimit (Cone.mk _ τ))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.37, Tag 0BKN](https://stacks.math.columbia.edu/tag/0BKN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
