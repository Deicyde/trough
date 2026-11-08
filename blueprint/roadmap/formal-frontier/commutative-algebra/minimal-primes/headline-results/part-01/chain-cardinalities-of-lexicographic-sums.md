---
declaration: theorem
origin: cited
lean: Set.chainHeight_sum_lex
statement: formalized
proof: formalized
---

# Chain cardinalities of lexicographic sums

For arbitrary relations `rα`, `rβ` on independently universed types and arbitrary
sets `s`, `t`, [`Set.chainHeight_sum_lex`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean)
proves that the union of the two injection images has chain height
`s.chainHeight rα + t.chainHeight rβ` for `Sum.Lex rα rβ`. Within each tag the
factor relation is used, and every left-tagged point precedes every right-tagged
point. No irreflexivity, transitivity, nonemptiness or finiteness is assumed.
`Set.chainHeight_toLex_sum` transports the formula under `toLex` to the canonical
less-than relation on `α ⊕ₗ β`, using only the given `LT` records on both factors.

The heights count vertices in `ENat`: two singleton blocks, or two nonempty
antichains, give height two. The disjoint relation `Sum.LiftRel`, used by ordinary
Sum less-than, is different. Empty factors contribute zero, including beside top.
The proof applies the disjoint cross-comparable union formula and Mathlib's
relation-embedding transport. Its union core glues subset chains by cross comparison,
without sorting chains or assuming their heights are attained. Unbounded finite
chain cardinalities are included.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Set.chainHeight_sum_lex` (theorem), declared in [MinimalPrimes/Order/ChainHeight.lean, line 624](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean#L624).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Set.chainHeight_sum_lex` in MinimalPrimes/Order/ChainHeight.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean#L624)
