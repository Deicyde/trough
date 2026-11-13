---
declaration: section
origin: cited
lean: Stacks.Algebraization.conditions_tfae_of_quasicoherent, Stacks.Algebraization.PrincipalQuotientTowerCompletion.nonempty_iso_derivedSections_limit_quotientTower_derivedCompletion, Stacks.Algebraization.PrincipalQuotientTowerDiagram.exists_formalFunctionsDiagram, Stacks.Algebraization.PrincipalQuotientTowerDiagram.exists_shortExact_topRow, Stacks.Algebraization.PrincipalQuotientTowerDiagram.exists_shortExact_middleRow, Stacks.Algebraization.PrincipalQuotientTowerDiagram.exists_shortExact_leftColumn, Stacks.Algebraization.PrincipalQuotientTowerDiagram.nonempty_iso_firstDerivedLimit_torsion, Stacks.Algebraization.PrincipalQuotientTowerFormalFunctions.nonempty_iso_derivedSections_limit_derivedCompletion
statement: formalized
proof: formalized
---

# 52.3 Formal sections, II

Section 52.3 of the Stacks Project, [Tag 0BLA](https://stacks.math.columbia.edu/tag/0BLA). 2 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EH9, a lemma

[Tag 0EH9](https://stacks.math.columbia.edu/tag/0EH9) in the Stacks Project.

**`Stacks.Algebraization.conditions_tfae_of_quasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicInverseSystem/TorsionFreeRealization.lean, line 518](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AdicInverseSystem/TorsionFreeRealization.lean#L518).

> **Stacks Project, Tag 0EH9.** Let `X` be a scheme, let `f` act by multiplication by a
> global section of `𝒪_X`, and let `… → ℱ₃ → ℱ₂ → ℱ₁` be an inverse system of quasi-coherent
> `𝒪_X`-modules. The following are equivalent:
>
> 1. for all `n ≥ 1` the map `f : ℱ_{n+1} → ℱ_{n+1}` factors through `ℱ_{n+1} → ℱ_n` to give a
>    short exact sequence `0 → ℱ_n → ℱ_{n+1} → ℱ₁ → 0`;
> 2. for all `n ≥ 1` the map `f^n : ℱ_{n+1} → ℱ_{n+1}` factors through `ℱ_{n+1} → ℱ₁` to give a
>    short exact sequence `0 → ℱ₁ → ℱ_{n+1} → ℱ_n → 0`;
> 3. there is an `f`-divisible `𝒪_X`-module `𝒢` with `ℱ_n = 𝒢[f^n]`;
> 4. there is an `f`-torsion-free `𝒪_X`-module `ℱ` with `ℱ_n = ℱ/f^nℱ`.
>
> The equivalence of (1), (2) and (3) holds over an arbitrary sheaf of rings and is Stacks
> 0H39; so does (4) ⇒ (1). The converse (1) ⇒ (4) is
> `Stacks.Algebraization.condition_one_iff_four_of_quasicoherent`, which is where the scheme
> structure and quasi-coherence enter.

```lean
theorem conditions_tfae_of_quasicoherent
    (X : Scheme.{u})
    (f : End (𝟭 (SheafOfModules.{u} X.ringCatSheaf)))
    (obj : ℕ → X.Modules) (map : ∀ n, obj (n + 1) ⟶ obj n)
    (hobj : ∀ n, (obj n).IsQuasicoherent) :
    List.TFAE
      [Condition1 f obj map, Condition2 f obj map, Condition3 f obj map,
        Condition4 f obj map]
```

## Tag 0BLD, a lemma

[Tag 0BLD](https://stacks.math.columbia.edu/tag/0BLD) in the Stacks Project.

**`Stacks.Algebraization.PrincipalQuotientTowerCompletion.nonempty_iso_derivedSections_limit_quotientTower_derivedCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerDerivedCompletion.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerDerivedCompletion.lean#L217). The attribute's comment: “the displayed equality `RΓ(X, lim ℱ/fⁿℱ) = RΓ(X, ℱ)^∧`, with derived f-adic completion presented as in Stacks 0BKG by an arbitrary left adjoint to the inclusion of the derived-complete objects; also derived completeness of `RΓ(X, lim ℱ/fⁿℱ)` and the identification `Hᵖ(X, lim ℱ/fⁿℱ) = Hᵖ(RΓ(X, ℱ)^∧)`. Unconditional. The levelwise identification `RΓ(X, ℱ ⊗_{𝒪_X} (𝒪_X --fⁿ--> 𝒪_X)) ≅ RΓ(X, ℱ) ⊗^L_A (A --fⁿ--> A)` of inverse systems, which the source's proof of Stacks 0H3C asserts with details left out, is proved here as `nonempty_iso_koszulTower_comp_derivedSections`, out of `Stacks.Cohomology.KoszulTowerSections.nonempty_iso_koszulTower_derivedSections`. The middle column of the diagram is carried by `PrincipalQuotientTower.exists_shortExact_homology_derivedSections_limit_quotientTower`; the remaining rows and columns of the diagram are not covered”.

> **Formal sections for a principal ideal: the displayed equality of [Stacks, Tag 0BLD].** Let
> `A` be a ring, `f ∈ A`, let `X` be a scheme over `A` through `ρ : A ⟶ Γ(X, 𝒪_X)` and let `ℱ` be a
> quasi-coherent `𝒪_X`-module whose `f`-power torsion stabilizes. Let `completion` be a left
> adjoint to the inclusion of the objects of `D(A)` that are derived complete for the ideal `(f)`,
> so that `(-)^∧ = completion ⋙ P.ι` is derived `f`-adic completion as in [Stacks, Tag 0BKG].
> Then
>
> `RΓ(X, lim ℱ/f^(n+1)ℱ) ≅ RΓ(X, ℱ)^∧`,
>
> the object `RΓ(X, lim ℱ/f^(n+1)ℱ)` is itself derived complete for `(f)`, and for every `p` its
> `p`-th cohomology module is that of `RΓ(X, ℱ)^∧` — the identification
> `Hᵖ(X, lim ℱ/fⁿℱ) = Hᵖ(RΓ(X, ℱ)^∧)` on which the diagram of the source rests.
>
> The levelwise comparison of the two `f`-power Koszul towers, which the source of
> [Stacks, Tag 0H3C] asserts with details omitted, is
> `nonempty_iso_koszulTower_comp_derivedSections`.

```lean
theorem nonempty_iso_derivedSections_limit_quotientTower_derivedCompletion
    (hℱ : (ℱ : X.Modules).IsQuasicoherent) (hstab : Stabilizes (mulF X ρ f ℱ))
    [HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A))]
    [HasProduct fun n : ℕ ↦ (Csys (mulF X ρ f ℱ)).obj ⟨n⟩]
    [HasProduct fun n : ℕ ↦ (Ksys (mulF X ρ f ℱ)).obj ⟨n⟩]
    [HasProduct fun n : ℕ ↦
      (Ksys (mulF X ρ f ℱ) ⋙ derivedSectionsOver X.toRingedSpace ρ).obj ⟨n⟩] :
    let P : ObjectProperty (DerivedCategory (ModuleCat.{u} A)) :=
      fun L ↦ IsDerivedComplete (Ideal.span {f}) L
    ∀ (completion : DerivedCategory (ModuleCat.{u} A) ⥤ P.FullSubcategory)
      (_ : completion ⊣ P.ι),
      let completed := completion ⋙ P.ι
      let Fhat : DerivedCategory (ModuleCat.{u} A) :=
        (derivedSectionsOver X.toRingedSpace ρ).obj
          ((DerivedCategory.singleFunctor
            (SheafOfModules.{u} (structureSheafRing X.toRingedSpace)) 0).obj
              (limit (quotientTower X ρ f ℱ)))
      Nonempty (Fhat ≅ completed.obj (derivedSectionsModule X ρ ℱ)) ∧
        IsDerivedComplete (Ideal.span {f}) Fhat ∧
        ∀ p : ℤ, Nonempty
          ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) p).obj Fhat ≅
            (DerivedCategory.homologyFunctor (ModuleCat.{u} A) p).obj
              (completed.obj (derivedSectionsModule X ρ ℱ)))
```

**`Stacks.Algebraization.PrincipalQuotientTowerDiagram.exists_formalFunctionsDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerDiagram.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerDiagram.lean#L258). The attribute's comment: “the commutative diagram with exact rows and columns, in full: the top row `0 ⟶ Hᵖ(X, ℱ)^ ⟶ lim Hᵖ(X, ℱ/fⁿℱ) ⟶ T_f(Hᵖ⁺¹(X, ℱ)) ⟶ 0`, the middle row `0 ⟶ H⁰(Hᵖ(X, ℱ)^∧) ⟶ Hᵖ(X, lim ℱ/fⁿℱ) ⟶ T_f(Hᵖ⁺¹(X, ℱ)) ⟶ 0`, the left column `0 ⟶ R¹lim Hᵖ(X, ℱ)[fⁿ] ⟶ H⁰(Hᵖ(X, ℱ)^∧) ⟶ Hᵖ(X, ℱ)^ ⟶ 0`, the middle column `0 ⟶ R¹lim Hᵖ⁻¹(X, ℱ/fⁿℱ) ⟶ Hᵖ(X, lim ℱ/fⁿℱ) ⟶ lim Hᵖ(X, ℱ/fⁿℱ) ⟶ 0`, the bottom isomorphism `R¹lim Hᵖ(X, ℱ)[fⁿ] ≅ R¹lim Hᵖ⁻¹(X, ℱ/fⁿℱ)`, the identity right column, and the commutativity of the three squares”.

> **The commutative diagram of [Stacks, Tag 0BLD].** Let `A` be a ring, `f ∈ A`, let `X` be a
> scheme over `A` through `ρ : A ⟶ Γ(X, 𝒪_X)` and let `ℱ` be a quasi-coherent `𝒪_X`-module whose
> `f`-power torsion stabilizes. Let `completion` be a left adjoint to the inclusion of the objects
> of `D(A)` that are derived complete for `(f)`, so that `(-)^∧ = completion ⋙ P.ι` is derived
> `f`-adic completion as in [Stacks, Tag 0BKG]. Then for every `p` there is a commutative diagram
>
> ```
>                      0                              0
>                      ↑                              ↑
> 0 ⟶  Hᵖ(X, ℱ)^   ⟶  lim Hᵖ(X, ℱ/fⁿℱ)  ⟶  T_f(Hᵖ⁺¹(X, ℱ))  ⟶  0
>                      ↑                              ↑              ‖
> 0 ⟶ H⁰(Hᵖ(X, ℱ)^∧) ⟶ Hᵖ(X, lim ℱ/fⁿℱ) ⟶  T_f(Hᵖ⁺¹(X, ℱ))  ⟶  0
>                      ↑                              ↑
>       R¹lim Hᵖ(X, ℱ)[fⁿ]  ≅  R¹lim Hᵖ⁻¹(X, ℱ/fⁿℱ)
>                      ↑                              ↑
>                      0                              0
> ```
>
> with exact rows and columns, where `Hᵖ(X, ℱ)^ = lim Hᵖ(X, ℱ)/fⁿHᵖ(X, ℱ)` is the ordinary `f`-adic
> completion and `T_f(-)` is the `f`-adic Tate module. The right-hand column is the identity: the
> two projections to `T_f(Hᵖ⁺¹(X, ℱ))` agree after the middle vertical map.
>
> This is the diagram of [Stacks, Tag 0H32] for `K = RΓ(X, ℱ)`, carried to the honest quotients
> `ℱ/fⁿℱ` along the displayed equality `RΓ(X, lim ℱ/fⁿℱ) ≅ RΓ(X, ℱ)^∧` and the two comparisons of
> limits provided by the middle-column theorem.

```lean
theorem exists_formalFunctionsDiagram
    [HasProduct fun n : ℕ ↦ (Csys (mulF X ρ f ℱ)).obj ⟨n⟩]
    [HasProduct fun n : ℕ ↦ (quotientSections X ρ f ℱ).obj ⟨n⟩]
    [HasProduct fun n : ℕ ↦ (Ksys (mulF X ρ f ℱ)).obj ⟨n⟩]
    [HasProduct fun n : ℕ ↦
      (Ksys (mulF X ρ f ℱ) ⋙ derivedSectionsOver X.toRingedSpace ρ).obj ⟨n⟩]
    (p : ℤ) :
    let Hq : ℤ → ModuleCat.{u} A := fun q ↦
      (DerivedCategory.homologyFunctor (ModuleCat.{u} A) q).obj (derivedSectionsModule X ρ ℱ)
    let P : ObjectProperty (DerivedCategory (ModuleCat.{u} A)) :=
      fun L ↦ IsDerivedComplete (Ideal.span {f}) L
    ∀ (completion : DerivedCategory (ModuleCat.{u} A) ⥤ P.FullSubcategory)
      (_ : completion ⊣ P.ι),
      let completed := completion ⋙ P.ι
      let ordinaryCompletion := limit (CompletionSequences.powerQuotientSystem A (Hq p) f)
      let tate := CompletionSequences.adicTateModule A (Hq (p + 1)) f
      let h0Completion := (DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).obj
        (completed.obj ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (Hq p)))
      let torsionR1 := CompletionSequences.firstDerivedLimit A
        (PrincipalTorsionTower.powerTorsionSystem A (Hq p) f)
      let limitQuotientCohomology := limit (quotientCohomology X ρ f ℱ p)
      let previousQuotientR1 := CompletionSequences.firstDerivedLimit A
        (quotientCohomology X ρ f ℱ (p - 1))
      let sectionsCohomology := (DerivedCategory.homologyFunctor (ModuleCat.{u} A) p).obj
        (limitQuotientSections X ρ f ℱ)
      ∃ (topIn : ordinaryCompletion ⟶ limitQuotientCohomology)
        (topOut : limitQuotientCohomology ⟶ tate)
        (htop : topIn ≫ topOut = 0)
        (middleIn : h0Completion ⟶ sectionsCohomology)
        (middleOut : sectionsCohomology ⟶ tate)
        (hmiddle : middleIn ≫ middleOut = 0)
        (leftIn : torsionR1 ⟶ h0Completion) (leftOut : h0Completion ⟶ ordinaryCompletion)
        (hleft : leftIn ≫ leftOut = 0)
        (columnIn : previousQuotientR1 ⟶ sectionsCohomology)
        (columnOut : sectionsCohomology ⟶ limitQuotientCohomology)
        (hcolumn : columnIn ≫ columnOut = 0)
        (bottom : torsionR1 ≅ previousQuotientR1),
        (ShortComplex.mk topIn topOut htop).ShortExact ∧
          (ShortComplex.mk middleIn middleOut hmiddle).ShortExact ∧
          (ShortComplex.mk leftIn leftOut hleft).ShortExact ∧
          (ShortComplex.mk columnIn columnOut hcolumn).ShortExact ∧
          middleIn ≫ columnOut = leftOut ≫ topIn ∧
          middleOut = columnOut ≫ topOut ∧
          bottom.hom ≫ columnIn = leftIn ≫ middleIn
```

**`Stacks.Algebraization.PrincipalQuotientTowerDiagram.exists_shortExact_topRow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerDiagram.lean, line 347](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerDiagram.lean#L347). The attribute's comment: “the top row of the diagram: the short exact sequence `0 ⟶ Hᵖ(X, ℱ)^ ⟶ lim Hᵖ(X, ℱ/fⁿℱ) ⟶ T_f(Hᵖ⁺¹(X, ℱ)) ⟶ 0` relating the ordinary f-adic completion of Hᵖ(X, ℱ) to the inverse limit of the cohomology of the quotients and the f-adic Tate module of Hᵖ⁺¹(X, ℱ). Unconditional: no reflector onto the derived-complete objects is assumed”.

> **The top row of the diagram of [Stacks, Tag 0BLD].** With `A`, `f`, `X` and `ℱ` as in the
> source, for every `p` there is a short exact sequence
>
> `0 ⟶ Hᵖ(X, ℱ)^ ⟶ lim Hᵖ(X, ℱ/fⁿℱ) ⟶ T_f(Hᵖ⁺¹(X, ℱ)) ⟶ 0`,
>
> where `Hᵖ(X, ℱ)^ = lim Hᵖ(X, ℱ)/fⁿHᵖ(X, ℱ)` is the ordinary `f`-adic completion and `T_f(-)` the
> `f`-adic Tate module. No reflector onto the derived-complete objects appears in the statement;
> one is supplied internally.

```lean
theorem exists_shortExact_topRow
    [HasProduct fun n : ℕ ↦ (Csys (mulF X ρ f ℱ)).obj ⟨n⟩]
    [HasProduct fun n : ℕ ↦ (quotientSections X ρ f ℱ).obj ⟨n⟩]
    [HasProduct fun n : ℕ ↦ (Ksys (mulF X ρ f ℱ)).obj ⟨n⟩]
    [HasProduct fun n : ℕ ↦
      (Ksys (mulF X ρ f ℱ) ⋙ derivedSectionsOver X.toRingedSpace ρ).obj ⟨n⟩]
    (p : ℤ) :
    let Hq : ℤ → ModuleCat.{u} A := fun q ↦
      (DerivedCategory.homologyFunctor (ModuleCat.{u} A) q).obj (derivedSectionsModule X ρ ℱ)
    ∃ (topIn : limit (CompletionSequences.powerQuotientSystem A (Hq p) f) ⟶
        limit (quotientCohomology X ρ f ℱ p))
      (topOut : limit (quotientCohomology X ρ f ℱ p) ⟶
        CompletionSequences.adicTateModule A (Hq (p + 1)) f)
      (htop : topIn ≫ topOut = 0),
      (ShortComplex.mk topIn topOut htop).ShortExact
```

**`Stacks.Algebraization.PrincipalQuotientTowerDiagram.exists_shortExact_middleRow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerDiagram.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerDiagram.lean#L380). The attribute's comment: “the middle row of the diagram: the short exact sequence `0 ⟶ H⁰(Hᵖ(X, ℱ)^∧) ⟶ Hᵖ(X, lim ℱ/fⁿℱ) ⟶ T_f(Hᵖ⁺¹(X, ℱ)) ⟶ 0`, with `(-)^∧` the derived f-adic completion presented as in Stacks 0BKG by an arbitrary left adjoint to the inclusion of the derived-complete objects”.

> **The middle row of the diagram of [Stacks, Tag 0BLD].** With `A`, `f`, `X` and `ℱ` as in the
> source and `(-)^∧` derived `f`-adic completion presented by an arbitrary left adjoint to the
> inclusion of the derived-complete objects, for every `p` there is a short exact sequence
>
> `0 ⟶ H⁰(Hᵖ(X, ℱ)^∧) ⟶ Hᵖ(X, lim ℱ/fⁿℱ) ⟶ T_f(Hᵖ⁺¹(X, ℱ)) ⟶ 0`.

```lean
theorem exists_shortExact_middleRow
    [HasProduct fun n : ℕ ↦ (Csys (mulF X ρ f ℱ)).obj ⟨n⟩]
    [HasProduct fun n : ℕ ↦ (quotientSections X ρ f ℱ).obj ⟨n⟩]
    [HasProduct fun n : ℕ ↦ (Ksys (mulF X ρ f ℱ)).obj ⟨n⟩]
    [HasProduct fun n : ℕ ↦
      (Ksys (mulF X ρ f ℱ) ⋙ derivedSectionsOver X.toRingedSpace ρ).obj ⟨n⟩]
    (p : ℤ) :
    let Hq : ℤ → ModuleCat.{u} A := fun q ↦
      (DerivedCategory.homologyFunctor (ModuleCat.{u} A) q).obj (derivedSectionsModule X ρ ℱ)
    let P : ObjectProperty (DerivedCategory (ModuleCat.{u} A)) :=
      fun L ↦ IsDerivedComplete (Ideal.span {f}) L
    ∀ (completion : DerivedCategory (ModuleCat.{u} A) ⥤ P.FullSubcategory)
      (_ : completion ⊣ P.ι),
      ∃ (middleIn : (DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).obj
          ((completion ⋙ P.ι).obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (Hq p))) ⟶
          (DerivedCategory.homologyFunctor (ModuleCat.{u} A) p).obj
            (limitQuotientSections X ρ f ℱ))
        (middleOut : (DerivedCategory.homologyFunctor (ModuleCat.{u} A) p).obj
            (limitQuotientSections X ρ f ℱ) ⟶
          CompletionSequences.adicTateModule A (Hq (p + 1)) f)
        (hmiddle : middleIn ≫ middleOut = 0),
        (ShortComplex.mk middleIn middleOut hmiddle).ShortExact
