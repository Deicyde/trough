---
declaration: definition
origin: cited
lean: SendWitness.reduction
statement: formalized
---

# SendWitness Reduction

The SendWitness reduction is a one-round protocol where the prover sends the complete witness to the verifier:

- **Protocol specification**: $\mathsf{pSpec} := [(\mathsf{P \!\!\rightarrow\!\! V}, \mathsf{WitIn})]$ (single message from prover to verifier)
- **Prover**: Sends the witness $\mathbb{w}$ as its single message
- **Verifier**: Receives the witness and combines it with the input statement to form the output
- **Input relation**: $R_{\mathsf{in}} : \mathsf{StmtIn} \to \mathsf{WitIn} \to \mathsf{Prop}$
- **Output relation**: $R_{\mathsf{out}} : (\mathsf{StmtIn} \times \mathsf{WitIn}) \to \mathsf{Unit} \to \mathsf{Prop}$ defined by $((\mathsf{stmt}, \mathsf{wit}), ()) \mapsto R_{\mathsf{in}}(\mathsf{stmt}, \mathsf{wit})$

## Depends on

- [Interactive Reduction](../../../oracle-reductions/definitions/part-01/def-reduction.md)

## Lean

Formalized as [`SendWitness.reduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/SendWitness.reduction).

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 43](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L43)
