---
declaration: section
origin: cited
lean: Stacks.Examples.EtaleSpecialization.exists_isEtale_specializes_pointsMap_eq
statement: formalized
proof: formalized
---

# 110.51 Specializations between points in fibre étale morphism

Section 110.51 of the Stacks Project, [Tag 06UJ](https://stacks.math.columbia.edu/tag/06UJ). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06UK, a lemma

[Tag 06UK](https://stacks.math.columbia.edu/tag/06UK) in the Stacks Project.

**`Stacks.Examples.EtaleSpecialization.exists_isEtale_specializes_pointsMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/EtaleSpecializationInFibre.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/EtaleSpecializationInFibre.lean#L149). The attribute's comment: “a specialization inside a fibre of an étale morphism of algebraic spaces”.

> **Stacks 06UK.** There is an étale morphism of algebraic spaces `f : X ⟶ Y` and a
> nontrivial specialization of points `x ⤳ x'` in `|X|` with `f x = f x'` in `|Y|`.
>
> The witness is the chart `X = Spec K[y, x_n : n ∈ ℤ]` of its own quotient `Y = X/ℤ` by the
> integer shift, at the tail points `x = p_1` and `x' = p_0`: the shift carries `p_0` to `p_1`,
> so the two have the same image in `Y`, while `p_1 ⊂ p_0` gives the specialization.
>
> That `Y` is an algebraic space is the algebraicity half of Stacks 02WW,
> `AlgebraicGeometry.Space.isAlgebraicSpace_quotient_unconditional`, which is a theorem.

```lean
theorem exists_isEtale_specializes_pointsMap_eq :
    ∃ (X Y : (BigFppfOver B (Spec (.of K)) hS)ᵒᵖ ⥤ Type u)
      (_ : IsAlgebraicSpace B (Spec (.of K)) hS X)
      (_ : IsAlgebraicSpace B (Spec (.of K)) hS Y)
      (f : X ⟶ Y) (x x' : Space.points B (Spec (.of K)) hS X),
      Space.IsEtale B (Spec (.of K)) hS f ∧ x ≠ x' ∧ x ⤳ x' ∧
        Space.pointsMap B (Spec (.of K)) hS X f x =
          Space.pointsMap B (Spec (.of K)) hS X f x'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.51, Tag 06UJ](https://stacks.math.columbia.edu/tag/06UJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
