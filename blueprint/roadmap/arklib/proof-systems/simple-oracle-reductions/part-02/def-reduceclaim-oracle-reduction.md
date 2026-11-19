---
declaration: definition
origin: cited
lean: ReduceClaim.oracleReduction
statement: formalized
---

# ReduceClaim Oracle Reduction

The oracle version additionally handles oracle statements through an embedding:

- **Oracle statement mapping**: Embedding $\mathsf{embedIdx} : \iota_{\mathsf{out}} \hookrightarrow \iota_{\mathsf{in}}$
- **Type compatibility**: $\mathsf{OStmtIn}(\mathsf{embedIdx}(i)) = \mathsf{OStmtOut}(i)$ for all $i$
- **Oracle embedding**: Maps output oracle indices to corresponding input oracle indices

## Depends on

- [Interactive Oracle Reduction](../../../oracle-reductions/definitions/part-01/def-oracle-reduction.md)
- [ReduceClaim Reduction](def-reduceclaim-reduction.md)

## Lean

Formalized as [`ReduceClaim.oracleReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ReduceClaim.oracleReduction).

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 339](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L339)
