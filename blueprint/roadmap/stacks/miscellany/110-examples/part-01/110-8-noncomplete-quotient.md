---
declaration: section
origin: cited
lean: Stacks.Examples.exists_complete_principal_ideal_not_complete_quotient
statement: formalized
proof: formalized
---

# 110.8 Noncomplete quotient

Section 110.8 of the Stacks Project, [Tag 05JD](https://stacks.math.columbia.edu/tag/05JD). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05JE, a lemma

[Tag 05JE](https://stacks.math.columbia.edu/tag/05JE) in the Stacks Project.

**`Stacks.Examples.exists_complete_principal_ideal_not_complete_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/NoncompleteQuotient.lean, line 421](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/NoncompleteQuotient.lean#L421).

> **Stacks 05JE.** A quotient by a principal ideal of a ring complete for another principal
> ideal need not be complete for the induced ideal.

```lean
theorem exists_complete_principal_ideal_not_complete_quotient :
    ∃ (R : Type u) (_ : CommRing R) (I J : Ideal R),
      I.IsPrincipal ∧ J.IsPrincipal ∧ IsAdicComplete I R ∧
        ¬ IsAdicComplete (I.map (Ideal.Quotient.mk J)) (R ⧸ J)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.8, Tag 05JD](https://stacks.math.columbia.edu/tag/05JD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
