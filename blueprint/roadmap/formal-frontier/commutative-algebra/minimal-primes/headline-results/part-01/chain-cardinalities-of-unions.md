---
declaration: theorem
origin: cited
lean: Set.chainHeight_union_le
statement: formalized
proof: formalized
---

# Chain cardinalities of unions

For an arbitrary relation `r` and subsets `s`, `t` of any type,
[`Set.chainHeight_union_le`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean) gives
`(s ∪ t).chainHeight r ≤ s.chainHeight r + t.chainHeight r`.
The pieces may overlap or be empty; neither relation laws nor finite heights or
attainment are required. The proof restricts each comparable subset to its two
intersections and uses `ENat` cardinality subadditivity.

For disjoint pieces with `∀ a ∈ s, ∀ b ∈ t, r a b ∨ r b a`,
[`Set.chainHeight_union_of_disjoint_of_cross`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean)
gives equality: `(s ∪ t).chainHeight r = s.chainHeight r + t.chainHeight r`.
Cross comparisons need not have a consistent direction. The binary lexicographic-sum
formula below reuses this common-ambient union result.

For an arbitrary relation `q : X → X → Prop`, family `P : κ → Set X` and
`J : Finset κ`, the finite-family formula
[`Set.chainHeight_biUnion_finset_of_disjoint_of_cross`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean)
states
`(⋃ i ∈ J, P i).chainHeight q = ∑ i ∈ J, (P i).chainHeight q`.
Pairwise disjointness and cross comparability are required **only on `J`**:
for distinct `i,j ∈ J`, the pieces are disjoint and every point of `P i` compares
with every point of `P j` in either direction. There are no relation laws,
ambient finiteness, decidable-equality, nonemptiness or attainment assumptions.
Empty pieces and unbounded, unattained chain heights are included.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Set.chainHeight_union_le` (theorem), declared in [MinimalPrimes/Order/ChainHeight.lean, line 585](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean#L585).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Set.chainHeight_union_le` in MinimalPrimes/Order/ChainHeight.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean#L585)
