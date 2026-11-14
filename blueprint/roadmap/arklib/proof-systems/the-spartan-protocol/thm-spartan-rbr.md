---
declaration: theorem
origin: cited
lean: Spartan.rbrKnowledgeSoundnessWith, Spartan.challengeError
statement: formalized
---

# Round-by-round knowledge soundness

The Spartan verifier is fixed-prefix round-by-round knowledge sound for the original R1CS relation, with each challenge charged the error of its stage listed in Definition [Spartan PIOP](def-spartan-reduction.md). The state function is the composition of the stage state functions, retaining every earlier rejecting check.

## Depends on

- [Spartan PIOP](def-spartan-reduction.md)
- [Round-by-Round Knowledge Soundness](../the-sum-check-protocol/thm-sumcheck-rbr-knowledge-soundness-standard.md)

## Lean

Stated as [`Spartan.rbrKnowledgeSoundnessWith`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Spartan.rbrKnowledgeSoundnessWith), [`Spartan.challengeError`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Spartan.challengeError); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/spartan.tex, line 102](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/spartan.tex#L102)
