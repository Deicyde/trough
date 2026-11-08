---
declaration: theorem
origin: cited
lean: Order.krullDim_le_iSup_of_subset_biUnion_finset
statement: formalized
proof: formalized
---

# Krull dimension under finite covers

For one given preorder on `α : Type u`, an independent index `ι : Type v`,
`I : Finset ι`, a family `s : ι → Set α`, and `t ⊆ ⋃ i ∈ I, s i`,
[`Order.krullDim_le_iSup_of_subset_biUnion_finset`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean)
states

```lean
Order.krullDim t ≤
  ⨆ J ∈ I.powerset, ⨆ (_ : J.Nonempty),
    (∑ i ∈ J, Order.krullDim (s i)) + ((J.card - 1 : ℕ) : WithBot ℕ∞)
```

All membership subtypes inherit the given preorder. The pieces may overlap or be
empty; there is no finiteness, antisymmetry, closure or attainment assumption on the
ambient order. Subtraction takes place in the natural numbers before casting.
Restricting to nonempty subfamilies makes the bound bottom for an empty family or
an all-empty cover, while singleton subfamilies preserve a piece of top dimension.
The three singleton pieces of a three-point total order give the sharp term two
from the full subfamily. A literal finite union is the reflexive-inclusion application.
The finite chain-height sum bound is already supplied by Mathlib's
`Finset.apply_union_le_sum` applied to `Set.chainHeight_empty` and
`Set.chainHeight_union_le`, followed by `Set.chainHeight_mono` for subsets.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Order.krullDim_le_iSup_of_subset_biUnion_finset` (theorem), declared in [MinimalPrimes/Order/KrullDimension.lean, line 1660](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L1660).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Order.krullDim_le_iSup_of_subset_biUnion_finset` in MinimalPrimes/Order/KrullDimension.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L1660)
