---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProEtale.IsConstructibleDerivedSheaf, AlgebraicGeometry.ProEtale.constructibleDerivedSheaves, AlgebraicGeometry.ProEtale.IsConstructibleViaDerivedReduction, AlgebraicGeometry.ProEtale.constructibleDerivedSheavesViaDerivedReduction, AlgebraicGeometry.ProEtale.hasConstructibleCohomology_derivedReduction_pow, AlgebraicGeometry.ProEtale.exists_isDerivedLimit_derivedReductionTower_and_hasTorAmplitude, AlgebraicGeometry.ProEtale.exists_etaleInverseImage_iso_derivedReduction_pow, AlgebraicGeometry.ProEtale.hasFiniteDisjointCompletedConstantModel_of_isLocallyConstant
statement: formalized
proof: formalized
---

# 61.29 A suitable derived category

Section 61.29 of the Stacks Project, [Tag 09C0](https://stacks.math.columbia.edu/tag/09C0). 7 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09C1, a definition

[Tag 09C1](https://stacks.math.columbia.edu/tag/09C1) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.IsConstructibleDerivedSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleComplexes.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleComplexes.lean#L254). The attribute's comment: “constructible objects”.

> **Stacks 09C1.** An object `K` of `D(X_proét, Λ)` is *constructible* with respect to the
> ideal `I` of the Noetherian coefficient ring `Λ` when it is derived complete along the ideal
> sheaf cut out by `I`, and its derived reduction `K ⊗_Λ^L Λ/I`, formed with the derived base
> change `T`, has constructible cohomology sheaves and locally has finite Tor dimension measured
> against the derived tensor products `D` on the slices.

```lean
abbrev IsConstructibleDerivedSheaf
    (T : DerivedReduction.{u, r, w} X Λ I)
    (D : ∀ U : (constantCoefficientRingedSite.{u, r, w} X (Λ ⧸ I)).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, max (u + 1) r w,
          max (u + 1) r w + 1}
        ((constantCoefficientRingedSite.{u, r, w} X (Λ ⧸ I)).over U))
    (K : DerivedSheaves.{u, r, w} X Λ) : Prop
```

**`AlgebraicGeometry.ProEtale.constructibleDerivedSheaves`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleComplexes.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleComplexes.lean#L271). The attribute's comment: “the full subcategory”.

> **Stacks 09C1.** The full subcategory `D_cons(X, Λ)` of `D(X_proét, Λ)` on the
> constructible objects.

```lean
abbrev constructibleDerivedSheaves
    (T : DerivedReduction.{u, r, w} X Λ I)
    (D : ∀ U : (constantCoefficientRingedSite.{u, r, w} X (Λ ⧸ I)).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, max (u + 1) r w,
          max (u + 1) r w + 1}
        ((constantCoefficientRingedSite.{u, r, w} X (Λ ⧸ I)).over U))
```

**`AlgebraicGeometry.ProEtale.IsConstructibleViaDerivedReduction`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleDerivedSheaves.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleDerivedSheaves.lean#L131). The attribute's comment: “constructible objects”.

> **Stacks 09C1.** An object `K` of `D(X_proét, Λ)` is *constructible* with respect to the
> ideal `I` of the Noetherian coefficient ring `Λ` when it is derived complete along the ideal
> sheaf cut out by `I`, and its derived reduction `K ⊗_Λ^L \underline{Λ/I}` has constructible
> cohomology sheaves and locally has finite Tor dimension.

```lean
abbrev IsConstructibleViaDerivedReduction (K : DerivedSheaves.{u, max (u + 1) w, w} X Λ) : Prop
```

**`AlgebraicGeometry.ProEtale.constructibleDerivedSheavesViaDerivedReduction`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleDerivedSheaves.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleDerivedSheaves.lean#L142). The attribute's comment: “the full subcategory”.

> **Stacks 09C1.** The full subcategory `D_cons(X, Λ)` of `D(X_proét, Λ)` on the
> constructible objects.

```lean
abbrev constructibleDerivedSheavesViaDerivedReduction
```

## Tag 09C2, a lemma

[Tag 09C2](https://stacks.math.columbia.edu/tag/09C2) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.hasConstructibleCohomology_derivedReduction_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleReductions.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleReductions.lean#L106). The attribute's comment: “part (3)”.

> **The reductions of a constructible complex have constructible cohomology sheaves.** If `X`
> is quasi-compact and `K` lies in `D_cons(X, Λ)`, every reduction
> `Kₙ = K ⊗_Λ^L Λ/Iⁿ` has constructible cohomology sheaves.

```lean
theorem hasConstructibleCohomology_derivedReduction_pow [CompactSpace X]
    {K : DerivedSheaves.{u, max (u + 1) w, w} X Λ}
    (hK : IsConstructibleViaDerivedReduction.{u, w} X Λ I K)
    (n : ℕ) :
    HasConstructibleModuleSheafCohomology.{u, w} X (Λ ⧸ I ^ n)
      ((derivedReduction.{u, w} X Λ (I ^ n)).obj K)
```

**`AlgebraicGeometry.ProEtale.exists_isDerivedLimit_derivedReductionTower_and_hasTorAmplitude`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleReductions.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleReductions.lean#L217). The attribute's comment: “parts (1) and (2)”.

> Let `X` be quasi-compact and `K` an object of `D_cons(X, Λ)`, and set
> `Kₙ = K ⊗_Λ^L \underline{Λ/Iⁿ}`. There are integers `a` and `b` such that
>
> 1. `K = R lim Kₙ`, with the reduction maps `K ⟶ Kₙ` as projections, and `Hⁱ(K) = 0` for
>    `i ∉ [a, b]`;
> 2. every `Kₙ` has Tor amplitude in `[a, b]`.
>
> In (1) the tower `Kₙ` is read in the derived category of sheaves of `Λ`-modules, as the derived
> tensor product of `K` with the constant sheaves `\underline{Λ/Iⁿ}`; in (2) `Kₙ` is the derived
> reduction of `K`, an object of `D(X_proét, Λ/Iⁿ)`.

```lean
theorem exists_isDerivedLimit_derivedReductionTower_and_hasTorAmplitude [CompactSpace X]
    {K : DerivedSheaves.{u, max (u + 1) w, w} X Λ}
    (hK : IsConstructibleViaDerivedReduction.{u, w} X Λ I K) :
    ∃ a b : ℤ,
      (NoetherianAdicCompletion.IsDerivedLimitWithProjections
          (derivedReductionTower.{u, w} X Λ I
            ((derivedModuleEquiv.{u, max (u + 1) w, w} X Λ).inverse.obj K))
          ((derivedModuleEquiv.{u, max (u + 1) w, w} X Λ).inverse.obj K)
          (fun n ↦ (Stacks.ModuleSheaf.derivedReductionMap (Scheme.ProEt.topology X) Λ I
            ((derivedModuleEquiv.{u, max (u + 1) w, w} X Λ).inverse.obj K)).app ⟨n⟩) ∧
        ∀ i : ℤ, i ∉ Set.Icc a b →
          IsZero ((DerivedCategory.homologyFunctor _ i).obj K)) ∧
      ∀ n : ℕ, Stacks.ModuleSheaf.HasTorAmplitude (J := Scheme.ProEt.topology X)
        ((derivedReduction.{u, w} X Λ (I ^ n)).obj K) (Set.Icc a b)
```

**`AlgebraicGeometry.ProEtale.exists_etaleInverseImage_iso_derivedReduction_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleReductions.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleReductions.lean#L294). The attribute's comment: “part (4)”.

> **The reductions of a constructible complex come from the étale site.** If `X` is
> quasi-compact and `K` lies in `D_cons(X, Λ)`, every reduction
> `Kₙ = K ⊗_Λ^L Λ/Iⁿ` is `ε⁻¹ Lₙ` for an object `Lₙ` of `D(X_étale, Λ/Iⁿ)` with constructible
> cohomology sheaves and finite Tor dimension.
>
> Here `ε⁻¹` on derived categories is `ε⁻¹` applied termwise.

```lean
theorem exists_etaleInverseImage_iso_derivedReduction_pow [CompactSpace X]
    {K : DerivedSheaves.{u, max (u + 1) w, w} X Λ}
    (hK : IsConstructibleViaDerivedReduction.{u, w} X Λ I K)
    (n : ℕ) :
    ∃ L : DerivedCategory (Sheaf X.smallEtaleTopology (ModuleCat.{max (u + 1) w} (Λ ⧸ I ^ n))),
      (∀ i : ℤ, Scheme.IsConstructibleEtaleModuleSheaf.{u, max (u + 1) w, w} X (Λ ⧸ I ^ n)
        ((DerivedCategory.homologyFunctor _ i).obj L)) ∧
      Stacks.ModuleSheaf.HasFiniteTorDimension (J := X.smallEtaleTopology) L ∧
      Nonempty ((Scheme.etaleInverseImage.{u, w} X (Λ ⧸ I ^ n)).mapDerivedCategory.obj L ≅
        (derivedReduction.{u, w} X Λ (I ^ n)).obj K)
```

## Tag 09C3, a lemma

[Tag 09C3](https://stacks.math.columbia.edu/tag/09C3) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.hasFiniteDisjointCompletedConstantModel_of_isLocallyConstant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/LocallyConstantCompletedModel.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/LocallyConstantCompletedModel.lean#L85).

> **Stacks 09C3.** Let `X` be a weakly contractible affine scheme, `Λ` a Noetherian ring,
> `I ⊆ Λ` an ideal and `K` an object of `D_cons(X, Λ)` such that the cohomology sheaves of
> `K ⊗_Λ^L \underline{Λ/I}` are locally constant. Then there are a finite disjoint open covering
> `X = ∐ U_i` and, for each `i`, finite projective `Λ^∧`-modules `M^a, …, M^b` such that `K|_{U_i}`
> is represented in `D(U_{i, proét}, Λ)` by a complex
> `(\underline{M^a})^∧ → ⋯ → (\underline{M^b})^∧` for some maps of sheaves of `Λ`-modules between
> consecutive terms.
>
> The covering, the restrictions and the models are those of
> `AlgebraicGeometry.ProEtale.HasFiniteDisjointCompletedConstantModel`; weak contractibility of `X`
> is that of Stacks 090L.

```lean
theorem hasFiniteDisjointCompletedConstantModel_of_isLocallyConstant [IsAffine X]
    (hX : ProetaleWContractible.IsWeaklyContractibleObj X)
    (K : DerivedSheaves.{u, max (u + 1) w, w} X Λ)
    (hK : IsConstructibleViaDerivedReduction.{u, w} X Λ I K)
    (hloc : ∀ i : ℤ, Stacks.ConstantSheaf.IsLocallyConstant (Scheme.ProEt.topology X)
      ((DerivedCategory.homologyFunctor _ i).obj ((derivedReduction.{u, w} X Λ I).obj K))) :
    HasFiniteDisjointCompletedConstantModel.{u, max (u + 1) w, w} X Λ I K
```

## Tag 09C4, a definition

[Tag 09C4](https://stacks.math.columbia.edu/tag/09C4) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.IsAdicConstructibleViaDerivedInverseImage`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/AdicConstructibleComplexes.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/AdicConstructibleComplexes.lean#L82). The attribute's comment: “part (2): adic constructible”.

> **Stacks 09C4, part (2).** An object `K` of `D(X_proét, Λ)` is *adic constructible* if every
> affine open `U` of `X` admits a decomposition `U = ∐ U_i` into constructible locally closed
> subschemes such that every restriction `K|_{U_i}` is adic lisse.

```lean
abbrev IsAdicConstructibleViaDerivedInverseImage (K : DerivedSheaves.{u, r, w} X Λ) : Prop
```

**`AlgebraicGeometry.ProEtale.IsAdicLisseDerivedSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleComplexes.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleComplexes.lean#L454). The attribute's comment: “part (1): adic lisse”.

> **Stacks 09C4, part (1).** An object `K` of `D(X_proét, Λ)` is *adic lisse* if there is a
> finite complex `M^•` of finite projective `Λ^∧`-modules such that `K` is pro-étale locally
> isomorphic to the complex `\underline{M^a}^∧ → ⋯ → \underline{M^b}^∧` of completed constant
> sheaves, whose differentials are those induced by the differentials of `M^•`.

```lean
abbrev IsAdicLisseDerivedSheaf (K : DerivedSheaves.{u, r, w} X Λ) : Prop
```

**`AlgebraicGeometry.ProEtale.IsAdicConstructibleDerivedSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleComplexes.lean, line 535](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleComplexes.lean#L535). The attribute's comment: “part (2): adic constructible”.

> **Stacks 09C4, part (2).** An object `K` of `D(X_proét, Λ)` is *adic constructible* if every
> affine open of `X` admits a decomposition into constructible locally closed subschemes on which
> the restriction of `K` is adic lisse.

```lean
abbrev IsAdicConstructibleDerivedSheaf (K : DerivedSheaves.{u, r, w} X Λ) : Prop
```

## Tag 09C5, a lemma

[Tag 09C5](https://stacks.math.columbia.edu/tag/09C5) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isMittagLefflerCategorical_derivedReductionSectionsSystem_of_isConstructibleViaDerivedReduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/AdicModelReductionSections.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/AdicModelReductionSections.lean#L272). The attribute's comment: “the Mittag-Leffler condition for the inverse system n ↦ H^0(X, K ⊗\_Λ^L Λ/I^n) of sections modules, with its canonical transition maps; the hypothesis that each reduction is a complex of constant sheaves is read, as in the source's proof, as K ⊗\_Λ^L Λ/I^n ≅ \underline\{E\_n} for an object E\_n of D(Λ/I^n)”.

> **Stacks 09C5.** Let `X` be a weakly contractible affine scheme, `Λ` a Noetherian ring,
> `I ⊆ Λ` an ideal and `K` an object of `D_cons(X, Λ)` such that every reduction
> `K ⊗_Λ^L Λ/Iⁿ` is isomorphic, in `D(X_proét, Λ/Iⁿ)`, to a complex of constant sheaves of
> `Λ/Iⁿ`-modules. Then the inverse system `n ↦ H⁰(X, K ⊗_Λ^L Λ/Iⁿ)` of `Λ`-modules satisfies the
> Mittag-Leffler condition.
>
> The conclusion is the Mittag-Leffler condition of Stacks Tag 02N0 for the system
> `derivedReductionSectionsSystem X Λ I K'`, `K'` being `K` read in the derived category of sheaves
> of `Λ`-modules; its terms are the sections modules `H⁰(X, K ⊗_Λ^L Λ/Iⁿ)` and its transition maps
> are induced by the reductions `Λ/Iⁿ⁺¹ → Λ/Iⁿ`. Constructibility is
> `AlgebraicGeometry.ProEtale.IsConstructibleViaDerivedReduction`, and the reductions are
> `AlgebraicGeometry.ProEtale.derivedReduction`.
>
> The proof: for a K-flat representative `P` of `K`,
> `AlgebraicGeometry.ProEtale.exists_isBoundedAboveFiniteFree_reduction_iso` gives a bounded
> above complex `F` of finite free `Λ^∧`-modules whose constant complex has, levelwise, the
> reductions of `P`; the sections system of the reductions of `\underline{F}` is
> `j ↦ Γ(X, \underline{H⁰(F/IʲF)})`, which is Mittag-Leffler by the Artin–Rees lemma
> (`AlgebraicGeometry.ProEtale.isMittagLefflerCategorical_constantComplexReductionSections`), and
> `Stacks.ModuleSheaf.isMittagLefflerCategorical_reductionSections_of_adicModel` transports the
> condition. Over the empty scheme every term of the system vanishes.

```lean
theorem
    isMittagLefflerCategorical_derivedReductionSectionsSystem_of_isConstructibleViaDerivedReduction
    [IsAffine X] (hX : ProetaleWContractible.IsWeaklyContractibleObj X)
    (K : DerivedSheaves.{u, max (u + 1) w, w} X Λ)
    (hK : IsConstructibleViaDerivedReduction.{u, w} X Λ I K)
    (hconstant : ∀ n : ℕ, ∃ E : DerivedCategory (ModuleCat.{max (u + 1) w} (Λ ⧸ I ^ n)),
      Nonempty ((derivedReduction.{u, w} X Λ (I ^ n)).obj K ≅
        (constantSheaf (Scheme.ProEt.topology X)
          (ModuleCat.{max (u + 1) w} (Λ ⧸ I ^ n))).mapDerivedCategory.obj E)) :
    IsMittagLefflerCategorical (derivedReductionSectionsSystem X Λ I
      ((derivedModuleEquiv.{u, max (u + 1) w, w} X Λ).inverse.obj K))
```

**`AlgebraicGeometry.ProEtale.isMittagLefflerCategorical_derivedReductionSectionsSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleReductionSections.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/ConstructibleReductionSections.lean#L336).

> **Stacks 09C5.** Let `X` be a weakly contractible affine scheme, `Λ` a Noetherian ring,
> `I ⊆ Λ` an ideal and `K` an object of `D_cons(X, Λ)` such that for every `n ≥ 1` the reduction
> `K ⊗_Λ^L \underline{Λ/Iⁿ}` is isomorphic in `D(X_proét, Λ/Iⁿ)` to a complex of constant sheaves
> of `Λ/Iⁿ`-modules. Then the inverse system `n ↦ H⁰(X, K ⊗_Λ^L Λ/Iⁿ)` of `Λ`-modules satisfies the
> Mittag-Leffler condition.
>
> The reductions in the hypothesis are taken with derived base changes `Tn n` along
> `Λ → Λ/Iⁿ` (any two of which are canonically isomorphic), and a complex of constant sheaves is
> the constant sheaf functor applied to a complex `E` of `Λ/Iⁿ`-modules. The inverse system of the
> conclusion is `AlgebraicGeometry.ProEtale.derivedReductionSectionsSystem`: degree-zero cohomology
> and sections over `X` of the derived tensor products of `K` with the constant sheaves
> `\underline{Λ/Iⁿ}`, whose transition maps are induced by the reductions `Λ/Iⁿ⁺¹ → Λ/Iⁿ`; here `K`
> is read in the derived category of sheaves of `Λ`-modules, where the derived tensor product is
> constructed, through the constant coefficients equivalence.

```lean
theorem isMittagLefflerCategorical_derivedReductionSectionsSystem [IsAffine X]
    (hX : ProetaleWContractible.IsWeaklyContractibleObj X)
    (T : DerivedReduction.{u, max (u + 1) w, w} X Λ I)
    (D : ∀ U : (constantCoefficientRingedSite.{u, max (u + 1) w, w} X (Λ ⧸ I)).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, max (u + 1) w,
          max (u + 1) w + 1}
        ((constantCoefficientRingedSite.{u, max (u + 1) w, w} X (Λ ⧸ I)).over U))
    (K : DerivedSheaves.{u, max (u + 1) w, w} X Λ)
    (hK : IsConstructibleDerivedSheaf.{u, max (u + 1) w, w} X Λ I T D K)
    (Tn : ∀ n : ℕ, DerivedReduction.{u, max (u + 1) w, w} X Λ (I ^ n))
    (hconstant : ∀ n : ℕ, 1 ≤ n →
      ∃ E : CochainComplex (ModuleCat.{max (u + 1) w} (Λ ⧸ I ^ n)) ℤ,
        Nonempty ((Tn n).baseChange.obj K ≅ DerivedCategory.Q.obj
          (((constantSheafOverCoefficients.{u, max (u + 1) w, w} X (Λ ⧸ I ^ n)).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj E))) :
    IsMittagLefflerCategorical (derivedReductionSectionsSystem X Λ I
      ((derivedCoefficientModuleSheafEquivalence.{u, max (u + 1) w, w} X Λ).functor.obj K))
```

**`AlgebraicGeometry.ProEtale.isMittagLefflerCategorical_reductionSectionsSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/LocallyConstantAdicModel.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/LocallyConstantAdicModel.lean#L367). The attribute's comment: “the Mittag-Leffler conclusion for the INVERSE SYSTEM over n, stated about the concrete system of sections modules H^0(X, K ⊗\_Λ^L Λ/I^n) and proved from the pro-domination of that system by the adic quotient system n ↦ N/I^nN of a Λ-module N. Two things are assumed rather than proved. First, the transition maps of the system are taken as a datum t: the source's are those induced by Λ/I^(n+1) → Λ/I^n, and the comparison of the derived base changes along Λ → Λ/I^(n+1) → Λ/I^n and along Λ → Λ/I^n is not constructed in the library, so the statement is proved for every family t. Second, the pro-domination itself is the output of the source's steps (1)-(6): steps (1)-(5) rest on 09C3 (the local adic model, also not formalized), 0658 (perfectness of the reduction E\_1), 09BE (local constancy of a map of complexes of constant sheaves) and 09AW (the complex M^• of finite projective Λ^∧-modules with M^•/I^nM^• ≅ E\_n), and step (6) on the Tor spectral sequence together with 0911 (strict pro-vanishing of Tor); that chain is not assembled. What is proved outright is the Mittag-Leffler condition for the sections system from that data, including the surjectivity of the transition maps of the adic quotient system. The source's weak contractibility of X and constructibility of K are not needed for this implication and are carried unused”.

> **Stacks 09C5**, for the inverse system over `n`, from the pro-domination data that the
> source's steps (1)–(6) supply.
>
> Let `X` be a weakly contractible affine scheme, `Λ` a Noetherian ring, `I ⊆ Λ` an ideal and `K`
> a constructible object of `D(X_proét, Λ)` such that every reduction `K ⊗_Λ^L Λ/Iⁿ` is
> isomorphic, in `D(X_proét, Λ/Iⁿ)`, to a complex of constant sheaves of `Λ/Iⁿ`-modules. Then the
> inverse system `n ↦ H⁰(X, K ⊗_Λ^L Λ/Iⁿ)` of `Λ`-modules satisfies the Mittag-Leffler condition.
>
> The conclusion is the Mittag-Leffler condition of Stacks Tag 02N0 for the system indexed by
> `n`, not a statement about any single `n`, and it is stated about the concrete system
> `reductionSectionsSystem X Λ I Tn K t` whose terms are the sections modules
> `H⁰(X, K ⊗_Λ^L Λ/Iⁿ)` themselves.
>
> The setting hypotheses `_hX`, `_hK` and `_hconstant` are not used in the proof: pro-domination
> of the sections system by an adic quotient system already forces the Mittag-Leffler condition,
> without weak contractibility of `X` and without constructibility of `K`. They are retained,
> underscore-prefixed, so that the statement reads as the source's; the result is therefore more
> general than the source, which this charter permits.

```lean
theorem isMittagLefflerCategorical_reductionSectionsSystem [IsAffine X]
    (_hX : ProetaleWContractible.IsWeaklyContractibleObj X)
    (T : DerivedReduction.{u, r, w} X Λ I)
    (D : ∀ U : (constantCoefficientRingedSite.{u, r, w} X (Λ ⧸ I)).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, max (u + 1) r w,
          max (u + 1) r w + 1}
        ((constantCoefficientRingedSite.{u, r, w} X (Λ ⧸ I)).over U))
    (K : DerivedSheaves.{u, r, w} X Λ)
    (_hK : IsConstructibleDerivedSheaf.{u, r, w} X Λ I T D K)
    (Tn : ∀ n : ℕ, DerivedReduction.{u, r, w} X Λ (I ^ n))
    (_hconstant : ∀ n : ℕ, IsConstantSheafComplexModel.{u, r, w} X (Λ ⧸ I ^ n)
      ((Tn n).baseChange.obj K))
    (t : ∀ n : ℕ, reductionSectionsObj.{u, r, w} X Λ I Tn K (n + 1) ⟶
      reductionSectionsObj.{u, r, w} X Λ I Tn K n)
    (N : ModuleCat.{max (u + 1) r w} Λ) (c : ℕ)
    (β : ∀ n : ℕ, (adicQuotientModuleSystem Λ I N).obj (op (n + c)) ⟶
      (reductionSectionsSystem.{u, r, w} X Λ I Tn K t).obj (op n))
    (hβ : ∀ (i j : ℕ) (h : i ≤ j),
      (adicQuotientModuleSystem Λ I N).map (homOfLE (Nat.add_le_add_right h c)).op ≫ β i =
        β j ≫ (reductionSectionsSystem.{u, r, w} X Λ I Tn K t).map (homOfLE h).op)
    (α : ∀ n : ℕ, (reductionSectionsSystem.{u, r, w} X Λ I Tn K t).obj (op (n + c)) ⟶
      (adicQuotientModuleSystem Λ I N).obj (op n))
    (hαβ : ∀ n : ℕ, α (n + c) ≫ β n =
      (reductionSectionsSystem.{u, r, w} X Λ I Tn K t).map
        (homOfLE (show n ≤ n + c + c by omega)).op) :
    IsMittagLefflerCategorical (reductionSectionsSystem.{u, r, w} X Λ I Tn K t)
```

## Tag 09C6, a lemma

[Tag 09C6](https://stacks.math.columbia.edu/tag/09C6) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isAdicLisseDerivedSheaf_of_isLocallyConstant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/AdicLisseOfLocallyConstant.lean, line 719](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/AdicLisseOfLocallyConstant.lean#L719). The attribute's comment: “a constructible complex over a connected scheme whose reduction modulo I has locally constant cohomology sheaves is adic lisse”.

> Let `X` be a connected scheme, `Λ` a Noetherian ring and `I ⊆ Λ` an ideal. If `K` is in
> `D_cons(X, Λ)` and `K ⊗_Λ^L \underline{Λ/I}` has locally constant cohomology sheaves, then `K` is
> adic lisse.

```lean
theorem isAdicLisseDerivedSheaf_of_isLocallyConstant [ConnectedSpace X] [IsNoetherianRing Λ]
    {K : DerivedSheaves.{u, max (u + 1) w, w} X Λ}
    (hK : IsConstructibleViaDerivedReduction.{u, w} X Λ I K)
    (hloc : ∀ i : ℤ, Stacks.ConstantSheaf.IsLocallyConstant (Scheme.ProEt.topology X)
      ((DerivedCategory.homologyFunctor _ i).obj ((derivedReduction.{u, w} X Λ I).obj K))) :
    IsAdicLisseDerivedSheaf.{u, max (u + 1) w, w} X Λ I K
```

## Tag 09C7, a proposition

[Tag 09C7](https://stacks.math.columbia.edu/tag/09C7) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isAdicConstructibleDerivedSheaf_of_isConstructibleDerivedSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/AdicConstructibleOfConstructible.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/AdicConstructibleOfConstructible.lean#L46).

> **Stacks 09C7.** Let `X` be a Noetherian scheme, `Λ` a Noetherian ring and `I ⊆ Λ` an
> ideal. Every object `K` of `D_cons(X, Λ)` is adic constructible.

```lean
theorem isAdicConstructibleDerivedSheaf_of_isConstructibleDerivedSheaf {X : Scheme.{u}}
    [IsNoetherian X] {Λ : Type (max (u + 1) w)} [CommRing Λ] [IsNoetherianRing Λ] {I : Ideal Λ}
    {K : DerivedSheaves.{u, max (u + 1) w, w} X Λ}
    (hK : IsConstructibleViaDerivedReduction.{u, w} X Λ I K) :
    IsAdicConstructibleViaDerivedInverseImage.{u, max (u + 1) w, w} X Λ I K
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.29, Tag 09C0](https://stacks.math.columbia.edu/tag/09C0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
