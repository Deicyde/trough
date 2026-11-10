---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isSheaf_fppf_of_isLocallyQuasicoherent_of_flatBaseChange, AlgebraicGeometry.Stack.isSheaf_fppf_of_isLocallyQuasicoherent_of_isLocallyBijective_flatLfp, AlgebraicGeometry.Stack.isZero_rightDerived_etaleComparisonPushforward_of_lqcFbc, AlgebraicGeometry.Stack.isSheaf_fppf_of_lqc_flatLfp, AlgebraicGeometry.Stack.isZero_rightDerived_etaleComparisonPushforward_lqcFbcModule, AlgebraicGeometry.Stack.nonempty_fppfCohomologyIso_etaleCohomology_lqcFbcModule, AlgebraicGeometry.Stack.nonempty_higherDirectImageIso_sheafify_etale_lqcFbcModule, AlgebraicGeometry.Stack.inclusionToposMorphism
statement: formalized
proof: formalized
---

# 96.23 Change of topology

Section 96.23 of the Stacks Project, [Tag 075Q](https://stacks.math.columbia.edu/tag/075Q). 3 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 076T, a lemma

[Tag 076T](https://stacks.math.columbia.edu/tag/076T) in the Stacks Project.

**`AlgebraicGeometry.Stack.isSheaf_fppf_of_isLocallyQuasicoherent_of_flatBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FppfSheafFlatBaseChangeProved.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FppfSheafFlatBaseChangeProved.lean#L90).

> **Stacks 076T.** Let `F` be a presheaf of modules over the structure sheaf of a category
> fibred in groupoids over the big fppf category of schemes over `S`. If `F` is locally
> quasi-coherent (**Stacks 06WJ**) and the comparison map `c_φ` of **Stacks 06WC** is an
> isomorphism for every arrow of `𝒳` lying over a morphism of schemes which is flat and locally of
> finite presentation, then `F` is a sheaf for the fppf topology of **Stacks 06TP**.
>
> The sheaf condition is tested, by
> `AlgebraicGeometry.Stack.isSheaf_of_isSheafFor_flatLfp`, on the families of arrows lying over an
> fppf covering of schemes; along such a family hypothesis (b) applies to every member, and the
> sheaf condition for it is
> `AlgebraicGeometry.Stack.isSheafForLiftedFppfFamily_of_isFiberedInGroupoids`.

```lean
theorem isSheaf_fppf_of_isLocallyQuasicoherent_of_flatBaseChange
    (F : PresheafOfModules.{u} (ringStructureSheafCore B S hS p hp (etaleTopology B)
      (etaleTopology_le_topology B)).obj)
    (hlqc : IsLocallyQuasicoherent B E h S hS p hp F)
    (hbc : HasFlatLfpBaseChangeProperty B E h S hS p hp (etaleTopology B)
      (etaleTopology_le_topology B) F) :
    Presheaf.IsSheaf (associatedTopology B S hS p B.topology) F.presheaf
```

**`AlgebraicGeometry.Stack.isSheaf_fppf_of_isLocallyQuasicoherent_of_isLocallyBijective_flatLfp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FppfSheafOfLocallyBijectiveFlatLfpComparison.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FppfSheafOfLocallyBijectiveFlatLfpComparison.lean#L62). The attribute's comment: “with the pullback of sheaves of Stacks 06WC in hypothesis (b)”.

> **Stacks 076T**, with the pullback of sheaves of Stacks 06WC. Let `F` be a presheaf of
> modules over the structure sheaf of a category fibred in groupoids over `(Sch/S)_{fppf}`. If `F`
> is locally quasi-coherent (Stacks 06WJ) and the comparison map
> `c_φ : f_{small}^*(F|_{V_ét}) ⟶ F|_{U_ét}` is an isomorphism of sheaves (it is locally injective
> and locally surjective for the étale topology of the small site of `U`) for every arrow `φ` of
> `𝒳` lying over a morphism of schemes which is flat and locally of finite presentation, then `F`
> is a sheaf for the fppf topology of Stacks 06TP.

```lean
theorem isSheaf_fppf_of_isLocallyQuasicoherent_of_isLocallyBijective_flatLfp
    (hlqc : IsLocallyQuasicoherent B E h S hS p hp F)
    (hbc : ∀ {x y : 𝒳} (φ : x ⟶ y), Flat (B.inclusion.map (p.map φ).left) →
      LocallyOfFinitePresentation (B.inclusion.map (p.map φ).left) →
        IsLocallyBijectiveRestrictModulePullbackComparisonUnivLE B E h S hS p hp
          (etaleTopology B) (etaleTopology_le_topology B) φ F) :
    Presheaf.IsSheaf (associatedTopology B S hS p B.topology) F.presheaf
```

## Tag 075R, a lemma

[Tag 075R](https://stacks.math.columbia.edu/tag/075R) in the Stacks Project.

**`AlgebraicGeometry.Stack.isZero_rightDerived_etaleComparisonPushforward_of_lqcFbc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/EtaleComparisonAcyclicity.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/EtaleComparisonAcyclicity.lean#L197). The attribute's comment: “clause (1), `Rε_*ℱ = ε_*ℱ` for the comparison ε : 𝒳_fppf ⟶ 𝒳_étale and a module which is locally quasi-coherent with flat base change: the vanishing of the higher direct images, reduced through Stacks 072W to the affine-object vanishing Stacks 08IY and 08IZ carry, which is carried here as that same predicate `hvan`, together with the étale covering class of the affine objects as `hB`. Clauses (2) and (3), which the source deduces from (1) by the Leray spectral sequence and by Stacks 075G, are not covered”.

> **Stacks 075R, clause (1).**  Let `𝒳` be a category fibred in groupoids over the big fppf
> site of `S`, let `ε : 𝒳_fppf ⟶ 𝒳_étale` be the comparison morphism, and let `ℱ` be a sheaf of
> `𝒪_𝒳`-modules on the fppf site which is locally quasi-coherent (**Stacks 06WJ**) and has the flat
> base change property (**Stacks 0762**).  Then
>
> `R^iε_*ℱ = 0` for `i > 0`,
>
> that is, `Rε_*ℱ = ε_*ℱ`.
>
> This is the source's reduction: by **Stacks 072W** the sheaf `R^iε_*ℱ` is the étale
> sheafification of the presheaf `x ↦ H^i_{fppf}(x, ℱ)`, and that presheaf vanishes on the objects
> lying over an affine scheme, which cover étale-locally.
>
> The affine vanishing `hvan` and the covering class `hB` are carried; see this file's module
> documentation.

```lean
theorem isZero_rightDerived_etaleComparisonPushforward_of_lqcFbc
    [HasSheafify (BigFppfOver.associatedTopology B S hS p .etale) AddCommGrpCat.{u}]
    [(BigFppfOver.associatedTopology B S hS p .etale).WEqualsLocallyBijective AddCommGrpCat.{u}]
    (hB : (BigFppfOver.associatedTopology B S hS p .etale).HasEnoughObjects
      (fun x => IsAffineOver B S hS (p.obj x)))
    (hvan : HasAffineAcyclicLqcFbcModules B E h S hS p hp)
    (ℱ : fppfSiteModules B S hS p hp)
    (hℱ : IsLocallyQuasicoherentWithFlatBaseChange B E h S hS p hp ℱ.val)
    (i : ℕ) (hi : 0 < i) :
    IsZero (((etaleComparisonPushforward B S hS p hp).rightDerived i).obj ℱ)
```

**`AlgebraicGeometry.Stack.isSheaf_fppf_of_lqc_flatLfp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FppfEtaleComparisonLqcFbc.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FppfEtaleComparisonLqcFbc.lean#L107). The attribute's comment: “the first assertion: a presheaf of modules satisfying (a) and (b) is an 𝒪_𝒳-module, i.e. a sheaf for the fppf topology”.

> **Stacks 075R, the first assertion.** A presheaf of `𝒪_𝒳`-modules which is locally
> quasi-coherent (**Stacks 06WJ**) and whose comparison maps `c_φ` of **Stacks 06WC** are
> isomorphisms along the arrows lying over flat morphisms locally of finite presentation is a sheaf
> for the fppf topology of `𝒳`, that is, an `𝒪_𝒳`-module.

```lean
theorem isSheaf_fppf_of_lqc_flatLfp :
    Presheaf.IsSheaf (BigFppfOver.associatedTopology B S hS p .fppf) F.presheaf
```

**`AlgebraicGeometry.Stack.isZero_rightDerived_etaleComparisonPushforward_lqcFbcModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FppfEtaleComparisonLqcFbc.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FppfEtaleComparisonLqcFbc.lean#L200). The attribute's comment: “clause (1): `Rε_*ℱ = ε_*ℱ`, i.e. `R^iε_*ℱ = 0` for `i > 0`, for the comparison `ε : 𝒳_fppf ⟶ 𝒳_étale` and a module satisfying (a) and (b)”.

> **Stacks 075R, clause (1).** Let `ℱ` be a presheaf of `𝒪_𝒳`-modules which is locally
> quasi-coherent (**Stacks 06WJ**) and whose comparison maps `c_φ` of **Stacks 06WC** are
> isomorphisms along the arrows lying over flat morphisms locally of finite presentation, and let
> `ε : 𝒳_{fppf} ⟶ 𝒳_{étale}` be the comparison morphism. Then
>
> `R^iε_*ℱ = 0` for `i > 0`,
>
> that is, `Rε_*ℱ = ε_*ℱ`. Here `ℱ` is the `𝒪_𝒳`-module of the first assertion,
> `AlgebraicGeometry.Stack.lqcFbcModule`.

```lean
theorem isZero_rightDerived_etaleComparisonPushforward_lqcFbcModule (i : ℕ) (hi : 0 < i) :
    IsZero (((etaleComparisonPushforward B S hS p hp).rightDerived i).obj
      (lqcFbcModule B E h S hS p hp F hlqc hbc))
```

**`AlgebraicGeometry.Stack.nonempty_fppfCohomologyIso_etaleCohomology_lqcFbcModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcFbcModuleFppfEtaleCohomology.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcFbcModuleFppfEtaleCohomology.lean#L203). The attribute's comment: “clause (2): fppf cohomology `H^p(𝒳, ℱ)`, `H^p(x, ℱ)` and the derived sections `RΓ(𝒳, ℱ)`, `RΓ(x, ℱ)` of a module satisfying (a) and (b) agree with those computed in the étale topology”.

> **Stacks 075R, clause (2).** Let `ℱ` be a presheaf of `𝒪_𝒳`-modules satisfying (a) and (b) of
> Stacks 075R, so an `𝒪_𝒳`-module (`AlgebraicGeometry.Stack.lqcFbcModule`), and let
> `ε : 𝒳_{fppf} ⟶ 𝒳_{étale}` be the comparison morphism. The cohomology of `ℱ` computed in the
> fppf topology agrees with the cohomology of `ε_*ℱ`, the same presheaf of modules, computed in the
> étale topology:
>
> * `H^n_{fppf}(𝒳, ℱ) ≅ H^n_{étale}(𝒳, ε_*ℱ)` for all `n`;
> * `H^n_{fppf}(x, ℱ) ≅ H^n_{étale}(x, ε_*ℱ)` for every object `x` of `𝒳` and all `n`;
> * `RΓ_{fppf}(𝒳, ℱ) ≅ RΓ_{étale}(𝒳, ε_*ℱ)` and `RΓ_{fppf}(x, ℱ) ≅ RΓ_{étale}(x, ε_*ℱ)`, the
>   derived sections being the complexes of sections of injective resolutions, up to homotopy.
>
> As in the source this follows formally from clause (1): `ε_*` is left exact and preserves
> injectives, and `ℱ` is `ε_*`-acyclic by
> `AlgebraicGeometry.Stack.isZero_rightDerived_etaleComparisonPushforward_lqcFbcModule`, so `ε_*`
> carries an injective resolution of `ℱ` to one of `ε_*ℱ`, and both cohomologies are computed by
> the same complex of sections.

```lean
theorem nonempty_fppfCohomologyIso_etaleCohomology_lqcFbcModule :
    (∀ n : ℕ, Nonempty (((Stacks.Cohomology.SiteModules.globalSectionsFunctor.{v, u, u, u}
        (fppfSiteRingSheaf B S hS p hp)).rightDerived n).obj
        (lqcFbcModule B E h S hS p hp F hlqc hbc) ≅
      ((Stacks.Cohomology.SiteModules.globalSectionsFunctor.{v, u, u, u}
        (etaleSiteRingSheaf B S hS p hp)).rightDerived n).obj
        ((etaleComparisonPushforward B S hS p hp).obj
          (lqcFbcModule B E h S hS p hp F hlqc hbc)))) ∧
    (∀ (x : 𝒳) (n : ℕ), Nonempty
      (((SheafOfModules.evaluation.{u} (fppfSiteRingSheaf B S hS p hp) (op x)).rightDerived n).obj
        (lqcFbcModule B E h S hS p hp F hlqc hbc) ≅
      ((SheafOfModules.evaluation.{u} (etaleSiteRingSheaf B S hS p hp) (op x)).rightDerived n).obj
        ((etaleComparisonPushforward B S hS p hp).obj
          (lqcFbcModule B E h S hS p hp F hlqc hbc)))) ∧
    Nonempty ((Stacks.Cohomology.SiteModules.globalSectionsFunctor.{v, u, u, u}
        (fppfSiteRingSheaf B S hS p hp)).rightDerivedToHomotopyCategory.obj
        (lqcFbcModule B E h S hS p hp F hlqc hbc) ≅
      (Stacks.Cohomology.SiteModules.globalSectionsFunctor.{v, u, u, u}
        (etaleSiteRingSheaf B S hS p hp)).rightDerivedToHomotopyCategory.obj
        ((etaleComparisonPushforward B S hS p hp).obj
          (lqcFbcModule B E h S hS p hp F hlqc hbc))) ∧
    (∀ x : 𝒳, Nonempty
      ((SheafOfModules.evaluation.{u} (fppfSiteRingSheaf B S hS p hp)
          (op x)).rightDerivedToHomotopyCategory.obj
        (lqcFbcModule B E h S hS p hp F hlqc hbc) ≅
      (SheafOfModules.evaluation.{u} (etaleSiteRingSheaf B S hS p hp)
          (op x)).rightDerivedToHomotopyCategory.obj
        ((etaleComparisonPushforward B S hS p hp).obj
          (lqcFbcModule B E h S hS p hp F hlqc hbc))))
```

**`AlgebraicGeometry.Stack.nonempty_higherDirectImageIso_sheafify_etale_lqcFbcModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcFbcModuleFppfEtaleHigherDirectImage.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcFbcModuleFppfEtaleHigherDirectImage.lean#L282). The attribute's comment: “clause (3): for a 1-morphism `f : 𝒳 → 𝒴` of categories fibred in groupoids and a module `ℱ` satisfying (a) and (b), `R^if_*ℱ` is the fppf sheafification of the higher direct image computed in the étale topology, and similarly for the derived direct image”.

> **Stacks 075R, clause (3).** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of categories fibred in groupoids
> over `(Sch/S)_{fppf}` and let `ℱ` be a presheaf of `𝒪_𝒳`-modules satisfying (a) and (b) of
> Stacks 075R, so an `𝒪_𝒳`-module (`AlgebraicGeometry.Stack.lqcFbcModule`). Then
>
> * `R^i f_*ℱ`, computed in the fppf topology, is the fppf sheafification of the higher direct image
>   `R^i f_{étale,*}(ε_*ℱ)` computed in the étale topology, for every `i`;
> * similarly for the derived direct image: `Rf_*ℱ` is `ε⁻¹(Rf_{étale,*}(ε_*ℱ))`, the direct images
>   being those of injective resolutions, up to homotopy, and `ε⁻¹` the fppf sheafification of
>   étale modules (`Stacks.SheafOfModules.comparisonPullbackIso`).
>
> The source deduces this from (2) and Stacks 075G. Here it is deduced from (1) directly:
> `f_{fppf,*} ≅ ε⁻¹ ∘ f_{étale,*} ∘ ε_*` (`AlgebraicGeometry.Stack.moduleDirectImageIsoEtale`),
> `ε_*` carries an injective resolution of the `ε_*`-acyclic module `ℱ` to one of `ε_*ℱ`, and
> `ε⁻¹` is exact.

```lean
theorem nonempty_higherDirectImageIso_sheafify_etale_lqcFbcModule :
    (∀ i : ℕ, Nonempty (((moduleDirectImageSmall B S hS p q hp hq f hf .fppf).rightDerived i).obj
        (lqcFbcModule B E h S hS p hp F hlqc hbc) ≅
      (PresheafOfModules.sheafification.{u} (𝟙 (fppfSiteRingSheaf B S hS q hq).obj)).obj
        (((moduleDirectImageSmall B S hS p q hp hq f hf .etale).rightDerived i).obj
          ((etaleComparisonPushforward B S hS p hp).obj
            (lqcFbcModule B E h S hS p hp F hlqc hbc))).val)) ∧
    Nonempty
      ((moduleDirectImageSmall B S hS p q hp hq f hf .fppf).rightDerivedToHomotopyCategory.obj
          (lqcFbcModule B E h S hS p hp F hlqc hbc) ≅
        ((etaleComparisonPullback B S hS q hq).mapHomotopyCategory (ComplexShape.up ℕ)).obj
          ((moduleDirectImageSmall B S hS p q hp hq f hf .etale).rightDerivedToHomotopyCategory.obj
            ((etaleComparisonPushforward B S hS p hp).obj
              (lqcFbcModule B E h S hS p hp F hlqc hbc))))
```

## Tag 07AK, a lemma

[Tag 07AK](https://stacks.math.columbia.edu/tag/07AK) in the Stacks Project.

**`AlgebraicGeometry.Stack.inclusionToposMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubcategorySiteKind.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubcategorySiteKind.lean#L133). The attribute's comment: “the morphism of topoi `g : Sh(𝒳'_τ) ⟶ Sh(𝒳_τ)` defined by the inclusion, whose inverse image is restriction to `𝒳'`”.

> **Stacks 07AK, the morphism of topoi.** Cocontinuity of the inclusion gives the adjoint pair
> `g^{-1} ⊣ g_*` between the topos of the subcategory site and that of the ambient site, with
> `g^{-1}` left exact: the morphism of topoi `g : Sh(𝒳'_τ) ⟶ Sh(𝒳_τ)` of the source.
>
> The sheaves take values in `Type max v w`, which is the universe in which the sheaves of sets on
> either site live.

```lean
def inclusionToposMorphism (τ : SiteKind) (hp : p.IsFiberedInGroupoids)
    (hclose : IsClosedUnderSitePullback B S hS p P τ) :
    MorphismOfTopoi
      (Sheaf (P.ι.inheritedTopology (BigFppfOver.associatedTopology B S hS p τ))
        (Type max v w))
      (Sheaf (BigFppfOver.associatedTopology B S hS p τ) (Type max v w))
```

**`AlgebraicGeometry.Stack.subsite_cohomology_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteCohomologyAtlas.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteCohomologyAtlas.lean#L238).

> **Stacks 07AK.** Let `𝒳` be an algebraic stack over `S`, let `τ` be the étale or the fppf
> topology, and let `𝒳' ⊆ 𝒳` be a full subcategory such that
>
> 1. if `x ⟶ x'` is a morphism of `𝒳` lying over a smooth (respectively flat and locally finitely
>    presented) morphism of schemes and `x'` is in `𝒳'`, then `x` is in `𝒳'` — this is
>    `AlgebraicGeometry.Stack.IsClosedUnderSitePullback`, which also pins `τ` down to one of the two
>    admissible topologies; and
> 2. there is an object `x` of `𝒳'` lying over a scheme `U` whose associated 1-morphism
>    `x : (Sch/U)_fppf ⟶ 𝒳` is smooth and surjective.
>
> Give `𝒳'` the topology whose coverings are the families of `𝒳'` that are coverings of `𝒳_τ`. Then
> the inclusion `𝒳' ⟶ 𝒳_τ` is fully faithful, continuous and cocontinuous, so it defines a morphism
> of topoi `g : Sh(𝒳'_τ) ⟶ Sh(𝒳_τ)` — `AlgebraicGeometry.Stack.inclusionToposMorphism`, whose inverse
> image is restriction to `𝒳'` — and `H^p(𝒳'_τ, g⁻¹ℱ) ≅ H^p(𝒳_τ, ℱ)` for all `p ≥ 0` and all abelian
> sheaves `ℱ` on `𝒳_τ`, where on abelian sheaves `g⁻¹` is again restriction to `𝒳'`.
>
> The isomorphism of cohomology groups is the natural isomorphism
> `AlgebraicGeometry.Stack.subsiteCohomologyIsoOfAtlas`.

```lean
theorem subsite_cohomology_comparison :
    P.ι.Full ∧ P.ι.Faithful ∧
      P.ι.IsContinuous (P.ι.inheritedTopology (BigFppfOver.associatedTopology B S hS
        𝒳.val.val.p τ)) (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p τ) ∧
      P.ι.IsCocontinuous (P.ι.inheritedTopology (BigFppfOver.associatedTopology B S hS
        𝒳.val.val.p τ)) (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p τ) ∧
      (haveI := isContinuous_ι_associatedTopology_of_isClosedUnderSitePullback B S hS
          𝒳.val.val.p P τ 𝒳.val.isFiberedInGroupoids hcl;
        Nonempty ((inclusionToposMorphism B S hS 𝒳.val.val.p P τ 𝒳.val.isFiberedInGroupoids
          hcl).inverseImage ≅ P.ι.sheafPushforwardContinuous (Type (u + 1))
            (P.ι.inheritedTopology (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p τ))
            (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p τ))) ∧
      ∀ q : ℕ,
        haveI := isContinuous_ι_associatedTopology_of_isClosedUnderSitePullback B S hS
          𝒳.val.val.p P τ 𝒳.val.isFiberedInGroupoids hcl;
        Nonempty (P.ι.sheafPushforwardContinuous AddCommGrpCat.{u + 1}
            (P.ι.inheritedTopology (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p τ))
            (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p τ) ⋙
          Sheaf.functorH.{u + 1, u + 1, u, u + 1}
            (P.ι.inheritedTopology (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p τ)) q ≅
          Sheaf.functorH.{u + 1, u + 1, u, u + 1}
            (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p τ) q)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.23, Tag 075Q](https://stacks.math.columbia.edu/tag/075Q)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
