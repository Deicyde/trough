---
declaration: theorem
origin: cited
lean: Verifier.rbrKnowledgeSoundness_implies_rbrSoundness
statement: formalized
---

# RBR Knowledge Soundness Implies RBR Soundness

Round-by-round knowledge soundness for relations $R_{\text{in}}, R_{\text{out}}$ with error function $\epsilon$ implies round-by-round soundness for the induced languages (the statements that have some valid witness) with the same error function $\epsilon$.

## Depends on

- [Round-by-Round Knowledge Soundness](def-round-by-round-knowledge-soundness.md)
- [Round-by-Round Soundness](def-round-by-round-soundness.md)

## Lean

Stated as [`Verifier.rbrKnowledgeSoundness_implies_rbrSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.rbrKnowledgeSoundness_implies_rbrSoundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 801](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L801)