```

**`Stacks.Algebraization.PrincipalQuotientTowerDiagram.exists_shortExact_leftColumn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerDiagram.lean, line 420](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerDiagram.lean#L420). The attribute's comment: “the left column of the diagram: the short exact sequence `0 ⟶ R¹lim Hᵖ(X, ℱ)[fⁿ] ⟶ H⁰(Hᵖ(X, ℱ)^∧) ⟶ Hᵖ(X, ℱ)^ ⟶ 0` comparing the degree-zero derived f-adic completion of Hᵖ(X, ℱ) with its ordinary f-adic completion and with the first derived inverse limit of its f-power torsion”.

> **The left column of the diagram of [Stacks, Tag 0BLD].** With `A`, `f`, `X` and `ℱ` as in the
> source and `(-)^∧` derived `f`-adic completion presented by an arbitrary left adjoint to the
> inclusion of the derived-complete objects, for every `p` there is a short exact sequence
>
> `0 ⟶ R¹lim Hᵖ(X, ℱ)[fⁿ] ⟶ H⁰(Hᵖ(X, ℱ)^∧) ⟶ Hᵖ(X, ℱ)^ ⟶ 0`
>
> relating the derived completion of `Hᵖ(X, ℱ)` in degree zero to its ordinary `f`-adic completion
> and to the first derived inverse limit of its `f`-power torsion.

```lean
theorem exists_shortExact_leftColumn
    [HasProduct fun n : ℕ ↦ (Csys (mulF X ρ f ℱ)).obj ⟨n⟩]
    [HasProduct fun n : ℕ ↦ (quotientSections X ρ f ℱ).obj ⟨n⟩]
    [HasProduct fun n : ℕ ↦ (Ksys (mulF X ρ f ℱ)).obj ⟨n⟩]
    [HasProduct fun n : ℕ ↦
      (Ksys (mulF X ρ f ℱ) ⋙ derivedSectionsOver X.toRingedSpace ρ).obj ⟨n⟩]
    (p : ℤ) :
    let Hq : ℤ → ModuleCat.{u} A := fun q ↦
      (DerivedCategory.homologyFunctor (ModuleCat.{u} A) q).obj (derivedSectionsModule X ρ ℱ)
    let P : ObjectProperty (DerivedCategory (ModuleCat.{u} A)) :=
      fun L ↦ IsDerivedComplete (Ideal.span {f}) L
    ∀ (completion : DerivedCategory (ModuleCat.{u} A) ⥤ P.FullSubcategory)
      (_ : completion ⊣ P.ι),
      ∃ (leftIn : CompletionSequences.firstDerivedLimit A
            (PrincipalTorsionTower.powerTorsionSystem A (Hq p) f) ⟶
          (DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).obj
            ((completion ⋙ P.ι).obj
              ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (Hq p))))
        (leftOut : (DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).obj
            ((completion ⋙ P.ι).obj
              ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (Hq p))) ⟶
          limit (CompletionSequences.powerQuotientSystem A (Hq p) f))
        (hleft : leftIn ≫ leftOut = 0),
        (ShortComplex.mk leftIn leftOut hleft).ShortExact
```

**`Stacks.Algebraization.PrincipalQuotientTowerDiagram.nonempty_iso_firstDerivedLimit_torsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerDiagram.lean, line 458](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerDiagram.lean#L458). The attribute's comment: “the bottom isomorphism of the diagram: `R¹lim Hᵖ(X, ℱ)[fⁿ] ≅ R¹lim Hᵖ⁻¹(X, ℱ/fⁿℱ)` between the first derived inverse limit of the f-power torsion of Hᵖ(X, ℱ) and the first derived inverse limit of Hᵖ⁻¹ of the quotients. Unconditional: no reflector onto the derived-complete objects is assumed”.

> **The bottom isomorphism of the diagram of [Stacks, Tag 0BLD].** With `A`, `f`, `X` and `ℱ` as
> in the source, for every `p` the first derived inverse limit of the `f`-power torsion of
> `Hᵖ(X, ℱ)` is isomorphic to the first derived inverse limit of `Hᵖ⁻¹(X, ℱ/fⁿℱ)`:
>
> `R¹lim Hᵖ(X, ℱ)[fⁿ] ≅ R¹lim Hᵖ⁻¹(X, ℱ/fⁿℱ)`.

```lean
theorem nonempty_iso_firstDerivedLimit_torsion
    [HasProduct fun n : ℕ ↦ (Csys (mulF X ρ f ℱ)).obj ⟨n⟩]
    [HasProduct fun n : ℕ ↦ (quotientSections X ρ f ℱ).obj ⟨n⟩]
    [HasProduct fun n : ℕ ↦ (Ksys (mulF X ρ f ℱ)).obj ⟨n⟩]
    [HasProduct fun n : ℕ ↦
      (Ksys (mulF X ρ f ℱ) ⋙ derivedSectionsOver X.toRingedSpace ρ).obj ⟨n⟩]
    (p : ℤ) :
    let Hq : ℤ → ModuleCat.{u} A := fun q ↦
      (DerivedCategory.homologyFunctor (ModuleCat.{u} A) q).obj (derivedSectionsModule X ρ ℱ)
    Nonempty (CompletionSequences.firstDerivedLimit A
        (PrincipalTorsionTower.powerTorsionSystem A (Hq p) f) ≅
      CompletionSequences.firstDerivedLimit A (quotientCohomology X ρ f ℱ (p - 1)))
```

**`Stacks.Algebraization.PrincipalQuotientTowerFormalFunctions.nonempty_iso_derivedSections_limit_derivedCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerFormalFunctions.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerFormalFunctions.lean#L108). The attribute's comment: “the displayed equality `RΓ(X, lim ℱ/fⁿℱ) = RΓ(X, ℱ)^∧`, with derived f-adic completion presented as in Stacks 0BKG by an arbitrary left adjoint to the inclusion of the derived-complete objects; also derived completeness of `RΓ(X, lim ℱ/fⁿℱ)` and the identification `Hᵖ(X, lim ℱ/fⁿℱ) = Hᵖ(RΓ(X, ℱ)^∧)`. Unconditional: the countable products of D(𝒪\_X) and D(A) are supplied, not assumed”.

> **The displayed equality of [Stacks, Tag 0BLD].** Let `A` be a ring, `f ∈ A`, let `X` be a
> scheme over `A` through `ρ : A ⟶ Γ(X, 𝒪_X)` and let `ℱ` be a quasi-coherent `𝒪_X`-module whose
> `f`-power torsion stabilizes. Let `completion` be a left adjoint to the inclusion of the objects
> of `D(A)` that are derived complete for the ideal `(f)`, so that `(-)^∧ = completion ⋙ P.ι` is
> derived `f`-adic completion as in [Stacks, Tag 0BKG]. Then
>
> `RΓ(X, lim ℱ/f^(n+1)ℱ) ≅ RΓ(X, ℱ)^∧`,
>
> the object `RΓ(X, lim ℱ/f^(n+1)ℱ)` is derived complete for `(f)`, and for every `p` its `p`-th
> cohomology module is that of `RΓ(X, ℱ)^∧`.
>
> This is `nonempty_iso_derivedSections_limit_quotientTower_derivedCompletion` (in the namespace
> `PrincipalQuotientTowerCompletion`) with the countable products of `D(𝒪_X)` and of `D(A)` it
> takes as instance binders supplied.

```lean
theorem nonempty_iso_derivedSections_limit_derivedCompletion
    (hℱ : (ℱ : X.Modules).IsQuasicoherent) (hstab : Stabilizes (mulF X ρ f ℱ)) :
    letI := HasDerivedCategory.standard (SheafOfModules.{u} (structureSheafRing X.toRingedSpace))
    letI := HasDerivedCategory.standard (ModuleCat.{u} A)
    let P : ObjectProperty (DerivedCategory (ModuleCat.{u} A)) :=
      fun L ↦ IsDerivedComplete (Ideal.span {f}) L
    ∀ (completion : DerivedCategory (ModuleCat.{u} A) ⥤ P.FullSubcategory)
      (_ : completion ⊣ P.ι),
      let completed := completion ⋙ P.ι
      let Fhat : DerivedCategory (ModuleCat.{u} A) :=
        (derivedSectionsOver X.toRingedSpace ρ).obj
          ((DerivedCategory.singleFunctor
            (SheafOfModules.{u} (structureSheafRing X.toRingedSpace)) 0).obj
            (limit (quotientTower X ρ f ℱ)))
      Nonempty (Fhat ≅ completed.obj (derivedSectionsModule X ρ ℱ)) ∧
        IsDerivedComplete (Ideal.span {f}) Fhat ∧
        ∀ p : ℤ, Nonempty
          ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) p).obj Fhat ≅
            (DerivedCategory.homologyFunctor (ModuleCat.{u} A) p).obj
              (completed.obj (derivedSectionsModule X ρ ℱ)))
```

**`Stacks.Algebraization.PrincipalQuotientTowerFormalFunctions.exists_shortExact_middleColumn_quotients`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerFormalFunctions.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerFormalFunctions.lean#L154). The attribute's comment: “the middle column of the diagram: the short exact sequence `0 ⟶ R¹lim Hᵖ⁻¹(X, ℱ/fⁿℱ) ⟶ Hᵖ(X, lim ℱ/fⁿℱ) ⟶ lim Hᵖ(X, ℱ/fⁿℱ) ⟶ 0` at the ordinary limit, together with the isomorphism of a derived limit of the f-power Koszul tower with `lim ℱ/fⁿℱ`. Unconditional: the countable products of D(𝒪\_X) and D(A) are supplied, not assumed”.

> **The middle column of the diagram of [Stacks, Tag 0BLD], in the form of [Stacks, Tag 0H3E].**
> With `A`, `f`, `X` and `ℱ` as in the source, let `E^` be a derived limit of the `f`-power Koszul
> tower `ℱ ⊗_{𝒪_X} (𝒪_X --f^(n+1)--> 𝒪_X)`. Then `E^ ≅ lim ℱ/f^(n+1)ℱ`, and for every `p` there is
> a short exact sequence
>
> `0 ⟶ R¹lim Hᵖ⁻¹(X, ℱ/fⁿℱ) ⟶ Hᵖ(X, lim ℱ/fⁿℱ) ⟶ lim Hᵖ(X, ℱ/fⁿℱ) ⟶ 0`,
>
> whose inclusion descends the connecting morphism of the Milnor triangle and whose projection is
> characterized by the limit projections, and whose outer terms are isomorphic to those of the
> corresponding sequence for the Koszul tower.
>
> This is `PrincipalQuotientTower.exists_shortExact_homology_derivedSections_limit_quotientTower`
> with the countable products of `D(𝒪_X)` and of `D(A)` it takes as instance binders supplied; the
> statement names them, since it mentions products and derived limits.

```lean
theorem exists_shortExact_middleColumn_quotients
    (hℱ : (ℱ : X.Modules).IsQuasicoherent) (hstab : Stabilizes (mulF X ρ f ℱ)) :
    letI := HasDerivedCategory.standard (SheafOfModules.{u} (structureSheafRing X.toRingedSpace))
    letI := HasDerivedCategory.standard (ModuleCat.{u} A)
    letI := Stacks.Algebraization.hasProductsOfShape_nat_derivedCategory_modules X
    letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A)) :=
      Stacks.DerivedProducts.hasProductsOfShape_derivedCategory
    ∀ (Ehat : DerivedCategory (SheafOfModules.{u} (structureSheafRing X.toRingedSpace))),
      IsDerivedLimit (Ksys (mulF X ρ f ℱ)) Ehat →
    let Fhat : DerivedCategory (SheafOfModules.{u} (structureSheafRing X.toRingedSpace)) :=
      (DerivedCategory.singleFunctor
        (SheafOfModules.{u} (structureSheafRing X.toRingedSpace)) 0).obj
        (limit (quotientTower X ρ f ℱ))
    let F : ℕᵒᵖ ⥤ DerivedCategory (ModuleCat.{u} A) :=
      Csys (mulF X ρ f ℱ) ⋙ derivedSectionsOver X.toRingedSpace ρ
    let G : ℕᵒᵖ ⥤ DerivedCategory (ModuleCat.{u} A) :=
      Ksys (mulF X ρ f ℱ) ⋙ derivedSectionsOver X.toRingedSpace ρ
    let Y : ℕ → DerivedCategory (ModuleCat.{u} A) := fun n ↦ F.obj (op n)
    let d : (∏ᶜ Y) ⟶ ∏ᶜ Y := Pi.lift fun n : ℕ ↦
      Pi.π Y n - Pi.π Y (n + 1) ≫ F.map (homOfLE (Nat.le_succ n)).op
    Nonempty (Ehat ≅ Fhat) ∧
      ∃ (a : (derivedSectionsOver X.toRingedSpace ρ).obj Fhat ⟶ ∏ᶜ Y)
        (b : (∏ᶜ Y) ⟶ ((derivedSectionsOver X.toRingedSpace ρ).obj Fhat)⟦(1 : ℤ)⟧),
        let T := Triangle.mk a d b
        T ∈ distTriang (DerivedCategory (ModuleCat.{u} A)) ∧
          ∀ p : ℤ,
            let H := DerivedCategory.homologyFunctor (ModuleCat.{u} A) p
            let H₁ := DerivedCategory.homologyFunctor (ModuleCat.{u} A) (p - 1)
            let homologySystem : ℕᵒᵖ ⥤ ModuleCat.{u} A := F ⋙ H
            let shiftedHomologySystem : ℕᵒᵖ ⥤ ModuleCat.{u} A := F ⋙ H₁
            let P : ModuleCat.{u} A :=
              ∏ᶜ fun n : ℕ ↦ shiftedHomologySystem.obj (op n)
            let δ : P ⟶ P := Pi.lift fun n : ℕ ↦
              Pi.π (fun n : ℕ ↦ shiftedHomologySystem.obj (op n)) n -
                Pi.π (fun n : ℕ ↦ shiftedHomologySystem.obj (op n)) (n + 1) ≫
                  shiftedHomologySystem.map (homOfLE (Nat.le_succ n)).op
            ∃ (e : H₁.obj (∏ᶜ Y) ≅ P)
              (i : cokernel δ ⟶ H.obj ((derivedSectionsOver X.toRingedSpace ρ).obj Fhat))
              (q : H.obj ((derivedSectionsOver X.toRingedSpace ρ).obj Fhat) ⟶
                limit homologySystem)
              (w : i ≫ q = 0),
              e.hom = piComparison H₁ Y ∧
                cokernel.π δ ≫ i = e.inv ≫
                  DerivedCategory.HomologySequence.δ T (p - 1) p (by omega) ∧
                (∀ n : ℕ, q ≫ limit.π homologySystem (op n) =
                  H.map a ≫ H.map (Pi.π Y n)) ∧
                (ShortComplex.mk i q w).ShortExact ∧
                Nonempty (limit homologySystem ≅ limit (G ⋙ H)) ∧
                Nonempty (cokernel δ ≅
                  CompletionSequences.firstDerivedLimit A (G ⋙ H₁))
```

**`Stacks.Algebraization.PrincipalQuotientTowerFormalFunctions.exists_diagram_derivedSections_limit_quotientTower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerFormalFunctions.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerFormalFunctions.lean#L251). The attribute's comment: “the commutative diagram with exact rows and columns, in full: the top row `0 ⟶ Hᵖ(X, ℱ)^ ⟶ lim Hᵖ(X, ℱ/fⁿℱ) ⟶ T_f(Hᵖ⁺¹(X, ℱ)) ⟶ 0`, the middle row `0 ⟶ H⁰(Hᵖ(X, ℱ)^∧) ⟶ Hᵖ(X, lim ℱ/fⁿℱ) ⟶ T_f(Hᵖ⁺¹(X, ℱ)) ⟶ 0`, the left column `0 ⟶ R¹lim Hᵖ(X, ℱ)[fⁿ] ⟶ H⁰(Hᵖ(X, ℱ)^∧) ⟶ Hᵖ(X, ℱ)^ ⟶ 0`, the middle column `0 ⟶ R¹lim Hᵖ⁻¹(X, ℱ/fⁿℱ) ⟶ Hᵖ(X, lim ℱ/fⁿℱ) ⟶ lim Hᵖ(X, ℱ/fⁿℱ) ⟶ 0`, the bottom isomorphism `R¹lim Hᵖ(X, ℱ)[fⁿ] ≅ R¹lim Hᵖ⁻¹(X, ℱ/fⁿℱ)`, the identity right column, and the commutativity of the three squares. Unconditional: the countable products of D(𝒪\_X) and D(A) are supplied, not assumed”.

> **The commutative diagram of [Stacks, Tag 0BLD].** Let `A` be a ring, `f ∈ A`, let `X` be a
> scheme over `A` through `ρ : A ⟶ Γ(X, 𝒪_X)` and let `ℱ` be a quasi-coherent `𝒪_X`-module whose
> `f`-power torsion stabilizes. Let `completion` be a left adjoint to the inclusion of the objects
> of `D(A)` that are derived complete for `(f)`, so that `(-)^∧ = completion ⋙ P.ι` is derived
> `f`-adic completion as in [Stacks, Tag 0BKG]. Then for every `p` there is a commutative diagram
>
> ```
>                      0                              0
>                      ↑                              ↑
> 0 ⟶  Hᵖ(X, ℱ)^   ⟶  lim Hᵖ(X, ℱ/fⁿℱ)  ⟶  T_f(Hᵖ⁺¹(X, ℱ))  ⟶  0
>                      ↑                              ↑              ‖
> 0 ⟶ H⁰(Hᵖ(X, ℱ)^∧) ⟶ Hᵖ(X, lim ℱ/fⁿℱ) ⟶  T_f(Hᵖ⁺¹(X, ℱ))  ⟶  0
>                      ↑                              ↑
>       R¹lim Hᵖ(X, ℱ)[fⁿ]  ≅  R¹lim Hᵖ⁻¹(X, ℱ/fⁿℱ)
>                      ↑                              ↑
>                      0                              0
> ```
>
> with exact rows and columns, where `Hᵖ(X, ℱ)^ = lim Hᵖ(X, ℱ)/fⁿHᵖ(X, ℱ)` is the ordinary `f`-adic
> completion and `T_f(-)` is the `f`-adic Tate module. The right-hand column is the identity: the
> two projections to `T_f(Hᵖ⁺¹(X, ℱ))` agree after the middle vertical map.
>
> This is `PrincipalQuotientTowerDiagram.exists_formalFunctionsDiagram` with the countable products
> of `D(𝒪_X)` and of `D(A)` it takes as instance binders supplied.

```lean
theorem exists_diagram_derivedSections_limit_quotientTower (p : ℤ) :
    letI := HasDerivedCategory.standard (ModuleCat.{u} A)
    let Hq : ℤ → ModuleCat.{u} A := fun q ↦
      (DerivedCategory.homologyFunctor (ModuleCat.{u} A) q).obj (derivedSectionsModule X ρ ℱ)
    let P : ObjectProperty (DerivedCategory (ModuleCat.{u} A)) :=
      fun L ↦ IsDerivedComplete (Ideal.span {f}) L
    ∀ (completion : DerivedCategory (ModuleCat.{u} A) ⥤ P.FullSubcategory)
      (_ : completion ⊣ P.ι),
      let completed := completion ⋙ P.ι
      let ordinaryCompletion := limit (CompletionSequences.powerQuotientSystem A (Hq p) f)
      let tate := CompletionSequences.adicTateModule A (Hq (p + 1)) f
      let h0Completion := (DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).obj
        (completed.obj ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (Hq p)))
      let torsionR1 := CompletionSequences.firstDerivedLimit A
        (PrincipalTorsionTower.powerTorsionSystem A (Hq p) f)
      let limitQuotientCohomology := limit (quotientCohomology X ρ f ℱ p)
      let previousQuotientR1 := CompletionSequences.firstDerivedLimit A
        (quotientCohomology X ρ f ℱ (p - 1))
      let sectionsCohomology := (DerivedCategory.homologyFunctor (ModuleCat.{u} A) p).obj
        (limitQuotientSections X ρ f ℱ)
      ∃ (topIn : ordinaryCompletion ⟶ limitQuotientCohomology)
        (topOut : limitQuotientCohomology ⟶ tate)
        (htop : topIn ≫ topOut = 0)
        (middleIn : h0Completion ⟶ sectionsCohomology)
        (middleOut : sectionsCohomology ⟶ tate)
        (hmiddle : middleIn ≫ middleOut = 0)
        (leftIn : torsionR1 ⟶ h0Completion) (leftOut : h0Completion ⟶ ordinaryCompletion)
        (hleft : leftIn ≫ leftOut = 0)
        (columnIn : previousQuotientR1 ⟶ sectionsCohomology)
        (columnOut : sectionsCohomology ⟶ limitQuotientCohomology)
        (hcolumn : columnIn ≫ columnOut = 0)
        (bottom : torsionR1 ≅ previousQuotientR1),
        (ShortComplex.mk topIn topOut htop).ShortExact ∧
          (ShortComplex.mk middleIn middleOut hmiddle).ShortExact ∧
          (ShortComplex.mk leftIn leftOut hleft).ShortExact ∧
          (ShortComplex.mk columnIn columnOut hcolumn).ShortExact ∧
          middleIn ≫ columnOut = leftOut ≫ topIn ∧
          middleOut = columnOut ≫ topOut ∧
          bottom.hom ≫ columnIn = leftIn ≫ middleIn
