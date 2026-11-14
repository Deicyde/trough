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

- [ArkLib blueprint: oracle_reductions/composition.tex, line 14](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L14)
