---
declaration: section
origin: cited
lean: exists_isJacobsonRing_isUniversallyCatenary_localization_ringKrullDim_one_and_two
statement: formalized
proof: formalized
---

# 110.21 Dimension in Noetherian Jacobson rings

Section 110.21 of the Stacks Project, [Tag 0EEH](https://stacks.math.columbia.edu/tag/0EEH). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EEI, a lemma

[Tag 0EEI](https://stacks.math.columbia.edu/tag/0EEI) in the Stacks Project.

**`exists_isJacobsonRing_isUniversallyCatenary_localization_ringKrullDim_one_and_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/MaximalIdealHeight.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/MaximalIdealHeight.lean#L297). References: EGA IV (10.7.3), “n = 2 case”.

> **Stacks 0EEI.** There is a Jacobson, universally catenary, Noetherian domain `B` with
> maximal ideals `𝔪₁` and `𝔪₂` such that `dim B_{𝔪₁} = 1` and `dim B_{𝔪₂} = 2`.

```lean
theorem exists_isJacobsonRing_isUniversallyCatenary_localization_ringKrullDim_one_and_two :
    ∃ (B : Type u) (_ : CommRing B) (_ : IsNoetherianRing B) (_ : IsDomain B),
      IsJacobsonRing B ∧ Ring.IsUniversallyCatenary B ∧
        ∃ m₁ m₂ : MaximalSpectrum B,
          ringKrullDim (Localization.AtPrime m₁.asIdeal) = 1 ∧
          ringKrullDim (Localization.AtPrime m₂.asIdeal) = 2
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.21, Tag 0EEH](https://stacks.math.columbia.edu/tag/0EEH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
