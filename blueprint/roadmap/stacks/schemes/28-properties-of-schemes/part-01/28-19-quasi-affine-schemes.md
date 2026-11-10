---
declaration: section
origin: cited
lean: AlgebraicGeometry.isIso_pullback_fromTildeΓ, AlgebraicGeometry.isIso_toSpecΓ_restrict_basicOpen, AlgebraicGeometry.Scheme.isQuasiAffine_iff_quasiCompact_and_isOpenImmersion_toSpecΓ, AlgebraicGeometry.isPullback_id_toSpecΓ_of_isOpenImmersion, AlgebraicGeometry.exists_affine_pullback_iso_affineSpace, AlgebraicGeometry.exists_contains_affine_pullback_iso_affineSpace
statement: formalized
proof: formalized
---

# 28.19 Quasi-affine schemes

Section 28.19 of the Stacks Project, [Tag 01P5](https://stacks.math.columbia.edu/tag/01P5). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EHM, a lemma

[Tag 0EHM](https://stacks.math.columbia.edu/tag/0EHM) in the Stacks Project.

**`AlgebraicGeometry.isIso_pullback_fromTildeΓ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/PrincipalOpens/QuasiCompactOpen.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/PrincipalOpens/QuasiCompactOpen.lean#L47).

> For a quasi-coherent module `F` on a quasi-compact open `U` of an affine scheme, the
> canonical map to `F` from the restriction to `U` of the sheaf associated to the global sections
> of `F` is an isomorphism.

```lean
theorem isIso_pullback_fromTildeΓ
    (R : CommRingCat.{u}) (U : (Spec R).Opens)
    (hU : IsCompact (U : Set (Spec R)))
    (F : U.toScheme.Modules) [F.IsQuasicoherent] :
    IsIso ((Scheme.Modules.pullback U.ι).map
      (Scheme.Modules.fromTildeΓ ((Scheme.Modules.pushforward U.ι).obj F)) ≫
      (Scheme.Modules.pullbackPushforwardAdjunction U.ι).counit.app F)
```

## Tag 01P8, a lemma

[Tag 01P8](https://stacks.math.columbia.edu/tag/01P8) in the Stacks Project.

**`AlgebraicGeometry.isIso_toSpecΓ_restrict_basicOpen`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/QuasiAffine.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/QuasiAffine.lean#L86).

> **Stacks Project, Tag 01P8.** If `X` is quasi-compact and quasi-separated
> and its basic open defined by `f` is affine, then the canonical morphism to
> `Spec Γ(X, ᵊ_X)` restricts to an isomorphism from that basic open onto the
> standard open defined by `f`.

```lean
lemma isIso_toSpecΓ_restrict_basicOpen (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] (f : Γ(X, ⊤)) (hf : IsAffineOpen (X.basicOpen f)) :
    IsIso (X.toSpecΓ ∣_ PrimeSpectrum.basicOpen f)
```

## Tag 01P9, a lemma

[Tag 01P9](https://stacks.math.columbia.edu/tag/01P9) in the Stacks Project.

**`AlgebraicGeometry.Scheme.isQuasiAffine_iff_quasiCompact_and_isOpenImmersion_toSpecΓ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/QuasiAffineToSpecGamma.lean, line 31](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/QuasiAffineToSpecGamma.lean#L31).

> **Stacks 01P9.** A scheme `X` is quasi-affine if and only if the canonical morphism
> `X ⟶ Spec Γ(X, ⊤)` is a quasi-compact open immersion.

```lean
theorem isQuasiAffine_iff_quasiCompact_and_isOpenImmersion_toSpecΓ (X : Scheme.{u}) :
    X.IsQuasiAffine ↔ QuasiCompact X.toSpecΓ ∧ IsOpenImmersion X.toSpecΓ
```

## Tag 0ARY, a lemma

[Tag 0ARY](https://stacks.math.columbia.edu/tag/0ARY) in the Stacks Project.

**`AlgebraicGeometry.isPullback_id_toSpecΓ_of_isOpenImmersion`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/QuasiAffine.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/QuasiAffine.lean#L132).

> **Stacks Project, Tag 0ARY.** For an open immersion `U ⟶ V` between
> quasi-affine schemes, the canonical morphism from `U` to the spectrum of its
> global sections is the base change of the induced morphism on spectra along
> the canonical morphism from `V`.

```lean
lemma isPullback_id_toSpecΓ_of_isOpenImmersion (U V : Scheme.{u}) (f : U ⟶ V)
    [IsOpenImmersion f]
    [U.IsQuasiAffine] [V.IsQuasiAffine] :
    IsPullback (𝟙 U) U.toSpecΓ (f ≫ V.toSpecΓ) (Spec.map f.appTop)
```

## Tag 0F82, a lemma

[Tag 0F82](https://stacks.math.columbia.edu/tag/0F82) in the Stacks Project.

**`AlgebraicGeometry.exists_affine_pullback_iso_affineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/QuasiAffineAffineSpaceBundle.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/QuasiAffineAffineSpaceBundle.lean#L391).

> **Stacks Project, Tag 0F82.** A quasi-affine scheme `X` admits an integer `n`, an affine
> scheme `T` and a morphism `T ⟶ X` such that for every morphism `X' ⟶ X` with `X'` affine the
> fibre product `X' ×_X T` is isomorphic to affine `n`-space over `X'`, as a scheme over `X'`.

```lean
theorem exists_affine_pullback_iso_affineSpace (X : Scheme.{u}) [X.IsQuasiAffine] :
    ∃ (n : ℕ) (T : Scheme.{u}), IsAffine T ∧
      ∃ f : T ⟶ X, ∀ (X' : Scheme.{u}) (_ : IsAffine X') (g : X' ⟶ X),
        Nonempty (Over.mk (pullback.fst g f) ≅
          Over.mk (AffineSpace.over (ULift.{u} (Fin n)) X').hom)
```

**`AlgebraicGeometry.exists_contains_affine_pullback_iso_affineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineAffineSpaceBundleInSite.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineAffineSpaceBundleInSite.lean#L82). The attribute's comment: “the bundle chosen inside a big fppf site”.

> For a quasi-affine scheme `X` satisfying the size cutoff of a big fppf site `B`, the
> affine-space bundle of Stacks 0F82 over `X` can be chosen with its total space satisfying the
> cutoff too, and its structure morphism is locally of finite type.

```lean
theorem exists_contains_affine_pullback_iso_affineSpace (B : BigFppfSite.{u})
    (X : Scheme.{u}) [X.IsQuasiAffine] (hX : B.Contains X) :
    ∃ (n : ℕ) (T : Scheme.{u}), IsAffine T ∧ B.Contains T ∧
      ∃ f : T ⟶ X, LocallyOfFiniteType f ∧
        ∀ (X' : Scheme.{u}) (_ : IsAffine X') (g : X' ⟶ X),
          Nonempty (Over.mk (pullback.fst g f) ≅
            Over.mk (AffineSpace.over (ULift.{u} (Fin n)) X').hom)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.19, Tag 01P5](https://stacks.math.columbia.edu/tag/01P5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
