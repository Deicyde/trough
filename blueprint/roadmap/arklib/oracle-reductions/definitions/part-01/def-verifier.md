---
declaration: definition
origin: cited
lean: Verifier
statement: formalized
---

# Type Signature of a Verifier

A verifier $\mathcal{V}$ in a reduction is specified by a single function:

$$
\mathsf{verify} : \mathsf{StmtIn} \to \mathsf{FullTranscript}(\mathsf{pSpec}) \to \mathsf{OptionT}(\mathsf{OracleComp}(\mathsf{oSpec}), \mathsf{StmtOut})
$$

This function takes the input statement and the complete transcript of the protocol interaction, and performs an oracle computation (potentially querying the shared oracle $\mathsf{oSpec}$) that either produces an output statement or fails. Failure, the $\mathsf{none}$ result of the $\mathsf{OptionT}$ layer, is how the verifier rejects.

The verifier is assumed to be *public-coin*, meaning it only sends uniformly random challenges and uses no other randomness beyond what is provided by the shared oracle.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Verifier`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 220](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L220)
