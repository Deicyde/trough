---
declaration: section
origin: cited
lean: Stacks.Duality.exists_isLE_derivedPushforward_obj, Stacks.Duality.exists_isLE_derivedPushforward_obj_anyModel, AlgebraicGeometry.exists_uniform_isZero_homology_derivedPushforward, AlgebraicGeometry.exists_isZero_homology_derivedPushforward_of_isLE_zero, AlgebraicGeometry.isQuasicoherent_derivedPushforward, AlgebraicGeometry.isQuasicoherent_derivedPushforward_affineLocal, AlgebraicGeometry.exists_isZero_homology_derivedPushforward_of_isLE, AlgebraicGeometry.isIso_to_rightDerived_of_termwise_acyclic
statement: formalized
proof: formalized
---

# 36.4 Total direct image

Section 36.4 of the Stacks Project, [Tag 08DY](https://stacks.math.columbia.edu/tag/08DY). 5 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08D5, a lemma

[Tag 08D5](https://stacks.math.columbia.edu/tag/08D5) in the Stacks Project.

**`Stacks.Duality.exists_isLE_derivedPushforward_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/UniformBound.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/UniformBound.lean#L116). The attribute's comment: “part (2), in the duality spelling”.

> **[Stacks, Tag 08D5] part (2), in the duality spelling.** Let `f : X ⟶ Y` be a quasi-compact
> and quasi-separated morphism of schemes with `Y` quasi-compact. There is an integer `N`,
> depending on `f` alone, such that `Rf_*E` lives in degrees `≤ b + N` for every object `E` of
> `D_QCoh(𝒪_X)` living in degrees `≤ b`.
>
> This is `AlgebraicGeometry.exists_isZero_homology_derivedPushforward` with `Rf_*` spelled
> `Stacks.Duality.derivedPushforward` and the conclusion packaged as `DerivedCategory.IsLE`; the
> degree drops by one in the repackaging because the source asserts vanishing *at* `b + N`.

```lean
theorem exists_isLE_derivedPushforward_obj [QuasiCompact f] [QuasiSeparated f]
    [CompactSpace Y] :
    ∃ N : ℤ, ∀ E : DerivedCategory X.Modules,
      (∀ j : ℤ, ((DerivedCategory.homologyFunctor X.Modules j).obj E).IsQuasicoherent) →
      ∀ b : ℤ, E.IsLE b → ((derivedPushforward f).obj E).IsLE (b + N)
```

**`Stacks.Duality.exists_isLE_derivedPushforward_obj_anyModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/UniformBoundAnyModel.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/UniformBoundAnyModel.lean#L256). The attribute's comment: “part (2), at an arbitrary derived category”.

> **[Stacks, Tag 08D5] part (2), at an arbitrary chosen model of the derived categories, in the
> `IsLE` form.** Let `f : X ⟶ Y` be a quasi-compact and quasi-separated morphism of schemes with `Y`
> quasi-compact. There is an integer `N`, depending on `f` alone, such that `Rf_*E` lives in degrees
> `≤ b + N` for every object `E` of `D(𝒪_X)` with quasi-coherent cohomology living in degrees `≤ b`.
>
> This is `Stacks.Duality.exists_isLE_derivedPushforward_obj` with the choice of derived category a
> binder rather than a term; the degree drops by one in the repackaging because
> `Stacks.Duality.exists_isZero_homology_derivedPushforward_anyModel` asserts vanishing *at*
> `b + N`.

```lean
theorem exists_isLE_derivedPushforward_obj_anyModel
    [QuasiCompact f] [QuasiSeparated f] [CompactSpace Y] :
    ∃ N : ℤ, ∀ E : DerivedCategory X.Modules,
      (∀ j : ℤ, ((DerivedCategory.homologyFunctor X.Modules j).obj E).IsQuasicoherent) →
      ∀ b : ℤ, E.IsLE b → ((derivedPushforward.{w} f).obj E).IsLE (b + N)
```

**`AlgebraicGeometry.exists_uniform_isZero_homology_derivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TotalDirectImage/BaseChangeBound.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TotalDirectImage/BaseChangeBound.lean#L144). The attribute's comment: “uniform\_bound\_after\_base\_change”.

> **Stacks 08D5, part (3).** Let `f : X ⟶ S` be a quasi-compact and quasi-separated morphism
> of schemes with `S` quasi-compact. There is an integer `N`, depending only on `f`, such that for
> every morphism `g : S' ⟶ S` the base change `f' : X ×_S S' ⟶ S'` satisfies `H^q(Rf'_* E) = 0`
> for every `q ≥ N` and every object `E` of `D(𝒪_{X ×_S S'})` with quasi-coherent cohomology
> sheaves and vanishing cohomology in positive degrees.
>
> The covering data of `f` is extracted once, by
> `AlgebraicGeometry.exists_affine_cover_data`, and
> `isZero_homology_derivedPushforward_of_commSq` is applied to the cartesian square, whose
> affineness hypothesis is `AlgebraicGeometry.isAffineOpen_inf_preimage`. The degree `N` is read
> off the covering data alone, so it does not depend on `g`.
>
> This is one of the three declarations carrying [Stacks, Tag 08D5]; the other two are
> `AlgebraicGeometry.isQuasicoherent_derivedPushforward` (part (1)) and
> `AlgebraicGeometry.exists_isZero_homology_derivedPushforward_of_isLE_zero` (part (2)).

```lean
theorem exists_uniform_isZero_homology_derivedPushforward {X S : Scheme.{u}} (f : X ⟶ S)
    [QuasiCompact f] [QuasiSeparated f] [CompactSpace S] :
    ∃ N : ℤ, ∀ (S' : Scheme.{u}) (g : S' ⟶ S)
      (E : DerivedCategory.{u + 1} (pullback f g).Modules),
      (∀ i : ℤ, ((DerivedCategory.homologyFunctor (pullback f g).Modules i).obj
        E).IsQuasicoherent) →
      E.IsLE 0 → ∀ q : ℤ, N ≤ q →
        IsZero ((DerivedCategory.homologyFunctor S'.Modules q).obj
          ((derivedPushforward (pullback.snd f g).toLRSHom.toShHom).obj E))
```

**`AlgebraicGeometry.exists_isZero_homology_derivedPushforward_of_isLE_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TotalDirectImage/BoundedCohomologicalDimension.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TotalDirectImage/BoundedCohomologicalDimension.lean#L131). The attribute's comment: “bounded\_cohomological\_dimension”.

> Let `f : X ⟶ S` be a quasi-compact and quasi-separated morphism of schemes with `S`
> quasi-compact. There is an integer `N`, depending only on `f`, such that every object `E` of
> `D(𝒪_X)` with quasi-coherent cohomology sheaves and vanishing cohomology in positive degrees has
> `H^m(Rf_* E) = 0` for all `m ≥ N`.

```lean
theorem exists_isZero_homology_derivedPushforward_of_isLE_zero
    [QuasiCompact f] [QuasiSeparated f] [CompactSpace S] :
    ∃ N : ℤ, ∀ E : DerivedCategory.{u + 1} X.Modules,
      (∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj E).IsQuasicoherent) →
      E.IsLE 0 → ∀ m : ℤ, N ≤ m →
        IsZero ((DerivedCategory.homologyFunctor S.Modules m).obj
          ((derivedPushforward f.toLRSHom.toShHom).obj E))
```

**`AlgebraicGeometry.isQuasicoherent_derivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TotalDirectImage/QuasiCoherentDirectImage.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TotalDirectImage/QuasiCoherentDirectImage.lean#L374). The attribute's comment: “quasi\_coherent\_direct\_image”.

> **Stacks 08D5, part (1).** Let `f : X ⟶ S` be a quasi-compact and quasi-separated morphism of
> schemes. The unbounded derived direct image `Rf_*` carries `D_QCoh(𝒪_X)` into `D_QCoh(𝒪_S)`: the
> cohomology sheaves of `Rf_* E` are quasi-coherent for every object `E` of `D(𝒪_X)` whose
> cohomology sheaves are.
>
> Quasi-coherence is local on the target and `Rf_*` commutes with restriction to an open, which is
> `AlgebraicGeometry.isQuasicoherent_derivedPushforward_of_compactTarget`; the affine case is
> `preservesQuasicoherentOnCompactTarget`.

```lean
theorem isQuasicoherent_derivedPushforward [QuasiCompact f] [QuasiSeparated f]
    (E : QuasicoherentDerivedCategory X) :
    DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherent S.ringCatSheaf)
      ((RingedSpace.derivedPushforward f.toLRSHom.toShHom).obj E.obj)
```

**`AlgebraicGeometry.isQuasicoherent_derivedPushforward_affineLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/UnboundedDerivedDirectImage/QuasiCoherence.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/UnboundedDerivedDirectImage/QuasiCoherence.lean#L281). The attribute's comment: “part (1)”.

> **[Stacks, Tag 08D5], part (1).** For a quasi-compact and quasi-separated morphism of schemes
> `f : X ⟶ S` the unbounded derived direct image `Rf_*` carries `D_QCoh(𝒪_X)` into `D_QCoh(𝒪_S)`:
> the cohomology sheaves of `Rf_*E` are quasi-coherent whenever those of `E` are.
>
> The question is local on `S`, and over an affine open of `S` it is the quasi-compact-target case
> `AlgebraicGeometry.preservesQuasicoherentOnCompactTarget`; the name records that affine-local
> route, the same statement being reached by the compact-target route in
> `AlgebraicGeometry.isQuasicoherent_derivedPushforward`.

```lean
theorem isQuasicoherent_derivedPushforward_affineLocal
    (E : QuasicoherentDerivedCategory X) :
    DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherent S.ringCatSheaf)
      ((RingedSpace.derivedPushforward f.toLRSHom.toShHom).obj E.obj)
```

**`AlgebraicGeometry.exists_isZero_homology_derivedPushforward_of_isLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/UnboundedDerivedDirectImage/UniformBound.lean, line 424](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/UnboundedDerivedDirectImage/UniformBound.lean#L424). The attribute's comment: “part (2)”.

> **[Stacks, Tag 08D5], part (2).** Let `f : X ⟶ S` be a quasi-compact and quasi-separated
> morphism of schemes with `S` quasi-compact. There is an integer `N`, depending on `X`, `S` and `f`
> alone, such that every object `E` of `D_QCoh(𝒪_X)` with `H^m(E) = 0` for `m > 0` has
> `H^m(Rf_*E) = 0` for `m ≥ N`.
>
> This is `AlgebraicGeometry.exists_isZero_homology_derivedPushforward` at `b = 0`.

```lean
theorem exists_isZero_homology_derivedPushforward_of_isLE (f : X ⟶ S) [QuasiCompact f]
    [QuasiSeparated f] [CompactSpace S] :
    ∃ N : ℤ, ∀ E : QuasicoherentDerivedCategory X, E.obj.IsLE 0 → ∀ m : ℤ, N ≤ m →
      IsZero ((DerivedCategory.homologyFunctor S.Modules m).obj
        ((RingedSpace.derivedPushforward f.toLRSHom.toShHom).obj E.obj))
```

## Tag 0G9N, a lemma

[Tag 0G9N](https://stacks.math.columbia.edu/tag/0G9N) in the Stacks Project.

**`AlgebraicGeometry.isIso_to_rightDerived_of_termwise_acyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedAcyclic/Pushforward.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedAcyclic/Pushforward.lean#L433).

> **Stacks Project, Tag 0G9N.** Let `f : X ⟶ S` be a quasi-separated and quasi-compact
> morphism of schemes and let `K` be a complex of quasi-coherent `𝒪_X`-modules each of which is
> right acyclic for `f_*`. Then `f_* K` represents `Rf_* K` in `D(𝒪_S)`: the canonical comparison
> from the termwise direct image to any right derived direct image is an isomorphism at `K`.

```lean
theorem isIso_to_rightDerived_of_termwise_acyclic
    {X S : Scheme.{u}} (f : X ⟶ S) [QuasiCompact f] [QuasiSeparated f]
    (K : CochainComplex X.Modules ℤ)
    (hqc : ∀ n, (K.X n).IsQuasicoherent)
    (hacyclic : ∀ n, (Scheme.Modules.pushforward f).rightAcyclic (K.X n))
    (Rf : DerivedCategory X.Modules ⥤ DerivedCategory S.Modules)
    (α : (Scheme.Modules.pushforward f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf)
    [Rf.IsRightDerivedFunctor α
      (HomotopyCategory.quasiIso X.Modules (ComplexShape.up ℤ))] :
    IsIso (α.app ((HomotopyCategory.quotient _ _).obj K))
```

**`AlgebraicGeometry.isIso_pushforwardComparisonQ_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/AffinePushforwardComparisonQ.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedAffineMorphism/AffinePushforwardComparisonQ.lean#L83). The attribute's comment: “the comparison Q(f\_*C) ⟶ Rf\_*(QC) at the Q spelling: it is invertible for an affine morphism of schemes and a complex of quasi-coherent modules, with no boundedness hypothesis”.

> **`Q(f_*C^•) ⟶ Rf_*(QC^•)` is invertible along an affine morphism of schemes**, for a
> cochain complex `C^•` of quasi-coherent `𝒪_X`-modules and with no boundedness hypothesis.
>
> The comparison is the unit of the derived direct image with the two comparisons between `Q` and
> `Qh ∘ quotient` inserted at either end.  Those are isomorphisms for every morphism, and the unit
> is invertible at a complex of quasi-coherent modules along an affine morphism by
> [Stacks, Tag 0G9N], `AlgebraicGeometry.AnyModel.isIso_derivedPushforwardUnit_app_of_isAffineHom`.
>
> This is the input that the source's proof of [Stacks, Tag 0B55] gets from [Stacks, Tag 08KS] for
> a closed embedding, and it is what the affine case of [Stacks, Tag 08I9] needs in its place.

```lean
theorem isIso_pushforwardComparisonQ_of_isAffineHom {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsAffineHom f]
    (C : CochainComplex
      (AlgebraicGeometry.RingedSpace.KFlatDerivedPullback.Modules X.toRingedSpace) ℤ)
    (hqc : ∀ n : ℤ, (C.X n : SheafOfModules.{u} X.ringCatSheaf).IsQuasicoherent) :
    IsIso (pushforwardComparisonQ f.toLRSHom.toShHom C)
```

## Tag 0G9P, a lemma

[Tag 0G9P](https://stacks.math.columbia.edu/tag/0G9P) in the Stacks Project.

**`AlgebraicGeometry.isIso_to_derivedGlobalSections_of_termwise_acyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedAcyclic/GlobalSections.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedAcyclic/GlobalSections.lean#L201).

> Let `X` be a quasi-separated and quasi-compact scheme and let `K` be a complex of
> quasi-coherent `𝒪_X`-modules each of which is right acyclic for `Γ(X, -)`. Then `Γ(X, K)`
> represents `RΓ(X, K)` in `D(Γ(X, 𝒪_X))`: the canonical comparison from termwise global sections
> to any right derived global-sections functor is an isomorphism at `K`.

```lean
theorem isIso_to_derivedGlobalSections_of_termwise_acyclic (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X]
    (K : CochainComplex X.Modules ℤ)
    (hqc : ∀ n, (K.X n).IsQuasicoherent)
    (hacyclic : ∀ n, (sectionsFunctor X ⊤).rightAcyclic (K.X n))
    (RΓ : DerivedCategory X.Modules ⥤ DerivedCategory (ModuleCat.{u} Γ(X, ⊤)))
    (α : (sectionsFunctor X ⊤).mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
      DerivedCategory.Qh ⋙ RΓ)
    [RΓ.IsRightDerivedFunctor α
      (HomotopyCategory.quasiIso X.Modules (ComplexShape.up ℤ))] :
    IsIso (α.app ((HomotopyCategory.quotient _ _).obj K))
```

## Tag 0G9Q, a lemma

[Tag 0G9Q](https://stacks.math.columbia.edu/tag/0G9Q) in the Stacks Project.

**`AlgebraicGeometry.hypercohomologySpectralSequence_isBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/HypercohomologySpectralSequence/Convergence.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/HypercohomologySpectralSequence/Convergence.lean#L275). The attribute's comment: “boundedness”.

> **Stacks Project, Tag 0G9Q.** The hypercohomology spectral sequence of an object of
> `D_QCoh(𝒪_X)` on a quasi-compact quasi-separated scheme is bounded: in each total degree only
> finitely many second-page terms are nonzero.
>
> The second page in bidegree `(i, j)` is `H^i(X, H^j(K))`, and `H^j(K)` is quasi-coherent, so by
> the uniform vanishing of the cohomology of quasi-coherent modules the term is zero unless
> `0 ≤ i ≤ N - 1`.

```lean
theorem hypercohomologySpectralSequence_isBounded (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] (K : QuasicoherentDerivedCategory X) :
    IsBounded (hypercohomologySpectralSequence X.toRingedSpace K.obj).spectralSequence
```

**`AlgebraicGeometry.hypercohomologySpectralSequence_abutsTo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/HypercohomologySpectralSequence/Convergence.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/HypercohomologySpectralSequence/Convergence.lean#L300). The attribute's comment: “convergence”.

> **Stacks Project, Tag 0G9Q.** The hypercohomology spectral sequence of an object `K` of
> `D_QCoh(𝒪_X)` on a quasi-compact quasi-separated scheme converges to the hypercohomology of `K`:
> there is a finite decreasing filtration of each `H^n(X, K)` whose graded pieces are the terms of
> the infinity page.
>
> The two hypotheses of the convergence statement of [Stacks, Tag 0BKK] are supplied by
> `AlgebraicGeometry.exists_isZero_hypercohomology_filtration_obj` and
> `AlgebraicGeometry.exists_isIso_hypercohomologyMap_filtration_ι`; what that statement delivers is
> the abutment of the unrenumbered spectral sequence to the hypercohomology of the underlying
> complex of the filtration, which is transported to `K` along the representative and then along
> the two renumberings.

```lean
theorem hypercohomologySpectralSequence_abutsTo (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] (K : QuasicoherentDerivedCategory X) :
    (hypercohomologySpectralSequence X.toRingedSpace K.obj).spectralSequence.AbutsTo
      (fun n => (DerivedCategory.homologyFunctor
        (ModuleCat.{u} ((structureSheafRing X.toRingedSpace).obj.obj
          (op (⊤ : Opens X.carrier)))) n).obj
        ((hypercohomologySpectralSequence X.toRingedSpace K.obj).truncation.RΓ.obj K.obj))
```

## Tag 08DZ, a lemma

[Tag 08DZ](https://stacks.math.columbia.edu/tag/08DZ) in the Stacks Project.

**`Stacks.Duality.DerivedPushforward.preservesColimitsOfShape_discrete_qcqsQuasiCoherentDerivedPushforward_locallySmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/QcohDirectSumsAnyModel.lean, line 599](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/QcohDirectSumsAnyModel.lean#L599). The attribute's comment: “locally\_small\_model”.

> **[Stacks, Tag 08DZ].** Let `f : X ⟶ S` be a quasi-separated and quasi-compact morphism of
> schemes. Then `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_S)` commutes with direct sums: for every index type
> `α` of the scheme universe it preserves `α`-indexed direct sums.
>
> The index types are those of the scheme universe because those are the ones for which
> `D_QCoh(𝒪_X)` has direct sums at all ([Stacks, Tag 08DT],
> `Stacks.Duality.DerivedPushforward.hasCoproducts_quasiCoherentDerivedCategory`).
>
> This is the tag at the locally small model of the derived categories, where that universe of index
> types is also the morphism universe; the companion registration
> `preservesColimitsOfShape_discrete_qcqsQuasiCoherentDerivedPushforward`
> is the tag at `CategoryTheory.HasDerivedCategory.standard`, where the two universes differ.

```lean
theorem preservesColimitsOfShape_discrete_qcqsQuasiCoherentDerivedPushforward_locallySmall
    (α : Type u) :
    PreservesColimitsOfShape (Discrete α)
      (qcqsQuasiCoherentDerivedPushforwardLocallySmall f)
```

**`Stacks.Duality.DerivedPushforward.preservesColimitsOfShape_discrete_qcqsQuasiCoherentDerivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/QuasiCoherentDirectSums.lean, line 558](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/QuasiCoherentDirectSums.lean#L558).

> **[Stacks, Tag 08DZ].** Let `f : X ⟶ S` be a quasi-separated and quasi-compact morphism of
> schemes. Then `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_S)` commutes with direct sums: for every index type
> `α` of the scheme universe it preserves `α`-indexed direct sums.
>
> The index types are those of the scheme universe because those are the ones for which
> `D_QCoh(𝒪_X)` has direct sums at all ([Stacks, Tag 08DT],
> `AlgebraicGeometry.hasCoproducts_quasicoherentDerivedCategory`).

```lean
theorem preservesColimitsOfShape_discrete_qcqsQuasiCoherentDerivedPushforward (α : Type u) :
    PreservesColimitsOfShape (Discrete α) (qcqsQuasiCoherentDerivedPushforward f)
```

**`Stacks.Duality.DerivedPushforward.preservesColimitsOfShape_discrete_qcqsRestrictedDerivedPushforward`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/QuasiCoherentDirectSumsLocallySmall.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/QuasiCoherentDirectSumsLocallySmall.lean#L415). The attribute's comment: “at the locally small model, which is the one Brown representability runs at”.

> **[Stacks, Tag 08DZ] at the locally small model, for the canonical restricted functor.** Let
> `f : X ⟶ Y` be a quasi-compact and quasi-separated morphism of schemes with `Y` quasi-compact.
> Then `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` commutes with direct sums indexed by any type of the
> scheme universe — which at this model is also the morphism universe of the category, so this is
> the hypothesis [Stacks, Tag 0A8G] asks for.
>
> `DerivedPushforward.preservesColimitsOfShape_discrete_qcqsQuasiCoherentDerivedPushforward` is
> the same statement at `CategoryTheory.HasDerivedCategory.standard`, where `HasCoproducts` of the
> morphism universe is false and the statement therefore cannot be fed to Brown representability.

```lean
instance preservesColimitsOfShape_discrete_qcqsRestrictedDerivedPushforward (α : Type u) :
    PreservesColimitsOfShape (Discrete α) (qcqsRestrictedDerivedPushforward f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.4, Tag 08DY](https://stacks.math.columbia.edu/tag/08DY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
