---
declaration: section
origin: cited
lean: Stacks.Discriminant.discriminantIdeal_properties, Stacks.Discriminant.etale_iff_discriminantIdeal_eq_top
statement: formalized
proof: formalized
---

# 49.3 Discriminant of a finite locally free morphism

Section 49.3 of the Stacks Project, [Tag 0BVH](https://stacks.math.columbia.edu/tag/0BVH). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BJF, a lemma

[Tag 0BJF](https://stacks.math.columbia.edu/tag/0BJF) in the Stacks Project.

**`Stacks.Discriminant.discriminantIdeal_properties`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/DiscriminantSheaf.lean, line 516](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/DiscriminantSheaf.lean#L516). The attribute's comment: “discriminant properties”.

> **Stacks Project, Tag 0BJF.** The discriminant of a finite locally free morphism is locally
> principal, its support consists of the images of the ramified points, and it is the unit ideal
> sheaf exactly when the morphism is étale.

```lean
theorem discriminantIdeal_properties :
    Stacks.Divisors.IsLocallyPrincipal (discriminantIdeal f) ∧
      (∀ y : Y, y ∈ (discriminantIdeal f).support ↔
        ∃ x : X, f x = y ∧ ¬ UnramifiedAt f x) ∧
      (Etale f ↔ discriminantIdeal f = ⊤)
```

**`Stacks.Discriminant.etale_iff_discriminantIdeal_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Discriminant/DiscriminantSheaf.lean, line 534](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Discriminant/DiscriminantSheaf.lean#L534).

> **Stacks Project, Tag 0BJF.** A finite locally free morphism is étale if and only if its
> discriminant is empty.

```lean
theorem etale_iff_discriminantIdeal_eq_top : Etale f ↔ discriminantIdeal f = ⊤
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 49.3, Tag 0BVH](https://stacks.math.columbia.edu/tag/0BVH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
