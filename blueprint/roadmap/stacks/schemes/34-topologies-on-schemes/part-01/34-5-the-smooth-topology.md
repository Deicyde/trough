---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.smoothPrecoverage, AlgebraicGeometry.Scheme.zariskiPrecoverage_le_smoothPrecoverage, AlgebraicGeometry.Scheme.etalePrecoverage_le_smoothPrecoverage, AlgebraicGeometry.Scheme.singleton_mem_smoothPrecoverage_of_isIso, AlgebraicGeometry.Scheme.ofArrows_comp_mem_smoothPrecoverage, AlgebraicGeometry.Scheme.ofArrows_pullback_mem_smoothPrecoverage, AlgebraicGeometry.exists_finite_affine_standardSmooth_refinement, AlgebraicGeometry.IsStandardSmoothCovering
statement: formalized
proof: formalized
---

# 34.5 The smooth topology

Section 34.5 of the Stacks Project, [Tag 021Y](https://stacks.math.columbia.edu/tag/021Y). 10 tags here are carried by 29 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 021Z, a definition

[Tag 021Z](https://stacks.math.columbia.edu/tag/021Z) in the Stacks Project.

**`AlgebraicGeometry.Scheme.smoothPrecoverage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SmoothAndStandardEtaleCoverings.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SmoothAndStandardEtaleCoverings.lean#L74).

> The smooth precoverage on the category of schemes: its covering families are the jointly
> surjective families of smooth morphisms.

```lean
public def smoothPrecoverage : Precoverage Scheme.{u}
```

## Tag 0220, a lemma

[Tag 0220](https://stacks.math.columbia.edu/tag/0220) in the Stacks Project.

**`AlgebraicGeometry.Scheme.zariskiPrecoverage_le_smoothPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SmoothCoverings.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SmoothCoverings.lean#L55). The attribute's comment: “Zariski coverings”.

> Every Zariski covering is a smooth covering.

```lean
public theorem zariskiPrecoverage_le_smoothPrecoverage :
    zariskiPrecoverage.{u} ≤ smoothPrecoverage
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.etalePrecoverage_le_smoothPrecoverage`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmoothEqualsEtale.lean#L86), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/SmoothCoverings.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SmoothCoverings.lean#L97) (StacksFrontier): “étale coverings”.

## Tag 0221, a lemma

[Tag 0221](https://stacks.math.columbia.edu/tag/0221) in the Stacks Project.

**`AlgebraicGeometry.Scheme.singleton_mem_smoothPrecoverage_of_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SmoothCoverings.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SmoothCoverings.lean#L61). The attribute's comment: “part (1)”.

> The singleton family of an isomorphism `T' ⟶ T` is a smooth covering of `T`.

```lean
public theorem singleton_mem_smoothPrecoverage_of_isIso {T' T : Scheme.{u}} (f : T' ⟶ T)
    [IsIso f] : Presieve.singleton f ∈ smoothPrecoverage T
```

**`AlgebraicGeometry.Scheme.ofArrows_comp_mem_smoothPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SmoothCoverings.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SmoothCoverings.lean#L72). The attribute's comment: “part (2)”.

> If `{fᵢ : Tᵢ ⟶ T}` is a smooth covering and `{gᵢⱼ : Tᵢⱼ ⟶ Tᵢ}` is a smooth covering of each
> `Tᵢ`, then the composite family `{gᵢⱼ ≫ fᵢ : Tᵢⱼ ⟶ T}` is a smooth covering.

```lean
public theorem ofArrows_comp_mem_smoothPrecoverage {I : Type w} {T : Scheme.{u}}
    {T' : I → Scheme.{u}} (f : ∀ i, T' i ⟶ T)
    (hf : Presieve.ofArrows T' f ∈ smoothPrecoverage T) {J : I → Type w'}
    {T'' : ∀ i, J i → Scheme.{u}} (g : ∀ i j, T'' i j ⟶ T' i)
    (hg : ∀ i, Presieve.ofArrows (T'' i) (g i) ∈ smoothPrecoverage (T' i)) :
    Presieve.ofArrows (fun p : Σ i, J i ↦ T'' p.1 p.2) (fun p ↦ g p.1 p.2 ≫ f p.1) ∈
      smoothPrecoverage T
```

**`AlgebraicGeometry.Scheme.ofArrows_pullback_mem_smoothPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SmoothCoverings.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SmoothCoverings.lean#L84). The attribute's comment: “part (3)”.

> If `{fᵢ : Tᵢ ⟶ T}` is a smooth covering and `g : T' ⟶ T` is a morphism of schemes, then the
> family of first projections `{T' ×_T Tᵢ ⟶ T'}` is a smooth covering.

```lean
public theorem ofArrows_pullback_mem_smoothPrecoverage {I : Type w} {T T' : Scheme.{u}}
    {Tᵢ : I → Scheme.{u}} (f : ∀ i, Tᵢ i ⟶ T)
    (hf : Presieve.ofArrows Tᵢ f ∈ smoothPrecoverage T) (g : T' ⟶ T) :
    Presieve.ofArrows (fun i ↦ pullback g (f i)) (fun i ↦ pullback.fst g (f i)) ∈
      smoothPrecoverage T'
```

## Tag 0222, a lemma

[Tag 0222](https://stacks.math.columbia.edu/tag/0222) in the Stacks Project.

**`AlgebraicGeometry.exists_finite_affine_standardSmooth_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/StandardRefinement.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/StandardRefinement.lean#L75).

> A smooth covering of an affine scheme has a finite refinement by affine schemes which are
> standard smooth over the target; each member of the refinement is an open subscheme of a member of
> the original covering.

```lean
public theorem exists_finite_affine_standardSmooth_refinement {T : Scheme.{u}} [IsAffine T]
    (U : T.Cover.{v} (Scheme.precoverage (@Smooth.{u}))) :
    ∃ (V : T.AffineCover.{u} (@Smooth.{u}))
        (refinement : V.cover.toPreZeroHypercover.Hom U.toPreZeroHypercover),
      Finite V.I₀ ∧
        (∀ j, IsStandardSmooth (V.f j)) ∧
          ∀ j, IsOpenImmersion (refinement.h₀ j)
```

## Tag 0223, a definition

[Tag 0223](https://stacks.math.columbia.edu/tag/0223) in the Stacks Project.

**`AlgebraicGeometry.IsStandardSmoothCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/StandardCovering.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/StandardCovering.lean#L39).

> A finite family `fᵢ : Uᵢ ⟶ T` of morphisms between affine schemes is a
> **standard smooth covering** if every `fᵢ` is standard smooth and their images
> cover `T`.

```lean
public abbrev IsStandardSmoothCovering {T : Scheme.{u}} [IsAffine T]
    {I : Type v} [Finite I] (U : I → Scheme.{u}) [∀ i, IsAffine (U i)]
    (f : ∀ i, U i ⟶ T) : Prop
```

## Tag 03WY, a definition

[Tag 03WY](https://stacks.math.columbia.edu/tag/03WY) in the Stacks Project.

**`AlgebraicGeometry.BigSmoothSite`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/BigSite.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/BigSite.lean#L69).

> A big smooth site.
>
> Besides the cutoff category and its selected bounded smooth coverings, this structure records
> the initial sets `S₀` and `Cov₀` and all the conditions imposed by the size-cutoff and
> set-sized-covering constructions.

```lean
public structure BigSmoothSite
```

## Tag 03WZ, a lemma

[Tag 03WZ](https://stacks.math.columbia.edu/tag/03WZ) in the Stacks Project.

**`AlgebraicGeometry.exists_covering_refining_smooth_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/BigSiteCoverings.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/BigSiteCoverings.lean#L153). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 03WZ, part (1).** Every smooth covering family of an object of a
> big smooth site is refined by a covering family belonging to the site.

```lean
public theorem exists_covering_refining_smooth_cover
    (B : BigSmoothSite.{u}) {T : B.category}
    (U : PreZeroHypercover.{v} ((ObjectProperty.ι _).obj T))
    (hU : U.presieve₀ ∈ Scheme.precoverage (@Smooth.{u}) ((ObjectProperty.ι _).obj T)) :
    ∃ V : PreZeroHypercover.{u + 1} T,
      B.IsCovering ⟨T, V⟩ ∧ Nonempty ((V.map (ObjectProperty.ι _)).Hom U)
```

**`AlgebraicGeometry.exists_covering_tautologicallyEquivalent_standardSmoothCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/BigSiteCoverings.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/BigSiteCoverings.lean#L193). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 03WZ, part (2).** A standard smooth covering of an object of a
> big smooth site is tautologically equivalent to a covering family belonging to the site.

```lean
public theorem exists_covering_tautologicallyEquivalent_standardSmoothCover
    (B : BigSmoothSite.{u}) {T : B.category}
    [IsAffine ((ObjectProperty.ι _).obj T)]
    (U : PreZeroHypercover.{v} ((ObjectProperty.ι _).obj T)) [Finite U.I₀]
    [∀ i, IsAffine (U.X i)]
    (hU : IsStandardSmoothCovering (fun i ↦ U.X i) (fun i ↦ U.f i)) :
    ∃ V : PreZeroHypercover.{u + 1} T,
      B.IsCovering ⟨T, V⟩ ∧
        PreZeroHypercover.TautologicallyEquivalent U (V.map (ObjectProperty.ι _))
```

**`AlgebraicGeometry.exists_covering_tautologicallyEquivalent_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/BigSiteCoverings.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/BigSiteCoverings.lean#L217). The attribute's comment: “part (3)”.

> **Stacks Project, Tag 03WZ, part (3).** A Zariski covering of an object of a big smooth
> site is tautologically equivalent to a covering family belonging to the site.

```lean
public theorem exists_covering_tautologicallyEquivalent_openCover
    (B : BigSmoothSite.{u}) (T : B.category)
    (U : ((ObjectProperty.ι _).obj T).OpenCover.{v}) :
    ∃ V : PreZeroHypercover.{u + 1} T,
      B.IsCovering ⟨T, V⟩ ∧
        PreZeroHypercover.TautologicallyEquivalent U.toPreZeroHypercover
          (V.map (ObjectProperty.ι _))
```

## Tag 03X0, a definition

[Tag 03X0](https://stacks.math.columbia.edu/tag/03X0) in the Stacks Project.

**`AlgebraicGeometry.BigSmoothOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/BigSiteOver.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/BigSiteOver.lean#L46). The attribute's comment: “part (1), category”.

> The big smooth category over `S`: the slice of the chosen big smooth category over `S`.

```lean
public abbrev BigSmoothOver
```

**`AlgebraicGeometry.BigSmoothOver.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/BigSiteOver.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/BigSiteOver.lean#L61). The attribute's comment: “part (1), coverings”.

> A family in the big smooth category over `S` is covering precisely when its underlying family
> is a covering in the chosen big smooth site.

```lean
public abbrev IsCovering (E : Covering (BigSmoothOver B S hS)) : Prop
```

**`AlgebraicGeometry.BigAffineSmooth`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/BigSiteOver.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/BigSiteOver.lean#L79). The attribute's comment: “part (2), category”.

> The big affine smooth category over `S`: the full subcategory of the big smooth category over
> `S` consisting of the objects whose underlying scheme is affine.

```lean
public abbrev BigAffineSmooth
```

**`AlgebraicGeometry.BigAffineSmooth.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/BigSiteOver.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/BigSiteOver.lean#L108). The attribute's comment: “part (2), coverings”.

> A family in the big affine smooth category over `S` is covering precisely when its image in the
> big smooth category over `S` is covering and its underlying family is a standard smooth
> covering.

```lean
public abbrev IsCovering (E : Covering (BigAffineSmooth B S hS)) : Prop
```

## Tag 06VC, a lemma

[Tag 06VC](https://stacks.math.columbia.edu/tag/06VC) in the Stacks Project.

**`AlgebraicGeometry.BigAffineSmooth.inclusion_isSpecialCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/AffineDenseSubsite.lean, line 333](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/AffineDenseSubsite.lean#L333).

> **Stacks 06VC.** The inclusion of the big affine smooth site over a scheme
> into its big smooth site is special cocontinuous. Its dense-subsite component
> is precisely the datum which gives the induced equivalence of topoi.

```lean
public theorem BigAffineSmooth.inclusion_isSpecialCocontinuous
    (B : BigSmoothSite.{u}) (S : Scheme.{u}) (hS : S.size < B.cutoff) :
    IsSpecialCocontinuous
      (BigAffineSmooth.topology B S hS)
      (BigSmoothOver.topology B S hS)
      (BigAffineSmooth.inclusion B S hS)
```

## Tag 04HC, a lemma

[Tag 04HC](https://stacks.math.columbia.edu/tag/04HC) in the Stacks Project.

**`AlgebraicGeometry.bigSmoothOverMap_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean#L108). The attribute's comment: “cocontinuity”.

> The functor `V / T ↦ V / S` between the big smooth sites over `T` and over `S`, given by
> composing the structure morphism with `f`, is cocontinuous.

```lean
public instance bigSmoothOverMap_isCocontinuous
    (B : BigSmoothSite.{u}) {T S : B.category} (f : T ⟶ S) :
    (Over.map f).IsCocontinuous
      (BigSmoothOver.topology B T.obj T.property)
      (BigSmoothOver.topology B S.obj S.property)
```

**`AlgebraicGeometry.bigSmoothOverMap_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean#L118). The attribute's comment: “continuity”.

> The functor `V / T ↦ V / S` between the big smooth sites over `T` and over `S` is
> continuous.

```lean
public instance bigSmoothOverMap_isContinuous
    (B : BigSmoothSite.{u}) {T S : B.category} (f : T ⟶ S) :
    (Over.map f).IsContinuous
      (BigSmoothOver.topology B T.obj T.property)
      (BigSmoothOver.topology B S.obj S.property)
```

**`AlgebraicGeometry.bigSmoothOverMapPullbackAdj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean#L128). The attribute's comment: “continuous\_right\_adjoint”.

> Base change along `f`, the functor `(U → S) ↦ (U ×_S T → T)` between the big smooth sites
> over `S` and over `T`, is right adjoint to composition with `f`.

```lean
public noncomputable def bigSmoothOverMapPullbackAdj
    (B : BigSmoothSite.{u}) {T S : B.category} (f : T ⟶ S) :
    (Over.map f : BigSmoothOver B T.obj T.property ⥤ BigSmoothOver B S.obj S.property) ⊣
      Over.pullback f
```

**`AlgebraicGeometry.bigSmoothOverPullback_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean#L136). The attribute's comment: “continuous\_right\_adjoint”.

> Base change along `f` is continuous for the two localized big smooth topologies.

```lean
public instance bigSmoothOverPullback_isContinuous
    (B : BigSmoothSite.{u}) {T S : B.category} (f : T ⟶ S) :
    (Over.pullback f).IsContinuous
      (BigSmoothOver.topology B S.obj S.property)
      (BigSmoothOver.topology B T.obj T.property)
```

**`AlgebraicGeometry.bigSmoothMorphismOfTopoi`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean#L146). The attribute's comment: “big\_smooth\_morphism\_of\_topoi”.

> The big smooth morphism of topoi associated to a morphism `f : T ⟶ S` in a big smooth site,
> induced by the cocontinuous functor sending `V ⟶ T` to the composite `V ⟶ T ⟶ S`.

```lean
public noncomputable def bigSmoothMorphismOfTopoi
    (B : BigSmoothSite.{u}) {T S : B.category} (f : T ⟶ S) :
    MorphismOfTopoi
      (Sheaf (BigSmoothOver.topology B T.obj T.property) (Type (u + 1)))
      (Sheaf (BigSmoothOver.topology B S.obj S.property) (Type (u + 1)))
```

**`AlgebraicGeometry.bigSmoothMorphismOfTopoiPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean#L169). The attribute's comment: “agreement”.

> The direct image of the big smooth morphism of topoi attached to postcomposition along `f`
> is isomorphic to the direct image along the continuous base-change functor `Over.pullback f`.

```lean
public noncomputable def bigSmoothMorphismOfTopoiPushforwardIso
    (B : BigSmoothSite.{u}) {T S : B.category} (f : T ⟶ S) :
    (bigSmoothMorphismOfTopoi B f).pushforward ≅
      (Over.pullback f).sheafPushforwardContinuous (Type (u + 1))
        (BigSmoothOver.topology B S.obj S.property)
        (BigSmoothOver.topology B T.obj T.property)
```

**`AlgebraicGeometry.bigSmoothMorphismOfTopoiPullbackAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean#L180). The attribute's comment: “agreement”.

> The inverse image of the big smooth morphism of topoi is left adjoint to restriction along
> base change.

```lean
public noncomputable def bigSmoothMorphismOfTopoiPullbackAdjunction
    (B : BigSmoothSite.{u}) {T S : B.category} (f : T ⟶ S) :
    (bigSmoothMorphismOfTopoi B f).inverseImage ⊣
      (Over.pullback f).sheafPushforwardContinuous (Type (u + 1))
        (BigSmoothOver.topology B S.obj S.property)
        (BigSmoothOver.topology B T.obj T.property)
```

**`AlgebraicGeometry.bigSmoothMorphismOfTopoiInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean#L200). The attribute's comment: “agreement”.

> The inverse image of the big smooth morphism of topoi is isomorphic to the left adjoint of
> restriction along base change.

```lean
public noncomputable def bigSmoothMorphismOfTopoiInverseImageIso
    (B : BigSmoothSite.{u}) {T S : B.category} (f : T ⟶ S) :
    (bigSmoothMorphismOfTopoi B f).inverseImage ≅
      ((Over.pullback f).sheafPushforwardContinuous (Type (u + 1))
        (BigSmoothOver.topology B S.obj S.property)
        (BigSmoothOver.topology B T.obj T.property)).leftAdjoint
```

**`AlgebraicGeometry.bigSmoothInverseImageObjIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean#L212). The attribute's comment: “inverse\_image”.

> The sections of an inverse image on `U / T` are the sections of the sheaf on `U / S`:
> `f⁻¹(G)(U / T) = G(U / S)`.

```lean
public noncomputable def bigSmoothInverseImageObjIso
    (B : BigSmoothSite.{u}) {T S : B.category} (f : T ⟶ S)
    (G : Sheaf (BigSmoothOver.topology B S.obj S.property) (Type (u + 1))) (U : Over T) :
    ((bigSmoothMorphismOfTopoi B f).inverseImage.obj G).obj.obj (Opposite.op U) ≅
      G.obj.obj (Opposite.op (Over.mk (U.hom ≫ f)))
```

**`AlgebraicGeometry.bigSmoothPushforwardObjIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean#L224). The attribute's comment: “direct\_image”.

> The sections of a direct image on `U / S` are the sections of the sheaf on the base change
> `U ×_S T / T`: `f_*(F)(U / S) = F(U ×_S T / T)`.

```lean
public noncomputable def bigSmoothPushforwardObjIso
    (B : BigSmoothSite.{u}) {T S : B.category} (f : T ⟶ S)
    (F : Sheaf (BigSmoothOver.topology B T.obj T.property) (Type (u + 1))) (U : Over S) :
    ((bigSmoothMorphismOfTopoi B f).pushforward.obj F).obj.obj (Opposite.op U) ≅
      F.obj.obj (Opposite.op (Over.mk (pullback.snd U.hom f)))
```

**`AlgebraicGeometry.bigSmoothInverseImage_isRightAdjoint`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean#L236). The attribute's comment: “left\_adjoint”.

> The inverse image of a big smooth morphism of topoi has a left adjoint.

```lean
public noncomputable instance bigSmoothInverseImage_isRightAdjoint
    (B : BigSmoothSite.{u}) {T S : B.category} (f : T ⟶ S) :
    (bigSmoothMorphismOfTopoi B f).inverseImage.IsRightAdjoint
```

**`AlgebraicGeometry.bigSmoothLowerShriek_preservesPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean#L268). The attribute's comment: “shriek\_limits”.

> The lower shriek of a big smooth morphism of topoi preserves fibre products.

```lean
public noncomputable instance bigSmoothLowerShriek_preservesPullbacks
    (B : BigSmoothSite.{u}) {T S : B.category} (f : T ⟶ S) :
    PreservesLimitsOfShape WalkingCospan
      (bigSmoothMorphismOfTopoi B f).inverseImage.leftAdjoint
```

**`AlgebraicGeometry.bigSmoothLowerShriek_preservesEqualizers`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean#L276). The attribute's comment: “shriek\_limits”.

> The lower shriek of a big smooth morphism of topoi preserves equalizers.

```lean
public noncomputable instance bigSmoothLowerShriek_preservesEqualizers
    (B : BigSmoothSite.{u}) {T S : B.category} (f : T ⟶ S) :
    PreservesLimitsOfShape WalkingParallelPair
      (bigSmoothMorphismOfTopoi B f).inverseImage.leftAdjoint
```

Declarations registered for the tag:

- [`CategoryTheory.Over.mapPullbackAdj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.mapPullbackAdj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/SliceAdjunction.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/SliceAdjunction.lean#L64) (StacksFrontier): “continuous\_right\_adjoint”.
- [`CategoryTheory.GrothendieckTopology.instIsContinuousOverPullbackOver`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.instIsContinuousOverPullbackOver#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/SliceAdjunction.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/SliceAdjunction.lean#L65) (StacksFrontier): “continuous\_right\_adjoint”.
- [`CategoryTheory.GrothendieckTopology.instIsCocontinuousOverMapOver`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.instIsCocontinuousOverMapOver#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/SliceAdjunction.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/SliceAdjunction.lean#L68) (StacksFrontier): “cocontinuity”.
- [`CategoryTheory.Functor.sheafPushforwardCocontinuousIsoRestriction`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L229), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean#L82) (StacksFrontier): “direct\_image”.
- [`CategoryTheory.Functor.sheafPullbackCocontinuousIsoSheafPushforwardContinuous`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L139), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Smooth/MorphismOfTopoi.lean#L85) (StacksFrontier): “inverse\_image”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 34.5, Tag 021Y](https://stacks.math.columbia.edu/tag/021Y)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
