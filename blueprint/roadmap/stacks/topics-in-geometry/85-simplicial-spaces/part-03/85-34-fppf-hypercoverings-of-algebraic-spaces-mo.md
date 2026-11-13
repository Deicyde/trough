---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.SimplicialSpacesEtaleSite.bigFppfAugmentationSquareTwoIso, descent_quasicoherent_of_isHypercoveringAugmentation, isIso_unit_and_isZero_rightDerived_of_isHypercoveringAugmentation, AlgebraicGeometry.Space.SimplicialSpacesEtaleSite.isWeakSerreClass_and_derivedPullback_equivalence, AlgebraicGeometry.Space.IsFppfHypercovering.isIso_derivedGlobalSectionsSemilinearMap, AlgebraicGeometry.Space.SimplicialSpacesEtaleSite.moduleSpectralSequence, AlgebraicGeometry.Space.SimplicialSpacesEtaleSite.moduleSpectralSequencePageOneIso, AlgebraicGeometry.Space.SimplicialSpacesEtaleSite.moduleSpectralSequence_abutsTo_of_isFppfHypercovering
statement: formalized
proof: formalized
---

# 85.34 Fppf hypercoverings of algebraic spaces: modules

Section 85.34 of the Stacks Project, [Tag 0DHB](https://stacks.math.columbia.edu/tag/0DHB). 6 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DHC, a lemma

[Tag 0DHC](https://stacks.math.columbia.edu/tag/0DHC) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.SimplicialSpacesEtaleSite.bigFppfAugmentationSquareTwoIso`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSmallEtaleBigFppfRinged.lean#L252), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialQuasicoherentDescentTags.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialQuasicoherentDescentTags.lean#L42) (StacksFrontier).

## Tag 0DHD, a lemma

[Tag 0DHD](https://stacks.math.columbia.edu/tag/0DHD) in the Stacks Project.

Declarations registered for the tag:

- [`descent_quasicoherent_of_isHypercoveringAugmentation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=descent_quasicoherent_of_isHypercoveringAugmentation#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialQuasicoherentDescentTags.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialQuasicoherentDescentTags.lean#L39) (StacksFrontier).

## Tag 0DHE, a lemma

[Tag 0DHE](https://stacks.math.columbia.edu/tag/0DHE) in the Stacks Project.

Declarations registered for the tag:

- [`isIso_unit_and_isZero_rightDerived_of_isHypercoveringAugmentation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isIso_unit_and_isZero_rightDerived_of_isHypercoveringAugmentation#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialQuasicoherentDescentTags.lean, line 36](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialQuasicoherentDescentTags.lean#L36) (StacksFrontier).

## Tag 0DHF, a lemma

[Tag 0DHF](https://stacks.math.columbia.edu/tag/0DHF) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.SimplicialSpacesEtaleSite.isWeakSerreClass_and_derivedPullback_equivalence`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialQuasicoherentDerivedDescentEquivalence.lean#L155), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialQuasicoherentDescentTags.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialQuasicoherentDescentTags.lean#L33) (StacksFrontier).

## Tag 0DHG, a lemma

[Tag 0DHG](https://stacks.math.columbia.edu/tag/0DHG) in the Stacks Project.

**`AlgebraicGeometry.Space.IsFppfHypercovering.isIso_derivedGlobalSectionsSemilinearMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/FppfHypercoveringQuasicoherentCohomology.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/FppfHypercoveringQuasicoherentCohomology.lean#L164).

> **Stacks Project, Tag 0DHG.** Let `S` be a scheme, `X` an algebraic space over `S`, `U` a
> simplicial algebraic space over `S` and `a : U → X` an augmentation. If `a : U → X` is an fppf
> hypercovering of `X`, then
>
> `RΓ(X_étale, K) = RΓ(U_étale, a^*K)`
>
> for `K ∈ D_QCoh(𝒪_X)`, where `a : (Sh(U_étale), 𝒪_U) → (Sh(X_étale), 𝒪_X)` is the morphism of
> ringed topoi of Section 0DE7 (`AlgebraicGeometry.Space.etaleAugmentationRingedHom`) and `a^*` its
> derived pullback: the canonical map `RΓ(X_étale, K) ⟶ RΓ(U_étale, a^*K)` is an isomorphism.
>
> Here `RΓ(X_étale, -)` and `RΓ(U_étale, -)` are the total right derived functors of global
> sections, with values in the derived categories of modules over coefficient rings `R'` and `R`
> mapping to `Γ(X, 𝒪_X)` and to `Γ(U, 𝒪_U)` through `ψ'` and `ψ`, compatibly (`h`) with
> `ρ : R' → R` and the map `Γ(X, 𝒪_X) → Γ(U, 𝒪_U)` of `a`; the right hand side is read in `D(R')`
> through restriction of scalars along `ρ`. For instance `R = R' = ℤ`. The canonical map
> (`Stacks.Cohomology.LerayOfToposHom.derivedGlobalSectionsSemilinearMap`) is `RΓ(X_étale, -)` of the
> derived unit `K → Ra_*a^*K`, invertible on `D_QCoh(𝒪_X)` by
> `AlgebraicGeometry.Space.IsFppfHypercovering.isIso_derivedAdjunction_unit_app`, followed by the
> identification `RΓ(X_étale, -) ∘ Ra_* = RΓ(U_étale, -)` of Cohomology on Sites, Remark 08J6.

```lean
theorem IsFppfHypercovering.isIso_derivedGlobalSectionsSemilinearMap (hA : IsFppfHypercovering A)
    {R : Type r} [Ring R] [HasDerivedCategory (ModuleCat.{u + 1} R)]
    {R' : Type r'} [Ring R'] [HasDerivedCategory (ModuleCat.{u + 1} R')]
    (ψ : R →+* RingCat.sectionsSubring ((Stacks.SheafOfModules.Tensor.ringSheaf
      (J := ((etaleSituation A).totalRingedTopos (etaleStructureSheaf A)).J))
        ((etaleSituation A).totalRingedTopos (etaleStructureSheaf A)).O).obj)
    (ψ' : R' →+* RingCat.sectionsSubring ((Stacks.SheafOfModules.Tensor.ringSheaf
      (J := (etaleRingedAugmentation A).augmentationRingedTopos.J))
        (etaleRingedAugmentation A).augmentationRingedTopos.O).obj)
    (ρ : R' →+* R)
    (h : (toposGlobalSectionsRingHom (etaleAugmentationRingedHom A)).comp ψ' = ψ.comp ρ)
    (K : @DerivedCategory (SheafOfModules.{u + 1}
      (Stacks.SheafOfModules.Tensor.ringSheaf (spacesEtaleRingedTopos B S hS A.right).O)) _ _
      (HasDerivedCategory.standard _))
    (hK : etaleQuasicoherentComplexes A K) :
    IsIso (derivedGlobalSectionsSemilinearMap.{u + 1, u + 1, u + 1, u + 1, u + 1, u + 1, r, r',
      _, _}
      (etaleAugmentationRingedHom A) ψ ψ' ρ h K)
```

## Tag 0DHH, a lemma

[Tag 0DHH](https://stacks.math.columbia.edu/tag/0DHH) in the Stacks Project.

**`AlgebraicGeometry.Space.SimplicialSpacesEtaleSite.moduleSpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialModuleSpectralSequence.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialModuleSpectralSequence.lean#L84). The attribute's comment: “the spectral sequence”.

> **The spectral sequence of a module pulled back to a simplicial algebraic space**
> `a : U → X`, as a functor of the `𝒪_X`-module `𝓕`: the spectral sequence of Stacks 0D7E for the
> pullback of `𝓕` to the total site of the strict components of `U_{spaces, étale}`.

```lean
def moduleSpectralSequence :
    SheafOfModules.{u + 1} (Stacks.SheafOfModules.Tensor.ringSheaf
        (spacesEtaleRingedTopos B S hS X).O) ⥤
      CohomologicalSpectralSequence AddCommGrpCat.{u + 1} 1
```

**`AlgebraicGeometry.Space.SimplicialSpacesEtaleSite.moduleSpectralSequencePageOneIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialModuleSpectralSequence.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialModuleSpectralSequence.lean#L124). The attribute's comment: “its first page `E_1^{p,q} = H^q_ét(U_p, 𝓕_p)`”.

> **`E_1^{p,q} = H^q_ét(U_p, a_p^*𝓕)`**, naturally in the `𝒪_X`-module `𝓕`, where `a_p^*` is
> the pullback of modules along the morphism of ringed topoi
> `(Sh((U_p)_{spaces, étale}), 𝒪_{U_p}) ⟶ (Sh(X_{spaces, étale}), 𝒪_X)` of `a_p : U_p → X`.

```lean
def moduleSpectralSequencePageOneIso (p q : ℕ) :
    moduleSpectralSequence a ⋙
        (CategoryTheory.SpectralSequence.pageFunctor AddCommGrpCat.{u + 1} _ 1 1 le_rfl ⋙
          HomologicalComplex.eval AddCommGrpCat.{u + 1} _ ((p : ℤ), (q : ℤ))) ≅
      (spacesEtaleRingedToposHom (Z₂ := X) (a.app (op ⦋p⦌))).toModulesHom.pullbackModules ⋙
        (spacesEtaleRingedTopos B S hS (U.obj (op ⦋p⦌))).moduleGlobalSections.rightDerived q
```

**`AlgebraicGeometry.Space.SimplicialSpacesEtaleSite.moduleSpectralSequence_abutsTo_of_isFppfHypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialQuasicoherentSpectralSequence.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialQuasicoherentSpectralSequence.lean#L94). The attribute's comment: “the spectral sequence converges to `H^{p+q}_ét(X, 𝓕)`”.

> **Stacks 0DHH.** Let `S` be a scheme, `X` an algebraic space over `S`, `U` a simplicial
> algebraic space over `S` and `a : U → X` an augmentation which is an fppf hypercovering of `X`.
> Let `𝓕` be a quasi-coherent `𝒪_X`-module and `𝓕_p = a_p^*𝓕` its pullback to `U_{p, étale}`. Then
> the spectral sequence `moduleSpectralSequence`, with first page
> `E_1^{p,q} = H^q_ét(U_p, 𝓕_p)` (`moduleSpectralSequencePageOneIso`), converges to
> `H^{p+q}_ét(X, 𝓕)`. The algebraic spaces are those of a big fppf site `T` of algebraic spaces
> over `S` (Stacks 0DBV).

```lean
theorem moduleSpectralSequence_abutsTo_of_isFppfHypercovering
    {A : SimplicialObject.Augmented T.Spaces} (hA : IsFppfHypercovering A)
    (F : SheafOfModules.{u + 1} (Stacks.SheafOfModules.Tensor.ringSheaf
      (spacesEtaleRingedTopos T.schemeSite S T.scheme_mem A.right).O))
    [F.IsQuasicoherentOnSite] :
    CategoryTheory.SpectralSequence.AbutsTo ((moduleSpectralSequence A.hom).obj F)
      (fun n => if 0 ≤ n then
        ((spacesEtaleRingedTopos T.schemeSite S T.scheme_mem
            A.right).moduleGlobalSections.rightDerived n.toNat).obj F
        else AddCommGrpCat.of PUnit.{u + 2})
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.34, Tag 0DHB](https://stacks.math.columbia.edu/tag/0DHB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
