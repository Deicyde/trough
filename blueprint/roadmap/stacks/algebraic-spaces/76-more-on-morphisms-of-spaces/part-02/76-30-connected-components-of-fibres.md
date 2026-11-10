---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.numberGeometricConnectedComponents_eq, AlgebraicGeometry.Space.numberGeometricConnectedComponents_baseChange, AlgebraicGeometry.Space.numberGeometricConnectedComponents
statement: formalized
proof: formalized
---

# 76.30 Connected components of fibres

Section 76.30 of the Stacks Project, [Tag 0E1A](https://stacks.math.columbia.edu/tag/0E1A). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E1B, a lemma

[Tag 0E1B](https://stacks.math.columbia.edu/tag/0E1B) in the Stacks Project.

**`AlgebraicGeometry.Space.numberGeometricConnectedComponents_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricComponentCount.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricComponentCount.lean#L352). The attribute's comment: “well-definedness”. References: EGA III (4.3.4), “more general”; EGA IV (4.5.1), “partial”.

> **Stacks 0E1B.** The number of geometric connected components of the fibres of a morphism
> of algebraic spaces is, at the image of a geometric point, the number of connected components
> of the fibre over that geometric point. In particular the defining infimum is attained at every
> geometric representative.

```lean
theorem numberGeometricConnectedComponents_eq (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) (p : GeometricPoint B S hS G) :
    numberGeometricConnectedComponents B S hS f p.image =
      geometricFiberComponentCount B S hS f p.val
```

**`AlgebraicGeometry.Space.numberGeometricConnectedComponents_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricComponentCount.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricComponentCount.lean#L372). The attribute's comment: “base change”.

> **Stacks 0E1B.** Formation of the number of geometric connected components of the fibres
> commutes with arbitrary base change: the function attached to the projection `F ×_G H ⟶ H` is
> the function attached to `f : F ⟶ G` composed with the map `|H| → |G|` on points.

```lean
theorem numberGeometricConnectedComponents_baseChange
    {H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (hH : IsAlgebraicSpace B S hS H) (f : F ⟶ G) (g : H ⟶ G) :
    numberGeometricConnectedComponents B S hS (pullback.snd f g) =
      numberGeometricConnectedComponents B S hS f ∘ pointsMap B S hS H g
```

**`AlgebraicGeometry.Space.numberGeometricConnectedComponents`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/GeometricComponents.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/GeometricComponents.lean#L114). The attribute's comment: “function”. References: EGA III (4.3.4); EGA IV (4.5.2), “partial”.

> **Stacks 0E1B.** The number of geometric connected components of the fibres of a morphism
> of algebraic spaces: the function on the points of the target whose value at `y` is the number
> of connected components of the fibre over any geometric point representing `y`.
>
> By `AlgebraicGeometry.Space.exists_geometricRepresentative` the set whose infimum is taken is
> nonempty, and the source lemma is that all of its elements agree.

```lean
noncomputable def numberGeometricConnectedComponents
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : F ⟶ G) : points B S hS G → ℕ∞
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.30, Tag 0E1A](https://stacks.math.columbia.edu/tag/0E1A)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
