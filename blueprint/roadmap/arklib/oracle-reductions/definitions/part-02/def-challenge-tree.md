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

- [ArkLib blueprint: oracle_reductions/defs.tex, line 733](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/defs.tex#L733)
