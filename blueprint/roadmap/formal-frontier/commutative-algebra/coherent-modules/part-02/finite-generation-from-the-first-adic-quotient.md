---
declaration: theorem
origin: cited
lean: Submodule.fg_iff_finite_quotient_smul
statement: formalized
proof: formalized
---

# Finite generation from the first adic quotient

For an arbitrary submodule
`N` of a finite original `R`-module `M`,
[`Submodule.fg_iff_finite_quotient_smul`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicKrull.lean)
detects `N.FG` on the intrinsic quotient `N / I N` over `R`, assuming APf and
`I ≤ (Module.annihilator R M).jacobson`. This is not the quotient by
`N ∩ I M`, and neither ideal-FG nor a Noetherian, finite-presentation,
flatness or completeness hypothesis is required.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Submodule.fg_iff_finite_quotient_smul` (theorem), declared in [CoherentModules/RingTheory/Ideal/AdicKrull.lean, line 238](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicKrull.lean#L238).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Submodule.fg_iff_finite_quotient_smul` in CoherentModules/RingTheory/Ideal/AdicKrull.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicKrull.lean#L238)
