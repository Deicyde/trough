---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isCoherent_and_supportOfSheaf_eq_univ_modulePushforward_structureSheaf_preimage, AlgebraicGeometry.Space.isCoherent_modulePushforward_structureSheaf_preimage, AlgebraicGeometry.Space.supportOfSheaf_modulePushforward_structureSheaf_preimage_eq_univ, AlgebraicGeometry.Space.isCoherent_modulePushforward_structureSheaf_preimage_of_isLocallyNoetherian, AlgebraicGeometry.Space.idealSmul_pushforward_eq_of_isQuasicoherentOnSite, AlgebraicGeometry.Space.isAffineSpace_of_isFinite_of_isSurjective
statement: formalized
proof: formalized
---

# 69.17 Finite morphisms and affines

Section 69.17 of the Stacks Project, [Tag 07VN](https://stacks.math.columbia.edu/tag/07VN). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GF7, a lemma

[Tag 0GF7](https://stacks.math.columbia.edu/tag/0GF7) in the Stacks Project.

**`AlgebraicGeometry.Space.isCoherent_and_supportOfSheaf_eq_univ_modulePushforward_structureSheaf_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteDirectImageChartCartesian.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteDirectImageChartCartesian.lean#L259). The attribute's comment: “the whole statement: for f finite and surjective with X locally Noetherian and i : Z -> X a closed immersion, the direct image f'\_* O\_\{Z'} along the induced morphism of the inverse image is a coherent O\_Z-module, and its support is all of Z”.

> Let `S` be a scheme and let `f : Y ⟶ X` be a morphism of algebraic spaces over `S` which is
> finite and surjective, with `X` locally Noetherian.  Let `i : Z ⟶ X` be a closed immersion, let
> `i' : Z' ⟶ Y` be the inverse image of `Z`, and let `f' : Z' ⟶ Z` be the induced morphism.  Then
> `𝒢 = f'_*𝒪_{Z'}` is a coherent `𝒪_Z`-module whose support is all of `Z`.

```lean
theorem isCoherent_and_supportOfSheaf_eq_univ_modulePushforward_structureSheaf_preimage
    {Z Z' : AlgebraicSpaces B S hS} (f : Y ⟶ X) (i : Z ⟶ X) {i' : Z' ⟶ Y} {f' : Z' ⟶ Z}
    (sq : IsPullback i' f' f i) (hf : IsFinite B S hS f.hom)
    (hsurj : IsSurjective B S hS f.hom)
    (hX : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} ↦ IsLocallyNoetherian T))
    (hi : IsClosedImmersion B S hS i.hom) :
    IsCoherent B S hS Z.1 Z.2 ((modulePushforward B S hS f').obj
        (SheafOfModules.unit (structureRingSheaf B S hS Z'))) ∧
      supportOfSheaf B S hS Z.1 ((SheafOfModules.toSheaf _).obj
        ((modulePushforward B S hS f').obj
          (SheafOfModules.unit (structureRingSheaf B S hS Z')))) = Set.univ
```

**`AlgebraicGeometry.Space.isCoherent_modulePushforward_structureSheaf_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePreimageStructureSheaf.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePreimageStructureSheaf.lean#L241). The attribute's comment: “coherence of the direct image, granted the chart case hchart of Stacks 03DW which Tag 07UH already carries”.

> **The coherence assertion of Stacks 0GF7, granted the chart case `hchart`.**  Let
> `f : Y ⟶ X` be a finite morphism of algebraic spaces over `S` with `X` locally Noetherian, let
> `i : Z ⟶ X` be a closed immersion, and let `f' : Z' ⟶ Z` be the base change of `f` along `i`.
> Then `𝒢 = f'_*𝒪_{Z'}` is a coherent `𝒪_Z`-module.
>
> `Z` is locally Noetherian by Stacks 06ED and 04ZK, `f'` is finite by Stacks 03ZS, `Z'` is
> locally Noetherian for the same reason as `Z`, and `𝒪_{Z'}` is then coherent by Stacks 07UB; so
> this is `AlgebraicGeometry.Space.isCoherent_modulePushforward_of_isFinite`, whose hypothesis
> `hchart` is the étale-site form of Stacks 01Y6, that is Stacks 03DW, which this development
> does not carry.  Surjectivity of `f` is not used.

```lean
theorem isCoherent_modulePushforward_structureSheaf_preimage (f : Y ⟶ X) (i : Z ⟶ X)
    {i' : Z' ⟶ Y} {f' : Z' ⟶ Z} (sq : IsPullback i' f' f i)
    (hf : IsFinite B S hS f.hom)
    (hX : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} ↦ IsLocallyNoetherian T))
    (hi : IsClosedImmersion B S hS i.hom)
    (V : SmallEtale B S hS Z.1) (hsurj : IsSurjective B S hS V.1.hom)
    (hchart : IsFinite B S hS (chartBaseChangeProjection B S hS f' V).hom →
      HasEtaleLocalProperty B S hS
        ((SpacesEtale.toSpaces B S hS Z).obj ((comparisonFunctor B S hS Z).obj V)).1
        (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) →
      IsCoherent B S hS Z'.1 Z'.2 (SheafOfModules.unit (structureRingSheaf B S hS Z')) →
      ((chartLocalizedModulePushforward B S hS f' V).obj
        ((moduleChartBaseChangeRestriction B S hS f' V).obj
          (SheafOfModules.unit (structureRingSheaf B S hS Z')))).IsCoherentOnSite) :
    IsCoherent B S hS Z.1 Z.2 ((modulePushforward B S hS f').obj
      (SheafOfModules.unit (structureRingSheaf B S hS Z')))
```

**`AlgebraicGeometry.Space.supportOfSheaf_modulePushforward_structureSheaf_preimage_eq_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePreimageStructureSheaf.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePreimageStructureSheaf.lean#L280). The attribute's comment: “the support of the direct image is all of Z”.

> **The support assertion of Stacks 0GF7.**  Let `f : Y ⟶ X` be a surjective morphism of
> algebraic spaces over `S`, let `i : Z ⟶ X` be any morphism and let `f' : Z' ⟶ Z` be the base
> change of `f` along `i`.  Then the support of `𝒢 = f'_*𝒪_{Z'}` is all of `Z`.
>
> Surjectivity is stable under base change by Stacks 03MH, so this is
> `AlgebraicGeometry.Space.supportOfSheaf_modulePushforward_structureSheaf_eq_univ`.  Neither the
> finiteness of `f`, nor the local Noetherianity of `X`, nor the closedness of the immersion `i`
> is used.

```lean
theorem supportOfSheaf_modulePushforward_structureSheaf_preimage_eq_univ (f : Y ⟶ X) (i : Z ⟶ X)
    {i' : Z' ⟶ Y} {f' : Z' ⟶ Z} (sq : IsPullback i' f' f i)
    (hf : IsSurjective B S hS f.hom) :
    supportOfSheaf B S hS Z.1 ((SheafOfModules.toSheaf _).obj
        ((modulePushforward B S hS f').obj
          (SheafOfModules.unit (structureRingSheaf B S hS Z')))) = Set.univ
```

**`AlgebraicGeometry.Space.isCoherent_modulePushforward_structureSheaf_preimage_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePreimageStructureSheafCoherent.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePreimageStructureSheafCoherent.lean#L53). The attribute's comment: “coherence of the direct image”.

> **The coherence assertion of Stacks 0GF7.**  Let `f : Y ⟶ X` be a finite morphism of
> algebraic spaces over `S` with `X` locally Noetherian, let `i : Z ⟶ X` be a closed immersion,
> and let `f' : Z' ⟶ Z` be the base change of `f` along `i`.  Then `𝒢 = f'_*𝒪_{Z'}` is a
> coherent `𝒪_Z`-module.
>
> `Z` is locally Noetherian by Stacks 06ED and 04ZK, `f'` is finite by Stacks 03ZS, `Z'` is
> locally Noetherian for the same reason as `Z`, and `𝒪_{Z'}` is then coherent by Stacks 07UB; so
> this is Stacks 07UH,
> `AlgebraicGeometry.Space.isCoherent_modulePushforward_of_isFinite'`.
> Surjectivity of `f` is not used.

```lean
theorem isCoherent_modulePushforward_structureSheaf_preimage_of_isLocallyNoetherian (f : Y ⟶ X)
    (i : Z ⟶ X) {i' : Z' ⟶ Y} {f' : Z' ⟶ Z} (sq : IsPullback i' f' f i)
    (hf : IsFinite B S hS f.hom)
    (hX : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} ↦ IsLocallyNoetherian T))
    (hi : IsClosedImmersion B S hS i.hom) :
    IsCoherent B S hS Z.1 Z.2 ((modulePushforward B S hS f').obj
      (SheafOfModules.unit (structureRingSheaf B S hS Z')))
```

## Tag 0GF8, a lemma

[Tag 0GF8](https://stacks.math.columbia.edu/tag/0GF8) in the Stacks Project.

**`AlgebraicGeometry.Space.idealSmul_pushforward_eq_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IdealPushforwardAffineComparison.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IdealPushforwardAffineComparison.lean#L255).

> **Stacks 0GF8.**  Let `S` be a scheme, let `f : Y ⟶ X` be a morphism of algebraic spaces
> over `S`, let `F` be a quasi-coherent sheaf on `Y` and let `I` be a quasi-coherent sheaf of
> ideals on `X`.  If `f` is affine then
>
> `I · f_*F = f_*((f⁻¹I) · F)`
>
> as subsheaves of `f_*F`.
>
> This is `AlgebraicGeometry.Space.idealSmul_pushforward_eq` with quasi-coherence, rather than
> the equivalent cartesian condition on affine charts, as the hypothesis of the source.

```lean
theorem idealSmul_pushforward_eq_of_isQuasicoherentOnSite
    (hI : I.toSheafOfModules.IsQuasicoherentOnSite) (hF : F.IsQuasicoherentOnSite) :
    Stacks.Sites.idealSmul (O := structureSheaf B S hS X.1 X.2)
        I (⊤ : ((smallBaseChangeModulePushforward B S hS f
          (relativelyRepresentable_hom_of_isAffineHom B S hS f haff)).obj F).Submodule) =
      pushforwardSubmodule B S hS f
        (relativelyRepresentable_hom_of_isAffineHom B S hS f haff) F
        (Stacks.Sites.idealSmul (O := structureSheaf B S hS Y.1 Y.2)
          (pullbackIdealSubsheaf B S hS f
            (relativelyRepresentable_hom_of_isAffineHom B S hS f haff) I) (⊤ : F.Submodule))
```

## Tag 07VP, a lemma

[Tag 07VP](https://stacks.math.columbia.edu/tag/07VP) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isAffineSpace_of_isFinite_of_isSurjective`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteSurjectiveAffineSource.lean#L722), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/AffinenessCriteria.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffinenessCriteria.lean#L55) (StacksFrontier).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.17, Tag 07VN](https://stacks.math.columbia.edu/tag/07VN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
