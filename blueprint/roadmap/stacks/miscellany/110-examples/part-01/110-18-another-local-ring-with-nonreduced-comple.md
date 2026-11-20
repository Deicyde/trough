---
declaration: section
origin: cited
lean: exists_nonreduced_adicCompletion_localization_away
statement: formalized
proof: formalized
---

# 110.18 Another local ring with nonreduced completion

Section 110.18 of the Stacks Project, [Tag 0GHH](https://stacks.math.columbia.edu/tag/0GHH). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf).

## Tag 0GHI, a lemma

[Tag 0GHI](https://stacks.math.columbia.edu/tag/0GHI) in the Stacks Project.

**`exists_nonreduced_adicCompletion_localization_away`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/NonreducedLocalizedCompletion.lean, line 345](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/RingTheory/AdicCompletion/NonreducedLocalizedCompletion.lean#L345).

> **Stacks 0GHI.** There is a local Noetherian two-dimensional domain `B`, complete with
> respect to a principal ideal `I = (b)`, and an element `f` of its maximal ideal outside `I`, such
> that the `I`-adic completion `C = (B_f)^` of the principal localization `B_f` is nonreduced, and
> even such that `C[1/b]` is nonreduced.

```lean
theorem exists_nonreduced_adicCompletion_localization_away :
    ∃ (B : Type u) (_ : CommRing B) (_ : IsDomain B) (_ : IsLocalRing B)
      (_ : IsNoetherianRing B) (b f : B),
      ringKrullDim B = 2 ∧
        IsAdicComplete (Ideal.span {b}) B ∧
        f ∈ IsLocalRing.maximalIdeal B ∧
        f ∉ Ideal.span {b} ∧
        (let C := AdicCompletion
            ((Ideal.span {b}).map (algebraMap B (Localization.Away f)))
            (Localization.Away f);
          (¬ IsReduced C) ∧
            (¬ IsReduced (Localization.Away (algebraMap B C b))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.18, Tag 0GHH](https://stacks.math.columbia.edu/tag/0GHH)
- [AxiomMath/Stacks at f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf)
