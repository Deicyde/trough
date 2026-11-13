---
declaration: theorem
origin: cited
lean: EuclideanJordan.frameBlock_isInternal
statement: formalized
proof: formalized
---

# Euclidean Jordan algebras and the frame Peirce decomposition

> The frame Peirce decomposition: relative to a Jordan frame, a Euclidean Jordan algebra is the internal direct sum of the blocks V_ij over unordered pairs of frame indices, and in finite dimension the diagonal blocks are lines, dim V_ii = 1 - the Faraut-Koranyi table entry. The frame is carried as data, so frame conjugacy is sidestepped and nothing here claims anything about the rank of J. Machine checked, not peer reviewed, no priority claim.

*Quoted from the card [LeanPool/projects/euclidean-jordan.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/euclidean-jordan.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`EuclideanJordan.frameBlock_isInternal`](https://leanpool.github.io/lean-pool/LeanPool/EuclideanJordan/EuclideanJordan/FramePeirce.html#EuclideanJordan.frameBlock_isInternal) (theorem; a main declaration), declared in [LeanPool/EuclideanJordan/EuclideanJordan/FramePeirce.lean, line 466](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/EuclideanJordan/EuclideanJordan/FramePeirce.lean#L466): “A Euclidean Jordan algebra is the internal direct sum of the Peirce blocks associated with a Jordan frame.”
- [`EuclideanJordan.finrank_frameBlock_diag`](https://leanpool.github.io/lean-pool/LeanPool/EuclideanJordan/EuclideanJordan/FramePeirceMul.html#EuclideanJordan.finrank_frameBlock_diag) (theorem), declared in [LeanPool/EuclideanJordan/EuclideanJordan/FramePeirceMul.lean, line 312](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/EuclideanJordan/EuclideanJordan/FramePeirceMul.lean#L312): “In finite dimension, every diagonal block of a Jordan frame has dimension one.”

## Project

- Authors: Bryan Ehrlich.
- Project repository: [ehrlich-b/euclidean-jordan](https://github.com/ehrlich-b/euclidean-jordan), at commit [a83407e4](https://github.com/ehrlich-b/euclidean-jordan/tree/a83407e4dbf73c77c31a2291c02f20b37a5ebbaf).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 17C20, 17C27, 17C37, 17C65, 17A15, 46L70.
- In Lean Pool: [LeanPool/EuclideanJordan](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/EuclideanJordan), from the card [LeanPool/projects/euclidean-jordan.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/euclidean-jordan.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/euclidean-jordan.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/euclidean-jordan.yaml)
- [Lean Pool at 701389c0: LeanPool/EuclideanJordan](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/EuclideanJordan)
