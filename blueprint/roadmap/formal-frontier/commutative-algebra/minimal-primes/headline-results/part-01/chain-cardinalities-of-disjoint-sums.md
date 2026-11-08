---
declaration: theorem
origin: cited
lean: Set.chainHeight_sum_liftRel
statement: formalized
proof: formalized
---

# Chain cardinalities of disjoint sums

For arbitrary relations `rα`, `rβ` on independently universed types and arbitrary
sets `s`, `t`, [`Set.chainHeight_sum_liftRel`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean)
gives chain height `max (s.chainHeight rα) (t.chainHeight rβ)` for the union of the
two tagged images under `Sum.LiftRel rα rβ`. No cross-tag points compare.
[`Set.chainHeight_sum`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean) gives the same formula
for ordinary `α ⊕ β` less-than, induced by precisely the two given `LT` records.
Neither result requires relation laws, nonemptiness, finiteness or attainment.

The heights are `ENat` vertex cardinalities: two nonempty antichains have disjoint-sum
height one, unlike lexicographic-sum height two. Empty factors contribute zero;
unbounded finite heights are included without assuming an infinite or longest chain.
The proof specializes the exclusive-piece maximum formula above, reusing Mathlib's
relation embeddings and image-height transport to identify the two tagged-piece heights.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Set.chainHeight_sum_liftRel` (theorem), declared in [MinimalPrimes/Order/ChainHeight.lean, line 933](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean#L933).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Set.chainHeight_sum_liftRel` in MinimalPrimes/Order/ChainHeight.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean#L933)
