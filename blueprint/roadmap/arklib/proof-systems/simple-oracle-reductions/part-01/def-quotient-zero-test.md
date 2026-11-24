---
declaration: definition
origin: cited
lean: QuotientZeroTest.oracleReduction
statement: formalized
---

# Quotient Zero Test

The input is one polynomial oracle $f$ of degree at most $d$, with no witness.

- **Input relation**: $f(h) = 0$ for every $h \in H$
- **Protocol specification**: The prover sends a polynomial oracle $q$ of degree at most $d - |H|$; then the verifier sends a uniformly random $z \in \mathbb{F}$
- **Honest prover**: Sends the quotient $q = f / Z_H$
- **Verifier**: Queries $f(z)$ and $q(z)$ and rejects unless $f(z) = q(z) \cdot Z_H(z)$
- **Output relation**: Every output is accepted; no oracle statements remain

## Depends on

- [Interactive Oracle Reduction](../../../oracle-reductions/definitions/part-01/def-oracle-reduction.md)

## Lean

Formalized as [`QuotientZeroTest.oracleReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/QuotientZeroTest.oracleReduction).

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 206](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/proof_systems/simple_protocols.tex#L206)
