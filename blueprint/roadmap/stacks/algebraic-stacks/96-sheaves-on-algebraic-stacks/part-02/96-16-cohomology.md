---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.cohomologyOverObjectComparison
statement: formalized
proof: formalized
---

# 96.16 Cohomology

Section 96.16 of the Stacks Project, [Tag 075E](https://stacks.math.columbia.edu/tag/075E). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 075F, a lemma

[Tag 075F](https://stacks.math.columbia.edu/tag/075F) in the Stacks Project.

**`AlgebraicGeometry.Stack.cohomologyOverObjectComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ObjectCohomologyLocalizationEtale.lean, line 596](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ObjectCohomologyLocalizationEtale.lean#L596). References: SGA 4 VII (4.1), “more general”.

> **Stacks 075F.** Let `S` be a scheme, `p : 𝒳 ⥤ (Sch/S)_{fppf}` a category fibred in groupoids,
> `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, and `x` an object of `𝒳` lying over the scheme
> `U`. For every degree `n`:
>
> * for `F` an abelian sheaf on `𝒳_τ`, `H^n_τ(x, F) = H^n((Sch/U)_τ, x^{-1}F)`;
> * for `F` a sheaf of `O_𝒳`-modules on `𝒳_τ`, `H^n_τ(x, F) = H^n((Sch/U)_τ, x^{-1}F)`;
> * if `τ = étale`, then also `H^n_{étale}(x, F) = H^n(U_{étale}, F|_{U_{étale}})`, for `F` an
>   abelian sheaf and for `F` a sheaf of `O_𝒳`-modules on `𝒳_{étale}`.
>
> Each identification is a natural isomorphism of functors of `F`; they are
> `AlgebraicGeometry.Stack.cohomologyOverObjectIso`,
> `AlgebraicGeometry.Stack.moduleCohomologyOverObjectIso`,
> `AlgebraicGeometry.Stack.etaleCohomologyOverObjectIso` and
> `AlgebraicGeometry.Stack.etaleModuleCohomologyOverObjectIso`, the first two of which are stated
> there for any topology on the underlying category of schemes (coarser than the fppf topology, for
> modules).
>
> The five topologies are `B.baseTopology τ` for `τ : AlgebraicGeometry.SiteKind`. Cohomology over
> `x` is the cohomology of the localized site `𝒳_τ/x` of the restriction of `F` (Stacks 03F3); the
> cohomology of a sheaf of modules is computed in the category of sheaves of modules, as `Ext` out
> of the structure sheaf; `(Sch/U)_τ` is the big `τ`-site of `U`, identified with `𝒳_τ/x` by the
> localization equivalence of Stacks 06W0, compatibly with the structure sheaves by Stacks 06W9;
> `x^{-1}F` is `AlgebraicGeometry.Stack.objectInverseImage`, resp.
> `AlgebraicGeometry.Stack.objectModuleInverseImage`; `U_{étale}` is the small étale site of `U`
> for the big étale site carried by `B` (Stacks 03FF); and `F|_{U_{étale}}` is the restriction of
> Stacks 06W1, `AlgebraicGeometry.Stack.objectSmallEtaleRestriction`, resp.
> `AlgebraicGeometry.Stack.objectSmallEtaleModuleRestriction`. Abelian sheaves and sheaves of
> modules have their sections in the universe `max v w (u + 1)` containing both sites, as explained
> in the module docstring of
> `StacksFrontier/AlgebraicGeometry/Stacks/ObjectCohomologyLocalization.lean`.

```lean
def cohomologyOverObjectComparison (τ : SiteKind) (n : ℕ) :
    (
      haveI := Stacks.Cohomology.SiteModules.site_hasSheafify_addCommGrp.{max v w, w, u + 1}
        (J := (associatedTopology B S hS p (B.baseTopology τ)).over x)
      haveI := Stacks.Cohomology.SiteModules.site_hasSheafify_addCommGrp.{u + 1, u, max v w}
        (J := (B.baseTopology τ).over (p.obj x).left)
      haveI := Stacks.Cohomology.SiteModules.site_hasExt_addCommGrp.{max v w, w, u + 1}
        (J := (associatedTopology B S hS p (B.baseTopology τ)).over x)
      haveI := Stacks.Cohomology.SiteModules.site_hasExt_addCommGrp.{u + 1, u, max v w}
        (J := (B.baseTopology τ).over (p.obj x).left)
      haveI := isDenseSubsite_overPost B S hS p hp (B.baseTopology τ) x
      (associatedTopology B S hS p (B.baseTopology τ)).overPullback
          AddCommGrpCat.{max v w (u + 1)} x ⋙
          Sheaf.functorH ((associatedTopology B S hS p (B.baseTopology τ)).over x) n ≅
        objectInverseImage B S hS p (B.baseTopology τ) x ⋙
          Sheaf.functorH ((B.baseTopology τ).over (p.obj x).left) n) ×
    (
      SheafOfModules.overFunctor (ringStructureSheaf.{u, v, w, u + 1} B S hS p hp
          (B.baseTopology τ) (B.baseTopology_le_topology τ)) x ⋙
          Stacks.Cohomology.BiggerSiteModules.moduleFunctorH.{u + 1, w, max v w}
            ((associatedTopology B S hS p (B.baseTopology τ)).over x)
            ((ringStructureSheaf.{u, v, w, u + 1} B S hS p hp (B.baseTopology τ)
              (B.baseTopology_le_topology τ)).over x) n ≅
        objectModuleInverseImage B S hS p hp (B.baseTopology τ) x
            (B.baseTopology_le_topology τ) ⋙
          Stacks.Cohomology.BiggerSiteModules.moduleFunctorH.{max v w, u, u + 1}
            ((B.baseTopology τ).over (p.obj x).left)
            (baseRingStructureSheafLift.{u, v, w} B (B.baseTopology τ)
              (B.baseTopology_le_topology τ) (p.obj x).left.1 (p.obj x).left.2) n) ×
    (τ = .etale →
      (
        haveI := Stacks.Cohomology.SiteModules.site_hasSheafify_addCommGrp.{max v w, w, u + 1}
          (J := (associatedTopology B S hS p B.etaleTopology).over x)
        haveI := Stacks.Cohomology.SiteModules.site_hasSheafify_addCommGrp.{u + 1, u, max v w}
          (J := SmallEtale.topology B.toBigEtaleSite (p.obj x).left.1
            (toBigEtaleSite_contains_left B S hS p x))
        haveI := Stacks.Cohomology.SiteModules.site_hasExt_addCommGrp.{max v w, w, u + 1}
          (J := (associatedTopology B S hS p B.etaleTopology).over x)
        haveI := Stacks.Cohomology.SiteModules.site_hasExt_addCommGrp.{u + 1, u, max v w}
          (J := SmallEtale.topology B.toBigEtaleSite (p.obj x).left.1
            (toBigEtaleSite_contains_left B S hS p x))
        (associatedTopology B S hS p B.etaleTopology).overPullback
            AddCommGrpCat.{max v w (u + 1)} x ⋙
            Sheaf.functorH ((associatedTopology B S hS p B.etaleTopology).over x) n ≅
          objectSmallEtaleRestriction B S hS p hp x ⋙
            Sheaf.functorH (SmallEtale.topology B.toBigEtaleSite (p.obj x).left.1
              (toBigEtaleSite_contains_left B S hS p x)) n) ×
      (
        SheafOfModules.overFunctor (ringStructureSheaf.{u, v, w, u + 1} B S hS p hp
            B.etaleTopology (etaleTopology_le_topology B)) x ⋙
            Stacks.Cohomology.BiggerSiteModules.moduleFunctorH.{u + 1, w, max v w}
              ((associatedTopology B S hS p B.etaleTopology).over x)
              ((ringStructureSheaf.{u, v, w, u + 1} B S hS p hp B.etaleTopology
                (etaleTopology_le_topology B)).over x) n ≅
          objectSmallEtaleModuleRestriction B S hS p hp x ⋙
            Stacks.Cohomology.BiggerSiteModules.moduleFunctorH.{max v w, u, u + 1}
              (SmallEtale.topology B.toBigEtaleSite (p.obj x).left.1
                (toBigEtaleSite_contains_left B S hS p x))
              (objectSmallEtaleRing B S hS p x) n))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.16, Tag 075E](https://stacks.math.columbia.edu/tag/075E)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
