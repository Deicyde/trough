---
declaration: section
origin: cited
lean: Stacks.Examples.exists_identifiesLocalRings_not_indEtale
statement: formalized
proof: formalized
---

# 110.46 A ring map which identifies local rings which is not ind-étale

Section 110.46 of the Stacks Project, [Tag 09AN](https://stacks.math.columbia.edu/tag/09AN). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09AP, a lemma

[Tag 09AP](https://stacks.math.columbia.edu/tag/09AP) in the Stacks Project.

**`Stacks.Examples.exists_identifiesLocalRings_not_indEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Schemes/LocalRingPreservingNotIndEtale.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Schemes/LocalRingPreservingNotIndEtale.lean#L436).

> **Stacks 09AP.** A ring map can identify local rings without being ind-étale or
> ind-Zariski.

```lean
theorem exists_identifiesLocalRings_not_indEtale :
    ∃ (A : Type u) (_ : CommRing A) (B : Type v) (_ : CommRing B) (_ : Algebra A B),
      Algebra.IdentifiesLocalRings A B ∧
        ¬ StacksDraft.IndEtale A B ∧
        ¬ AlgebraicGeometry.ProEtale.IsIndZariski.{u, v, w} A B
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.46, Tag 09AN](https://stacks.math.columbia.edu/tag/09AN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
