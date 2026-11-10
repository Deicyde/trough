---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isRightDerivedFunctor_quasicoherentPushforwardMapDerivedCategory, AlgebraicGeometry.Space.derivedQuasicoherentComparisonSquareOfIsAffineHom, AlgebraicGeometry.Space.flatPushforwardDerivedCoheratorIso, AlgebraicGeometry.Space.flatPushforwardDerivedCoheratorIsoOfForallAffine, AlgebraicGeometry.Space.derivedModulePushforwardCompDerivedCoheratorIso, AlgebraicGeometry.Space.inclusionAdjunctionGlobalSectionsAssociated, AlgebraicGeometry.Space.coheratorIsoAssociatedGlobalSections, AlgebraicGeometry.Space.derivedCoheratorIsoAssociatedDerivedGlobalSections
statement: formalized
proof: formalized
---

# 75.11 The coherator

Section 75.11 of the Stacks Project, [Tag 08GX](https://stacks.math.columbia.edu/tag/08GX). 6 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08GY, a lemma

[Tag 08GY](https://stacks.math.columbia.edu/tag/08GY) in the Stacks Project.

**`AlgebraicGeometry.Space.isRightDerivedFunctor_quasicoherentPushforwardMapDerivedCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineDerivedQuasicoherentPushforward.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineDerivedQuasicoherentPushforward.lean#L133). The attribute's comment: “the derived functor”.

> **[Stacks, Tag 08GY], the derived functor.**  Let `f : X ⟶ Y` be an affine morphism of
> algebraic spaces over a scheme `S`.  Then direct image defines a derived functor
> `f_* : D(QCoh(𝒪_X)) ⥤ D(QCoh(𝒪_Y))`: the functor induced on the unbounded derived categories by
> the exact functor `AlgebraicGeometry.Space.quasicoherentPushforward` is a total right derived
> functor of it.  No resolutions are involved, and the derived functor is computed by applying
> `f_*` to a representative complex, which is how the source states it.
>
> The structure map is `CategoryTheory.Functor.mapDerivedCategoryFactorsh.inv`, which exhibits the
> induced functor as a lift through the localization `DerivedCategory.Qh`; a lift of a functor that
> inverts the quasi-isomorphisms is a right derived functor for the inverse of the lifting
> isomorphism.

```lean
theorem isRightDerivedFunctor_quasicoherentPushforwardMapDerivedCategory (f : X ⟶ Y)
    (hf : IsAffineHom B S hS f.hom) :
    letI := preservesFiniteColimitsQuasicoherentPushforwardOfIsAffineHom B S hS f hf
    Functor.IsRightDerivedFunctor
      (quasicoherentPushforward B S hS f
        (pushforwardPreservesQuasicoherence_of_isAffineHom B S hS f hf)).mapDerivedCategory
      (quasicoherentPushforward B S hS f
          (pushforwardPreservesQuasicoherence_of_isAffineHom B S hS f
            hf)).mapDerivedCategoryFactorsh.inv
      (HomotopyCategory.quasiIso (QuasicoherentSheaves.{u, u} B S hS X.1 X.2)
        (ComplexShape.up ℤ))
```

**`AlgebraicGeometry.Space.derivedQuasicoherentComparisonSquareOfIsAffineHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineDerivedQuasicoherentPushforward.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineDerivedQuasicoherentPushforward.lean#L198). The attribute's comment: “the commuting square”.

> **[Stacks, Tag 08GY], the commuting square.**  Let `f : X ⟶ Y` be an affine morphism of
> algebraic spaces over a scheme `S`, and let `Rf_*` be a total right derived functor of the direct
> image of all `𝒪_X`-modules, with derivation unit `α`.  Then the square
>
> `D(QCoh(𝒪_X)) ⟶ D_QCoh(𝒪_X) ⟶^{Rf_*} D_QCoh(𝒪_Y)`,
> `D(QCoh(𝒪_X)) ⟶^{f_*} D(QCoh(𝒪_Y)) ⟶ D_QCoh(𝒪_Y)`
>
> commutes, its rows being the comparison functor of [Stacks, Tag 08F1] and its left edge the
> derived functor of
> `AlgebraicGeometry.Space.isRightDerivedFunctor_quasicoherentPushforwardMapDerivedCategory`.
>
> This is `AlgebraicGeometry.Space.derivedQuasicoherentComparisonSquare` with both of its inputs
> supplied: right exactness of the quasi-coherent direct image by
> `AlgebraicGeometry.Space.preservesFiniteColimitsQuasicoherentPushforwardOfIsAffineHom`, and that
> a complex of quasi-coherent modules computes its derived direct image by
> `AlgebraicGeometry.Space.isIso_derivedModulePushforwardUnit_app_of_isQuasicoherentOnSite`.

```lean
noncomputable def derivedQuasicoherentComparisonSquareOfIsAffineHom :
    letI := preservesFiniteColimitsQuasicoherentPushforwardOfIsAffineHom B S hS f hf
    (quasicoherentPushforward B S hS f
          (pushforwardPreservesQuasicoherence_of_isAffineHom B S hS f hf)).mapDerivedCategory ⋙
        quasicoherentDerivedComparisonSchemeUniverse B S hS Y.1 Y.2 ⋙
          (DerivedCategoryB.derivedCategoryB
            (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
              (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS Y.1 Y.2).O))).ι ≅
      quasicoherentDerivedComparisonSchemeUniverse B S hS X.1 X.2 ⋙
        (DerivedCategoryB.derivedCategoryB
          (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
            (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O))).ι ⋙
        Rf
```

## Tag 08GZ, a lemma

[Tag 08GZ](https://stacks.math.columbia.edu/tag/08GZ) in the Stacks Project.

**`AlgebraicGeometry.Space.flatPushforwardDerivedCoheratorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoheratorFlatPushforward.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoheratorFlatPushforward.lean#L303). The attribute's comment: “granted Stacks 03M9 that the direct image preserves quasi-coherence, Stacks 03GA that the inverse image does, Stacks 077V part (1) that QCoh(𝒪_X) is Grothendieck abelian, and flatness in the ringed-topos form of Stacks 04JC”.

> **Stacks Project, Tag 08GZ.**  Let `f : X ⟶ Y` be a flat morphism of algebraic spaces whose
> direct image and inverse image preserve quasi-coherence.  Let `Rf_*` be a total right derived
> functor of the direct image of all modules, let `RQ_X`, `RQ_Y` be total right derived functors of
> coherators of `X` and `Y`, and let `Φ` be a total right derived functor of the direct image
> restricted to quasi-coherent modules.  Then `Rf_* ⋙ RQ_Y ≅ RQ_X ⋙ Φ`.
>
> Both sides are right adjoint to the same functor `D(QCoh(𝒪_Y)) ⥤ D(𝒪_X)`: flatness makes the
> inverse image exact, on all modules and on quasi-coherent modules alike, so it induces functors
> of derived categories with no derivation, and these compose to one functor in two ways which
> agree because the inverse image commutes with the inclusion of the quasi-coherent modules
> already before deriving.

```lean
noncomputable def flatPushforwardDerivedCoheratorIso
    (hpush : PushforwardPreservesQuasicoherence B S hS f)
    (Φ : DerivedCategory (QuasicoherentSheaves.{u, u} B S hS X.1 X.2) ⥤
      DerivedCategory (QuasicoherentSheaves.{u, u} B S hS Y.1 Y.2))
    (ΦUnit : (quasicoherentPushforward B S hS f hpush).mapHomologicalComplex
        (ComplexShape.up ℤ) ⋙ QY ⟶ QX ⋙ Φ)
    [Φ.IsRightDerivedFunctor ΦUnit (HomologicalComplex.quasiIso
      (QuasicoherentSheaves.{u, u} B S hS X.1 X.2) (ComplexShape.up ℤ))] :
    Rf ⋙ RQY ≅ RQX ⋙ Φ
```

**`AlgebraicGeometry.Space.flatPushforwardDerivedCoheratorIsoOfForallAffine`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoheratorFlatPushforward.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoheratorFlatPushforward.lean#L393). The attribute's comment: “in the binders of the source statement, granted the affine-base case of the preservation of quasi-coherence by the direct image, Stacks 03GA that the inverse image preserves quasi-coherence, Stacks 077V part (1) that QCoh(𝒪_X) is Grothendieck abelian, and flatness in the ringed-topos form of Stacks 04JC”.

> **Stacks Project, Tag 08GZ, in the binders of the source statement.**  Let `f : X ⟶ Y` be a
> quasi-compact, quasi-separated and flat morphism of algebraic spaces whose inverse image
> preserves quasi-coherence.  With `Rf_*`, `RQ_X`, `RQ_Y` and `Φ` as above,
> `Rf_* ⋙ RQ_Y ≅ RQ_X ⋙ Φ`.
>
> Quasi-compactness and quasi-separatedness enter exactly where the source puts them: they are what
> makes the direct image preserve quasi-coherence, by the reduction of Stacks 03M9 whose residual
> affine-base case is `haffine`.

```lean
noncomputable def flatPushforwardDerivedCoheratorIsoOfForallAffine
    (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (haffine : ∀ F : Modules.{u, u} B S hS X.1 X.2, F.IsQuasicoherentOnSite →
      ∀ V : SmallEtale B S hS Y.1,
        IsAffine ((BigFppfOver.toScheme B S hS).obj ((SmallEtale.toOver B S hS Y.1).obj V)) →
        IsQuasiCompact B S hS (chartBaseChangeProjection B S hS f V).hom →
        IsQuasiSeparated B S hS (chartBaseChangeProjection B S hS f V).hom →
        ((chartLocalizedModulePushforward B S hS f V).obj
          ((moduleChartBaseChangeRestriction B S hS f V).obj F)).IsQuasicoherentOnSite)
    (Φ : DerivedCategory (QuasicoherentSheaves.{u, u} B S hS X.1 X.2) ⥤
      DerivedCategory (QuasicoherentSheaves.{u, u} B S hS Y.1 Y.2))
    (ΦUnit : (quasicoherentPushforward B S hS f
        (pushforwardPreservesQuasicoherence_of_forall_affine B S hS f hfqc hfqs
          haffine)).mapHomologicalComplex (ComplexShape.up ℤ) ⋙ QY ⟶ QX ⋙ Φ)
    [Φ.IsRightDerivedFunctor ΦUnit (HomologicalComplex.quasiIso
      (QuasicoherentSheaves.{u, u} B S hS X.1 X.2) (ComplexShape.up ℤ))] :
    Rf ⋙ RQY ≅ RQX ⋙ Φ
```

**`AlgebraicGeometry.Space.derivedModulePushforwardCompDerivedCoheratorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoheratorFlatPushforwardQcqs.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoheratorFlatPushforwardQcqs.lean#L326). The attribute's comment: “RQ_Y ∘ Rf_* = Φ ∘ RQ_X for a flat, quasi-compact, quasi-separated morphism”.

> **The derived coherator commutes with the direct image along a flat morphism.**  Let
> `f : X ⟶ Y` be a quasi-compact, quasi-separated and flat morphism of algebraic spaces over `S`,
> and let `Φ : D(QCoh(𝒪_X)) ⥤ D(QCoh(𝒪_Y))` be the right derived functor of
> `f_* : QCoh(𝒪_X) ⥤ QCoh(𝒪_Y)`.  Then `RQ_Y ∘ Rf_* = Φ ∘ RQ_X`, as a natural isomorphism
> `Rf_* ⋙ RQ_Y ≅ RQ_X ⋙ Φ`.
>
> Here `Rf_*` is `AlgebraicGeometry.Space.derivedModulePushforward`, `RQ_X` and `RQ_Y` are
> `AlgebraicGeometry.Space.derivedCoherator`, and `Φ` is
> `AlgebraicGeometry.Space.derivedQuasicoherentPushforward` at the preservation of quasi-coherence of
> Stacks 03M9.

```lean
def derivedModulePushforwardCompDerivedCoheratorIso (f : X ⟶ Y)
    (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hflat : IsFlat B S hS f.hom) :
    derivedModulePushforward B S hS f ⋙ derivedCoherator B S hS Y.1 Y.2 ≅
      derivedCoherator B S hS X.1 X.2 ⋙ derivedQuasicoherentPushforward B S hS f
        (pushforwardPreservesQuasicoherence_of_qcqs B S hS f hfqc hfqs)
```

## Tag 08H0, a lemma

[Tag 08H0](https://stacks.math.columbia.edu/tag/08H0) in the Stacks Project.

**`AlgebraicGeometry.Space.inclusionAdjunctionGlobalSectionsAssociated`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineCoheratorGlobalSections.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineCoheratorGlobalSections.lean#L171). The attribute's comment: “(1): the coherator of an affine algebraic space is the associated module of the global sections; carried are the associated-module equivalence Mod(A) ≌ QCoh(O_X) of the affine case of Stacks 03DX(2) and its adjunction to global sections (Stacks 01BH(4)), neither of which this development has on the small etale site of an algebraic space”.

> **Stacks 08H0 (1).**  Let `X` be an affine algebraic space and `A = Γ(X, 𝒪_X)`.  The functor
> sending an `𝒪_X`-module `𝓕` to the quasi-coherent `𝒪_X`-module associated to the `A`-module
> `Γ(X, 𝓕)` is a right adjoint of the inclusion `QCoh(𝒪_X) ⥤ Mod(𝒪_X)`; that is, it is a
> coherator of `X`.
>
> Carried: the associated-module equivalence `assoc : Mod(A) ≌ QCoh(𝒪_X)` of the affine case of
> Stacks 03DX (2) and its adjunction `adjAssoc` to global sections, Stacks 01BH (4).  See
> "What is carried, and why it is an input and not the conclusion" in the module documentation.
>
> The proof is the source's, and is the one the scheme analogue Stacks 08D9 (1) uses: composing
> the adjunction `assoc.inverse ⊣ assoc.functor` of the equivalence with `adjAssoc` gives
> `assoc.inverse ⋙ assoc.functor ⋙ ι ⊣ Γ(X, -) ⋙ assoc.functor`, and the left-hand side is `ι`
> by the counit of the equivalence.

```lean
def inclusionAdjunctionGlobalSectionsAssociated (_hAffine : IsAffineSpace B S hS F) :
    (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, m}
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O))).ι ⊣
        moduleGlobalSectionsSmallEtale.{u, m} B S hS F hF ⋙ assoc.functor
```

**`AlgebraicGeometry.Space.coheratorIsoAssociatedGlobalSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineCoheratorGlobalSections.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineCoheratorGlobalSections.lean#L199). The attribute's comment: “(1): every coherator of an affine algebraic space is naturally the associated module of the global sections; carried are a coherator with its adjunction (Stacks 077V(2), which the development has only as an existence statement) and the associated-module equivalence Mod(A) ≌ QCoh(O_X) of the affine case of Stacks 03DX(2) with its adjunction to global sections”.

> **Stacks 08H0 (1).**  Let `X` be an affine algebraic space and `A = Γ(X, 𝒪_X)`.  Every
> coherator `Q_X : Mod(𝒪_X) ⥤ QCoh(𝒪_X)` of `X` — every right adjoint of the inclusion
> `QCoh(𝒪_X) ⥤ Mod(𝒪_X)`, which is what Stacks 077V (2) produces — is naturally isomorphic to the
> functor sending `𝓕` to the quasi-coherent `𝒪_X`-module associated to the `A`-module
> `Γ(X, 𝓕)`.
>
> Carried: a coherator `Q` with its adjunction `adjQ`, and the associated-module equivalence; see
> "What is carried, and why it is an input and not the conclusion" in the module documentation.
> Both sides are right adjoints of the inclusion, by `adjQ` and by
> `AlgebraicGeometry.Space.inclusionAdjunctionGlobalSectionsAssociated`, and a right adjoint is
> unique up to a unique natural isomorphism.

```lean
def coheratorIsoAssociatedGlobalSections
    (Q : Modules.{u, m} B S hS F hF ⥤ QuasicoherentSheaves.{u, m} B S hS F hF)
    (adjQ : (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, m}
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O))).ι ⊣ Q)
    (hAffine : IsAffineSpace B S hS F) :
    Q ≅ moduleGlobalSectionsSmallEtale.{u, m} B S hS F hF ⋙ assoc.functor
```

**`AlgebraicGeometry.Space.derivedCoheratorIsoAssociatedDerivedGlobalSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineDerivedCoheratorGlobalSections.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineDerivedCoheratorGlobalSections.lean#L205). The attribute's comment: “(2): the derived coherator of an affine algebraic space is the associated complex of the derived global sections; carried are a coherator with its adjunction (Stacks 077V(2), which the development has only as an existence statement) and the associated-module equivalence Mod(A) ≌ QCoh(O_X) of the affine case of Stacks 03DX(2) with its adjunction to global sections”.

> Let `X` be an affine algebraic space and `A = Γ(X, 𝒪_X)`. The derived coherator
> `RQ_X : D(𝒪_X) ⥤ D(QCoh(𝒪_X))` sends an object `E` of `D(𝒪_X)` to the complex of
> quasi-coherent `𝒪_X`-modules associated to the object `RΓ(X, E)` of `D(A)`.

```lean
def derivedCoheratorIsoAssociatedDerivedGlobalSections (hAffine : IsAffineSpace B S hS F) :
    letI := modulesAbelianSmallEtale B S hS F hF
    letI := quasicoherentSheavesAbelianSmallEtale B S hS F hF
    letI := modulesHasDerivedCategorySmallEtale B S hS F hF
    letI := quasicoherentSheavesHasDerivedCategorySmallEtale B S hS F hF
    letI := additive_assoc_functor B S hS F hF assoc adjAssoc
    letI := additive_coherator B S hS F hF Q adjQ
    letI := isGrothendieckAbelian_modules B S hS F hF
    derivedCoheratorSmallEtale B S hS F hF Q adjQ ≅
      derivedModuleGlobalSectionsSmallEtale B S hS F hF ⋙ assoc.functor.mapDerivedCategory
```

**`AlgebraicGeometry.Space.inclusionAdjunctionGlobalSectionsAssociated_of_isAffineSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineSpaceCoheratorAssociatedModule.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineSpaceCoheratorAssociatedModule.lean#L196). The attribute's comment: “part (1)”.

> **Stacks 08H0 (1).**  Let `X` be an affine algebraic space over a scheme `S` and set
> `A = Γ(X, 𝒪_X)`.  The functor sending an `𝒪_X`-module `𝓕` to the quasi-coherent `𝒪_X`-module
> associated to the `A`-module `Γ(X, 𝓕)` is a right adjoint of the inclusion
> `QCoh(𝒪_X) ⥤ Mod(𝒪_X)`; that is, it is a coherator of `X` in the sense of Stacks 077V (2).
>
> The proof is the source's: composing the adjunction `(-)^~ ⋙ ι ⊣ Γ(X, -)` of the affine case of
> Stacks 01BH (4) with the adjunction `((-)^~)^{-1} ⊣ (-)^~` of the associated-module equivalence
> gives `((-)^~)^{-1} ⋙ (-)^~ ⋙ ι ⊣ Γ(X, -) ⋙ (-)^~`, and the left-hand side is `ι` by the counit
> of the equivalence.

```lean
def inclusionAdjunctionGlobalSectionsAssociated_of_isAffineSpace :
    (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O))).ι ⊣
      affineSpaceGlobalSections B S hS F hF hAffine ⋙
        (affineSpaceAssociatedModuleEquivalence B S hS F hF hAffine).functor
