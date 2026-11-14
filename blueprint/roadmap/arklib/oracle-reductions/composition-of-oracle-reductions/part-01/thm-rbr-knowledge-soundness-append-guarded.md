---
declaration: theorem
origin: cited
lean: Verifier.append_rbrKnowledgeSoundnessWith_of_guarded_first, Verifier.append_rbrKnowledgeSoundness_of_guarded_first
statement: formalized
---

# Round-by-Round Knowledge Soundness under a Guarded First Verifier

Suppose $V_1$ is guarded: it returns a deterministic verdict when its check passes and aborts otherwise. Suppose $V_1$ and $V_2$ are round-by-round knowledge sound for every fixed transcript prefix, with intermediate relation $R_2$ shared between them. Then $V_1.\mathsf{append}\ V_2$ is round-by-round knowledge sound for every fixed transcript prefix, and each challenge keeps its component's error. The composed extractor runs the second extractor from the first verdict and then the first extractor. The composed knowledge state is the first one up to the seam, and after it is the first check together with the second knowledge state at the first verdict. At the seam, the second knowledge state at round $0$ places the verdict in $R_2$, and a passing check makes that verdict a positive-probability output of $V_1$.

## Depends on

- [Guarded Verifier](../../definitions/part-02/def-guarded-verifier.md)
- [Round-by-Round Knowledge Soundness](../../definitions/part-02/def-round-by-round-knowledge-soundness.md)
- [Verifier Append](def-verifier-append.md)

## Lean

Stated as [`Verifier.append_rbrKnowledgeSoundnessWith_of_guarded_first`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.append_rbrKnowledgeSoundnessWith_of_guarded_first), [`Verifier.append_rbrKnowledgeSoundness_of_guarded_first`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.append_rbrKnowledgeSoundness_of_guarded_first); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 187](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L187)
