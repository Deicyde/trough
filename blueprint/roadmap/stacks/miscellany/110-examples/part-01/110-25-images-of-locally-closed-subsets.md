---
declaration: section
origin: cited
lean: Stacks.Examples.exists_affine_finitePresentation_image_not_finiteUnionLocallyClosed
statement: formalized
proof: formalized
---

# 110.25 Images of locally closed subsets

Section 110.25 of the Stacks Project, [Tag 0GZL](https://stacks.math.columbia.edu/tag/0GZL). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GZM, a lemma

[Tag 0GZM](https://stacks.math.columbia.edu/tag/0GZM) in the Stacks Project.

**`Stacks.Examples.exists_affine_finitePresentation_image_not_finiteUnionLocallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Scheme/ImageNotFiniteUnionLocallyClosed.lean, line 429](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Scheme/ImageNotFiniteUnionLocallyClosed.lean#L429).

> **Stacks 0GZM.** A finite-presentation morphism of affine schemes can take a locally closed
> subset to a set that is not a finite union of locally closed subsets.

```lean
theorem exists_affine_finitePresentation_image_not_finiteUnionLocallyClosed :
    ∃ (X Y : Scheme.{u}) (f : X ⟶ Y) (T : Set X),
      IsAffine X ∧ IsAffine Y ∧ FinitePresentation f ∧
        IsLocallyClosed T ∧ ¬ IsFiniteUnionLocallyClosed (f.base '' T)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.25, Tag 0GZL](https://stacks.math.columbia.edu/tag/0GZL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
