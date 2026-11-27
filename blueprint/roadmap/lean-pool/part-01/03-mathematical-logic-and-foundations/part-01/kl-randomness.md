---
declaration: theorem
origin: cited
lean: Klr.martinLofRandom_ssubset_kolmogorovLovelandRandom, Klr.exists_not_martinLofRandom_no_partial_rational_success, Klr.binary_random_ssubset_baseFour_random
statement: formalized
proof: formalized
---

# Kolmogorov–Loveland and Martin–Löf randomness

> Formalizes the separation of Martin–Löf randomness from Kolmogorov–Loveland randomness for binary sequences under Liu and Meng's convention of total fresh scans and uniformly computable real capital. It also proves that randomness for base-four strategies need not imply binary Kolmogorov–Loveland randomness under adjacent-bit grouping. The proof develops effective open tests, methods for conditioning on parity constraints, and success-preserving transformations of betting strategies.

*Quoted from the card [LeanPool/projects/kl-randomness.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/kl-randomness.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Klr.martinLofRandom_ssubset_kolmogorovLovelandRandom`](https://leanpool.github.io/lean-pool/LeanPool/KLRandomness/Separation.html#Klr.martinLofRandom_ssubset_kolmogorovLovelandRandom) (theorem; a main declaration), declared in [LeanPool/KLRandomness/Separation.lean, line 59](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/KLRandomness/Separation.lean#L59): “The binary sequences avoiding all Martin–Löf tests form a proper subset of those on which every total fresh computable betting strategy with nonnegative fair and uniformly computable real capital has bounded capital.”
- [`Klr.exists_not_martinLofRandom_no_partial_rational_success`](https://leanpool.github.io/lean-pool/LeanPool/KLRandomness/Separation.html#Klr.exists_not_martinLofRandom_no_partial_rational_success) (theorem; a main declaration), declared in [LeanPool/KLRandomness/Separation.lean, line 43](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/KLRandomness/Separation.lean#L43): “Some binary sequence fails a Martin–Löf test while every infinite fresh run of a partial rational-wager program on that sequence has bounded capital.”
- [`Klr.binary_random_ssubset_baseFour_random`](https://leanpool.github.io/lean-pool/LeanPool/KLRandomness/BaseInvariance.html#Klr.binary_random_ssubset_baseFour_random) (theorem; a main declaration), declared in [LeanPool/KLRandomness/BaseInvariance.lean, line 41](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/KLRandomness/BaseInvariance.lean#L41): “The binary Kolmogorov–Loveland random sequences form a proper subset of the sequences whose adjacent-bit pairs are Kolmogorov–Loveland random digits in base four, with total computable-real strategies in both bases. This is an additional upstream result from pull request 3, separate from the result registered with Palomar.”

## Project

- Authors: Bjørn Kjos-Hanssen.
- Source: *Separating Kolmogorov–Loveland randomness from Martin–Löf randomness*, [arXiv:2611.31004v1](https://arxiv.org/abs/2611.31004v1).
- Project repository: [bjoernkjoshanssen/klr](https://github.com/bjoernkjoshanssen/klr), at commit [81f5fef2](https://github.com/bjoernkjoshanssen/klr/tree/81f5fef2de3142aad714624033a5aa4f12031a6b).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 03D32, 03B35.
- In Lean Pool: [LeanPool/KLRandomness](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/KLRandomness), from the card [LeanPool/projects/kl-randomness.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/kl-randomness.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/kl-randomness.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/kl-randomness.yaml)
- [Lean Pool at bb99e52c: LeanPool/KLRandomness](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/KLRandomness)
