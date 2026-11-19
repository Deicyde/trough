---
declaration: theorem
origin: cited
lean: Verifier.GuardedForm.knowledgeSoundness_of_rbrKnowledgeSoundness
statement: formalized
---

# RBR Knowledge Soundness Implies Knowledge Soundness

For a verifier with a guarded form, round-by-round knowledge soundness with error function $\epsilon$ implies knowledge soundness with error $\sum_i \epsilon(i)$, where the sum is over all challenge rounds $i$. The extractor folds the round-by-round extractor backward along the transcript.

## Depends on

- [Round-by-Round Knowledge Soundness](def-round-by-round-knowledge-soundness.md)
- [Knowledge Soundness](def-knowledge-soundness.md)
- [Guarded Verifier](def-guarded-verifier.md)

## Lean

Stated as [`Verifier.GuardedForm.knowledgeSoundness_of_rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.GuardedForm.knowledgeSoundness_of_rbrKnowledgeSoundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 825](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L825)
