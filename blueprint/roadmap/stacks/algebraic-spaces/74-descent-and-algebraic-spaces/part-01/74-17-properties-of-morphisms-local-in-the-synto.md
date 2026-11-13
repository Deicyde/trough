---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.syntomic_isLocalAtSource_syntomic
statement: formalized
proof: formalized
---

# 74.17 Properties of morphisms local in the syntomic topology on the source

Section 74.17 of the Stacks Project, [Tag 06EZ](https://stacks.math.columbia.edu/tag/06EZ). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06F0, a lemma

[Tag 06F0](https://stacks.math.columbia.edu/tag/06F0) in the Stacks Project.

**`AlgebraicGeometry.Space.syntomic_isLocalAtSource_syntomic`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SyntomicSourceLocalityTransfer.lean, line 353](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SyntomicSourceLocalityTransfer.lean#L353).

> **Stacks 06F0.** Syntomicity of a morphism of algebraic spaces over `S` is local on the
> source for the syntomic topology of Stacks 03YH.
>
> Syntomicity of morphisms of schemes is étale local on the source and target
> ([Stacks Project, Tag 04R3]) and local on the source for the syntomic topology of schemes
> ([Stacks Project, Tag 036S]), so this is the instance of
> `AlgebraicGeometry.Space.isLocalAtSource_syntomic_of_schemes` at that property.

```lean
instance syntomic_isLocalAtSource_syntomic :
    MorphismProperty.IsLocalAtSource
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) => IsSyntomic B S hS f.hom)
      (Topology.precoverage.{u, v} .syntomic B S hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.17, Tag 06EZ](https://stacks.math.columbia.edu/tag/06EZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
