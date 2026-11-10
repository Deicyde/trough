---
declaration: theorem
origin: cited
lean: Module.IsCoherent.of_semilinear_retract
statement: formalized
proof: formalized
---

# Coherence along semilinear retractions

For arbitrary rings `R`, `S` and
additive commutative monoids `N`, `M` with their given `R`- and `S`-module
structures, let `σ : R →+* S`, `τ : S →+* R`, `f : N →ₛₗ[σ] M` and
`g : M →ₛₗ[τ] N` satisfy `τ ∘ σ = id` and `g ∘ f = id`. Then
[`Module.IsCoherent.of_semilinear_retract`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Retraction.lean)
descends coherence of `M` over `S` to coherence of `N` over `R`. The four
carrier universes are independent; no additional scalar action, finiteness,
flatness, Noetherianity, faithfulness or nontriviality assumption is required.
The regular-module corollary `IsCoherentRing.of_retract` says that a ring
retract of a coherent ring is coherent, including noncommutative rings.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.IsCoherent.of_semilinear_retract` (theorem), declared in [CoherentModules/Retraction.lean, line 46](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Retraction.lean#L46).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Module.IsCoherent.of_semilinear_retract` in CoherentModules/Retraction.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Retraction.lean#L46)
