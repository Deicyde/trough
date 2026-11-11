---
declaration: section
origin: cited
lean: NatTrans.hcomp, CategoryTheory.NatTrans.horiz_vert_interchange
statement: formalized
proof: formalized
---

# 4.28 Formal properties

Section 4.28 of the Stacks Project, [Tag 003D](https://stacks.math.columbia.edu/tag/003D). 2 tags here are carried by 1 declaration of the repository (in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 003E, a definition

[Tag 003E](https://stacks.math.columbia.edu/tag/003E) in the Stacks Project.

Declarations registered for the tag:

- [`NatTrans.hcomp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=NatTrans.hcomp#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Basic.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Basic.lean#L89) (StacksCore).

## Tag 003F, a lemma

[Tag 003F](https://stacks.math.columbia.edu/tag/003F) in the Stacks Project.

**`CategoryTheory.NatTrans.horiz_vert_interchange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Bicategory/InterchangeLaw.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Bicategory/InterchangeLaw.lean#L56).

> **Stacks 003F** (interchange law). The horizontal (`◫`) and vertical (`≫`)
> compositions of natural transformations satisfy
> `(t ≫ t') ◫ (s ≫ s') = (t ◫ s) ≫ (t' ◫ s')`.

```lean
theorem horiz_vert_interchange
    {A : Type u₁} {B : Type u₂} {C : Type u₃}
    [Category.{v₁} A] [Category.{v₂} B] [Category.{v₃} C]
    {F F' F'' : A ⥤ B} {G G' G'' : B ⥤ C}
    (t : F ⟶ F') (t' : F' ⟶ F'')
    (s : G ⟶ G') (s' : G' ⟶ G'') :
    (t ≫ t') ◫ (s ≫ s') = (t ◫ s) ≫ (t' ◫ s')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.28, Tag 003D](https://stacks.math.columbia.edu/tag/003D)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
