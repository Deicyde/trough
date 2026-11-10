---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_flat_stratification, AlgebraicGeometry.HasFlatStratification.of_finitePresentation, AlgebraicGeometry.HasFlatStratification.of_finitePresentation_of_isNoetherian, AlgebraicGeometry.exists_isFlat_iff_exists_isFlat_derivedPullback, Module.exists_flat_localizedModule_coker, AlgebraicGeometry.hasImageBaseChangeStratification
statement: formalized
proof: formalized
---

# 37.54 Generic flatness stratification

Section 37.54 of the Stacks Project, [Tag 0H3Y](https://stacks.math.columbia.edu/tag/0H3Y). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ASY, a lemma

[Tag 0ASY](https://stacks.math.columbia.edu/tag/0ASY) in the Stacks Project.

**`AlgebraicGeometry.exists_flat_stratification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GenericFlatness/FlatStratificationQcqs.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GenericFlatness/FlatStratificationQcqs.lean#L171). References: EGA IV (6.9.3), “more general”; EGA IV (8.9.5).

> **Stacks Project, Tag 0ASY.**
>
> For a morphism of finite presentation `f : X ⟶ S` between quasi-compact, quasi-separated schemes
> and a finitely presented `𝒪_X`-module `ℱ`, the base carries a finite ascending chain of
> quasi-coherent ideal sheaves of finite type whose first closed subscheme is a thickening of `S`
> and whose last closed subscheme is empty, such that the pullback of `ℱ` to the fibre product of
> `X` with each locally closed stratum is flat over that stratum.
>
> The general case is reduced to the Noetherian case
> `AlgebraicGeometry.exists_flat_stratification_of_isNoetherian`; see the module docstring.

```lean
public theorem exists_flat_stratification {X S : Scheme.{u}} (f : X ⟶ S)
    [CompactSpace X] [QuasiSeparatedSpace X] [CompactSpace S] [QuasiSeparatedSpace S]
    (hf : FinitePresentation f) (F : X.Modules) [F.IsFinitePresentation] :
    ∃ (t : ℕ) (I : Fin (t + 1) → S.IdealSheafData),
      Stacks.Thickenings.IsThickening (I 0).subschemeι ∧
      (∀ i, Scheme.IdealSheafData.IsFiniteType (I i)) ∧
      (∀ i : Fin t, I (Fin.castSucc i) ≤ I (Fin.succ i)) ∧
      I (Fin.last t) = ⊤ ∧
      ∀ i : Fin t,
        let Z := I (Fin.castSucc i)
        let V : S.Opens := (I (Fin.succ i)).support.compl
        let U : Z.subscheme.Opens := Z.subschemeι ⁻¹ᵁ V
        let g : U.toScheme ⟶ S := U.ι ≫ Z.subschemeι
        IsFlatOver (pullback.snd f g).toLRSHom.toShHom
          ((Scheme.Modules.pullback (pullback.fst f g)).obj F)
```

## Tag 0H3Z, a lemma

[Tag 0H3Z](https://stacks.math.columbia.edu/tag/0H3Z) in the Stacks Project.

**`AlgebraicGeometry.HasFlatStratification.of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GenericFlatness/MorphismFlatStratificationQcqs.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GenericFlatness/MorphismFlatStratificationQcqs.lean#L62). References: EGA IV (6.9.3), “Case F = O_X”; EGA IV (8.9.5), “Case F = O_X”; SGA 6 XIII (1.13), “special case”.

> A morphism of finite presentation between quasi-compact quasi-separated
> schemes has a flat stratification of its base: a finite descending chain of closed subschemes,
> each cut out by an ideal sheaf of finite type, beginning with a thickening of the base and ending
> with the empty scheme, over each of whose locally closed strata the base change of the morphism
> is flat.

```lean
public theorem HasFlatStratification.of_finitePresentation {X S : Scheme.{u}} (f : X ⟶ S)
    [CompactSpace X] [QuasiSeparatedSpace X] [CompactSpace S] [QuasiSeparatedSpace S]
    (hf : FinitePresentation f) : HasFlatStratification f
```

**`AlgebraicGeometry.HasFlatStratification.of_finitePresentation_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GenericFlatness/NoetherianFlatStratification.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GenericFlatness/NoetherianFlatStratification.lean#L283). The attribute's comment: “the case of a Noetherian base. The general quasi-compact quasi-separated case of the tag is `AlgebraicGeometry.HasFlatStratification.of_finitePresentation`, which reduces to this one by absolute Noetherian approximation”.

> **The Noetherian case of Stacks 0H3Z**, with the hypotheses of the tag: a morphism of finite
> presentation to a Noetherian base has a flat stratification.

```lean
theorem HasFlatStratification.of_finitePresentation_of_isNoetherian {X S : Scheme.{u}}
    [IsNoetherian S] (f : X ⟶ S) (hf : FinitePresentation f) : HasFlatStratification f
```

## Tag 0H89, a lemma

[Tag 0H89](https://stacks.math.columbia.edu/tag/0H89) in the Stacks Project.

**`AlgebraicGeometry.exists_isFlat_iff_exists_isFlat_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GenericFlatness/FlatSingleDerivedPullbackConverse.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GenericFlatness/FlatSingleDerivedPullbackConverse.lean#L425).

> **Stacks 0H89** (Longke Tang). Let `f : X ⟶ S` be a surjective morphism of finite presentation
> and let `M` be an object of `D_QCoh(𝒪_S)` such that `H^i(M) = 0` for `i > 0`. Then `M` is
> isomorphic to a flat `𝒪_S`-module placed in degree `0` if and only if `Lf^*M` is isomorphic to a
> flat `𝒪_X`-module placed in degree `0`.

```lean
theorem exists_isFlat_iff_exists_isFlat_derivedPullback [Surjective f]
    (hf : FinitePresentation f)
    (M : DerivedCategory (SheafOfModules.{u} (structureSheafRing S.toRingedSpace)))
    (hQCoh : ∀ i : ℤ, ((DerivedCategory.homologyFunctor
      (SheafOfModules.{u} (structureSheafRing S.toRingedSpace)) i).obj M).IsQuasicoherent)
    (hM : ∀ i : ℤ, 0 < i → IsZero ((DerivedCategory.homologyFunctor
      (SheafOfModules.{u} (structureSheafRing S.toRingedSpace)) i).obj M)) :
    (∃ F : SheafOfModules.{u} (structureSheafRing S.toRingedSpace),
      SheafOfModules.IsFlat.{u, u, u, u} (O := S.toRingedSpace.sheaf) F ∧
        Nonempty (M ≅ (DerivedCategory.singleFunctor
          (SheafOfModules.{u} (structureSheafRing S.toRingedSpace)) 0).obj F)) ↔
      ∃ G : SheafOfModules.{u} (structureSheafRing X.toRingedSpace),
        SheafOfModules.IsFlat.{u, u, u, u} (O := X.toRingedSpace.sheaf) G ∧
          Nonempty ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
              f.toLRSHom.toShHom).obj M ≅
            (DerivedCategory.singleFunctor
              (SheafOfModules.{u} (structureSheafRing X.toRingedSpace)) 0).obj G)
```

## Tag 0H40, a lemma

[Tag 0H40](https://stacks.math.columbia.edu/tag/0H40) in the Stacks Project.

**`Module.exists_flat_localizedModule_coker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/CokernelGenericFlatness.lean, line 561](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/CokernelGenericFlatness.lean#L561). References: SGA 1 IV (6.7), “flatness clause”.

> **Stacks Project, Tag 0H40.** A map from a finite `A`-module to a finite
> `B`-module, for finite type algebras `R → A → B` over a Noetherian domain,
> has flat cokernel over `R` after a suitable principal localization.

```lean
theorem Module.exists_flat_localizedModule_coker
    {R : Type uR} {A : Type uA} {B : Type uB}
    [CommRing R] [IsNoetherianRing R] [IsDomain R]
    [CommRing A] [Algebra R A] [Algebra.FiniteType R A]
    [CommRing B] [Algebra A B] [Algebra.FiniteType A B]
    [Algebra R B] [IsScalarTower R A B]
    {M : Type uM} [AddCommGroup M] [Module A M] [Module.Finite A M]
    [Module R M] [IsScalarTower R A M]
    {N : Type uN} [AddCommGroup N] [Module B N] [Module.Finite B N]
    [Module A N] [IsScalarTower A B N]
    [Module R N] [IsScalarTower R A N]
    (φ : M →ₗ[A] N) :
    ∃ f : R, f ≠ 0 ∧
      Module.Flat (Localization.Away f)
        (LocalizedModule.Away f (N ⧸ LinearMap.range (φ.restrictScalars R)))
```

## Tag 0H41, a lemma

[Tag 0H41](https://stacks.math.columbia.edu/tag/0H41) in the Stacks Project.

**`AlgebraicGeometry.hasImageBaseChangeStratification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GenericFlatness/ImageStratification.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GenericFlatness/ImageStratification.lean#L392).

> **Stacks Project, Tag 0H41.** Let `S` be a quasi-compact and quasi-separated scheme and
> `f : X ⟶ Y` a morphism of schemes over `S` with both `X` and `Y` of finite presentation over `S`.
> Then there are a `t ≥ 0` and closed subschemes `S ⊇ S₀ ⊇ S₁ ⊇ ⋯ ⊇ S_t = ∅` such that each
> `S_i → S` is defined by a finite type ideal sheaf, `S₀ ⊆ S` is a thickening, and formation of the
> scheme-theoretic image of the base change of `f` to each stratum `S_i ∖ S_{i+1}` commutes with
> arbitrary base change.

```lean
theorem hasImageBaseChangeStratification {S : Scheme.{u}}
    [CompactSpace S] [QuasiSeparatedSpace S] (X Y : Over S) (f : X ⟶ Y)
    (hX : FinitePresentation X.hom) (hY : FinitePresentation Y.hom) :
    HasImageBaseChangeStratification f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.54, Tag 0H3Y](https://stacks.math.columbia.edu/tag/0H3Y)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
