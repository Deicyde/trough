---
declaration: section
origin: cited
lean: CategoryTheory.GradedObject, CategoryTheory.GradedObject.categoryOfGradedObjects, CategoryTheory.GradedObject.preadditive, CategoryTheory.GradedObject.abelian, CategoryTheory.GradedObject.hasShift, CategoryTheory.GradedObject.shiftFunctor_obj_apply, CategoryTheory.GradedObject.shiftFunctor_map_apply
statement: formalized
proof: formalized
---

# 12.16 Graded objects

Section 12.16 of the Stacks Project, [Tag 09MF](https://stacks.math.columbia.edu/tag/09MF). 3 tags here are carried by 2 declarations of the repository (all in StacksCore) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0125, a definition

[Tag 0125](https://stacks.math.columbia.edu/tag/0125) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.GradedObject`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GradedObject#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/GradedObject.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/GradedObject.lean#L30) (StacksCore): “for an arbitrary index type and an arbitrary category”.
- [`CategoryTheory.GradedObject.categoryOfGradedObjects`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GradedObject.categoryOfGradedObjects#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/GradedObject.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/GradedObject.lean#L32) (StacksCore): “the category structure”.

## Tag 0126, a lemma

[Tag 0126](https://stacks.math.columbia.edu/tag/0126) in the Stacks Project.

**`CategoryTheory.GradedObject.preadditive`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/GradedObject/Abelian.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/GradedObject/Abelian.lean#L164). The attribute's comment: “the preadditive structure, for an arbitrary index type”.

```lean
instance preadditive : Preadditive (GradedObject β C)
```

**`CategoryTheory.GradedObject.abelian`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/GradedObject/Abelian.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/GradedObject/Abelian.lean#L233). The attribute's comment: “for an arbitrary index type”.

> **Stacks 0126**: the category of graded objects of an abelian category is abelian.
> Stated for an arbitrary index type; the tag's statement is the case `β := ℤ`.

```lean
noncomputable instance abelian : Abelian (GradedObject β C)
```

## Tag 09MG, a definition

[Tag 09MG](https://stacks.math.columbia.edu/tag/09MG) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.GradedObject.hasShift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GradedObject.hasShift#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/GradedObject.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/GradedObject.lean#L34) (StacksCore): “for translation by any `s` in an `AddCommGroup` grading; the tag is `s := 1`”. References: EGA II (3.1.1), “partial”; SGA 6 VI (1.2), “partial”.
- [`CategoryTheory.GradedObject.shiftFunctor_obj_apply`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GradedObject.shiftFunctor_obj_apply#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/GradedObject.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/GradedObject.lean#L36) (StacksCore): “the computation rule: at `s := 1` it is the tag's `A[k]^i = A^{k + i}`”. References: EGA II (3.1.1), “partial”; SGA 6 VI (1.2), “partial”.
- [`CategoryTheory.GradedObject.shiftFunctor_map_apply`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GradedObject.shiftFunctor_map_apply#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/GradedObject.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/GradedObject.lean#L38) (StacksCore): “the shift on morphisms”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.16, Tag 09MF](https://stacks.math.columbia.edu/tag/09MF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
