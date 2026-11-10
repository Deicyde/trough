---
declaration: section
origin: cited
lean: Stacks.WeaklyContractible.exact_sheafSections_of_isWeaklyContractible, Stacks.WeaklyContractible.subsingleton_cohomology_of_isWeaklyContractible, Stacks.WeaklyContractible.nonempty_sections_of_isWeaklyContractible_of_isTorsor, Stacks.SheafOfModules.WeaklyContractible.hasExactLimitsOfShape_discrete, Stacks.WeaklyContractible.isZero_homology_of_isDerivedLimit_single, Stacks.WeaklyContractible.nonempty_cokernel_iso_homology_one_of_isDerivedLimit_single, Stacks.WeaklyContractible.isLimit_productFanInDerivedCategory_of_weaklyContractibleObjectsSituation, Stacks.WeaklyContractible.exact_iff_exact_sections_of_weaklyContractibleObjectsSituation
statement: formalized
proof: formalized
---

# 21.51 Weakly contractible objects

Section 21.51 of the Stacks Project, [Tag 0945](https://stacks.math.columbia.edu/tag/0945). 2 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0946, a lemma

[Tag 0946](https://stacks.math.columbia.edu/tag/0946) in the Stacks Project.

**`Stacks.WeaklyContractible.exact_sheafSections_of_isWeaklyContractible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/WeaklyContractible/CohomologyOverAWeaklyContractibleObject.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/WeaklyContractible/CohomologyOverAWeaklyContractibleObject.lean#L108). The attribute's comment: “part (1)”.

> Evaluation of abelian sheaves at a weakly contractible object is exact, with weak
> contractibility tested in the value universe `w`.

```lean
theorem exact_sheafSections_of_isWeaklyContractible
    [HasSheafify J AddCommGrpCat.{w}]
    (U : C)
    (hU : ∀ (F G : Sheaf J (Type w)) (φ : F ⟶ G),
      Sheaf.IsLocallySurjective φ → Function.Surjective (φ.hom.app (op U))) :
    exactFunctor (Sheaf J AddCommGrpCat.{w}) AddCommGrpCat.{w}
      ((sheafSections J AddCommGrpCat.{w}).obj (op U))
```

**`Stacks.WeaklyContractible.subsingleton_cohomology_of_isWeaklyContractible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/WeaklyContractible/CohomologyOverAWeaklyContractibleObject.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/WeaklyContractible/CohomologyOverAWeaklyContractibleObject.lean#L139). The attribute's comment: “part (2)”.

> The positive-degree cohomology of an abelian sheaf over a weakly contractible object
> vanishes.

```lean
theorem subsingleton_cohomology_of_isWeaklyContractible
    [HasSheafify J AddCommGrpCat.{v}]
    [HasExt.{w'} (Sheaf J AddCommGrpCat.{v})]
    (U : C) (hU : J.IsWeaklyContractible U)
    (F : Sheaf J AddCommGrpCat.{v}) (p : ℕ) (hp : 1 ≤ p) :
    Subsingleton (Sheaf.H'.{w', v} F p U)
```

**`Stacks.WeaklyContractible.nonempty_sections_of_isWeaklyContractible_of_isTorsor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/WeaklyContractible/CohomologyOverAWeaklyContractibleObject.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/WeaklyContractible/CohomologyOverAWeaklyContractibleObject.lean#L153). The attribute's comment: “part (3)”.

> Every torsor has a section over a weakly contractible object.

```lean
theorem nonempty_sections_of_isWeaklyContractible_of_isTorsor
    (U : C) (hU : J.IsWeaklyContractible U)
    (G : SheafOfGroups.{v, v, u} (C := C) J)
    (F : PseudoTorsor (C := C) G) (hF : F.IsTorsor) :
    Nonempty (F.presheaf.obj (op U))
```

## Tag 0947, a proposition

[Tag 0947](https://stacks.math.columbia.edu/tag/0947) in the Stacks Project.

**`Stacks.SheafOfModules.WeaklyContractible.hasExactLimitsOfShape_discrete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/WeaklyContractibleProducts.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/WeaklyContractibleProducts.lean#L214). The attribute's comment: “(4)”.

> **Stacks 0947(4).** On a site every object of which has a covering by weakly contractible
> objects, products of sheaves of modules are exact -- over an *arbitrary* index type `ι`, in an
> arbitrary universe, subject only to the `t`-smallness that makes the product exist at all.

```lean
theorem hasExactLimitsOfShape_discrete (ι : Type u₀) [Small.{t} ι] (B : ObjectProperty C)
    (hB : J.HasEnoughObjects B)
    (hwc : ∀ ⦃U : C⦄, B U → ∀ (F G : Sheaf J (Type t)) (φ : F ⟶ G),
      Sheaf.IsLocallySurjective φ → Function.Surjective (φ.hom.app (op U))) :
    HasExactLimitsOfShape (Discrete ι) (SheafOfModules.{t} R)
```

**`Stacks.WeaklyContractible.isZero_homology_of_isDerivedLimit_single`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WeaklyContractible/DerivedLimitOfModules.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WeaklyContractible/DerivedLimitOfModules.lean#L99). The attribute's comment: “(6), vanishing of the higher derived limits”.

> **Stacks 0947(6).** On a ringed site with a covering collection of weakly contractible
> objects, the derived limit of a countable inverse system `(Fₙ)` of sheaves of modules has no
> cohomology outside degrees `0` and `1`: `Rᵖ lim Fₙ = 0` for every `p ≠ 0, 1`, in particular for
> every `p > 1`.

```lean
theorem isZero_homology_of_isDerivedLimit_single
    (S : WeaklyContractibleObjectsSituation.{w, v, u, t} C J)
    [HasDerivedCategory (SheafOfModules.{t} S.O)]
    (G : ℕᵒᵖ ⥤ SheafOfModules.{t} S.O)
    (L : DerivedCategory (SheafOfModules.{t} S.O))
    (hL : IsDerivedLimit (G ⋙ DerivedCategory.singleFunctor (SheafOfModules.{t} S.O) 0) L)
    (p : ℤ) (hp₀ : p ≠ 0) (hp₁ : p ≠ 1) :
    IsZero ((DerivedCategory.homologyFunctor (SheafOfModules.{t} S.O) p).obj L)
```

**`Stacks.WeaklyContractible.nonempty_cokernel_iso_homology_one_of_isDerivedLimit_single`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WeaklyContractible/DerivedLimitOfModules.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WeaklyContractible/DerivedLimitOfModules.lean#L119). The attribute's comment: “(6), R¹lim as a cokernel”.

> **Stacks 0947(6).** On a ringed site with a covering collection of weakly contractible
> objects, the first derived limit of a countable inverse system `(Fₙ)` of sheaves of modules is
> the cokernel of the difference map `(xₙ) ↦ (xₙ - fₙ₊₁(xₙ₊₁))` on the product `∏ₙ Fₙ`.

```lean
theorem nonempty_cokernel_iso_homology_one_of_isDerivedLimit_single
    (S : WeaklyContractibleObjectsSituation.{w, v, u, t} C J)
    [HasDerivedCategory (SheafOfModules.{t} S.O)]
    (G : ℕᵒᵖ ⥤ SheafOfModules.{t} S.O)
    (L : DerivedCategory (SheafOfModules.{t} S.O))
    (hL : IsDerivedLimit (G ⋙ DerivedCategory.singleFunctor (SheafOfModules.{t} S.O) 0) L) :
    Nonempty (cokernel (Pi.lift fun n : ℕ ↦ Pi.π (fun n : ℕ ↦ G.obj ⟨n⟩) n -
        Pi.π (fun n : ℕ ↦ G.obj ⟨n⟩) (n + 1) ≫ G.map (homOfLE (Nat.le_succ n)).op) ≅
      (DerivedCategory.homologyFunctor (SheafOfModules.{t} S.O) 1).obj L)
```

**`Stacks.WeaklyContractible.isLimit_productFanInDerivedCategory_of_weaklyContractibleObjectsSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WeaklyContractible/DerivedProducts.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WeaklyContractible/DerivedProducts.lean#L68). The attribute's comment: “derived_products_termwise”.

> **Stacks 0947(5).** On a ringed site with a covering collection of weakly contractible
> objects, products in the derived category of sheaves of modules are computed by termwise
> products of representing complexes: for every family `K` of cochain complexes of sheaves of
> modules indexed by an *arbitrary* type `ι`, the fan whose apex is the image of the termwise
> product complex `∏ᶜ K` and whose legs are the images of the projections `Pi.π K i` is a limit
> fan.

```lean
theorem isLimit_productFanInDerivedCategory_of_weaklyContractibleObjectsSituation
    (S : WeaklyContractibleObjectsSituation.{w, v, u, t} C J)
    [HasDerivedCategory (SheafOfModules.{t} S.O)] (ι : Type u₀) [Small.{t} ι]
    (K : ι → CochainComplex (SheafOfModules.{t} S.O) ℤ) :
    Nonempty (IsLimit (Stacks.DerivedProducts.productFanInDerivedCategory K))
```

**`Stacks.WeaklyContractible.exact_iff_exact_sections_of_weaklyContractibleObjectsSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WeaklyContractible/ExactSections.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WeaklyContractible/ExactSections.lean#L98). The attribute's comment: “exact_iff_sections”.

> In a site covered by weakly contractible objects, a complex of sheaves of modules is
> exact if and only if it is exact on sections over every chosen weakly contractible object.

```lean
theorem exact_iff_exact_sections_of_weaklyContractibleObjectsSituation
    [HasSheafify J AddCommGrpCat.{t}]
    [J.WEqualsLocallyBijective AddCommGrpCat.{t}]
    (h : WeaklyContractibleObjectsSituation.{w, v, u, t} C J)
    (S : ShortComplex (SheafOfModules.{t} h.O)) :
    S.Exact ↔ ∀ ⦃U : C⦄, h.B U →
      Function.Exact (S.f.val.app (op U)) (S.g.val.app (op U))
```

**`Stacks.WeaklyContractible.exists_milnor_shortExact_of_weaklyContractibleObjectsSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WeaklyContractible/MilnorSequence.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WeaklyContractible/MilnorSequence.lean#L57). The attribute's comment: “(7)”.

> **Milnor sequences.** On a ringed site with a covering collection of weakly contractible
> objects, an inverse system `K` in the derived category of sheaves of modules and a derived limit
> `L` of it fit, in every degree `r`, into a short exact sequence
>
> `0 ⟶ R¹lim Hʳ⁻¹(Kₙ) ⟶ Hʳ(L) ⟶ lim Hʳ(Kₙ) ⟶ 0`,
>
> where `R¹lim` of an inverse system of sheaves of modules is the cokernel of the difference map
> `1 - shift` on the product of its terms. The first map is induced by the connecting morphism of
> the triangle `L ⟶ ∏ Kₙ ⟶ ∏ Kₙ ⟶ L[1]` through the comparison `Hʳ⁻¹(∏ Kₙ) ≅ ∏ Hʳ⁻¹(Kₙ)`, and the
> second is the map whose components are `Hʳ` of the composites `L ⟶ ∏ Kₙ ⟶ Kₙ`.

```lean
theorem exists_milnor_shortExact_of_weaklyContractibleObjectsSituation
    (S : WeaklyContractibleObjectsSituation.{w, v, u, t} C J)
    [HasDerivedCategory (SheafOfModules.{t} S.O)]
    (F : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{t} S.O))
    (L : DerivedCategory (SheafOfModules.{t} S.O)) (hL : IsDerivedLimit F L) :
    let X : ℕ → DerivedCategory (SheafOfModules.{t} S.O) := fun n ↦ F.obj (Opposite.op n)
    let d : (∏ᶜ X) ⟶ ∏ᶜ X := Pi.lift fun n : ℕ ↦
      Pi.π X n - Pi.π X (n + 1) ≫ F.map (homOfLE (Nat.le_succ n)).op
    ∃ (a : L ⟶ ∏ᶜ X) (b : (∏ᶜ X) ⟶ L⟦(1 : ℤ)⟧),
      let T := Triangle.mk a d b
      T ∈ distTriang (DerivedCategory (SheafOfModules.{t} S.O)) ∧
        ∀ r : ℤ,
          let H := DerivedCategory.homologyFunctor (SheafOfModules.{t} S.O) r
          let H₁ := DerivedCategory.homologyFunctor (SheafOfModules.{t} S.O) (r - 1)
          let homologySystem : ℕᵒᵖ ⥤ SheafOfModules.{t} S.O := F ⋙ H
          let shiftedHomologySystem : ℕᵒᵖ ⥤ SheafOfModules.{t} S.O := F ⋙ H₁
          let P : SheafOfModules.{t} S.O :=
            ∏ᶜ fun n : ℕ ↦ shiftedHomologySystem.obj (Opposite.op n)
          let δ : P ⟶ P := Pi.lift fun n : ℕ ↦
            Pi.π (fun n : ℕ ↦ shiftedHomologySystem.obj (Opposite.op n)) n -
              Pi.π (fun n : ℕ ↦ shiftedHomologySystem.obj (Opposite.op n)) (n + 1) ≫
                shiftedHomologySystem.map (homOfLE (Nat.le_succ n)).op
          ∃ (e : H₁.obj (∏ᶜ X) ≅ P)
            (i : cokernel δ ⟶ H.obj L) (q : H.obj L ⟶ limit homologySystem)
            (w : i ≫ q = 0),
            e.hom = piComparison H₁ X ∧
              cokernel.π δ ≫ i = e.inv ≫
                DerivedCategory.HomologySequence.δ T (r - 1) r ∧
              (∀ n : ℕ, q ≫ limit.π homologySystem (Opposite.op n) =
                H.map a ≫ H.map (Pi.π X n)) ∧
              (ShortComplex.mk i q w).ShortExact
```

**`Stacks.WeaklyContractible.epi_limit_π_zero_of_epi_map_succ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WeaklyContractible/SurjectiveTower.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WeaklyContractible/SurjectiveTower.lean#L85). The attribute's comment: “(3)”.

> **Stacks 0947(3).** On a ringed site with a covering collection of weakly contractible
> objects, let `G` be a countable inverse system of sheaves of modules whose transition maps
> `Gₙ₊₁ ⟶ Gₙ` are all epimorphisms. Then the projection `lim G ⟶ G₀` from the inverse limit onto
> the bottom term of the tower is an epimorphism.

```lean
theorem epi_limit_π_zero_of_epi_map_succ
    (S : WeaklyContractibleObjectsSituation.{w, v, u, t} C J)
    (G : ℕᵒᵖ ⥤ SheafOfModules.{t} S.O)
    (hG : ∀ n : ℕ, Epi (G.map (homOfLE (Nat.le_succ n)).op)) :
    Epi (limit.π G ⟨0⟩)
```

**`Stacks.WeaklyContractible.exists_isDerivedLimit_truncGETower_of_weaklyContractibleObjectsSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WeaklyContractible/TruncationDerivedLimit.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WeaklyContractible/TruncationDerivedLimit.lean#L145). The attribute's comment: “(2)”.

> **Stacks 0947(2).** On a ringed site with a covering collection of weakly contractible
> objects, every object `E` of the unbounded derived category of sheaves of modules *is* a derived
> limit of the tower `n ↦ τ_{≥ -n} E` of its canonical truncations from below:
> `E = R lim τ_{≥ -n} E`. The product of the tower exists because each of its stages is bounded
> below, and is part of the conclusion.

```lean
theorem exists_isDerivedLimit_truncGETower_of_weaklyContractibleObjectsSituation
    [HasSheafify J AddCommGrpCat.{max u v w t}]
    [J.WEqualsLocallyBijective AddCommGrpCat.{max u v w t}]
    (S : WeaklyContractibleObjectsSituation.{w, v, u, max u v w t} C J)
    (E : DerivedCategory (SheafOfModules.{max u v w t} S.O)) :
    ∃ _ : HasProduct fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v w t} S.O) E).obj ⟨n⟩,
      IsDerivedLimit (Stacks.DerivedLimit.truncGETower (SheafOfModules.{max u v w t} S.O) E)
        E
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.51, Tag 0945](https://stacks.math.columbia.edu/tag/0945)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
