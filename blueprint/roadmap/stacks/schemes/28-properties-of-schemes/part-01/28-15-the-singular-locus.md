---
declaration: section
origin: cited
lean: AlgebraicGeometry.regularLocus, AlgebraicGeometry.singularLocus
statement: formalized
proof: formalized
---

# 28.15 The singular locus

Section 28.15 of the Stacks Project, [Tag 07R0](https://stacks.math.columbia.edu/tag/07R0). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07R1, a definition

[Tag 07R1](https://stacks.math.columbia.edu/tag/07R1) in the Stacks Project.

**`AlgebraicGeometry.regularLocus`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Regular.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Regular.lean#L94). The attribute's comment: “regular locus”. References: EGA IV (6.12.1), “Reg(X)”; EGA IV (7.3.12), “special case”.

> The regular locus of a scheme: the points at which its local ring is regular.

```lean
public abbrev regularLocus (X : Scheme.{u}) : Set X
```

**`AlgebraicGeometry.singularLocus`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Regular.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/Regular.lean#L100). The attribute's comment: “singular locus”. References: EGA IV (6.12.1), “Sing(X)”.

> The singular locus of a scheme, the complement of its regular locus.

```lean
public abbrev singularLocus (X : Scheme.{u}) : Set X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.15, Tag 07R0](https://stacks.math.columbia.edu/tag/07R0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
