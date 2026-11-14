---
declaration: definition
origin: cited
lean: ProtocolSpec.ChallengeTree, ProtocolSpec.ChallengeTreeShape
statement: formalized
---

# Challenge Tree

A **challenge tree** for a protocol specification branches only at challenge rounds: a message round has one child, and a challenge round has one child per branch, labelled by the challenge sent on that branch. Every root-to-leaf path reads off one full transcript. A *shape* fixes the branching arity of each challenge round and a condition on the sibling challenges at each node.

## Depends on

- [Protocol Transcript](../part-01/def-transcript.md)

## Lean

Formalized as [`ProtocolSpec.ChallengeTree`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.ChallengeTree), [`ProtocolSpec.ChallengeTreeShape`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.ChallengeTreeShape).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 733](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L733)
