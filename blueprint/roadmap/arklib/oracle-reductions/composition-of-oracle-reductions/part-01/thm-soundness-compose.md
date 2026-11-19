---
declaration: theorem
origin: cited
lean: Verifier.seqCompose_soundness
statement: formalized
---

# General Soundness Preservation

Let $V_0, \ldots, V_{k-1}$ be guarded verifiers, each sound with error $\epsilon_i$ from every deterministic shared state. Then their sequential composition is sound from any initial distribution with error $\sum_{i=0}^{k-1} \epsilon_i$.

## Depends on

- [Guarded Verifier](../../definitions/part-02/def-guarded-verifier.md)
- [Soundness](../../definitions/part-02/def-soundness.md)
- [General Verifier Composition](def-verifier-compose.md)

## Lean

Stated as [`Verifier.seqCompose_soundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.seqCompose_soundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 220](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L220)