```

**`AlgebraicGeometry.Space.coheratorIsoGlobalSectionsAssociated_of_isAffineSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineSpaceCoheratorAssociatedModule.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineSpaceCoheratorAssociatedModule.lean#L225). The attribute's comment: “part (1)”.

> **Stacks 08H0 (1).**  Let `X` be an affine algebraic space over a scheme `S` and set
> `A = Γ(X, 𝒪_X)`.  The coherator `Q_X : Mod(𝒪_X) ⥤ QCoh(𝒪_X)` of Stacks 077V (2) is naturally
> isomorphic to the functor sending `𝓕` to the quasi-coherent `𝒪_X`-module associated to the
> `A`-module `Γ(X, 𝓕)`.
>
> Both are right adjoints of the inclusion `QCoh(𝒪_X) ⥤ Mod(𝒪_X)` — the coherator by
> `AlgebraicGeometry.Space.coheratorAdjunction` and the other by
> `AlgebraicGeometry.Space.inclusionAdjunctionGlobalSectionsAssociated_of_isAffineSpace` — and a
> right adjoint is unique up to a unique natural isomorphism.

```lean
def coheratorIsoGlobalSectionsAssociated_of_isAffineSpace :
    coherator B S hS F hF ≅
      affineSpaceGlobalSections B S hS F hF hAffine ⋙
        (affineSpaceAssociatedModuleEquivalence B S hS F hF hAffine).functor
```

