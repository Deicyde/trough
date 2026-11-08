---
declaration: theorem
origin: cited
lean: Module.isCoherent_iff_of_bijective_of_fg_ker
statement: formalized
proof: formalized
---

# Coherence along quotient coefficients

For possibly noncommutative rings
`R`, `S` and additive commutative monoids `N`, `M` with their given `R`- and
`S`-module structures,
[`Module.isCoherent_iff_of_bijective_of_fg_ker`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/FinitePresentation.lean)
gives `Module.IsCoherent R N ↔ Module.IsCoherent S M` along a bijective
semilinear map `f : N →ₛₗ[σ] M`, provided `σ : R →+* S` is surjective and
`(RingHom.ker σ).FG`. Kernel finite generation is as a **left** ideal, not
merely as a two-sided ideal. The four carrier universes are independent;
`σ` need not be injective. No extra action, scalar inverse, coherence of an
ambient ring, Noetherianity, flatness or nontriviality hypothesis is required.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.isCoherent_iff_of_bijective_of_fg_ker` (theorem), declared in [CoherentModules/FinitePresentation.lean, line 282](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/FinitePresentation.lean#L282).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Module.isCoherent_iff_of_bijective_of_fg_ker` in CoherentModules/FinitePresentation.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/FinitePresentation.lean#L282)
