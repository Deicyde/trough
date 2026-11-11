---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.objectOverStarModObj, CategoryTheory.ModObj, CategoryTheory.IsModHom, AlgebraicGeometry.Space.IsFreeAction, AlgebraicGeometry.Space.isFreeAction_iff_mono_leftSMul
statement: formalized
proof: formalized
---

# 78.8 Actions of group algebraic spaces

Section 78.8 of the Stacks Project, [Tag 043P](https://stacks.math.columbia.edu/tag/043P). 4 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 043Q, a definition

[Tag 043Q](https://stacks.math.columbia.edu/tag/043Q) in the Stacks Project.

**`AlgebraicGeometry.Space.objectOverStarModObj`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ActionInSite.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ActionInSite.lean#L109). The attribute's comment: “part (1): the action over `B` attached to an action on points”.

> **Stacks Project, Tag 043Q, part (1).** An action of a presheaf of groups on a presheaf over
> the big fppf site over `S` is an action of `B ×_S G` on `B ×_S X` in presheaves over `B`.

```lean
noncomputable instance objectOverStarModObj (F : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ GrpCat.{u})
    (P : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u) [ModObj (F ⋙ forget GrpCat) P] :
    ModObj (groupOverStar 𝒞 S hS B F) (objectOverStar 𝒞 S hS B P)
```

Declarations registered for the tag:

- [`CategoryTheory.ModObj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ModObj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActions.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActions.lean#L107) (StacksFrontier): “part (1): action of a group algebraic space”.
- [`CategoryTheory.IsModHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.IsModHom#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActions.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActions.lean#L108) (StacksFrontier): “part (2): equivariant morphism”.

## Tag 043R, an equation

[Tag 043R](https://stacks.math.columbia.edu/tag/043R) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.ModObj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ModObj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActions.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActions.lean#L109) (StacksFrontier): “the unit and associativity diagrams of a group action”.

## Tag 06P8, a definition

[Tag 06P8](https://stacks.math.columbia.edu/tag/06P8) in the Stacks Project.

**`AlgebraicGeometry.Space.IsFreeAction`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActions.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActions.lean#L114).

> **Stacks Project, Tag 06P8.** A group object over `B` acts freely on `X` when its
> action is free on the points of every scheme over `B`.

```lean
abbrev IsFreeAction (𝒞 : BigFppfSite.{u}) (S : Scheme.{u}) (hS : 𝒞.Contains S)
    (B : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u) (G X : Over B) [GrpObj G] [ModObj G X] : Prop
```

## Tag 06P9, a lemma

[Tag 06P9](https://stacks.math.columbia.edu/tag/06P9) in the Stacks Project.

**`AlgebraicGeometry.Space.isFreeAction_iff_mono_leftSMul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FreeAction.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FreeAction.lean#L80). References: SGA 3 IV (3.2.1), “(i), special case”.

> **Stacks 06P9.** An action of a group algebraic space is free exactly when the
> action–projection morphism `G ×_B X ⟶ X ×_B X`, `(g, x) ↦ (g · x, x)`, is a monomorphism.

```lean
theorem isFreeAction_iff_mono_leftSMul (G X : Over B) [GrpObj G] [ModObj G X] :
    IsFreeAction 𝒞 S hS B G X ↔ Mono (ModObj.leftSMul G X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.8, Tag 043P](https://stacks.math.columbia.edu/tag/043P)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
