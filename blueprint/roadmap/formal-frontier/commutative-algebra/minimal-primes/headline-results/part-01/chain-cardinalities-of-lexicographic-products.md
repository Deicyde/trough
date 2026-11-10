---
declaration: theorem
origin: cited
lean: Set.chainHeight_prod_lex
statement: formalized
proof: formalized
---

# Chain cardinalities of lexicographic products

For arbitrary relations `rα`, `rβ` on independently universed types and arbitrary
sets `s`, `t`, [`Set.chainHeight_prod_lex`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean)
proves that the chain height of `s ×ˢ t` for `Prod.Lex rα rβ` is the product of
the factor chain heights, provided `rα` is irreflexive **on `s`**. Neither relation
needs to be transitive; the second may have loops. `Set.chainHeight_toLex_prod`
transports this formula to the canonical less-than relation on the image under `toLex`,
with only `LT` on both types and first-relation `Std.Irrefl`.

These are `ENat` **vertex cardinalities**, not edge counts, Krull dimensions or
ordinal ranks. Empty factors give zero even beside infinite height. The proof
uses products of comparable subsets for the lower bound and finite first-coordinate
fibre counting for the upper bound, so it neither sorts a nontransitive comparable
set nor assumes a longest chain exists. It does not assert the analogous formula
for canonical weak `≤` in arbitrary preorders.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Set.chainHeight_prod_lex` (theorem), declared in [MinimalPrimes/Order/ChainHeight.lean, line 251](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean#L251).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Set.chainHeight_prod_lex` in MinimalPrimes/Order/ChainHeight.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean#L251)
