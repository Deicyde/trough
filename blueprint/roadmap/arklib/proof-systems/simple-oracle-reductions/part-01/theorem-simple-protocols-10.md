---
declaration: theorem
origin: cited
lean: QuotientZeroTest.oracleReduction_perfectCompleteness, QuotientZeroTest.oracleVerifier_rbrKnowledgeSoundness, QuotientZeroTest.oracleVerifier_knowledgeSoundnessWith
statement: formalized
---

# Quotient Zero Test Security

The quotient zero test is perfectly complete. If $|H| \leq d$, its verifier is fixed-prefix round-by-round knowledge sound with error $\frac{d}{|\mathbb{F}|}$ at its single challenge, and knowledge sound with the same total error.

## Depends on

- [Quotient Zero Test](def-quotient-zero-test.md)

## Lean

Stated as [`QuotientZeroTest.oracleReduction_perfectCompleteness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/QuotientZeroTest.oracleReduction_perfectCompleteness), [`QuotientZeroTest.oracleVerifier_rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/QuotientZeroTest.oracleVerifier_rbrKnowledgeSoundness), [`QuotientZeroTest.oracleVerifier_knowledgeSoundnessWith`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/QuotientZeroTest.oracleVerifier_knowledgeSoundnessWith); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 221](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L221)
