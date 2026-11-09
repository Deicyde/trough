---
declaration: theorem
origin: cited
lean: LeanPool.SingleCopyStabilizer.ExactLearningTheorem.exact_learning
statement: formalized
proof: formalized
---

# Exact adaptive single-copy stabilizer learning

> Exact recovery of pure qubit stabilizer states from adaptive single-copy measurements, with explicit confidence, copy and elementary gate upper bounds.

*Quoted from the card [LeanPool/projects/single-copy-stabilizer-learning.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/single-copy-stabilizer-learning.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`LeanPool.SingleCopyStabilizer.ExactLearningTheorem.exact_learning`](https://leanpool.github.io/lean-pool/LeanPool/SingleCopyStabilizer/ExactLearningTheorem.html#LeanPool.SingleCopyStabilizer.ExactLearningTheorem.exact_learning) (theorem; a main declaration), declared in [LeanPool/SingleCopyStabilizer/ExactLearningTheorem.lean, line 43](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SingleCopyStabilizer/ExactLearningTheorem.lean#L43): “For every normalized pure qubit stabilizer state and failure parameter 0 < delta <= 1, the physical learner returns a finite circuit and readout that decode to the input up to global phase with probability at least 1 - delta. Every supported execution uses exactly 2T + 1 copies and at most (n + 1)T^2 elementary gate applications at the stated round budget T.”
- [`LeanPool.SingleCopyStabilizer.ExactLearningTheorem.exact_learning_copy_bound_linear`](https://leanpool.github.io/lean-pool/LeanPool/SingleCopyStabilizer/ExactLearningTheorem.html#LeanPool.SingleCopyStabilizer.ExactLearningTheorem.exact_learning_copy_bound_linear) (theorem), declared in [LeanPool/SingleCopyStabilizer/ExactLearningTheorem.lean, line 78](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SingleCopyStabilizer/ExactLearningTheorem.lean#L78): “For n >= 1, every supported output at the confidence budget consumes fewer than 136(n + log(1 / delta)) input copies.”

## Project

- Authors: Antonio Anna Mele.
- Source: [arXiv:2610.02031](https://arxiv.org/abs/2610.02031).
- Project repository: [AntMele/single-copy-stabilizer-learning-lean](https://github.com/AntMele/single-copy-stabilizer-learning-lean).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 81P68, 68Q32, 81P45.
- In Lean Pool: [LeanPool/SingleCopyStabilizer](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SingleCopyStabilizer), from the card [LeanPool/projects/single-copy-stabilizer-learning.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/single-copy-stabilizer-learning.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/single-copy-stabilizer-learning.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/single-copy-stabilizer-learning.yaml)
- [Lean Pool at 2b205bf9: LeanPool/SingleCopyStabilizer](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SingleCopyStabilizer)
