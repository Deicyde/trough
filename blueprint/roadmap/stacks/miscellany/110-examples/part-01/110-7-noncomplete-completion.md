---
declaration: section
origin: cited
lean: Stacks.Examples.CountableVarLocalization.exists_isLocalRing_adicCompletion_not_complete
statement: formalized
proof: formalized
---

# 110.7 Noncomplete completion

Section 110.7 of the Stacks Project, [Tag 05JA](https://stacks.math.columbia.edu/tag/05JA). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05JC, a lemma

[Tag 05JC](https://stacks.math.columbia.edu/tag/05JC) in the Stacks Project.

**`Stacks.Examples.CountableVarLocalization.exists_isLocalRing_adicCompletion_not_complete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/CompletionPathologies.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/CompletionPathologies.lean#L43).

> **Stacks 05JC.** There exists a local ring `R` and a maximal ideal `m` of it such that the
> `m`-adic completion `R ^∧` of `R` is local with maximal ideal different from `m R ^∧`, is not
> complete for its own maximal ideal, and is not `m`-adically complete as an `R`-module.

```lean
theorem exists_isLocalRing_adicCompletion_not_complete :
    ∃ (R : Type) (_ : CommRing R) (_ : IsLocalRing R) (m : Ideal R), m.IsMaximal ∧
      ∃ _ : IsLocalRing (AdicCompletion m R),
        IsLocalRing.maximalIdeal (AdicCompletion m R) ≠ m.map (AdicCompletion.of m R) ∧
        ¬ IsAdicComplete (IsLocalRing.maximalIdeal (AdicCompletion m R))
            (AdicCompletion m R) ∧
        ¬ IsAdicComplete m (AdicCompletion m R)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.7, Tag 05JA](https://stacks.math.columbia.edu/tag/05JA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
