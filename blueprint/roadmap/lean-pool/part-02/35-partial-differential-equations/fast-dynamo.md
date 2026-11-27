---
declaration: theorem
origin: cited
lean: FastDynamo.challenge_statement, FastDynamo.main_theorem_strengthened, FastDynamo.tendstoUniformlyOn_resistiveEvolution_mainIdealGroup
statement: formalized
proof: formalized
---

# A fast dynamo with zero topological entropy

> Constructs a Lipschitz divergence-free velocity on the flat three-torus that drives uniform exponential growth in the resistive kinematic induction equation at small positive diffusivity. The particle flow has zero topological entropy and the ideal induction group has zero exponential growth rate.

*Quoted from the card [LeanPool/projects/fast-dynamo.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/fast-dynamo.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`FastDynamo.challenge_statement`](https://leanpool.github.io/lean-pool/LeanPool/FastDynamo/Palomar/Main.html#FastDynamo.challenge_statement) (theorem; a main declaration), declared in [LeanPool/FastDynamo/Palomar/Main.lean, line 138](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FastDynamo/Palomar/Main.lean#L138): “A single velocity yields a uniform positive resistive growth rate with a growing real solution, a zero-entropy particle flow and a unique ideal solution group of zero exponential growth rate.”
- [`FastDynamo.main_theorem_strengthened`](https://leanpool.github.io/lean-pool/LeanPool/FastDynamo/MainTheoremStrengthened.html#FastDynamo.main_theorem_strengthened) (theorem; a main declaration), declared in [LeanPool/FastDynamo/MainTheoremStrengthened.lean, line 553](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FastDynamo/MainTheoremStrengthened.lean#L553): “The construction supplies explicit velocity regularity, spectral and solution witnesses.”
- [`FastDynamo.tendstoUniformlyOn_resistiveEvolution_mainIdealGroup`](https://leanpool.github.io/lean-pool/LeanPool/FastDynamo/Dynamics/VanishingDiffusivity/Limit.html#FastDynamo.tendstoUniformlyOn_resistiveEvolution_mainIdealGroup) (theorem; a main declaration), declared in [LeanPool/FastDynamo/Dynamics/VanishingDiffusivity/Limit.lean, line 429](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FastDynamo/Dynamics/VanishingDiffusivity/Limit.lean#L429): “For each fixed divergence-free L² datum, as positive diffusivity tends to zero, the resistive evolution converges in L² to the ideal group uniformly on bounded intervals of nonnegative time.”

## Project

- Authors: Lukas Niebel.
- Source: *A fast dynamo with zero topological entropy*, [arXiv:2608.02586v3](https://arxiv.org/abs/2608.02586v3).
- Project repository: [lukasniebel/fast_dynamo_lean](https://github.com/lukasniebel/fast_dynamo_lean), at commit [f2e17cdd](https://github.com/lukasniebel/fast_dynamo_lean/tree/f2e17cdd0f814af1bd9c0a6ce10320b216ed4fe0).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 35Q35, 76W05, 37B40.
- In Lean Pool: [LeanPool/FastDynamo](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FastDynamo), from the card [LeanPool/projects/fast-dynamo.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/fast-dynamo.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/fast-dynamo.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/fast-dynamo.yaml)
- [Lean Pool at bb99e52c: LeanPool/FastDynamo](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FastDynamo)