**`AlgebraicGeometry.Space.derivedCoheratorIsoComparisonInv_of_isAffineSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineSpaceCoheratorComparisonInverse.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineSpaceCoheratorComparisonInverse.lean#L46). The attribute's comment: “part (3)”.

> **Stacks 08H0 (3).**  On an affine algebraic space the derived coherator `RQ_X`, restricted
> to the complexes of `𝒪_X`-modules with quasi-coherent cohomology, is naturally isomorphic to the
> inverse of the comparison functor `i_X : D(QCoh(𝒪_X)) ⥤ D_QCoh(𝒪_X)` of Stacks 08F1.

```lean
def derivedCoheratorIsoComparisonInv_of_isAffineSpace (hAffine : IsAffineSpace B S hS F) :
    letI := isEquivalence_quasicoherentDerivedComparison_of_isAffineSpace B S hS F hF hAffine
    (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS F hF).O)))).ι ⋙ derivedCoherator B S hS F hF ≅
      (quasicoherentDerivedComparison B S hS F hF).inv
```

**`AlgebraicGeometry.Space.derivedCoheratorIsoDerivedGlobalSectionsAssociated_of_isAffineSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineSpaceDerivedCoheratorAssociatedModule.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineSpaceDerivedCoheratorAssociatedModule.lean#L100). The attribute's comment: “part (2)”.

