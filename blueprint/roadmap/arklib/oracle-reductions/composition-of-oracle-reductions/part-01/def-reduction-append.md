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

- [ArkLib blueprint: oracle_reductions/composition.tex, line 63](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L63)
