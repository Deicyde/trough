---
declaration: theorem
origin: cited
lean: Submodule.adic_cofinality_iff_of_semilinearEquiv
statement: formalized
proof: formalized
---

# Semilinear transport of adic cofinality

For semirings `R`, `S`, a
coefficient equivalence `σ : R ≃+* S` and a compatible semilinear
equivalence `e : M ≃ₛₗ[(σ : R →+* S)] P` between additive commutative
semimodules with their given actions,
[`Submodule.adic_cofinality_iff_of_semilinearEquiv`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicCompatibility.lean)
transports `∀ n, ∃ m, N ⊓ (I ^ m • ⊤) ≤ I ^ n • N` to the condition for
`I.map σ.toRingHom` and `N.map e.toLinearMap`. It allows arbitrary left
ideals and submodules in four independent universes, without finiteness
or additive inverses. For commutative rings, the companion
`Ideal.hasSubmoduleAdicCofinality_iff_of_ringEquiv` and
`Ideal.hasFiniteSubmoduleAdicCofinality_iff_of_ringEquiv` give (AP)/(APf)
invariance under coefficient equivalence. Both predicates quantify over
finite ambient modules; only (APf) restricts submodules to be finitely
generated.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Submodule.adic_cofinality_iff_of_semilinearEquiv` (theorem), declared in [CoherentModules/RingTheory/Ideal/AdicCompatibility.lean, line 192](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicCompatibility.lean#L192).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Submodule.adic_cofinality_iff_of_semilinearEquiv` in CoherentModules/RingTheory/Ideal/AdicCompatibility.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicCompatibility.lean#L192)
