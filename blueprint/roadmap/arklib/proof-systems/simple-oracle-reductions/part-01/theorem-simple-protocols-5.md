---
declaration: theorem
origin: cited
lean: SendSingleWitness.Adapter.perfectCompleteness, SendSingleWitness.Adapter.rbrKnowledgeSoundnessWith
statement: formalized
---

# Single-message adapter security

If every honest input $(s, w) \in R_{\mathsf{in}}$ has its output for the message $\mathsf{encode}(w)$ in $R_{\mathsf{out}}$, the reduction is perfectly complete. If every message $w$ whose output lies in $R_{\mathsf{out}}$ satisfies $(s, \mathsf{decode}(w)) \in R_{\mathsf{in}}$, the verifier is fixed-prefix round-by-round knowledge sound with error $0$, with the extractor that decodes the transcript message.

## Depends on

- [Single-message adapter](def-sendsinglewitness-adapter.md)

## Lean

Stated as [`SendSingleWitness.Adapter.perfectCompleteness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/SendSingleWitness.Adapter.perfectCompleteness), [`SendSingleWitness.Adapter.rbrKnowledgeSoundnessWith`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/SendSingleWitness.Adapter.rbrKnowledgeSoundnessWith); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 118](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/proof_systems/simple_protocols.tex#L118)
