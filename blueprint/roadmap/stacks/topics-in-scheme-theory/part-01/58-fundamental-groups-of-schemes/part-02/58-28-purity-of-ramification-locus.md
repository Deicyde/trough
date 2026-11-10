---
declaration: section
origin: cited
lean: AlgebraicGeometry.DualizingDivisor.eq_top_of_isMinimalResolution_of_relativeDualizingModule_iso, AlgebraicGeometry.DualizingDivisor.definesRationalSingularity_of_relativeDualizingModule_iso, AlgebraicGeometry.etaleAt_of_etaleAt_outside_closure_of_ringKrullDim_eq_two, AlgebraicGeometry.etaleAt_of_etaleAt_codimensionOne
statement: formalized
proof: formalized
---

# 58.28 Purity of ramification locus

Section 58.28 of the Stacks Project, [Tag 0EA1](https://stacks.math.columbia.edu/tag/0EA1). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EA2, a lemma

[Tag 0EA2](https://stacks.math.columbia.edu/tag/0EA2) in the Stacks Project.

**`AlgebraicGeometry.DualizingDivisor.eq_top_of_isMinimalResolution_of_relativeDualizingModule_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/DualizingDivisor/MinimalResolution.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/DualizingDivisor/MinimalResolution.lean#L68). The attribute's comment: “second sentence: if f is a minimal resolution, then E = 0”.

> **[Stacks, Tag 0EA2], second sentence.** Let `A` be a Noetherian normal local domain of
> dimension two which is Nagata and has a dualizing module `ω_A`, and let `f : X ⟶ Spec(A)` be a
> minimal resolution of singularities. Let `ω_X = H^{-2}(f^×(ω_A[2]))` be as in
> [Stacks, Remark 0B4R] (`Stacks.Duality.relativeDualizingModule` at `ω_A[2]^~`, as in the first
> sentence, `definesRationalSingularity_of_relativeDualizingModule_iso`). If `ω_X ≅ 𝒪_X(E)` for an
> effective Cartier divisor `E ⊆ X` supported on the exceptional fibre, then `E = 0`, i.e. the ideal
> sheaf of `E` is the unit ideal `⊤`. The hypotheses are those of the first sentence with
> `IsMinimalResolution f` in place of `IsResolution f`; properness of `f` and quasi-compactness and
> quasi-separatedness of `X`, needed to form `f^×`, are derived from it inside the statement.

```lean
theorem eq_top_of_isMinimalResolution_of_relativeDualizingModule_iso (A : Type u) [CommRing A]
    [IsLocalRing A] [IsNoetherianRing A] [IsNormalDomain A] (hdim : ringKrullDim A = 2)
    (hNagata : IsNagataRing A) (ωA : ModuleCat.{u} A)
    (hω : Stacks.Duality.IsDualizingRingModule A ωA)
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) (hf : IsMinimalResolution f)
    (E : X.IdealSheafData) [Stacks.Divisors.IsEffectiveCartierDivisor E]
    (hE : ∀ x : X, x ∈ E.support → f x = closedPoint A)
    (e : haveI : IsProper f := hf.1.1.isProper
      haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
      haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
      Nonempty (relativeDualizingModule f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        ((derivedTilde (CommRingCat.of A)).obj ((singleFunctor (ModuleCat.{u} A) (-2)).obj ωA)) ≅
          (Stacks.Divisors.invertibleSheaf' E : X.Modules))) :
    E = ⊤
```

**`AlgebraicGeometry.DualizingDivisor.definesRationalSingularity_of_relativeDualizingModule_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/DualizingDivisor/RationalSingularity.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/DualizingDivisor/RationalSingularity.lean#L380). The attribute's comment: “first sentence: if ω\_X ≅ O\_X(E) for an effective Cartier divisor E supported on the exceptional fibre of a resolution, then A defines a rational singularity”.

> **[Stacks, Tag 0EA2], first sentence.** Let `A` be a Noetherian normal local domain of
> dimension two which is Nagata, has a dualizing module `ω_A`, and has a resolution of
> singularities `f : X ⟶ Spec(A)`. Let `ω_X` be as in [Stacks, Tag 0B4R]: the dualizing module of
> `X` normalized with respect to `ω_A`, that is `ω_X = H^{-2}(f^×(ω_A[2]))` with `f^×` the twisted
> inverse image (`Stacks.Duality.relativeDualizingModule` at `ω_A[2]^~`, whose degree `-dim X` is
> `-2`). If `ω_X ≅ 𝒪_X(E)` for an effective Cartier divisor `E ⊆ X` supported on the exceptional
> fibre (every point of `E` lies over the closed point), then `A` defines a rational singularity.
>
> Following the source, duality turns the map `𝒪_X ⟶ 𝒪_X(E) = ω_X` into a generator of
> `Hom(RΓ(X, 𝒪_X[2]), ω_A[2])` (`hom_derivedSectionsUnitShift_free`); the criterion
> `Stacks.PurityRamification.subsingleton_homology_succ_of_forall_eq_smul` (depth of `ω_A`,
> [Stacks, Tag 0AXC], torsion of `H¹(X, 𝒪_X)`) gives `H¹(X, 𝒪_X) = 0`, and a resolution with
> `H¹(X, 𝒪_X) = 0` makes `A` a rational singularity
> (`definesRationalSingularity_of_isResolution_of_isZero_structureSheafH1`). Forming `f^×`, hence
> `ω_X`, uses that `f` is proper and `X` quasi-compact and quasi-separated; inside the statement
> these are derived from `IsResolution f` (a resolution is proper over the affine scheme
> `Spec(A)`) by `haveI`, not assumed.

```lean
theorem definesRationalSingularity_of_relativeDualizingModule_iso (A : Type u) [CommRing A]
    [IsLocalRing A] [IsNoetherianRing A] [IsNormalDomain A] (hdim : ringKrullDim A = 2)
    (hNagata : IsNagataRing A) (ωA : ModuleCat.{u} A)
    (hω : Stacks.Duality.IsDualizingRingModule A ωA)
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) (hf : IsResolution f)
    (E : X.IdealSheafData) [Stacks.Divisors.IsEffectiveCartierDivisor E]
    (hE : ∀ x : X, x ∈ E.support → f x = closedPoint A)
    (e : haveI : IsProper f := hf.1.isProper
      haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
      haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
      Nonempty (relativeDualizingModule f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        ((derivedTilde (CommRingCat.of A)).obj ((singleFunctor (ModuleCat.{u} A) (-2)).obj ωA)) ≅
          (Stacks.Divisors.invertibleSheaf' E : X.Modules))) :
    DefinesRationalSingularity A
```

## Tag 0EA3, a lemma

[Tag 0EA3](https://stacks.math.columbia.edu/tag/0EA3) in the Stacks Project.

**`AlgebraicGeometry.etaleAt_of_etaleAt_outside_closure_of_ringKrullDim_eq_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityRamification/EtaleAtDimensionTwo.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityRamification/EtaleAtDimensionTwo.lean#L52).

> **Stacks Project, Tag 0EA3.** Let `f : X ⟶ Spec A` be a morphism (locally) of finite type and
> `x ∈ X`. Assume `A` is an excellent regular local ring, `𝒪_{X, x}` is normal of dimension `2`,
> and `f` is étale at every point outside `closure {x}`. Then `f` is étale at `x`.

```lean
theorem etaleAt_of_etaleAt_outside_closure_of_ringKrullDim_eq_two {A : Type u} [CommRing A]
    [IsRegularLocalRing A] (hA : IsExcellent A) {X : Scheme.{u}} (f : X ⟶ Spec (.of A))
    [LocallyOfFiniteType f] (x : X) (hX : IsNormalRing (X.presheaf.stalk x))
    (hdim : ringKrullDim (X.presheaf.stalk x) = 2)
    (het : ∀ z : X, z ∉ closure ({x} : Set X) → EtaleAt f z) : EtaleAt f x
```

## Tag 0EA4, a lemma

[Tag 0EA4](https://stacks.math.columbia.edu/tag/0EA4) in the Stacks Project.

**`AlgebraicGeometry.etaleAt_of_etaleAt_codimensionOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityRamificationLocus/Induction.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityRamificationLocus/Induction.lean#L378). The attribute's comment: “the whole lemma: hypotheses (1) `𝒪_{X,x}` normal of dimension `≥ 1`, (2) `𝒪_{Y,f x}` regular, (3) `f` locally of finite type, (4) `f` étale at every `x' ⤳ x` with `dim 𝒪_{X,x'} = 1`; the conclusion is `EtaleAt f x`.”. References: EGA IV (21.12.14), “more general”; SGA 1 X (3.1), “more general”.

> **[Stacks, Tag 0EA4], purity of the ramification locus.** Let `f : X ⟶ Y` be a morphism of
> locally Noetherian schemes, let `x : X` and `y = f x`, and assume that (1) `𝒪_{X,x}` is normal of
> dimension at least one, (2) `𝒪_{Y,y}` is regular, (3) `f` is locally of finite type, and (4) `f`
> is étale at every specialization `x' ⤳ x` with `dim 𝒪_{X,x'} = 1`. Then `f` is étale at `x`.
>
> The hypotheses are exactly the tag's own. "Normal" is `IsNormalRing` of the stalk (for a local
> ring: a normal domain), "dimension" is `ringKrullDim`, and a specialization `x' ⤳ x` of the
> source is Mathlib's `x' ⤳ x`, that is `x ∈ closure {x'}`.
>
> The proof is the source's: the proper generizations of `x` are handled by induction on
> `dim 𝒪_{X,x}`, base change to `Spec 𝒪_{Y,f x}` ([Stacks, Tag 0476]) and then to the spectrum of
> its completion changes neither étaleness at the relevant point (both being flat) nor normality of
> the local ring there (Serre's criterion), and over the complete — hence excellent — regular local
> base the induction of `AlgebraicGeometry.etaleAt_of_etaleAt_codimensionOne_over_excellent`
> applies, with [Stacks, Tag 0EA3] in dimension two and [Stacks, Tag 0BMB] above it.

```lean
theorem etaleAt_of_etaleAt_codimensionOne
    {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsLocallyNoetherian X] [IsLocallyNoetherian Y] [LocallyOfFiniteType f] (x : X)
    (hX : IsNormalRing (X.presheaf.stalk x))
    (hY : IsRegularLocalRing (Y.presheaf.stalk (f x)))
    (hpositive : 1 ≤ ringKrullDim (X.presheaf.stalk x))
    (hetale : ∀ x' : X, x' ⤳ x → ringKrullDim (X.presheaf.stalk x') = 1 → EtaleAt f x') :
    EtaleAt f x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.28, Tag 0EA1](https://stacks.math.columbia.edu/tag/0EA1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
