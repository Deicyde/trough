---
declaration: section
origin: cited
lean: Stacks.Examples.InjectiveTilde.exists_injective_tilde_not_flasque, Stacks.Examples.InjectiveTilde.exists_injective_tilde_basicOpen_restriction_not_surjective, Stacks.Examples.InjectiveTilde.exists_injective_tilde_nonzero_firstCohomology
statement: formalized
proof: formalized
---

# 110.47 Non flasque quasi-coherent sheaf associated to injective module

Section 110.47 of the Stacks Project, [Tag 0273](https://stacks.math.columbia.edu/tag/0273). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0274, a lemma

[Tag 0274](https://stacks.math.columbia.edu/tag/0274) in the Stacks Project.

**`Stacks.Examples.InjectiveTilde.exists_injective_tilde_not_flasque`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/QuasiCoherentPushforward/NotFlasque.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/QuasiCoherentPushforward/NotFlasque.lean#L248). The attribute's comment: “nonflasque associated sheaf”. References: SGA 6 II (AppI.0.1), “not flasque”; SGA 6 II (AppI.1.2), “Ĩ not flasque”.

> **Stacks Project, Tag 0274.** An injective module can have a nonflasque associated sheaf
> on its affine spectrum.

```lean
theorem exists_injective_tilde_not_flasque :
    ∃ (A : CommRingCat) (J : ModuleCat A),
      Injective J ∧ ¬ TopCat.Presheaf.IsFlasque (tilde J).presheaf
```

**`Stacks.Examples.InjectiveTilde.exists_injective_tilde_basicOpen_restriction_not_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/QuasiCoherentPushforward/NotFlasque.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/QuasiCoherentPushforward/NotFlasque.lean#L260). The attribute's comment: “basic-open restriction not surjective”. References: SGA 6 II (AppI.0.1), “not flasque (std open)”; SGA 6 II (AppI.1.2), “Ĩ not flasque”.

> **Stacks Project, Tag 0274.** Even restriction to a standard open can fail to be
> surjective for the associated sheaf of an injective module.

```lean
theorem exists_injective_tilde_basicOpen_restriction_not_surjective :
    ∃ (A : CommRingCat) (J : ModuleCat A) (f : A),
      Injective J ∧
        ¬ Function.Surjective
          ((tilde J).presheaf.map
            (homOfLE (le_top : PrimeSpectrum.basicOpen f ≤ ⊤)).op)
```

## Tag 0CRZ, a lemma

[Tag 0CRZ](https://stacks.math.columbia.edu/tag/0CRZ) in the Stacks Project.

**`Stacks.Examples.InjectiveTilde.exists_injective_tilde_nonzero_firstCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/QuasiCoherentPushforward/NonvanishingCohomology.lean, line 641](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/QuasiCoherentPushforward/NonvanishingCohomology.lean#L641). References: SGA 6 II (AppI.0.1), “noetherian space case”; SGA 6 II (AppI.1.2), “H¹(U,Ĩ)≠0”.

> **Stacks Project, Tag 0CRZ.** An injective module on an affine scheme with Noetherian
> underlying space can have nonzero first cohomology on a quasi-compact open.

```lean
theorem exists_injective_tilde_nonzero_firstCohomology :
    ∃ (A : CommRingCat.{u}) (I : ModuleCat.{u} A) (U : (Spec A).Opens),
      NoetherianSpace (Spec A) ∧ Injective I ∧
        IsCompact (U : Set (Spec A)) ∧
          ¬ IsZero (Hgroup (Spec A).ringCatSheaf U 1 (tilde I))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.47, Tag 0273](https://stacks.math.columbia.edu/tag/0273)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
