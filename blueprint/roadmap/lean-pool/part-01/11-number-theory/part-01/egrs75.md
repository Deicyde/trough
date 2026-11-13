---
declaration: theorem
origin: cited
lean: Egrs75.MuFinish.egrs_two_prime_mu, Egrs75.Finish.egrs_two_prime_finish
statement: formalized
proof: formalized
---

# The Erdős–Graham–Ruzsa–Straus two-prime theorem

> A complete machine-checked proof that for any two distinct odd primes p and q there are infinitely many n with binom(2n,n) coprime to pq, including the iterated carry-controlled digit-clearing step that Bloom and Croot defer to the 1975 paper, via a per-move lexicographic measure, an elementary staircase lemma, and a Dirichlet-approximation seed.

*Quoted from the card [LeanPool/projects/egrs75.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/egrs75.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Egrs75.MuFinish.egrs_two_prime_mu`](https://leanpool.github.io/lean-pool/LeanPool/Egrs75/MuFinish.html#Egrs75.MuFinish.egrs_two_prime_mu) (theorem; a main declaration), declared in [LeanPool/Egrs75/MuFinish.lean, line 445](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Egrs75/MuFinish.lean#L445): “Proves that for distinct odd primes p and q there are infinitely many n with p and q both not dividing the central binomial coefficient binom(2n,n), via the mu-measure descent.”
- [`Egrs75.Finish.egrs_two_prime_finish`](https://leanpool.github.io/lean-pool/LeanPool/Egrs75/BadPrefixRoute.html#Egrs75.Finish.egrs_two_prime_finish) (theorem; a main declaration), declared in [LeanPool/Egrs75/BadPrefixRoute.lean, line 435](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Egrs75/BadPrefixRoute.lean#L435): “Reassembles the same theorem via bad-bit-mask strong induction, with the low-case clearing discharged by Egrs75.MuFinish.egrs_clearing_low_mu.”
- [`Egrs75.not_dvd_centralBinom_iff_lowDigits`](https://leanpool.github.io/lean-pool/LeanPool/Egrs75/Defs.html#Egrs75.not_dvd_centralBinom_iff_lowDigits) (theorem), declared in [LeanPool/Egrs75/Defs.lean, line 86](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Egrs75/Defs.lean#L86): “The Kummer bridge, stating that an odd prime p does not divide binom(2n,n) exactly when every base-p digit of n is at most (p-1)/2.”
- [`Egrs75.MathlibAPI.irrational_log_div_log`](https://leanpool.github.io/lean-pool/LeanPool/Egrs75/LogIrrationality.html#Egrs75.MathlibAPI.irrational_log_div_log) (theorem), declared in [LeanPool/Egrs75/LogIrrationality.lean, line 96](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Egrs75/LogIrrationality.lean#L96): “Proves that the ratio of logarithms of two distinct primes is irrational.”

## Project

- Authors: Egor Lyfar.
- Source: *On the prime factors of (2n choose n)* by Paul Erdős, Ronald L. Graham, Imre Z. Ruzsa, Ernst G. Straus, [doi:10.1090/S0025-5718-1975-0369288-3](https://doi.org/10.1090/S0025-5718-1975-0369288-3).
- Project repository: [lyfar/egrs75-lean](https://github.com/lyfar/egrs75-lean).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11A63, 11B65.
- In Lean Pool: [LeanPool/Egrs75](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Egrs75), from the card [LeanPool/projects/egrs75.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/egrs75.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/egrs75.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/egrs75.yaml)
- [Lean Pool at 701389c0: LeanPool/Egrs75](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Egrs75)
