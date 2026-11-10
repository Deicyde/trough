---
declaration: section
origin: cited
lean: Stacks.RetrocompactOneDimensional.isZero_rightDerived_pushforward_of_isRetrocompact, AlgebraicGeometry.isAffineOpen_of_isCompact_of_krullDimLE_one, Stacks.RetrocompactOneDimensional.isAffineOpen_of_isCompact, Stacks.PicSurjectiveOpen.exists_isInvertible_modulePullback_iso_of_isRetrocompact, AlgebraicGeometry.exists_isInvertible_nonvanishingOpen_eq, AlgebraicGeometry.exists_isInvertible_generatingSections_nonvanishingOpen_eq, AlgebraicGeometry.Scheme.Modules.exists_isAmple_of_globallyGenerated_affine_nonvanishing, AlgebraicGeometry.Scheme.Modules.exists_isAmple_of_topologicalKrullDim_one
statement: formalized
proof: formalized
---

# 33.38 One dimensional Noetherian schemes

Section 33.38 of the Stacks Project, [Tag 09N7](https://stacks.math.columbia.edu/tag/09N7). 14 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09N8, a lemma

[Tag 09N8](https://stacks.math.columbia.edu/tag/09N8) in the Stacks Project.

**`Stacks.RetrocompactOneDimensional.isZero_rightDerived_pushforward_of_isRetrocompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RetrocompactOneDimensional/Basic.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RetrocompactOneDimensional/Basic.lean#L32).

> The positive higher direct images of a quasi-coherent module along the inclusion of a
> retrocompact open subscheme of a scheme whose local rings are Noetherian of dimension at most one
> vanish.

```lean
theorem isZero_rightDerived_pushforward_of_isRetrocompact
    (X : Scheme.{u}) (U : X.Opens)
    (hU : IsRetrocompact (U : Set X))
    (h_noetherian : ∀ x : X, IsNoetherianRing (X.presheaf.stalk x))
    (h_dimension : ∀ x : X, Ring.KrullDimLE 1 (X.presheaf.stalk x))
    (F : U.toScheme.Modules) (hF : F.IsQuasicoherent)
    (p : ℕ) (hp : 0 < p) :
    IsZero (((Scheme.Modules.pushforward U.ι).rightDerived p).obj F)
```

## Tag 09N9, a lemma

[Tag 09N9](https://stacks.math.columbia.edu/tag/09N9) in the Stacks Project.

**`AlgebraicGeometry.isAffineOpen_of_isCompact_of_krullDimLE_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/OneDimensionalLocal/QuasiCompactOpen.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/OneDimensionalLocal/QuasiCompactOpen.lean#L245). References: EGA IV (21.12.9), “more general”.

> **[Stacks, Tag 09N9].** Let `X` be an affine scheme all of whose local rings are Noetherian of
> dimension at most one. Then every quasi-compact open `V ⊆ X` is affine.
>
> The sections of `𝒪_X` over `V` whose basic open is affine span `Γ(X, V)` by
> `span_eq_top_of_isCompact`, and they cover `V` by `iSup_basicOpen_isAffineOpen_eq`, so
> [Stacks, Tag 01QF] applies. The dimension hypothesis enters only through
> `AlgebraicGeometry.isAffineOpen_of_krullDimLE_one`, which makes every open of the spectrum of a
> local ring of `X` affine.

```lean
theorem isAffineOpen_of_isCompact_of_krullDimLE_one {X : Scheme.{u}} [IsAffine X]
    (hN : ∀ x : X, IsNoetherianRing (X.presheaf.stalk x))
    (hD : ∀ x : X, Ring.KrullDimLE 1 (X.presheaf.stalk x))
    (V : X.Opens) (hV : IsCompact (V : Set X)) : IsAffineOpen V
```

**`Stacks.RetrocompactOneDimensional.isAffineOpen_of_isCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RetrocompactOneDimensional/Affine.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RetrocompactOneDimensional/Affine.lean#L164).

> A quasi-compact open subset of an affine scheme is affine when every local ring is Noetherian
> and has Krull dimension at most one.

```lean
theorem isAffineOpen_of_isCompact (X : Scheme.{u}) [IsAffine X]
    (h_noetherian : ∀ x : X, IsNoetherianRing (X.presheaf.stalk x))
    (h_dim : ∀ x : X, Ring.KrullDimLE 1 (X.presheaf.stalk x))
    (U : X.Opens) (hU : IsCompact (U : Set X)) : IsAffineOpen U
```

## Tag 09NA, a lemma

[Tag 09NA](https://stacks.math.columbia.edu/tag/09NA) in the Stacks Project.

**`Stacks.PicSurjectiveOpen.exists_isInvertible_modulePullback_iso_of_isRetrocompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicSurjectiveOpen/Retrocompact.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PicSurjectiveOpen/Retrocompact.lean#L82). The attribute's comment: “surjectivity of the restriction Pic(X) -> Pic(U)”.

> **Clause (2) of Stacks Tag 09NA.** For a retrocompact open `U` of a scheme `X` whose
> complement is discrete and along which the local rings of `X` are Noetherian of Krull dimension
> at most one, every invertible `𝒪_U`-module is the pullback of an invertible `𝒪_X`-module; that
> is, `Pic(X) → Pic(U)` is surjective.

```lean
theorem exists_isInvertible_modulePullback_iso_of_isRetrocompact
    (hU : IsRetrocompact (U : Set X)) [DiscreteTopology (Uᶜ : Set X)]
    (h_noetherian : ∀ x : X, x ∈ (U : Set X)ᶜ → IsNoetherianRing (X.presheaf.stalk x))
    (h_dimension : ∀ x : X, x ∈ (U : Set X)ᶜ → Ring.KrullDimLE 1 (X.presheaf.stalk x))
    (N : U.toScheme.Modules)
    [IsInvertible U.toScheme.presheaf
      (structureSheafRing U.toScheme.toRingedSpace).property N] :
    ∃ (L : X.Modules)
      (_ : IsInvertible X.presheaf (structureSheafRing X.toRingedSpace).property L),
      Nonempty ((modulePullback U.ι.toLRSHom.toShHom).obj L ≅ N)
```

**`AlgebraicGeometry.exists_isInvertible_nonvanishingOpen_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NoetherianDimensionOne/NonvanishingLocus.lean, line 865](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/NoetherianDimensionOne/NonvanishingLocus.lean#L865). The attribute's comment: “nonvanishing\_locus”.

> **Stacks Project, Tag 09NA.** A retrocompact open with discrete complement along which the
> local rings are Noetherian of Krull dimension at most one is the nonvanishing open of a global
> section of an invertible module.

```lean
theorem exists_isInvertible_nonvanishingOpen_eq
    (X : Scheme.{u}) (U : X.Opens)
    (hU : IsRetrocompact (U : Set X))
    [DiscreteTopology (Uᶜ : Set X)]
    (h_noetherian : ∀ x : X, x ∈ (U : Set X)ᶜ →
      IsNoetherianRing (X.presheaf.stalk x))
    (h_dimension : ∀ x : X, x ∈ (U : Set X)ᶜ →
      Ring.KrullDimLE 1 (X.presheaf.stalk x)) :
    ∃ (L : X.Modules)
      (hL : Stacks.SheafOfModules.IsInvertible X.toRingedSpace.presheaf
        (structureSheafRing X.toRingedSpace).property
          L)
      (s : L.sections),
      U = (letI := hL
           Stacks.SheafOfModules.nonvanishingOpen (X := X.toRingedSpace) L s)
```

## Tag 09NB, a lemma

[Tag 09NB](https://stacks.math.columbia.edu/tag/09NB) in the Stacks Project.

**`AlgebraicGeometry.exists_isInvertible_generatingSections_nonvanishingOpen_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/NoetherianDimensionOne/GloballyGenerated.lean, line 1311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/NoetherianDimensionOne/GloballyGenerated.lean#L1311).

> **Stacks Project, Tag 09NB.** On an integral separated scheme, a nonempty affine open with
> finite complement along which the local rings are Noetherian of dimension one is the
> nonvanishing open of a global section of a globally generated invertible module.

```lean
theorem exists_isInvertible_generatingSections_nonvanishingOpen_eq
    (X : Scheme.{u}) [IsIntegral X] [X.IsSeparated]
    (U : X.Opens) (hU : IsAffineOpen U) (hU_nonempty : U ≠ ⊥)
    (hfinite : ((U : Set X)ᶜ).Finite)
    (hnoetherian : ∀ x : X, x ∉ U → IsNoetherianRing (X.presheaf.stalk x))
    (hdim : ∀ x : X, x ∉ U → ringKrullDim (X.presheaf.stalk x) = 1) :
    ∃ (L : X.Modules)
      (hL : Stacks.SheafOfModules.IsInvertible X.toRingedSpace.presheaf
        (structureSheafRing X.toRingedSpace).property
          L)
      (s : L.sections),
      Nonempty L.GeneratingSections ∧
        U = (letI := hL
             Stacks.SheafOfModules.nonvanishingOpen (X := X.toRingedSpace) L s)
```

## Tag 09NC, a lemma

[Tag 09NC](https://stacks.math.columbia.edu/tag/09NC) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.exists_isAmple_of_globallyGenerated_affine_nonvanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleFromAffineNonvanishing/Basic.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleFromAffineNonvanishing/Basic.lean#L410).

> **Stacks Project, Tag 09NC.** A quasi-compact scheme every point of which lies in an affine
> nonvanishing locus of a global section of some globally generated invertible sheaf carries an
> ample invertible sheaf.
>
> The proof is the Stacks Project's. Quasi-compactness gives finitely many pairs `(L i, t i)` with
> `X = ⋃ X_{t i}` and each `X_{t i}` affine; put `B = L 0 ⊗ ⋯ ⊗ L n`. For a point `x`, pick an
> index `j` with `x ∈ X_{t j}` and take `σ = s 0 ⊗ ⋯ ⊗ s n` where `s j = t j` and, for `i ≠ j`,
> `s i` is a member of the generating family of `L i` not vanishing at `x`
> (`Stacks.SheafOfModules.exists_generatingSection_nonvanishing`). Then `X_σ = ⋂ X_{s i}` contains
> `x` and is contained in `X_{t j}`, so Tag 01PV applied `n + 1` times makes it affine. Ampleness
> is read at exponent `1` through `Stacks.SheafOfModules.Invertible.tensorPowerOneIso`.
>
> **Two invertibility predicates.** The hypothesis is spelled with
> `Stacks.SheafOfModules.IsInvertible`, which is the one `Stacks.SheafOfModules.nonvanishingOpen`
> is defined for, and the conclusion with `AlgebraicGeometry.SheafOfModules.IsInvertible`, which is
> the one `AlgebraicGeometry.Scheme.Modules.IsAmple` is defined for. Both are `Prop`s, so the
> choice of witness does not affect what either statement says, and
> `Stacks.SheafOfModules.isInvertible_iff_algebraicGeometry` crosses between them.

```lean
public theorem exists_isAmple_of_globallyGenerated_affine_nonvanishing (Y : Scheme.{u})
    (hcpt : CompactSpace Y)
    (hcover : ∀ y : Y, ∃ (M : Y.Modules)
      (hM : Stacks.SheafOfModules.IsInvertible Y.toRingedSpace.sheaf.obj
        (structureSheaf Y.toRingedSpace.sheaf).property M),
      Nonempty M.GeneratingSections ∧
        ∃ t : M.sections,
          y ∈ @Stacks.SheafOfModules.nonvanishingOpen
              Y.toLocallyRingedSpace.toRingedSpace _ M hM t ∧
            IsAffineOpen (@Stacks.SheafOfModules.nonvanishingOpen
              Y.toLocallyRingedSpace.toRingedSpace _ M hM t)) :
    ∃ (M : Y.Modules)
      (hM : AlgebraicGeometry.SheafOfModules.IsInvertible Y.toRingedSpace.presheaf
        (structureSheafRing Y.toRingedSpace).property M),
      @AlgebraicGeometry.Scheme.Modules.IsAmple Y M hM
```

## Tag 09ND, a lemma

[Tag 09ND](https://stacks.math.columbia.edu/tag/09ND) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.exists_isAmple_of_topologicalKrullDim_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleFromAffineNonvanishing/Basic.lean, line 520](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleFromAffineNonvanishing/Basic.lean#L520).

> **Stacks Project, Tag 09ND.** A Noetherian integral separated scheme of topological Krull
> dimension one has an ample invertible sheaf.
>
> It is `Stacks.AlgebraicGeometry.AmpleDimensionOne.exists_ample_invertible_of_09NC` applied to
> `exists_isAmple_of_globallyGenerated_affine_nonvanishing`.

```lean
public theorem exists_isAmple_of_topologicalKrullDim_one (X : Scheme.{u})
    [IsNoetherian X] [IsIntegral X] [X.IsSeparated]
    (hdim : topologicalKrullDim X = 1) :
    ∃ (L : X.Modules)
      (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.toRingedSpace.presheaf
        (structureSheafRing X.toRingedSpace).property L),
      @AlgebraicGeometry.Scheme.Modules.IsAmple X L hL
```

## Tag 0C0T, a lemma

[Tag 0C0T](https://stacks.math.columbia.edu/tag/0C0T) in the Stacks Project.

**`Stacks.PicFinite.exists_isInvertible_modulePullback_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicSurjectiveFinite/Basic.lean, line 1038](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PicSurjectiveFinite/Basic.lean#L1038).

> **An invertible module descends along a finite morphism that is an isomorphism away
> from a discrete closed subset.**

```lean
theorem exists_isInvertible_modulePullback_iso
    {X Y : AlgebraicGeometry.Scheme.{u}} (f : X ⟶ Y) [AlgebraicGeometry.IsFinite f]
    (V : Y.Opens) [IsIso (f ∣_ V)] [DiscreteTopology (Vᶜ : Set Y)]
    (L : X.Modules)
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf
      ((Presheaf.isSheaf_iff_isSheaf_comp _ X.presheaf
        (forget₂ CommRingCat RingCat)).mp X.IsSheaf) L) :
    ∃ M : Y.Modules,
      AlgebraicGeometry.SheafOfModules.IsInvertible Y.presheaf
          ((Presheaf.isSheaf_iff_isSheaf_comp _ Y.presheaf
            (forget₂ CommRingCat RingCat)).mp Y.IsSheaf) M ∧
        Nonempty ((AlgebraicGeometry.Scheme.Modules.pullback f).obj M ≅ L)
```

## Tag 09NE, a lemma

[Tag 09NE](https://stacks.math.columbia.edu/tag/09NE) in the Stacks Project.

**`StacksTag09NE.exists_invertible_of_closed_cover_discrete_intersections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedCoverGlue/Basic.lean, line 837](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ClosedCoverGlue/Basic.lean#L837). The attribute's comment: “existence of an invertible sheaf”.

> Invertible sheaves on a finite closed cover of a reduced scheme extend when
> pairwise intersections are discrete.

```lean
public theorem exists_invertible_of_closed_cover_discrete_intersections
    {ι : Type v} [Finite ι] (X : Scheme.{u}) [IsReduced X]
    (Z : ι → Scheme.{u}) (f : ∀ i, Z i ⟶ X)
    [∀ i, IsClosedImmersion (f i)]
    (hcover : ∀ x : X, ∃ i z, f i z = x)
    (hdiscrete : ∀ i j, i ≠ j → DiscreteTopology
      (↥(Set.range (f i) ∩ Set.range (f j) : Set X)))
    (L : ∀ i, (Z i).Modules)
    [∀ i, AlgebraicGeometry.SheafOfModules.IsInvertible (Z i).presheaf (Z i).ringCatSheaf.2 (L i)] :
    ∃ (M : X.Modules)
      (_ : AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 M),
      ∀ i, Nonempty ((modulePullback (f i).toLRSHom.toShHom).obj M ≅ L i)
```

**`StacksTag09NE.exists_invertible_with_sections_of_closed_cover_discrete_intersections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedCoverGlue/Sections.lean, line 782](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ClosedCoverGlue/Sections.lean#L782). The attribute's comment: “existence with prescribed sections”.

> Sections nonvanishing along the pairwise intersections can be glued along
> with the invertible sheaves.

```lean
public theorem exists_invertible_with_sections_of_closed_cover_discrete_intersections
    {ι : Type v} [Finite ι] (X : Scheme.{u}) [IsReduced X]
    (Z : ι → Scheme.{u}) (f : ∀ i, Z i ⟶ X)
    [∀ i, IsClosedImmersion (f i)]
    (hcover : ∀ x : X, ∃ i z, f i z = x)
    (hdiscrete : ∀ i j, i ≠ j → DiscreteTopology
      (↥(Set.range (f i) ∩ Set.range (f j) : Set X)))
    (L : ∀ i, (Z i).Modules)
    [∀ i, AlgebraicGeometry.SheafOfModules.IsInvertible (Z i).presheaf (Z i).ringCatSheaf.2 (L i)]
    (s : ∀ i, (L i).sections)
    (hs : ∀ i j, i ≠ j → ∀ z : Z i,
      (f i) z ∈ Set.range (f j) →
        z ∈ Stacks.SheafOfModules.nonvanishingLocus (X := (Z i).toRingedSpace) (L i) (s i)) :
    ∃ (M : X.Modules)
      (_ : AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 M)
      (t : M.sections),
      ∀ i, ∃ e : (modulePullback (f i).toLRSHom.toShHom).obj M ≅ L i,
        e.hom.val.app (op ⊤)
          (((modulePullbackPushforwardAdjunction (f i).toLRSHom.toShHom).unit.app M).val.app
            (op ⊤) (t.eval (op ⊤))) = (s i).eval (op ⊤)
```

**`AlgebraicGeometry.exists_invertible_of_closed_cover_discrete_intersections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InvertibleOnClosedCover/Basic.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/InvertibleOnClosedCover/Basic.lean#L542). The attribute's comment: “existence of an invertible sheaf”.

> Invertible sheaves on a finite closed cover of a reduced scheme extend when
> pairwise intersections are discrete.

```lean
public theorem exists_invertible_of_closed_cover_discrete_intersections
    {ι : Type v} [Finite ι] (X : Scheme.{u}) [IsReduced X]
    (Z : ι → Scheme.{u}) (f : ∀ i, Z i ⟶ X)
    [∀ i, IsClosedImmersion (f i)]
    (hcover : ∀ x : X, ∃ i z, f i z = x)
    (hdiscrete : ∀ i j, i ≠ j → DiscreteTopology
      (↥(Set.range (f i) ∩ Set.range (f j) : Set X)))
    (L : ∀ i, (Z i).Modules)
    [∀ i, IsInvertible (Z i).presheaf (Z i).ringCatSheaf.2 (L i)] :
    ∃ (M : X.Modules)
      (_ : IsInvertible X.presheaf X.ringCatSheaf.2 M),
      ∀ i, Nonempty ((modulePullback (f i).toLRSHom.toShHom).obj M ≅ L i)
```

**`AlgebraicGeometry.exists_invertible_with_sections_of_closed_cover_discrete_intersections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InvertibleOnClosedCover/Basic.lean, line 982](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/InvertibleOnClosedCover/Basic.lean#L982). The attribute's comment: “existence with prescribed sections”.

> Sections nonvanishing along the pairwise intersections can be glued along
> with the invertible sheaves.

```lean
public theorem exists_invertible_with_sections_of_closed_cover_discrete_intersections
    {ι : Type v} [Finite ι] (X : Scheme.{u}) [IsReduced X]
    (Z : ι → Scheme.{u}) (f : ∀ i, Z i ⟶ X)
    [∀ i, IsClosedImmersion (f i)]
    (hcover : ∀ x : X, ∃ i z, f i z = x)
    (_hdiscrete : ∀ i j, i ≠ j → DiscreteTopology
      (↥(Set.range (f i) ∩ Set.range (f j) : Set X)))
    (L : ∀ i, (Z i).Modules)
    [∀ i, IsInvertible (Z i).presheaf (Z i).ringCatSheaf.2 (L i)]
    (s : ∀ i, (L i).sections)
    (hs : ∀ i j, i ≠ j → ∀ z : Z i,
      (f i) z ∈ Set.range (f j) →
        z ∈ Stacks.NonvanishingTrivialize.nonvanishingLocus (Z i).toRingedSpace (L i) (s i)) :
    ∃ (M : X.Modules)
      (_ : IsInvertible X.presheaf X.ringCatSheaf.2 M)
      (t : M.sections),
      ∀ i, ∃ e : (modulePullback (f i).toLRSHom.toShHom).obj M ≅ L i,
        e.hom.val.app (op ⊤)
          (((modulePullbackPushforwardAdjunction (f i).toLRSHom.toShHom).unit.app M).val.app
            (op ⊤) (t.eval (op ⊤))) = (s i).eval (op ⊤)
```

## Tag 09NW, a remark

[Tag 09NW](https://stacks.math.columbia.edu/tag/09NW) in the Stacks Project.

**`Ideal.inf_eq_bot_of_zeroLocus_union_eq_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/Conductor.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/Conductor.lean#L56).

> In a reduced ring, ideals whose zero loci cover the spectrum have zero
> intersection.

```lean
public theorem inf_eq_bot_of_zeroLocus_union_eq_univ
    {A : Type u} [CommRing A] [IsReduced A] (I J : Ideal A)
    (h : PrimeSpectrum.zeroLocus (I : Set A) ∪
      PrimeSpectrum.zeroLocus (J : Set A) = Set.univ) :
    I ⊓ J = ⊥
```

**`Ideal.idealMap_quotient_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/Conductor.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/Conductor.lean#L68).

> If `V(I) ∪ V(J) = Spec A` in a reduced ring, the canonical map from `I`
> to its extension in `A ⧸ J` is an isomorphism of `A`-modules.

```lean
public theorem idealMap_quotient_bijective
    {A : Type u} [CommRing A] [IsReduced A] (I J : Ideal A)
    (h : PrimeSpectrum.zeroLocus (I : Set A) ∪
      PrimeSpectrum.zeroLocus (J : Set A) = Set.univ) :
    Function.Bijective (Algebra.idealMap (A ⧸ J) I)
```

**`Ideal.multipleQuotientMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/Conductor.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DimensionOne/Conductor.lean#L88).

> If `V(I) ∪ V(J) = Spec A`, the quotient map induces an isomorphism
> `I • P ≅ I • (P ⧸ J • P)` for every flat `A`-module `P`. In particular this applies when
> `P` is projective.

```lean
public theorem multipleQuotientMap_bijective
    {A : Type u} [CommRing A] [IsReduced A] (I J : Ideal A)
    {P : Type v} [AddCommGroup P] [Module A P] [Module.Flat A P]
    (h : PrimeSpectrum.zeroLocus (I : Set A) ∪
      PrimeSpectrum.zeroLocus (J : Set A) = Set.univ) :
    Function.Bijective (multipleQuotientMap (P := P) I J)
```

## Tag 09NX, a lemma

[Tag 09NX](https://stacks.math.columbia.edu/tag/09NX) in the Stacks Project.

**`Stacks.AmpleReducedDimensionOne.exists_isAmple_of_isReduced_of_topologicalKrullDim_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleReducedDimensionOne/Extension.lean, line 502](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleReducedDimensionOne/Extension.lean#L502).

> **[Stacks, Tag 09NX].**  A Noetherian, reduced, separated scheme of topological Krull
> dimension at most one carries an ample invertible sheaf.
>
> The sheaf is the `M` glued from the components by Tag 09NE: its distinguished global section `t`
> serves every point of the overlap `T`, at exponent one, and
> `Stacks.AmpleReducedDimensionOne.exists_sections_of_notMem_componentOverlap` serves every point
> off `T`.
>
> The hypothesis is `≤ 1` rather than `= 1`, so this applies to schemes of dimension zero as well
> and is stronger than the source's statement.
>
> The name carries `isReduced` because
> `StacksTag09NX.exists_isAmple_of_topologicalKrullDim_le_one` already exists and is a *different*
> theorem — Tag 09ND for an **integral** scheme, which is the first step of this proof rather than
> its conclusion. Two declarations with that name-tail, one of them in a namespace called
> `StacksTag09NX`, would be a twin-constant hazard, so the hypothesis
> that distinguishes them is in the name.

```lean
theorem exists_isAmple_of_isReduced_of_topologicalKrullDim_le_one (Y : Scheme.{u})
    [AlgebraicGeometry.IsNoetherian Y] [AlgebraicGeometry.IsReduced Y] [Y.IsSeparated]
    (hdim : topologicalKrullDim (Y : Type u) ≤ 1) :
    ∃ (M : Y.Modules)
      (_ : AlgebraicGeometry.SheafOfModules.IsInvertible Y.presheaf Y.ringCatSheaf.2 M),
      AlgebraicGeometry.Scheme.Modules.IsAmple Y M
```

## Tag 09NY, a lemma

[Tag 09NY](https://stacks.math.columbia.edu/tag/09NY) in the Stacks Project.

**`Stacks.LiftInvertible.exists_modulePullback_iso_of_isClosedImmersion_of_dimension_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LiftInvertible/ClosedUnionGlue.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LiftInvertible/ClosedUnionGlue.lean#L213).

> An invertible module on a closed subscheme of a scheme whose underlying space is Noetherian
> and has dimension at most one is the pullback of an invertible module on the ambient scheme.

```lean
theorem exists_modulePullback_iso_of_isClosedImmersion_of_dimension_le_one
    (X Z : Scheme.{u}) (i : Z ⟶ X) [IsClosedImmersion i]
    [NoetherianSpace X] (hdim : topologicalKrullDim X ≤ 1)
    (L : SheafOfModules.{u} (structureSheafRing Z.toRingedSpace))
    [AlgebraicGeometry.SheafOfModules.IsInvertible Z.presheaf
      (Presheaf.isSheaf_comp_of_isSheaf _ _ (forget₂ CommRingCat RingCat) Z.IsSheaf) L] :
    ∃ (M : SheafOfModules.{u} (structureSheafRing X.toRingedSpace))
      (_ : AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf
        (Presheaf.isSheaf_comp_of_isSheaf _ _ (forget₂ CommRingCat RingCat) X.IsSheaf) M),
      Nonempty ((modulePullback i.toLRSHom.toShHom).obj M ≅ L)
```

## Tag 09NZ, a proposition

[Tag 09NZ](https://stacks.math.columbia.edu/tag/09NZ) in the Stacks Project.

**`Stacks.AmpleNoetherianDimensionOne.exists_isAmple_of_isNoetherian_of_topologicalKrullDim_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleNoetherianDimensionOne/Basic.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleNoetherianDimensionOne/Basic.lean#L117). The attribute's comment: “with dimension at most one in place of the source's dimension one”.

> **[Stacks, Tag 09NZ].** A Noetherian separated scheme of topological Krull dimension at most
> one carries an ample invertible module.
>
> The reduction `Z` of `X` is Noetherian, reduced, separated and of dimension at most one, so it has
> an ample invertible module by [Stacks, Tag 09NX]; that module is `i^* L` for an invertible module
> `L` on `X` by [Stacks, Tag 09NY]; and `L` is ample because `i^* L` is, by the converse half of
> [Stacks, Tag 09MS] applied to the surjective closed immersion `i : Z ⟶ X`.

```lean
theorem exists_isAmple_of_isNoetherian_of_topologicalKrullDim_le_one
    (X : Scheme.{u}) [AlgebraicGeometry.IsNoetherian X] [X.IsSeparated]
    (hdim : topologicalKrullDim (X : Type u) ≤ 1) :
    ∃ (L : X.Modules)
      (_ : AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L),
      AlgebraicGeometry.Scheme.Modules.IsAmple X L
```

## Tag 09P0, a remark

[Tag 09P0](https://stacks.math.columbia.edu/tag/09P0) in the Stacks Project.

**`Stacks.AmpleNoetherianReduction.exists_isAmple_of_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleNoetherianReduction/Basic.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleNoetherianReduction/Basic.lean#L234). The attribute's comment: “granted the converse half of Tag 09MW as `AmpleDescendsAlongThickening`”.

> **[Stacks, Tag 09P0].** A scheme whose reduction is a Noetherian separated scheme of
> dimension at most one has an ample invertible sheaf, granted the converse half of
> [Stacks, Tag 09MW].
>
> The hypotheses are on the reduction only; `X` itself is not assumed Noetherian, which is exactly
> what distinguishes this from [Stacks, Tag 09NZ] and what forces Tag 09MW in place of
> [Stacks, Tag 09MS].

```lean
theorem exists_isAmple_of_reduction (X : Scheme.{u})
    (hdesc : AmpleDescendsAlongThickening.{u})
    [IsNoetherian (vanishingIdeal (⊤ : Closeds X)).subscheme]
    [(vanishingIdeal (⊤ : Closeds X)).subscheme.IsSeparated]
    (hdim : topologicalKrullDim ((vanishingIdeal (⊤ : Closeds X)).subscheme : Type u) ≤ 1) :
    ∃ (L : X.Modules) (hL : IsInvertibleModule X L), @IsAmple X L hL
```

**`Stacks.AmpleNoetherianReduction.exists_isAmple_of_reduction_of_topologicalKrullDim_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleNoetherianReduction/Unconditional.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleNoetherianReduction/Unconditional.lean#L68).

> **[Stacks, Tag 09P0].** A scheme whose reduction is a Noetherian separated scheme of
> dimension at most one has an ample invertible sheaf.
>
> The hypotheses are on the reduction `X_red = (vanishingIdeal ⊤).subscheme` only; `X` itself is
> not assumed Noetherian.

```lean
theorem exists_isAmple_of_reduction_of_topologicalKrullDim_le_one (X : Scheme.{u})
    [IsNoetherian (vanishingIdeal (⊤ : Closeds X)).subscheme]
    [(vanishingIdeal (⊤ : Closeds X)).subscheme.IsSeparated]
    (hdim : topologicalKrullDim ((vanishingIdeal (⊤ : Closeds X)).subscheme : Type u) ≤ 1) :
    ∃ (L : X.Modules) (hL : IsInvertibleModule X L), @IsAmple X L hL
```

## Tag 0C0U, a lemma

[Tag 0C0U](https://stacks.math.columbia.edu/tag/0C0U) in the Stacks Project.

**`Stacks.PicFinite.exists_isInvertible_modulePullback_iso_of_isClosedImmersion_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicSurjectiveFinite/DenseClosedImmersion.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PicSurjectiveFinite/DenseClosedImmersion.lean#L105).

> **Stacks Project, Tag 0C0U.** Let `f : X ⟶ Y` be a finite morphism of schemes with `Y` of
> Noetherian underlying space and dimension at most one, and suppose `f` is a closed immersion
> over a dense open subset `V` of `Y`. Then every invertible `𝒪_X`-module is the pullback of an
> invertible `𝒪_Y`-module.
>
> The morphism factors as `f.toImage ≫ f.imageι` through its scheme-theoretic image `Z`. Over
> `U := f.imageι ⁻¹ᵁ V` the first factor is a closed immersion with trivial kernel ideal sheaf,
> hence an isomorphism, and the part of `Z` outside `U` is discrete, so Tag 0C0T descends the
> module to `Z`; Tag 09NY then lifts it across the closed immersion `f.imageι` to `Y`.

```lean
theorem exists_isInvertible_modulePullback_iso_of_isClosedImmersion_restrict
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsFinite f] [NoetherianSpace Y]
    (hdim : topologicalKrullDim Y ≤ 1) (V : Y.Opens) (hV : Dense (V : Set Y))
    [IsClosedImmersion (f ∣_ V)]
    (L : X.Modules)
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf
      ((Presheaf.isSheaf_iff_isSheaf_comp _ X.presheaf
        (forget₂ CommRingCat RingCat)).mp X.IsSheaf) L) :
    ∃ M : Y.Modules,
      AlgebraicGeometry.SheafOfModules.IsInvertible Y.presheaf
          ((Presheaf.isSheaf_iff_isSheaf_comp _ Y.presheaf
            (forget₂ CommRingCat RingCat)).mp Y.IsSheaf) M ∧
        Nonempty ((AlgebraicGeometry.Scheme.Modules.pullback f).obj M ≅ L)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.38, Tag 09N7](https://stacks.math.columbia.edu/tag/09N7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
