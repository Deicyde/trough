---
declaration: theorem
origin: cited
lean: Set.scottContinuous_chainHeight
statement: formalized
proof: formalized
---

# Directed suprema of relations on a fixed set

For any type `α` and fixed subset `s`,
[`Set.scottContinuous_chainHeight`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean) states that
`r ↦ s.chainHeight r` is Scott continuous for the pointwise implication order on relations
`α → α → Prop`. No order or relation laws on `α` are needed. Scott continuity preserves
suprema of **nonempty directed** families, not arbitrary joins or bottom.

For a directed family `r : ι → α → α → Prop`, with independent `ι : Sort v`,
[`Set.chainHeight_iSup_of_directed`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean) gives
`H(⨆ i, r i) = H(⊥) ⊔ ⨆ i, H(r i)`, where `H(r) = s.chainHeight r` takes values in
`ENat` and `⊔` is maximum. The false-relation baseline is zero for empty `s` and one
otherwise; it is essential when `ι` is empty. The proof captures all distinct-point
comparisons of a finite chain in one relation, without sorting or assuming attainment.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Set.scottContinuous_chainHeight` (theorem), declared in [MinimalPrimes/Order/ChainHeight.lean, line 806](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean#L806).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Set.scottContinuous_chainHeight` in MinimalPrimes/Order/ChainHeight.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean#L806)
