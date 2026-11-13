---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProjectiveLinePow.exists_fpqc_sheaf_not_isAlgebraicSpace
statement: formalized
proof: formalized
---

# 110.56 Sheaf with quasi-compact flat covering which is not algebraic

Section 110.56 of the Stacks Project, [Tag 078E](https://stacks.math.columbia.edu/tag/078E). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 078F, a lemma

[Tag 078F](https://stacks.math.columbia.edu/tag/078F) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveLinePow.exists_fpqc_sheaf_not_isAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/ProductOfProjectiveLinesNotAlgebraic.lean, line 550](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/ProductOfProjectiveLinesNotAlgebraic.lean#L550).

> **Stacks 078F.** There is a functor `F : Sch^{opp} ⥤ Sets` which satisfies the sheaf
> condition for the fpqc topology, has representable diagonal `F ⟶ F × F`, and receives a
> surjective, flat, universally open, quasi-compact morphism `U ⟶ F` from a scheme `U`, but which
> is not an algebraic space: for every big fppf site `B`, its restriction to the big fppf site of
> `Spec ℤ` in `B` is not an algebraic space over `Spec ℤ`.
>
> The functor is `(ℙ¹)^∞`, sending a scheme `T` to the set of sequences of morphisms `T ⟶ ℙ¹`.
> Its sheaf property and representable diagonal are
> `AlgebraicGeometry.isSheaf_fpqc_projectiveLinePow` and
> `AlgebraicGeometry.relativelyRepresentable_diag_projectiveLinePow`. The morphism `U ⟶ F` is
> `projectiveLinePowFlatCover`, from the product of countably many copies of the disjoint union of
> the two standard charts of `ℙ¹`, an affine scheme. That `F` is not an algebraic space is
> `not_isAlgebraicSpace_siteRestrict_projectiveLinePow`. A morphism from a scheme to `F` is
> surjective, flat, universally open or quasi-compact when every base change of it along a morphism
> from a scheme is, in the sense of `CategoryTheory.MorphismProperty.presheaf`.

```lean
theorem exists_fpqc_sheaf_not_isAlgebraicSpace :
    ∃ F : Scheme.{u}ᵒᵖ ⥤ Type u,
      Presheaf.IsSheaf Scheme.fpqcTopology.{u} F ∧
      yoneda.relativelyRepresentable (diag F) ∧
      (∃ (U : Scheme.{u}) (p : yoneda.obj U ⟶ F),
        MorphismProperty.presheaf (C := Scheme.{u}) @Surjective p ∧
        MorphismProperty.presheaf (C := Scheme.{u}) @Flat p ∧
        MorphismProperty.presheaf (C := Scheme.{u}) @UniversallyOpen p ∧
        MorphismProperty.presheaf (C := Scheme.{u}) @QuasiCompact p) ∧
      ∀ B : BigFppfSite.{u}, ¬ IsAlgebraicSpace B (Spec (.of (ULift.{u} ℤ)))
        B.contains_spec_ulift_int (siteRestrict B B.contains_spec_ulift_int F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.56, Tag 078E](https://stacks.math.columbia.edu/tag/078E)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
