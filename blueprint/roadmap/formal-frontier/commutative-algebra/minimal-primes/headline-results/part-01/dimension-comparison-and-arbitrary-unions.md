---
declaration: theorem
origin: cited
lean: Order.krullDim_le_krullDim_iff_chainHeight_le_chainHeight
statement: formalized
proof: formalized
---

# Dimension comparison and arbitrary unions

For arbitrary subsets of independently universed given preorders,
[`Order.krullDim_le_krullDim_iff_chainHeight_le_chainHeight`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean)
states
`κ(s) ≤ κ(t) ↔ H(s) ≤ H(t)`, where `κ` is the dimension of the membership
subtype in `WithBot ℕ∞` and `H` is ambient strict-chain vertex height in `ℕ∞`.
There is no map between the carriers, and each subtype inherits its given preorder.
Empty sets have values bottom and zero; singletons have values zero and one.
Distinct equivalent preorder points do not form a strict step. Infinite values
include unbounded finite chains without a longest or infinite chain.

For arbitrary subsets in one given preorder, `Order.krullDim_union_le` states
`κ(s ∪ t) ≤ κ(s) ⊔ κ(t) ⊔ (κ(s) + κ(t) + 1)`.
No disjointness, upper/lower closure, directedness, antisymmetry, nonemptiness,
finiteness or attainment is assumed. All right-hand operations are in `WithBot ℕ∞`;
the separate joins preserve the other dimension when one piece is empty, even at top.
In the five-point total order, the alternating pieces `{0, 2, 4}` and `{1, 3}`
have dimensions two and one, while their union has dimension four: the additive
term is sharp and a maximum-only bound fails. Overlap is also allowed.

The comparison extends the finite-cut dimension/height equivalences to arbitrary
bounds, including bottom and top. The arbitrary-union bound relates the existing
`Set.chainHeight_union_le` and `Set.chainHeight_toLex_sum` height formulas to the
exact dimension formula `Order.krullDim_toLex_sum` for lexicographic sums.
These interfaces build on Mathlib's subtype orders, Krull dimension, strict-chain
height and extended-natural arithmetic.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Order.krullDim_le_krullDim_iff_chainHeight_le_chainHeight` (theorem), declared in [MinimalPrimes/Order/KrullDimension.lean, line 1108](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L1108).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Order.krullDim_le_krullDim_iff_chainHeight_le_chainHeight` in MinimalPrimes/Order/KrullDimension.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L1108)
