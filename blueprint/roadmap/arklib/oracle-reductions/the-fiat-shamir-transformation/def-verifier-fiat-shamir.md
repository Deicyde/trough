---
declaration: definition
origin: cited
lean: Verifier.fiatShamir
statement: formalized
---

# Fiat-Shamir Verifier Transformation

Given an interactive verifier $V$ for $\mathsf{pSpec}$, the transformation produces a non-interactive verifier

$$
V.\mathsf{fiatShamir} : \mathsf{NonInteractiveVerifier}\ (\forall i, \mathsf{pSpec}.\mathsf{Message}\ i)\ (\mathsf{oSpec} \mathrel{+} \mathsf{srChallengeOracle}\ \mathsf{StmtIn}\ \mathsf{pSpec})\ \mathsf{StmtIn}\ \mathsf{StmtOut} .
$$

On a statement and a proof consisting of all prover messages, it derives the full transcript with $\mathsf{deriveTranscriptFS}$ and runs $V$'s verification on it.

## Depends on

- [Fiat-Shamir Transcript Derivation](def-derive-transcript-fs.md)

## Lean

Formalized as [`Verifier.fiatShamir`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.fiatShamir).

## Sources

- [ArkLib blueprint: oracle_reductions/fiat_shamir.tex, line 110](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/fiat_shamir.tex#L110)
