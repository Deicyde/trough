---
declaration: section
origin: cited
lean: SheafOfModules.GradedModule.isGrothendieckAbelian
statement: formalized
proof: formalized
---

# 24.11 Shift functors on sheaves of graded modules

Section 24.11 of the Stacks Project, [Tag 0FRC](https://stacks.math.columbia.edu/tag/0FRC). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf).

## Tag 0FRD, a lemma

[Tag 0FRD](https://stacks.math.columbia.edu/tag/0FRD) in the Stacks Project.

**`SheafOfModules.GradedModule.isGrothendieckAbelian`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafModulesGrothendieck.lean, line 240](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafModulesGrothendieck.lean#L240).

> **The category of right graded modules over a sheaf of graded algebras on a site is a
> Grothendieck abelian category.**
>
> It is abelian and has filtered colimits by Tag 0FR0, those colimits are exact by
> `gradedModule_ab5`, it is locally small, and it has the separator
> `⨁_{k, U} j_{U!} A_U[k]`.

```lean
noncomputable instance isGrothendieckAbelian (A : GradedAlgebra.{t, a} R) :
    IsGrothendieckAbelian.{max u v a w} (GradedModule.{t, a, max u v a w} A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.11, Tag 0FRC](https://stacks.math.columbia.edu/tag/0FRC)
- [AxiomMath/Stacks at f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf)
