---
declaration: theorem
origin: cited
lean: OrthogonalIdempotents.semiconj_sum_fiberwise_of_mapsTo_range
statement: formalized
proof: formalized
---

# Fibrewise additive intertwining

For additive commutative monoids `M`, `N`,
let `P : I → AddMonoid.End M` have finite index set and sum to the identity, and
let `Q : J → AddMonoid.End N` be an orthogonal idempotent family, with
decidable equality on `J`. For any `q : I → J` and additive `h : M →+ N`,
sending `range (P i)` into `range (Q (q i))` for every `i` implies
`h ∘ (∑ i with q i = j, P i) = Q j ∘ h` for every `j`. This implication uses
no source orthogonality; it is an equivalence when `P` is a complete orthogonal
idempotent family.
The target label set may be infinite, and `Q` need not be complete; labels may
be merged or omitted. An unused `Q j` need only kill `h(M)`, not vanish on all
of `N`. No subtraction, cancellation or scalar compatibility is required, and
the two monoid and two index universes are independent. See
[`OrthogonalIdempotents.semiconj_sum_fiberwise_of_mapsTo_range`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Idempotents.lean)
and [`CompleteOrthogonalIdempotents.semiconj_sum_fiberwise_iff_mapsTo_range`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Idempotents.lean).

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `OrthogonalIdempotents.semiconj_sum_fiberwise_of_mapsTo_range` (theorem), declared in [CoherentModules/RingTheory/Idempotents.lean, line 81](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Idempotents.lean#L81).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `OrthogonalIdempotents.semiconj_sum_fiberwise_of_mapsTo_range` in CoherentModules/RingTheory/Idempotents.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Idempotents.lean#L81)
