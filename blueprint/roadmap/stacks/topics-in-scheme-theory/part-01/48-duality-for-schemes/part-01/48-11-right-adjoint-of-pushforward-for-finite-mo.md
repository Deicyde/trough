---
declaration: section
origin: cited
lean: AlgebraicGeometry.sections_rightAdjoint_restrictionToStructureSheaf, RingedSpaceModuleAdjunction.restrictScalarsHomAdjunction, AlgebraicGeometry.derivedRestriction_adj_derivedHomSheaf, AlgebraicGeometry.derivedHomSheaf_comp_derivedRestriction_iso, AlgebraicGeometry.derivedHomSheaf_finite_pseudoCoherent, AlgebraicGeometry.pseudoCoherent_of_isFinite_of_isLocallyNoetherian, AlgebraicGeometry.derivedCategoryBPlus_derivedSheafHom_pushforwardStructureSheaf, AlgebraicGeometry.derivedCategoryBPlus_derivedSheafHom_of_pseudoCoherent
statement: formalized
proof: formalized
---

# 48.11 Right adjoint of pushforward for finite morphisms

Section 48.11 of the Stacks Project, [Tag 0AWZ](https://stacks.math.columbia.edu/tag/0AWZ). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BUZ, a lemma

[Tag 0BUZ](https://stacks.math.columbia.edu/tag/0BUZ) in the Stacks Project.

**`AlgebraicGeometry.sections_rightAdjoint_restrictionToStructureSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/AffineSections.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/AffineSections.lean#L139). The attribute's comment: “sections on an affine open”.

> **Stacks Project, Tag 0BUZ (sections on an affine open).** If `f : Y ⟶ X` is
> affine and `U ⊆ X` is affine, sections over `U` of the internal-Hom right adjoint
> are the `Γ(X,U)`-linear maps from `Γ(Y,f⁻¹U)` to the sections of `F` over `U`.

```lean
public noncomputable def sections_rightAdjoint_restrictionToStructureSheaf
    {X Y : Scheme.{u}} (f : Y ⟶ X) [IsAffineHom f] (F : X.Modules)
    (U : X.Opens) (hU : IsAffineOpen U) :
    letI : Algebra Γ(X, U) Γ(Y, f ⁻¹ᵁ U) := (f.app U).hom.toAlgebra
    (((RingedSpaceModuleAdjunction.homSheaf f.toRingCatSheafHom).obj F).val.obj
        (op U) : Type u) ≃+
      (ModuleCat.of Γ(X, U) Γ(Y, f ⁻¹ᵁ U) ⟶ ModuleCat.of Γ(X, U) Γ(F, U))
```

Declarations registered for the tag:

- [`RingedSpaceModuleAdjunction.restrictScalarsHomAdjunction`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Module/HomSheaf.lean#L438), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/AffineSections.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/AffineSections.lean#L90) (StacksFrontier): “the adjunction”.

## Tag 0BV0, a lemma

[Tag 0BV0](https://stacks.math.columbia.edu/tag/0BV0) in the Stacks Project.

**`AlgebraicGeometry.derivedRestriction_adj_derivedHomSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/ConstructedDerivedAdjunction.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/ConstructedDerivedAdjunction.lean#L195).

> **Stacks 0BV0.** For a morphism of schemes `f : Y ⟶ X`, the derived internal-Hom functor
> `R ℰom(f₊ 𝒪_Y, -) : D(𝒪_X) ⥤ D(f₊ 𝒪_Y)` is right adjoint to the functor `D(f₊ 𝒪_Y) ⥤ D(𝒪_X)`
> induced by restriction of scalars.

```lean
public theorem derivedRestriction_adj_derivedHomSheaf :
    Nonempty (derivedRestrictionOfScalars f ⊣ derivedHomSheaf f)
```

## Tag 0BV1, a lemma

[Tag 0BV1](https://stacks.math.columbia.edu/tag/0BV1) in the Stacks Project.

**`AlgebraicGeometry.derivedHomSheaf_comp_derivedRestriction_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/ConstructedDerivedAdjunction.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/ConstructedDerivedAdjunction.lean#L291).

> **Stacks 0BV1.** Following `R ℰom(f₊ 𝒪_Y, -)` by the functor `D(f₊ 𝒪_Y) ⥤ D(𝒪_X)` induced
> by restriction of scalars gives `R ℰom_{𝒪_X}(f₊ 𝒪_Y, -)`. The displayed compatibility with the
> comparison maps characterizes the isomorphism uniquely.

```lean
public theorem derivedHomSheaf_comp_derivedRestriction_iso :
    ∃! e : derivedHomSheaf f ⋙ derivedRestrictionOfScalars f ≅
        derivedInternalHomPushforward f,
      compositeDerivedHomSheafUnit f ≫ whiskerLeft DerivedCategory.Qh e.hom =
        derivedInternalHomPushforwardUnit f
```

## Tag 0AX2, a lemma

[Tag 0AX2](https://stacks.math.columbia.edu/tag/0AX2) in the Stacks Project.

**`AlgebraicGeometry.derivedHomSheaf_finite_pseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/FiniteTwistedInverseImage.lean, line 482](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/FiniteTwistedInverseImage.lean#L482).

> **Stacks, Tag 0AX2.** Let `f : Y ⟶ X` be a finite pseudo-coherent morphism of schemes. The
> functor `R ℰom(f₊ 𝒪_Y, -) : D(𝒪_X) ⥤ D(f₊ 𝒪_Y)` maps `D⁺_QCoh(𝒪_X)` into `D⁺_QCoh(f₊ 𝒪_Y)`.
> If `X` is quasi-compact and quasi-separated, then on `D⁺_QCoh(𝒪_X)` the functor `Φ ∘ a` agrees
> with `R ℰom(f₊ 𝒪_Y, -)`, where `a` is the right adjoint of Stacks, Tag 0A9E for `f` and `Φ` is
> the equivalence of Stacks, Tag 0AVW. The functors `a` and `Φ` are taken at the locally small
> models and `R ℰom(f₊ 𝒪_Y, -)` at the standard one, compared along the identity-on-objects
> equivalence of the two models.

```lean
theorem derivedHomSheaf_finite_pseudoCoherent [IsFinite f] [PseudoCoherent f] :
    (∀ K : @DerivedCategory (SheafOfModules.{u} X.ringCatSheaf) _ _
          (HasDerivedCategory.standard _),
        @DerivedCategoryB.derivedCategoryBPlus _ _ _ (HasDerivedCategory.standard _)
            (SheafOfModules.isQuasicoherent X.ringCatSheaf) K →
          @DerivedCategoryB.derivedCategoryBPlus _ _ _ (HasDerivedCategory.standard _)
            (SheafOfModules.isQuasicoherent (pushforwardRingCatSheaf f))
            ((derivedHomSheaf f).obj K)) ∧
      ∀ [CompactSpace X] [QuasiSeparatedSpace X],
        haveI : CompactSpace Y := QuasiCompact.compactSpace_of_compactSpace f
        haveI : QuasiSeparatedSpace Y := quasiSeparatedSpace_of_quasiSeparated f
        Nonempty (ObjectProperty.ι (fun K : Stacks.Duality.quasiCoherentDerivedCategory X =>
              DerivedCategoryB.IsBoundedBelow K.obj) ⋙ twistedInverseImageQcqs f ⋙
            (derivedQuasicoherentPushforwardOverRingEquivalence f).functor ⋙
              ObjectProperty.ι _ ≅
          ObjectProperty.ι (fun K : Stacks.Duality.quasiCoherentDerivedCategory X =>
              DerivedCategoryB.IsBoundedBelow K.obj) ⋙ ObjectProperty.ι _ ⋙
            (structureSheafModelEquiv X).inverse ⋙ derivedHomSheaf f ⋙
              (pushforwardRingModelEquiv f).functor)
```

**`AlgebraicGeometry.pseudoCoherent_of_isFinite_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/FiniteOverNoetherian.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentMorphism/FiniteOverNoetherian.lean#L35). The attribute's comment: “parenthetical remark: a finite morphism of Noetherian schemes is pseudo-coherent”.

> A finite morphism `f : Y ⟶ X` to a locally
> Noetherian scheme is pseudo-coherent; in particular a finite morphism of Noetherian schemes is
> pseudo-coherent.

```lean
theorem pseudoCoherent_of_isFinite_of_isLocallyNoetherian {X Y : Scheme.{u}}
    [IsLocallyNoetherian X] (f : Y ⟶ X) [IsFinite f] : PseudoCoherent f
```

**`AlgebraicGeometry.derivedCategoryBPlus_derivedSheafHom_pushforwardStructureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/FinitePushforwardDerivedSheafHom.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/FinitePushforwardDerivedSheafHom.lean#L92). The attribute's comment: “the preservation clause with quasi-coherence read over 𝒪_X rather than over f_* 𝒪_Y; the commutative-diagram clause is not proved”.

> For a finite pseudo-coherent morphism `f : Y ⟶ X`, the derived internal Hom
> `R𝓗om_{𝒪_X}(f_* 𝒪_Y, -)` carries `D⁺_QCoh(𝒪_X)` into `D⁺_QCoh(𝒪_X)`.

```lean
theorem derivedCategoryBPlus_derivedSheafHom_pushforwardStructureSheaf (f : Y ⟶ X) [IsFinite f]
    (hf : PseudoCoherent f) (K : DerivedCategory (StructureSheafModules X.sheaf))
    (hK : DerivedCategoryB.derivedCategoryBPlus
      (SheafOfModules.isQuasicoherent X.ringCatSheaf) K) :
    DerivedCategoryB.derivedCategoryBPlus (SheafOfModules.isQuasicoherent X.ringCatSheaf)
      (((Stacks.SheafOfModules.derivedSheafHom X.sheaf).obj
        (op ((DerivedCategory.singleFunctor X.Modules 0).obj
          ((Scheme.Modules.pushforward f).obj (SheafOfModules.unit Y.ringCatSheaf))))).obj K)
```

**`AlgebraicGeometry.derivedCategoryBPlus_derivedSheafHom_of_pseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/FinitePushforwardDerivedSheafHom.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/FinitePushforwardDerivedSheafHom.lean#L114). The attribute's comment: “the preservation clause, for a derived sheaf-Hom functor given together with its identification of Tag 0BV1; the commutative-diagram clause is not proved”.

> Let `f : Y ⟶ X` be a finite pseudo-coherent morphism of schemes and let
> `derivedSheafHom : D(𝒪_X) ⥤ D(f_* 𝒪_Y)` be a functor whose composite with restriction of scalars
> along `𝒪_X ⟶ f_* 𝒪_Y` is the derived internal Hom `R𝓗om_{𝒪_X}(f_* 𝒪_Y, -)`, which is what
> [Stacks, Tag 0BV1] says of the derived sheaf-Hom functor.  Then `derivedSheafHom` maps
> `D⁺_QCoh(𝒪_X)` into `D⁺_QCoh(f_* 𝒪_Y)`.

```lean
theorem derivedCategoryBPlus_derivedSheafHom_of_pseudoCoherent (f : Y ⟶ X) [IsFinite f]
    (hf : PseudoCoherent f)
    (derivedSheafHom : DerivedCategory (SheafOfModules.{u} X.ringCatSheaf) ⥤
      DerivedCategory (SheafOfModules.{u} (pushforwardRing f.base Y.ringCatSheaf)))
    (hsplit : derivedSheafHom ⋙ (scalarRestriction f).mapDerivedCategory ≅
      (Stacks.SheafOfModules.derivedSheafHom X.sheaf).obj
        (op ((DerivedCategory.singleFunctor X.Modules 0).obj
          ((Scheme.Modules.pushforward f).obj (SheafOfModules.unit Y.ringCatSheaf)))))
    (K : DerivedCategory (SheafOfModules.{u} X.ringCatSheaf))
    (hK : DerivedCategoryB.derivedCategoryBPlus
      (SheafOfModules.isQuasicoherent X.ringCatSheaf) K) :
    DerivedCategoryB.derivedCategoryBPlus
      (SheafOfModules.isQuasicoherent (pushforwardRing f.base Y.ringCatSheaf))
      (derivedSheafHom.obj K)
```

## Tag 0AX3, a remark

[Tag 0AX3](https://stacks.math.columbia.edu/tag/0AX3) in the Stacks Project.

**`AlgebraicGeometry.isIso_pushforwardRightAdjointToDerivedInternalHom_and_comp_evaluation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/FiniteTraceDerivedInternalHomIso.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/FiniteTraceDerivedInternalHomIso.lean#L461). The attribute's comment: “the whole remark, for every right adjoint a of Rf_* on D_QCoh and every adjunction exhibiting it: the comparison map Rf_* a(K) ⟶ R Eom_{O_X}(f_* O_Y, K) of Tag 0AX2 is an isomorphism (the left equality of the square) and, followed by the map induced by O_X ⟶ f_* O_Y, it is the trace Tr_{f, K}. Stated for f finite and X locally Noetherian, which contains the source's finite morphism of Noetherian schemes, and K in D_QCoh^+(O_X)”.

> **Stacks Project, Tag 0AX3 (Remark 48.11.5).** Let `f : Y ⟶ X` be a finite morphism of
> schemes with `X` locally Noetherian — in particular a finite morphism of Noetherian schemes —
> let `a` be a right adjoint of `Rf_* : D_QCoh(𝒪_Y) ⥤ D_QCoh(𝒪_X)`, and let `K` be an object of
> `D_QCoh^+(𝒪_X)`.  Then in the square
>
> ```
> Rf_* a(K)                     --Tr_{f, K}-->   K
>     ‖                                          ‖
> R ℰom_{𝒪_X}(f₊ 𝒪_Y, K)            -->          K
> ```
>
> the left edge — the comparison map `Rf_* a(K) ⟶ R ℰom_{𝒪_X}(f₊ 𝒪_Y, K)` of
> [Stacks, Tag 0AX2] — is an isomorphism, so that it is the identification the source draws as an
> equality, and the square commutes: that isomorphism followed by the map
> `R ℰom_{𝒪_X}(f₊ 𝒪_Y, K) ⟶ K` induced by `𝒪_X ⟶ f₊ 𝒪_Y` is the trace map `Tr_{f, K}`, the counit
> of `Rf_* ⊣ a`.

```lean
theorem isIso_pushforwardRightAdjointToDerivedInternalHom_and_comp_evaluation
    [IsLocallyNoetherian X] (K : quasiCoherentDerivedCategory X)
    (hK : DerivedCategoryB.IsBoundedBelow K.obj) :
    IsIso (pushforwardRightAdjointToDerivedInternalHom f adj K) ∧
      pushforwardRightAdjointToDerivedInternalHom f adj K ≫
          (derivedInternalHomPushforwardEvaluation f).app K.obj =
        (adj.counit.app K).hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.11, Tag 0AWZ](https://stacks.math.columbia.edu/tag/0AWZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
