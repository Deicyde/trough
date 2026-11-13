---
declaration: section
origin: cited
lean: Stacks.AdicClosedSubmodule.tfae_isClosed_eq_iInf_sup_isAdicComplete_quotient, Stacks.Examples.hasKernels_iAdicallyCompleteModuleCat, Stacks.Examples.hasCokernels_iAdicallyCompleteModuleCat, Stacks.Examples.not_abelian_iAdicallyCompleteModuleCat_of_principal, Stacks.Examples.exists_not_abelian_iAdicallyCompleteModuleCat
statement: formalized
proof: formalized
---

# 110.10 The category of complete modules is not abelian

Section 110.10 of the Stacks Project, [Tag 07JQ](https://stacks.math.columbia.edu/tag/07JQ). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0HB3, a lemma

[Tag 0HB3](https://stacks.math.columbia.edu/tag/0HB3) in the Stacks Project.

**`Stacks.AdicClosedSubmodule.tfae_isClosed_eq_iInf_sup_isAdicComplete_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/ClosedSubmodule.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/ClosedSubmodule.lean#L148). The attribute's comment: “Complete statement: the three equivalent conditions, and completeness of `N` for finitely generated `I`. The intersection in (2) is over all `n`; the `n = 0` term is `M`.”.

> **Stacks 0HB3.** Let `I ⊆ R` be an ideal of a ring, `M` an `I`-adically complete
> `R`-module and `N ⊆ M` a submodule. The following are equivalent: (1) `N` is closed in `M` (for
> the `I`-adic topology), (2) `N = ⋂_{n ≥ 1} (N + IⁿM)`, (3) `M ⧸ N` is `I`-adically complete.
> If `I` is finitely generated, these conditions imply that `N` is `I`-adically complete.

```lean
theorem tfae_isClosed_eq_iInf_sup_isAdicComplete_quotient [IsAdicComplete I M]
    (N : Submodule R M) :
    List.TFAE [@IsClosed M (I.adicModuleTopology M) (N : Set M),
      N = ⨅ n : ℕ, (N ⊔ (I ^ n • ⊤ : Submodule R M)),
      IsAdicComplete I (M ⧸ N)] ∧
    (I.FG → @IsClosed M (I.adicModuleTopology M) (N : Set M) → IsAdicComplete I N)
```

## Tag 07JR, a lemma

[Tag 07JR](https://stacks.math.columbia.edu/tag/07JR) in the Stacks Project.

**`Stacks.Examples.hasKernels_iAdicallyCompleteModuleCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/CompleteModuleCategory.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/CompleteModuleCategory.lean#L155). The attribute's comment: “kernels”.

> **Stacks 07JR.** If `I` is a finitely generated ideal of `R`, then the category of
> `I`-adically complete `R`-modules has kernels.

```lean
theorem hasKernels_iAdicallyCompleteModuleCat
    (R : Type u) [CommRing R] (I : Ideal R) (hI : I.FG) :
    HasKernels (IAdicallyCompleteModuleCat.{v} R I)
```

**`Stacks.Examples.hasCokernels_iAdicallyCompleteModuleCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/CompleteModuleCategory.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/CompleteModuleCategory.lean#L242). The attribute's comment: “cokernels”.

> **Stacks 07JR.** If `I` is a finitely generated ideal of `R`, then the category of
> `I`-adically complete `R`-modules has cokernels.

```lean
theorem hasCokernels_iAdicallyCompleteModuleCat
    (R : Type u) [CommRing R] (I : Ideal R) (hI : I.FG) :
    HasCokernels (IAdicallyCompleteModuleCat.{v} R I)
```

**`Stacks.Examples.not_abelian_iAdicallyCompleteModuleCat_of_principal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/CompleteModulesNotAbelian.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/CompleteModulesNotAbelian.lean#L117). The attribute's comment: “not\_abelian, for a named ring and a named principal ideal”.

> If `R` is a Noetherian ring without zero divisors which is complete for a principal ideal
> `I = (π)` whose generator is neither zero nor a unit, and `E : Type v` is an `R`-module with a
> linear equivalence `E ≃ₗ[R] R`, then the category of `I`-adically complete `R`-modules in
> `Type v` is not abelian.

```lean
theorem not_abelian_iAdicallyCompleteModuleCat_of_principal
    (R : Type u) [CommRing R] [IsNoetherianRing R] [NoZeroDivisors R]
    (I : Ideal R) (hR : IsAdicComplete I R) (π : R) (hIspan : I = Ideal.span {π})
    (hπ : π ≠ 0) (hπnonunit : ¬ IsUnit π)
    (E : Type v) [AddCommGroup E] [Module R E] (eER : E ≃ₗ[R] R) :
    ¬ Nonempty (Abelian (IAdicallyCompleteModuleCat.{v} R I))
```

**`Stacks.Examples.exists_not_abelian_iAdicallyCompleteModuleCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Completion/CompleteModulesNotAbelian.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Completion/CompleteModulesNotAbelian.lean#L319). The attribute's comment: “not\_abelian”.

> There is a commutative ring with a finitely generated ideal for which the category of
> adically complete modules is not abelian.

```lean
theorem exists_not_abelian_iAdicallyCompleteModuleCat :
    ∃ (R : Type u) (_ : CommRing R) (I : Ideal R),
      I.FG ∧ ¬ Nonempty (Abelian (IAdicallyCompleteModuleCat.{v} R I))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.10, Tag 07JQ](https://stacks.math.columbia.edu/tag/07JQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
