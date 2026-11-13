---
declaration: theorem
origin: cited
lean: ECRuntime.proposed_randomStakeCoupon_allDimensionPaperSharpCentered, ECRuntime.proposed_strictMonotoneRLS_allDimensionPaperSharpCentered
statement: formalized
proof: formalized
---

# Sharp coupon collection and randomized local search

> Proves the sharp additive minus-one-half correction for the mean time to collect uniformly sampled coupons from an independent uniform initial set, and for one-bit randomized local search on strictly coordinate-monotone Boolean fitness functions. The centering uses the average of the floor and ceiling half-dimension harmonic numbers, so the limit covers both parities. Develops finite Markov transitions, first-hitting-time expectations, geometric tail bounds, and the exact finite-dimensional mean formulas used in the proof.

*Quoted from the card [LeanPool/projects/ec-runtime-coupon-collector.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/ec-runtime-coupon-collector.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`ECRuntime.proposed_randomStakeCoupon_allDimensionPaperSharpCentered`](https://leanpool.github.io/lean-pool/LeanPool/ECRuntime/RandomStakeCouponSharpPaperCentered.html#ECRuntime.proposed_randomStakeCoupon_allDimensionPaperSharpCentered) (theorem; a main declaration), declared in [LeanPool/ECRuntime/RandomStakeCouponSharpPaperCentered.lean, line 28](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ECRuntime/RandomStakeCouponSharpPaperCentered.lean#L28): “For n coupon types, with each coupon independently present initially with probability one half, the expected remaining number of independent uniform coupon draws minus n times the average of H_floor(n/2) and H_ceil(n/2) converges to minus one half as n tends to infinity.” Its source, as the card gives it: “Doerr and Doerr, Collecting Coupons with Random Initial Stake, Theorem 1.”
- [`ECRuntime.proposed_strictMonotoneRLS_allDimensionPaperSharpCentered`](https://leanpool.github.io/lean-pool/LeanPool/ECRuntime/RLSAllDimensionPaperSharpCentered.html#ECRuntime.proposed_strictMonotoneRLS_allDimensionPaperSharpCentered) (theorem; a main declaration), declared in [LeanPool/ECRuntime/RLSAllDimensionPaperSharpCentered.lean, line 55](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ECRuntime/RLSAllDimensionPaperSharpCentered.lean#L55): “For any family of strictly coordinate-monotone real-valued Boolean fitness functions, the uniform-start mean number of one-bit elitist RLS mutation iterations to reach the all-one string, excluding the initial evaluation, has the same all-dimension additive minus-one-half correction.” Its source, as the card gives it: “Doerr and Doerr, Collecting Coupons with Random Initial Stake, Theorem 3 (RLS corollary).”

## Project

- Authors: Jiri Kovar, Jakub Kudela.
- Source: *Collecting Coupons with Random Initial Stake* by Benjamin Doerr, Carola Doerr, [arXiv:1308.6384](https://arxiv.org/abs/1308.6384).
- Project repository: [UAI-VUT-Brno/Runtime-analysis-of-evolutionary-computation-algorithms](https://github.com/UAI-VUT-Brno/Runtime-analysis-of-evolutionary-computation-algorithms), at commit [a0e34dce](https://github.com/UAI-VUT-Brno/Runtime-analysis-of-evolutionary-computation-algorithms/tree/a0e34dce6395d48d0fb9c7b8850088973f503d8b).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 60J10, 60G40, 68Q25, 68W20.
- In Lean Pool: [LeanPool/ECRuntime](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ECRuntime), from the card [LeanPool/projects/ec-runtime-coupon-collector.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/ec-runtime-coupon-collector.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/ec-runtime-coupon-collector.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/ec-runtime-coupon-collector.yaml)
- [Lean Pool at 701389c0: LeanPool/ECRuntime](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ECRuntime)
