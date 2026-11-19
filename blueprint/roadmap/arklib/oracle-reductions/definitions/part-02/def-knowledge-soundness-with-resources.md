---
declaration: definition
origin: cited
lean: Verifier.knowledgeSoundnessWithResources
statement: formalized
---

# Knowledge Soundness with Measured Extraction

For a named straightline extractor $E$, a measured program $M$ and a budget $B$, $\mathsf{knowledgeSoundnessWithResources}$ holds when $E$ satisfies the knowledge game of [Knowledge Soundness](def-knowledge-soundness.md) with error $\epsilon$, the run of $E$ is the execution of $M$ on its view without querying the shared oracle, and every execution path of $M$ costs at most $B$. The budget counts only the instructions that $M$ declares.

## Depends on

- [Knowledge Soundness](def-knowledge-soundness.md)

## Lean

Formalized as [`Verifier.knowledgeSoundnessWithResources`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.knowledgeSoundnessWithResources).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 624](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L624)
