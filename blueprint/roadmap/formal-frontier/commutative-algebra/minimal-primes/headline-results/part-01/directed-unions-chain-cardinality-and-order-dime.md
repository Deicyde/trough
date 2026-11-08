---
declaration: theorem
origin: cited
lean: Set.chainHeight_iUnion_of_directed
statement: formalized
proof: formalized
---

# Directed unions: chain cardinality and order dimension

For an inclusion-directed family `s : ι → Set α`, with independent carrier and
index universes and an arbitrary index `ι : Sort v`,
[`Set.chainHeight_iUnion_of_directed`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean)
identifies the `ENat` chain height of the union with the supremum of the piece
heights for **any relation** on `α`. With only a preorder on `α`,
[`Order.krullDim_iUnion_of_directed`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean)
gives the analogous equality for the induced subtype orders in `WithBot ℕ∞`.
The relation invariant counts vertices; order dimension counts strict steps.
Empty unions have values zero and bottom respectively, and infinite suprema
need not be attained by a piece. No nonemptiness, antisymmetry or finite-height
assumption is required. The proofs capture finite chain witnesses in one piece;
they do not select a longest or infinite chain. These are relation-height and
induced-order formulas, not topological subspace dimension formulas.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Set.chainHeight_iUnion_of_directed` (theorem), declared in [MinimalPrimes/Order/ChainHeight.lean, line 216](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean#L216).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Set.chainHeight_iUnion_of_directed` in MinimalPrimes/Order/ChainHeight.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean#L216)
