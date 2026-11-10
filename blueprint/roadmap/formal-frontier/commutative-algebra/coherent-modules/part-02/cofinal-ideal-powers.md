---
declaration: theorem
origin: cited
lean: Ideal.hasSubmoduleAdicCofinality_iff_of_pow_le
statement: formalized
proof: formalized
---

# Cofinal ideal powers

For ideals `I, J` of a commutative ring with
`I ^ a ≤ J` and `J ^ b ≤ I` for some natural numbers `a, b`,
[`Ideal.hasSubmoduleAdicCofinality_iff_of_pow_le`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicCompatibility.lean)
makes (AP) equivalent for `I` and `J`; the companion
`hasFiniteSubmoduleAdicCofinality_iff_of_pow_le` does the same for (APf).
The witnesses may be zero. In particular, replacing an ideal by any positive
power preserves both conditions. The shared pointwise theorem
`Submodule.adic_cofinality_iff_of_pow_le` already applies to arbitrary left
ideals of a semiring and arbitrary submodules of an additive commutative
semimodule, with its given action and independent carrier universes.
This comparison needs no finiteness or additive-inverse hypothesis.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Ideal.hasSubmoduleAdicCofinality_iff_of_pow_le` (theorem), declared in [CoherentModules/RingTheory/Ideal/AdicCompatibility.lean, line 436](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicCompatibility.lean#L436).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Ideal.hasSubmoduleAdicCofinality_iff_of_pow_le` in CoherentModules/RingTheory/Ideal/AdicCompatibility.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicCompatibility.lean#L436)