```

**`Stacks.Algebraization.PrincipalQuotientTowerFormalFunctions.exists_shortExact_topRow_quotients`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerFormalFunctions.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerFormalFunctions.lean#L308). The attribute's comment: “the top row of the diagram: the short exact sequence `0 ⟶ Hᵖ(X, ℱ)^ ⟶ lim Hᵖ(X, ℱ/fⁿℱ) ⟶ T_f(Hᵖ⁺¹(X, ℱ)) ⟶ 0`. Unconditional: no reflector onto the derived-complete objects and no countable products are assumed”.

> **The top row of the diagram of [Stacks, Tag 0BLD].** With `A`, `f`, `X` and `ℱ` as in the
> source, for every `p` there is a short exact sequence
>
> `0 ⟶ Hᵖ(X, ℱ)^ ⟶ lim Hᵖ(X, ℱ/fⁿℱ) ⟶ T_f(Hᵖ⁺¹(X, ℱ)) ⟶ 0`,
>
> where `Hᵖ(X, ℱ)^ = lim Hᵖ(X, ℱ)/fⁿHᵖ(X, ℱ)` is the ordinary `f`-adic completion and `T_f(-)` the
> `f`-adic Tate module. This is `PrincipalQuotientTowerDiagram.exists_shortExact_topRow` with its
> countable products supplied.

```lean
theorem exists_shortExact_topRow_quotients (p : ℤ) :
    letI := HasDerivedCategory.standard (ModuleCat.{u} A)
    let Hq : ℤ → ModuleCat.{u} A := fun q ↦
      (DerivedCategory.homologyFunctor (ModuleCat.{u} A) q).obj (derivedSectionsModule X ρ ℱ)
    ∃ (topIn : limit (CompletionSequences.powerQuotientSystem A (Hq p) f) ⟶
        limit (quotientCohomology X ρ f ℱ p))
      (topOut : limit (quotientCohomology X ρ f ℱ p) ⟶
        CompletionSequences.adicTateModule A (Hq (p + 1)) f)
      (htop : topIn ≫ topOut = 0),
      (ShortComplex.mk topIn topOut htop).ShortExact
