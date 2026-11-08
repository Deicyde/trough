---
declaration: theorem
origin: cited
lean: Order.krullDim_iUnion_of_not_lt
statement: formalized
proof: formalized
---

# Krull dimension of exclusive-piece unions

For a given preorder on `α : Type u`, an arbitrary independent `ι : Sort v`, and
`s : ι → Set α`,
[`Order.krullDim_iUnion_of_not_lt`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean) states
`Order.krullDim (⋃ i, s i) = ⨆ i, Order.krullDim (s i)` when points in
`s i \ s j` and `s j \ s i` satisfy `¬ a < b` for every ordered pair `i,j`.
All membership subtypes inherit the given preorder. No antisymmetry, inhabitation,
finiteness, directedness or attainment is assumed.

The finite-cut comparisons `Order.le_krullDim_iff_le_chainHeight` and
`Order.krullDim_le_iff_chainHeight_le` relate dimension bounds `n : ℕ` to
strict-chain height bounds `n + 1`, without assuming finite height. Dimension lies
in `WithBot ℕ∞` and counts strict steps, whereas chain height lies in `ℕ∞` and
counts vertices. Empty sets have values bottom and zero, singletons zero and one,
and unbounded finite chains give top. These generic order interfaces are
Mathlib-upstream candidates.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Order.krullDim_iUnion_of_not_lt` (theorem), declared in [MinimalPrimes/Order/KrullDimension.lean, line 500](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L500).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Order.krullDim_iUnion_of_not_lt` in MinimalPrimes/Order/KrullDimension.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L500)
