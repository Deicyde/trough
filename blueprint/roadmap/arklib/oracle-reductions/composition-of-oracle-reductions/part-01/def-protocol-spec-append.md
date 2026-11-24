---
declaration: definition
origin: cited
lean: ProtocolSpec.append
statement: formalized
---

# Protocol Specification Append

Given two protocol specifications $\mathsf{pSpec}_1 : \mathsf{ProtocolSpec}\ m$ and $\mathsf{pSpec}_2 : \mathsf{ProtocolSpec}\ n$, their sequential composition is:

$$
\mathsf{pSpec}_1 \mathrel{++_\mathsf{p}} \mathsf{pSpec}_2 : \mathsf{ProtocolSpec}\ (m + n)
$$

## Depends on

- [Protocol Specification](../../definitions/part-01/def-protocol-spec.md)

## Lean

Formalized as [`ProtocolSpec.append`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.append).

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 14](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/composition.tex#L14)
