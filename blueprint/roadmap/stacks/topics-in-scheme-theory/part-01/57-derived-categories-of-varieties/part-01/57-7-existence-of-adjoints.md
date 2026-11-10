---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.DerivedVarieties.Orlov.exists_exact_rightAdjoint_and_leftAdjoint
statement: formalized
proof: formalized
---

# 57.7 Existence of adjoints

Section 57.7 of the Stacks Project, [Tag 0FYM](https://stacks.math.columbia.edu/tag/0FYM). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FYN, a lemma

[Tag 0FYN](https://stacks.math.columbia.edu/tag/0FYN) in the Stacks Project.

**`Stacks.AlgebraicGeometry.DerivedVarieties.Orlov.exists_exact_rightAdjoint_and_leftAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/Adjoints.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/Adjoints.lean#L378).

> **[Stacks, Tag 0FYN].** Let `k` be a field and let `X`, `Y` be proper schemes over `k`. If `X`
> is regular, then any `k`-linear exact functor `F : D_perf(𝒪_X) ⥤ D_perf(𝒪_Y)` has an exact right
> adjoint and an exact left adjoint.
>
> Here `D_perf` is `PerfectDerivedCategory`, "exact" is a triangulated functor (a commutation with
> the shift making it `CategoryTheory.Functor.IsTriangulated`), and `k`-linearity is for the
> structure induced by the structure morphisms (`AlgebraicGeometry.modulesLinear`).

```lean
theorem exists_exact_rightAdjoint_and_leftAdjoint (hX : IsRegular X.left)
    (F : PerfectDerivedCategory X.left ⥤ PerfectDerivedCategory Y.left)
    [F.CommShift ℤ] [F.IsTriangulated] [F.Linear k] :
    (∃ G : PerfectDerivedCategory Y.left ⥤ PerfectDerivedCategory X.left,
      Nonempty (F ⊣ G) ∧ ∃ hG : G.CommShift ℤ, letI := hG; G.IsTriangulated) ∧
    (∃ G : PerfectDerivedCategory Y.left ⥤ PerfectDerivedCategory X.left,
      Nonempty (G ⊣ F) ∧ ∃ hG : G.CommShift ℤ, letI := hG; G.IsTriangulated)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 57.7, Tag 0FYM](https://stacks.math.columbia.edu/tag/0FYM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
