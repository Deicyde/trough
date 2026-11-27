---
declaration: theorem
origin: cited
lean: WeightedHornCores.exists_positive_core
statement: formalized
proof: formalized
---

# Small unsatisfiable cores in weighted Horn formulas

> For finite weighted Horn formulas, bounds the number of distinct clauses needed for an unsatisfiable subset in terms of the minimum assignment loss and the weight of rules with two premises. The subset uses only positive weights. A unary chain shows the linear inverse-gap factor is necessary.

*Quoted from the card [LeanPool/projects/weighted-horn-cores.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/weighted-horn-cores.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`WeightedHornCores.exists_positive_core`](https://leanpool.github.io/lean-pool/LeanPool/WeightedHornCores/RealBound.html#WeightedHornCores.exists_positive_core) (theorem; a main declaration), declared in [LeanPool/WeightedHornCores/RealBound.lean, line 83](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/WeightedHornCores/RealBound.lean#L83): “Suppose the positive-headed rules have at most two premises, denials have at most a premises, and every assignment violates weight at least t > 0. If W is the total nonnegative weight and B is the weight of two-premise positive-headed rules, an unsatisfiable subset of positive weight clauses has size at most 1 + a(1 + W/(t ln 2)) 2^(1 + B/t).” Its source, as the card gives it: “Direct finite charging argument in CoreBound.lean and RealBound.lean.”
- [`WeightedHornCores.eq_unaryChain_of_unsatisfiable`](https://leanpool.github.io/lean-pool/LeanPool/WeightedHornCores/UnaryChain.html#WeightedHornCores.eq_unaryChain_of_unsatisfiable) (theorem), declared in [LeanPool/WeightedHornCores/UnaryChain.lean, line 100](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/WeightedHornCores/UnaryChain.lean#L100): “The unary implication chain with opposing endpoint units has no proper unsatisfiable subset.” Its source, as the card gives it: “Cut assignments in UnaryChain.lean.”
- [`WeightedHornCores.card_unaryChain`](https://leanpool.github.io/lean-pool/LeanPool/WeightedHornCores/UnaryChain.html#WeightedHornCores.card_unaryChain) (theorem), declared in [LeanPool/WeightedHornCores/UnaryChain.lean, line 39](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/WeightedHornCores/UnaryChain.lean#L39): “The unary chain with n links has n+2 distinct clauses.” Its source, as the card gives it: “UnaryChain.lean.”
- [`WeightedHornCores.branchingWeight_unaryChain`](https://leanpool.github.io/lean-pool/LeanPool/WeightedHornCores/UnaryChain.html#WeightedHornCores.branchingWeight_unaryChain) (theorem), declared in [LeanPool/WeightedHornCores/UnaryChain.lean, line 110](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/WeightedHornCores/UnaryChain.lean#L110): “The unary chain has branching weight zero for any weight function.” Its source, as the card gives it: “UnaryChain.lean.”
- [`WeightedHornCores.unaryChain_isLeast_violationWeight`](https://leanpool.github.io/lean-pool/LeanPool/WeightedHornCores/UnaryChain.html#WeightedHornCores.unaryChain_isLeast_violationWeight) (theorem), declared in [LeanPool/WeightedHornCores/UnaryChain.lean, line 119](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/WeightedHornCores/UnaryChain.lean#L119): “Under unit weights, the minimum violated weight over all assignments is one.” Its source, as the card gives it: “UnaryChain.lean.”

## Project

- Authors: Weighted Horn Cores contributors.
- Source: *Weighted Horn core bounds, direct Lean development*, [https://github.com/lockwo/lean-pool/tree/6b48b5f93366c7528bd1bc679341d9c953d1f412/LeanPool/WeightedHornCores](https://github.com/lockwo/lean-pool/tree/6b48b5f93366c7528bd1bc679341d9c953d1f412/LeanPool/WeightedHornCores).
- Project repository: [lockwo/lean-pool](https://github.com/lockwo/lean-pool), at commit [6b48b5f9](https://github.com/lockwo/lean-pool/tree/6b48b5f93366c7528bd1bc679341d9c953d1f412).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 03B05, 68Q25.
- In Lean Pool: [LeanPool/WeightedHornCores](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/WeightedHornCores), from the card [LeanPool/projects/weighted-horn-cores.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/weighted-horn-cores.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/weighted-horn-cores.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/weighted-horn-cores.yaml)
- [Lean Pool at bb99e52c: LeanPool/WeightedHornCores](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/WeightedHornCores)
