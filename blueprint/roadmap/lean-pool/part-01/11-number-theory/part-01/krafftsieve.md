---
declaration: theorem
origin: cited
lean: KrafftSieve.mu_min_lt_one_implies_tpc
statement: formalized
proof: formalized
---

# A Conditional Sieve Criterion for Twin Primes via Krafft Geometry

> Introduces an original conditional sieve criterion for the Twin Prime Conjecture. Using a centered modular alignment (termed the Krafft alignment), proves that if the Rayleigh-Ritz quotient over the orthogonal unit sphere satisfies muMin < 1, then a twin prime pair must exist in the corresponding interval.

*Quoted from the card [LeanPool/projects/krafftsieve.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/krafftsieve.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`KrafftSieve.krafft_sieve_guarantee_with_mu_min`](https://leanpool.github.io/lean-pool/LeanPool/KrafftSieve/OptimalWeights.html#KrafftSieve.krafft_sieve_guarantee_with_mu_min) (theorem), declared in [LeanPool/KrafftSieve/OptimalWeights.lean, line 730](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/KrafftSieve/OptimalWeights.lean#L730): “Proves that muMin n < 1 is a sufficient condition for the existence of a twin prime pair in the corresponding interval.”
- [`KrafftSieve.mu_min_lt_one_implies_tpc`](https://leanpool.github.io/lean-pool/LeanPool/KrafftSieve/MainTheorem.html#KrafftSieve.mu_min_lt_one_implies_tpc) (theorem; a main declaration), declared in [LeanPool/KrafftSieve/MainTheorem.lean, line 28](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/KrafftSieve/MainTheorem.lean#L28): “If there are infinitely many intervals where the optimal multidimensional weight achieves a ratio strictly less than 1, then there are infinitely many twin primes. This is a conditional reduction; the hypothesis muMin n < 1 is not established here for any n.”

## Project

- Authors: Fernando Portela.
- Source: [doi:10.5281/zenodo.19763833](https://doi.org/10.5281/zenodo.19763833).
- Project repository: [ElNando888/KrafftSieve](https://github.com/ElNando888/KrafftSieve).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11N05, 11N35.
- In Lean Pool: [LeanPool/KrafftSieve](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/KrafftSieve), from the card [LeanPool/projects/krafftsieve.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/krafftsieve.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/krafftsieve.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/krafftsieve.yaml)
- [Lean Pool at 701389c0: LeanPool/KrafftSieve](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/KrafftSieve)
