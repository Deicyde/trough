---
declaration: theorem
origin: cited
lean: Verifier.liftContext_knowledgeSoundness
statement: formalized
---

# Knowledge Soundness Preservation under Context Lifting

If a verifier is knowledge sound with error $\epsilon$ and the extractor lens is knowledge-soundness-preserving, then the verifier lifted along its statement lens is knowledge sound with error $\epsilon$. The inner output statement and inner input witness types must be inhabited: when the inner extractor fails, the lifted extractor lifts a default inner witness. That default is a valid outer input witness when the shortcut disjunct of the lens condition holds; failure in the other branch is charged to the inner knowledge error.

## Depends on

- [Knowledge Soundness](../../definitions/part-02/def-knowledge-soundness.md)
- [Verifier Context Lifting](def-verifier-lift-context.md)
- [Knowledge-Soundness-Preserving Extractor Lens](def-context-lens-is-knowledge-sound.md)

## Lean

Stated as [`Verifier.liftContext_knowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.liftContext_knowledgeSoundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 425](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/composition.tex#L425)
