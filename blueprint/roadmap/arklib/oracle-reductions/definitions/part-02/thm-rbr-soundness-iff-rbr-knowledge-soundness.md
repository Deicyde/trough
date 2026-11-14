---
declaration: theorem
origin: cited
lean: Verifier.rbrSoundness_iff_rbrKnowledgeSoundness, Verifier.forall_rbrSoundness_iff_rbrKnowledgeSoundness_iff
statement: formalized
---

# RBR Soundness and RBR Knowledge Soundness Coincide

If the input witness type is nonempty, round-by-round soundness of the induced languages with error function $\epsilon$ is equivalent to round-by-round knowledge soundness with the same $\epsilon$. More precisely, this equivalence holds for all relations and all error functions if and only if the input witness type is nonempty, or no input statement, full transcript and output witness exist together. The condition depends neither on the verifier nor on the error. The equivalence uses an unconstrained round-by-round extractor.

## Depends on

- [Round-by-Round Knowledge Soundness](def-round-by-round-knowledge-soundness.md)
- [Round-by-Round Soundness](def-round-by-round-soundness.md)

## Lean

Stated as [`Verifier.rbrSoundness_iff_rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.rbrSoundness_iff_rbrKnowledgeSoundness), [`Verifier.forall_rbrSoundness_iff_rbrKnowledgeSoundness_iff`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.forall_rbrSoundness_iff_rbrKnowledgeSoundness_iff); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 811](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L811)
