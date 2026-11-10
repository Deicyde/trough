---
declaration: section
origin: cited
lean: AlgebraicGeometry.GradedConeAlgebra.cone, AlgebraicGeometry.AbstractCone, AlgebraicGeometry.AbstractCone.Hom
statement: formalized
proof: formalized
---

# 27.7 Cones

Section 27.7 of the Stacks Project, [Tag 062P](https://stacks.math.columbia.edu/tag/062P). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 062Q, a definition

[Tag 062Q](https://stacks.math.columbia.edu/tag/062Q) in the Stacks Project.

**`AlgebraicGeometry.GradedConeAlgebra.cone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/ConeOfGradedAlgebra.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/ConeOfGradedAlgebra.lean#L153). References: EGA II (8.3.1), “affine cone C=Spec(S)”; EGA II (8.6.1), “partial”; SGA 7 XV (2.1.1), “more general”.

> The cone, or affine cone, associated to a quasi-coherent graded `𝒪_S`-algebra `𝒜` whose
> degree-zero part is `𝒪_S`: the relative spectrum `C(𝒜) = Spec_S(𝒜)`.

```lean
public noncomputable def cone : Scheme.{u}
```

## Tag 062R, a definition

[Tag 062R](https://stacks.math.columbia.edu/tag/062R) in the Stacks Project.

**`AlgebraicGeometry.AbstractCone`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/Cone.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/Cone.lean#L65). The attribute's comment: “cones”.

> A cone over `S`: an affine morphism whose direct-image algebra is nonnegatively graded and
> has degree-zero part `𝒪_S`.

```lean
public structure AbstractCone (S : Scheme.{u})
```

**`AlgebraicGeometry.AbstractCone.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Constructions/Cone.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Constructions/Cone.lean#L117). The attribute's comment: “morphisms of cones”.

> A morphism of cones.  The map on direct images is the pullback on functions induced by the
> displayed morphism of total spaces.

```lean
public structure Hom {S : Scheme.{u}} (X Y : AbstractCone S)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.7, Tag 062P](https://stacks.math.columbia.edu/tag/062P)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
