---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.ModuleMapSituation.isoLocusRepresentation_of_isPureRelative, AlgebraicGeometry.Space.ModuleMapSituation.isoLocusRepresentation_of_hasProperSupport, AlgebraicGeometry.Space.ModuleMapSituation.exists_isOpenSubspace_isSurjectiveAt_iff
statement: formalized
proof: formalized
---

# 77.9 Flattening a map

Section 77.9 of the Stacks Project, [Tag 0CVN](https://stacks.math.columbia.edu/tag/0CVN). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CWD, a theorem

[Tag 0CWD](https://stacks.math.columbia.edu/tag/0CWD) in the Stacks Project.

**`AlgebraicGeometry.Space.ModuleMapSituation.isoLocusRepresentation_of_isPureRelative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IsoLocusClosedOfPure.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IsoLocusClosedOfPure.lean#L117). The attribute's comment: “F\_iso is represented by a closed subspace Z of the base, and Z → B is of finite presentation when 𝒢 is of finite presentation (the source's 'Z → S' is a misprint for Z → B, see the module notes)”.

> **Stacks 0CWD.**  In Situation 083F, assume (1) `f` is of finite presentation, (2) `ℱ` is of
> finite presentation, flat over `B` and pure relative to `B`, and (3) `u` is surjective.  Then
> `F_iso` is representable by a closed immersion `Z ⟶ B`: there is a closed subspace `Z` of `B`
> such that a scheme `T` over `B` lies in `F_iso` — the base change `u_T` is an isomorphism —
> exactly when its structure morphism factors through `Z`.  Moreover `Z ⟶ B` is of finite
> presentation if `𝒢` is of finite presentation.
>
> The source writes `Z ⟶ S` in the last sentence, which is false as written; its proof gives
> `Z ⟶ B`, and that is what is stated.  See the implementation notes of this file.

```lean
theorem isoLocusRepresentation_of_isPureRelative
    (D : ModuleMapSituation.{u, u} B S hS)
    (hf : IsFinitePresentation B S hS D.f.hom)
    (hFfp : SheafOfModules.IsFinitePresentationOnSite D.F)
    (hFflat : _root_.AlgebraicGeometry.Space.IsFlatOver B S hS D.X.2 D.f.hom D.F)
    (hpure : ∀ y : points B S hS D.Y.1, IsPureRelative (D.fpSourcePrePureSituation hf hFfp y))
    [Epi D.u] :
    D.IsoLocusRepresentation
```

## Tag 083N, a lemma

[Tag 083N](https://stacks.math.columbia.edu/tag/083N) in the Stacks Project.

**`AlgebraicGeometry.Space.ModuleMapSituation.isoLocusRepresentation_of_hasProperSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IsoLocusClosedProperSupport.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IsoLocusClosedProperSupport.lean#L74). The attribute's comment: “the full statement at the source's hypotheses alone: f locally of finite presentation, F locally of finite presentation and flat over B with support proper over B, u surjective; F\_iso is represented by a closed subspace of B, of finite presentation over B when G is of finite presentation”.

> **Stacks 083N.**  In Situation 083F, assume that
> 1. `f` is locally of finite presentation,
> 2. `ℱ` is locally of finite presentation and flat over `B`,
> 3. the support of `ℱ` is proper over `B`, and
> 4. `u` is surjective.
>
> Then the functor `F_iso` is an algebraic space and `F_iso ⟶ B` is a closed immersion; if `𝒢` is
> of finite presentation, then `F_iso ⟶ B` is of finite presentation.
>
> The conclusion `AlgebraicGeometry.Space.ModuleMapSituation.IsoLocusRepresentation` is the
> existence of a subfunctor `Z` of `B` which is a closed subspace (an algebraic space whose
> inclusion is a closed immersion), whose inclusion is of finite presentation when `𝒢` is of finite
> presentation, and which represents `F_iso`.  Being of finite presentation is a local condition
> for modules on a site, so `SheafOfModules.IsFinitePresentationOnSite` is the source's "locally
> of finite presentation".  The hypotheses are exactly the source's.
>
> The proof is the source's: Stacks 083M applied to the kernel inclusion `Ker(u) ⟶ ℱ`
> (`AlgebraicGeometry.Space.ModuleMapSituation.zeroLocusRepresentation_of_hasProperSupport` on
> `AlgebraicGeometry.Space.ModuleMapSituation.kernelSituation`), transported to `F_iso` by
> Stacks 0CVM and Stacks 082T
> (`AlgebraicGeometry.Space.ModuleMapSituation.isoLocusRepresentation_of_kernelSituation`).

```lean
theorem isoLocusRepresentation_of_hasProperSupport (D : ModuleMapSituation.{u, u} B S hS)
    (hf : IsLocallyOfFinitePresentation B S hS D.f.hom)
    (hFfp : SheafOfModules.IsFinitePresentationOnSite D.F)
    (hFflat : IsFlatOver B S hS D.X.property D.f.hom D.F)
    (hproper : HasProperSupport B S hS D.X.property D.Y.property D.f.hom
      (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation B S hS hf)
      ((SheafOfModules.toSheaf _).obj D.F))
    (hu : Epi D.u) :
    D.IsoLocusRepresentation
```

## Tag 09TP, a lemma

[Tag 09TP](https://stacks.math.columbia.edu/tag/09TP) in the Stacks Project.

**`AlgebraicGeometry.Space.ModuleMapSituation.exists_isOpenSubspace_isSurjectiveAt_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SurjectiveLocusOpenSubspace.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SurjectiveLocusOpenSubspace.lean#L308). References: SGA 6 XII (4.6), “partial”.

> **Stacks 09TP.** In the situation of Stacks 083F, assume that `f` is locally of finite
> presentation, that `G` is of finite type and that the support of `G` is proper over `Y`.  Then
> the locus `F_surj` on which the base change of `u` is surjective is represented by an open
> subspace of `Y`; in particular it is an algebraic space and its morphism to `Y` is an open
> immersion.
>
> The open subspace is the one of Stacks 03BZ on the complement of `|f|(Supp(Coker u))`, which is
> open because that image is closed by Stacks 0CZG, the support of the cokernel being a closed
> subset of the support of `G` and hence proper over `Y`.  The identification at a test scheme is
> `AlgebraicGeometry.Space.ModuleMapSituation.isSurjectiveAt_iff_range_pointsMap_subset`.

```lean
theorem exists_isOpenSubspace_isSurjectiveAt_iff
    (hf : IsLocallyOfFinitePresentation B S hS D.f.hom)
    (hG : SheafOfModules.IsFiniteTypeOnSite D.G)
    (hproper : HasProperSupport B S hS D.X.property D.Y.property D.f.hom
      (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation B S hS hf)
      ((SheafOfModules.toSheaf _).obj D.G)) :
    ∃ U : Subfunctor D.Y.1, IsOpenSubspace B S hS U ∧
      ∀ T : D.SchemesOver,
        D.IsSurjectiveAt (modulePullbackSystem B S hS) T ↔
          ∃ k : yoneda.obj T.left ⟶ U.toFunctor, k ≫ U.ι = T.hom.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 77.9, Tag 0CVN](https://stacks.math.columbia.edu/tag/0CVN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
