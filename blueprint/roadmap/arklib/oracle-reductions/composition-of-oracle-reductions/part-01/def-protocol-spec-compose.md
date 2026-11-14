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

- [ArkLib blueprint: oracle_reductions/composition.tex, line 84](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L84)
