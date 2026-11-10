---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_of_hasProperSupport, AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_derivedTensor, AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_derivedSheafHom
statement: formalized
proof: formalized
---

# 75.22 Producing perfect complexes

Section 75.22 of the Stacks Project, [Tag 0A1L](https://stacks.math.columbia.edu/tag/0A1L). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08IS, a lemma

[Tag 08IS](https://stacks.math.columbia.edu/tag/08IS) in the Stacks Project.

**`AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_of_hasProperSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectDirectImage.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectDirectImage.lean#L208). References: SGA 6 IV (2.12), “partial”.

> **Perfect direct images.**  Let `S` be a scheme, `Y` a Noetherian algebraic space over `S` and
> `f : X ⟶ Y` a morphism of algebraic spaces which is locally of finite type and quasi-separated.
> Let `E ∈ D(𝒪_X)` be such that
>
> 1. `E ∈ D^b_{Coh}(𝒪_X)`,
> 2. the support of `Hⁱ(E)` is proper over `Y` for all `i`,
> 3. `E` has finite tor dimension as an object of `D(f⁻¹𝒪_Y)`.
>
> Then `Rf_*E` is a perfect object of `D(𝒪_Y)`.
>
> `Rf_*` is the total right derived functor of the direct image of modules, and the tor dimension
> of `E`, read in `D(f⁻¹𝒪_Y)` by restriction of scalars along `f♯ : f⁻¹𝒪_Y ⟶ 𝒪_X`, is measured
> against any derived tensor product `T` on `f⁻¹𝒪_Y`-modules (they all agree, being characterized
> by their values on K-flat complexes).

```lean
theorem isPerfect_derivedModulePushforward_of_hasProperSupport
    (hTop : B.Contains (⊤_ Scheme.{u})) (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f.hom)
    (hfqs : IsQuasiSeparated B S hS f.hom) (hY : IsNoetherian B S hS hTop Y.1)
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hE : derivedCategoryBBounded (isCoherent.{u, u} B S hS X.1 X.2) E)
    (hsupp : ∀ i : ℤ, HasProperSupport B S hS X.2 Y.2 f.hom hf
      ((SheafOfModules.toSheaf _).obj
        ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X.1 X.2) i).obj E)))
    (T : Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, u, u + 1}
      (inverseImageRingedSite B S hS f))
    (hTor : Stacks.SheafOfModules.DerivedTensorProduct.HasFiniteTorDimension.{u + 1, u, u, u + 1} T
      ((derivedScalarRestriction B S hS f).obj E)) :
    (smallEtaleRingedSite B S hS Y.1 Y.2).IsPerfect
      ((Stacks.DerivedFunctor.totalRightDerived (modulePushforward B S hS f)).obj E)
```

## Tag 0DKJ, a lemma

[Tag 0DKJ](https://stacks.math.columbia.edu/tag/0DKJ) in the Stacks Project.

**`AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectPushforwardTensor.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectPushforwardTensor.lean#L90).

> **Stacks 0DKJ.**  Let `Y` be a Noetherian algebraic space and `f : X ⟶ Y` a morphism locally
> of finite type and quasi-separated.  Let `E` be a perfect object of `D(𝒪_X)` and `𝒢^•` a bounded
> complex of coherent `𝒪_X`-modules, flat over `Y`, with support proper over `Y`.  Then
> `Rf_*(E ⊗^L_{𝒪_X} 𝒢^•)` is a perfect object of `D(𝒪_Y)`, for any derived tensor product
> `⊗^L` on `D(𝒪_X)`.

```lean
theorem isPerfect_derivedModulePushforward_derivedTensor (hTop : B.Contains (⊤_ Scheme.{u}))
    (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hY : IsNoetherian B S hS hTop Y.1)
    (T : Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, u, u + 1}
      (smallEtaleRingedSite B S hS X.1 X.2))
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hE : (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect E)
    (G : CochainComplex (Modules.{u, u} B S hS X.1 X.2) ℤ)
    (hG : FlatProperSupportComplex B S hS f hf G) :
    (smallEtaleRingedSite B S hS Y.1 Y.2).IsPerfect
      ((Stacks.DerivedFunctor.totalRightDerived (modulePushforward B S hS f)).obj
        ((T.tensor.obj E).obj (DerivedCategory.Q.obj G)))
```

## Tag 0DKK, a lemma

[Tag 0DKK](https://stacks.math.columbia.edu/tag/0DKK) in the Stacks Project.

**`AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_derivedSheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectPushforwardInternalHom.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectPushforwardInternalHom.lean#L62).

> **Stacks 0DKK.**  Let `Y` be a Noetherian algebraic space and `f : X ⟶ Y` a morphism locally
> of finite type and quasi-separated.  Let `E` be a perfect object of `D(𝒪_X)` and `𝒢^•` a bounded
> complex of coherent `𝒪_X`-modules, flat over `Y`, with support proper over `Y`.  Then
> `Rf_* RSheafHom(E, 𝒢^•)` is a perfect object of `D(𝒪_Y)`.

```lean
theorem isPerfect_derivedModulePushforward_derivedSheafHom (hTop : B.Contains (⊤_ Scheme.{u}))
    (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hY : IsNoetherian B S hS hTop Y.1)
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hE : (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect E)
    (G : CochainComplex (Modules.{u, u} B S hS X.1 X.2) ℤ)
    (hG : FlatProperSupportComplex B S hS f hf G) :
    (smallEtaleRingedSite B S hS Y.1 Y.2).IsPerfect
      ((Stacks.DerivedFunctor.totalRightDerived (modulePushforward B S hS f)).obj
        (((RingedSite.derivedSheafHomSmallBifunctor (smallEtaleRingedSite B S hS X.1 X.2)).obj
          (op E)).obj (DerivedCategory.Q.obj G)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.22, Tag 0A1L](https://stacks.math.columbia.edu/tag/0A1L)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
