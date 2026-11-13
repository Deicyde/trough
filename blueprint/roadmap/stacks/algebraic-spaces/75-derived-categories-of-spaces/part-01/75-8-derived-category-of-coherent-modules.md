---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.coherentDerivedComparison_mem, AlgebraicGeometry.Space.coherentDerivedComparison, AlgebraicGeometry.Space.coherentDerivedComparisonCompιIso, AlgebraicGeometry.Space.derivedCategoryBBounded_derivedModulePushforward_of_hasProperSupport, AlgebraicGeometry.Space.derivedCategoryBPlus_derivedModulePushforward_of_hasProperSupport, AlgebraicGeometry.Space.isBoundedBelow_sheafHomComplex, AlgebraicGeometry.Space.isBoundedBelow_derivedSheafHomOnSpace, AlgebraicGeometry.Space.derivedCategoryBPlus_isCoherentOnSite_sheafHomComplex
statement: formalized
proof: formalized
---

# 75.8 Derived category of coherent modules

Section 75.8 of the Stacks Project, [Tag 08GI](https://stacks.math.columbia.edu/tag/08GI). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08GJ, an equation

[Tag 08GJ](https://stacks.math.columbia.edu/tag/08GJ) in the Stacks Project.

**`AlgebraicGeometry.Space.coherentDerivedComparison_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentDerivedComparison.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoherentDerivedComparison.lean#L210). The attribute's comment: “well-definedness”.

> **Stacks 08GJ, well-definedness.**  The derived functor of the inclusion of the coherent
> `𝒪_F`-modules has coherent cohomology in every degree: the inclusion is exact, so it commutes
> with cohomology.

```lean
theorem coherentDerivedComparison_mem (K : DerivedCategory (CoherentModules.{u, u} B S hS F hF)) :
    DerivedCategoryB.derivedCategoryB (isCoherent.{u, u} B S hS F hF)
      ((isCoherent.{u, u} B S hS F hF).ι.mapDerivedCategory.obj K)
```

**`AlgebraicGeometry.Space.coherentDerivedComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentDerivedComparison.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoherentDerivedComparison.lean#L226).

> **Stacks 08GJ.**  The canonical functor from the derived category of the coherent
> `𝒪_F`-modules to the derived category of all `𝒪_F`-modules with coherent cohomology,
>
> `D(Coh(𝒪_F)) ⟶ D_Coh(𝒪_F)`,
>
> obtained by factoring the derived functor of the exact inclusion `Coh(𝒪_F) ⥤ Mod(𝒪_F)` through
> `D_Coh(𝒪_F)`.

```lean
noncomputable def coherentDerivedComparison :
    DerivedCategory (CoherentModules.{u, u} B S hS F hF) ⥤
      CoherentDerivedCategory.{u} B S hS F hF
```

**`AlgebraicGeometry.Space.coherentDerivedComparisonCompιIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentDerivedComparison.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoherentDerivedComparison.lean#L237). The attribute's comment: “canonical comparison”.

> **Stacks 08GJ, the canonical comparison.**  The functor `D(Coh(𝒪_F)) ⥤ D_Coh(𝒪_F)` followed
> by the inclusion of `D_Coh(𝒪_F)` into `D(𝒪_F)` is the derived functor of the inclusion
> `Coh(𝒪_F) ⥤ Mod(𝒪_F)`; that is, the comparison is a factorisation of the latter.

```lean
noncomputable def coherentDerivedComparisonCompιIso :
    coherentDerivedComparison B S hS F hF ⋙
        (DerivedCategoryB.derivedCategoryB (isCoherent.{u, u} B S hS F hF)).ι ≅
      (isCoherent.{u, u} B S hS F hF).ι.mapDerivedCategory
```

## Tag 08GK, a lemma

[Tag 08GK](https://stacks.math.columbia.edu/tag/08GK) in the Stacks Project.

**`AlgebraicGeometry.Space.derivedCategoryBBounded_derivedModulePushforward_of_hasProperSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedPushforwardCoherentProperSupport.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedPushforwardCoherentProperSupport.lean#L154).

> Let `S` be a scheme and `f : X ⟶ Y` a morphism of algebraic spaces over `S` which is locally
> of finite type, with `Y` Noetherian.  Let `E ∈ D^b_{Coh}(𝒪_X)` be such that the support of
> `H^i(E)` is proper over `Y` for all `i`.  Then `Rf_*E ∈ D^b_{Coh}(𝒪_Y)`.

```lean
theorem derivedCategoryBBounded_derivedModulePushforward_of_hasProperSupport
    (hTop : B.Contains (⊤_ Scheme.{u})) (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f.hom)
    (hY : IsNoetherian B S hS hTop Y.1)
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hE : derivedCategoryBBounded (isCoherent.{u, u} B S hS X.1 X.2) E)
    (hsupp : ∀ i : ℤ, HasProperSupport B S hS X.2 Y.2 f.hom hf
      ((SheafOfModules.toSheaf _).obj
        ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X.1 X.2) i).obj E))) :
    derivedCategoryBBounded (isCoherent.{u, u} B S hS Y.1 Y.2)
      ((Stacks.DerivedFunctor.totalRightDerived (modulePushforward B S hS f)).obj E)
```

## Tag 0D0R, a lemma

[Tag 0D0R](https://stacks.math.columbia.edu/tag/0D0R) in the Stacks Project.

**`AlgebraicGeometry.Space.derivedCategoryBPlus_derivedModulePushforward_of_hasProperSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedPushforwardCoherentProperSupport.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedPushforwardCoherentProperSupport.lean#L182). The attribute's comment: “with the support of each H^i(E) proper over Y: proper over S, as printed, the statement fails (the open immersion of one chart P^1 into the projective line with doubled origin over a field, with E = O\_X), and Y is what the source's proof, through 08GK, uses”.

> Let `S` be a scheme and `f : X ⟶ Y` a morphism of algebraic spaces over `S` which is locally
> of finite type, with `Y` Noetherian.  Let `E ∈ D^+_{Coh}(𝒪_X)` be such that the support of
> `H^i(E)` is proper over `Y` for all `i`.  Then `Rf_*E ∈ D^+_{Coh}(𝒪_Y)`.  (With the support
> only proper over `S` the statement is false; see the module documentation.)

```lean
theorem derivedCategoryBPlus_derivedModulePushforward_of_hasProperSupport
    (hTop : B.Contains (⊤_ Scheme.{u})) (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f.hom)
    (hY : IsNoetherian B S hS hTop Y.1)
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hE : derivedCategoryBPlus (isCoherent.{u, u} B S hS X.1 X.2) E)
    (hsupp : ∀ i : ℤ, HasProperSupport B S hS X.2 Y.2 f.hom hf
      ((SheafOfModules.toSheaf _).obj
        ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X.1 X.2) i).obj E))) :
    derivedCategoryBPlus (isCoherent.{u, u} B S hS Y.1 Y.2)
      ((Stacks.DerivedFunctor.totalRightDerived (modulePushforward B S hS f)).obj E)
