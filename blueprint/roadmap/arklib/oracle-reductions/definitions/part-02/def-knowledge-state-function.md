---
declaration: definition
origin: cited
lean: Verifier.KnowledgeStateFunction
statement: formalized
---

# Knowledge State Function

A **knowledge state function** for a verifier, with respect to input relation $R_{\text{in}}$, output relation $R_{\text{out}}$, and intermediate witness types, extends the basic state function to track witness validity throughout the protocol execution. This is used to define round-by-round knowledge soundness.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Verifier.KnowledgeStateFunction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.KnowledgeStateFunction).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 656](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/defs.tex#L656)
