---
declaration: theorem
origin: cited
lean: Egyptian.eventuallyGreedy, Egyptian.asymptoticRigidity
statement: formalized
proof: formalized
---

# Eventually greedy best Egyptian underapproximations

> For every positive rational target, best strict Egyptian underapproximations with denominators at least two can be constructed from a common optimal prefix followed by a uniquely optimal greedy tail. Among nondecreasing reciprocal expansions with denominators at least two, matching the extremal asymptotic growth forces eventual agreement with an optimizing sequence.

*Quoted from the card [LeanPool/projects/egyptian-underapproximations.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/egyptian-underapproximations.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Egyptian.eventuallyGreedy`](https://leanpool.github.io/lean-pool/LeanPool/Egyptian.html#Egyptian.eventuallyGreedy) (theorem; a main declaration), declared in [LeanPool/Egyptian.lean, line 28](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Egyptian.lean#L28): “For each positive rational target and either the nondecreasing or strictly increasing convention, among strict reciprocal underapproximations with denominators at least two, a single maximizing prefix extends optimally at every later length with the uniquely maximizing greedy tail of its remainder.” Its source, as the card gives it: “Theorem 1”
- [`Egyptian.asymptoticRigidity`](https://leanpool.github.io/lean-pool/LeanPool/Egyptian.html#Egyptian.asymptoticRigidity) (theorem; a main declaration), declared in [LeanPool/Egyptian.lean, line 32](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Egyptian.lean#L32): “For every positive rational target a benchmark nondecreasing reciprocal expansion with denominators at least two exists. Each benchmark has a finite positive limit of the normalized denominator growth. Every nondecreasing reciprocal expansion of the same target with denominators at least two has a strictly smaller growth liminf or eventually agrees with that benchmark term by term.” Its source, as the card gives it: “Theorem 4”

## Project

- Authors: Vjekoslav Kovač, Quanyu Tang.
- Source: *Eventually greedy best Egyptian underapproximations of rational numbers via optimal control* by Vjekoslav Kovač, Quanyu Tang, [arXiv:2607.28387v2](https://arxiv.org/abs/2607.28387v2).
- Project repository: [VjekoKovac/lean-egyptian-underapproximations](https://github.com/VjekoKovac/lean-egyptian-underapproximations), at commit [8c7fbe08](https://github.com/VjekoKovac/lean-egyptian-underapproximations/tree/8c7fbe0847a828e29d7dde64e80fc8b70414478a).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11D68, 49N90.
- In Lean Pool: [LeanPool/Egyptian](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Egyptian), from the card [LeanPool/projects/egyptian-underapproximations.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/egyptian-underapproximations.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/egyptian-underapproximations.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/egyptian-underapproximations.yaml)
- [Lean Pool at bb99e52c: LeanPool/Egyptian](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/Egyptian)
