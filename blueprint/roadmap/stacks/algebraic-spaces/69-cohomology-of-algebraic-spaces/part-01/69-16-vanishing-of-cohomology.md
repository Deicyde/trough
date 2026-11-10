---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.CohomologyVanishingSituation, AlgebraicGeometry.Space.CohomologyVanishingSituation.isIso_unit_tensorSheaf, AlgebraicGeometry.Space.CohomologyVanishingSituation.globalSectionsTensorLinearEquiv, Stacks.Cohomology.SiteModules.sectionTensorFreeIso, Stacks.Cohomology.SiteModules.sectionTensorSheafAdjunction, Stacks.Cohomology.SiteModules.isIso_sectionTensorSheafUnit_free, Stacks.Cohomology.SiteModules.isQuasicoherentOnSite_sectionTensor, AlgebraicGeometry.Space.CohomologyVanishingSituation.isZero_rightDerived_one_globalSectionsFunctor_of_isAffineHom
statement: formalized
proof: formalized
---

# 69.16 Vanishing of cohomology

Section 69.16 of the Stacks Project, [Tag 07UX](https://stacks.math.columbia.edu/tag/07UX). 9 tags here are carried by 18 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07UY, a situation

[Tag 07UY](https://stacks.math.columbia.edu/tag/07UY) in the Stacks Project.

**`AlgebraicGeometry.Space.CohomologyVanishingSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishing.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishing.lean#L75).

> **Stacks 07UY.** A quasi-compact, quasi-separated algebraic space `X` over a scheme `S`
> every one of whose quasi-coherent modules has vanishing first cohomology.

```lean
structure CohomologyVanishingSituation
```

## Tag 07UZ, a lemma

[Tag 07UZ](https://stacks.math.columbia.edu/tag/07UZ) in the Stacks Project.

**`AlgebraicGeometry.Space.CohomologyVanishingSituation.isIso_unit_tensorSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingTensorStructureSheaf.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingTensorStructureSheaf.lean#L360). The attribute's comment: “first assertion: p\_*(M ⊗\_A 𝒪\_X) = M~, the unit M~ ⟶ p\_*p^*M~ of the adjunction p^* ⊣ p\_* being an isomorphism”.

> **Stacks 07UZ, first assertion: `p_*(M ⊗_A 𝒪_X) = M~`.**  In Situation 07UY, for every
> `A`-module `M`, the unit `M~ ⟶ p_*p^*M~ = p_*(M ⊗_A 𝒪_X)` of the adjunction `p^* ⊣ p_*` of
> Stacks 03LU is an isomorphism.
>
> `p` is an isomorphism (`…CohomologyVanishingSituation.isIso_toSpecA`), so `p^*` is fully faithful
> and the unit is invertible.

```lean
theorem isIso_unit_tensorSheaf :
    IsIso ((modulePullbackAdjunction T.site (⊤_ Scheme.{u}) T.containsTerminal T.toSpecA).unit.app
      (T.tildeModule M))
```

**`AlgebraicGeometry.Space.CohomologyVanishingSituation.globalSectionsTensorLinearEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingTensorStructureSheaf.lean, line 688](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingTensorStructureSheaf.lean#L688). The attribute's comment: “second assertion: Γ(X, M ⊗\_A 𝒪\_X) = M, as A-modules”.

> **Stacks 07UZ, second assertion: `Γ(X, M ⊗_A 𝒪_X) = M`.**  In Situation 07UY, for every
> `A`-module `M`, the global sections of `M ⊗_A 𝒪_X = p^*M~` are `M`, as `A`-modules, the global
> sections being a module over `A = Γ(X, 𝒪_X)`.
>
> It is `M = Γ(Spec A, M~) = Γ(Spec A, p_*p^*M~) = Γ(X, p^*M~)`, the middle step being the first
> assertion `…CohomologyVanishingSituation.isIso_unit_tensorSheaf` and the last Stacks 0732.

```lean
def globalSectionsTensorLinearEquiv :
    M ≃ₗ[T.globalFunctions]
      (ModuleCat.restrictScalars T.globalFunctionsOverIntegersEquiv.toRingHom).obj
        (T.spaceSections M)
```

**`Stacks.Cohomology.SiteModules.sectionTensorFreeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/FreeTensorStructureSheaf.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/FreeTensorStructureSheaf.lean#L210). The attribute's comment: “the case of a free module: (⨁\_I A) ⊗\_A 𝒪\_X is the free sheaf of modules on I”.

> **The tensor of a free module over the global functions with the structure sheaf is the free
> sheaf of modules on the same index set**: `(⨁_I A) ⊗_A 𝒪 ≅ 𝒪^{(I)}`.
>
> Both sides corepresent the functor `F ↦ (I → Γ(C, F))`, and the isomorphism compares the two
> corepresenting objects.

```lean
def sectionTensorFreeIso (I : Type (max u r)) :
    (sectionTensorSheafFunctor.{u, v, max u r, u} O).obj (freeGlobalModule O I) ≅
      SheafOfModules.free (R := ringSheafOfSite O) I
```

**`Stacks.Cohomology.SiteModules.sectionTensorSheafAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/GlobalSectionsTensor.lean, line 633](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/GlobalSectionsTensor.lean#L633). The attribute's comment: “the module M ⊗\_A 𝒪\_X of the statement, as the left adjoint of global sections”.

> **The functor `M ↦ M ⊗_A 𝒪` is left adjoint to global sections.**
>
> Consequently it preserves all colimits; in particular it is right exact, which is what a
> presentation of `M` by free `A`-modules is used for.

```lean
def sectionTensorSheafAdjunction :
    sectionTensorSheafFunctor O ⊣ globalSectionsFunctor (ringSheafOfSite O)
```

**`Stacks.Cohomology.SiteModules.isIso_sectionTensorSheafUnit_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/SectionTensorGlobalSections.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/SectionTensorGlobalSections.lean#L343). The attribute's comment: “the free-module case of Γ(X, M ⊗\_A 𝒪\_X) = M, i.e. the direct-sum computation Γ(X, ⨁\_I 𝒪\_X) = ⨁\_I A, granted that global sections commute with that direct sum”.

> **`Γ(C, (⨁_I A) ⊗_A 𝒪) = ⨁_I A`**, granted that the global-sections functor commutes with the
> coproduct of `I` copies of the structure sheaf.
>
> The canonical map factors as the comparison `⨁_I A ⟶ Γ(C, 𝒪^{(I)})` through the global sections
> of the isomorphism `(⨁_I A) ⊗_A 𝒪 ≅ 𝒪^{(I)}`, and that comparison is invertible because
> `Γ(C, ⨁_{i ∈ I} 𝒪) = ⨁_{i ∈ I} A`.

```lean
theorem isIso_sectionTensorSheafUnit_free (I : Type (max u r))
    (hI : PreservesColimit
      (Discrete.functor (fun _ : I => SheafOfModules.unit (ringSheafOfSite O)))
      (globalSectionsFunctor.{u, v, max u r, max u r} (ringSheafOfSite O))) :
    IsIso (sectionTensorSheafUnit.{u, v, max u r, u} (freeGlobalModule O I))
```

**`Stacks.Cohomology.SiteModules.isQuasicoherentOnSite_sectionTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/SectionTensorPresentation.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/SectionTensorPresentation.lean#L253). The attribute's comment: “quasi-coherence of the module M ⊗\_A 𝒪\_X attached to a module over the global functions”.

> **`M ⊗_A 𝒪` is quasi-coherent on the site for every module `M` over the global functions.**
> It is the cokernel of a map of free sheaves of `O`-modules, which is a global presentation.

```lean
theorem isQuasicoherentOnSite_sectionTensor (M : ModuleCat.{max u r} (GlobalFunctionRing O)) :
    ((sectionTensorSheafFunctor.{u, v, max u r, u} O).obj M).IsQuasicoherentOnSite
```

## Tag 07V0, a lemma

[Tag 07V0](https://stacks.math.columbia.edu/tag/07V0) in the Stacks Project.

**`AlgebraicGeometry.Space.CohomologyVanishingSituation.isZero_rightDerived_one_globalSectionsFunctor_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingAffineMorphism.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingAffineMorphism.lean#L120). The attribute's comment: “part (1); cohomology of modules at the universe of the structure sheaf”.

> **Clause (1) of Stacks 07V0.** In the situation of Stacks 07UY, let `f : X' ⟶ X` be an affine
> morphism of algebraic spaces and let `𝓕'` be a quasi-coherent `𝒪_{X'}`-module.  Then
> `H¹(X', 𝓕') = 0`.

```lean
theorem isZero_rightDerived_one_globalSectionsFunctor_of_isAffineHom
    {X' : AlgebraicSpaces T.site T.base T.containsBase} (f : X' ⟶ T.space)
    (hf : IsAffineHom T.site T.base T.containsBase f.hom)
    (F : Modules.{u, u} T.site T.base T.containsBase X'.1 X'.2)
    (hF : F.IsQuasicoherentOnSite) :
    have := enoughInjectives_modules T.site T.base T.containsBase X'.1 X'.2
    IsZero (((globalSectionsFunctor.{u + 1, u, u, u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallEtaleRingedSite T.site T.base T.containsBase X'.1 X'.2).O)).rightDerived 1).obj F)
```

**`AlgebraicGeometry.Space.CohomologyVanishingSituation.isAffineHom_of_isPullback_toSpecGlobalFunctions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingBaseChange.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingBaseChange.lean#L133). The attribute's comment: “clause (2), the affineness assertion only: the projection X ×\_\{Spec A} Spec A' → X is affine. The computation Γ(X', 𝒪\_\{X'}) = A' of the same clause is NOT proved -- it needs the pushforward-computation assertion of Stacks 07U8, which the library's form of that tag does not carry. See this file's implementation notes, and for clause (1) see StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingAffine.lean”.

> **The affineness assertion of clause (2) of Stacks 07V0.** Let `X` be as in Stacks 07UY, let
> `A = Γ(X, 𝒪_X)`, and let `A'` be an `A`-algebra, presented by a morphism `q : W ⟶ V` of affine
> objects of the site over the presentation of `Spec A`.  Then the projection
> `X' = X ×_{Spec A} Spec A' ⟶ X` is affine.
>
> A morphism of affine objects of the site is an affine morphism of algebraic spaces, and affine
> morphisms are stable under base change, which is Stacks 03WI.

```lean
theorem isAffineHom_of_isPullback_toSpecGlobalFunctions
    {W : BigFppfOver T.site T.base T.containsBase}
    [IsAffine ((BigFppfOver.toScheme T.site T.base T.containsBase).obj W)]
    (q : W ⟶ V) {X' : AlgebraicSpaces T.site T.base T.containsBase}
    {pr : X' ⟶ T.space} {pr' : X' ⟶ _root_.AlgebraicGeometry.schemeSpace W}
    (sq : IsPullback pr' pr (_root_.AlgebraicGeometry.schemeSpaceMap q)
      (toSpecGlobalFunctions T hterminal V e)) :
    IsAffineHom T.site T.base T.containsBase pr.hom
```

**`AlgebraicGeometry.Space.CohomologyVanishingSituation.isAffineHom_and_bijective_of_isPullback_toSpecGlobalFunctionsOverIntegers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingBaseChangeGlobalFunctions.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingBaseChangeGlobalFunctions.lean#L168). The attribute's comment: “part (2); `Spec A'` is an affine object `W` of the site over the presentation `V` of `Spec A`”.

> **Clause (2) of Stacks 07V0.** Let `X` be as in Stacks 07UY, let `A = Γ(X, 𝒪_X)`, and let `A'`
> be an `A`-algebra, presented by a morphism `q : W ⟶ V` of affine objects of the site over the
> presentation `V` of `Spec A`.  Then the projection `X' = X ×_{Spec A} Spec A' ⟶ X` is affine and
> the canonical map `A' = Γ(W, 𝒪_W) ⟶ Γ(X', 𝒪_{X'})` is a bijection.

```lean
theorem isAffineHom_and_bijective_of_isPullback_toSpecGlobalFunctionsOverIntegers
    {W : BigFppfOver T.site (⊤_ Scheme.{u}) T.containsTerminal}
    [IsAffine ((BigFppfOver.toScheme T.site (⊤_ Scheme.{u}) T.containsTerminal).obj W)]
    (q : W ⟶ V) {X' : AlgebraicSpaces T.site (⊤_ Scheme.{u}) T.containsTerminal}
    {pr : X' ⟶ T.spaceOverIntegers} {pr' : X' ⟶ _root_.AlgebraicGeometry.schemeSpace W}
    (sq : IsPullback pr' pr (_root_.AlgebraicGeometry.schemeSpaceMap q)
      (toSpecGlobalFunctionsOverIntegers T V e)) :
    IsAffineHom T.site (⊤_ Scheme.{u}) T.containsTerminal pr.hom ∧
      Function.Bijective
        (pullbackToGlobalFunctions T.site (⊤_ Scheme.{u}) T.containsTerminal X' W pr')
```

## Tag 07V1, a lemma

[Tag 07V1](https://stacks.math.columbia.edu/tag/07V1) in the Stacks Project.

**`AlgebraicGeometry.exists_sub_one_mem_vanishingIdeal_of_disjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingSeparation.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingSeparation.lean#L335). The attribute's comment: “the conclusion for an affine scheme, with the two closed subsets taken in the scheme rather than in the points of an algebraic space”.

> **Two disjoint closed subsets of an affine scheme are separated by a global function.**
> The vanishing ideals of the two sets are comaximal, because the support of their join is the
> intersection of the two sets, so `1` is a sum `a + b` with `a` vanishing on the first set and
> `b` on the second; then `a - 1 = -b` vanishes on the second.

```lean
theorem exists_sub_one_mem_vanishingIdeal_of_disjoint (X : Scheme.{u}) [IsAffine X]
    {T₀ T₁ : Set X} (hT₀ : IsClosed T₀) (hT₁ : IsClosed T₁) (hdisj : Disjoint T₀ T₁) :
    ∃ a : Γ(X, ⊤), T₀ ⊆ X.zeroLocus {a} ∧ T₁ ⊆ X.zeroLocus {a - 1}
```

**`AlgebraicGeometry.Space.CohomologyVanishingSituation.exists_subset_compl_sectionSupport_of_disjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingSeparation.lean, line 768](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingSeparation.lean#L768). The attribute's comment: “the conclusion for an algebraic space, with the cohomology-vanishing hypothesis of Situation 07UY imposed at the module universe of the structure sheaf rather than at a general module universe”.

> **Stacks 07V1 for an algebraic space.** In the situation of Stacks 07UY, two disjoint closed
> subsets `Z₀, Z₁` of the points of `X` are separated by a global regular function: there is
> `a ∈ A = Γ(X, 𝒪_X)` with `Z₀ ⊆ V(a)` and `Z₁ ⊆ V(a - 1)`. The vanishing locus `V(-)` is the
> complement of `AlgebraicGeometry.Space.sectionSupport`, the set of points at which a global
> function does not vanish.
>
> The function is produced by
> `AlgebraicGeometry.Space.CohomologyVanishingSituation.exists_mem_definingIdealAt_and_sub_one_mem`
> applied to the reduced closed subspaces of Stacks 03IQ on `Z₀`, on `Z₁` and on `Z₀ ∪ Z₁`. Its two
> hypotheses are exactly the two statements about the defining ideal sheaves of reduced closed
> subspaces proved in
> `StacksFrontier/AlgebraicGeometry/Spaces/ReducedClosedSubspaceDefiningIdeal.lean`: the defining
> ideals of the subspaces on two *disjoint* closed sets are comaximal on every affine chart, and the
> defining ideal sheaves of the subspaces on `Z₀` and on `Z₁` meet in that of the subspace on
> `Z₀ ∪ Z₁`. The passage from the resulting ideal memberships to the point-set conclusion is
> `AlgebraicGeometry.Space.subset_compl_sectionSupport_of_forall_mem_definingIdealAt`.
>
> The situation is one at the module universe of the structure sheaf — see the implementation
> notes — because that is the form in which the lifting statement
> `AlgebraicGeometry.Space.CohomologyVanishingSituation.surjective_sectionsMap_of_epi` is
> available.

```lean
theorem exists_subset_compl_sectionSupport_of_disjoint
    {Z₀ Z₁ : Set (points T'.site T'.base T'.containsBase T'.space.1)}
    (hZ₀ : IsClosed Z₀) (hZ₁ : IsClosed Z₁) (hdisj : Disjoint Z₀ Z₁) :
    ∃ a : _root_.AlgebraicGeometry.Space.globalFunctions
        T'.site T'.base T'.containsBase T'.space.1,
      Z₀ ⊆ (_root_.AlgebraicGeometry.Space.sectionSupport
          T'.site T'.base T'.containsBase T'.space.1 a)ᶜ ∧
        Z₁ ⊆ (_root_.AlgebraicGeometry.Space.sectionSupport
          T'.site T'.base T'.containsBase T'.space.1 (a - 1))ᶜ
```

## Tag 07V4, a lemma

[Tag 07V4](https://stacks.math.columbia.edu/tag/07V4) in the Stacks Project.

**`AlgebraicGeometry.Space.CohomologyVanishingSituation.pointsToScheme_pointsMap_toSpecGlobalFunctions_ne_of_isClosed_of_ne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingClosedPoints.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingClosedPoints.lean#L190). The attribute's comment: “the final step of the source proof only: in Situation 07UY the morphism p : X -> Spec A separates the closed points of |X|, two distinct closed points of |X| having distinct images. Universal injectivity of p, which is the assertion of the tag, is NOT proved by this declaration, and neither is injectivity of p on all of |X|; see universallyInjective\_toSpecGlobalFunctions in this same file, which does state universal injectivity and carries the two steps that are missing. The source reaches universal injectivity from this step by three reductions, none of them available in this development. Clause (2) of Stacks 07V0 reduces to the case of a field A, but its library form -- isAffineHom\_of\_isPullback\_toSpecGlobalFunctions -- carries the affineness assertion only and not the computation Gamma(X', O\_X') = A' that the reduction needs. Stacks 0488 then replaces the field by a large algebraically closed extension and Stacks 07U5 makes the resulting field-valued points closed points of |X|, but the library's 07U5 -- isClosed\_singleton\_class\_of\_isAlgebraic\_residueField -- requires the field of the point to be algebraic over the residue field at a closed point of the base, which is exactly what the first reduction would have arranged. And the source's passage from one point of |X| to one field-valued point of X is left implicit there. IsTerminal T'.base, the affine object V and the isomorphism e are inherited from the signature of toSpecGlobalFunctions, as for the neighbouring Stacks 07V5”.

> **The canonical morphism to `Spec A` separates the closed points of `|X|`.** In the
> situation of Stacks 07UY, two distinct closed points of `|X|` have distinct images in `Spec A`
> under `p : X ⟶ Spec A`, where `Spec A` is presented by an affine object `V` of the site through
> a ring isomorphism `Γ(V, 𝒪_V) ≅ A = Γ(X, 𝒪_X)`.
>
> Stacks 07V1 supplies `a ∈ A` vanishing at the first point and taking the value `1` at the
> second; if the two images agreed, that point of `Spec A` would lie in neither the nonvanishing
> locus of `a` nor that of `a - 1`, which no point of a scheme does.

```lean
theorem pointsToScheme_pointsMap_toSpecGlobalFunctions_ne_of_isClosed_of_ne
    {x y : points T'.site T'.base T'.containsBase T'.space.1}
    (hx : IsClosed ({x} : Set (points T'.site T'.base T'.containsBase T'.space.1)))
    (hy : IsClosed ({y} : Set (points T'.site T'.base T'.containsBase T'.space.1)))
    (hxy : x ≠ y) :
    pointsToScheme T'.site T'.base T'.containsBase V
        (pointsMap T'.site T'.base T'.containsBase T'.space.1
          (toSpecGlobalFunctions T' hterminal V e).hom x) ≠
      pointsToScheme T'.site T'.base T'.containsBase V
        (pointsMap T'.site T'.base T'.containsBase T'.space.1
          (toSpecGlobalFunctions T' hterminal V e).hom y)
```

**`AlgebraicGeometry.Space.CohomologyVanishingSituation.universallyInjective_toSpecGlobalFunctionsOverIntegers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingUniversallyInjective.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingUniversallyInjective.lean#L132).

> **Stacks 07V4.** In the situation of Stacks 07UY, over an arbitrary base scheme `S`, the
> canonical morphism `p : X ⟶ Spec A` is universally injective.  As in the source, `p` is the
> morphism of Stacks 05Z1 formed after regarding `X` as an algebraic space over `Spec ℤ`, and
> `Spec A` is presented by an affine object `V` of the site through a ring isomorphism
> `Γ(V, 𝒪_V) ≅ A = Γ(X, 𝒪_X)`.
>
> The view of `X` over `Spec ℤ` has the same small étale ringed site, hence the same global
> functions and right exact global sections, and it is quasi-compact and quasi-separated; the
> statement is then
> `AlgebraicGeometry.Space.universallyInjective_of_surjective_pullbackToGlobalFunctions`.

```lean
theorem universallyInjective_toSpecGlobalFunctionsOverIntegers :
    _root_.AlgebraicGeometry.Space.UniversallyInjective T.site (⊤_ Scheme.{u}) T.containsTerminal
      (toSpecGlobalFunctionsOverIntegers T V e).hom
```

## Tag 07V5, a lemma

[Tag 07V5](https://stacks.math.columbia.edu/tag/07V5) in the Stacks Project.

**`AlgebraicGeometry.Space.CohomologyVanishingSituation.isSeparated_toSpecGlobalFunctions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingSeparatedMorphism.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingSeparatedMorphism.lean#L187). The attribute's comment: “two inputs are carried as named hypotheses -- h09YB, clause (1) of Stacks 09YB, and h07V0, clause (1) of Stacks 07V0 for a scheme of the site affine over X with its first cohomology read in the Zariski topology of that scheme. IsTerminal T.base is inherited from the signature of toSpecGlobalFunctions. See this file's implementation notes”.

> **Stacks 07V5.** In the situation of Stacks 07UY, the canonical morphism
> `p : X ⟶ Spec Γ(X, 𝒪_X)` is separated, `Spec Γ(X, 𝒪_X)` being presented by an affine object `V`
> of the site through a ring isomorphism `Γ(V, 𝒪_V) ≅ Γ(X, 𝒪_X)`.

```lean
theorem isSeparated_toSpecGlobalFunctions
    (h09YB : ExistsIntegralSurjectiveSchemeCover T.site T.base T.containsBase T.space.1)
    (h07V0 : SchemeAffineOverFirstZariskiCohomologyVanishing T.site T.base T.containsBase
      T.space.1) :
    IsSeparated T.site T.base T.containsBase
      (toSpecGlobalFunctions T hterminal V e).hom
```

**`AlgebraicGeometry.Space.CohomologyVanishingSituation.isSeparated_toSpecGlobalFunctionsOverIntegers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedOverGlobalFunctions.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedOverGlobalFunctions.lean#L116).

> **Stacks 07V5.** In the situation of Stacks 07UY, over an arbitrary base scheme `S`, the
> canonical morphism `p : X ⟶ Spec A` is separated.  As in the source, `p` is the morphism of
> Stacks 05Z1 formed after regarding `X` as an algebraic space over `Spec ℤ`, and `Spec A` is
> presented by an affine object `V` of the site through a ring isomorphism
> `Γ(V, 𝒪_V) ≅ A = Γ(X, 𝒪_X)`.
>
> The view of `X` over `Spec ℤ` has right exact global sections on quasi-coherent modules and is
> quasi-compact and quasi-separated, and every global function on it is pulled back along `p`;
> the statement is then
> `AlgebraicGeometry.Space.isSeparated_of_surjective_pullbackToGlobalFunctions`.

```lean
theorem isSeparated_toSpecGlobalFunctionsOverIntegers :
    IsSeparated T.site (⊤_ Scheme.{u}) T.containsTerminal
      (toSpecGlobalFunctionsOverIntegers T V e).hom
```

## Tag 07V6, a proposition

[Tag 07V6](https://stacks.math.columbia.edu/tag/07V6) in the Stacks Project.

**`AlgebraicGeometry.Space.CohomologyVanishingSituation.isAffineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffinenessCriteria.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffinenessCriteria.lean#L63). The attribute's comment: “more precisely: an algebraic space as in Situation 07UY is an affine scheme”.

> **Stacks 07V6, more precisely.** An algebraic space in the situation of Stacks 07UY is an
> affine scheme: it is represented by an object of the site over the base whose underlying scheme
> is affine.

```lean
theorem isAffineSpace (T : CohomologyVanishingSituation.{u, u}) :
    IsAffineSpace T.site T.base T.containsBase T.space.1
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isAffineSpace_iff_forall_isZero_rightDerived`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingAffineness.lean#L493), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/AffinenessCriteria.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffinenessCriteria.lean#L48) (StacksFrontier): “first sentence: a quasi-compact and quasi-separated algebraic space is affine iff the higher cohomology of its quasi-coherent modules vanishes”.

## Tag 0D2V, a lemma

[Tag 0D2V](https://stacks.math.columbia.edu/tag/0D2V) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isAffineSpace_of_forall_isCoherent_isZero_rightDerived_one`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyVanishingNoetherianAffine.lean#L181), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/AffinenessCriteria.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffinenessCriteria.lean#L52) (StacksFrontier).

## Tag 0D2W, a lemma

[Tag 0D2W](https://stacks.math.columbia.edu/tag/0D2W) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isAmple_of_forall_isCoherent_isZero_rightDerived_one_twistStep`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologicalAmplenessCriterion.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohomologicalAmplenessCriterion.lean#L201).

> **Stacks 0D2W.**  Let `S` be a scheme, `X` a Noetherian algebraic space over `S` and `𝓛` an
> invertible `𝒪_X`-module.  If every coherent `𝒪_X`-module `𝓕` has some `n ≥ 1` with
> `H¹(X, 𝓕 ⊗ 𝓛^{⊗ n}) = 0`, then `X` is a scheme and `𝓛` is ample on it: there are an object `U`
> of the site and an isomorphism `yoneda.obj U ≅ X` for which the restriction of `𝓛` to the scheme
> underlying `U` is an invertible and ample module.  See the module docstring.

```lean
theorem exists_isAmple_of_forall_isCoherent_isZero_rightDerived_one_twistStep
    (hZ : B.Contains (⊤_ Scheme.{u})) (X : AlgebraicSpaces B S hS)
    (hN : IsNoetherian B S hS hZ X.1) (L : Modules.{u, u} B S hS X.1 X.2)
    [hL : Stacks.SheafOfModules.IsInvertible (structurePresheaf B S hS X.1)
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O).property L]
    (h : have := enoughInjectives_modules B S hS X.1 X.2
      ∀ F : Modules.{u, u} B S hS X.1 X.2, IsCoherent B S hS X.1 X.2 F →
        ∃ n : ℕ, 1 ≤ n ∧ IsZero (((globalSectionsFunctor.{u + 1, u, u, u}
          (Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS X.1 X.2).O)).rightDerived 1).obj
            (twistStep B S hS X.1 X.2 L n F))) :
    ∃ (U : BigFppfOver B S hS) (eX : yoneda.obj U ≅ X.1)
      (_ : Stacks.Ample.IsInvertibleModule ((BigFppfOver.toScheme B S hS).obj U)
        (baseChangeModule B S hS L U eX.hom)),
      Stacks.Ample.IsAmple ((BigFppfOver.toScheme B S hS).obj U)
        (baseChangeModule B S hS L U eX.hom)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.16, Tag 07UX](https://stacks.math.columbia.edu/tag/07UX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
