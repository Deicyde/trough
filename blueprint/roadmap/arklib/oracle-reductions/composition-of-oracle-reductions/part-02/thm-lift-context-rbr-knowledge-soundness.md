---
declaration: theorem
origin: cited
lean: Verifier.liftContext_rbrKnowledgeSoundness, Verifier.liftContext_rbrKnowledgeSoundnessWith
statement: formalized
---

# RBR Knowledge Soundness Preservation under Context Lifting

If a verifier is round-by-round knowledge sound with error $\epsilon$ and the extractor lens is knowledge-soundness-preserving, then the lifted verifier is round-by-round knowledge sound with the same error at every challenge. The named form keeps the lifted extractor and knowledge state function explicit.

## Depends on

- [Round-by-Round Knowledge Soundness](../../definitions/part-02/def-round-by-round-knowledge-soundness.md)
- [Verifier Context Lifting](def-verifier-lift-context.md)
- [Knowledge-Soundness-Preserving Extractor Lens](def-context-lens-is-knowledge-sound.md)

## Lean

Stated as [`Verifier.liftContext_rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.liftContext_rbrKnowledgeSoundness), [`Verifier.liftContext_rbrKnowledgeSoundnessWith`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.liftContext_rbrKnowledgeSoundnessWith); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 448](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L448)