```

**`Stacks.Algebraization.PrincipalQuotientTowerFormalFunctions.exists_shortExact_middleRow_quotients`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerFormalFunctions.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerFormalFunctions.lean#L337). The attribute's comment: “the middle row of the diagram: the short exact sequence `0 ⟶ H⁰(Hᵖ(X, ℱ)^∧) ⟶ Hᵖ(X, lim ℱ/fⁿℱ) ⟶ T_f(Hᵖ⁺¹(X, ℱ)) ⟶ 0`, with `(-)^∧` the derived f-adic completion presented as in Stacks 0BKG by an arbitrary left adjoint to the inclusion of the derived-complete objects. Unconditional: no countable products are assumed”.

> **The middle row of the diagram of [Stacks, Tag 0BLD].** With `A`, `f`, `X` and `ℱ` as in the
> source and `(-)^∧` derived `f`-adic completion presented by an arbitrary left adjoint to the
> inclusion of the derived-complete objects, for every `p` there is a short exact sequence
>
> `0 ⟶ H⁰(Hᵖ(X, ℱ)^∧) ⟶ Hᵖ(X, lim ℱ/fⁿℱ) ⟶ T_f(Hᵖ⁺¹(X, ℱ)) ⟶ 0`.
>
> This is `PrincipalQuotientTowerDiagram.exists_shortExact_middleRow` with its countable products
> supplied.

```lean
theorem exists_shortExact_middleRow_quotients (p : ℤ) :
    letI := HasDerivedCategory.standard (ModuleCat.{u} A)
    let Hq : ℤ → ModuleCat.{u} A := fun q ↦
      (DerivedCategory.homologyFunctor (ModuleCat.{u} A) q).obj (derivedSectionsModule X ρ ℱ)
    let P : ObjectProperty (DerivedCategory (ModuleCat.{u} A)) :=
      fun L ↦ IsDerivedComplete (Ideal.span {f}) L
    ∀ (completion : DerivedCategory (ModuleCat.{u} A) ⥤ P.FullSubcategory)
      (_ : completion ⊣ P.ι),
      ∃ (middleIn : (DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).obj
          ((completion ⋙ P.ι).obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (Hq p))) ⟶
          (DerivedCategory.homologyFunctor (ModuleCat.{u} A) p).obj
            (limitQuotientSections X ρ f ℱ))
        (middleOut : (DerivedCategory.homologyFunctor (ModuleCat.{u} A) p).obj
            (limitQuotientSections X ρ f ℱ) ⟶
          CompletionSequences.adicTateModule A (Hq (p + 1)) f)
        (hmiddle : middleIn ≫ middleOut = 0),
        (ShortComplex.mk middleIn middleOut hmiddle).ShortExact
