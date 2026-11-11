---
declaration: section
origin: cited
lean: CompletionAdjunction.derivedCompleteModules_abelian_hasLimits_exact_hasColimits
statement: formalized
proof: formalized
---

# 15.94 The category of derived complete modules

Section 15.94 of the Stacks Project, [Tag 0GLN](https://stacks.math.columbia.edu/tag/0GLN). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GLP, a lemma

[Tag 0GLP](https://stacks.math.columbia.edu/tag/0GLP) in the Stacks Project.

**`CompletionAdjunction.derivedCompleteModules_abelian_hasLimits_exact_hasColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedComplete/CompletionAdjunction.lean, line 854](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/DerivedComplete/CompletionAdjunction.lean#L854).

> The full subcategory of modules derived complete with respect to an ideal is abelian and has
> all limits, and its inclusion into modules is exact and preserves limits. If the ideal is
> finitely generated, the subcategory has all colimits and the inclusion has a left adjoint.

```lean
public theorem derivedCompleteModules_abelian_hasLimits_exact_hasColimits
    (A : Type u) [CommRing A] (I : Ideal A) :
    letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{u} A)) :=
      Stacks.DerivedProducts.hasProductsOfShape_derivedCategory
    let P : ObjectProperty (ModuleCat.{u} A) :=
      fun M => IsDerivedCompleteModule I M
    let C := P.FullSubcategory
    let F : C ⥤ ModuleCat.{u} A := P.ι
    Nonempty (Abelian C) ∧
      HasLimitsOfSize.{u, u} C ∧
      PreservesLimitsOfSize.{u, u} F ∧
      exactFunctor C (ModuleCat.{u} A) F ∧
      (I.FG → HasColimitsOfSize.{u, u} C ∧ F.IsRightAdjoint)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.94, Tag 0GLN](https://stacks.math.columbia.edu/tag/0GLN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
