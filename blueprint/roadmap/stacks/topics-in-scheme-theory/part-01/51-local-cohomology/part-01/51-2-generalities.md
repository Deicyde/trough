---
declaration: section
origin: cited
lean: Stacks.LocalCohomologySequence.cohomologyWithSupportTildeSpanSingletonIso, Stacks.LocalCohomologyTilde.mem_sectionsWithSupportIn_iff, Stacks.LocalCohomologyTilde.image_sectionsWithSupportIn, Stacks.LocalCohomologyTilde.image_primaryComponent, Stacks.LocalCohomologyTilde.sectionsWithSupportTildeIso, Stacks.LocalCohomologyTilde.localCohomologyIsoDerivedSectionsWithSupport, Stacks.LocalCohomology.nonempty_complementSheafCohomology_iso_localCohomologyModule, Stacks.LocalCohomology.exists_module_iso_restrict_tilde
statement: formalized
proof: formalized
---

# 51.2 Generalities

Section 51.2 of the Stacks Project, [Tag 0DWQ](https://stacks.math.columbia.edu/tag/0DWQ). 6 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A6T, a lemma

[Tag 0A6T](https://stacks.math.columbia.edu/tag/0A6T) in the Stacks Project.

**`Stacks.LocalCohomologySequence.cohomologyWithSupportTildeSpanSingletonIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyDegreewise.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyDegreewise.lean#L125). The attribute's comment: “degreewise, for a module and a principal ideal”. References: EGA III (1.1.10), “principal ideal, Noeth.”.

> **Stacks 0A6T degreewise, for a module and a principal ideal.**  Let `A` be a Noetherian
> ring, `f : A`, `X = Spec A` and `Z = V(f)`.  For an `A`-module `M` the cohomology of `X` with
> support in `Z` of the sheaf `M̃`, read as an `A`-module, is the algebraic local cohomology
> `H^n_Z(M)` of `M`, in every degree `n`.

```lean
def cohomologyWithSupportTildeSpanSingletonIso [IsNoetherianRing A] (f : A)
    (M : ModuleCat.{u} A) (n : ℕ) :
    (globalToBase A).obj ((cohomologyWithSupport (Ideal.span {f}) n).obj (tildeSheaf M)) ≅
      (localCohomologySpanSingleton A f n).obj M
```

**`Stacks.LocalCohomologyTilde.mem_sectionsWithSupportIn_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyTilde.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyTilde.lean#L98). The attribute's comment: “degree zero”.

> **Stacks 0A6T in degree zero.** An element of `M` is an algebraic section with support in a
> subset `T` of the spectrum exactly when the corresponding global section of `M̃` has all its
> germs outside `T` equal to zero.

```lean
theorem mem_sectionsWithSupportIn_iff (T : Set (PrimeSpectrum R)) (m : M) :
    m ∈ Stacks.LocalCohomology.sectionsWithSupportIn R T M ↔
      (tilde.toOpen M ⊤) m ∈ (supportedSectionsSubmodule T (tilde M)).obj (op ⊤)
```

**`Stacks.LocalCohomologyTilde.image_sectionsWithSupportIn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyTilde.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyTilde.lean#L117). The attribute's comment: “degree zero”.

> **Stacks 0A6T in degree zero.** The canonical isomorphism from `M` to the global sections of
> `M̃` carries the algebraic sections with support in `T` onto the geometric ones.

```lean
theorem image_sectionsWithSupportIn (T : Set (PrimeSpectrum R)) :
    (tilde.toOpen M ⊤).hom '' (Stacks.LocalCohomology.sectionsWithSupportIn R T M : Set M) =
      ((supportedSectionsSubmodule T (tilde M)).obj (op ⊤) :
        Set ((tilde M).val.obj (op ⊤)))
```

**`Stacks.LocalCohomologyTilde.image_primaryComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyTilde.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyTilde.lean#L147). The attribute's comment: “degree zero”.

> **Stacks 0A6T in degree zero.** For a finitely generated ideal `I` and `Z = V(I)`, the
> canonical isomorphism from `M` to the global sections of `M̃` carries the degree-zero local
> cohomology `H⁰_Z(M)`, namely the `I`-power-torsion submodule, onto the global sections of `M̃`
> with support in `Z`.

```lean
theorem image_primaryComponent :
    (tilde.toOpen M ⊤).hom '' (I.primaryComponent M : Set M) =
      ((supportedSectionsSubmodule (zeroLocus (I : Set R)) (tilde M)).obj (op ⊤) :
        Set ((tilde M).val.obj (op ⊤)))
```

**`Stacks.LocalCohomologyTilde.sectionsWithSupportTildeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyTildeFunctor.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyTildeFunctor.lean#L354). The attribute's comment: “degree zero, as a natural isomorphism of functors”.

> For a closed subset `T` of `Spec A`, the global sections with support in `T` of the sheaf
> `M̃`, read as an `A`-module, are the algebraic sections of `M` with support in `T`, naturally in
> `M`.

```lean
def sectionsWithSupportTildeIso :
    tildeSupportSheaf T hT ⋙ globalToBase A ≅
      sectionsWithSupportInFunctor.{u, u} A T
```

**`Stacks.LocalCohomologyTilde.localCohomologyIsoDerivedSectionsWithSupport`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyTildeSectionsWithSupport.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyTildeSectionsWithSupport.lean#L250).

> Let `A` be a ring, let `I ⊆ A` be a finitely generated ideal and set `Z = V(I) ⊆ X = Spec A`.
> For `K ∈ D(A)`, corresponding to `K̃ ∈ D_QCoh(𝒪_X)` by [Stacks, Tag 06Z0], there is an
> isomorphism
>
> `RΓ_Z(K) ≅ RΓ_Z(X, K̃)`
>
> in `D(A)`, functorial in `K`. On the left is the local cohomology functor of
> [Stacks, Tag 0A6Q], followed by the inclusion of the complexes with `I`-power-torsion cohomology
> into `D(A)`. On the right is the total right derived functor
> `RΓ_Z(X, -) : D(𝒪_X) ⥤ D(𝒪_X(X))` of `F ↦ Γ_Z(X, F)` on the unbounded derived category, as in
> [Stacks, Section 0G6Y], applied to `K̃` and read as a complex of `A`-modules by restriction of
> scalars along the canonical isomorphism `A ≅ 𝒪_X(X)`.
>
> The ring is arbitrary, `K` is an arbitrary object of the unbounded derived category, and the
> only hypothesis on `I` is finite generation.

```lean
def localCohomologyIsoDerivedSectionsWithSupport :
    Dualizing.localCohomologyFunctor (A : Type u) I hI ⋙
        (Dualizing.derivedPowerTorsionProperty (A : Type u) I hI).ι ≅
      (tildeSheafFunctor A).mapDerivedCategory ⋙
        canonicalDerivedSectionsWithSupport (Spec A).toRingedSpace (vanishingSet A I)
          (isClosed_vanishingSet A I) ⋙
        (globalToBase A).mapDerivedCategory
```

## Tag 0DWR, a lemma

[Tag 0DWR](https://stacks.math.columbia.edu/tag/0DWR) in the Stacks Project.

**`Stacks.LocalCohomology.nonempty_complementSheafCohomology_iso_localCohomologyModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/Generalities/ComplementCohomologyModule.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/Generalities/ComplementCohomologyModule.lean#L99). The attribute's comment: “higher_cohomology_comparison”.

> **[Stacks, Tag 0DWR] (2), the isomorphisms above degree zero.** Let `R` be a ring and let
> `I ⊆ R` be a finitely generated ideal. Set `X = Spec R`, `Z = V(I)` and `U = X ∖ Z`. Let `F` be
> an `𝒪_U`-module and let `M` be an `R`-module with `F ≅ M̃|_U`. Then
> `H^p(U, F) ≅ H^{p+1}_Z(M)` as `R`-modules for every `p ≥ 1`.
>
> The isomorphism is transported along `F ≅ M̃|_U`, then
> `complementSheafCohomologyTildeIso` passes to the cohomology over `U` of `M̃` on `X`, where
> `Stacks.LocalCohomologySequence.nonempty_complementCohomologyBase_iso_localCohomologyModule` is
> the comparison with local cohomology. The source only asserts that the two modules are
> isomorphic, so the conclusion is nonemptiness of the type of isomorphisms.

```lean
theorem nonempty_complementSheafCohomology_iso_localCohomologyModule (hI : I.FG)
    (M : ModuleCat.{u} R) (F : (complementZeroLocus R I : Scheme).Modules)
    (e : F ≅ complementTilde R I M) (p : ℕ) (hp : 1 ≤ p) :
    Nonempty ((complementSheafCohomology R I p).obj F ≅
      localCohomologyModule R I hI M ((p + 1 : ℕ) : ℤ))
```

**`Stacks.LocalCohomology.exists_module_iso_restrict_tilde`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/Generalities/QuasiCoherentExtension.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/Generalities/QuasiCoherentExtension.lean#L65). The attribute's comment: “extension”.

> **Stacks Project, Tag 0DWR.** Every quasi-coherent module on the complement of the zero
> locus of a finitely generated ideal in an affine spectrum is the restriction of the sheaf
> associated to a module.

```lean
theorem exists_module_iso_restrict_tilde
    (R : Type u) [CommRing R] (I : Ideal R) (_hI : I.FG)
    (F : (complementZeroLocus R I : Scheme).Modules) [F.IsQuasicoherent] :
    ∃ M : ModuleCat.{u} R,
      Nonempty
        (F ≅ ((tilde.functor (CommRingCat.of R)).obj M).restrict
          (complementZeroLocus R I).ι)
```

**`Stacks.LocalCohomology.exact_lowDegreeSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/LowDegree/CechSectionsComparison.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/LowDegree/CechSectionsComparison.lean#L373). The attribute's comment: “low_degree_sequence”. References: EGA III (1.4.3), “(1.4.3.2), special case”; SGA 2 II (Corollary4), “(4.2)”; SGA 4 V (6.5), “(6.5.3), special case”.

> **Stacks 0BK0, the low-degree sequence.** Let `I` be a finitely generated ideal of a
> commutative ring `A`, let `U = Spec A \ V(I)`, let `M` be an `A`-module and let `F` be a sheaf of
> modules on `U` identified with the restriction to `U` of the sheaf associated to `M`. Then the
> four-term sequence
> `0 ⟶ H⁰_I(M) ⟶ M ⟶ Γ(U, F) ⟶ H¹_I(M) ⟶ 0`
> is exact: the map out of degree-zero local cohomology is injective, the sequence is exact at `M`
> and at `Γ(U, F)`, and the connecting map onto `H¹_I(M)` is surjective.
>
> Every ideal of a Noetherian ring is finitely generated, by `Ideal.fg_of_isNoetherianRing`, so
> this covers the Noetherian hypothesis of the source; and it does not assume `M` finite or `F`
> coherent, which the source does.
>
> The same four-term sequence is the first half of clause (2) of Stacks 0DWR, which assumes only
> that `I` is finitely generated. The second half of that clause, the comparison
> `H^p(U, F) ≅ H^{p+1}_I(M)` in degrees `p ≥ 1`, `A`-linearly and for the same `F` and `M`, is
> `Stacks.LocalCohomology.nonempty_complementSheafCohomology_iso_localCohomologyModule`, under the
> same hypothesis `I.FG`.

```lean
theorem exact_lowDegreeSequence (M : ModuleCat.{max u v} A)
    (F : SheafOfModules.{max u v} (complementZeroLocus A I : Scheme).ringCatSheaf)
    (e : F ≅ complementTilde A I M) :
    Function.Injective (localCohomologyZeroToModule A I hI M).hom ∧
      Function.Exact (localCohomologyZeroToModule A I hI M)
        (restrictionToComplement (localizationTriangleData.{v} A I hI) M F e) ∧
      Function.Exact (restrictionToComplement (localizationTriangleData.{v} A I hI) M F e)
        (localizationBoundary (localizationTriangleData.{v} A I hI) M F e) ∧
      Function.Surjective (localizationBoundary (localizationTriangleData.{v} A I hI) M F e)
```

**`Stacks.LocalCohomology.iso_restrict_tilde_globalSectionsModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/LowDegree/GlobalSectionsChoice.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/LowDegree/GlobalSectionsChoice.lean#L150). The attribute's comment: “global_sections_choice”.

> A quasi-coherent module on the complement of `V(I)` is the restriction of the associated sheaf
> of its global-sections `R`-module.

```lean
theorem iso_restrict_tilde_globalSectionsModule
    (F : (complementZeroLocus R I : Scheme).Modules) [F.IsQuasicoherent] :
    Nonempty
      (F ≅ ((tilde.functor (CommRingCat.of R)).obj
        (complementGlobalSections R I F)).restrict
        (complementZeroLocus R I).ι)
```

**`Stacks.LocalCohomology.isZero_localCohomology_zero_globalSectionsModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/LowDegree/GlobalSectionsChoice.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/LowDegree/GlobalSectionsChoice.lean#L161). The attribute's comment: “global_sections_choice”.

> The degree-zero local cohomology of the global-sections module vanishes.

```lean
theorem isZero_localCohomology_zero_globalSectionsModule
    (F : (complementZeroLocus R I : Scheme).Modules) [F.IsQuasicoherent] :
    IsZero (localCohomologyModule R I hI (complementGlobalSections R I F) 0)
```

**`Stacks.LocalCohomology.isZero_localCohomology_one_globalSectionsModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/LowDegree/GlobalSectionsChoice.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/LowDegree/GlobalSectionsChoice.lean#L181). The attribute's comment: “global_sections_choice”.

> The degree-one local cohomology of the global-sections module vanishes.

```lean
theorem isZero_localCohomology_one_globalSectionsModule
    (F : (complementZeroLocus R I : Scheme).Modules) [F.IsQuasicoherent] :
    IsZero (localCohomologyModule R I hI (complementGlobalSections R I F) 1)
```

## Tag 0DWS, a lemma

[Tag 0DWS](https://stacks.math.columbia.edu/tag/0DWS) in the Stacks Project.

**`Stacks.LocalCohomology.isIso_homology_localCohomologyComparison_of_isIPowerTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/AlreadyTorsion.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/AlreadyTorsion.lean#L266).

> **Stacks 0DWS.** For an `I`-power-torsion module `M`, the canonical map
> `H^i_{V(I) ∩ V(J)}(M) ⟶ H^i_{V(J)}(M)` is an isomorphism in every degree.

```lean
theorem isIso_homology_localCohomologyComparison_of_isIPowerTorsion
    (I J : Ideal A) (hI : I.FG) (hJ : J.FG) (M : ModuleCat.{v} A)
    (hM : IsIPowerTorsion A M I) (i : ℤ) :
    IsIso ((DerivedCategory.homologyFunctor (ModuleCat.{v} A) i).map
      (Stacks.Algebraization.localCohomologyComparison A (I ⊔ J) J
        (Submodule.FG.sup hI hJ) hJ le_sup_right
        ((DerivedCategory.singleFunctor (ModuleCat.{v} A) 0).obj M)))
```

## Tag 0DWT, a lemma

[Tag 0DWT](https://stacks.math.columbia.edu/tag/0DWT) in the Stacks Project.

**`Stacks.LocalCohomology.isIso_colimitPrincipalLocalCohomologyToModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/AwayColimit/MultiplicativeSet.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/AwayColimit/MultiplicativeSet.lean#L369). The attribute's comment: “degree zero”.

> **Stacks 0DWT, degree zero.** Let `S` be a multiplicative subset of a commutative ring `A`
> and let `M` be an `A`-module whose localization at `S` vanishes. Then the canonical map
> `colim_{f ∈ S} H⁰_{V(f)}(M) ⟶ M` is an isomorphism.
>
> The legs `H⁰_{V(f)}(M) ⟶ M` are injective, which gives injectivity on the filtered colimit; and
> every `m ∈ M` is annihilated by some `f ∈ S`, hence restricts to zero on `Spec A ∖ V(f)` and so
> lies in the image of the leg at `f`.

```lean
theorem isIso_colimitPrincipalLocalCohomologyToModule (S : Submonoid A) (M : ModuleCat.{u} A)
    [Subsingleton (LocalizedModule S M)] :
    IsIso (colimitPrincipalLocalCohomologyToModule A S M)
```

**`Stacks.LocalCohomology.isZero_colimitPrincipalLocalCohomologyOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/AwayColimit/MultiplicativeSet.lean, line 543](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/AwayColimit/MultiplicativeSet.lean#L543). The attribute's comment: “degree one”.

> **Stacks 0DWT, degree one.** Let `S` be a multiplicative subset of a commutative ring `A` and
> let `M` be an `A`-module whose localization at `S` vanishes. Then
> `colim_{f ∈ S} H¹_{V(f)}(M) = 0`.
>
> Every class in the system dies at a larger index, so every leg into the colimit is zero and the
> identity of the colimit is zero.

```lean
theorem isZero_colimitPrincipalLocalCohomologyOne (S : Submonoid A) (M : ModuleCat.{u} A)
    [Subsingleton (LocalizedModule S M)] :
    IsZero (colimit (principalLocalCohomologySystem A S M 1))
```

## Tag 0DWU, a lemma

[Tag 0DWU](https://stacks.math.columbia.edu/tag/0DWU) in the Stacks Project.

**`Stacks.LocalCohomology.range_localCohomologyAwayComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/AwayColimit/Basic.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/AwayColimit/Basic.lean#L281). The attribute's comment: “part (1)”.

> **Stacks 0DWU, part (1).** The image of the comparison out of the colimit of the local
> cohomology modules on the supports `V(I + (f))`, for `f` outside the prime `𝔭`, is the kernel of
> localization at `𝔭`.

```lean
theorem range_localCohomologyAwayComparison
    (A : Type u) [CommRing A] (I p : Ideal A) (hp : p.IsPrime) (hI : I.FG)
    (M : ModuleCat.{u} A) (i : ℤ) (_hi : 0 ≤ i) :
    LinearMap.range (localCohomologyAwayColimitData A I p hp hI M i).comparison.hom =
      LinearMap.ker (LocalizedModule.mkLinearMap p.primeCompl
        (localCohomologyModule A I hI M i))
```

**`Stacks.LocalCohomology.localCohomologyAwayComparison_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/AwayColimit/Basic.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/AwayColimit/Basic.lean#L306). The attribute's comment: “part (2)”.

> **Stacks 0DWU, part (2).** If `Hⁱ⁻¹_{V(I)}(M)` vanishes after localization at the prime `𝔭`,
> the comparison out of the colimit is injective.

```lean
theorem localCohomologyAwayComparison_injective
    (A : Type u) [CommRing A] (I p : Ideal A) (hp : p.IsPrime) (hI : I.FG)
    (M : ModuleCat.{u} A) (i : ℤ) (_hi : 0 ≤ i)
    (hvan : Subsingleton
      (LocalizedModule p.primeCompl (localCohomologyModule A I hI M (i - 1)))) :
    Function.Injective
      (localCohomologyAwayColimitData A I p hp hI M i).comparison.hom
```

**`Stacks.LocalCohomology.localCohomologyAwayComparison_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/AwayColimit/Basic.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/AwayColimit/Basic.lean#L344). The attribute's comment: “part (3)”.

> **Stacks 0DWU, part (3).** If `Hⁱ⁻¹_{V(I)}(M)` and `Hⁱ_{V(I)}(M)` both vanish after
> localization at the prime `𝔭`, the comparison out of the colimit is an isomorphism.

```lean
theorem localCohomologyAwayComparison_isIso
    (A : Type u) [CommRing A] (I p : Ideal A) (hp : p.IsPrime) (hI : I.FG)
    (M : ModuleCat.{u} A) (i : ℤ) (hi : 0 ≤ i)
    (hvanPrev : Subsingleton
      (LocalizedModule p.primeCompl (localCohomologyModule A I hI M (i - 1))))
    (hvan : Subsingleton
      (LocalizedModule p.primeCompl (localCohomologyModule A I hI M i))) :
    IsIso (localCohomologyAwayColimitData A I p hp hI M i).comparison
```

## Tag 0DWV, a lemma

[Tag 0DWV](https://stacks.math.columbia.edu/tag/0DWV) in the Stacks Project.

**`Stacks.LocalCohomology.localCohomologyModuleMapOfLE_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/F6Sweep/LocalCohomologySupportSurjectivity.lean, line 1155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/F6Sweep/LocalCohomologySupportSurjectivity.lean#L1155). The attribute's comment: “surjectivity”.

> **Stacks 0DWV, part (1).** Surjectivity of the comparison map.
>
> The covering set of the bare tag `0DWV` is three declarations, one per part of the source. The
> other two are `Stacks.LocalCohomology.localCohomologyModuleMapOfLE_injective` and
> `Stacks.LocalCohomology.isIso_localCohomologyModuleMapOfLE`.

```lean
public theorem localCohomologyModuleMapOfLE_surjective
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (I J : Ideal A) (hI : I.FG) (hJ : J.FG) (hIJ : I ≤ J)
    (M : ModuleCat.{v} A) (i : ℤ) (hi : 0 ≤ i)
    (hvan : ∀ (p : Ideal A) [p.IsPrime], I ≤ p → ¬ J ≤ p →
      IsZero (localCohomologyModule (Localization.AtPrime p)
        (p.map (algebraMap A (Localization.AtPrime p)))
        ((Ideal.fg_of_isNoetherianRing p).map (algebraMap A (Localization.AtPrime p)))
        (ModuleCat.of (Localization.AtPrime p) (LocalizedModule p.primeCompl M)) i)) :
    Function.Surjective
      ((DerivedCategory.homologyFunctor (ModuleCat.{v} A) i).map
        (Stacks.Algebraization.localCohomologyComparison A J I hJ hI hIJ
          ((DerivedCategory.singleFunctor (ModuleCat.{v} A) 0).obj M))).hom
```

**`Stacks.LocalCohomology.localCohomologyModuleMapOfLE_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/SupportInjectivity/Basic.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/SupportInjectivity/Basic.lean#L429). The attribute's comment: “injectivity”.

> **Injectivity of the change of support.** For finitely generated ideals `I ≤ J` of a
> Noetherian ring, the canonical map `Hⁱ_{V(J)}(M) ⟶ Hⁱ_{V(I)}(M)` is injective as soon as the
> local cohomology of `M_𝔭` with support in the maximal ideal of `A_𝔭` vanishes in degree `i - 1`
> for every prime `𝔭 ∈ V(I) \ V(J)`.

```lean
public theorem localCohomologyModuleMapOfLE_injective
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (I J : Ideal A) (hI : I.FG) (hJ : J.FG) (hIJ : I ≤ J)
    (M : ModuleCat.{v} A) (i : ℤ) (_hi : 0 ≤ i)
    (hvan : ∀ (p : Ideal A) [p.IsPrime], I ≤ p → ¬ J ≤ p →
      Subsingleton
        (localCohomologyModule (Localization.AtPrime p)
          (p.map (algebraMap A (Localization.AtPrime p)))
          ((Ideal.fg_of_isNoetherianRing p).map (algebraMap A (Localization.AtPrime p)))
          (ModuleCat.of (Localization.AtPrime p) (LocalizedModule p.primeCompl M))
          (i - 1))) :
    Function.Injective
      ((DerivedCategory.homologyFunctor (ModuleCat.{v} A) i).map
        (Stacks.Algebraization.localCohomologyComparison A J I hJ hI hIJ
          ((DerivedCategory.singleFunctor (ModuleCat.{v} A) 0).obj M))).hom
```

**`Stacks.LocalCohomology.isIso_localCohomologyModuleMapOfLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/SupportInjectivity/Basic.lean, line 533](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/SupportInjectivity/Basic.lean#L533). The attribute's comment: “isomorphism”.

> **The change of support is an isomorphism.** For finitely generated ideals `I ≤ J` of a
> Noetherian ring, the canonical map `Hⁱ_{V(J)}(M) ⟶ Hⁱ_{V(I)}(M)` is an isomorphism as soon as the
> local cohomology of `M_𝔭` with support in the maximal ideal of `A_𝔭` vanishes in degrees `i` and
> `i - 1` for every prime `𝔭 ∈ V(I) \ V(J)`.

```lean
public theorem isIso_localCohomologyModuleMapOfLE
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (I J : Ideal A) (hI : I.FG) (hJ : J.FG) (hIJ : I ≤ J)
    (M : ModuleCat.{v} A) (i : ℤ) (hi : 0 ≤ i)
    (hvan : ∀ (p : Ideal A) [p.IsPrime], I ≤ p → ¬ J ≤ p →
      (IsZero (localCohomologyModule (Localization.AtPrime p)
        (p.map (algebraMap A (Localization.AtPrime p)))
        ((Ideal.fg_of_isNoetherianRing p).map (algebraMap A (Localization.AtPrime p)))
        (ModuleCat.of (Localization.AtPrime p) (LocalizedModule p.primeCompl M)) i) ∧
      IsZero (localCohomologyModule (Localization.AtPrime p)
        (p.map (algebraMap A (Localization.AtPrime p)))
        ((Ideal.fg_of_isNoetherianRing p).map (algebraMap A (Localization.AtPrime p)))
        (ModuleCat.of (Localization.AtPrime p) (LocalizedModule p.primeCompl M))
        (i - 1)))) :
    IsIso ((DerivedCategory.homologyFunctor (ModuleCat.{v} A) i).map
      (Stacks.Algebraization.localCohomologyComparison A J I hJ hI hIJ
        ((DerivedCategory.singleFunctor (ModuleCat.{v} A) 0).obj M)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.2, Tag 0DWQ](https://stacks.math.columbia.edu/tag/0DWQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
