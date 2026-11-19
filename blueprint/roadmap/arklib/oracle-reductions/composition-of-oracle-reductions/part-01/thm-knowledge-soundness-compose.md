---
declaration: theorem
origin: cited
lean: Verifier.seqCompose_knowledgeSoundness
statement: formalized
---

# General Knowledge Soundness Preservation

Let $V_0, \ldots, V_{k-1}$ be guarded verifiers. For each component $i$, choose one pure extractor $e_i$, a function of the input statement, the transcript and the output witness, that satisfies the knowledge game of $V_i$ with error $\epsilon_i$ from every deterministic initial shared state. Then their sequential composition is knowledge sound from any initial distribution with error $\sum_{i=0}^{k-1} \epsilon_i$, with the extractors folded backwards over the chain.

## Depends on

- [Guarded Verifier](../../definitions/part-02/def-guarded-verifier.md)
- [Knowledge Soundness](../../definitions/part-02/def-knowledge-soundness.md)
- [General Verifier Composition](def-verifier-compose.md)

## Lean

Stated as [`Verifier.seqCompose_knowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.seqCompose_knowledgeSoundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 230](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L230)
