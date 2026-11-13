---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsSyntomicCovering, AlgebraicGeometry.isSyntomicCovering_of_mem_smoothPrecoverage, AlgebraicGeometry.isSyntomicCovering_of_mem_etalePrecoverage, AlgebraicGeometry.isSyntomicCovering_of_mem_zariskiPrecoverage, AlgebraicGeometry.isSyntomicCovering_singleton_of_isIso, AlgebraicGeometry.IsSyntomicCovering.comp, AlgebraicGeometry.isSyntomicCovering_pullback, AlgebraicGeometry.exists_finite_affine_standardSyntomic_refinement
statement: formalized
proof: formalized
---

# 34.6 The syntomic topology

Section 34.6 of the Stacks Project, [Tag 0224](https://stacks.math.columbia.edu/tag/0224). 10 tags here are carried by 23 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0225, a definition

[Tag 0225](https://stacks.math.columbia.edu/tag/0225) in the Stacks Project.

**`AlgebraicGeometry.IsSyntomicCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/Coverings.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/Coverings.lean#L51).

> A family `fᵢ : Tᵢ ⟶ T` is a **syntomic covering** if every `fᵢ` is
> syntomic and their images cover `T`.

```lean
public abbrev IsSyntomicCovering {T : AlgebraicGeometry.Scheme.{u}}
    {I : Type v} (X : I → AlgebraicGeometry.Scheme.{u}) (f : ∀ i, X i ⟶ T) : Prop
```

## Tag 0226, a lemma

[Tag 0226](https://stacks.math.columbia.edu/tag/0226) in the Stacks Project.

**`AlgebraicGeometry.isSyntomicCovering_of_mem_smoothPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SyntomicTopology/Coverings.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SyntomicTopology/Coverings.lean#L46). The attribute's comment: “smooth coverings”.

> **Stacks Project, Tag 0226.** Every smooth covering is a syntomic covering.

```lean
public theorem isSyntomicCovering_of_mem_smoothPrecoverage
    {T : Scheme.{u}} {I : Type v} {X : I → Scheme.{u}} {f : ∀ i, X i ⟶ T}
    (hf : Presieve.ofArrows X f ∈ Scheme.precoverage (@Smooth.{u}) T) :
    IsSyntomicCovering X f
```

**`AlgebraicGeometry.isSyntomicCovering_of_mem_etalePrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SyntomicTopology/Coverings.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SyntomicTopology/Coverings.lean#L56). The attribute's comment: “étale coverings”.

> **Stacks Project, Tag 0226.** Every étale covering is a syntomic covering.

```lean
public theorem isSyntomicCovering_of_mem_etalePrecoverage
    {T : Scheme.{u}} {I : Type v} {X : I → Scheme.{u}} {f : ∀ i, X i ⟶ T}
    (hf : Presieve.ofArrows X f ∈ Scheme.etalePrecoverage T) :
    IsSyntomicCovering X f
```

**`AlgebraicGeometry.isSyntomicCovering_of_mem_zariskiPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SyntomicTopology/Coverings.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SyntomicTopology/Coverings.lean#L66). The attribute's comment: “Zariski coverings”.

> **Stacks Project, Tag 0226.** Every Zariski covering is a syntomic covering.

```lean
public theorem isSyntomicCovering_of_mem_zariskiPrecoverage
    {T : Scheme.{u}} {I : Type v} {X : I → Scheme.{u}} {f : ∀ i, X i ⟶ T}
    (hf : Presieve.ofArrows X f ∈ Scheme.zariskiPrecoverage T) :
    IsSyntomicCovering X f
```

## Tag 0227, a lemma

[Tag 0227](https://stacks.math.columbia.edu/tag/0227) in the Stacks Project.

**`AlgebraicGeometry.isSyntomicCovering_singleton_of_isIso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/Stability.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/Stability.lean#L54). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 0227, part (1).** An isomorphism, regarded as a singleton family, is
> a syntomic covering.

```lean
public lemma isSyntomicCovering_singleton_of_isIso {T' T : Scheme.{u}}
    (f : T' ⟶ T) [IsIso f] :
    IsSyntomicCovering (fun _ : Unit ↦ T') (fun _ ↦ f)
```

**`AlgebraicGeometry.IsSyntomicCovering.comp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/Stability.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/Stability.lean#L65). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 0227, part (2).** Refining every member of a syntomic covering by a
> syntomic covering gives another syntomic covering.

```lean
public lemma IsSyntomicCovering.comp {T : Scheme.{u}} {I : Type v}
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T)
    (hf : IsSyntomicCovering X f) {J : I → Type w}
    (Y : ∀ i, J i → Scheme.{u}) (g : ∀ i j, Y i j ⟶ X i)
    (hg : ∀ i, IsSyntomicCovering (Y i) (g i)) :
    IsSyntomicCovering
      (fun ij : Σ i, J i ↦ Y ij.1 ij.2)
      (fun ij ↦ g ij.1 ij.2 ≫ f ij.1)
```

**`AlgebraicGeometry.isSyntomicCovering_pullback`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/Stability.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/Stability.lean#L82). The attribute's comment: “part (3)”.

> **Stacks Project, Tag 0227, part (3).** Pulling a syntomic covering back along an arbitrary
> morphism gives a syntomic covering.

```lean
public lemma isSyntomicCovering_pullback {T : Scheme.{u}} {I : Type v}
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T) {T' : Scheme.{u}}
    (g : T' ⟶ T) (hf : IsSyntomicCovering X f) :
    IsSyntomicCovering
      (fun i ↦ pullback (f i) g)
      (fun i ↦ pullback.snd (f i) g)
```

## Tag 0228, a lemma

[Tag 0228](https://stacks.math.columbia.edu/tag/0228) in the Stacks Project.

**`AlgebraicGeometry.exists_finite_affine_standardSyntomic_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/StandardRefinement.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/StandardRefinement.lean#L163).

> **Stacks Project, Tag 0228.** A syntomic covering of an affine scheme has a finite
> refinement by affine schemes which are standard syntomic over the target; each member of the
> refinement is an open subscheme of a member of the original covering.

```lean
public theorem exists_finite_affine_standardSyntomic_refinement
    {T : Scheme.{u}} [IsAffine T] (U : PreZeroHypercover.{v} T)
    (hU : IsSyntomicCovering U.X U.f) :
    ∃ (V : T.AffineCover.{u} (@Syntomic.{u}))
        (refinement : V.cover.toPreZeroHypercover.Hom U),
      Finite V.I₀ ∧
        (∀ j, IsStandardSyntomic (V.f j)) ∧
          ∀ j, IsOpenImmersion (refinement.h₀ j)
```

## Tag 0229, a definition

[Tag 0229](https://stacks.math.columbia.edu/tag/0229) in the Stacks Project.

**`AlgebraicGeometry.IsStandardSyntomicCovering`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/Coverings.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/Coverings.lean#L58).

> A family `fᵢ : Uᵢ ⟶ T` is a **standard syntomic covering** if its
> indexing type is finite, its source and target schemes are affine, every `fᵢ`
> is standard syntomic, and their images cover `T`.

```lean
public structure IsStandardSyntomicCovering {T : Scheme.{u}} {I : Type v}
    (U : I → Scheme.{u}) (f : ∀ i, U i ⟶ T) : Prop
```

## Tag 03X1, a definition

[Tag 03X1](https://stacks.math.columbia.edu/tag/03X1) in the Stacks Project.

**`AlgebraicGeometry.BigSyntomicSite`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/BigSite.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/BigSite.lean#L69).

> **Stacks 03X1.** A big syntomic site consists of an initial set of
> schemes and syntomic coverings, a size cutoff containing those schemes, and
> a bounded collection of syntomic coverings containing the initial ones and
> satisfying the site axioms.

```lean
public structure BigSyntomicSite
```

## Tag 03X2, a lemma

[Tag 03X2](https://stacks.math.columbia.edu/tag/03X2) in the Stacks Project.

**`AlgebraicGeometry.BigSyntomicSite.exists_isCovering_tautologicallyEquivalent_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/ConstantSheaf.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/ConstantSheaf.lean#L61). The attribute's comment: “part (3)”.

> A Zariski covering of an object of a big syntomic site is tautologically equivalent to one
> of the site's own covering families.

```lean
public theorem BigSyntomicSite.exists_isCovering_tautologicallyEquivalent_openCover
    (B : BigSyntomicSite.{u}) (T : B.category) (𝒰 : Scheme.OpenCover.{w} T.1) :
    ∃ V : PreZeroHypercover.{u + 1} T,
      B.IsCovering ⟨T, V⟩ ∧
        PreZeroHypercover.TautologicallyEquivalent 𝒰.toPreZeroHypercover
          (V.map B.inclusion)
```

**`AlgebraicGeometry.exists_siteCovering_refining`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SyntomicTopology/SiteRefinement.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SyntomicTopology/SiteRefinement.lean#L78). The attribute's comment: “site\_refinement”.

> Every syntomic covering of an object of a big syntomic site admits a
> refinement by a covering in the site.

```lean
public theorem exists_siteCovering_refining
    (B : BigSyntomicSite.{u}) (T : B.category)
    (E : PreZeroHypercover.{v} (B.inclusion.obj T))
    (hE : IsSyntomicCovering E.X E.f) :
    ∃ 𝒰 : PreZeroHypercover.{u + 1} T,
      B.IsCovering ⟨T, 𝒰⟩ ∧
        Nonempty ((𝒰.map B.inclusion).Hom E)
```

**`AlgebraicGeometry.BigSyntomicSite.exists_isCovering_tautologicallyEquivalent_standardCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SyntomicTopology/SiteRefinement.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SyntomicTopology/SiteRefinement.lean#L132). The attribute's comment: “part (2)”.

> A standard syntomic covering of an object of a big syntomic site is tautologically
> equivalent to a covering belonging to the site.

```lean
public theorem BigSyntomicSite.exists_isCovering_tautologicallyEquivalent_standardCovering
    (B : BigSyntomicSite.{u}) (T : B.category)
    (U : PreZeroHypercover.{v} (B.inclusion.obj T))
    (hU : IsStandardSyntomicCovering U.X U.f) :
    ∃ V : PreZeroHypercover.{u + 1} T,
      B.IsCovering ⟨T, V⟩ ∧
        PreZeroHypercover.TautologicallyEquivalent U (V.map B.inclusion)
```

## Tag 03X3, a definition

[Tag 03X3](https://stacks.math.columbia.edu/tag/03X3) in the Stacks Project.

**`AlgebraicGeometry.BigSyntomicOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/BigSiteOver.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/BigSiteOver.lean#L48). The attribute's comment: “part (1), category”.

> The big syntomic category over `S` is the slice of the chosen big syntomic category at `S`.

```lean
public abbrev BigSyntomicOver
```

**`AlgebraicGeometry.BigSyntomicOver.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/BigSiteOver.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/BigSiteOver.lean#L62). The attribute's comment: “part (1), coverings”.

> A family in the slice is covering precisely when its underlying family is covering in the
> chosen big syntomic site.

```lean
public abbrev IsCovering (E : Covering (BigSyntomicOver B S hS)) : Prop
```

**`AlgebraicGeometry.BigAffineSyntomic`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/BigSiteOver.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/BigSiteOver.lean#L78). The attribute's comment: “part (2), category”.

> The big affine syntomic category over `S` is the full subcategory of the big syntomic category
> over `S` on affine source schemes.

```lean
public abbrev BigAffineSyntomic
```

**`AlgebraicGeometry.BigAffineSyntomic.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/BigSiteOver.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/BigSiteOver.lean#L103). The attribute's comment: “part (2), coverings”.

> A family in the big affine syntomic site is covering exactly when it is covering in the
> localized big syntomic site and is a standard syntomic covering of schemes.

```lean
public abbrev IsCovering (E : Covering (BigAffineSyntomic B S hS)) : Prop
```

## Tag 06VD, a lemma

[Tag 06VD](https://stacks.math.columbia.edu/tag/06VD) in the Stacks Project.

**`AlgebraicGeometry.BigAffineSyntomic.inclusion_isSpecialCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/AffineSyntomicDenseSubsite.lean, line 352](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/AffineSyntomicDenseSubsite.lean#L352).

> **Stacks 06VD.** The inclusion of affine objects over `S` into the big
> syntomic site over `S` is special cocontinuous. Its dense-subsite component
> gives the induced equivalence of topoi.

```lean
public theorem BigAffineSyntomic.inclusion_isSpecialCocontinuous
    (B : BigSyntomicSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) :
    IsSpecialCocontinuous
      (BigAffineSyntomic.topology B S hS)
      (BigSyntomicOver.topology B S hS)
      (BigAffineSyntomic.inclusion B S hS)
```

## Tag 04HD, a lemma

[Tag 04HD](https://stacks.math.columbia.edu/tag/04HD) in the Stacks Project.

**`AlgebraicGeometry.bigSyntomicMorphismOfTopoi`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean#L111). The attribute's comment: “big\_syntomic\_morphism”.

> **Stacks Project, Tag 04HD.** The big syntomic morphism of topoi attached
> to `f : T ⟶ S` in a chosen big syntomic site. Its defining functor sends
> `V ⟶ T` to the composite `V ⟶ T ⟶ S`.

```lean
public noncomputable def bigSyntomicMorphismOfTopoi : MorphismOfTopoi
    (Sheaf (BigSyntomicOver.topology B T.obj T.property) (Type (u + 1)))
    (Sheaf (BigSyntomicOver.topology B S.obj S.property) (Type (u + 1)))
```

**`AlgebraicGeometry.bigSyntomicMorphismPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean#L133). The attribute's comment: “same\_morphism”.

> **Stacks Project, Tag 04HD.** The big syntomic morphism of topoi defined by postcomposition
> along `f` is the morphism of topoi induced by the continuous base-change functor
> `Over.pullback f`: their direct images are canonically isomorphic.

```lean
public noncomputable def bigSyntomicMorphismPushforwardIso :
    (bigSyntomicMorphismOfTopoi B f).pushforward ≅
      (Over.pullback f).sheafPushforwardContinuous (Type (u + 1))
        (BigSyntomicOver.topology B S.obj S.property)
        (BigSyntomicOver.topology B T.obj T.property)
```

**`AlgebraicGeometry.bigSyntomicLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean#L143). The attribute's comment: “lower\_shriek”.

> **Stacks Project, Tag 04HD.** The lower shriek on big syntomic sheaves is left adjoint to
> inverse image.

```lean
public noncomputable def bigSyntomicLowerShriekAdjunction :
    (Over.map f).sheafPullback (Type (u + 1))
      (BigSyntomicOver.topology B T.obj T.property)
      (BigSyntomicOver.topology B S.obj S.property) ⊣
        (bigSyntomicMorphismOfTopoi B f).inverseImage
```

**`AlgebraicGeometry.bigSyntomicLowerShriek_preservesPullbacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean#L160). The attribute's comment: “lower\_shriek”.

> **Stacks Project, Tag 04HD.** The lower shriek preserves fibre products.

```lean
public theorem bigSyntomicLowerShriek_preservesPullbacks :
    PreservesLimitsOfShape WalkingCospan
      ((Over.map f).sheafPullback (Type (u + 1))
        (BigSyntomicOver.topology B T.obj T.property)
        (BigSyntomicOver.topology B S.obj S.property))
```

**`AlgebraicGeometry.bigSyntomicLowerShriek_preservesEqualizers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean#L171). The attribute's comment: “lower\_shriek”.

> **Stacks Project, Tag 04HD.** The lower shriek preserves equalizers.

```lean
public theorem bigSyntomicLowerShriek_preservesEqualizers :
    PreservesLimitsOfShape WalkingParallelPair
      ((Over.map f).sheafPullback (Type (u + 1))
        (BigSyntomicOver.topology B T.obj T.property)
        (BigSyntomicOver.topology B S.obj S.property))
```

Declarations registered for the tag:

- [`CategoryTheory.GrothendieckTopology.instIsCocontinuousOverMapOver`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.instIsCocontinuousOverMapOver#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean#L63) (StacksFrontier): “cocontinuity”.
- [`CategoryTheory.Over.mapPullbackAdj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.mapPullbackAdj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean#L66) (StacksFrontier): “right\_adjoint”.
- [`CategoryTheory.GrothendieckTopology.instIsContinuousOverPullbackOver`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.instIsContinuousOverPullbackOver#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean#L67) (StacksFrontier): “right\_adjoint”.
- [`CategoryTheory.Functor.sheafPullbackCocontinuousIsoSheafPushforwardContinuous`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L139), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean#L70) (StacksFrontier): “inverse\_image”.
- [`CategoryTheory.Functor.sheafPushforwardCocontinuousIsoRestriction`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L229), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Syntomic/MorphismOfTopoi.lean#L73) (StacksFrontier): “direct\_image”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 34.6, Tag 0224](https://stacks.math.columbia.edu/tag/0224)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