```

## Tag 0D0S, a lemma

[Tag 0D0S](https://stacks.math.columbia.edu/tag/0D0S) in the Stacks Project.

**`AlgebraicGeometry.Space.isBoundedBelow_sheafHomComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentDerivedInternalHom.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoherentDerivedInternalHom.lean#L269). The attribute's comment: “the bounded-below clause, on a pair of models and with no Noetherian or coherence hypothesis”.

> **Stacks 0D0S, the bounded-below clause, on a pair of models.** If `A` is concentrated in
> degrees `≤ d` and `J` in degrees `≥ b`, the class of the internal Hom complex `SheafHom(A, J)`
> in `D(𝒪_X)` is cohomologically bounded below.
>
> For `A` a model of `K` and `J` a K-injective model of `L` this object is `RSheafHom(K, L)`, so
> this is the `D⁺` half of the tag, with no hypothesis beyond the two bounds — neither local
> Noetherianity nor coherence of the cohomology of `K` and `L`.

```lean
public theorem isBoundedBelow_sheafHomComplex
    (d b : ℤ) (A J : CochainComplex (Modules.{u, max (u + 1) m} B S hS F hF) ℤ)
    [CochainComplex.IsStrictlyLE A d] [CochainComplex.IsStrictlyGE J b] :
    DerivedCategoryB.IsBoundedBelow
      (DerivedCategory.Q.obj
        (sheafHomComplex (smallEtaleRingedSite B S hS F hF) A J).obj)
```