```

**`Stacks.Algebraization.PrincipalQuotientTowerFormalFunctions.exists_shortExact_leftColumn_quotients`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerFormalFunctions.lean, line 374](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerFormalFunctions.lean#L374). The attribute's comment: “the left column of the diagram: the short exact sequence `0 ⟶ R¹lim Hᵖ(X, ℱ)[fⁿ] ⟶ H⁰(Hᵖ(X, ℱ)^∧) ⟶ Hᵖ(X, ℱ)^ ⟶ 0`, with `(-)^∧` the derived f-adic completion presented as in Stacks 0BKG by an arbitrary left adjoint to the inclusion of the derived-complete objects. Unconditional: no countable products are assumed”.

> **The left column of the diagram of [Stacks, Tag 0BLD].** With `A`, `f`, `X` and `ℱ` as in the
> source and `(-)^∧` derived `f`-adic completion presented by an arbitrary left adjoint to the
> inclusion of the derived-complete objects, for every `p` there is a short exact sequence
>
> `0 ⟶ R¹lim Hᵖ(X, ℱ)[fⁿ] ⟶ H⁰(Hᵖ(X, ℱ)^∧) ⟶ Hᵖ(X, ℱ)^ ⟶ 0`.
>
> This is `PrincipalQuotientTowerDiagram.exists_shortExact_leftColumn` with its countable products
> supplied.

```lean
theorem exists_shortExact_leftColumn_quotients (p : ℤ) :
    letI := HasDerivedCategory.standard (ModuleCat.{u} A)
    let Hq : ℤ → ModuleCat.{u} A := fun q ↦
      (DerivedCategory.homologyFunctor (ModuleCat.{u} A) q).obj (derivedSectionsModule X ρ ℱ)
    let P : ObjectProperty (DerivedCategory (ModuleCat.{u} A)) :=
      fun L ↦ IsDerivedComplete (Ideal.span {f}) L
    ∀ (completion : DerivedCategory (ModuleCat.{u} A) ⥤ P.FullSubcategory)
      (_ : completion ⊣ P.ι),
      ∃ (leftIn : CompletionSequences.firstDerivedLimit A
            (PrincipalTorsionTower.powerTorsionSystem A (Hq p) f) ⟶
          (DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).obj
            ((completion ⋙ P.ι).obj
              ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (Hq p))))
        (leftOut : (DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).obj
            ((completion ⋙ P.ι).obj
              ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (Hq p))) ⟶
          limit (CompletionSequences.powerQuotientSystem A (Hq p) f))
        (hleft : leftIn ≫ leftOut = 0),
        (ShortComplex.mk leftIn leftOut hleft).ShortExact
