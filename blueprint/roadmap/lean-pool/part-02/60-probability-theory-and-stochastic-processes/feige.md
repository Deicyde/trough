---
declaration: theorem
origin: cited
lean: Feige.sharp_unit_slack_feige_complete
statement: formalized
proof: formalized
---

# Feige's sharp unit-slack inequality

> For small-universe probability spaces, proves the sharp fixed-dimensional unit-slack lower bound for sums of independent nonnegative random variables: if each coordinate has mean at most one, then the probability that the sum lies below its mean plus one is at least (n/(n+1))^n, and this constant is optimal. The supporting library formalizes the Vlassis--Thomas exact distribution-free calibration theorem, Grünbaum's centroid-halfspace inequality and sharp simplex example, and the normalized-exponential bridge joining them.

*Quoted from the card [LeanPool/projects/feige.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/feige.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Feige.sharp_unit_slack_feige_complete`](https://leanpool.github.io/lean-pool/LeanPool/Feige/MainTheorem.html#Feige.sharp_unit_slack_feige_complete) (theorem; a main declaration), declared in [LeanPool/Feige/MainTheorem.lean, line 26](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Feige/MainTheorem.lean#L26): “For every positive dimension n and every small-universe probability space, the sharp fixed-dimensional lower bound for the strict event that a sum of independent nonnegative random variables is below its expectation plus one is (n/(n+1))^n, and an explicit finite family proves optimality.”
- [`VlassisThomas.exactCalibration`](https://leanpool.github.io/lean-pool/LeanPool/Feige/VlassisThomas/Main.html#VlassisThomas.exactCalibration) (theorem), declared in [LeanPool/Feige/VlassisThomas/Main.lean, line 30](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Feige/VlassisThomas/Main.lean#L30): “On every small-universe probability space, the Dirichlet statistic used in the proof is super-uniform for every independent family of measurable, integrable, nonnegative random variables whose coordinate means are at most one.”
- [`Grunbaum.grunbaum_centroid_halfspace`](https://leanpool.github.io/lean-pool/LeanPool/Feige/Grunbaum/Main.html#Grunbaum.grunbaum_centroid_halfspace) (theorem), declared in [LeanPool/Feige/Grunbaum/Main.lean, line 187](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Feige/Grunbaum/Main.lean#L187): “Every closed halfspace containing the centroid of a positive-volume convex body in finite-dimensional Euclidean space contains at least the sharp Grünbaum fraction of the body's volume.”

## Project

- Authors: Zhengqing Zhou.
- Source: *Sharp Small-Deviation Inequalities for Sums of Independent Nonnegative Random Variables* by Weibo Fu, Yanjun Han, Guanyang Wang, Jun Yan, Peng Zhang, Zhengqing Zhou, [arXiv:2607.23980](https://arxiv.org/abs/2607.23980).
- Project repository: [pengzhang91/Feige](https://github.com/pengzhang91/Feige), at commit [98ab466e](https://github.com/pengzhang91/Feige/tree/98ab466e74280ae9d40622c19dc7f24f01b60864).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 60E15, 52A20.
- In Lean Pool: [LeanPool/Feige](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Feige), from the card [LeanPool/projects/feige.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/feige.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/feige.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/feige.yaml)
- [Lean Pool at 701389c0: LeanPool/Feige](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Feige)
