---
declaration: theorem
origin: cited
lean: fundamental_theorem, littlestone_characterization, pac_not_implies_online
statement: formalized
proof: formalized
---

# Formal Learning Theory Kernel

> Formalizes major equivalences and separations in PAC, VC, Gold-style, and online learning theory.

*Quoted from the card [LeanPool/projects/formal-learning-theory.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/formal-learning-theory.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 8 main results, each with its informal statement quoted from the card. The scan finds 8 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`vc_characterization`](https://leanpool.github.io/lean-pool/LeanPool/FormalLearningTheory/Theorem/PAC.html#vc_characterization) (theorem), declared in [LeanPool/FormalLearningTheory/Theorem/PAC.lean, line 125](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FormalLearningTheory/Theorem/PAC.lean#L125): “Characterizes PAC learnability by finite VC dimension.”
- [`fundamental_theorem`](https://leanpool.github.io/lean-pool/LeanPool/FormalLearningTheory/Theorem/PAC.html#fundamental_theorem) (theorem; a main declaration), declared in [LeanPool/FormalLearningTheory/Theorem/PAC.lean, line 280](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FormalLearningTheory/Theorem/PAC.lean#L280): “Bundles the central PAC, VC, compression, Rademacher, and sample-complexity equivalences.”
- [`fundamental_vc_compression`](https://leanpool.github.io/lean-pool/LeanPool/FormalLearningTheory/Theorem/PAC.html#fundamental_vc_compression) (theorem), declared in [LeanPool/FormalLearningTheory/Theorem/PAC.lean, line 238](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FormalLearningTheory/Theorem/PAC.lean#L238): “Relates finite VC dimension to compression with side information.”
- [`gold_theorem`](https://leanpool.github.io/lean-pool/LeanPool/FormalLearningTheory/Theorem/Gold.html#gold_theorem) (theorem), declared in [LeanPool/FormalLearningTheory/Theorem/Gold.lean, line 24](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FormalLearningTheory/Theorem/Gold.lean#L24): “States the Gold-style characterization for identification in the limit.”
- [`mind_change_characterization`](https://leanpool.github.io/lean-pool/LeanPool/FormalLearningTheory/Theorem/Gold.html#mind_change_characterization) (theorem), declared in [LeanPool/FormalLearningTheory/Theorem/Gold.lean, line 215](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FormalLearningTheory/Theorem/Gold.lean#L215): “Shows EX-learnability is equivalent to some learner having a finite mind-change ordinal on every text; since that ordinal is defined to be ω unless the learner converges to the target, this is a near-definitional restatement.”
- [`littlestone_characterization`](https://leanpool.github.io/lean-pool/LeanPool/FormalLearningTheory/Theorem/Online.html#littlestone_characterization) (theorem; a main declaration), declared in [LeanPool/FormalLearningTheory/Theorem/Online.lean, line 415](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FormalLearningTheory/Theorem/Online.lean#L415): “Characterizes online learnability by finite Littlestone dimension.”
- [`pac_not_implies_online`](https://leanpool.github.io/lean-pool/LeanPool/FormalLearningTheory/Theorem/Separation.html#pac_not_implies_online) (theorem; a main declaration), declared in [LeanPool/FormalLearningTheory/Theorem/Separation.lean, line 1072](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FormalLearningTheory/Theorem/Separation.lean#L1072): “Separates PAC learnability from online learnability.”
- [`ex_not_implies_pac`](https://leanpool.github.io/lean-pool/LeanPool/FormalLearningTheory/Theorem/Separation.html#ex_not_implies_pac) (theorem), declared in [LeanPool/FormalLearningTheory/Theorem/Separation.lean, line 1111](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FormalLearningTheory/Theorem/Separation.lean#L1111): “Separates explanatory learnability from PAC learnability.”

## Project

- Authors: Dhruv Gupta.
- Project repository: [Zetetic-Dhruv/formal-learning-theory-kernel](https://github.com/Zetetic-Dhruv/formal-learning-theory-kernel).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 68Q32, 68T05.
- In Lean Pool: [LeanPool/FormalLearningTheory](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FormalLearningTheory), from the card [LeanPool/projects/formal-learning-theory.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/formal-learning-theory.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/formal-learning-theory.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/formal-learning-theory.yaml)
- [Lean Pool at bb99e52c: LeanPool/FormalLearningTheory](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FormalLearningTheory)
