---
declaration: section
origin: cited
lean: Stacks.Cohomology.PrincipalFormalFunctions.formalFunctionsDiagram_principalKoszulTower, proIso_Ksys_Csys, Stacks.Cohomology.PrincipalFormalFunctions.nonempty_iso_derivedSections_quotientTower_derivedCompletion, Stacks.Cohomology.PrincipalFormalFunctions.exists_formalFunctionsDiagram_quotientTower, Stacks.Cohomology.QuotientTowerFormalFunctions.exists_shortExact_homology_derivedSections_quotientTower
statement: formalized
proof: formalized
---

# 20.39 Inverse systems and cohomology, III

Section 20.39 of the Stacks Project, [Tag 0H3B](https://stacks.math.columbia.edu/tag/0H3B). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H3C, a lemma

[Tag 0H3C](https://stacks.math.columbia.edu/tag/0H3C) in the Stacks Project.

**`Stacks.Cohomology.PrincipalFormalFunctions.formalFunctionsDiagram_principalKoszulTower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalFormalFunctionsDiagram.lean, line 749](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalFormalFunctionsDiagram.lean#L749). The attribute's comment: “the whole diagram, with its maps the ones induced by E ⟶ E\_n, the boundaries of E ⟶ E ⟶ E\_n ⟶ E[1], the projections E^ ⟶ E\_n and the triangle of E^, the sequences of Stacks 0BKG and 0H32 read through RΓ(X, E^) ≅ RΓ(X, E)^∧ (compatible with the maps to RΓ(X, E\_n)); exactness of rows and columns and the three commutativities”.

> **Formal functions for a principal ideal on a ringed space: [Stacks, Tag 0H3C].** Let
> `(X, 𝒪_X)` be a ringed space, let `ρ : A ⟶ Γ(X, 𝒪_X)` be a homomorphism from a commutative ring
> `A`, let `f ∈ A` and let `E ∈ D(𝒪_X)`. Let `E_n = E ⊗_{𝒪_X} (𝒪_X --f^(n+1)--> 𝒪_X)` be the
> `f`-power Koszul tower, the cone of multiplication by `f^(n+1)` on `E`, so that there are
> distinguished triangles `E ⟶ E ⟶ E_n ⟶ E[1]`, and let `E^ = R lim E_n`, given with its
> distinguished triangle `E^ ⟶ ∏ E_n ⟶ ∏ E_n ⟶ E^[1]` whose middle map is `1 - shift`. Write
> `Hᵖ(X, -)` for the cohomology of `RΓ(X, -) : D(𝒪_X) ⥤ D(A)`, let `(-)^∧` be derived `f`-adic
> completion (a left adjoint `completion` to the inclusion of the derived-complete objects), and
> let `p ∈ ℤ`. Then `RΓ(X, E^) ≅ RΓ(X, E)^∧` by an isomorphism `Φ` which, composed with the unit
> `RΓ(X, E) ⟶ RΓ(X, E)^∧` and the projections `RΓ(X, E^) ⟶ RΓ(X, E_n)`, gives the maps
> `RΓ(X, E) ⟶ RΓ(X, E_n)` induced by `E ⟶ E_n`, and there is the commutative diagram with exact
> rows and columns
>
> * the top row `0 ⟶ Hᵖ(X, E)^ ⟶ lim Hᵖ(X, E_n) ⟶ T_f(Hᵖ⁺¹(X, E)) ⟶ 0`, where `Hᵖ(X, E)^` is the
>   `f`-adic completion `lim Hᵖ(X, E)/fⁿ⁺¹` and `T_f` the `f`-adic Tate module `lim (-)[fⁿ⁺¹]`;
>   its first map is the limit of the maps `Hᵖ(X, E)/fⁿ⁺¹ ⟶ Hᵖ(X, E_n)` induced by `E ⟶ E_n`, its
>   second the limit of the boundaries `Hᵖ(X, E_n) ⟶ Hᵖ⁺¹(X, E)[fⁿ⁺¹]` of `E ⟶ E ⟶ E_n ⟶ E[1]`;
> * the middle row `0 ⟶ H⁰(Hᵖ(X, E)^∧) ⟶ Hᵖ(X, E^) ⟶ T_f(Hᵖ⁺¹(X, E)) ⟶ 0`, the sequence of
>   [Stacks, Tag 0H32] for `K = RΓ(X, E)` read through `Hᵖ(Φ)`;
> * the left column `0 ⟶ R¹lim Hᵖ(X, E)[fⁿ] ⟶ H⁰(Hᵖ(X, E)^∧) ⟶ Hᵖ(X, E)^ ⟶ 0` of
>   [Stacks, Tag 0BKG];
> * the middle column `0 ⟶ R¹lim Hᵖ⁻¹(X, E_n) ⟶ Hᵖ(X, E^) ⟶ lim Hᵖ(X, E_n) ⟶ 0`, whose second
>   map is induced by the projections `E^ ⟶ E_n` and whose first descends the boundary of the
>   image under `RΓ(X, -)` of the triangle of `E^`, read through the isomorphism
>   `Hᵖ⁻¹(X, ∏ E_n) ≅ ∏ Hᵖ⁻¹(X, E_n)`;
> * the bottom isomorphism `R¹lim Hᵖ(X, E)[fⁿ] ≅ R¹lim Hᵖ⁻¹(X, E_n)`, inverse to `R¹lim` of the
>   boundaries `Hᵖ⁻¹(X, E_n) ⟶ Hᵖ(X, E)[fⁿ⁺¹]`;
>
> the right-hand column being the identity of `T_f(Hᵖ⁺¹(X, E))`.

```lean
theorem formalFunctionsDiagram_principalKoszulTower
    (E Ehat : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (a : Ehat ⟶ ∏ᶜ fun n : ℕ ↦ (principalKoszulTower X ρ f E).obj ⟨n⟩)
    (b : (∏ᶜ fun n : ℕ ↦ (principalKoszulTower X ρ f E).obj ⟨n⟩) ⟶ Ehat⟦(1 : ℤ)⟧)
    (hT : Triangle.mk a (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦ (principalKoszulTower X ρ f E).obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦ (principalKoszulTower X ρ f E).obj ⟨n⟩) (n + 1) ≫
            (principalKoszulTower X ρ f E).map (homOfLE (Nat.le_succ n)).op) b ∈
      distTriang (DerivedCategory (SheafOfModules.{u} (structureSheafRing X))))
    (p : ℤ) :
    let P : ObjectProperty (DerivedCategory (ModuleCat.{u} A)) :=
      fun L ↦ IsDerivedComplete (Ideal.span {f}) L
    ∀ (completion : DerivedCategory (ModuleCat.{u} A) ⥤ P.FullSubcategory)
      (adj : completion ⊣ P.ι),
      let completed := completion ⋙ P.ι
      let HH (q : ℤ) := DerivedCategory.homologyFunctor (ModuleCat.{u} A) q
      let RΓ := derivedSectionsOver X ρ
      let K := RΓ.obj E
      let H (q : ℤ) := (HH q).obj K
      let CE := DerivedCategory.Q.objPreimage E
      let eE := DerivedCategory.Q.objObjPreimageIso E
      let koszulTriangle (n : ℕ) := RΓ.mapTriangle.obj (DerivedCategory.Q.mapTriangle.obj
        (CochainComplex.mappingCone.triangle (smulComplex X (baseSmul X ρ f) CE ^ (n + 1)).asHom))
      let Y := fun n : ℕ ↦ (principalKoszulTower X ρ f E).obj ⟨n⟩
      let limitTriangle := RΓ.mapTriangle.obj (Triangle.mk a (Pi.lift fun n : ℕ ↦
        Pi.π Y n - Pi.π Y (n + 1) ≫
          (principalKoszulTower X ρ f E).map (homOfLE (Nat.le_succ n)).op) b)
      let cohTower (q : ℤ) := (principalKoszulTower X ρ f E ⋙ RΓ) ⋙ HH q
      let ordinaryCompletion := limit (CompletionSequences.powerQuotientSystem A (H p) f)
      let limitCoh := limit (cohTower p)
      let tate := CompletionSequences.adicTateModule A (H (p + 1)) f
      let H0CompletedHp := (HH 0).obj
        (completed.obj ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (H p)))
      let HpEhat := (HH p).obj (RΓ.obj Ehat)
      let R1Torsion := CompletionSequences.firstDerivedLimit A
        (PrincipalTorsionTower.powerTorsionSystem A (H p) f)
      let R1PreviousCoh := CompletionSequences.firstDerivedLimit A (cohTower (p - 1))
      let productComparison : (HH (p - 1)).obj (RΓ.obj (∏ᶜ Y)) ⟶
          CompletionSequences.moduleProduct A (cohTower (p - 1)) :=
        Pi.lift fun n : ℕ ↦ (HH (p - 1)).map (RΓ.map (Pi.π Y n))
      ∃ (S : CompletionSequences.PrincipalCompletionSequences A f completed adj.unit)
        (Φ : RΓ.obj Ehat ≅ completed.obj K),
        let middleIn : H0CompletedHp ⟶ HpEhat :=
          (S.truncation K p).inclusion S.shift ≫ (HH p).map Φ.inv
        let middleOut : HpEhat ⟶ tate := (HH p).map Φ.hom ≫
          (S.truncation K p).projection f S.shift (S.moduleSequence (H (p + 1))).tateIso
        let leftIn : R1Torsion ⟶ H0CompletedHp := (S.moduleSequence (H p)).inclusion
        let leftOut : H0CompletedHp ⟶ ordinaryCompletion := (S.moduleSequence (H p)).projection
        ∃ (termIn : CompletionSequences.powerQuotientSystem A (H p) f ⟶ cohTower p)
          (termOut : cohTower p ⟶ PrincipalTorsionTower.powerTorsionSystem A (H (p + 1)) f)
          (previousOut : cohTower (p - 1) ⟶
            PrincipalTorsionTower.powerTorsionSystem A (H p) f)
          (topIn : ordinaryCompletion ⟶ limitCoh)
          (topOut : limitCoh ⟶ tate)
          (htop : topIn ≫ topOut = 0)
          (hmiddle : middleIn ≫ middleOut = 0)
          (hleft : leftIn ≫ leftOut = 0)
          (columnIn : R1PreviousCoh ⟶ HpEhat)
          (columnOut : HpEhat ⟶ limitCoh)
          (hcolumn : columnIn ≫ columnOut = 0)
          (bottom : R1Torsion ≅ R1PreviousCoh),
          (∀ n : ℕ, adj.unit.app K ≫ Φ.inv ≫ RΓ.map a ≫ RΓ.map (Pi.π Y n) =
            RΓ.map (eE.inv ≫ DerivedCategory.Q.map
              (CochainComplex.mappingCone.inr
                (smulComplex X (baseSmul X ρ f) CE ^ (n + 1)).asHom))) ∧
          (∀ n : ℕ,
            cokernel.π (PrincipalTorsionTower.powerMultiplication A (H p) (f ^ (n + 1))) ≫
                termIn.app ⟨n⟩ =
              (HH p).map (RΓ.map (eE.inv ≫ DerivedCategory.Q.map
                (CochainComplex.mappingCone.inr
                  (smulComplex X (baseSmul X ρ f) CE ^ (n + 1)).asHom)))) ∧
          (∀ n : ℕ,
            termOut.app ⟨n⟩ ≫
                kernel.ι (PrincipalTorsionTower.powerMultiplication A (H (p + 1)) (f ^ (n + 1))) =
              (HH 0).homologySequenceδ (koszulTriangle n) p (p + 1) (by omega) ≫
                (HH (p + 1)).map (RΓ.map eE.hom)) ∧
          (∀ n : ℕ,
            previousOut.app ⟨n⟩ ≫
                kernel.ι (PrincipalTorsionTower.powerMultiplication A (H p) (f ^ (n + 1))) =
              (HH 0).homologySequenceδ (koszulTriangle n) (p - 1) p (by omega) ≫
                (HH p).map (RΓ.map eE.hom)) ∧
          (∀ n : ℕ, topIn ≫ limit.π (cohTower p) ⟨n⟩ =
            limit.π (CompletionSequences.powerQuotientSystem A (H p) f) ⟨n⟩ ≫ termIn.app ⟨n⟩) ∧
          (∀ n : ℕ, topOut ≫
              limit.π (PrincipalTorsionTower.powerTorsionSystem A (H (p + 1)) f) ⟨n⟩ =
            limit.π (cohTower p) ⟨n⟩ ≫ termOut.app ⟨n⟩) ∧
          IsIso productComparison ∧
          (productComparison ≫
              cokernel.π (CompletionSequences.moduleDifference A (cohTower (p - 1))) ≫ columnIn =
            (HH 0).homologySequenceδ limitTriangle (p - 1) p (by omega)) ∧
          (∀ n : ℕ, columnOut ≫ limit.π (cohTower p) ⟨n⟩ =
            (HH p).map (RΓ.map a ≫ RΓ.map (Pi.π Y n))) ∧
          (cokernel.π (CompletionSequences.moduleDifference A (cohTower (p - 1))) ≫ bottom.inv =
            (Pi.lift fun n : ℕ ↦
              Pi.π (fun n : ℕ ↦ (cohTower (p - 1)).obj ⟨n⟩) n ≫ previousOut.app ⟨n⟩) ≫
              cokernel.π (CompletionSequences.moduleDifference A
                (PrincipalTorsionTower.powerTorsionSystem A (H p) f))) ∧
          (ShortComplex.mk topIn topOut htop).ShortExact ∧
          (ShortComplex.mk middleIn middleOut hmiddle).ShortExact ∧
          (ShortComplex.mk leftIn leftOut hleft).ShortExact ∧
          (ShortComplex.mk columnIn columnOut hcolumn).ShortExact ∧
          middleIn ≫ columnOut = leftOut ≫ topIn ∧
          middleOut = columnOut ≫ topOut ∧
          bottom.hom ≫ columnIn = leftIn ≫ middleIn
```

## Tag 0H3D, a lemma

[Tag 0H3D](https://stacks.math.columbia.edu/tag/0H3D) in the Stacks Project.

**`proIso_Ksys_Csys`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/ProIsomorphismOfKernelSystems.lean, line 640](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/ProIsomorphismOfKernelSystems.lean#L640).

> If `M[f^n]` stabilizes, then the inverse systems `(K_n)` and `(C_n)` are pro-isomorphic in
> `D(A)`.

```lean
theorem proIso_Ksys_Csys {M : C} (f : M ⟶ M) [HasDerivedCategory C] (hf : Stabilizes f) :
    Nonempty (InverseSequence.ProIso (Ksys f) (Csys f))
```

## Tag 0H3E, an example

[Tag 0H3E](https://stacks.math.columbia.edu/tag/0H3E) in the Stacks Project.

**`Stacks.Cohomology.PrincipalFormalFunctions.nonempty_iso_derivedSections_quotientTower_derivedCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalFormalFunctionsDiagram.lean, line 1180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalFormalFunctionsDiagram.lean#L1180). The attribute's comment: “the identification RΓ(X, ℱ^) = RΓ(X, ℱ)^∧ and the resulting Hᵖ(X, ℱ^) = Hᵖ(RΓ(X, ℱ)^∧), on a ringed space, with derived f-adic completion presented as in Stacks 0BKG by an arbitrary left adjoint to the inclusion of the derived-complete objects; also derived completeness of RΓ(X, ℱ^)”.

> **Clause (7) of [Stacks, Tag 0H3E]: `RΓ(X, ℱ^) = RΓ(X, ℱ)^∧` on a ringed space.** Let
> `(X, 𝒪_X)` be a ringed space, let `ρ : A ⟶ Γ(X, 𝒪_X)` be a homomorphism from a commutative ring
> `A`, let `f ∈ A` and let `ℱ` be a sheaf of `𝒪_X`-modules whose `f`-power torsion stabilizes.  Let
> `ℱ^` be a derived limit of the tower of honest quotients `ℱ/f^(n+1)ℱ`.  Then
>
> `RΓ(X, ℱ^) ≅ RΓ(X, ℱ)^∧`,
>
> the object `RΓ(X, ℱ^)` is derived complete for `(f)`, and for every `p` its `p`-th cohomology
> module is that of `RΓ(X, ℱ)^∧` — the identification `Hᵖ(X, ℱ^) = Hᵖ(RΓ(X, ℱ)^∧)` the diagram of
> the source rests on.
>
> This is the displayed equality of [Stacks, Tag 0BLD] on an arbitrary ringed space: the Koszul
> form of it is `nonempty_iso_derivedSections_koszulTower_derivedCompletion`, and the
> pro-isomorphism of [Stacks, Tag 0H3D] replaces the Koszul tower by the quotient tower.  No
> quasi-coherence is needed, only stabilization of the `f`-power torsion.

```lean
theorem nonempty_iso_derivedSections_quotientTower_derivedCompletion
    (ℱ : SheafOfModules.{u} (structureSheafRing X))
    (hstab : Stabilizes ((baseSmul X ρ f).asHom.app ℱ))
    (Fhat : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (hFhat : IsDerivedLimit (Csys ((baseSmul X ρ f).asHom.app ℱ)) Fhat) :
    let P : ObjectProperty (DerivedCategory (ModuleCat.{u} A)) :=
      fun L ↦ IsDerivedComplete (Ideal.span {f}) L
    ∀ (completion : DerivedCategory (ModuleCat.{u} A) ⥤ P.FullSubcategory)
      (_ : completion ⊣ P.ι),
      let completed := completion ⋙ P.ι
      let sglF :=
        (DerivedCategory.singleFunctor (SheafOfModules.{u} (structureSheafRing X)) 0).obj ℱ
      Nonempty ((derivedSectionsOver X ρ).obj Fhat ≅
          completed.obj ((derivedSectionsOver X ρ).obj sglF)) ∧
        IsDerivedComplete (Ideal.span {f}) ((derivedSectionsOver X ρ).obj Fhat) ∧
        ∀ p : ℤ, Nonempty
          ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) p).obj
              ((derivedSectionsOver X ρ).obj Fhat) ≅
            (DerivedCategory.homologyFunctor (ModuleCat.{u} A) p).obj
              (completed.obj ((derivedSectionsOver X ρ).obj sglF)))
```

**`Stacks.Cohomology.PrincipalFormalFunctions.exists_formalFunctionsDiagram_quotientTower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalFormalFunctionsDiagram.lean, line 1248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/PrincipalFormalFunctionsDiagram.lean#L1248). The attribute's comment: “the whole diagram for the quotient tower ℱ/fⁿℱ: the top row, the middle row, the left column, the middle column, the bottom isomorphism, the three commutativities, and the identification RΓ(X, ℱ^) = RΓ(X, ℱ)^∧; derived f-adic completion presented as in Stacks 0BKG by an arbitrary left adjoint to the inclusion of the derived-complete objects”.

> **Formal functions for a principal ideal along the quotient tower: the whole diagram of
> [Stacks, Tag 0H3E].** Let `(X, 𝒪_X)` be a ringed space, let `ρ : A ⟶ Γ(X, 𝒪_X)` be a homomorphism
> from a commutative ring `A`, let `f ∈ A`, let `ℱ` be a sheaf of `𝒪_X`-modules whose `f`-power
> torsion stabilizes, and let `ℱ^` be a derived limit of the tower of quotients `ℱ/f^(n+1)ℱ`.  Then
> for every `p` the commutative diagram of the source exists, with exact rows and columns:
>
> * the top row `0 ⟶ Hᵖ(X, ℱ)^ ⟶ lim Hᵖ(X, ℱ/fⁿℱ) ⟶ T_f(Hᵖ⁺¹(X, ℱ)) ⟶ 0`;
> * the middle row `0 ⟶ H⁰(Hᵖ(X, ℱ)^∧) ⟶ Hᵖ(X, ℱ^) ⟶ T_f(Hᵖ⁺¹(X, ℱ)) ⟶ 0`;
> * the left column `0 ⟶ R¹lim Hᵖ(X, ℱ)[fⁿ] ⟶ H⁰(Hᵖ(X, ℱ)^∧) ⟶ Hᵖ(X, ℱ)^ ⟶ 0`;
> * the middle column `0 ⟶ R¹lim Hᵖ⁻¹(X, ℱ/fⁿℱ) ⟶ Hᵖ(X, ℱ^) ⟶ lim Hᵖ(X, ℱ/fⁿℱ) ⟶ 0`;
> * the bottom comparison `R¹lim Hᵖ(X, ℱ)[fⁿ] ≅ R¹lim Hᵖ⁻¹(X, ℱ/fⁿℱ)`;
>
> the three commutativities that make the nine terms a diagram, and the identification
> `RΓ(X, ℱ^) ≅ RΓ(X, ℱ)^∧`.  As in [Stacks, Tag 0H32], `S` is the data of the two completion
> sequences of [Stacks, Tag 0BKG] for `RΓ(X, ℱ)`, so the middle row and the left column are that
> source's own maps, and `γ` is the identification of `Hᵖ(X, ℱ^)` with `Hᵖ(RΓ(X, ℱ)^∧)`.
>
> This is `exists_formalFunctionsDiagram_principalKoszulTower` with the `f`-power Koszul tower
> replaced by the tower of honest quotients, the replacement being licensed by the pro-isomorphism
> of [Stacks, Tag 0H3D].  Only the two tower-dependent terms and `Hᵖ(X, ℱ^)` change, and they
> change by isomorphism: a pro-isomorphism shifts the index, so the limit and the first derived
> limit of the two cohomology towers agree as modules while the individual projections do not
> correspond, which is why the per-level normalizations of the Koszul form are not asserted here.
> The middle column *is* available with its maps normalized directly by the Milnor triangle of the
> quotient tower, as `Stacks.Cohomology.QuotientTowerFormalFunctions`
> `.exists_shortExact_homology_derivedSections_quotientTower`.

```lean
theorem exists_formalFunctionsDiagram_quotientTower
    (ℱ : SheafOfModules.{u} (structureSheafRing X))
    (hstab : Stabilizes ((baseSmul X ρ f).asHom.app ℱ))
    (Fhat : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (hFhat : IsDerivedLimit (Csys ((baseSmul X ρ f).asHom.app ℱ)) Fhat)
    (p : ℤ) :
    let P : ObjectProperty (DerivedCategory (ModuleCat.{u} A)) :=
      fun L ↦ IsDerivedComplete (Ideal.span {f}) L
    ∀ (completion : DerivedCategory (ModuleCat.{u} A) ⥤ P.FullSubcategory)
      (adj : completion ⊣ P.ι),
      let completed := completion ⋙ P.ι
      let HH (q : ℤ) := DerivedCategory.homologyFunctor (ModuleCat.{u} A) q
      let sglF :=
        (DerivedCategory.singleFunctor (SheafOfModules.{u} (structureSheafRing X)) 0).obj ℱ
      let K := (derivedSectionsOver X ρ).obj sglF
      let H (q : ℤ) := (HH q).obj K
      let quotTower (q : ℤ) :=
        (Csys ((baseSmul X ρ f).asHom.app ℱ) ⋙ derivedSectionsOver X ρ) ⋙ HH q
      let ordinaryCompletion := limit (CompletionSequences.powerQuotientSystem A (H p) f)
      let limitQuot := limit (quotTower p)
      let tate := CompletionSequences.adicTateModule A (H (p + 1)) f
      let H0CompletedHp := (HH 0).obj
        (completed.obj ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (H p)))
      let HpFhat := (HH p).obj ((derivedSectionsOver X ρ).obj Fhat)
      let R1Torsion := CompletionSequences.firstDerivedLimit A
        (PrincipalTorsionTower.powerTorsionSystem A (H p) f)
      let R1PreviousQuot := CompletionSequences.firstDerivedLimit A (quotTower (p - 1))
      ∃ (S : CompletionSequences.PrincipalCompletionSequences A f completed adj.unit)
        (γ : HpFhat ≅ (HH p).obj (completed.obj K)),
        let middleIn : H0CompletedHp ⟶ HpFhat := (S.truncation K p).inclusion S.shift ≫ γ.inv
        let middleOut : HpFhat ⟶ tate := γ.hom ≫ (S.truncation K p).projection f S.shift
          (S.moduleSequence (H (p + 1))).tateIso
        let leftIn : R1Torsion ⟶ H0CompletedHp := (S.moduleSequence (H p)).inclusion
        let leftOut : H0CompletedHp ⟶ ordinaryCompletion := (S.moduleSequence (H p)).projection
        ∃ (topIn : ordinaryCompletion ⟶ limitQuot)
          (topOut : limitQuot ⟶ tate)
          (htop : topIn ≫ topOut = 0)
          (hmiddle : middleIn ≫ middleOut = 0)
          (hleft : leftIn ≫ leftOut = 0)
          (columnIn : R1PreviousQuot ⟶ HpFhat)
          (columnOut : HpFhat ⟶ limitQuot)
          (hcolumn : columnIn ≫ columnOut = 0)
          (bottom : R1Torsion ≅ R1PreviousQuot),
          (ShortComplex.mk topIn topOut htop).ShortExact ∧
          (ShortComplex.mk middleIn middleOut hmiddle).ShortExact ∧
          (ShortComplex.mk leftIn leftOut hleft).ShortExact ∧
          (ShortComplex.mk columnIn columnOut hcolumn).ShortExact ∧
          middleIn ≫ columnOut = leftOut ≫ topIn ∧
          middleOut = columnOut ≫ topOut ∧
          bottom.hom ≫ columnIn = leftIn ≫ middleIn ∧
          Nonempty ((derivedSectionsOver X ρ).obj Fhat ≅ completed.obj K)
```

**`Stacks.Cohomology.QuotientTowerFormalFunctions.exists_shortExact_homology_derivedSections_quotientTower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/QuotientTowerFormalFunctions.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/QuotientTowerFormalFunctions.lean#L354). The attribute's comment: “the middle column of the diagram, transported to the quotient tower ℱ/fⁿℱ by the pro-isomorphism of Tag 0H3D; its two maps normalized by the Milnor triangle of the quotient tower itself”.

> **Formal functions for a principal ideal along the quotient tower: the middle column.**
> Let `(X, 𝒪_X)` be a ringed space, let `ρ : A ⟶ Γ(X, 𝒪_X)` be a homomorphism from a commutative
> ring `A`, let `f ∈ A` and let `ℱ` be a sheaf of `𝒪_X`-modules whose `f`-power torsion stabilizes.
> Let `ℱ^` be a derived limit of the tower of quotients `ℱ/f^(n+1)ℱ` and let `E^` be a derived limit
> of the `f`-power Koszul tower. Then `E^ ≅ ℱ^`, and for every `p` the cohomology of `RΓ(X, ℱ^)`
> over `A` sits in a short exact sequence
>
> `0 ⟶ R¹lim Hᵖ⁻¹(X, ℱ/f^(n+1)ℱ) ⟶ Hᵖ(X, ℱ^) ⟶ lim Hᵖ(X, ℱ/f^(n+1)ℱ) ⟶ 0`,
>
> whose inclusion descends the connecting morphism of the Milnor triangle and whose projection is
> characterized by the limit projections, and whose outer terms are isomorphic to the outer terms of
> the corresponding sequence for the Koszul tower.

```lean
theorem exists_shortExact_homology_derivedSections_quotientTower (f : A)
    (ℱ : SheafOfModules.{u} (structureSheafRing X))
    (hstab : Stabilizes ((baseSmul X ρ f).asHom.app ℱ))
    (Fhat Ehat : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (hFhat : IsDerivedLimit (Csys ((baseSmul X ρ f).asHom.app ℱ)) Fhat)
    (hEhat : IsDerivedLimit (Ksys ((baseSmul X ρ f).asHom.app ℱ)) Ehat) :
    let F : ℕᵒᵖ ⥤ DerivedCategory (ModuleCat.{u} A) :=
      Csys ((baseSmul X ρ f).asHom.app ℱ) ⋙ derivedSectionsOver X ρ
    let G : ℕᵒᵖ ⥤ DerivedCategory (ModuleCat.{u} A) :=
      Ksys ((baseSmul X ρ f).asHom.app ℱ) ⋙ derivedSectionsOver X ρ
    let Y : ℕ → DerivedCategory (ModuleCat.{u} A) := fun n ↦ F.obj (op n)
    let d : (∏ᶜ Y) ⟶ ∏ᶜ Y := Pi.lift fun n : ℕ ↦
      Pi.π Y n - Pi.π Y (n + 1) ≫ F.map (homOfLE (Nat.le_succ n)).op
    Nonempty (Ehat ≅ Fhat) ∧
      ∃ (a : (derivedSectionsOver X ρ).obj Fhat ⟶ ∏ᶜ Y)
        (b : (∏ᶜ Y) ⟶ ((derivedSectionsOver X ρ).obj Fhat)⟦(1 : ℤ)⟧),
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
              (i : cokernel δ ⟶ H.obj ((derivedSectionsOver X ρ).obj Fhat))
              (q : H.obj ((derivedSectionsOver X ρ).obj Fhat) ⟶ limit homologySystem)
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

- [Section 20.39, Tag 0H3B](https://stacks.math.columbia.edu/tag/0H3B)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
