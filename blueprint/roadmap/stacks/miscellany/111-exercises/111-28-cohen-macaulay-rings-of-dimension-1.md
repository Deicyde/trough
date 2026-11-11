---
declaration: section
origin: cited
lean: IsLocalRing.IsCohenMacaulayOfDimension
statement: formalized
proof: formalized
---

# 111.28 Cohen-Macaulay rings of dimension 1

Section 111.28 of the Stacks Project, [Tag 0284](https://stacks.math.columbia.edu/tag/0284). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0285, a definition

[Tag 0285](https://stacks.math.columbia.edu/tag/0285) in the Stacks Project.

**`IsLocalRing.IsCohenMacaulayOfDimension`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Exercises/CohenMacaulay.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Exercises/CohenMacaulay.lean#L39).

> A local ring `A` is *Cohen--Macaulay of dimension `d`* if its Krull dimension is `d` and
> there is a system of parameters `x₁, ..., x_d` such that every `xᵢ` is a nonzerodivisor on the
> quotient by its predecessors.

```lean
abbrev IsCohenMacaulayOfDimension (A : Type*) [CommRing A] [IsLocalRing A] (d : ℕ) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 111.28, Tag 0284](https://stacks.math.columbia.edu/tag/0284)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
