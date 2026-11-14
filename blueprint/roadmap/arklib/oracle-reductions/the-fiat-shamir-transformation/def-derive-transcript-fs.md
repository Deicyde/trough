---
declaration: definition
origin: cited
lean: ProtocolSpec.Messages.deriveTranscriptFS
statement: formalized
---

# Fiat-Shamir Transcript Derivation

Given an input statement $x$ and all prover messages, $\mathsf{deriveTranscriptFS}$ reconstructs the full transcript

$$
\mathsf{messages}.\mathsf{deriveTranscriptFS}\ x : \mathsf{OracleComp}\ (\mathsf{oSpec} \mathrel{+} \mathsf{srChallengeOracle}\ \mathsf{StmtIn}\ \mathsf{pSpec})\ (\mathsf{pSpec}.\mathsf{FullTranscript}) .
$$

Round by round, it copies each prover message and obtains each challenge by querying the challenge oracle at the statement and the messages before that round. The name is an alias of $\mathsf{deriveTranscriptSR}$.

## Depends on

- [Challenge Oracle Specification](def-fiat-shamir-spec.md)

## Lean

Formalized as [`ProtocolSpec.Messages.deriveTranscriptFS`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.Messages.deriveTranscriptFS).

## Sources

- [ArkLib blueprint: oracle_reductions/fiat_shamir.tex, line 97](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/fiat_shamir.tex#L97)
