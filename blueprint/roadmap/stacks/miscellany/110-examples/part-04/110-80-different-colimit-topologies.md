---
declaration: section
origin: cited
lean: Stacks.Examples.exists_sequential_colimit_not_preserved
statement: formalized
proof: formalized
---

# 110.80 Different colimit topologies

Section 110.80 of the Stacks Project, [Tag 0B2Y](https://stacks.math.columbia.edu/tag/0B2Y). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B2Z, a lemma

[Tag 0B2Z](https://stacks.math.columbia.edu/tag/0B2Z) in the Stacks Project.

**`Stacks.Examples.exists_sequential_colimit_not_preserved`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/ColimitTopologies.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/ColimitTopologies.lean#L450).

> A sequential diagram of abelian topological groups for which the colimit topology as spaces
> differs from the colimit topology as groups.

```lean
public theorem exists_sequential_colimit_not_preserved :
    ∃ F : ℕ ⥤ TopGrp.{u},
      (∀ n : ℕ, ∀ x y : F.obj n, x * y = y * x) ∧
        ¬ PreservesColimit F TopGrp.forgetToTopCat
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.80, Tag 0B2Y](https://stacks.math.columbia.edu/tag/0B2Y)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
