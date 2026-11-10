---
declaration: theorem
origin: cited
lean: TwoSidedIdeal.isCoatomic
statement: formalized
proof: formalized
---

# Coatomicity of two-sided ideals

For any unital, possibly nonassociative ring `R`,
[`TwoSidedIdeal.isCoatomic`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/TwoSidedIdeal/Atoms.lean)
proves `IsCoatomic (TwoSidedIdeal R)`: every proper two-sided ideal lies below a
maximal proper two-sided ideal. No nontriviality, commutativity or finiteness
assumption is needed. Use this theorem as a local instance with Mathlib's
coatom consumers. The
[simple-quotient example](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModulesTest/RingTheory/TwoSidedIdeal.lean)
combines it with the congruence correspondence to obtain a nontrivial simple
quotient of an arbitrary nontrivial ring, with its surjective unital quotient map.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `TwoSidedIdeal.isCoatomic` (theorem), declared in [CoherentModules/RingTheory/TwoSidedIdeal/Atoms.lean, line 52](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/TwoSidedIdeal/Atoms.lean#L52).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `TwoSidedIdeal.isCoatomic` in CoherentModules/RingTheory/TwoSidedIdeal/Atoms.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/TwoSidedIdeal/Atoms.lean#L52)
