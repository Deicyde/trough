---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSite.derivedCategoryB_tensorWithComplexDerived_obj_scheme, AlgebraicGeometry.RingedSite.derivedCategoryB_isQuasicoherent_tensorWithComplexDerived_obj_scheme, AlgebraicGeometry.exists_differentialGradedAlgebra_quasiCoherentDerivedCategory_equivalence, Stacks.Duality.SupportedGeneration.exists_dga_equivalence_quasiCoherentSupported, AlgebraicGeometry.exists_dga_quasiCoherentDerived_linearEquivalence_and_derivedTensor_iso
statement: formalized
proof: formalized
---

# 36.18 Derived categories as module categories

Section 36.18 of the Stacks Project, [Tag 09M2](https://stacks.math.columbia.edu/tag/09M2). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09M3, a lemma

[Tag 09M3](https://stacks.math.columbia.edu/tag/09M3) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.derivedCategoryB_tensorWithComplexDerived_obj_scheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexQuasicoherentAdjoint.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexQuasicoherentAdjoint.lean#L262). The attribute's comment: “for the site of opens of the scheme”.

> **Stacks 09M3.** *"Let `X` be a scheme, `K` a complex of `O_X`-modules with quasi-coherent
> cohomology sheaves, `(E, d) = Hom(K, K)`. Then `- ⊗_E^𝐋 K : D(E, d) ⟶ D(O_X)` of Tag 09LX has
> image contained in `D_QCoh(O_X)`."* The scheme is read as the ringed site of its opens.

```lean
theorem derivedCategoryB_tensorWithComplexDerived_obj_scheme (Y : Scheme.{u})
    (K : CochainComplex (ModO.{u, u, u, u}
      (Stacks.AlgebraicGeometry.ReflexiveModules.schemeRingedSite Y)) ℤ)
    (hK : tensorModOQuasicoherentDerived.{u, u, u, u, u}
      (Stacks.AlgebraicGeometry.ReflexiveModules.schemeRingedSite Y)
      (DerivedCategory.Q.obj (liftComplex.{u, u, u, u, u}
        (Stacks.AlgebraicGeometry.ReflexiveModules.schemeRingedSite Y) K)))
    (M : DifferentialGradedModule.derivedCategory.{0, u, u}
      (Rep.{u, u, u, u, u, 0}
        (Stacks.AlgebraicGeometry.ReflexiveModules.schemeRingedSite Y) ℤ K).algebra) :
    tensorModOQuasicoherentDerived.{u, u, u, u, u}
      (Stacks.AlgebraicGeometry.ReflexiveModules.schemeRingedSite Y)
      ((tensorWithComplexDerived.{u, u, u, u, u, 0}
        (Stacks.AlgebraicGeometry.ReflexiveModules.schemeRingedSite Y) ℤ K).obj M)
```

**`AlgebraicGeometry.RingedSite.derivedCategoryB_isQuasicoherent_tensorWithComplexDerived_obj_scheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexQuasicoherentAdjoint.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexQuasicoherentAdjoint.lean#L284).

> **Stacks 09M3.** Every cohomology sheaf of `M ⊗_E^𝐋 K` is a quasi-coherent `O_Y`-module, for
> `Y` a scheme and `K` a complex of `O_Y`-modules with quasi-coherent cohomology sheaves.

```lean
theorem derivedCategoryB_isQuasicoherent_tensorWithComplexDerived_obj_scheme (Y : Scheme.{u})
    (K : CochainComplex (ModO.{u, u, u, u}
      (Stacks.AlgebraicGeometry.ReflexiveModules.schemeRingedSite Y)) ℤ)
    (hK : tensorModOQuasicoherentDerived.{u, u, u, u, u}
      (Stacks.AlgebraicGeometry.ReflexiveModules.schemeRingedSite Y)
      (DerivedCategory.Q.obj (liftComplex.{u, u, u, u, u}
        (Stacks.AlgebraicGeometry.ReflexiveModules.schemeRingedSite Y) K)))
    (M : DifferentialGradedModule.derivedCategory.{0, u, u}
      (Rep.{u, u, u, u, u, 0}
        (Stacks.AlgebraicGeometry.ReflexiveModules.schemeRingedSite Y) ℤ K).algebra) :
    DerivedCategoryB.derivedCategoryB
        (A := TensorModO.{u, u, u, u, u}
          (Stacks.AlgebraicGeometry.ReflexiveModules.schemeRingedSite Y))
        (SheafOfModules.isQuasicoherent Y.ringCatSheaf)
      ((tensorWithComplexDerived.{u, u, u, u, u, 0}
        (Stacks.AlgebraicGeometry.ReflexiveModules.schemeRingedSite Y) ℤ K).obj M)
```

## Tag 09M5, a theorem

[Tag 09M5](https://stacks.math.columbia.edu/tag/09M5) in the Stacks Project.

**`AlgebraicGeometry.exists_differentialGradedAlgebra_quasiCoherentDerivedCategory_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/QuasiCoherentDerived/DGAModel.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/QuasiCoherentDerived/DGAModel.lean#L250).

> **Stacks 09M5** (Bondal–van den Bergh). *Let `X` be a quasi-compact and quasi-separated
> scheme. Then there exist a differential graded algebra `(E, d)` with only a finite number of
> nonzero cohomology groups `H^i(E)` such that `D_QCoh(O_X)` is equivalent to `D(E, d)`.*
>
> `D_QCoh(O_X)` is the full subcategory of the derived category of `O_X`-modules — at an arbitrary
> chosen model — of the objects all of whose cohomology sheaves are quasi-coherent, and `D(E, d)` is
> the derived category of differential graded `E`-modules. The algebra is an algebra over `ℤ`, the
> endomorphism algebra `Hom_{Comp^dg(O_X)}(K^•, K^•)` of a K-injective perfect generator `K^•` of
> `D_QCoh(O_X)`; the equivalence is the derived tensor product `- ⊗_E^𝐋 K^•` of Tag 09LX, see
> `AlgebraicGeometry.exists_isKInjective_tensorWithComplexDerived_lift_isEquivalence`, followed by
> the comparison of the standard model with the chosen one.

```lean
theorem exists_differentialGradedAlgebra_quasiCoherentDerivedCategory_equivalence
    (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X] [HasDerivedCategory X.Modules] :
    ∃ E : DifferentialGradedAlgebra.{0, u} ℤ,
      {i : ℤ | Nontrivial (E.Cohomology i)}.Finite ∧
        Nonempty ((DerivedCategoryB.derivedCategoryB (A := X.Modules)
          (SheafOfModules.isQuasicoherent X.ringCatSheaf)).FullSubcategory ≌
            DifferentialGradedModule.derivedCategory.{0, u, u} E)
```

## Tag 0DJL, a remark

[Tag 0DJL](https://stacks.math.columbia.edu/tag/0DJL) in the Stacks Project.

**`Stacks.Duality.SupportedGeneration.exists_dga_equivalence_quasiCoherentSupported`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/SupportedDGAModel.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/SupportedDGAModel.lean#L235).

> **[Stacks, Tag 0DJL].** *"Let `X` be a quasi-compact and quasi-separated scheme. Let
> `T ⊂ X` be a closed subset such that `X ∖ T` is quasi-compact. The analogue of Theorem 09M5 holds
> for `D_{QCoh,T}(𝒪_X)`."* That is: there is a differential graded algebra `(E, d)` with only a
> finite number of nonzero cohomology groups `H^i(E)` such that `D_{QCoh,T}(𝒪_X)` is equivalent to
> `D(E, d)`. The derived category of `𝒪_X`-modules is taken at an arbitrary model `h`.

```lean
theorem exists_dga_equivalence_quasiCoherentSupported (hT : IsClosed T)
    (hTc : IsCompact (Tᶜ : Set X))
    [h : HasDerivedCategory.{w} (SheafOfModules.{u} X.ringCatSheaf)] :
    ∃ E : DifferentialGradedAlgebra.{0, u} ℤ, {i : ℤ | Nontrivial (E.Cohomology i)}.Finite ∧
      Nonempty (@Stacks.Duality.QuasiCoherentSupportedDerivedCategory X T h ≌
        DifferentialGradedModule.derivedCategory.{0, u, u} E)
```

## Tag 09SU, a remark

[Tag 09SU](https://stacks.math.columbia.edu/tag/09SU) in the Stacks Project.

**`AlgebraicGeometry.exists_dga_quasiCoherentDerived_linearEquivalence_and_derivedTensor_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/QuasiCoherentDerived/DGAUniqueness/Remark.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/QuasiCoherentDerived/DGAUniqueness/Remark.lean#L142).

> **Stacks 09SU** (uniqueness of the differential graded algebra). *Let `X` be a quasi-compact
> and quasi-separated scheme over a ring `R`. By the construction of the proof of Tag 09M5 there
> exists a differential graded algebra `(A, d)` over `R` such that `D_QCoh(X)` is `R`-linearly
> equivalent to `D(A, d)` as a triangulated category. If `(B, d)` is a second such pair, then
> `(A, d) = Hom_{Comp^dg(𝒪_X)}(K, K)` and `(B, d) = Hom_{Comp^dg(𝒪_X)}(L, L)` for K-injective
> complexes `K`, `L` of `𝒪_X`-modules corresponding to perfect generators of `D_QCoh(𝒪_X)`; with
> `Ω = Hom(K, L)` and `Ω' = Hom(L, K)`, `Ω` is a differential graded `B^{opp} ⊗_R A`-module and `Ω'`
> a differential graded `A^{opp} ⊗_R B`-module, and the equivalence
> `D(A, d) → D_QCoh(𝒪_X) → D(B, d)` is given by `- ⊗_A^𝐋 Ω'`, and similarly its quasi-inverse by
> `- ⊗_B^𝐋 Ω`.*
>
> The scheme is over `R` through `f : X ⟶ Spec R`, which makes `𝒪_X`-modules `R`-linear
> (`AlgebraicGeometry.overRingLinear`). `D_QCoh(X)` is taken at an arbitrary model `h` of the derived
> category of `𝒪_X`-modules. The pairs of the construction are indexed by the complexes `K` with
> `IsPerfectGeneratorRepresentative X K` (K-injective, perfect, generating `D_QCoh(𝒪_X)`): the
> algebra is `A = Hom_{Comp^dg(𝒪_X)}(K, K)` (`RingedSite.Rep … K`'s algebra, a differential graded
> `R`-algebra) and the equivalence is `AlgebraicGeometry.dgaModelEquivalenceAt`, the quasi-inverse
> of `- ⊗_A^𝐋 K`.
>
> 1. Such a `K` exists, and the equivalence `D_QCoh(X) ≌ D(A, d)` is `R`-linear and exact.
> 2. For two of them `K`, `L`, `Ω' = Hom(L, K)` is the differential graded `(A, B)`-bimodule
>    `RingedSite.homBimodule … K L` — its right `B`-module is the Hom complex of Tag 09LE, and
>    `a ∈ A` acts by postcomposition — and, through Tag 0FQJ, comes from a differential graded
>    `A^{opp} ⊗_R B`-module; symmetrically for `Ω = Hom(K, L)`, a `(B, A)`-bimodule coming from a
>    `B^{opp} ⊗_R A`-module.
> 3. The composite equivalence `D(A, d) ≌ D_QCoh(X) ≌ D(B, d)` has functor isomorphic to
>    `- ⊗_A^𝐋 Ω'` and quasi-inverse isomorphic to `- ⊗_B^𝐋 Ω`.

```lean
theorem exists_dga_quasiCoherentDerived_linearEquivalence_and_derivedTensor_iso
    (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X] {R : CommRingCat.{u}}
    (f : X ⟶ Spec R) [h : HasDerivedCategory.{w} X.Modules] :
    letI := overRingLinear f
    letI := overRingScalarSections f
    (∃ K : CochainComplex (RingedSite.ModO.{u, u, u, u} (𝒮 X)) ℤ,
      ∃ hK : IsPerfectGeneratorRepresentative X K,
        (dgaModelEquivalenceAt R hK h).functor.Linear R ∧
          ∃ _ : (dgaModelEquivalenceAt R hK h).functor.CommShift ℤ,
            (dgaModelEquivalenceAt R hK h).functor.IsTriangulated) ∧
    ∀ (K L : CochainComplex (RingedSite.ModO.{u, u, u, u} (𝒮 X)) ℤ)
      (hK : IsPerfectGeneratorRepresentative X K) (hL : IsPerfectGeneratorRepresentative X L),
      -- `Ω' = Hom(L, K)`: an `(A, B)`-bimodule, by pre- and postcomposition
      (RingedSite.homBimodule (𝒮 X) R K L).rightModule =
          (RingedSite.Rep.{u, u, u, u, u, u} (𝒮 X) R L).functor.obj
            (RingedSite.liftComplex.{u, u, u, u, u} (𝒮 X) K) ∧
        (∀ (n : ℤ) (a : (RingedSite.Rep.{u, u, u, u, u, u} (𝒮 X) R K).algebra.grading n),
          (RingedSite.homBimodule (𝒮 X) R K L).leftAction.1.action n a =
            DifferentialGradedModule.homogeneousMapToCochain _
              ((RingedSite.Rep.{u, u, u, u, u, u} (𝒮 X) R L).functor.map
                ((RingedSite.Rep.{u, u, u, u, u, u} (𝒮 X) R K).algebraHom n a))) ∧
        -- `Ω' = Hom(L, K)`: a differential graded `A^{opp} ⊗_R B`-module (Tag 0FQJ)
        (∃ N : DifferentialGradedModule.{u, u, u} (DifferentialGraded.Bimodule.tensorAlgebra
            (RingedSite.Rep.{u, u, u, u, u, u} (𝒮 X) R K).algebra
            (RingedSite.Rep.{u, u, u, u, u, u} (𝒮 X) R L).algebra),
          Nonempty ((DifferentialGraded.Bimodule.tensorEquivalence _ _).equivalence.inverse.obj N ≅
            RingedSite.homBimodule (𝒮 X) R K L)) ∧
        -- `Ω = Hom(K, L)`: a `(B, A)`-bimodule, by pre- and postcomposition
        (RingedSite.homBimodule (𝒮 X) R L K).rightModule =
          (RingedSite.Rep.{u, u, u, u, u, u} (𝒮 X) R K).functor.obj
            (RingedSite.liftComplex.{u, u, u, u, u} (𝒮 X) L) ∧
        (∀ (n : ℤ) (b : (RingedSite.Rep.{u, u, u, u, u, u} (𝒮 X) R L).algebra.grading n),
          (RingedSite.homBimodule (𝒮 X) R L K).leftAction.1.action n b =
            DifferentialGradedModule.homogeneousMapToCochain _
              ((RingedSite.Rep.{u, u, u, u, u, u} (𝒮 X) R K).functor.map
                ((RingedSite.Rep.{u, u, u, u, u, u} (𝒮 X) R L).algebraHom n b))) ∧
        -- `Ω = Hom(K, L)`: a differential graded `B^{opp} ⊗_R A`-module (Tag 0FQJ)
        (∃ N : DifferentialGradedModule.{u, u, u} (DifferentialGraded.Bimodule.tensorAlgebra
            (RingedSite.Rep.{u, u, u, u, u, u} (𝒮 X) R L).algebra
            (RingedSite.Rep.{u, u, u, u, u, u} (𝒮 X) R K).algebra),
          Nonempty ((DifferentialGraded.Bimodule.tensorEquivalence _ _).equivalence.inverse.obj N ≅
            RingedSite.homBimodule (𝒮 X) R L K)) ∧
        -- the composite `D(A, d) ≌ D_QCoh(X) ≌ D(B, d)` is `- ⊗_A^𝐋 Ω'`, with quasi-inverse
        -- `- ⊗_B^𝐋 Ω`
        Nonempty (((dgaModelEquivalenceAt R hK h).symm.trans
            (dgaModelEquivalenceAt R hL h)).functor ≅
          RingedSite.derivedTensorHom (𝒮 X) R K L) ∧
        Nonempty (((dgaModelEquivalenceAt R hK h).symm.trans
            (dgaModelEquivalenceAt R hL h)).inverse ≅
          RingedSite.derivedTensorHom (𝒮 X) R L K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.18, Tag 09M2](https://stacks.math.columbia.edu/tag/09M2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