```

**`Stacks.Algebraization.PrincipalQuotientTowerFormalFunctions.nonempty_iso_firstDerivedLimit_torsion_quotients`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerFormalFunctions.lean, line 410](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerFormalFunctions.lean#L410). The attribute's comment: “the bottom isomorphism of the diagram: `R¹lim Hᵖ(X, ℱ)[fⁿ] ≅ R¹lim Hᵖ⁻¹(X, ℱ/fⁿℱ)`. Unconditional: no reflector onto the derived-complete objects and no countable products are assumed”.

> **The bottom isomorphism of the diagram of [Stacks, Tag 0BLD].** With `A`, `f`, `X` and `ℱ` as
> in the source, for every `p`
>
> `R¹lim Hᵖ(X, ℱ)[fⁿ] ≅ R¹lim Hᵖ⁻¹(X, ℱ/fⁿℱ)`.
>
> This is `PrincipalQuotientTowerDiagram.nonempty_iso_firstDerivedLimit_torsion` with its countable
> products supplied.

```lean
theorem nonempty_iso_firstDerivedLimit_torsion_quotients (p : ℤ) :
    letI := HasDerivedCategory.standard (ModuleCat.{u} A)
    let Hq : ℤ → ModuleCat.{u} A := fun q ↦
      (DerivedCategory.homologyFunctor (ModuleCat.{u} A) q).obj (derivedSectionsModule X ρ ℱ)
    Nonempty (CompletionSequences.firstDerivedLimit A
        (PrincipalTorsionTower.powerTorsionSystem A (Hq p) f) ≅
      CompletionSequences.firstDerivedLimit A (quotientCohomology X ρ f ℱ (p - 1)))
