---
declaration: definition
origin: cited
lean: OracleVerifier, OracleOutputEmbedding, OracleOutputSimulation
statement: formalized
---

# Type Signature of an Oracle Verifier

An oracle verifier $\mathcal{V}$ consists of the following components:

- **Verification Logic**: A function

    $$
    \mathsf{verify} : \mathsf{StmtIn} \to \mathsf{pSpec}.\mathsf{Challenges} \to \mathsf{OptionT}(\mathsf{OracleComp}(\mathsf{oSpec} \mathrel{++_\mathsf{o}} ([\mathsf{OStmtIn}]_\mathsf{o} \mathrel{++_\mathsf{o}} [\mathsf{pSpec}.\mathsf{Message}]_\mathsf{o})), \mathsf{StmtOut})
    $$

    that takes the input statement and verifier challenges, and performs oracle queries to the shared oracle, input oracle statements, and prover messages to produce an output statement or reject. As for a verifier, rejection is the $\mathsf{none}$ result of the $\mathsf{OptionT}$ layer.

- **Output Oracle Representation**: one of the following two forms.

    - *Embedding.* An injective function

        $$
        \mathsf{embed} : \iota_{\mathsf{so}} \hookrightarrow \iota_{\mathsf{si}} \oplus \mathsf{pSpec}.\mathsf{MessageIdx}
        $$

        that selects, for each output oracle statement, an input oracle statement or a prover message, together with a proof

        $$
        \mathsf{hEq} : \forall i : \iota_{\mathsf{so}}, \mathsf{OStmtOut}(i) = \begin{cases}
        \mathsf{OStmtIn}(j) & \text{if } \mathsf{embed}(i) = \mathsf{inl}(j) \\
        \mathsf{pSpec}.\mathsf{Message}(k) & \text{if } \mathsf{embed}(i) = \mathsf{inr}(k)
        \end{cases}
        $$

        that the types match, and a proof that the oracle interfaces match.

    - *Virtual simulation.* A map $\mathsf{materializeOutput}$ from the challenges, the input oracle data and the messages to the output oracle data; a query implementation $\mathsf{simulateOutputQuery}$ answering each output-oracle query by queries to the input oracle statements and prover messages; and a proof that, on actual data, the simulated answer equals the answer computed from the materialized output.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`OracleVerifier`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleVerifier), [`OracleOutputEmbedding`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleOutputEmbedding), [`OracleOutputSimulation`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleOutputSimulation).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 232](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L232)
