---
declaration: definition
origin: cited
lean: Verifier.rbrKnowledgeSoundnessWith
statement: formalized
---

# Round-by-Round Knowledge Soundness with a Named Extractor

$\mathsf{rbrKnowledgeSoundnessWith}$ is the condition of [Round-by-Round Knowledge Soundness](def-round-by-round-knowledge-soundness.md) for one given family of intermediate witness types, round-by-round extractor and knowledge state function. These objects stay visible in the statement, so downstream composition and extraction theorems can name them. Round-by-round knowledge soundness is its existential closure.

## Depends on

- [Round-by-Round Knowledge Soundness](def-round-by-round-knowledge-soundness.md)

## Lean

Formalized as [`Verifier.rbrKnowledgeSoundnessWith`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.rbrKnowledgeSoundnessWith).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 716](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L716)
