---
declaration: theorem
origin: cited
lean: Verifier.append_knowledgeSoundness
statement: formalized
---

# Knowledge Soundness Preservation under Append

Suppose $V_1$ is guarded. Suppose there are fixed pure extractors $e_1$ and $e_2$, each a function of the input statement, the transcript and the output witness, such that $e_1$ satisfies the knowledge game of $V_1$ with error $\epsilon_1$ from $\mu$, and this same $e_2$ satisfies the knowledge game of $V_2$ with error $\epsilon_2$ from every deterministic shared state. Then $V_1.\mathsf{append}\ V_2$ is knowledge sound from $\mu$ with error $\epsilon_1 + \epsilon_2$, with the extractor that runs the second extractor and then the first.

## Depends on

- [Guarded Verifier](../../definitions/part-02/def-guarded-verifier.md)
- [Knowledge Soundness](../../definitions/part-02/def-knowledge-soundness.md)
- [Verifier Append](def-verifier-append.md)

## Lean

Stated as [`Verifier.append_knowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.append_knowledgeSoundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 171](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L171)
