---
declaration: theorem
origin: cited
lean: Ideal.finitePresentation_iff_forall_quotient_smul
statement: formalized
proof: formalized
---

# Finite presentation from cofinal ideal quotients

For a finite module `M`
over a commutative ring `R` and an ideal `I` satisfying full submodule adic
cofinality and `I ≤ Ideal.jacobson ⊥`,
[`Ideal.finitePresentation_iff_forall_quotient_smul`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicFinitePresentation.lean)
detects finite presentation over `R` on all reductions `M / J j M` over
`R / J j`, for any family `J : ι → Ideal R` with
`∀ n : ℕ, ∃ j, J j ≤ I ^ n`. The positive-powers criterion
`Ideal.finitePresentation_iff_forall_quotient_pow_smul` is a specialization.
The ring, module and index universes are independent; no ideal finite
generation or ordering condition on the family is required.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Ideal.finitePresentation_iff_forall_quotient_smul` (theorem), declared in [CoherentModules/RingTheory/Ideal/AdicFinitePresentation.lean, line 163](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicFinitePresentation.lean#L163).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Ideal.finitePresentation_iff_forall_quotient_smul` in CoherentModules/RingTheory/Ideal/AdicFinitePresentation.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicFinitePresentation.lean#L163)
