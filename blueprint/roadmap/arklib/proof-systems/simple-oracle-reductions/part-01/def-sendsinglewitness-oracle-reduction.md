---
declaration: definition
origin: cited
lean: SendSingleWitness.oracleReduction
statement: formalized
---

# SendSingleWitness Oracle Reduction

A specialized variant for a single witness with oracle interface:

- **Witness type**: $\mathsf{WitIn} : \mathsf{Type}$ with oracle interface
- **Protocol specification**: $\mathsf{pSpec} := [(\mathsf{P \!\!\rightarrow\!\! V}, \mathsf{WitIn})]$
- **Output oracle statements**: The input oracle statements together with the sent witness, indexed by $\iota_{\mathsf{in}} \oplus \mathsf{Fin}(1)$
- **Output relation**: $R_{\mathsf{in}}$ read off the output oracles, with the witness at index $\mathsf{inr}(0)$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`SendSingleWitness.oracleReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/SendSingleWitness.oracleReduction).

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 80](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L80)
