---
declaration: definition
origin: cited
lean: Reduction.append
statement: formalized
---

# Reduction Append

Sequential composition of reductions combines the corresponding provers and verifiers:

$$
R_1.\mathsf{append}\ R_2 : \mathsf{Reduction}\ (\mathsf{pSpec}_1 \mathrel{++_\mathsf{p}} \mathsf{pSpec}_2)\ \mathsf{oSpec}\ \mathsf{StmtIn}_1\ \mathsf{WitIn}_1\ \mathsf{StmtOut}_2\ \mathsf{WitOut}_2
$$

## Depends on

- [Interactive Reduction](../../definitions/part-01/def-reduction.md)
- [Prover Append](def-prover-append.md)
- [Verifier Append](def-verifier-append.md)

## Lean

Formalized as [`Reduction.append`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Reduction.append).

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 63](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/composition.tex#L63)
