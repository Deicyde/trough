---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isGeometricallyUnibranchAt_of_isFlatAt, AlgebraicGeometry.Space.isReduced_of_flat_of_surjective, AlgebraicGeometry.Space.isLocallyNoetherian_of_isSurjective_of_isFlat_of_isLocallyOfFinitePresentation, AlgebraicGeometry.Space.hasEtaleLocalProperty_isRegular_of_isSurjective_of_isFlat_of_isLocallyOfFinitePresentation, AlgebraicGeometry.Space.hasEtaleLocalPropertyULift_isReduced_of_isSmoothULift, AlgebraicGeometry.Space.isReduced_source_of_isSmooth
statement: formalized
proof: formalized
---

# 74.9 Descending properties of spaces

Section 74.9 of the Stacks Project, [Tag 06DP](https://stacks.math.columbia.edu/tag/06DP). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06DQ, a lemma

[Tag 06DQ](https://stacks.math.columbia.edu/tag/06DQ) in the Stacks Project.

**`AlgebraicGeometry.Space.isGeometricallyUnibranchAt_of_isFlatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/GeometricallyUnibranch.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/GeometricallyUnibranch.lean#L108).

> **Stacks 06DQ.** Let `f : F ⟶ G` be a morphism of algebraic spaces over a scheme `S` and
> let `x` be a point of `|F|`. If `f` is flat at `x` and `F` is geometrically unibranch at `x`,
> then `G` is geometrically unibranch at `f(x)`.

```lean
theorem isGeometricallyUnibranchAt_of_isFlatAt (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) (x : points B S hS F)
    (hf : IsFlatAt B S hS f x) (hx : IsGeometricallyUnibranchAt B S hS F x) :
    IsGeometricallyUnibranchAt B S hS G (pointsMap B S hS F f x)
```

## Tag 06MI, a lemma

[Tag 06MI](https://stacks.math.columbia.edu/tag/06MI) in the Stacks Project.

**`AlgebraicGeometry.Space.isReduced_of_flat_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/Reduced.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/Reduced.lean#L41).

> A flat surjective morphism of algebraic spaces over `S` whose source is reduced has reduced
> target.

```lean
theorem isReduced_of_flat_of_surjective
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y)
    (hflat : IsFlat B S hS f)
    (hsurj : IsSurjective B S hS f)
    (hred : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsReduced T)) :
    HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsReduced T)
```

## Tag 06MJ, a lemma

[Tag 06MJ](https://stacks.math.columbia.edu/tag/06MJ) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyNoetherian_of_isSurjective_of_isFlat_of_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/Noetherian.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/Noetherian.lean#L85).

> **Stacks 06MJ.** Local Noetherianity passes from the source of a surjective, flat
> morphism of algebraic spaces over `S` locally of finite presentation to its target.
>
> This is the case `P = AlgebraicGeometry.IsLocallyNoetherian` of
> `hasEtaleLocalProperty_of_isSurjective_of_isFlat_of_isLocallyOfFinitePresentation`, whose two
> locality hypotheses hold for local Noetherianity of schemes.

```lean
theorem isLocallyNoetherian_of_isSurjective_of_isFlat_of_isLocallyOfFinitePresentation
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y)
    (hfp : IsLocallyOfFinitePresentation B S hS f)
    (hflat : IsFlat B S hS f)
    (hsurj : IsSurjective B S hS f)
    (hnoeth : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T)) :
    HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsLocallyNoetherian T)
```

## Tag 06MK, a lemma

[Tag 06MK](https://stacks.math.columbia.edu/tag/06MK) in the Stacks Project.

**`AlgebraicGeometry.Space.hasEtaleLocalProperty_isRegular_of_isSurjective_of_isFlat_of_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/Regular.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/Regular.lean#L109). References: SGA 1 I (9.2), “converse (X reg ⇒ Y reg)”.

> **Stacks 06MK.** Regularity passes from the source of a surjective, flat morphism of
> algebraic spaces over `S` locally of finite presentation to its target.
>
> A regular scheme is locally Noetherian, so a regular étale chart of the source witnesses local
> Noetherianity of the source; Stacks 06MJ carries that to the target, and
> `hasEtaleLocalProperty_isRegular_of_isSurjective_of_isFlat` then applies.

```lean
theorem hasEtaleLocalProperty_isRegular_of_isSurjective_of_isFlat_of_isLocallyOfFinitePresentation
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y)
    (hfp : IsLocallyOfFinitePresentation B S hS f)
    (hflat : IsFlat B S hS f)
    (hsurj : IsSurjective B S hS f)
    (hreg : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsRegular T)) :
    HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsRegular T)
```

## Tag 0GB3, a lemma

[Tag 0GB3](https://stacks.math.columbia.edu/tag/0GB3) in the Stacks Project.

**`AlgebraicGeometry.Space.hasEtaleLocalPropertyULift_isReduced_of_isSmoothULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSmoothBaseChange.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ReductionSmoothBaseChange.lean#L143). The attribute's comment: “reducedness of the source, in an arbitrary value universe”.

> **Stacks 0GB3, reducedness of the source**, for presheaves with values in a universe
> `max w u` independent of the universe `u` of the schemes: a smooth morphism of algebraic spaces
> over `S` whose target is reduced has reduced source.
>
> A reduced surjective étale atlas `V` of the target and an atlas `W` of the base change of the
> morphism along it form a commuting square of étale charts, so the scheme morphism `W ⟶ V` is
> smooth and `W` is reduced by Stacks 033B; it is a reduced surjective étale atlas of the
> source.

```lean
theorem hasEtaleLocalPropertyULift_isReduced_of_isSmoothULift
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (max w u)}
    (hF : IsAlgebraicSpaceULift.{w} B S hS F) (hG : IsAlgebraicSpaceULift.{w} B S hS G)
    (f : F ⟶ G) (hf : IsSmoothULift.{w} B S hS f)
    (hred : HasEtaleLocalPropertyULift.{w} B S hS G (fun T : Scheme.{u} ↦ IsReduced T)) :
    HasEtaleLocalPropertyULift.{w} B S hS F (fun T : Scheme.{u} ↦ IsReduced T)
```

**`AlgebraicGeometry.Space.isReduced_of_flat_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/Reduced.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/Reduced.lean#L41). The attribute's comment: “reducedness of the target under surjectivity”.

> A flat surjective morphism of algebraic spaces over `S` whose source is reduced has reduced
> target.

```lean
theorem isReduced_of_flat_of_surjective
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y)
    (hflat : IsFlat B S hS f)
    (hsurj : IsSurjective B S hS f)
    (hred : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsReduced T)) :
    HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsReduced T)
```

**`AlgebraicGeometry.Space.isReduced_source_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/Reduced.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Properties/Reduced.lean#L64). The attribute's comment: “reducedness of the source”. References: SGA 1 II (3.1), “reduced, Y ⇒ X”.

> A smooth morphism of algebraic spaces over `S` whose target is reduced has reduced source.

```lean
theorem isReduced_source_of_isSmooth
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (hf : IsSmooth B S hS f)
    (hred : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsReduced T)) :
    HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsReduced T)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.9, Tag 06DP](https://stacks.math.columbia.edu/tag/06DP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
