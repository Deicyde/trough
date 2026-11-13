---
declaration: section
origin: cited
lean: CategoryTheory.Adjunction.rightAdjointCommShift, CategoryTheory.Adjunction.right_adjoint_additive, CategoryTheory.Adjunction.isTriangulated_rightAdjoint, isEquivalence_of_fullyFaithful_of_adjunction_of_ker_eq_zero
statement: formalized
proof: formalized
---

# 13.7 Adjoints for exact functors

Section 13.7 of the Stacks Project, [Tag 0A8C](https://stacks.math.columbia.edu/tag/0A8C). 2 tags here are carried by 1 declaration of the repository (in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A8D, a lemma

[Tag 0A8D](https://stacks.math.columbia.edu/tag/0A8D) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Adjunction.rightAdjointCommShift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Adjunction.rightAdjointCommShift#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Triangulated/AdjointsForExactFunctors.lean, line 36](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/AdjointsForExactFunctors.lean#L36) (StacksFrontier): “the commutation of the right adjoint with the shift”.
- [`CategoryTheory.Adjunction.right_adjoint_additive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Adjunction.right_adjoint_additive#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Triangulated/AdjointsForExactFunctors.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/AdjointsForExactFunctors.lean#L38) (StacksFrontier): “additivity of the right adjoint”. References: SGA 4 XVII (2.2.13.1), “special case”.
- [`CategoryTheory.Adjunction.isTriangulated_rightAdjoint`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Adjunction.isTriangulated_rightAdjoint#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Triangulated/AdjointsForExactFunctors.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/AdjointsForExactFunctors.lean#L41) (StacksFrontier): “the right adjoint preserves distinguished triangles”. References: SGA 4½ Etat 0 (2.6.7), “more general”.

## Tag 09J1, a lemma

[Tag 09J1](https://stacks.math.columbia.edu/tag/09J1) in the Stacks Project.

**`isEquivalence_of_fullyFaithful_of_adjunction_of_ker_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/AdjointsForExactFunctors.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/AdjointsForExactFunctors.lean#L123).

> Let `F : D ⥤ D'` and `G : D' ⥤ D` be exact functors of pretriangulated categories with
> `F ⊣ G`. If `F` is fully faithful and every `X : D'` with `G X` a zero object is itself a zero
> object, then `F` is an equivalence of categories.

```lean
theorem isEquivalence_of_fullyFaithful_of_adjunction_of_ker_eq_zero
    [F.IsTriangulated] [G.IsTriangulated] [F.Full] [F.Faithful]
    (adj : F ⊣ G)
    (hker : ∀ X : D', IsZero (G.obj X) → IsZero X) :
    F.IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.7, Tag 0A8C](https://stacks.math.columbia.edu/tag/0A8C)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
