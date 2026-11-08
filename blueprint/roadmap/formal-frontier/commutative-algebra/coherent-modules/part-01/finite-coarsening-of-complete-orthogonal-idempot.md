---
declaration: theorem
origin: cited
lean: CompleteOrthogonalIdempotents.sum_fiberwise
statement: formalized
proof: formalized
---

# Finite coarsening of complete orthogonal idempotents

Over any possibly
noncommutative `Semiring A`, summing a finite complete orthogonal family over
the fibres of an arbitrary map `q : I → J` gives a complete orthogonal family
indexed by `J`. Both index types have `Fintype` instances, with decidable equality
needed only on `J`; the three universes are independent. The map need not be
surjective: unused labels have value zero. Empty index types and zero semirings
are allowed; no additive inverses, cancellation or centrality is required. See
[`CompleteOrthogonalIdempotents.sum_fiberwise`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Idempotents.lean).

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `CompleteOrthogonalIdempotents.sum_fiberwise` (theorem), declared in [CoherentModules/RingTheory/Idempotents.lean, line 140](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Idempotents.lean#L140).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `CompleteOrthogonalIdempotents.sum_fiberwise` in CoherentModules/RingTheory/Idempotents.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Idempotents.lean#L140)