> **Stacks 08H0 (2).**  Let `X` be an affine algebraic space over a scheme `S` and set
> `A = Γ(X, 𝒪_X)`.  The derived coherator `RQ_X : D(𝒪_X) ⥤ D(QCoh(𝒪_X))` sends an object `E` of
> `D(𝒪_X)` to the complex of quasi-coherent `𝒪_X`-modules associated to the object `RΓ(X, E)` of
> `D(A)`.

```lean
def derivedCoheratorIsoDerivedGlobalSectionsAssociated_of_isAffineSpace :
    derivedCoherator B S hS F hF ≅
      affineSpaceDerivedGlobalSections B S hS F hF hAffine ⋙
        (affineSpaceAssociatedModuleEquivalence B S hS F hF hAffine).functor.mapDerivedCategory
```

## Tag 09TG, a lemma

[Tag 09TG](https://stacks.math.columbia.edu/tag/09TG) in the Stacks Project.

**`AlgebraicGeometry.Space.quasicoherentDerivedComparison_isEquivalence_of_affineEtaleDerivedPushforwardSquareCommutes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoheratorEquivalence.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoheratorEquivalence.lean#L88). The attribute's comment: “equivalence clause”.

> Let `X` be a quasi-compact and quasi-separated algebraic space over `S`.  Suppose that for
> every étale morphism `j : V ⟶ W` with `W ⊆ X` a quasi-compact open and `V` affine, the right
> derived functor `Φ` of `j_* : QCoh(𝒪_V) ⥤ QCoh(𝒪_W)` fits into the commutative square
> `i_W ∘ Φ ≅ Rj_* ∘ i_V` (`AlgebraicGeometry.Space.ExistsAffineEtaleDerivedPushforwardSquare`).
> Then the comparison functor `i_X : D(QCoh(𝒪_X)) ⥤ D_QCoh(𝒪_X)` of Stacks 08F1 is an
> equivalence.

```lean
theorem quasicoherentDerivedComparison_isEquivalence_of_affineEtaleDerivedPushforwardSquareCommutes
    (hXqc : IsQuasiCompactSpace B S hS X.1) (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (h : ExistsAffineEtaleDerivedPushforwardSquare B S hS X.1 X.2) :
    (quasicoherentDerivedComparison B S hS X.1 X.2).IsEquivalence
```

**`AlgebraicGeometry.Space.derivedCoherator_isoInv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoheratorQuasiInverse.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoheratorQuasiInverse.lean#L366). The attribute's comment: “quasi-inverse clause, given the equivalence”.

> **[Stacks, Tag 09TG], quasi-inverse clause.**  Let `X` be an algebraic space whose comparison
> functor `i_X : D(QCoh(𝒪_X)) ⥤ D_QCoh(𝒪_X)` of Stacks 08F1 is an equivalence, and let `RQ_X` be
> any total right derived functor of a coherator `C_X` of `X`.  Then the quasi-inverse of `i_X` is
> `RQ_X` restricted to the complexes with quasi-coherent cohomology.
>
> `AlgebraicGeometry.Space.comparisonDerivedCoheratorAdjunction` exhibits that restriction as a
> right adjoint of `i_X`, the inverse of an equivalence is another, and a right adjoint is unique
> up to a unique natural isomorphism.
>
> This is the second clause of the conclusion of [Stacks, Tag 09TG], deduced from the first clause
> rather than from the tag's affine-étale hypothesis
> `AlgebraicGeometry.Space.AffineEtaleDerivedPushforwardCompatible`; the first clause — that the
> comparison functor is an equivalence — is the source's induction over the elementary
> distinguished squares of a quasi-compact, quasi-separated algebraic space, and is not proved
> here.

```lean
def derivedCoherator_isoInv
    [(quasicoherentDerivedComparison B S hS F hF).IsEquivalence] :
    (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O)))).ι ⋙ RQ ≅
      (quasicoherentDerivedComparison B S hS F hF).inv
```

## Tag 08H1, a proposition

[Tag 08H1](https://stacks.math.columbia.edu/tag/08H1) in the Stacks Project.

**`AlgebraicGeometry.Space.quasicoherentDerivedComparison_isEquivalence_of_isAffineHom_diag`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoheratorEquivalence.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoheratorEquivalence.lean#L129). The attribute's comment: “equivalence”.

> On a quasi-compact algebraic space with affine diagonal over `ℤ` the comparison functor
> `i_X : D(QCoh(𝒪_X)) ⥤ D_QCoh(𝒪_X)` of Stacks 08F1 is an equivalence.

```lean
theorem quasicoherentDerivedComparison_isEquivalence_of_isAffineHom_diag
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXdiag : IsAffineHom B (⊤_ Scheme.{u}) hZ (diag (viewOverIntegers B S hS hZ X.1))) :
    (quasicoherentDerivedComparison B S hS X.1 X.2).IsEquivalence
```

**`AlgebraicGeometry.Space.exists_equivalence_functor_eq_and_inverse_eq_derivedCoherator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoheratorEquivalence.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedCoheratorEquivalence.lean#L202). The attribute's comment: “equivalence with quasi-inverse RQ_X”.

> Let `X` be a quasi-compact algebraic space with affine diagonal over `ℤ`, `C_X` a coherator
> of `X` and `RQ_X` a total right derived functor of it.  Then the comparison functor
> `i_X : D(QCoh(𝒪_X)) ⥤ D_QCoh(𝒪_X)` of Stacks 08F1 is an equivalence with quasi-inverse `RQ_X`
> restricted to `D_QCoh(𝒪_X)`: there is an equivalence whose functor is `i_X` and whose inverse is
> `J ⋙ RQ_X`, for `J : D_QCoh(𝒪_X) ⥤ D(𝒪_X)` the inclusion.

```lean
theorem exists_equivalence_functor_eq_and_inverse_eq_derivedCoherator :
    ∃ e : DerivedCategory (QuasicoherentSheaves.{u, u} B S hS X.1 X.2) ≌
        QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2,
      e.functor = quasicoherentDerivedComparison B S hS X.1 X.2 ∧
        e.inverse =
          (DerivedCategoryB.derivedCategoryB
            (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
              ((Stacks.SheafOfModules.Tensor.ringSheaf
                (smallEtaleRingedSite B S hS X.1 X.2).O)))).ι ⋙ RQ
```

## Tag 0CSR, a lemma

[Tag 0CSR](https://stacks.math.columbia.edu/tag/0CSR) in the Stacks Project.

**`AlgebraicGeometry.Space.derivedQuasicoherentPushforwardSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedPushforwardQuasicoherentSquareTag.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedPushforwardQuasicoherentSquareTag.lean#L112).

> **[Stacks, Tag 0CSR].**  Let `f : X ⟶ Y` be a morphism of algebraic spaces over a scheme `S`,
> with `X` and `Y` quasi-compact with affine diagonal over `ℤ`.  Let `Φ` be a right derived functor
> of `f_* : QCoh(𝒪_X) ⥤ QCoh(𝒪_Y)` with unit `αΦ`, and `Rf_*` a right derived functor of the
> direct image of all modules with unit `α`.  Then the square
>
> `D(QCoh(𝒪_X)) ⟶ D_QCoh(𝒪_X) ⟶^{Rf_*} D_QCoh(𝒪_Y)`,
> `D(QCoh(𝒪_X)) ⟶^{Φ} D(QCoh(𝒪_Y)) ⟶ D_QCoh(𝒪_Y)`
>
> commutes, its rows being the comparison functors of [Stacks, Tag 08F1]; it is stated after the
> fully faithful inclusion `D_QCoh(𝒪_Y) ⥤ D(𝒪_Y)`, as for [Stacks, Tag 08GY].
>
> `f_*` preserves quasi-coherence because `f` is quasi-compact and quasi-separated
> ([Stacks, Tag 03M9]), by
> `AlgebraicGeometry.Space.pushforwardPreservesQuasicoherence_of_isQuasiCompactWithAffineDiagonal`.
> The isomorphism is the canonical comparison of the two right derived functors.

```lean
def derivedQuasicoherentPushforwardSquare {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXdiag : IsAffineHom B (⊤_ Scheme.{u}) hZ (diag (viewOverIntegers B S hS hZ X.1)))
    (hYqc : IsQuasiCompactSpace B S hS Y.1)
    (hYdiag : IsAffineHom B (⊤_ Scheme.{u}) hZ (diag (viewOverIntegers B S hS hZ Y.1)))
    (Φ : DerivedCategory (QuasicoherentSheaves.{u, u} B S hS X.1 X.2) ⥤
      DerivedCategory (QuasicoherentSheaves.{u, u} B S hS Y.1 Y.2))
    (αΦ : (quasicoherentPushforward B S hS f
        (pushforwardPreservesQuasicoherence_of_isQuasiCompactWithAffineDiagonal B S hS hZ f
          ⟨hXqc, hXdiag⟩ ⟨hYqc, hYdiag⟩)).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Φ)
    [Φ.IsRightDerivedFunctor αΦ
      (HomotopyCategory.quasiIso (QuasicoherentSheaves.{u, u} B S hS X.1 X.2) (ComplexShape.up ℤ))]
    (Rf : DerivedCategory (Modules.{u, u} B S hS X.1 X.2) ⥤
      DerivedCategory (Modules.{u, u} B S hS Y.1 Y.2))
    (α : (modulePushforward B S hS f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf)
    [Rf.IsRightDerivedFunctor α
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS X.1 X.2) (ComplexShape.up ℤ))] :
    Φ ⋙ quasicoherentDerivedComparisonSchemeUniverse B S hS Y.1 Y.2 ⋙
        (DerivedCategoryB.derivedCategoryB
          (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
            (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS Y.1 Y.2).O))).ι ≅
      quasicoherentDerivedComparisonSchemeUniverse B S hS X.1 X.2 ⋙
        (DerivedCategoryB.derivedCategoryB
          (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
            (Stacks.SheafOfModules.Tensor.ringSheaf
              (smallEtaleRingedSite B S hS X.1 X.2).O))).ι ⋙ Rf
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.11, Tag 08GX](https://stacks.math.columbia.edu/tag/08GX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
