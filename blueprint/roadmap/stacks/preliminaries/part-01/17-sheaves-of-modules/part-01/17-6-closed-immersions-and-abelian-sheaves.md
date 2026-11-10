---
declaration: section
origin: cited
lean: Stacks.ClosedImmersion.exactFunctor_closedInclusionPushforward, Stacks.ClosedImmersion.preservesFiniteLimits_closedInclusionPushforward, Stacks.ClosedImmersion.preservesFiniteColimits_closedInclusionPushforward, Stacks.ClosedImmersion.essImage_closedInclusionPushforward_iff_forall_stalk_isZero, Stacks.ClosedImmersion.essImage_closedInclusionPushforward_iff_support_subset, closedInclusion_pushforward_faithful, closedInclusion_pushforward_full, ClosedImmersionSheaves.sheaf_pullback_pushforward_counit_isIso
statement: formalized
proof: formalized
---

# 17.6 Closed immersions and abelian sheaves

Section 17.6 of the Stacks Project, [Tag 01AW](https://stacks.math.columbia.edu/tag/01AW). 3 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01AX, a lemma

[Tag 01AX](https://stacks.math.columbia.edu/tag/01AX) in the Stacks Project.

**`Stacks.ClosedImmersion.exactFunctor_closedInclusionPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/AbelianExact.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/AbelianExact.lean#L145). The attribute's comment: “exactness”.

> **Stacks 01AX, exactness.** Pushforward of sheaves of abelian groups along a closed
> embedding `i : Z ⟶ X` is an exact functor `Ab(Z) ⥤ Ab(X)`.
>
> Exactness is detected on stalks. Over a point of the image of `i` the stalk of `i_* 𝒜` is the
> stalk of `𝒜`, naturally in `𝒜`, because a closed embedding is inducing; over a point off the
> image the stalk of `i_* 𝒜` vanishes.

```lean
theorem exactFunctor_closedInclusionPushforward (hi : IsClosedEmbedding i.hom) :
    exactFunctor (TopCat.Sheaf AddCommGrpCat.{u} Z) (TopCat.Sheaf AddCommGrpCat.{u} X)
      (closedInclusionPushforward Z X i)
```

**`Stacks.ClosedImmersion.preservesFiniteLimits_closedInclusionPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/AbelianExact.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/AbelianExact.lean#L163). The attribute's comment: “exactness: left exactness”.

> **Stacks 01AX, exactness.** Pushforward along a closed embedding preserves finite
> limits.

```lean
theorem preservesFiniteLimits_closedInclusionPushforward (hi : IsClosedEmbedding i.hom) :
    PreservesFiniteLimits (closedInclusionPushforward Z X i)
```

**`Stacks.ClosedImmersion.preservesFiniteColimits_closedInclusionPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/AbelianExact.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/AbelianExact.lean#L170). The attribute's comment: “exactness: right exactness”.

> **Stacks 01AX, exactness.** Pushforward along a closed embedding preserves finite
> colimits.

```lean
theorem preservesFiniteColimits_closedInclusionPushforward (hi : IsClosedEmbedding i.hom) :
    PreservesFiniteColimits (closedInclusionPushforward Z X i)
```

**`Stacks.ClosedImmersion.essImage_closedInclusionPushforward_iff_forall_stalk_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/AbelianExact.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/AbelianExact.lean#L210). The attribute's comment: “essential image”. References: EGA 0 (4.2.5), “Ψ_*M is zero outside X”.

> **Stacks 01AX, essential image.** A sheaf `G` of abelian groups on `X` is in the essential
> image of pushforward along the closed embedding `i : Z ⟶ X` if and only if the stalk of `G`
> vanishes at every point outside the image of `i`.
>
> The forward direction is Stacks 00AG
> (`closedInclusion_pushforward_essImage_stalk_isZero`). For the converse the preimage is the
> sheafification `ℱ` of `i^{-1} G`; the canonical morphism `η : G ⟶ i_* ℱ` is an isomorphism
> because it is one on every stalk: off the image of `i` both stalks vanish, and at `i z` the
> composite of the stalk of `η` with the isomorphism `(i_* ℱ)_{i z} ⟶ ℱ_z` is an isomorphism by
> `stalkFunctor_map_unit_comp_stalkPushforward` together with
> `TopCat.Presheaf.stalkFunctor_map_unit_toSheafify_isIso`.

```lean
theorem essImage_closedInclusionPushforward_iff_forall_stalk_isZero
    (hi : IsClosedEmbedding i.hom) (G : TopCat.Sheaf AddCommGrpCat.{u} X) :
    (closedInclusionPushforward Z X i).essImage G ↔
      ∀ x : X, x ∉ Set.range i.hom → IsZero (G.presheaf.stalk x)
```

**`Stacks.ClosedImmersion.essImage_closedInclusionPushforward_iff_support_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/AbelianExact.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/AbelianExact.lean#L248). The attribute's comment: “essential image, in terms of the support”. References: EGA 0 (4.2.5), “Ψ_*M is zero outside X”.

> **Stacks 01AX, essential image.** The essential image of pushforward along a closed
> embedding `i : Z ⟶ X` consists exactly of the sheaves of abelian groups whose support is
> contained in the image of `i`.
>
> This is the source's phrasing of
> `essImage_closedInclusionPushforward_iff_forall_stalk_isZero`, since the support of an abelian
> sheaf is by definition the set of points with nonzero stalk.

```lean
theorem essImage_closedInclusionPushforward_iff_support_subset
    (hi : IsClosedEmbedding i.hom) (G : TopCat.Sheaf AddCommGrpCat.{u} X) :
    (closedInclusionPushforward Z X i).essImage G ↔
      Stacks.AbelianSheaf.support G ⊆ Set.range i.hom
```

Declarations registered for the tag:

- [`closedInclusion_pushforward_faithful`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/Abelian.lean#L63), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/ClosedImmersion/AbelianExact.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/AbelianExact.lean#L261) (StacksFrontier): “fully faithful: faithfulness”.
- [`closedInclusion_pushforward_full`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/Abelian.lean#L71), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/ClosedImmersion/AbelianExact.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/AbelianExact.lean#L262) (StacksFrontier): “fully faithful: fullness”.
- [`ClosedImmersionSheaves.sheaf_pullback_pushforward_counit_isIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/Pushforward.lean#L202), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/ClosedImmersion/AbelianExact.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/AbelianExact.lean#L263) (StacksFrontier): “`i^{-1}` is a left inverse to `i_*`: the counit of `i^{-1} ⊣ i_*` is an isomorphism”.

## Tag 01AY, a remark

[Tag 01AY](https://stacks.math.columbia.edu/tag/01AY) in the Stacks Project.

**`ClosedImmersionSheaves.supportedSectionsSheaf_mem_closedInclusionPushforward_essImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/SupportedSectionsOnClosed.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/SupportedSectionsOnClosed.lean#L105). The attribute's comment: “realization on Z”.

> **Stacks 01AY.** For a closed subset `Z`, the sheaf of sections supported on `Z` is, up
> to isomorphism, pushed forward from an abelian sheaf on `Z`.

```lean
theorem supportedSectionsSheaf_mem_closedInclusionPushforward_essImage
    {X : TopCat.{u}} (Z : Set X) (hZ : IsClosed Z) (F : X.Sheaf AddCommGrpCat.{u}) :
    (closedInclusionPushforward (TopCat.of Z) X (closedSubsetInclusion Z)).essImage
      (supportedSectionsSheaf Z F)
```

**`ClosedImmersionSheaves.supportedSectionsSheaf_maximal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/SupportedSectionsOnClosed.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/SupportedSectionsOnClosed.lean#L184). The attribute's comment: “largest abelian subsheaf supported in Z”.

> **Stacks 01AY.** The sheaf of sections supported on `Z` is the largest abelian subsheaf
> of `F` whose support is contained in `Z`: every abelian subsheaf of `F` supported in `Z`
> factors through it, and the factorisation is unique.

```lean
theorem supportedSectionsSheaf_maximal {X : TopCat.{u}} (Z : Set X)
    {A F : X.Sheaf AddCommGrpCat.{u}} (f : A ⟶ F) [Mono f]
    (hA : Stacks.AbelianSheaf.support A ⊆ Z) :
    ∃! g : A ⟶ supportedSectionsSheaf Z F, g ≫ supportedSectionsSheafι Z F = f
```

**`ClosedImmersionSheaves.supportedSectionsOnClosedFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/SupportedSectionsOnClosed.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/SupportedSectionsOnClosed.lean#L287). The attribute's comment: “realization on Z”.

> The supported-sections functor, regarded as taking values in abelian sheaves on the
> closed subspace `Z`.

```lean
noncomputable def supportedSectionsOnClosedFunctor {X : TopCat.{u}}
    (Z : Set X) (hZ : IsClosed Z) :
    X.Sheaf AddCommGrpCat.{u} ⥤ (TopCat.of Z).Sheaf AddCommGrpCat.{u}
```

**`ClosedImmersionSheaves.supportedSectionsOnClosedFunctor_comp_pushforward_iso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/SupportedSectionsOnClosed.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/SupportedSectionsOnClosed.lean#L301). The attribute's comment: “realization on Z”.

> Pushforward of the realization on the closed subspace is naturally isomorphic to the
> sheaf of supported sections.

```lean
noncomputable def supportedSectionsOnClosedFunctor_comp_pushforward_iso
    {X : TopCat.{u}} (Z : Set X) (hZ : IsClosed Z) :
    supportedSectionsOnClosedFunctor Z hZ ⋙
        closedInclusionPushforward (TopCat.of Z) X (closedSubsetInclusion Z) ≅
      supportedSectionsFunctor Z
```

**`ClosedImmersionSheaves.supportedSectionsOnClosedFunctor_leftExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/SupportedSectionsOnClosed.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/SupportedSectionsOnClosed.lean#L318). The attribute's comment: “left exact functor Ab(X) → Ab(Z)”. References: SGA 4 V (6.3), “special case”.

> **Stacks 01AY.** Taking sections supported on a closed subset, viewed as an abelian sheaf
> on that subset, is left exact.

```lean
theorem supportedSectionsOnClosedFunctor_leftExact {X : TopCat.{u}}
    (Z : Set X) (hZ : IsClosed Z) :
    leftExactFunctor (X.Sheaf AddCommGrpCat.{u})
      ((TopCat.of Z).Sheaf AddCommGrpCat.{u})
      (supportedSectionsOnClosedFunctor Z hZ)
```

**`AlgebraicGeometry.SheafOfModules.supportedSectionsSubsheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Support.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Support.lean#L196). The attribute's comment: “supported_sections_subsheaf”. References: SGA 2 XIV (1.0), “sheaf Γ_Y(F)”.

> The abelian subsheaf of `F` consisting of the local sections supported on
> `Z`. It is bundled together with its canonical inclusion into `F`.

```lean
public noncomputable def supportedSectionsSubsheaf (Z : Set X)
    (F : X.Sheaf AddCommGrpCat.{u}) : MonoOver F
```

## Tag 01AZ, a lemma

[Tag 01AZ](https://stacks.math.columbia.edu/tag/01AZ) in the Stacks Project.

**`ClosedImmersionSheaves.closedInclusionPushforward_supportedSectionsOnClosedFunctor_adjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/SupportedSectionsOnClosed.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/SupportedSectionsOnClosed.lean#L345). The attribute's comment: “adjunction”.

> **Stacks 01AZ, adjunction.** Pushforward from a closed subset is left adjoint to the
> functor of sections supported on that subset.

```lean
noncomputable def closedInclusionPushforward_supportedSectionsOnClosedFunctor_adjunction
    {X : TopCat.{u}} (Z : Set X) (hZ : IsClosed Z) :
    closedInclusionPushforward (TopCat.of Z) X (closedSubsetInclusion Z) ⊣
      supportedSectionsOnClosedFunctor Z hZ
```

**`ClosedImmersionSheaves.closedInclusionPushforward_preservesColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/SupportedSectionsOnClosed.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/SupportedSectionsOnClosed.lean#L412). The attribute's comment: “colimits”.

> **Stacks 01AZ, colimits.** Pushforward of abelian sheaves along a closed inclusion
> preserves arbitrary colimits.

```lean
theorem closedInclusionPushforward_preservesColimits
    {X : TopCat.{u}} (Z : Set X) (hZ : IsClosed Z) :
    PreservesColimits
      (closedInclusionPushforward (TopCat.of Z) X (closedSubsetInclusion Z))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.6, Tag 01AW](https://stacks.math.columbia.edu/tag/01AW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
