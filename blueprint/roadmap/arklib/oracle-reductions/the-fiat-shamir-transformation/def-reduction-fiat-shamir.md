---
declaration: definition
origin: cited
lean: Reduction.fiatShamir
statement: formalized
---

# Fiat-Shamir Reduction Transformation

Given an interactive reduction $R$ for $\mathsf{pSpec}$, its transform

$$
R.\mathsf{fiatShamir} : \mathsf{NonInteractiveReduction}\ (\forall i, \mathsf{pSpec}.\mathsf{Message}\ i)\ (\mathsf{oSpec} \mathrel{+} \mathsf{srChallengeOracle}\ \mathsf{StmtIn}\ \mathsf{pSpec})\ \mathsf{StmtIn}\ \mathsf{WitIn}\ \mathsf{StmtOut}\ \mathsf{WitOut}
$$

applies the transformation to the prover and to the verifier of $R$.

## Depends on

- [Fiat-Shamir Prover Transformation](def-prover-fiat-shamir.md)
- [Fiat-Shamir Verifier Transformation](def-verifier-fiat-shamir.md)

## Lean

Formalized as [`Reduction.fiatShamir`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Reduction.fiatShamir).

## Sources

- [ArkLib blueprint: oracle_reductions/fiat_shamir.tex, line 124](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/fiat_shamir.tex#L124)
