---
declaration: theorem
origin: cited
lean: Ideal.hasSubmoduleAdicCofinality_iff_forall_exists_inf_pow_smul_eq_bot
statement: formalized
proof: formalized
---

# Power-killed submodule criteria

For an ideal `I` of a commutative ring `R`,
[`Ideal.hasSubmoduleAdicCofinality_iff_forall_exists_inf_pow_smul_eq_bot`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicCompatibility.lean)
characterizes (AP) by `∃ m, N ⊓ (I ^ m • ⊤) = ⊥` whenever
`∃ k, I ^ k • N = ⊥`, for every submodule `N` of every finite `R`-module.
The corresponding (APf) criterion tests only finitely generated `N`.
Both `.exists_inf_pow_smul_eq_bot` consumers allow an independent module
universe. A single common exponent kills the whole submodule; `I` need not
be finitely generated or nilpotent. The converse uses images in canonical
module quotients over the original coefficient ring `R`.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Ideal.hasSubmoduleAdicCofinality_iff_forall_exists_inf_pow_smul_eq_bot` (theorem), declared in [CoherentModules/RingTheory/Ideal/AdicCompatibility.lean, line 393](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicCompatibility.lean#L393).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Ideal.hasSubmoduleAdicCofinality_iff_forall_exists_inf_pow_smul_eq_bot` in CoherentModules/RingTheory/Ideal/AdicCompatibility.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicCompatibility.lean#L393)
