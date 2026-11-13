---
declaration: section
origin: cited
lean: Stacks.Descent.isImmersion_isLocalAtTarget_fppf, AlgebraicGeometry.isDominant_isLocalAtTarget_fppf
statement: formalized
proof: formalized
---

# 35.24 Properties of morphisms local in the fppf topology on the target

Section 35.24 of the Stacks Project, [Tag 02YL](https://stacks.math.columbia.edu/tag/02YL). 2 tags here are carried by 1 declaration of the repository (in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02YM, a lemma

[Tag 02YM](https://stacks.math.columbia.edu/tag/02YM) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.Descent.isImmersion_isLocalAtTarget_fppf`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/MorphismPropertyTopology/FppfLocalAtTarget.lean#L339), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/MorphismPropertyTopology/FppfLocalAtTarget.lean, line 345](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/MorphismPropertyTopology/FppfLocalAtTarget.lean#L345) (StacksFrontier).

## Tag 0H8J, a lemma

[Tag 0H8J](https://stacks.math.columbia.edu/tag/0H8J) in the Stacks Project.

**`AlgebraicGeometry.isDominant_isLocalAtTarget_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/Dominant.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/Dominant.lean#L113). References: EGA I (2.2.8), “more general”.

> **Stacks Project, Tag 0H8J.** Being dominant is fppf local on the base.

```lean
instance isDominant_isLocalAtTarget_fppf :
    MorphismProperty.IsLocalAtTarget (@IsDominant : MorphismProperty Scheme.{u})
      Scheme.fppfPrecoverage
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.24, Tag 02YL](https://stacks.math.columbia.edu/tag/02YL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
