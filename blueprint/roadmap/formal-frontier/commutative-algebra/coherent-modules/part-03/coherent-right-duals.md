---
declaration: theorem
origin: cited
lean: Module.FinitePresentation.isCoherent_dual
statement: formalized
proof: formalized
---

# Coherent right duals

For a possibly noncommutative `Ring R` and a finitely
presented left `R`-module `M` with its given `AddCommMonoid` and module structure,
[`Module.FinitePresentation.isCoherent_dual`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Hom.lean) gives
`Module.IsCoherent Rᵐᵒᵖ (Module.Dual R M)` assuming only right coherence
`[IsCoherentRing Rᵐᵒᵖ]` of the ring. The dual uses the canonical right action
`(q • f) x = f x * MulOpposite.unop q` for `q : Rᵐᵒᵖ`, induced by right
multiplication on the codomain `R`. The ring and module universes are independent;
neither left coherence nor a supplied additive group structure on `M` is required.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.FinitePresentation.isCoherent_dual` (theorem), declared in [CoherentModules/Hom.lean, line 185](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Hom.lean#L185).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Module.FinitePresentation.isCoherent_dual` in CoherentModules/Hom.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Hom.lean#L185)
