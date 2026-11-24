---
declaration: definition
origin: cited
lean: ProtocolSpec.seqCompose
statement: formalized
---

# General Protocol Specification Composition

Given a family of protocol specifications $\mathsf{pSpec} : \forall i : \mathsf{Fin}(m+1), \mathsf{ProtocolSpec}\ (n\ i)$, their composition is:

$$
\mathsf{compose}\ m\ n\ \mathsf{pSpec} : \mathsf{ProtocolSpec}\ (\sum_{i} n\ i)
$$

## Depends on

- [Protocol Specification](../../definitions/part-01/def-protocol-spec.md)

## Lean

Formalized as [`ProtocolSpec.seqCompose`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.seqCompose).

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 84](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/composition.tex#L84)
