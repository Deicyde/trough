---
declaration: theorem
origin: cited
lean: Set.chainHeight_iUnion_of_not_rel
statement: formalized
proof: formalized
---

# Chain cardinalities of exclusive-piece unions

For an arbitrary relation `r` on `α : Type u` and a family `s : ι → Set α` with
independent `ι : Sort v`,
[`Set.chainHeight_iUnion_of_not_rel`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean) gives
`(⋃ i, s i).chainHeight r = ⨆ i, (s i).chainHeight r` when points in
`s i \ s j` and `s j \ s i` cannot compare for every ordered pair `i,j`.
For each pair, the no-cross condition concerns only its opposite exclusive pieces;
all loops remain unrestricted. The family need not be directed, finite or nonempty,
and no relation laws or attainment are assumed.
The heights are `ENat` vertex cardinalities: the empty union and empty supremum are
zero, a singleton has height one, and unbounded finite chain sizes give top.

The proof shows that the traces of each chain on the pieces are inclusion-directed
and applies the existing directed-union formula to those traces. It does not choose
one piece containing the whole chain: nested finite initial segments of an infinite
chain satisfy the hypothesis but no piece contains their union.
The retained `Set.chainHeight_union_of_not_rel` is the Bool-family corollary, giving
the two-piece maximum formula with the same exclusive-piece hypothesis.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Set.chainHeight_iUnion_of_not_rel` (theorem), declared in [MinimalPrimes/Order/ChainHeight.lean, line 879](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean#L879).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Set.chainHeight_iUnion_of_not_rel` in MinimalPrimes/Order/ChainHeight.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/ChainHeight.lean#L879)
