---
declaration: theorem
origin: cited
lean: Order.krullDim_toLex_prod
statement: formalized
proof: formalized
---

# Krull dimension of lexicographic products

For arbitrary subsets `s`, `t` of independently universed preorders,
[`Order.krullDim_toLex_prod`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean) states
`κ(toLex '' (s ×ˢ t)) = κ(s) * κ(t) + κ(s) + κ(t)` in `WithBot ℕ∞`.
The carrier is the membership subtype of that image in `α ×ₗ β`, with the
`Prod.Lex` preorder of the given factor preorders. Ties in the first coordinate
require equality, not preorder equivalence. No antisymmetry, nonemptiness,
finiteness or attainment is assumed.

An empty factor gives bottom even beside top. In the stock arithmetic,
`⊥ * 0 = 0`, but the explicit bottom summand still absorbs the whole polynomial.
A singleton factor preserves the other dimension, including bottom and top;
top with dimension zero gives top despite its zero multiplication term.
Two distinct equivalent first coordinates with three-point chain fibres give
two incomparable fibres and dimension two. Infinite dimension includes
unbounded finite chains without a longest or infinite chain.
`Fin 2 ×ₗ Fin 3` has dimension five, whereas its pointwise product has dimension
three and its tagged lexicographic sum has dimension four.
The vertex-height input is the existing whole `Set.chainHeight_toLex_prod`
formula, together with the finite-cut dimension comparisons above.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Order.krullDim_toLex_prod` (theorem), declared in [MinimalPrimes/Order/KrullDimension.lean, line 1031](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L1031).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Order.krullDim_toLex_prod` in MinimalPrimes/Order/KrullDimension.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L1031)
