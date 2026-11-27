---
declaration: theorem
origin: cited
lean: DynamicMcs.Proofs.common_order_extends_prefix, DynamicMcs.Proofs.insert_break_iff_old, DynamicMcs.Proofs.exec_insert_update_eq_mcsOrder, DynamicMcs.Proofs.exec_delete_update_eq_mcsOrder, DynamicMcs.Proofs.exec_insert_cost_le, DynamicMcs.Proofs.exec_delete_cost_of_no_break
statement: formalized
proof: formalized
---

# Dynamic maximum cardinality search

> Formalizes stability of maximum-cardinality search orderings under one-sided edge updates. For the canonical least-index tie break, it verifies exactly where a single edge update can invalidate an old choice and proves that a Boolean-adjacency probe-and-repair implementation gives the same ordering as greedy recomputation. Instrumented implementations count legality tests and greedy selections in a unit-cost model.

*Quoted from the card [LeanPool/projects/dynamic-mcs.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/dynamic-mcs.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`DynamicMcs.Proofs.common_order_extends_prefix`](https://leanpool.github.io/lean-pool/LeanPool/DynamicMcs/Stability.html#DynamicMcs.Proofs.common_order_extends_prefix) (theorem; a main declaration), declared in [LeanPool/DynamicMcs/Stability.lean, line 100](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DynamicMcs/Stability.lean#L100): “If the unchosen neighbor counts stay unchanged or increase by one along each proper common prefix, every common prefix extends to a common ordering.”
- [`DynamicMcs.Proofs.insert_break_iff_old`](https://leanpool.github.io/lean-pool/LeanPool/DynamicMcs/Correctness.html#DynamicMcs.Proofs.insert_break_iff_old) (theorem; a main declaration), declared in [LeanPool/DynamicMcs/Correctness.lean, line 206](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DynamicMcs/Correctness.lean#L206): “At a position strictly between the inserted edge's endpoints, the old choice is invalid exactly when the later endpoint previously tied it on the neighbor count, or trailed by one and has the smaller index.”
- [`DynamicMcs.Proofs.exec_insert_update_eq_mcsOrder`](https://leanpool.github.io/lean-pool/LeanPool/DynamicMcs/ExecUpdate.html#DynamicMcs.Proofs.exec_insert_update_eq_mcsOrder) (theorem; a main declaration), declared in [LeanPool/DynamicMcs/ExecUpdate.lean, line 122](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DynamicMcs/ExecUpdate.lean#L122): “On symmetric loop-free adjacency matrices related by a single insertion, updating the old canonical ordering by the executable probe and repair agrees with greedy recomputation.”
- [`DynamicMcs.Proofs.exec_delete_update_eq_mcsOrder`](https://leanpool.github.io/lean-pool/LeanPool/DynamicMcs/ExecUpdate.html#DynamicMcs.Proofs.exec_delete_update_eq_mcsOrder) (theorem; a main declaration), declared in [LeanPool/DynamicMcs/ExecUpdate.lean, line 177](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DynamicMcs/ExecUpdate.lean#L177): “The analogous executable deletion update also agrees with greedy recomputation on the updated adjacency matrix.”
- [`DynamicMcs.Proofs.exec_insert_cost_le`](https://leanpool.github.io/lean-pool/LeanPool/DynamicMcs/ExecUpdate.html#DynamicMcs.Proofs.exec_insert_cost_le) (theorem; a main declaration), declared in [LeanPool/DynamicMcs/ExecUpdate.lean, line 337](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DynamicMcs/ExecUpdate.lean#L337): “When the old ordering lists as many entries as the adjacency matrix has rows, the total operation count for insertion is at most the row count.”
- [`DynamicMcs.Proofs.exec_delete_cost_of_no_break`](https://leanpool.github.io/lean-pool/LeanPool/DynamicMcs/ExecUpdate.html#DynamicMcs.Proofs.exec_delete_cost_of_no_break) (theorem; a main declaration), declared in [LeanPool/DynamicMcs/ExecUpdate.lean, line 317](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DynamicMcs/ExecUpdate.lean#L317): “When the deletion probe returns no break, the instrumented update takes one counted operation.”

## Project

- Authors: Md Thoriqul Islam Thonmay, Gregory Morse.
- Source: *How rigid is maximum cardinality search? Stability and locality of MCS orderings under edge updates, verified in Lean*, [arXiv:2611.18369](https://arxiv.org/abs/2611.18369).
- Project repository: [thonmay/mcs-lean](https://github.com/thonmay/mcs-lean), at commit [0d0ddffb](https://github.com/thonmay/mcs-lean/tree/0d0ddffbcef5817c50a073a350428edd2da5bfb5).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 05C85, 68W40.
- In Lean Pool: [LeanPool/DynamicMcs](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DynamicMcs), from the card [LeanPool/projects/dynamic-mcs.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/dynamic-mcs.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/dynamic-mcs.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/dynamic-mcs.yaml)
- [Lean Pool at bb99e52c: LeanPool/DynamicMcs](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DynamicMcs)
