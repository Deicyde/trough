---
declaration: section
origin: cited
lean: AlgebraicGeometry.relativeWeaklyAssociatedPoints, AlgebraicGeometry.relativeWeaklyAssociatedPoints_eq_relativeAssassin, AlgebraicGeometry.relativeWeaklyAssociatedPoints_pushforward_eq_image
statement: formalized
proof: formalized
---

# 31.8 Relative weak assassin

Section 31.8 of the Stacks Project, [Tag 05AU](https://stacks.math.columbia.edu/tag/05AU). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05AV, a definition

[Tag 05AV](https://stacks.math.columbia.edu/tag/05AV) in the Stacks Project.

**`AlgebraicGeometry.relativeWeaklyAssociatedPoints`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/RelativeWeakAssassin.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/RelativeWeakAssassin.lean#L54).

> **Stacks Project, Tag 05AV.** The relative weak assassin of an `𝒪_X`-module `F` along
> `f : X ⟶ S`, viewed as a set of points of `X`.

```lean
noncomputable abbrev relativeWeaklyAssociatedPoints {X S : Scheme.{u}} (f : X ⟶ S)
    (F : X.Modules) : Set X
```

## Tag 05F2, a lemma

[Tag 05F2](https://stacks.math.columbia.edu/tag/05F2) in the Stacks Project.

**`AlgebraicGeometry.relativeWeaklyAssociatedPoints_eq_relativeAssassin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/RelativeWeakAssassin.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AssociatedPoints/RelativeWeakAssassin.lean#L62).

> **Stacks Project, Tag 05F2.** For a morphism locally of finite type the relative weak
> assassin of a module is its relative assassin.

```lean
theorem relativeWeaklyAssociatedPoints_eq_relativeAssassin {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (F : X.Modules) :
    relativeWeaklyAssociatedPoints f F = Stacks.Divisors.relativeAssassin f F
```

## Tag 0CUD, a lemma

[Tag 0CUD](https://stacks.math.columbia.edu/tag/0CUD) in the Stacks Project.

**`AlgebraicGeometry.relativeWeaklyAssociatedPoints_pushforward_eq_image`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RelativeWeakAssassin/FinitePushforward.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/RelativeWeakAssassin/FinitePushforward.lean#L111).

> **Stacks Project, Tag 0CUD.**  The relative weak assassin of a finite direct image is the
> image of the relative weak assassin on the source.

```lean
theorem relativeWeaklyAssociatedPoints_pushforward_eq_image
    {Z X S : Scheme.{u}} (f : X ⟶ S) (i : Z ⟶ X) [IsFinite i]
    (F : Z.Modules) [F.IsQuasicoherent] :
    relativeWeaklyAssociatedPoints f ((Scheme.Modules.pushforward i).obj F) =
      i '' relativeWeaklyAssociatedPoints (i ≫ f) F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.8, Tag 05AU](https://stacks.math.columbia.edu/tag/05AU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
