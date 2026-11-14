---
declaration: theorem
origin: cited
lean: Verifier.seqCompose_rbrKnowledgeSoundness_of_guarded
statement: formalized
---

# Round-by-Round Knowledge Soundness of a Guarded Chain

If every verifier of a finite chain is guarded and round-by-round knowledge sound for every fixed transcript prefix between consecutive relations, so is the chain. Each combined challenge keeps the error of the component challenge it corresponds to. The proof iterates Theorem [Round-by-Round Knowledge Soundness under a Guarded First Verifier](thm-rbr-knowledge-soundness-append-guarded.md).

## Depends on

- [Guarded Verifier](../../definitions/part-02/def-guarded-verifier.md)
- [Round-by-Round Knowledge Soundness](../../definitions/part-02/def-round-by-round-knowledge-soundness.md)
- [General Verifier Composition](def-verifier-compose.md)
- [Round-by-Round Knowledge Soundness under a Guarded First Verifier](thm-rbr-knowledge-soundness-append-guarded.md)

## Lean

Stated as [`Verifier.seqCompose_rbrKnowledgeSoundness_of_guarded`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.seqCompose_rbrKnowledgeSoundness_of_guarded); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 243](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L243)
