---
declaration: section
origin: cited
lean: Stacks.Cohomology.SchemeColimits.higherDirectImage_preservesFilteredColimits
statement: formalized
proof: formalized
---

# 30.6 Colimits and higher direct images

Section 30.6 of the Stacks Project, [Tag 07TA](https://stacks.math.columbia.edu/tag/07TA). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07TB, a lemma

[Tag 07TB](https://stacks.math.columbia.edu/tag/07TB) in the Stacks Project.

**`Stacks.Cohomology.SchemeColimits.higherDirectImage_preservesFilteredColimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/ColimitsHigherDirect/HigherDirectImage.lean, line 399](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/ColimitsHigherDirect/HigherDirectImage.lean#L399).

> For a quasi-compact and quasi-separated morphism of schemes, its `p`-th higher direct
> image functor on sheaves of abelian groups preserves all filtered colimits.

```lean
instance higherDirectImage_preservesFilteredColimits
    {X S : AlgebraicGeometry.Scheme.{u}} (f : X ⟶ S)
    [AlgebraicGeometry.QuasiCompact f] [AlgebraicGeometry.QuasiSeparated f] (p : ℕ) :
    PreservesFilteredColimits
      ((TopCat.Sheaf.pushforward AddCommGrpCat.{u} f.base).rightDerived p)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.6, Tag 07TA](https://stacks.math.columbia.edu/tag/07TA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
