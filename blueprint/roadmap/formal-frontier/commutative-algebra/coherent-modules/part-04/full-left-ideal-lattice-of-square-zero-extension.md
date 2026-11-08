---
declaration: def
origin: cited
lean: TrivSqZeroExt.idealOrderIsoWithTop
statement: formalized
---

# Full left-ideal lattice of square-zero extensions

For a possibly
noncommutative division semiring `D : Type u` and an additive commutative group
`M : Type v` with its given actions `[Module D M]`, `[Module Dᵐᵒᵖ M]` and
`[SMulCommClass D Dᵐᵒᵖ M]`,
[`TrivSqZeroExt.idealOrderIsoWithTop`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Ideal.lean)
identifies `Ideal (TrivSqZeroExt D M)` with `WithTop (Submodule D M)` as ordered
lattices. The two carrier universes are independent. A coefficient submodule
`N` corresponds to `0 × N`, using the original left action. The adjoined top
is the whole extension, whereas the coerced internal top is the proper
projection kernel
`K = RingHom.ker (TrivSqZeroExt.fstHom ℕ D M : TrivSqZeroExt D M →+* D)`,
even when `M` is zero. The
[coatom client](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModulesTest/Algebra/TrivSqZeroExt/Ideal.lean) derives
maximality of this kernel through the order isomorphism. No ring structure on
`D`, centrality or finiteness assumption is required. Coefficient submodules
can be cones rather than additive subgroups and need not be stable under the
right action; this classifies **left** ideals, not only two-sided ideals.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `TrivSqZeroExt.idealOrderIsoWithTop` (def), declared in [CoherentModules/Algebra/TrivSqZeroExt/Ideal.lean, line 60](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Ideal.lean#L60).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `TrivSqZeroExt.idealOrderIsoWithTop` in CoherentModules/Algebra/TrivSqZeroExt/Ideal.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Ideal.lean#L60)
