---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsEtaleCovering, AlgebraicGeometry.Space.isEtaleCovering_of_isZariskiCovering, AlgebraicGeometry.Space.isEtaleCovering_comp, AlgebraicGeometry.Space.isEtaleCovering_pullback, AlgebraicGeometry.Space.isEtaleCovering_of_isIso, AlgebraicGeometry.Space.exists_isEtaleCovering_refining_isSmoothCovering, AlgebraicGeometry.Space.exists_isEtaleCovering_representable_refining_isSmoothCovering, AlgebraicGeometry.BigEtaleSpaceSite
statement: formalized
proof: formalized
---

# 73.4 Étale topology

Section 73.4 of the Stacks Project, [Tag 03YC](https://stacks.math.columbia.edu/tag/03YC). 14 tags here are carried by 55 declarations of the repository (all in StacksFrontier) and 20 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 041E, a definition

[Tag 041E](https://stacks.math.columbia.edu/tag/041E) in the Stacks Project.

**`AlgebraicGeometry.Space.IsEtaleCovering`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean#L344).

> **Stacks 041E.** A family of morphisms of algebraic spaces over `S` with common target
> is an *étale covering* when every member is étale and the family is jointly surjective on
> points.

```lean
structure IsEtaleCovering {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : ∀ i, X i ⟶ F) : Prop
```

## Tag 0DF1, a lemma

[Tag 0DF1](https://stacks.math.columbia.edu/tag/0DF1) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtaleCovering_of_isZariskiCovering`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/Zariski.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/Zariski.lean#L158).

> **Stacks 0DF1.** Every Zariski covering of algebraic spaces is an étale covering.

```lean
lemma isEtaleCovering_of_isZariskiCovering
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {I : Type v} {Xᵢ : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {f : ∀ i, Xᵢ i ⟶ X}
    (hX : IsAlgebraicSpace B S hS X)
    (hXᵢ : ∀ i, IsAlgebraicSpace B S hS (Xᵢ i))
    (h : IsZariskiCovering B S hS I Xᵢ f) :
    IsEtaleCovering B S hS Xᵢ f
```

## Tag 041F, a lemma

[Tag 041F](https://stacks.math.columbia.edu/tag/041F) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtaleCovering_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleCovering.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleCovering.lean#L75). The attribute's comment: “etale_covering_comp”.

> An étale covering of each member of an étale covering composes to an
> étale covering of the original algebraic space.

```lean
public theorem isEtaleCovering_comp
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {I : Type v} (J : I → Type w)
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (Xᵢ : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (f : ∀ i, Xᵢ i ⟶ X)
    (Xᵢⱼ : ∀ i, J i → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (g : ∀ i j, Xᵢⱼ i j ⟶ Xᵢ i)
    (hf : IsEtaleCovering B S hS Xᵢ f)
    (hg : ∀ i, IsEtaleCovering B S hS (Xᵢⱼ i) (g i)) :
    IsEtaleCovering B S hS
      (fun ij : (i : I) × J i => Xᵢⱼ ij.1 ij.2)
      (fun ij => g ij.1 ij.2 ≫ f ij.1)
```

**`AlgebraicGeometry.Space.isEtaleCovering_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleCovering.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleCovering.lean#L103). The attribute's comment: “etale_covering_base_change”.

> **Stacks 041F**, the base-change clause. The first projections of the presheaf fibre
> products of an étale covering of an algebraic space over `S` with a morphism `g` into its
> target form an étale covering of the source of `g`.

```lean
theorem isEtaleCovering_pullback
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {I : Type v} {X X' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (g : X' ⟶ X) (hX' : IsAlgebraicSpace B S hS X')
    (Y : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : ∀ i, Y i ⟶ X)
    (h : IsEtaleCovering B S hS Y f) :
    IsEtaleCovering B S hS (fun i => CategoryTheory.Limits.pullback g (f i))
      (fun i => CategoryTheory.Limits.pullback.fst g (f i))
```

**`AlgebraicGeometry.Space.isEtaleCovering_of_isIso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleCovering.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleCovering.lean#L134). The attribute's comment: “isomorphism_etale_covering”.

> **Stacks 041F**, the isomorphism clause. An isomorphism of algebraic spaces over `S`,
> regarded as a family indexed by a point, is an étale covering.

```lean
lemma isEtaleCovering_of_isIso
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X' ⟶ X) [IsIso f]
    (hX : IsAlgebraicSpace B S hS X) :
    IsEtaleCovering B S hS (fun _ : Unit ↦ X') (fun _ ↦ f)
```

## Tag 0CFV, a lemma

[Tag 0CFV](https://stacks.math.columbia.edu/tag/0CFV) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isEtaleCovering_refining_isSmoothCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmoothEtaleRefinement.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmoothEtaleRefinement.lean#L41).

> A smooth covering of an algebraic space over `S` is refined by an étale covering of it: there
> is an étale covering each of whose members factors through a member of the given smooth covering,
> compatibly with the morphisms to the common target.

```lean
theorem exists_isEtaleCovering_refining_isSmoothCovering
    {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : ∀ i, X i ⟶ F}
    (hf : IsSmoothCovering B S hS X f) :
    ∃ (J : Type u) (U : J → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (g : ∀ j, U j ⟶ F),
      IsEtaleCovering B S hS U g ∧
        ∀ j, ∃ (i : I) (h : U j ⟶ X i), h ≫ f i = g j
```

**`AlgebraicGeometry.Space.exists_isEtaleCovering_representable_refining_isSmoothCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmoothEtaleRefinementRepresentable.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmoothEtaleRefinementRepresentable.lean#L168). The attribute's comment: “the refinement with every member of it representable by a scheme of the site”.

> **Stacks 0CFV.** Every smooth covering of an algebraic space over `S` is refined by an étale
> covering: there are an étale covering of the same target, whose members are schemes of the site,
> and, for each of its members, a member of the given covering together with a morphism to it over
> the common target.

```lean
theorem exists_isEtaleCovering_representable_refining_isSmoothCovering
    {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : ∀ i, X i ⟶ F}
    (hsm : IsSmoothCovering B S hS X f) :
    ∃ (J : Type (u + 1)) (Y : J → BigFppfOver B S hS) (g : ∀ j, yoneda.obj (Y j) ⟶ F),
      IsEtaleCovering B S hS (fun j => yoneda.obj (Y j)) g ∧
        ∀ j, ∃ (i : I) (h : yoneda.obj (Y j) ⟶ X i), h ≫ f i = g j
```

## Tag 0DBX, a definition

[Tag 0DBX](https://stacks.math.columbia.edu/tag/0DBX) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSpaceSite`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleSite.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleSite.lean#L89).

> **Stacks 0DBX.** A big étale site of algebraic spaces over `S`: the chosen big étale site
> of schemes containing `S`, the category of algebraic spaces over `S`, and the set-sized
> system of étale covering families supplied by Stacks 000X.

```lean
structure BigEtaleSpaceSite (S : Scheme.{u})
```

## Tag 0DBY, a definition

[Tag 0DBY](https://stacks.math.columbia.edu/tag/0DBY) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSpaceSite.bigEtaleTopology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleSite.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleSite.lean#L184).

> **Stacks 0DBY.** The big étale topology of an algebraic space `X` of the site: the
> localization at `X` of the big étale topology of algebraic spaces over the base scheme.

```lean
abbrev bigEtaleTopology (T : BigEtaleSpaceSite S) (X : T.Spaces) :
    GrothendieckTopology (Over X)
```

## Tag 0DF2, a lemma

[Tag 0DF2](https://stacks.math.columbia.edu/tag/0DF2) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSpaceSite.inclusionFunctor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallToBigEtale.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallToBigEtale.lean#L88). The attribute's comment: “the inclusion functor”.

> **Stacks 0DF2.** Composition with `f` regards an algebraic space étale over `Y` as an
> object of the big étale site of `X`.

```lean
abbrev inclusionFunctor :
    Space.SpacesEtale T.fppfSite S T.fppf_mem Y ⥤ Over X
```

**`AlgebraicGeometry.BigEtaleSpaceSite.inclusionFunctor_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallToBigEtale.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallToBigEtale.lean#L248). The attribute's comment: “cocontinuity”.

> **Stacks 0DF2.** The inclusion of the spaces-étale site of `Y` into the big étale site of
> `X` is cocontinuous.

```lean
instance inclusionFunctor_isCocontinuous :
    (inclusionFunctor T f).IsCocontinuous
      (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) (T.bigEtaleTopology X)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.smallToBigEtaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallToBigEtale.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallToBigEtale.lean#L323). The attribute's comment: “the morphism of topoi”.

> **Stacks 0DF2.** The morphism of topoi from the spaces-étale topos of `Y` to the big
> étale topos of `X` induced by the inclusion functor. Its inverse image is restriction of
> sheaves along the inclusion, so its sections are computed by
> `CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj`.

```lean
noncomputable def smallToBigEtaleMorphism :
    MorphismOfTopoi
      (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) (Type (u + 1)))
      (Sheaf (T.bigEtaleTopology X) (Type (u + 1)))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.lowerShriek`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallToBigEtale.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallToBigEtale.lean#L342). The attribute's comment: “the lower-shriek functor”.

> **Stacks 0DF2.** The left adjoint of restriction along the inclusion functor.

```lean
noncomputable abbrev lowerShriek :
    Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) (Type (u + 1)) ⥤
      Sheaf (T.bigEtaleTopology X) (Type (u + 1))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.lowerShriek_preservesPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallToBigEtale.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallToBigEtale.lean#L350). The attribute's comment: “lower shriek preserves fibre products”.

> **Stacks 0DF2.** Lower shriek preserves fibre products.

```lean
noncomputable instance lowerShriek_preservesPullbacks :
    PreservesLimitsOfShape WalkingCospan (lowerShriek T f)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.lowerShriek_preservesEqualizers`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallToBigEtale.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallToBigEtale.lean#L358). The attribute's comment: “lower shriek preserves equalizers”.

> **Stacks 0DF2.** Lower shriek preserves equalizers.

```lean
noncomputable instance lowerShriek_preservesEqualizers :
    PreservesLimitsOfShape WalkingParallelPair (lowerShriek T f)
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallToBigEtale.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallToBigEtale.lean#L335) (StacksFrontier): “the inverse-image formula”.
- [`CategoryTheory.Functor.sheafAdjunctionContinuous`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafAdjunctionContinuous#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallToBigEtale.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallToBigEtale.lean#L337) (StacksFrontier): “existence of lower shriek”.

## Tag 0DF3, a lemma

[Tag 0DF3](https://stacks.math.columbia.edu/tag/0DF3) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSpaceSite.inclusion_isMorphismOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtale.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtale.lean#L73). The attribute's comment: “the morphism of sites”.

> **Stacks 0DF3.** The full inclusion of the spaces-étale site of `X` into the big étale
> site of `X` is a morphism of sites in the reverse direction.

```lean
theorem inclusion_isMorphismOfSites :
    (Space.SpacesEtale.inclusion T.fppfSite S T.fppf_mem X).IsMorphismOfSites
      (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) (T.bigEtaleTopology X)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.inclusionFunctorIdIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtale.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtale.lean#L96). The attribute's comment: “identification with the identity case of 0DF2”.

> **Stacks 0DF3.** The inclusion of the spaces-étale site of `X` is canonically the functor
> of Tag 0DF2 for the identity morphism of `X`.

```lean
noncomputable def inclusionFunctorIdIso :
    inclusionFunctor T (𝟙 X) ≅ Space.SpacesEtale.inclusion T.fppfSite S T.fppf_mem X
```

**`AlgebraicGeometry.BigEtaleSpaceSite.bigToSmallEtaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtale.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtale.lean#L105). The attribute's comment: “the morphism of topoi”.

> **Stacks 0DF3.** The morphism of topoi from the big étale topos of `X` to its small étale
> topos, induced by the inclusion of the spaces-étale site as a morphism of sites.

```lean
noncomputable def bigToSmallEtaleMorphism :
    MorphismOfTopoi
      (Sheaf (T.bigEtaleTopology X) (Type (u + 1)))
      (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) (Type (u + 1)))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.bigToSmall_comp_smallToBig_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtale.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtale.lean#L115). The attribute's comment: “the retraction identity”.

> **Stacks 0DF3.** Composing the morphism of topoi induced by the inclusion with the
> small-to-big morphism `i_X` gives the identity on the small étale topos, canonically up to
> natural isomorphism.

```lean
noncomputable def bigToSmall_comp_smallToBig_pushforwardIso :
    ((bigToSmallEtaleMorphism T X).comp (smallToBigEtaleMorphism T (𝟙 X))).pushforward ≅
      𝟭 (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) (Type (u + 1)))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.smallToBig_inverseImageIso_bigToSmall_pushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtale.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtale.lean#L136). The attribute's comment: “the inverse-image identification”.

> **Stacks 0DF3.** The inverse image of the small-to-big morphism `i_X` is the direct image
> of the big-to-small morphism of sites: both restrict a big étale sheaf to the objects étale
> over `X`.

```lean
noncomputable def smallToBig_inverseImageIso_bigToSmall_pushforward :
    (smallToBigEtaleMorphism T (𝟙 X)).inverseImage ≅
      (bigToSmallEtaleMorphism T X).pushforward
```

**`AlgebraicGeometry.Space.SpacesEtale.hasPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleSite.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleSite.lean#L298). The attribute's comment: “fibre products in the small site”.

> **Stacks 0DF3.** The spaces-étale site of `X` has fibre products: it is the full
> subcategory of the slice over `X` cut out by a base-change stable property of morphisms, so a
> fibre product of algebraic spaces étale over `X` is again étale over `X`.

```lean
instance hasPullbacks : HasPullbacks (SpacesEtale B S hS X)
```

**`AlgebraicGeometry.Space.SpacesEtale.hasTerminal`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleSite.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleSite.lean#L320). The attribute's comment: “the final object of the small site”.

> **Stacks 0DF3.** The spaces-étale site of `X` has a final object, the identity of `X`.

```lean
noncomputable instance hasTerminal : HasTerminal (SpacesEtale B S hS X)
```

**`AlgebraicGeometry.Space.SpacesEtale.inclusion_preservesTerminalShape`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleSite.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleSite.lean#L344). The attribute's comment: “the inclusion preserves the final object”.

> **Stacks 0DF3.** The final object of the spaces-étale site of `X` remains final in the
> slice over `X`.

```lean
noncomputable instance inclusion_preservesTerminalShape :
    PreservesLimitsOfShape (Discrete PEmpty.{1}) (inclusion B S hS X)
```

**`AlgebraicGeometry.Space.SpacesEtale.inclusion_preservesPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleSite.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleSite.lean#L351). The attribute's comment: “the inclusion preserves fibre products”.

> **Stacks 0DF3.** The inclusion of the spaces-étale site of `X` into the slice over `X`
> preserves fibre products.

```lean
instance inclusion_preservesPullbacks :
    PreservesLimitsOfShape WalkingCospan (inclusion B S hS X)
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtale.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtale.lean#L145) (StacksFrontier): “the section rule for inverse image”.

## Tag 0DF4, a definition

[Tag 0DF4](https://stacks.math.columbia.edu/tag/0DF4) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSpaceSite.bigToSmallEtaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtale.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtale.lean#L105). The attribute's comment: “its pushforward is the restriction to the small étale site”.

> **Stacks 0DF3.** The morphism of topoi from the big étale topos of `X` to its small étale
> topos, induced by the inclusion of the spaces-étale site as a morphism of sites.

```lean
noncomputable def bigToSmallEtaleMorphism :
    MorphismOfTopoi
      (Sheaf (T.bigEtaleTopology X) (Type (u + 1)))
      (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) (Type (u + 1)))
```

## Tag 0DF5, a lemma

[Tag 0DF5](https://stacks.math.columbia.edu/tag/0DF5) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSpaceSite.bigEtaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean#L115). The attribute's comment: “the morphism of big étale topoi and its inverse-image formula”. References: SGA 4 IV (4.7), “special case”.

> **Stacks 0DF5.** The morphism of big étale topoi induced by a morphism of algebraic
> spaces: its direct image is the cocontinuous pushforward along composition with `f` and its
> inverse image is the continuous pushforward along the same functor, so sections of the
> inverse image are given by `CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj`.

```lean
noncomputable def bigEtaleMorphism :
    MorphismOfTopoi
      (Sheaf (T.bigEtaleTopology Y) (Type (u + 1)))
      (Sheaf (T.bigEtaleTopology X) (Type (u + 1)))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.bigEtaleLowerShriek_preservesPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean#L130). The attribute's comment: “lower shriek preserves fibre products”.

> **Stacks 0DF5.** The left adjoint of the inverse image of
> `AlgebraicGeometry.BigEtaleSpaceSite.bigEtaleMorphism` preserves fibre products.

```lean
noncomputable instance bigEtaleLowerShriek_preservesPullbacks :
    PreservesLimitsOfShape WalkingCospan
      ((Over.map f).sheafPullback (Type (u + 1))
        (T.bigEtaleTopology Y) (T.bigEtaleTopology X))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.bigEtaleLowerShriek_preservesEqualizers`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean#L140). The attribute's comment: “lower shriek preserves equalizers”.

> **Stacks 0DF5.** The left adjoint of the inverse image of
> `AlgebraicGeometry.BigEtaleSpaceSite.bigEtaleMorphism` preserves equalizers.

```lean
noncomputable instance bigEtaleLowerShriek_preservesEqualizers :
    PreservesLimitsOfShape WalkingParallelPair
      ((Over.map f).sheafPullback (Type (u + 1))
        (T.bigEtaleTopology Y) (T.bigEtaleTopology X))
```

Declarations registered for the tag:

- [`map_isCocontinuous`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/RelocalizationTriangle.lean#L80), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean#L73) (StacksFrontier): “cocontinuity of the composition functor”.
- [`StacksRelocalization.isMorphismOfSites_overPullback`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/OverPullbackMorphism.lean#L43), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean#L75) (StacksFrontier): “continuous base-change right adjoint”.
- [`CategoryTheory.Over.mapPullbackAdj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.mapPullbackAdj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean#L77) (StacksFrontier): “adjunction of composition and base change”.
- [`StacksRelocalization.sheafPushforwardOverMapIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/OverPullbackMorphism.lean#L51), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean#L79) (StacksFrontier): “comparison of the two morphisms of topoi”.
- [`StacksRelocalization.sheafPullbackOverPullbackIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/OverPullbackMorphism.lean#L59), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean#L81) (StacksFrontier): “inverse-image comparison”.
- [`CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean#L83) (StacksFrontier): “inverse-image formula”.
- [`StacksRelocalization.sheafPushforwardObjEquiv`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/OverPullbackMorphism.lean#L67), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean#L85) (StacksFrontier): “direct-image formula”.
- [`CategoryTheory.Functor.sheafAdjunctionContinuous`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafAdjunctionContinuous#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleMorphism.lean#L87) (StacksFrontier): “existence of lower shriek”.

## Tag 0DF6, a lemma

[Tag 0DF6](https://stacks.math.columbia.edu/tag/0DF6) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSpaceSite.smallEtaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean#L79). The attribute's comment: “part (2), morphism of small étale topoi”.

> **Stacks 0DF6, part (2).** The morphism of spaces-étale topoi induced by cartesian base
> change along `f`.

```lean
noncomputable def smallEtaleMorphism :
    MorphismOfTopoi
      (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) (Type (u + 1)))
      (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) (Type (u + 1)))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.smallToBig_comp_big_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean#L88). The attribute's comment: “part (1), factorization of the small-to-big morphism”.

> **Stacks 0DF6, part (1).** The small-to-big morphism `i_f` agrees with the composite of
> `i_Y` and the big étale morphism along `f`.

```lean
noncomputable def smallToBig_comp_big_pushforwardIso :
    (smallToBigEtaleMorphism T f).pushforward ≅
      (smallToBigEtaleMorphism T (𝟙 Y)).pushforward ⋙ (bigEtaleMorphism T f).pushforward
```

**`AlgebraicGeometry.BigEtaleSpaceSite.smallBaseChange_comp_inclusionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean#L138). The attribute's comment: “part (3), commutative square of site functors”.

> **Stacks 0DF6, part (3).** The inclusion of the étale objects commutes with base change in
> the big slice site, up to the canonical isomorphism of cartesian squares.

```lean
noncomputable def smallBaseChange_comp_inclusionIso :
    (Space.spacesBaseChange T.fppfSite S T.fppf_mem f).functor ⋙
        Space.SpacesEtale.inclusion T.fppfSite S T.fppf_mem Y ≅
      Space.SpacesEtale.inclusion T.fppfSite S T.fppf_mem X ⋙ Over.pullback f
```

**`AlgebraicGeometry.BigEtaleSpaceSite.smallBaseChange_comp_inclusionIso_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean#L150). The attribute's comment: “part (3), cartesian projection coherence”.

> **Stacks 0DF6, part (3).** The site-square comparison is the cartesian comparison: its
> underlying map to the original chart is the projection defining base change.

```lean
theorem smallBaseChange_comp_inclusionIso_projection
    (U : Space.SpacesEtale T.fppfSite S T.fppf_mem X) :
    ((smallBaseChange_comp_inclusionIso T f).hom.app U).left ≫ pullback.fst U.1.hom f =
      (Space.spacesBaseChange T.fppfSite S T.fppf_mem f).projection.app U
```

**`AlgebraicGeometry.BigEtaleSpaceSite.bigSmallEtale_pushforwardCommIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean#L159). The attribute's comment: “part (3), commutative square of topoi”.

> **Stacks 0DF6, part (3).** The square of big and small étale morphisms commutes on direct
> images.

```lean
noncomputable def bigSmallEtale_pushforwardCommIso :
    ((smallEtaleMorphism T f).comp (bigToSmallEtaleMorphism T Y)).pushforward ≅
      ((bigToSmallEtaleMorphism T X).comp (bigEtaleMorphism T f)).pushforward
```

**`AlgebraicGeometry.BigEtaleSpaceSite.smallEtale_pushforwardIsoBigFactorization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean#L199). The attribute's comment: “part (4), factorization through both big topoi”.

> **Stacks 0DF6, part (4).** The small étale direct image factors through the big étale
> topoi of both `Y` and `X`.

```lean
noncomputable def smallEtale_pushforwardIsoBigFactorization :
    (smallEtaleMorphism T f).pushforward ≅
      ((bigToSmallEtaleMorphism T X).comp
        ((bigEtaleMorphism T f).comp (smallToBigEtaleMorphism T (𝟙 Y)))).pushforward
```

**`AlgebraicGeometry.BigEtaleSpaceSite.smallEtale_pushforwardIsoDirectFactorization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean#L212). The attribute's comment: “part (4), direct factorization through the big topos”.

> **Stacks 0DF6, part (4).** The small étale direct image factors directly through `i_f`.

```lean
noncomputable def smallEtale_pushforwardIsoDirectFactorization :
    (smallEtaleMorphism T f).pushforward ≅
      ((bigToSmallEtaleMorphism T X).comp (smallToBigEtaleMorphism T f)).pushforward
```

**`AlgebraicGeometry.BigEtaleSpaceSite.smallEtale_pushforwardIsoBigFactorization_coherence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean#L229). The attribute's comment: “part (4), coherence with the topos square”.

> **Stacks 0DF6, part (4).** The factorization through both big topoi is the topos square
> after inserting the small/big retraction at `Y`.

```lean
theorem smallEtale_pushforwardIsoBigFactorization_coherence
    (F : Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) (Type (u + 1))) :
    (smallEtaleMorphism T f).pushforward.map
        ((bigToSmall_comp_smallToBig_pushforwardIso T Y).inv.app F) ≫
      (bigSmallEtale_pushforwardCommIso T f).hom.app
        ((smallToBigEtaleMorphism T (𝟙 Y)).pushforward.obj F) =
    (smallEtale_pushforwardIsoBigFactorization T f).hom.app F
```

**`AlgebraicGeometry.BigEtaleSpaceSite.smallEtale_pushforwardIsoDirectFactorization_coherence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean#L241). The attribute's comment: “part (4), coherence of the two factorizations”.

> **Stacks 0DF6, part (4).** The direct factorization and the factorization through `i_Y`
> are identified by the canonical comparison `i_f ≅ f_big ∘ i_Y` of part (1).

```lean
theorem smallEtale_pushforwardIsoDirectFactorization_coherence
    (F : Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) (Type (u + 1))) :
    (smallEtale_pushforwardIsoDirectFactorization T f).hom.app F ≫
      (bigToSmallEtaleMorphism T X).pushforward.map
        ((smallToBig_comp_big_pushforwardIso T f).hom.app F) =
    (smallEtale_pushforwardIsoBigFactorization T f).hom.app F
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleSquare.lean#L71) (StacksFrontier): “part (2), direct-image section formula”.

## Tag 0DF7, a lemma

[Tag 0DF7](https://stacks.math.columbia.edu/tag/0DF7) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSpaceSite.bigEtaleMorphism_comp_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleToposFunctoriality.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleToposFunctoriality.lean#L74). The attribute's comment: “big étale direct images”.

> The direct images of composable morphisms of big étale topoi agree canonically with the direct
> image of the composite.

```lean
def bigEtaleMorphism_comp_pushforwardIso :
    ((bigEtaleMorphism T g).comp (bigEtaleMorphism T f)).pushforward ≅
      (bigEtaleMorphism T (f ≫ g)).pushforward
```

**`AlgebraicGeometry.BigEtaleSpaceSite.bigEtaleMorphism_comp_inverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleToposFunctoriality.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleToposFunctoriality.lean#L85). The attribute's comment: “big étale inverse images”.

> The inverse-image comparison for the big étale topoi is the adjunction mate of the direct-image
> comparison.

```lean
def bigEtaleMorphism_comp_inverseImageIso :
    ((bigEtaleMorphism T g).comp (bigEtaleMorphism T f)).inverseImage ≅
      (bigEtaleMorphism T (f ≫ g)).inverseImage
```

**`AlgebraicGeometry.BigEtaleSpaceSite.smallEtaleMorphism_comp_inverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleToposFunctoriality.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleToposFunctoriality.lean#L94). The attribute's comment: “small étale inverse images”.

> The inverse-image comparison for the small étale topoi is the adjunction mate of the canonical
> composition comparison for cartesian base change on the spaces-étale sites.

```lean
def smallEtaleMorphism_comp_inverseImageIso :
    ((smallEtaleMorphism T g).comp (smallEtaleMorphism T f)).inverseImage ≅
      (smallEtaleMorphism T (f ≫ g)).inverseImage
```

Declarations registered for the tag:

- [`Space.spacesBaseChange_pushforward_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Space.spacesBaseChange_pushforward_comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleToposFunctoriality.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleToposFunctoriality.lean#L65) (StacksFrontier): “small étale direct images”.

## Tag 0DF8, a lemma

[Tag 0DF8](https://stacks.math.columbia.edu/tag/0DF8) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSpaceSite.smallEtalePushforwardBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleToposFunctoriality.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleToposFunctoriality.lean#L141). The attribute's comment: “small-site base change”.

> Restriction to the small étale site commutes canonically with big étale direct image across a
> cartesian square of algebraic spaces.

```lean
def smallEtalePushforwardBaseChangeIso :
    (bigEtaleMorphism T f).pushforward ⋙ (smallToBigEtaleMorphism T g).inverseImage ≅
      (smallToBigEtaleMorphism T g').inverseImage ⋙ (smallEtaleMorphism T f').pushforward
```

**`AlgebraicGeometry.BigEtaleSpaceSite.bigEtalePushforwardBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleToposFunctoriality.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleToposFunctoriality.lean#L199). The attribute's comment: “big-site base change”.

> Big étale inverse image commutes canonically with big étale direct image across a cartesian
> square of algebraic spaces.

```lean
def bigEtalePushforwardBaseChangeIso :
    (bigEtaleMorphism T f).pushforward ⋙ (bigEtaleMorphism T g).inverseImage ≅
      (bigEtaleMorphism T g').inverseImage ⋙ (bigEtaleMorphism T f').pushforward
```

**`AlgebraicGeometry.BigEtaleSpaceSite.smallEtaleCartesianIndexIso_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleToposFunctoriality.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleToposFunctoriality.lean#L320). The attribute's comment: “projection coherence of the index comparison”.

> **Projection coherence.** The comparison of the two descriptions of the small étale site of
> `X'` inside the big étale site of `Y` is the cartesian comparison: its underlying map, followed by
> the projection of the fibre product with `f`, is the projection defining the base change along
> `f'`. This is `AlgebraicGeometry.BigEtaleSpaceSite.smallBaseChange_comp_inclusionIso_projection`
> across the whole cartesian square.

```lean
theorem smallEtaleCartesianIndexIso_projection
    (U : Space.SpacesEtale T.fppfSite S T.fppf_mem X') :
    ((smallEtaleCartesianIndexIso T g' f' f g h).inv.app U).left ≫
        pullback.fst ((inclusionFunctor T g).obj U).hom f =
      (Space.spacesBaseChange T.fppfSite S T.fppf_mem f').projection.app U
```

**`AlgebraicGeometry.BigEtaleSpaceSite.sharpCommSqBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleToposFunctoriality.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleToposFunctoriality.lean#L341). The attribute's comment: “structure-map coherence over the cartesian square”.

> **Structure-map coherence.** The structure maps of `i_g`, `f_big`, `i_{g'}` and `f'_small` are
> compatible with the comparison of the two composite site functors over the cartesian square: both
> composite structure maps are pullback of global regular functions along the cartesian projection of
> the base change. This is `AlgebraicGeometry.BigEtaleSpaceSite.sharpCommSq` across the whole square.

```lean
theorem sharpCommSqBaseChange :
    (restrictAlongSharp T g ≫
        ((inclusionFunctor T g).sheafPushforwardContinuous RingCat.{u + 1}
          (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X')
          (T.bigEtaleTopology X)).map (bigPullbackSharp T f)) ≫
      (Functor.sheafPushforwardContinuousNatTrans
        (smallEtaleCartesianIndexIso T g' f' f g h).symm.hom RingCat.{u + 1}
        (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X')
        (T.bigEtaleTopology Y)).app (bigEtaleRingSheaf T Y) =
    smallBaseChangeSharp T f' ≫
      ((Space.spacesBaseChange T.fppfSite S T.fppf_mem f').functor.sheafPushforwardContinuous
        RingCat.{u + 1} (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X')
        (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y')).map
        (restrictAlongSharp T g')
```

**`AlgebraicGeometry.BigEtaleSpaceSite.smallEtaleModulePushforwardBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleToposFunctoriality.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleToposFunctoriality.lean#L371). The attribute's comment: “the sheaf-of-modules form over a cartesian square”.

> Restriction to the small étale site commutes canonically with big étale direct image of sheaves
> of `𝒪`-modules across a cartesian square of algebraic spaces:
> `i_g^*(f_{big,*}F) = f'_{small,*}(i_{g'}^*F)`.
>
> This is the `𝒪`-module form of
> `AlgebraicGeometry.BigEtaleSpaceSite.smallEtalePushforwardBaseChangeIso`, which states the same
> square for sheaves of sets.

```lean
def smallEtaleModulePushforwardBaseChangeIso :
    bigEtaleModulePushforward.{u, u + 1} T f ⋙ restrictModulesAlong T g ≅
      restrictModulesAlong T g' ⋙ smallEtaleModulePushforward.{u, u + 1} T f'
```

## Tag 0DF9, a remark

[Tag 0DF9](https://stacks.math.columbia.edu/tag/0DF9) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSpaceSite.restrictSharp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtalePushforwardModules.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtalePushforwardModules.lean#L175). The attribute's comment: “item (3), the structure map of the comparison morphism π_X”.

> **Stacks 0DF9, item (3).** The structure map of the comparison morphism `π_X`: the sections
> of the direct image of the big étale structure sheaf over an algebraic space étale over `X` are
> its own global regular functions, so the structure map is the identity.

```lean
def restrictSharp (X : T.Spaces) :
    spacesEtaleRingSheaf T X ⟶
      ((Space.SpacesEtale.inclusion T.fppfSite S T.fppf_mem X).sheafPushforwardContinuous
        RingCat.{u + 1} (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X)
        (T.bigEtaleTopology X)).obj (bigEtaleRingSheaf T X)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.bigPullbackSharp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtalePushforwardModules.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtalePushforwardModules.lean#L185). The attribute's comment: “item (5), the structure map of the big étale morphism f_big”.

> **Stacks 0DF9, item (5).** The structure map of the big étale morphism `f_big`: pullback of
> global regular functions along the projection of the fibre product `V ×_X Y` to `V`.

```lean
def bigPullbackSharp (f : Y ⟶ X) :
    bigEtaleRingSheaf T X ⟶
      ((Over.pullback f).sheafPushforwardContinuous RingCat.{u + 1}
        (T.bigEtaleTopology X) (T.bigEtaleTopology Y)).obj (bigEtaleRingSheaf T Y)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.smallBaseChangeSharp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtalePushforwardModules.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtalePushforwardModules.lean#L196). The attribute's comment: “item (4), the structure map of the small étale morphism f_small”.

> **Stacks 0DF9, item (4).** The structure map of the small étale morphism `f_small`:
> pullback of global regular functions along the cartesian projection of the base change of an
> algebraic space étale over `X`.

```lean
def smallBaseChangeSharp (f : Y ⟶ X) :
    spacesEtaleRingSheaf T X ⟶
      ((Space.spacesBaseChange T.fppfSite S T.fppf_mem f).functor.sheafPushforwardContinuous
        RingCat.{u + 1} (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X)
        (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y)).obj
        (spacesEtaleRingSheaf T Y)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.smallToBigRestrictionStructureIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean#L88). The attribute's comment: “case (1): restriction along the inclusion functor”.

> Restriction of the big étale structure sheaf of `X` along the inclusion of the spaces-étale
> site of `Y` is the spaces-étale structure sheaf of `Y`: an object étale over `Y` has the same
> ring of global regular functions read in either site, and the restriction maps agree.

```lean
noncomputable def smallToBigRestrictionStructureIso (f : Y ⟶ X) :
    ((inclusionFunctor T f).sheafPushforwardContinuous CommRingCat.{u + 1}
        (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y)
        (T.bigEtaleTopology X)).obj (T.structureSheaf X) ≅
      Space.SpacesEtale.structureSheaf T.fppfSite S T.fppf_mem Y
```

**`AlgebraicGeometry.BigEtaleSpaceSite.smallToBigEtaleStructureIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean#L101). The attribute's comment: “case (1): the isomorphism i_f⁻¹𝒪 ≅ 𝒪_Y”.

> **Stacks 0DF9, case (1).** The canonical isomorphism from the inverse image along `i_f` of
> the big étale structure sheaf of `X` to the spaces-étale structure sheaf of `Y`.

```lean
noncomputable def smallToBigEtaleStructureIso (f : Y ⟶ X) :
    (inverseImageCommRingFunctor (smallToBigEtaleMorphism T f)).obj
        (bigEtaleRingedTopos T X).O ≅
      (Space.spacesEtaleRingedTopos T.fppfSite S T.fppf_mem Y).O
```

**`AlgebraicGeometry.BigEtaleSpaceSite.smallToBigEtaleRingedMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean#L113). The attribute's comment: “case (1): i_f as a morphism of ringed topoi”.

> **Stacks 0DF9, case (1).** The morphism `i_f` from the spaces-étale topos of `Y` to the big
> étale topos of `X` as a morphism of ringed topoi: the structure map is the adjunct of the
> canonical isomorphism of structure sheaves.

```lean
noncomputable def smallToBigEtaleRingedMorphism (f : Y ⟶ X) :
    RingedToposHom (Space.spacesEtaleRingedTopos T.fppfSite S T.fppf_mem Y)
      (bigEtaleRingedTopos T X)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.iXEtaleRingedMorphism`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean#L131). The attribute's comment: “case (2): i_X as a morphism of ringed topoi”.

> **Stacks 0DF9, case (2).** The morphism `i_X` as a morphism of ringed topoi: it is the
> identity-morphism case `f = 𝟙 X` of `i_f`.

```lean
noncomputable abbrev iXEtaleRingedMorphism (X : T.Spaces) :
    RingedToposHom (Space.spacesEtaleRingedTopos T.fppfSite S T.fppf_mem X)
      (bigEtaleRingedTopos T X)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.bigToSmallRestrictionStructureIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean#L142). The attribute's comment: “case (3): restriction along the inclusion of the spaces-étale site”.

> Restriction of the big étale structure sheaf of `X` along the inclusion of the spaces-étale
> site of `X` is the spaces-étale structure sheaf of `X`, in the direction needed for the direct
> image along `π_X`.

```lean
noncomputable def bigToSmallRestrictionStructureIso (X : T.Spaces) :
    Space.SpacesEtale.structureSheaf T.fppfSite S T.fppf_mem X ≅
      ((Space.SpacesEtale.inclusion T.fppfSite S T.fppf_mem X).sheafPushforwardContinuous
          CommRingCat.{u + 1} (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X)
          (T.bigEtaleTopology X)).obj (T.structureSheaf X)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.bigToSmallEtaleStructureIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean#L155). The attribute's comment: “case (3): the isomorphism 𝒪_X ≅ π_{X,*}𝒪”.

> **Stacks 0DF9, case (3).** The canonical isomorphism from the spaces-étale structure sheaf
> of `X` to the direct image along `π_X` of the big étale structure sheaf of `X`.

```lean
noncomputable def bigToSmallEtaleStructureIso (X : T.Spaces) :
    (Space.spacesEtaleRingedTopos T.fppfSite S T.fppf_mem X).O ≅
      (pushforwardCommRingFunctor (bigToSmallEtaleMorphism T X)).obj
        (bigEtaleRingedTopos T X).O
```

**`AlgebraicGeometry.BigEtaleSpaceSite.bigToSmallEtaleRingedMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean#L168). The attribute's comment: “case (3): π_X as a morphism of ringed topoi”.

> **Stacks 0DF9, case (3).** The morphism `π_X` from the big étale topos of `X` to its
> spaces-étale topos as a morphism of ringed topoi, with the canonical isomorphism
> `𝒪_X ≅ π_{X,*}𝒪` as its structure map.

```lean
noncomputable def bigToSmallEtaleRingedMorphism (X : T.Spaces) :
    RingedToposHom (bigEtaleRingedTopos T X)
      (Space.spacesEtaleRingedTopos T.fppfSite S T.fppf_mem X)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.BigEtaleSpaceSite.structurePresheaf_isSheaf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleStructureSheaf.lean#L469), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean#L176) (StacksFrontier): “the big étale structure presheaf is a sheaf”.
- [`AlgebraicGeometry.BigEtaleSpaceSite.structureSheaf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleStructureSheaf.lean#L475), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean#L178) (StacksFrontier): “the structure sheaf of the big étale site”.
- [`AlgebraicGeometry.Space.SpacesEtale.structurePresheaf_isSheaf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleStructureSheaf.lean#L308), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean#L180) (StacksFrontier): “the spaces-étale structure presheaf is a sheaf”.
- [`AlgebraicGeometry.Space.SpacesEtale.structureSheaf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleStructureSheaf.lean#L321), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean#L182) (StacksFrontier): “the structure sheaf of the spaces-étale site”.
- [`AlgebraicGeometry.Space.smallEtaleRingedToposHom`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRingedToposHom.lean#L281), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean#L184) (StacksFrontier): “case (4): f_small as a morphism of ringed topoi”.
- [`AlgebraicGeometry.BigEtaleSpaceSite.bigEtaleStructureIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleRingedTopos.lean#L85), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean#L186) (StacksFrontier): “case (5): the isomorphism f_big⁻¹𝒪₁ ≅ 𝒪₂”.
- [`AlgebraicGeometry.BigEtaleSpaceSite.bigEtaleRingedMorphism`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleRingedTopos.lean#L107), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtaleRingedComparison.lean#L188) (StacksFrontier): “case (5): f_big as a morphism of ringed topoi”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 73.4, Tag 03YC](https://stacks.math.columbia.edu/tag/03YC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
