---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsPHCovering, AlgebraicGeometry.Space.isPHCovering_of_isEtaleCovering, AlgebraicGeometry.Space.isPHCovering_of_isFppfCovering, AlgebraicGeometry.Space.isPHCovering_of_isSyntomicCovering, AlgebraicGeometry.Space.isPHCovering_of_isSmoothCovering, AlgebraicGeometry.Space.isPHCovering_of_isZariskiCovering, AlgebraicGeometry.Space.isPHCovering_of_isProper_isSurjective, AlgebraicGeometry.Space.isPHCovering_comp
statement: formalized
proof: formalized
---

# 73.8 The ph topology

Section 73.8 of the Stacks Project, [Tag 0DFF](https://stacks.math.columbia.edu/tag/0DFF). 10 tags here are carried by 28 declarations of the repository (all in StacksFrontier) and 9 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DFG, a definition

[Tag 0DFG](https://stacks.math.columbia.edu/tag/0DFG) in the Stacks Project.

**`AlgebraicGeometry.Space.IsPHCovering`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/PhCoverings.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/PhCoverings.lean#L90).

> **Stacks 0DFG.** A family of morphisms of algebraic spaces over `S` with common target is
> a *ph covering* when every member is locally of finite type and every affine scheme-valued
> point of the target admits a standard ph covering refining the pullback of the family.

```lean
structure IsPHCovering {I : Type v} {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (Xᵢ : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : ∀ i, Xᵢ i ⟶ X) : Prop
```

## Tag 0DFH, a lemma

[Tag 0DFH](https://stacks.math.columbia.edu/tag/0DFH) in the Stacks Project.

**`AlgebraicGeometry.Space.isPHCovering_of_isEtaleCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtalePhCoverings.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/EtalePhCoverings.lean#L207). The attribute's comment: “étale coverings”.

> **The étale case of Stacks 0DFH.** An étale covering of an algebraic space over `S` is a
> ph covering of it.
>
> Each member is locally of finite type because it is étale. For an affine scheme-valued point
> `a` of the target, the family is base changed along `a` and each base changed member is
> replaced by a scheme atlas of it; the resulting family of morphisms of representables is still
> étale and jointly surjective, so the underlying family of morphisms of schemes is an étale
> covering of the affine test scheme and is refined by a standard ph covering of it by
> `AlgebraicGeometry.isPHCovering_of_etale`. The members of that refinement are affine and of
> finite type over the test object, hence lie in the site, and the refinement morphisms compose
> with the atlases and the fibre product projections to refine the original family over `a`.

```lean
theorem isPHCovering_of_isEtaleCovering {I : Type v}
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {f : ∀ i, X i ⟶ F} (hf : IsEtaleCovering B S hS X f) :
    IsPHCovering B S hS X f
```

**`AlgebraicGeometry.Space.isPHCovering_of_isFppfCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FppfPhCoverings.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FppfPhCoverings.lean#L57). The attribute's comment: “fppf coverings”.

> An fppf covering of an algebraic space over `S` is a ph covering of it.

```lean
theorem isPHCovering_of_isFppfCovering {I : Type v}
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {f : ∀ i, X i ⟶ F} (hf : IsFppfCovering B S hS X f) :
    IsPHCovering B S hS X f
```

**`AlgebraicGeometry.Space.isPHCovering_of_isSyntomicCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FppfPhCoverings.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FppfPhCoverings.lean#L119). The attribute's comment: “syntomic coverings”.

> A syntomic covering of an algebraic space over `S` is a ph covering of it.

```lean
theorem isPHCovering_of_isSyntomicCovering {I : Type v}
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {f : ∀ i, X i ⟶ F} (hf : IsSyntomicCovering B S hS X f) :
    IsPHCovering B S hS X f
```

**`AlgebraicGeometry.Space.isPHCovering_of_isSmoothCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FppfPhCoverings.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FppfPhCoverings.lean#L127). The attribute's comment: “smooth coverings”.

> A smooth covering of an algebraic space over `S` is a ph covering of it.

```lean
theorem isPHCovering_of_isSmoothCovering {I : Type v}
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {f : ∀ i, X i ⟶ F} (hf : IsSmoothCovering B S hS X f) :
    IsPHCovering B S hS X f
```

**`AlgebraicGeometry.Space.isPHCovering_of_isZariskiCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FppfPhCoverings.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FppfPhCoverings.lean#L136). The attribute's comment: “Zariski coverings”.

> A Zariski covering of an algebraic space over `S` by algebraic spaces is a ph covering of
> it.

```lean
theorem isPHCovering_of_isZariskiCovering {I : Type v}
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {f : ∀ i, X i ⟶ F} (hF : IsAlgebraicSpace B S hS F)
    (hX : ∀ i, IsAlgebraicSpace B S hS (X i))
    (hf : IsZariskiCovering B S hS I X f) :
    IsPHCovering B S hS X f
```

## Tag 0DFI, a lemma

[Tag 0DFI](https://stacks.math.columbia.edu/tag/0DFI) in the Stacks Project.

**`AlgebraicGeometry.Space.isPHCovering_of_isProper_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/PhCoveringProperSurjective.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/PhCoveringProperSurjective.lean#L209).

> **Stacks 0DFI.** A proper surjective morphism of algebraic spaces over `S`, regarded as a
> one-member family, is a ph covering.
>
> Over an affine object `U` of the site the pullback `Y ×_X h_U` is proper and surjective over
> `h_U`, so Chow's lemma over `U` — in the form
> `AlgebraicGeometry.Space.exists_properSurjective_schemeCover_of_isProper_toAffine` — produces a
> proper surjective morphism of schemes `V ⟶ U` which factors through that pullback. A finite
> affine open covering of `V` is then a standard ph covering of `U`, and it refines the family
> pulled back along `a` through the factorization.

```lean
theorem isPHCovering_of_isProper_isSurjective
    {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X' ⟶ X)
    (hX : IsAlgebraicSpace B S hS X) (hX' : IsAlgebraicSpace B S hS X')
    (hp : IsProper B S hS f) (hs : IsSurjective B S hS f) :
    IsPHCovering B S hS (fun _ : Unit ↦ X') (fun _ ↦ f)
```

## Tag 0DFJ, a lemma

[Tag 0DFJ](https://stacks.math.columbia.edu/tag/0DFJ) in the Stacks Project.

**`AlgebraicGeometry.Space.isPHCovering_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/PhCoveringComposition.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/PhCoveringComposition.lean#L39). The attribute's comment: “composition”.

> **Ph coverings compose.** If `{Xᵢ i ⟶ X}` is a ph covering of an algebraic space over `S`
> and `{Xᵢⱼ i j ⟶ Xᵢ i}` is a ph covering for every `i`, then the family of all composites
> `Xᵢⱼ i j ⟶ Xᵢ i ⟶ X`, indexed by `Σ i, J i`, is a ph covering of `X`.

```lean
theorem isPHCovering_comp
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {I : Type v} {J : I → Type w}
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (Xᵢ : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : ∀ i, Xᵢ i ⟶ X)
    (Xᵢⱼ : ∀ i, J i → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (g : ∀ i j, Xᵢⱼ i j ⟶ Xᵢ i)
    (hf : IsPHCovering B S hS Xᵢ f)
    (hg : ∀ i, IsPHCovering B S hS (Xᵢⱼ i) (g i)) :
    IsPHCovering B S hS (fun ij : Σ i, J i ↦ Xᵢⱼ ij.1 ij.2)
      (fun ij : Σ i, J i ↦ g ij.1 ij.2 ≫ f ij.1)
```

**`AlgebraicGeometry.Space.isPHCovering_of_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/PhCoverings.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/PhCoverings.lean#L112). The attribute's comment: “ph\_covering\_of\_isomorphism”.

> **Stacks 0DFJ**, the isomorphism clause. An isomorphism of algebraic spaces over `S`,
> regarded as a family indexed by a point, is a ph covering: the identity of an affine test
> scheme is a standard ph covering of it, and it refines the pulled-back family through the
> inverse isomorphism.

```lean
theorem isPHCovering_of_isIso
    {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X' ⟶ X) [IsIso f]
    (hX : IsAlgebraicSpace B S hS X) :
    IsPHCovering B S hS (fun _ : Unit ↦ X') (fun _ ↦ f)
```

**`AlgebraicGeometry.Space.isPHCovering_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/PhCoverings.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/PhCoverings.lean#L144). The attribute's comment: “ph\_covering\_base\_change”.

> **Stacks 0DFJ**, the base-change clause. The first projections of the fibre products of a
> ph covering of an algebraic space over `S` with a morphism `g` into its target form a ph
> covering of the source of `g`: a standard ph refinement of the original family over an affine
> point `a` of the new base refines the pulled-back family through the universal property of the
> fibre product.

```lean
theorem isPHCovering_baseChange
    {I : Type v} {X X' : AlgebraicSpaces B S hS} (Xᵢ : I → AlgebraicSpaces B S hS)
    (f : ∀ i, Xᵢ i ⟶ X) (g : X' ⟶ X)
    (hf : IsPHCovering B S hS (fun i ↦ (Xᵢ i).1) (fun i ↦ (f i).hom)) :
    IsPHCovering B S hS (fun i ↦ (AlgebraicSpaces.fiberProduct B S hS g (f i)).1)
      (fun i ↦ pullback.fst g.hom (f i).hom)
```

## Tag 0DFK, a definition

[Tag 0DFK](https://stacks.math.columbia.edu/tag/0DFK) in the Stacks Project.

**`AlgebraicGeometry.BigPHSpaceSite`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhSite.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhSite.lean#L99).

> **Stacks 0DFK.** A big ph site of algebraic spaces over `S`: the chosen big ph site of
> schemes containing `S`, the category of algebraic spaces over `S`, and the set-sized system of
> ph covering families supplied by Stacks 000X.

```lean
structure BigPHSpaceSite (S : Scheme.{u})
```

## Tag 0DFL, a definition

[Tag 0DFL](https://stacks.math.columbia.edu/tag/0DFL) in the Stacks Project.

**`AlgebraicGeometry.BigPHSpaceOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhSite.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhSite.lean#L220). The attribute's comment: “underlying category”.

> **Stacks 0DFL.** The category underlying the big ph site of an algebraic space `X` of the
> site is the slice of the big ph category of algebraic spaces at `X`.

```lean
abbrev BigPHSpaceOver
```

**`AlgebraicGeometry.BigPHSpaceOver.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhSite.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhSite.lean#L225). The attribute's comment: “covering families”.

> A family over `X` covers when its underlying family covers in the big ph site of
> algebraic spaces.

```lean
abbrev BigPHSpaceOver.IsCovering (E : Covering (BigPHSpaceOver T X)) : Prop
```

**`AlgebraicGeometry.BigPHSpaceOver.topology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhSite.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhSite.lean#L231). The attribute's comment: “localized topology”.

> **Stacks 0DFL.** The big ph topology of `X` is the localization at `X` of the big ph
> topology of algebraic spaces over the base scheme.

```lean
abbrev BigPHSpaceOver.topology : GrothendieckTopology (BigPHSpaceOver T X)
```

## Tag 0DFM, a lemma

[Tag 0DFM](https://stacks.math.columbia.edu/tag/0DFM) in the Stacks Project.

**`AlgebraicGeometry.Space.isSheaf_of_etale_and_properSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/PhSheafCriterion.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/PhSheafCriterion.lean#L373). The attribute's comment: “sufficiency: etale descent plus proper-surjective descent imply the ph sheaf condition”.

> A presheaf of sets on the big ph site of an algebraic space `X` of a big ph site of
> algebraic spaces is a sheaf as soon as it satisfies étale descent and descent along every proper
> surjective morphism of the site.

```lean
theorem isSheaf_of_etale_and_properSurjective (h₁ : IsEtaleSheafOver T X F)
    (h₂ : IsProperSurjectiveSheafOver T X F) :
    Presieve.IsSheaf (BigPHSpaceOver.topology T X) F
```

**`AlgebraicGeometry.Space.isEtaleSheafOver_of_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/PhSheafCriterion.lean, line 436](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/PhSheafCriterion.lean#L436). The attribute's comment: “necessity, etale descent: a ph sheaf satisfies etale descent”.

> A sheaf of sets on the big ph site of an algebraic space `X` of a big ph site of algebraic
> spaces satisfies étale descent.

```lean
theorem isEtaleSheafOver_of_isSheaf (h : Presieve.IsSheaf (BigPHSpaceOver.topology T X) F) :
    IsEtaleSheafOver T X F
```

**`AlgebraicGeometry.Space.isProperSurjectiveSheafOver_of_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/PhSheafCriterion.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/PhSheafCriterion.lean#L446). The attribute's comment: “necessity, proper-surjective descent: a ph sheaf satisfies descent along every proper surjective morphism of the site”.

> A sheaf of sets on the big ph site of an algebraic space `X` of a big ph site of algebraic
> spaces satisfies descent along every proper surjective morphism of the site.

```lean
theorem isProperSurjectiveSheafOver_of_isSheaf
    (h : Presieve.IsSheaf (BigPHSpaceOver.topology T X) F) :
    IsProperSurjectiveSheafOver T X F
```

**`AlgebraicGeometry.Space.isSheaf_iff_isEtaleSheafOver_and_isProperSurjectiveSheafOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/PhSheafCriterion.lean, line 459](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/PhSheafCriterion.lean#L459). The attribute's comment: “the biconditional”.

> A presheaf of sets on the big ph site of an algebraic space `X` of a big ph site of
> algebraic spaces is a sheaf if and only if it satisfies étale descent and descent along every
> proper surjective morphism of the site.

```lean
theorem isSheaf_iff_isEtaleSheafOver_and_isProperSurjectiveSheafOver :
    Presieve.IsSheaf (BigPHSpaceOver.topology T X) F ↔
      IsEtaleSheafOver T X F ∧ IsProperSurjectiveSheafOver T X F
```

## Tag 0DFN, a lemma

[Tag 0DFN](https://stacks.math.columbia.edu/tag/0DFN) in the Stacks Project.

**`AlgebraicGeometry.BigPHSpaceSite.bigPHMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean#L96). The attribute's comment: “the morphism of topoi”. References: SGA 4 IV (4.7), “special case”.

> **Stacks 0DFN.** The morphism of big ph topoi induced by a morphism of algebraic spaces:
> its direct image is the cocontinuous pushforward along composition with `f` and its inverse
> image is the continuous pushforward along the same functor, so sections of the inverse image
> are given by `CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj`.

```lean
noncomputable def bigPHMorphism :
    MorphismOfTopoi
      (Sheaf (BigPHSpaceOver.topology T Y) (Type (u + 1)))
      (Sheaf (BigPHSpaceOver.topology T X) (Type (u + 1)))
```

**`AlgebraicGeometry.BigPHSpaceSite.bigPHMorphismInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean#L110). The attribute's comment: “inverse-image formula”.

> **Stacks 0DFN.** The inverse image is restriction along composition with `f`.

```lean
noncomputable def bigPHMorphismInverseImageIso :
    (bigPHMorphism T f).inverseImage ≅
      (Over.map f).sheafPushforwardContinuous (Type (u + 1))
        (BigPHSpaceOver.topology T Y) (BigPHSpaceOver.topology T X)
```

**`AlgebraicGeometry.BigPHSpaceSite.bigPHMorphismPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean#L120). The attribute's comment: “direct-image formula and agreement of the induced morphisms”.

> **Stacks 0DFN.** The direct image is restriction along base change by `f`, which is the
> adjoint comparison of the cocontinuous pushforward with the continuous pushforward along the
> right adjoint of `Over.map f`.

```lean
noncomputable def bigPHMorphismPushforwardIso :
    (bigPHMorphism T f).pushforward ≅
      (Over.pullback f).sheafPushforwardContinuous (Type (u + 1))
        (BigPHSpaceOver.topology T X) (BigPHSpaceOver.topology T Y)
```

**`AlgebraicGeometry.BigPHSpaceSite.bigPHMorphismLowerShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean#L129). The attribute's comment: “lower shriek”.

> **Stacks 0DFN.** The left adjoint of the inverse image of
> `AlgebraicGeometry.BigPHSpaceSite.bigPHMorphism`.

```lean
noncomputable def bigPHMorphismLowerShriek :
    Sheaf (BigPHSpaceOver.topology T Y) (Type (u + 1)) ⥤
      Sheaf (BigPHSpaceOver.topology T X) (Type (u + 1))
```

**`AlgebraicGeometry.BigPHSpaceSite.bigPHMorphismLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean#L137). The attribute's comment: “lower-shriek adjunction”.

> **Stacks 0DFN.** Lower shriek is left adjoint to the inverse image.

```lean
noncomputable def bigPHMorphismLowerShriekAdjunction :
    bigPHMorphismLowerShriek T f ⊣ (bigPHMorphism T f).inverseImage
```

**`AlgebraicGeometry.BigPHSpaceSite.bigPHMorphismLowerShriek_preservesPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean#L144). The attribute's comment: “lower shriek preserves fibre products”.

> **Stacks 0DFN.** Lower shriek preserves fibre products.

```lean
noncomputable instance bigPHMorphismLowerShriek_preservesPullbacks :
    PreservesLimitsOfShape WalkingCospan (bigPHMorphismLowerShriek T f)
```

**`AlgebraicGeometry.BigPHSpaceSite.bigPHMorphismLowerShriek_preservesEqualizers`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean#L151). The attribute's comment: “lower shriek preserves equalizers”.

> **Stacks 0DFN.** Lower shriek preserves equalizers.

```lean
noncomputable instance bigPHMorphismLowerShriek_preservesEqualizers :
    PreservesLimitsOfShape WalkingParallelPair (bigPHMorphismLowerShriek T f)
```

Declarations registered for the tag:

- [`CategoryTheory.Over.map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.map#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean#L75) (StacksFrontier): “postcomposition functor”. References: EGA I (2.5.3); EGA I (2.5.4), “more general”; SGA 3 I (1.6); SGA 4 IV (5.5).
- [`CategoryTheory.Over.pullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.pullback#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean#L76) (StacksFrontier): “fibre-product right adjoint”. References: EGA I (3.3.7), “more general”; EGA IV (8.2.6); SGA 3 I (1.6); SGA 4 III (5.5); SGA 4 IV (5.2), “more general”; SGA 4 IV (5.5).
- [`CategoryTheory.Over.mapPullbackAdj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.mapPullbackAdj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean#L77) (StacksFrontier): “site adjunction”.
- [`map_isCocontinuous`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/RelocalizationTriangle.lean#L80), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean#L78) (StacksFrontier): “cocontinuity of postcomposition”.
- [`map_isContinuous`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/RelocalizationTriangle.lean#L74), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean#L79) (StacksFrontier): “continuity of postcomposition”.
- [`StacksRelocalization.isMorphismOfSites_overPullback`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/OverPullbackMorphism.lean#L43), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean#L80) (StacksFrontier): “continuous base change”.
- [`StacksRelocalization.sheafPushforwardOverMapIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/OverPullbackMorphism.lean#L51), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean#L82) (StacksFrontier): “agreement of the induced morphisms”.
- [`CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafPushforwardContinuous_obj_obj_obj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean#L84) (StacksFrontier): “inverse-image sections”.
- [`StacksRelocalization.sheafPushforwardObjEquiv`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/OverPullbackMorphism.lean#L67), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean#L86) (StacksFrontier): “direct-image sections”.

## Tag 0DFP, a lemma

[Tag 0DFP](https://stacks.math.columbia.edu/tag/0DFP) in the Stacks Project.

**`AlgebraicGeometry.BigPHSpaceSite.bigPHMorphism_comp_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean#L164). The attribute's comment: “direct-image composition”.

> **Stacks 0DFP.** The direct image of the composite agrees canonically with the composite
> of the direct images on the big ph topoi, because base change along a composite is the
> composite of the base changes.

```lean
noncomputable def bigPHMorphism_comp_pushforwardIso :
    ((bigPHMorphism T g).comp (bigPHMorphism T f)).pushforward ≅
      (bigPHMorphism T (f ≫ g)).pushforward
```

**`AlgebraicGeometry.BigPHSpaceSite.bigPHMorphism_comp_inverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhMorphism.lean#L179). The attribute's comment: “inverse-image composition”.

> **Stacks 0DFP.** The inverse-image comparison is the adjunction mate of the direct-image
> comparison.

```lean
noncomputable def bigPHMorphism_comp_inverseImageIso :
    ((bigPHMorphism T g).comp (bigPHMorphism T f)).inverseImage ≅
      (bigPHMorphism T (f ≫ g)).inverseImage
```

## Tag 0DK6, a lemma

[Tag 0DK6](https://stacks.math.columbia.edu/tag/0DK6) in the Stacks Project.

**`AlgebraicGeometry.Space.holds_of_affine_of_cechLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/AffineCechCriterion.lean, line 681](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/AffineCechCriterion.lean#L681).

> A Čech-local property of objects of the big fppf site over `X` can be
> checked on affine objects flat and locally of finite presentation over `X`.

```lean
public theorem holds_of_affine_of_cechLocal
    {S : Scheme.{u}} (T : AlgebraicGeometry.BigFppfSpaceSite S) (X : T.Spaces)
    (P : Over X → Prop)
    (hcech : ∀ (E : Covering (Over X)),
      AlgebraicGeometry.BigFppfSpaceOver.IsCovering T X E →
      (∀ (n : ℕ) (i : Fin (n + 1) → E.2.I₀)
        (c : WidePullbackCone (fun k : Fin (n + 1) => E.2.f (i k))),
        IsLimit c → P c.pt) → P E.1)
    (haffine : ∀ U : Over X,
      AlgebraicGeometry.Space.IsAffineSpace T.schemeSite S T.scheme_mem U.left.1 →
      AlgebraicGeometry.Space.IsFlat T.schemeSite S T.scheme_mem U.hom.hom →
      AlgebraicGeometry.Space.IsLocallyOfFinitePresentation T.schemeSite S T.scheme_mem
        U.hom.hom → P U) :
    P (Over.mk (𝟙 X))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 73.8, Tag 0DFF](https://stacks.math.columbia.edu/tag/0DFF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
