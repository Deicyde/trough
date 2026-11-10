---
declaration: section
origin: cited
lean: Stacks.Examples.exists_isCompactObject_not_representable_by_finite_gradedProjective
statement: formalized
proof: formalized
---

# 110.71 An interesting compact object

Section 110.71 of the Stacks Project, [Tag 09R4](https://stacks.math.columbia.edu/tag/09R4). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09R5, a lemma

[Tag 09R5](https://stacks.math.columbia.edu/tag/09R5) in the Stacks Project.

**`Stacks.Examples.exists_isCompactObject_not_representable_by_finite_gradedProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/CompactObjectNoFiniteProjectiveModel.lean, line 1081](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/CompactObjectNoFiniteProjectiveModel.lean#L1081).

> **[Stacks, Tag 09R5].** *"There exists a differential graded algebra `(A, d)` and a compact
> object `E` of `D(A, d)` such that `E` cannot be represented by a finite and graded projective
> differential graded `A`-module."*
>
> The algebra is `A = k[x, y]/(y²)` over `k = ZMod 2`, with `x` of degree `0`, `y` of degree `-1`
> and `d y = x² + x`, and `E` is the summand of the regular module cut out by the idempotent given
> by multiplication by `x` (Tag 09R4). The obstruction is
> `Stacks.Examples.not_representable_by_finite_gradedProjective_of_retract_charTwoRegularModule`;
> compactness of `E` enters only to discharge the first conjunct.

```lean
theorem exists_isCompactObject_not_representable_by_finite_gradedProjective :
    ∃ (A : DifferentialGradedAlgebra.{0, 0} (ZMod 2)) (E : derivedCategory' A),
      IsCompactObject.{0} E ∧
        ¬ ∃ P : DifferentialGradedModule.{0, 0, 0} A, IsFinite P ∧
            Stacks.DifferentialGraded.DGModule.IsProjectiveAsGradedModule.{0, 0, 0, 0}
              (Unbundled.module P) ∧
            Nonempty (E ≅ (toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj P)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.71, Tag 09R4](https://stacks.math.columbia.edu/tag/09R4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
