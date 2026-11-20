---
declaration: section
origin: cited
lean: Stacks.Examples.exists_inverse_system_isCompact_not_isCompact_limit
statement: formalized
proof: formalized
---

# 110.4 Non-quasi-compact inverse limit of quasi-compact spaces

Section 110.4 of the Stacks Project, [Tag 09ZJ](https://stacks.math.columbia.edu/tag/09ZJ). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf).

## Tag 09ZK, a lemma

[Tag 09ZK](https://stacks.math.columbia.edu/tag/09ZK) in the Stacks Project.

**`Stacks.Examples.exists_inverse_system_isCompact_not_isCompact_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/NonQuasiCompactInverseLimit.lean, line 94](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/Examples/Completion/NonQuasiCompactInverseLimit.lean#L94).

> **Stacks 09ZK.** There is an inverse system of quasi-compact topological spaces over the
> natural numbers whose limit is not quasi-compact.

```lean
theorem exists_inverse_system_isCompact_not_isCompact_limit :
    ∃ F : ℕᵒᵖ ⥤ TopCat.{0},
      (∀ n, IsCompact (Set.univ : Set (F.obj n))) ∧
        ¬ IsCompact (Set.univ : Set ↑(limit F : TopCat.{0}))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.4, Tag 09ZJ](https://stacks.math.columbia.edu/tag/09ZJ)
- [AxiomMath/Stacks at f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf)
