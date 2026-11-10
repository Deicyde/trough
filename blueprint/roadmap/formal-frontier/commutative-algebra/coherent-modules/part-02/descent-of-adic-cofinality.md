---
declaration: theorem
origin: cited
lean: Ideal.HasSubmoduleAdicCofinality.of_map_of_faithfullyFlat
statement: formalized
proof: formalized
---

# Descent of adic cofinality

For commutative rings `R`, `A`,
[`Ideal.HasSubmoduleAdicCofinality.of_map_of_faithfullyFlat`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicBaseChange.lean)
descends (AP) from `I.map (algebraMap R A)` to `I` along a faithfully flat
algebra. Alternatively,
[`Ideal.HasSubmoduleAdicCofinality.of_map_of_linearRetraction`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicBaseChange.lean)
uses an `R`-linear map `p : A →ₗ[R] R` with `p 1 = 1`, without a flatness
hypothesis; `p` need not preserve multiplication. Both have corresponding
`HasFiniteSubmoduleAdicCofinality` methods for (APf). The algebra need not be
module-finite, the ideal need not be finitely generated, and no finite
presentation or Noetherian hypothesis is required. The pointwise
linear-retraction theorem works over commutative semirings and arbitrary
semimodules; its tensor membership and inclusion-reflection lemmas even
allow noncommutative scalar algebras. All carrier universes are independent.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Ideal.HasSubmoduleAdicCofinality.of_map_of_faithfullyFlat` (theorem), declared in [CoherentModules/RingTheory/Ideal/AdicBaseChange.lean, line 118](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicBaseChange.lean#L118).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Ideal.HasSubmoduleAdicCofinality.of_map_of_faithfullyFlat` in CoherentModules/RingTheory/Ideal/AdicBaseChange.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicBaseChange.lean#L118)
