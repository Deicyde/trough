---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.HasUniversallyBoundedFibers, AlgebraicGeometry.Space.hasUniversallyBoundedFibers_comp, AlgebraicGeometry.Space.hasUniversallyBoundedFibers_baseChange, AlgebraicGeometry.Space.hasUniversallyBoundedFibers_of_baseChange_of_range_subset, AlgebraicGeometry.Space.hasUniversallyBoundedFibers_of_comp_of_surjective_flat, AlgebraicGeometry.Space.cardinalMk_pointFiber_le_of_hasUniversallyBoundedFibers
statement: formalized
proof: formalized
---

# 68.3 Universally bounded fibres

Section 68.3 of the Stacks Project, [Tag 03JK](https://stacks.math.columbia.edu/tag/03JK). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03JL, a definition

[Tag 03JL](https://stacks.math.columbia.edu/tag/03JL) in the Stacks Project.

**`AlgebraicGeometry.Space.HasUniversallyBoundedFibers`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/UniversallyBoundedFibres.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/UniversallyBoundedFibres.lean#L57).

> A scheme morphism to a presheaf has universally bounded fibres if every field-valued
> base change is represented by a finite scheme and all their degrees have one integer bound.

```lean
abbrev HasUniversallyBoundedFibers (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (U : BigFppfOver B S hS)
    (f : yoneda.obj U ⟶ X) : Prop
```

## Tag 03JM, a lemma

[Tag 03JM](https://stacks.math.columbia.edu/tag/03JM) in the Stacks Project.

**`AlgebraicGeometry.Space.hasUniversallyBoundedFibers_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/UniversallyBoundedFibresComposition.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/UniversallyBoundedFibresComposition.lean#L170).

> **Stacks 03JM.** Let `X` be a presheaf on the big fppf site of `S`, let `f : V ⟶ U` be a
> morphism of schemes over `S` and let `g : U ⟶ X` be a morphism over `S`. If the fibres of `f`
> and of `g` are universally bounded, then so are the fibres of the composite `V ⟶ X`.

```lean
theorem hasUniversallyBoundedFibers_comp
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {V U : BigFppfOver B S hS}
    (f : V ⟶ U) (g : yoneda.obj U ⟶ X)
    (hf : HasUniversallyBoundedFibers B S hS V (yoneda.map f))
    (hg : HasUniversallyBoundedFibers B S hS U g) :
    HasUniversallyBoundedFibers B S hS V (yoneda.map f ≫ g)
```

## Tag 03JN, a lemma

[Tag 03JN](https://stacks.math.columbia.edu/tag/03JN) in the Stacks Project.

**`AlgebraicGeometry.Space.hasUniversallyBoundedFibers_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/UniversallyBoundedFibres.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/UniversallyBoundedFibres.lean#L72).

> A representable base change of a scheme morphism with universally bounded fibres
> is represented by a scheme whose fibres remain universally bounded.

```lean
theorem hasUniversallyBoundedFibers_baseChange
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (g : Y ⟶ X) (hg : yoneda.relativelyRepresentable g)
    (U : BigFppfOver B S hS) (f : yoneda.obj U ⟶ X)
    (hf : HasUniversallyBoundedFibers B S hS U f) :
    ∃ (V : BigFppfOver B S hS)
      (i : yoneda.obj V ⟶ yoneda.obj U) (p : yoneda.obj V ⟶ Y),
      IsPullback i p f g ∧ HasUniversallyBoundedFibers B S hS V p
```

## Tag 03JO, a lemma

[Tag 03JO](https://stacks.math.columbia.edu/tag/03JO) in the Stacks Project.

**`AlgebraicGeometry.Space.hasUniversallyBoundedFibers_of_baseChange_of_range_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/UniversallyBoundedFibresDescent.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/UniversallyBoundedFibresDescent.lean#L298).

> **Stacks 03JO.** Let `g : Y ⟶ X` be a morphism of algebraic spaces over `S`, let
> `f : h_U ⟶ X` be a morphism from a scheme over `S`, and let `h_V ⟶ Y` be a base change of `f`
> along `g`. If the image of `|h_U| → |X|` is contained in the image of `|Y| → |X|` and the
> fibres of `h_V ⟶ Y` are universally bounded, then the fibres of `f` are universally
> bounded, with the same bound.

```lean
theorem hasUniversallyBoundedFibers_of_baseChange_of_range_subset
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (g : Y ⟶ X)
    {U : BigFppfOver B S hS} (f : yoneda.obj U ⟶ X)
    (himage : Set.range (pointsMap B S hS (yoneda.obj U) f) ⊆
      Set.range (pointsMap B S hS Y g))
    {V : BigFppfOver B S hS} {i : yoneda.obj V ⟶ yoneda.obj U} {p : yoneda.obj V ⟶ Y}
    (hcart : IsPullback i p f g) (hp : HasUniversallyBoundedFibers B S hS V p) :
    HasUniversallyBoundedFibers B S hS U f
```

## Tag 03JP, a lemma

[Tag 03JP](https://stacks.math.columbia.edu/tag/03JP) in the Stacks Project.

**`AlgebraicGeometry.Space.hasUniversallyBoundedFibers_of_comp_of_surjective_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/UniversallyBoundedFibresDescent.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/UniversallyBoundedFibresDescent.lean#L127).

> **Stacks 03JP.** Let `X` be an algebraic space over `S`, let `U ⟶ V` be a morphism of
> schemes over `S` and let `V ⟶ X` be a morphism over `S`. If the fibres of the composite
> `U ⟶ X` are universally bounded and `U ⟶ V` is surjective and flat, then the fibres of
> `V ⟶ X` are universally bounded, with the same bound.

```lean
theorem hasUniversallyBoundedFibers_of_comp_of_surjective_flat
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    {U V : BigFppfOver B S hS} (φ : U ⟶ V) (h : yoneda.obj V ⟶ X)
    [AlgebraicGeometry.Surjective ((BigFppfOver.toScheme B S hS).map φ)]
    [AlgebraicGeometry.Flat ((BigFppfOver.toScheme B S hS).map φ)]
    (hU : HasUniversallyBoundedFibers B S hS U (yoneda.map φ ≫ h)) :
    HasUniversallyBoundedFibers B S hS V h
```

## Tag 03JQ, a lemma

[Tag 03JQ](https://stacks.math.columbia.edu/tag/03JQ) in the Stacks Project.

**`AlgebraicGeometry.Space.cardinalMk_pointFiber_le_of_hasUniversallyBoundedFibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/BoundedPointFibres.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/BoundedPointFibres.lean#L84).

> **Stacks 03JQ.** If the fibres of a morphism `f : h_U ⟶ X` from a represented presheaf
> are universally bounded, then one natural number bounds the number of points of `|h_U|`
> lying above each point of `|X|`.

```lean
theorem cardinalMk_pointFiber_le_of_hasUniversallyBoundedFibers
    (hf : HasUniversallyBoundedFibers B S hS U f) :
    ∃ n : ℕ, ∀ x : points B S hS X,
      Cardinal.mk (pointsMap B S hS (yoneda.obj U) f ⁻¹' {x}) ≤ (n : Cardinal)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.3, Tag 03JK](https://stacks.math.columbia.edu/tag/03JK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
