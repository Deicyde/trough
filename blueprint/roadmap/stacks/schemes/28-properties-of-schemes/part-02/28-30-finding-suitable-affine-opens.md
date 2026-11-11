---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_pairwise_disjoint_affine_opens_of_generic_points, AlgebraicGeometry.exists_affine_open_containing_generic_points, AlgebraicGeometry.exists_dense_open_isSeparated, AlgebraicGeometry.exists_affineOpen_mem_of_genericPoints_irreducibleComponents, Stacks.AmpleAffineAvoidance.exists_affineOpen_containing_finite_of_ample, Stacks.AmpleCluster.exists_affineOpen_containing_finite_of_immersion_proj, Stacks.AmpleCluster.exists_affineOpen_containing_finite_of_isQuasiAffine, Stacks.AmpleCluster.exists_affineOpen_containing_finite_of_immersion_affine
statement: formalized
proof: formalized
---

# 28.30 Finding suitable affine opens

Section 28.30 of the Stacks Project, [Tag 01ZU](https://stacks.math.columbia.edu/tag/01ZU). 8 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01ZV, a lemma

[Tag 01ZV](https://stacks.math.columbia.edu/tag/01ZV) in the Stacks Project.

**`AlgebraicGeometry.exists_pairwise_disjoint_affine_opens_of_generic_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/GenericPoints.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/GenericPoints.lean#L113). The attribute's comment: “pairwise disjoint neighborhoods”.

> **Stacks Project, Tag 01ZV.** A finite family of distinct irreducible components
> of a quasi-separated scheme has pairwise disjoint affine open neighborhoods of its
> generic points; the union of these neighborhoods is affine.

```lean
theorem exists_pairwise_disjoint_affine_opens_of_generic_points
    [QuasiSeparatedSpace X] (Z : ι → Set X)
    (hZ : ∀ i, Z i ∈ irreducibleComponents X) (hZ_injective : Injective Z)
    (η : ι → X) (hη : ∀ i, IsGenericPoint (η i) (Z i)) :
    ∃ U : ι → X.Opens,
      (∀ i, AlgebraicGeometry.IsAffineOpen (U i)) ∧
      (∀ i, η i ∈ U i) ∧
      Pairwise (Disjoint on U) ∧
      AlgebraicGeometry.IsAffineOpen (iSup U)
```

**`AlgebraicGeometry.exists_affine_open_containing_generic_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/GenericPoints.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/GenericPoints.lean#L164). The attribute's comment: “common affine neighborhood”.

> **Stacks Project, Tag 01ZV.** The generic points of a finite family of distinct
> irreducible components of a quasi-separated scheme lie in a single affine open.

```lean
theorem exists_affine_open_containing_generic_points
    [QuasiSeparatedSpace X] (Z : ι → Set X)
    (hZ : ∀ i, Z i ∈ irreducibleComponents X) (hZ_injective : Injective Z)
    (η : ι → X) (hη : ∀ i, IsGenericPoint (η i) (Z i)) :
    ∃ U : X.Opens, AlgebraicGeometry.IsAffineOpen U ∧ ∀ i, η i ∈ U
```

## Tag 03J1, a lemma

[Tag 03J1](https://stacks.math.columbia.edu/tag/03J1) in the Stacks Project.

**`AlgebraicGeometry.exists_dense_open_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/AmpleAndExtension/SuitableAffineOpens.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/AmpleAndExtension/SuitableAffineOpens.lean#L138). References: SGA 3 VIB (5.8.3), “special case”.

> A quasi-compact scheme has a separated dense open subscheme.

```lean
theorem exists_dense_open_isSeparated (X : Scheme.{u}) [CompactSpace X] :
    ∃ V : X.Opens, Dense (V : Set X) ∧ Scheme.IsSeparated V
```

## Tag 01ZX, a lemma

[Tag 01ZX](https://stacks.math.columbia.edu/tag/01ZX) in the Stacks Project.

**`AlgebraicGeometry.exists_affineOpen_mem_of_genericPoints_irreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/GenericPoints.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/GenericPoints.lean#L179).

> **Stacks Project, Tag 01ZX.** In a quasi-separated scheme, any point and
> the generic points of finitely many pairwise distinct irreducible components
> are contained in a common affine open.

```lean
theorem exists_affineOpen_mem_of_genericPoints_irreducibleComponents
    (X : Scheme.{u}) [QuasiSeparatedSpace X] {n : ℕ}
    (Z : Fin n → Set X) (hZ : ∀ i, Z i ∈ irreducibleComponents X)
    (hZ_injective : Function.Injective Z)
    (η : Fin n → X) (hη : ∀ i, IsGenericPoint (η i) (Z i)) (x : X) :
    ∃ U : X.Opens, IsAffineOpen U ∧ x ∈ U ∧ ∀ i, η i ∈ U
```

## Tag 01ZY, a lemma

[Tag 01ZY](https://stacks.math.columbia.edu/tag/01ZY) in the Stacks Project.

**`Stacks.AmpleAffineAvoidance.exists_affineOpen_containing_finite_of_ample`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleAffineAvoidance/AmpleFiniteSet.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleAffineAvoidance/AmpleFiniteSet.lean#L223). The attribute's comment: “part (3)”.

> **Stacks Tag 01ZY, part (3).** A finite set of points of a scheme carrying an ample invertible
> `𝒪_X`-module lies in an affine open.

```lean
theorem exists_affineOpen_containing_finite_of_ample (hL : IsAmple X L) {E : Set X}
    (hE : E.Finite) : ∃ U : X.Opens, IsAffineOpen U ∧ E ⊆ (U : Set X)
```

**`Stacks.AmpleCluster.exists_affineOpen_containing_finite_of_immersion_proj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCluster/ProjImmersion.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCluster/ProjImmersion.lean#L54). The attribute's comment: “part (4)”.

> A finite set of points of a scheme `X` with an immersion `X ⟶ Proj 𝒮` lies in an affine open of
> `X`.

```lean
theorem exists_affineOpen_containing_finite_of_immersion_proj {X : Scheme.{u}} {S : Type u}
    {σ : Type v} [CommRing S] [SetLike σ S] [AddSubgroupClass σ S] (𝒮 : ℕ → σ) [GradedRing 𝒮]
    (i : X ⟶ Proj 𝒮) [IsImmersion i] {E : Set X} (hE : E.Finite) :
    ∃ U : X.Opens, IsAffineOpen U ∧ E ⊆ (U : Set X)
```

**`Stacks.AmpleCluster.exists_affineOpen_containing_finite_of_isQuasiAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCluster/QuasiAffineAndImmersion.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCluster/QuasiAffineAndImmersion.lean#L86). The attribute's comment: “part (1)”.

> **Stacks Tag 01ZY, part (1).** A finite set of points of a quasi-affine scheme lies in an
> affine open.

```lean
theorem exists_affineOpen_containing_finite_of_isQuasiAffine {X : Scheme.{u}} [X.IsQuasiAffine]
    {E : Set X} (hE : E.Finite) : ∃ U : X.Opens, IsAffineOpen U ∧ E ⊆ U
```

**`Stacks.AmpleCluster.exists_affineOpen_containing_finite_of_immersion_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleCluster/QuasiAffineAndImmersion.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleCluster/QuasiAffineAndImmersion.lean#L95). The attribute's comment: “part (2)”.

> **Stacks Tag 01ZY, part (2).** A finite set of points of a locally closed subscheme of an
> affine scheme lies in an affine open.

```lean
theorem exists_affineOpen_containing_finite_of_immersion_affine {X Y : Scheme.{u}} (i : X ⟶ Y)
    [IsImmersion i] [IsAffine Y] {E : Set X} (hE : E.Finite) :
    ∃ U : X.Opens, IsAffineOpen U ∧ E ⊆ U
```

**`AlgebraicGeometry.exists_isAffineOpen_of_isImmersion_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/FiniteSetInAffineOpen.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/FiniteSetInAffineOpen.lean#L55). The attribute's comment: “case (2)”.

> A scheme `X` with an immersion `i : X ⟶ Y` into an affine scheme `Y` (that is, isomorphic to
> a locally closed subscheme of an affine scheme) has every finite set of its points inside a
> single affine open.

```lean
theorem exists_isAffineOpen_of_isImmersion_of_isAffine {X Y : Scheme.{u}} [IsAffine Y]
    (i : X ⟶ Y) [IsImmersion i] {E : Set X} (hE : E.Finite) :
    ∃ U : X.Opens, IsAffineOpen U ∧ E ⊆ (U : Set X)
```

**`AlgebraicGeometry.exists_isAffineOpen_of_isQuasiAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/FiniteSetInAffineOpen.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/FiniteSetInAffineOpen.lean#L67). The attribute's comment: “case (1)”.

> A quasi-affine scheme has every finite set of its points inside a single affine open.

```lean
theorem exists_isAffineOpen_of_isQuasiAffine (X : Scheme.{u}) [X.IsQuasiAffine] {E : Set X}
    (hE : E.Finite) : ∃ U : X.Opens, IsAffineOpen U ∧ E ⊆ (U : Set X)
```

## Tag 09NV, a lemma

[Tag 09NV](https://stacks.math.columbia.edu/tag/09NV) in the Stacks Project.

**`Stacks.AmpleFiniteAffineNonvanishing.exists_affine_nonvanishingOpen_containing_finite_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleFiniteAffineNonvanishing/Basic.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleFiniteAffineNonvanishing/Basic.lean#L111). References: EGA II (4.5.4).

> Let `L` be an ample invertible `𝒪_X`-module on a scheme `X`. A finite subset `E` of an open
> `W` of `X` lies in an affine ringed-space nonvanishing locus of a section of a positive tensor
> power of `L`, with that locus contained in `W`.

```lean
theorem exists_affine_nonvanishingOpen_containing_finite_sections (hL : IsAmple X L) {E : Set X}
    (hE : E.Finite) (W : X.Opens) (hEW : E ⊆ (W : Set X)) :
    ∃ n : ℕ, 1 ≤ n ∧
      ∃ s : (toSheafOfModules X (tensorPowModule X L (n : ℤ))).sections,
        IsAffineOpen (Stacks.NonvanishingTrivialize.nonvanishingOpen X.toRingedSpace
            (toSheafOfModules X (tensorPowModule X L (n : ℤ))) s) ∧
          E ⊆ (Stacks.NonvanishingTrivialize.nonvanishingOpen X.toRingedSpace
            (toSheafOfModules X (tensorPowModule X L (n : ℤ))) s : Set X) ∧
            (Stacks.NonvanishingTrivialize.nonvanishingOpen X.toRingedSpace
              (toSheafOfModules X (tensorPowModule X L (n : ℤ))) s : Set X) ⊆ (W : Set X)
```

**`Stacks.SheafOfModules.Invertible.exists_sections_finite_subset_nonvanishingOpen_le_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionExtension/FiniteSet.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionExtension/FiniteSet.lean#L148). References: EGA II (4.5.4).

> Let `L` be an ample invertible module on a scheme `Y`, and let `E ⊆ W ⊆ Y` with `E` finite
> and `W` open. Then there are an `n ≥ 1` and a global section `s` of `L^{⊗ n}` whose nonvanishing
> locus is affine and satisfies `E ⊆ Y_s ⊆ W`.

```lean
theorem exists_sections_finite_subset_nonvanishingOpen_le_of_isAmple
    (hL : AlgebraicGeometry.Scheme.Modules.IsAmple Y M)
    {E : Set Y} (hE : E.Finite) (W : Y.Opens) (hEW : E ⊆ W) :
    ∃ (m : ℕ) (_ : 1 ≤ m) (s : Mpow[m].sections),
      IsAffineOpen NV[m, s] ∧ E ⊆ (NV[m, s] : Set Y) ∧ (NV[m, s] : Set Y) ⊆ W
```

## Tag 0F20, a lemma

[Tag 0F20](https://stacks.math.columbia.edu/tag/0F20) in the Stacks Project.

**`Stacks.QuasiAffineGlobalGeneration.exists_affine_nonvanishingOpen_containing_finite_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiAffineGlobalGeneration/Basic.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiAffineGlobalGeneration/Basic.lean#L106).

> **Stacks Tag 0F20, at the ringed-space spelling**: over `L.sections`, with the
> ringed-space nonvanishing open of Stacks Tag 01CY. Transported from
> `Stacks.QuasiAffineGlobalGeneration.exists_affine_nonvanishingOpen_containing_finite` along
> `Stacks.NonvanishingSpelling.nonvanishingOpen_symm_eq`.

```lean
theorem exists_affine_nonvanishingOpen_containing_finite_sections [X.IsQuasiAffine]
    (L : X.Modules) [IsInvertibleModule X L] {E : Set X} (hE : E.Finite) (W : X.Opens)
    (hEW : E ⊆ (W : Set X)) :
    ∃ s : (toSheafOfModules X L).sections,
      IsAffineOpen (Stacks.NonvanishingTrivialize.nonvanishingOpen X.toRingedSpace
        (toSheafOfModules X L) s) ∧
      E ⊆ (Stacks.NonvanishingTrivialize.nonvanishingOpen X.toRingedSpace
        (toSheafOfModules X L) s : Set X) ∧
      Stacks.NonvanishingTrivialize.nonvanishingOpen X.toRingedSpace
        (toSheafOfModules X L) s ≤ W
```

## Tag 0BX3, a lemma

[Tag 0BX3](https://stacks.math.columbia.edu/tag/0BX3) in the Stacks Project.

**`AlgebraicGeometry.exists_affineOpen_germ_injective_of_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/GermInjective.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/GermInjective.lean#L37). The attribute's comment: “part (1)”.

> On an integral scheme, every point admits an affine open neighbourhood whose canonical
> map from its ring of sections to the local ring at the point is injective.

```lean
theorem exists_affineOpen_germ_injective_of_isIntegral (X : Scheme.{u}) (x : X)
    [IsIntegral X] :
    ∃ (U : X.Opens) (hx : x ∈ U),
      IsAffineOpen U ∧ Function.Injective (X.presheaf.germ U x hx)
```

**`AlgebraicGeometry.exists_affineOpen_germ_injective_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/GermInjective.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/GermInjective.lean#L46). The attribute's comment: “part (2)”.

> On a locally Noetherian scheme, every point admits an affine open neighbourhood whose
> canonical map from its ring of sections to the local ring at the point is injective.

```lean
theorem exists_affineOpen_germ_injective_of_isLocallyNoetherian (X : Scheme.{u}) (x : X)
    [IsLocallyNoetherian X] :
    ∃ (U : X.Opens) (hx : x ∈ U),
      IsAffineOpen U ∧ Function.Injective (X.presheaf.germ U x hx)
```

**`AlgebraicGeometry.exists_affineOpen_germ_injective_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/GermInjective.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/GermInjective.lean#L56). The attribute's comment: “part (3)”.

> On a reduced scheme with finitely many irreducible components, every point admits an
> affine open neighbourhood whose canonical map from its ring of sections to the local ring at
> the point is injective.

```lean
theorem exists_affineOpen_germ_injective_of_isReduced (X : Scheme.{u}) (x : X)
    [IsReduced X] (hX : (irreducibleComponents X).Finite) :
    ∃ (U : X.Opens) (hx : x ∈ U),
      IsAffineOpen U ∧ Function.Injective (X.presheaf.germ U x hx)
```

## Tag 0H9B, a lemma

[Tag 0H9B](https://stacks.math.columbia.edu/tag/0H9B) in the Stacks Project.

**`AlgebraicGeometry.exists_isAffineOpen_mapped_to_basicOpens`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/AffineNeighborhood.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/AffineNeighborhood.lean#L50).

> A point of a scheme admitting open immersions into two affine schemes has an affine open
> neighbourhood whose image in each scheme is a basic open.

```lean
theorem exists_isAffineOpen_mapped_to_basicOpens
    (U V W : Scheme.{u}) [IsAffine U] [IsAffine V]
    (i : W ⟶ U) (j : W ⟶ V) [IsOpenImmersion i] [IsOpenImmersion j] (w : W) :
    ∃ (W' : W.Opens) (f : Γ(U, ⊤)) (g : Γ(V, ⊤)),
      IsAffineOpen W' ∧ w ∈ W' ∧
        i.opensFunctor.obj W' = U.basicOpen f ∧
        j.opensFunctor.obj W' = V.basicOpen g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.30, Tag 01ZU](https://stacks.math.columbia.edu/tag/01ZU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
