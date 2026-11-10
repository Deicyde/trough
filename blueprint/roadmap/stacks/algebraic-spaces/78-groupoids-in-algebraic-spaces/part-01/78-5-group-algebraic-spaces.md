---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.GroupAlgebraicSpace, AlgebraicGeometry.Space.groupOverStarGrpObj, AlgebraicGeometry.Space.GroupAlgebraicSpace.baseChange, AlgebraicGeometry.Space.GroupAlgebraicSpace.baseChange_obj_X, AlgebraicGeometry.Space.GroupAlgebraicSpace.ofGroupSchemeInSite, AlgebraicGeometry.Space.isSmooth_prod_fst_multiplicativeGroupULift
statement: formalized
proof: formalized
---

# 78.5 Group algebraic spaces

Section 78.5 of the Stacks Project, [Tag 043G](https://stacks.math.columbia.edu/tag/043G). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 043H, a definition

[Tag 043H](https://stacks.math.columbia.edu/tag/043H) in the Stacks Project.

**`AlgebraicGeometry.Space.GroupAlgebraicSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActions.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActions.lean#L101).

> **Stacks Project, Tag 043H.** Group algebraic spaces over an algebraic space `B`.  An
> object is a group object in presheaves over `B` whose underlying presheaf is an algebraic
> space; morphisms are group-object morphisms over `B`.

```lean
noncomputable abbrev GroupAlgebraicSpace (𝒞 : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : 𝒞.Contains S) (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    (_hB : IsAlgebraicSpace 𝒞 S hS B)
```

## Tag 043I, a lemma

[Tag 043I](https://stacks.math.columbia.edu/tag/043I) in the Stacks Project.

**`AlgebraicGeometry.Space.groupOverStarGrpObj`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ActionInSite.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ActionInSite.lean#L98). The attribute's comment: “the group object over `B` attached to a presheaf of groups on the site”.

> **Stacks Project, Tag 043I.** `B ×_S G` is a group object of presheaves over `B`, with the
> pointwise group law of the given presheaf of groups.

```lean
noncomputable instance groupOverStarGrpObj (F : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ GrpCat.{u}) :
    GrpObj (groupOverStar 𝒞 S hS B F)
```

**`AlgebraicGeometry.Space.GroupAlgebraicSpace.baseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseChange.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseChange.lean#L215).

> **Stacks Project, Tag 043I.** The pullback of a group algebraic space over `B` along a
> morphism `B' ⟶ B` of algebraic spaces is a group algebraic space over `B'`.

```lean
noncomputable def GroupAlgebraicSpace.baseChange
    {B B' : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u} {hB : IsAlgebraicSpace 𝒞 S hS B}
    (hB' : IsAlgebraicSpace 𝒞 S hS B') (f : B' ⟶ B)
    (G : GroupAlgebraicSpace 𝒞 S hS B hB) :
    GroupAlgebraicSpace 𝒞 S hS B' hB'
```

**`AlgebraicGeometry.Space.GroupAlgebraicSpace.baseChange_obj_X`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseChange.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseChange.lean#L226). The attribute's comment: “the underlying pullback”.

> **Stacks Project, Tag 043I.** The algebraic space underlying the pullback of a group
> algebraic space is the fibre product of the original one with the new base.

```lean
theorem GroupAlgebraicSpace.baseChange_obj_X
    {B B' : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u} {hB : IsAlgebraicSpace 𝒞 S hS B}
    (hB' : IsAlgebraicSpace 𝒞 S hS B') (f : B' ⟶ B)
    (G : GroupAlgebraicSpace 𝒞 S hS B hB) :
    (GroupAlgebraicSpace.baseChange 𝒞 S hS hB' f G).obj.X =
      (Over.mk (pullback.snd G.obj.X.hom f) : Over B')
```

**`AlgebraicGeometry.Space.GroupAlgebraicSpace.ofGroupSchemeInSite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseChange.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/BaseChange.lean#L355). The attribute's comment: “the group algebraic space attached to a group scheme over the base”.

> **Stacks Project, Tag 043I.** The group algebraic space `G_B = B ×_S G` over an algebraic
> space `B` over `S` attached to a group scheme `G` over `S` belonging to the big fppf site: it is
> the base change of `G`, regarded as a group algebraic space over the terminal algebraic space,
> along the structure morphism of `B`.  Its points over a scheme `T` over `B` are the morphisms
> `T ⟶ G` of schemes over `S`.

```lean
noncomputable def GroupAlgebraicSpace.ofGroupSchemeInSite
    (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u) (hB : IsAlgebraicSpace 𝒞 S hS B)
    (G : BigFppfOver 𝒞 S hS) (hG : GrpObj ((toSchemeOver 𝒞 S hS).obj G)) :
    GroupAlgebraicSpace 𝒞 S hS B hB
```

**`AlgebraicGeometry.Space.isSmooth_prod_fst_multiplicativeGroupULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/MultiplicativeSmooth.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/Examples/MultiplicativeSmooth.lean#L98). The attribute's comment: “the structure morphism of the multiplicative group algebraic space is smooth”. References: SGA 3 VIII (2.1), “(e), special case”.

> The structure morphism of the group algebraic space `Gₘ,B = B ×_{Spec ℤ} Gₘ` over an
> arbitrary algebraic space `B` over `Spec ℤ` is a smooth morphism of algebraic spaces.

```lean
theorem isSmooth_prod_fst_multiplicativeGroupULift
    (B : (BigFppfOver 𝒞 (Spec (.of (ULift.{u} ℤ))) (contains_specULiftZ 𝒞))ᵒᵖ ⥤ Type u)
    (hB : IsAlgebraicSpace 𝒞 (Spec (.of (ULift.{u} ℤ))) (contains_specULiftZ 𝒞) B) :
    IsSmooth 𝒞 (Spec (.of (ULift.{u} ℤ))) (contains_specULiftZ 𝒞)
      (prod.fst : B ⨯ (pointsOnSite 𝒞 (Spec (.of (ULift.{u} ℤ))) (contains_specULiftZ 𝒞)
        (multiplicativeGroupULiftSiteObject 𝒞)
        (multiplicativeGroupULiftSiteObjectGrpObj 𝒞) ⋙ forget GrpCat) ⟶ B)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.5, Tag 043G](https://stacks.math.columbia.edu/tag/043G)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
