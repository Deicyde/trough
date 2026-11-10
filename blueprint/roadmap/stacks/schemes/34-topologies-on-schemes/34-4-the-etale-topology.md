---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.etalePrecoverage, AlgebraicGeometry.Scheme.zariskiPrecoverage_le_etalePrecoverage, AlgebraicGeometry.Scheme.etalePretopology, AlgebraicGeometry.exists_finite_affine_etaleCovering_le_of_mem_etaleTopology, exists_finite_affine_etale_refinement, AlgebraicGeometry.IsStandardEtaleCovering, AlgebraicGeometry.BigEtaleSite, AlgebraicGeometry.Scheme.etaleTopology
statement: formalized
proof: formalized
---

# 34.4 The étale topology

Section 34.4 of the Stacks Project, [Tag 0214](https://stacks.math.columbia.edu/tag/0214). 20 tags here are carried by 78 declarations of the repository (all in StacksFrontier) and 14 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0215, a definition

[Tag 0215](https://stacks.math.columbia.edu/tag/0215) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.etalePrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.etalePrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch34.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch34.lean#L21) (StacksFrontier). References: SGA 4 VII (1.2); SGA 4 XVII (0.10), “partial”.

## Tag 0216, a lemma

[Tag 0216](https://stacks.math.columbia.edu/tag/0216) in the Stacks Project.

**`AlgebraicGeometry.Scheme.zariskiPrecoverage_le_etalePrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SmoothAndStandardEtaleCoverings.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/SmoothAndStandardEtaleCoverings.lean#L67).

> Every Zariski covering is an étale covering.

```lean
public theorem zariskiPrecoverage_le_etalePrecoverage :
    zariskiPrecoverage.{u} ≤ etalePrecoverage
```

## Tag 0217, a lemma

[Tag 0217](https://stacks.math.columbia.edu/tag/0217) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.etalePretopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.etalePretopology#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch34.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch34.lean#L22) (StacksFrontier). References: SGA 4 VII (1.2); SGA 4 VII (1.3); SGA 4 XVII (0.10), “étale pretopology on Sch”.

## Tag 0218, a lemma

[Tag 0218](https://stacks.math.columbia.edu/tag/0218) in the Stacks Project.

**`AlgebraicGeometry.exists_finite_affine_etaleCovering_le_of_mem_etaleTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenEtaleAffineRefinement.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/ChosenEtaleAffineRefinement.lean#L69). The attribute's comment: “for the étale subcollection of a big fppf site, inside a covering sieve”.

> **Stacks 0218 for the étale subcollection of a big fppf site.** A covering sieve of the big
> étale topology `AlgebraicGeometry.etaleTopology B` at an object `X` whose underlying scheme is
> affine contains a selected étale covering family of `X` which is finite and whose members again
> have affine underlying scheme.
>
> This is the étale analogue of `AlgebraicGeometry.exists_standardFppf_refinement` (Stacks 021P) on
> the same category, and it is proved by reading the étale subcollection as the big étale site
> `AlgebraicGeometry.BigFppfSite.toBigEtaleSite` and applying
> `AlgebraicGeometry.BigEtaleSite.exists_finite_affine_refinement` there; see the module
> documentation.

```lean
theorem exists_finite_affine_etaleCovering_le_of_mem_etaleTopology (B : BigFppfSite.{u})
    {X : B.Schemes} (hX : IsAffine (B.inclusion.obj X))
    {R : Sieve X} (hR : R ∈ etaleTopology B X) :
    ∃ E : PreZeroHypercover.{u + 1} X, etaleCovering B ⟨X, E⟩ ∧ Finite E.I₀ ∧
      (∀ i, IsAffine (B.inclusion.obj (E.X i))) ∧ E.presieve₀ ≤ R.arrows
```

Declarations registered for the tag:

- [`exists_finite_affine_etale_refinement`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=exists_finite_affine_etale_refinement#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAffineHypercoverRefinement.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAffineHypercoverRefinement.lean#L106) (StacksFrontier).

## Tag 0219, a definition

[Tag 0219](https://stacks.math.columbia.edu/tag/0219) in the Stacks Project.

**`AlgebraicGeometry.IsStandardEtaleCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SmoothAndStandardEtaleCoverings.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/SmoothAndStandardEtaleCoverings.lean#L50).

> A standard étale covering of an affine scheme `T`: a finite family of étale morphisms
> `f i : U i ⟶ T` with affine sources whose images cover `T`, that is, the étale case of
> `AlgebraicGeometry.IsStandardCovering`.

```lean
public abbrev IsStandardEtaleCovering {T : Scheme.{u}} [IsAffine T] {I : Type v}
    (U : I → Scheme.{u}) (f : ∀ i, U i ⟶ T) : Prop
```

## Tag 021A, a definition

[Tag 021A](https://stacks.math.columbia.edu/tag/021A) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSite`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale.lean#L80).

> A big étale site: a size-bounded full category of schemes and a chosen bounded class of étale
> covering families on it, containing an initial set of schemes and an initial set of étale
> coverings.

```lean
public structure BigEtaleSite
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.etaleTopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.etaleTopology#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Etale.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale.lean#L182) (StacksFrontier). References: SGA 3 IV (6.3); SGA 4 VII (1.2); SGA 4 VII (1.3); SGA 4 XVII (0.10), “étale topology on Sch”.

## Tag 03WW, a lemma

[Tag 03WW](https://stacks.math.columbia.edu/tag/03WW) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSite.exists_covering_refining_etale_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigSiteCoverings.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigSiteCoverings.lean#L82). The attribute's comment: “etale_refinement”.

> **Stacks Project, Tag 03WW.** Every étale covering family of an object of a big étale
> site, formed in the ambient category of schemes, is refined by a covering family internal to
> the site.

```lean
public theorem exists_covering_refining_etale_cover
    (B : AlgebraicGeometry.BigEtaleSite.{u}) {T : B.Scheme}
    (𝒰 : PreZeroHypercover.{u + 1} (B.inclusion.obj T))
    (h𝒰 : 𝒰.presieve₀ ∈ Scheme.etalePrecoverage (B.inclusion.obj T)) :
    ∃ 𝒱 : PreZeroHypercover.{u + 1} T,
      B.IsCovering ⟨T, 𝒱⟩ ∧ Nonempty ((𝒱.map B.inclusion).Hom 𝒰)
```

**`AlgebraicGeometry.BigEtaleSite.exists_isCovering_tautologicallyEquivalent_affineCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigSiteCoverings.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigSiteCoverings.lean#L166). The attribute's comment: “standard_etale_equivalence”.

> **Stacks Project, Tag 03WW.** A standard étale covering of an object of a big étale
> site is tautologically equivalent to a covering belonging to that site.

```lean
public theorem exists_isCovering_tautologicallyEquivalent_affineCover
    (B : AlgebraicGeometry.BigEtaleSite.{u}) (T : B.Scheme)
    [IsAffine (B.inclusion.obj T)]
    (U : (B.inclusion.obj T).AffineCover.{u + 1} @Etale) [Finite U.I₀] :
    ∃ V : PreZeroHypercover.{u + 1} T,
      B.IsCovering ⟨T, V⟩ ∧
        PreZeroHypercover.TautologicallyEquivalent U.cover.toPreZeroHypercover
          (V.map B.inclusion)
```

**`AlgebraicGeometry.BigEtaleSite.exists_isCovering_tautologicallyEquivalent_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigSiteCoverings.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigSiteCoverings.lean#L192). The attribute's comment: “zariski_equivalence”.

> **Stacks Project, Tag 03WW.** A Zariski covering of an object of a big étale site is
> tautologically equivalent to a covering belonging to that site.

```lean
public theorem exists_isCovering_tautologicallyEquivalent_openCover
    (B : AlgebraicGeometry.BigEtaleSite.{u}) (T : B.Scheme)
    (U : (B.inclusion.obj T).OpenCover.{u + 1}) :
    ∃ V : PreZeroHypercover.{u + 1} T,
      B.IsCovering ⟨T, V⟩ ∧
        PreZeroHypercover.TautologicallyEquivalent U.toPreZeroHypercover
          (V.map B.inclusion)
```

## Tag 021B, a definition

[Tag 021B](https://stacks.math.columbia.edu/tag/021B) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L73). The attribute's comment: “part (1), category”. References: SGA 4 XVII (0.10), “big étale site”.

> **Stacks 021B, part (1).** The underlying category of the big étale site of `S` is the
> slice of the chosen big étale category over `S`.

```lean
public abbrev BigEtaleOver
```

**`AlgebraicGeometry.BigEtaleOver.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L88). The attribute's comment: “part (1), coverings”. References: SGA 4 XVII (0.10), “big étale site”.

> **Stacks 021B, part (1).** A family in the slice is covering precisely when its underlying
> family is a covering in the chosen big étale site.

```lean
public abbrev IsCovering (E : Covering (BigEtaleOver B S hS)) : Prop
```

**`AlgebraicGeometry.SmallEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L132). The attribute's comment: “part (2), category”.

> **Stacks 021B, part (2).** The small étale category of `S` is the full subcategory of the
> big étale category over `S` consisting of objects étale over `S`.

```lean
public abbrev SmallEtale
```

**`AlgebraicGeometry.SmallEtale.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L153). The attribute's comment: “part (2), coverings”.

> **Stacks 021B, part (2).** A family in the small étale category is covering when its
> image in the big étale category over `S` is covering.

```lean
public abbrev IsCovering (E : Covering (SmallEtale B S hS)) : Prop
```

**`AlgebraicGeometry.BigAffineEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L179). The attribute's comment: “part (3), category”.

> **Stacks 021B, part (3).** The big affine étale category over `S` is the full subcategory
> of the big étale category over `S` consisting of affine source schemes.

```lean
public abbrev BigAffineEtale
```

**`AlgebraicGeometry.BigAffineEtale.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L200). The attribute's comment: “part (3), coverings”.

> **Stacks 021B, part (3).** A family in the big affine étale category is covering when its
> image in the big étale category over `S` is a standard étale covering.

```lean
public abbrev IsCovering (E : Covering (BigAffineEtale B S hS)) : Prop
```

**`AlgebraicGeometry.SmallAffineEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L231). The attribute's comment: “part (4), category”.

> **Stacks 021B, part (4).** The small affine étale category of `S` is the full subcategory
> of the small étale category consisting of affine schemes.

```lean
public abbrev SmallAffineEtale
```

**`AlgebraicGeometry.SmallAffineEtale.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Sites.lean#L253). The attribute's comment: “part (4), coverings”.

> **Stacks 021B, part (4).** A family in the small affine étale category is covering when
> its image in the small étale category is covering and it is finite (hence standard étale,
> since its source objects are affine).

```lean
public abbrev IsCovering (E : Covering (SmallAffineEtale B S hS)) : Prop
```

## Tag 021C, a lemma

[Tag 021C](https://stacks.math.columbia.edu/tag/021C) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.isSite`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SiteAxioms.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SiteAxioms.lean#L70). The attribute's comment: “small_etale_site”.

> **Stacks 021C, small étale site.** The étale covering families on the
> small étale category of a scheme satisfy the axioms of a site.

```lean
public lemma SmallEtale.isSite (B : AlgebraicGeometry.BigEtaleSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) : IsSite (SmallEtale.IsCovering B S hS)
```

**`AlgebraicGeometry.BigAffineEtale.isSite`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SiteAxioms.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SiteAxioms.lean#L111). The attribute's comment: “big_affine_etale_site”.

> **Stacks 021C, big affine étale site.** The standard étale covering families of
> affine objects over `S` satisfy the site axioms.

```lean
public lemma BigAffineEtale.isSite (B : AlgebraicGeometry.BigEtaleSite.{u})
    (S : Scheme.{u})
    (hS : B.Contains S) : IsSite (BigAffineEtale.IsCovering B S hS)
```

**`AlgebraicGeometry.SmallAffineEtale.isSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SiteAxioms.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SiteAxioms.lean#L177). The attribute's comment: “small_affine_etale_site”.

> **Stacks 021C, small affine étale site.** The standard étale covering families on
> the small affine étale category of a scheme satisfy the axioms of a site.

```lean
public theorem SmallAffineEtale.isSite (B : AlgebraicGeometry.BigEtaleSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) :
    IsSite (SmallAffineEtale.IsCovering B S hS)
```

## Tag 021D, a lemma

[Tag 021D](https://stacks.math.columbia.edu/tag/021D) in the Stacks Project.

**`AlgebraicGeometry.hasPullbacks_bigEtaleSite`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean#L75). The attribute's comment: “fibre products in the big étale site”.

> The underlying category of a big étale site admits fibre products.

```lean
public instance hasPullbacks_bigEtaleSite : HasPullbacks B.Scheme
```

**`AlgebraicGeometry.hasPullbacks_smallEtale`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean#L102). The attribute's comment: “fibre products in the small étale site”.

> The small étale category of `S` admits fibre products.

```lean
public instance hasPullbacks_smallEtale :
    HasPullbacks (SmallEtale B S hS)
```

**`AlgebraicGeometry.preservesPullbacks_smallEtaleToScheme`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean#L118). The attribute's comment: “preservation by the small étale functor to schemes”.

> The canonical functor from the small étale category of `S` to schemes preserves fibre
> products.

```lean
public instance preservesPullbacks_smallEtaleToScheme :
    PreservesLimitsOfShape WalkingCospan (SmallEtale.toScheme B S hS)
```

**`AlgebraicGeometry.hasPullbacks_bigAffineEtale`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean#L129). The attribute's comment: “fibre products in the big affine étale site”.

> The category of affine objects in the big étale category over `S` admits fibre
> products.

```lean
public instance hasPullbacks_bigAffineEtale :
    HasPullbacks (BigAffineEtale B S hS)
```

**`AlgebraicGeometry.hasPullbacks_smallAffineEtale`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean#L139). The attribute's comment: “fibre products in the affine small étale site”.

> The affine small étale category of `S` admits fibre products.

```lean
public instance hasPullbacks_smallAffineEtale :
    HasPullbacks (SmallAffineEtale B S hS)
```

**`AlgebraicGeometry.preservesPullbacks_bigEtaleSiteInclusion`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean#L146). The attribute's comment: “preservation by the big étale site inclusion”.

> The inclusion of a big étale site's underlying category into schemes preserves fibre
> products.

```lean
public instance preservesPullbacks_bigEtaleSiteInclusion :
    PreservesLimitsOfShape WalkingCospan B.inclusion
```

**`AlgebraicGeometry.preservesPullbacks_bigAffineEtaleToScheme`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean#L157). The attribute's comment: “preservation by the big affine étale functor to schemes”.

> The canonical functor from affine objects over `S` to schemes preserves fibre products.

```lean
public instance preservesPullbacks_bigAffineEtaleToScheme :
    PreservesLimitsOfShape WalkingCospan (BigAffineEtale.toScheme B S hS)
```

**`AlgebraicGeometry.preservesPullbacks_smallAffineEtaleToScheme`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean#L164). The attribute's comment: “preservation by the affine small étale functor to schemes”.

> The canonical functor from the affine small étale category of `S` to schemes preserves
> fibre products.

```lean
public instance preservesPullbacks_smallAffineEtaleToScheme :
    PreservesLimitsOfShape WalkingCospan
      (SmallAffineEtale.toScheme B S hS)
```

**`AlgebraicGeometry.SmallEtale.finalIsTerminal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean#L180). The attribute's comment: “the final object of the small étale site”.

> The object `S / S` is final in the small étale category of `S`.

```lean
public noncomputable def SmallEtale.finalIsTerminal :
    IsTerminal (SmallEtale.final B S hS)
```

Declarations registered for the tag:

- [`CategoryTheory.Over.instHasPullbacks`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.instHasPullbacks#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean#L97) (StacksFrontier): “fibre products in the big étale slice”.
- [`CategoryTheory.Over.preservesLimitsOfShape_forget_of_isConnected`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.preservesLimitsOfShape_forget_of_isConnected#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean#L149) (StacksFrontier): “preservation by the big étale slice forgetful functor”. References: SGA 4 IV (5.10), “more general”; SGA 4 IV (5.3), “partial”.
- [`CategoryTheory.Limits.comp_preservesLimitsOfShape`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.comp_preservesLimitsOfShape#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean#L152) (StacksFrontier): “preservation under composition for the big étale slice functor”.
- [`CategoryTheory.Over.mkIdTerminal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.mkIdTerminal#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean#L169) (StacksFrontier): “the final object of the big étale slice”. References: EGA 0 (8.1.10), “more general”; SGA 3 I (1.3); SGA 4 IV (5.11.1), “terminal object (X”.

## Tag 021E, a lemma

[Tag 021E](https://stacks.math.columbia.edu/tag/021E) in the Stacks Project.

**`AlgebraicGeometry.BigAffineEtale.inclusion_isSpecialCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/AffineDenseSubsite.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/AffineDenseSubsite.lean#L359).

> **Stacks 021E.** The inclusion of the big affine étale site over a scheme
> into its big étale site is special cocontinuous. Its dense-subsite component
> gives the induced equivalence of topoi.

```lean
public theorem BigAffineEtale.inclusion_isSpecialCocontinuous
    (B : AlgebraicGeometry.BigEtaleSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) :
    IsSpecialCocontinuous
      (BigAffineEtale.topology B S hS)
      (BigEtaleOver.topology B S hS)
      (BigAffineEtale.inclusion B S hS)
```

## Tag 04HR, a lemma

[Tag 04HR](https://stacks.math.columbia.edu/tag/04HR) in the Stacks Project.

**`AlgebraicGeometry.SmallAffineEtale.sheafEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/SmallEtaleAffineSheafEquiv.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/SmallEtaleAffineSheafEquiv.lean#L67). The attribute's comment: “the induced equivalence of topoi `Sh(S_{affine,étale}) ≌ Sh(S_étale)`, for sheaves of sets with values in `Type (u + 1)`”.

> **Stacks 04HR on sheaves of sets.** Restriction along the inclusion of the small affine étale
> site of `S` into its small étale site is an equivalence of categories of sheaves of sets with
> values in `Type (u + 1)`. No affineness of `S` is needed.

```lean
public noncomputable def sheafEquiv :
    Sheaf (topology B S hS) (Type (u + 1)) ≌
      Sheaf (SmallEtale.topology B S hS) (Type (u + 1))
```

**`AlgebraicGeometry.SmallAffineEtale.inclusion_isSpecialCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/SmallEtale.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/SmallEtale.lean#L372).

> The inclusion of the small affine étale site of a scheme into its small étale site is a special
> cocontinuous functor.

```lean
public theorem SmallAffineEtale.inclusion_isSpecialCocontinuous
    (B : AlgebraicGeometry.BigEtaleSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) :
    IsSpecialCocontinuous
      (AlgebraicGeometry.SmallAffineEtale.topology B S hS)
      (AlgebraicGeometry.SmallEtale.topology B S hS)
      (AlgebraicGeometry.SmallAffineEtale.inclusion B S hS)
```

## Tag 021F, a lemma

[Tag 021F](https://stacks.math.columbia.edu/tag/021F) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleToBigEtaleToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedToposIf.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedToposIf.lean#L197). The attribute's comment: “the morphism of topoi, at the universe of the structure rings”.

> **Stacks 021F at the universe of the structure rings.**  The morphism of topoi
> `i_f : \mathrm{Sh}(T_\etale) ⟶ \mathrm{Sh}((\Sch/S)_\etale)` on sheaves of sets in `Type u`.

```lean
public noncomputable def smallEtaleToBigEtaleToposHom :
    MorphismOfTopoi (Sheaf (SmallEtale.topology B T.obj T.property) (Type u))
      (Sheaf (BigEtaleOver.topology B S.obj S.property) (Type u))
```

**`AlgebraicGeometry.smallEtaleToBigEtaleFunctor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallToBigTopos.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallToBigTopos.lean#L83). The attribute's comment: “the functor”.

> Send an étale object `U / T` to the composite `U / S`.

```lean
public abbrev smallEtaleToBigEtaleFunctor :
    SmallEtale B T.obj T.property ⥤ BigEtaleOver B S.obj S.property
```

**`AlgebraicGeometry.smallEtaleToBigEtaleFunctor_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallToBigTopos.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallToBigTopos.lean#L215). The attribute's comment: “cocontinuity”.

> Postcomposition from the small étale site of `T` to the big étale site over `S`
> is cocontinuous.

```lean
public instance smallEtaleToBigEtaleFunctor_isCocontinuous :
    (smallEtaleToBigEtaleFunctor B T S f).IsCocontinuous
      (SmallEtale.topology B T.obj T.property)
      (BigEtaleOver.topology B S.obj S.property)
```

**`AlgebraicGeometry.smallEtaleToBigEtaleFunctor_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallToBigTopos.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallToBigTopos.lean#L255). The attribute's comment: “continuity”.

> Postcomposition also preserves coverings and fibre products, hence is continuous.

```lean
public instance smallEtaleToBigEtaleFunctor_isContinuous :
    (smallEtaleToBigEtaleFunctor B T S f).IsContinuous
      (SmallEtale.topology B T.obj T.property)
      (BigEtaleOver.topology B S.obj S.property)
```

**`AlgebraicGeometry.smallEtaleToBigEtaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallToBigTopos.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallToBigTopos.lean#L265). The attribute's comment: “the morphism of topoi”.

> The geometric morphism `i_f : Sh(Tₑₜ) ⟶ Sh((Sch/S)ₑₜ)` induced by
> postcomposition.

```lean
public noncomputable def smallEtaleToBigEtaleMorphism :
    MorphismOfTopoi
      (Sheaf (SmallEtale.topology B T.obj T.property) (Type (u + 1)))
      (Sheaf (BigEtaleOver.topology B S.obj S.property) (Type (u + 1)))
```

**`AlgebraicGeometry.smallEtaleToBigEtaleLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallToBigTopos.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallToBigTopos.lean#L290). The attribute's comment: “existence of lower shriek”.

> The lower shriek is left adjoint to inverse image.

```lean
public noncomputable def smallEtaleToBigEtaleLowerShriekAdjunction :
    smallEtaleToBigEtaleLowerShriek B T S f ⊣
      (smallEtaleToBigEtaleMorphism B T S f).inverseImage
```

**`AlgebraicGeometry.smallEtaleToBigEtaleLowerShriek_preservesPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallToBigTopos.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallToBigTopos.lean#L306). The attribute's comment: “lower shriek preserves fibre products”.

> The lower shriek preserves fibre products.

```lean
public instance smallEtaleToBigEtaleLowerShriek_preservesPullbacks :
    PreservesLimitsOfShape WalkingCospan
      (smallEtaleToBigEtaleLowerShriek B T S f)
```

**`AlgebraicGeometry.smallEtaleToBigEtaleLowerShriek_preservesEqualizers`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallToBigTopos.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallToBigTopos.lean#L315). The attribute's comment: “lower shriek preserves equalizers”.

> The lower shriek preserves equalizers.

```lean
public instance smallEtaleToBigEtaleLowerShriek_preservesEqualizers :
    PreservesLimitsOfShape WalkingParallelPair
      (smallEtaleToBigEtaleLowerShriek B T S f)
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.sheafPullbackCocontinuousIsoSheafPushforwardContinuous`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L139), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallToBigTopos.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallToBigTopos.lean#L74) (StacksFrontier): “the inverse-image formula”.

## Tag 021G, a lemma

[Tag 021G](https://stacks.math.columbia.edu/tag/021G) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleInclusion_isMorphismOfSites_ringUniverse`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedProjectionAndIf.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedProjectionAndIf.lean#L191). The attribute's comment: “the morphism of sites, at the universe of the structure rings”.

> The inclusion of the small étale site of `S` into the big étale site over `S` defines a
> morphism of sites for sheaves of sets valued in the universe of the sections of the structure
> sheaves.
>
> `AlgebraicGeometry.smallEtaleInclusion_isMorphismOfSites` is the same assertion for sheaves of
> sets in `Type (u + 1)`, the universe of the objects of the sites; neither implies the other.

```lean
public instance smallEtaleInclusion_isMorphismOfSites_ringUniverse :
    IsMorphismOfSites.{u} (SmallEtale.inclusion B S.obj S.property)
      (SmallEtale.topology B S.obj S.property) (BigEtaleOver.topology B S.obj S.property)
```

**`AlgebraicGeometry.smallEtaleInclusion_preservesTerminal`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/Limits.lean#L200). The attribute's comment: “preservation of the final object”.

> The inclusion of the small étale category carries its final object to the
> final object of the big étale slice.

```lean
public instance smallEtaleInclusion_preservesTerminal :
    PreservesLimit (Functor.empty.{0} (SmallEtale B S hS))
      (SmallEtale.inclusion B S hS)
```

**`AlgebraicGeometry.smallEtaleInclusion_isMorphismOfSites`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleProjection.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleProjection.lean#L94). The attribute's comment: “the morphism of sites”.

> The full inclusion of the small étale site defines a morphism of sites
> from the big étale slice to the small étale site.

```lean
public instance smallEtaleInclusion_isMorphismOfSites :
    _root_.IsMorphismOfSites.{u + 1} (SmallEtale.inclusion B S hS)
      (SmallEtale.topology B S hS) (BigEtaleOver.topology B S hS)
```

**`AlgebraicGeometry.bigEtaleToSmallEtaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleProjection.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleProjection.lean#L149). The attribute's comment: “the projection of topoi”.

> The geometric morphism `π_S` associated to the inclusion of the small
> étale site into the big étale slice.

```lean
public noncomputable def bigEtaleToSmallEtaleMorphism :
    MorphismOfTopoi
      (Sheaf (BigEtaleOver.topology B S hS) (Type (u + 1)))
      (Sheaf (SmallEtale.topology B S hS) (Type (u + 1)))
```

**`AlgebraicGeometry.projectionCompInclusionPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleProjection.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleProjection.lean#L166). The attribute's comment: “the section property”.

> The composite `π_S ∘ i_S` is naturally the identity of the small étale
> topos, where `i_S` is the geometric morphism attached to `𝟙_S`.

```lean
public noncomputable def projectionCompInclusionPushforwardIso :
    (smallEtaleToBigEtaleMorphism B (B.obj S hS) (B.obj S hS)
        (𝟙 (B.obj S hS))).pushforward ⋙
      (bigEtaleToSmallEtaleMorphism B S hS).pushforward ≅
        𝟭 (Sheaf (SmallEtale.topology B S hS) (Type (u + 1)))
```

**`AlgebraicGeometry.inclusionInverseImageIsoProjectionPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleProjection.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleProjection.lean#L211). The attribute's comment: “inverse image is restriction”.

> Inverse image along `i_S` is naturally restriction to the small étale
> site, equivalently direct image along `π_S`.

```lean
public noncomputable def inclusionInverseImageIsoProjectionPushforward :
    (smallEtaleToBigEtaleMorphism B (B.obj S hS) (B.obj S hS)
        (𝟙 (B.obj S hS))).inverseImage ≅
      (bigEtaleToSmallEtaleMorphism B S hS).pushforward
```

## Tag 04BT, a definition

[Tag 04BT](https://stacks.math.columbia.edu/tag/04BT) in the Stacks Project.

**`AlgebraicGeometry.inclusionInverseImageIsoProjectionPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleProjection.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleProjection.lean#L211). The attribute's comment: “restriction to the small étale site, i.e. `i_S^{-1} = π_{S,*}`”.

> Inverse image along `i_S` is naturally restriction to the small étale
> site, equivalently direct image along `π_S`.

```lean
public noncomputable def inclusionInverseImageIsoProjectionPushforward :
    (smallEtaleToBigEtaleMorphism B (B.obj S hS) (B.obj S hS)
        (𝟙 (B.obj S hS))).inverseImage ≅
      (bigEtaleToSmallEtaleMorphism B S hS).pushforward
```

## Tag 021H, a lemma

[Tag 021H](https://stacks.math.columbia.edu/tag/021H) in the Stacks Project.

**`AlgebraicGeometry.bigEtaleMap_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean#L83). The attribute's comment: “cocontinuity”.

> **Stacks 021H.** Composition with `f` is cocontinuous for the big étale topologies.

```lean
public instance bigEtaleMap_isCocontinuous :
    (Over.map f).IsCocontinuous
      (BigEtaleOver.topology B T.obj T.property)
      (BigEtaleOver.topology B S.obj S.property)
```

**`AlgebraicGeometry.bigEtaleMap_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean#L94). The attribute's comment: “continuity”.

> Composition with `f` is also continuous.  This is the continuity used to identify inverse
> image with restriction and to construct the lower shriek.

```lean
public instance bigEtaleMap_isContinuous :
    (Over.map f).IsContinuous
      (BigEtaleOver.topology B T.obj T.property)
      (BigEtaleOver.topology B S.obj S.property)
```

**`AlgebraicGeometry.bigEtalePullback_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean#L105). The attribute's comment: “continuity of the base-change right adjoint”.

> **Stacks 021H.** Pullback along `f`, sending `U / S` to the canonical fibre product
> `U ×_S T / T`, is continuous for the big étale topologies.

```lean
public instance bigEtalePullback_isContinuous :
    (Over.pullback f).IsContinuous
      (BigEtaleOver.topology B S.obj S.property)
      (BigEtaleOver.topology B T.obj T.property)
```

**`AlgebraicGeometry.bigEtaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean#L116). The attribute's comment: “the morphism of topoi”.

> **Stacks 021H.** The morphism of big étale topoi induced by the cocontinuous functor
> `Over.map f`.

```lean
public noncomputable def bigEtaleMorphism (f : T ⟶ S) :
    MorphismOfTopoi
      (Sheaf (BigEtaleOver.topology B T.obj T.property) (Type (u + 1)))
      (Sheaf (BigEtaleOver.topology B S.obj S.property) (Type (u + 1)))
```

**`AlgebraicGeometry.bigEtaleMorphismInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean#L139). The attribute's comment: “the inverse-image formula”.

> **Stacks 021H.** Inverse image is restriction along composition with `f`.  On an object
> `U / T`, this is the formula `f_big⁻¹(G)(U / T) ≅ G(U / S)`.

```lean
public noncomputable def bigEtaleMorphismInverseImageIso :
    (bigEtaleMorphism B T S f).inverseImage ≅
      (Over.map f).sheafPushforwardContinuous (Type (u + 1))
        (BigEtaleOver.topology B T.obj T.property)
        (BigEtaleOver.topology B S.obj S.property)
```

**`AlgebraicGeometry.bigEtaleMorphismPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean#L151). The attribute's comment: “the direct-image formula”.

> **Stacks 021H.** Direct image is restriction along base change.  On an object `U / S`,
> this is the formula `f_big,*(F)(U / S) ≅ F(U ×_S T / T)`.

```lean
public noncomputable def bigEtaleMorphismPushforwardIso :
    (bigEtaleMorphism B T S f).pushforward ≅
      (Over.pullback f).sheafPushforwardContinuous (Type (u + 1))
        (BigEtaleOver.topology B S.obj S.property)
        (BigEtaleOver.topology B T.obj T.property)
```

**`AlgebraicGeometry.bigEtaleLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean#L162). The attribute's comment: “existence of lower shriek”.

> **Stacks 021H.** The inverse-image functor has the sheaf pullback along postcomposition
> as a left adjoint; this is `f_big!`.

```lean
public noncomputable def bigEtaleLowerShriekAdjunction :
    (Over.map f).sheafPullback (Type (u + 1))
      (BigEtaleOver.topology B T.obj T.property)
      (BigEtaleOver.topology B S.obj S.property) ⊣
        (bigEtaleMorphism B T S f).inverseImage
```

**`AlgebraicGeometry.bigEtaleLowerShriek_preservesPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean#L177). The attribute's comment: “lower shriek preserves fibre products”.

> **Stacks 021H.** The lower shriek commutes with fibre products.

```lean
public instance bigEtaleLowerShriek_preservesPullbacks :
    PreservesLimitsOfShape WalkingCospan
      ((Over.map f).sheafPullback (Type (u + 1))
        (BigEtaleOver.topology B T.obj T.property)
        (BigEtaleOver.topology B S.obj S.property))
```

**`AlgebraicGeometry.bigEtaleLowerShriek_preservesEqualizers`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean#L191). The attribute's comment: “lower shriek preserves equalizers”.

> **Stacks 021H.** The lower shriek commutes with equalizers.

```lean
public instance bigEtaleLowerShriek_preservesEqualizers :
    PreservesLimitsOfShape WalkingParallelPair
      ((Over.map f).sheafPullback (Type (u + 1))
        (BigEtaleOver.topology B T.obj T.property)
        (BigEtaleOver.topology B S.obj S.property))
```

Declarations registered for the tag:

- [`CategoryTheory.Over.map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.map#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean#L73) (StacksFrontier): “the postcomposition functor”. References: EGA I (2.5.3); EGA I (2.5.4), “more general”; SGA 3 I (1.6); SGA 4 IV (5.5).
- [`CategoryTheory.Over.pullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.pullback#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean#L74) (StacksFrontier): “the base-change functor”. References: EGA I (3.3.7), “more general”; EGA IV (8.2.6); SGA 3 I (1.6); SGA 4 III (5.5); SGA 4 IV (5.2), “more general”; SGA 4 IV (5.5).
- [`CategoryTheory.Over.mapPullbackAdj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.mapPullbackAdj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/BigEtaleMorphism.lean#L75) (StacksFrontier): “the base-change adjunction”.

## Tag 021I, a lemma

[Tag 021I](https://stacks.math.columbia.edu/tag/021I) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleRestrictionProjectionPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProjectionPullback.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProjectionPullback.lean#L170). The attribute's comment: “small-site factorization, inverse images”.

> **`i_f^{-1}π_S^{-1} = f_{small}^{-1}`.** Pulling a sheaf back from the small étale site of `S`
> to the big étale site over `S` and then restricting it to the small étale site of `T` along `f`
> is pulling it back along `f_{small}` directly.
>
> This is the identity the clauses of Stacks 0DDH about `π_S^{-1}` reduce to: it converts the
> comparison of big-site cohomology over `T` with small-site cohomology of `i_f^{-1}` into a
> statement about `f_{small}^{-1}`.

```lean
public def smallEtaleRestrictionProjectionPullbackIso :
    (SmallEtale.inclusion B S.obj S.property).sheafPullback A
        (SmallEtale.topology B S.obj S.property)
        (BigEtaleOver.topology B S.obj S.property) ⋙
      (smallEtaleToBigEtaleFunctor B T S f).sheafPushforwardContinuous A
        (SmallEtale.topology B T.obj T.property)
        (BigEtaleOver.topology B S.obj S.property) ≅
    (smallEtaleBaseChange B f).sheafPullback A
      (SmallEtale.topology B S.obj S.property)
      (SmallEtale.topology B T.obj T.property)
```

**`AlgebraicGeometry.smallEtaleBaseChange_isMorphismOfSites_ringUniverse`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/RingedSiteHom.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/RingedSiteHom.lean#L205). The attribute's comment: “small_etale_morphism at the universe of the structure rings”.

> **Stacks 021I at the universe of the structure rings.** Base change along `f : T ⟶ S` defines
> a morphism of sites from the small étale site of `T` to that of `S`, for sheaves of sets valued in
> the universe `u` of the sections of the structure sheaves.

```lean
public instance smallEtaleBaseChange_isMorphismOfSites_ringUniverse :
    IsMorphismOfSites.{u} (smallEtaleBaseChange B f)
      (SmallEtale.topology B S.obj S.property)
      (SmallEtale.topology B T.obj T.property)
```

**`AlgebraicGeometry.smallEtaleBaseChange_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean#L247). The attribute's comment: “base_change_continuous”.

> **Stacks 021I, base-change continuity.** Base change along a morphism in a big étale
> site is a continuous functor between the corresponding small étale sites.

```lean
public instance smallEtaleBaseChange_isContinuous {S T : B.Scheme} (f : T ⟶ S) :
    Functor.IsContinuous (smallEtaleBaseChange B f)
      (SmallEtale.topology B S.obj S.property)
      (SmallEtale.topology B T.obj T.property)
```

**`AlgebraicGeometry.smallEtaleBaseChange_isMorphismOfSites`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean#L262). The attribute's comment: “small_etale_morphism”.

> **Stacks 021I, small étale morphism.** Base change along `f : T ⟶ S` defines a
> morphism of sites from the small étale site of `T` to that of `S`.

```lean
public instance smallEtaleBaseChange_isMorphismOfSites {S T : B.Scheme} (f : T ⟶ S) :
    IsMorphismOfSites.{u + 1} (smallEtaleBaseChange B f)
      (SmallEtale.topology B S.obj S.property)
      (SmallEtale.topology B T.obj T.property)
```

**`AlgebraicGeometry.bigSmallEtalePushforwardCommIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean#L327). The attribute's comment: “commutative_diagram”.

> **Stacks 021I, commutative diagram.** The square formed by small étale base change, big
> étale base change, and the two projections from big to small étale topoi commutes on direct
> images.

```lean
public noncomputable def bigSmallEtalePushforwardCommIso :
    (bigEtaleToSmallEtaleMorphism B T.obj T.property).pushforward ⋙
        (smallEtaleBaseChange B f).sheafPushforwardContinuous
          (Type (u + 1)) (SmallEtale.topology B S.obj S.property)
          (SmallEtale.topology B T.obj T.property) ≅
      (bigEtaleMorphism B T S f).pushforward ⋙
        (bigEtaleToSmallEtaleMorphism B S.obj S.property).pushforward
```

**`AlgebraicGeometry.smallEtaleToBigEtaleMorphism_comp_inverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean#L373). The attribute's comment: “big_site_factorization”.

> **Stacks 021I, big-site factorization.** The inverse-image functor of `i_f` is naturally
> isomorphic to the inverse image of `f_big ∘ i_T`.

```lean
public noncomputable def smallEtaleToBigEtaleMorphism_comp_inverseImageIso :
    (smallEtaleToBigEtaleMorphism B T S f).inverseImage ≅
      (bigEtaleMorphism B T S f).inverseImage ⋙
        (smallEtaleToBigEtaleMorphism B T T (𝟙 T)).inverseImage
```

**`AlgebraicGeometry.smallEtaleToBigEtaleMorphism_comp_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean#L401). The attribute's comment: “big_site_factorization”.

> **Stacks 021I, big-site factorization.** The direct-image comparison for
> `i_f = f_big ∘ i_T`, naturally in the small étale sheaf.

```lean
public noncomputable def smallEtaleToBigEtaleMorphism_comp_pushforwardIso :
    (smallEtaleToBigEtaleMorphism B T S f).pushforward ≅
      (smallEtaleToBigEtaleMorphism B T T (𝟙 T)).pushforward ⋙
        (bigEtaleMorphism B T S f).pushforward
```

**`AlgebraicGeometry.smallEtalePushforwardIsoBigFactorization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean#L415). The attribute's comment: “small_site_factorization”.

> **Stacks 021I, small-site factorization.** The small étale direct image is canonically the
> composite of inclusion into the big étale topos over `T`, big-site direct image along `f`, and
> projection to the small étale topos of `S`.

```lean
public noncomputable def smallEtalePushforwardIsoBigFactorization :
    (smallEtaleBaseChange B f).sheafPushforwardContinuous
        (Type (u + 1)) (SmallEtale.topology B S.obj S.property)
          (SmallEtale.topology B T.obj T.property) ≅
      (smallEtaleToBigEtaleMorphism B T T (𝟙 T)).pushforward ⋙
        (bigEtaleMorphism B T S f).pushforward ⋙
          (bigEtaleToSmallEtaleMorphism B S.obj S.property).pushforward
```

**`AlgebraicGeometry.smallEtalePushforwardIsoDirectFactorization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean, line 439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean#L439). The attribute's comment: “small_site_factorization”.

> **Stacks 021I, small-site factorization.** The small étale direct image is canonically the
> composite of the direct morphism `i_f` to the big étale topos over `S` and its projection.

```lean
public noncomputable def smallEtalePushforwardIsoDirectFactorization :
    (smallEtaleBaseChange B f).sheafPushforwardContinuous
        (Type (u + 1)) (SmallEtale.topology B S.obj S.property)
          (SmallEtale.topology B T.obj T.property) ≅
      (smallEtaleToBigEtaleMorphism B T S f).pushforward ⋙
        (bigEtaleToSmallEtaleMorphism B S.obj S.property).pushforward
```

Declarations registered for the tag:

- [`AlgebraicGeometry.smallEtaleBaseChange_comp_inclusion`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean#L153), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean#L157) (StacksFrontier): “commutative_diagram”.
- [`CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtaleBaseChange.lean#L450) (StacksFrontier): “small_site_pushforward”.

## Tag 021J, a lemma

[Tag 021J](https://stacks.math.columbia.edu/tag/021J) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleBaseChange_idIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtalePullbackFunctoriality.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtalePullbackFunctoriality.lean#L126). The attribute's comment: “small étale site functor at the identity”.

> **Stacks 021J.** Small étale base change along an identity morphism is the identity
> functor, since pullback along an identity is.

```lean
public def smallEtaleBaseChange_idIso (X : B.Scheme) :
    smallEtaleBaseChange B (𝟙 X) ≅ 𝟭 (SmallEtale B X.obj X.property)
```

**`AlgebraicGeometry.smallEtaleSheafPullbackIdIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtalePullbackFunctoriality.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtalePullbackFunctoriality.lean#L137). The attribute's comment: “small étale inverse image at the identity”.

> **Stacks 021J.** Inverse image along the identity morphism of a scheme is the identity on
> sheaves on its small étale site, for any coefficient category.

```lean
public def smallEtaleSheafPullbackIdIso (X : B.Scheme) (A : Type u₁) [Category.{v₁} A]
    [((smallEtaleBaseChange B (𝟙 X)).sheafPushforwardContinuous A
      (SmallEtale.topology B X.obj X.property)
      (SmallEtale.topology B X.obj X.property)).IsRightAdjoint] :
    (smallEtaleBaseChange B (𝟙 X)).sheafPullback A
        (SmallEtale.topology B X.obj X.property)
        (SmallEtale.topology B X.obj X.property) ≅
      𝟭 (Sheaf (SmallEtale.topology B X.obj X.property) A)
```

**`AlgebraicGeometry.smallEtaleSheafPullbackCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtalePullbackFunctoriality.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtalePullbackFunctoriality.lean#L150). The attribute's comment: “small étale inverse images, general coefficients”.

> **Stacks 021J.** Inverse image along a composite of morphisms of a big étale site is the
> composite of the inverse images, for any coefficient category.

```lean
public def smallEtaleSheafPullbackCompIso (X Y Z : B.Scheme) (f : X ⟶ Y) (g : Y ⟶ Z)
    (A : Type u₁) [Category.{v₁} A]
    [((smallEtaleBaseChange B g).sheafPushforwardContinuous A
      (SmallEtale.topology B Z.obj Z.property)
      (SmallEtale.topology B Y.obj Y.property)).IsRightAdjoint]
    [((smallEtaleBaseChange B f).sheafPushforwardContinuous A
      (SmallEtale.topology B Y.obj Y.property)
      (SmallEtale.topology B X.obj X.property)).IsRightAdjoint]
    [((smallEtaleBaseChange B (f ≫ g)).sheafPushforwardContinuous A
      (SmallEtale.topology B Z.obj Z.property)
      (SmallEtale.topology B X.obj X.property)).IsRightAdjoint] :
    (smallEtaleBaseChange B g).sheafPullback A
        (SmallEtale.topology B Z.obj Z.property)
        (SmallEtale.topology B Y.obj Y.property) ⋙
      (smallEtaleBaseChange B f).sheafPullback A
        (SmallEtale.topology B Y.obj Y.property)
        (SmallEtale.topology B X.obj X.property) ≅
    (smallEtaleBaseChange B (f ≫ g)).sheafPullback A
      (SmallEtale.topology B Z.obj Z.property)
      (SmallEtale.topology B X.obj X.property)
```

**`AlgebraicGeometry.smallEtaleBaseChange_compIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/MorphismComposition.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/MorphismComposition.lean#L99). The attribute's comment: “small étale site functor composition”.

> **Stacks 021J.** The canonical comparison of successive small étale base changes with
> base change along the composite, characterized by its image under the inclusion of the small
> étale category.

```lean
public noncomputable def smallEtaleBaseChange_compIso :
    { e : smallEtaleBaseChange B g ⋙ smallEtaleBaseChange B f ≅
        smallEtaleBaseChange B (f ≫ g) //
      ∀ U : SmallEtale B Z.obj Z.property,
        (SmallEtale.inclusion B X.obj X.property).map (e.hom.app U) =
          (Over.pullbackComp f g).inv.app U.obj }
```

**`AlgebraicGeometry.smallEtaleBaseChange_compIso_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/MorphismComposition.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/MorphismComposition.lean#L124). The attribute's comment: “canonicity of small étale site composition”.

> **Stacks 021J.** The small-site comparison is the canonical comparison of pullbacks in
> the ambient slice category, after forgetting the étale condition.

```lean
public theorem smallEtaleBaseChange_compIso_app
    (U : SmallEtale B Z.obj Z.property) :
    (SmallEtale.inclusion B X.obj X.property).map
      ((smallEtaleBaseChange_compIso B X Y Z f g).val.hom.app U) =
    (Over.pullbackComp f g).inv.app U.obj
```

**`AlgebraicGeometry.bigEtaleMorphism_comp_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/MorphismComposition.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/MorphismComposition.lean#L161). The attribute's comment: “big étale direct images”.

> **Stacks 021J.** The canonical big-site direct-image comparison, obtained from the
> base-change formula and the composition comparison of pullbacks.

```lean
public noncomputable def bigEtaleMorphism_comp_pushforwardIso :
    (bigEtaleMorphism B X Y f).pushforward ⋙
        (bigEtaleMorphism B Y Z g).pushforward ≅
      (bigEtaleMorphism B X Z (f ≫ g)).pushforward
```

**`AlgebraicGeometry.bigEtaleMorphism_comp_inverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/MorphismComposition.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/MorphismComposition.lean#L182). The attribute's comment: “big étale inverse images”.

> **Stacks 021J.** The inverse-image comparison is the mate of the big direct-image
> comparison under the three geometric adjunctions.

```lean
public noncomputable def bigEtaleMorphism_comp_inverseImageIso :
    (bigEtaleMorphism B Y Z g).inverseImage ⋙
        (bigEtaleMorphism B X Y f).inverseImage ≅
      (bigEtaleMorphism B X Z (f ≫ g)).inverseImage
```

**`AlgebraicGeometry.smallEtaleMorphism_comp_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/MorphismComposition.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/MorphismComposition.lean#L195). The attribute's comment: “small étale direct images”.

> **Stacks 021J.** The direct-image comparison induced by the canonical composition
> comparison of small-site base-change functors.

```lean
public noncomputable def smallEtaleMorphism_comp_pushforwardIso :
    (smallEtaleBaseChange B f).sheafPushforwardContinuous
        (Type (u + 1)) (SmallEtale.topology B Y.obj Y.property)
          (SmallEtale.topology B X.obj X.property) ⋙
      (smallEtaleBaseChange B g).sheafPushforwardContinuous
        (Type (u + 1)) (SmallEtale.topology B Z.obj Z.property)
          (SmallEtale.topology B Y.obj Y.property) ≅
    (smallEtaleBaseChange B (f ≫ g)).sheafPushforwardContinuous
      (Type (u + 1)) (SmallEtale.topology B Z.obj Z.property)
        (SmallEtale.topology B X.obj X.property)
```

**`AlgebraicGeometry.smallEtaleMorphism_comp_inverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/MorphismComposition.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/MorphismComposition.lean#L214). The attribute's comment: “small étale inverse images”.

> **Stacks 021J.** The inverse-image comparison is the mate of the small direct-image
> comparison under the three sheaf adjunctions.

```lean
public noncomputable def smallEtaleMorphism_comp_inverseImageIso :
    (smallEtaleBaseChange B g).sheafPullback
        (Type (u + 1)) (SmallEtale.topology B Z.obj Z.property)
          (SmallEtale.topology B Y.obj Y.property) ⋙
      (smallEtaleBaseChange B f).sheafPullback
        (Type (u + 1)) (SmallEtale.topology B Y.obj Y.property)
          (SmallEtale.topology B X.obj X.property) ≅
    (smallEtaleBaseChange B (f ≫ g)).sheafPullback
      (Type (u + 1)) (SmallEtale.topology B Z.obj Z.property)
        (SmallEtale.topology B X.obj X.property)
```

## Tag 0DDA, a lemma

[Tag 0DDA](https://stacks.math.columbia.edu/tag/0DDA) in the Stacks Project.

**`AlgebraicGeometry.smallEtalePushforwardBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/BaseChangeCommutation.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/BaseChangeCommutation.lean#L142). The attribute's comment: “small-site base change”.

> On a cartesian square, restriction to the small étale site commutes canonically with
> big-site direct image.

```lean
public noncomputable def smallEtalePushforwardBaseChangeIso
    (B : AlgebraicGeometry.BigEtaleSite.{u}) {T' T S' S : B.Scheme}
    (g' : T' ⟶ T) (f' : T' ⟶ S') (f : T ⟶ S) (g : S' ⟶ S)
    (h : IsPullback g' f' f g) :
    (bigEtaleMorphism B T S f).pushforward ⋙
      (smallEtaleToBigEtaleMorphism B S' S g).inverseImage ≅
    (smallEtaleToBigEtaleMorphism B T' T g').inverseImage ⋙
      (smallEtaleBaseChange B f').sheafPushforwardContinuous
        (Type (u + 1)) (SmallEtale.topology B S'.obj S'.property)
          (SmallEtale.topology B T'.obj T'.property)
```

**`AlgebraicGeometry.bigEtalePushforwardBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/BaseChangeCommutation.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Etale/BaseChangeCommutation.lean#L222). The attribute's comment: “big-site base change”.

> On a cartesian square, big étale direct image commutes canonically with big étale inverse
> image.

```lean
public noncomputable def bigEtalePushforwardBaseChangeIso
    (B : AlgebraicGeometry.BigEtaleSite.{u}) {T' T S' S : B.Scheme}
    (g' : T' ⟶ T) (f' : T' ⟶ S') (f : T ⟶ S) (g : S' ⟶ S)
    (h : IsPullback g' f' f g) :
    (bigEtaleMorphism B T S f).pushforward ⋙
      (bigEtaleMorphism B S' S g).inverseImage ≅
    (bigEtaleMorphism B T' T g').inverseImage ⋙
      (bigEtaleMorphism B T' S' f').pushforward
```

## Tag 021K, a lemma

[Tag 021K](https://stacks.math.columbia.edu/tag/021K) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSheafData`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigEtale/CompatibleSystem.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigEtale/CompatibleSystem.lean#L58). The attribute's comment: “the compatible data”.

> A compatible system of sheaves on the small étale sites of the schemes over `S`: a sheaf on
> the small étale site of every `T / S`, a comparison map from the inverse image of the sheaf at `T`
> to the sheaf at `T'` along every morphism `T' ⟶ T` over `S`, subject to the cocycle condition for
> a composite and to being an isomorphism whenever the morphism is étale.

```lean
public structure BigEtaleSheafData
```

**`AlgebraicGeometry.characterizeSheafBigEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigEtale/SmallEtaleComparison.lean, line 1206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigEtale/SmallEtaleComparison.lean#L1206). The attribute's comment: “equivalence with big étale sheaves”.

> **Stacks Project, Tag 021K.** A sheaf on the big étale site over `S` is precisely a
> compatible family of sheaves on the small étale sites of all the schemes over `S`: the
> restriction functor is an equivalence of categories.

```lean
public def characterizeSheafBigEtale :
    Sheaf (BigEtaleOver.topology B S hS) (Type (max (u + 1) v)) ≌
      BigEtaleSheafData.{u, v} B S hS
```

**`AlgebraicGeometry.characterizeSheafBigEtale_functor_comp_eval`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigEtale/SmallEtaleComparison.lean, line 1221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigEtale/SmallEtaleComparison.lean#L1221). The attribute's comment: “equivalence with big étale sheaves”.

> **Stacks Project, Tag 021K.** Evaluating the equivalence at a scheme `T` over `S` is
> restriction to the small étale site of `T`.

```lean
public theorem characterizeSheafBigEtale_functor_comp_eval (T : BigEtaleOver B S hS) :
    (characterizeSheafBigEtale.{u, v} B S hS).functor ⋙ BigEtaleSheafData.eval B S hS T =
      bigEtaleSheafRestrictionAt B S hS T
```

**`AlgebraicGeometry.characterizeSheafBigEtale_pullback_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigEtale/SmallEtaleComparison.lean, line 1230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigEtale/SmallEtaleComparison.lean#L1230). The attribute's comment: “equivalence with big étale sheaves”.

> **Stacks Project, Tag 021K.** Under the equivalence the adjoint of each comparison map is
> restriction along the projection `U ×[T] T' ⟶ U`, for every small étale object `U` of `T`; so
> the equivalence determines the comparison maps as well as the sheaves.

```lean
public theorem characterizeSheafBigEtale_pullback_app
    (F : Sheaf (BigEtaleOver.topology B S hS) (Type (max (u + 1) v)))
    {T T' : BigEtaleOver B S hS} (f : T' ⟶ T)
    (U : SmallEtale B T.left.1 T.left.property) :
    ((B.smallPullbackAdjunction f.left (Type (max (u + 1) v))).homEquiv _ _
        (((characterizeSheafBigEtale.{u, v} B S hS).functor.obj F).pullback f)).hom.app
          (op U) =
      F.obj.map (bigEtaleBaseChangeProjection B S hS f U).op
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 34.4, Tag 0214](https://stacks.math.columbia.edu/tag/0214)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
