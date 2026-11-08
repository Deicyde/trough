---
declaration: theorem
origin: cited
lean: ENat.WithBot.succ_sum_powerset_nonempty
statement: formalized
proof: formalized
---

# Successors of finite product expansions

For arbitrary `ι : Type u`, `J : Finset ι` and `d : ι → WithBot ℕ∞`,
[`ENat.WithBot.succ_sum_powerset_nonempty`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Data/ENat/BigOperators.lean)
states that the bottom-aware successor of the sum of `∏ i ∈ U, d i` over nonempty
subsets `U` of `J` equals `∏ i ∈ J, WithBot.succ (d i)`. The equality is in `ℕ∞`;
the subset products and their sum are in `WithBot ℕ∞`. Empty `J` and arbitrary
bottom and top values are included, with no decidable-equality premise on `ι`.
The proof reuses Mathlib's whole finite-product expansion `Finset.prod_add_one`.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `ENat.WithBot.succ_sum_powerset_nonempty` (theorem), declared in [MinimalPrimes/Data/ENat/BigOperators.lean, line 45](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Data/ENat/BigOperators.lean#L45).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `ENat.WithBot.succ_sum_powerset_nonempty` in MinimalPrimes/Data/ENat/BigOperators.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Data/ENat/BigOperators.lean#L45)
