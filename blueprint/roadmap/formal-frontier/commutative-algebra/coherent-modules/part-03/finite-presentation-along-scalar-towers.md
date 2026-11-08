---
declaration: theorem
origin: cited
lean: Module.FinitePresentation.trans_of_tower
statement: formalized
proof: formalized
---

# Finite presentation along scalar towers

For possibly noncommutative rings
`R`, `S` and an additive commutative monoid `N` with its given `R`- and
`S`-module structures and towers `R → S → S` and `R → S → N`,
[`Module.FinitePresentation.trans_of_tower`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/FinitePresentation.lean)
gives finite presentation of `N` over `R` from finite presentation of `S`
over `R` and of `N` over `S`. Conversely, `of_restrictScalars` gives finite
presentation over `S` from finite presentation over `R` assuming only that
`S` is finite over `R`. Thus `restrictScalars_iff` equates the two finite-
presentation properties when `S` is finitely presented over `R`, without
assuming either property of `N` in advance. The three universes are
independent; no coherence, Noetherianity, centrality or faithfulness is
required. `trans_of_algebra` recovers the type and argument order of Mathlib's
commutative-algebra `Module.FinitePresentation.trans` as a corollary of the
scalar-tower theorem.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.FinitePresentation.trans_of_tower` (theorem), declared in [CoherentModules/FinitePresentation.lean, line 215](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/FinitePresentation.lean#L215).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Module.FinitePresentation.trans_of_tower` in CoherentModules/FinitePresentation.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/FinitePresentation.lean#L215)
