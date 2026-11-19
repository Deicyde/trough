---
declaration: definition
origin: cited
lean: SendSingleWitness.Adapter, SendSingleWitness.Adapter.oracleReduction
statement: formalized
---

# Single-message adapter

An adapter for a one-message oracle reduction with message type $W$ consists of

- a statement map $\mathsf{stmtOut} : \mathsf{StmtIn} \to \mathsf{StmtOut}$, which does not inspect the message;
- an encoding $\mathsf{encode} : \mathsf{WitIn} \to W$, the message sent by the honest prover;
- a decoding $\mathsf{decode} : W \to \mathsf{WitIn}$, which recovers an input witness;
- an output-oracle representation, either an embedding of the input and message oracles or a query simulation over them.

The induced verifier never rejects: it outputs $\mathsf{stmtOut}$ of the input statement together with the output oracles determined by the message.

## Depends on

- [Interactive Oracle Reduction](../../../oracle-reductions/definitions/part-01/def-oracle-reduction.md)

## Lean

Formalized as [`SendSingleWitness.Adapter`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/SendSingleWitness.Adapter), [`SendSingleWitness.Adapter.oracleReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/SendSingleWitness.Adapter.oracleReduction).

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 103](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L103)
