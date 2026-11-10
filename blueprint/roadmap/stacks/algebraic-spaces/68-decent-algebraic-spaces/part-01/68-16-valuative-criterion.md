---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.universallyClosed_iff_valuativeCriterion_existence
statement: formalized
proof: formalized
---

# 68.16 Valuative criterion

Section 68.16 of the Stacks Project, [Tag 06NP](https://stacks.math.columbia.edu/tag/06NP). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03KJ, a proposition

[Tag 03KJ](https://stacks.math.columbia.edu/tag/03KJ) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyClosed_iff_valuativeCriterion_existence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/UniversallyClosedValuative.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/UniversallyClosedValuative.lean#L374).

> **Stacks 03KJ.** A quasi-compact morphism of algebraic spaces over `S` whose source is a
> decent algebraic space is universally closed exactly when it satisfies the existence part of
> the valuative criterion.

```lean
theorem universallyClosed_iff_valuativeCriterion_existence
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsQuasiCompact B S hS f)
    (hdecent : IsDecentSpace B S hS X) :
    UniversallyClosed B S hS f ↔ ValuativeCriterion.Existence f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.16, Tag 06NP](https://stacks.math.columbia.edu/tag/06NP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
