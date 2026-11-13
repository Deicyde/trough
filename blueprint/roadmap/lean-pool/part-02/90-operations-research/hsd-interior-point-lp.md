---
declaration: theorem
origin: cited
lean: HSDInteriorPointLP.YTM_fixed_local_theory_from_paper
statement: formalized
proof: formalized
---

# Homogeneous self-dual interior-point method for linear programming

> Formalizes a homogeneous self-dual interior-point method for linear programming, including primal-dual data, Newton block solvability from full row rank, fixed Ye-Todd-Mizuno predictor/corrector local estimates, contraction bounds, and logarithmic stopping certificates for generated iterates.

*Quoted from the card [LeanPool/projects/hsd-interior-point-lp.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/hsd-interior-point-lp.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`HSDInteriorPointLP.YTM_fixed_local_theory_from_paper`](https://leanpool.github.io/lean-pool/LeanPool/HSDInteriorPointLP/FixedYTMTheory.html#HSDInteriorPointLP.YTM_fixed_local_theory_from_paper) (theorem; a main declaration), declared in [LeanPool/HSDInteriorPointLP/FixedYTMTheory.lean, line 1007](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HSDInteriorPointLP/FixedYTMTheory.lean#L1007): “Packages the fixed Ye-Todd-Mizuno local theory, combining predictor and corrector estimates for the tight and wide central neighborhoods.” Its source, as the card gives it: “Y. Ye, M. J. Todd, and S. Mizuno, An O(√nL)-iteration homogeneous and self-dual linear programming algorithm, Mathematics of Operations Research 19(1):53-67, 1994.”
- [`HSDInteriorPointLP.HSDGeneratedAlgorithm.gap_stop_even_at_logPairBound`](https://leanpool.github.io/lean-pool/LeanPool/HSDInteriorPointLP/GeneratedConvergence.html#HSDInteriorPointLP.HSDGeneratedAlgorithm.gap_stop_even_at_logPairBound) (theorem), declared in [LeanPool/HSDInteriorPointLP/GeneratedConvergence.lean, line 253](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HSDInteriorPointLP/GeneratedConvergence.lean#L253): “Proves that the generated even iterate satisfies the gap stopping test at the logarithmic pair bound.”
- [`HSDInteriorPointLP.HSDGeneratedAlgorithm.mu_stop_even_at_logPairBound`](https://leanpool.github.io/lean-pool/LeanPool/HSDInteriorPointLP/GeneratedConvergence.html#HSDInteriorPointLP.HSDGeneratedAlgorithm.mu_stop_even_at_logPairBound) (theorem), declared in [LeanPool/HSDInteriorPointLP/GeneratedConvergence.lean, line 279](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HSDInteriorPointLP/GeneratedConvergence.lean#L279): “Proves that the generated even iterate satisfies the duality-measure stopping test at the scaled logarithmic pair bound.”
- [`HSDInteriorPointLP.HLP_newton_block_system_solvable_from_full_row_rank`](https://leanpool.github.io/lean-pool/LeanPool/HSDInteriorPointLP/NewtonSystem.html#HSDInteriorPointLP.HLP_newton_block_system_solvable_from_full_row_rank) (theorem), declared in [LeanPool/HSDInteriorPointLP/NewtonSystem.lean, line 808](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HSDInteriorPointLP/NewtonSystem.lean#L808): “Shows solvability of the Newton block system from the full-row-rank assumption through finite-dimensional linear algebra.”
- [`HSDInteriorPointLP.YTM_contraction_power_le_exp`](https://leanpool.github.io/lean-pool/LeanPool/HSDInteriorPointLP/FixedYTMTheory.html#HSDInteriorPointLP.YTM_contraction_power_le_exp) (theorem), declared in [LeanPool/HSDInteriorPointLP/FixedYTMTheory.lean, line 1170](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HSDInteriorPointLP/FixedYTMTheory.lean#L1170): “Bounds the fixed YTM contraction power by the corresponding exponential decay estimate.”

## Project

- Authors: Makoto Yamashita.
- Source: *An O(√nL)-iteration homogeneous and self-dual linear programming algorithm* by Yinyu Ye, Michael J. Todd, Shinji Mizuno, [doi:10.1287/moor.19.1.53](https://doi.org/10.1287/moor.19.1.53).
- Project repository: [makoto-yamashita/proof-on-a-homogeneous-self-dual-interior-point-method-for-linear-programming](https://github.com/makoto-yamashita/proof-on-a-homogeneous-self-dual-interior-point-method-for-linear-programming).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 90C05, 90C51.
- In Lean Pool: [LeanPool/HSDInteriorPointLP](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HSDInteriorPointLP), from the card [LeanPool/projects/hsd-interior-point-lp.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/hsd-interior-point-lp.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/hsd-interior-point-lp.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/hsd-interior-point-lp.yaml)
- [Lean Pool at 701389c0: LeanPool/HSDInteriorPointLP](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HSDInteriorPointLP)
