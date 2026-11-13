---
declaration: section
origin: cited
lean: NaiveCotangent.naiveCotangent_baseChange_truncGE_comparison_isIso, NaiveCotangent.naiveCotangentComplex_baseChange_homology, NaiveCotangent.naiveCotangentComplex_quasiIso_baseChange_of_flat, NaiveCotangent.naiveCotangentComplex_isPerfect_and_hasTorAmplitude, NaiveCotangent.finite_projective_ker_naiveCotangent_baseChange_homology_negOne
statement: formalized
proof: formalized
---

# 15.87 The naive cotangent complex

Section 15.87 of the Stacks Project, [Tag 0FUX](https://stacks.math.columbia.edu/tag/0FUX). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FUY, a lemma

[Tag 0FUY](https://stacks.math.columbia.edu/tag/0FUY) in the Stacks Project.

**`NaiveCotangent.naiveCotangent_baseChange_truncGE_comparison_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/DerivedBaseChange.lean, line 556](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/DerivedBaseChange.lean#L556).

> **Stacks 0FUY.** For `R → S → S'`, the canonical comparison from derived to termwise base
> change of the naive cotangent complex induces an isomorphism after truncation in degrees at
> least `-1`. This holds for the canonical presentation and for every polynomial presentation of
> `S` over `R`.

```lean
public theorem naiveCotangent_baseChange_truncGE_comparison_isIso
    {R : Type uR} {S : Type uS} {S' : Type uS'}
    [CommRing R] [CommRing S] [CommRing S'] [Algebra R S] [Algebra S S'] :
    letI : Functor.IsLeftAdjoint
        (ModuleCat.extendScalars.{uS, uS', max uS' (max uR uS w)} (algebraMap S S')) :=
      ModuleCat.instIsLeftAdjointExtendScalars.{uS, uS', max uR uS w} (algebraMap S S')
    ∀ (derivedBaseChange : DerivedCategory (ModuleCat.{max uS' (max uR uS w)} S) ⥤
        DerivedCategory (ModuleCat.{max uS' (max uR uS w)} S'))
      (comparison : DerivedCategory.Q ⋙ derivedBaseChange ⟶
        (ModuleCat.extendScalars.{uS, uS', max uS' (max uR uS w)}
          (algebraMap S S')).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
      [derivedBaseChange.IsLeftDerivedFunctor comparison
        (HomologicalComplex.quasiIso (ModuleCat.{max uS' (max uR uS w)} S)
          (ComplexShape.up ℤ))],
    let canonicalMapInducesIso
        (L : CochainComplex (ModuleCat.{max uS' (max uR uS w)} S) ℤ) : Prop :=
      ∃ f : ((DerivedCategory.TStructure.t
                (C := ModuleCat.{max uS' (max uR uS w)} S')).truncGE (-1)).obj
              (derivedBaseChange.obj (DerivedCategory.Q.obj L)) ⟶
            DerivedCategory.Q.obj
              (((ModuleCat.extendScalars.{uS, uS', max uS' (max uR uS w)}
                  (algebraMap S S')).mapHomologicalComplex
                (ComplexShape.up ℤ)).obj L),
        comparison.app L =
          ((DerivedCategory.TStructure.t
              (C := ModuleCat.{max uS' (max uR uS w)} S')).truncGEπ (-1)).app
            (derivedBaseChange.obj (DerivedCategory.Q.obj L)) ≫ f ∧
          IsIso f
    canonicalMapInducesIso
        (CochainComplex.mappingCone
          ((CochainComplex.singleFunctor (ModuleCat.{max uS' (max uR uS w)} S) 0).map
            (ModuleCat.ofHom
              (ULift.moduleEquiv.{uS, max uR uS,
                  max uS' (max uR uS w)}.symm.toLinearMap.comp
                ((NaiveCotangent.NL (NaiveCotangent.canonicalGenerators R S)).d.comp
                  ULift.moduleEquiv.{uS, max uR uS,
                    max uS' (max uR uS w)}.toLinearMap))))) ∧
      ∀ (ι : Type w) (P : Algebra.Generators R S ι),
        canonicalMapInducesIso
          (CochainComplex.mappingCone
            ((CochainComplex.singleFunctor (ModuleCat.{max uS' (max uR uS w)} S) 0).map
              (ModuleCat.ofHom
                (ULift.moduleEquiv.{uS, max (max uR uS) w,
                    max uS' (max uR uS w)}.symm.toLinearMap.comp
                  ((NaiveCotangent.NL P).d.comp
                    ULift.moduleEquiv.{uS, max uR w,
                      max uS' (max uR uS w)}.toLinearMap)))))
```

## Tag 0FUZ, a lemma

[Tag 0FUZ](https://stacks.math.columbia.edu/tag/0FUZ) in the Stacks Project.

**`NaiveCotangent.naiveCotangentComplex_baseChange_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/DerivedBaseChange.lean, line 481](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/DerivedBaseChange.lean#L481).

> **Stacks 0FUZ.** Formation of the naive cotangent complex commutes with arbitrary base change
> on `H⁰` and is surjective on `H⁻¹`, both for a chosen polynomial presentation and for the
> canonical one.

```lean
public theorem naiveCotangentComplex_baseChange_homology
    {R : Type u} {S : Type v} {T : Type w} [CommRing R] [CommRing S] [CommRing T]
    [Algebra R S] [Algebra R T] {ι : Type t} (P : Algebra.Generators R S ι) :
    let S' := T ⊗[R] S
    letI : Algebra S S' := Algebra.TensorProduct.rightAlgebra
    let P' := P.baseChange T
    let h := (P.baseChangeFromBaseChange T).comp (P.toExtension.toBaseChange T)
    let d := AlgebraTensorModule.lTensor S' S' P.toExtension.cotangentComplex
    let f₁ := (Algebra.Extension.Cotangent.map h).liftBaseChange S'
    let f₀ := (Algebra.Extension.CotangentSpace.map h).liftBaseChange S'
    P'.toExtension.cotangentComplex ∘ₗ f₁ = f₀ ∘ₗ d ∧
      (∀ y, ∃ x, y - f₀ x ∈ LinearMap.range P'.toExtension.cotangentComplex) ∧
      (∀ x, f₀ x ∈ LinearMap.range P'.toExtension.cotangentComplex ↔
        x ∈ LinearMap.range d) ∧
      (∀ y, P'.toExtension.cotangentComplex y = 0 →
        ∃ x, d x = 0 ∧ f₁ x = y) ∧
      let Pc := Algebra.Generators.self R S
      let Pc' := Algebra.Generators.self T S'
      let hc := (Pc.defaultHom Pc').toExtensionHom
      let dc := AlgebraTensorModule.lTensor S' S' Pc.toExtension.cotangentComplex
      let fc₁ := (Algebra.Extension.Cotangent.map hc).liftBaseChange S'
      let fc₀ := (Algebra.Extension.CotangentSpace.map hc).liftBaseChange S'
      Pc'.toExtension.cotangentComplex ∘ₗ fc₁ = fc₀ ∘ₗ dc ∧
        (∀ y, ∃ x, y - fc₀ x ∈ LinearMap.range Pc'.toExtension.cotangentComplex) ∧
        (∀ x, fc₀ x ∈ LinearMap.range Pc'.toExtension.cotangentComplex ↔
          x ∈ LinearMap.range dc) ∧
        ∀ y, Pc'.toExtension.cotangentComplex y = 0 →
          ∃ x, dc x = 0 ∧ fc₁ x = y
```

## Tag 0FJU, a lemma

[Tag 0FJU](https://stacks.math.columbia.edu/tag/0FJU) in the Stacks Project.

**`NaiveCotangent.naiveCotangentComplex_quasiIso_baseChange_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/Cocartesian.lean, line 829](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/Cocartesian.lean#L829).

> **Stacks 0FJU.** Let `A → B` be flat, let `A → A'` be arbitrary and let `B' = A' ⊗[A] B` be
> the pushout, so that the square with corners `A, A', B, B'` is cocartesian. Then the canonical
> map `NL_{B/A} ⊗_B B' → NL_{B'/A'}` is a quasi-isomorphism, and if in addition `NL_{B/A}` has Tor
> amplitude in `[-1, 0]` then the derived base-change map `NL_{B/A} ⊗_B^L B' → NL_{B'/A'}` is a
> quasi-isomorphism too.
>
> The naive cotangent complexes are the two-term complexes `HomologicalComplex.double` of the
> canonical presentations, in cohomological degrees `-1` and `0`, with their modules and rings
> lifted to one universe. The map of the first assertion is the displayed chain map `g`; the map of
> the second is that chain map composed with the comparison from derived to ordinary extension of
> scalars, which is what makes the composite the derived base-change map.

```lean
public theorem naiveCotangentComplex_quasiIso_baseChange_of_flat
    {A : Type uA} {B : Type uB} {A' : Type uC}
    [CommRing A] [CommRing B] [CommRing A'] [Algebra A B] [Algebra A A'] [Module.Flat A B] :
    let B' := A' ⊗[A] B
    letI : Algebra B B' := Algebra.TensorProduct.rightAlgebra
    let P := Algebra.Generators.self A B
    let P' := Algebra.Generators.self A' B'
    let h := (P.defaultHom P').toExtensionHom
    let X₁ : ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B) :=
      ModuleCat.of (ULift.{max uA uB uC} B)
        (ULift.{max uA uB uC} P.toExtension.Cotangent)
    let X₀ : ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B) :=
      ModuleCat.of (ULift.{max uA uB uC} B)
        (ULift.{max uA uB uC} P.toExtension.CotangentSpace)
    let X₁' : ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B') :=
      ModuleCat.of (ULift.{max uA uB uC} B')
        (ULift.{max uA uB uC} P'.toExtension.Cotangent)
    let X₀' : ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B') :=
      ModuleCat.of (ULift.{max uA uB uC} B')
        (ULift.{max uA uB uC} P'.toExtension.CotangentSpace)
    let d : X₁ ⟶ X₀ := ModuleCat.ofHom {
      toFun := fun x => ULift.up (P.toExtension.cotangentComplex x.down)
      map_add' := by
        intro x y
        exact congrArg ULift.up (P.toExtension.cotangentComplex.map_add x.down y.down)
      map_smul' := by
        intro r x
        exact congrArg ULift.up (P.toExtension.cotangentComplex.map_smul r.down x.down) }
    let d' : X₁' ⟶ X₀' := ModuleCat.ofHom {
      toFun := fun x => ULift.up (P'.toExtension.cotangentComplex x.down)
      map_add' := by
        intro x y
        exact congrArg ULift.up (P'.toExtension.cotangentComplex.map_add x.down y.down)
      map_smul' := by
        intro r x
        exact congrArg ULift.up (P'.toExtension.cotangentComplex.map_smul r.down x.down) }
    let hd : (ComplexShape.up ℤ).Rel (-1) 0 := by decide
    let hne : (-1 : ℤ) ≠ 0 := by decide
    let K : CochainComplex (ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B)) ℤ :=
      HomologicalComplex.double d hd
    let K' : CochainComplex (ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B')) ℤ :=
      HomologicalComplex.double d' hd
    let E : ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B) ⥤
        ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B') :=
      ModuleCat.extendScalars.{max uA uB uC, max uA uB uC, max uA uB uC}
        ((algebraMap B B').ulift)
    let f₁ : E.obj X₁ ⟶ X₁' :=
      ModuleCat.ExtendRestrictScalarsAdj.HomEquiv.fromExtendScalars ((algebraMap B B').ulift)
        (ModuleCat.ofHom (Y := (ModuleCat.restrictScalars ((algebraMap B B').ulift)).obj X₁')
          { toFun := fun x => ULift.up (Algebra.Extension.Cotangent.map h x.down)
            map_add' := by
              intro x y
              exact congrArg ULift.up ((Algebra.Extension.Cotangent.map h).map_add x.down y.down)
            map_smul' := by
              intro r x
              change ULift.up _ = ULift.up _
              congr 1
              change (Algebra.Extension.Cotangent.map h) (r.down • x.down) =
                (algebraMap B B' r.down) • (Algebra.Extension.Cotangent.map h x.down)
              exact (Algebra.Extension.Cotangent.map h).map_smul r.down x.down })
    let f₀ : E.obj X₀ ⟶ X₀' :=
      ModuleCat.ExtendRestrictScalarsAdj.HomEquiv.fromExtendScalars ((algebraMap B B').ulift)
        (ModuleCat.ofHom (Y := (ModuleCat.restrictScalars ((algebraMap B B').ulift)).obj X₀')
          { toFun := fun x => ULift.up (Algebra.Extension.CotangentSpace.map h x.down)
            map_add' := by
              intro x y
              exact congrArg ULift.up
                ((Algebra.Extension.CotangentSpace.map h).map_add x.down y.down)
            map_smul' := by
              intro r x
              change ULift.up _ = ULift.up _
              congr 1
              change (Algebra.Extension.CotangentSpace.map h) (r.down • x.down) =
                (algebraMap B B' r.down) • (Algebra.Extension.CotangentSpace.map h x.down)
              rw [IsScalarTower.algebraMap_smul]
              exact (Algebra.Extension.CotangentSpace.map h).map_smul r.down x.down })
    ∀ (derivedTensor :
        DerivedCategory (ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B)) ⥤
          DerivedCategory (ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B)) ⥤
            DerivedCategory (ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B)))
      (tensorComparison : ∀ M : ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B),
        DerivedCategory.Q ⋙ derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor
              (ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B)) 0).obj M) ⟶
          (StacksDraft.TorAmplitude.tensorModuleRight M).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
      (tensorIsLeftDerived : ∀ M : ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B),
        (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor
            (ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B))
            0).obj M)).IsLeftDerivedFunctor
          (tensorComparison M)
          (HomologicalComplex.quasiIso
            (ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B)) (ComplexShape.up ℤ)))
      (tensorCommShift : ∀ M : ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B),
        (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor
            (ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B)) 0).obj M)).CommShift ℤ)
      (tensorTriangulated : ∀ M : ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B),
        letI := tensorCommShift M
        (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor
            (ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B)) 0).obj M)).IsTriangulated)
      (derivedExtension :
        DerivedCategory (ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B)) ⥤
          DerivedCategory (ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B')))
      (extensionComparison :
        DerivedCategory.Q ⋙ derivedExtension ⟶
          E.mapHomologicalComplex (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
      (_extensionIsLeftDerived : derivedExtension.IsLeftDerivedFunctor extensionComparison
        (HomologicalComplex.quasiIso
          (ModuleCat.{max uA uB uC} (ULift.{max uA uB uC} B)) (ComplexShape.up ℤ))),
    ∃ g : (E.mapHomologicalComplex (ComplexShape.up ℤ)).obj K ⟶ K',
      g.f (-1) =
          E.map (HomologicalComplex.doubleXIso₀ d hd).hom ≫ f₁ ≫
            (HomologicalComplex.doubleXIso₀ d' hd).inv ∧
        g.f 0 =
          E.map (HomologicalComplex.doubleXIso₁ d hd hne).hom ≫ f₀ ≫
            (HomologicalComplex.doubleXIso₁ d' hd hne).inv ∧
        QuasiIso g ∧
        (StacksDraft.TorAmplitude.HasTorAmplitude derivedTensor tensorComparison
            tensorIsLeftDerived (DerivedCategory.Q.obj K) (-1) 0 →
          IsIso (extensionComparison.app K ≫ DerivedCategory.Q.map g))
```

## Tag 0FV0, a lemma

[Tag 0FV0](https://stacks.math.columbia.edu/tag/0FV0) in the Stacks Project.

**`NaiveCotangent.naiveCotangentComplex_isPerfect_and_hasTorAmplitude`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/NaiveCotangentPerfect.lean, line 415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteIntersection/NaiveCotangentPerfect.lean#L415). References: SGA 6 0 (4.4), “affine case”.

> The naive cotangent complex of a local complete intersection is perfect and
> has Tor-amplitude in `[-1, 0]`.

```lean
public theorem naiveCotangentComplex_isPerfect_and_hasTorAmplitude
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    (h : RingHom.IsLocalCompleteIntersection (algebraMap A B))
    (derivedTensor :
      DerivedCategory (ModuleCat.{max u v} B) ⥤
        DerivedCategory (ModuleCat.{max u v} B) ⥤
          DerivedCategory (ModuleCat.{max u v} B))
    (comparison : ∀ M : ModuleCat.{max u v} B,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{max u v} B) 0).obj M) ⟶
        (tensorModuleRight M).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ M : ModuleCat.{max u v} B,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{max u v} B) 0).obj M)).IsLeftDerivedFunctor
        (comparison M)
        (HomologicalComplex.quasiIso (ModuleCat.{max u v} B) (ComplexShape.up ℤ))) :
    StacksDraft.Perfect.IsPerfect (naiveCotangentObject A B) ∧
      HasTorAmplitude derivedTensor comparison isLeftDerived
        (naiveCotangentObject A B) (-1) 0
```

## Tag 0FV1, a lemma

[Tag 0FV1](https://stacks.math.columbia.edu/tag/0FV1) in the Stacks Project.

**`NaiveCotangent.finite_projective_ker_naiveCotangent_baseChange_homology_negOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/CocartesianKernel.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NaiveCotangent/CocartesianKernel.lean#L294).

> **Stacks 0FV1.** In a pushout square of rings, if both parallel maps are local complete
> intersections, then the kernel of the base-change map on degree `-1` homology of the naive
> cotangent complex is a finite projective module over the pushout.

```lean
public theorem finite_projective_ker_naiveCotangent_baseChange_homology_negOne
    {A : Type u} {B : Type v} {A' : Type w}
    [CommRing A] [CommRing B] [CommRing A'] [Algebra A B] [Algebra A A']
    (h : RingHom.IsLocalCompleteIntersection (algebraMap A B)) :
    let B' := A' ⊗[A] B
    letI : Algebra B B' := Algebra.TensorProduct.rightAlgebra
    RingHom.IsLocalCompleteIntersection (algebraMap A' B') →
      let P := Algebra.Generators.self A B
      let P' := Algebra.Generators.self A' B'
      let comparison := (P.defaultHom P').toExtensionHom
      let d := AlgebraTensorModule.lTensor B' B' P.toExtension.cotangentComplex
      let f := (Algebra.Extension.Cotangent.map comparison).liftBaseChange B'
      Module.Finite B' (LinearMap.ker (f.domRestrict (LinearMap.ker d))) ∧
        Module.Projective B' (LinearMap.ker (f.domRestrict (LinearMap.ker d)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.87, Tag 0FUX](https://stacks.math.columbia.edu/tag/0FUX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
