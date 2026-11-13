---
declaration: theorem
origin: cited
lean: LongGapsBetweenPrimes.long_prime_gaps
statement: formalized
proof: formalized
---

# Improved long gaps between consecutive primes

> Formalizes the unconditional lower bound showing that, for all sufficiently large X, the largest gap between consecutive primes below X is at least a positive constant times log X (log log X)^2 log log log log X / (log log log X)^2. The development includes the short-translates sieve proposition, divisor coefficient estimates, truncated product weights, moment bounds, and the Erdos--Rankin covering argument used to derive the headline result.

*Quoted from the card [LeanPool/projects/long-gaps-between-primes.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/long-gaps-between-primes.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LongGapsBetweenPrimes.long_prime_gaps`](https://leanpool.github.io/lean-pool/LeanPool/LongGapsBetweenPrimes/Main.html#LongGapsBetweenPrimes.long_prime_gaps) (theorem; a main declaration), declared in [LeanPool/LongGapsBetweenPrimes/Main.lean, line 4524](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LongGapsBetweenPrimes/Main.lean#L4524): “There are a positive constant c and a real threshold X0 such that for every X at least X0, some pair of consecutive indexed primes below X has gap greater than c times log X (log log X)^2 log log log log X / (log log log X)^2.”
- [`LongGapsBetweenPrimes.long_gap_theorem`](https://leanpool.github.io/lean-pool/LeanPool/LongGapsBetweenPrimes/Main.html#LongGapsBetweenPrimes.long_gap_theorem) (theorem), declared in [LeanPool/LongGapsBetweenPrimes/Main.lean, line 4490](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LongGapsBetweenPrimes/Main.lean#L4490): “For all sufficiently large X, there are consecutive primes p < q with q at most X and q - p at least a fixed positive multiple of the improved long-gap scale.”
- [`LongGapsBetweenPrimes.short_translates`](https://leanpool.github.io/lean-pool/LeanPool/LongGapsBetweenPrimes/Main.html#LongGapsBetweenPrimes.short_translates) (lemma), declared in [LeanPool/LongGapsBetweenPrimes/Main.lean, line 3694](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LongGapsBetweenPrimes/Main.lean#L3694): “For all sufficiently large x, every sufficiently sparse subset S of an interval of length between x and x(log x)^2 has a translate b + Q(x)t + S consisting entirely of composite numbers, with 1 <= t <= exp x.”

## Project

- Authors: OpenAI.
- Source: *Improved Long Gaps Between Primes* by OpenAI, [https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/long_gaps.pdf](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/long_gaps.pdf).
- Project repository: [openai/LongGapsBetweenPrimes](https://github.com/openai/LongGapsBetweenPrimes), at commit [03a1190d](https://github.com/openai/LongGapsBetweenPrimes/tree/03a1190d0bc5502d9f54eeb60ad3e45e22b0df0b).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11N05.
- In Lean Pool: [LeanPool/LongGapsBetweenPrimes](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LongGapsBetweenPrimes), from the card [LeanPool/projects/long-gaps-between-primes.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/long-gaps-between-primes.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/long-gaps-between-primes.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/long-gaps-between-primes.yaml)
- [Lean Pool at 701389c0: LeanPool/LongGapsBetweenPrimes](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LongGapsBetweenPrimes)