**`AlgebraicGeometry.Space.isBoundedBelow_derivedSheafHomOnSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentDerivedInternalHom.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoherentDerivedInternalHom.lean#L319). The attribute's comment: “the bounded-below clause, for K and L themselves and with no Noetherian hypothesis”.

> **Stacks 0D0S, the bounded-below clause.** Let `X` be an algebraic space over `S`. If `K` is
> in `D⁻_Coh(𝒪_X)` and `L` is in `D⁺_Coh(𝒪_X)`, then `RSheafHom(K, L)` is cohomologically bounded
> below.
>
> `RSheafHom(K, L)` is the class of the internal Hom complex `SheafHom(A, J)` of a model `A` of
> `K` and a K-injective model `J` of `L`; such a pair exists by
> `AlgebraicGeometry.Space.exists_isStrictlyLE_isStrictlyGE_isKInjective_model`, and the
> conclusion holds for it, by `AlgebraicGeometry.Space.isBoundedBelow_sheafHomComplex`.
>
> Only the boundedness halves of `hK` and `hL` are used, and local Noetherianity of `X` is not
> needed.

```lean
public theorem isBoundedBelow_derivedSheafHomOnSpace
    (K L : DerivedCategory (Modules.{u, max (u + 1) m} B S hS F hF))
    (hK : DerivedCategoryB.derivedCategoryBMinus
      (fun N : Modules.{u, max (u + 1) m} B S hS F hF =>
        SheafOfModules.IsCoherentOnSite N) K)
    (hL : DerivedCategoryB.derivedCategoryBPlus
      (fun N : Modules.{u, max (u + 1) m} B S hS F hF =>
        SheafOfModules.IsCoherentOnSite N) L) :
    ∃ A J : CochainComplex (Modules.{u, max (u + 1) m} B S hS F hF) ℤ,
      CochainComplex.IsKInjective J ∧ Nonempty (DerivedCategory.Q.obj A ≅ K) ∧
        Nonempty (DerivedCategory.Q.obj J ≅ L) ∧
        DerivedCategoryB.IsBoundedBelow
          (DerivedCategory.Q.obj
            (sheafHomComplex (smallEtaleRingedSite B S hS F hF) A J).obj)
```

**`AlgebraicGeometry.Space.derivedCategoryBPlus_isCoherentOnSite_sheafHomComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentDerivedInternalHomCoherentCohomology.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoherentDerivedInternalHomCoherentCohomology.lean#L151). The attribute's comment: “read on a model of K and a K-injective model of L”.

> **Stacks 0D0S.** On a locally Noetherian algebraic space, `RSheafHom(K, L)` lies in
> `D⁺_Coh(𝒪_X)` for `K` in `D⁻_Coh(𝒪_X)` and `L` in `D⁺_Coh(𝒪_X)`, read on a model `A` of `K` and
> a K-injective model `J` of `L`.

```lean
theorem derivedCategoryBPlus_isCoherentOnSite_sheafHomComplex
    [HasDerivedCategory.{t} (Modules.{u, u + 1} B S hS X.1 X.2)]
    (hN : HasEtaleLocalProperty B S hS X.1 (fun V : Scheme.{u} ↦ IsLocallyNoetherian V))
    (d b : ℤ) (A J : CochainComplex (Modules.{u, u} B S hS X.1 X.2) ℤ)
    [CochainComplex.IsStrictlyLE A d] [CochainComplex.IsKInjective J]
    [CochainComplex.IsStrictlyGE J b]
    (hA : ∀ i, SheafOfModules.IsCoherentOnSite (A.homology i))
    (hJ : ∀ i, SheafOfModules.IsCoherentOnSite (J.homology i)) :
    DerivedCategoryB.derivedCategoryBPlus
      (fun N : Modules.{u, u + 1} B S hS X.1 X.2 => SheafOfModules.IsCoherentOnSite N)
      (DerivedCategory.Q.obj
        (sheafHomComplex (smallEtaleRingedSite B S hS X.1 X.2) A J).obj)
```

## Tag 0D0T, a lemma

[Tag 0D0T](https://stacks.math.columbia.edu/tag/0D0T) in the Stacks Project.

**`AlgebraicGeometry.Space.moduleFinite_hom_shift_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperExtFiniteComplexes.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProperExtFiniteComplexes.lean#L223).

> **Stacks 0D0T.**  Let `A` be a Noetherian ring and `X` an algebraic space over `A` proper over
> `A`.  Let `K ∈ D⁻_Coh(𝒪_X)` and `L ∈ D⁺_Coh(𝒪_X)`.  Then `Ext^n_X(K, L) = Hom_{D(𝒪_X)}(K, L[n])`
> is a finite `A`-module for every `n ∈ ℤ`.

```lean
theorem moduleFinite_hom_shift_of_isProper [IsNoetherianRing A]
    (f : X ⟶ yoneda.obj (baseObject A B hA)) (hf : IsProper B (Spec (.of A)) hA f)
    (K L : DerivedCategory (Modules.{u, u} B (Spec (.of A)) hA X hX))
    (hK : DerivedCategoryB.derivedCategoryBMinus (isCoherent.{u, u} B (Spec (.of A)) hA X hX) K)
    (hL : DerivedCategoryB.derivedCategoryBPlus (isCoherent.{u, u} B (Spec (.of A)) hA X hX) L)
    (n : ℤ) : Module.Finite A (K ⟶ L⟦n⟧)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.8, Tag 08GI](https://stacks.math.columbia.edu/tag/08GI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
