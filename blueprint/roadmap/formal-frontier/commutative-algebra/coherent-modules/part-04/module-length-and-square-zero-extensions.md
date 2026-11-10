---
declaration: theorem
origin: cited
lean: LinearMap.length_eq_of_bijective
statement: formalized
proof: formalized
---

# Module length and square-zero extensions

For modules over arbitrary rings,
[`LinearMap.length_eq_of_bijective`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Length.lean)
preserves length under a bijective semilinear map whose scalar homomorphism is
surjective, without requiring that scalar homomorphism to be injective. The
rings and modules have four independent universes, and infinite lengths are
included. Its [algebra-map specialization](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModulesTest/RingTheory/Length.lean)
recovers Mathlib's surjective-algebra comparison under the same hypotheses.
For a division ring `D` and the original compatible left/right actions on `M`,
[`TrivSqZeroExt.length`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Length.lean)
computes the regular left-module length as `Module.length D M + 1`, directly
from the ideal-lattice classification. Only the finrank corollary adds
`[Module.Finite D M]`; neither centrality nor right-finiteness is assumed.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `LinearMap.length_eq_of_bijective` (theorem), declared in [CoherentModules/RingTheory/Length.lean, line 40](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Length.lean#L40).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `LinearMap.length_eq_of_bijective` in CoherentModules/RingTheory/Length.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Length.lean#L40)
