---
declaration: theorem
origin: cited
lean: BannaiBannaiStanton.bannai_bannai_stanton_bound
statement: formalized
proof: formalized
---

# The Bannai-Bannai-Stanton Bound on Distance Sets

> Formalizes the Bannai-Bannai-Stanton theorem: a distance set `S` in `ℝ^d` realizing `s` distinct distances has size at most `Nat.choose (d + s) s`. Follows the short polynomial-method proof of Petrov and Pohoata via a generalized Croot-Lev-Pach rank lemma, with auxiliary results on the diagonal linear-independence argument for polynomials, monomial counting of bounded degree, and a rank bound for sums of matrices.

*Quoted from the card [LeanPool/projects/bannai-bannai-stanton.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/bannai-bannai-stanton.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists one main result, with its informal statement quoted from the card. The scan finds its declaration in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`BannaiBannaiStanton.bannai_bannai_stanton_bound`](https://leanpool.github.io/lean-pool/LeanPool/BannaiBannaiStanton/BoundOnDistanceSet.html#BannaiBannaiStanton.bannai_bannai_stanton_bound) (theorem; a main declaration), declared in [LeanPool/BannaiBannaiStanton/BoundOnDistanceSet.lean, line 954](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BannaiBannaiStanton/BoundOnDistanceSet.lean#L954): “A distance set `S` in Euclidean space `ℝ^d` realizing `s` distinct distances satisfies `S.encard ≤ Nat.choose (d + s) s`.”

## Project

- Authors: Antoine du Fresne von Hohenesche.
- Project repository: [AntoineduFresne/Bannai-Bannai-Stanton_Theorem](https://github.com/AntoineduFresne/Bannai-Bannai-Stanton_Theorem).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 52C10, 05B30.
- In Lean Pool: [LeanPool/BannaiBannaiStanton](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BannaiBannaiStanton), from the card [LeanPool/projects/bannai-bannai-stanton.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/bannai-bannai-stanton.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/bannai-bannai-stanton.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/bannai-bannai-stanton.yaml)
- [Lean Pool at 2b205bf9: LeanPool/BannaiBannaiStanton](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BannaiBannaiStanton)
