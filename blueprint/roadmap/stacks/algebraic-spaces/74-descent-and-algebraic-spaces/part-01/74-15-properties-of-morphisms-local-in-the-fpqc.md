---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isFlat_isLocalAtSource_fpqc
statement: formalized
proof: formalized
---

# 74.15 Properties of morphisms local in the fpqc topology on the source

Section 74.15 of the Stacks Project, [Tag 06ES](https://stacks.math.columbia.edu/tag/06ES). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06ET, a lemma

[Tag 06ET](https://stacks.math.columbia.edu/tag/06ET) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_isLocalAtSource_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatFpqcLocality.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatFpqcLocality.lean#L62).

> **Stacks 06ET.** Flatness of morphisms of algebraic spaces over `S` is local on the source
> for the fpqc topology.

```lean
instance isFlat_isLocalAtSource_fpqc
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    MorphismProperty.IsLocalAtSource
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) => IsFlat B S hS f.hom)
      (Topology.fpqc.precoverage.{u, v} B S hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.15, Tag 06ES](https://stacks.math.columbia.edu/tag/06ES)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
