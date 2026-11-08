---
declaration: theorem
origin: cited
lean: Module.IsCoherent.semilinearMap
statement: formalized
proof: formalized
---

# Hom, tensor, and categories

For semirings `R`, `R₂`, a ring `S`, and any
`σ : R →+* R₂`, [`Module.IsCoherent.semilinearMap`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Hom.lean)
makes `M →ₛₗ[σ] N` coherent over `S` when the additive commutative group `M`
is finitely presented over `R` and the additive commutative group `N` is
coherent over `S`, with commuting given `R₂`- and `S`-actions on `N`.
The five universes are independent and the Hom action is pointwise. No
`S`-action on `M`, `R`-action on `N`, scalar commutativity or surjectivity
of `σ` is required. The existing `linearMap` theorem is its same-base
commutative-ring specialization. For a commutative base ring `R` and an
independent, possibly noncommutative ring `S`,
[`tensorProduct_left`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/TensorProduct.lean) makes `M ⊗[R] N`
coherent over `S` when `M` is coherent over `S`, `N` is finitely presented
over `R`, and the given `R`- and `S`-actions on `M` commute. No `R`-module
structure on `S` or `S`-action on `N` is required. The existing `tensorProduct`
theorem retains the same-base, finitely-presented-first specialization.
These are theorems, not global instances, and assume neither
coherence nor Noetherianity of an ambient scalar ring.
[`CoherentModuleCat`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/ModuleCat.lean) is a transparent full
subcategory with abelian structure obtained through generic category constructions.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.IsCoherent.semilinearMap` (theorem), declared in [CoherentModules/Hom.lean, line 126](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Hom.lean#L126).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Module.IsCoherent.semilinearMap` in CoherentModules/Hom.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Hom.lean#L126)
