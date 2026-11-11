---
declaration: section
origin: cited
lean: Stacks.Examples.exists_locally_principal_ideal_not_invertible
statement: formalized
proof: formalized
---

# 110.32 A noninvertible ideal invertible in stalks

Section 110.32 of the Stacks Project, [Tag 0CBZ](https://stacks.math.columbia.edu/tag/0CBZ). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CC0, a lemma

[Tag 0CC0](https://stacks.math.columbia.edu/tag/0CC0) in the Stacks Project.

**`Stacks.Examples.exists_locally_principal_ideal_not_invertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Scheme/LocallyPrincipalNotInvertible.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Scheme/LocallyPrincipalNotInvertible.lean#L215).

> **Stacks 0CC0.** A nonzero ideal in a domain can be principal at every prime localization
> without being invertible as a module.

```lean
theorem exists_locally_principal_ideal_not_invertible :
    ∃ (A : Type*) (_ : CommRing A) (_ : IsDomain A) (I : Ideal A),
      I ≠ ⊥ ∧
      (∀ (q : Ideal A) [q.IsPrime],
        Submodule.IsPrincipal
          (I.map (algebraMap A (Localization.AtPrime q)))) ∧
      ¬ Module.Invertible A I
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.32, Tag 0CBZ](https://stacks.math.columbia.edu/tag/0CBZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
