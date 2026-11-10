---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsQuasiCompactSpace, AlgebraicGeometry.Space.isQuasiCompactSpaceULift_iff_compactSpace_pointsULift, AlgebraicGeometry.Space.isQuasiCompactSpace_iff_compactSpace_points, AlgebraicGeometry.Space.isAlgebraicSpace_finiteCoproduct, AlgebraicGeometry.Space.isQuasiCompactSpace_finiteCoproduct, AlgebraicGeometry.Space.hasBasis_nhds_isOpen_isCompact, AlgebraicGeometry.Space.locallyCompactSpace
statement: formalized
proof: formalized
---

# 66.5 Quasi-compact spaces

Section 66.5 of the Stacks Project, [Tag 03E2](https://stacks.math.columbia.edu/tag/03E2). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03E3, a definition

[Tag 03E3](https://stacks.math.columbia.edu/tag/03E3) in the Stacks Project.

**`AlgebraicGeometry.Space.IsQuasiCompactSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean#L237).

> **Stacks 03E3.** An algebraic space over `S` is *quasi-compact* when it admits a
> surjective étale morphism from a representable presheaf whose underlying scheme is
> quasi-compact.

```lean
abbrev IsQuasiCompactSpace (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) : Prop
```

## Tag 03E4, a lemma

[Tag 03E4](https://stacks.math.columbia.edu/tag/03E4) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiCompactSpaceULift_iff_compactSpace_pointsULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedQuasiCompactPoints.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedQuasiCompactPoints.lean#L180). The attribute's comment: “for a value universe independent of the universe of the schemes”.

> **Stacks 03E4** for a value universe `max w u` independent of the universe `u` of the
> schemes: an algebraic space over `S` is quasi-compact if and only if its space of points is
> quasi-compact.

```lean
theorem isQuasiCompactSpaceULift_iff_compactSpace_pointsULift
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (max w u)}
    (hF : IsAlgebraicSpaceULift.{w} B S hS F) :
    IsQuasiCompactSpaceULift.{w} B S hS F ↔ CompactSpace (pointsULift.{w} B S hS F)
```

**`AlgebraicGeometry.Space.isQuasiCompactSpace_iff_compactSpace_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointSpace.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactPointSpace.lean#L199).

> **Stacks 03E4.** An algebraic space over `S` is quasi-compact if and only if its space of
> points is quasi-compact.

```lean
theorem isQuasiCompactSpace_iff_compactSpace_points
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F) :
    IsQuasiCompactSpace B S hS F ↔ CompactSpace (points B S hS F)
```

## Tag 040T, a lemma

[Tag 040T](https://stacks.math.columbia.edu/tag/040T) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_finiteCoproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoproductQuasiCompact.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoproductQuasiCompact.lean#L92). The attribute's comment: “algebraicity”.

> **Stacks 040T, algebraicity.** A coproduct of finitely many algebraic spaces over `S` is
> an algebraic space over `S`.

```lean
theorem isAlgebraicSpace_finiteCoproduct {I : Type v} [Finite I]
    (F : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : ∀ i, IsAlgebraicSpace B S hS (F i))
    (G : Sheaf (BigFppfOver.topology B S hS) (Type u))
    (ι : ∀ i, (⟨F i, (hF i).isSheaf⟩ :
      Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶ G)
    (hG : IsColimit (Cofan.mk G ι)) : IsAlgebraicSpace B S hS G.obj
```

**`AlgebraicGeometry.Space.isQuasiCompactSpace_finiteCoproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoproductQuasiCompact.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoproductQuasiCompact.lean#L108). The attribute's comment: “quasi-compactness”.

> **Stacks 040T, quasi-compactness.** A coproduct of finitely many quasi-compact algebraic
> spaces over `S` is quasi-compact.

```lean
theorem isQuasiCompactSpace_finiteCoproduct {I : Type v} [Finite I]
    (F : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : ∀ i, IsAlgebraicSpace B S hS (F i))
    (hqc : ∀ i, IsQuasiCompactSpace B S hS (F i))
    (G : Sheaf (BigFppfOver.topology B S hS) (Type u))
    (ι : ∀ i, (⟨F i, (hF i).isSheaf⟩ :
      Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶ G)
    (hG : IsColimit (Cofan.mk G ι)) : IsQuasiCompactSpace B S hS G.obj
```

## Tag 04NN, a lemma

[Tag 04NN](https://stacks.math.columbia.edu/tag/04NN) in the Stacks Project.

**`AlgebraicGeometry.Space.hasBasis_nhds_isOpen_isCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LocallyCompactPoints.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LocallyCompactPoints.lean#L77). The attribute's comment: “fundamental system of open quasi-compact neighbourhoods”.

> The quasi-compact open neighbourhoods of a point of an algebraic space over `S` are a
> fundamental system of neighbourhoods of that point.

```lean
theorem hasBasis_nhds_isOpen_isCompact (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) (x : points B S hS F) :
    (nhds x).HasBasis
      (fun W : Set (points B S hS F) ↦ IsOpen W ∧ IsCompact W ∧ x ∈ W) id
```

**`AlgebraicGeometry.Space.locallyCompactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LocallyCompactPoints.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LocallyCompactPoints.lean#L89). The attribute's comment: “local quasi-compactness”.

> The space of points of an algebraic space over `S` is locally quasi-compact.

```lean
theorem locallyCompactSpace (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) : LocallyCompactSpace (points B S hS F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.5, Tag 03E2](https://stacks.math.columbia.edu/tag/03E2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
