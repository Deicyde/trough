---
declaration: section
origin: cited
lean: AlgebraicGeometry.not_isAlgebraicStack_cartesianProperFlatBasedCategory
statement: formalized
proof: formalized
---

# 110.73 The stack of proper algebraic spaces is not algebraic

Section 110.73 of the Stacks Project, [Tag 0D1Q](https://stacks.math.columbia.edu/tag/0D1Q). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D1R, a lemma

[Tag 0D1R](https://stacks.math.columbia.edu/tag/0D1R) in the Stacks Project.

**`AlgebraicGeometry.not_isAlgebraicStack_cartesianProperFlatBasedCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Stacks/ProperSpacesNotAlgebraic.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Stacks/ProperSpacesNotAlgebraic.lean#L137).

> **Stacks 0D1R.** The stack in groupoids
> `p'_{fp, flat, proper} : Spaces'_{fp, flat, proper} ⟶ Sch_fppf` whose category of sections over
> a scheme `S` is the category of flat, proper, finitely presented algebraic spaces over `S`, over
> the big fppf site of `Spec ℤ` (any big fppf site `B`, as in Stacks 021R), is not an algebraic
> stack.
>
> As in the source, the proof is: an algebraic stack has effective formal objects (07X8), but over
> `Spec ℚ` the versal formal deformation of a smooth quartic surface (here the Fermat quartic) is a
> non-effective formal object (`AlgebraicGeometry.properFlatSpacesNonEffectiveInput`), and
> algebraicity over `Spec ℤ` would give algebraicity over `Spec ℚ`. The source argues over `ℂ`; by
> its footnote any field of characteristic zero works, and `ℚ` (lifted to the universe `u`) is
> used here.

```lean
theorem not_isAlgebraicStack_cartesianProperFlatBasedCategory (B : BigFppfSite.{u})
    (hZ : B.Contains integerBase) :
    ¬ Stack.IsAlgebraicStack.{u, w} B integerBase hZ
      (cartesianProperFlatBasedCategory B integerBase hZ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.73, Tag 0D1Q](https://stacks.math.columbia.edu/tag/0D1Q)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
