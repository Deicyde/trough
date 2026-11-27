---
declaration: theorem
origin: cited
lean: NoncommutativeAMGM.withoutReplacementMean_quadratic_bounds, NoncommutativeAMGM.withoutReplacementMean_rounded_lower, NoncommutativeAMGM.withoutReplacementMean_endpoint_lower, NoncommutativeAMGM.withoutReplacementMean_sine_bounds, NoncommutativeAMGM.withoutReplacementMean_cubic_bounds
statement: formalized
proof: formalized
---

# Noncommutative arithmetic–geometric mean bounds for ordered products

> Bounds the mean of products of m distinct real positive semidefinite matrices in Loewner order when their sum is at most nI. Proves the two-sided quadratic threshold, the original sine-node and cubic criteria, and the strengthened lower bounds, using harmonic decomposition and Chebyshev quadrature on Boolean slices.

*Quoted from the card [LeanPool/projects/noncommutative-amgm.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/noncommutative-amgm.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`NoncommutativeAMGM.withoutReplacementMean_quadratic_bounds`](https://leanpool.github.io/lean-pool/LeanPool/NoncommutativeAMGM/QuadraticBound.html#NoncommutativeAMGM.withoutReplacementMean_quadratic_bounds) (theorem; a main declaration), declared in [LeanPool/NoncommutativeAMGM/QuadraticBound.lean, line 101](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/NoncommutativeAMGM/QuadraticBound.lean#L101): “The mean lies between −I and I when n ≥ 2⌈m/2⌉².”
- [`NoncommutativeAMGM.withoutReplacementMean_rounded_lower`](https://leanpool.github.io/lean-pool/LeanPool/NoncommutativeAMGM/RoundedLowerBound.html#NoncommutativeAMGM.withoutReplacementMean_rounded_lower) (theorem; a main declaration), declared in [LeanPool/NoncommutativeAMGM/RoundedLowerBound.lean, line 60](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/NoncommutativeAMGM/RoundedLowerBound.lean#L60): “The mean is at least (−1 + 1/(2m))I when n ≥ 4m².”
- [`NoncommutativeAMGM.withoutReplacementMean_endpoint_lower`](https://leanpool.github.io/lean-pool/LeanPool/NoncommutativeAMGM/StrengthenedLowerBound.html#NoncommutativeAMGM.withoutReplacementMean_endpoint_lower) (theorem; a main declaration), declared in [LeanPool/NoncommutativeAMGM/StrengthenedLowerBound.lean, line 22](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/NoncommutativeAMGM/StrengthenedLowerBound.lean#L22): “Keeping the zero-slice endpoint yields the lower bound (−1 + 1/m)I at the quadratic threshold.”
- [`NoncommutativeAMGM.withoutReplacementMean_sine_bounds`](https://leanpool.github.io/lean-pool/LeanPool/NoncommutativeAMGM/SineBound.html#NoncommutativeAMGM.withoutReplacementMean_sine_bounds) (theorem; a main declaration), declared in [LeanPool/NoncommutativeAMGM/SineBound.lean, line 22](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/NoncommutativeAMGM/SineBound.lean#L22): “The paper's sine-node criterion implies the two-sided bound.”
- [`NoncommutativeAMGM.withoutReplacementMean_cubic_bounds`](https://leanpool.github.io/lean-pool/LeanPool/NoncommutativeAMGM/CubicBound.html#NoncommutativeAMGM.withoutReplacementMean_cubic_bounds) (theorem; a main declaration), declared in [LeanPool/NoncommutativeAMGM/CubicBound.lean, line 34](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/NoncommutativeAMGM/CubicBound.lean#L34): “The sufficient condition m³ ≤ 2n implies the two-sided bound.”

## Project

- Authors: Yimin Zhong.
- Source: *When the noncommutative AM-GM inequality holds*, [arXiv:2610.04874v1](https://arxiv.org/abs/2610.04874v1).
- Project repository: [lowrank/noncommutative-amgm-lean](https://github.com/lowrank/noncommutative-amgm-lean), at commit [26ecfa50](https://github.com/lowrank/noncommutative-amgm-lean/tree/26ecfa508fd375e3d8fae87a4526d0be5efd8b3f).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 15A45, 47A63, 41A55.
- In Lean Pool: [LeanPool/NoncommutativeAMGM](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/NoncommutativeAMGM), from the card [LeanPool/projects/noncommutative-amgm.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/noncommutative-amgm.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/noncommutative-amgm.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/noncommutative-amgm.yaml)
- [Lean Pool at bb99e52c: LeanPool/NoncommutativeAMGM](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/NoncommutativeAMGM)
