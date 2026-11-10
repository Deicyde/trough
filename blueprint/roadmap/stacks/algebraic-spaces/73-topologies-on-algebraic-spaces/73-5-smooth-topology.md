---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsSmoothCovering, AlgebraicGeometry.Space.isSmoothCovering_of_isEtaleCovering, AlgebraicGeometry.Space.isSmoothCovering_of_isZariskiCovering, AlgebraicGeometry.Space.isSmoothCovering_of_isIso, AlgebraicGeometry.Space.isSmoothCovering_comp, AlgebraicGeometry.Space.isSmoothCovering_fiberProduct
statement: formalized
proof: formalized
---

# 73.5 Smooth topology

Section 73.5 of the Stacks Project, [Tag 03YB](https://stacks.math.columbia.edu/tag/03YB). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 041C, a definition

[Tag 041C](https://stacks.math.columbia.edu/tag/041C) in the Stacks Project.

**`AlgebraicGeometry.Space.IsSmoothCovering`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean#L300).

> **Stacks 041C.** A family of morphisms of algebraic spaces over `S` with common target
> is a *smooth covering* when every member is smooth and the family is jointly surjective on
> points.

```lean
structure IsSmoothCovering {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : ∀ i, X i ⟶ F) : Prop
```

## Tag 0DFA, a lemma

[Tag 0DFA](https://stacks.math.columbia.edu/tag/0DFA) in the Stacks Project.

**`AlgebraicGeometry.Space.isSmoothCovering_of_isEtaleCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean#L118). The attribute's comment: “étale coverings”.

> **Stacks 0DFA**, the étale case: an étale covering of algebraic spaces over `S` is a smooth
> covering.

```lean
theorem isSmoothCovering_of_isEtaleCovering
    {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : ∀ i, X i ⟶ F}
    (hf : IsEtaleCovering B S hS X f) :
    IsSmoothCovering B S hS X f
```

**`AlgebraicGeometry.Space.isSmoothCovering_of_isZariskiCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparisonTopologies.lean#L242). The attribute's comment: “Zariski coverings”.

> **Stacks 0DFA**, the Zariski case: a Zariski covering of algebraic spaces over `S` is a
> smooth covering, because it is an étale covering by Stacks 0DF1.

```lean
theorem isSmoothCovering_of_isZariskiCovering
    {I : Type v} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : ∀ i, X i ⟶ F}
    (hF : IsAlgebraicSpace B S hS F) (hX : ∀ i, IsAlgebraicSpace B S hS (X i))
    (hf : IsZariskiCovering B S hS I X f) :
    IsSmoothCovering B S hS X f
```

## Tag 041D, a lemma

[Tag 041D](https://stacks.math.columbia.edu/tag/041D) in the Stacks Project.

**`AlgebraicGeometry.Space.isSmoothCovering_of_isIso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmoothCoverings.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmoothCoverings.lean#L64). The attribute's comment: “isomorphism”.

> **Stacks 041D**, the isomorphism clause. An isomorphism of algebraic spaces over `S`,
> regarded as a family indexed by a point, is a smooth covering.

```lean
lemma isSmoothCovering_of_isIso
    {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X' ⟶ X) [IsIso f]
    (hX : IsAlgebraicSpace B S hS X) :
    IsSmoothCovering B S hS (fun _ : Unit ↦ X') (fun _ ↦ f)
```

**`AlgebraicGeometry.Space.isSmoothCovering_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmoothCoverings.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmoothCoverings.lean#L86). The attribute's comment: “composition”.

> **Stacks 041D**, the composition clause. Composing a smooth covering of an algebraic space
> over `S` with a smooth covering of each of its members gives a smooth covering.

```lean
theorem isSmoothCovering_comp
    {I : Type v} {J : I → Type w} {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (X : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : ∀ i, X i ⟶ F)
    (Y : ∀ i, J i → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (g : ∀ i j, Y i j ⟶ X i)
    (hf : IsSmoothCovering B S hS X f)
    (hg : ∀ i, IsSmoothCovering B S hS (Y i) (g i)) :
    IsSmoothCovering B S hS (fun ij : Σ i, J i ↦ Y ij.1 ij.2)
      (fun ij : Σ i, J i ↦ g ij.1 ij.2 ≫ f ij.1)
```

**`AlgebraicGeometry.Space.isSmoothCovering_fiberProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmoothCoverings.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmoothCoverings.lean#L113). The attribute's comment: “base_change”.

> **Stacks 041D**, the base-change clause. The first projections of the fibre products of a
> smooth covering of an algebraic space over `S` with a morphism `g` into its target form a
> smooth covering of the source of `g`.

```lean
theorem isSmoothCovering_fiberProduct
    {I : Type v} {X X' : AlgebraicSpaces B S hS} (Xi : I → AlgebraicSpaces B S hS)
    (f : ∀ i, Xi i ⟶ X) (g : X' ⟶ X)
    (hf : IsSmoothCovering B S hS (fun i ↦ (Xi i).1) (fun i ↦ (f i).hom)) :
    IsSmoothCovering B S hS (fun i ↦ (AlgebraicSpaces.fiberProduct B S hS g (f i)).1)
      (fun i ↦ pullback.fst g.hom (f i).hom)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 73.5, Tag 03YB](https://stacks.math.columbia.edu/tag/03YB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
