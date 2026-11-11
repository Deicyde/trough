---
declaration: section
origin: cited
lean: Stacks.Examples.exists_universallySubmersive_not_isVCovering
statement: formalized
proof: formalized
---

# 110.81 Universally submersive but not V covering

Section 110.81 of the Stacks Project, [Tag 0EU8](https://stacks.math.columbia.edu/tag/0EU8). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EU9, a lemma

[Tag 0EU9](https://stacks.math.columbia.edu/tag/0EU9) in the Stacks Project.

**`Stacks.Examples.exists_universallySubmersive_not_isVCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/UniversallySubmersiveNotVCovering.lean, line 775](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/UniversallySubmersiveNotVCovering.lean#L775).

> An affine, universally submersive morphism whose singleton family is not a
> V covering.

```lean
public theorem exists_universallySubmersive_not_isVCovering :
    ∃ (X Y : Scheme.{u}) (_ : IsAffine X) (_ : IsAffine Y) (f : X ⟶ Y),
      (topologically @Topology.IsQuotientMap : MorphismProperty Scheme.{u}).universally f ∧
        ¬ AlgebraicGeometry.IsVCovering (fun _ : Unit => X) (fun _ => f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.81, Tag 0EU8](https://stacks.math.columbia.edu/tag/0EU8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
