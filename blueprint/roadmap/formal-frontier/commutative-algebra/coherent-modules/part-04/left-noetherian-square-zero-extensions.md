---
declaration: theorem
origin: cited
lean: TrivSqZeroExt.isNoetherianRing_iff
statement: formalized
proof: formalized
---

# Left Noetherian square-zero extensions

For a possibly noncommutative
`Ring R` and an `AddCommMonoid M` with commuting left and right `R`-module
actions, [`TrivSqZeroExt.isNoetherianRing_iff`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Noetherian.lean)
characterizes `IsNoetherianRing (TrivSqZeroExt R M)` by
`IsNoetherianRing R ∧ Module.Finite R M`. Finiteness here is as a **left**
`R`-module. The companion `TrivSqZeroExt.isNoetherianRing_iff_isNoetherian`
replaces `Module.Finite R M` by `IsNoetherian R M`. Centrality is not required,
and the two carrier universes are independent.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `TrivSqZeroExt.isNoetherianRing_iff` (theorem), declared in [CoherentModules/Algebra/TrivSqZeroExt/Noetherian.lean, line 75](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Noetherian.lean#L75).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `TrivSqZeroExt.isNoetherianRing_iff` in CoherentModules/Algebra/TrivSqZeroExt/Noetherian.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Noetherian.lean#L75)
