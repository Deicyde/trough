---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.isSurjective_iff_isSurjectiveULift_red, AlgebraicGeometry.FormalSpace.IsSurjective.comp, AlgebraicGeometry.FormalSpace.IsSurjective.of_isPullback, AlgebraicGeometry.FormalSpace.IsSurjective.hasSurjectiveFormalAtlas, AlgebraicGeometry.FormalSpace.isSurjective_of_hasSurjectiveFormalAtlas, AlgebraicGeometry.FormalSpace.isSurjective_tfae
statement: formalized
proof: formalized
---

# 87.25 Surjective morphisms

Section 87.25 of the Stacks Project, [Tag 0GHN](https://stacks.math.columbia.edu/tag/0GHN). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GHP, a definition

[Tag 0GHP](https://stacks.math.columbia.edu/tag/0GHP) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isSurjective_iff_isSurjectiveULift_red`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Surjective.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Surjective.lean#L97). The attribute's comment: “the definition, identified with the source's condition on the morphism of underlying reduced algebraic spaces”.

> Surjectivity on points of a morphism of formal algebraic spaces over `S` is the condition
> of Stacks 0GHP on it: the morphism between any two reductions of its source and target
> compatible with it is a surjective morphism of algebraic spaces exactly when the morphism
> itself is surjective on points.

```lean
theorem isSurjective_iff_isSurjectiveULift_red {X Y Xred Yred : FppfSheaf B S hS}
    {iX : Xred ⟶ X} {iY : Yred ⟶ Y}
    (hiX : IsReduction B S hS X Xred iX) (hiY : IsReduction B S hS Y Yred iY)
    {f : X ⟶ Y} {fred : Xred ⟶ Yred} (hfred : fred ≫ iY = iX ≫ f) :
    IsSurjective B S hS f ↔ Space.IsSurjectiveULift.{u + 1} B S hS fred.hom
```

## Tag 0GHQ, a lemma

[Tag 0GHQ](https://stacks.math.columbia.edu/tag/0GHQ) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsSurjective.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Surjective.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Surjective.lean#L128).

> The composition of two surjective morphisms of fppf sheaves on the big fppf site of `S` is
> surjective.

```lean
theorem IsSurjective.comp {X Y Z : FppfSheaf B S hS} {f : X ⟶ Y} {g : Y ⟶ Z}
    (hf : IsSurjective B S hS f) (hg : IsSurjective B S hS g) :
    IsSurjective B S hS (f ≫ g)
```

## Tag 0GHR, a lemma

[Tag 0GHR](https://stacks.math.columbia.edu/tag/0GHR) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsSurjective.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Surjective.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Surjective.lean#L143).

> A base change of a surjective morphism of fppf sheaves on the big fppf site of `S` is
> surjective.

```lean
theorem IsSurjective.of_isPullback {W X Z Y : FppfSheaf B S hS}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y} (sq : IsPullback p q g f)
    (hf : IsSurjective B S hS f) : IsSurjective B S hS p
```

## Tag 0GHS, a lemma

[Tag 0GHS](https://stacks.math.columbia.edu/tag/0GHS) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsSurjective.hasSurjectiveFormalAtlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Surjective.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Surjective.lean#L306). The attribute's comment: “condition (1) implies condition (4)”.

> **Stacks 0GHS, condition (1) implies condition (4).** If `f : X ⟶ Y` is surjective and `Y`
> is a formal algebraic space over `S`, then the atlas of `Y` furnished by Stacks 0AIM is a
> covering `{Y_j ⟶ Y}` as in Definition 0AIM along which every base change of `f` is
> surjective.

```lean
theorem IsSurjective.hasSurjectiveFormalAtlas {X Y : FppfSheaf B S hS} {f : X ⟶ Y}
    (hY : IsFormalAlgebraicSpace B S hS Y) (hf : IsSurjective B S hS f) :
    HasSurjectiveFormalAtlas B S hS f
```

**`AlgebraicGeometry.FormalSpace.isSurjective_of_hasSurjectiveFormalAtlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Surjective.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Surjective.lean#L317). The attribute's comment: “condition (4) implies condition (1)”.

> **Stacks 0GHS, condition (4) implies condition (1).** If a morphism `f : X ⟶ Y` of fppf
> sheaves on the big fppf site of `S` admits a covering `{Y_j ⟶ Y}` of its target as in
> Definition 0AIM along which every base change of `f` is surjective, then `f` is surjective.

```lean
theorem isSurjective_of_hasSurjectiveFormalAtlas {X Y : FppfSheaf B S hS} {f : X ⟶ Y}
    (h : HasSurjectiveFormalAtlas B S hS f) : IsSurjective B S hS f
```

**`AlgebraicGeometry.FormalSpace.isSurjective_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Surjective.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Surjective.lean#L338). The attribute's comment: “conditions (1), (2), (3), (4) and (5)”.

> For a morphism `f : X ⟶ Y` of formal algebraic spaces over `S` the following are
> equivalent:
>
> 1. `f` is surjective;
> 2. for every scheme `T` over `S` in the site and every `T ⟶ Y` the projection
>    `X ×_Y T ⟶ T` is surjective;
> 3. the same for every affine scheme `T` over `S` in the site;
> 4. there is a covering `{Y_j ⟶ Y}` as in Definition 0AIM such that each projection
>    `X ×_Y Y_j ⟶ Y_j` is surjective;
> 5. there is a surjective morphism `Z ⟶ Y` of formal algebraic spaces over `S` such that
>    `X ×_Y Z ⟶ Z` is surjective.

```lean
theorem isSurjective_tfae {X Y : FppfSheaf B S hS} (hY : IsFormalAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) :
    List.TFAE
      [IsSurjective B S hS f,
        IsSurjectiveOnSchemeBaseChanges B S hS f,
        IsSurjectiveOnAffineBaseChanges B S hS f,
        HasSurjectiveFormalAtlas B S hS f,
        HasSurjectiveFormalCover B S hS f]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.25, Tag 0GHN](https://stacks.math.columbia.edu/tag/0GHN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
