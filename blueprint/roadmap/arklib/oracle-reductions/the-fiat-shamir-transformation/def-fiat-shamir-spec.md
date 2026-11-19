---
declaration: definition
origin: cited
lean: ProtocolSpec.srChallengeOracle, ProtocolSpec.fsChallengeOracle
statement: formalized
---

# Challenge Oracle Specification

The challenge oracle specification is

$$
\mathsf{srChallengeOracle}\ \mathsf{StmtIn}\ \mathsf{pSpec} : \mathsf{OracleSpec}\ \big((i : \mathsf{pSpec}.\mathsf{ChallengeIdx}) \times (\mathsf{StmtIn} \times \mathsf{pSpec}.\mathsf{MessagesUpTo}\ i.\mathsf{val}.\mathsf{castSucc})\big),
$$

which answers the query $\langle i, (x, m) \rangle$ with a value of type $\mathsf{pSpec}.\mathsf{Challenge}\ i$. The index type pairs a challenge round with a query of the interface of [Challenge Oracle Interface](def-fiat-shamir-challenge-oracle-interface.md). The name $\mathsf{fsChallengeOracle}$ is an alias.

## Depends on

- [Challenge Oracle Interface](def-fiat-shamir-challenge-oracle-interface.md)

## Lean

Formalized as [`ProtocolSpec.srChallengeOracle`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.srChallengeOracle), [`ProtocolSpec.fsChallengeOracle`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.fsChallengeOracle).

## Sources

- [ArkLib blueprint: oracle_reductions/fiat_shamir.tex, line 34](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/fiat_shamir.tex#L34)
