---
declaration: theorem
origin: cited
lean: BannaiBannaiStanton.bannai_bannai_stanton_bound
statement: formalized
proof: formalized
---

# The Bannai-Bannai-Stanton Bound on Distance Sets

> Formalizes the Bannai-Bannai-Stanton theorem: a distance set `S` in `ℝ^d` realizing `s` distinct distances has size at most `Nat.choose (d + s) s`. Follows the short polynomial-method proof of Petrov and Pohoata via a generalized Croot-Lev-Pach rank lemma, with auxiliary results on the diagonal linear-independence argument for polynomials, monomial counting of bounded degree, and a rank bound for sums of matrices.

*Quoted from the card [LeanPool/projects/bannai-bannai-stanton.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/bannai-bannai-stanton.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists one main result, with its informal statement quoted from the card. The scan finds its declaration in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`BannaiBannaiStanton.bannai_bannai_stanton_bound`](https://leanpool.github.io/lean-pool/LeanPool/BannaiBannaiStanton/BoundOnDistanceSet.html#BannaiBannaiStanton.bannai_bannai_stanton_bound) (theorem; a main declaration), declared in [LeanPool/BannaiBannaiStanton/BoundOnDistanceSet.lean, line 954](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/BannaiBannaiStanton/BoundOnDistanceSet.lean#L954): “A distance set `S` in Euclidean space `ℝ^d` realizing `s` distinct distances satisfies `S.encard ≤ Nat.choose (d + s) s`.”

## Project

- Authors: Antoine du Fresne von Hohenesche.
- Project repository: [AntoineduFresne/Bannai-Bannai-Stanton_Theorem](https://github.com/AntoineduFresne/Bannai-Bannai-Stanton_Theorem).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 52C10, 05B30.
- In Lean Pool: [LeanPool/BannaiBannaiStanton](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/BannaiBannaiStanton), from the card [LeanPool/projects/bannai-bannai-stanton.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/bannai-bannai-stanton.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/bannai-bannai-stanton.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/bannai-bannai-stanton.yaml)
- [Lean Pool at 701389c0: LeanPool/BannaiBannaiStanton](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/BannaiBannaiStanton)