```

**`Stacks.Algebraization.PrincipalQuotientTower.exists_shortExact_homology_derivedSections_limit_quotientTower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerSections.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalQuotientTowerSections.lean#L245). The attribute's comment: “the middle column of the diagram, for a quasi-coherent module on a scheme: the short exact sequence `0 ⟶ R¹lim Hᵖ⁻¹(X, ℱ/fⁿℱ) ⟶ Hᵖ(X, lim ℱ/fⁿℱ) ⟶ lim Hᵖ(X, ℱ/fⁿℱ) ⟶ 0` at the ordinary limit, together with the isomorphism of a derived limit of the f-power Koszul tower with `lim ℱ/fⁿℱ`. The displayed equality `RΓ(X, lim ℱ/fⁿℱ) = RΓ(X, ℱ)^∧` and the remaining rows and columns of the diagram are not covered”.

> **Formal sections for a principal ideal on a scheme: the middle column of the diagram.**
> Let `A` be a ring, `f ∈ A`, let `X` be a scheme over `A` through `ρ : A ⟶ Γ(X, 𝒪_X)` and let `ℱ`
> be a quasi-coherent `𝒪_X`-module whose `f`-power torsion stabilizes. Let `E^` be a derived limit
> of the `f`-power Koszul tower `ℱ ⊗_{𝒪_X} (𝒪_X --f^(n+1)--> 𝒪_X)`. Then `E^` is isomorphic to the
> ordinary inverse limit `lim ℱ/f^(n+1)ℱ`, and for every `p` the cohomology of
> `RΓ(X, lim ℱ/f^(n+1)ℱ)` over `A` sits in a short exact sequence
>
> `0 ⟶ R¹lim Hᵖ⁻¹(X, ℱ/fⁿℱ) ⟶ Hᵖ(X, lim ℱ/fⁿℱ) ⟶ lim Hᵖ(X, ℱ/fⁿℱ) ⟶ 0`,
>
> whose inclusion descends the connecting morphism of the Milnor triangle and whose projection is
> characterized by the limit projections, and whose outer terms are isomorphic to the outer terms of
> the corresponding sequence for the Koszul tower.

