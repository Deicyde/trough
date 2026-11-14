---
declaration: theorem
origin: cited
lean: Verifier.liftContext_soundness
statement: formalized
---

# Soundness Preservation under Context Lifting

If a verifier is sound with error $\epsilon$ and the statement lens is soundness-preserving, then the lifted verifier is sound with error $\epsilon$. The inner output statement type must be inhabited.

## Depends on

- [Soundness](../../definitions/part-02/def-soundness.md)
- [Verifier Context Lifting](def-verifier-lift-context.md)
- [Soundness-Preserving Statement Lens](def-statement-lens-is-sound.md)

## Lean

Stated as [`Verifier.liftContext_soundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.liftContext_soundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 415](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L415)
