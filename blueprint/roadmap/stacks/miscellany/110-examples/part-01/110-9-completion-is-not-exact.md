---
declaration: section
origin: cited
lean: Stacks.Examples.exists_not_left_exact_adicCompletion, Stacks.Examples.exists_not_right_exact_adicCompletion_finitePresentation
statement: formalized
proof: formalized
---

# 110.9 Completion is not exact

Section 110.9 of the Stacks Project, [Tag 05JF](https://stacks.math.columbia.edu/tag/05JF). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05JG, a lemma

[Tag 05JG](https://stacks.math.columbia.edu/tag/05JG) in the Stacks Project.

**`Stacks.Examples.exists_not_left_exact_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/CompletionNotExact.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/CompletionNotExact.lean#L99). The attribute's comment: “failure of left exactness”.

> **Stacks 05JG.** Adic completion need not preserve the exactness of a short exact sequence
> at its middle term, so it is not left exact in general.

```lean
theorem exists_not_left_exact_adicCompletion :
    ∃ (R : Type u) (_ : CommRing R) (I J : Ideal R),
      I.IsPrincipal ∧ J.IsPrincipal ∧
        Function.Exact (Submodule.subtype (J : Submodule R R))
          (Submodule.mkQ (J : Submodule R R)) ∧
        ¬ Function.Exact
          (AdicCompletion.map I (Submodule.subtype (J : Submodule R R)))
          (AdicCompletion.map I (Submodule.mkQ (J : Submodule R R)))
```

**`Stacks.Examples.exists_not_right_exact_adicCompletion_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/CompletionNotExact.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/CompletionNotExact.lean#L152). The attribute's comment: “failure of right exactness on finitely presented modules”.

> **Stacks 05JG.** Completion is not right exact even on finitely presented modules over a
> ring, with a principal ideal of definition.

```lean
theorem exists_not_right_exact_adicCompletion_finitePresentation :
    ∃ (R : Type u) (_ : CommRing R) (I : Ideal R) (f : R),
      I.IsPrincipal ∧
        Module.FinitePresentation R (R ⧸ (Ideal.span {f} : Submodule R R)) ∧
        Function.Exact (LinearMap.mulLeft R f)
          (Submodule.mkQ (Ideal.span {f} : Submodule R R)) ∧
        ¬ Function.Exact
          (AdicCompletion.map I (LinearMap.mulLeft R f))
          (AdicCompletion.map I (Submodule.mkQ (Ideal.span {f} : Submodule R R)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.9, Tag 05JF](https://stacks.math.columbia.edu/tag/05JF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