```lean
theorem exists_shortExact_homology_derivedSections_limit_quotientTower
    (hstab : Stabilizes (mulF X ρ f ℱ))
    [HasProduct fun n : ℕ ↦ (Csys (mulF X ρ f ℱ)).obj ⟨n⟩]
    [HasProduct fun n : ℕ ↦
      (Csys (mulF X ρ f ℱ) ⋙ derivedSectionsOver X.toRingedSpace ρ).obj ⟨n⟩]
    [HasProduct fun n : ℕ ↦ (Ksys (mulF X ρ f ℱ)).obj ⟨n⟩]
    (Ehat : DerivedCategory (SheafOfModules.{u} (structureSheafRing X.toRingedSpace)))
    (hEhat : IsDerivedLimit (Ksys (mulF X ρ f ℱ)) Ehat) :
    let Fhat : DerivedCategory (SheafOfModules.{u} (structureSheafRing X.toRingedSpace)) :=
      (DerivedCategory.singleFunctor
        (SheafOfModules.{u} (structureSheafRing X.toRingedSpace)) 0).obj
        (limit (quotientTower X ρ f ℱ))
    let F : ℕᵒᵖ ⥤ DerivedCategory (ModuleCat.{u} A) :=
      Csys (mulF X ρ f ℱ) ⋙ derivedSectionsOver X.toRingedSpace ρ
    let G : ℕᵒᵖ ⥤ DerivedCategory (ModuleCat.{u} A) :=
      Ksys (mulF X ρ f ℱ) ⋙ derivedSectionsOver X.toRingedSpace ρ
    let Y : ℕ → DerivedCategory (ModuleCat.{u} A) := fun n ↦ F.obj (op n)
    let d : (∏ᶜ Y) ⟶ ∏ᶜ Y := Pi.lift fun n : ℕ ↦
      Pi.π Y n - Pi.π Y (n + 1) ≫ F.map (homOfLE (Nat.le_succ n)).op
    Nonempty (Ehat ≅ Fhat) ∧
      ∃ (a : (derivedSectionsOver X.toRingedSpace ρ).obj Fhat ⟶ ∏ᶜ Y)
        (b : (∏ᶜ Y) ⟶ ((derivedSectionsOver X.toRingedSpace ρ).obj Fhat)⟦(1 : ℤ)⟧),
        let T := Triangle.mk a d b
        T ∈ distTriang (DerivedCategory (ModuleCat.{u} A)) ∧
          ∀ p : ℤ,
            let H := DerivedCategory.homologyFunctor (ModuleCat.{u} A) p
            let H₁ := DerivedCategory.homologyFunctor (ModuleCat.{u} A) (p - 1)
            let homologySystem : ℕᵒᵖ ⥤ ModuleCat.{u} A := F ⋙ H
            let shiftedHomologySystem : ℕᵒᵖ ⥤ ModuleCat.{u} A := F ⋙ H₁
            let P : ModuleCat.{u} A :=
              ∏ᶜ fun n : ℕ ↦ shiftedHomologySystem.obj (op n)
            let δ : P ⟶ P := Pi.lift fun n : ℕ ↦
              Pi.π (fun n : ℕ ↦ shiftedHomologySystem.obj (op n)) n -
                Pi.π (fun n : ℕ ↦ shiftedHomologySystem.obj (op n)) (n + 1) ≫
                  shiftedHomologySystem.map (homOfLE (Nat.le_succ n)).op
            ∃ (e : H₁.obj (∏ᶜ Y) ≅ P)
              (i : cokernel δ ⟶ H.obj ((derivedSectionsOver X.toRingedSpace ρ).obj Fhat))
              (q : H.obj ((derivedSectionsOver X.toRingedSpace ρ).obj Fhat) ⟶
                limit homologySystem)
              (w : i ≫ q = 0),
              e.hom = piComparison H₁ Y ∧
                cokernel.π δ ≫ i = e.inv ≫
                  DerivedCategory.HomologySequence.δ T (p - 1) p ∧
                (∀ n : ℕ, q ≫ limit.π homologySystem (op n) =
                  H.map a ≫ H.map (Pi.π Y n)) ∧
                (ShortComplex.mk i q w).ShortExact ∧
                Nonempty (limit homologySystem ≅ limit (G ⋙ H)) ∧
                Nonempty (cokernel δ ≅
                  CompletionSequences.firstDerivedLimit A (G ⋙ H₁))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.3, Tag 0BLA](https://stacks.math.columbia.edu/tag/0BLA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
