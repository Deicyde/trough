---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsFppfCovering, AlgebraicGeometry.Space.isFppfCovering_of_isSyntomicCovering, AlgebraicGeometry.Space.isFppfCovering_of_isSmoothCovering, AlgebraicGeometry.Space.isFppfCovering_of_isEtaleCovering, AlgebraicGeometry.Space.isFppfCovering_of_isZariskiCovering, AlgebraicGeometry.Space.isFppfCovering_yoneda_of_openCover, AlgebraicGeometry.Space.Topology.precoverage_etale_le_fppf, AlgebraicGeometry.Space.isFppfCovering_fibreProduct
statement: formalized
proof: formalized
---

# 73.7 Fppf topology

Section 73.7 of the Stacks Project, [Tag 03Y7](https://stacks.math.columbia.edu/tag/03Y7). 9 tags here are carried by 27 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03Y8, a definition

[Tag 03Y8](https://stacks.math.columbia.edu/tag/03Y8) in the Stacks Project.

**`AlgebraicGeometry.Space.IsFppfCovering`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean#L211).

> **Stacks 03Y8.** A family of morphisms of algebraic spaces over `S` with common target
> is an *fppf covering* when every member is flat and locally of finite presentation and the
> family is jointly surjective on points.

```lean
structure IsFppfCovering {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : ∀ i, X i ⟶ F) : Prop
```

## Tag 0DFC, a lemma

[Tag 0DFC](https://stacks.math.columbia.edu/tag/0DFC) in the Stacks Project.

**`AlgebraicGeometry.Space.isFppfCovering_of_isSyntomicCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean#L156). The attribute's comment: “syntomic coverings”.

> **Stacks 0DFC**, the syntomic case: a syntomic covering of algebraic spaces over `S` is an
> fppf covering.

```lean
theorem isFppfCovering_of_isSyntomicCovering
    {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : ∀ i, X i ⟶ F}
    (hf : IsSyntomicCovering B S hS X f) :
    IsFppfCovering B S hS X f
```

**`AlgebraicGeometry.Space.isFppfCovering_of_isSmoothCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean#L169). The attribute's comment: “smooth coverings”.

> **Stacks 0DFC**, the smooth case: a smooth covering of algebraic spaces over `S` is an fppf
> covering.

```lean
theorem isFppfCovering_of_isSmoothCovering
    {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : ∀ i, X i ⟶ F}
    (hf : IsSmoothCovering B S hS X f) :
    IsFppfCovering B S hS X f
```

**`AlgebraicGeometry.Space.isFppfCovering_of_isEtaleCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean#L180). The attribute's comment: “étale coverings”.

> **Stacks 0DFC**, the étale case: an étale covering of algebraic spaces over `S` is an fppf
> covering.

```lean
theorem isFppfCovering_of_isEtaleCovering
    {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : ∀ i, X i ⟶ F}
    (hf : IsEtaleCovering B S hS X f) :
    IsFppfCovering B S hS X f
```

**`AlgebraicGeometry.Space.isFppfCovering_of_isZariskiCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean, line 266](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean#L266). The attribute's comment: “Zariski coverings”.

> **Stacks 0DFC**, the Zariski case: a Zariski covering of algebraic spaces over `S` is an
> fppf covering.

```lean
theorem isFppfCovering_of_isZariskiCovering
    {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : ∀ i, X i ⟶ F}
    (hF : IsAlgebraicSpace B S hS F) (hX : ∀ i, IsAlgebraicSpace B S hS (X i))
    (hf : IsZariskiCovering B S hS I X f) :
    IsFppfCovering B S hS X f
```

**`AlgebraicGeometry.Space.isFppfCovering_yoneda_of_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiCoveringOfOpenCover.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiCoveringOfOpenCover.lean#L128). The attribute's comment: “an open cover of an object of the site”.

> **Stacks 0DFC for an open cover of an object of the big fppf site of `S`.** The family of
> representables of an open cover of an object of the site is an fppf covering of the
> representable of that object: it is a Zariski covering by Stacks 041G.

```lean
theorem isFppfCovering_yoneda_of_openCover
    {I : Type v} {T : BigFppfOver B S hS} (X : I → BigFppfOver B S hS) (g : ∀ i, X i ⟶ T)
    (hopen : ∀ i, _root_.AlgebraicGeometry.IsOpenImmersion
      ((BigFppfOver.toScheme B S hS).map (g i)))
    (hcov : ∀ x : (BigFppfOver.toScheme B S hS).obj T,
      ∃ i, x ∈ Set.range ((BigFppfOver.toScheme B S hS).map (g i))) :
    IsFppfCovering B S hS (fun i => yoneda.obj (X i)) (fun i => yoneda.map (g i))
```

**`AlgebraicGeometry.Space.Topology.precoverage_etale_le_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoproductChartPropertyDescent.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoproductChartPropertyDescent.lean#L104). The attribute's comment: “étale coverings, at the precoverages”.

> The étale precoverage of algebraic spaces over `S` is contained in the fppf one.

```lean
theorem precoverage_etale_le_fppf :
    Topology.precoverage.{u, v} .etale B S hS ≤ Topology.precoverage.{u, v} .fppf B S hS
```

## Tag 03Y9, a lemma

[Tag 03Y9](https://stacks.math.columbia.edu/tag/03Y9) in the Stacks Project.

**`AlgebraicGeometry.Space.isFppfCovering_fibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparison.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparison.lean#L133). The attribute's comment: “base\_change\_cover”.

> **Stacks 03Y9.** Pulling an fppf covering of algebraic spaces over `S` back along a
> morphism of algebraic spaces gives an fppf covering of the new target: the first projections of
> the fibre products of Stacks 02X2 form an fppf covering.

```lean
theorem isFppfCovering_fibreProduct
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {I : Type v} {X X' : AlgebraicSpaces B S hS}
    (Xi : I → AlgebraicSpaces B S hS)
    (f : ∀ i, Xi i ⟶ X) (g : X' ⟶ X)
    (hf : IsFppfCovering B S hS (fun i => (Xi i).1) (fun i => (f i).hom)) :
    IsFppfCovering B S hS
      (fun i => (AlgebraicSpaces.fiberProduct B S hS g (f i)).1)
      (fun i => pullback.fst g.hom (f i).hom)
```

**`AlgebraicGeometry.Space.isFppfCovering_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparison.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparison.lean#L167). The attribute's comment: “composition\_cover”.

> **Stacks 03Y9.** Composing an fppf covering of an algebraic space over `S` with an fppf
> covering of each of its members gives an fppf covering: flatness and being locally of finite
> presentation are stable under composition (Stacks 03MN and 03XQ), and a point of the target is
> hit by a member of the first covering, hence by a member of the covering of that member.

```lean
theorem isFppfCovering_comp
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (I : Type v) (J : I → Type w)
    (Xᵢ : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (Xᵢⱼ : ∀ i, J i → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (f : ∀ i, Xᵢ i ⟶ X) (g : ∀ i j, Xᵢⱼ i j ⟶ Xᵢ i)
    (hf : IsFppfCovering B S hS Xᵢ f)
    (hg : ∀ i, IsFppfCovering B S hS (Xᵢⱼ i) (g i)) :
    IsFppfCovering B S hS (fun p : Σ i, J i => Xᵢⱼ p.1 p.2)
      (fun p => g p.1 p.2 ≫ f p.1)
```

**`AlgebraicGeometry.Space.isFppfCovering_of_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean#L194). The attribute's comment: “isomorphism\_cover”.

> **Stacks 03Y9**, the isomorphism clause. An isomorphism of algebraic spaces over `S`,
> regarded as a family indexed by a point, is an fppf covering: it is an étale covering by
> **Stacks 041F**, hence an fppf covering by **Stacks 0DFC**.

```lean
theorem isFppfCovering_of_isIso
    (X X' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : X' ⟶ X) [IsIso f]
    (hX : IsAlgebraicSpace B S hS X) :
    IsFppfCovering B S hS (fun _ : PUnit.{v + 1} => X') (fun _ => f)
```

## Tag 042T, a lemma

[Tag 042T](https://stacks.math.columbia.edu/tag/042T) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_fppfCovering_scheme_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FppfCoverings.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FppfCoverings.lean#L72).

> **Stacks 042T.** An fppf covering of an algebraic space over `S` admits a refinement by a
> family of schemes which is again an fppf covering.

```lean
theorem exists_fppfCovering_scheme_refinement
    {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : ∀ i, X i ⟶ F)
    (hf : IsFppfCovering B S hS X f) :
    ∃ (T : I → BigFppfOver B S hS) (h : ∀ i, yoneda.obj (T i) ⟶ X i),
      IsFppfCovering B S hS (fun i => yoneda.obj (T i)) (fun i => h i ≫ f i)
```

## Tag 0469, a lemma

[Tag 0469](https://stacks.math.columbia.edu/tag/0469) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallySurjective_coproductDesc_of_isFppfCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FppfCoverings.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FppfCoverings.lean#L192).

> **Stacks 0469.** The map from the coproduct of an fppf covering family of algebraic spaces
> over `S`, taken in the category of fppf sheaves of sets, to its target is surjective as a map
> of fppf sheaves.

```lean
theorem isLocallySurjective_coproductDesc_of_isFppfCovering
    {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : ∀ i, X i ⟶ F)
    (hf : IsFppfCovering B S hS X f)
    (G : Sheaf (BigFppfOver.topology B S hS) (Type u))
    (ι : ∀ i, (⟨X i, (hf.source_isAlgebraicSpace i).isSheaf⟩ :
      Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶ G)
    (hG : IsColimit (Cofan.mk G ι)) :
    Sheaf.IsLocallySurjective
      (hG.desc (Cofan.mk
        (⟨F, hf.target_isAlgebraicSpace.isSheaf⟩ :
          Sheaf (BigFppfOver.topology B S hS) (Type u))
        (fun i =>
          (Sheaf.homEquiv (X :=
            (⟨X i, (hf.source_isAlgebraicSpace i).isSheaf⟩ :
              Sheaf (BigFppfOver.topology B S hS) (Type u)))
            (Y :=
            (⟨F, hf.target_isAlgebraicSpace.isSheaf⟩ :
              Sheaf (BigFppfOver.topology B S hS) (Type u)))).symm (f i))))
```

## Tag 0DBV, a definition

[Tag 0DBV](https://stacks.math.columbia.edu/tag/0DBV) in the Stacks Project.

**`AlgebraicGeometry.BigFppfSpaceSite`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfSite.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfSite.lean#L115).

> **Stacks 0DBV.** A big fppf site of algebraic spaces over `S`: the chosen big fppf site of
> schemes containing `S`, the category of algebraic spaces over `S`, and the set-sized system of
> fppf covering families supplied by Stacks 000X.

```lean
structure BigFppfSpaceSite (S : Scheme.{u})
```

## Tag 0DBW, a definition

[Tag 0DBW](https://stacks.math.columbia.edu/tag/0DBW) in the Stacks Project.

**`AlgebraicGeometry.BigFppfSpaceOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfSite.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfSite.lean#L210). The attribute's comment: “underlying category”.

> **Stacks 0DBW.** The category underlying the big fppf site of an algebraic space `X` of
> the site is the slice of the big fppf category of algebraic spaces at `X`.

```lean
abbrev BigFppfSpaceOver
```

**`AlgebraicGeometry.BigFppfSpaceOver.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfSite.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfSite.lean#L215). The attribute's comment: “covering families”.

> A family over `X` covers when its underlying family covers in the big fppf site of
> algebraic spaces.

```lean
abbrev BigFppfSpaceOver.IsCovering (E : Covering (BigFppfSpaceOver T X)) : Prop
```

**`AlgebraicGeometry.BigFppfSpaceOver.topology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfSite.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfSite.lean#L221). The attribute's comment: “localized topology”.

> **Stacks 0DBW.** The big fppf topology of `X` is the localization at `X` of the big fppf
> topology of algebraic spaces over the base scheme.

```lean
abbrev BigFppfSpaceOver.topology : GrothendieckTopology (BigFppfSpaceOver T X)
```

## Tag 0DFD, a lemma

[Tag 0DFD](https://stacks.math.columbia.edu/tag/0DFD) in the Stacks Project.

**`AlgebraicGeometry.BigFppfSpaceSite.bigFppfMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean#L87). The attribute's comment: “the morphism of topoi”.

> **Stacks 0DFD.** The morphism of big fppf topoi induced by a morphism of algebraic
> spaces: the functor of sites is base change along `f`, which is continuous with exact
> pullback.

```lean
noncomputable def bigFppfMorphism :
    MorphismOfTopoi
      (Sheaf (BigFppfSpaceOver.topology T Y) (Type (u + 1)))
      (Sheaf (BigFppfSpaceOver.topology T X) (Type (u + 1)))
```

**`AlgebraicGeometry.BigFppfSpaceSite.bigFppfMorphism_inverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean#L95). The attribute's comment: “inverse-image functor”.

> **Stacks 0DFD.** The inverse image is naturally restriction along composition with `f`.

```lean
noncomputable def bigFppfMorphism_inverseImageIso :
    (bigFppfMorphism T f).inverseImage ≅
      (Over.map f).sheafPushforwardContinuous (Type (u + 1))
        (BigFppfSpaceOver.topology T Y) (BigFppfSpaceOver.topology T X)
```

**`AlgebraicGeometry.BigFppfSpaceSite.bigFppfMorphism_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean#L105). The attribute's comment: “equality of the two induced morphisms of topoi”.

> **Stacks 0DFD.** The direct image agrees naturally with the pushforward attached to the
> cocontinuous composition functor, so the two morphisms of topoi one can attach to `f`
> coincide.

```lean
noncomputable def bigFppfMorphism_pushforwardIso :
    (bigFppfMorphism T f).pushforward ≅
      (Over.map f).sheafPushforwardCocontinuous (Type (u + 1))
        (BigFppfSpaceOver.topology T Y) (BigFppfSpaceOver.topology T X)
```

**`AlgebraicGeometry.BigFppfSpaceSite.bigFppfMorphism_inverseImage_sections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean#L114). The attribute's comment: “inverse-image sections”.

> **Stacks 0DFD.** The sections of the inverse image of a sheaf over an object `V` of the
> big fppf site of `Y` are its sections over `V` composed with `f`.

```lean
noncomputable def bigFppfMorphism_inverseImage_sections
    (G : Sheaf (BigFppfSpaceOver.topology T X) (Type (u + 1))) (V : Over Y) :
    ((bigFppfMorphism T f).inverseImage.obj G).obj.obj (op V) ≃
      G.obj.obj (op ((Over.map f).obj V))
```

**`AlgebraicGeometry.BigFppfSpaceSite.bigFppfMorphism_pushforward_sections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean#L124). The attribute's comment: “direct-image sections”.

> **Stacks 0DFD.** The sections of the direct image of a sheaf over an object `U` of the big
> fppf site of `X` are its sections over the fibre product of `U` with `Y` over `X`.

```lean
noncomputable def bigFppfMorphism_pushforward_sections
    (F : Sheaf (BigFppfSpaceOver.topology T Y) (Type (u + 1))) (U : Over X) :
    ((bigFppfMorphism T f).pushforward.obj F).obj.obj (op U) ≃
      F.obj.obj (op ((Over.pullback f).obj U))
```

**`AlgebraicGeometry.BigFppfSpaceSite.bigFppfMorphism_lowerShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean#L134). The attribute's comment: “left adjoint to inverse image”.

> **Stacks 0DFD.** The further left adjoint of the inverse image.

```lean
noncomputable def bigFppfMorphism_lowerShriek :
    Sheaf (BigFppfSpaceOver.topology T Y) (Type (u + 1)) ⥤
      Sheaf (BigFppfSpaceOver.topology T X) (Type (u + 1))
```

**`AlgebraicGeometry.BigFppfSpaceSite.bigFppfMorphism_lowerShriek_adjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean#L142). The attribute's comment: “lower-shriek adjunction”.

> **Stacks 0DFD.** Lower shriek is left adjoint to the inverse image.

```lean
noncomputable def bigFppfMorphism_lowerShriek_adjunction :
    bigFppfMorphism_lowerShriek T f ⊣ (bigFppfMorphism T f).inverseImage
```

**`AlgebraicGeometry.BigFppfSpaceSite.bigFppfMorphism_lowerShriek_preservesPullbacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean#L151). The attribute's comment: “lower shriek preserves fibre products”.

> **Stacks 0DFD.** Lower shriek preserves fibre products of big fppf sheaves.

```lean
theorem bigFppfMorphism_lowerShriek_preservesPullbacks :
    PreservesLimitsOfShape WalkingCospan (bigFppfMorphism_lowerShriek T f)
```

**`AlgebraicGeometry.BigFppfSpaceSite.bigFppfMorphism_lowerShriek_preservesEqualizers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean#L158). The attribute's comment: “lower shriek preserves equalizers”.

> **Stacks 0DFD.** Lower shriek preserves equalizers of big fppf sheaves.

```lean
theorem bigFppfMorphism_lowerShriek_preservesEqualizers :
    PreservesLimitsOfShape WalkingParallelPair (bigFppfMorphism_lowerShriek T f)
```

Declarations registered for the tag:

- [`CategoryTheory.Over.map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.map#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean#L77) (StacksFrontier): “postcomposition functor”. References: EGA I (2.5.3); EGA I (2.5.4), “more general”; SGA 3 I (1.6); SGA 4 IV (5.5).
- [`CategoryTheory.Over.pullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.pullback#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean#L78) (StacksFrontier): “fibre-product right adjoint”. References: EGA I (3.3.7), “more general”; EGA IV (8.2.6); SGA 3 I (1.6); SGA 4 III (5.5); SGA 4 IV (5.2), “more general”; SGA 4 IV (5.5).
- [`CategoryTheory.Over.mapPullbackAdj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.mapPullbackAdj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean#L79) (StacksFrontier): “site adjunction”.

## Tag 0DFE, a lemma

[Tag 0DFE](https://stacks.math.columbia.edu/tag/0DFE) in the Stacks Project.

**`AlgebraicGeometry.BigFppfSpaceSite.bigFppfMorphism_comp_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean#L170). The attribute's comment: “direct images”.

> **Stacks 0DFE.** The direct images of composable morphisms of big fppf topoi agree
> canonically with the direct image of the composite.

```lean
noncomputable def bigFppfMorphism_comp_pushforwardIso :
    ((bigFppfMorphism T h).comp (bigFppfMorphism T g)).pushforward ≅
      (bigFppfMorphism T (g ≫ h)).pushforward
```

**`AlgebraicGeometry.BigFppfSpaceSite.bigFppfMorphism_comp_inverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfMorphism.lean#L189). The attribute's comment: “inverse images”.

> **Stacks 0DFE.** The inverse-image comparison is the adjunction mate of the direct-image
> comparison.

```lean
noncomputable def bigFppfMorphism_comp_inverseImageIso :
    ((bigFppfMorphism T h).comp (bigFppfMorphism T g)).inverseImage ≅
      (bigFppfMorphism T (g ≫ h)).inverseImage
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 73.7, Tag 03Y7](https://stacks.math.columbia.edu/tag/03Y7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
