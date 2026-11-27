---
declaration: theorem
origin: cited
lean: OrderMaintenance.Impl.theoremAB_word, OrderMaintenance.Impl.theoremAB_flat_word, OrderMaintenance.Zeroing.zeroing
statement: formalized
proof: formalized
---

# Verified worst-case constant-step order maintenance

> Verifies an order-maintenance program against a list specification, with a constant worst-case instruction bound and logarithmic word width in the number of operations. Includes fixed-width and preallocated allocation-free RAM variants, a zeroing-game bound, and reusable machine cost semantics.

*Quoted from the card [LeanPool/projects/order-maintenance.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/order-maintenance.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`OrderMaintenance.Impl.theoremAB_word`](https://leanpool.github.io/lean-pool/LeanPool/OrderMaintenance/Impl/PeakWord.html#OrderMaintenance.Impl.theoremAB_word) (theorem; a main declaration), declared in [LeanPool/OrderMaintenance/Impl/PeakWord.lean, line 354](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/OrderMaintenance/Impl/PeakWord.lean#L354): “For every parameter 4 ≤ K_B < 2^512, every valid finite operation trace and sufficiently wide fixed words, the RAM program returns the list specification answers and each operation takes at most opB K_B steps, independent of the trace length and number of live elements. Word width grows logarithmically with the number of operations.”
- [`OrderMaintenance.Impl.theoremAB_flat_word`](https://leanpool.github.io/lean-pool/LeanPool/OrderMaintenance/Impl/FlatRun.html#OrderMaintenance.Impl.theoremAB_flat_word) (theorem; a main declaration), declared in [LeanPool/OrderMaintenance/Impl/FlatRun.lean, line 286](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/OrderMaintenance/Impl/FlatRun.lean#L286): “The translated program has no allocation instructions and satisfies the same specification with at most five times the operation-step bound, on sufficiently large preallocated zero-filled memory and sufficiently wide fixed words.”
- [`OrderMaintenance.Zeroing.zeroing`](https://leanpool.github.io/lean-pool/LeanPool/OrderMaintenance/Proof/Cost/Zeroing.html#OrderMaintenance.Zeroing.zeroing) (theorem; a main declaration), declared in [LeanPool/OrderMaintenance/Proof/Cost/Zeroing.lean, line 194](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/OrderMaintenance/Proof/Cost/Zeroing.lean#L194): “In the zeroing game starting from zero, resetting a maximal coordinate before adding total nonnegative mass at most R bounds every coordinate by R times one plus the (n-1)st harmonic number.”

## Project

- Authors: Denis Firsov.
- Source: *Order Maintenance in Worst-Case Constant Time, Verified* by Denis Firsov, [arXiv:2610.38616](https://arxiv.org/abs/2610.38616).
- Project repository: [dfirsov/order_maintenance](https://github.com/dfirsov/order_maintenance), at commit [312b7b7d](https://github.com/dfirsov/order_maintenance/tree/312b7b7d0686550ce7106fff1f6a47acb3e72866).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 68P05, 68Q60.
- In Lean Pool: [LeanPool/OrderMaintenance](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/OrderMaintenance), from the card [LeanPool/projects/order-maintenance.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/order-maintenance.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/order-maintenance.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/order-maintenance.yaml)
- [Lean Pool at bb99e52c: LeanPool/OrderMaintenance](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/OrderMaintenance)
