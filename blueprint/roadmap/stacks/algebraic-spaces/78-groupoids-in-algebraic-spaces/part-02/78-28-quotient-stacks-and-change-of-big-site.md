---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isEquivalenceOver_changeBigSiteQuotientEquivalence
statement: formalized
proof: formalized
---

# 78.28 Quotient stacks and change of big site

Section 78.28 of the Stacks Project, [Tag 04WW](https://stacks.math.columbia.edu/tag/04WW). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf).

## Tag 04WX, a lemma

[Tag 04WX](https://stacks.math.columbia.edu/tag/04WX) in the Stacks Project.

**`AlgebraicGeometry.Stack.isEquivalenceOver_changeBigSiteQuotientEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ChangeBigSiteQuotientUnconditional.lean, line 70](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ChangeBigSiteQuotientUnconditional.lean#L70).

> The canonical 1-morphism `[f⁻¹U/f⁻¹R] ⟶ f⁻¹[U/R]` is an equivalence in the 2-category of
> fibred categories over the enlarged localized big fppf site: it has a quasi-inverse strictly over
> the site, with vertical unit and counit.

```lean
theorem isEquivalenceOver_changeBigSiteQuotientEquivalence :
    Nonempty (Functor.IsEquivalenceOver
      (quotientStack (changeBigSiteGroupoid B B' h S hS G)).p
      (pullbackQuotientStack h S hS G).p
      (changeBigSiteQuotientEquivalence B B' h S hS G))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.28, Tag 04WW](https://stacks.math.columbia.edu/tag/04WW)
- [AxiomMath/Stacks at f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf)
