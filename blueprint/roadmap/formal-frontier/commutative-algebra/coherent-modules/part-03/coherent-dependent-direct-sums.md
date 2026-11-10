---
declaration: theorem
origin: cited
lean: Module.IsCoherent.directSum_iff
statement: formalized
proof: formalized
---

# Coherent dependent direct sums

For an arbitrary index type, a possibly
noncommutative ring `R`, and additive commutative monoids `M i` with their
given `R`-module structures,
[`Module.IsCoherent.directSum_iff`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/DirectSum.lean)
gives
```lean
Module.IsCoherent R (DirectSum ι M) ↔
  (∀ i, Module.IsCoherent R (M i)) ∧ Set.Finite {i | ¬ Subsingleton (M i)}
```
Thus the nontrivial summands, not the ambient index type, must form a finite
set. Coherence means finite generation and finite presentation of every
finitely generated submodule. Empty index types, zero summands and zero
rings are allowed; no base-ring coherence, Noetherianity, faithfulness or
commutativity assumption is added. The index, ring and summand universes
are independent. `Module.IsCoherent.of_directSum` reflects coherence to
each original coordinate without a finite-index assumption. The supporting
[`Module.Finite.finite_nontrivial_summands`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/DirectSum.lean)
already obtains finiteness of the nontrivial summands from finite generation
over a semiring.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.IsCoherent.directSum_iff` (theorem), declared in [CoherentModules/RingTheory/DirectSum.lean, line 63](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/DirectSum.lean#L63).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Module.IsCoherent.directSum_iff` in CoherentModules/RingTheory/DirectSum.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/DirectSum.lean#L63)
