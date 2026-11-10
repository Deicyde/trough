---
declaration: theorem
origin: cited
lean: Ideal.exists_pow_inf_eq_pow_smul_of_isNoetherian
statement: formalized
proof: formalized
---

# Artin–Rees for Noetherian modules

For an arbitrary commutative ring `R`,
ideal `I` and submodule `K` of a Noetherian `R`-module `M`,
[`Ideal.exists_pow_inf_eq_pow_smul_of_isNoetherian`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Filtration.lean)
gives a constant `c` such that
`(I ^ n • ⊤) ⊓ K = I ^ (n - c) • ((I ^ c • ⊤) ⊓ K)` for every `n ≥ c`.
Neither Noetherianity of `R` nor finite generation of `I` is assumed.
The ring and module universes are independent. The proof uses Mathlib's full
Artin–Rees theorem over the quotient by the module's annihilator. The
[shifted-cofinality client](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModulesTest/RingTheory/Filtration.lean) uses
the full equality at Mathlib's Noetherian-ring and finite-module hypotheses.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Ideal.exists_pow_inf_eq_pow_smul_of_isNoetherian` (theorem), declared in [CoherentModules/RingTheory/Filtration.lean, line 58](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Filtration.lean#L58).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Ideal.exists_pow_inf_eq_pow_smul_of_isNoetherian` in CoherentModules/RingTheory/Filtration.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Filtration.lean#L58)
