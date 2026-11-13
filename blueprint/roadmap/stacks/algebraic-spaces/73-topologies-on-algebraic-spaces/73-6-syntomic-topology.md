---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsSyntomicCovering, AlgebraicGeometry.Space.isSyntomicCovering_iff, AlgebraicGeometry.Space.isSyntomicCovering_of_isSmoothCovering, AlgebraicGeometry.Space.isSyntomicCovering_of_isEtaleCovering, AlgebraicGeometry.Space.isSyntomicCovering_of_isZariskiCovering, AlgebraicGeometry.Space.isSyntomicCovering_pullback, AlgebraicGeometry.Space.isSyntomicCovering_comp, AlgebraicGeometry.Space.isSyntomicCovering_of_isIso
statement: formalized
proof: formalized
---

# 73.6 Syntomic topology

Section 73.6 of the Stacks Project, [Tag 03YA](https://stacks.math.columbia.edu/tag/03YA). 3 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 041A, a definition

[Tag 041A](https://stacks.math.columbia.edu/tag/041A) in the Stacks Project.

**`AlgebraicGeometry.Space.IsSyntomicCovering`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean#L242).

> **Stacks 041A.** A family of morphisms of algebraic spaces over `S` with common target
> is a *syntomic covering* when every member is syntomic and the family is jointly
> surjective on points.

```lean
structure IsSyntomicCovering {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : ∀ i, X i ⟶ F) : Prop
```

**`AlgebraicGeometry.Space.isSyntomicCovering_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean#L257). The attribute's comment: “the condition unfolded”.

> **Stacks 041A.** Being a syntomic covering is exactly: the target and all the sources are
> algebraic spaces, every member of the family is syntomic, and the images of the maps on points
> exhaust the points of the target.

```lean
theorem isSyntomicCovering_iff {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : ∀ i, X i ⟶ F) :
    IsSyntomicCovering B S hS X f ↔
      (IsAlgebraicSpace B S hS F ∧ (∀ i, IsAlgebraicSpace B S hS (X i)) ∧
        (∀ i, IsSyntomic B S hS (f i)) ∧
        Set.univ = ⋃ i, Set.range (pointsMap B S hS (X i) (f i)))
```

## Tag 0DFB, a lemma

[Tag 0DFB](https://stacks.math.columbia.edu/tag/0DFB) in the Stacks Project.

**`AlgebraicGeometry.Space.isSyntomicCovering_of_isSmoothCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean#L132). The attribute's comment: “smooth coverings”.

> **Stacks 0DFB**, the smooth case: a smooth covering of algebraic spaces over `S` is a
> syntomic covering.

```lean
theorem isSyntomicCovering_of_isSmoothCovering
    {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : ∀ i, X i ⟶ F}
    (hf : IsSmoothCovering B S hS X f) :
    IsSyntomicCovering B S hS X f
```

**`AlgebraicGeometry.Space.isSyntomicCovering_of_isEtaleCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean#L143). The attribute's comment: “étale coverings”.

> **Stacks 0DFB**, the étale case: an étale covering of algebraic spaces over `S` is a
> syntomic covering.

```lean
theorem isSyntomicCovering_of_isEtaleCovering
    {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : ∀ i, X i ⟶ F}
    (hf : IsEtaleCovering B S hS X f) :
    IsSyntomicCovering B S hS X f
```

**`AlgebraicGeometry.Space.isSyntomicCovering_of_isZariskiCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean#L254). The attribute's comment: “Zariski coverings”.

> **Stacks 0DFB**, the Zariski case: a Zariski covering of algebraic spaces over `S` is a
> syntomic covering.

```lean
theorem isSyntomicCovering_of_isZariskiCovering
    {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : ∀ i, X i ⟶ F}
    (hF : IsAlgebraicSpace B S hS F) (hX : ∀ i, IsAlgebraicSpace B S hS (X i))
    (hf : IsZariskiCovering B S hS I X f) :
    IsSyntomicCovering B S hS X f
```

## Tag 041B, a lemma

[Tag 041B](https://stacks.math.columbia.edu/tag/041B) in the Stacks Project.

**`AlgebraicGeometry.Space.isSyntomicCovering_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SyntomicCoveringBaseChange.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SyntomicCoveringBaseChange.lean#L85). The attribute's comment: “part (3), base change”.

> **Stacks 041B**, the base-change clause. The first projections of the presheaf fibre
> products of a syntomic covering of an algebraic space over `S` with a morphism `g` into its
> target form a syntomic covering of the source of `g`.

```lean
theorem isSyntomicCovering_pullback {I : Type v}
    {X X' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (g : X' ⟶ X) (hX' : IsAlgebraicSpace B S hS X')
    (Y : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : ∀ i, Y i ⟶ X)
    (h : IsSyntomicCovering B S hS Y f) :
    IsSyntomicCovering B S hS (fun i => pullback g (f i))
      (fun i => pullback.fst g (f i))
```

**`AlgebraicGeometry.Space.isSyntomicCovering_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SyntomicCoveringComposition.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SyntomicCoveringComposition.lean#L54). The attribute's comment: “part (2), composition”.

> **Stacks 041B**, the composition clause. A syntomic covering of each member of a syntomic
> covering composes to a syntomic covering of the original algebraic space.

```lean
theorem isSyntomicCovering_comp {I : Type v} (J : I → Type w)
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (Xᵢ : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : ∀ i, Xᵢ i ⟶ X)
    (Xᵢⱼ : ∀ i, J i → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (g : ∀ i j, Xᵢⱼ i j ⟶ Xᵢ i)
    (hf : IsSyntomicCovering B S hS Xᵢ f)
    (hg : ∀ i, IsSyntomicCovering B S hS (Xᵢⱼ i) (g i)) :
    IsSyntomicCovering B S hS
      (fun ij : (i : I) × J i => Xᵢⱼ ij.1 ij.2)
      (fun ij => g ij.1 ij.2 ≫ f ij.1)
```

**`AlgebraicGeometry.Space.isSyntomicCovering_of_isIso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SyntomicCoverings.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SyntomicCoverings.lean#L46). The attribute's comment: “part (1), isomorphisms”.

> **Stacks 041B**, the isomorphism clause. An isomorphism of algebraic spaces over `S`,
> regarded as a family indexed by a point, is a syntomic covering.

```lean
lemma isSyntomicCovering_of_isIso
    {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X' ⟶ X) [IsIso f]
    (hX : IsAlgebraicSpace B S hS X) :
    IsSyntomicCovering B S hS (fun _ : Unit ↦ X') (fun _ ↦ f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 73.6, Tag 03YA](https://stacks.math.columbia.edu/tag/03YA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
