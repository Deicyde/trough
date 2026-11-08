---
declaration: theorem
origin: cited
lean: isNoetherian_semilinearMap
statement: formalized
proof: formalized
---

# Noetherian semilinear Hom

For semirings `R`, `R₂`, a ring `S`, a finitely
generated `R`-semimodule `M`, and a Noetherian `S`-module `N` with a commuting
`R₂`-action,
[`isNoetherian_semilinearMap`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Noetherian.lean)
makes `M →ₛₗ[σ] N` Noetherian for the canonical pointwise `S`-action, for every
`σ : R →+* R₂`. The five universes are independent; no surjectivity of `σ`,
scalar commutativity or ambient Noetherianity is required.
`isNoetherian_linearMap_of_finite` gives the plain-linear specialization and
recovers Mathlib's `isNoetherian_linearMap` proposition in its commutative-ring
case, with the same pointwise action.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `isNoetherian_semilinearMap` (theorem), declared in [CoherentModules/RingTheory/Noetherian.lean, line 209](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Noetherian.lean#L209).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `isNoetherian_semilinearMap` in CoherentModules/RingTheory/Noetherian.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Noetherian.lean#L209)
