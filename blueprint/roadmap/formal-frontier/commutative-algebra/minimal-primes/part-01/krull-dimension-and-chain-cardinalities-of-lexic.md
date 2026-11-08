---
declaration: theorem
origin: cited
lean: Order.krullDim_toLex_sigma, Order.krullDim_toLex_sum, Set.chainHeight_sigma_lex
statement: formalized
proof: formalized
---

# Krull dimension and chain cardinalities of lexicographic sums

For arbitrary subsets of independently universed dependent preorders whose active indices form a finite strict chain, the stock lexicographic Sigma dimension is the active-index dimension plus the sum of active fiber dimensions. Empty support and infinite fiber dimensions are included. For two arbitrary preorder subsets, the tagged lexicographic union has the maximum of their dimensions and their sum plus one. For arbitrary subsets of independently universed dependent sums with raw relations, chain height is the supremum of finite sums of fiber heights, assuming only pairwise comparability and irreflexivity of the active indices. Empty fibers and infinite heights are allowed, with no transitivity, global order, finiteness or attainment hypothesis.

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/formalization.yaml) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Order.krullDim_toLex_sigma` (theorem), declared in [MinimalPrimes/Order/KrullDimension.lean, line 1596](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L1596).
- `Order.krullDim_toLex_sum` (theorem), declared in [MinimalPrimes/Order/KrullDimension.lean, line 949](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L949).
- `Set.chainHeight_sigma_lex` (theorem), declared in [MinimalPrimes/Order/ChainHeight.lean, line 773](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean#L773).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: formalization.yaml](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/formalization.yaml)
- [Source of `Order.krullDim_toLex_sigma` in MinimalPrimes/Order/KrullDimension.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L1596)
- [Source of `Order.krullDim_toLex_sum` in MinimalPrimes/Order/KrullDimension.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L949)
- [Source of `Set.chainHeight_sigma_lex` in MinimalPrimes/Order/ChainHeight.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean#L773)
