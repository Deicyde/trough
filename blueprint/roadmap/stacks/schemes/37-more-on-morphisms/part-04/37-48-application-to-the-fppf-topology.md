---
declaration: section
origin: cited
lean: Stacks.Topologies.Fppf.etaleFiniteLocallyFreeDominates, Stacks.Topologies.Fppf.exists_openCover_finiteLocallyFree_refinement, AlgebraicGeometry.exists_integral_surjective_extension, Stacks.FiniteFactorization.exists_finite_surjective_extension, AlgebraicGeometry.exists_integral_surjective_openCover_factorization_of_mem_fppfPrecoverage, AlgebraicGeometry.exists_finite_surjective_openCover_factorization_of_mem_fppfPrecoverage, AlgebraicGeometry.isPHCoveringInCutoff_of_isEtaleCovering, AlgebraicGeometry.bigEtaleOverTopology_le_bigPHOverTopology
statement: formalized
proof: formalized
---

# 37.48 Application to the fppf topology

Section 37.48 of the Stacks Project, [Tag 05WM](https://stacks.math.columbia.edu/tag/05WM). 8 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DET, a lemma

[Tag 0DET](https://stacks.math.columbia.edu/tag/0DET) in the Stacks Project.

**`Stacks.Topologies.Fppf.etaleFiniteLocallyFreeDominates`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/LocallyQuasiFiniteRefinement.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/LocallyQuasiFiniteRefinement.lean#L151).

> **Stacks Project, Tag 0DET.** An fppf covering `{S_i ⟶ S}` is refined by an fppf covering
> `{V_a ⟶ S}` whose members factor as `V_a ⟶ S'_a ⟶ S` with `{S'_a ⟶ S}` an étale covering and
> `V_a ⟶ S'_a` surjective finite locally free.

```lean
theorem etaleFiniteLocallyFreeDominates {S : Scheme.{u}}
    (𝒰 : S.Cover.{v} Scheme.fppfPrecoverage) :
    EtaleFiniteLocallyFreeDominates 𝒰
```

## Tag 05WN, a lemma

[Tag 05WN](https://stacks.math.columbia.edu/tag/05WN) in the Stacks Project.

**`Stacks.Topologies.Fppf.exists_openCover_finiteLocallyFree_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/LocallyQuasiFiniteRefinement.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/LocallyQuasiFiniteRefinement.lean#L193).

> **Stacks Project, Tag 05WN.** Let `𝒮 = {S_i ⟶ S}` be an fppf covering of a scheme. Then
> there are a Zariski open covering `S = ⋃ U_j`, surjective finite locally free morphisms
> `W_j ⟶ U_j`, Zariski open coverings `W_j = ⋃_k W_{j,k}`, and surjective finite locally free
> morphisms `T_{j,k} ⟶ W_{j,k}`, such that the composites `{T_{j,k} ⟶ S}` form an fppf covering
> refining `𝒮`.
>
> This is `exists_openCover_finiteLocallyFree_refinement_of_hasQuasiFiniteSlices` applied to
> `AlgebraicGeometry.hasQuasiFiniteSlices`, the form of [Stacks, Tag 0570] used here.

```lean
theorem exists_openCover_finiteLocallyFree_refinement (S : Scheme.{u})
    (𝒮 : S.Cover.{v} Scheme.fppfPrecoverage) :
    ∃ (𝒰 : S.OpenCover.{max u v})
      (W : 𝒰.I₀ → Scheme.{u})
      (g : ∀ j, W j ⟶ 𝒰.X j)
      (𝒲 : ∀ j, (W j).OpenCover.{max u v})
      (T : ∀ j, (𝒲 j).I₀ → Scheme.{u})
      (h : ∀ j k, T j k ⟶ (𝒲 j).X k),
      (∀ j, Surjective (g j) ∧ Stacks.Morphisms.IsFiniteLocallyFree (g j)) ∧
      (∀ j k, Surjective (h j k) ∧ Stacks.Morphisms.IsFiniteLocallyFree (h j k)) ∧
      Presieve.ofArrows
          (fun jk : Σ j, (𝒲 j).I₀ ↦ T jk.1 jk.2)
          (fun jk ↦ h jk.1 jk.2 ≫ (𝒲 jk.1).f jk.2 ≫ g jk.1 ≫ 𝒰.f jk.1) ∈
        Scheme.fppfPrecoverage S ∧
      ∀ j k, ∃ i, ∃ l : T j k ⟶ 𝒮.X i,
        l ≫ 𝒮.f i = h j k ≫ (𝒲 j).f k ≫ g j ≫ 𝒰.f j
```

## Tag 0CNX, a lemma

[Tag 0CNX](https://stacks.math.columbia.edu/tag/0CNX) in the Stacks Project.

**`AlgebraicGeometry.exists_integral_surjective_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FppfApplication/IntegralSurjectiveExtension.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FppfApplication/IntegralSurjectiveExtension.lean#L81). The attribute's comment: “a surjective integral morphism over a retrocompact open of S extends to a surjective integral morphism over S with the same restriction to the open”.

> **Stacks Project, Tag 0CNX**, in corrected form, with `U` retrocompact in `S`: a surjective
> integral morphism over a retrocompact open subscheme extends to a surjective integral morphism
> over the whole scheme, without changing its restriction to the open subscheme. The general
> statement of [Stacks, Tag 0CNX] is false;
> `AlgebraicGeometry.exists_integral_surjective_extension_and_not_forall` pairs this theorem with
> the failure of the statement for an arbitrary open subscheme.

```lean
theorem exists_integral_surjective_extension
    {S : Scheme.{u}} (U : S.Opens) [QuasiCompact U.ι]
    {V : Scheme.{u}} (f : V ⟶ U.toScheme) [IsIntegralHom f] [Surjective f] :
    ∃ (W : Scheme.{u}) (g : W ⟶ S),
      IsIntegralHom g ∧ Surjective g ∧
        Nonempty (Over.mk f ≅ (Over.pullback U.ι).obj (Over.mk g))
```

## Tag 0CNY, a lemma

[Tag 0CNY](https://stacks.math.columbia.edu/tag/0CNY) in the Stacks Project.

**`Stacks.FiniteFactorization.exists_finite_surjective_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteFactorization/ExtendFiniteSurjective.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FiniteFactorization/ExtendFiniteSurjective.lean#L47).

> Let `S` be a quasi-compact quasi-separated scheme and let `U ⊆ S` be a quasi-compact open.
> A finite surjective morphism `f : V ⟶ U` extends to a finite surjective morphism `g : V̄ ⟶ S`:
> there is an isomorphism `e : V̄ ×_S U ≅ V` identifying the projection `V̄ ×_S U ⟶ U` with `f`, so
> that `e` is an isomorphism of schemes over `U`.

```lean
theorem exists_finite_surjective_extension {S V : Scheme.{u}}
    [CompactSpace S] [QuasiSeparatedSpace S]
    (U : S.Opens) (hU : IsCompact (U : Set S))
    (f : V ⟶ U.toScheme) [IsFinite f] [Surjective f] :
    ∃ (Vbar : Scheme.{u}) (g : Vbar ⟶ S),
      IsFinite g ∧ Surjective g ∧
        ∃ e : pullback g U.ι ≅ V,
          e.hom ≫ f = pullback.snd g U.ι
```

## Tag 0CNZ, a lemma

[Tag 0CNZ](https://stacks.math.columbia.edu/tag/0CNZ) in the Stacks Project.

**`AlgebraicGeometry.exists_integral_surjective_openCover_factorization_of_mem_fppfPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FppfApplication/IntegralDomination.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FppfApplication/IntegralDomination.lean#L125).

> **Stacks Project, Tag 0CNZ.** For every fppf covering `{X i ⟶ S}` of a scheme `S` there
> are a surjective integral morphism `g : S' ⟶ S` and an open covering of `S'` such that each
> member `U c` of the covering maps to `S` through some member `X i` of the given covering.
>
> No hypothesis is imposed on `S`, as none is imposed in the source.

```lean
theorem exists_integral_surjective_openCover_factorization_of_mem_fppfPrecoverage
    {I : Type v} {S : Scheme.{u}}
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ S)
    (hf : Presieve.ofArrows X f ∈ Scheme.fppfPrecoverage S) :
    ∃ (S' : Scheme.{u}) (g : S' ⟶ S), IsIntegralHom g ∧ Surjective g ∧
      ∃ (J : Type u) (U : J → S'.Opens), (⨆ c, U c) = ⊤ ∧
        ∀ c, ∃ i, ∃ t : (U c).toScheme ⟶ X i, (U c).ι ≫ g = t ≫ f i
```

## Tag 0CP0, a lemma

[Tag 0CP0](https://stacks.math.columbia.edu/tag/0CP0) in the Stacks Project.

**`AlgebraicGeometry.exists_finite_surjective_openCover_factorization_of_mem_fppfPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FppfApplication/FiniteDomination.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FppfApplication/FiniteDomination.lean#L165).

> **[Stacks, Tag 0CP0].** For every fppf covering `{X i ⟶ S}` of a quasi-compact and
> quasi-separated scheme `S` there are a surjective finite morphism `g : S' ⟶ S` of finite
> presentation and an open covering of `S'` such that each member `U c` of the covering maps to
> `S` through some member `X i` of the given covering.
>
> The second input of the source proof, [Stacks, Tag 09YZ], is supplied by
> `Stacks.AlgebraicGeometry.Tag0817PartTwo.nonempty_integralLimitPresentation`, which proves it
> at exactly the quasi-compactness and quasi-separatedness assumed here.

```lean
theorem exists_finite_surjective_openCover_factorization_of_mem_fppfPrecoverage
    {I : Type v} {S : Scheme.{u}} [CompactSpace S] [QuasiSeparatedSpace S]
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ S)
    (hf : Presieve.ofArrows X f ∈ Scheme.fppfPrecoverage S) :
    ∃ (S' : Scheme.{u}) (g : S' ⟶ S), IsFinite g ∧ Surjective g ∧ FinitePresentation g ∧
      ∃ (J : Type u) (U : J → S'.Opens), (⨆ c, U c) = ⊤ ∧
        ∀ c, ∃ i, ∃ t : (U c).toScheme ⟶ X i, (U c).ι ≫ g = t ≫ f i
```

## Tag 0DBT, a lemma

[Tag 0DBT](https://stacks.math.columbia.edu/tag/0DBT) in the Stacks Project.

**`AlgebraicGeometry.isPHCoveringInCutoff_of_isEtaleCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToEtaleSquares.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToEtaleSquares.lean#L81). The attribute's comment: “étale coverings in a cutoff category”.

> An étale covering family in a size-bounded category of schemes is a ph covering family
> there, since both conditions are read off the image of the family in all schemes.

```lean
public theorem isPHCoveringInCutoff_of_isEtaleCovering {κ : Cardinal.{u}}
    (𝒰 : Covering.{u + 1, u, u + 1} (SchemeBelow κ)) (h𝒰 : IsEtaleCovering 𝒰) :
    IsPHCoveringInCutoff 𝒰
```

**`AlgebraicGeometry.bigEtaleOverTopology_le_bigPHOverTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToEtaleSquares.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToEtaleSquares.lean#L176). The attribute's comment: “étale coverings on a slice”.

> The big-site comparison from ph to étale is induced by the identity functor on the common
> slice category: every étale covering of the slice is a ph covering of the slice.

```lean
public theorem bigEtaleOverTopology_le_bigPHOverTopology (B : BigPHSite.{u}) (X : B.Schemes) :
    BigEtaleOver.topology (phAssociatedBigEtaleSite B) X.1 X.2 ≤ B.topology.over X
```

**`AlgebraicGeometry.isPHCovering_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/EtaleHComparison.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/EtaleHComparison.lean#L102). The attribute's comment: “étale coverings”.

> A family of étale morphisms of schemes whose images cover the target is a ph covering.

```lean
public theorem isPHCovering_of_etale {T : Scheme.{u}} {I : Type v} (X : I → Scheme.{u})
    (f : ∀ i, X i ⟶ T) (hsurj : ∀ x : T, ∃ i, x ∈ Set.range (f i).base)
    (hetale : ∀ i, Etale (f i)) :
    IsPHCovering X f
```

**`AlgebraicGeometry.IsPHCovering.of_mem_fppfPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/V/FppfAffineDomination.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/V/FppfAffineDomination.lean#L116).

> An fppf covering of schemes is a ph covering.

```lean
theorem IsPHCovering.of_mem_fppfPrecoverage
    {T : Scheme.{u}} {I : Type v} (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T)
    (hf : Presieve.ofArrows X f ∈ Scheme.fppfPrecoverage T) :
    IsPHCovering X f
```

## Tag 0DBU, a remark

[Tag 0DBU](https://stacks.math.columbia.edu/tag/0DBU) in the Stacks Project.

**`AlgebraicGeometry.phToFppf_isMorphismOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToFppfComparison.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToFppfComparison.lean#L407). The attribute's comment: “the comparison is the morphism of sites given by the identity functor on underlying categories”.

> **Stacks 0DBU: `ε` is the morphism of sites given by the identity functor on underlying
> categories.** The two sites have the one underlying category, the slice over `X` of the common
> category of schemes, and the identity functor of it, read from the fppf site to the ph site,
> satisfies the two conditions of Stacks 00X1: it is continuous and the functor it induces on
> sheaves of sets is left exact.  So it is a morphism of sites `(Sch/S)_ph ⟶ (Sch/S)_fppf`, and
> `AlgebraicGeometry.phToBigFppfMorphism` is the morphism of topoi Stacks 00XC attaches to it.

```lean
public theorem phToFppf_isMorphismOfSites (B : BigPHSite.{u}) (X : B.Schemes) :
    IsMorphismOfSites.{u + 1} (𝟭 (Over X))
      (BigFppfOver.topology (phAssociatedBigFppfSite B) X.1 X.2) (B.topology.over X)
```

**`AlgebraicGeometry.phToBigFppf_pushforward_comp_sheafToPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToFppfComparison.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToFppfComparison.lean#L419). The attribute's comment: “the direct image is the identity on underlying presheaves”.

> **Stacks 0DBU: `ε_*` is the identity on underlying presheaves.** Forming the direct image of
> a ph sheaf and then forgetting the fppf sheaf condition gives back the presheaf one started
> from, because the direct image is restriction along the identity functor of the common slice
> category.  The two sides are equal, not merely isomorphic.

```lean
public theorem phToBigFppf_pushforward_comp_sheafToPresheaf (B : BigPHSite.{u})
    (X : B.Schemes) :
    (phToBigFppfMorphism B X).pushforward ⋙
        sheafToPresheaf (BigFppfOver.topology (phAssociatedBigFppfSite B) X.1 X.2)
          (Type (u + 1)) =
      sheafToPresheaf (B.topology.over X) (Type (u + 1))
```

**`AlgebraicGeometry.phToBigFppf_inverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToFppfComparison.lean, line 439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToFppfComparison.lean#L439). The attribute's comment: “the inverse image is the ph sheafification of an fppf sheaf”.

> **Stacks 0DBU: `ε⁻¹` associates to an fppf sheaf its ph sheafification.** The inverse image
> is the functor on sheaves of sets induced by the identity functor of the common slice, and the
> left Kan extension along the identity is the identity, so the inverse image is the forgetful
> functor to presheaves followed by ph sheafification.
>
> The isomorphism is the canonical one, not just some isomorphism of the right type: `ε` is by
> construction the change-of-topology morphism of the identity functor, and the comparison is
> `CategoryTheory.changeOfTopologyMorphism_inverseImageIso`, built from the construction of the
> induced functor as a left Kan extension followed by sheafification.

```lean
public def phToBigFppf_inverseImageIso (B : BigPHSite.{u}) (X : B.Schemes) :
    (phToBigFppfMorphism B X).inverseImage ≅
      sheafToPresheaf (BigFppfOver.topology (phAssociatedBigFppfSite B) X.1 X.2)
          (Type (u + 1)) ⋙
        presheafToSheaf (B.topology.over X) (Type (u + 1))
```

**`AlgebraicGeometry.phToZariski_pushforward_comp_sheafToPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToFppfComparison.lean, line 518](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToFppfComparison.lean#L518). The attribute's comment: “by composition, the comparison of the ph topology with the Zariski topology”.

> **Stacks 0DBU: by composition the ph topology is compared with the Zariski topology.**
> `AlgebraicGeometry.phToZariskiMorphism`, the composition of `ε` with the change-of-topology
> morphism from the fppf to the Zariski topology, is a comparison of the ph topology with the
> Zariski topology of Stacks 03FF: it is a morphism of topoi from ph sheaves to Zariski sheaves
> whose direct image is the identity on underlying presheaves, as `ε`'s own is.

```lean
public theorem phToZariski_pushforward_comp_sheafToPresheaf (B : BigPHSite.{u})
    (X : B.Schemes) :
    (phToZariskiMorphism B X).pushforward ⋙
        sheafToPresheaf ((phAssociatedBigFppfSite B).zariskiTopology.over X) (Type (u + 1)) =
      sheafToPresheaf (B.topology.over X) (Type (u + 1))
```

**`AlgebraicGeometry.phToEtale_pushforward_comp_sheafToPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToFppfComparison.lean, line 544](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToFppfComparison.lean#L544). The attribute's comment: “by composition, the comparison of the ph topology with the étale topology”.

> **Stacks 0DBU: by composition the ph topology is compared with the étale topology.**
> `AlgebraicGeometry.phToEtaleMorphism`, the composition of `ε` with the change-of-topology
> morphism from the fppf to the étale topology, is a comparison of the ph topology with the étale
> topology of Stacks 03FF: it is a morphism of topoi from ph sheaves to étale sheaves whose
> direct image is the identity on underlying presheaves, as `ε`'s own is.

```lean
public theorem phToEtale_pushforward_comp_sheafToPresheaf (B : BigPHSite.{u}) (X : B.Schemes) :
    (phToEtaleMorphism B X).pushforward ⋙
        sheafToPresheaf ((phAssociatedBigFppfSite B).etaleTopology.over X) (Type (u + 1)) =
      sheafToPresheaf (B.topology.over X) (Type (u + 1))
```

**`AlgebraicGeometry.phToSmooth_pushforward_comp_sheafToPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToFppfComparison.lean, line 569](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToFppfComparison.lean#L569). The attribute's comment: “by composition, the comparison of the ph topology with the smooth topology”.

> **Stacks 0DBU: by composition the ph topology is compared with the smooth topology.**
> `AlgebraicGeometry.phToSmoothMorphism`, the composition of `ε` with the change-of-topology
> morphism from the fppf to the smooth topology, is a comparison of the ph topology with the
> smooth topology of Stacks 03FF: it is a morphism of topoi from ph sheaves to smooth sheaves
> whose direct image is the identity on underlying presheaves, as `ε`'s own is.

```lean
public theorem phToSmooth_pushforward_comp_sheafToPresheaf (B : BigPHSite.{u}) (X : B.Schemes) :
    (phToSmoothMorphism B X).pushforward ⋙
        sheafToPresheaf ((phAssociatedBigFppfSite B).smoothTopology.over X) (Type (u + 1)) =
      sheafToPresheaf (B.topology.over X) (Type (u + 1))
```

**`AlgebraicGeometry.phToSyntomic_pushforward_comp_sheafToPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToFppfComparison.lean, line 594](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToFppfComparison.lean#L594). The attribute's comment: “by composition, the comparison of the ph topology with the syntomic topology”.

> **Stacks 0DBU: by composition the ph topology is compared with the syntomic topology.**
> `AlgebraicGeometry.phToSyntomicMorphism`, the composition of `ε` with the change-of-topology
> morphism from the fppf to the syntomic topology, is a comparison of the ph topology with the
> syntomic topology of Stacks 03FF: it is a morphism of topoi from ph sheaves to syntomic sheaves
> whose direct image is the identity on underlying presheaves, as `ε`'s own is.

```lean
public theorem phToSyntomic_pushforward_comp_sheafToPresheaf (B : BigPHSite.{u})
    (X : B.Schemes) :
    (phToSyntomicMorphism B X).pushforward ⋙
        sheafToPresheaf ((phAssociatedBigFppfSite B).syntomicTopology.over X) (Type (u + 1)) =
      sheafToPresheaf (B.topology.over X) (Type (u + 1))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.48, Tag 05WM](https://stacks.math.columbia.edu/tag/05WM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
