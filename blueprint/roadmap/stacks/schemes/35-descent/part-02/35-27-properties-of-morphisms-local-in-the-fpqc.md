---
declaration: section
origin: cited
lean: AlgebraicGeometry.flat_isLocalAtSource_fpqc, AlgebraicGeometry.stalkwiseInjective_isLocalAtSource_fpqc
statement: formalized
proof: formalized
---

# 35.27 Properties of morphisms local in the fpqc topology on the source

Section 35.27 of the Stacks Project, [Tag 036J](https://stacks.math.columbia.edu/tag/036J). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 036K, a lemma

[Tag 036K](https://stacks.math.columbia.edu/tag/036K) in the Stacks Project.

**`AlgebraicGeometry.flat_isLocalAtSource_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Fpqc.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Fpqc.lean#L74).

> Flatness of scheme morphisms is fpqc-local on the source.

```lean
public instance flat_isLocalAtSource_fpqc :
    MorphismProperty.IsLocalAtSource (@Flat : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 036L, a lemma

[Tag 036L](https://stacks.math.columbia.edu/tag/036L) in the Stacks Project.

**`AlgebraicGeometry.stalkwiseInjective_isLocalAtSource_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Fpqc.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Fpqc.lean#L102).

> Injectivity of all the local-ring maps of a scheme morphism is fpqc-local on its source.

```lean
public instance stalkwiseInjective_isLocalAtSource_fpqc :
    MorphismProperty.IsLocalAtSource
      (stalkwise (fun f => Function.Injective f) : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.27, Tag 036J](https://stacks.math.columbia.edu/tag/036J)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
