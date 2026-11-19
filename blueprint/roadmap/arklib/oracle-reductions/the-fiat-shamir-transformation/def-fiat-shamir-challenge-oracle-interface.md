---
declaration: definition
origin: cited
lean: ProtocolSpec.challengeOracleInterfaceSR, ProtocolSpec.challengeOracleInterfaceFS
statement: formalized
---

# Challenge Oracle Interface

For each challenge index $i : \mathsf{pSpec}.\mathsf{ChallengeIdx}$, the state-restoration (and Fiat–Shamir) oracle interface on $\mathsf{pSpec}.\mathsf{Challenge}\ i$ has:

- **Query type**: $\mathsf{StmtIn} \times \mathsf{pSpec}.\mathsf{MessagesUpTo}\ i.\mathsf{val}.\mathsf{castSucc}$, the input statement together with the prover messages sent before round $i$;
- **Response type**: $\mathsf{pSpec}.\mathsf{Challenge}\ i$;
- **Oracle behavior**: return the challenge itself.

The Lean name is $\mathsf{challengeOracleInterfaceSR}$, with alias $\mathsf{challengeOracleInterfaceFS}$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`ProtocolSpec.challengeOracleInterfaceSR`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.challengeOracleInterfaceSR), [`ProtocolSpec.challengeOracleInterfaceFS`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.challengeOracleInterfaceFS).

## Sources

- [ArkLib blueprint: oracle_reductions/fiat_shamir.tex, line 18](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/fiat_shamir.tex#L18)
