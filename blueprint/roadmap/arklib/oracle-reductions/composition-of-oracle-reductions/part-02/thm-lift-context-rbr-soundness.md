---
declaration: theorem
origin: cited
lean: Verifier.liftContext_rbrSoundness
statement: formalized
---

# RBR Soundness Preservation under Context Lifting

If a verifier is round-by-round sound with error $\epsilon$ and the statement lens is soundness-preserving, then the lifted verifier is round-by-round sound with the same error at every challenge.

## Depends on

- [Round-by-Round Soundness](../../definitions/part-02/def-round-by-round-soundness.md)
- [Verifier Context Lifting](def-verifier-lift-context.md)
- [Soundness-Preserving Statement Lens](def-statement-lens-is-sound.md)

## Lean

Stated as [`Verifier.liftContext_rbrSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.liftContext_rbrSoundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 438](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L438)
