---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.zariskiPrecoverage, AlgebraicGeometry.Scheme.OpenCover, AlgebraicGeometry.Scheme.zariskiPretopology, AlgebraicGeometry.Scheme.OpenCover.exists_isStandardZariski_refinement, AlgebraicGeometry.IsStandardZariskiCovering, AlgebraicGeometry.BigZariskiSite, AlgebraicGeometry.BigZariskiSite.exists_isCovering_tautologicallyEquivalent_openCover, AlgebraicGeometry.BigZariskiOver
statement: formalized
proof: formalized
---

# 34.3 The Zariski topology

Section 34.3 of the Stacks Project, [Tag 020N](https://stacks.math.columbia.edu/tag/020N). 20 tags here are carried by 78 declarations of the repository (all in StacksFrontier) and 15 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 020O, a definition

[Tag 020O](https://stacks.math.columbia.edu/tag/020O) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.zariskiPrecoverage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.zariskiPrecoverage#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch34.lean, line 18](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch34.lean#L18) (StacksFrontier). References: SGA 3 IV (6.1); SGA 4 VII (4.2).
- [`AlgebraicGeometry.Scheme.OpenCover`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.OpenCover#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch34.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch34.lean#L19) (StacksFrontier). References: SGA 3 IV (6.1), “partial”.

## Tag 020P, a lemma

[Tag 020P](https://stacks.math.columbia.edu/tag/020P) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.zariskiPretopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.zariskiPretopology#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch34.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch34.lean#L20) (StacksFrontier). References: SGA 3 IV (6.1); SGA 4 VII (4.2).

## Tag 020Q, a lemma

[Tag 020Q](https://stacks.math.columbia.edu/tag/020Q) in the Stacks Project.

**`AlgebraicGeometry.Scheme.OpenCover.exists_isStandardZariski_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Zariski/StandardCovering.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Zariski/StandardCovering.lean#L56).

> **Stacks Project, Tag 020Q.** Every Zariski covering of an affine scheme has a finite
> refinement by standard opens, each contained in a member of the original covering.

```lean
public theorem OpenCover.exists_isStandardZariski_refinement {T : Scheme.{u}} [IsAffine T]
    (𝒰 : T.OpenCover.{v}) :
    ∃ (𝒱 : T.OpenCover.{v}) (_refinement : 𝒱 ⟶ 𝒰),
      AlgebraicGeometry.IsStandardZariskiCovering 𝒱
```

## Tag 020R, a definition

[Tag 020R](https://stacks.math.columbia.edu/tag/020R) in the Stacks Project.

**`AlgebraicGeometry.IsStandardZariskiCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/StandardCoverings.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/StandardCoverings.lean#L32).

> A Zariski covering of an affine scheme `T` is standard if it has finitely many members and
> every member identifies with a standard affine open `T.basicOpen f` of the target.

```lean
public abbrev IsStandardZariskiCovering {T : Scheme.{u}} [IsAffine T]
    (𝒰 : T.Cover.{v} Scheme.zariskiPrecoverage) : Prop
```

## Tag 020S, a definition

[Tag 020S](https://stacks.math.columbia.edu/tag/020S) in the Stacks Project.

**`AlgebraicGeometry.BigZariskiSite`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Zariski/BigSite.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Zariski/BigSite.lean#L90).

> **Stacks 020S.** A big Zariski site consists of an initial set of schemes and initial
> Zariski covering families, a sufficiently large cutoff category containing those schemes,
> and a bounded set of Zariski covering families.
>
> The last two fields say that the selected families satisfy the site axioms and that every
> Zariski covering family has a combinatorially equivalent selected representative.

```lean
public structure BigZariskiSite
```

## Tag 03WV, a lemma

[Tag 03WV](https://stacks.math.columbia.edu/tag/03WV) in the Stacks Project.

**`AlgebraicGeometry.BigZariskiSite.exists_isCovering_tautologicallyEquivalent_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Zariski/BigSite.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Zariski/BigSite.lean#L171).

> **Stacks Project, Tag 03WV.** Every Zariski covering of an object of a big Zariski site
> is tautologically equivalent to a covering belonging to that site.

```lean
public theorem exists_isCovering_tautologicallyEquivalent_openCover
    (B : BigZariskiSite.{u}) (T : B.Schemes)
    (U : (B.inclusion.obj T).OpenCover.{v}) :
    ∃ V : PreZeroHypercover.{u + 1} T,
      B.IsCovering ⟨T, V⟩ ∧
        PreZeroHypercover.TautologicallyEquivalent U.toPreZeroHypercover
          (V.map B.inclusion)
```

## Tag 020T, a definition

[Tag 020T](https://stacks.math.columbia.edu/tag/020T) in the Stacks Project.

**`AlgebraicGeometry.BigZariskiOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L53). The attribute's comment: “part (1), category”.

> The big Zariski category of `S` is the slice of the chosen big category.

```lean
public abbrev BigZariskiOver
```

**`AlgebraicGeometry.BigZariskiOver.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L66). The attribute's comment: “part (1), coverings”.

> A family over `S` covers when its underlying family covers in the chosen big site.

```lean
public abbrev IsCovering (E : Covering (BigZariskiOver B S hS)) : Prop
```

**`AlgebraicGeometry.SmallZariski`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L95). The attribute's comment: “part (2), category”.

> The small Zariski category consists of schemes open in `S`.

```lean
public abbrev SmallZariski
```

**`AlgebraicGeometry.SmallZariski.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L112). The attribute's comment: “part (2), coverings”.

> Small-site coverings are precisely big-site coverings of small-site objects.

```lean
public abbrev IsCovering (E : Covering (SmallZariski B S hS)) : Prop
```

**`AlgebraicGeometry.BigAffineZariski`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L151). The attribute's comment: “part (3), category”.

> The big affine Zariski category consists of affine schemes over `S`.

```lean
public abbrev BigAffineZariski
```

**`AlgebraicGeometry.BigAffineZariski.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L169). The attribute's comment: “part (3), coverings”.

> Big affine coverings are standard Zariski coverings.

```lean
public abbrev IsCovering (E : Covering (BigAffineZariski B S hS)) : Prop
```

**`AlgebraicGeometry.SmallAffineZariski`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L200). The attribute's comment: “part (4), category”.

> The small affine Zariski category consists of affine opens in `S`.

```lean
public abbrev SmallAffineZariski
```

**`AlgebraicGeometry.SmallAffineZariski.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/Sites.lean#L220). The attribute's comment: “part (4), coverings”.

> Small affine coverings are the standard Zariski coverings inherited from the small site.

```lean
public abbrev IsCovering (E : Covering (SmallAffineZariski B S hS)) : Prop
```

## Tag 020U, a lemma

[Tag 020U](https://stacks.math.columbia.edu/tag/020U) in the Stacks Project.

**`AlgebraicGeometry.SmallZariski.isSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiSiteAxioms.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiSiteAxioms.lean#L239). The attribute's comment: “small Zariski site”.

> Zariski coverings of schemes open in `S` satisfy the site axioms.

```lean
public theorem isSite (B : AlgebraicGeometry.BigZariskiSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) : IsSite (AlgebraicGeometry.SmallZariski.IsCovering B S hS)
```

**`AlgebraicGeometry.BigAffineZariski.isSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiSiteAxioms.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiSiteAxioms.lean#L314). The attribute's comment: “big affine Zariski site”.

> Standard Zariski coverings of affine schemes over `S` satisfy the site axioms.

```lean
public theorem isSite (B : AlgebraicGeometry.BigZariskiSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) : IsSite (AlgebraicGeometry.BigAffineZariski.IsCovering B S hS)
```

**`AlgebraicGeometry.SmallAffineZariski.isSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiSiteAxioms.lean, line 414](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiSiteAxioms.lean#L414). The attribute's comment: “small affine Zariski site”.

> Standard Zariski coverings of affine opens of `S` satisfy the site axioms.

```lean
public theorem isSite (B : AlgebraicGeometry.BigZariskiSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) : IsSite (AlgebraicGeometry.SmallAffineZariski.IsCovering B S hS)
```

## Tag 020V, a lemma

[Tag 020V](https://stacks.math.columbia.edu/tag/020V) in the Stacks Project.

**`AlgebraicGeometry.hasPullbacks_bigZariskiSite`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean#L94). The attribute's comment: “fibre products in the big Zariski site”.

> The underlying category of a big Zariski site has fibre products.

```lean
public instance hasPullbacks_bigZariskiSite : HasPullbacks B.Schemes
```

**`AlgebraicGeometry.hasPullbacks_smallZariski`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean#L107). The attribute's comment: “fibre products in the small Zariski site”.

> The small Zariski category of `S` has fibre products.

```lean
public instance hasPullbacks_smallZariski : HasPullbacks (SmallZariski B S hS)
```

**`AlgebraicGeometry.hasPullbacks_bigAffineZariski`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean#L128). The attribute's comment: “fibre products in the big affine Zariski site”.

> The category of affine objects in the big Zariski category over `S` has fibre products.

```lean
public instance hasPullbacks_bigAffineZariski : HasPullbacks (BigAffineZariski B S hS)
```

**`AlgebraicGeometry.hasPullbacks_smallAffineZariski`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean#L143). The attribute's comment: “fibre products in the small affine Zariski site”.

> The affine small Zariski category of `S` has fibre products.

```lean
public instance hasPullbacks_smallAffineZariski : HasPullbacks (SmallAffineZariski B S hS)
```

**`AlgebraicGeometry.preservesPullbacks_bigZariskiSiteInclusion`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean#L150). The attribute's comment: “preservation by the big Zariski site inclusion”.

> The inclusion of a big Zariski site's underlying category into schemes preserves fibre
> products.

```lean
public instance preservesPullbacks_bigZariskiSiteInclusion :
    PreservesLimitsOfShape WalkingCospan B.inclusion
```

**`AlgebraicGeometry.preservesPullbacks_smallZariskiToScheme`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean#L165). The attribute's comment: “preservation by the small Zariski functor to schemes”.

> The canonical functor from the small Zariski category to schemes preserves fibre
> products.

```lean
public instance preservesPullbacks_smallZariskiToScheme :
    PreservesLimitsOfShape WalkingCospan (SmallZariski.toScheme B S hS)
```

**`AlgebraicGeometry.preservesPullbacks_bigAffineZariskiToScheme`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean#L174). The attribute's comment: “preservation by the big affine Zariski functor to schemes”.

> The canonical functor from affine objects over `S` to schemes preserves fibre products.

```lean
public instance preservesPullbacks_bigAffineZariskiToScheme :
    PreservesLimitsOfShape WalkingCospan (BigAffineZariski.toScheme B S hS)
```

**`AlgebraicGeometry.preservesPullbacks_smallAffineZariskiToScheme`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean#L180). The attribute's comment: “preservation by the small affine Zariski functor to schemes”.

> The canonical functor from affine open objects over `S` to schemes preserves fibre
> products.

```lean
public instance preservesPullbacks_smallAffineZariskiToScheme :
    PreservesLimitsOfShape WalkingCospan (SmallAffineZariski.toScheme B S hS)
```

**`AlgebraicGeometry.SmallZariski.finalIsTerminal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean#L194). The attribute's comment: “the final object of the small Zariski site”.

> The object `S / S` is final in the small Zariski category of `S`.

```lean
public noncomputable def SmallZariski.finalIsTerminal :
    IsTerminal (SmallZariski.final B S hS)
```

Declarations registered for the tag:

- [`CategoryTheory.Over.instHasPullbacks`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.instHasPullbacks#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean#L102) (StacksFrontier): “fibre products in the big Zariski slice”.
- [`CategoryTheory.Over.preservesLimitsOfShape_forget_of_isConnected`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.preservesLimitsOfShape_forget_of_isConnected#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean#L153) (StacksFrontier): “preservation by the big Zariski slice forgetful functor”. References: SGA 4 IV (5.10), “more general”; SGA 4 IV (5.3), “partial”.
- [`CategoryTheory.Limits.comp_preservesLimitsOfShape`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.comp_preservesLimitsOfShape#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean#L159) (StacksFrontier): “preservation under composition for the big Zariski slice functor”.
- [`CategoryTheory.Over.mkIdTerminal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.mkIdTerminal#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean#L183) (StacksFrontier): “the final object of the big Zariski slice”. References: EGA 0 (8.1.10), “more general”; SGA 3 I (1.3); SGA 4 IV (5.11.1), “terminal object (X”.

## Tag 020W, a lemma

[Tag 020W](https://stacks.math.columbia.edu/tag/020W) in the Stacks Project.

**`AlgebraicGeometry.BigAffineZariski.inclusion_isSpecialCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/AffineZariskiDenseSubsite.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/AffineZariskiDenseSubsite.lean#L317).

> **Stacks 020W.** The inclusion of the big affine Zariski site over a scheme
> into its big Zariski site is special cocontinuous. Its dense-subsite component
> gives the induced equivalence of topoi.

```lean
public theorem BigAffineZariski.inclusion_isSpecialCocontinuous
    (B : BigZariskiSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) :
    IsSpecialCocontinuous
      (BigAffineZariski.topology B S hS)
      (BigZariskiOver.topology B S hS)
      (BigAffineZariski.inclusion B S hS)
```

## Tag 0F1B, a lemma

[Tag 0F1B](https://stacks.math.columbia.edu/tag/0F1B) in the Stacks Project.

**`AlgebraicGeometry.SmallAffineZariski.inclusion_isSpecialCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/SmallAffineDenseSubsite.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiTopology/SmallAffineDenseSubsite.lean#L320).

> **Stacks 0F1B.** The inclusion of the small affine Zariski site of a scheme into its small
> Zariski site is a special cocontinuous functor. Its dense-subsite component is the induced
> equivalence of topoi `Sh(S_{affine, Zar}) ≌ Sh(S_Zar)`, given by
> `CategoryTheory.Functor.IsDenseSubsite.sheafEquiv`.

```lean
public theorem SmallAffineZariski.inclusion_isSpecialCocontinuous
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    IsSpecialCocontinuous (SmallAffineZariski.topology B S hS)
      (SmallZariski.topology B S hS) (SmallAffineZariski.inclusion B S hS)
```

## Tag 020X, a lemma

[Tag 020X](https://stacks.math.columbia.edu/tag/020X) in the Stacks Project.

**`AlgebraicGeometry.smallZariskiSheafEquivWith`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiOpens.lean, line 412](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiOpens.lean#L412).

> The equivalence between sheaves with values in a category `A` on the small Zariski site of
> `S` and on the opens of `S`, induced by `smallZariskiSiteEquiv B S hS`.

```lean
public noncomputable def smallZariskiSheafEquivWith (A : Type w) [Category.{v} A] :
    Sheaf (SmallZariski.topology B S hS) A ≌
      Sheaf (Opens.grothendieckTopology S.carrier) A
```

## Tag 020Y, a lemma

[Tag 020Y](https://stacks.math.columbia.edu/tag/020Y) in the Stacks Project.

**`AlgebraicGeometry.smallZariskiToBigZariskiToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedToposIf.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedToposIf.lean#L110). The attribute's comment: “the morphism of topoi, at the universe of the structure rings”.

> **Stacks 020Y at the universe of the structure rings.**  The morphism of topoi
> `i_f : \mathrm{Sh}(T_{Zar}) ⟶ \mathrm{Sh}((\Sch/S)_{Zar})` on sheaves of sets in `Type u`.
>
> The library's `AlgebraicGeometry.smallZariskiToBigZariskiMorphism` is the same morphism for sheaves
> of sets in `Type (u + 1)`, the universe of the objects of the sites; a ringed topos declares its
> topos at the universe of the sections of its structure sheaf, so that one cannot carry a
> morphism of ringed topoi.

```lean
public noncomputable def smallZariskiToBigZariskiToposHom :
    MorphismOfTopoi (Sheaf (SmallZariski.topology B T.1 T.property) (Type u))
      (Sheaf (BigZariskiOver.topology B S.1 S.property) (Type u))
```

**`AlgebraicGeometry.smallZariskiToBigZariskiFunctor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiToBig.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiToBig.lean#L107). The attribute's comment: “the functor”.

> Send an open immersion `U ⟶ T` to the composite `U ⟶ S`.

```lean
public abbrev smallZariskiToBigZariskiFunctor :
    SmallZariski B T.obj T.property ⥤ BigZariskiOver B S.obj S.property
```

**`AlgebraicGeometry.smallZariskiToBigZariskiFunctor_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiToBig.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiToBig.lean#L123). The attribute's comment: “cocontinuity”.

> Postcomposition from the small Zariski site is cocontinuous.

```lean
public instance smallZariskiToBigZariskiFunctor_isCocontinuous :
    (smallZariskiToBigZariskiFunctor B T S f).IsCocontinuous
      (SmallZariski.topology B T.obj T.property)
      (BigZariskiOver.topology B S.obj S.property)
```

**`AlgebraicGeometry.smallZariskiToBigZariskiFunctor_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiToBig.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiToBig.lean#L194). The attribute's comment: “continuity”.

> Postcomposition preserves coverings and fibre products, hence is continuous.

```lean
public instance smallZariskiToBigZariskiFunctor_isContinuous :
    (smallZariskiToBigZariskiFunctor B T S f).IsContinuous
      (SmallZariski.topology B T.obj T.property)
      (BigZariskiOver.topology B S.obj S.property)
```

**`AlgebraicGeometry.smallZariskiToBigZariskiMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiToBig.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiToBig.lean#L226). The attribute's comment: “the morphism of topoi”.

> The geometric morphism `i_f : Sh(T_Zar) ⟶ Sh((Sch/S)_Zar)`.

```lean
public noncomputable def smallZariskiToBigZariskiMorphism :
    MorphismOfTopoi
      (Sheaf (SmallZariski.topology B T.obj T.property) (Type (u + 1)))
      (Sheaf (BigZariskiOver.topology B S.obj S.property) (Type (u + 1)))
```

**`AlgebraicGeometry.smallZariskiToBigZariskiLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiToBig.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiToBig.lean#L251). The attribute's comment: “existence of lower shriek”.

> Lower shriek is left adjoint to inverse image.

```lean
public noncomputable def smallZariskiToBigZariskiLowerShriekAdjunction :
    smallZariskiToBigZariskiLowerShriek B T S f ⊣
      (smallZariskiToBigZariskiMorphism B T S f).inverseImage
```

**`AlgebraicGeometry.smallZariskiToBigZariskiLowerShriek_preservesPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiToBig.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiToBig.lean#L267). The attribute's comment: “lower shriek preserves fibre products”.

> Lower shriek preserves fibre products.

```lean
public instance smallZariskiToBigZariskiLowerShriek_preservesPullbacks :
    PreservesLimitsOfShape WalkingCospan
      (smallZariskiToBigZariskiLowerShriek B T S f)
```

**`AlgebraicGeometry.smallZariskiToBigZariskiLowerShriek_preservesEqualizers`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiToBig.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiToBig.lean#L277). The attribute's comment: “lower shriek preserves equalizers”.

> Lower shriek preserves equalizers.

```lean
public instance smallZariskiToBigZariskiLowerShriek_preservesEqualizers :
    PreservesLimitsOfShape WalkingParallelPair
      (smallZariskiToBigZariskiLowerShriek B T S f)
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.sheafPullbackCocontinuousIsoSheafPushforwardContinuous`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L139), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiToBig.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiToBig.lean#L65) (StacksFrontier): “the inverse-image formula”.

## Tag 020Z, a lemma

[Tag 020Z](https://stacks.math.columbia.edu/tag/020Z) in the Stacks Project.

**`AlgebraicGeometry.smallZariskiInclusion_isMorphismOfSites_ringUniverse`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedProjectionAndIf.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedProjectionAndIf.lean#L108). The attribute's comment: “the morphism of sites, at the universe of the structure rings”.

> The inclusion of the small Zariski site of `S` into the big Zariski site over `S` defines a
> morphism of sites for sheaves of sets valued in the universe of the sections of the structure
> sheaves.

```lean
public instance smallZariskiInclusion_isMorphismOfSites_ringUniverse :
    IsMorphismOfSites.{u} (SmallZariski.inclusion B S.1 S.property)
      (SmallZariski.topology B S.1 S.property) (BigZariskiOver.topology B S.1 S.property)
```

**`AlgebraicGeometry.smallZariskiInclusion_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiProjection.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiProjection.lean#L72). The attribute's comment: “continuity of the site morphism”.

> The inclusion of the small Zariski site in the big slice site is continuous.

```lean
public instance smallZariskiInclusion_isContinuous :
    (SmallZariski.inclusion B S.obj S.property).IsContinuous
      (SmallZariski.topology B S.obj S.property)
      (BigZariskiOver.topology B S.obj S.property)
```

**`AlgebraicGeometry.smallZariskiInclusion_preservesFiniteLimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiProjection.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiProjection.lean#L85). The attribute's comment: “exactness of the site morphism”.

> The inverse-image functor of the site morphism is left exact.

```lean
public instance smallZariskiInclusion_preservesFiniteLimits :
    PreservesFiniteLimits
      ((SmallZariski.inclusion B S.obj S.property).sheafPullback (Type (u + 1))
        (SmallZariski.topology B S.obj S.property)
        (BigZariskiOver.topology B S.obj S.property))
```

**`AlgebraicGeometry.smallZariskiProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiProjection.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiProjection.lean#L112). The attribute's comment: “the projection of topoi”.

> The projection `π_S` from the big Zariski topos to the small one.

```lean
public noncomputable def smallZariskiProjection :
    MorphismOfTopoi
      (Sheaf (BigZariskiOver.topology B S.obj S.property) (Type (u + 1)))
      (Sheaf (SmallZariski.topology B S.obj S.property) (Type (u + 1)))
```

**`AlgebraicGeometry.smallZariskiProjection_comp_identity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiProjection.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiProjection.lean#L129). The attribute's comment: “the retraction”.

> The inverse-image functor of `π_S ∘ i_{id_S}` is naturally the identity.

```lean
public noncomputable def smallZariskiProjection_comp_identity :
    ((smallZariskiProjection B S).comp
      (smallZariskiToBigZariskiMorphism B S S (𝟙 S))).inverseImage ≅
        𝟭 (Sheaf (SmallZariski.topology B S.obj S.property) (Type (u + 1)))
```

**`AlgebraicGeometry.smallZariskiIdentityInverseImageIsoProjectionPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiProjection.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiProjection.lean#L188). The attribute's comment: “the inverse-image formula”.

> Inverse image along `i_S = i_{id_S}` is the direct image along `π_S`,
> namely restriction of a big-site sheaf to the small site.

```lean
public noncomputable def smallZariskiIdentityInverseImageIsoProjectionPushforward :
    (smallZariskiToBigZariskiMorphism B S S (𝟙 S)).inverseImage ≅
      (smallZariskiProjection B S).pushforward
```

**`AlgebraicGeometry.smallZariskiIdentityInverseImageSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiProjection.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiProjection.lean#L214). The attribute's comment: “the formula on sections”.

> For a big-site sheaf `G` and an open subscheme `U / S`, inverse image
> along `i_S` has sections canonically isomorphic to `G(U / S)`.

```lean
public noncomputable def smallZariskiIdentityInverseImageSections
    (G : Sheaf (BigZariskiOver.topology B S.obj S.property) (Type (u + 1)))
    (U : SmallZariski B S.obj S.property) :
    (((smallZariskiToBigZariskiMorphism B S S (𝟙 S)).inverseImage.obj G).obj.obj
      (Opposite.op U)) ≅ G.obj.obj (Opposite.op U.obj)
```

**`AlgebraicGeometry.preservesPullbacks_smallZariskiInclusion`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean#L116). The attribute's comment: “preservation of site pullbacks”.

> The full inclusion of the small Zariski category into the big Zariski category over `S`
> preserves fibre products.

```lean
public instance preservesPullbacks_smallZariskiInclusion :
    PreservesLimitsOfShape WalkingCospan (SmallZariski.inclusion B S hS)
```

**`AlgebraicGeometry.preservesTerminal_smallZariskiInclusion`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiLimits.lean#L207). The attribute's comment: “preservation of the final object”.

> The full inclusion of the small Zariski category into the big Zariski category over `S`
> carries `S / S` to the final object of the slice, hence preserves the final object.

```lean
public instance preservesTerminal_smallZariskiInclusion :
    PreservesLimitsOfShape (Discrete PEmpty.{1}) (SmallZariski.inclusion B S hS)
```

Declarations registered for the tag:

- [`CategoryTheory.ObjectProperty.fullyFaithfulι`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ObjectProperty.fullyFaithfulι#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiProjection.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiProjection.lean#L62) (StacksFrontier): “full faithfulness of the small-site inclusion”. References: SGA 3 I (1.1.1), “Hom\_C(X,Y) = Hom\_D(X,Y)”; SGA 6 II (3.0), “more general”.
- [`smallZariskiToBigZariskiFunctor_isCocontinuous`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=smallZariskiToBigZariskiFunctor_isCocontinuous#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiProjection.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiProjection.lean#L65) (StacksFrontier): “cocontinuity of the small-site inclusion”.

## Tag 04BS, a definition

[Tag 04BS](https://stacks.math.columbia.edu/tag/04BS) in the Stacks Project.

**`AlgebraicGeometry.smallZariskiProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiProjection.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiProjection.lean#L112). The attribute's comment: “restriction to the small Zariski site is its direct image”.

> The projection `π_S` from the big Zariski topos to the small one.

```lean
public noncomputable def smallZariskiProjection :
    MorphismOfTopoi
      (Sheaf (BigZariskiOver.topology B S.obj S.property) (Type (u + 1)))
      (Sheaf (SmallZariski.topology B S.obj S.property) (Type (u + 1)))
```

## Tag 0210, a lemma

[Tag 0210](https://stacks.math.columbia.edu/tag/0210) in the Stacks Project.

**`AlgebraicGeometry.bigZariskiMap_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean#L104). The attribute's comment: “cocontinuity”.

> **Stacks 0210.** Postcomposition with `f` is cocontinuous for the big Zariski
> topologies.

```lean
public instance bigZariskiMap_isCocontinuous :
    (Over.map f).IsCocontinuous
      (BigZariskiOver.topology B T.1 T.property)
      (BigZariskiOver.topology B S.1 S.property)
```

**`AlgebraicGeometry.bigZariskiMap_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean#L114). The attribute's comment: “continuity”.

> **Stacks 0210.** Postcomposition with `f` is continuous as well. This is the continuity
> used to identify inverse image with restriction and to construct the lower shriek.

```lean
public instance bigZariskiMap_isContinuous :
    (Over.map f).IsContinuous
      (BigZariskiOver.topology B T.1 T.property)
      (BigZariskiOver.topology B S.1 S.property)
```

**`AlgebraicGeometry.bigZariskiPullback_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean#L124). The attribute's comment: “continuity of the base-change right adjoint”.

> **Stacks 0210.** Base change along `f`, sending `U / S` to the canonical fibre product
> `U ×_S T / T`, is continuous.

```lean
public instance bigZariskiPullback_isContinuous :
    (Over.pullback f).IsContinuous
      (BigZariskiOver.topology B S.1 S.property)
      (BigZariskiOver.topology B T.1 T.property)
```

**`AlgebraicGeometry.bigZariskiMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean#L133). The attribute's comment: “the morphism of topoi”.

> **Stacks 0210.** The morphism of big Zariski topoi induced by postcomposition.

```lean
public noncomputable def bigZariskiMorphism :
    MorphismOfTopoi
      (Sheaf (BigZariskiOver.topology B T.1 T.property) (Type (u + 1)))
      (Sheaf (BigZariskiOver.topology B S.1 S.property) (Type (u + 1)))
```

**`AlgebraicGeometry.bigZariskiLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean#L151). The attribute's comment: “existence of lower shriek”.

> **Stacks 0210.** The sheaf pullback along postcomposition is the lower shriek, left
> adjoint to inverse image.

```lean
public noncomputable def bigZariskiLowerShriekAdjunction :
    (Over.map f).sheafPullback (Type (u + 1))
      (BigZariskiOver.topology B T.1 T.property)
      (BigZariskiOver.topology B S.1 S.property) ⊣
        (bigZariskiMorphism B T S f).inverseImage
```

**`AlgebraicGeometry.bigZariskiLowerShriek_preservesPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean#L168). The attribute's comment: “lower shriek preserves fibre products”.

> **Stacks 0210.** The lower shriek commutes with fibre products.

```lean
public instance bigZariskiLowerShriek_preservesPullbacks :
    PreservesLimitsOfShape WalkingCospan
      ((Over.map f).sheafPullback (Type (u + 1))
        (BigZariskiOver.topology B T.1 T.property)
        (BigZariskiOver.topology B S.1 S.property))
```

**`AlgebraicGeometry.bigZariskiLowerShriek_preservesEqualizers`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean#L183). The attribute's comment: “lower shriek preserves equalizers”.

> **Stacks 0210.** The lower shriek commutes with equalizers.

```lean
public instance bigZariskiLowerShriek_preservesEqualizers :
    PreservesLimitsOfShape WalkingParallelPair
      ((Over.map f).sheafPullback (Type (u + 1))
        (BigZariskiOver.topology B T.1 T.property)
        (BigZariskiOver.topology B S.1 S.property))
```

Declarations registered for the tag:

- [`CategoryTheory.Over.map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.map#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean#L76) (StacksFrontier): “the postcomposition functor”. References: EGA I (2.5.3); EGA I (2.5.4), “more general”; SGA 3 I (1.6); SGA 4 IV (5.5).
- [`CategoryTheory.Over.pullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.pullback#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean#L77) (StacksFrontier): “the base-change functor”. References: EGA I (3.3.7), “more general”; EGA IV (8.2.6); SGA 3 I (1.6); SGA 4 III (5.5); SGA 4 IV (5.2), “more general”; SGA 4 IV (5.5).
- [`CategoryTheory.Over.mapPullbackAdj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.mapPullbackAdj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean#L78) (StacksFrontier): “the base-change adjunction”.
- [`CategoryTheory.Functor.sheafPullbackCocontinuousIsoSheafPushforwardContinuous`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L139), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean#L79) (StacksFrontier): “the inverse-image formula”.
- [`CategoryTheory.Adjunction.sheafPushforwardCocontinuousIso`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/PushforwardAdjunction.lean#L70), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ZariskiCovering/BigZariskiMorphism.lean#L81) (StacksFrontier): “the direct-image formula and agreement of morphisms”.

## Tag 0211, a lemma

[Tag 0211](https://stacks.math.columbia.edu/tag/0211) in the Stacks Project.

**`AlgebraicGeometry.exists_smallZariskiBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiBaseChange.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiBaseChange.lean#L276). The attribute's comment: “f\_small”.

> There is a morphism of small Zariski sites from `T` to `S` whose underlying functor, after
> including both small sites into schemes over `T` and `S`, is naturally isomorphic to base change
> along `f`.

```lean
public theorem exists_smallZariskiBaseChange :
    ∃ F : SmallZariski B S.1 S.property ⥤
        SmallZariski B T.1 T.property,
      _root_.IsMorphismOfSites.{u + 1} F
        (SmallZariski.topology B S.1 S.property)
        (SmallZariski.topology B T.1 T.property) ∧
      Nonempty (F ⋙ smallSiteInSchemesOver B T ≅
        smallSiteInSchemesOver B S ⋙ Over.pullback (B.inclusion.map f))
```

**`AlgebraicGeometry.smallZariskiBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiBaseChange.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiBaseChange.lean#L296). The attribute's comment: “f\_small”.

> The continuous base-change functor on small Zariski sites.

```lean
public noncomputable def smallZariskiBaseChange :
    SmallZariski B S.1 S.property ⥤
      SmallZariski B T.1 T.property
```

**`AlgebraicGeometry.smallZariskiBaseChange_isMorphismOfSites_ringUniverse`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiRingedSiteHom.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiRingedSiteHom.lean#L171). The attribute's comment: “f\_small on small Zariski sites, at the universe of the structure rings”.

> **Stacks 0211 at the universe of the structure rings.**  Small Zariski base change along
> `f` defines a morphism of sites for sheaves of sets valued in the universe `u` of the sections
> of the structure sheaves.
>
> This is the input a morphism of ringed sites needs, and
> `AlgebraicGeometry.smallZariskiBaseChange_isMorphismOfSites` does not provide it: that one is
> stated for sheaves of sets in `Type (u + 1)`, the universe of the objects of the site.

```lean
public instance smallZariskiBaseChange_isMorphismOfSites_ringUniverse :
    IsMorphismOfSites.{u} (smallZariskiBaseChange B f)
      (SmallZariski.topology B S.1 S.property) (SmallZariski.topology B T.1 T.property)
```

**`AlgebraicGeometry.smallZariskiPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiSpaceFunctors.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiSpaceFunctors.lean#L146). The attribute's comment: “usual\_small\_functors”.

> Under the small-site equivalences, inverse image is the usual inverse image
> of sheaves on the underlying topological spaces.

```lean
public noncomputable def smallZariskiPullbackIso :
    (smallZariskiSheafEquiv B S.1 S.property).functor ⋙
      (Opens.map (B.inclusion.map f).base).sheafPullback (Type (u + 1))
        (Opens.grothendieckTopology ((B.inclusion.obj S).toPresheafedSpace : TopCat))
        (Opens.grothendieckTopology ((B.inclusion.obj T).toPresheafedSpace : TopCat)) ≅
      (smallZariskiBaseChange B f).sheafPullback (Type (u + 1))
      (SmallZariski.topology B S.1 S.property)
      (SmallZariski.topology B T.1 T.property) ⋙
      (smallZariskiSheafEquiv B T.1 T.property).functor
```

**`AlgebraicGeometry.smallZariskiPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiSpaceFunctors.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiSpaceFunctors.lean#L177). The attribute's comment: “usual\_small\_functors”.

> Under the small-site equivalences, direct image is the usual direct image
> of sheaves on the underlying topological spaces.

```lean
public noncomputable def smallZariskiPushforwardIso :
    (smallZariskiSheafEquiv B T.1 T.property).functor ⋙
      (Opens.map (B.inclusion.map f).base).sheafPushforwardContinuous (Type (u + 1))
        (Opens.grothendieckTopology ((B.inclusion.obj S).toPresheafedSpace : TopCat))
        (Opens.grothendieckTopology ((B.inclusion.obj T).toPresheafedSpace : TopCat)) ≅
      (smallZariskiBaseChange B f).sheafPushforwardContinuous
      (Type (u + 1))
      (SmallZariski.topology B S.1 S.property)
      (SmallZariski.topology B T.1 T.property) ⋙
      (smallZariskiSheafEquiv B S.1 S.property).functor
```

**`AlgebraicGeometry.smallZariskiBaseChange_comp_inclusionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiFactorization.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiFactorization.lean#L83). The attribute's comment: “commutative\_square”.

> The square of functors underlying the four morphisms of Zariski sites
> commutes up to a natural isomorphism.

```lean
public noncomputable def smallZariskiBaseChange_comp_inclusionIso :
    smallZariskiBaseChange B f ⋙
        SmallZariski.inclusion B T.1 T.property ≅
      SmallZariski.inclusion B S.1 S.property ⋙ Over.pullback f
```

**`AlgebraicGeometry.smallZariskiProjection_baseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiFactorization.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiFactorization.lean#L110). The attribute's comment: “commutative\_square”.

> The geometric morphisms satisfy `f_small ∘ π_T ≅ π_S ∘ f_big`;
> the isomorphism of inverse-image functors is natural in sheaves.

```lean
public noncomputable def smallZariskiProjection_baseChangeIso :
    ((smallZariskiMorphism B T S f).comp
      (smallZariskiProjection B T)).inverseImage ≅
    ((smallZariskiProjection B S).comp
      (bigZariskiMorphism B T S f)).inverseImage
```

**`AlgebraicGeometry.smallZariskiToBigZariskiMorphism_factor_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiFactorization.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiFactorization.lean#L163). The attribute's comment: “if\_factorization”.

> The direct image of `i_f` agrees naturally with that of `f_big ∘ i_T`.

```lean
public noncomputable def smallZariskiToBigZariskiMorphism_factor_pushforwardIso :
    (smallZariskiToBigZariskiMorphism B T S f).pushforward ≅
      ((bigZariskiMorphism B T S f).comp
        (smallZariskiToBigZariskiMorphism B T T (𝟙 T))).pushforward
```

**`AlgebraicGeometry.smallZariskiToBigZariskiMorphism_factor_inverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiFactorization.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiFactorization.lean#L210). The attribute's comment: “if\_factorization”.

> The inverse image of `i_f` agrees naturally with that of `f_big ∘ i_T`.

```lean
public noncomputable def smallZariskiToBigZariskiMorphism_factor_inverseImageIso :
    (smallZariskiToBigZariskiMorphism B T S f).inverseImage ≅
      ((bigZariskiMorphism B T S f).comp
        (smallZariskiToBigZariskiMorphism B T T (𝟙 T))).inverseImage
```

**`AlgebraicGeometry.smallZariskiMorphismIsoProjectionCompBig`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiFactorization.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiFactorization.lean#L226). The attribute's comment: “small\_factorization”.

> The small-site morphism factors through the two big Zariski topoi.

```lean
public noncomputable def smallZariskiMorphismIsoProjectionCompBig :
    (smallZariskiMorphism B T S f).inverseImage ≅
      ((smallZariskiProjection B S).comp
        ((bigZariskiMorphism B T S f).comp
          (smallZariskiToBigZariskiMorphism B T T (𝟙 T)))).inverseImage
```

**`AlgebraicGeometry.smallZariskiMorphismIsoProjectionCompInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiFactorization.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiFactorization.lean#L255). The attribute's comment: “small\_factorization”.

> The same morphism factors through `i_f` and the projection at `S`.

```lean
public noncomputable def smallZariskiMorphismIsoProjectionCompInclusion :
    (smallZariskiMorphism B T S f).inverseImage ≅
      ((smallZariskiProjection B S).comp
        (smallZariskiToBigZariskiMorphism B T S f)).inverseImage
```

## Tag 0212, a lemma

[Tag 0212](https://stacks.math.columbia.edu/tag/0212) in the Stacks Project.

**`AlgebraicGeometry.bigZariskiMorphism_comp_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiMorphismComposition.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiMorphismComposition.lean#L73). The attribute's comment: “the big sites, direct image”.

> **Stacks 0212.** The direct image of `g_big ∘ f_big` agrees naturally with that of
> `(g ∘ f)_big`.
>
> Both are read as restriction along slice base change, where the comparison is the canonical
> isomorphism `(U ×_Z Y) ×_Y X ≅ U ×_Z X` of iterated fibre products.

```lean
public noncomputable def bigZariskiMorphism_comp_pushforwardIso :
    ((bigZariskiMorphism B Y Z g).comp (bigZariskiMorphism B X Y f)).pushforward ≅
      (bigZariskiMorphism B X Z (f ≫ g)).pushforward
```

**`AlgebraicGeometry.bigZariskiMorphism_comp_inverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiMorphismComposition.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiMorphismComposition.lean#L95). The attribute's comment: “the big sites, inverse image”.

> **Stacks 0212.** The inverse image of `g_big ∘ f_big` agrees naturally with that of
> `(g ∘ f)_big`; the isomorphism is the mate of the direct-image comparison under the three
> geometric adjunctions.

```lean
public noncomputable def bigZariskiMorphism_comp_inverseImageIso :
    ((bigZariskiMorphism B Y Z g).comp (bigZariskiMorphism B X Y f)).inverseImage ≅
      (bigZariskiMorphism B X Z (f ≫ g)).inverseImage
```

**`AlgebraicGeometry.smallZariskiMorphism_comp_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiMorphismComposition.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiMorphismComposition.lean#L108). The attribute's comment: “the small sites, direct image”.

> **Stacks 0212.** The direct image of `g_small ∘ f_small` agrees naturally with that of
> `(g ∘ f)_small`, by the composition comparison of the underlying small-site base-change
> functors.

```lean
public noncomputable def smallZariskiMorphism_comp_pushforwardIso :
    ((smallZariskiMorphism B Y Z g).comp (smallZariskiMorphism B X Y f)).pushforward ≅
      (smallZariskiMorphism B X Z (f ≫ g)).pushforward
```

**`AlgebraicGeometry.smallZariskiMorphism_comp_inverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiMorphismComposition.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiMorphismComposition.lean#L121). The attribute's comment: “the small sites, inverse image”.

> **Stacks 0212.** The inverse image of `g_small ∘ f_small` agrees naturally with that of
> `(g ∘ f)_small`; the isomorphism is the mate of the direct-image comparison under the three
> sheaf adjunctions.

```lean
public noncomputable def smallZariskiMorphism_comp_inverseImageIso :
    ((smallZariskiMorphism B Y Z g).comp (smallZariskiMorphism B X Y f)).inverseImage ≅
      (smallZariskiMorphism B X Z (f ≫ g)).inverseImage
```

## Tag 0DD9, a lemma

[Tag 0DD9](https://stacks.math.columbia.edu/tag/0DD9) in the Stacks Project.

**`AlgebraicGeometry.bigZariskiBaseChange_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiPushforwardBaseChange.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiPushforwardBaseChange.lean#L122). The attribute's comment: “big-site equality”.

> Big-site inverse image commutes with big-site direct image around a
> cartesian square, naturally in the sheaf.

```lean
public noncomputable def bigZariskiBaseChange_pushforwardIso
    (h : IsPullback g' f' f g) :
    (bigZariskiMorphism B T S f).pushforward ⋙
        (bigZariskiMorphism B S' S g).inverseImage ≅
      (bigZariskiMorphism B T' T g').inverseImage ⋙
        (bigZariskiMorphism B T' S' f').pushforward
```

**`AlgebraicGeometry.smallZariskiBaseChange_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiPushforwardBaseChange.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/ZariskiPushforwardBaseChange.lean#L210). The attribute's comment: “small-site equality”.

> Restricting a big-site direct image to the small site of `S'` agrees,
> naturally, with restricting to the small site of `T'` and taking the small-site
> direct image.

```lean
public noncomputable def smallZariskiBaseChange_pushforwardIso
    (h : IsPullback g' f' f g) :
    (bigZariskiMorphism B T S f).pushforward ⋙
        (smallZariskiToBigZariskiMorphism B S' S g).inverseImage ≅
      (smallZariskiToBigZariskiMorphism B T' T g').inverseImage ⋙
        (smallZariskiBaseChange B f').sheafPushforwardContinuous
          (Type (u + 1))
          (SmallZariski.topology B S'.1 S'.property)
          (SmallZariski.topology B T'.1 T'.property)
```

## Tag 0213, a lemma

[Tag 0213](https://stacks.math.columbia.edu/tag/0213) in the Stacks Project.

**`AlgebraicGeometry.BigZariskiSheafData`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigZariski/CompatibleData.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigZariski/CompatibleData.lean#L45). The attribute's comment: “the compatible data”.

> A sheaf on each scheme over `S`, with compatible inverse-image comparisons.

```lean
public structure BigZariskiSheafData
```

**`AlgebraicGeometry.characterizeSheafBigZariski`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigZariski/Equivalence.lean, line 673](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigZariski/Equivalence.lean#L673). The attribute's comment: “equivalence of categories”.

> The canonical restriction functor is an equivalence of categories.

```lean
public noncomputable def characterizeSheafBigZariski :
    Sheaf (BigZariskiOver.topology B S hS) (Type (max u v)) ≌
      BigZariskiSheafData.{u, v} B S hS
```

**`AlgebraicGeometry.characterizeSheafBigZariski_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigZariski/Equivalence.lean, line 682](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigZariski/Equivalence.lean#L682). The attribute's comment: “canonicality of the equivalence”.

> The equivalence uses the canonical restriction functor, not an arbitrary
> equivalent object assignment.

```lean
public theorem characterizeSheafBigZariski_functor :
    (characterizeSheafBigZariski.{u, v} B S hS).functor =
      bigZariskiSheafRestriction.{u, v} B S hS
```

**`AlgebraicGeometry.bigZariskiSheafRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigZariski/Restriction.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigZariski/Restriction.lean#L48). The attribute's comment: “canonical restriction functor”.

> The canonical restriction of a big-site sheaf to all ordinary Zariski sites,
> including its comparison maps induced by big-site restrictions.

```lean
public noncomputable def bigZariskiSheafRestriction :
    Sheaf (BigZariskiOver.topology B S hS) (Type (max u v)) ⥤
      BigZariskiSheafData.{u, v} B S hS
```

**`AlgebraicGeometry.bigZariskiSheafRestriction_sectionEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigZariski/Restriction.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigZariski/Restriction.lean#L160). The attribute's comment: “canonical identification of sections”.

> Global sections of the canonical restriction at a scheme are the sections
> of the original big-site sheaf at that scheme.

```lean
public noncomputable def bigZariskiSheafRestriction_sectionEquiv
    (F : Sheaf (BigZariskiOver.topology B S hS) (Type (max u v)))
    (T : BigZariskiOver B S hS) :
    (((bigZariskiSheafRestriction.{u, v} B S hS).obj F).sheaf T).1.obj (op ⊤) ≃
      F.1.obj (op T)
```

**`AlgebraicGeometry.bigZariskiSheafRestriction_sectionEquiv_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigZariski/Restriction.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigZariski/Restriction.lean#L169). The attribute's comment: “naturality of section identification”.

> The identification of global sections is natural in the big-site sheaf.

```lean
public theorem bigZariskiSheafRestriction_sectionEquiv_naturality
    {F G : Sheaf (BigZariskiOver.topology B S hS) (Type (max u v))}
    (α : F ⟶ G) (T : BigZariskiOver B S hS)
    (s : (((bigZariskiSheafRestriction.{u, v} B S hS).obj F).sheaf T).1.obj (op ⊤)) :
  bigZariskiSheafRestriction_sectionEquiv B S hS G T
      (((((bigZariskiSheafRestriction.{u, v} B S hS).map α).app T).1.app (op ⊤)) s) =
    α.1.app (op T)
      (bigZariskiSheafRestriction_sectionEquiv B S hS F T s)
```

**`AlgebraicGeometry.bigZariskiSheafRestriction_pullback_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigZariski/Restriction.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigZariski/Restriction.lean#L222). The attribute's comment: “canonicality of pullback comparisons”.

> Under the canonical identifications of global sections, the pullback
> comparison is exactly the restriction map of the big-site sheaf. Applying this
> to every object, including open subschemes, controls the comparison on opens.

```lean
public theorem bigZariskiSheafRestriction_pullback_sections
    (F : Sheaf (BigZariskiOver.topology B S hS) (Type (max u v)))
    {T T' : BigZariskiOver B S hS} (f : T' ⟶ T)
    (s : F.1.obj (op T)) :
    let D := (bigZariskiSheafRestriction.{u, v} B S hS).obj F
    let ftop := (B.inclusion.map f.left).base
    let η := (TopCat.Sheaf.inverseImagePushforwardAdjunction.{u, v} ftop).unit.app
      (D.sheaf T)
    bigZariskiSheafRestriction_sectionEquiv B S hS F T'
      ((D.pullback f).1.app (op ⊤)
        (η.1.app (op ⊤)
          ((bigZariskiSheafRestriction_sectionEquiv B S hS F T).symm s))) =
      F.1.map f.op s
```

**`AlgebraicGeometry.bigZariskiSheafRestriction_sheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigZariski/Restriction.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigZariski/Restriction.lean#L284). The attribute's comment: “canonical sheaf on each scheme”.

> At each scheme over `S` the sheaf produced by canonical restriction is the inverse image
> of the big-site sheaf along the small-to-big morphism of topoi, transported to the space of
> that scheme.

```lean
public noncomputable def bigZariskiSheafRestriction_sheaf
    (F : Sheaf (BigZariskiOver.topology B S hS) (Type (max u v)))
    (T : BigZariskiOver B S hS) :
    ((bigZariskiSheafRestriction.{u, v} B S hS).obj F).sheaf T ≅
      canonicalSmallSheaf B S hS F T
```

**`AlgebraicGeometry.bigZariskiSheafRestriction_sheafNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigZariski/Restriction.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigZariski/Restriction.lean#L294). The attribute's comment: “naturality on opens and in the sheaf”.

> The componentwise identification is natural in the big-site sheaf; hence
> its maps on every open subset are the canonical restriction maps.

```lean
public noncomputable def bigZariskiSheafRestriction_sheafNatIso
    (T : BigZariskiOver B S hS) :
    bigZariskiSheafRestriction.{u, v} B S hS ⋙ BigZariskiSheafData.eval B S hS T ≅
      canonicalSmallSheafFunctor.{u, v} B S hS T
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 34.3, Tag 020N](https://stacks.math.columbia.edu/tag/020N)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
