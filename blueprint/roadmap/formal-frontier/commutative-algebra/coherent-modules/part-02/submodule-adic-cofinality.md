---
declaration: def
origin: cited
lean: Ideal.HasSubmoduleAdicCofinality
statement: formalized
---

# Submodule adic cofinality

For an arbitrary ideal `I` of a commutative
ring `R`,
[`Ideal.HasSubmoduleAdicCofinality`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicCompatibility.lean)
expresses `∀ n, ∃ m, N ⊓ (I ^ m • ⊤) ≤ I ^ n • N` for every submodule
`N` of every finite `R`-module. This is Fujiwara--Kato's (AP); restricting to
finitely generated submodules gives the existing
`Ideal.HasFiniteSubmoduleAdicCofinality` condition (APf). Both `.cofinal`
eliminators allow an independent module universe. Nilpotent ideals satisfy
(AP) without Noetherianity or finite generation of the ideal or submodule;
every ideal of a Noetherian ring satisfies it by
[Artin–Rees](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Filtration.lean). The ambient module
need not be finitely presented. Cofinality is pointwise, not a full shifted
Artin–Rees equality. The APf providers follow from (AP), and the
[range client](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModulesTest/RingTheory/Filtration.lean) applies the APf
API to maps between finite modules in independent universes.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Ideal.HasSubmoduleAdicCofinality` (def), declared in [CoherentModules/RingTheory/Ideal/AdicCompatibility.lean, line 254](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicCompatibility.lean#L254).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Ideal.HasSubmoduleAdicCofinality` in CoherentModules/RingTheory/Ideal/AdicCompatibility.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicCompatibility.lean#L254)
