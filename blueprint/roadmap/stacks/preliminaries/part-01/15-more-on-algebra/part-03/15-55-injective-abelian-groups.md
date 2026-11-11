---
declaration: section
origin: cited
lean: AddCommGrpCat.injective_iff_divisible
statement: formalized
proof: formalized
---

# 15.55 Injective abelian groups

Section 15.55 of the Stacks Project, [Tag 01D6](https://stacks.math.columbia.edu/tag/01D6). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01D7, a lemma

[Tag 01D7](https://stacks.math.columbia.edu/tag/01D7) in the Stacks Project.

**`AddCommGrpCat.injective_iff_divisible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Injective/Criteria.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Injective/Criteria.lean#L114).

> **Stacks 01D7.** An abelian group is an injective object in the category of abelian groups
> if and only if it is divisible.
>
> Divisibility is Baer's criterion over `ℤ`: an injective group is Baer, and dividing `x` by `n`
> is extending to `ℤ` the map `nℤ → J` determined by `n ↦ x`. Conversely a divisible group is
> injective, which is Mathlib's `AddCommGrpCat.injective_of_divisible`.

```lean
theorem AddCommGrpCat.injective_iff_divisible (J : Type u) [AddCommGroup J] :
    Injective (C := AddCommGrpCat) (AddCommGrpCat.of J) ↔ Nonempty (DivisibleBy J ℕ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.55, Tag 01D6](https://stacks.math.columbia.edu/tag/01D6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
