---
declaration: definition
origin: cited
lean: Verifier.soundness
statement: formalized
---

# Soundness

A reduction satisfies **soundness** with error $\epsilon \geq 0$ and with respect to input language $L_{\text{in}} \subseteq \text{Statement}_{\text{in}}$ and output language $L_{\text{out}} \subseteq \text{Statement}_{\text{out}}$ if:

- for all (malicious) provers with arbitrary types for witness types,
- for all arbitrary input witness,
- for all input statement $x_{\text{in}} \notin L_{\text{in}}$,

the execution between the prover and the honest verifier will result in an output statement $x_{\text{out}} \in L_{\text{out}}$ with probability at most $\epsilon$.

## Depends on

- [Type Signature of a Verifier](../part-01/def-verifier.md)
- [Complete Prover Execution](../part-01/def-prover-run.md)

## Lean

Formalized as [`Verifier.soundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.soundness).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 564](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L564)
